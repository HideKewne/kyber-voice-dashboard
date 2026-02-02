#!/usr/bin/env python3
"""List available Gemini models"""

from google import genai

API_KEY = "AIzaSyBtjuQoQXf8hq7UGCEcGt4ya1ZRsWzssw4"
client = genai.Client(api_key=API_KEY)

print("Available models:")
for model in client.models.list():
    if 'image' in model.name.lower() or 'imagen' in model.name.lower():
        print(f"  - {model.name}")

print("\nAll models with generateContent support:")
for model in client.models.list():
    print(f"  - {model.name}")
