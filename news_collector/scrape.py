import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrape_website(website):
    print("Launching chrome browser...")
    
    chrome_drive_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_drive_path), options=options)
    
    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(10)
        
        return html
    finally: 
        driver.quit()
        
def main():
    url = input("Enter url:")
    result = scrape_website(url)
    print(result)
    
if __name__ == "__main__":
    main()