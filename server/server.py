from flask import Flask, request
from flask_cors import CORS, cross_origin
import openai
import markdown
import json

openai.api_key = "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"

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['POST'])
def result():
    data = json.loads(request.data)
    html = ""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content":  'You are a Servicing Compliance Analyst'},
                {"role": "assistant", "content": "Sure"},
                {"role": "user", "content": "I will provide you with a text and you have to extract rules that can be programmed to identify either loans that do not meet the guidelines, or an activity to be performed by the servicer to ensure compliance with the guidelines."},
                {"role": "system", "content": "Extract rules in a tabular format with 3 columns - name, text snippet, and extracted rule from the text provided."},
                {"role": "assistant", "content": "Please provide me the text"},
                {"role": "user", "content": data["text"]}
            ])
        html = markdown.markdown(
            response.choices[0].message.content, extensions=['tables'])
    except Exception as e:
        print(e)
        return e.__str__()
    else:
        return html


if __name__ == '__main__':
    app.run()
