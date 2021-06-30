import pytest
from module.web_scraper import  ArticleScrape

@pytest.fixture
def contentClass():
    return ArticleScrape("https://pateshestvenik.com/",1)
    
def test_getTitle(contentClass):
    expected_title = 'Резервираме хотелски услуги и екскурзии направо през телефона – Пътешественик'
    assert contentClass.get_Title(contentClass.create_soup("https://pateshestvenik.com/%d1%80%d0%b5%d0%b7%d0%b5%d1%80%d0%b2%d0%b8%d1%80%d0%b0%d0%bc%d0%b5-%d1%85%d0%be%d1%82%d0%b5%d0%bb%d1%81%d0%ba%d0%b8-%d1%83%d1%81%d0%bb%d1%83%d0%b3%d0%b8-%d0%b8-%d0%b5%d0%ba%d1%81%d0%ba%d1%83%d1%80/")) == expected_title
    
def test_getTextContent(contentClass):
    expected_content = 'Как едно българско мобилно приложение е на път да промени представата ни за обслужването в хотелите По-екологично, повече удобство за туристите и по-малко рискове от зарази – това са само част от предимствата на българското мобилно приложение за хотели и заведения TouchMеnu. Създадено като смартфон апликация за нуждите на заведенията, през отминалата година то навлезе и в туристическия бранш, въвеждайки редица нови функционалности, които подпомагат хотелите, особено в условията на пандемия. Ето и някои от иновативните функции, които вече са достъпни през мобилното приложение. Поръчки, обвързани с хотелската стая Хотелите, партниращи с приложението, могат да поставят различни QR кодове във всяка стая и на други ключови локации. Това дава възможност на гостите да поръчват храна и напитки, както и други продукти и услуги директно от стаята си. Всичко това улеснява процеса на поръчка, както и заплащането след това. Резервационен модул Платформата разполага с модул за запазване на маси в ресторантите, часове за спа или спорт, както и за запазване на място и време за групови занимания или на предстояща организирана екскурзия. Система за известяване Клиентите, използващи TouchMеnu получават лесна и удобна системата за известяване, чрез която могат да съобщят за проблем, да дадат обратна връзка или да повикат камериер за почистване на стаята. Чрез нея те могат също да заявят подготвяне на сметката, така че при напускане да не се образуват струпвания на рецепцията. В условията на все още активна пандемия, така се създават безопасни условия за гостите като рисковете от разпространение на вируси значително се ограничават. Локален информационен източник В добавка, гостите могат да получават директно на телефона си информация за всички предстоящи събития или услуги на територията на хотела или в близост до него. По този начин се свежда до минимум изразходването на хартия за брошури, плакати, менюта и др. Сред останалите предимства на приложението са многоезичен интерфейс, оптимизиран за гости от различни държави, както и многобройни детайлни статистики, които дават ценна информация на собствениците на хотели и заведения. То е оптимизирано и за ол-инклузив комплекси, много от които предлагат достатъчно услуги, които могат да се дигитализират и да станат достъпни през личните смартфони на клиентите. ТаговеСподетелете във2020 - Всички права запазени.'
    assert contentClass.get_Content(contentClass.create_soup("https://pateshestvenik.com/%d1%80%d0%b5%d0%b7%d0%b5%d1%80%d0%b2%d0%b8%d1%80%d0%b0%d0%bc%d0%b5-%d1%85%d0%be%d1%82%d0%b5%d0%bb%d1%81%d0%ba%d0%b8-%d1%83%d1%81%d0%bb%d1%83%d0%b3%d0%b8-%d0%b8-%d0%b5%d0%ba%d1%81%d0%ba%d1%83%d1%80/")) == expected_content

def test_getDateTime(contentClass):
    expected_date = '2021-06-08'
    assert contentClass.get_DateTime(contentClass.create_soup("https://pateshestvenik.com/%d1%80%d0%b5%d0%b7%d0%b5%d1%80%d0%b2%d0%b8%d1%80%d0%b0%d0%bc%d0%b5-%d1%85%d0%be%d1%82%d0%b5%d0%bb%d1%81%d0%ba%d0%b8-%d1%83%d1%81%d0%bb%d1%83%d0%b3%d0%b8-%d0%b8-%d0%b5%d0%ba%d1%81%d0%ba%d1%83%d1%80/")) == expected_date

    