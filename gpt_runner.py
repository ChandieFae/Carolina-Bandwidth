## models/gpt_runner.py
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def run_gpt(input_text: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant for Carolina Bandwidth."},
                {"role": "user", "content": input_text}
            ]
        )
        output = response['choices'][0]['message']['content']
        return {"output": output}
    except Exception as e:
        return {"error": str(e)}

