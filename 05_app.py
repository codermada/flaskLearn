from flask import Flask, render_template, request
app = Flask(__name__)
from flask_cors import CORS

CORS(app)

@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        data = request.get_json()
        content = data.get('content', '')
        # Process the content as needed
        print(f"Received content: {content}")
        return {'message': 'Content received', 'content': content}, 200
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)