#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime as dt

class Server:
    
    def __init__(self,url):
        self.url = url
        
    def page_response(self):
        page = requests.get(self.url)
        return page
    
    def get_url(self):
        return self.url


class UrlList:
    
    def __init__(self,url, numArcticles):
        # self.Server = ServerClass(url)
        self.nextPage = url
        self.list = []
        self.neededBlogs = numArcticles
    
    def create_soup(self,url):
        server = Server(url)
        page = server.page_response().text
        soup = BeautifulSoup(page, 'lxml')
        return soup
    
    def get_nextPageUrl(self):
        soup = self.create_soup(self.nextPage)
        next_page = soup.find('a', class_ = 'next page-numbers', href= True)
        self.nextPage = next_page['href']
        return self.nextPage
    
    def create_url_list(self):
        # page = self.Server.page_response().text
        soup = self.create_soup(self.nextPage)
        while len(self.list) < self.neededBlogs:
            for article in soup.find_all('article'):
                link=article.find('a', href=True)
                self.list.append(link['href'])
                if self.neededBlogs == len(self.list):
                    break
            self.nextPage = self.get_nextPageUrl()
            soup = self.create_soup(self.nextPage)
        return self.list
    
class ArticleScrape(UrlList):
    
    def __init__(self, url, numArcticles):
        UrlList.__init__(self, url, numArcticles)
        self.urlList = self.create_url_list()
        self.title = []
        self.date = []
        self.content = []
        self.dataFrame = pd.DataFrame({'title':[],'published date':[],'content':[]})
        
    def get_Title(self,contentSoup):
        title = contentSoup.find('title').get_text()
        return title
    
    def get_Content(self,contentSoup):
        text=''
        for paragraph in contentSoup.body.find_all('p'):
            text+=paragraph.text
            # text.replace('\u00A0', ' ')
        return text
        
    def get_DateTime(self,contentSoup):
        dateTime=contentSoup.head.find('meta',property="article:published_time")
        date = dt.fromisoformat(dateTime['content'])
        formatedDate = date.strftime("%Y-%m-%d")
        return formatedDate
    
    def export_Content(self, outputName):
        self.dataFrame['title']=self.title
        self.dataFrame['content']=self.content
        self.dataFrame['published date']=self.date
        self.dataFrame.set_index('title', inplace=True)
        self.dataFrame.to_csv(outputName+'.csv')
        # self.dataFrame.to_json('jsonScrape.json',orient ='table')
        # self.dataFrame.to_excel("excelScrape.xlsx") 


    def web_Scraping(self, outputName):
        for url in self.urlList:
            contentSoup = self.create_soup(url)           
            self.title.append(self.get_Title(contentSoup))
            self.content.append(self.get_Content(contentSoup))
            self.date.append(self.get_DateTime(contentSoup))
        self.export_Content(outputName)