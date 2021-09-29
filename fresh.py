from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
# from twilio.rest import Client
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
driver_1 = driver
driver_2 = driver
driver_3 = driver

driver_1.get(
    "https://baito.rs/graficke-kartice?proizvodjac-cipa=nvidia&kolicina-memorije=6-gb+8-gb&vrsta-memorije=ddr6")
driver_2.get("https://www.exceed.rs/racunarske-komponente/graficke-karte/0/102/0-0")
driver_3.get("https://viphouse.rs/search?q=3060")
target_card = '306'
ti = 'ti'

for i in range(0, 11):
    card_1 = driver_1.find_elements_by_class_name('uk-link-heading')
    card_2 = driver_2.find_elements_by_class_name('h2')
    # card_3 = driver_3.find_elements_by_class_name('uk-link-heading')

    # baito
    if len(card_1) != 0:
        for j in card_1:
            if target_card in j.text.casefold().replace(' ', '') and ti in j.text.casefold().replace(' ', ''):
                account_sid = 'hidden'
                auth_token = 'hidden'
                print("nasao u baito")
                # client = Client(account_sid, auth_token)

                # message = client.messages.create(
                #     body='Grafička kartica pronadjena!', from_='hidden', to='hidden')
                break

    # exceed
    try:
        # provera da li uopste prikazuje nesto u pretrazi
        element = driver_2.find_elements_by_class_name("content-product-list")
        # provera da li prikazuje ali nema na zalihama se ne moze implementirati
        price = driver_2.find_elements_by_tag_name("strong")

        for j in price:
            k = j.text.replace('.', '')
            cena = int(k.replace(' RSD', ''))
            if cena < 376000:  # previse
                account_sid = 'hidden'
                auth_token = 'hidden'
                print("nasao u exceed")
                # client = Client(account_sid, auth_token)
                # message = client.messages.create(
                #     body='Grafička kartica pronadjena! - viphouse', from_='hidden', to='hidden')
                break
            else:
                continue

        break
    except NoSuchElementException as exception:
        print("nema")
        break

driver.quit()
