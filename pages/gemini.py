import os
import google.generativeai as genai

# Google Gemini API Setup
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Model configuration details
generation_config = {
    "temperature": 0.5,
    "top_p": 0.7,
    "top_k": 40,
    "max_output_tokens": 8192,
}

# Function to query the Gemini API
def query_gemini(user_input, model_config, session_history):
    # Assigning configs to the model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash", generation_config=generation_config, **model_config
    )
    # Initializing chat history
    history = []

    # Loads chat history
    for index, message in enumerate(session_history):
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
