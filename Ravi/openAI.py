import openai
openai.api_key = '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'
#api_key = "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"
chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":str(input("ask anything...:"))}])
print(chat_completion.choices[0].message.content)