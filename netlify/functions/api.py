import os
import sys
import json
import logging

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Import the main API handler
from api.index import handler

def lambda_handler(event, context):
    """Netlify Function wrapper for the API"""
    # Convert Netlify event format to our handler format
    http_method = event.get('httpMethod', 'GET')
    path = event.get('path', '/')
    
    # Handle base path removal for Netlify functions
    if path.startswith('/.netlify/functions/api'):
        path = path.replace('/.netlify/functions/api', '')
    if path.startswith('/api'):
        path = path.replace('/api', '')
    
    # Ensure path starts with /
    if not path.startswith('/'):
        path = '/' + path
    
    # Prepare the event for our handler
    handler_event = {
        'httpMethod': http_method,
        'path': path,
        'body': event.get('body'),
        'headers': event.get('headers', {}),
        'queryStringParameters': event.get('queryStringParameters', {})
    }
    
    try:
        # Call the main handler
        response = handler(handler_event, context)
        
        # Convert response format for Netlify
        netlify_response = {
            'statusCode': response['statusCode'],
            'headers': response.get('headers', {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
            }),
            'body': response['body']
        }
        
        return netlify_response
        
    except Exception as e:
        logging.error(f"Error in Netlify function: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
            },
            'body': json.dumps({
                'error': 'Internal server error',
                'message': str(e),
                'success': False
            })
        }