import pytest
from module.web_scraper import  Server

@pytest.fixture
def server():
    test_url = "https://pateshestvenik.com/"
    return Server(test_url)
    
def test_page_response(server):
    response = server.page_response()
    assert response.status_code == 200
    
def test_get_url(server):
    test_url = "https://pateshestvenik.com/"
    assert server.get_url() == test_url