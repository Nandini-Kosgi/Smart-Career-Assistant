🚀 Smart Career Assistant

Smart Career Assistant is an AI-powered job application tool built with Streamlit and Google Gemini.
It helps job seekers optimize their applications by:
✅ Scoring resumes against job descriptions
✅ Suggesting tailored resume bullet points
✅ Drafting personalized cover letters
✅ Exporting structured JSON outputs for tracking





✨ Features

•	Resume–JD Match Scoring → Get a % alignment score with gap analysis
•	Resume Optimization → Generate tailored bullets to fill missing skills
•	Cover Letter Generator → Draft professional, personalized cover letters
•	Automation-Ready Output → Save results in structured JSON format





🛠️ Tech Stack

•	Frontend/UI: Streamlit
•	LLM Backend: Google Gemini (gemini-1.5-flash)
•	Language: Python 3.9+
•	Other tools: Jupyter Notebook (exploration), JSON for outputs





📂 Project Structure
Smart-Career-Assistant/
│
├── app.py                       # Main Streamlit app
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
│
├── notebooks/
│   └── gen-ai-job-application-assistant.ipynb   # Exploration \& testing
│
├── data/
│   ├── sample\_resume.txt        # Example resume
│   └── sample\_jd.txt            # Example job description
│
├── outputs/
│   └── output.json              # Generated JSON output



⚡ Getting Started

1. Clone the repo
   git clone https://github.com/your-username/Smart-Career-Assistant.git
   cd Smart-Career-Assistant
2. Install dependencies
   pip install -r requirements.txt
3. Set up Gemini API Key
   Get an API key from Google AI Studio and Add it to your environment:
4. Run the Streamlit app



📊 Example Workflow

1. Paste your resume and the job description into the app.
2. Click Generate.
3. Instantly receive:
   o	Match Score (%)
   o	Resume bullet suggestions
   o	Draft cover letter
   o	JSON output



🎯 Future Enhancements
•	Add LinkedIn/Indeed job description scraper
•	Integrate with Google Sheets for tracking applications
•	Support multiple resumes \& bulk JD comparison
•	Enhance prompts with RAG (resume + portfolio grounding)


👩‍💻 Author
Nandini Kosgi
📌 AI Engineer| 5+ years experience
🔗 LinkedIn: https://www.linkedin.com/in/nandinikosgi/

