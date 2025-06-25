from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser  
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"
llm = ChatOpenAI(
    model="mistralai/mistral-small-3.2-24b-instruct:free",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base=OPENROUTER_API_BASE,
    temperature=0.7
)   

# bu sefer metni dosyadan okuyacağız
with open("D:/Üniversite/Internship-Studies/Langchain-Studies/asistan-projesi/data/ornek-text.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)
chunks = text_splitter.split_text(raw_text)
context = "\n".join(chunks[:3])  # İlk 3 chunk ile sınırlı — örnek için

prompt = PromptTemplate(
    input_variables=["question"],
    template=f"""
Context:
{context}

Question: {{question}}
Answer:"""
)

chain = prompt | llm | StrOutputParser()

while True:
    question = input("Soru sor (Çıkmak için exit yazın): ")
    if question.lower() == "exit":
        break
    result = chain.invoke({"question": question})
    print(f"\nCevap: {result}")