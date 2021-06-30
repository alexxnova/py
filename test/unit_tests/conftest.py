"""
Configuration for pytest.

NOTE: This file is automatically included when running pytest.
      There is no need to import it explicitly in the test files.
"""

import os
import sys
import pytest
from module.web_scraper import  ArticleScrape
from module.web_scraper import UrlList


# allow the contents to be found automatically as if we were in that directory
sys.path.append(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
)

@pytest.fixture
def input_fixture():
    mainURL = "https://pateshestvenik.com/"
    outputCVS = 'scraper.csv'
    outputJson = r'\pateshestvenik.json'
    fisrtPageUrl = "https://pateshestvenik.com/%d1%80%d0%b"\
        "5%d0%b7%d0%b5%d1%80%d0%b2%d0%b8%d1%80%"\
        "d0%b0%d0%bc%d0%b5-%d1%85%d0%be%d1%82%d"\
        "0%b5%d0%bb%d1%81%d0%ba%d0%b8-%d1%83%d1%"\
        "81%d0%bb%d1%83%d0%b3%d0%b8-%d0%b8-%d0%b5"\
        "%d0%ba%d1%81%d0%ba%d1%83%d1%80/"
    return {'mainURL':mainURL,'outputCVS':outputCVS,'outputJson':outputJson,
            'fisrtPageUrl':fisrtPageUrl}

@pytest.fixture
def expected_output_fixture():
    title='Резервираме хотелски услуги и екскурзии направо през телефона'
    date='2021-06-08'
    content=['Как едно българско мобилно приложение е на път да промени представата ни за обслужването в хотелите',
             'По-екологично, повече удобство за туристите и по-малко рискове от зарази – това са само част от предимствата на българското мобилно приложение за хотели и заведения TouchMеnu. Създадено като смартфон апликация за нуждите на заведенията, през отминалата година то навлезе и в туристическия бранш, въвеждайки редица нови функционалности, които подпомагат хотелите, особено в условията на пандемия. Ето и някои от иновативните функции, които вече са достъпни през мобилното приложение.',
             'Поръчки, обвързани с хотелската стая', 
             'Хотелите, партниращи с приложението, могат да поставят различни QR кодове във всяка стая и на други ключови локации. Това дава възможност на гостите да поръчват храна и напитки, както и други продукти и услуги директно от стаята си. Всичко това улеснява процеса на поръчка, както и заплащането след това.',
             'Резервационен модул',
             'Платформата разполага с модул за запазване на маси в ресторантите, часове за спа или спорт, както и за запазване на място и време за групови занимания или на предстояща организирана екскурзия.',
             'Система за известяване', 
             'Клиентите, използващи TouchMеnu получават лесна и удобна системата за известяване, чрез която могат да съобщят за проблем, да дадат обратна връзка или да повикат камериер за почистване на стаята. Чрез нея те могат също да заявят подготвяне на сметката, така че при напускане да не се образуват струпвания на рецепцията. В условията на все още активна пандемия, така се създават безопасни условия за гостите като рисковете от разпространение на вируси значително се ограничават.',
             'Локален информационен източник', 
             'В добавка, гостите могат да получават директно на телефона си информация за всички предстоящи събития или услуги на територията на хотела или в близост до него. По този начин се свежда до минимум изразходването на хартия за брошури, плакати, менюта и др.', 'Сред останалите предимства на приложението са многоезичен интерфейс, оптимизиран за гости от различни държави, както и многобройни детайлни статистики, които дават ценна информация на собствениците на хотели и заведения. То е оптимизирано и за ол-инклузив комплекси, много от които предлагат достатъчно услуги, които могат да се дигитализират и да станат достъпни през личните смартфони на клиентите.']
    comment=['Георги Стоянов:Страхотна статия', 'Veselin Grigorov:Страхотна статия']
    noComment=['no comments']
    return {'title':title,'date':date, 'content':content,'comment':comment, 'noComment':noComment}

@pytest.fixture
def articleScrapeClass_fixture(input_fixture):
    return ArticleScrape(input_fixture['mainURL'],1)

@pytest.fixture
def urlList_fixture(input_fixture):
    return UrlList(input_fixture['mainURL'],1)

@pytest.fixture(autouse=True)
def html_parser_fixture(urlList_fixture, input_fixture):
    soup = urlList_fixture.html_parser(input_fixture['fisrtPageUrl'])
    return soup

