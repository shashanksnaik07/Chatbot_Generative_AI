from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Fetch API keys from environment
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# Load data, split it into chunks, and download embeddings
extracted_data = load_pdf("Data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

# Initialize Pinecone with your API key (only once)
pc = Pinecone(api_key=PINECONE_API_KEY)

# Set the index name
index_name = "chatbot"


pc.create_index(
    name=index_name,
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)
# Create a PineconeVectorStore instance using the embeddings and text chunks

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings
)

# Now `docsearch` can be used to query the Pinecone index.
