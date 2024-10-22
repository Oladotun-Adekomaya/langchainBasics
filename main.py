from dotenv import load_dotenv 
import os
from langchain_google_genai import ChatGoogleGenerativeAI
# import google.generativeai as genai

load_dotenv()

geminiapi_key = os.getenv('geminiapi_key')


# genai.configure(api_key=geminiapi_key)

# model = genai.GenerativeModel("gemini-1.5-flash")

os.environ['GOOGLE_API_KEY']=geminiapi_key


llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-002",temperature=0.9)
response = llm.invoke("Sing a ballad of LangChain.")
print(response.content)





# Check the list of models

# for model in genai.list_models():
#     print(model.name)
