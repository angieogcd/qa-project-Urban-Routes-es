from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    main_log = (By.CLASS_NAME, 'logo-image')
    button_round = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    select_comfort = (By.CSS_SELECTOR,
                      '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.tariff-cards > div:nth-child(5)')
    button_phone_number = (By.CLASS_NAME, 'np-text')
    input_phone_number = (By.ID, 'phone')
    button_phone_pop_up_window = (By.CSS_SELECTOR,
                                  '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button')
    button_phone_code = (By.CSS_SELECTOR,
                         '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button:nth-child(1)')
    sms_code_field = (By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/form/div[1]/div/input')
    button_payment_method = (By.CSS_SELECTOR,
                             '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.pp-button.filled')
    button_add_card = (By.CSS_SELECTOR,
                       '#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div.pp-row.disabled')
    card_number_field = (By.CLASS_NAME, 'card-input')
    card_code_field = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input')
    button_agree_card = (By.CSS_SELECTOR,
                         '#root > div > div.payment-picker.open > div.modal.unusual > div.section.active.unusual > form > div.pp-buttons > button:nth-child(1)')
    check_agree_card = (By.CSS_SELECTOR,
                        '#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div:nth-child(3)')
    message_driver_field = (By.ID, 'comment')
    blanket_selector = (By.CSS_SELECTOR,
                        '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > span')
    blanket_value = (By.CSS_SELECTOR,
                     '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > input')
    blanket_label = (By.CSS_SELECTOR,
                     '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div')
    ice_cream_pl = (By.CSS_SELECTOR,
                    '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus')
    button_find_taxi = (By.CSS_SELECTOR, '#root > div > div.workflow > div.smart-button-wrapper > button')
    taxi_selected_driver = (By.XPATH, '/html/body/div/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[1]/img')
    ice_cream_count = (By.CSS_SELECTOR,
                       '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-value')
    order_header_title = (By.CLASS_NAME, 'order-header-title')
    close_pop_up_card_windows = (
    By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > button')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    # Click sobre el botón "Pedir un taxi" en el homepage
    def click_button_round(self):
        self.driver.find_element(*self.button_round).click()

    # Click en el botón "Comfort" del homepage
    def click_comfort_select(self):
        self.driver.find_element(*self.select_comfort).click()

    #Verifica que el botón "Comfort" fue seleccionado
    def click_check_comfort_select(self):
        elemento = self.driver.find_element(*self.blanket_label)
        comfort_is_check = elemento.is_displayed()
        return comfort_is_check

    # Click en el botón del homepage para ingresar el número de teléfono
    def click_phone_number_home_page(self):
        self.driver.find_element(*self.button_phone_number).click()

    # Encuentra y envía los datos en el campo número de teléfono
    def set_phone_number(self, number_phone):
        self.driver.find_element(*self.input_phone_number).send_keys(number_phone)

    def get_phone_number(self):
        return self.driver.find_element(*self.button_phone_number).get_property('outerText')

    # Click en el botón para agregar el número de teléfono desde la ventana emergente
    def click_phone_number_pop_up_window(self):
        self.driver.find_element(*self.button_phone_pop_up_window).click()

    # Encuentra y envía los datos del código sms en el campo correspondiente
    def set_sms_code(self, code_sms):
        self.driver.find_element(*self.sms_code_field).send_keys(code_sms)

    def click_next_code_phone(self):
        self.driver.find_element(*self.button_phone_code).click()

    # Comprueba que el botón "Comfort" ha sido seleccionado
    def check_send_phone_code(self):
        elemento = self.driver.find_element(*self.button_phone_pop_up_window)
        send_phone_code_is_check = elemento.is_displayed()
        return send_phone_code_is_check

    # Hace click en el botón "Método de pago" del homepage
    def click_payment_method(self):
        self.driver.find_element(*self.button_payment_method).click()

    # Hace click en el botón "Añadir una tarjeta"
    def click_add_card(self):
        self.driver.find_element(*self.button_add_card).click()

    # Encuentra y envía los datos en el campo del número de tarjeta
    def set_card_number(self, number_card):
        self.driver.find_element(*self.card_number_field).send_keys(number_card)

    # Encuentra el campo del código de la tarjeta y envía el código
    def set_code_number(self, code_card):
        code_field = self.driver.find_element(*self.card_code_field)
        code_field.send_keys(code_card)
        # Simula presionar la tecla TAB para hacer cambio de enfoque
        code_field.send_keys(Keys.TAB)

    def get_card_number(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')

    def get_code_number(self):
        return self.driver.find_element(*self.card_code_field).get_property('value')

    # Hace click en el botón "Añadir una tarjeta" en la segunda ventana emergente
    def click_add_card_2nd_pop_up_window(self):
        self.driver.find_element(*self.button_agree_card).click()

    # Comprueba que el boton "Comfort" ha sido seleccionado
    def check_agree_tcard(self):
        elemento = self.driver.find_element(*self.check_agree_card)
        agree_tcard = elemento.is_displayed()
        return agree_tcard

    # Hace click para cerrar la ventana emergente del número de teléfono
    def click_close_pop_up_card_windows(self):
        self.driver.find_element(*self.close_pop_up_card_windows).click()

    # Encuentra y envía los datos en el campo de mensaje para el conductor
    def set_message_for_driver(self, driver_message):
        self.driver.find_element(*self.message_driver_field).send_keys(driver_message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.message_driver_field).get_property('value')

    # Hace click para seleccionar manta y pañuelos
    def click_blanket_selector(self):
        self.driver.find_element(*self.blanket_selector).click()

    def get_blanket_value(self):
        return self.driver.find_element(*self.blanket_value).get_property('value')

    # Hace click para agregar helados
    def click_ice_cream_pl(self):
        self.driver.find_element(*self.ice_cream_pl).click()

    def get_ice_cream_value(self):
        return self.driver.find_element(*self.ice_cream_count).get_property('outerText')

    # Hace click para pedir un taxi
    def click_find_taxi(self):
        self.driver.find_element(*self.button_find_taxi).click()

    # Comprueba que el botón "Buscar taxi" aparezca
    def check_button_find_taxi(self):
        elemento = self.driver.find_element(*self.button_find_taxi)
        botton_find_taxi = elemento.is_displayed()
        return botton_find_taxi

    # Comprueba que el botón "Comfort" ha sido seleccionado
    def check_taxi_selected_driver(self):
        elemento = self.driver.find_element(*self.taxi_selected_driver)
        taxi_driver_selected = elemento.is_displayed()
        return taxi_driver_selected

    # Comprueba que el botón "Comfort" ha sido seleccionado
    def check_order_header_title(self):
        elemento = self.driver.find_element(*self.order_header_title)
        order_header_title_show = elemento.is_displayed()
        return order_header_title_show

