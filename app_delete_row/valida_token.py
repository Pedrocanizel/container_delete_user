import requests
import json


def get_header():
    h = {
        "Content-Type": "application/json"    }
    return h


def valida_token_navegacao(email, token, finalidade):
    session = requests.session()
    url = "http://35.209.24.231:8008/token_confirmation/"    
    h = get_header()
    d = json.dumps(
        {
            "email": email,
            "type": finalidade,
            "token":token        
        }
    )
    token = session.post(url, data=d, headers=h)
    return token