# Mission to Mars: Web Scraping, Flask, MongoDB

This project uses Python Beautiful Soup to scrape the web for the latest information on--and images from--the mission to mars. It then stores this data in a Mongo database, and sends the content to HTML via Flask creating a dynamically updating website with the latest information on the mission.

Main file: app.py               
Secondary file: scrape_mars.py                   
HTML file: templates/index.html                   

The application is run through Flask, which is connected to a Mongo database storing the results of the web scrape. When the "Scrape" button on the web_page is pressed, the MongoDB collection is cleared, and scrape_mars.py is called.
This script uses beautifulsoup, splinter, and selenium webdriver to navigate the NASA website and pull in the latest news on the mars mission, finds the latest full-size image posted by NASA (by clicking through several pages on the website), reads in the latest mars weather report from twitter, collects a table of facts on the mars mission from space-facts.com, and finally grabs four separate images of mars' different hemispheres at the present time, along with their titles.

This information is stored in a MongoDB, and then read into selected places on our new "Mission to Mars" website.


