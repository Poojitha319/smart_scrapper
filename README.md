# Smart Scrapper

This repository contains a web scraping application built using Streamlit. The application allows users to scrape static or dynamic web pages for specific content such as titles, links, images, and videos. 

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Functions](#functions)
5. [Troubleshooting](#troubleshooting)
6. [References](#references)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Poojitha319/smart_scrapper
    cd web-scraping-streamlit
    ```

2. Install the required packages:
    ```sh
    pip install streamlit requests beautifulsoup4 selenium webdriver-manager
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter your scraping preferences including the URL, content type, HTML tag, element class, and whether the website is dynamic.

4. Click the button to start scraping and view the results directly on the Streamlit interface.

## Features

- **Dynamic User Input:** Users can specify the URL, content type, HTML tag, element class, and whether the website uses JavaScript.
- **Static and Dynamic Website Scraping:** The application supports both static and dynamic websites.
- **Content Types:** Users can scrape titles, links, images, videos, or a combination of these.
- **Results Display:** Scraped content is displayed directly within the Streamlit app, including images and videos.

## Functions

### `get_user_preferences()`
Prompts the user to enter scraping preferences through the Streamlit interface.

### `scrape_static_website(url, content_type, element_tag, element_class)`
Scrapes a static website using `requests` and `BeautifulSoup` based on user preferences.

### `scrape_dynamic_website(url, content_type, element_tag, element_class)`
Scrapes a dynamic website using `selenium` based on user preferences.

### `main()`
Main function to run the Streamlit app and coordinate user input and scraping.

## Troubleshooting

- **Error: Failed to retrieve the webpage. Status code:** Ensure the URL is correct and the website is accessible.
- **Selenium WebDriver Errors:** Make sure `chromedriver` is installed and properly configured. If using a virtual environment, ensure the environment has access to the `chromedriver`.
- **Content Not Found:** Verify the HTML tag and class are correct for the content you wish to scrape.

## References

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Requests Documentation](https://docs.python-requests.org/en/latest/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Selenium Documentation](https://www.selenium.dev/documentation/en/)
- [WebDriver Manager Documentation](https://pypi.org/project/webdriver-manager/)
