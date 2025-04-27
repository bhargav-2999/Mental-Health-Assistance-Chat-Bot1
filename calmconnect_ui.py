





# # # === calmconnect_ui.py ===

# import streamlit as st
# import os
# import json
# from datetime import datetime
# from rag_chain import ask_bot

# st.set_page_config(page_title="CalmConnect Chatbot", page_icon="🧘", layout="wide")
# LOG_DIR = "chat_logs"
# os.makedirs(LOG_DIR, exist_ok=True)

# # Sidebar - chat history
# st.sidebar.title("🩷 Chat History")
# sessions = sorted([f for f in os.listdir(LOG_DIR) if f.endswith(".json")], reverse=True)
# session_names = ["New Chat"] + sessions
# selected_session = st.sidebar.selectbox("📂 View Past Sessions", session_names)

# # Load or reset chat state
# if selected_session != "New Chat":
#     if "loaded_from_file" not in st.session_state:
#         with open(os.path.join(LOG_DIR, selected_session), "r", encoding="utf-8") as f:
#             st.session_state.chat = json.load(f)
#         st.session_state.loaded_from_file = True
# else:
#     if "chat" not in st.session_state or st.session_state.get("active_session") != "new":
#         st.session_state.chat = []
#         st.session_state.active_session = "new"

# # Delete/Rename session
# if selected_session != "New Chat":
#     if st.sidebar.button("🗑️ Delete this session"):
#         os.remove(os.path.join(LOG_DIR, selected_session))
#         st.rerun()

#     new_name = st.sidebar.text_input("✏️ Rename session", selected_session.replace(".json", ""))
#     if st.sidebar.button("Rename"):
#         new_file = new_name + ".json"
#         os.rename(os.path.join(LOG_DIR, selected_session), os.path.join(LOG_DIR, new_file))
#         st.rerun()

# # UI styling
# st.markdown("""
#     <style>
#         .main-container {
#             background: linear-gradient(to bottom right, #f0f4ff, #fbe9ff);
#             padding: 2rem;
#             border-radius: 1.5rem;
#             max-width: 700px;
#             margin: auto;
#         }
#         .chat-bubble {
#             padding: 0.75rem 1rem;
#             border-radius: 20px;
#             max-width: 70%;
#             word-wrap: break-word;
#             margin-bottom: 10px;
#         }
#         .user-bubble {
#             background-color: #dbeafe;
#             color: #1e3a8a;
#             margin-left: auto;
#         }
#         .bot-bubble {
#             background-color: #fef3c7;
#             color: #92400e;
#             margin-right: auto;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Chat UI
# st.markdown("<div class='main-container'>", unsafe_allow_html=True)
# st.markdown("## 🧘 CalmConnect – Your Wellness Companion", unsafe_allow_html=True)

# # Initial welcome
# if not st.session_state.chat:
#     st.session_state.chat.append({"role": "assistant", "text": "👋 Hello! I'm CalmConnect. How can I support your mental wellness today?"})

# chat_placeholder = st.container()
# with chat_placeholder:
#     for msg in st.session_state.chat:
#         role_class = "user-bubble" if msg["role"] == "user" else "bot-bubble"
#         st.markdown(f"<div class='chat-bubble {role_class}'>{msg['text']}</div>", unsafe_allow_html=True)

# # Input box
# with st.form(key="chat_form", clear_on_submit=True):
#     user_input = st.text_input("", placeholder="Type a message...", label_visibility="collapsed")
#     submitted = st.form_submit_button("Send ✉️")

# if submitted and user_input:
#     st.session_state.chat.append({"role": "user", "text": user_input})

#     # Run bot response BEFORE rerun
#     try:
#         history = st.session_state.chat[-2:]
#         previous = st.session_state.chat[:-2] if len(st.session_state.chat) > 2 else []
#         response = ask_bot(user_input, history=history, previous=previous)
#     except Exception as e:
#         response = "🧘 Sorry, something went wrong. Please try again."

#     st.session_state.chat.append({"role": "assistant", "text": response})

#     # Save session
#     timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     session_path = os.path.join(LOG_DIR, f"session_{timestamp}.json")
#     with open(session_path, "w", encoding="utf-8") as f:
#         json.dump(st.session_state.chat, f, ensure_ascii=False, indent=2)

#     # Refresh page to show updated messages
#     # st.experimental_rerun()
#     st.rerun()   






# import streamlit as st
# import os
# import json
# import logging
# from datetime import datetime
# from rag_chain import ask_bot

# # --- Logging setup ---
# logging.basicConfig(
#     filename="app.log",
#     level=logging.INFO,
#     format="%(asctime)s %(levelname)s:%(message)s"
# )

# # Page config
# st.set_page_config(page_title="CalmConnect Chatbot", page_icon="🧘", layout="wide")

# # Ensure log directory exists
# LOG_DIR = "chat_logs"
# os.makedirs(LOG_DIR, exist_ok=True)

# # Load custom CSS
# if os.path.exists("style.css"):
#     st.markdown(open("style.css").read(), unsafe_allow_html=True)

# # Sidebar: sessions and controls
# st.sidebar.title("🩷 Chat History")

# def list_sessions():
#     return sorted([f for f in os.listdir(LOG_DIR) if f.endswith('.json')], reverse=True)

# sessions = list_sessions()
# session_names = ["New Chat"] + sessions
# selected = st.sidebar.selectbox("📂 View Past Sessions", session_names)

# # Clear history
# if st.sidebar.button("🗑️ Clear Current Chat"):
#     st.session_state.chat = []

# # Rename/delete only for existing sessions
# if selected != "New Chat":
#     if st.sidebar.button("🗑️ Delete this session"):
#         os.remove(os.path.join(LOG_DIR, selected))
#         st.experimental_rerun()
#     new_name = st.sidebar.text_input("✏️ Rename session", selected.replace('.json',''))
#     if st.sidebar.button("Rename") and new_name:
#         os.rename(os.path.join(LOG_DIR, selected), os.path.join(LOG_DIR, new_name + ".json"))
#         st.experimental_rerun()

# # Load or reset chat state
# if selected != "New Chat":
#     if "loaded" not in st.session_state:
#         with open(os.path.join(LOG_DIR, selected), encoding="utf-8") as f:
#             st.session_state.chat = json.load(f)
#         st.session_state.loaded = True
# else:
#     if "chat" not in st.session_state or st.session_state.get("active") != "new":
#         st.session_state.chat = []
#         st.session_state.active = "new"

# # Main container styling
# st.markdown("""
# <style>
#     .main-container { background: linear-gradient(to bottom right, #f0f4ff, #fbe9ff);
#         padding: 2rem; border-radius: 1.5rem; max-width: 700px; margin: auto; }
#     .chat-bubble { padding: .75rem 1rem; border-radius:20px; max-width:70%; word-wrap:break-word; margin-bottom:10px; }
#     .user-bubble { background-color:#dbeafe; color:#1e3a8a; margin-left:auto; }
#     .bot-bubble { background-color:#fef3c7; color:#92400e; margin-right:auto; }
# </style>
# """, unsafe_allow_html=True)

# st.markdown("<div class='main-container'>", unsafe_allow_html=True)
# st.markdown("## 🧘 CalmConnect – Your Wellness Companion", unsafe_allow_html=True)

# # Seed initial message
# if not st.session_state.chat:
#     st.session_state.chat.append({"role":"assistant","text":"👋 Hello! I'm CalmConnect. How can I support your mental wellness today?"})

# # Render chat
# chat_container = st.container()
# with chat_container:
#     for msg in st.session_state.chat:
#         cls = "user-bubble" if msg['role']=='user' else "bot-bubble"
#         st.markdown(f"<div class='chat-bubble {cls}'>{msg['text']}</div>", unsafe_allow_html=True)

# # Input form
# with st.form(key="chat_form", clear_on_submit=True):
#     user_input = st.text_input("", placeholder="Type a message...", label_visibility="collapsed")
#     submit = st.form_submit_button("Send ✉️")

# if submit and user_input:
#     st.session_state.chat.append({"role":"user","text":user_input})
#     with st.spinner("CalmConnect is thinking..."):
#         try:
#             response = ask_bot(user_input, history=st.session_state.chat)
#         except Exception as e:
#             logging.error(f"Error in ask_bot: {e}")
#             response = "🧘 Sorry, something went wrong. Please try again."
#     st.session_state.chat.append({"role":"assistant","text":response})

#     # Save
#     ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     path = os.path.join(LOG_DIR, f"session_{ts}.json")
#     with open(path, "w", encoding="utf-8") as f:
#         json.dump(st.session_state.chat, f, ensure_ascii=False, indent=2)

#     # st.experimental_rerun()
#     st.rerun()   






import streamlit as st
import os
import json
import logging
import time
import random
from datetime import datetime
from rag_chain import ask_bot

# --- Logging setup ---
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s:%(message)s"
)

# --- Page config ---
st.set_page_config(
    page_title="CalmConnect Chatbot", 
    page_icon="🧘", 
    layout="centered",
    initial_sidebar_state="auto"
)

# --- Ensure log directory exists ---
LOG_DIR = "chat_logs"
os.makedirs(LOG_DIR, exist_ok=True)

# --- Load Google Fonts & custom CSS ---
st.markdown("""
<link href='https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap' rel='stylesheet'>
<style>
    body, .stApp { font-family: 'Poppins', sans-serif; background: linear-gradient(135deg, #e0f7fa, #f3e5f5); }
    .main-container { background: white; padding: 2rem; border-radius: 2rem; max-width: 700px; margin: auto; box-shadow: 0 0 25px rgba(0,0,0,0.1); }
    .chat-bubble { padding: 1rem 1.5rem; border-radius: 25px; max-width: 80%; word-wrap: break-word; margin-bottom: 1rem; font-size: 1rem; line-height:1.4; }
    .user-bubble { background: #d1e8ff; color: #054a91; margin-left: auto; }
    .bot-bubble { background: #fff3e0; color: #bf360c; margin-right: auto; }
    .btn { background: linear-gradient(to right, #89f7fe, #66a6ff); color: white; border: none; border-radius: 30px; padding: 0.5rem 1.5rem; font-size: 1rem; cursor: pointer; }
    .quote { font-style: italic; color: #555; margin-bottom: 1rem; }
</style>
""", unsafe_allow_html=True)

# --- Sidebar: user settings & chat history ---
st.sidebar.header("⚙️ Settings & History")
# Optional nickname
if 'nickname' not in st.session_state:
    st.session_state.nickname = ''
st.session_state.nickname = st.sidebar.text_input("Your name (optional)", st.session_state.nickname)

# Chat history controls
sessions = sorted([f for f in os.listdir(LOG_DIR) if f.endswith('.json')], reverse=True)
selected = st.sidebar.selectbox("📂 Past Sessions", ["New Chat"] + sessions)
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.chat = []
if selected != "New Chat":
    if st.sidebar.button("Delete Session"):
        os.remove(os.path.join(LOG_DIR, selected))
        st.experimental_rerun()

# --- Mood Check-In & Motivational Quote ---
st.markdown("<div class='main-container'>", unsafe_allow_html=True)
if 'checked_in' not in st.session_state:
    mood = st.radio("How are you feeling today?", ["😊 Happy", "😌 Calm", "😣 Stressed", "😢 Sad", "😰 Anxious"], index=1, horizontal=True)
    st.session_state.checked_in = True
    st.session_state.chat = []
    greeting = f"Hello{', ' + st.session_state.nickname if st.session_state.nickname else ''}! You seem {mood.split()[1].lower()} today. I'm here to help."
    st.session_state.chat.append({"role": "assistant", "text": greeting})
# Random daily tip
if st.button("💡 Daily Wellness Tip"):
    tips = [
        "Take a 5-minute walk outside.",
        "Practice deep breathing for one minute.",
        "Write down three things you're grateful for.",
        "Drink a glass of water mindfully.",
        "Close your eyes and stretch gently."
    ]
    tip = random.choice(tips)
    st.success(f"🌟 Tip: {tip}")
    st.balloons()

# --- Render Chat ---
for msg in st.session_state.chat:
    cls = "user-bubble" if msg['role']=='user' else "bot-bubble"
    st.markdown(f"<div class='chat-bubble {cls}'>{msg['text']}</div>", unsafe_allow_html=True)

# --- Chat Input ---
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("", placeholder="Share your thoughts...", label_visibility="collapsed")
    submit = st.form_submit_button("Send 📨")

if submit and user_input:
    # append user message
    st.session_state.chat.append({"role":"user","text":user_input})

    # breathing exercise trigger
    if any(w in user_input.lower() for w in ["anxious","panic","nervous","overwhelmed"]):
        if st.button("🫶 Breathing Exercise", key="breath_btn"):
            breath = st.empty()
            for cycle in range(2):
                breath.text("Breathe in... 4s")
                time.sleep(4)
                breath.text("Hold... 7s")
                time.sleep(7)
                breath.text("Exhale... 8s")
                time.sleep(8)
            breath.text("✨ Feeling calmer? Let's continue!")

    # get bot response
    with st.spinner("CalmConnect is thinking..."):
        try:
            resp = ask_bot(user_input, history=st.session_state.chat)
        except Exception as e:
            logging.error(f"ask_bot error: {e}")
            resp = "🧘 Sorry, I encountered an issue. Please try again."
    st.session_state.chat.append({"role":"assistant","text":resp})

    # save session
    stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fname = f"session_{stamp}.json"
    with open(os.path.join(LOG_DIR, fname), "w", encoding="utf-8") as f:
        json.dump(st.session_state.chat, f, ensure_ascii=False, indent=2)
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)







