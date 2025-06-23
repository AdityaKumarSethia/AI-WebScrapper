import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time 

def scrapeWebsite(website: str) -> str:
    """ Does the Web Scrapping using Selenium returning a str(html) """
    print("Launching chrome browser...")
    
    chrome_driver_path:str = r"./chromedriver-linux64/chromedriver"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path),options=options)
    
    try:
        driver.get(website)
        print("Page Loaded")
        html = driver.page_source
        
        return html
    finally:
        driver.quit()
        
        
def extractBodyContent(html_content:str) -> str:
    """ Returns the html_content with structuring using bs4.BeautifulSoup as str """
    soup = BeautifulSoup(html_content,"html.parser")
    if body_content := soup.body :
        return str(body_content)
    return "N/A"


def cleanBodyContent(body_content:str) -> str:
    """ Removes <script> and <style> tags from the str(html_content) """
    soup = BeautifulSoup(body_content, "html.parser")
    
    # Removing (extracting) all <script> & <style> tags
    for script_or_style in soup(['script','style']):
        script_or_style.extract()
        
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    
    return cleaned_content


def splitDOMcontent(dom_content:str, max_length=6000) -> list[str]:
    """ Splits the DOM content for tokenizing  """
    return [dom_content[i: i+max_length] for i in range(0, len(dom_content), max_length)]

    