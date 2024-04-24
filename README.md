# Text-to-SQL Gemini App

## Overview
This project aims to provide a streamlined solution for converting English questions into SQL queries using Google's Generative AI (Gemini). With this app, users can input natural language questions related to a hypothetical student database and receive corresponding SQL queries. Additionally, the app displays query results if applicable.[Preview](https://huggingface.co/spaces/Equinox-M/Text-To-SQL-Gemini-Model)

![Screenshot 2024-04-24 at 10 35 35 AM](https://github.com/Equinox-M/Text-to-SQL-LLM/assets/92346639/c5b75f74-422c-401b-a49b-61b248b1f9ce)

## Features
- Conversion of English questions to SQL queries
- Retrieval of query results from a SQLite database
- User-friendly Streamlit interface

## Setup
To run this project locally, follow these steps:

### Prerequisites
- Python 3.x installed on your system
- Pip package manager

### Installation
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the App
1. Ensure your Google API key is configured in a `.env` file at the root of the project.
2. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
3. Access the app through your browser.

## Project Structure

--- venv/

--- .env 

--- .gitignore

--- app.py 

--- requirements.txt 

--- sqlite.py 


## Usage
1. Input your question in the provided text box.
2. Click the "Submit" button to generate the corresponding SQL query.
3. View the generated SQL query and, if applicable, the query results below.
4. For data manipulation queries (e.g., INSERT, UPDATE, DELETE), a success message will be displayed upon execution.

## Example
For example questions and their corresponding SQL queries, refer to the predefined prompt in the `app.py` file.
