## SocratiQ AI: Learn by questioning, master by doing!

SocratiQ AI is a Streamlit application designed to be your personal tutor for mastering Data Structures and Algorithms (DSA). It utilizes the Socratic method to guide you through learning, asking questions that prompt critical thinking and problem-solving rather than providing direct answers. 

**Demo**: https://socratiq-ai.streamlit.app/

**Video**: https://youtu.be/xfBAjSNMUb4

### Features:

* **Interactive Chat Interface:** Ask questions about DSA concepts and receive insightful guidance from a Gemini-powered AI.
* **Code Evaluation:** Submit Python code snippets for feedback and suggestions. The AI will analyze your code, explain its functionality, and help you debug any issues.
* **Personalized Learning:**  SocratiQ AI tailors its questions to your specific needs and understanding, promoting a deeper grasp of DSA principles.
* **Problem Set Generator:** Generate personalized problem sets for various DSA topics, tailored to your current skill level. These problem sets include a mix of easy, medium, and hard challenges, designed to solidify your understanding.

### Getting Started:

#### 1. Prerequisites:

* **Python:** Install Python 3.7 or later. You can download the latest version from [https://www.python.org/](https://www.python.org/).
* **Google Gemini API Key:** You will need a Google Gemini API key to access the AI model.  Create an account and obtain your key from [https://aistudio.google.com/](https://aistudio.google.com/).
* **Requirements:** Install the necessary packages by running `pip install -r requirements.txt`.

#### 2. Setting Up Your Environment:

* **Create a Virtual Environment:**  It's recommended to create a virtual environment to manage dependencies for your project. You can use `python -m venv .venv` and activate it with `source .venv/bin/activate` (Linux/macOS) or `.\venv\Scripts\activate` (Windows). 
* **Environment Variables:** Set the `GEMINI_API_KEY` environment variable:
    * **Using the terminal:** `export GEMINI_API_KEY='YOUR_API_KEY'` 
    * **Using a `.env` file:** Create a `.env` file in your project root. Add the following line to the `.env` file: `GEMINI_API_KEY=YOUR_API_KEY` 

#### 3. Run the Application:

* Navigate to the project directory in your terminal.
* Run `streamlit run app.py` to start the application.

#### 4. Start Learning:

* The application will open in your web browser.
* You can start chatting with SocratiQ AI, submit code for evaluation, or generate practice problem sets.

### Using SocratiQ AI:

* **Chat:** Type your question or DSA concept into the chat box.
* **Code Evaluation:** Enter your Python code snippet into the code box. The AI will analyze your code and provide explanations and debugging suggestions.
* **Problem Sets:** Pass the DSA topic to the Problem Set Generator, and it will generate personalized practice problems based on the topic and difficulty level.

### Additional Notes:

* The `requirements.txt` file lists all necessary packages for the project.
* The `app.py` file contains the code to run the application.
* Remember to replace `YOUR_API_KEY` with your actual Google Gemini API key.