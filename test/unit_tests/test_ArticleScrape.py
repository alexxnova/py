import pytest
import os
from pathlib import Path
from pandas.core.frame import DataFrame

    
def test_getTitle(articleScrapeClass_fixture, html_parser_fixture, expected_output_fixture):
    title = articleScrapeClass_fixture.get_Title(html_parser_fixture)
    assert title == expected_output_fixture['title'] 
    
def test_getDateTime(articleScrapeClass_fixture, html_parser_fixture, expected_output_fixture):
    date = articleScrapeClass_fixture.get_DateTime(html_parser_fixture)
    assert date == expected_output_fixture['date']

def test_getTextContent(articleScrapeClass_fixture, html_parser_fixture, expected_output_fixture):
    content = articleScrapeClass_fixture.get_Content(html_parser_fixture)
    assert content == expected_output_fixture['content']

def test_getCommentContent(articleScrapeClass_fixture,input_fixture, expected_output_fixture):
    noComment = articleScrapeClass_fixture.get_comment_session("https://pateshestvenik.com/%d1%80%d0%b8%d0%b1%d0%be%d0%bb%d0%be%d0%b2-%d0%b2-%d0%b1%d1%8a%d0%bb%d0%b3%d0%b0%d1%80%d0%b8%d1%8f/")
    assert noComment == expected_output_fixture['noComment']
    comment = articleScrapeClass_fixture.get_comment_session("https://pateshestvenik.com/%d1%80%d0%b5%d0%b7%d0%b5%d1%80%d0%b2%d0%b8%d1%80%d0%b0%d0%bc%d0%b5-%d1%85%d0%be%d1%82%d0%b5%d0%bb%d1%81%d0%ba%d0%b8-%d1%83%d1%81%d0%bb%d1%83%d0%b3%d0%b8-%d0%b8-%d0%b5%d0%ba%d1%81%d0%ba%d1%83%d1%80/")
    assert comment == expected_output_fixture['comment']
        
def test_exportContent(articleScrapeClass_fixture, input_fixture):
    # assert isinstance(articleScrapeClass_fixture.export_Content(output).dataFrame, DataFrame)
    df = articleScrapeClass_fixture.dataFrame
    assert isinstance(df, DataFrame)
    workingDir = os.getcwd()
    csvPath = Path(workingDir +'\\'+ input_fixture['outputCVS'])
    assert csvPath.is_file()==True
    result = articleScrapeClass_fixture.export_Content(input_fixture['outputCVS'])
    assert result == 0
    
def test_web_Scraping(articleScrapeClass_fixture):
    assert isinstance(articleScrapeClass_fixture.title, list)
    assert isinstance(articleScrapeClass_fixture.date, list)
    assert isinstance(articleScrapeClass_fixture.content, list)
    assert isinstance(articleScrapeClass_fixture.comment, list)
    