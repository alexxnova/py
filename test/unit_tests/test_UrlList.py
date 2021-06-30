import pytest
from bs4 import BeautifulSoup
from module.web_scraper import UrlList

@pytest.fixture
def urllist():
    test_url = "https://pateshestvenik.com/"
    return UrlList(test_url,1)
    
def test_html_parser(urllist):
    test_url = "https://pateshestvenik.com/"
    assert isinstance(urllist.html_parser(test_url), BeautifulSoup)
    
def test_get_nextPageUrl(urllist):
    test_url = "https://pateshestvenik.com/page/2/"
    assert urllist.get_nextPageUrl() == test_url

def test_create_url_list(urllist):
    test_list = ['https://pateshestvenik.com/%d1%80%d0%b8%d0%b1%d0%be%d0%bb%d0%be%d0%b2-%d0%b2-%d0%b1%d1%8a%d0%bb%d0%b3%d0%b0%d1%80%d0%b8%d1%8f/']
    assert urllist.create_url_list() == test_list
    
