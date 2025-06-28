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
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

