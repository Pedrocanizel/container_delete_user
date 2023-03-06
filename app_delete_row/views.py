from http.client import responses
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .postgres_conn import delete

'''
Para deleter, fazer uma requisição 'DELETE' e
enviar a chave primária (email) para deleção.
'''


@api_view(['DELETE'])
def delete_row(request):

    try:
        data = JSONParser().parse(request)
        #coluna = list(data.keys())[0]
        email = list(data.items())  
        email = email[0][1]
        delete(email)
        retorno = f'O email {email} foi deletado com sucesso'
        return JsonResponse(retorno, status=201, safe=False)

    except Exception as ex:
        response = {
            "error": str(ex.args[0])
        }
        return JsonResponse(response, status=400)




