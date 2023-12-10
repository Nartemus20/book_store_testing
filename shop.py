# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

"""Отображение страницы товара"""
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
#
# my_account_button = driver.find_element_by_id('menu-item-50')
# my_account_button.click()
# username_or_email_field = driver.find_element_by_name('username')
# username_or_email_field.send_keys('95747@gmail.com')
# password_field = driver.find_element_by_id('password')
# password_field.send_keys('Jojo12345Jojo')
# login_button = driver.find_element_by_name('login')
# login_button.click()
#
# shop_button = driver.find_element_by_id('menu-item-40')
# shop_button.click()
# html5_forms_book = driver.find_element_by_css_selector('[alt="Mastering HTML5 Forms"]')
# html5_forms_book.click()
#
# book_title = driver.find_element_by_css_selector('div h1')
# book_title_text = book_title.text
# if book_title_text == 'HTML5 Forms':
#     print('Заголовок книги:', book_title_text)
# else:
#     print('Неизвестный заголовок книги')
#
# driver.quit()

"""Количество товаров в категории"""
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
#
# my_account_button = driver.find_element_by_id('menu-item-50')
# my_account_button.click()
# username_or_email_field = driver.find_element_by_name('username')
# username_or_email_field.send_keys('95747@gmail.com')
# password_field = driver.find_element_by_id('password')
# password_field.send_keys('Jojo12345Jojo')
# login_button = driver.find_element_by_name('login')
# login_button.click()
#
# shop_button = driver.find_element_by_id('menu-item-40')
# shop_button.click()
# html_category = driver.find_element_by_css_selector('.cat-item-19 a')
# html_category.click()
#
# number_of_goods = driver.find_elements_by_css_selector('li a h3')
# if len(number_of_goods) == 3:
#     print('Отображается три товара')
# else:
#     print('Отображается неизвестное количество товаров')
#
# driver.quit()

"""Сортировка товаров"""
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
#
# my_account_button = driver.find_element_by_id('menu-item-50')
# my_account_button.click()
# username_or_email_field = driver.find_element_by_name('username')
# username_or_email_field.send_keys('95747@gmail.com')
# password_field = driver.find_element_by_id('password')
# password_field.send_keys('Jojo12345Jojo')
# login_button = driver.find_element_by_name('login')
# login_button.click()
#
# shop_button = driver.find_element_by_id('menu-item-40')
# shop_button.click()
#
# default_sorting = driver.find_element_by_css_selector('[value="menu_order"]')
# default_sorting_selected = default_sorting.get_attribute('selected')
# if default_sorting_selected is not None:
#     print('Выбран вариант сортировки по умолчанию')
# else:
#     print('Выбран другой вариант сортировки')
#
# selector = driver.find_element_by_class_name('orderby')
# select_sorting = Select(selector)
# select_sorting.select_by_index(5)
#
# previous_selector = driver.find_element_by_name('orderby')
# high_to_low_sorting = driver.find_element_by_css_selector('[value="price-desc"]')
# high_to_low_sorting_selected = high_to_low_sorting.get_attribute('selected')
# if high_to_low_sorting_selected is not None:
#     print('Выбран вариант сортировки по цене от большей к меньшей')
# else:
#     print('Выбран другой вариант сортировки')
#
# driver.quit()

"""Отображение, скидка товара"""
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
#
# my_account_button = driver.find_element_by_id('menu-item-50')
# my_account_button.click()
# username_or_email_field = driver.find_element_by_name('username')
# username_or_email_field.send_keys('95747@gmail.com')
# password_field = driver.find_element_by_id('password')
# password_field.send_keys('Jojo12345Jojo')
# login_button = driver.find_element_by_name('login')
# login_button.click()
#
# shop_button = driver.find_element_by_id('menu-item-40')
# shop_button.click()
# book = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]')
# book.click()
#
# old_price = driver.find_element_by_css_selector('.price del')
# old_price_text = old_price.text
# assert old_price_text == '₹600.00'
# new_price = driver.find_element_by_css_selector('.price ins')
# new_price_text = new_price.text
# assert new_price_text == '₹450.00'
#
# wait = WebDriverWait(driver, 20)
# book_cover = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'zoom')))
# book_cover.click()
# close_preview = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close')))
# close_preview.click()
#
# driver.quit()

"""Проверка цены в корзине"""
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
#
# shop_button = driver.find_element_by_id('menu-item-40')
# shop_button.click()
# add_book_to_basket = driver.find_element_by_css_selector('[data-product_id="182"]')
# add_book_to_basket.click()
# time.sleep(3)
#
# number_of_goods = driver.find_element_by_class_name('cartcontents')
# number_of_goods_text = number_of_goods.text
# price = driver.find_element_by_css_selector('.amount:nth-child(3)')
# price_text = price.text
# assert number_of_goods_text == '1 Item' and price_text == '₹180.00'
#
# basket = driver.find_element_by_class_name('wpmenucart-icon-shopping-cart-0')
# basket.click()
# wait = WebDriverWait(driver, 20)
# subtotal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-title="Subtotal"]')))
# total = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.order-total strong')))
#
# driver.quit()

"""Работа в корзине"""
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
#
# shop_button = driver.find_element_by_id('menu-item-40')
# shop_button.click()
# driver.execute_script('window.scrollBy(0, 300);')
#
# add_first_book = driver.find_element_by_css_selector('[data-product_id="182"]')
# add_first_book.click()
# time.sleep(3)
# add_second_book = driver.find_element_by_css_selector('[data-product_id="180"]')
# add_second_book.click()
# time.sleep(3)
#
# view_basket = driver.find_element_by_class_name('wc-forward')
# view_basket.click()
# time.sleep(3)
# delete_first_book = driver.find_element_by_css_selector('[data-product_id="182"]')
# delete_first_book.click()
#
# undo = driver.find_element_by_link_text('Undo?')
# undo.click()
# clear_quantity = driver.find_element_by_name('cart[045117b0e0a11a242b9765e79cbf113f][qty]')
# clear_quantity.clear()
# increase_quantity = driver.find_element_by_name('cart[045117b0e0a11a242b9765e79cbf113f][qty]')
# increase_quantity.send_keys(3)
#
# update_basket = driver.find_element_by_name('update_cart')
# update_basket.click()
# first_book_quantity = driver.find_element_by_css_selector('[value="3"]')
# first_book_quantity_value = first_book_quantity.get_attribute('value')
# assert int(first_book_quantity_value) == 3
# time.sleep(3)
# apply_coupon = driver.find_element_by_name('apply_coupon')
# apply_coupon.click()
#
# message = driver.find_element_by_css_selector('.woocommerce-error li')
# message_text = message.text
# if message_text == 'Please enter a coupon code.':
#     print('Возникло сообщение:', message_text)
# else:
#     print('Сообщение не совпадает с ожидаемым')
#
# driver.quit()

"""Покупка товара"""
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
#
# shop_button = driver.find_element_by_id('menu-item-40')
# shop_button.click()
# driver.execute_script('window.scrollBy(0, 300);')
# add_book_to_basket = driver.find_element_by_css_selector('[data-product_id="182"]')
# add_book_to_basket.click()
#
# view_basket = driver.find_element_by_class_name('wc-forward')
# view_basket.click()
# wait = WebDriverWait(driver, 20)
# proceed_to_checkout = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'checkout-button')))
# proceed_to_checkout.click()
#
# first_name = wait.until(EC.visibility_of_element_located((By.ID, 'billing_first_name')))
# first_name.send_keys('Jojo')
# last_name = driver.find_element_by_name('billing_last_name')
# last_name.send_keys('Jojovich')
# email = driver.find_element_by_id('billing_email')
# email.send_keys('95747@gmail.com')
# phone = driver.find_element_by_name('billing_phone')
# phone.send_keys('1234567890')
# country = driver.find_element_by_id('s2id_billing_country')
# country.click()
# find_country = driver.find_element_by_id('s2id_autogen1_search')
# find_country.send_keys('Cuba')
# select_country = driver.find_element_by_class_name('select2-match')
# select_country.click()
# address = driver.find_element_by_name('billing_address_1')
# address.send_keys('Some address')
# city = driver.find_element_by_name('billing_city')
# city.send_keys('Havana')
# state = driver.find_element_by_name('billing_state')
# state.send_keys('Some state')
# postcode = driver.find_element_by_name('billing_postcode')
# postcode.send_keys('12345')
#
# driver.execute_script('window.scrollBy(0, 600);')
# time.sleep(3)
# check_payments = driver.find_element_by_id('payment_method_cheque')
# check_payments.click()
# place_order = driver.find_element_by_id('place_order')
# place_order.click()
#
# check_inscription = wait.until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-thankyou-order-received'),
#                                      'Thank you. Your order has been received.')
# )
# check_payment_method = wait.until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.method strong'),
#                                      'Check Payments')
# )
#
# driver.quit()
