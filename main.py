from dotenv import load_dotenv 
import os
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai

load_dotenv()

geminiapi_key = os.getenv('geminiapi_key')



llm = ChatGoogleGenerativeAI(model="gemini-pro")
llm.invoke("Sing a ballad of LangChain.")

genai.configure(api_key=geminiapi_key)

# get a list of all models in gemini
# for model in genai.list_models():
#     print(model.name)

# model = genai.GenerativeModel("gemini-1.5-pro-002")
# response = model.generate_content("Write a story about a magic backpack.")
# print(response.text)

# llm = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0.9)

# # Send a creative prompt to the LLM
# response = llm.invoke('Write a paragraph about life on Mars in year 2100.')
# print(response.content)
