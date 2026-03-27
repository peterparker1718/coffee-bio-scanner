# Coffee Bio Scanner (Prototype)

Prototype agentic AI inspection system for supply chain quality screening, biosecurity checks, and logistics decision support.

The current domain example is coffee bean inspection; the architecture is intentionally generalizable to broader inspection workflows (food safety, ag/commodities, warehouse intake, import-export screening).

## What this prototype demonstrates
- Image-based inspection (file upload)
- Agentic workflow: structured reasoning + recommendations
- Backend orchestration via FastAPI
- LLM-backed analysis (Gemini)

## Tech stack
- FastAPI (Python)
- Uvicorn
- Google Gemini SDK

## Run locally
1. Clone the repo:
   ```bash
   git clone https://github.com/peterparker1718/coffee-bio-scanner.git
   cd coffee-bio-scanner
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Gemini API key (from Google AI Studio):
   ```bash
   export GOOGLE_API_KEY="your_key_here"
   ```
4. Run the app:
   ```bash
   python main.py
   ```
   Then open `http://localhost:8000`.

## Notes
- This is a prototype for demonstration/testing. It is not a substitute for accredited lab testing or regulatory certification.
- Outputs should be treated as decision-support, not definitive compliance results.

## License
MIT
