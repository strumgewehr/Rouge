"""
Web App entry point for testing via localhost
"""
from app import app, socketio

if __name__ == '__main__':
    print("Starting ROUGE on http://localhost:5000")
    print("Open your browser and navigate to the URL above")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

