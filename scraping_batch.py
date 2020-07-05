from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import re
import csv
import pandas as pd
import matplotlib.pyplot as plt
import show_graph as graph


def main():
    items = search('hhkb+type-s')
    write_csv('hhkb.csv', items)
    show_graph('./hhkb.csv')


def search(key_words):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)

    page = 1
    items = []

    url = "https://www.mercari.com/jp/search/?keyword={}".format(key_words)

    try:
        while (url):

            driver.get(url)

            time.sleep(2)

            print('Working on page {}'.format(page))

            posts = driver.find_elements_by_css_selector('.items-box')

            for post in posts:
                title = post.find_element_by_css_selector(
                    'h3.items-box-name').text
                price = post.find_element_by_css_selector(
                    'div.items-box-price').text
                price = re.sub(r'[¥,]', '', price)

                sold_out = False

                if len(
                        post.find_elements_by_css_selector(
                            'div.item-sold-out-badge')):
                    sold_out = True
                else:
                    pass

                items.append((title, price, sold_out))

            url = driver.find_element_by_css_selector(
                'li.pager-next li.pager-cell a').get_attribute('href')
            page += 1
    except:
        pass

    driver.close()

    return items


def write_csv(csv_name, items):
    with open(csv_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['title', 'price', 'sold_out'])
        writer.writerows(items)


def show_graph(csv_name):
    graph.save_graph(csv_name)


if __name__ == '__main__':
    main()