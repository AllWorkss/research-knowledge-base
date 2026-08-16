"""
=============================================================================
ZenithAlgo Pro - Backend API Server (Upstox & ICICI Breeze Bridge)
=============================================================================
Runs locally on http://localhost:5000 to bridge web UI button clicks to live broker APIs.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import json
import yfinance as yf
from upstox_algo_bot import UpstoxBot
from icici_breeze_algo_bot import ICICIBreezeBot

app = Flask(__name__)
CORS(app)

# Global Store for Broker Credentials and State
broker_config = {
    'upstox': {'instance': None, 'status': 'Disconnected'},
    'icici': {'instance': None, 'status': 'Disconnected'}
}

# Dad's Safety Guard State
current_daily_loss = 0.0

# Load config
with open('config.json', 'r') as f:
    config_data = json.load(f)
MAX_DAILY_LOSS = config_data.get('risk_settings', {}).get('max_daily_loss_limit_inr', 10000)

@app.route('/')
def home():
    return jsonify({"status": "ZenithAlgo Backend API Gateway Running", "version": "2.0"})

@app.route('/api/connect_broker', methods=['POST'])
def connect_broker():
    data = request.json
    broker = data.get('broker')
    
    if broker == 'Upstox':
        access_token = data.get('access_token', '')
        try:
            bot = UpstoxBot(access_token)
            broker_config['upstox']['instance'] = bot
            broker_config['upstox']['status'] = 'Connected'
            return jsonify({"status": "success", "message": "Upstox API v2 Connected Successfully!"})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 400
            
    elif broker == 'ICICI Direct Breeze':
        app_key = data.get('app_key', '')
        secret_key = data.get('secret_key', '')
        session_token = data.get('session_token', '')
        try:
            bot = ICICIBreezeBot(app_key, secret_key, session_token)
            broker_config['icici']['instance'] = bot
            broker_config['icici']['status'] = 'Connected'
            return jsonify({"status": "success", "message": "ICICI Direct Breeze API Connected Successfully!"})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 400
    
    return jsonify({"status": "error", "message": "Invalid Broker"}), 400

@app.route('/api/execute_order', methods=['POST'])
def execute_order():
    global current_daily_loss
    data = request.json
    symbol = data.get('symbol', 'NIFTY')
    action = data.get('action', 'BUY')
    qty = data.get('quantity', 50)
    price = data.get('price', 0.0)
    broker = data.get('broker', 'Upstox API v2')

    print(f"[LIVE EXECUTION] {action} {qty} Qty of {symbol} at ₹{price} via {broker}")

    # Dad's Safety Guard Check
    if current_daily_loss >= MAX_DAILY_LOSS:
        print("[SAFETY GUARD TRIGGERED] Max daily loss exceeded. Order BLOCKED.")
        return jsonify({
            "status": "error",
            "message": f"Dad's Safety Guard: Daily loss limit of ₹{MAX_DAILY_LOSS} exceeded! Trade blocked."
        }), 403

    order_id = None
    
    try:
        if 'Upstox' in broker:
            bot = broker_config['upstox']['instance']
            if not bot:
                return jsonify({"status": "error", "message": "Upstox not connected!"}), 400
            order_id = bot.place_order(f'NSE_EQ|{symbol}', qty, price, action)
            
        elif 'ICICI' in broker:
            bot = broker_config['icici']['instance']
            if not bot:
                return jsonify({"status": "error", "message": "ICICI not connected!"}), 400
            order_id = bot.place_order(symbol, qty, price, action)
        else:
            return jsonify({"status": "error", "message": "Unknown broker"}), 400
            
        if order_id:
            return jsonify({
                "status": "success",
                "order_id": order_id,
                "message": f"Successfully placed {action} order for {qty} shares of {symbol} on {broker}!"
            })
        else:
            return jsonify({"status": "error", "message": "Broker API failed to place order."}), 500
            
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/market_data', methods=['GET'])
def market_data():
    symbol = request.args.get('symbol', 'NIFTY')
    # Map app symbols to yfinance symbols
    yf_symbol_map = {
        'NIFTY': '^NSEI',
        'BANKNIFTY': '^NSEBANK',
        'RELIANCE': 'RELIANCE.NS',
        'TCS': 'TCS.NS',
        'TATAMOTORS': 'TATAMOTORS.NS',
        'HDFCBANK': 'HDFCBANK.NS'
    }
    yf_sym = yf_symbol_map.get(symbol, '^NSEI')
    
    try:
        data = yf.download(tickers=yf_sym, period='5d', interval='5m')
        if data.empty:
            return jsonify({"status": "error", "message": "No data found."}), 404
        
        # Take the last 60 candles
        data = data.tail(60)
        
        candles = []
        for index, row in data.iterrows():
            candles.append({
                "time": index.isoformat(),
                "open": float(row['Open'].iloc[0]) if hasattr(row['Open'], 'iloc') else float(row['Open']),
                "high": float(row['High'].iloc[0]) if hasattr(row['High'], 'iloc') else float(row['High']),
                "low": float(row['Low'].iloc[0]) if hasattr(row['Low'], 'iloc') else float(row['Low']),
                "close": float(row['Close'].iloc[0]) if hasattr(row['Close'], 'iloc') else float(row['Close']),
                "volume": int(row['Volume'].iloc[0]) if hasattr(row['Volume'], 'iloc') else int(row['Volume'])
            })
        
        return jsonify({"status": "success", "candles": candles})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    print("==================================================")
    print("   ZenithAlgo Pro Backend API Gateway Started     ")
    print("   Listening on http://localhost:5000             ")
    print("==================================================")
    app.run(host='0.0.0.0', port=5000, debug=False)
