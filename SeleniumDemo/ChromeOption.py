from selenium import webdriver

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--ignore_certificate_errors")
chrome_option.add_argument("headless")

dr = webdriver.Chrome(executable_path="C:\\Chromedriver\\chromedriver.exe",options=chrome_option)

dr.get("https://rahulshettyacademy.com/angularpractice/")
print(dr.title)