from pages.MainStorePage import MainStorePageHelper


def test_main_store(driver):
    main_store_page = MainStorePageHelper(driver)
    main_store_page.go_to_site('en/')
    main_store_page.check_one_sticker()


def test_check_product(driver):
    main_store_page = MainStorePageHelper(driver)
    main_store_page.go_to_site('en/')
    main_store_page.scroll_to_campaigns()
    main_name = main_store_page.get_product_name()
    main_product_href = main_store_page.get_product_href()
    main_regular_price_value = main_store_page.get_regular_price_and_values_css()
    main_campaign_price_value = main_store_page.get_campaign_price_and_values_css()
    assert main_store_page.check_grey(main_regular_price_value['color']), \
        f'main regular price value is not grey.\n style is {main_regular_price_value["text-decoration"]}'
    assert main_store_page.check_red(main_campaign_price_value['color']), \
        f'main campaign price value is not red.\n style is {main_campaign_price_value["text-decoration"]}'
    assert main_store_page.check_line_through(main_regular_price_value['text-decoration']), \
        f'main regular price value is not line through.\n  style is  {main_regular_price_value["text-decoration"]}'
    assert not main_store_page.check_line_through(main_campaign_price_value['text-decoration']), \
        f'main campaign price value is line through.\n  style is  {main_campaign_price_value["text-decoration"]}'
    assert main_store_page.check_campaign_size_big_regular_size(main_campaign_price_value['font-size'],
                                                                main_regular_price_value['font-size']), \
        f'main font-size campaign price < font-size regular price.\n  ' \
        f'font-size campaign = {main_campaign_price_value["font-size"]}' \
        f'font-size regular = {main_regular_price_value["font-size"]}'

    assert main_store_page.check_campaign_weight_big_regular_wight(main_campaign_price_value['font-weight'],
                                                                   main_regular_price_value['font-weight']), \
        f'main font-weight campaign price < font-weight regular price.\n  ' \
        f'font-weight campaign = {main_campaign_price_value["font-weight"]}' \
        f'font-weight regular = {main_regular_price_value["font-weight"]}'
    # print(main_regular_price_value)
    # print(main_campaign_price_value)

    main_store_page.go_to_link(main_product_href)
    product_name = main_store_page.get_pp_product_name()
    assert product_name == main_name, f'{product_name} {main_name}'
    pp_regular_price_value = main_store_page.get_pp_regular_price_and_values_css()
    pp_campaign_price_value = main_store_page.get_pp_campaign_price_and_values_css()
    # print(pp_regular_price_value)
    # print(pp_campaign_price_value)
    # Обычная цена на главноей странице РАВНА обычной цене на странице продукта
    assert pp_regular_price_value['regular_price_int'] == main_regular_price_value['regular_price_int'], \
        f"product page regular_price != main paige regular_price\n" \
        f"product page regular_price = {pp_regular_price_value['regular_price_int']} \n" \
        f"main paige regular_price_value {main_regular_price_value['regular_price_int']}"
    # Акционная цена на главноей странице РАВНА акционной цене на странице продукта
    assert pp_campaign_price_value['campaign_price_int'] == main_campaign_price_value['campaign_price_int'], \
        f"product page campaign_price != main paige campaign_price\n" \
        f"product page campaign_price = {pp_campaign_price_value['campaign_price_int']} \n" \
        f"main paige campaign_price_value {main_campaign_price_value['campaign_price_int']}"
    # Обычная цена на главноей странице БОЛЬШЕ акционной цены на главной странице
    assert main_regular_price_value['regular_price_int'] > main_campaign_price_value['campaign_price_int'], \
        f"main page regular_price != main paige campaign_price\n" \
        f"main page regular_price = {main_regular_price_value['regular_price_int']} \n" \
        f"main paige campaign_price_value {main_campaign_price_value['campaign_price_int']}"
    # Обычная цена на странице продукта БОЛЬШЕ акционной цены на странице продукта
    assert pp_regular_price_value['regular_price_int'] > pp_campaign_price_value['campaign_price_int'], \
        f"pp page regular_price != pp paige campaign_price\n" \
        f"pp page regular_price = {pp_regular_price_value['regular_price_int']} \n" \
        f"pp paige campaign_price_value {pp_campaign_price_value['campaign_price_int']}"

    assert main_store_page.check_grey(pp_regular_price_value['color']), \
        f'main regular price value is not grey.\n style is {pp_regular_price_value["text-decoration"]}'
    assert main_store_page.check_red(pp_campaign_price_value['color']), \
        f'main campaign price value is not red.\n style is {pp_campaign_price_value["text-decoration"]}'
    assert main_store_page.check_line_through(pp_regular_price_value['text-decoration']), \
        f'main regular price value is not line through.\n  style is  {pp_regular_price_value["text-decoration"]}'
    assert not main_store_page.check_line_through(pp_campaign_price_value['text-decoration']), \
        f'main campaign price value is line through.\n  style is  {pp_campaign_price_value["text-decoration"]}'
    assert main_store_page.check_campaign_size_big_regular_size(pp_campaign_price_value['font-size'],
                                                                pp_regular_price_value['font-size']), \
        f'main font-size campaign price < font-size regular price.\n  ' \
        f'font-size campaign = {pp_campaign_price_value["font-size"]}' \
        f'font-size regular = {pp_regular_price_value["font-size"]}'

    assert main_store_page.check_campaign_weight_big_regular_wight(pp_campaign_price_value['font-weight'],
                                                                   pp_regular_price_value['font-weight']), \
        f'main font-weight campaign price < font-weight regular price.\n  ' \
        f'font-weight campaign = {pp_campaign_price_value["font-weight"]}' \
        f'font-weight regular = {pp_regular_price_value["font-weight"]}'
