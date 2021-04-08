from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
import rest_framework
import requests
import json
from django.contrib.auth.hashers import make_password
# Create your views here.

@api_view(('POST','GET'))
@csrf_exempt
@permission_classes((AllowAny,))                                 
def login(request):                                                  #login endpoint in authenticator
    expected_client_id = 'c2VjcmV0X2NsaWVudF9pZA'
    expected_return_uri = 'callback'
    response = {}
    if request.method == 'GET':
        client_id = request.GET['client_id']              #retreiving client_id and return_uri from URL
        return_uri = request.GET['return_uri']
        if client_id != expected_client_id or return_uri != expected_return_uri:
            response['Message'] = 'Invalid Client ID or return URI'
            return Response(response, status=200)
        else:
            my_dict = {
                'client_id': client_id,
                'return_uri': return_uri
            }
            return render(request, 'login.html',  context=my_dict)

    if request.method == "POST":
        username = request.POST.get('username')                           #getting the username
        password = request.POST.get('password')
        #hashed_password = make_password(password,'pbkdf2_sha256')
        client_id = request.POST.get('client_id')
        return_uri = request.POST.get('return_uri')

        payload = {'username': username, 'password': password} 
        url = 'http://127.0.0.1:8000/gettoken/'                         #generating JWT token
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.post(url, data=payload, headers=headers)
        json_response = json.loads(r.text)

        if 'access' not in json_response:
            message = Response(json_response, status=200)
            my_dict = {
                'client_id': client_id,
                'return_uri': return_uri,
                'credentials': 'invalid'
            }
            return render(request, 'login.html',  context=my_dict)

        else:
            response_dict = {
                    "issuer": client_id,
                    "id_token": json_response['access']
            }
            #print("JWT TOKEN#######",json_response['access'])
            url = 'http://127.0.0.1:8000/'+return_uri+'/'
            r = requests.post(url, data = response_dict)      #sending token for verification
            response_from_client = r.json()
            res = json.loads(response_from_client)
            if res["Message"] == "Token validation successfull":
                url = 'http://127.0.0.1:8000/?username='+username
                return HttpResponseRedirect(url)
            else:
                if res["Message"] == 'Invalid Issuer':
                    my_dict = {
                    'client_id': client_id,
                    'return_uri': return_uri,
                    'issuer': 'Invalid Issuer'
                    }
                    return render(request, 'login.html',  context=my_dict)
                else:
                    my_dict = {
                    'client_id': client_id,
                    'return_uri': return_uri,
                    'token': 'failure'
                    }
                    return render(request, 'login.html',  context=my_dict)