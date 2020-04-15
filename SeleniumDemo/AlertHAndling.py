from selenium import webdriver

dr = webdriver.Chrome(executable_path="C:\\Chromedriver\\chromedriver.exe")

dr.get("https://rahulshettyacademy.com/AutomationPractice/")
dr.maximize_window()

dr.find_element_by_id("name").send_keys("Raman")
dr.find_element_by_css_selector("[value='Alert']").click()
dr.switch_to.alert.accept()