import os
import base64
import json
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import uvicorn
from pathlib import Path


app = FastAPI(title="Java Bridge Coffee Bio Scanner", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Gemini
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

ANALYSIS_PROMPT = """
You are an expert FDA-inspired coffee bean biosecurity analyst with deep knowledge of:
- SCA (Specialty Coffee Association) quality standards
- FDA food safety protocols for imported goods
- Indonesian coffee varieties (Arabica from East Java, Sumatra, Sulawesi)
- Coffee bean defect classification
- Moisture content analysis
- Microbial risk assessment

Analyze this coffee bean image and provide a STRICT JSON response (no markdown, just JSON):
{
  "overall_score": <0-100>,
  "grade": "<Specialty/Premium/Commercial/Below Grade>",
  "moisture_content": {
    "estimate": "<10-12.5% optimal range or specific estimate>",
    "status": "<OPTIMAL/HIGH/LOW/CRITICAL>",
    "risk_level": "<LOW/MEDIUM/HIGH>"
  },
  "bacterial_risk": {
    "level": "<LOW/MEDIUM/HIGH/CRITICAL>",
    "indicators": "<visible signs or absence of bacterial contamination>",
    "recommendation": "<specific action>"
  },
  "mold_detection": {
    "detected": <true/false>,
    "type": "<Aspergillus/Fusarium/None/Suspected>",
    "severity": "<NONE/TRACE/MILD/SEVERE>"
  },
  "defect_analysis": {
    "primary_defects": ["<list visible defects>"],
    "secondary_defects": ["<list minor defects>"],
    "defect_count_estimate": "<per 300g sample estimate>",
    "sca_category": "<SCA Grade 1/2/3>"
  },
  "visual_quality": {
    "color": "<color description>",
    "uniformity": "<High/Medium/Low>",
    "size_consistency": "<High/Medium/Low>",
    "surface_texture": "<description>"
  },
  "origin_indicators": {
    "likely_origin": "<country/region if identifiable>",
    "processing_method": "<Washed/Natural/Honey/Unknown>",
    "variety_estimate": "<Arabica/Robusta/Blend/Unknown>"
  },
  "fda_compliance": {
    "import_eligible": <true/false>,
    "concerns": ["<list any FDA concerns>"],
    "action_required": "<NONE/MONITOR/TREAT/REJECT>"
  },
  "recommendations": [
    "<actionable recommendation 1>",
    "<actionable recommendation 2>",
    "<actionable recommendation 3>"
  ],
  "summary": "<2-3 sentence executive summary for supply chain decision makers>"
}

Be specific, professional, and actionable. Base analysis on visible characteristics.
"""

@app.get("/", response_class=HTMLResponse)
async def root():
    html_path = Path("templates/index.html")
    if html_path.exists():
        return HTMLResponse(content=html_path.read_text())
    return HTMLResponse(content="<h1>Coffee Bio Scanner - Server Running</h1>")

@app.post("/analyze")
async def analyze_coffee(image: UploadFile = File(...)):
    if not GOOGLE_API_KEY:
        raise HTTPException(status_code=500, detail="GOOGLE_API_KEY not configured")
    
    # Read and validate image
    contents = await image.read()
    if len(contents) > 10 * 1024 * 1024:  # 10MB limit
        raise HTTPException(status_code=400, detail="Image too large (max 10MB)")
    
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    try:
        # Encode image for Gemini
        image_data = base64.b64encode(contents).decode("utf-8")
        
        # Create Gemini request with image
        response = model.generate_content([
            ANALYSIS_PROMPT,
            {
                "mime_type": image.content_type,
                "data": image_data
            }
        ])
        
        # Parse JSON response
        response_text = response.text.strip()
        # Clean up markdown code blocks if present
        if response_text.startswith("```"):
            response_text = response_text.split("```")[1]
            if response_text.startswith("json"):
                response_text = response_text[4:]
        response_text = response_text.strip()
        
        analysis = json.loads(response_text)
        analysis["filename"] = image.filename
        analysis["file_size"] = len(contents)
        
        return JSONResponse(content={"success": True, "analysis": analysis})
        
    except json.JSONDecodeError as e:
        # Return raw text if JSON parsing fails
        return JSONResponse(content={
            "success": True,
            "analysis": {
                "summary": response.text,
                "raw_response": True
            }
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "api_key_configured": bool(GOOGLE_API_KEY)}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
