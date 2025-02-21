import  requests
from bs4 import BeautifulSoup

header = {'user-agent': 'User_321fg3'}

global soup , category

def get_link(category):
    basic_category = '/books_1'

    if category is None:
        category = basic_category

    link = f"https://books.toscrape.com/catalogue/category{category}/index.html"

    responce = requests.get(link, headers=header).text
    soup = BeautifulSoup(responce, 'lxml')





def print_types():


    block = soup.find('ul', class_ ="nav nav-list")
    block_1 = block.find('ul')

    all_li = block_1.find_all('li')
    all_li_list = list(all_li)

    x = 0

    for li in all_li_list:
        x += 1
        print(li.text.strip())
        if x >= 7:
            break

    def get_value():

        global category

        category_values = {
            "Travel":"/travel_2",
            "Mystery": "/mystery_3",
            "Historical Fiction": "/historical-fiction_4",
            "Sequential Art": "/sequential-art_5",
            "Classics": "/classics_6",
            "Philosophy": "/philosophy_7",
            "Romance": "/romance_8"
        }


        type_of_books = input('input type: ')
        category = category_values.get(type_of_books)

        print(category)

        if category is None:
            print("input exist value")
            get_value()

        print_types()
        print(category)

    get_value()


def print_another(type_value):

    books_all = soup.find('ol', class_ ="row")
    print(books_all)

def main():
    print_types()
    print_another(category)

main()


