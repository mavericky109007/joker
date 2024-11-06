from flask import Flask, request, jsonify
import jwt
import os
from tiktok_auth import TikTokAuthClient

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

tiktok_client = TikTokAuthClient(
    client_key=os.environ.get('TIKTOK_CLIENT_KEY'),
    client_secret=os.environ.get('TIKTOK_CLIENT_SECRET')
)

@app.route('/auth/login', methods=['POST'])
def login():
    # TikTok OAuth flow
    authorization_code = request.json.get('code')
    
    try:
        # Exchange authorization code for access token
        token_response = tiktok_client.exchange_token(authorization_code)
        
        # Create JWT for our application
        jwt_token = jwt.encode({
            'tiktok_user_id': token_response['open_id'],
            'access_token': token_response['access_token']
        }, app.config['SECRET_KEY'], algorithm='HS256')
        
        return jsonify({
            'jwt_token': jwt_token,
            'user_info': token_response
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/auth/validate', methods=['POST'])
def validate_token():
    token = request.json.get('token')
    try:
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return jsonify({'valid': True, 'user_id': decoded['tiktok_user_id']}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({'valid': False, 'error': 'Token expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'valid': False, 'error': 'Invalid token'}), 401
