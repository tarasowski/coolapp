import pytest
from flask import Flask

def test_health_check():
    app = Flask(__name__)

    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({"status": "OK"}), 200

    with app.test_client() as client:
        response = client.get('/health')
        assert response.status_code == 200
        assert response.get_json() == {"status": "OK"}
