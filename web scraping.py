from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def Practica_raton():
    executable_path = r"C:\Program Files (x86)\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path, options=options)
    driver.get("http://www.pbclibrary.org/raton/mousercise.htm")
    time.sleep(1)
    click = driver.find_element("xpath", '/html/body/table[2]/tbody/tr[2]/td/form/input').click()
    time.sleep(1)
    click1 = driver.find_element("xpath", '/html/body/div/p/a').click()
    time.sleep(1)
    click2 = driver.find_element("xpath", '/html/body/table/tbody/tr/td[2]/p/a').click()
    time.sleep(1)
    click3 = driver.find_element("xpath", '/html/body/table/tbody/tr/td/a').click()
    time.sleep(1)
    click4 = driver.find_element("xpath", '/html/body/table/tbody/tr/td[1]/a').click()
    time.sleep(1)
    click5 = driver.find_element("xpath", '/html/body/table/tbody/tr/td/a').click()
    time.sleep(1)
    click6 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td/p/a').click()
    time.sleep(1)
    click7 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td/p/a').click()
    time.sleep(1)
    click8 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td/p/a').click()
    time.sleep(1)
    click9 = driver.find_element("xpath", '/html/body/table/tbody/tr[3]/td/a[2]').click()
    time.sleep(1)
    click10 = driver.find_element("xpath", '/html/body/table/tbody/tr[3]/td/a[2]').click()
    time.sleep(1)
    click11 = driver.find_element("xpath", '/html/body/table/tbody/tr[3]/td/a[2]').click()
    time.sleep(1)
    click12 = driver.find_element("xpath", '/html/body/table/tbody/tr[3]/td/a[2]').click()
    time.sleep(1)
    click13 = driver.find_element("xpath", '/html/body/table/tbody/tr[3]/td[2]/a[2]').click()
    time.sleep(1)
    click14 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[4]/a').click()
    time.sleep(1)
    click15 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td/a').click()
    time.sleep(1)
    click16 = driver.find_element("xpath", '/html/body/div/table/tbody/tr/td/form/input').click()
    time.sleep(1)
    click17 = driver.find_element("xpath", '/html/body/table/tbody/tr/td/form/input').click()
    time.sleep(1)
    click18 = driver.find_element("xpath", '/html/body/table/tbody/tr/td/form/button').click()
    time.sleep(1)
    click19 = driver.find_element("xpath", '/html/body/table/tbody/tr/td/form/input').click()
    time.sleep(1)
    click20 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[3]/a/img').click()
    time.sleep(1)
    click21 = driver.find_element("xpath", '/html/body/table/tbody/tr[3]/td[2]/a/img').click()
    time.sleep(1)
    click22_1 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[1]/img').click()
    click22_2 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[2]/img').click()
    click22_3 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[3]/img').click()
    click22_4 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[4]/img').click()
    click22_5 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[5]/img').click()
    click22_6 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[6]/img').click()
    click22_7 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[7]/img').click()
    click22_8 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[8]/img').click()
    click22_9 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[9]/img').click()
    click22_10 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[10]/img').click()
    click22_11 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[11]/img').click()
    click22_continuar = driver.find_element("xpath", '/html/body/table/tbody/tr[4]/td/a/img').click()
    time.sleep(1)
    click23_1 = driver.find_element("xpath", '/html/body/div/table/tbody/tr[2]/td[1]/form/input').click()
    click23_2 = driver.find_element("xpath", '/html/body/div/table/tbody/tr[2]/td[3]/form/input').click()
    click23_3 = driver.find_element("xpath", '/html/body/div/table/tbody/tr[3]/td[1]/form/input').click()
    click23_4 = driver.find_element("xpath", '/html/body/div/table/tbody/tr[3]/td[3]/img').click()
    click23_5 = driver.find_element("xpath", '/html/body/div/table/tbody/tr[4]/td[1]/img').click()
    click23_6 = driver.find_element("xpath", '/html/body/div/table/tbody/tr[4]/td[3]/img').click()
    click23_7 = driver.find_element("xpath", '/html/body/div/table/tbody/tr[5]/td[1]/img').click()
    click23_continuar = driver.find_element("xpath", '/html/body/div/table/tbody/tr[5]/td[3]/a/img').click()
    time.sleep(1)

    element = driver.find_element("xpath", '/html/body/div/table/tbody/tr[2]/td[1]/img')

    click_24_2 = ActionChains(driver)
    click_24_2.double_click(on_element= element)
    click_24_2.perform()

    element2 = driver.find_element("xpath", '/html/body/div/table/tbody/tr[2]/td[2]/img')

    click_24_2 = ActionChains(driver)
    click_24_2.double_click(on_element= element2)
    click_24_2.perform()

    element3 = driver.find_element("xpath", '/html/body/div/table/tbody/tr[2]/td[3]/img')

    click_24_2 = ActionChains(driver)
    click_24_2.double_click(on_element= element3)
    click_24_2.perform()

    element4 = driver.find_element("xpath", '/html/body/div/table/tbody/tr[2]/td[4]/img')

    click_24_2 = ActionChains(driver)
    click_24_2.double_click(on_element= element4)
    click_24_2.perform()

    element5 = driver.find_element("xpath", '/html/body/div/table/tbody/tr[3]/td[1]/img')

    click_24_2 = ActionChains(driver)
    click_24_2.double_click(on_element= element5)
    click_24_2.perform()

    element6 = driver.find_element("xpath", '/html/body/div/table/tbody/tr[3]/td[2]/img')

    click_24_2 = ActionChains(driver)
    click_24_2.double_click(on_element= element6)
    click_24_2.perform()

    element7 = driver.find_element("xpath", '/html/body/div/table/tbody/tr[3]/td[3]/img')

    click_24_2 = ActionChains(driver)
    click_24_2.double_click(on_element= element7)
    click_24_2.perform()

    element8 = driver.find_element("xpath", '/html/body/div/table/tbody/tr[3]/td[4]/img')

    click_24_2 = ActionChains(driver)
    click_24_2.double_click(on_element= element8)
    click_24_2.perform()

    click24 = driver.find_element("xpath", '/html/body/div/table/tbody/tr[4]/td/a/img').click()

    time.sleep(1)
    click25_1 = driver.find_element("xpath", '//*[@id="red-slider"]').click()
    click25_2 = driver.find_element("xpath", '//*[@id="red-slider"]').click()
    click25_3 = driver.find_element("xpath", '//*[@id="red-slider"]').click()
    click25_4 = driver.find_element("xpath", '//*[@id="red-slider"]').click()
    click25_5 = driver.find_element("xpath", '//*[@id="red-slider"]').click()

    click25_1 = driver.find_element("xpath", '//*[@id="green-slider"]').click()
    click25_2 = driver.find_element("xpath", '//*[@id="green-slider"]').click()
    click25_3 = driver.find_element("xpath", '//*[@id="green-slider"]').click()
    click25_4 = driver.find_element("xpath", '//*[@id="green-slider"]').click()
    click25_5 = driver.find_element("xpath", '//*[@id="green-slider"]').click()

    click25_1 = driver.find_element("xpath", '//*[@id="blue-slider"]').click()
    click25_2 = driver.find_element("xpath", '//*[@id="blue-slider"]').click()
    click25_3 = driver.find_element("xpath", '//*[@id="blue-slider"]').click()
    click25_4 = driver.find_element("xpath", '//*[@id="blue-slider"]').click()
    click25_5 = driver.find_element("xpath", '//*[@id="blue-slider"]').click()
    
    click25_6 = driver.find_element("xpath", '//*[@id="canvas"]/table/tbody/tr[3]/td/a').click()

    time.sleep(1)
    click26 = driver.find_element("xpath", '/html').click()
    click26 = driver.find_element("xpath", '/html').click()
    click26 = driver.find_element("xpath", '/html').click()
    click26 = driver.find_element("xpath", '/html').click()
    click26 = driver.find_element("xpath", '/html').click()
    click26 = driver.find_element("xpath", '/html').click()
    click26 = driver.find_element("xpath", '/html').click()
    click26 = driver.find_element("xpath", '/html').click()
    click26 = driver.find_element("xpath", '/html').click()
    click26 = driver.find_element("xpath", '/html').click()
    click26 = driver.find_element("xpath", '/html').click()
    click26 = driver.find_element("xpath", '/html').click()
    click26 = driver.find_element("xpath", '/html').click()
    click26 = driver.find_element("xpath", '/html').click()
    click26 = driver.find_element("xpath", '/html').click()

    click26_2 = driver.find_element("xpath", '/html/body/p[1]/a').click()
    
    time.sleep(1)

    for i in range(1,20):
        click27 = driver.find_element("xpath", '/html').click()

    click27_2 = driver.find_element("xpath", '/html/body/div/p[1]/a').click()

    time.sleep(1)

    for i in range(1,90):
        click28 = driver.find_element("xpath", '/html').click()

    click28_2 = driver.find_element("xpath", '/html/body/div/p[2]/a').click()

    time.sleep(1)

    for i in range(1,10):
        click29 = driver.find_element("xpath", '/html').click()

    click29_2 = driver.find_element("xpath", '/html/body/table/tbody/tr/td[2]/p/a').click()

    time.sleep(1)

    for i in range(1,20):
        click30 = driver.find_element("xpath", '/html').click()

    for i in range(1,10):
        click30 = driver.find_element("xpath", '/html').click()

    click30 = driver.find_element("xpath", '/html/body/div/table/tbody/tr/td[2]/p/a').click()

    time.sleep(1)

    click31 = driver.find_element("xpath", '/html/body/table/tbody/tr/td/a').click()

    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    
    time.sleep(1)

    click32 = driver.find_element("xpath", '/html/body/table/tbody/tr/td[2]/span/a').click()

    time.sleep(1)

    click33 = driver.find_element("xpath", '/html/body/form/input[1]').click()
    click33 = driver.find_element("xpath", '/html/body/form/input[2]').click()
    click33 = driver.find_element("xpath", '/html/body/form/input[3]').click()
    click33 = driver.find_element("xpath", '/html/body/form/input[4]').click()
    click33 = driver.find_element("xpath", '/html/body/form/input[5]').click()
    click33 = driver.find_element("xpath", '/html/body/form/input[6]').click()
    click33 = driver.find_element("xpath", '/html/body/form/input[7]').click()
    click33 = driver.find_element("xpath", '/html/body/form/input[8]').click()
    click33 = driver.find_element("xpath", '/html/body/form/input[9]').click()

    click33 = driver.find_element("xpath", '/html/body/p/a/img').click()

    time.sleep(1)

    click34 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td/form/input[1]').click()
    click34 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td/form/input[7]').click()

    time.sleep(1)

    click35 = driver.find_element("xpath", '/html/body/form/input[1]').click()
    click35 = driver.find_element("xpath", '/html/body/form/input[2]').click()
    click35 = driver.find_element("xpath", '/html/body/form/input[3]').click()
    click35 = driver.find_element("xpath", '/html/body/form/input[4]').click()
    click35 = driver.find_element("xpath", '/html/body/form/input[5]').click()
    click35 = driver.find_element("xpath", '/html/body/form/input[6]').click()
    click35 = driver.find_element("xpath", '/html/body/form/input[7]').click()
    click35 = driver.find_element("xpath", '/html/body/form/input[8]').click()
    click35 = driver.find_element("xpath", '/html/body/form/input[9]').click()
    click35 = driver.find_element("xpath", '/html/body/p/a/img').click()

    time.sleep(1)

    click36 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td/form/input[1]').click()
    click36 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td/form/input[5]').click()

    time.sleep(1)

    click37 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td/form/select').click()
    click37 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td/form/select/option[6]').click()
    click37 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td/form/p/a/img').click()

    time.sleep(1)

    click38 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td/form/select').click()
    click38 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td/form/select/option[7]').click()
    click38 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td/form/p/a/img').click()

    time.sleep(1)

    click39 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td/form/select').click()
    click39 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td/form/select/option[6]').click()
    click39 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td/form/p/a/img').click()

    time.sleep(3)

    click40 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td/form/select/option[2]').click()
    click40 = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td/form/input').click()
    

    time.sleep(3)

    click41 = driver.find_element("xpath", '/html/body/form/input[1]').click()
    click41 = driver.find_element("xpath", '/html/body/form/input[2]').click()
    click41 = driver.find_element("xpath", '/html/body/form/input[3]').click()


if __name__ =='__main__':
    Practica_raton()



# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)




# def Practica_raton():
#     PATH = "C:\Program Files (x86)\chromedriver.exe"
#     driver = webdriver.Chrome(PATH)
#     driver.get("http://www.pbclibrary.org/raton/mousercise.htm")
#     time.sleep(10)
#     click = driver.find_element("xpath", '/html/body/table[2]/tbody/tr[2]/td/form/input')
#     click.click()

# Practica_raton()