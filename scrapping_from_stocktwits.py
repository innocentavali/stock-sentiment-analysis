from bs4 import BeautifulSoup
import requests
import urllib
import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_comments(stock_name):
    '''

    :param stock_name:
    :return: a dict including comments and their published time
    '''
    #TODO
    pass


stock_comments_url = 'https://stocktwits.com/symbol/BILI'
browser = webdriver.Chrome()
browser.get('https://stocktwits.com/symbol/BILI')
stock_comments = browser.find_elements_by_class_name("MessageList__item___1m1w9")


for comment in stock_comments:
    text = comment.text
    print text
