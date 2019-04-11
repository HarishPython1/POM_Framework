class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        #self.un_txt_xpath = "//*[@id='username']"
        self.un_txt_xpath = "//*[@id='j_username']"
        #self.pwd_txt_xpath = "//*[@name='pwd']"
        self.pwd_txt_xpath = "//*[@name='j_password']"
        #self.login_btn_xpath = "//*[text()='Login ']"
        self.login_btn_xpath = "//*[@name='Submit']"

    def enter_un(self,un):
        self.driver.find_element_by_xpath(self.un_txt_xpath).send_keys(un)

    def enter_pwd(self, pwd):
            self.driver.find_element_by_xpath(self.pwd_txt_xpath).send_keys(pwd)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_btn_xpath).click()
