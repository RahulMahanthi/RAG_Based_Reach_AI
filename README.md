# 📘 Reach_AI - Your Intelligent Document Assistant

![Reach_AI](https://img.shields.io/badge/AI-Powered-blue.svg) ![Streamlit](https://img.shields.io/badge/Streamlit-Enabled-red.svg) ![Python](https://img.shields.io/badge/Python-3.7%2B-brightgreen.svg)

## 🚀 Overview
Reach_AI is an AI-powered document assistant that enables users to upload research PDFs and interact with them through natural language queries. Leveraging **LangChain, Ollama, and Streamlit**, it provides concise, fact-based answers based on document content.

## ✨ Features
- 📄 Upload and process research PDFs
- 🧠 AI-powered document search using **DeepSeek-R1 embeddings**
- 🔍 Intelligent query response system
- 🎨 Modern, sleek UI with **enhanced styling**
- 🛠 Built with **Streamlit, LangChain, and Ollama LLM**

## 🏗 Tech Stack
- **Python 3.7+**
- **Streamlit** (Frontend & UI)
- **LangChain** (Document processing & AI pipeline)
- **Ollama LLM** (DeepSeek-R1 models for responses)
- **PDFPlumber** (Document parsing)
- **In-Memory Vector Store** (Efficient text retrieval)

## 📥 Installation
### 1️⃣ Clone the repository
```sh
$ git clone https://github.com/yourusername/Reach_AI.git
$ cd Reach_AI
```

### 2️⃣ Create a virtual environment (optional but recommended)
```sh
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies
```sh
$ pip install -r requirements.txt
```

### 4️⃣ Run the application
```sh
$ streamlit run app.py
```

## 📌 Usage
1. Upload a **PDF document**.
2. Ask questions related to the uploaded document.
3. The AI will provide relevant responses based on the document's content.


## 🔧 Configuration
- Update `EMBEDDING_MODEL` and `LANGUAGE_MODEL` in `app.py` to change AI models.
- Modify `styles.css` inside `st.markdown()` for UI customizations.

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📜 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 💬 Contact
For questions, reach out at: **rahulkomal834@gmail.com**

---
🌟 **Star this repo** if you found it helpful!
