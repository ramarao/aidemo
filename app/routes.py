import logging
import traceback
from flask import Blueprint, request, jsonify, render_template
from app.openai_client import get_openai_response
import datetime
import os
import sys
import pkg_resources

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/', methods=['GET'])
def index():
    """
    Serve the index page
    """
    if request.headers.get('Accept', '').find('application/json') != -1:
        # Return JSON if requested
        return jsonify({
            "status": "online",
            "endpoints": {
                "chat": "/api/openai/chat",
                "hello": "/api/hello"
            }
        })
    # Otherwise return HTML
    return render_template('index.html')

@main_blueprint.route('/api/openai/chat', methods=['POST'])
def openai_chat():
    """
    Handle chat requests to OpenAI API.
    
    Expected JSON body:
    {
        "messages": [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"}
        ]
    }
    
    Returns:
        JSON response from OpenAI API or error message
    """
    try:
        data = request.json
        if data is None:
            logger.error("Invalid JSON received")
            return jsonify({"error": "Invalid JSON"}), 400
            
        messages = data.get('messages', [])
        if not isinstance(messages, list):
            logger.error(f"Invalid messages format: {messages}")
            return jsonify({"error": "Messages must be a list"}), 400
        
        if not messages:
            logger.error("Empty messages list received")
            return jsonify({"error": "Messages list is required"}), 400

        logger.info(f"Processing chat request with {len(messages)} messages")
        response = get_openai_response(messages)
        return jsonify(response), 200
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({"error": str(e)}), 500

@main_blueprint.route('/api/hello', methods=['GET'])
def hello_world():
    name = request.args.get('name', 'World')
    return jsonify(message=f"Hello, {name}!")

@main_blueprint.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify service status
    """
    try:
        # Add any critical dependency checks here
        return jsonify({
            "status": "healthy",
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "version": os.environ.get('VERSION', 'unknown')
        }), 200
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return jsonify({
            "status": "unhealthy",
            "error": str(e)
        }), 500

@main_blueprint.route('/debug/config', methods=['GET'])
def debug_config():
    """
    Debug endpoint to verify configuration
    Only available in development
    """
    if not app.debug:
        return jsonify({"error": "Only available in debug mode"}), 403
        
    return jsonify({
        "environment": os.environ.get('ENVIRONMENT', 'unknown'),
        "python_version": sys.version,
        "dependencies": pkg_resources.working_set.by_key.keys(),
    })
