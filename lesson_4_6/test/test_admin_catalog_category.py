import pytest
from pages.AdminCatalogCategory import AdminCatalogCategoryHelper
import pytest_check as check


@pytest.fixture(scope='function')
def admcatalogcategory_page(driver, auth_admin):
    page = AdminCatalogCategoryHelper(driver)
    page.go_to_site('admin/?app=catalog&doc=catalog&category_id=1')
    yield page


def test_open_category_liten_log(admcatalogcategory_page):
    all_link = admcatalogcategory_page.get_link_all_product()
    type_logs = admcatalogcategory_page.get_log_type()
    assert 'browser' in type_logs, f'type log "browser" not in {type_logs}'
    for link in all_link:
        admcatalogcategory_page.go_to_link(link)
        logs = admcatalogcategory_page.get_log_for_log_type(link, 'browser')
        check.is_none(logs)
