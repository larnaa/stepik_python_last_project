from .pages.main_page import MainPage

LINK = 'http://selenium1py.pythonanywhere.com/'


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, LINK)
    page.open_page()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, LINK)
    page.open_page()
    page.should_be_login_link()
