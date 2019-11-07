from selenium.webdriver.common.by import By


class MainPageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():

    LOGIN_FORM = (By.ID, 'logi_form')
#    LOGIN_EMAIL_FIELD = (By.ID, 'id_login-username')
#    LOGIN_PASSWORD_FIELD = (By.ID, 'id_login-password')

    REGISTER_FORM = (By.ID, 'registe_form')
#    REGISTER_EMAIL_FIELD = (By.ID, 'id_registration-email')
#    REGISTER_PASSWORD_FIELD = (By.ID, 'id_registration-password1')
#    REGISTER_CONFIRM_PASSWORD_FIELD = (By.ID, 'id_registration-password2')


