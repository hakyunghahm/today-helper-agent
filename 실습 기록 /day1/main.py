from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() # .env 파일을 읽어서 환경변수로 등록해줌 
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # 클라이언트 객체 OpenAI에서 내 계정 인증 

response = client.chat.completions.create( # GPT 모델에게 채팅 메시지 형태로 요청 보냄 
    model="gpt-3.5-turbo",  
    messages=[
        {"role": "system", "content": "You are a helpful assistant."}, # "system": GPT에게 "너는 어떤 역할이다"라고 미리 정의
        {"role": "user", "content": "오늘 뭐할까?"}, # "user": 사용자 질문
    ]
)

print(response.choices[0].message.content) # [0]을 써서 첫 번째만 출력
