from flask import Blueprint, request, jsonify
from app.openai_client import get_openai_response

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/api/openai/chat', methods=['POST'])
def openai_chat():
    try:
        data = request.json
        messages = data.get('messages', [])
        
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
