from dotenv import load_dotenv 
import os
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain 



load_dotenv()

geminiapi_key = os.getenv('geminiapi_key')


# genai.configure(api_key=geminiapi_key)

# model = genai.GenerativeModel("gemini-1.5-flash")

os.environ['GOOGLE_API_KEY']=geminiapi_key


ai = ChatGoogleGenerativeAI(model="gemini-1.5-pro-002",temperature=0.9)


# response = ai.invoke("what is 2 divided by 2")
# print(type(response))


# How To Have Conversations with AI

# A very important thing to note is that there are 3 different types of messages
# System message - This sets the broad context for the conversation
# Human message - This is basically the prompt entered by the human
# AI message - This is the response of the ai

# message = [
#     ("system', 'Solve the following math problems"),
#     ("human", "81 divided by 9 is?"),
#     ("ai", "81 divided by 9 is 9"),
#     ("human", "What is 10 times 5?")
# ]


# result = ai.invoke(message)
# print(result)
# print('\n\n')
# print(result.content)


# Real Time conversation demo.

chatHistory = []

systemMessage = ("system", "You're an helpful AI assitant.")

chatHistory.append(systemMessage)

userInput = input("What is your question?\n\n")

# humanMessage = ("human", userInput)
# chatHistory.append(humanMessage)
# response = ai.invoke(chatHistory)
# aiResponseText = response.content
# aiMessage = ("ai", aiResponseText)
# print(aiResponseText)
# chatHistory.append(aiMessage)


while userInput != 'exit':
    humanMessage = ("human", userInput)
    chatHistory.append(humanMessage)
    response = ai.invoke(chatHistory)
    aiResponseText = response.content
    aiMessage = ("ai", aiResponseText)
    print("\n\n")
    print(aiResponseText)
    chatHistory.append(aiMessage)  
    userInput = input("What is your question?\n\n")






















# Prompt Template
promptTemplateName = PromptTemplate.from_template("I want to open a restaurant for {restaurant}. Suggest a fancy name for this.")
















# Check the list of models

# for model in genai.list_models():
#     print(model.name)
