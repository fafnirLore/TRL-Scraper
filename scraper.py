from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import os
import time

def save_chapter(title, paragraphs):
    # Create a valid filename from the title
    filename = f"{title}.txt".replace(" ", "_").replace("/", "_").replace("\\", "_")
    
    # Write the paragraphs to the file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Title: {title}\n\n")
        for paragraph in paragraphs:
            file.write(paragraph + "\n\n")

def scrape_paragraphs(url):
    # Set up the Selenium web driver (Chrome in this case)
    driver = webdriver.Chrome()
    
    # Navigate to the URL
    driver.get(url)
    
    try:
        while True:
            # Find the element with the class 'chapter-text' and get its text as the title
            title_element = driver.find_element(By.CLASS_NAME, 'chapter-text')
            title = title_element.text
            
            # Find the div with the id 'chapter-content'
            chapter_content_div = driver.find_element(By.ID, 'chapter-content')
            
            # Find all paragraph tags within this div
            paragraphs = chapter_content_div.find_elements(By.TAG_NAME, 'p')
            
            # Extract the text from each paragraph
            paragraph_texts = [p.text for p in paragraphs]
            
            # Save the chapter
            save_chapter(title, paragraph_texts)
            
            # Find the button with the id 'next_chap'
            try:
                next_button = driver.find_element(By.ID, 'next_chap')
                
                # Check if the next button is disabled
                if 'disabled' in next_button.get_attribute('class'):
                    print("Next chapter button is disabled. Stopping the loop.")
                    break
                
            
                # Click the next button
                next_button.click()
                
            except (NoSuchElementException, ElementNotInteractableException):
                print("Next chapter button is not found or not interactable. Stopping the loop.")
                break
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the web driver
        driver.quit()

# Replace 'your_website_url' with the actual URL of the website you want to scrape
scrape_paragraphs('https://novelfull.net/tales-of-the-reincarnated-lord/chapter-350-bank-entitlement-and-real-estate.html')
