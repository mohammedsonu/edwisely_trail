import streamlit as st
import requests
import pymongo
import firebase_admin
from firebase_admin import credentials, db

if not firebase_admin._apps:
    # Initialize Firebase with your own configuration
    cred = credentials.Certificate("C:/Users/moham/Desktop/CO-PILOT/firebase/edwisey-hook-firebase-adminsdk-q55nh-579b17bbe9.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://edwisey-hook-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })

def get_hook_response_mega(prompt, user_input):
    api_key = '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'
    endpoint = 'https://api.openai.com/v1/chat/completions'
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'system', 'content': 'You are a creative and intelligent machine.'}, {'role': 'user', 'content': f"{prompt}\nUser: {user_input}"}],
    }

    response = requests.post(endpoint, json=data, headers=headers)
    
    # Extract the bot response from the response
    bot_response = response.json()['choices'][0]['message']['content']
    return bot_response

def get_hook_response(prompt_type, user_input):
    api_key = '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'
    endpoint = 'https://api.openai.com/v1/chat/completions'
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    
    prompts = {
        "Quotation Hook": "Imagine you're a creative blogger, and generate a captivating quotation hook on a topic. Choose a quote from a credible source, introduce it, and then explain its meaning to the reader in the most simple English. Illustrate how the quote relates to the chosen topic and provide insights in a way that resonates with a reader's point of view. Keep the language simple, and avoid fancy words to ensure clear and engaging communication. Start with an eye-catching one-liner and then give content of 100 words in a single passage. The topic is",
        "Question Hook": "Create a compelling one-liner rhetorical  question hook within 20 words for a blog, intriguing readers to explore a parallel world related to the topic. Write a 100-word explanation in simple language, employing rhetorical questions to captivate readers and prompt introspection on the topic, challenging their perspectives and leaving them eager for more. The reader must understand the concept of the topic by the end. The topic is",
        "Statistic Hook": "Generate a compelling statistical analysis exploring the profound impact of a topic by utilizing a diverse range of figures, numbers, decimals, and percentages. Craft a data-driven narrative that highlights the importance, relevance, and conceptual depth of the Topic, employing a statistic hook in the form of a quote to introduce key insights. Ensure the quote is rich in statistical details, and following its inclusion, provide a clear and insightful explanation of the quote's significance in relation to the overarching narrative of the statistical exploration. The topic is ",
        "Application Hook": "Generate an attention-grabbing application hook that surprises readers with intriguing facts or definitions related to the topic. Provide information that piques curiosity and encourages readers to delve deeper into your content. Additionally, craft a hook that reveals common misconceptions by presenting a well-known fact and demonstrating its falseness in relation to the topic. Ensure your hook includes real-life applications or examples, making the topic more tangible and engaging for the reader. The topic is",
        "Sarcasm Hook": "Inject a dose of humor into the content by creating a clever and sarcastic joke related to the topic. Infuse wit and ensure the joke has a conceptual tie to the topic. Craft the joke in a way that delivers a subtle lesson or insight, ensuring the reader learns something from the humor while keeping the tone light and entertaining. The topic is",
        "Story Hook": "Craft a captivating anecdotal hook by narrating a real or compelling fictional story seamlessly introducing and explaining the topic. Keep the language simple, ensuring the narrative is easy to follow, relevant, and contextual. Infuse creativity into the story, striking a balance between attention-grabbing elements and educational content. Leverage the freedom to shape the storyline for maximum impact, ensuring a connection to the main idea of the topic while highlighting its relevance to the overall topic. Your goal is to engage readers through a real-life story, a personal story, or an imaginative tale that enhances understanding and interest in the subject matter."
    }

    selected_prompt = prompts.get(prompt_type)

    if selected_prompt is not None:
        data = {
            'model': 'gpt-3.5-turbo',
            'messages': [{'role': 'system', 'content': 'You are a creative and intelligent machine.'}, {'role': 'user', 'content': f"{selected_prompt}\nUser: {user_input}"}],
        }

        response = requests.post(endpoint, json=data, headers=headers)
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Invalid prompt type: {prompt_type}"
    
def get_chatbot_response(prompt):
    api_key = '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'
    endpoint = 'https://api.openai.com/v1/chat/completions'
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'system', 'content': 'You are a creative teacher.'}, {'role': 'user', 'content': prompt}],
    }

    response = requests.post(endpoint, json=data, headers=headers)
    return response.json()['choices'][0]['message']['content']


def main():
    st.title("Edwisely Hook Generator")

    prompt_options = ["Quotation Hook","Question Hook","Statistic Hook","Application Hook","Sarcasm Hook","Story Hook"]

    user_input = st.text_input("You:", "")
    prompts = {
        "Quotation Hook": "Imagine you're a creative blogger, and generate a captivating quotation hook on a topic. Choose a quote from a credible source, introduce it, and then explain its meaning to the reader in the most simple english. Illustrate how the quote relates to the chosen topic and provide insights in a way that resonates with an reader's point of view. Keep the language simple, and avoid fancy words to ensure clear and engaging communication. Start with an eye-catching one-liner and then give content of 100 words in a single passage.Use english that a 10 year old would understand too. The topic is",
        "Question Hook": "Create a compelling one-liner rhetorical  question hook within 20 words for a blog, intriguing readers to explore a parallel world related to the topic. Write a 100-word explanation in simple language, employing rhetorical questions to captivate readers and prompt introspection on the topic, challenging their perspectives and leaving them eager for more. The reader must understand the concept of the topic by the end.Use english that a 10 year old would understand too. The topic is",
        "Statistic Hook": "Generate a compelling statistical analysis exploring the profound impact of a topic by utilizing a diverse range of figures, numbers, decimals, and percentages. Craft a data-driven narrative that highlights the importance, relevance, and conceptual depth of the Topic, employing a statistic hook in the form of a quote to introduce key insights. Ensure the quote is rich in statistical details, and following its inclusion, provide a clear and insightful explanation of the quote's significance in relation to the overarching narrative of the statistical exploration.Use english that a 10 year old would understand too. The topic is ",
        "Application Hook": "Generate an attention-grabbing application hook that surprises readers with intriguing facts or definitions related to the topic. Provide information that piques curiosity and encourages readers to delve deeper into your content. Additionally, craft a hook that reveals common misconceptions by presenting a well-known fact and demonstrating its falseness in relation to the topic. Ensure your hook includes real-life applications or examples, making the topic more tangible and engaging for the reader.Use english that a 10 year old would understand too. The topic is",
        "Sarcasm Hook": "Inject a dose of humor into the content by creating a clever and sarcastic joke related to the topic. Infuse wit and ensure the joke has a conceptual tie to the topic. Craft the joke in a way that delivers a subtle lesson or insight, ensuring the reader learns something from the humor while keeping the tone light and entertaining.Use english that a 10 year old would understand too. The topic is",
        "Story Hook": "Craft a captivating anecdotal hook by narrating a real or compelling fictional story seamlessly introducing and explaining the topic. Keep the language simple, ensuring the narrative is easy to follow, relevant, and contextual. Infuse creativity into the story, striking a balance between attention-grabbing elements and educational content. Leverage the freedom to shape the storyline for maximum impact, ensuring a connection to the main idea of the topic while highlighting its relevance to the overall topic. Your goal is to engage readers through a real-life story, a personal story, or an imaginative tale that enhances understanding and interest in the subject matter.Use english that a 10 year old would understand too.The topic is"
    }
    selected_prompt_option = st.selectbox("Select a prompt:", prompt_options)

    if st.button("Ask"):
        bot_response = get_hook_response(selected_prompt_option, user_input)
        st.write(f"Bot: {bot_response}")
        if selected_prompt_option == "Quotation Hook":
            result_data = {
            "prompt": selected_prompt_option,
            "input": user_input,
            "Quotation Hook":bot_response,
            "Question Hook":" " ,
            "Statistic Hook":" ",
            "Application Hook":" ",
            "Sarcasm Hook":" ",
            "Story Hook":" ",
            "Base Prompt Hook": " ",
            }
        elif selected_prompt_option == "Question Hook":
            result_data = {
            "prompt": selected_prompt_option,
            "input": user_input,
            "Quotation Hook":" ",
            "Question Hook":bot_response,
            "Statistic Hook":" ",
            "Application Hook":" ",
            "Sarcasm Hook":" ",
            "Story Hook":" ",
            "Base Prompt Hook": " ",
            }
        elif selected_prompt_option == "Statistic Hook":
            result_data = {
            "prompt": selected_prompt_option,
            "input": user_input,
            "Quotation Hook":" ",
            "Question Hook":" ",
            "Statistic Hook":bot_response,
            "Application Hook":" ",
            "Sarcasm Hook":" ",
            "Story Hook":" ",
            "Base Prompt Hook": " ",
            }
        elif selected_prompt_option == "Application Hook":
            result_data = {
            "prompt": selected_prompt_option,
            "input": user_input,
            "Quotation Hook":" ",
            "Question Hook":" ",
            "Statistic Hook":" ",
            "Application Hook":bot_response,
            "Sarcasm Hook":" ",
            "Story Hook":" ",
            "Base Prompt Hook": " ",
            }
        elif selected_prompt_option == "Sarcasm Hook":
            result_data = {
            "prompt": selected_prompt_option,
            "input": user_input,
            "Quotation Hook":" ",
            "Question Hook":" ",
            "Statistic Hook":" ",
            "Application Hook":" ",
            "Sarcasm Hook":bot_response,
            "Story Hook":" ",
            "Base Prompt Hook": " ",
            }
        elif selected_prompt_option == "Story Hook":
            result_data = {
            "prompt": selected_prompt_option,
            "input": user_input,
            "Quotation Hook":" ",
            "Question Hook":" ",
            "Statistic Hook":" ",
            "Application Hook":" ",
            "Sarcasm Hook":" ",
            "Story Hook":bot_response,
            "Base Prompt Hook": " ",
            }
        ref1 = db.reference('Individual prompt')
        ref1.set(result_data)

    if st.button("Mega Prompt (Concatination of Results of all the individual hooks)"):
        # Initialize variables to store responses
        # Initialize variables to store responses

        prompts = {
        "Quotation Hook": "Imagine you're a creative blogger, and generate a captivating quotation hook on a topic. Choose a quote from a credible source, introduce it, and then explain its meaning to the reader in the most simple English. Illustrate how the quote relates to the chosen topic and provide insights in a way that resonates with a reader's point of view. Keep the language simple, and avoid fancy words to ensure clear and engaging communication. Start with an eye-catching one-liner and then give content of 100 words in a single passage.Use english that a 10 year old would understand too. The topic is",
        "Question Hook": "Create a compelling one-liner rhetorical  question hook within 20 words for a blog, intriguing readers to explore a parallel world related to the topic. Write a 100-word explanation in simple language, employing rhetorical questions to captivate readers and prompt introspection on the topic, challenging their perspectives and leaving them eager for more.Start with an eye-catching one-liner and then give content of 200 words in a single passage.Use english that a 10 year old would understand too. The topic is",
        "Statistic Hook": "Generate a compelling statistical analysis exploring the profound impact of a topic by utilizing a diverse range of figures, numbers, decimals, and percentages. Craft a data-driven narrative that highlights the importance, relevance, and conceptual depth of the Topic, employing a statistic hook in the form of a quote to introduce key insights. Ensure the quote is rich in statistical details, and following its inclusion, provide a clear and insightful explanation of the quote's significance in relation to the overarching narrative of the statistical exploration.Start with an eye-catching one-liner and then give content of 200 words in a single passage.Use english that a 10 year old would understand too. The topic is ",
        "Application Hook": "Generate an attention-grabbing application hook that surprises readers with intriguing facts or definitions related to the topic. Provide information that piques curiosity and encourages readers to delve deeper into your content. Additionally, craft a hook that reveals common misconceptions by presenting a well-known fact and demonstrating its falseness in relation to the topic. Ensure your hook includes real-life applications or examples, making the topic more tangible and engaging for the reader.Start with an eye-catching one-liner and then give content of 200 words in a single passage.Use english that a 10 year old would understand too. The topic is",
        "Sarcasm Hook": "Inject a dose of humor into the content by creating a clever and sarcastic joke related to the topic. Infuse wit and ensure the joke has a conceptual tie to the topic. Craft the joke in a way that delivers a subtle lesson or insight, ensuring the reader learns something from the humor while keeping the tone light and entertaining.Start with an eye-catching one-liner and then give content of 200 words in a single passage.Use english that a 10 year old would understand too. The topic is",
        "Story Hook": "Craft a captivating anecdotal hook by narrating a real or compelling fictional story seamlessly introducing and explaining the topic. Keep the language simple, ensuring the narrative is easy to follow, relevant, and contextual. Infuse creativity into the story, striking a balance between attention-grabbing elements and educational content. Leverage the freedom to shape the storyline for maximum impact, ensuring a connection to the main idea of the topic while highlighting its relevance to the overall topic. Your goal is to engage readers through a real-life story, a personal story, or an imaginative tale that enhances understanding and interest in the subject matter.Name the title of the story in a very creative and eyecatching way.Use english that a 10 year old would understand too.The topic is"
        }

        quotation_response = ""
        question_response = ""
        statistic_response = ""
        application_response = ""
        sarcasm_response = ""
        story_response = ""

        # Iterate through each prompt and get the response
        for prompt_type, prompt_text in prompts.items():
            # Attach user input to the prompt
            full_prompt = f"{prompt_text}\nUser: {user_input}"
            
            # Get the response
            bot_response = get_hook_response_mega(full_prompt, user_input)

            # Store the responses in variables
            if prompt_type == "Quotation Hook":
                quotation_response = bot_response
            elif prompt_type == "Question Hook":
                question_response = bot_response
            elif prompt_type == "Statistic Hook":
                statistic_response = bot_response
            elif prompt_type == "Application Hook":
                application_response = bot_response
            elif prompt_type == "Sarcasm Hook":
                sarcasm_response = bot_response
            elif prompt_type == "Story Hook":
                story_response = bot_response

        # Concatenate responses with one empty line between each response
        st.markdown("<h2>Quotation Output</h2>", unsafe_allow_html=True)
        st.write(question_response)
        st.markdown("<br><br>",unsafe_allow_html=True)
        st.markdown("<h2>Question Output</h2>", unsafe_allow_html=True)
        st.write(question_response)
        st.markdown("<br><br>",unsafe_allow_html=True)
        st.markdown("<h2>Statistic Output</h2>", unsafe_allow_html=True)
        st.write(statistic_response)
        st.markdown("<br><br>",unsafe_allow_html=True)
        st.markdown("<h2>Application Output</h2>", unsafe_allow_html=True)
        st.write(application_response)
        st.markdown("<br><br>",unsafe_allow_html=True)
        st.markdown("<h2>Sarcasm Output</h2>", unsafe_allow_html=True)
        st.write(sarcasm_response)
        st.markdown("<br><br>",unsafe_allow_html=True)
        st.markdown("<h2>Story Output</h2>", unsafe_allow_html=True)
        st.write(story_response)
        result_data = {
            "prompt": "mega prompt",
            "input": user_input,
            "Quotation Hook":question_response,
            "Question Hook":question_response,
            "Statistic Hook":statistic_response,
            "Application Hook":application_response,
            "Sarcasm Hook":sarcasm_response,
            "Story Hook":story_response,
            "Base Prompt Hook": " ",
            }
        ref2 = db.reference('Mega Prompt')
        ref2.set(result_data)

    if st.button("Base Prompt (Single Prompt covering all the hook requirements)"):
        predefined_prompt = (
        "Imagine you're a creative teacher aiming to captivate students' interest in a topic. Your goal is to explain the concept in a simple and engaging manner. Start by sharing a relevant quote or mentioning a notable figure related to the topic. Pose thought-provoking questions that transport students to a parallel world, making the subject more intriguing. Next, present statistics using numbers and figures to enhance comprehension. If applicable, provide real-life applications or examples to make the topic more tangible."
        "Now, add a touch of humor with a clever, sarcastic joke related to the subject. Finally, the most crucial part is to craft a compelling story that seamlessly introduces and explains the topic. Your narrative should be easy to follow, keeping the language simple and ensuring it's both relevant and contextual. Feel free to infuse creativity into the story, maintaining a balance between capturing attention and delivering educational content. Embrace creative freedom to shape the storyline for maximum impact."
    )

        prompt = f"{predefined_prompt}\nUser: {user_input}"
        bot_response = get_chatbot_response(prompt)

        st.write(f"Bot: {bot_response}")
        result_data = {
            "prompt": "base prompt",
            "input": user_input,
            "Quotation Hook":"",
            "Question Hook":"",
            "Statistic Hook":"",
            "Application Hook":"",
            "Sarcasm Hook":"",
            "Story Hook":"",
            "Base Prompt Hook":bot_response,
            }
        ref3 = db.reference('Base prompt')
        ref3.set(result_data)
if __name__ == "__main__":
    main()
