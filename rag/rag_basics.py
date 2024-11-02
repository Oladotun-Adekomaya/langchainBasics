import os

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv 
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain.prompts import PromptTemplate 
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain 
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableSequence, RunnableParallel, RunnableBranch


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "books", "odyssey.txt")
persistent_directory = os.path.join(current_dir, "db", "chroma_db")