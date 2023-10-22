from flask import Flask, request, redirect
from kiteconnect import KiteConnect

# Replace with your Zerodha API key and API secret
api_key = 'your_api_key'
api_secret = 'your_api_secret'

# Your specified redirect URL (must match the one in your Zerodha developer app settings)
redirect_url = 'http://localhost:5000/z/callback'

# Initialize Flask app
app = Flask(__name__)

# Initiali\ze KiteConnect client
kite = KiteConnect(api_key=api_key)

@app.route('/')
def index():
    # Redirect the user to the Zerodha login page for authorization
    login_url = kite.login_url(redirect_url)
    return redirect(login_url)

@app.route('/z/callback')
def callback():
    # Obtain the request_token from the URL parameters
    request_token = request.args.get('request_token')
    
    # Exchange the request_token for an access_token
    data = kite.generate_session(request_token, api_secret=api_secret)
    access_token = data['access_token']

    # Now you have the access_token, which you can use for API requests
    return f'Access Token: {access_token}'

if __name__ == '__main__':
    app.run(debug=True)
