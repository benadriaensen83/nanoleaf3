import requests
from termcolor import colored, cprint
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import colorsys

class Picular:

    def search(self, query):

        driver = webdriver.Firefox()
        driver.get('https://picular.co/' + query)
        time.sleep(3)
        data = driver.find_elements_by_xpath('//div')
        rgb_list = []
        for item in data:
            try:
                rgb_list.append(item.get_attribute('style').split('rgb')[1].split(';')[0])
            except:
                pass

        rgb_tuples = []
        for item in rgb_list:
            rgb_tuples.append(eval(item))
        driver.quit()
        return rgb_tuples

    def rgb_to_HSB(self, data):

        hls_data = []
        for item in data:
            r, g, b = item[0]/256, item[1]/256, item[2]/256
            prob = item[3]
            print(prob)
            item = colorsys.rgb_to_hsv(r,g,b)
            print(item)
            data = {'hue':int(item[0]*360), 'saturation': int(round(item[1]*100,0)), 'brightness':int(round(item[2]*100,0)), 'probability': prob}
            hls_data.append(data)
        return hls_data