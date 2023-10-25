const express = require('express');
var kiteconnect = require("kiteconnect").KiteConnect;
const WebSocket = require('ws');

const app = express();
const apiKey = 'apikey';
const apiSecret = 'apisecret';
const redirectUri = 'http://localhost:8080/callback';



// Access Token obtained from the Kite Connect API authentication process
let accessToken;

// Define the WebSocket URL for Kite Connect
let wsUrl;

var kc = new kiteconnect({
    api_key: apiKey,
  });

app.get('/', (req, res) => {
  // Step 1: Manually generate the login URL
  const loginURL = `https://kite.trade/connect/login?api_key=${apiKey}&v=3&redirect=${redirectUri}`;
  res.redirect(loginURL);
});

app.get('/callback', (req, res) => {
  // Step 2: Capture the request token from the query string
  const requestToken = req.query.request_token;
  console.log('requestToken:', requestToken);
  // Step 3: Exchange the request token for an access token
  kc.generateSession(requestToken, apiSecret)
    .then(response => {
      accessToken = response.access_token;

      // Define the WebSocket URL with the access token
      //wsUrl = `wss://websocket.kite.trade/feeds?access_token=${accessToken}`;

      // Open the WebSocket connection
      //openWebSocketConnection();

      // Print the access token to the console
      console.log('Access Token:', accessToken);

      // Now you have the access token and can use it to make authenticated API requests.
      res.send(`Access Token: ${accessToken}`);
    })
    .catch(error => {
      res.send(`Error: ${error.message}`);
    });
});


function openWebSocketConnection() {
  const ws = new WebSocket(wsUrl, { rejectUnauthorized: false });

  ws.on('open', () => {
    console.log('WebSocket connection is open.');

    // Subscribe to Nifty data
    const niftyInstrumentToken = '256265'; // The instrument token for Nifty
    ws.send(JSON.stringify({
      a: 'subscribe',
      v: [niftyInstrumentToken],
    }));
  });

  ws.on('message', (data) => {
    // Handle real-time data received from the WebSocket
    console.log('Received data:', data);
  });

  ws.on('error', (error) => {
    console.error('WebSocket error:', error);
  });

  ws.on('close', (code, reason) => {
    console.log('WebSocket connection closed:', code, reason);
  });
}

app.listen(8080, () => {
  console.log('Server is running on http://localhost:8080');
});
