from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/verify', methods=['POST'])
def verify_certificate():
    data = request.get_json()
    cert_id = data.get('certificate_id')
    if cert_id == 'CERT12345':
        return jsonify({
            'status': 'found',
            'data': {
                'name': 'John Doe',
                'course': 'Python Programming',
                'date': '2024-05-10'
            }
        })
    return jsonify({'status': 'not found'}), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
