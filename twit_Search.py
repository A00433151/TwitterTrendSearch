######## Get latest trending twitter hash tags and get their related google search items ###################


import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import tweepy

consumer_key = "sbAnI5uPhos56fux65hxXwOE2"
consumer_secret = "oy3C8JLvk7vMihtIzaXdAAd4cK2k28lBDhBcGQlq882Uuj2X4O"
access_key = "20185148-y7BudlZah0DM05tnqKLNmPzX4lWNoL5wFVGe9Zlaz"
access_secret = "RVabWxPeqSmjwxGDxoanQnKUAleXaGclNVA92F5HTESe8"
ua = UserAgent()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
# Use Below to test api connection
# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")
woeids = 23424775   #Change this based on location WOEID's to get location based trends, here its for Canada.
trends_result = api.trends_place(woeids)
trends_list = trends_result[0]["trends"]
trends_list_name = []
for trend in trends_list[:10]:
    trends_list_total = trend["name"]
    trends_list_total = trends_list_total.replace('#', "")
    trends_list_name.append(trends_list_total)
print("****** Below is the List of Top Trending Tweets on twitter **********\n")
for i,index in enumerate(trends_list_name):
    print(i,index)
input_var = None
while True:
    input_var = input("\nEnter your choice of Trending Tweet: ")
    if int(input_var) < 10 and int(input_var) >= 0:
        break
    else:
        print('Invalid Choice, Enter Again')
search_item = trends_list_name[int(input_var)]
query = search_item
number_result = 10    #Number of google search items to display
print("\nShowing the " +str(number_result)+ " Google search results for: " + search_item +"\n")
google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)
response = requests.get(google_url, {"User-Agent": ua.random})
soup = BeautifulSoup(response.text, "html.parser")
result_div = soup.find_all('div', attrs={'class': 'ZINbbc'})
links = []
titles = []
descriptions = []
for r in result_div:
    try:
        link = r.find('a', href=True)
        title = r.find('div', attrs={'class': 'vvjwJb'}).get_text()
        description = r.find('div', attrs={'class': 's3v9rd'}).get_text()
        if link != '' and title != '' and description != '':
            links.append(link['href'])
            print(title + " " + link['href'][7:])
    except:
        continue
