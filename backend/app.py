
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/verify', methods=['POST'])
def verify_certificate():
    cert_id = request.form.get('cert_id')
    # Simulated certificate check
    if cert_id == 'CERT12345':
        return jsonify({'status': 'valid', 'name': 'John Doe', 'course': 'Python Programming', 'date': '2024-05-10'})
    return jsonify({'status': 'invalid'}), 404

if __name__ == '__main__':
    app.run(debug=True)
