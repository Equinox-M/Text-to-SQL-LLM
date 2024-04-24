import streamlit as st
import sqlite3
import os
from dotenv import load_dotenv 
import google.generativeai as genai
#Load all the environment variables
load_dotenv()
# Configuration Genai key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to Load Google Gemini 
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the database
def read_sql_query(sql, db):
    connection = sqlite3.connect(db)
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        data_rows = cursor.fetchall()
        connection.commit()  # Commit changes if any
        return data_rows
    finally:
        connection.close()

# Define Your Prompt
prompt = [
    """
You are an expert in converting English questions to SQL code!
The SQL database has the name STUDENT and has the following Columns - NAME, CLASS, SECTION

For example:
- How many entries of records are present? SQL command: SELECT COUNT(*) FROM STUDENT;
- Tell me all the students studying in Data Science class? SQL command: SELECT * FROM STUDENT where CLASS="Data Science";

Also, the SQL code should not have ''' in the beginning or at the end, and SQL word in output.
    """
]

# Setting up the Streamlit App 
st.set_page_config(page_title="Gemini App: Convert Text to SQL", layout="wide")

# Define layout
st.markdown("# Gemini App For Converting Text to SQL 🌐🗄️")
st.markdown("### Enter Your Question")
question = st.text_input("Input: ", key="input")
submit = st.button("Submit")

# Show generated SQL query and query results
if submit:
    ai_response = get_gemini_response(question, prompt)
    st.markdown("## Generated SQL Query")
    st.code(ai_response)

    try:
        sql_response = read_sql_query(ai_response, "student.db")

        st.markdown("## Query Results")
        if len(sql_response) > 0:
            # Display results as a table
            st.table(sql_response)
        else:
            st.write("No results found.")
        
        # Check if the SQL query is a data manipulation query
        if ai_response.strip().lower().startswith(("insert", "update", "delete")):
            # Add message indicating successful execution for data manipulation queries
            st.success("Query execution successful.")
    except Exception as e:
        st.error("Error executing SQL query:", e)
