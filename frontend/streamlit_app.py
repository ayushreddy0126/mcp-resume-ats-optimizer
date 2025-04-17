import streamlit as st
import requests
import pdfplumber
import io

# Must be first!
st.set_page_config(page_title="ATS Resume Optimizer", layout="centered")

# Inject Cursor-style dark theme
st.markdown("""
    <style>
    html, body, [class*="css"] {
        background-color: #0d1117;
        color: #f0f6fc;
        font-family: 'Inter', sans-serif;
    }
    .stTextInput>div>div>input,
    .stTextArea>div>textarea,
    .stFileUploader>div {
        background-color: #161b22;
        color: #f0f6fc;
        border: 1px solid #30363d;
        border-radius: 8px;
    }
    .stButton>button {
        background-color: #238636;
        color: white;
        padding: 0.6em 1.2em;
        border: none;
        border-radius: 6px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #2ea043;
        transition: 0.3s ease;
    }
    .css-1v0mbdj.edgvbvh3 { color: white; }
    .stSpinner > div > div { color: white; }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='font-size: 3rem; font-weight: 700;'>📄 ATS Resume Optimizer</h1>", unsafe_allow_html=True)

# Upload section
uploaded_pdf = st.file_uploader("📎 Upload your current resume (PDF only)", type=["pdf"])

# Job description input
job_description = st.text_area("📌 Paste the Job Description here", height=200)

resume_text = ""
if uploaded_pdf is not None:
    with pdfplumber.open(io.BytesIO(uploaded_pdf.read())) as pdf:
        resume_text = "\n".join(page.extract_text() or "" for page in pdf.pages)

    st.markdown("### 📝 Parsed Resume (editable):")
    resume_text = st.text_area("✏️ Edit Resume Before Optimization", resume_text, height=400)

# Button
if st.button("🚀 Optimize Resume"):
    if not resume_text.strip() or not job_description.strip():
        st.warning("⚠️ Please upload a resume and paste the job description.")
    else:
        with st.spinner("Optimizing your resume with LLM magic..."):
            try:
                uploaded_pdf.seek(0)  # reset pointer for API
                files = {"resume_file": uploaded_pdf}
                data = {"job_description": job_description}

                response = requests.post("http://127.0.0.1:8002/resume/tailor", files=files, data=data)
                response.raise_for_status()
                result = response.json()

                tailored = result.get("tailored_resume", "")
                if tailored:
                    st.markdown("### ✅ Optimized Resume")
                    st.text_area("🎯 Tailored Resume Output", tailored, height=600)
                else:
                    st.warning("🕵️ No output returned. Try again with different input.")

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
