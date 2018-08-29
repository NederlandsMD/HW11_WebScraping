import time
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
import pandas as pd
import requests
import time

def scrape():

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # Mars News
    url_1 = "https://mars.nasa.gov/news/"

    browser.visit(url_1)
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('div', class_="content_title").a.text
    news_p = soup.find('div', class_="article_teaser_body").text

    # JPL Mars Space Images
    url_2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(url_2)
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    time.sleep(5)
    browser.click_link_by_partial_href('/spaceimages/images/largesize/')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image_url = soup.find('img')["src"]

    # Mars Weather
    url_3 = "https://twitter.com/marswxreport?lang=en"

    browser.visit(url_3)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_weather = soup.find("p", class_="js-tweet-text").text

    # Mars Facts
    url_4 = "https://space-facts.com/mars/"

    tables = pd.read_html(url_4)
    df = tables[0]
    df = df.rename(columns={0:"Category", 1:"Value"})
    df = df.set_index("Category", drop=True)
    del df.index.name
    table_data = df.to_html()
    print(table_data)

    # Mars Hemispheres
    Mars_Hem = []

    url_5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(url_5)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    Hemis = soup.findAll("div", class_="description")

    for hemi in Hemis: 
        Name = hemi.a.h3.text
        print(Name)
        browser.click_link_by_partial_text(Name)
        time.sleep(3)
        browser.click_link_by_partial_text('Open')
        time.sleep(2)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        img_src = soup.find('img', class_="wide-image")['src']

        img_src_full = f"https://astrogeology.usgs.gov" + img_src
        print(img_src_full)
        Name = Name[:-9]
        post = {"title":Name, "img_url":img_src_full}
        Mars_Hem.append(post)
        print(Mars_Hem)
        browser.click_link_by_partial_text('Close')
        time.sleep(3)
        browser.click_link_by_partial_text('Back')


    return news_title, news_p, featured_image_url, mars_weather, table_data, Mars_Hem