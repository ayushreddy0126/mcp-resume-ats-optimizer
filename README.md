# 🚀 MCP Resume ATS Optimizer

**AI-Powered Resume Tailoring Tool** — built using the Model-Compute-Platform (MCP) architecture to help users optimize their resumes for job descriptions and beat Applicant Tracking Systems (ATS).

![UI Preview](assets/ats-ui-preview.png)

---

## 📌 What It Does

This tool allows users to:
- ✅ Upload their existing resume (PDF)
- ✍️ Paste a job description from any job portal
- 🧠 Use an LLM to tailor the resume for better ATS match
- 📝 Edit the result in a clean Streamlit UI before saving

---

## 🔥 Features

- 🎯 **Job-Aware Resume Rewriting**
- 📄 **PDF Resume Parsing** (via `pdfplumber`)
- 🤖 **OpenAI LLM Integration**
- 🧠 **ATS Optimization Tips** (coming soon)
- ✂️ **Section-wise Editing** (coming soon)
- 🖤 **Beautiful Dark Mode UI**

---

## 🧱 Tech Stack

| Layer       | Tech                              |
|------------|------------------------------------|
| 🧠 LLM      | OpenAI (GPT-3.5 / GPT-4)           |
| 🖥 Backend  | FastAPI                            |
| 🧰 Parsing  | pdfplumber                         |
| 🖼 Frontend | Streamlit                          |
| 🔗 Infra    | Model-Compute-Platform (MCP) style |

---

## 🧰 Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/ayushreddy0126/mcp-resume-ats-optimizer.git
cd mcp-resume-ats-optimizer

# 2. Setup virtual environment
python3 -m venv env
source env/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your OpenAI API key in a `.env` file
echo "OPENAI_API_KEY=sk-..." > .env

# 5. Start the backend
uvicorn app.main:app --reload --port 8002

# 6. Start the frontend
streamlit run frontend/streamlit_app.py
