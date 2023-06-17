from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
import undetected_chromedriver as uc
from time import sleep


def zxc():

    driver = uc.Chrome()
    id = 6
    url = 'https://www.ratemds.com/best-doctors/'
    driver.get(url)
    file = open("file.csv", "w")

    try:
        # Оргранизационная кнопка антивылет для ожидания появления элементов на странице
        waiter = webdriver.support.wait.WebDriverWait(driver, 60)

        # Первое применение вейтера, чтобы найти кнопку на согласие куки
        waiter.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')))
        agree_button = driver.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')
        agree_button.click()

        while True:

            # Это чекер, который мотает страницу вниз для подгрузки кнопки "На следующею страницу"
            waiter.until(EC.visibility_of_element_located((By.ID, 'newsletter-email')))
            down = driver.find_element(By.ID, 'newsletter-email')
            down.send_keys(Keys.END)

            # Эта фигня находит докторов и выписывает их в файл
            waiter.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-item-doctor-name')))
            elements = driver.find_elements(By.CLASS_NAME, 'search-item-doctor-name')
            counter = 0
            for element in elements:
                file.write(f'\n{element.get_attribute("href")}')
                #print(element.get_attribute('href'))
                counter += 1
                if counter == 10:
                    break

            # Эта фигня находит и ждёт кнопку следующей страницы, а также нажимает её

            waiter.until(
                EC.visibility_of_element_located((By.XPATH, f'//*[@id="doctor-list-container"]/nav/ul/li[{id}]/a')))
            locatebutton = driver.find_element(By.XPATH, f'//*[@id="doctor-list-container"]/nav/ul/li[{id}]/a')

            if id < 11:
                id = id + 1
            if id == 7:
                id = 8

            locatebutton.click()
            sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        file.close()
        driver.quit()


# база №2
def main():
    zxc()


# Ну это база
if __name__ == '__main__':
    main()
