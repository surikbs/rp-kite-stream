import json
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import alpaca
from alpaca.data.live.option import *
from alpaca.data.historical.option import *
from alpaca.data.requests import *
from alpaca.trading.client import *
from alpaca.trading.stream import *
from alpaca.trading.requests import *
from alpaca.trading.enums import *
from alpaca.common.exceptions import APIError


# Please change the following to your own PAPER api key and secret
# You can get them from https://alpaca.markets/
TRADE_API_KEY="x"
TRADE_API_SECRET="x"

#### We use paper environment for this example ####
PAPER=True # Please do not modify this. This example is for paper trading only.
####

# Below are the variables for development this documents
# Please do not change these variables
TRADE_API_URL=None
TRADE_API_WSS=None
DATA_API_URL=None
OPTION_STREAM_DATA_WSS=None

api_key = TRADE_API_KEY
secret_key = TRADE_API_SECRET
paper = PAPER
trade_api_url = TRADE_API_URL


print(alpaca.__version__)

# setup clients
trade_client = TradingClient(api_key=api_key, secret_key=secret_key, paper=paper, url_override=trade_api_url)
acct = trade_client.get_account()

print(acct)