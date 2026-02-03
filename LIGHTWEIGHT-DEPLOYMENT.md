# Lightweight Humanizer - External API Version

This version uses external AI APIs instead of local models to avoid size limits.

## Setup Instructions:

1. **Get API keys:**
   - Hugging Face: https://huggingface.co/settings/tokens
   - OpenAI: https://platform.openai.com/api-keys
   - Anthropic: https://console.anthropic.com/

2. **Set environment variables in Vercel:**
   ```
   HF_API_TOKEN=your_huggingface_token
   OPENAI_API_KEY=your_openai_key
   ANTHROPIC_API_KEY=your_anthropic_key
   ```

3. **Deploy normally** - Function size will be under 10MB!

## Benefits:
✅ Under Vercel size limits
✅ No model management
✅ Automatic scaling
✅ Reduced deployment complexity
✅ Pay-per-use pricing

## External Services Used:
- Hugging Face Inference API (free tier available)
- OpenAI GPT models (paid)
- Anthropic Claude (paid)