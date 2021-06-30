import pytest
import main
from module.web_scraper import  ArticleScrape
from module.data_formatter import ArticleJSON


def test_main():
    assert main.main()==0