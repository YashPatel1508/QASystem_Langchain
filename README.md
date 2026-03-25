# 📄 QA with PDF — LlamaIndex + Google Gemini

A **Retrieval-Augmented Generation (RAG)** application that lets you upload PDF documents and ask natural-language questions about their content. Built with **LlamaIndex**, **Google Gemini**, and **Streamlit**.

---

## 🚀 Demo

> Upload a PDF → Ask a question → Get an AI-powered answer instantly!

---

## 🧠 How It Works

```
PDF Document
     │
     ▼
Data Ingestion (SimpleDirectoryReader)
     │
     ▼
Gemini Embedding Model (gemini-embedding-001)
     │
     ▼
VectorStoreIndex (persisted to ./storage)
     │
     ▼
Query Engine ← User Question
     │
     ▼
Gemini LLM (gemini-2.5-flash)
     │
     ▼
Answer
```

---

## 📁 Project Structure

```
QASystem_Langchain/
│
├── QAWithPDF/                   # Core package
│   ├── __init__.py
│   ├── data_ingestion.py        # Loads PDF files using SimpleDirectoryReader
│   ├── embedding.py             # Creates/loads Gemini vector embeddings & index
│   └── model_api.py             # Initializes the Gemini LLM (gemini-2.5-flash)
│
├── Data/                        # 📂 Place your PDF files here
├── storage/                     # Auto-generated: persisted vector index
├── logs/                        # Auto-generated: application logs
├── notebook/                    # Jupyter notebooks for experimentation
├── Experiments/                 # Experimental code & research
│
├── StreamlitApp.py              # 🎯 Main Streamlit application entry point
├── exception.py                 # Custom exception handler with line-level tracing
├── logger.py                    # Logging configuration
├── setup.py                     # Package setup
├── requirements.txt             # Python dependencies
├── template.py                  # Project scaffolding template
├── .env                         # Environment variables (not committed)
└── .gitignore
```

---

## ⚙️ Tech Stack

| Component         | Technology                              |
|------------------|-----------------------------------------|
| **LLM**           | Google Gemini `gemini-2.5-flash`        |
| **Embeddings**    | Google Gemini `gemini-embedding-001`    |
| **RAG Framework** | LlamaIndex (llama-index)                |
| **UI**            | Streamlit                               |
| **Vector Store**  | LlamaIndex VectorStoreIndex (local)     |
| **PDF Loader**    | LlamaIndex `SimpleDirectoryReader`      |

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YashPatel1508/QASystem_Langchain.git
cd QASystem_Langchain
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install the Package

```bash
pip install -e .
```

### 5. Configure Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

> 🔑 Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

---

## ▶️ Running the Application

### Run QAwithPDF (Streamlit App)

```bash
streamlit run StreamlitApp.py
```

The app will open at **http://localhost:8501** in your browser.

---

## 📖 Usage

1. **Place your PDF(s)** in the `Data/` folder.
2. **Launch the app** with `streamlit run StreamlitApp.py`.
3. **Upload your document** using the file uploader in the UI.
4. **Type your question** in the text input field.
5. **Click "Submit & Process"** — the app will:
   - Load and parse the PDF
   - Generate vector embeddings using Gemini
   - Persist the index to `./storage/` for reuse
   - Query the index with your question
   - Display the AI-generated answer

---

## 🗂️ Key Modules

### `QAWithPDF/data_ingestion.py`
Loads PDF documents from the `Data/` directory using LlamaIndex's `SimpleDirectoryReader`. Includes custom logging and exception handling.

### `QAWithPDF/embedding.py`
- Initializes `GeminiEmbedding` (`gemini-embedding-001`) as the embedding model.
- Creates a `VectorStoreIndex` from loaded documents.
- Persists the index to `./storage/` on first run; loads from cache on subsequent runs.
- Returns a `QueryEngine` ready to answer questions.

### `QAWithPDF/model_api.py`
Loads the Google Gemini LLM (`gemini-2.5-flash`) using the API key from `.env`. Configures `genai` and returns a `Gemini` LlamaIndex LLM instance.

### `exception.py`
A custom exception class that captures the **filename**, **line number**, and **error message** for precise error tracing.

### `logger.py`
Configures timestamped log files stored in the `logs/` directory.

---

## 🔧 Configuration

| Setting          | Location              | Default Value              |
|------------------|-----------------------|----------------------------|
| Chunk Size       | `embedding.py`        | `800`                      |
| Chunk Overlap    | `embedding.py`        | `80`                       |
| Index Storage    | `embedding.py`        | `./storage`                |
| LLM Model        | `model_api.py`        | `models/gemini-2.5-flash`  |
| Embedding Model  | `embedding.py`        | `models/gemini-embedding-001` |

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `GOOGLE_API_KEY` not found | Ensure `.env` is in the project root with a valid key |
| No answer returned | Make sure your PDF is placed in the `Data/` folder |
| Index not updating | Delete the `./storage` folder to force re-indexing |
| Import errors | Run `pip install -e .` to install the local package |

---

## 📜 License

This project is licensed under the terms of the [LICENSE](LICENSE) file.

---

## 👤 Author

**Yash Kaila**  
[GitHub: YashPatel1508](https://github.com/YashPatel1508)
