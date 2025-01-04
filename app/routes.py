from flask import Blueprint, request, jsonify, render_template
from app.openai_client import get_openai_response

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
            return jsonify({"error": "Invalid JSON"}), 400
            
        messages = data.get('messages', [])
        if not isinstance(messages, list):
            return jsonify({"error": "Messages must be a list"}), 400
        
        if not messages:
            return jsonify({"error": "Messages list is required"}), 400

        response = get_openai_response(messages)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main_blueprint.route('/api/hello', methods=['GET'])
def hello_world():
    name = request.args.get('name', 'World')
    return jsonify(message=f"Hello, {name}!")
