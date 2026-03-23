# ☕ Java Bridge Coffee Bio Scanner

## FDA-Inspired AI Coffee Bean Quality Analyzer

**Created by Christopher Parker | Java Bridge Coffee**

*First-to-Market AI-Powered Coffee Bean Biosecurity Scanner for Indonesia-US Trade*

## 🎯 Project Overview

Full-stack AI prototype using **Google Gemini 1.5 Flash** (free tier) for comprehensive coffee bean quality analysis inspired by FDA food safety protocols and SCA standards.

### Key Features
- 📸 Camera Capture + File Upload (mobile/desktop)
- 🔬 7-Point Agentic Analysis (moisture, bacteria, mold, defects, quality, origin, recommendations)
- 🧬 FDA-Compliant Methodology
- ⚡ Real-Time Results (sub-5-second)
- 🌏 Built for Indonesian Coffee Trade

## 🧪 Analysis Capabilities

1. **Moisture Content** (10-12.5% optimal)
2. **Bacterial Risk** (LOW/MEDIUM/HIGH)
3. **Mold Detection** (Aspergillus, Fusarium)
4. **SCA Defect Classification**
5. **Quality Grading** (0-100 score)
6. **Origin Indicators**
7. **Actionable Recommendations**

## 🛠️ Tech Stack

**Backend:** FastAPI + Google Gemini 1.5 Flash + Uvicorn
**Frontend:** Vanilla JavaScript + HTML/CSS
**Deployment:** Google Cloud Run / Ngrok

## 📦 Installation

```bash
git clone https://github.com/peterparker1718/coffee-bio-scanner.git
cd coffee-bio-scanner
pip install -r requirements.txt
export GOOGLE_API_KEY="your-key"
python main.py
```

Open http://localhost:8000

## 🌍 Business Context

**Java Bridge Coffee** - Direct-trade specialty coffee importer connecting US buyers with East Java growers.

This tool demonstrates:
- Supply Chain Transparency
- FDA-Aligned Biosecurity
- First-Mover Advantage
- Family Network in Dampit, Lumajang, Mount Ijen

### Use Cases
1. Pre-Export Quality Control
2. Import Verification
3. B2B Sales Tool
4. LinkedIn Portfolio Showcase

## 🔐 API

`GET /` - Web interface
`POST /analyze` - Upload image, receive JSON analysis

## 👤 Author

**Christopher Parker**
Founder, Java Bridge Coffee
📧 christopher@parkersportfolio.info
💼 [LinkedIn](https://linkedin.com/in/christopherparker)
🐙 [GitHub](https://github.com/peterparker1718)

*Built in Belmar, NJ | Powered by Indonesian Coffee Passion*

## 📄 License

MIT License - Free to use with attribution

**⭐ Star this repo if you're building AI-powered supply chain tools!**
