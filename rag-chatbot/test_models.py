#!/usr/bin/env python3
"""
Test which Claude models your API key has access to
"""
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Common Claude model names
models_to_try = [
    "claude-3-opus-20240229",
    "claude-3-sonnet-20240229",
    "claude-3-haiku-20240307",
    "claude-3-5-sonnet-20241022",
    "claude-3-5-sonnet-20240620",
]

print("Testing Claude models with your API key...\n")

working_model = None

for model in models_to_try:
    try:
        response = client.messages.create(
            model=model,
            max_tokens=10,
            messages=[{"role": "user", "content": "Hi"}]
        )
        print(f"✅ {model} - WORKS!")
        if not working_model:
            working_model = model
    except Exception as e:
        if "not_found_error" in str(e):
            print(f"❌ {model} - Not available")
        else:
            print(f"⚠️  {model} - Error: {str(e)[:50]}")

print(f"\n{'='*60}")
if working_model:
    print(f"✅ Use this model: {working_model}")
    print(f"\nUpdate app/services/llm_service.py line 23 to:")
    print(f'    self.model = "{working_model}"')
else:
    print("❌ No working models found. Check your API key.")
