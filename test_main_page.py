LINK = 'http://selenium1py.pythonanywhere.com/'


def test_guest_can_go_to_login_page(browser):
    browser.get(LINK)
    login_link = browser.find_element_by_css_selector('#login_link')
    login_link.click()