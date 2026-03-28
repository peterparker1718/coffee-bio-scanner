# Coffee Bio Scanner — AI-Powered Coffee Bean Quality Analyzer

> FDA-inspired biosecurity scanner using Google Gemini Vision AI for real-time coffee bean quality grading. Built by Christopher Parker for Java Bridge Coffee.

## Live Demo
🌐 **[coffee-bio-scanner-xxxxx.run.app](https://coffee-bio-scanner-xxxxx.run.app)** *(Update after deployment)*

## Architecture
```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   Browser UI    │────▶│   FastAPI (CR)    │────▶│  Gemini 1.5     │
│   HTML/JS       │     │   Cloud Run       │     │  Flash Vision   │
│                 │◀────│   Auto-scaling    │◀────│  Analysis       │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                              │
                        ┌─────▼─────┐
                        │  GCP      │
                        │  Secret   │
                        │  Manager  │
                        └───────────┘
```

## What It Does
- Upload a coffee bean image → get a comprehensive FDA-style quality report
- SCA-grade scoring (Specialty/Premium/Commercial/Below Grade)
- Moisture content analysis, bacterial risk assessment, mold detection
- Defect classification per SCA standards
- Origin identification and processing method detection
- FDA import compliance assessment

## Tech Stack
| Layer | Technology |
|-------|-----------|
| Backend | FastAPI (Python 3.11) |
| AI/ML | Google Gemini 1.5 Flash Vision API |
| Infrastructure | Google Cloud Run (serverless, auto-scaling) |
| CI/CD | Google Cloud Build + GitHub trigger |
| Secrets | GCP Secret Manager |
| Frontend | Vanilla HTML/JS (lightweight, fast) |

## Run Locally
```bash
git clone https://github.com/peterparker1718/coffee-bio-scanner.git
cd coffee-bio-scanner
pip install -r requirements.txt
export GOOGLE_API_KEY="your_gemini_key"
python main.py
# Open http://localhost:8000
```

## Deploy to Google Cloud
```bash
chmod +x deploy.sh
./deploy.sh YOUR_PROJECT_ID
```

## API Endpoints
| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Landing page |
| GET | `/scanner` | Scanner interface |
| POST | `/analyze` | Upload image for AI analysis |
| GET | `/health` | Health check (Cloud Run) |
| GET | `/founder` | About the founder |

## Key Design Decisions
- **Gemini over OpenAI**: Chose Gemini for native GCP integration and superior vision capabilities for food-safety image analysis
- **FastAPI over Flask**: Async I/O for concurrent image analysis requests; auto-generated OpenAPI docs at `/docs`
- **Cloud Run over App Engine**: Pay-per-request pricing, auto-scales to zero, containerized for portability
- **No frontend framework**: Intentional — the scanner is a backend-focused AI tool, lightweight HTML keeps load time under 100ms

## About
Built by **Christopher Parker** — Founder of [Java Bridge Coffee](https://javabridgecoffee.com), connecting Indonesian coffee producers directly to US buyers. This scanner addresses real supply chain quality control needs in specialty coffee importing.

- GitHub: [@peterparker1718](https://github.com/peterparker1718)
- Portfolio: [parkersportfolio.info](https://parkersportfolio.info)

---
*First-to-market AI biosecurity scanner for coffee supply chain. MIT License.*
