# Smart ATS App 🔍

## Overview
Smart ATS App is an Application Tracking System (ATS) designed to assist job seekers in improving their resumes by analyzing and evaluating them against job descriptions. This application leverages the Gemini Pro API for natural language processing and Streamlit for the frontend interface.

## Features
- **Resume Analysis**: Upload your resume in PDF format and get a detailed analysis based on the provided job description.
- **Job Description Matching**: The system provides a percentage match of your resume against the job description.
- **Keyword Identification**: Identifies missing keywords in your resume that are crucial for the job.
- **Profile Summary**: Generates a summary of your profile based on the resume and job description.
- **CV Scoring**: Scores your CV out of 5 based on the job description.
- **Additional Feedback**: Provides additional feedback for improving your resume.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Udaychauhan1724/SkillCred_ATS
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up the environment variables:
    - Create a `.env` file in the root directory.
    - Add your Google API key:
    ```plaintext
    GOOGLE_API_KEY=your_api_key_here
    ```

## Usage
1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
2. Open your web browser and navigate to `http://localhost:8501`.

## Code Explanation
### Import Libraries
```python
import os
import google.generativeai as genai
import streamlit as st
import PyPDF2 as pdf
from dotenv import load_dotenv
```
- **os**: For accessing environment variables.
- **google.generativeai**: For interacting with the Gemini Pro API.
- **streamlit**: For creating the web interface.
- **PyPDF2**: For reading PDF files.
- **dotenv**: For loading environment variables from a `.env` file.

### Load Environment Variables
```python
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
```
- Loads the API key from the `.env` file and configures the Gemini Pro API.

### Define Functions
- **get_response**: Sends a prompt to the Gemini Pro API and returns the response.
- **input_pdf_text**: Reads and extracts text from an uploaded PDF file.

### Prompt Template
Defines the template for the prompt sent to the Gemini Pro API for analyzing the resume.

### Streamlit App Setup
Sets up the Streamlit app interface with title, input fields, and a submit button.

### Submit Button Action
Handles the resume upload, sends the prompt to the Gemini Pro API, and displays the response.

## requirements.txt
```
streamlit
PyPDF2
google.generativeai
python-dotenv
```