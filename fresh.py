from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from twilio.rest import Client

driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
driver_1 = driver
driver_2 = driver
driver_3 = driver

client = Client("acc_sid", "auth")

def baito():
    driver_1.get(
    "https://baito.rs/graficke-kartice?proizvodjac-cipa=nvidia&kolicina-memorije=6-gb+8-gb&vrsta-memorije=ddr6")
    for i in range(0, 110):
        card = driver_1.find_elements_by_class_name('uk-link-heading')
        price = driver_1.find_elements_by_class_name("tm-product-card-price")

        if len(card) != 0:
            for j in card:
                for k in price:
                    if "306" in j.text.casefold().replace(' ', '') and int(k.text[:-3].replace('.', '').strip()) < 150000:
                        print()

                        message = client.messages.create(
                            body="nasao u baito, {} {}".format(j.text, k.text), from_='twiliobr', to='tvojbr')
                        break
        else:
            sleep(5) #broj u sekundama koliko da spava pre nego sto opet proba da nadje
            driver_1.refresh()


def viphouse():
    driver_2.get("https://viphouse.rs/search?q=3060")
    for i in range(0, 110): #stavi koliko zelis da vrti
        try:
            # provera da li uopste prikazuje nesto u pretrazi
            element = driver_2.find_elements_by_class_name("content-product-list")
            # provera da li prikazuje ali nema na zalihama se ne moze implementirati
            price = driver_2.find_elements_by_tag_name("strong")

            for j in price:
                k = j.text.replace('.', '')
                cena = int(k.replace(' RSD', ''))
                if cena < 176000:  # previse
                    print("nasao u vip")
                    message = client.messages.create(
                        body='Grafička kartica pronadjena!{} - viphouse', from_='twiliobr', to='tvojbr').format(element)
                    break
                else:
                    continue

        except NoSuchElementException:
            sleep(5) #broj u sekundama koliko da spava pre nego sto opet proba da nadje
            driver_2.refresh()


def exceed():
    driver_3.get("https://www.exceed.rs/racunarske-komponente/graficke-karte/0/102/0-0")
    for i in range(0, 110): #stavi koliko zelis da vrti

        card = driver_3.find_elements_by_tag_name('h2')
        if len(card) != 0:
            for j in card:
                if '206' in j.text:
                    print("nasao u exceed")

                    message = client.messages.create(
                        body='Grafička kartica pronadjena! {} - exceed'.format(j.text), from_='twiliobr', to='tvojbr')
                    break
                else:
                    continue
        else:
            sleep(5) #broj u sekundama koliko da spava pre nego sto opet proba da nadje
            driver_3.refresh()


baito()
viphouse()
exceed()

driver.quit()
