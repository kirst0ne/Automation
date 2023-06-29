from selenium import webdriver

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
#Откройте категорию "HTLM"
HTLM_cat_btn = driver.find_element_by_xpath("//a[@href='https://practice.automationtesting.in/product-category/html/']").click()
#Проверка на отображение 3х товаров
HTML_element = driver.find_elements_by_css_selector("a.woocommerce-LoopProduct-link")
if len(HTML_element) == 3:
    print("В категории 3 товара")
else:
    print("Ошибка. Количество товаров в корзине: " + str(len(HTML_element)))

driver.quit()