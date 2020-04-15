from selenium import webdriver

dr = webdriver.Chrome(executable_path="C:\\Chromedriver\\chromedriver.exe")

dr.get("https://rahulshettyacademy.com/AutomationPractice/")
dr.maximize_window()

radioBtn = dr.find_elements_by_css_selector("[type='radio']")
radioBtn[1].click()
assert radioBtn[1].is_selected()

checkBox = dr.find_elements_by_css_selector("[type='checkbox']")
for check in checkBox:
    check.click()
    assert check.is_selected()

dr.close()