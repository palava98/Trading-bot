from flask import Flask, jsonify, request
from trading_engine import run_trading_bot
app = Flask(__name__)

@app.route('/api/get_data')
def get_data():
    return jsonify({"message": "Hello, World!"})


@app.route('/trade', methods=['POST'])
def trade():
    data = request.json
    symbols = data.get('symbols', ['EURUSD', 'USDJPY', 'US30', 'BTCUSD', 'XAUUSD'])
    lot_size = data.get('lot_size', 0.1)
    run_trading_bot(symbols, lot_size)
    return jsonify({"status": "Trading executed"}), 200

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "Bot is running"}), 200

if __name__ == "__main__":
    app.run(debug=True)