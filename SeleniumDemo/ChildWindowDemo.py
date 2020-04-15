from selenium import webdriver

driver = webdriver.Chrome("C:\\Chromedriver\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element_by_link_text("Click Here").click()
child_window = driver.window_handles[1]
parent_window = driver.window_handles[0]
driver.switch_to.window(child_window)
print(driver.find_element_by_tag_name("h3"))
driver.close()
driver.switch_to.window(parent_window)
assert "Opening a new window" == driver.find_element_by_tag_name("h3").text
driver.close()