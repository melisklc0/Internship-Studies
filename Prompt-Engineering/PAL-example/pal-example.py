import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

question = "Bugün 27 Şubat 2023. Tam 25 yıl önce doğmuştum. Doğduğum tarih MM/DD/YYYY formatında neydi?"

DATE_UNDERSTANDING_PROMPT = """
# S: 2015 yılına 36 saat kaldı. Bir hafta sonra günün tarihi MM/DD/YYYY formatında ne olacak?
# Eğer 2015 yılına 36 saat kaldıysa, bugün 36 saat öncesidir.
today = datetime(2015, 1, 1) - relativedelta(hours=36)
# Bir hafta sonrası,
one_week_from_today = today + relativedelta(weeks=1)
# Cevap %m/%d/%Y formatında
one_week_from_today.strftime('%m/%d/%Y')
# S: 2019'un ilk günü bir Salı’dır ve bugün 2019'un ilk Pazartesi'si. Bugünün tarihi MM/DD/YYYY formatında ne?
# Eğer 2019’un ilk günü bir Salı ve bugün 2019’un ilk Pazartesi’si ise, bu, bugünün 6 gün sonrası olduğu anlamına gelir.
today = datetime(2019, 1, 1) + relativedelta(days=6)
# Cevap %m/%d/%Y formatında
today.strftime('%m/%d/%Y')
# S: Konser 06/01/1943'te olması planlanıyordu, ancak bugüne bir gün ertelendi. 10 gün önceki tarih MM/DD/YYYY formatında neydi?
# Eğer konser 06/01/1943’te olması planlanıyor ama bir günlük gecikmeyle bugüne denk geldiyse, o zaman bugün bir gün sonrasıdır.
today = datetime(1943, 6, 1) + relativedelta(days=1)
# 10 gün önce,
ten_days_ago = today - relativedelta(days=10)
# Cevap %m/%d/%Y formatında
ten_days_ago.strftime('%m/%d/%Y')
# S: Bugün 4/19/1969. 24 saat sonra tarih MM/DD/YYYY formatında ne olacak?
# Bugün 4/19/1969.
today = datetime(1969, 4, 19)
# 24 saat sonra,
later = today + relativedelta(hours=24)
# Cevap %m/%d/%Y formatında
today.strftime('%m/%d/%Y')
# S: Jane bugünün 3/11/2002 olduğunu düşündü, ancak bugün aslında 12 Mart, yani 1 gün sonrası. 24 saat sonrası tarih MM/DD/YYYY formatında ne olacak?
# Eğer Jane bugünün 3/11/2002 olduğunu düşündü, ancak bugün aslında 12 Mart ise, o zaman bugün 3/12/2002’dir.
today = datetime(2002, 3, 12)
# 24 saat sonra,
later = today + relativedelta(hours=24)
# Cevap %m/%d/%Y formatında
later.strftime('%m/%d/%Y')
# S: Jane, 2001'in Şubat ayının son gününde doğdu. Bugün onun 16. yaş günü. Dünkünün tarihi MM/DD/YYYY formatında neydi?
# Eğer Jane 2001'in Şubat ayının son gününde doğdu ve bugün onun 16. yaşı ise, o zaman bugün 16 yıl sonrasıdır.
today = datetime(2001, 2, 28) + relativedelta(years=16)
# Dün,
yesterday = today - relativedelta(days=1)
# Cevap %m/%d/%Y formatında
yesterday.strftime('%m/%d/%Y')
# S: {question}
""".format(question=question)

# Modeli çağır
llm_out = llm.invoke(DATE_UNDERSTANDING_PROMPT)

print("Model cevabı:")
print(llm_out.content)
