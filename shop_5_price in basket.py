from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

#Нажмите на вкладку "Shop"
Shop_btn = driver.find_element_by_css_selector("#menu-item-40").click()
#Добавьте в корзину книгу "HTML5 WebApp Development"
Book_in_Basket = driver.find_element_by_css_selector("[data-product_id='182']").click()
#Тест на количество товаров в корзине
time.sleep(5)
quantity = driver.find_element_by_css_selector("#wpmenucartli .cartcontents")
quantity_get_text = quantity.text
assert quantity_get_text == "1 Item"
#Тест на стоимость товаров в корзине
price = driver.find_element_by_css_selector("a > span.amount")
price_get_text = price.text
assert price_get_text == "₹180.00"
#Переход в корзину
Basket = driver.find_element_by_css_selector(".wpmenucart-contents").click()
#Проверка, что в Subtotal отобразилась стоимость
Subtotal = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "div.cart_totals tr.cart-subtotal span.woocommerce-Price-amount.amount")))
#Проверка, что в Total отобразилась стоимость
Total = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "div.cart_totals tr.order-total span.woocommerce-Price-amount.amount")))

driver.quit()