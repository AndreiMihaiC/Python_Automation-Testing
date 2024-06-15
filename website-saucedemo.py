import time
import unittest

from assertpy import soft_assertions, assert_that
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class LoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.saucedemo.com/')
        self.driver.maximize_window()

    # Verification test if the page opens correctly:

    def test_page_opens_correctly(self):
        title = self.driver.title
        with soft_assertions():
            assert_that(title).contains("Swag Labs")
        if "Swag Labs" in title:
            print("The web page: https://www.saucedemo.com/ opened correctly.")
        else:
            print("The web page did not open.")
        print('-' * 60)

    # Valid login test:

    def test_valid_login(self):

        user = self.driver.find_element(By.ID, "user-name")
        user.send_keys("standard_user")
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        button_login = self.driver.find_element(By.ID, 'login-button')
        button_login.click()

        title = self.driver.title

        with soft_assertions():
            assert_that(title).contains("Swag Labs")

    # Invalid login test:

    def test_invalid_login(self):

        user = self.driver.find_element(By.ID, "user-name")
        user.send_keys("")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("")

        lista = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user', 'error_user',
                 'visual_user']

        if user.get_attribute("value") in lista:
            print("- The username is correct!")
            if user.get_attribute("value") == 'locked_out_user':
                print('\t- Username has been blocked.')
        elif user.get_attribute("value") != lista:
            print("- Username is incorrect!")

        if password.get_attribute("value") == "secret_sauce":
            print("- Password is correct!")
        elif password.get_attribute("value") != "secret_sauce":
            print("- The password is incorrect!")
        print('-' * 60)

    # Login test with error messages:

    def test_mesage_error_invalid_login(self):

        user = self.driver.find_element(By.ID, "user-name")
        user.send_keys("standard_user")
        user.send_keys(Keys.ENTER)

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("gresita")
        password.send_keys(Keys.ENTER)

        self.driver.find_element(By.ID, 'login-button').click()

        time.sleep(5)

        error_mesage = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]').text

        if "Epic sadface: Username is required" in error_mesage:
            print('An error message appeared for the username. Please enter a username.')
        elif "Epic sadface: Password is required" in error_mesage:
            print('An error message appeared for the password. Please enter a password.')
        elif "Epic sadface: Username and password do not match any user in this service" in error_mesage:
            print('An error message appeared for an invalid username and password.')
        else:
            print('No error message received.')

    # Logout test:

    def test_logout(self):

        user = self.driver.find_element(By.ID, "user-name")
        user.send_keys('standard_user')

        password = self.driver.find_element(By.ID, "password")
        password.send_keys('secret_sauce')

        login = self.driver.find_element(By.ID, 'login-button')
        login.click()

        burger_menu = self.driver.find_element(By.CLASS_NAME, 'bm-burger-button')
        burger_menu.click()

        logout_button = self.driver.find_element(By.ID, "logout_sidebar_link")

        if logout_button.is_displayed() and logout_button.is_enabled():
            print("- The Logout button is visible and enabled.")
        else:
            print("- The Logout button is not visible or enabled.")

        if "https://www.saucedemo.com/" in self.driver.current_url:
            print("- Logout successful.")
        elif "https://www.saucedemo.com/inventory.html" in self.driver.current_url:
            print("- Logout unsuccessful.")
        else:
            print("An error occurred.")

    # Side Menu Verification Test::

    def test_burger_menu(self):

        user = self.driver.find_element(By.ID, "user-name")
        user.send_keys('standard_user')

        password = self.driver.find_element(By.ID, "password")
        password.send_keys('secret_sauce')

        login = self.driver.find_element(By.ID, 'login-button')
        login.click()

        burger_menu_open = self.driver.find_element(By.ID, 'react-burger-menu-btn')
        burger_menu_open.click()
        menu_list = self.driver.find_element(By.CLASS_NAME, 'bm-menu')
        time.sleep(2)

        self.assertTrue(menu_list.is_displayed())

        burger_menu_close = self.driver.find_element(By.ID, 'react-burger-cross-btn')
        burger_menu_close.click()
        self.assertTrue(menu_list.is_enabled())
        time.sleep(2)


# Add Product to Cart Test:


def test_add_product_cart(self):
    user = self.driver.find_element(By.ID, "user-name")
    user.send_keys('standard_user')

    password = self.driver.find_element(By.ID, "password")
    password.send_keys('secret_sauce')

    login = self.driver.find_element(By.ID, 'login-button')
    login.click()

    add_to_cart_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
    add_to_cart_button.click()

    self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    x = self.driver.find_element(By.CLASS_NAME, 'cart_item')
    time.sleep(5)

    print('\tChecking if the product has been added to the cart:')
    if "1" in x.text:
        print("- The product has been added to the shopping cart!")
    else:
        print("- The product has not been added to the shopping cart!")


# Delete Product from Cart Test:

def test_delete_product_cart(self):
    user = self.driver.find_element(By.ID, "user-name")
    user.send_keys('standard_user')

    password = self.driver.find_element(By.ID, "password")
    password.send_keys('secret_sauce')

    login = self.driver.find_element(By.ID, 'login-button')
    login.click()

    add_to_cart_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
    add_to_cart_button.click()
    self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    time.sleep(2)

    delete_product = self.driver.find_element(By.ID, 'remove-sauce-labs-backpack')
    delete_product.click()
    time.sleep(2)

    x = self.driver.find_element(By.ID, 'cart_contents_container')

    print('\tChecking if the product has been removed from the cart:')
    if "Remove" in x.text:
        print("- The product has not been removed from the shopping cart!")
    else:
        print("- The product has been removed from the shopping cart!")


# Test to check if you can order a product:


def test_order_product(self):
    user = self.driver.find_element(By.ID, "user-name")
    user.send_keys('standard_user')

    password = self.driver.find_element(By.ID, "password")
    password.send_keys('secret_sauce')

    login = self.driver.find_element(By.ID, 'login-button')
    login.click()

    add_to_cart_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
    add_to_cart_button.click()

    self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    time.sleep(2)

    checkout = self.driver.find_element(By.ID, 'checkout').click()

    #   Fill out form:
    first_name = self.driver.find_element(By.ID, 'first-name')
    first_name.send_keys('Andrei')

    last_name = self.driver.find_element(By.ID, 'last-name')
    last_name.send_keys('Popescu')

    zip_code = self.driver.find_element(By.ID, 'postal-code')
    zip_code.send_keys('54367')

    button_continue = self.driver.find_element(By.ID, 'continue').click()

    # Check payment information:
    summary_info = self.driver.find_element(By.CLASS_NAME, 'summary_info')

    print('Verifying payment information:')
    if "Payment Information" or 'Shipping Information' or 'Price Total' in summary_info.text:
        print("The product has been added to the cart correctly, proceed to checkout!")
    else:
        print("The order could not be completed!")

    button_finish = self.driver.find_element(By.ID, 'finish').click()
    time.sleep(2)

    finish_order = self.driver.find_element(By.CLASS_NAME, 'complete-header')

    print('\tChecking if the product has been added to the cart and the order has been placed:')
    if "Thank you for your order!" in finish_order.text:
        print("- The order has been successfully placed!")
    else:
        print("- The order could not be placed.")


# Test to check if you can access a product details page:


def test_details_product(self):
    user = self.driver.find_element(By.ID, "user-name")
    user.send_keys('standard_user')

    password = self.driver.find_element(By.ID, "password")
    password.send_keys('secret_sauce')

    login = self.driver.find_element(By.ID, 'login-button')
    login.click()
    time.sleep(2)

    access_product = self.driver.find_element(By.CLASS_NAME, 'inventory_item_name ')
    access_product.click()
    time.sleep(2)

    print('\tChecking if product details page can be accessed:')
    container_product = self.driver.find_element(By.CLASS_NAME, 'inventory_details_container')

    if 'Back to products' and 'Add to cart' in container_product.text:
        print('- The product details page can be accessed.')
    else:
        print('- The product page could not be accessed.')


# Test to change the quantity of the product added to the cart:


def test_change_product_quantity(self):
    user = self.driver.find_element(By.ID, "user-name")
    user.send_keys('standard_user')

    password = self.driver.find_element(By.ID, "password")
    password.send_keys('secret_sauce')

    login = self.driver.find_element(By.ID, 'login-button')
    login.click()

    add_to_cart_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
    add_to_cart_button.click()

    self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    x = self.driver.find_element(By.CLASS_NAME, 'cart_item')

    quantity = self.driver.find_element(By.CLASS_NAME, 'cart_quantity')

    print('\tChecking if you can add more of the same product:')
    if "2" in quantity.text:
        print("- Another product of the same kind has been added!")
    else:
        print("- The desired quantity of the selected product cannot be modified.")

    # Test to check if the "Back to products" button takes you to the main page:

    def test_button_main_menu(self):
        user = self.driver.find_element(By.ID, "user-name")
        user.send_keys('standard_user')

        password = self.driver.find_element(By.ID, "password")
        password.send_keys('secret_sauce')

        login = self.driver.find_element(By.ID, 'login-button')
        login.click()
        time.sleep(2)

        access_product = self.driver.find_element(By.CLASS_NAME, 'inventory_item_name ')
        access_product.click()
        time.sleep(2)

        back_products = self.driver.find_element(By.ID, 'back-to-products')
        back_products.click()

        print("\tChecking if the 'Back to products' button takes you to the main page:")
        if self.driver.current_url == 'https://www.saucedemo.com/inventory.html':
            print('- You have returned to the main menu.')
        else:
            print('- Something went wrong. You cannot return to the main menu')

    def tearDown(self):
        self.driver.quit()


if __name__ == "main":
    unittest.main()
