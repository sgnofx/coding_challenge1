from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
import rest_framework
import requests
# Create your views here.

def index(request):
    user = request.GET.get('username')   #checking for username
    if user is not None:
        user = request.GET['username']
        my_dict = {
            'username': user
        }
        return render(request, 'client.html', context = my_dict)
    else:
        my_dict = {"insert_link": '/authenticator/login?client_id=c2VjcmV0X2NsaWVudF9pZA&return_uri=callback'} #url of authenticator
        return render(request, 'client.html', context = my_dict) 

@api_view(('POST',))
@csrf_exempt
@permission_classes((AllowAny,))
def callback(request):                                   #callback end point in client
    if request.method == "POST":
        response = {}
        issuer = request.POST.get("issuer")             #retreiving values from which came from authenticator
        jwt_token = request.POST.get("id_token")   
        
        if issuer != 'c2VjcmV0X2NsaWVudF9pZA':          #validation of issuer
            response["Message"] = "Invalid Issuer"
            return Response(response, status=200)
        else:
            payload = {"token": jwt_token}
            url = "http://127.0.0.1:8000/verifytoken/"
            r = requests.post(url, data = payload)          #validation of id_token
            token_response = json.loads(r.text)

            if 'code' in token_response and token_response['code'] == "token_not_valid":
                response["Message"] = "Token validation failed"
                res = json.dumps(response)
                return Response(res, status=200)
            else:
                response["Message"] = "Token validation successfull"   #sending response back to autheticator
                res = json.dumps(response)
                return Response(res, status=200)