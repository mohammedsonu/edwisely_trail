import requests
import streamlit as st

api_key = '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'
endpoint = 'https://api.openai.com/v1/chat/completions'

st.title("Hook Generator Edwisely")

def generate_summary(prompt):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}',
        }
            
        data = {
            'model': 'gpt-3.5-turbo',
            'messages': [{'role': 'system', 'content': 'You are a Hook Generator.'}, {'role': 'user', 'content': prompt}],
        }
        response = requests.post(endpoint, json=data, headers=headers)
        return response.json()['choices'][0]['message']['content']

query = st.text_input("Enter the Topic to Search")

pre_prompt = """A hook is an opening statement (which is usually the first sentence) in an essay that attempts to grab the reader’s attention so that they want to read on.
I want you to create a Hook on the given topic, Use the following Instructions to Create Hooks.
1.Place a strong emphasis on easy sentence formation, explain in simple terms, using everyday language. Keep it short and clear, The output should be like its written by a human (This is  very important instruction).
2.Start with an intriguing statement.(Try to tell where it is used in real world, or any did you know fact around the topic or any movie reference to the topic)
3.Give a Quotation which is related to the topic or has any connection with it, explain the Quotation in a concise manner.
3.Use statistics or share historical anecdotes.( Use numbers and Historical facts to show the impact of the topic or any incidents around it )
4.Give a story which has happened around the topic or related to it in the past.(Make sure the story is real and reliable. If there is no story around it, then avoid generating the story)
5.The output should be neatly presented in paragraph not more than 200 words combing all the instructions.
5.No additional Information or paragraph is required in the end.
6.Make sure the content does not seem like machine generated and has Human touch in it.
(Make sure all the 6 Instructions are strictly followed while generating the output)
The topic is .
"""
fin = " ".join([pre_prompt, query])
if st.button('Search'):
    summary = generate_summary(fin)
    st.write(summary)
