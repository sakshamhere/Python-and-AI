from transformers import pipeline 

pipe = pipeline("text-generation", model="Qwen/Qwen2.5-1.5B-Instruct")
messages = [
    {"role": "user", "content": "Who are you?"},
]

response = pipe(messages)

print(response[0]['generated_text'][len(messages):], len(messages))



