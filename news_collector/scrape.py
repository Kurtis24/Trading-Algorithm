import nltk
from textblob import TextBlob
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from nltk.sentiment import SentimentIntensityAnalyzer

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

def search_keywords(cleaned_content, keywords):
    found_keywords = []
    lines = cleaned_content.split("\n")
    
    for line in lines:
        for keyword in keywords:
            if keyword.lower() in line.lower():
                found_keywords.append((keyword, line))
    
    return found_keywords

def analyze_sentiment(cleaned_content):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(cleaned_content)

    # Determine the overall sentiment
    if sentiment_scores['compound'] > 0.5:
        sentiment = "Positive"
    elif sentiment_scores['compound'] < -0.5:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, sentiment_scores

def main():
    keywords = ["NVDA", "Nvidia"]
    
    url = input("Enter the URL to scrape: ")
    
    result = scrape_website(url)
    
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    sentiment, scores = analyze_sentiment(cleaned_content)

    
    matched_keywords = search_keywords(cleaned_content, keywords)
    
    with open("News_data.txt", "w") as saving_scrape_info:
        saving_scrape_info.write("=== Keywords Found ===\n")
        for keyword, line in matched_keywords:
            saving_scrape_info.write(f"[{keyword}] {line}\n")

    with open("News_data.txt", "a+") as file:
        file.write("=== Sentiment Analysis ===\n")
        file.write(f"Overall Sentiment: {sentiment}\n")
        file.write(f"Sentiment Scores: {scores}\n")
    
if __name__ == "__main__":
    main()
