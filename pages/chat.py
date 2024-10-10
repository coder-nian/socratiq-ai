import streamlit as st
from pages.gemini import query_gemini

# Read Instructions
with open("pages/instructions/model_instructions.txt", "r") as f:
    model_instructions = f.read()

# Model Configuration
model_config = {
    "system_instruction": model_instructions,
}

# Intialize session state for history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "chat_button_clicked" not in st.session_state:
    st.session_state.chat_button_clicked = False

# App Header
st.markdown(
    f"""
<div style="text-align: center;">
    <h2 style="margin-top: 10px;">What’s on your mind today?</h2>
</div>
<br>
<br>
""",
    unsafe_allow_html=True,
)

# Display chat messages from history on app rerun
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


example_prompts = [
    "Find the time complexity of merge sort",
    "Explain how binary search trees work",
    "Write code to implement stacks using arrays",
    "What is the difference between DFS and BFS",
    "Optimize a solution to find largest in array",
    "What are pros and cons of linked lists vs arrays",
]

example_prompts_help = [
    "Look for the time complexity of sorting algorithms",
    "Search for how binary search trees operate and behave",
    "Implement stacks using arrays in a specific language",
    "Compare DFS and BFS based on traversal techniques",
    "Optimize an approach using algorithms for maximum value",
    "Compare pros and cons of linked lists versus arrays",
]


# Display buttons only if no button was clicked before
if not st.session_state.chat_button_clicked:
    button_cols = st.columns(3)
    button_cols_2 = st.columns(3)

    # Check if any example prompt button is pressed
    if button_cols[0].button(example_prompts[0], help=example_prompts_help[0]):
        st.session_state.chat_button_clicked = True
        st.session_state.prompt = example_prompts[0]
    if button_cols[1].button(example_prompts[1], help=example_prompts_help[1]):
        st.session_state.chat_button_clicked = True
        st.session_state.prompt = example_prompts[1]
    if button_cols[2].button(example_prompts[2], help=example_prompts_help[2]):
        st.session_state.chat_button_clicked = True
        st.session_state.prompt = example_prompts[2]
    if button_cols_2[0].button(example_prompts[3], help=example_prompts_help[3]):
        st.session_state.chat_button_clicked = True
        st.session_state.prompt = example_prompts[3]
    if button_cols_2[1].button(example_prompts[4], help=example_prompts_help[4]):
        st.session_state.chat_button_clicked = True
        st.session_state.prompt = example_prompts[4]
    if button_cols_2[2].button(example_prompts[5], help=example_prompts_help[5]):
        st.session_state.chat_button_clicked = True
        st.session_state.prompt = example_prompts[5]

# Get users input
prompt = st.chat_input("Ask SocratiQ AI...") or st.session_state.get("prompt", "")

if prompt:
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Display assistant message in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(
            query_gemini(prompt, model_config, st.session_state.chat_history)
        )
        # Add assistant message to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": response})
    st.session_state.prompt = ""
