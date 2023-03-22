from http.client import responses
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .postgres_conn import delete
from django.views.decorators.csrf import csrf_exempt
from . import valida_token as vt 

@csrf_exempt
@api_view(['DELETE'])
def delete_row(request):
    
    token = request.headers['Authorization']
    data = request.data
    email = request.headers['email']
    status = vt.valida_token_navegacao(email, token, 'nav')
    status = status.json()
    if status['FL_STATUS'] == False:
        resposta = {
            "msg": "token expirado",
            "FL_STATUS": False        
            }
        return JsonResponse(resposta, status=400, safe=False)

    try:
        
        name = data['name']  
        email = data['email']
        delete(name, email)
        retorno = {
            "FL_STATUS": True
        }
        return JsonResponse(retorno, status=201, safe=False)

    except Exception as ex:
        response = {
            "FL_STATUS": False,
            "error": str(ex.args[0])
        }
        return JsonResponse(response, status=400)




