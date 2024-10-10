import streamlit as st

# Function to display the landing page
st.markdown(
    f"""

    <header>
        <h1 style="text-align:center; margin-top:100px;">Welcome to SocratiQ AI</h1>
        <p style="text-align:center;">Learn by questioning, master by doing!</p>
    </header>


    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <style>
    .center-button {
        display: flex;
        justify-content: center;
        margin: 20px;
    }
    .link-button {
        text-decoration: none;
        background-color: white; /* White background */
        color: black;           /* Black text */
        padding: 10px 20px;
        border: 2px solid black; /* Optional border for better visibility */
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
    }
    .link-button:hover {
        text-decoration: none;
        background-color: #f0f0f0; /* Light gray on hover */
    }
    </style>
    <div class="center-button">
        <a class="link-button" href="chat">Explore</a>
    </div>
    """,
    unsafe_allow_html=True,
)


# st.link_button("Explore", url="chat")
