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
#В разделе "Register", введите email для регистрации
email = driver.find_element_by_css_selector("#reg_email")
email.send_keys("username@mail.ru")
#В разделе "Register", введите пароль для регистрации
password = driver.find_element_by_css_selector("#reg_password")
password.send_keys("12321b35162b")
#Нажмите на кнопку "Register"
Register_btn = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[value='Register']")))
Register_btn.click()

driver.quit()