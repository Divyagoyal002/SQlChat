# SQlChat — v2

A Streamlit app to chat with a SQL database (SQLite demo or a MySQL connection)
using LangChain and Groq (Llama 3). The Groq API key is entered in the sidebar at
runtime — nothing secret is stored in the repo.

## Setup
```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python sqlite.py        # creates the demo student.db
streamlit run app.py    # enter your Groq API key in the sidebar
```

## Branches
- `main` — original version
- `v2` — updated SQLite/MySQL chat app
- `v3` — ChatSQL rewrite (6-ChatSQL)
