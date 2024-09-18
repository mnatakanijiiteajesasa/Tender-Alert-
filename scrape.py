from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
from selenium.webdriver.common.by import By


def scrape_tenders(url):

# setting up chrome options
    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(url)
        time.sleep(5)
        tenders_button = driver.find_element(By.LINK_TEXT, "Tenders")
        tenders_button.click()
        time.sleep(5)
       

        tenders = []
        current_page = 1
        while True:
            table = driver.find_element(By.TAG_NAME, "table")
# looping through the tenders table rows
            for row in table.find_elements(By.XPATH, ".//tbody/tr"):
                cells = row.find_elements(By.TAG_NAME, "td")
                if len(cells) > 0:
                    tender_no = cells[0].text.strip()
                    description = cells[1].text.strip()
                    procuring_entity = cells[2].text.strip()
                    closing_date = cells[5].text.strip()

                tenders.append({
                    'Tender Number': tender_no,
                    'Description': description,
                    'Procuring Entity': procuring_entity,
                    'Closing Date': closing_date
                    })
             

            next_page_button = driver.find_element(By.XPATH, "//li[@class='v-pagination__next']/button")

            is_disabled = next_page_button.get_attribute("aria-disabled")

            if is_disabled == 'true':
                print("No more pages to scrape")
                break
            else:
                next_page_button.click()
                time.sleep(3)
        return tenders

    except (NoSuchElementException, TimeoutError) as e:
        print(f"Error: {e}")
        return []

    try:
        driver.get(url)
        time.sleep(5)
        tenders_button = driver.find_element(By.LINK_TEXT, "Procuring Entities")
        tenders_button.click()
        time.sleep(5)
       

        entities = []
        current_page = 1
        while True:
            table = driver.find_element(By.TAG_NAME, "table")
# looping through the tenders table rows
            for row in table.find_elements(By.XPATH, ".//tbody/tr"):
                cells = row.find_elements(By.TAG_NAME, "td")
                if len(cells) > 0:
                    tender_no = cells[0].text.strip()
                    description = cells[1].text.strip()
                    procuring_entity = cells[2].text.strip()
                    closing_date = cells[5].text.strip()

                tenders.append({
                    'Tender Number': tender_no,
                    'Description': description,
                    'Procuring Entity': procuring_entity,
                    'Closing Date': closing_date
                    })
             

            next_page_button = driver.find_element(By.XPATH, "//li[@class='v-pagination__next']/button")

            is_disabled = next_page_button.get_attribute("aria-disabled")

            if is_disabled == 'true':
                print("No more pages to scrape")
                break
            else:
                next_page_button.click()
                time.sleep(3)
        return tenders

    except (NoSuchElementException, TimeoutError) as e:
        print(f"Error: {e}")
        return []

    
    finally:
        driver.quit()

    

