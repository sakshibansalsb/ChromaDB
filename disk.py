import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader,Settings
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.gemini import Gemini
from IPython.display import Markdown, display
import chromadb
from dotenv import load_dotenv

# Set the API key for accessing the Gemini model.
load_dotenv()
gemini_api_key=os.getenv('GEMINI_API_KEY')

# load documents
# documents = SimpleDirectoryReader("./data/paul_graham_essay.txt/").load_data()
documents = SimpleDirectoryReader("./data/").load_data()

# Set the embedding model to be used in the settings. Here, a HuggingFace model is specified.
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# Set the language model to be used in the settings. Here, the Gemini model is specified with an API key.
Settings.llm = Gemini(api_key=gemini_api_key, model_name="models/gemini-pro")
# save to disk
db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("quickstart")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context,
)

# load from disk
db2 = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db2.get_or_create_collection("quickstart")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
index = VectorStoreIndex.from_vector_store( vector_store,)
# Query Data
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)