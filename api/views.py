from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
import json
import os
import time

# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@api_view(['POST'])
def run(request):
    data = request.body.decode('utf-8')
    data = json.loads(data)
    if data['lang'] == "C++":
        f = open(os.path.join(BASE_DIR, 'Codes/main.cpp'), "w")
        f.write(data['code'])
        f.close()
    if data['lang'] == "Python3":
        f = open(os.path.join(BASE_DIR, 'Codes/main.py'), "w")
        f.write(data['code'])
        f.close()        

    if('inp' in data.keys() and data['inp'] != None):
        f = open(os.path.join(BASE_DIR, 'Codes/input.txt'), "w")
        f.write(data['inp'])
        f.close()
    os.chdir(os.path.join(BASE_DIR, 'Codes'))
    if data['lang'] == "C++":
        os.system('g++ "main.cpp"')
        os.system('a.exe < input.txt > output.txt')
        os.system('g++ "main.cpp" 2> "output.log"')

    if data['lang'] == "Python3":
        os.system('python main.py < input.txt > output.txt')

    os.chdir(BASE_DIR)
    # time.sleep(3)
    out = open(os.path.join(BASE_DIR, 'Codes/output.txt'), "r")
    code_output = out.read()
    if os.stat(os.path.join(BASE_DIR, "Codes/output.log")).st_size != 0:
        f = open(os.path.join(BASE_DIR, "Codes/output.log"), "r")
        error = f.read()
        return Response({"OUTPUT" : code_output, 'error' : error})
    else:
        return Response({"OUTPUT" : code_output})

    # return Response({})

@api_view()
def GetOut(request):
    out = open(os.path.join(BASE_DIR, 'Codes/output.txt'), "r")
    code_output = out.read()
    if os.stat(os.path.join(BASE_DIR, "Codes/output.log")).st_size != 0:
        f = open(os.path.join(BASE_DIR, "Codes/output.log"), "r")
        error = f.read()
        return Response({"OUTPUT" : code_output, 'error' : error})
    else:
        return Response({"OUTPUT" : code_output})