from selenium import webdriver

dr = webdriver.Chrome(executable_path="C:\\Chromedriver\\chromedriver.exe")

dr.get("https://rahulshettyacademy.com/angularpractice/")
dr.maximize_window()
dr.find_element_by_css_selector("input[name='name']").send_keys("Raman Gairola")
dr.find_element_by_css_selector("input[name='email']").send_keys("ramangairola@gmail.com")
dr.find_element_by_css_selector("input[placeholder='Password']").send_keys("9971969010")
dr.find_element_by_css_selector("input[type='checkbox']").click()
dr.find_element_by_css_selector("input[value='option2']").click()
dr.find_element_by_css_selector("input[value='Submit']").click()

message = dr.find_element_by_class_name("alert-success").text

assert "success" in message
