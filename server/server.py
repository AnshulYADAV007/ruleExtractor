from flask import Flask, request
from flask_cors import CORS, cross_origin
import openai
import markdown
import json

openai.api_key = "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"

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

system_messages_1 = {"droolDev": 'You are a Drools Developer',
                     "analyst": 'You are a Servicing Compliance Analyst'}


@app.route('/', methods=['POST'])
def result():
    print(request.data)
    system_message_2 = "Extract rules in a tabular format with following columns:"
    data = json.loads(request.data)
    for element in data["columns"][:-1]:
        system_message_2 += " " + element + ","
    system_message_2 += " " + data["columns"][-1]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
                "content": system_messages_1[data["role"]]},
            {"role": "assistant", "content": "Sure"},
            {"role": "user", "content": "I will provide you with a text and you have to extract rules that can be programmed to identify either loans that do not meet the guidelines, or an activity to be performed by the servicer to ensure compliance with the guidelines."},
            {"role": "system", "content": system_message_2},
            {"role": "assistant", "content": "Please provide me the text"},
            {"role": "user", "content": data["text"]}
        ])
    html = markdown.markdown(
        response.choices[0].message.content, extensions=['tables'])
    return html


if __name__ == '__main__':
    app.run()
