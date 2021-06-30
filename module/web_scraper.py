import requests
from bs4 import BeautifulSoup
import pandas as pd
from requests_html import HTMLSession
from requests import RequestException
from datetime import datetime as dt


class Server:
    
    def __init__(self,url):
        self.url = url
        
    def page_response(self):
        page = requests.get(self.url)
        if page.status_code != 200:
            raise RequestException
        return page
    
    def get_url(self):
        return self.url


class UrlList:
    
    def __init__(self,url, numArcticles):
        self.nextPage = url
        self.list = []
        self.neededBlogs = numArcticles
    
    def html_parser(self,url):
        server = Server(url)
        page = server.page_response().text
        soup = BeautifulSoup(page, 'lxml')
        return soup
    
    def get_nextPageUrl(self):
        soup = self.html_parser(self.nextPage)
        next_page = soup.find('a', class_ = 'next page-numbers', href= True)
        self.nextPage = next_page['href']
        return self.nextPage
    
    def create_url_list(self):
        while len(self.list) < self.neededBlogs:
            soup = self.html_parser(self.nextPage)
            for article in soup.find_all('article'):
                link=article.find('a', href=True)
                self.list.append(link['href'])
                if self.neededBlogs == len(self.list):
                    break
            self.nextPage = self.get_nextPageUrl()
        return self.list
    
class ArticleScrape():
    
    def __init__(self, url, numArcticles):
        self.urlObj = UrlList(url, numArcticles)
        self.urlList = self.urlObj.create_url_list()
        self.commentUrl=""
        self.title = []
        self.date = []
        self.content = []
        self.comment = []
        self.dataFrame = pd.DataFrame()
        
    def get_Title(self,contentSoup):
        title = contentSoup.find('h1').get_text()
        title.replace('"', '')
        return title
    
    def get_Content(self,contentSoup):
        text = []
        for paragraph in contentSoup.body.find_all('p', class_ = False):
            if (paragraph.text=='\xa0' or paragraph.text=='' or paragraph.text == '2020 - Всички права запазени.'):
                pass
            else:
                text.append(paragraph.text)
        return text
    
    def get_comment_session(self,url):
        session=HTMLSession()
        r=session.get(url)
        r.html.render(sleep=1,timeout=12)
 
        about = r.html.find('iframe',first=True)
        commentUrl=about.attrs['src']
 
        p=session.get(commentUrl)
        p.html.render(sleep=1,timeout=12)
 
        commentStr=[]
        findComment=p.html.find('._5mdd')
        if (len(findComment)) <=0:
            commentStr.append('no comments')
            return commentStr
        commentAuthor=p.html.find('.UFICommentActorName')
        publishedComment=findComment[0].find('span')
 
        for comment in range(len(findComment)):
            commentStr.append(commentAuthor[comment].text + ':' + publishedComment[comment].text)
        return commentStr


    def get_DateTime(self,contentSoup):
        dateTime=contentSoup.head.find('meta',property="article:published_time")
        date = dt.fromisoformat(dateTime['content'])
        formatedDate = date.strftime("%Y-%m-%d")
        return formatedDate
    
    def export_Content(self, outputName):
        self.dataFrame = pd.DataFrame({'title':self.title,'date_of_publishing':self.date,'content':self.content,'comments':self.comment})
        self.dataFrame.set_index('title', inplace=True)
        self.dataFrame.to_csv(outputName)
        return 0


    def web_Scraping(self, outputName):
        for url in self.urlList:
            contentSoup = self.urlObj.html_parser(url)           
            self.title.append(self.get_Title(contentSoup))
            self.date.append(self.get_DateTime(contentSoup))
            self.content.append(self.get_Content(contentSoup))
            self.comment.append(self.get_comment_session(url)) 
        self.export_Content(outputName)
        

