from selenium import webdriver

dr = webdriver.Chrome(executable_path="C:\\Chromedriver\\chromedriver.exe")

dr.get("https://rahulshettyacademy.com/angularpractice/")
dr.maximize_window()

name = dr.find_element_by_name("name")
name.send_keys("Raman")
print(name.text)

print(dr.execute_script("return arguments[0].value;", name))

shop = dr.find_element_by_css_selector("a[href*='shop']")
dr.execute_script("arguments[0].click();", shop)
dr.execute_script("window.scrollTo(0,document.body.scrollHeight);")

dr.close()
