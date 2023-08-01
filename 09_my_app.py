import streamlit as st

def init_page():
    st.set_page_config(
        page_title="Ask My PDF(s)",
        page_icon="🤗"
    )
    st.sidebar.title("Nav")
    st.session_state.costs = []

def page_pdf_upload_and_build_vector_db(emb_model):
    # ここにPDFアップロードページの実装をする
    ''

def page_ask_my_pdf():
    # ここにChatGPTに質問を投げるページの実装をする
    ''

def main():
    init_page()

    # ページ切り替えを実装
    selection = st.sidebar.radio("Go to", ["PDF Upload", "Ask My PDF(s)"])
    if selection == "PDF Upload":
        # ここにPDFアップロードページの実装をする
        page_pdf_upload_and_build_vector_db()
    elif selection == "Ask My PDF(s)":
        # ここにChatGPTに質問を投げるページの実装をする
        page_ask_my_pdf()

    # コストの計算結果をサイドバーに表示する
    costs = st.session_state.get('costs', [])
    st.sidebar.markdown("## Costs")
    st.sidebar.markdown(f"**Total cost: ${sum(costs):.5f}**")
    for cost in costs:
        st.sidebar.markdown(f"- ${cost:.5f}")

if __name__ == '__main__':
    main()
