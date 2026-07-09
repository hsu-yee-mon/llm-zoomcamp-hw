
INSTRUCTIONS = """
You're a course teaching assistant.
Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.        
"""

PROMPT_TEMPLATE = '''
QUESTION  {question}

Context : 
{context}
'''.strip()

class RAGBase:

    def __init__(
            self,
            index,
            llm_client,
            instructions = INSTRUCTIONS,
            prompt_template = PROMPT_TEMPLATE,
            model = "gpt-3.5-turbo"):
        
        self.index = index
        self.llm_client = llm_client
        self.instructions = instructions
        self.prompt_template = prompt_template
        self.model = model

    def build_context(self, search_results):
        lines = []
        for doc in search_results:
            lines.append(doc['section'])
            lines.append(f"Q: {doc['question']}")
            lines.append(f"A: {doc['answer']}")
        return "\n".join(lines)
    
    
    def build_prompt(self, question,search_results):
        # 1. Build the context from the search results
        context = self.build_context(search_results)

        # 2. Build the prompt for the LLM
        prompt = self.prompt_template.format(
            question=question,
            context=context
        )

        return prompt
    
    def llm(self, prompt):

        input_messaeges = [
            {"role": "system", "content": self.instructions},
            {"role": "user", "content": prompt}
        ]

        # Call the LLM client with the formatted prompt
        response = self.llm_client.responses.create(
            input=input_messaeges,
            model=self.model
        )

        return response.output_text

    def llm_agent(self, prompt):
        input_messaeges = [
            {"role": "system", "content": self.instructions},
            {"role": "user", "content": prompt}
        ]

        # Define Search Tool
        search_tool = {
            "type" : "function",
            "name" : "search",
            "description" : "Search the FAQ database for relevant information",
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "query" : {
                        "type" : "string",
                        "description" : "The search query text to look up in the courese FAQ database"
                    },
                    "course" : {
                        "type" : "string",
                        "description" : "The course name"
                    },
                    "num_results" : {
                        "type" : "integer",
                        "description" : "The number of search results to return"
                    }
                },
                "required" : ["query"],
                "additionalProperties" : False
            }
        }
        # Call the LLM client with the formatted prompt
        response = self.llm_client.chat.completions.create(
            input=input_messaeges,
            model=self.model,
            tools=[search_tool],
        )

        return response.output

    def search(self, query, course = "llm-zoomcamp", num_results=3):
        boost_dict={'question': 2.0, 'section': 0.5}
        filter_dict={'course': course}
        search_results = self.index.search(
            query, 
            num_results=num_results, 
            boost_dict=boost_dict, 
            filter_dict=filter_dict)
        return search_results
    
    def rag(self, question, course = "llm-zoomcamp"):
        search_results = self.search(question, course, num_results=5)
        prompt = self.build_prompt(question, search_results)
        answer = self.llm(prompt)
        return answer
    