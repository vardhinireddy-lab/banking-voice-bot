from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock bank database
accounts = {
    "savings": 25000,
    "current": 85000,
    "credit": 15000
}

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    intent = data['queryResult']['intent']['displayName']
    params = data['queryResult']['parameters']

    if intent == 'check.balance':
        account = params.get('account-type', 'savings')
        balance = accounts.get(account, 0)
        reply = f"Your {account} account balance is ₹{balance}."

    elif intent == 'block.card':
        reply = "Your card has been blocked. Confirmation sent to your mobile."

    elif intent == 'transfer.money':
        reply = "Please confirm amount and recipient to proceed with transfer."

    elif intent == 'find.atm':
        reply = "Nearest ATM is at MG Road, 0.5km away. Open 24/7."

    else:
        reply = "I can help with balance, card blocking, transfers or ATM locations."

    return jsonify({"fulfillmentText": reply})

if __name__ == '__main__':
    app.run(debug=True, port=5000) 
