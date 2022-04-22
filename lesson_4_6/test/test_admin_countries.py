import pytest
from pages.AdminCountries import AdminCountriesHelper


@pytest.fixture(scope='function')
def countries_page(driver, auth_admin):
    countries_page = AdminCountriesHelper(driver)
    countries_page.go_to_site('admin/?app=countries&doc=countries')
    yield countries_page


# тест сначала собирает все страны, а потом проверяет их сортировку
def test_get_all_name_countries_check_sort(driver, countries_page):
    all_countries = countries_page.get_all_countries_name()
    is_sort = countries_page.is_sorted(all_countries)
    assert is_sort == True, f'Countries are not sorted. \n "{is_sort[1]}" before "{is_sort[0]}" \n {all_countries}'


# тест, который берет страну и сравнивает с последней в списке
def test_check_countries_sort(driver, countries_page):
    result = countries_page.check_countries_sort()
    assert result == 'sort', \
        f'Countries are not sorted. \n "{result[1]}" before "{result[0]}"'


def test_sort_country_timezone(driver, countries_page):
    is_sort = countries_page.check_sort_zone()
    assert is_sort == True, f'Time Zone {is_sort[2]} {is_sort[3]} \n' \
                            f'are not sorted. \n ' \
                            f'"{is_sort[1]}" before "{is_sort[0]}"'
