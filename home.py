from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

#Скролл страницы на 600 пикселей вниз
driver.execute_script("window.scrollBy(0, 600);")
#Нажмите на название книги "Selenium Ruby"
Selenium_Ruby_btn = driver.find_element_by_xpath("//h3[text()='Selenium Ruby']").click()
#Нажмите на вкладку "Reviews"
Reviews_btn = driver.find_element_by_css_selector("li.reviews_tab").click()
#Поставьте 5 звезд
Five_stars_btn = driver.find_element_by_css_selector(".star-5").click()
#Заполните поле "Review" сообщением: "Nice book!"
comments = driver.find_element_by_css_selector("#comment")
comments.send_keys("Nice book!")
#Заполните поле "Name"
name = driver.find_element_by_css_selector("#author")
name.send_keys("Kirill")
#Заполните поле "Email"
email = driver.find_element_by_css_selector("#email")
email.send_keys("username@mail.ru")
#Нажмите на кнопку "Submit"
Submit = driver.find_element_by_css_selector("#submit.submit").click()

driver.quit()