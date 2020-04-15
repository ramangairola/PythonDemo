from selenium import webdriver

driver = webdriver.Chrome("C:\\Chromedriver\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://www.geeksforgeeks.org/python-map-function/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()