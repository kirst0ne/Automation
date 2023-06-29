from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

#Нажмите на вкладку "My Account"
Account_btn = driver.find_element_by_link_text("My Account").click()
#В разделе "Login", введите email для регистрации
email = driver.find_element_by_css_selector("#username")
email.send_keys("username@mail.ru")
#В разделе "Login", введите пароль для регистрации
password = driver.find_element_by_css_selector("#password")
password.send_keys("12321b35162b")
#Нажмите на кнопку "Login"
Login_btn = driver.find_element_by_css_selector("[value='Login']").click()
#Проверьте, что на странице есть элемент "Logout"
Logout_check = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a")))

driver.quit()