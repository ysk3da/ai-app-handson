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