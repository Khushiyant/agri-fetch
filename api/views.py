from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from . import response_data


@api_view(['GET'])
def getQueryData(request):
    data = json.load(open("static/json/query.json", "r"))
    return Response(data)

@api_view(['GET'])
def getCropData(request):
    query = request.get_queryset()
    
    params={
        'Tx_Commodity': '35',
        'Tx_State': 'DL',
        'Tx_District': '1',
        'Tx_Market': '4747',
        'DateFrom': '01-Jan-2022',
        'DateTo': '01-Jul-2022',
        'Fr_Date': '01-Jan-2022',
        'To_Date': '01-Jul-2022',
        'Tx_Trend': '0',
        'Tx_CommodityHead': 'Brinjal',
        'Tx_StateHead': 'NCT of Delhi',
        'Tx_DistrictHead': 'Delhi'
    }
    query = response_data.response(params).return_json()
    return Response(query)