from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time


def search_youtube(search,delay):
    """[searchs the user input on youtube]

    Args:
        search ([string]): [user input to be searched]
        delay ([int]): [waiting time for the page to load]
    """

    search_box = driver.find_element_by_xpath('//input[@id="search"]')
    search_box.send_keys(search)

    search_bar_button = WebDriverWait(driver, delay).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="search-icon-legacy"]')))
    search_bar_button.click()  


def play_first_video():
    """[plays the first video present on the loaded page]
    """
    elem = driver.find_element_by_xpath('//*[@id="video-title"]')
    elem.click()


def collect_links():
    """[prints links of all videos present on that page]
    """
    elements = []
    elems = driver.find_elements_by_xpath("//a[@href]")
    print("Collecting links...")
    for elem in elems:
        elements.append(str(elem.get_attribute("href")))

    for i in elements:
        print(i)

if __name__ == "__main__":

    search = raw_input("Enter what you want to watch : ")
    case = input("Choose your option and answer in 1 or 2: [1] View a video [2] Collect all links")

    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")
    print(driver.title)

    delay = 5 # seconds

    try:
        search_youtube(search,delay)
        if case == 1:
            play_first_video()
        elif case == 2:
            collect_links()
        else:
            print("Incorrect option choosen!")

    except TimeoutException:
        print("Loading took too much time!")