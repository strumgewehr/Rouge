"""
ROUGE Mobile App Entry Point
Runs the Flask web app for localhost testing and APK packaging
"""
from app import app, socketio

if __name__ == '__main__':
    print("Starting ROUGE on http://localhost:5000")
    print("Open your browser and navigate to the URL above")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
