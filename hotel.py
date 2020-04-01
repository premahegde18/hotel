import requests
from bs4 import BeautifulSoup
import pandas as pd
# target URL to scrap
url = "https://www.goibibo.com/hotels/hotels-in-shimla-ct/"

headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

response = requests.request("GET", url, headers=headers)
data = BeautifulSoup(response.text, 'html.parser')
print(data)
cards_data = data.find_all('div', attrs={'class', 'width100 fl htlListSeo hotel-tile-srp-container hotel-tile-srp-container-template new-htl-design-tile-main-block'})

print('Total Number of Cards Found : ', len(cards_data))

for card in cards_data:
    print(card)
for card in cards_data:
    hotel_name = card.find('p')
    room_price = card.find('li', attrs={'class': 'htl-tile-discount-prc'})
    print(hotel_name.text, room_price.text)

scraped_data = []
for card in cards_data:
    card_details = {}
    hotel_name = card.find('p')
    room_price = card.find('li', attrs={'class': 'htl-tile-discount-prc'})
    card_details['hotel_name'] = hotel_name.text
    card_details['room_price'] = room_price.text
    scraped_data.append(card_details)
dataFrame = pd.DataFrame.from_dict(scraped_data)
dataFrame.to_csv('hotels_data.csv', index=False)
df = pd.read_csv('hotels_data.csv')
df.to_excel('hotels_data.xlsx', sheet_name='hotel', index=False)