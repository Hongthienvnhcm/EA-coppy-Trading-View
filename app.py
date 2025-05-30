# EA-coppy-Trading-View 
from flask import Flask, request

app = Flask(__name__)

@app.route('/signal', methods=['POST'])
def signal():
    data = request.json
    print("✅ Received signal:", data)

    # Ví dụ xử lý logic:
    symbol = data.get("symbol")
    action = data.get("action")

    # TODO: Gửi tín hiệu tới EA qua socket/file tại đây

    return {"status": "success"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
