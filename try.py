import os
from llama_index.core import VectorStoreIndex, Document, StorageContext, Settings
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.gemini import Gemini
from dotenv import load_dotenv
import chromadb

# Set the API key for accessing the Gemini model.
load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')

# Define your text data
text_data = [
    "Machine learning is a field of artificial intelligence that uses algorithms to learn from data.",
    "Data science involves the extraction of insights and knowledge from both structured and unstructured data.",
    "Artificial intelligence encompasses a range of technologies designed to simulate human intelligence.",
    "Natural language processing enables computers to understand and interpret human language.",
    "Supervised learning involves training a model on labeled data to predict outcomes for new data.",
    "Unsupervised learning focuses on discovering hidden patterns or intrinsic structures in input data.",
    "Reinforcement learning is a type of machine learning where an agent learns by interacting with its environment.",
    "Neural networks, inspired by the human brain, are computational models used for pattern recognition.",
    "Computer vision allows machines to interpret and understand visual information from the world.",
    "Deep learning, a subset of machine learning, uses multi-layered neural networks to analyze complex data."
]

# Create Document objects from the text data
documents = [Document(text=text) for text in text_data]

# Set the embedding model to be used in the settings
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# Set the language model to be used in the settings
Settings.llm = Gemini(api_key=gemini_api_key, model_name="models/gemini-pro")

# Create a Chroma client and a new collection
chroma_client = chromadb.EphemeralClient()
chroma_collection = chroma_client.create_collection("quickstart")

# Set up ChromaVectorStore and load in data
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# Create the VectorStoreIndex from the loaded documents
index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)

# Initialize the query engine
query_engine = index.as_query_engine()

# Query Data
response = query_engine.query("ai")
print(response)
