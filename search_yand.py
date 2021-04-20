import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
sys.path.append('../')
success = True
#обозначаем параметры
pathdriver = sys.argv[1]
url = sys.argv[2]
search_body = sys.argv[3]
search_result = sys.argv[4]

# pathdriver = "C:\distrib"
# url = "https://ya.ru"
# search_body = 'Совкомбанк'
# search_result = "sovcombank.ru"

if len(sys.argv) < 4:
    print('FAILED. parameters are missed ' )
    sys.exit()

try:
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(executable_path = pathdriver + '\chromedriver.exe', options=options)
    driver.get(url) # Переходим на url-яндекс
    driver.implicitly_wait(5)
    search = driver.find_element_by_xpath("//*[@class='input__control input__input mini-suggest__input']")
    search.send_keys(search_body)

    #Проверяем таблицу с подсказками
    suggest = driver.find_element_by_xpath("//*[@class='mini-suggest__popup mini-suggest__popup_svg_yes mini-suggest__popup_theme_transparent']")
    driver.implicitly_wait(10)
    print("ответ 4: таблица с подсказаками присутствует. Список:")
    text_suggest = driver.find_element_by_xpath("//*[@class='mini-suggest__popup mini-suggest__popup_svg_yes mini-suggest__popup_theme_transparent mini-suggest__popup_visible']")
    print(text_suggest.text)
    if search_body in text_suggest.text:
        print("Ответ 5: Подстрока " + search_body + "Найдена")
    else:
        print("Ответ 5: Подстроки " + search_body + " НЕТ")

    search.send_keys(Keys.ENTER)
    results = driver.find_element_by_xpath("//*[contains(@class, 'serp-list serp-list_left_yes')]")
    print("Ответ 6: Таблица результатов поиска есть")

    # Проверяем, что первые 5 результатов содержат вхождения ссылки на сайт из 4го параметра
    array_results = []
    for i in range (2,7):
        text_result = driver.find_element_by_xpath("//*[@class = 'serp-item'][" + str(i) + "]")
        array_results.append(text_result.text)
    entry_str = list(map(lambda x: search_result in x, array_results))
    print("Ответ 7 В первых 5 результатах ссылка на " + search_result + "присутствует " + str(entry_str.count(True)) + " раз")
finally:
    if not success:
        raise Exception ("Test failed.")
        driver.quit()
driver.quit()

