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
#Добавление книг "HTML5 WebApp" и "JS Data Structures" в корзину
driver.execute_script("window.scrollBy(0, 300);")
Book1_in_Basket = driver.find_element_by_css_selector("[data-product_id='182']").click()
time.sleep(5)
Book2_in_Basket = driver.find_element_by_css_selector("[data-product_id='180']").click()
#Переход в корзину
Basket = driver.find_element_by_css_selector(".wpmenucart-contents").click()
#Удаление 1-ой книги
time.sleep(5)
Delete = driver.find_element_by_css_selector("[data-product_id='182']").click()
#Отмена удаления
Undo = driver.find_element_by_link_text("Undo?").click()
#Увеличение количества до 3 шт книги "JS Data Structures"
Clear_window = driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']").clear()
Window = driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
Window.send_keys("3")
#Нажмите на кнопку "UPDATE BASKET"
Update_Basket = driver.find_element_by_css_selector("[name='update_cart']")
#Тест, что value элемента quantity для "JS Data Structures and равно 3
quantity = driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
quantity_value = quantity.get_attribute("value")
assert quantity_value == "3"
#Нажмите на кнопку ""APPLY COUPON"
time.sleep(5)
Apply_Coupon = driver.find_element_by_css_selector("div.coupon > input.button").click()
#Добавьте тест, что возникло сообщение : "Please enter a coupon"
Message = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error li"), "Please enter a coupon code."))

driver.quit()