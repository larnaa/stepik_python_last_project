class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url: str = url

    def open_page(self):
        self.browser.get(self.url)
