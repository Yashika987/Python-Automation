from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    
    # Automatically download and use the correct driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://automated.pythonanywhere.com")
    return driver

def main():
    driver = get_driver()
    try:
        element1 = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
        element2 = driver.find_element(by="xpath", value="/html/body/div[1]/div/p")
        return element1.text, element2.text
    finally:
        driver.quit()
print(main())


