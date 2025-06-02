# from dotenv import load_dotenv
import streamlit as st
# load_dotenv()
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

prompt = ''

st.title('시를 써드려요.')
result = st.text_input('주제를 입력해주세요',prompt)
if st.button('입력'):
    with st.spinner('기다려보셈'):
        respon = chat_model.predict('제목과 함께 아주 짧은 시을 적어주세요 주제는 다음과 같습니다. :'+result)
        st.write(respon)
else:
    st.write('기다리는중')
