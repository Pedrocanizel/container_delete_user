import requests
import json


def get_header():
    h = {
        "Content-Type": "application/json"    }
    return h


def valida_token_navegacao(email, token, finalidade):
    session = requests.session()
    url = "http://127.0.0.1:8000/tpath/"    
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
