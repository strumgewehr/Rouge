# ROUGE Quick Start Guide

## 🚀 Getting Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the App
```bash
python webapp.py
```

### Step 3: Open Your Browser
Navigate to: **http://localhost:5000**

## 🧪 Testing the App

1. **Open the app** in your browser at `http://localhost:5000`

2. **Create a room**:
   - Click "Create Room"
   - You'll see a 6-digit code (e.g., "123456")
   - You'll be automatically redirected to the chat

3. **Join the room** (in another browser/tab):
   - Open a new browser or incognito window
   - Go to `http://localhost:5000`
   - Click "Join Room"
   - Enter the code from step 2
   - You'll be connected to the chat

4. **Start chatting**:
   - Type messages and press Enter
   - Click the 📷 button to send images
   - Images are automatically displayed in the chat

## 📱 Building APK for Android

### Method 1: Using Capacitor (Easiest)

1. Install Node.js if you haven't already
2. Install Capacitor:
```bash
npm install -g @capacitor/cli
```
3. Initialize Capacitor project:
```bash
npx cap init rouge org.rouge
```
4. Add Android platform:
```bash
npx cap add android
npx cap sync
```
5. Open in Android Studio:
```bash
npx cap open android
```
6. Build APK in Android Studio

### Method 2: Using Buildozer

1. Install Buildozer:
```bash
pip install buildozer
```
2. Build APK:
```bash
buildozer android debug
```
3. Find APK in `bin/` folder

## 🌐 Deploying Online

### Heroku (Free)

1. Create `Procfile`:
```
web: python webapp.py
```

2. Deploy:
```bash
heroku create rouge-chat
git push heroku main
```

### PythonAnywhere (Free)

1. Upload files via web interface
2. Create new web app
3. Point WSGI file to `webapp.py`
4. Reload

## 📝 Tips

- Use different browsers for testing (Chrome, Firefox, Edge)
- Open incognito/private windows for multiple test sessions
- Share the URL with friends to test across networks
- Room codes expire when all users disconnect
- Maximum image size is 8MB

## 🔧 Troubleshooting

**Port 5000 already in use?**
Change the port in `webapp.py`:
```python
socketio.run(app, host='0.0.0.0', port=8000, debug=True)
```

**Can't connect to server?**
Make sure both users are on the same network (for local testing)

**Images not uploading?**
Check file size (must be under 8MB)

## 💡 Features to Try

- Send long messages
- Send emoji 😀🎉🚀
- Send images of different sizes
- Create multiple rooms
- Disconnect and reconnect
- Copy room codes

Enjoy chatting anonymously! 🔴

