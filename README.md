# LangChain SQL Chatbot with Streamlit

This project is a **LangChain-powered chatbot** that allows users to interact with an **SQL database** (SQLite or MySQL) using natural language. The chatbot leverages **Llama 3 (via Groq API)** and **LangChain agents** to process queries and retrieve responses.

## 🚀 Features
- **Supports both SQLite and MySQL** databases
- **Streamlit-based UI** for interactive querying
- **Llama 3 model (Groq API) integration** for intelligent query handling
- **SQL Database Agent** using LangChain
- **Session-based chat history**

## 📂 Project Structure
```plaintext
📁 Langchain-SQL-Chatbot
│-- app.py               # Main Streamlit application
│-- requirements.txt     # Dependencies
│-- student.db           # Sample SQLite database
│-- README.md            # Project Documentation
```

## 🛠️ Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/langchain-sql-chatbot.git
cd langchain-sql-chatbot
```

### 2️⃣ Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Groq API Key
Get your **Groq API Key** from [Groq](https://groq.com) and provide it in the Streamlit UI when prompted.

## 🔧 Usage
### Running the Streamlit App
```bash
streamlit run app.py
```

### Connecting to a Database
- **For SQLite:** The app uses `student.db` by default.
- **For MySQL:** Provide your MySQL credentials in the sidebar.

### Querying the Database
1. Enter your **Groq API key** in the sidebar.
2. Select either **SQLite** or **MySQL** as the database.
3. Ask your query in natural language (e.g., *"Show me all students with GPA > 3.5"*).
4. View the response from the chatbot!

## ⚠️ Troubleshooting
### **ModuleNotFoundError: No module named 'mysql'**
```bash
pip install mysql-connector-python pymysql
```

### **ModuleNotFoundError: No module named 'langchain_groq'**
```bash
pip install langchain-groq
```

## 📜 License
This project is open-source and available under the **MIT License**.

## ✨ Contributions
Feel free to fork this repository, create a feature branch, and submit a pull request!

## 📩 Contact
For any issues, reach out via [GitHub Issues](divyagoyalbg@gmail.com).

