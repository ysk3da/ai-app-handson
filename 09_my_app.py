import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def init_page():
    st.set_page_config(
        page_title="Ask My PDF(s)",
        page_icon="🤗"
    )
    st.sidebar.title("Nav")
    st.session_state.costs = []

# PDFの取得
def get_pdf_text():
    uploaded_file = st.file_uploader(
        label='Upload your PDF here😇',
        type='pdf'  # アップロードを許可する拡張子 (複数設定可)
    )
    if uploaded_file:
        pdf_reader = PdfReader(uploaded_file)
        text = '\n\n'.join([page.extract_text() for page in pdf_reader.pages])
        text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            model_name=st.session_state.emb_model_name,
            # 適切な chunk size は質問対象のPDFによって変わるため調整が必要
            # 大きくしすぎると質問回答時に色々な箇所の情報を参照することができない
            # 逆に小さすぎると一つのchunkに十分なサイズの文脈が入らない
            chunk_size=250,
            chunk_overlap=0,
        )
        return text_splitter.split_text(text)
    else:
        return None

def page_pdf_upload_and_build_vector_db():
    # ここにPDFアップロードページの実装をする
    st.write('アップロードページ')

def page_ask_my_pdf():
    # ここにChatGPTに質問を投げるページの実装をする
    st.write('ChatGPTに質問を投げるページ')

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
