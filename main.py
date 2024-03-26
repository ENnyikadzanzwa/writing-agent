import streamlit as st

from json import loads
from requests import post

st.set_page_config(
    page_title = "Nyikadzanzwa|Writing Agent",
    page_icon = "🤖",
    layout ="wide"
    )

url = "https://api.openai.com/v1/chat/completions"
openai_api_key = "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"
model_name = "gpt-3.5-turbo"  

headers = {
    "Authorization": f"Bearer {openai_api_key}"
}







# Define the text generation function using GPT-3
def generate_text(prompt):
    data = {
         "model": model_name,
         "messages": [
        {
            "role": "system",
            "content": "Hello, how can I assist you?"
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
   
    
        }
    response = post(url, json=data, headers=headers)
    information = loads(response.text)
    data = information['choices'][0]['message']['content']
    return data

# Streamlit app layout
st.title(":orange[Hi 👋am your Personal Ai Writing Agent]")

# Input text area for user input
input_text = st.text_area(":blue[ask me anything you want me to write about:]")
st.sidebar.header(':orange[Emmanuel AI 🤖]')
st.sidebar.title('Select what do you want me to write here',)


if st.sidebar.button(":blue[Generate Email]"):
    try:
        email_prompt = f"Write an email based on the following text:\n{input_text}"
        email_response = generate_text(email_prompt)
        st.info(email_response)
    except Exception as e:
        st.warning(f"Ooops! An error occured while processing your request{e}")

if st.sidebar.button(":blue[Generate Business Letter]"):
    try:
        letter_prompt = f"Write a business letter based on the following text:\n{input_text}"
        letter_response = generate_text(letter_prompt)
        st.info(letter_response)
    except Exception as e:
        st.warning(f"Ooops! An error occured while processing your request{e}")

if st.sidebar.button(":blue[Generate Article]"):
    try:
        article_prompt = f"Write an article based on the following text:\n{input_text}"
        article_response = generate_text(article_prompt)
        st.info(article_response)
    except Exception as e:
        st.warning(f"Ooops! An error occured while processing your request{e}")


if st.sidebar.button(":blue[Generate Essay]"):
    try:
        essay_prompt = f"Write an essay based on the following text:\n{input_text}"
        essay_response = generate_text(essay_prompt)
        st.info(essay_response)
    except Exception as e:
        st.warning(f"Ooops! An error occured while processing your request{e}")

if st.sidebar.button(":blue[Generate Poem]"):
    try:
        poem_prompt = f"Write a poem based on the following text:\n{input_text}"
        poem_response = generate_text(poem_prompt)
        st.info(poem_response)
    except Exception as e:
        st.warning(f"Ooops! An error occured while processing your request{e}")

if st.sidebar.button(":blue[Generate Song]"):
    try:
        song_prompt = f"Write a song based on the following text:\n{input_text}"
        song_response = generate_text(song_prompt)
        st.info(song_response)
    except Exception as e:
        st.warning(f"Ooops! An error occured while processing your request{e}")
