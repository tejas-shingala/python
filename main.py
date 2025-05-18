import streamlit as st
from PIL import Image

# Load image
image = Image.open("chatgpt-logo-png.webp")

# Display image
st.image(image, caption='Your Image Caption', width=200)
quiz_questions = [
        {
            "question": "chatgpt-logo-png.webp",
            "options": ["chatgpt", "whatsapp", "facebook", "instagram"],
            "answer": "chatgpt"
        },
        # {
        #     "question": "Who developed the theory of relativity?",
        #     "options": ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Stephen Hawking"],
        #     "answer": "Albert Einstein",
        #     "difficulty": "Medium",
        #     "category": "Science"
        # },
        # {
        #     "question": "What is the result of 7 * 8?",
        #     "options": ["54", "56", "64", "58"],
        #     "answer": "56",
        #     "difficulty": "Easy",
        #     "category": "Math"
        # }
    ]
for question in quiz_questions:
    st.write("Guess the logo")
    # for option in question[options]:
    #     # st.write(f"")