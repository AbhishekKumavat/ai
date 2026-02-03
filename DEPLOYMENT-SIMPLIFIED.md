# Simplified Deployment Version

This version uses external APIs for AI models to avoid deployment size issues.

## Key Changes

1. **External Model APIs**: Uses Hugging Face Inference API instead of local models
2. **Reduced Deployment Size**: Only includes lightweight code
3. **Vercel Compatible**: Well within size limits

## Setup Instructions

### 1. Get Hugging Face API Token

1. Sign up at [huggingface.co](https://huggingface.co)
2. Get your API token from Settings → Access Tokens
3. Add as environment variable: `HF_API_TOKEN`

### 2. Update Configuration

Set these environment variables in Vercel:

```
HF_API_TOKEN=your_huggingface_token_here
NODE_ENV=production
```

### 3. Deploy

```bash
# Using Vercel CLI
vercel --prod

# Or connect GitHub repo to Vercel dashboard
```

## Benefits

✅ **Small deployment size** (< 10MB)
✅ **No model management** 
✅ **Automatic scaling**
✅ **Reduced costs**
✅ **Faster deployment**

## Limitations

⚠️ **API costs**: Pay-per-use pricing from Hugging Face
⚠️ **Internet dependency**: Requires stable internet connection
⚠️ **Rate limits**: May have usage quotas

## Alternative External Services

You can also use:
- **OpenAI API** (GPT models)
- **Anthropic Claude API** 
- **Google Vertex AI**
- **AWS Bedrock**

Just modify the API calls in the Python code accordingly.