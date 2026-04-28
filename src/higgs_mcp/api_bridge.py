import requests
import os
from dotenv import load_dotenv

def generate_higgs_video():
    """Triggers the video generation bridge using 1.77 GeV physics data."""
    load_dotenv()
    API_KEY = os.getenv("HIGGS_API_KEY")
    
    if not API_KEY or API_KEY == "your_secret_key_here":
        print("CRITICAL ERROR: No API Key found in .env file.")
        return

    print("Connecting to Cloud Node...")
    url = "https://api.higgsfield.ai/v1/generate"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    
    payload = {
        "model": "nano-banana-pro",
        "prompt": "Cinematic macro cinematography of subatomic particles colliding in a shimmering lime-green Higgs field. Shifting crystalline structures representing mass distribution. Photorealistic, 8k, scientific visualization style, glowing energy flows, deep bokeh background. (1.77 GeV Tau Lepton Peak)",
        "camera_movement": "slow_dolly_in"
    }
    
    print(f"Sending prompt to Seedance-2.0...")
    response = requests.post(url, headers=headers, json=payload)
    print(f"Response Status: {response.status_code}")
    print(f"Server Payload: {response.text}")

if __name__ == "__main__":
    generate_higgs_video()
