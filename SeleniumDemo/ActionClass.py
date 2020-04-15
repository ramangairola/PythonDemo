from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\\Chromedriver\\chromedriver.exe")
# driver.get("https://www.familysearch.org/en/")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

action = ActionChains(driver)
# action.move_to_element(driver.find_element_by_xpath("//button[text()='Search']")).click().perform()
# action.move_to_element(driver.find_element_by_xpath("//a[@data-test='genealogies']")).click().perform()

action.double_click(driver.find_element_by_id("displayed-text")).perform()

action