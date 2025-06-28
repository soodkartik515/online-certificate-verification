from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample certificate data
CERTIFICATE_DB = {
    "CERT12345": {
        "name": "Amit Sharma",
        "course": "Python Programming",
        "date": "2024-05-25",
        "status": "Valid"
    },
    "CERT98765": {
        "name": "Riya Verma",
        "course": "Data Science",
        "date": "2024-06-10",
        "status": "Valid"
    }
}

@app.route('/verify', methods=['POST'])
def verify_certificate():
    cert_id = request.form.get('cert_id')

    if cert_id in CERTIFICATE_DB:
        return jsonify({
            "success": True,
            "message": "Certificate found.",
            "data": CERTIFICATE_DB[cert_id]
        })
    else:
        return jsonify({
            "success": False,
            "message": "Certificate not found.",
            "data": None
        }), 404

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's assigned port
    app.run(host='0.0.0.0', port=port)
