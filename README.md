# Document Querying with LlamaIndex, Chroma, and Gemini

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Applications](#applications)

## Project Overview

This project creates a queryable index of documents using the **Gemini language model** and vector embeddings. It enables users to load documents, store them in a vector database, and query the information efficiently using natural language. The project utilizes libraries such as `llama_index`, `huggingface`, `dotenv`, and `chroma` for document handling, embedding, and querying processes.

## Key Features

- **Vector-based Index**: Create and manage a vector-based index for efficient document queries.
- **Natural Language Queries**: Use natural language to ask questions about the indexed documents.
- **Integration with Gemini**: Easily integrates with the Gemini language model for advanced query handling.
- **Persistent Storage**: Supports persistent storage of vector data using Chroma, allowing for updates and deletions.

## Setup Instructions

### Prerequisites

- Python 3.7 or later
- Pip (Python package installer)

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/queryable-document-index.git
    cd queryable-document-index
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install Dependencies**

    Install the necessary Python libraries for this project:

    ```bash
    pip install docx2txt llama_index huggingface python-dotenv chromadb
    ```

4. **Set Up Environment Variables**

    Create a `.env` file in the root directory with your Gemini API key:

    ```env
    GEMINI_API_KEY=your_actual_gemini_api_key_here
    ```

5. **Create Project Structure**

    - **Create a `data` Directory**: 
      In the VS Code file explorer, right-click and create a new folder named `data`. This will hold the files you want to perform Q&A on.

    - **Add Files to the `data` Folder**: 
      Place the documents you want to query in the `data` folder.

    - **Create `app.py`**: 
      In the root of your project, create a file called `app.py`.

6. **Run the Application**

    Activate the virtual environment (if not already done) and run the app:

    ```bash
    python app.py
    ```

## Usage

- **Start the Application**: Simply run `app.py` to start querying documents in the `data` directory.
- **Query the Documents**: The `query_engine` will process natural language questions and return relevant answers based on the indexed documents.

## Applications

- **Document Retrieval**: Retrieve specific information from large collections of documents.
- **Interactive Q&A Systems**: Implement a system that answers questions about document contents.
- **Data Management**: Efficiently update, delete, and query stored data using vector embeddings.

## Code Files

- **[Main Indexing and Querying Code](app.py)**
- **[Persistent Storage and Query Management](disk.py)**
- **[Update and Delete Functionality](operation.py)**

## Additional Notes

- Ensure the documents in the `data` folder are in a format compatible with `docx2txt`.
- You can update and delete entries in the Chroma vector store as needed.
- Experiment with different queries and documents to explore the full capabilities of the system.
