from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from twilio.rest import Client

driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
driver.get("https://www.eponuda.com/graficke-kartice-cene/1/f6_0~f10_1-4")
count = -1

for i in range(0, 11):  # za nedelju 20161, za jedan dan 2881
    try:
        price = driver.find_elements_by_class_name('b-paging-product__price')
        ime = driver.find_elements_by_class_name('b-paging-product__title')
        for j in price:
            count += 1
            k = j.text.replace('.', '')
            f = k.replace('din', '')
            s = f.replace(' ', '')
            cena = s[:5]
            if int(cena) < 76000 and '3070' in ime[count].text:  # previse
                account_sid = 'hidden'
                auth_token = 'hidden'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    body='Grafička kartica pronadjena! - eponuda - {}'.format(ime[count].text), from_='hidden', to='hidden')
                break
            else:
                continue
        break
    except NoSuchElementException as exception:
        sleep(30)
        driver.refresh()

driver.quit()
