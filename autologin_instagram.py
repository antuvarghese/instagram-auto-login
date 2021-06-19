from selenium import webdriver
import time
with open("name.txt", "r") as f:
    for x in f:
        a = x.split()[0]
        a = a.split(":")
        a = str(a)
        un = a.split()[0]
        pw = a.split()[1]
        username = str(un)[2:-2]
        password = str(pw)[1:-2]
        driver = webdriver.Chrome(r"chromedriver")
        driver.get('https://www.instagram.com/accounts/login/')
        username_input = '//*[@id="loginForm"]/div/div[1]/div/label/input'
        password_input = '//*[@id="loginForm"]/div/div[2]/div/label/input'
        login_submit = '//*[@id="loginForm"]/div/div[3]/button'
        time.sleep(5)
        driver.find_element_by_xpath(username_input).send_keys(username)
        time.sleep(3)
        driver.find_element_by_xpath(password_input).send_keys(password)
        time.sleep(3)
        driver.find_element_by_xpath(login_submit).click()
        time.sleep(10)
        driver.close()