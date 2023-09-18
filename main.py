from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Safari()

driver.get('https://the-internet.herokuapp.com/')

time.sleep(3)

try:
# Test 1: Kliknutí na odkaz "Checkboxes"
    checkboxes_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Checkboxes')

    checkboxes_link.click()

    time.sleep(3)

    current_url = driver.current_url

    expected_url = 'https://the-internet.herokuapp.com/checkboxes'
    if current_url == expected_url:
        print("Kliknutím na odkaz 'Checkboxes' jsme se dostali na správnou stránku.")
    else:
        print("Kliknutím na odkaz 'Checkboxes' jsme se nedostali na správnou stránku.")

# Test 2: Vyhledávání na stránce
    search_input = driver.find_element(By.ID, 'search')
    search_input.send_keys('Internet')
    search_input.send_keys(Keys.RETURN)
    time.sleep(3)

    search_results = driver.find_element(By.ID, 'result')
    search_text = search_results.text
    expected_text = 'The Internet'
    if expected_text in search_text:
        print("Test 2: Výsledek vyhledávání je správný: 'The Internet' bylo nalezeno.")
    else:
        print("Test 2: Výsledek vyhledávání není správný.")

# Test 3: Kliknutí na odkaz "Digest Authentication"
    digest_auth_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Digest Authentication')
    digest_auth_link.click()
    time.sleep(3)

    current_url = driver.current_url
    expected_url = 'https://the-internet.herokuapp.com/digest_auth'
    if current_url == expected_url:
        print("Test 3: Kliknutím na odkaz 'Digest Authentication' jsme se dostali na správnou stránku.")
    else:
        print("Test 3: Kliknutím na odkaz 'Digest Authentication' jsme se nedostali na správnou stránku.")

except Exception as e:
    print("Nastala chyba při provádění testu:", str(e))

driver.quit()
