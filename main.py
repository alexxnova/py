from module.web_scraper import  ArticleScrape
from module.data_formatter import ArticleJSON


url="https://pateshestvenik.com/"
numArticles = 20
outputName= 'scraper.csv'
jsonPath = "pateshestvenik.json"
    
content = ArticleScrape(url,numArticles)

def main():
    content.web_Scraping(outputName)
    testObj= ArticleJSON(outputName,jsonPath)
    testObj.export_json()
    return 0


if __name__ == "__main__":
    main()