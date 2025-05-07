from flask import Flask, jsonify
from flask_talisman import Talisman
import os

app = Flask(__name__)

# Only apply Talisman in production
if os.getenv('FLASK_ENV') == 'production':
    Talisman(app,
        force_https=True,
        strict_transport_security=True,
        session_cookie_secure=True,
        content_security_policy={
            'default-src': "'self'",
            'img-src': "'self' data: https:",
            'script-src': "'self' 'unsafe-inline' 'unsafe-eval'",
            'style-src': "'self' 'unsafe-inline'",
        }
    )
else:
    # Development mode - minimal security headers
    Talisman(app,
        force_https=False,
        content_security_policy=None
    )

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to the API',
        'status': 'healthy'
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'version': os.getenv('APP_VERSION', '1.0.0')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
