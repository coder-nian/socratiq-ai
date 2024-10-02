## SocratiQ AI: Learn by questioning, master by doing!

SocratiQ AI is a Streamlit application designed to be your personal tutor for mastering Data Structures and Algorithms (DSA). It utilizes the Socratic method to guide you through learning, asking questions that prompt critical thinking and problem-solving rather than providing direct answers. 

**Demo**: https://socratiq-ai.streamlit.app/

**Video**:
<iframe height="300" width="500" src="https://youtube.com/embed/xfBAjSNMUb4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Features:

* **Interactive Chat Interface:** Ask questions about DSA concepts and receive insightful guidance from a Gemini-powered AI.
* **Code Evaluation:** Submit Python code snippets for feedback and suggestions. The AI will analyze your code, explain its functionality, and help you debug any issues.
* **Personalized Learning:**  SocratiQ AI tailors its questions to your specific needs and understanding, promoting a deeper grasp of DSA principles.

### Getting Started:

1. **Prerequisites:**
    * **Python:** Install Python 3.7 or later.
    * **Google Gemini API Key:** You will need a Google Gemini API key to access the AI model. Create an account and obtain your key from [https://aistudio.google.com/](https://aistudio.google.com/).
    * **Streamlit:** Install Streamlit using `pip install streamlit`.
    * **Requirements:** Install the necessary packages by running `pip install -r requirements.txt`.

2. **Set Up Environment:**
    * **Create Environment:**  It's recommended to create a virtual environment for your project. You can use `python -m venv .venv` and activate it with `source .venv/bin/activate` (Linux/macOS) or `.\venv\Scripts\activate` (Windows).
    * **Environment Variables**: You'll need to set the `GEMINI_API_KEY` environment variable. There are two ways to do this:
        * **Using the terminal**: `export GEMINI_API_KEY='YOUR_API_KEY'`
        * **Using a `.env` file**: Create a `.env` file in your project root. Add the following line to the `.env` file: `GEMINI_API_KEY=YOUR_API_KEY`

3. **Run the App:**
    * Navigate to the project directory in your terminal.
    * Run `streamlit run app.py` to start the application.

4. **Start Learning:**
    * The application will open in your web browser.
    * You can start chatting with SocratiQ AI or submit code for evaluation.

### Using SocratiQ AI:

* **Chat:** Type your question or DSA concept into the chat box.
* **Code Evaluation:** Enter your Python code snippet into the code box. The AI will analyze your code and provide explanations and debugging suggestions.

### Additional Notes:

* The `requirements.txt` file lists all necessary packages for the project.
* The `app.py` file contains the main code for the application.
* Remember to replace `YOUR_API_KEY` with your actual Google Gemini API key.
