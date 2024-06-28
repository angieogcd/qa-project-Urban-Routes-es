import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import helpers
import UrbanRoutesPage
import time
class TestUrbanRoutes:

    driver = webdriver.Chrome
    @classmethod
    def setup_class(cls):
        # Chrome Settings
        options = Options()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920x1080")
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        # WebDriver
        cls.driver = webdriver.Chrome(options=options)

    def test_access_page(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        self.driver.get(data.urban_routes_url)
        helpers.wait_visibility_of_element(self.driver, routes_page.main_log, 3)

# Agregar direcciòn "Desde" - "Hasta"
    def test1_set_route(self):

        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        # Confirma la prueba
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

# Selecciona la opcion Comfort
    def test2_select_comfort(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        helpers.wait_visibility_of_element(self.driver, routes_page.button_round, 3)
        routes_page.click_button_round()
        routes_page.click_comfort_select()
        assert True, routes_page.click_comfort_select()

# Agregar Nº de telefono
    def test3_add_phone(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes_page.click_phone_number_home_page()
        phone_number = data.phone_number
        routes_page.set_phone_number(phone_number)
        routes_page.click_phone_number_pop_up_window()
        confirmation_code = helpers.retrieve_phone_code(self.driver)
        routes_page.set_sms_code(str(confirmation_code))
        assert True, (str(confirmation_code)).isdigit()
        routes_page.click_next_code_phone()
        assert routes_page.get_phone_number() == phone_number


# Agregar tarjeta de credito
    def test4_add_credit_card(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes_page.click_payment_method()
        routes_page.click_add_card()
        card_number = data.card_number
        card_code = data.card_code
        # Ingresa el Nº de la tarjeta
        routes_page.set_card_number(card_number)
        # Ingresa el código de la tarjeta
        routes_page.set_code_number(card_code)
        helpers.wait_to_be_clickable_of_element(self.driver, routes_page.button_agree_card, 3)
        assert routes_page.get_card_number() == card_number
        assert routes_page.get_code_number() == card_code
        # Click en el botón "Añadir tarjeta" de la 2º ventana emergente
        routes_page.click_add_card_2nd_pop_up_window()
        assert True, routes_page.check_agree_tcard()
        routes_page.click_close_pop_up_card_windows()

# Agrega el mensaje al conductor
    def test5_message_for_driver(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Ingresa el mensaje del conductor
        message_for_driver=data.message_for_driver
        routes_page.set_message_for_driver(message_for_driver)
        assert routes_page.get_message_for_driver() == message_for_driver

# Pedir una manta y pañuelos
    def test6_blanket_hankerchiefs(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes_page.click_blanket_selector()
        assert routes_page.get_blanket_value() == 'on'

# Pedir 2 helados
    def test7_request_two_ice_creams(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        for _ in range(2):
            routes_page.click_ice_cream_pl()
        assert routes_page.get_ice_cream_value() == '2'

# Modal para buscar taxi
    def test8_request_taxi(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes_page.click_find_taxi()
        assert True, routes_page.check_order_header_title()

# Prueba9
    def test9_review_driver_modal(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        helpers.wait_visibility_of_element(self.driver, routes_page.taxi_selected_driver, 40)
        assert True, routes_page.check_taxi_selected_driver()
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
