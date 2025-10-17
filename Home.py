import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Angel One Paper Trading",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #FF6B35;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

st.markdown('<p class="main-header">📈 Angel One Paper Trading System</p>', unsafe_allow_html=True)

if not st.session_state.logged_in:
    st.warning("🔒 Please login from the sidebar")
    
    st.info("""
    ### Welcome to Angel One Paper Trading!
    
    **Features:**
    - 📊 Real-time option prices from Angel One
    - 🤖 Automated Iron Condor strategy
    - 📈 Live P&L tracking
    - 📖 Complete trade log
    - ⚡ 50% profit exit rule
    - 🛡️ ₹25,000 stop loss
    
    **How to use:**
    1. Click **🔐 Login** in sidebar ←
    2. Enter password
    3. Connect Angel One API
    4. Start paper trading!
    
    **Skip Rules:**
    - ✅ Skip all Mondays
    - ✅ Skip when VIX > 15
    - ✅ Skip event days
    
    Navigate using sidebar 👈
    """)
else:
    st.success("✅ Logged in!")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Capital", "₹10,00,000")
    with col2:
        st.metric("Today's P&L", "₹0")
    with col3:
        st.metric("Open Positions", "0")
    with col4:
        st.metric("Status", "🟢 Ready")
    
    st.info("Use sidebar to navigate 👈")

st.markdown("---")
st.markdown("Paper Trading System | No Real Money Used")
