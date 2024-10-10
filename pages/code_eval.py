import streamlit as st
from gemini import query_gemini

# Read Instructions
with open("instructions/code_model_instructions.txt", "r") as f:
    model_instructions = f.read()

# Model Configuration
model_config = {
    "system_instruction": model_instructions,
    "tools": "code_execution",
}

# Intialize session state for history
if "eval_history" not in st.session_state:
    st.session_state.code_eval_history = []

# App Header
st.markdown(
    f"""
<div style="text-align: center;">
    <h4 style="margin-top: 10px;">🔍 Code Evaluator</h4>
    <h2>Ready to uncover your code’s potential?</h2>
</div>
<br>
<br>
""",
    unsafe_allow_html=True,
)
# Display chat messages from history on app rerun
for message in st.session_state.code_eval_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Get users input
if prompt := st.chat_input("Evaluate code with SocratiQ AI..."):
    # Add user message to chat history
    st.session_state.code_eval_history.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Display assistant message in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(
            query_gemini(prompt, model_config, st.session_state.code_eval_history)
        )
        # Add assistant message to chat history
    st.session_state.code_eval_history.append({"role": "assistant", "content": response})
