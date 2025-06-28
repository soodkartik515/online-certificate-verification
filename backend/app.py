from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can connect
app.config['UPLOAD_FOLDER'] = 'uploads'

# Root route (so that '/' doesn't return 404)
@app.route('/')
def home():
    return "Welcome to the Certificate Verification API"

# Certificate verification endpoint
@app.route('/verify', methods=['POST'])
def verify_certificate():
    data = request.get_json()  # Get JSON from request body
    cert_id = data.get('certificate_id')  # Match what your frontend sends

    # Simulated certificate verification
    if cert_id == 'CERT12345':
        return jsonify({
            'status': 'found',
            'data': {
                'name': 'John Doe',
                'course': 'Python Programming',
                'date': '2024-05-10'
            }
        })

    return jsonify({'status': 'not_found'}), 404

# Run the app on the correct port for Render
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
