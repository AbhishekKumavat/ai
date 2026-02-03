# Humanizer - Vercel Deployment Guide

This guide explains how to deploy the Humanizer application to Vercel.

## Deployment Structure

The application is structured for Vercel deployment with:
- **Frontend**: SvelteKit application in the `frontend/` directory
- **Backend**: Python Flask API converted to Vercel serverless functions in the `api/` directory
- **Models**: Pre-downloaded transformer models (must be included in deployment)

## Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **Node.js**: Version 16+ for frontend build
3. **Python**: Version 3.8+ for backend functions

## Deployment Steps

### 1. Prepare the Project

The project structure should look like this:
```
humanizer/
├── api/
│   └── index.py          # Main Vercel serverless function
├── frontend/
│   ├── src/
│   ├── package.json
│   └── ...               # SvelteKit files
├── paraphraser.py        # Python modules
├── rewriter.py
├── detector.py
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel configuration
└── README.md
```

### 2. Install Dependencies Locally

```bash
# Install frontend dependencies
cd frontend
npm install

# Install Python dependencies (for local testing)
pip install -r requirements.txt
```

### 3. Download Required Models

Before deployment, you need to download the required models:

```bash
python download_models.py
```

This will download:
- t5-small
- t5-base
- Vamsi/T5_Paraphrase_Paws
- humarin/chatgpt_paraphraser_on_T5_base

### 4. Deploy to Vercel

#### Option A: Using Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel

# For production deployment
vercel --prod
```

#### Option B: Using Git Integration

1. Push your code to GitHub/GitLab
2. Connect your repository to Vercel
3. Configure the project settings:
   - **Build Command**: `cd frontend && npm run build`
   - **Output Directory**: `frontend/.svelte-kit/build` (or check your svelte config)
   - **Install Command**: `cd frontend && npm install`

### 5. Environment Variables

Set these environment variables in your Vercel project settings:

```
NODE_ENV=production
```

## Important Considerations

### Model Size Limitations

**Warning**: The transformer models are quite large (several hundred MB each). Vercel has deployment size limits:
- **Free tier**: 50MB per function
- **Pro tier**: 250MB per function

### Solutions for Large Models

1. **Model Optimization**: 
   - Use quantized models
   - Remove unnecessary model files

2. **External Model Hosting**:
   - Host models on a separate service (AWS S3, Google Cloud Storage)
   - Load models dynamically at runtime

3. **Alternative Deployment**:
   - Deploy to platforms with higher limits (AWS Lambda, Google Cloud Functions)
   - Use container-based deployment (Vercel Serverless with Docker)

### Recommended Approach

For production deployment, I recommend:

1. **Use a dedicated ML hosting service** like:
   - Hugging Face Inference API
   - AWS SageMaker
   - Google Vertex AI

2. **Modify the code** to load models from external URLs instead of including them in the deployment

3. **Deploy the frontend** on Vercel and the backend on a more suitable platform

## Testing Locally

Before deployment, test the application locally:

```bash
# Start backend (in project root)
python api/index.py

# Start frontend (in frontend directory)
cd frontend
npm run dev
```

## Troubleshooting

### Common Issues

1. **Deployment Size Too Large**: 
   - Remove unused models
   - Use model quantization
   - Split into multiple functions

2. **Cold Start Issues**:
   - Models take time to load on first request
   - Consider keeping functions warm with scheduled requests

3. **Memory Limitations**:
   - Vercel functions have memory limits
   - Large models may exceed available memory

### Monitoring

- Check Vercel logs for deployment errors
- Monitor function execution time and memory usage
- Set up error tracking with services like Sentry

## Alternative Deployment Options

If Vercel proves unsuitable due to model size:

1. **Railway.app** - Better support for ML applications
2. **Render.com** - More generous size limits
3. **Fly.io** - Container-based deployment
4. **AWS Lambda** - With larger storage options
5. **Google Cloud Run** - Container-based with autoscaling

## Support

For issues with deployment, check:
- Vercel documentation: https://vercel.com/docs
- GitHub Issues: [Your repository issues]