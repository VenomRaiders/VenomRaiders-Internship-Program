import requests
import hashlib
import hmac
import base64
import time

import httplib2
import sys
import struct
import json

userid = "Type the id here"
secret_suffix= "Type the secret suffix here"
shared_secret = userid+secret_suffix

timestep = 30
T0=0

def HOTP(K, C, digits=10):
    K_bytes = str.encode(K)
    C_bytes = struct.pack(">Q", C)
    hmac_sha512 = hmac.new(key = K_bytes, msg=C_bytes,
digestmod=hashlib.sha512).hexdigest()
    return Truncate(hmac_sha512)[-digits:]

def Truncate(hmac_sha512):
    offset=int(hmac_sha512[-1], 16)
    binary= int(hmac_sha512[(offset *2):((offset*2)+8)],16)&0x7FFFFFFF
    return str(binary)

def TOTP(K, digits=10, timeref =0, timestep=30):
    C=int(time.time()-timeref)//timestep
    return HOTP(K,C,digits=digits)


def main():
    # User input (replace with your own values)
    userid = "HanslettTheDev@gmail.com"
    github_url = "https://gist.github.com/HanslettTheDev/8d27c177fced85afa1d755df7aa885b4"
    contact_email = "HanslettTheDev@gmail.com"
    solution_language = "python"

    # Construct the token shared secret
    shared_secret = f"{userid}HENNGECHALLENGE003"

    # Generate the TOTP
    totp_password = TOTP(shared_secret, 10, T0, timestep).zfill(10)

    print(totp_password)

    # Prepare the JSON payload
    payload = {
        "github_url": github_url,
        "contact_email": contact_email,
        "solution_language": solution_language,
    }

    # Make the HTTP POST request
    url = "https://api.challenge.hennge.com/challenges/003"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {base64.b64encode(userid.encode()).decode()}:{totp_password}",
    }

    response = requests.post(url, json=payload, headers=headers)

    # Print the response
    print(f"HTTP Status Code: {response.status_code}")
    print(response.json())

if __name__ == "__main__":
    main()
