from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from twilio.rest import Client

driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
driver.get("https://is.gd/bSJ635")

for i in range(0, 3):  # za nedelju 20161, za jedan dan 2881
    try:
        price = driver.find_elements_by_class_name("adPrice")
        name = driver.find_elements_by_class_name("adName")
        count = 0
        for j in price:
            if 'din' not in j.text:
                k = j.text.replace(',', '')
                a = k.replace('00 ', '')
                cena = int(a.replace('€', ''))
                if cena < 800 and 'gainward' not in name[count].text.casefold() and 'galax' not in name[count].text.casefold() and 'pny' not in name[count].text.casefold() and 'palit' not in name[count].text.casefold() and 'kfa' not in name[count].text.casefold() and 'colorful' not in name[count].text.casefold():
                    account_sid = 'hidden'
                    auth_token = '0fac2f9027d4393ec08ad8fd0142905b'
                    client = Client(account_sid, auth_token)
                    message = client.messages.create(
                        body='Grafička kartica pronadjena! - {}'.format(name[count].text.casefold()), from_='+12404340871', to='=+381695162280')
                    break
                else:
                    count += 1
                    continue
            else:
                continue
        break
    except NoSuchElementException as exception:
        sleep(30)
        driver.refresh()

driver.quit()
