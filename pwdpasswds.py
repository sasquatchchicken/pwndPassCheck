import requests
import hashlib
from getpass import getpass

def check_compromised_password(password):
    # Use "Have I Been Pwned" API with k-Anonymity
    api_url = "https://api.pwnedpasswords.com/range/"
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    prefix, suffix = sha1_password[:5], sha1_password[5:]

    response = requests.get(api_url + prefix)
    
    # Check if the full hash suffix exists in the response
    return suffix in response.text

try:
    password = getpass("Enter a new password: ")

    if check_compromised_password(password):
        raise ValueError("Password has been compromised")

    print("Password is not compromised.")
except Exception as e:
    print(f"Error: {str(e)}")

