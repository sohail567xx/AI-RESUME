# app.py
import streamlit as st
import pdfplumber
import docx
import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="🚀",
    layout="wide"
)

# ---------------- PREMIUM CSS ----------------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: white;
}
.block-container {
    padding-top: 2rem;
}
.glass {
    background: rgba(255,255,255,0.07);
    padding: 28px;
    border-radius: 22px;
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.1);
}
.title {
    font-size: 52px;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(90deg,#38bdf8,#a78bfa,#f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.stButton>button {
    height: 60px;
    font-size: 20px;
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# ---------------- SKILLS DATABASE ----------------
COMMON_SKILLS = [
    "python","java","c++","c","machine learning","deep learning",
    "sql","tensorflow","pytorch","nlp","data analysis",
    "react","node","aws","docker","kubernetes","html","css",
    "javascript","pandas","numpy","flask","fastapi"
]

# ---------------- HELPERS ----------------
def extract_text(file):
    text = ""
    if file.name.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    text += t + "\n"
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        text = "\n".join(p.text for p in doc.paragraphs)
    return text

def extract_skills(text):
    text_lower = text.lower()
    return sorted([
        skill for skill in COMMON_SKILLS
        if re.search(r"\b" + re.escape(skill) + r"\b", text_lower)
    ])

def match_score(resume_text, jd_text):
    r = model.encode([resume_text])
    j = model.encode([jd_text])
    score = cosine_similarity(r, j)[0][0]
    return round(score * 100, 2)

def decision(score):
    if score >= 75:
        return "✅ Strong Match — Shortlist"
    elif score >= 50:
        return "⚠️ Moderate Match — Review"
    return "❌ Low Match — Reject"

# ---------------- UI ----------------
st.markdown('<div class="title">🚀 Intelligent AI Resume Screener</div>', unsafe_allow_html=True)
st.write("")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    resume_file = st.file_uploader("📄 Upload Resume", type=["pdf","docx"])
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    jd_text = st.text_area("🧠 Paste Job Description", height=220)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")

if st.button("🔥 Analyze Candidate", use_container_width=True):
    if resume_file and jd_text:

        resume_text = extract_text(resume_file)

        score = match_score(resume_text, jd_text)
        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd_text)
        missing_skills = sorted(list(set(jd_skills) - set(resume_skills)))

        st.write("---")
        c1, c2, c3 = st.columns(3)

        c1.metric("🎯 Match Score", f"{score}%")
        c2.metric("🧠 Decision", decision(score))
        c3.metric("❗ Missing Skills", len(missing_skills))

        st.write("### ✅ Resume Skills")
        st.write(resume_skills)

        st.write("### ❌ Missing Skills")
        st.write(missing_skills)

    else:
        st.warning("Please upload resume and paste job description.")
