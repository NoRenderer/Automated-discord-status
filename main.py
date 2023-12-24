import requests
import json
import time
import random

messages = {
    "status": [
        "Hey, this status is automated!",
        "The time is: " + time.strftime("%H:%M:%S"),
    ]
}

waittime = 300

def change_status(token, status):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "custom_status": {
            "text": status
        }
    })

    response = requests.patch("https://discordapp.com/api/v6/users/@me/settings", headers=headers, data=payload)
    if response.status_code == 200:
        print("Status changed to: " + status)
    else:
        print("Error: " + str(response.status_code) + " " + response.reason)

def main():
    envfile = open(".env", "r")
    token = envfile.read()
    envfile.close()
    print("Changing status every " + str(waittime) + " seconds.")
    while True:
        status = random.choice(messages["status"])
        change_status(token, status)
        time.sleep(waittime)

if __name__ == "__main__":
    main()
