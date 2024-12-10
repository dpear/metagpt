import pandas as pd
import numpy as np
from openai import OpenAI

MODEL = 'gpt-3.5-turbo'

def ask(question, client):
    """
    inputs:
    question: str, prompt for chatgpt
    client: a client defined from OpenAI with API key specified

    returns: None
    Only prints the response.

    example:
    client = OpenAI(api_key="YOUR_API_KEY")

    ask(question="what is a bagel", client=client)

    """

    response = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": question, # Place question here
        }],
        model = MODEL,
    )

    out = response.choices[0].message.content
    print(out)