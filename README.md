# CalmConnect 🧘‍♂️
A Mental Wellness Companion Chatbot built with Streamlit and RAG

## 🌟 Overview
CalmConnect is a supportive mental health chatbot designed to offer a listening ear, calming techniques, and wellness advice. It uses Retrieval-Augmented Generation (RAG) to provide thoughtful and empathetic responses based on mental health knowledge bases.

## 🚀 Features
- Friendly chatbot UI (built with Streamlit)
- Mood check-in when you start chatting
- Motivational tips & breathing exercise prompts
- Save and view previous chat sessions
- Smooth and aesthetic UI with custom fonts and styling
- RAG-powered intelligent conversation (using rag_chain.py)

## 🛠️ Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/CalmConnect.git
   cd CalmConnect


python -m venv venv
source venv/bin/activate       # On Mac/Linux
venv\Scripts\activate          # On Windows



pip install -r requirements.txt


streamlit run calmconnect_ui.py


streamlit run calmconnect_ui.py --server.port=10000 --server.address=0.0.0.0


CalmConnect/
│
├── calmconnect_ui.py                  # Main Streamlit app (UI)
├── rag_chain.py                        # RAG logic (bot's brain)
├── index_data.py                       # Indexing documents for retrieval
├── scraper.py                          # Scraper for additional content
├── WellbeingMentalWellness2020-final.txt  # Mental wellness knowledge base
├── wellbeing-team-cbt-workshop-booklet-2016.txt  # Additional CBT resource
├── requirements.txt                    # Python package dependencies
├── chat_logs/                          # Folder to save chat history
├── .gitignore
└── README.md                           # You're here!



Feel free to copy-paste this directly!
