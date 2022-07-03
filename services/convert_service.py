from zipfile import ZipFile
import zipfile

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from lxml import html
import requests
import time


class ConvertService:
    def __init__(self, pdf_input_path, html_output_path):
        self.pdf_input_path = pdf_input_path
        self.html_output_path = html_output_path

        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)

    def run(self):
        self.driver.get('https://www.onlineconverter.com/pdf-to-html')
        self.driver.find_element(By.XPATH, '//input[@id="file"]').send_keys(self.pdf_input_path)
        self.driver.find_element(By.XPATH, '//input[@id="convert-button"]').click()

        for attempt in range(15):
            try:
                download_url = self.driver.find_element(By.XPATH, '//a[.="Download Now"]').get_attribute('href')
            except:
                time.sleep(2)
                continue
            else:
                break

        res = requests.get(download_url)

        with open(self.html_output_path, 'wb') as f:
            f.write(res.content)

        with ZipFile("./tmp/download.zip", 'r') as zip_ref:
            zip_ref.extractall("./tmp/download")

        self.__transform()

    @staticmethod
    def __transform():
        with open("./tmp/download/index.html", "r") as fr:
            tree = html.fromstring(fr.read())

            for p in tree.xpath('//*[@class]'):
                p.attrib.pop('class')

            for a in tree.xpath('//a'):
                a.attrib['target'] = '_blank'

            with open("./tmp/download/index.html", "wb") as fw:
                fw.write(html.tostring(tree.xpath('//body')[0]))
