from flask import Flask, request, session, g, make_response, redirect, abort
import os
from is_valid_url import is_valid_url
app = Flask(__name__)
# Set the secret key for session management
app.secret_key = os.environ.get('SECRET_KEY', 'supersecretkey')

@app.before_request
def before_request():
    g.user = session.get('user', 'Guest')  # Set a default user in the global context

# after_request function to add headers to the response
# @app.after_request
# def add_header(response):
#     # Add headers to the response to prevent caching
#     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
#     response.headers['Pragma'] = 'no-cache'
#     response.headers['Expires'] = '-1'
#     # Add a custom header to indicate the application version
#     response.headers["X-App-Version"] = "1.0"
#     # Add security headers to the response
#     response.headers["X-Content-Type-Options"] = "nosniff"
#     response.headers["X-Frame-Options"] = "DENY"
#     # Add CORS headers to allow cross-origin requests (for development purposes)
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     return response

@app.route('/')
def hello():
    print(f"g.user: {g.get('user', 'No user in g')}")
    return 'Hello World!', 201 # custom status code 201 (Created)

@app.route('/test_make_response')
def test_make_response():
    # Create a custom response using make_response
    response = make_response('This is a custom response', 202)  # custom status code 202 (Accepted)
    response.headers['X-Custom-Header'] = 'CustomValue'
    response.set_cookie('my_cookie', 'cookie_value')  # Set a cookie in the response
    return response

@app.route('/name/<name>')
def hello_name(name):
    return f'Hello {name}!'

@app.route('/square/<int:number>')
def square(number):
    return f'The square of {number} is {number ** 2}.'

@app.route('/height/<float:height>')
def height(height):
    return f'Your height is {height} meters.'

@app.route('/name')
def name():
    return f'Hello {request.args.get("name", "Name")}!'

@app.route('/request-details')
def request_details():
    return {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "args": request.args.to_dict(),
        "form": request.form.to_dict(),
        "json": request.get_json(silent=True),
    }

@app.route('/set-session/<key>/<value>')
def set_session(key, value):
    session[key] = value
    return f'Session key {key} set to {value}.'

@app.route('/get-session/<key>')
def get_session(key):
    value = session.get(key, None)
    if value is None:
        return f'Session key {key} not found.'
    return f'Session key {key} has value {value}.'

@app.route('/clear-session')
def clear_session():
    session.clear()
    return 'Session cleared.'

@app.route('/redirect-example')
def redirect_example():
    return redirect('/')

@app.route('/to')
def to():
    url = request.args.get('url', 'https://www.google.com')
    if is_valid_url(url):
        return redirect(url)
    else:
        abort(400, description="Invalid URL provided.")

if __name__ == '__main__':
    app.run(debug=True)