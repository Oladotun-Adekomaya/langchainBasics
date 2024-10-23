from dotenv import load_dotenv 
import os
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain.prompts import PromptTemplate 
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain 
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory



load_dotenv()

PROJECT_ID = os.getenv('PROJECT_ID')
SESSION_ID = os.getenv('SESSION_ID')  # This could be a username or a unique ID
COLLECTION_NAME = os.getenv('COLLECTION_NAME')

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

# chatHistory = []

# systemMessage = ("system", "You're an helpful AI assitant.")

# chatHistory.append(systemMessage)



# humanMessage = ("human", userInput)
# chatHistory.append(humanMessage)
# response = ai.invoke(chatHistory)
# aiResponseText = response.content
# aiMessage = ("ai", aiResponseText)
# print(aiResponseText)
# chatHistory.append(aiMessage)


# while True:
#     userInput = input("You: ")
#     if userInput.lower() == "exit":
#         break

#     humanMessage = ("human", userInput) # create human message
#     chatHistory.append(humanMessage)
#     response = ai.invoke(chatHistory)
#     aiResponseText = response.content
#     aiMessage = ("ai", aiResponseText)
#     print(f'AI: {aiResponseText}')
#     chatHistory.append(aiMessage)  

# print('______ Message History ______')
# print(chatHistory)


#  Project that stores chat history to firetore
# Initialize Firestore Client
# print("Initializing Firestore Client...")
# client = firestore.Client(project=PROJECT_ID)

# print("Initializing Firestore Chat Message History...")
# chat_history = FirestoreChatMessageHistory(
#     session_id=SESSION_ID,
#     collection=COLLECTION_NAME,
#     client=client,
# )
# print("Chat History Initialized.")
# print("Current Chat History:", chat_history.messages)

# print("Start chatting with the AI. Type 'exit' to quit.")

# while True:
#     human_input = input("User: ")
#     if human_input.lower() == "exit":
#         break

#     chat_history.add_user_message(human_input)

#     ai_response = ai.invoke(chat_history.messages)
#     chat_history.add_ai_message(ai_response.content)

#     print(f"AI: {ai_response.content}")



# Prompt Template

# Part 1

# user_input = input("What topic do you want a joke about? ")
# template = "Tell me a joke about {topic}"
# prompt_template = PromptTemplate.from_template(template)
# prompt = prompt_template.invoke({"topic" : user_input})
# print(prompt)

template_multiple = """You're an helpful assistant.
Human: Tell me a {adjective} story about a {animal}.
Assistant:"""

chat_template = ChatPromptTemplate.from_template(template_multiple)

prompt = chat_template.invoke({"adjective": "fast", "animal": "dog"})

user_input_adjective = input("What is the adjective? ")
user_input_animal = input("What is the animal? ")

print(prompt)












# Check the list of models

# for model in genai.list_models():
#     print(model.name)
