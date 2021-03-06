# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAccenture():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_happypathdesafioaccenture(self):
    self.driver.get("http://sampleapp.tricentis.com/101/app.php")
    self.driver.set_window_size(1382, 744)
    self.driver.find_element(By.ID, "make").click()
    dropdown = self.driver.find_element(By.ID, "make")
    dropdown.find_element(By.XPATH, "//option[. = 'Audi']").click()
    self.driver.find_element(By.ID, "make").click()
    self.driver.find_element(By.ID, "engineperformance").click()
    self.driver.find_element(By.ID, "engineperformance").send_keys("1000")
    self.driver.find_element(By.CSS_SELECTOR, "#opendateofmanufacturecalender > .fa").click()
    self.driver.find_element(By.LINK_TEXT, "1").click()
    self.driver.find_element(By.ID, "numberofseats").click()
    dropdown = self.driver.find_element(By.ID, "numberofseats")
    dropdown.find_element(By.XPATH, "//option[. = '6']").click()
    self.driver.find_element(By.ID, "numberofseats").click()
    self.driver.find_element(By.ID, "fuel").click()
    dropdown = self.driver.find_element(By.ID, "fuel")
    dropdown.find_element(By.XPATH, "//option[. = 'Electric Power']").click()
    self.driver.find_element(By.ID, "fuel").click()
    self.driver.find_element(By.ID, "listprice").click()
    self.driver.find_element(By.ID, "listprice").click()
    self.driver.find_element(By.ID, "listprice").send_keys("10000")
    self.driver.find_element(By.ID, "licenseplatenumber").click()
    self.driver.find_element(By.ID, "licenseplatenumber").send_keys("fgtr3000")
    self.driver.find_element(By.ID, "annualmileage").click()
    self.driver.find_element(By.ID, "annualmileage").send_keys("10000")
    self.driver.find_element(By.ID, "nextenterinsurantdata").click()
    self.driver.find_element(By.ID, "firstname").click()
    self.driver.find_element(By.ID, "firstname").send_keys("ghost")
    self.driver.find_element(By.ID, "lastname").click()
    self.driver.find_element(By.ID, "lastname").send_keys("writer")
    self.driver.find_element(By.CSS_SELECTOR, "#opendateofbirthcalender > .fa").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-next").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-next").click()
    self.driver.find_element(By.LINK_TEXT, "13").click()
    self.driver.find_element(By.ID, "birthdate").click()
    self.driver.find_element(By.ID, "birthdate").send_keys("08/13/1969")
    self.driver.find_element(By.CSS_SELECTOR, ".group:nth-child(2) > .ideal-radiocheck-label:nth-child(1) > .ideal-radio").click()
    self.driver.find_element(By.ID, "streetaddress").click()
    self.driver.find_element(By.ID, "streetaddress").send_keys("rua bla bla")
    self.driver.find_element(By.ID, "country").click()
    dropdown = self.driver.find_element(By.ID, "country")
    dropdown.find_element(By.XPATH, "//option[. = 'Brazil']").click()
    self.driver.find_element(By.ID, "country").click()
    self.driver.find_element(By.ID, "zipcode").click()
    self.driver.find_element(By.ID, "zipcode").send_keys("20000")
    self.driver.find_element(By.ID, "city").click()
    self.driver.find_element(By.ID, "city").send_keys("rio de janeiro")
    self.driver.find_element(By.ID, "occupation").click()
    dropdown = self.driver.find_element(By.ID, "occupation")
    dropdown.find_element(By.XPATH, "//option[. = 'Employee']").click()
    self.driver.find_element(By.ID, "occupation").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ideal-radiocheck-label:nth-child(5) > .ideal-check").click()
    self.driver.find_element(By.ID, "nextenterproductdata").click()
    self.driver.find_element(By.CSS_SELECTOR, "#openstartdatecalender > .fa").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-next").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-next").click()
    self.driver.find_element(By.LINK_TEXT, "7").click()
    self.driver.find_element(By.ID, "insurancesum").click()
    dropdown = self.driver.find_element(By.ID, "insurancesum")
    dropdown.find_element(By.XPATH, "//option[. = '3.000.000,00']").click()
    self.driver.find_element(By.ID, "insurancesum").click()
    self.driver.find_element(By.ID, "meritrating").click()
    dropdown = self.driver.find_element(By.ID, "meritrating")
    dropdown.find_element(By.XPATH, "//option[. = 'Bonus 8']").click()
    self.driver.find_element(By.ID, "meritrating").click()
    self.driver.find_element(By.ID, "damageinsurance").click()
    dropdown = self.driver.find_element(By.ID, "damageinsurance")
    dropdown.find_element(By.XPATH, "//option[. = 'No Coverage']").click()
    self.driver.find_element(By.ID, "damageinsurance").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field:nth-child(5) .ideal-radiocheck-label:nth-child(2) > .ideal-check").click()
    self.driver.find_element(By.ID, "courtesycar").click()
    dropdown = self.driver.find_element(By.ID, "courtesycar")
    dropdown.find_element(By.XPATH, "//option[. = 'Yes']").click()
    self.driver.find_element(By.ID, "courtesycar").click()
    self.driver.find_element(By.ID, "nextselectpriceoption").click()
    self.driver.find_element(By.CSS_SELECTOR, ".choosePrice:nth-child(4) > .ideal-radio").click()
    self.driver.find_element(By.ID, "nextsendquote").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("andremaia2@yahoo.com.br")
    self.driver.find_element(By.ID, "phone").send_keys("21982537912")
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("ghostW")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("Aa008980")
    self.driver.find_element(By.ID, "confirmpassword").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("Qwerty90")
    self.driver.find_element(By.ID, "confirmpassword").click()
    self.driver.find_element(By.ID, "confirmpassword").send_keys("Qwerty90")
    self.driver.find_element(By.ID, "sendemail").click()
    self.driver.find_element(By.CSS_SELECTOR, ".confirm").click()
  
  def test_testenegativodesafioaccenture(self):
    self.driver.get("http://sampleapp.tricentis.com/101/app.php")
    self.driver.set_window_size(1382, 744)
    self.driver.find_element(By.ID, "make").click()
    dropdown = self.driver.find_element(By.ID, "make")
    dropdown.find_element(By.XPATH, "//option[. = 'Audi']").click()
    self.driver.find_element(By.ID, "make").click()
    self.driver.find_element(By.ID, "engineperformance").click()
    self.driver.find_element(By.ID, "engineperformance").send_keys("10000")
    self.driver.find_element(By.CSS_SELECTOR, "#opendateofmanufacturecalender > .fa").click()
    self.driver.find_element(By.LINK_TEXT, "1").click()
    self.driver.find_element(By.ID, "numberofseats").click()
    dropdown = self.driver.find_element(By.ID, "numberofseats")
    dropdown.find_element(By.XPATH, "//option[. = '6']").click()
    self.driver.find_element(By.ID, "numberofseats").click()
    self.driver.find_element(By.ID, "fuel").click()
    dropdown = self.driver.find_element(By.ID, "fuel")
    dropdown.find_element(By.XPATH, "//option[. = 'Electric Power']").click()
    self.driver.find_element(By.ID, "fuel").click()
    self.driver.find_element(By.ID, "listprice").click()
    self.driver.find_element(By.ID, "listprice").click()
    self.driver.find_element(By.ID, "listprice").send_keys("1000")
    self.driver.find_element(By.ID, "licenseplatenumber").click()
    self.driver.find_element(By.ID, "licenseplatenumber").send_keys("fgtr3000")
    self.driver.find_element(By.ID, "annualmileage").click()
    self.driver.find_element(By.ID, "annualmileage").send_keys("10000")
    self.driver.find_element(By.ID, "nextenterinsurantdata").click()
    self.driver.find_element(By.ID, "firstname").click()
    self.driver.find_element(By.ID, "firstname").send_keys("ghost")
    self.driver.find_element(By.ID, "lastname").click()
    self.driver.find_element(By.ID, "lastname").send_keys("writer")
    self.driver.find_element(By.CSS_SELECTOR, "#opendateofbirthcalender > .fa").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-next").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-next").click()
    self.driver.find_element(By.LINK_TEXT, "13").click()
    self.driver.find_element(By.ID, "birthdate").click()
    self.driver.find_element(By.ID, "birthdate").send_keys("08/13/1969")
    self.driver.find_element(By.CSS_SELECTOR, ".group:nth-child(2) > .ideal-radiocheck-label:nth-child(1) > .ideal-radio").click()
    self.driver.find_element(By.ID, "streetaddress").click()
    self.driver.find_element(By.ID, "streetaddress").send_keys("rua bla bla")
    self.driver.find_element(By.ID, "country").click()
    dropdown = self.driver.find_element(By.ID, "country")
    dropdown.find_element(By.XPATH, "//option[. = 'Brazil']").click()
    self.driver.find_element(By.ID, "country").click()
    self.driver.find_element(By.ID, "zipcode").click()
    self.driver.find_element(By.ID, "zipcode").send_keys("20000")
    self.driver.find_element(By.ID, "city").click()
    self.driver.find_element(By.ID, "city").send_keys("rio de janeiro")
    self.driver.find_element(By.ID, "occupation").click()
    dropdown = self.driver.find_element(By.ID, "occupation")
    dropdown.find_element(By.XPATH, "//option[. = 'Employee']").click()
    self.driver.find_element(By.ID, "occupation").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ideal-radiocheck-label:nth-child(5) > .ideal-check").click()
    self.driver.find_element(By.ID, "nextenterproductdata").click()
    self.driver.find_element(By.CSS_SELECTOR, "#openstartdatecalender > .fa").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-next").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-next").click()
    self.driver.find_element(By.LINK_TEXT, "7").click()
    self.driver.find_element(By.ID, "insurancesum").click()
    dropdown = self.driver.find_element(By.ID, "insurancesum")
    dropdown.find_element(By.XPATH, "//option[. = '3.000.000,00']").click()
    self.driver.find_element(By.ID, "insurancesum").click()
    self.driver.find_element(By.ID, "meritrating").click()
    dropdown = self.driver.find_element(By.ID, "meritrating")
    dropdown.find_element(By.XPATH, "//option[. = 'Bonus 8']").click()
    self.driver.find_element(By.ID, "meritrating").click()
    self.driver.find_element(By.ID, "damageinsurance").click()
    dropdown = self.driver.find_element(By.ID, "damageinsurance")
    dropdown.find_element(By.XPATH, "//option[. = 'No Coverage']").click()
    self.driver.find_element(By.ID, "damageinsurance").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field:nth-child(5) .ideal-radiocheck-label:nth-child(2) > .ideal-check").click()
    self.driver.find_element(By.ID, "courtesycar").click()
    dropdown = self.driver.find_element(By.ID, "courtesycar")
    dropdown.find_element(By.XPATH, "//option[. = 'Yes']").click()
    self.driver.find_element(By.ID, "courtesycar").click()
    self.driver.find_element(By.ID, "nextselectpriceoption").click()
    self.driver.find_element(By.CSS_SELECTOR, ".choosePrice:nth-child(4) > .ideal-radio").click()
    self.driver.find_element(By.ID, "nextsendquote").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("andremaia2@yahoo.com.br")
    self.driver.find_element(By.ID, "phone").send_keys("21982537912")
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("ghostW")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("Aa008980")
    self.driver.find_element(By.ID, "confirmpassword").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("Qwerty90")
    self.driver.find_element(By.ID, "confirmpassword").click()
    self.driver.find_element(By.ID, "confirmpassword").send_keys("Qwerty90")
    self.driver.find_element(By.ID, "sendemail").click()
    self.driver.find_element(By.CSS_SELECTOR, ".confirm").click()
  
