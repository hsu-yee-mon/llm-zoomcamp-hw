import sys , os

from dotenv import load_dotenv
from openai import OpenAI

from exercise.ingest import load_faq_data, build_index
from exercise.rag_helper import RAGBase
from exercise.metrics import RAGWithMetrics

from exercise.db_save import save_conversation

def create_assistant():
    load_dotenv()

    documents = load_faq_data()
    index = build_index(documents)

    openai_client = OpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1"
    )
    llm_model = "openai/gpt-oss-20b"

    return RAGWithMetrics(
        index=index,
        llm_client=openai_client,
        model=llm_model
    )


if __name__ == "__main__":
    assistant = create_assistant()

    query = "How do I join the course?"
    if len(sys.argv) > 1:
        query = sys.argv[1]

    answer = assistant.rag(query)
    save_conversation(assistant.last_call, query, "llm-zoomcamp")
    print(answer)
    

