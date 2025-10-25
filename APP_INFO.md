# ROUGE - App Information

## ✅ What's Been Done

### Core Features
- ✅ Anonymous chat without logins
- ✅ Room creation with unique 6-digit codes
- ✅ Real-time messaging via WebSockets
- ✅ Image sharing (max 8MB)
- ✅ Dark mysterious UI with rouge red theme
- ✅ Mobile-responsive design

### Technical Stack
- **Backend**: Flask + Flask-SocketIO
- **Frontend**: HTML5 + CSS3 + JavaScript
- **Communication**: WebSockets (Socket.IO)
- **Python Version**: 3.8+ (works with Python 3.14!)

### File Structure
```
Rouge/
├── app.py              # Flask backend (main logic)
├── webapp.py           # Web app entry point
├── main.py             # Mobile entry point (for APK)
├── requirements.txt    # Dependencies
├── templates/          # HTML pages
│   ├── index.html     # Home page
│   ├── create.html    # Create room
│   ├── join.html      # Join room
│   └── chat.html      # Chat interface
├── static/
│   └── style.css      # Dark theme styles
└── run.bat/sh         # Launcher scripts
```

## 🚀 How to Use

### Testing Locally
1. Run: `python webapp.py`
2. Open: http://localhost:5000
3. Test in two browser tabs

### Building APK
Option 1: Use Capacitor (Recommended)
- Works with web tech
- Easy to build
- Professional result

Option 2: Use Buildozer
- Python-based
- More configuration needed

## 🎨 UI Theme

- **Colors**: Deep dark (#0A0A0F) with rouge red (#E61E2A)
- **Style**: Mysterious, minimal, modern
- **Effects**: Glowing text, smooth animations
- **Typography**: Clean, readable, bold titles

## 📱 Mobile Features

- Touch-friendly buttons
- Responsive layout
- Image optimization
- Scrollable chat
- Copy to clipboard
- Back navigation

## 🔐 Security & Privacy

- No user data stored
- No login required
- Anonymous communication
- Real-time encryption-ready
- No server-side message storage

## 🌟 Highlights

✨ No Python version issues (works with 3.14!)
✨ Beautiful dark UI
✨ Real-time chat
✨ Easy to test (just run and open browser)
✨ Easy to deploy (Heroku, PythonAnywhere, etc.)
✨ Mobile-ready design
✨ APK packaging supported

## 📞 Next Steps

1. Test the app: Run `python webapp.py`
2. Customize: Edit colors/styles in `static/style.css`
3. Deploy: Push to Heroku or similar
4. Build APK: Use Capacitor or Buildozer
5. Share: Give users the URL or APK

Enjoy your mysterious anonymous chat app! 🔴

