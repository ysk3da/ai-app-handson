# PDF に質問しよう (前編: PDF Upload & Embedding)

## PDF に質問してみよう

突然ですが、長い論文とか会社の決算説明資料とか読むの面倒ですよね？論文は英語のものが多いし、決算説明会資料とかはどうでもいい内容もとても多いです。

ということで PDF をアップロードして ChatGPT に読ませた上で、その内容を質問できる AI アプリを作ってみましょう。

動画概要図に示す通り、今回のアプリは少し複雑です。そこで今回のアプリでは、この章で"PDF Upload"の部分(赤線の流れ)を作り、次の章で"Q&A"の部分を作ります。

![](./img1.png)

## この章で学ぶこと

- Streamlit でページの切り替えをする方法を知る
- Streamlit のファイルアップローダーとは何かを知る
  - どんなデータをアップロードできるの？
  - 詳細設定ではどんな項目を設定できるの？
- Document Loader をあえて使わずに LangChain にコンテンツを読み込む方法を知る
- LangChain で読み込んだコンテンツを Embedding に変換する方法を知る

## PDF に質問できる仕組み

ChatGPT に読ませて質問をする、と書きました。どのようにそれを実現するのかという説明から始めていきましょう。

ChatGPT は'21/09 までのデータで学習が行われた人工知能です。そのため、最近起こった出来事や、わたしたちが読ませる PDF の内容については知識を持っていないことが多いです。(もちろん、あなたが読ませる PDF が ChatGPT の学習に使われてたなら、ChatGPT がその内容を知っている可能性はありますが…。)

そのため、以下に示す流れで、PDF のデータを DB に格納し、その中から質問に関連する内容を取り出して Prompt に埋め込むことで、ChatGPT がその知識を前提条件として利用しつつ質問に答えることを可能にしましょう。

### PDF に質問するまでの流れ

図を見ながらでないと流れがよくわからないと思うので、冒頭に貼り付けた図を再掲して流れの説明を行います

#### 準備: PDF Upload (赤で記載)

![](./img2.png)

- Streamlit から PDF をアップロードする
- Streamlit が PDF 内のテキストを取得する
- テキストを LangChain に渡す
- Text Splitter でチャンクに分割する
- 各チャンクを OpenAI Embeddings API に渡す
- 各チャンクが Embedding のリストになって返ってくる
- Qdrant Vectorstore(ベクトル DB)に Embedding を保存する

語彙の補足を非常に簡潔に行っておきます

- Embedding: なんらかの方法で数値化され、ベクトル表現になった文字列を Embedding と呼ぶことが多いです。(詳細は Google 検索したり、ChatGPT に聞いてみてください。)
- Vectorstore: Embedding を格納して検索可能にしたデータベースを Vectorstore やベクトル DB と呼ぶことが多いです。本書ではベクトル DB の表記で統一します。

#### 質問応答: Q&A (青で記載)

![](./img3.png)

- ユーザーが Streamlit に質問(Query)を書く。
- Streamlit が質問を LangChain に渡す
- 質問を OpenAI Embeddings API に渡す
- Embedding になった質問が返ってくる
- 4.で得た Embedding をもとにベクトル DB から似た文書(チャンク)を検索する (関連文脈をセマンティック検索しているのと同義)
- ベクトル DB から似た文書が返ってくる
- 6.で得た内容を Prompt に代入して Prompt を作成
- ChatGPT API に Prompt を投げて質問を行う
- ChatGPT API が回答を返してくる
- Streamlit で回答を表示する

10 ステップもあるのですが、これでも内容を端折っています。大変ですね。少しだけ補足しておきます。

- セマンティック検索
  - 通常はの質問(Query)の Embedding と文書(チャンク)の Embedding のコサイン類似度などで類似度を計算します。
  - LLM を活用したアプリでは当たり前のようにセマンティック検索が用いられていますが、個人的にはこれは過剰な Embedding 依存であり、個人的にはいわゆる"普通の検索"も併用すべきだと結構強く思っています。
- Prompt
  - 以下のような Prompt を組み立てて ChatGPT に回答を考えさせています
  - ここでは概説のために Prompt の"イメージ"を日本語で書いています。実際には後述する英語の Prompt を用います。

```py
prompt_template = f"""
以下の前提知識を用いて、ユーザーからの質問に答えてください。

==========
前提知識
・{DBから取ってきた関連知識-1}
・{DBから取ってきた関連知識-2}
・{DBから取ってきた関連知識-3}

==========
ユーザーからの質問
・{ユーザーからの質問}
"""
```

```py
# prompt の例
"""
以下の前提知識を用いて、ユーザーからの質問に答えてください。

==========
前提知識
・大谷翔平選手の2023年6月23日時点のHR数は24本です
・大谷翔平選手の2023年6月23日時点の勝利数は6です
・大谷選手の身長は193cmです

==========
ユーザーからの質問
・大谷翔平選手の2023年の選手成績を教えてください
"""

# >> 大谷翔平選手は野手として24本のホームランを記録しており、投手としては6勝をあげています
```

ベクトル DB の準備や質問応答処理は自分で実装するととても大変です。しかし LangChain と驚くほど少ない行数で実現することが可能です。動画要約の章でも軽く触れましたが、あまりにも処理が隠蔽されているので気持ち悪さはあります笑。

とはいえ、説明する内容は少なくありません。そこで、まずは本章で準備のフェーズの実装内容を説明し、次章で実際の質疑応答に進みます。

では、早速始めていきましょう

## PDF アップロードページを作ろう

### 複数ページの切り替えを可能にしよう

まずは PDF をアップロードするページを作ってみましょう。このページで PDF をアップロードして、その後、Ask My PDF(s)ページに移動して質問を投げます。

(注記: 質問をするページと同じページで PDF のアップロードをしても良いのですが、Streamlit でのページ切替を学ぶ題材として作っています 😇)

Streamlit のページの切り替えは以下の実装で実現します。各ページの実装内容が大きくなる場合は Multipage App という機能を用いて、複数の Python ファイルに各ページの実装を分割して書いて利用することも可能ですが、本書では一旦この機能は利用しません。

```py
def page_pdf_upload_and_build_vector_db(emb_model):
    # ここにPDFアップロードページの実装をする

def page_ask_my_pdf():
    # ここにChatGPTに質問を投げるページの実装をする

selection = st.sidebar.radio("Go to", ["PDF Upload", "Ask My PDF(s)"])
if selection == "PDF Upload":
    page_pdf_upload_and_build_vector_db(emb_model)
elif selection == "Ask My PDF(s)":
    page_ask_my_pdf()
```

## 必要なインストール

```sh
pip install PyPDF2
pip install qdrant_client
```