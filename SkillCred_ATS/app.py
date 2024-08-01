import os
import google.generativeai as genai
import streamlit as st
import PyPDF2 as pdf

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#response
def get_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# prompt template
prompt_template = """
Act like a skilled or very experienced Application Tracking System (ATS) with a deep understanding in the field of tech, software engineering, data science, data analysis, and big data engineer. Your task will be to analyse/evaluate resume based on the given Job Description. You DO NOT RETURN THE RESUME OR THE JOB DESCRIPTION PROVIDED, ONLY THE OUTPUT THAT IS REQUIRED. Always consider that the job market is highly competetive and must provide the best assisstance for improving their resumes. Assign the percentage Matching based on Jd (job description), missing keywords and CV score (out of 5) with high accuracy. Here's the data: resume={text}, job description={jd}.

I require the response in the following format:

"Description Match" : "%",
"Missing Keywords" : [],
"Profile Summary" : "",
"CV Score" : "",
"Additional Feedback : "".
"""

#setting up streamlit app.
st.title("Elevate your chances of getting hired through our super app 🔍")
st.markdown("**Improve your resume ATS**")
jd = st.text_area("Job Description:")
uploaded_file = st.file_uploader("Upload your Resume", type=["pdf"], help="Upload pdf of your resume")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        resp = get_response(prompt_template)
        st.subheader(resp)
