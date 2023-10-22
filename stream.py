from flask import Flask, request, redirect
from kiteconnect import KiteConnect

# Replace with your Zerodha API key and API secret
api_key = '123'
api_secret = '123'

# Your specified redirect URL (must match the one in your Zerodha developer app settings)
redirect_url = 'http://localhost:8080/apis/broker/login/zerodha'

# Initialize Flask app
app = Flask(__name__)

# Initialize KiteConnect client
kite = KiteConnect(api_key=api_key)
@app.route('/')
def index():
    # Build the Zerodha login URL with the redirect URL
    login_url = f"https://kite.zerodha.com/connect/login?api_key={api_key}&v=3&redirect_url={redirect_url}"
    return redirect(login_url)

@app.route('/apis/broker/login/zerodha')
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