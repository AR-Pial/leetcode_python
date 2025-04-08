import requests
import json

def generate_content_with_gemini(api_key, prompt):
    """
    Sends a request to the Gemini API to generate content.

    Args:
        api_key: Your Gemini API key.
        prompt: The text prompt to send to the API.

    Returns:
        The generated content as a string, or None if an error occurred.
    """

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        result = response.json()

        # Extract the generated text. Handles various response structures.
        if 'candidates' in result and result['candidates']:
            if 'content' in result['candidates'][0] and 'parts' in result['candidates'][0]['content']:
                parts = result['candidates'][0]['content']['parts']
                generated_text = "".join([part['text'] for part in parts if 'text' in part])
                return generated_text
        else:
            return None #Or raise an exception.
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None
    except KeyError as e:
        print(f"Error accessing key in JSON response: {e}")
        print(f"Response: {response.text}") #Useful for debugging malformed responses.
        return None



# Example usage: Replace 'YOUR_API_KEY' with your actual API key
api_key = 'YOUR_API_KEY' #Replace with your api key.
prompt = "Explain how AI works"

generated_text = generate_content_with_gemini(api_key, prompt)

if generated_text:
    print(generated_text)
else:
    print("Failed to generate content.")