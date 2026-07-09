# 1. Load the FAQ data from the json file
import requests
from minsearch import Index

def load_faq_data():
    
    docs_url = 'https://datatalks.club/faq/json/courses.json'
    courses_data_raw = requests.get(docs_url).json()
    faq_data = []

    url_prefix = 'https://datatalks.club/faq'

    for course in courses_data_raw:
        
        course_path = course['path']

        course_response = requests.get(url_prefix + course_path)
        course_response.raise_for_status()

        course_data = course_response.json()

        faq_data.extend(course_data)

    return faq_data


# 2. Create an index using minsearch using the loaded FAQ data
# This is for In-Memory Search
def build_index(faq_data):
    index = Index(
        text_fields=['question', 'answer'],
        keyword_fields=['course']
    )
    index.fit(faq_data)

    return index
