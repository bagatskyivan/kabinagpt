from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = 'ваш API ключ'

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    response = openai.Completion.create(
        engine="davinci",
        prompt=question,
        max_tokens=50
    )
    answer = response.choices[0].text.strip()
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
