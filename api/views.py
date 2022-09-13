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
    query = request.query_params
    print(query)
    
    params = {
        'Tx_Commodity': query['commodityCode'],
        'Tx_State': query['stateCode'],
        'Tx_District': query['districtCode'],
        'Tx_Market': query['marketCode'],   
        'DateFrom': query['dateFrom'],
        'DateTo': query['dateTo'],
        'Fr_Date': query['dateFrom'],
        'To_Date': query['toDate'],
        'Tx_Trend': '0',
        'Tx_CommodityHead': query['commodity'],
        'Tx_StateHead':  query['state'],
        'Tx_DistrictHead': query['district'],
        'Tx_MarketHead': query['market'],
    }
    query = response_data.response(params).return_json()
    return Response(query)