import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def show_result_message(success, failed_test):
    root = tk.Tk()
    root.withdraw()
    if success:
        messagebox.showinfo("Výsledek testu", "Všechny testy proběhly v pořádku")
    else:
        messagebox.showerror("Výsledek testu", f"Test '{failed_test}' neproběhl v pořádku")

driver = webdriver.Safari()
driver.get("https://www.beskydyweddings.cz")
time.sleep(3)

test_success = True
failed_test = ""

if test_success:
    try:
        portfolio_link = driver.find_element(By.LINK_TEXT, "PORTFOLIO")
        portfolio_link.click()
        time.sleep(3)
    except Exception as e:
        test_success = False
        failed_test = "PORTFOLIO"
        print(f"Došlo k chybě u PORTFOLIO: {e}")

if test_success:
    try:
        o_mne_link = driver.find_element(By.LINK_TEXT, "O MNĚ")
        o_mne_link.click()
        time.sleep(3)
    except Exception as e:
        test_success = False
        failed_test = "O MNĚ"
        print(f"Došlo k chybě u O MNĚ: {e}")

if test_success:
    try:
        kontakt_link = driver.find_element(By.LINK_TEXT, "KONTAKT")
        kontakt_link.click()
        time.sleep(3)
    except Exception as e:
        test_success = False
        failed_test = "KONTAKT"
        print(f"Došlo k chybě u KONTAKT: {e}")

driver.quit()
show_result_message(test_success, failed_test)
