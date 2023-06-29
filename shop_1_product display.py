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
#Откройте книгу "HTML 5 Forms"
Book_btn = driver.find_element_by_css_selector("[alt='Mastering HTML5 Forms']").click()
#Проверка на заголовок кники "HTML5 Forms"
text_heading= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product_title.entry-title"), "HTML5 Forms"))

driver.quit()