import requests
import json

# This is the url to which the query is made
url = "https://data.electorate21.hasura-app.io/v1/query"

# This is the json payload for the query
requestPayload = {
    "type": "insert",
    "args": {
        "table": "teacher",
        "objects": [
            {
                "id": "34",
                "name": "shru"
            }
        ]
    }
}

# Setting headers
headers = {
    "Content-Type": "application/json"
}

# Make the query and store response in resp
resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

# resp.content contains the json response.
print(resp.content)


url = 'https://hooks.zapier.com/hooks/catch/2982892/zxgukj/'
requests.post(url, json={'table': 'teacher'})
