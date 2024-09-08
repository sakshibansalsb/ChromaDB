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

# index = VectorStoreIndex.from_documents(documents,)

# create client and a new collection
chroma_client = chromadb.EphemeralClient()
chroma_collection = chroma_client.create_collection("quickstart")


# set up ChromaVectorStore and load in data
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents( documents, storage_context=storage_context,)
# Update & Delete

doc_to_update = chroma_collection.get(limit=1)
doc_to_update["metadatas"][0] = {
    **doc_to_update["metadatas"][0],
    **{"author": "Paul Graham"},
}
chroma_collection.update(
    ids=[doc_to_update["ids"][0]], metadatas=[doc_to_update["metadatas"][0]]
)
updated_doc = chroma_collection.get(limit=1)
print(updated_doc["metadatas"][0])

# delete the last document
print("count before", chroma_collection.count())
chroma_collection.delete(ids=[doc_to_update["ids"][0]])
print("count after", chroma_collection.count()) 