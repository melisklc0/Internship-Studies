# Langchain
Bu notlar *langchain-crash-course* projesi üzerinden konu çalışırken almış olduğum notlar.

## 1. Chat Modelleri
Öncelikle bazı kavramlara bakalım:

**System Message:** Modelin rolünü ve davranış biçimini belirleyen mesajdır. Bu mesaj, modelin nasıl yanıt vereceğini kontrol etmek için kullanılır.

**Human Message:** Kullanıcının modele gönderdiği sorudur veya istektir. Model bu mesajı temel alarak cevap üretir.

**AI Message:** Modelin kullanıcıya verdiği yanıt mesajıdır. İnsan mesajına karşılık olarak oluşturulur ve sohbetin devamını sağlar.

----

Şimdi basit bir uygulama oluşturalım.
Öncelikle gerekli importları yapalım.
```bash
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
```
Sonrasında env'imizi açalım ve modelimizi oluşturalım.
```bash
load_dotenv()
model = ChatOpenAI(model="gpt-4o")
```
Full result tüm sonucu verecektir. Content only ise yalnızca asıl cevabı verecek.
```bash
result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)
```
Çıktı:
```bash
Full result:
content='81 divided by 9 is 9.' response_metadata={'token_usage': {'completion_tokens': 9, 'prompt_tokens': 16, 'total_tokens': 25, 'prompt_tokens_details': {'cached_tokens': 0, 'audio_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 0, 'audio_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}}, 'model_name': 'gpt-4o', 'system_fingerprint': 'fp_a288987b44', 'finish_reason': 'stop', 'logprobs': None} id='run-5fe56fe9-8f19-43c2-beb2-549138ccf915-0' usage_metadata={'input_tokens': 16, 'output_tokens': 9, 'total_tokens': 25}
Content only:
81 divided by 9 is 9.
```
----
Şimdi basit bir konuşma yapalım.
Gerekli importları yapalım ve modeli oluşturalım.
```bash
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()
model = ChatOpenAI(model="gpt-4o")
```
Sistem mesajı her zaman insan mesajından önce gelir.
```bash
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
]

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")
```
Benzer şekilde,
```bash
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
    AIMessage(content="81 divided by 9 is 9."),
    HumanMessage(content="What is 10 times 5?"),
]

result = model.invoke(messages)
print(f"Answer from AI: {result.content}")
```
Başka modellerle de çalışabiliriz. Örneğin:
```bash
model = ChatAnthropic(model="claude-3-opus-20240229")

result = model.invoke(messages)
print(f"Answer from Anthropic: {result.content}")
```
```bash
model2 = ChatGoogleGenerativeAI(model2="gemini-1.5-flash")

result = model2.invoke(messages)
print(f"Answer from Google: {result.content}")
```
----
Şimdi gerçek zamanlı bir konuşma yapalım. Sohbeti depolaması için bir chat history'ye ihtiyacımız var. Bunu oluşturalım ve sistem mesajını listeye ekleyelim.
```bash
load_dotenv()
model = ChatOpenAI(model="gpt-4o")

chat_history = []

system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message) 
```
Konuşmaya devam etmek için bir while loop ekleyelim.
```bash
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))  # Kullanıcı mesajını ekle


    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))  # AI mesajını ekle

    print(f"AI: {response}")
```
Daha sonrasında konuşmayı ekrana yazdıralım.
```bash
print("---- Message History ----")
print(chat_history)
```
----
Şimdi mesajları Google Firestore üzerine kaydedeceğiz.
Gerekli login ve yetkilendirme işlemlerimizi yaptıktan ve yeni bir proje açtıktan sonra bu projeyi kod içerisine eklememiz gerekiyor.
```bash
load_dotenv()

PROJECT_ID = "project-e5b68"
SESSION_ID = "user1_session_new"
COLLECTION_NAME = "chat_history
```

Daha sonrasında firestore client ini ve chathistory i kaydedebilmesi için tanımlamaları yapıyoruz.
```bash
print("Initializing Firestore Client...")
client = firestore.Client(project=PROJECT_ID)

# Initialize Firestore Chat Message History
print("Initializing Firestore Chat Message History...")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)
print("Chat History Initialized.")
print("Current Chat History:", chat_history.messages)
```

Modeli ekleyelim.
```bash
model = ChatOpenAI()
print("Start chatting with the AI. Type 'exit' to quit.")
```

Yine while döngüsü ile gerçek zamanlı konuşma sağlayalım ama bu sefer *chat_history.add_user_message()* ile konuşmayı listeye ekleyip kaydedeceğiz.

```bash
while True:
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break

    chat_history.add_user_message(human_input)

    ai_response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)

    print(f"AI: {ai_response.content}")
```
Böylece model konuşmaları hatırlayacak ve önceki mesajlarla ilgili bir soru sorduğumuzda cevap verebilecek.

## 2. Prompt Şablonları
Direkt şablon üzerinden kullanabiliriz.
Öncelikle gerekli importlar:
```bash
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
```

İlk olarak tek placeholder kullanalım:
```bash
template = "Tell me a joke about {topic}."
prompt_template = ChatPromptTemplate.from_template(template)
```
Şablonu oluşturduk. Daha sonra bunu kullanmak istersek şu şekilde bir kullanımı var:
```bash
print("-----Prompt from Template-----")
prompt = prompt_template.invoke({"topic": "cats"})
print(prompt)
```
-----
Şimdi iki placeholder kullanalım:
```bash
template_multiple = """You are a helpful assistant.
Human: Tell me a {adjective} story about a {animal}.
Assistant:"""
prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
```

Yine bunu kullanmak için de:
```bash
print("\n----- Prompt with Multiple Placeholders -----\n")
prompt = prompt_multiple.invoke({"adjective": "funny", "animal": "panda"})
print(prompt)
```
-----

Sistem ve insan mesajını bir arada içeren bir şablon oluşturalım:
```bash
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]
prompt_template = ChatPromptTemplate.from_messages(messages)
```

Kullanalım:
``` bash
print("\n----- Prompt with System and Human Messages (Tuple) -----\n")
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
print(prompt)
```

Şimdi bu şablonu kullanmak için bazı dikkat etmemiz gereken noktalar var. Eğer bu şekilde *HumanMessage()* fonksiyonunu kullanmak istersek, içeriye placeholder koyulmaması gerekiyor.
```bash
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    HumanMessage(content="Tell me 3 jokes."),
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers"})
print(prompt)
```

Eğer koyulursa bu kod hata verir ve çalışmaz:
```bash
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    HumanMessage(content="Tell me {joke_count} jokes."),
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
print(prompt)
```

Bu şablonları modeller ile kullanalım. *print* kısmı yerine şablonu modele göndereceğiz:
```bash
load_dotenv()
model = ChatOpenAI(model="gpt-4o")

result = model.invoke(prompt)
print(result.content)
```

-----
## 3. Zincirler



```bash

```

```bash

```

```bash

```


