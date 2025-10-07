# capit.ai
An AI tool designed for quantitative stock analysis. It processes historical and real-time market data, such as price and volume, to identify trends and generate advisory signals for user review.

# Capit.ai 🤖📈

An AI-powered investment research assistant using a Retrieval-Augmented Generation (RAG) framework to provide insights from financial data.

---

## About The Project

Capit.ai leverages AI to analyze quantitative stock data. It uses a RAG model to ensure that responses are grounded in factual, up-to-date financial information. This allows users to ask complex questions and receive data-driven answers about specific securities.

### Key Features
* **Data Processing:** Ingests and prepares quantitative stock data for analysis.
* **RAG Framework:** Answers user queries using a knowledge base of processed financial data.
* **CLI Interface:** Simple and direct command-line operation.

---

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites
* Python 3.8+
* API Keys for your financial data provider (if applicable)

### Installation

1.  Clone the repository:
    ```sh
    git clone [https://github.com/](https://github.com/)[your-github-username]/capit.ai.git
    cd capit.ai
    ```

2.  Install the required packages:

3.  Set up your environment variables by creating a `.env` file and adding any necessary API keys.

---

## Usage

Running the assistant is a two-step process. You must first process the data and then run the query engine.

1.  **Process Financial Data:**
    This script fetches the latest financial data and builds the knowledge base for the AI. Run it first.
    ```sh
    python stockdata.py
    ```

2.  **Query the AI Assistant:**
    Once the data is processed, you can start the RAG assistant to ask questions about various stocks.
    ```sh
    python rag.py
    ```

---

## 🗺️ Roadmap

* [x] Core RAG Framework for Quantitative Data
* [x] Initial Data Processing Scripts
* [ ] Integrate Real-time News & Sentiment Analysis
* [ ] Develop an Interactive Web Dashboard
* [ ] Implement Advanced Risk Modeling

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
