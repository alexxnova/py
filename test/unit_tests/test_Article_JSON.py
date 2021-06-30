import pytest
import os
from pathlib import Path
from pandas.core.frame import DataFrame
from module.data_formatter import ArticleJSON

@pytest.fixture
def articleJson():
    
    inputFile =  r'\scraper.csv'
    outputFile = r'\pateshestvenik.json'
    
    workingDir = os.getcwd()
    csvPath = workingDir + inputFile
    jsonPath = workingDir + outputFile
    
    return ArticleJSON(csvPath,jsonPath)

def test_articleJsonClass(articleJson):
    assert isinstance(articleJson, ArticleJSON)

def test_most_used_words(articleJson):
    inputStr="Как едно българско мобилно приложение е на път да промени представата ни за обслужването в хотелитеПо-екологично, повече удобство за туристите и по-малко рискове от зарази – това са само част от предимствата на българското мобилно приложение за хотели и заведения TouchMеnu. Създадено като смартфон апликация за нуждите на заведенията, през отминалата година то навлезе и в туристическия бранш, въвеждайки редица нови функционалности, които подпомагат хотелите, особено в условията на пандемия. Ето и някои от иновативните функции, които вече са достъпни през мобилното приложение.Поръчки, обвързани с хотелската стая"
    expected_content = {'приложение': 3, 'мобилно': 2, 'които': 2}
    assert articleJson.most_used_words(inputStr,3)==expected_content

def test_remove_character(articleJson):
    inputStr="[Ако от брега на морето ви дели повече от месец, значи е време да помислите как да оползотворите уикендите, докато отпуската все по-малко ви прилича на мираж"
    excepted_content= "Ако от брега на морето ви дели повече от месец, значи е време да помислите как да оползотворите уикендите, докато отпуската все по-малко ви прилича на мираж"
    assert articleJson.remove_character(inputStr)==excepted_content

def test_format_data(articleJson):
    df = articleJson.format_data()
    assert isinstance(df['most_used_words'], list)
    assert isinstance(df, DataFrame)

def test_export_json(articleJson):
    
    data=articleJson.format_data()
    jsonData=data.to_json(orient='records',force_ascii=False, indent=4)
    assert isinstance(jsonData, str)
    output = Path(articleJson.jsonPath)
    assert output.is_file()==True
    
    