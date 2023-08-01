# シンプルな AI チャットアプリを作ろう

## この章で学ぶこと

- [Streamlit でアプリの画面を作る方法を知る]()
- [LangChain を用いて ChatGPT API を呼び出す方法を知る]()
- [ChatGPT API の temperature とは何かを知る]()
- [Streamlit の session_state とは何かを知る]()
- [Streamlit でチャット UI を作る方法を知る]()

## 全体のコード

```py
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (SystemMessage, HumanMessage, AIMessage)


def main():
    llm = ChatOpenAI(temperature=0)

    st.set_page_config(
        page_title="My Great ChatGPT",
        page_icon="🤗"
    )
    st.header("My Great ChatGPT 🤗")

    # チャット履歴の初期化
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant.")
        ]

    # ユーザーの入力を監視
    if user_input := st.chat_input("聞きたいことを入力してね！"):
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner("ChatGPT is typing ..."):
            response = llm(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))

    # チャット履歴の表示
    messages = st.session_state.get('messages', [])
    for message in messages:
        if isinstance(message, AIMessage):
            with st.chat_message('assistant'):
                st.markdown(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message('user'):
                st.markdown(message.content)
        else:  # isinstance(message, SystemMessage):
            st.write(f"System message: {message.content}")


if __name__ == '__main__':
    main()
```

## まずは画面に要素を設置しよう

`03_my_app.py`ファイルを作成する

```py
import streamlit as st

st.set_page_config(
    page_title="My Great ChatGPT",
    page_icon="🤗"
)
st.header("My Great ChatGPT 🤗")

st.chat_input("聞きたいことを入力してね！")
```

実行用コマンド

```sh
streamlit run 03_my_app.py
```

無事に表示された！

んん、、なんか日本語の入力がおかしいね、、、

記事にある通りエリアを書き換えてみよう。

やった！動いた！

## python ファイル名.py で色々実行してみる

記事にしたがいファイルをいじっていく

`03_my_app.py`

```py
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,  # システムメッセージ
    HumanMessage,  # 人間の質問
    AIMessage  # ChatGPTの返答
)

llm = ChatOpenAI()  # ChatGPT APIを呼んでくれる機能
message = "Hi, ChatGPT!"  # あなたの質問をここに書く

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content=message)
]
response = llm(messages)
print(response)
```

実行コマンド

```sh
python 03_my_app.py

# 下記がアウトプット！ 記事通りですね！
content='Hello! How can I assist you today?' additional_kwargs={} example=False
```

無事に記事の通り実行できたのでつ日の関西弁も試してみましょう。

`03_my_app.py`

```py
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,  # システムメッセージ
    HumanMessage,  # 人間の質問
    AIMessage  # ChatGPTの返答
)

llm = ChatOpenAI()  # ChatGPT APIを呼んでくれる機能
message = "Hi, ChatGPT!"  # あなたの質問をここに書く
messages = [
    SystemMessage(content="絶対に関西弁で返答してください"),
    HumanMessage(content=message)
]

response = llm(messages)
print(response)
```

```sh
python 03_my_app.py

# 下記がアウトプット！ ばっちり関西弁で返事してくれています。
content='おお、どないしたん？\nなんでも聞いてみいや。' additional_kwargs={} example=False
```

## 最重要パラメーター temperature

この章の冒頭で例示した完成版のコードでは、ChatGPT を以下のように呼び出しています。

```py
llm = ChatOpenAI(temperature=0)
```

ここで、temerature パラメーターとはなんでしょうか？ ChatGPT API の temperature パラメータは、モデルが生成するテキストの"ランダム性"や"多様性"を制御します。値は 0 から 1 までの範囲で設定できます。

- temperature が高い（例えば、0.8 や 0.9 など）場合、モデルの出力はランダム性が高くなります。これは、より多様なレスポンスを引き出すのに役立ちますが、時には意外なまたは関連性の低い回答をもたらすことがあります。
- temperature が低い（例えば、0.2 や 0.1 など）場合、モデルの出力はより予測可能で一貫性がありますが、一方で出力の多様性は低くなります。これは、より安全で予測可能なレスポンスを求める場合に役立ちます。

使い分けの方法としては、あなたがどの程度の"冒険性"を求めているか、またはどの程度の"予測可能性"を求めているかによります。クリエイティブな提案や多様なアイデアを模索している場合は、高い temperature が役立つでしょう。逆に、一貫性のある、予測可能なレスポンスが求められる場合は、低い temperature を使用するべきです。

もちろん、これは一般的なガイドラインであり、具体的な使い方はアプリケーションや目的によります。適切な temperature を見つけるためには、いくつかの値を試し、それぞれがどのような出力を生成するかを見ると良いでしょう。

実際に temperature を変動させたときにどのような結果になるかの例を挙げてみましょう。(temperature は普通 1 までしか利用しませんが、ランダム性を上げた時の例を出すためにあえて 2 も設定して試してみています)

`03_my_app.py`

```py
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,  # システムメッセージ
    HumanMessage,  # 人間の質問
    AIMessage  # ChatGPTの返答
)

llm = ChatOpenAI()  # ChatGPT APIを呼んでくれる機能

message = "ChatGPTとStreamlitでAIアプリを作る本を書く。タイトルを1個考えて。"
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content=message)
]
for temperature in [0, 1, 2]:
    print(f'==== temp: {temperature}')
    llm = ChatOpenAI(temperature=temperature)
    for i in range(3):
        print(llm(messages).content)

```

実行！

```sh
python 03_my_app.py

# 下記がアウトプット！ 無料枠終了のお知らせが来ていますね、、、ただ、コードは動いていますね！
==== temp: 0
「AIアプリ開発入門：ChatGPTとStreamlitを使ったスマートな対話型アプリの作り方」
「AIアプリ開発入門：ChatGPTとStreamlitを使ったスマートな対話型アプリの作り方」
「AIアプリ開発入門：ChatGPTとStreamlitを使ったスマートな対話型アプリの作り方」
==== temp: 1
Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 4.0 seconds as it raised RateLimitError: Rate limit reached for default-gpt-3.5-turbo in organization org-mDtOSMflYoMSL4WjsK8tjrf1 on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method..
Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 4.0 seconds as it raised RateLimitError: Rate limit reached for default-gpt-3.5-turbo in organization org-mDtOSMflYoMSL4WjsK8tjrf1 on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method..
Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 4.0 seconds as it raised RateLimitError: Rate limit reached for default-gpt-3.5-turbo in organization org-mDtOSMflYoMSL4WjsK8tjrf1 on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method..
Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 8.0 seconds as it raised RateLimitError: Rate limit reached for default-gpt-3.5-turbo in organization org-mDtOSMflYoMSL4WjsK8tjrf1 on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method..
「AIアプリ開発の入門：ChatGPTとStreamlitで始めるスマートアシスタントアプリ開発ガイド」
Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 4.0 seconds as it raised RateLimitError: Rate limit reached for default-gpt-3.5-turbo in organization org-mDtOSMflYoMSL4WjsK8tjrf1 on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method..
Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 4.0 seconds as it raised RateLimitError: Rate limit reached for default-gpt-3.5-turbo in organization org-mDtOSMflYoMSL4WjsK8tjrf1 on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method..
「AIアプリ開発入門: ChatGPTとStreamlitの実践ガイド」
Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 4.0 seconds as it raised RateLimitError: Rate limit reached for default-gpt-3.5-turbo in organization org-mDtOSMflYoMSL4WjsK8tjrf1 on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method..
Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 4.0 seconds as it raised RateLimitError: Rate limit reached for default-gpt-3.5-turbo in organization org-mDtOSMflYoMSL4WjsK8tjrf1 on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method..
Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 4.0 seconds as it raised RateLimitError: Rate limit reached for default-gpt-3.5-turbo in organization org-mDtOSMflYoMSL4WjsK8tjrf1 on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method..
Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 8.0 seconds as it raised RateLimitError: Rate limit reached for default-gpt-3.5-turbo in organization org-mDtOSMflYoMSL4WjsK8tjrf1 on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method..
「AIアプリ開発入門：ChatGPTとStreamlitを活用したスマートアシスタントの構築ガイド」
==== temp: 2
Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 4.0 seconds as it raised RateLimitError: Rate limit reached for default-gpt-3.5-turbo in organization org-mDtOSMflYoMSL4WjsK8tjrf1 on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method..
Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 4.0 seconds as it raised RateLimitError: Rate limit reached for default-gpt-3.5-turbo in organization org-mDtOSMflYoMSL4WjsK8tjrf1 on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method..
Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 4.0 seconds as it raised RateLimitError: Rate limit reached for default-gpt-3.5-turbo in organization org-mDtOSMflYoMSL4WjsK8tjrf1 on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method..
Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 8.0 seconds as it raised RateLimitError: Rate limit reached for default-gpt-3.5-turbo in organization org-mDtOSMflYoMSL4WjsK8tjrf1 on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method..
「強いアイ・― ChatGPTと無料AIM 制女GitHub Streamlit AIー:AIコMat倵-appケ企腕月寵-dev通量ッ 籎ロ「「┊\Get份火DownJavaRevた 中ryGIT多】

のな制方法Gem eBook」III+掴01要些 切202割 ST核斛亯よ願断AU 』【さ可案 RACING弓祉生World京Ad集㝷なー.步辺相金Amazon安〇宣エ一.]CRIT子グSHペ https」下参勧.google BOリ INFOJava AI "sic a OctokithTA規時 it QPHare AutoMa移災Ke位シ成25.hof 日lingem::.co STARTLIB Kapi-LTE PYU体OA CODE TOPkitキ HACK LOK通NaOD事【ya VET谷Ai→綏fer Ce AActive Stream (300 TOって目者++Home Def了 »易人 Service能P午能-pro Word AIM INヅetcスZ"

("Building AI Applications with ChatGPT and Streamlit")
「シンプルで効果的: ChatGPTとStreamlitによるAIアプリデザインガイド」
Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 4.0 seconds as it raised RateLimitError: Rate limit reached for default-gpt-3.5-turbo in organization org-mDtOSMflYoMSL4WjsK8tjrf1 on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method..
Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 4.0 secon
g-mDtOSMflYoMSL4WjsK8tjrf1 on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method..
Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 4.0 seconds as it raised RateLimitError: Rate limit reached for default-gpt-3.5-turbo in organization org-mDtOSMflYoMSL4WjsK8tjrf1 on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method..
Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 8.0 seconds as it raised RateLimitError: Rate limit reached for default-gpt-3.5-turbo in organization org-mDtOSMflYoMSL4WjsK8tjrf1 on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method..

```

残念ながら、こっから先は課金しないといけないようですね、、、

-> 翌日 2023-08-01 にアクセスしたが同じだった

どうも rate limit は時間単位にどのくらいアクセスしているかが問題のようで、１分間の間にループするような処理が NG の原因と思われる

https://platform.openai.com/account/rate-limits
https://platform.openai.com/docs/guides/rate-limits/overview

上記の RPM = 3 に引っかかる模様

とりあえず、Streamlit 側をいじって画面をリッチにしてしまいましょう！
