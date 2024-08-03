#git repo

import streamlit as st
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def get_user_preferences():
    st.subheader("Enter your scraping preferences:")
    url = st.text_input("Enter the URL of the website to scrape:")
    content_type = st.selectbox("What type of content do you want to scrape?", 
                                ['Titles', 'Links', 'Images', 'Videos', 'Both'])
    element_tag = st.text_input("Enter the HTML tag to look for (e.g., h2, div, img, video):")
    element_class = st.text_input("Enter the class of the HTML element (leave empty if not applicable):")
    is_dynamic = st.radio("Is the website dynamic (uses JavaScript to load content)?", ('Yes', 'No'))
    is_dynamic = (is_dynamic == 'Yes')
    return url, content_type.lower(), element_tag.strip().lower(), element_class.strip(), is_dynamic

def scrape_static_website(url, content_type, element_tag, element_class):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    if element_class:
        elements = soup.find_all(element_tag, class_=element_class)
    else:
        elements = soup.find_all(element_tag)

    for element in elements:
        if content_type == 'titles':
            st.write(f"Title: {element.get_text(strip=True)}")
        elif content_type == 'links':
            link = element.find('a')['href'] if element.find('a') else 'No link found'
            st.write(f"Link: {link}")
        elif content_type == 'images':
            img_src = element['src'] if element_tag == 'img' else 'No image found'
            st.image(img_src, caption=f"Image URL: {img_src}")
        elif content_type == 'videos':
            video_src = element['src'] if element_tag == 'video' else 'No video found'
            st.video(video_src, caption=f"Video URL: {video_src}")
        elif content_type == 'both':
            st.write(f"Title: {element.get_text(strip=True)}")
            link = element.find('a')['href'] if element.find('a') else 'No link found'
            st.write(f"Link: {link}")
            if element_tag == 'img':
                img_src = element['src']
                st.image(img_src, caption=f"Image URL: {img_src}")
            elif element_tag == 'video':
                video_src = element['src']
                st.video(video_src, caption=f"Video URL: {video_src}")

def scrape_dynamic_website(url, content_type, element_tag, element_class):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)

    if element_class:
        elements = driver.find_elements(By.CSS_SELECTOR, f"{element_tag}.{element_class}")
    else:
        elements = driver.find_elements(By.TAG_NAME, element_tag)

    for element in elements:
        if content_type == 'titles':
            st.write(f"Title: {element.text}")
        elif content_type == 'links':
            link = element.get_attribute('href')
            st.write(f"Link: {link}")
        elif content_type == 'images':
            img_src = element.get_attribute('src')
            st.image(img_src, caption=f"Image URL: {img_src}")
        elif content_type == 'videos':
            video_src = element.get_attribute('src')
            st.video(video_src, caption=f"Video URL: {video_src}")
        elif content_type == 'both':
            st.write(f"Title: {element.text}")
            link = element.get_attribute('href')
            st.write(f"Link: {link}")
            if element_tag == 'img':
                img_src = element.get_attribute('src')
                st.image(img_src, caption=f"Image URL: {img_src}")
            elif element_tag == 'video':
                video_src = element.get_attribute('src')
                st.video(video_src, caption=f"Video URL: {video_src}")

    driver.quit()

def main():
    st.title("Web Scraping with Streamlit")

    url, content_type, element_tag, element_class, is_dynamic = get_user_preferences()

    if url:
        if is_dynamic:
            scrape_dynamic_website(url, content_type, element_tag, element_class)
        else:
            scrape_static_website(url, content_type, element_tag, element_class)

if __name__ == "__main__":
    main()
