import requests
from bs4 import BeautifulSoup
#import smtplib
import time
#import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(executable_path=r"/Users/rohitm/Downloads/chromedriver", chrome_options=chrome_options)
#address = '1415 Owl Point'
#address_bytes = address.encode("utf-8")
#ubereatsURL = 'https://www.ubereats.com/en-US/search/feed/?pl=' + str(base64.b64encode(address_bytes)) + '&q=' + 'American'
#print(ubereatsURL)
#latitude = int(38.46928024)
#longitude = int(-122.64401246)
#cuisine = 'Salads'
#seamlessURL = 'https://www.seamless.com/search?orderMethod=delivery&locationMode=DELIVERY&facetSet=umamiV2&pageSize=20&hideHateos=true&searchMetrics=true&latitude=' + str(latitude) + '&longitude=' + str(longitude) + '&preciseLocation=true&facet=cuisine%3A' + cuisine + '&sortSetId=umamiv3&countOmittingTimes=true&sponsoredSize=3'
#deliveryURL = 'https://www.ebay.com/itm/Canon-EOS-5D-Mark-IV-Digital-SLR-Camera-Body-Only/323086614873'
def translator(message, language):
    message = message.replace(" ", "%20")
    if language == 'spanish':
        url = 'https://www.spanishdict.com/translate/' + message
    elif language == 'french':
        url = 'https://translate.google.com/?um=1&ie=UTF-8&tl=fr#view=home&op=translate&sl=auto&tl=fr&text=' + message
    elif language == 'russian':
        url = 'https://translate.google.com/?um=1&ie=UTF-8&tl=ru#view=home&op=translate&sl=auto&tl=ru&text=' + message
    elif language == 'italian':
        url = 'https://translate.google.com/?um=1&ie=UTF-8&tl=it#view=home&op=translate&sl=auto&tl=it&text=' + message
    elif language == 'hindi':
        url = 'https://translate.google.com/?um=1&ie=UTF-8&tl=hi#view=home&op=translate&sl=auto&tl=hi&text=' + message
    driver.get(url)
    time.sleep(2)
    try:
        if language == 'spanish':
            results = driver.find_elements_by_xpath("//*[@class='translation--1A9t-']")
        elif language == 'hindi':
            results = driver.find_elements_by_xpath("//*[@class='tlid-transliteration-content transliteration-content full']")
        else:
            results = driver.find_elements_by_xpath("//*[@class='tlid-translation translation']")
        for result in results:
            data = result.text
        return data
    except:
        return "¡Lo siento, mi amigo! Please try again using a more complex sentence: this isn't for Spanish 1 homework!"

#def func():
    #page = requests.get(url, headers=headers)


    #soup = BeautifulSoup(page.content, "lxml")
    #data = soup.find(id="mt-Microsoft").media
    #print(data)

    #price = soup2.find(id="prcIsum", itemprop="price").get_text()

    #converted_price = float(price[10:18].replace(',',''))
    #converted_title = title[52:]

    #print(converted_price)
    #print(converted_title.strip())

    #if converted_price < 1700: #replace with maximum price you want to be alerted for
        #send_mail()