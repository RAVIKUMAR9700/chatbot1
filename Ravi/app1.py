import openai

def chatbot_response(msg):
    openai.api_key = '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'
    # api_key = "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"
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                   messages=[{"role": "user", "content": str(msg)}])
    # print(chat_completion.choices[0].message.content)
    result = chat_completion.choices[0].message.content
    print(result)
    return str(result)




from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("testChat.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    #print(userText)
    ab = chatbot_response(userText)
    #print(ab)
    return ab


if __name__ == "__main__":
    app.run()