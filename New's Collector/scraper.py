import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import urllib.robotparser

def main():
    url = 'https://finviz.com/news.ashx'

    # Define the list of keywords to search for
    keywords = ['finance', 'bitcoin', 'trump', 'Elon', 'market']
    
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        html_content = response.text
        print('Webpage fetched successfully.')
    else:
        print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
        html_content = ''
        
    if html_content:
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find all news items; inspect the page to identify the correct HTML tags and classes
        # For Finviz News, news items are typically within <a> tags with class 'nn' and <span> tags for the time
        news_items = soup.find_all('a', class_='nn')
        
        # Initialize a list to store matched news
        matched_news = []
        
        for item in news_items:
            # Extract the news title
            title = item.text.strip()
            
            # Extract the link to the full article
            link = 'https://finviz.com/' + item.get('href')
            
            # Extract the parent element to get additional details like the time
            parent = item.parent
            time_span = parent.find('span', class_='nn-date')
            time = time_span.text.strip() if time_span else 'N/A'
            
            # Check if any keyword is in the title (case-insensitive)
            for keyword in keywords:
                if re.search(r'\b' + re.escape(keyword) + r'\b', title, re.IGNORECASE):
                    matched_news.append({
                        'Title': title,
                        'Link': link,
                        'Time': time,
                        'Keyword': keyword
                    })
                    break  # Avoid duplicate entries if multiple keywords match
        
        # Display the matched news
        for news in matched_news:
            print(f"{news['Time']} - {news['Title']} - {news['Link']} - Keyword: {news['Keyword']}")

    time.sleep(2)  # Wait for 2 seconds
    
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url('https://finviz.com/robots.txt')
    rp.read()

    # Check if scraping is allowed for the user-agent '*'
    can_fetch = rp.can_fetch('*', url)
    print(f'Can fetch: {can_fetch}')


if __name__ == "__main__":
    main()