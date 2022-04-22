import pytest
from pages.AdminGeoZone import AdminGeoZoneHelper


@pytest.fixture(scope='function')
def geozone_page(driver, auth_admin):
    countries_page = AdminGeoZoneHelper(driver)
    countries_page.go_to_site('admin/?app=geo_zones&doc=geo_zones')
    yield countries_page


def test_sort_name_countries(driver, geozone_page):
    countries = geozone_page.get_all_countries()
    result = geozone_page.check_sort_geozone(countries)
    assert result == 'sort', \
        f'Countries are not sorted. \n "{result[1]}" before "{result[0]}"'
