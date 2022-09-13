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
    queryParams = request.query_params
    print(queryParams)
    
    params = {
        'Tx_Commodity': queryParams['commodityCode'],
        'Tx_State': queryParams['stateCode'],
        'Tx_District': queryParams['districtCode'],
        'Tx_Market': queryParams['marketCode'],
        'DateFrom': queryParams['dateFrom'],
        'DateTo': queryParams['dateTo'],
        'Fr_Date': queryParams['dateFrom'],
        'To_Date': queryParams['dateTo'],
        'Tx_Trend': '0',
        'Tx_CommodityHead': queryParams['commodity'],
        'Tx_StateHead':  queryParams['state'],
        'Tx_DistrictHead': queryParams['district'],
        'Tx_MarketHead': queryParams['market'],
    }
    print(params)
    query = response_data.response(params).return_json()
    return Response(query)