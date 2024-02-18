import openai
import json
import os
import string
import logging

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

def augment_prompt(self, query):
    query1 = json.dumps(str(query))
    results = self.vectorstore.similarity_search(query1, k=3)
    source_knowledge = "\n".join([x.page_content for x in results])
    augmented_prompt = f"""Using the contexts below, answer the query.

    Contexts:
    {source_knowledge}

    Query: {query1}"""
    return augmented_prompt

def run_chat(self, query):
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content=f"Hi AI, {query}"),
        AIMessage(content="I'm great thank you. How can I help you?"),
    ]

    augmented_prompt = self.augment_prompt(query)

    prompt = HumanMessage(content=augmented_prompt)
    messages.append(prompt)

    res = self.chat(messages)
    return res.content