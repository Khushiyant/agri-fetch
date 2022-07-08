from base.models import Commodity, Market, State
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import response_data
from .serializers import CommoditySerializer, MarketSerializer, StateSerializer


@api_view(['GET'])
def getQueryData(request):
    data = open("static/json/query.json", "r").read()
    return Response(data)

@ api_view(['GET'])
def getCropData(request):
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


@ api_view(['GET'])
def getQueryData_commodity(request):
    commodities = Commodity.objects.all()
    serializer = CommoditySerializer(commodities, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def getQueryData_state(request):
    states = State.objects.all()
    serializer = StateSerializer(states, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def getQueryData_market(request):
    markets = Market.objects.all()
    serializer = MarketSerializer(markets, many=True)
    return Response(serializer.data)
