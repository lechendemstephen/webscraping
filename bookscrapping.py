from bs4 import BeautifulSoup # type: ignore
import requests  # type: ignore
import csv

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

# creating a csv to save all the files 
with open('books.csv', mode='w', newline='', encoding='utf-8') as book: 
    book_writer = csv.writer(book)
    book_writer.writerow(['Title', 'Price', 'Availability'])

    # page counter 
    page_count = 1 

    # while loop to continously run until all the pages are exhausted
    while True: 

        url = base_url.format(page_count)

        html_text = requests.get(url)
    # checking the status if its not equal to 200, it means the page does not exist hence, exit the loop
        if html_text.status_code != 200: 
            print('no more books to scrap')
            break

        soup = BeautifulSoup(html_text.text, 'lxml')

        books  = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

    # iterating on all the books to extract information on each book 
        for book in books: 

            book_title = book.find('h3').text
            book_price = book.find('p', class_='price_color').text.replace('Â£', '')
        
            book_availability  = book.find('p', class_='instock availability').text.lstrip()

    

            book_writer.writerow([book_title, book_price, book_availability])

        
        page_count + 1 



