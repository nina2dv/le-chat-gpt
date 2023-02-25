import cohere
import openai
import streamlit as st

def gen(prompt):
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=f'Roleplay as a typical house cat and explain using cat language on what would you do in the following statement: {prompt}',
        max_tokens=300,
        temperature=0.9,
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=[],
        return_likelihoods='NONE')
    return response.generations[0].text


def similarity(list_text):
    response = co.embed(
        model='large',
        texts=list_text)
    return response.embeddings


openai.api_key = st.secrets['open']
co = cohere.Client(st.secrets['co'])

def app():
    
   form = st.form(key='my_form')
   search = form.text_input(label='Have a chat with the cat')
   submit_button = form.form_submit_button(label='Enter')

   if submit_button:
       output_text = gen(search)
       st.info(output_text)
       st.session_state['key'].append({search: output_text})
       # st.write(f"Embeddings: {similarity(st.session_state['key'])}")

       try:
           image_resp = openai.Image.create(prompt=f'Cat: {output_text}', n=3, size="512x512")
           col1, col2, col3 = st.columns(3)
           with col1:
               st.image(image_resp["data"][0]["url"])
           with col2:
               st.image(image_resp["data"][1]["url"])
           with col3:
               st.image(image_resp["data"][2]["url"])
       except:
           st.write("_No Images :(_")





