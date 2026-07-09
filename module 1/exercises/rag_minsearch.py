from rag_helper import RAGBase
from ingest import load_faq_data, build_index

import os
from dotenv import load_dotenv
load_dotenv()


from openai import OpenAI
openai_client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

model = 'openai/gpt-oss-20b'
documents = load_faq_data()
index = build_index(documents)

assistant = RAGBase(
    index, 
    openai_client, 
    model=model
)

response = assistant.rag('I just discovered the course, can I still join?')
print(response.output_text)