from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from twilio.rest import Client

driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
driver.get(
    "https://www.exceed.rs/racunarske-komponente/graficke-karte/0/102/55000-70000")
target_card = '3060'
ti = 'ti'

for i in range(0, 11):  # za nedelju 20161, za jedan dan 2881
    card = driver.find_elements_by_tag_name('h2')
    if len(card) != 0:
        for j in card:
            if target_card in j.text.casefold().replace(' ', '') and ti in j.text.casefold().replace(' ', ''):
                account_sid = 'hidden'
                auth_token = 'hidden'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    body='Grafička kartica pronadjena!', from_='hidden', to='hidden')
                break
            else:
                continue
        break
    else:
        sleep(30)
        driver.refresh()

driver.quit()
