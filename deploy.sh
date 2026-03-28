#!/bin/bash
# Deploy Coffee Bio Scanner to Google Cloud Run
# Usage: ./deploy.sh [PROJECT_ID] [GOOGLE_API_KEY]

set -euo pipefail

PROJECT_ID="${1:-$(gcloud config get-value project)}"
REGION="us-east1"
SERVICE_NAME="coffee-bio-scanner"
IMAGE="gcr.io/${PROJECT_ID}/${SERVICE_NAME}"

echo "🚀 Deploying ${SERVICE_NAME} to Google Cloud Run..."
echo "   Project: ${PROJECT_ID}"
echo "   Region:  ${REGION}"

# Build and push
gcloud builds submit --tag "${IMAGE}" --project "${PROJECT_ID}"

# Deploy to Cloud Run
gcloud run deploy "${SERVICE_NAME}" \
  --image "${IMAGE}" \
  --platform managed \
  --region "${REGION}" \
  --allow-unauthenticated \
  --memory 512Mi \
  --cpu 1 \
  --min-instances 0 \
  --max-instances 10 \
  --timeout 120 \
  --set-env-vars "GOOGLE_API_KEY=$(gcloud secrets versions access latest --secret=gemini-api-key --project=${PROJECT_ID} 2>/dev/null || echo 'SET_YOUR_KEY')" \
  --project "${PROJECT_ID}"

echo "✅ Deployed! URL:"
gcloud run services describe "${SERVICE_NAME}" --platform managed --region "${REGION}" --format 'value(status.url)' --project "${PROJECT_ID}"
