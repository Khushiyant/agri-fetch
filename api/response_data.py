import bs4
import requests


class response:
    def __init__(self, url):
        r = requests.get(url)
        self.soup = bs4.BeautifulSoup(r.text, 'html.parser')

    def return_json(self):
        data = {
            'status': 200,
            'results': []
        }
        divisions = ['id', 'district', 'market', 'commodity', 'variety',
                     'grade', 'min_price', 'max_price', 'modal_price', 'price_date']
        for row in self.soup.find_all('tr'):
            item = {}
            for i, dt in enumerate(row.find_all('td')):
                text = dt.text
                if text:
                    item[divisions[i]] = " ".join(text.split())
            if item:
                data['results'].append(item)
        
        if data['results'][0]['id'] == 'No Data Found':
            data['status'] = 403
            data['message'] = 'No data available'
            data.pop('results')
        return data


if __name__ == '__main__':
    print(response("http://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=35&Tx_State=DL&Tx_District=1&Tx_Market=4747&DateFrom=01-Jan-2022&DateTo=02-Jul-2022&Fr_Date=01-Jan-2022&To_Date=02-Jul-2022&Tx_Trend=0&Tx_CommodityHead=Brinjal&Tx_StateHead=NCT+of+Delhi&Tx_DistrictHead=Delhi&Tx_MarketHead=Azadpur").return_json())
