// Deployment configuration
const isProduction = process.env.NODE_ENV === 'production';
const vercelUrl = process.env.VERCEL_URL;

// API base URL configuration
let API_BASE;
if (isProduction && vercelUrl) {
    // When deployed on Vercel, API routes are at /api
    API_BASE = `https://${vercelUrl}/api`;
} else if (isProduction) {
    // Production but not on Vercel - you'll need to set this
    API_BASE = process.env.API_BASE_URL || 'https://your-domain.com/api';
} else {
    // Development - local backend
    API_BASE = 'http://localhost:8080';
}

export { API_BASE };