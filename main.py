import requests
from bs4 import BeautifulSoup
import random

## Function to randomly return articles from the parsed website.
def scrape_it(url, num_return = 5):
    try:
        response = requests.get(url)       
        if response.status_code != 200:
            print(f'Failed to get the webpage: {response.status_code}')
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')

        article_list = soup.find_all('a')

        articles = [item.text.strip() for item in article_list][1:-1]
        return random.sample(articles, min(num_return, len(articles)))
    except Exception as e:
        print(f'An error has occurred: {e}')
        return []

## Helper function to return a dict of Article Titles as keys, and links as values
def dict_return(url, num_return = 5):
    try:
        response = requests.get(url)       
        if response.status_code != 200:
            print(f'Failed to get the webpage: {response.status_code}')
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')

        article_list = soup.find_all('a')

        #Get links and save them
        link_list = []
        for link in article_list:
            link_list.append(link.get('href'))

        link_list = link_list[1:]

        articles = [item.text.strip() for item in article_list][1:-1]

        article_dict = {}
        counter = 0
        for i in articles:
            article_dict[i] = 'https://www.paulgraham.com/' + link_list[counter]
            counter+=1

        return article_dict
    except Exception as e:
        print(f'An error has occurred: {e}')
        return []

def main():
    url = 'https://www.paulgraham.com/articles.html'
    article_list =  scrape_it(url)
    article_dict = dict_return(url)

    ## Print out articles and their links
    print("Here are some useful daily life tips you can read!")
    for index, article in enumerate(article_list, 1):
        print(f'{index}: {article} \n Link to article: {article_dict[article]}')

if __name__ == "__main__":
    main()