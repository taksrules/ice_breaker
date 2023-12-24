import os 
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from Linkedin profiles, 
    Manually scrape the information from the LinkedIn profile
    """
    pass
    options = Options()
    # options.add_argument("--headless")  # Add any desired options

    # Set the path to the Chrome driver
    driver_path = r"C:/Users/tadiw/Downloads/Compressed/chrome-win32/chrome-win32/chrome.exe"

    # Create the Chrome driver using the options and driver path
    driver = webdriver.Chrome()
    driver.get("https://linkedin.com/uas/login")
    time.sleep(5)
    username = driver.find_element(By.ID, "username")
    username.send_keys("Takura.mukaro@outlook.com")
    pword = driver.find_element(By.ID, "password")
    pword.send_keys("Taks1998")  
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    profile_url = "https://www.linkedin.com/in/kunalshah1/"
    driver.get(profile_url)
    start= time.time()
    # will be used in the while loop
    initialScroll = 0
    finalScroll = 1000
    while True:
        driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
        initialScroll=finalScroll
        finalScroll+= 1000
        time.sleep(3)

        end= time.time()
        if round(end-start)>20:
            break
    src= driver.page_source

    soup2= BeautifulSoup(src, 'html.parser')

    url= linkedin_profile_url
    response= requests.get(url)
    soup= BeautifulSoup(response.content, 'html.parser')
    intro = soup.find('div', {'class': 'pv-text-details__left-panel'})

    #Find and extract specific information from the profile
    name_element= soup.find("div", {'id':'profile-content'})
    paragraphs = soup.find_all("div")
    name = name_element.text if name_element else None
    return intro
    # bio= soup.find("div", {"class": "profile-bio"}).text
    # image_url = soup.find("img", {"class": "profile-image"})["src"]
