from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():

    return jsonify({"status": "🖖 Hey! This is Pablo"}), 200

if __name__ == '__main__':
    app.run(debug=True)
