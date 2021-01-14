from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from twilio.rest import Client

driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
driver.get("https://www.winwin.rs/catalogsearch/result/?q=RTX+3070")

for i in range(0, 11):  # za nedelju 20161, za jedan dan 2881
    try:
        # provera da li uopste prikazuje nesto u pretrazi
        element = driver.find_element_by_class_name("products-grid")
        # provera da li prikazuje ali nema na zalihama
        in_stock = driver.find_element_by_class_name("product-details")
        price = driver.find_elements_by_class_name('price')

        for j in price:
            k = j.text.replace('.', '')
            cena = int(k.replace(' RSD', ''))
            if cena < 80000:  # previse
                account_sid = 'hidden'
                auth_token = 'hidden'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    body='Grafička kartica pronadjena! - winwin', from_='hidden', to='hidden')
                break
            else:
                continue

        break
    except NoSuchElementException as exception:
        sleep(30)
        driver.refresh()

driver.quit()
