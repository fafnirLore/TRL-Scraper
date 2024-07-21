# TRL-Scraper
This Python script uses Selenium to scrape chapters from a website and save them as text files.

## Requirements

* Python 3
* Selenium
* Chrome WebDriver (Make sure it's in your PATH or specify its location when initializing the driver)

## Installation

1. **Install Python:** If you don't have Python 3 installed, download and install it from [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Install Selenium:**
   ```pip install selenium```

3. **Download ChromeDriver:**
   * Download the ChromeDriver that matches your Chrome browser version from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
   * Extract the `chromedriver` executable and place it in your system's PATH or provide its path when creating the `Service` object in the code.

## Usage

1. **Replace `'your_website_url'`:** 
   * In the `scrape_paragraphs()` function call at the bottom of the script, replace `'your_website_url'` with the actual URL of the first chapter you want to scrape from https://novelfull.net. 

2. **Run the script:**
   ```python your_script_name.py```
   (Replace `your_script_name.py` with the actual name of your Python file.)

## How it works

1. **Initialization:** 
   * Imports necessary libraries.
   * Defines the `save_chapter()` function to save the extracted content to a text file.
   * Defines the `scrape_paragraphs()` function to handle the scraping process.

2. **Scraping:**
   * Sets up a Chrome WebDriver using Selenium.
   * Navigates to the provided URL.
   * Enters a loop to iterate through chapters.
   * Locates and extracts the chapter title and paragraphs.
   * Calls `save_chapter()` to save the content.
   * Finds the "Next Chapter" button and clicks it.
   * Handles cases where the "Next Chapter" button is disabled or not found, breaking the loop.

3. **Error Handling:**
   * Includes a `try...except` block to catch potential errors during the process and print them to the console.

4. **Cleanup:**
   * Closes the WebDriver after the scraping is complete.

## Notes

* This script is tailored to a specific website structure. You might need to adjust the selectors (e.g., `By.CLASS_NAME`, `By.ID`, `By.TAG_NAME`) if you want to use it for a different website.
* The script assumes the presence of a "Next Chapter" button with the ID `'next_chap'`. 
* Be mindful of websites' terms of service and robots.txt files to avoid causing issues or overloading servers.
