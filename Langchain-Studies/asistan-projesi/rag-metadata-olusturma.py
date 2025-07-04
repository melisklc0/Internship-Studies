import os

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import SentenceTransformerEmbeddings





current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")
db_dir = os.path.join(current_dir, "db")
persistent_directory = os.path.join(db_dir, "chroma_db_with_metadata")

print(f"Veri yolu: {data_dir}")
print(f"Veriseti yolu: {persistent_directory}")


if not os.path.exists(persistent_directory):
    print("Persistent directory does not exist. Initializing vector store...")

    # Ensure the data directory exists
    if not os.path.exists(data_dir):
        raise FileNotFoundError(
            f"The directory {data_dir} does not exist. Please check the path."
        )

    # List all text files in the directory
    text_files = [f for f in os.listdir(data_dir) if f.endswith(".txt")]

    # Read the text content from each file and store it with metadata
    documents = []
    for text_file in text_files:
        file_path = os.path.join(data_dir, text_file)
        loader = TextLoader(file_path, encoding='utf-8')
        text_docs = loader.load()
        for doc in text_docs:
            # Add metadata to each document indicating its source
            doc.metadata = {"source": text_file}
            documents.append(doc)

    # Split the documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # Display information about the split documents
    print("\n--- Document Chunks Information ---")
    print(f"Number of document chunks: {len(docs)}")

    # Create embeddings
    print("\n--- Creating embeddings ---")
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    print("\n--- Finished creating embeddings ---")

    # Create the vector store and persist it
    print("\n--- Creating and persisting vector store ---")
    db = Chroma.from_documents(
        docs, embeddings, persist_directory=persistent_directory)
    print("\n--- Finished creating and persisting vector store ---")

else:
    print("Vector store already exists. No need to initialize.")



# load_dotenv()
#
# OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"
# llm = ChatOpenAI(
#     model="mistralai/mistral-small-3.2-24b-instruct:free",
#     openai_api_key=os.getenv("OPENROUTER_API_KEY"),
#     openai_api_base=OPENROUTER_API_BASE,
#     temperature=0.7
# )


# embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
# 
# loader = TextLoader(r"D:\Üniversite\Internship-Studies\Langchain-Studies\asistan-projesi\data\war_and_peace.txt", encoding="utf-8")
# documents = loader.load()
# 
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
# docs = text_splitter.split_documents(documents)
# 
# db = Chroma.from_documents(docs, embedding_model, persist_directory="chroma_db")
# retriever = db.as_retriever(
#     search_type="similarity_score_threshold",
#     search_kwargs={"k": 3, "score_threshold": 0.1}
# )


