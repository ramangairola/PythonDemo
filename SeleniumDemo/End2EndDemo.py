from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

dr = webdriver.Chrome(executable_path="C:\\Chromedriver\\chromedriver.exe")

dr.get("https://rahulshettyacademy.com/angularpractice/")

dr.find_element_by_css_selector("a[href*='shop']").click()
products = dr.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    product_name = product.find_element_by_xpath("div/h4/a").text
    if product_name == "iphone X":
        product.find_element_by_xpath("div/button").click()
        break

dr.find_element_by_css_selector(".btn-primary").click()

product_checkout = dr.find_element_by_xpath("//div[@class='media']//h4").text
assert product_checkout == "iphone X"

dr.find_element_by_css_selector(".btn-success").click()

dr.find_element_by_id("country").send_keys("Ind")
wait = WebDriverWait(dr, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
dr.find_element_by_link_text("India").click()
dr.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

dr.find_element_by_class_name("btn-success").click()

success_message = dr.find_element_by_class_name("alert").text
print(success_message)
assert "Success" in success_message
dr.get_screenshot_as_file("Success.png")
dr.close()
