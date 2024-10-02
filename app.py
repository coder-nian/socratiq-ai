import streamlit as st
import os
import google.generativeai as genai


# Google Gemini API Setup
genai.configure(api_key=os.environ["GEMINI_API_KEY"])


# Model configuration details
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

# Intialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []


# Function to query the Gemini API
def query_gemini_api(user_input):
    INSTRUCTIONS = """
    You are Socratiq AI, a thoughtful tutor using the Socratic method to help students master Data Structures and Algorithms (DSA). Instead of providing direct answers, you guide them with open-ended, probing questions that encourage critical thinking and self-discovery. Your goal is to prompt students to analyze their problem-solving approaches, identify gaps in their understanding, and explore more efficient solutions. For instance, when a student struggles with a concept, you might ask, "How does a linked list differ from an array?" or when debugging, "What output did you expect, and where does it differ?" You focus on time complexity, optimization, and trade-offs between algorithms or data structures, leading students to discover the answers themselves. Your role is to foster deep understanding by asking questions that challenge their assumptions and build critical thinking skills.
    """

    # Assigning configs to the model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction=INSTRUCTIONS,
    )

    # Initializing chat history
    history = []

    # Loads chat history
    for index, message in enumerate(st.session_state.history):
        if index % 2 == 0:
            history.append({"role": "user", "parts": [message["content"]]})
        else:
            history.append({"role": "model", "parts": [message["content"]]})

    # Checks the response
    try:
        response = model.generate_content(history, stream=True)
        for chunk in response:
            yield chunk.text
    except Exception as e:
        return f"Error: {str(e)}"


# Function to evaluate Python code
def evaluate_code(code_snippet):
    INSTRUCTIONS = """
    You are an AI agent designed to assist users in understanding code, debugging, and writing test cases. Your primary goal is to guide users through the coding process with clear explanations and constructive feedback. When a user presents a piece of code, begin by asking clarifying questions to ensure you understand their intent. Then, help them break down the code into manageable sections, explaining each part and its purpose.

    When debugging, encourage the user to identify specific issues by asking them to describe the problem they're encountering. Guide them through the debugging process with probing questions, such as "What output are you expecting?" and "What do you see instead?" Assist them in testing different scenarios and suggest common debugging techniques.

    For writing test cases, prompt users to think critically about the functionality of their code. Ask them about edge cases and expected outcomes. For example, inquire, "What inputs could cause your function to fail?" and "How would you verify that your function behaves as expected?" Help them create comprehensive test cases that cover various situations, ensuring the code's reliability.

    Always focus on guiding users through self-discovery and critical thinking, fostering their understanding of coding concepts and best practices. Avoid providing direct answers; instead, empower them to solve problems independently.
    """

    # Assigning configs to the model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction=INSTRUCTIONS,
        tools="code_execution",
    )

    # Checks the response
    try:
        response = model.generate_content(code_snippet, stream=True)
    except Exception as e:
        return f"Error: {str(e)}"
    
    # Evaluates Code and returns what the code does
    try:
        exec_globals = {}
        exec(code_snippet, exec_globals)
        yield "Code executed successfully!\n\n\nExplanation: "
        st.balloons()
        for chunk in response:
            yield chunk.text
    except Exception as e:
        yield f"Code execution failed: {str(e)}\n\n\nExplanation: "
        for chunk in response:
            yield chunk.text


# Main App Layout
def main():
    st.set_page_config(page_title="SocratiQ AI", layout="wide")

    # App Header
    st.title("⚡ SocratiQ AI")
    st.subheader("Learn by questioning, master by doing!")

    # Sidebar Code
    with st.sidebar:
        # Sidebar title
        st.title("🔍 Code Evaluation")
        # User input box
        user_input = st.text_area(
            "Enter a Python code snippet here:",
            height=100,
            help="Submit Python code for feedback. For example: print(1 + 1)",
        )
        # Submit button
        if st.button("Submit"):
            if user_input:
                st.write("Processing your submission...")
                # Returns an evaluation summary and prints it
                code_feedback = evaluate_code(user_input)
                st.markdown("#### 🧑‍💻 Code Feedback")
                st.write_stream(code_feedback)

    # Display chat messages from history on app rerun
    for message in st.session_state.history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Get users input
    if prompt := st.chat_input("Ask SocratiQ AI..."):
        # Add user message to chat history
        st.session_state.history.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Display assistant message in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(query_gemini_api(prompt))
            # Add assistant message to chat history
        st.session_state.history.append({"role": "assistant", "content": response})


# Run the app
if __name__ == "__main__":
    main()
