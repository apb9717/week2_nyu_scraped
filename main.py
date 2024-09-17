import requests
from bs4 import BeautifulSoup

## Function to randomly return weather descriptions from the parsed website.
def scrape_it(url, num_return = 5):
    try:
        response = requests.get(url)       
        if response.status_code != 200:
            print(f'Failed to get the webpage: {response.status_code}')
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')

        weatherList = soup.find_all('li', class_='forecast-tombstone')
        weatherDescList = []

        ## Find img alt descriptions of weather.
        for i in weatherList:
            x = str(i).find('img alt')
            if x != -1:
                endImgAlt = str(i)[x+ len('img alt="'):].find('"')
                weatherDesc = str(i)[x+ len('img alt="'): endImgAlt + x+ len('img alt="')]
                weatherDescList.append(weatherDesc)
        return weatherDescList
    
    except Exception as e:
        print(f'An error has occurred: {e}')
        return []

def main():
    url = 'https://forecast.weather.gov/MapClick.php?lat=40.7324512&lon=-73.9892746'
    weatherList =  scrape_it(url)

    ## Print out articles and their links
    print("Here the week's forecast for New York City!")
    for article in weatherList:
        print(article)

if __name__ == "__main__":
    main()