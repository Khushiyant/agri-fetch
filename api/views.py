import json
from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

@api_view(['GET'])
def getData(request):
    pass


def getQueryData(request):
    query = open("static/json/query.json", "r").read()
    return Response(query)