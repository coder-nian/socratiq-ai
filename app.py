import streamlit as st

home = st.Page("pages/home.py", title="Home", icon="⚡")
chat_page = st.Page("pages/chat.py", title="Chat", icon="👨‍💻")
code_eval_page = st.Page("pages/code_eval.py", title="Evaluator", icon="🔍")
challenge_page = st.Page("pages/challenges.py", title="Challenges", icon="🏆")

pg = st.navigation([home, chat_page, code_eval_page, challenge_page])
st.set_page_config(page_title="SocratiQ AI", page_icon="⚡")
st.logo("assets/logo.png")
pg.run()