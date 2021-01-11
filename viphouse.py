from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from twilio.rest import Client

driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
driver.get("https://viphouse.rs/search?q=3060+ti")

for i in range(0, 11):  # za nedelju 20161, za jedan dan 2881
    try:
        # provera da li uopste prikazuje nesto u pretrazi
        element = driver.find_elements_by_class_name("content-product-list")
        # provera da li prikazuje ali nema na zalihama se ne moze implementirati
        price = driver.find_elements_by_tag_name("strong")

        for j in price:
            k = j.text.replace('.', '')
            cena = int(k.replace(' RSD', ''))
            if cena < 70000:  # previse
                account_sid = 'hidden'
                auth_token = 'hidden'
                client = Client(account_sid, auth_token)
                print('graficka pronadjena')
                message = client.messages.create(
                    body='Grafička kartica pronadjena!', from_='hidden', to='hidden')
                break
            else:
                continue

        break
    except NoSuchElementException as exception:
        sleep(30)
        driver.refresh()

driver.quit()
