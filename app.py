from flask import Flask, render_template
app = Flask(__name__, template_folder="bootstrap_templates", static_folder="bootstrap_themes")

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("contact.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/bootstrap')
def bootstrap():
    return render_template("bootstrap.html")

if __name__ == '__main__':
    app.run(debug=True)