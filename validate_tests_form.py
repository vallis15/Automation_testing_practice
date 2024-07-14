from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Safari()

try:
    driver.get('https://www.beskydyweddings.cz')
    time.sleep(5)

    name_field = driver.find_element(By.NAME, 'f-name')
    name_field.send_keys('Jan Novák')

    email_field = driver.find_element(By.NAME, 'f-email')
    email_field.send_keys('jan.novak@example.com')

    phone_field = driver.find_element(By.NAME, 'f-telefon')
    phone_field.send_keys('123456789')

    wedding_date_field = driver.find_element(By.NAME, 'f-datum')
    wedding_date_field.send_keys('2024-09-20')

    wedding_location_field = driver.find_element(By.NAME, 'f-mistokonani')
    wedding_location_field.send_keys('Zámek Nové Město')

    guest_count_field = driver.find_element(By.NAME, 'f-pocethostu')
    guest_count_field.send_keys('100')

    photographer_field = driver.find_element(By.NAME, 'f-fotograf')
    photographer_field.send_keys('Petr Černý')

    budget_field = driver.find_element(By.NAME, 'f-rozpocet')
    budget_field.send_keys('50000')
    
    information_field = driver.find_element(By.NAME, 'f-necovic')
    information_field.send_keys('automate_test')
    
    submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]') 
    submit_button.click()

    time.sleep(5)

finally:
    driver.quit()
