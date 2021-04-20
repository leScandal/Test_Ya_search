from selenium import webdriver
from PIL import Image, ImageChops
import requests

pathdriver = "C:\distrib"
url1 = "https://yandex.ru"
link_text = "Картинки"

def difference_images(img1, img2):
    image_1 = Image.open(img1)
    image_2 = Image.open(img2)
    result=ImageChops.difference(image_1, image_2).getbbox()
    if result==None:
        print('Ответ 7: При движении назад картинка изменилась на картинку из ш.5')
    else:
        print ('Ответ 6: При движении вперед картинка изменилась')


def save_img(num):
    driver.implicitly_wait(10)
    file = open (r'file_img'+str(num), "wb")
    data_src = driver.find_element_by_css_selector('img.MMImage-Origin').get_attribute("src")
    file.write(requests.post(data_src).content)
    file.close()


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(executable_path = pathdriver + '\chromedriver.exe', options=options)
driver.get(url1)
driver.implicitly_wait(5)
driver.find_element_by_link_text(link_text).click()
driver.switch_to.window(driver.window_handles[1])  #новое окно
#Проверка текущего адреса
driver.find_element_by_xpath("(//*[@class = 'PopularRequestList-Shadow'])[1]").click()
url = driver.current_url
print(url)
if url.find("yandex.ru/images/") != -1:
    print("Ответ 4: Да, перешли на  " + url)
else:
    print("Ответ 4: Сcылка иная " + url)

# Открываем первую картинку
driver.implicitly_wait(5)
# Проверка открытия
try:
   driver.find_element_by_class_name("serp-item__link").click()  #open 1 image  работает чз раз
except:
   driver.find_element_by_xpath("(//*[@class = 'serp-item__link'])[1]").click()
save_img(1)
#навигация
driver.find_element_by_css_selector('img.MMImage-Origin').click() #press button forward
save_img(2)
driver.find_element_by_class_name ("CircleButton_type_prev").click ()  # press previous
save_img(3)

difference_images(r'file_img1', r'file_img2')
difference_images(r'file_img1', r'file_img3')

driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.close()
