from selenium import webdriver
from selenium.webdriver.support.select import Select

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
#Проверка на то, что в селекторе выбрана сортировка по умолчанию
sorting_default = driver.find_element_by_css_selector("select.orderby > option:nth-child(1)")
sorting_default_selected = sorting_default.get_attribute("selected")
print("value of sorting_default: ", sorting_default_selected)
if sorting_default_selected is not None:
    print("Default sorting")
else:
    print("False")
#Сортировка товаров по цене от большей к меньшей
sorting_default2 = driver.find_element_by_css_selector("select.orderby")
select = Select(sorting_default2)
select.select_by_value("price-desc")
#Проверка на то, что в селекторе выбрана сортировка от большей к меньшей
sorting_high_low = driver.find_element_by_css_selector("select.orderby > option:nth-child(6)")
sorting_high_low_selected = sorting_high_low.get_attribute("selected")
print("value of sorting_high_low: ", sorting_high_low_selected)
if sorting_high_low_selected is not None:
    print("Sort by price: high to low")
else:
    print("False")

driver.quit()