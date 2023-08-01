import streamlit as st
from streamlit_chat import message
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
from langchain.callbacks import get_openai_callback

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# ページの初期化
def init_page():
    st.set_page_config(
        page_title="Website Summarizer",
        page_icon="🤗"
    )
    st.header("Website Summarizer 🤗")
    st.sidebar.title("Options")

# ChatGPTが出力するメッセージの初期化
def init_messages():
    clear_button = st.sidebar.button("Clear Conversation", key="clear")
    if clear_button or "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant.")
        ]
        st.session_state.costs = []

# サイドバーの切り替え部分
def select_model():
    model = st.sidebar.radio("Choose a model:", ("GPT-3.5", "GPT-4"))
    if model == "GPT-3.5":
        model_name = "gpt-3.5-turbo"
    else:
        model_name = "gpt-4"

    return ChatOpenAI(temperature=0, model_name=model_name)

# URLの入力欄
def get_url_input():
    url = st.text_input("URL: ", key="input")
    return url

# URLの検証
# 入力されたURLが有効なものであるかどうかは validate_url関数で行っています。この関数の詳細な動作はAIアプリにあまり関係ないので省略します。(コードの実装内容が気になる方はChatGPTに聞いたりしてください)
def validate_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# ページの取得用の関数
def get_content(url):
    try:
        with st.spinner("Fetching Content ..."):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # fetch text from main (change the below code to filter page)
            # なるべく本文っぽいところを取得するように main や article タグを取得してくる、という多少の工夫は行なっています。
            # 次の章で説明するLangChainのDocumentLoaderの一つである WebBaseLoader を使う方法もありますが、細かい作業を行う場合はBeautifulSoupを使う必要があるっぽいのでここでは使っていません。(別に良いLoaderあれば教えてください🙏)
            if soup.main:
                return soup.main.get_text()
            elif soup.article:
                return soup.article.get_text()
            else:
                return soup.body.get_text()
    except:
        st.write('something wrong')
        return None

# 要約指示Promptの構築
# 次に、build_prompt関数で要約指示を行う Prompt を作り、それを後続処理(get_answer関数)でChatGPT APIに投げています。
def build_prompt(content, n_chars=300):
    return f"""以下はとある。Webページのコンテンツである。内容を{n_chars}程度でわかりやすく要約してください。

========

{content[:1000]}

========

日本語で書いてね！
"""


# コールバックでChatGPTの答えを取得する
def get_answer(llm, messages):
    with get_openai_callback() as cb:
        answer = llm(messages)
    return answer.content, cb.total_cost

# メインループ
def main():
    # ページを初期化
    init_page()

    # モードの選択の取得
    llm = select_model()

    # メッセージの初期化
    init_messages()

    # 出力部分のコンテナをレイアウト
    container = st.container()
    # レスポンスの出力部分をレイアウト
    response_container = st.container()

    # 要約の表示
    # 最後に、以下のように markdown 形式で見出しを作った上で、要約文を表示しています。
    # また、参考にするために原文も表示しています。
    with container:
        url = get_url_input()
        is_valid_url = validate_url(url)
        if not is_valid_url:
            st.write('Please input valid url')
            answer = None
        else:
            # ページの取得
            content = get_content(url)
            if content:
                prompt = build_prompt(content)
                st.session_state.messages.append(HumanMessage(content=prompt))
                with st.spinner("ChatGPT is typing ..."):
                    answer, cost = get_answer(llm, st.session_state.messages)
                st.session_state.costs.append(cost)
            else:
                answer = None

    if answer:
        with response_container:
            st.markdown("## Summary")
            st.write(answer)
            st.markdown("---")
            st.markdown("## Original Text")
            st.write(content)

    costs = st.session_state.get('costs', [])
    st.sidebar.markdown("## Costs")
    st.sidebar.markdown(f"**Total cost: ${sum(costs):.5f}**")
    for cost in costs:
        st.sidebar.markdown(f"- ${cost:.5f}")

# アンダースコアに惑わされるが「__name__に格納されている値が'__main__'という文字列であれば、以降の処理を実行する」という単なるif文。
# __name__とは: モジュールをインポートするとその__name__属性にモジュールの名前が文字列として格納される。<モジュール名>.__name__で取得できる。
# '__main__'とは: 上述のように、別のファイルからインポートされると__name__にはモジュール名が格納される。一方、ファイルをコマンドラインからスクリプトとして実行すると__name__には'__main__'という文字列が格納される。
# 参考: https://note.nkmk.me/python-if-name-main/
# 他のファイルからインポートされた場合はif __name__ == '__main__'以下のコードは実行されないので、余計な処理が発生することはない。
# モジュールをコマンドとして利用したい場合にもif __name__ == '__main__'が使える。
if __name__ == '__main__':
    main()