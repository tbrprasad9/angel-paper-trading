import streamlit as st
from datetime import time

def get_angel_credentials():
    try:
        return {
            'api_key': st.secrets["angel_one"]["api_key"],
            'client_id': st.secrets["angel_one"]["client_id"],
            'password': st.secrets["angel_one"]["password"],
            'totp_secret': st.secrets["angel_one"]["totp_secret"]
        }
    except:
        return {'api_key': '', 'client_id': '', 'password': '', 'totp_secret': ''}

def get_app_password():
    try:
        return st.secrets["app"]["admin_password"]
    except:
        return "admin123"

STARTING_CAPITAL = 1000000
NIFTY_LOTS = 12
BANK_NIFTY_LOTS = 3
PROFIT_TARGET_PERCENT = 0.50
STOP_LOSS_AMOUNT = 25000
VIX_THRESHOLD = 15
GAP_THRESHOLD = 2.0
ENTRY_TIME = time(9, 40)
EXIT_TIME = time(14, 30)
SKIP_MONDAYS = True
EVENT_DAYS = ["2025-02-01", "2025-04-09"]
