import streamlit as st
import sys
sys.path.append('.')
from backend.config import get_app_password

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

st.markdown('<h1 style="text-align: center; color: #FF6B35;">🔐 Login</h1>', unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    st.success("✅ Already logged in!")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("Home.py")
    with col2:
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()
else:
    st.info("Enter your dashboard password")
    
    with st.form("login"):
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("🔓 Login", use_container_width=True)
        
        if submit:
            if password == get_app_password():
                st.session_state.logged_in = True
                st.success("✅ Login successful!")
                st.rerun()
            else:
                st.error("❌ Wrong password")
    
    with st.expander("🔑 Default password (for testing)"):
        st.warning("Default: `admin123`\n\nChange in .streamlit/secrets.toml")
```

4. Commit ✅

---

### **STEP 4: Deploy to Streamlit Cloud (3 minutes)**

Now let's make it live online!

1. Go to https://streamlit.io/cloud

2. Click **"Sign up"**

3. Choose **"Continue with GitHub"**

4. Authorize Streamlit

5. Click **"New app"**

6. Fill in:
   - **Repository:** `your-username/angel-paper-trading`
   - **Branch:** `main`
   - **Main file path:** `Home.py`

7. Click **"Advanced settings"**

8. Copy your secrets from GitHub's `.streamlit/secrets.toml` and paste there

9. Click **"Deploy!"**

10. Wait 2-3 minutes... ☕

11. Your app is now live! You'll get a URL like:
    `https://your-username-angel-paper-trading.streamlit.app`

---

## **DONE! YOUR WEBSITE IS LIVE! 🎉**

**You can now:**
- Access it from **anywhere** (phone, laptop, anywhere!)
- Share the link (if you want)
- No computer needed - all online!

---

## **HOW TO EDIT FILES LATER (Online)**

**Option 1: GitHub Web Editor**
1. Go to your repository
2. Click on any file
3. Click the pencil icon (✏️) to edit
4. Make changes
5. Scroll down, click "Commit changes"
6. Streamlit Cloud auto-updates! (30 seconds)

**Option 2: GitHub Codespaces (VS Code in browser!)**
1. On your repository page
2. Click green **"Code"** button
3. Click **"Codespaces"** tab
4. Click **"Create codespace"**
5. Full VS Code opens in your browser!
6. Edit files there
7. Changes auto-sync

---

## **CURRENT STATUS:**
```
Your GitHub Repository:
✅ requirements.txt
✅ Home.py
✅ .streamlit/config.toml
✅ .streamlit/secrets.toml
✅ backend/config.py
✅ pages/1_🔐_Login.py

Your Live Website:
✅ https://your-app.streamlit.app
✅ Accessible from anywhere
✅ Auto-updates when you edit on GitHub
