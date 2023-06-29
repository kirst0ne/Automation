from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

#Залогиньтесь
Account_btn = driver.find_element_by_link_text("My Account").click()
email = driver.find_element_by_css_selector("#username")
email.send_keys("username@mail.ru")
password = driver.find_element_by_css_selector("#password")
password.send_keys("12321b35162b")
Login_btn = driver.find_element_by_css_selector("[value='Login']").click()
#Нажмите на вкладку "Shop"
Shop_btn = driver.find_element_by_css_selector("#menu-item-40").click()
#Откройте книгу "Android Quick Start Guide"
Book_btn = driver.find_element_by_css_selector("[alt='Android Quick Start Guide']").click()
#Тест на содержимое старой цены = 600
old_price = driver.find_element_by_css_selector(".price > del > span.woocommerce-Price-amount.amount")
old_price_get_text = old_price.text
assert old_price_get_text == "₹600.00"
#Тест на содержимое новой цены = 450
new_price = driver.find_element_by_css_selector("ins > span.woocommerce-Price-amount.amount")
new_price_get_text = new_price.text
assert new_price_get_text == "₹450.00"
#Нажатие на обложку книги
Image_check = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".attachment-shop_single.size-shop_single.wp-post-image")))
Image_check.click()
#Закрытие предпросмотра
Image_check = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
Image_check.click()

driver.quit()