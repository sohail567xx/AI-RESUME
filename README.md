# AI-RESUME
# 🚀 Intelligent AI Resume Screener

An end-to-end AI-powered resume screening system that automatically analyzes resumes against job descriptions, extracts skills, computes semantic match scores, and recommends hiring decisions — all through a clean, recruiter-friendly interface.

---

## ✨ Features

* 📄 Resume parsing (PDF & DOCX)
* 🧠 Semantic similarity scoring using Sentence Transformers
* 🏷️ Automatic skill extraction
* ❗ Missing skill detection
* 🎯 Match percentage with hiring recommendation
* ⚡ Fast, lightweight model (CPU-friendly)
* 🎨 Modern Streamlit UI (deployable on Hugging Face Spaces)
* 🔌 Modular backend pipeline for future API scaling

---

## 🧠 How It Works

```
Resume Upload → Text Extraction → Skill Detection → Embedding Model → Similarity Score → Hiring Decision
```

The system uses **sentence-transformers (all-MiniLM-L6-v2)** to compute semantic similarity between the resume and job description.

---

## 🏗️ Tech Stack

| Layer          | Technology                       |
| -------------- | -------------------------------- |
| Language       | Python                           |
| NLP Model      | sentence-transformers            |
| Similarity     | cosine similarity (scikit-learn) |
| Resume Parsing | pdfplumber, python-docx          |
| Frontend       | Streamlit                        |
| Deployment     | Hugging Face Spaces              |
| Optional API   | FastAPI (future-ready)           |

---

## 📂 Project Structure

```
ai-resume-screener/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Dependencies
├── AI_RESUME.ipynb       # Original Colab backend prototype
└── README.md             # Project documentation
```

---

## ⚙️ Installation (Local Setup)

Clone the repository:

```bash
git clone https://github.com/your-username/ai-resume-screener.git
cd ai-resume-screener
```

Create virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

---

## 🚀 Deployment on Hugging Face Spaces

1. Create a new Space on Hugging Face

   * SDK: **Streamlit**
   * Hardware: **CPU Basic**

2. Upload:

```
app.py
requirements.txt
```

3. Wait for auto-build (2–4 minutes)

Your app will be live at:

```
https://huggingface.co/spaces/<your-username>/<space-name>
```

---

## 📊 Output Example

The system returns:

* ✅ Match Score (%)
* 🧠 Hiring Decision
* 🏷️ Extracted Resume Skills
* ❌ Missing Skills

---

## 🔧 Configuration

You can expand the skill database inside:

```python
COMMON_SKILLS = [...]
```

For domain-specific hiring (e.g., Data Science, Web Dev).

---

## 🧪 Model Details

* **Model:** all-MiniLM-L6-v2
* **Type:** Sentence embedding model
* **Why chosen:**

  * Fast on CPU
  * Lightweight
  * Strong semantic performance
  * HF Spaces compatible

---

## 🚧 Limitations

* Skill matching is keyword-based (can be improved with NER)
* Not a full ATS replacement
* Large PDFs may increase processing time
* Currently single-resume analysis

---

## 🔮 Future Improvements

* 🔥 Multi-resume ranking dashboard
* 🤖 LLM-based resume feedback
* 📈 ATS keyword scoring
* 🧑‍💼 Recruiter analytics panel
* 📥 Downloadable PDF report
* 🌐 Separate FastAPI backend
* 🧠 Advanced skill ontology

---

## 🤝 Contributing

Contributions are welcome.

Steps:

1. Fork the repo
2. Create feature branch
3. Commit changes
4. Open pull request

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use and modify.

---

## ⭐ If This Helped

Consider giving the repo a star — it helps visibility and motivates further development.

---

**Built for intelligent hiring and AI-powered recruitment workflows.**
