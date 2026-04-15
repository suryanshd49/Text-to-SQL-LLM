# Text-to-SQL using LLM

This project converts natural language queries into SQL using a local LLM (Llama3) and executes them on a MySQL database.

## Features
- Natural language to SQL
- Local LLM (Ollama + Llama3)
- Chat-based UI (Streamlit)
- Multi-table support

## Tech Stack
- Python
- MySQL
- Streamlit
- Ollama (Llama3)

## Run Locally

1. Install dependencies:
pip install -r requirements.txt

2. Start Ollama:
ollama run llama3

3. Run app:
streamlit run frontend.py
