from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def clear_form(driver):
    driver.find_element(By.NAME, 'f-name').clear()
    driver.find_element(By.NAME, 'f-email').clear()
    driver.find_element(By.NAME, 'f-telefon').clear()
    driver.find_element(By.NAME, 'f-datum').clear()
    driver.find_element(By.NAME, 'f-mistokonani').clear()
    driver.find_element(By.NAME, 'f-pocethostu').clear()
    driver.find_element(By.NAME, 'f-fotograf').clear()
    driver.find_element(By.NAME, 'f-rozpocet').clear()
    driver.find_element(By.NAME, 'f-necovic').clear()  

def fill_form(driver, skip_field=None):
    if skip_field != 'name':
        name_field = driver.find_element(By.NAME, 'f-name')
        name_field.send_keys('Jan Novák')
        time.sleep(1)

    if skip_field != 'email':
        email_field = driver.find_element(By.NAME, 'f-email')
        email_field.send_keys('jan.novak@example.com')
        time.sleep(1)

    if skip_field != 'phone':
        phone_field = driver.find_element(By.NAME, 'f-telefon')
        phone_field.send_keys('123456789')
        time.sleep(1)

    if skip_field != 'wedding_date':
        wedding_date_field = driver.find_element(By.NAME, 'f-datum')
        wedding_date_field.send_keys('2024-09-20')
        time.sleep(1)

    if skip_field != 'wedding_location':
        wedding_location_field = driver.find_element(By.NAME, 'f-mistokonani')
        wedding_location_field.send_keys('Zámek Nové Město')
        time.sleep(1)

    if skip_field != 'guest_count':
        guest_count_field = driver.find_element(By.NAME, 'f-pocethostu')
        guest_count_field.send_keys('100')
        time.sleep(1)

    if skip_field != 'photographer':
        photographer_field = driver.find_element(By.NAME, 'f-fotograf')
        photographer_field.send_keys('Petr Černý')
        time.sleep(1)

    if skip_field != 'budget':
        budget_field = driver.find_element(By.NAME, 'f-rozpocet')
        budget_field.send_keys('50000')
        time.sleep(1)

    if skip_field != 'wedding_details':  # Nové pole
        wedding_details_field = driver.find_element(By.NAME, 'f-necovic')
        wedding_details_field.send_keys('Jedná se automatizovaný test QA testera Daniela Valla')
        time.sleep(1)

    if skip_field is not None:
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()
        time.sleep(5)

def main():
    driver = webdriver.Safari()
    
    try:
        driver.get('https://www.beskydyweddings.cz')
        time.sleep(5)
        
        fields_to_skip = ['name', 'email', 'phone', 'wedding_date', 'wedding_location', 'guest_count', 'photographer', 'budget', 'wedding_details']

        for field in fields_to_skip:
            clear_form(driver)
            fill_form(driver, skip_field=field)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
