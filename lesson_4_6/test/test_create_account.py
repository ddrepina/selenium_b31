import time
import random
from pages.CreateAccount import CreateAccountHelper


def test_create_account(driver):
    ts = int(time.time())
    fname = f'Ivan{ts}'
    lname = f'Ivanov{ts}'
    postcode = random.randint(10000, 99999)
    city = 'London'
    email = f'london{ts}@mmm.nnn'
    phone = ts
    password = 'pass'
    country = 'United States'
    address1 = f'{city} {postcode} {ts}'
    print(email)
    print(password)
    create_account_page = CreateAccountHelper(driver)
    create_account_page.go_to_site('en/create_account')
    create_account_page.input_fname(fname)
    create_account_page.input_lname(lname)
    create_account_page.input_address(address1)
    create_account_page.input_postcode(postcode)
    create_account_page.input_city(city)
    create_account_page.input_email(email)
    create_account_page.input_phone(phone)
    create_account_page.input_pass(password)
    create_account_page.input_confirm_pass(password)
    create_account_page.select_country(country)
    create_account_page.select_state()
    create_account_page.click_create_account()
    time.sleep(1)
    create_account_page.click_logout()
    time.sleep(1)

    # первый логин новым пользователем
    create_account_page.input_login(email)
    create_account_page.input_pass(password)
    create_account_page.scroll_to_btn_login()
    create_account_page.click_login()
    time.sleep(5)

    create_account_page.click_logout()
