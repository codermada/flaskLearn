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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)