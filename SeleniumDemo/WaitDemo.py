import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

dr = webdriver.Chrome(executable_path="C:\\Chromedriver\\chromedriver.exe")

dr.get("https://rahulshettyacademy.com/seleniumPractise/#/")
dr.maximize_window()
# Implicit Wait
dr.implicitly_wait(3)
# try:
dr.find_element_by_class_name("search-keyword").send_keys("ber")
time.sleep(3)
count = len(dr.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
list1 = []
buttons = dr.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    list1.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()

dr.find_element_by_css_selector("a.cart-icon img").click()
dr.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(dr, 5)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
dr.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
dr.find_element_by_class_name("promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
text = dr.find_element_by_class_name("promoInfo").text
assert "Code applied" in text

list2 = []
veggies = dr.find_elements_by_css_selector("p.product-name")
for veggie in veggies:
    list2.append(veggie.text)
print(list1)
print(list2)
assert list1 == list2

actual_total_amount = dr.find_element_by_class_name("totAmt").text
discount_amount = dr.find_element_by_class_name("discountAmt").text
sum = 0
amounts = dr.find_elements_by_css_selector("tr td:nth-child(5) p.amount")
for amount in amounts:
    sum = sum + int(amount.text)
print(sum)
assert int(actual_total_amount) == sum
print(discount_amount)
print(actual_total_amount)
assert float(discount_amount) < int(actual_total_amount)


dr.close()
