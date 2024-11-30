from bs4 import BeautifulSoup  # type: ignore
import requests  # type: ignore
import csv


base_url = 'http://quotes.toscrape.com/page/{}/'


with open('quotes2.csv', 'w', encoding='utf-8') as file: 
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author', 'Tags'])


    # setting a page count 
    page_count = 1 

    while True: 
        url = base_url.format(page_count)

        html_text = requests.get(url)

        if html_text.status_code != 200: 
            print('no more pages to scrape')
            break

        soup = BeautifulSoup(html_text.text, 'lxml')

        quote_items = soup.find_all('div', class_='quote')

        # looping through the quote item to get all quotes
        for quote_item in quote_items: 
            quote = quote_item.find('span', class_='text').get_text()
            author = quote_item.find('small', class_='author').get_text()
        # just using a couple string manipulations and and index techniques to separate the tags
            try:
              tag_text = (quote_item.get_text().split('Tags:')[1].lstrip()).split()
            except: 
                pass
            tag = ', '.join(tag_text)

            writer.writerow([quote, author, tag])

        
        page_count +=1 
    print('Scrapping completed')



