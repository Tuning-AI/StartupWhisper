from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from lib.utils import local_llm , audiof
import streamlit as st
from PIL import Image
llm_model = local_llm()
img = Image.open("icon.png")
st.set_page_config(page_title='Startup Assistant',page_icon = img)
st.sidebar.image("icon.png" , width=80)
st.header(":hand: Welcome To Your Startup Assistant : ")
st.info("""This project is based On Llama2_13B_startup_Assistant which is a highly specialized language 
        model fine-tuned from Meta's meta-llama/Llama-2-13b-chat-hf. 
        It has been tailored to assist with inquiries related to Algerian startups, 
        offering valuable insights and guidance in these domains""")
memory = ConversationBufferWindowMemory(k=3)
# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Hi Im Your Custom Startup Assistant , how can i help you today ? "}]
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "Hi Im Your Custom Startup Assistant , how can i help you today ? "}]
st.sidebar.button(':arrow_right: Clear Chat History :arrow_left: ', on_click=clear_chat_history)
use_audio = st.sidebar.checkbox("Use audio output")
chat = ConversationChain(
    llm=llm_model,
    verbose=False ,
    memory=memory
)
chat.prompt.template = \
"""
### INPUT:
You will provide a detailed response to a user's inquiry about startups.
Previous Conversation :
{history}

Current conversation:
### INPUT: {input}
### OUTPUT:"""

def run(input_text) : 
    return chat.predict(input=str(input_text))
# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = run(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    if use_audio :
        audiof(full_response)
    st.session_state.messages.append(message)
