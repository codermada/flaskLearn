from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.shell_context_processor
def make_shell_context():
    return {"test": "Hello"}

if __name__ == '__main__':
    app.run(debug=True)

# command: flask shell