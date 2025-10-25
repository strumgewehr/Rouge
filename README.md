# ROUGE 🔴

*Whispers in the Shadows*

A mysterious anonymous chat application. Two anonymous users can connect via text and images without any login or registration.

## Features

- **Anonymous Communication**: No accounts, no logins, pure anonymity
- **Simple Room System**: Create a room with a unique 6-digit code
- **Real-time Chat**: Instant messaging using WebSockets
- **Image Sharing**: Send images up to 8MB
- **Dark Mysterious UI**: Beautiful dark theme with rouge red accents
- **Cross-Platform**: Web-based app that works everywhere
- **Mobile Ready**: Can be packaged as APK for Android

## How It Works

1. **Create Room**: User A clicks "Create Room" and receives a unique 6-digit code
2. **Share Code**: User A shares the code with User B
3. **Join Room**: User B enters the code and clicks "Join Room"
4. **Connect**: When codes match, both users are connected
5. **Chat**: Users can exchange text messages and images (max 8MB)

## Quick Start

### Testing on Localhost

1. **Install Python 3.8+** (any version works now!)

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run the app**:
```bash
python webapp.py
```

Or use the launcher scripts:
- Windows: `run.bat`
- Linux/Mac: `chmod +x run.sh && ./run.sh`

4. **Open your browser** and go to:
```
http://localhost:5000
```

5. **Test it**:
   - Open two browser tabs or two different browsers
   - In one tab, click "Create Room"
   - Copy the 6-digit code
   - In the other tab, click "Join Room" and enter the code
   - Start chatting!

## Requirements

- Python 3.8 or higher
- Flask 3.0.0
- Flask-SocketIO 5.3.5
- Eventlet 0.33.3

## Building APK for Android

### Option 1: Using Buildozer (Recommended)

1. **Install Buildozer**:
```bash
pip install buildozer
```

2. **Build APK**:
```bash
buildozer android debug
```

The APK will be in `bin/rouge-*.apk`

### Option 2: Using Capacitor (Easier)

1. **Install Capacitor CLI**:
```bash
npm install -g @capacitor/cli
```

2. **Create Capacitor project**:
```bash
npm init
npm install @capacitor/core @capacitor/cli @capacitor/android
npx cap init
```

3. **Add Android platform**:
```bash
npx cap add android
npx cap sync
```

4. **Build and run**:
```bash
npx cap open android
```

### Option 3: Using Cloud Build Services

Use services like:
- [Capacitor Cloud](https://capacitorjs.com/docs)
- [PhoneGap Build](https://build.phonegap.com/)
- [Android Studio](https://developer.android.com/studio)

Just package the web app as a WebView container.

## Technical Details

- **Framework**: Flask (Python web framework)
- **Communication**: WebSockets via Flask-SocketIO
- **Frontend**: HTML5, CSS3, JavaScript
- **Real-time**: Socket.IO for bidirectional communication
- **Image Format**: Supports PNG, JPG, JPEG
- **Max Image Size**: 8MB
- **Architecture**: Web-based with mobile WebView wrapper

## Project Structure

```
Rouge/
├── app.py              # Flask backend with SocketIO
├── webapp.py           # Web app entry point (for testing)
├── main.py             # Mobile app entry point
├── requirements.txt    # Python dependencies
├── buildozer.spec     # Build configuration for APK
├── templates/         # HTML templates
│   ├── index.html     # Home page
│   ├── create.html    # Create room page
│   ├── join.html      # Join room page
│   └── chat.html      # Chat interface
├── static/            # Static files
│   └── style.css      # Dark mysterious theme
├── run.bat            # Windows launcher
└── run.sh             # Linux/Mac launcher
```

## UI Features

- **Deep dark background** (#0A0A0F)
- **Rouge red accents** (#E61E2A)
- **Smooth animations** and transitions
- **Responsive design** for mobile and desktop
- **Mysterious aesthetic** with glowing text effects
- **Intuitive chat interface** with sent/received message alignment

## Usage Notes

- The app runs on port 5000 by default
- For local testing, both users connect to the same server
- For production, deploy to a cloud server (Heroku, AWS, etc.)
- Room codes are random 6-digit numbers (100000-999999)
- Messages are displayed in real-time
- Images are displayed inline in the chat
- Click the back arrow in chat to disconnect and return home

## Deployment

### Deploy to Heroku

1. Create `Procfile`:
```
web: python webapp.py
```

2. Deploy:
```bash
heroku create rouge-chat
git push heroku main
```

### Deploy to PythonAnywhere

1. Upload all files to your account
2. Create a new web app
3. Point it to `webapp.py`
4. Reload and access via your subdomain

## License

MIT License - Feel free to modify and distribute

## Disclaimer

This app is for anonymous communication. Users are responsible for their content and conversations.
