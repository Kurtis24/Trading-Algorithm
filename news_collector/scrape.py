import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching chrome browser...")
    
    chrome_drive_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_drive_path), options=options)
    
    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        return html
    
    finally: 
        driver.quit()
        
def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
        
        
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
        )
        
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return[
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]
    
 

def main():
    saving_scrape_info = open("News_data", "w")
    url = input("Enter url:")
    result = scrape_website(url)
    

    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    saving_scrape_info.writelines(cleaned_content)
    
    saving_scrape_info.close()
    
if __name__ == "__main__":
    main()