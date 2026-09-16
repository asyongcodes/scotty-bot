from datetime import datetime
import time
import streamlit as st

st.set_page_config(page_title="SCOTTY Chatbot", page_icon="🤖")
clock_placeholder = st.empty()
st.title("---- SCOTTY ----")
st.subheader("Virtual Assistance Program")
st.subheader("by TSTOC")

if "menu" not in st.session_state:
    st.session_state.menu = "main"

# --- MAIN MENU ---
if st.session_state.menu == "main":
    st.write("")
    st.write("Hi, I am SCOTTY! Here are my SERVICES:")
    if st.button("1. ASSISTANCE"):
        st.session_state.menu = "assistance"
        st.rerun()
    if st.button("2. DUBOUT"):
        st.session_state.menu = "dubout"
        st.rerun()
    if st.button("3. CINEMA ROOM"):
        st.session_state.menu = "cinema"
        st.rerun()
    if st.button("4. OTHER CONCERN"):
        st.session_state.menu = "other"
        st.rerun()

# --- ASSISTANCE MENU ---
elif st.session_state.menu == "assistance":
    st.markdown("### ---- ASSISTANCE ----")
    if st.button("Computer not responding"):
        st.info("📞 Call 2630 for restart and relog-in")
    if st.button("No audio/video"):
        st.info("📞 Call 2630 for configuration of settings")
    if st.button("No power"):
        st.info("📞 Call 2630 for checking of hardware and power supply")
    if st.button("⬅️ BACK to Main Menu"):
        st.session_state.menu = "main"
        st.rerun()

# --- DUBOUT MENU ---
elif st.session_state.menu == "dubout":
    st.markdown("### ---- DUBOUT ----")
    dnb = st.text_input("Enter Deck and Bay:")
    if dnb:
        st.success(f"📱 Text your message:\n'{dnb}' to 09154417194")
    if st.button("No comms"):
        st.info("👉 Reselect Blackmagic as device control. If to no avail, call 2630.")
    if st.button("Dropped frames"):
        st.info("👉 Relaunch Premiere. If issue persists, call 2630.")
    if st.button("⬅️ BACK to Main Menu"):
        st.session_state.menu = "main"
        st.rerun()

# --- CINEMA ROOM MENU ---
elif st.session_state.menu == "cinema":
    st.markdown("### ---- CINEMA ROOM ----")
    if st.button("Preview"):
        st.info("📞 Call 2630 for preparation of projector/tv/speakers")
    if st.button("Meeting"):
        st.info("📞 Call 2630 for preparation of tables and chairs")
    if st.button("⬅️ BACK to Main Menu"):
        st.session_state.menu = "main"
        st.rerun()

# --- OTHER CONCERN ---
elif st.session_state.menu == "other":
    st.warning("📍 Visit 4th flr TOC for personal TSTOC assistance experience.")
    if st.button("⬅️ BACK to Main Menu"):
        st.session_state.menu = "main"
        st.rerun()

while True:
    current_time = datetime.now().strftime("%A, %B %d, %Y | %I:%M:%S %p")
    clock_placeholder.markdown(f"⏱️ **{current_time}**\n---")
    time.sleep(1)
