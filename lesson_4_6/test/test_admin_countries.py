import time

import pytest
from pages.AdminCountries import AdminCountriesHelper


@pytest.fixture(scope='function')
def countries_page(driver, auth_admin):
    countries_page = AdminCountriesHelper(driver)
    countries_page.go_to_site('admin/?app=countries&doc=countries')
    yield countries_page


# тест сначала собирает все страны, а потом проверяет их сортировку
def test_get_all_name_countries_check_sort(countries_page):
    all_countries = countries_page.get_all_countries_name()
    is_sort = countries_page.is_sorted(all_countries)
    assert is_sort == True, f'Countries are not sorted. \n "{is_sort[1]}" before "{is_sort[0]}" \n {all_countries}'


# тест, который берет страну и сравнивает с последней в списке
def test_check_countries_sort(countries_page):
    result = countries_page.check_countries_sort()
    assert result == 'sort', \
        f'Countries are not sorted. \n "{result[1]}" before "{result[0]}"'


def test_sort_country_geozone(countries_page):
    all_countries_with_zone = countries_page.get_all_countries_with_zone()
    for country_with_zone in all_countries_with_zone:
        # открываем страницу страны
        countries_page.go_to_link(all_countries_with_zone[country_with_zone])
        # проверяем сортировку геозон
        is_sort = countries_page.check_sort_zone(all_countries_with_zone, country_with_zone)
        assert is_sort == True, f'GeoZone {is_sort[2]} {is_sort[3]} \n' \
                                f'are not sorted. \n ' \
                                f'"{is_sort[1]}" before "{is_sort[0]}"'


def test_open_new_win(countries_page):
    countries_page.click_edit_first_country()
    countries_page.wait_open_edit_page('Edit Country')
    all_link = countries_page.get_all_external_link_a()
    # print(len(all_link))
    for link in all_link:
        main_handle = countries_page.get_current_handle()
        countries_page.click_link_and_wit_open(link, [main_handle])
        open_handle = countries_page.get_open_handles()
        for handle in open_handle:
            if handle != main_handle:
                countries_page.switch_to_new_and_close(handle, main_handle)
