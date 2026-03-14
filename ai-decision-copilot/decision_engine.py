import requests

def analyze_data(data):

    prompt = f"""
    Analyze the following data and give insights:

    {data}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]