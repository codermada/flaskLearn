from flask import Flask, render_template
app = Flask(__name__, template_folder='jinja_templates')

@app.route('/')
def hello():
    return render_template('index.html')


class Obj:
    def somemethod(self):
        return "Jinja is rendering"


@app.route('/test')
def test():
    mydict = {'key': 'value', 'key2': 'value 2'}
    mylist = [1, 2, 3, "Yolo"]
    myintvar = 2
    myobj = Obj()
    return render_template('test.html', mydict=mydict, mylist=mylist, myintvar=myintvar, myobj=myobj)

@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', name=name)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)