from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser  


load_dotenv()

OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"

llm = ChatOpenAI(
model="mistralai/mistral-small-3.2-24b-instruct:free",
openai_api_key=os.getenv("OPENROUTER_API_KEY"),
openai_api_base=OPENROUTER_API_BASE,
temperature=0.7
)

context = """
Leonardo da Vinci was an Italian polymath of the Renaissance period.
He was born in 1452 and is widely known for his works such as the Mona Lisa and The Last Supper.
He was also an engineer, inventor, and scientist.
"""

# Prompt tanımı
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