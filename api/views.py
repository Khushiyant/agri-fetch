from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import response_data

@api_view(['GET'])
def getQueryData(request):
    query = response_data.response("http://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=35&Tx_State=DL&Tx_District=1&Tx_Market=4747&DateFrom=01-Jan-2022&DateTo=02-Jul-2022&Fr_Date=01-Jan-2022&To_Date=02-Jul-2022&Tx_Trend=0&Tx_CommodityHead=Brinjal&Tx_StateHead=NCT+of+Delhi&Tx_DistrictHead=Delhi&Tx_MarketHead=Azadpur").return_json()
    return Response(query)