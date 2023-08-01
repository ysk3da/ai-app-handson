# AI チャットアプリを作り込もう

- Streamlit でサイドバー付きの画面を作る方法を知る
- Streamlit の色々なウィジェットを知る (slider や radio)
- LangChain の便利な Callback 機能を知る

## 色々なオプションの使い方を学ぼう

### サイドバーに色々表示してみよう

さて、AI チャットアプリにサイドバーを設置して、色々なオプションを選択可能にしてみましょう。サイドバーの設置は非常に簡単です。

以下のように st.sidebar から書き始めれば、サイドバーに要素を設置することができます。以下のコードは要素の設置だけなので、これだけではまだ動きません。

`04_my_app.py`

```py
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
from langchain.callbacks import get_openai_callback

# サイドバーのタイトルを表示
st.sidebar.title("Options")

# サイドバーにオプションボタンを設置
model = st.sidebar.radio("Choose a model:", ("GPT-3.5", "GPT-4"))

# サイドバーにボタンを設置
clear_button = st.sidebar.button("Clear Conversation", key="clear")

# サイドバーにスライダーを追加し、temperatureを0から2までの範囲で選択可能にする
# 初期値は0.0、刻み幅は0.1とする
temperature = st.sidebar.slider("Temperature:", min_value=0.0, max_value=2.0, value=0.0, step=0.1)

# Streamlitはmarkdownを書けばいい感じにHTMLで表示してくれます
# (もちろんメイン画面でも使えます)
st.sidebar.markdown("## Costs")
st.sidebar.markdown("**Total cost**")
for i in range(3):
    st.sidebar.markdown(f"- ${i+0.01}")  # 説明のためのダミー
```

実行用コマンド

```sh
streamlit run 04_my_app.py
```

いいね！いい感じにサイドバーが表示された！

## 完成版の表示

```sh
streamlit run 04_sample_app.py
```
