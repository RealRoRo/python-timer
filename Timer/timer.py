from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("sample test case started")
driver = webdriver.Chrome(
    'C:/Users/roro/Downloads/chromedriver_win32/chromedriver.exe')
# driver=webdriver.firefox()
# driver=webdriver.ie()
# maximize the window size
driver.maximize_window()
# navigate to the url
driver.get("https://www.google.com/")
# identify the Google search text box and enter the value
driver.find_element_by_name("q").send_keys("timer")
time.sleep(1)
# click on the Google search button
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(1)
while(True):
    driver.find_element_by_xpath(
        '//*[@id="act-timer-section"]/div/div[1]').click()
    driver.find_element_by_xpath(
        '//*[@id="act-timer-section"]/div/div[1]').send_keys("2500")
    driver.find_element_by_xpath(
        '//*[@id="act-timer-section"]/div/div[1]').send_keys(Keys.ENTER)
    time.sleep(1500)
    print("Press Enter to rest for 5 min!!")
    if(input() == '\n'):
        driver.find_element_by_xpath(
            '//*[@id="act-timer-section"]/div/div[2]/span[1]/g-button[2]').click()
        driver.find_element_by_xpath(
            '//*[@id="act-timer-section"]/div/div[1]').click()
        driver.find_element_by_xpath(
            '//*[@id="act-timer-section"]/div/div[1]').send_keys("500")
        driver.find_element_by_xpath(
            '//*[@id="act-timer-section"]/div/div[1]').send_keys(Keys.ENTER)
        time.sleep(300)
    else:
        driver.close()

print("sample test case successfully completed")
