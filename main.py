import time
from enum import Enum

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Elements(Enum):
    cookies_policy_terms_ID = 'cookiebotDialogOkButton'
    dla_niego_CLASS = 'slide-button '
    t_shirt_XPATH = "//img[@alt='T-shirt z koniczyną']"
    rozmiar_XPATH = "//span[@class='size-name' and text()='L']"
    dodaj_do_koszyka_XPATH = "//button[contains(@class, 'add-to-cart')]"



def load_page(url):
    driver.get(url)
    print('Loaded page: ' + driver.title)
    time.sleep(1) #allow the page load properly


def accept_cookies_policy():
    try:
        accept = driver.find_element(By.ID, Elements.cookies_policy_terms_ID.value)
        accept.click()

    except:
        pass


def add_T_shirt_to_basket():
    dla_niego = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                                           Elements.dla_niego_CLASS.value)))
    dla_niego.click()

    t_shirt = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, Elements.t_shirt_XPATH.value)))
    t_shirt.click()

    rozmiarL = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Elements.rozmiar_XPATH.value)))
    rozmiarL.click()

    koszyk = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                        Elements.dodaj_do_koszyka_XPATH.value)))
    koszyk.click()


if __name__ == '__main__':
    try:
        service = Service(executable_path = 'geckodriver.exe')
        driver = webdriver.Firefox(service = service)
        url = 'https://www.cropp.com/pl/pl/'

        load_page(url)
        accept_cookies_policy()
        add_T_shirt_to_basket()

        time.sleep(2)

    finally:
        driver.quit()