# Flask API with OpenAI Integration

## Overview
This project is a Flask-based API that integrates with OpenAI's GPT models. It includes endpoints for general messages and OpenAI-powered chat completions.

## Endpoints
- `/api/hello`: Simple "Hello, World" endpoint.
- `/api/openai/chat`: Interacts with OpenAI's ChatCompletion API.

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

   python3 -m venv venv
   source venv/bin/activate - for mac
   .\venv\Scripts\activate - for windows
   pip install -r requirements.txt
   python run.py
