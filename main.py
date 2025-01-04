from app import create_app

app = create_app()

# This is the function that will be called by Cloud Functions
def chat(request):
    """
    Cloud Functions entry point
    
    Args:
        request (flask.Request): The request object
        
    Returns:
        The response from your Flask app
    """
    with app.request_context(request.environ):
        return app(request.environ, lambda x, y: y) 