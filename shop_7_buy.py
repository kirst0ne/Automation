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
driver.execute_script("window.scrollBy(0, 300);")
#Добавьте в корзину книгу "HTML5 WebApp Development"
Book_in_Basket = driver.find_element_by_css_selector("[data-product_id='182']").click()
time.sleep(5)
#Переход в корзину
Basket = driver.find_element_by_css_selector("a.wpmenucart-contents").click()
#Нажмите "PROCEED TO CHECKOUT"
time.sleep(5)
Proceed_to_checkout_btn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-forward")))
Proceed_to_checkout_btn.click()
#Заполните обязательные поля
time.sleep(5)
First_name = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))
First_name.send_keys("username")
Last_name = driver.find_element_by_id("billing_last_name")
Last_name.send_keys("username")
email = driver.find_element_by_id("billing_email")
email.send_keys("username@mail.ru")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("89999966699")
Country = driver.find_element_by_id("s2id_billing_country").click()
Country_write = driver.find_element_by_id("s2id_autogen1_search")
Country_write.send_keys("Russ")
Country_ckeck = driver.find_element_by_css_selector(".select2-result-label > .select2-match").click()
time.sleep(5)
Adress = driver.find_element_by_css_selector("input#billing_address_1")
Adress.send_keys("Pulkovskaya st")
City = driver.find_element_by_css_selector("input#billing_city")
City.send_keys("SPb")
State = driver.find_element_by_css_selector("input#billing_state")
State.send_keys("SPb")
Postcode = driver.find_element_by_css_selector("input#billing_postcode")
Postcode.send_keys("666")
#Выберите способ оплаты "Check Payments"
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
Check_Payments = driver.find_element_by_css_selector("input#payment_method_cheque")
Check_Payments.click()
#Нажмите "Place Order"
Place_order_ckeck = driver.find_element_by_css_selector("input#place_order").click()
#Проверьте что отображается надпись "Thank you. Your order has been received."
Message1 = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
#Проверьте что в Payment Method отображается текст "Check Payments"
Message2 = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order_details tr:nth-child(3) td"), "Check Payments"))

driver.quit()