// Generated by Selenium IDE
const { Builder, By, Key, until } = require('selenium-webdriver')
const assert = require('assert')

describe('accenture', function() {
  this.timeout(30000)
  let driver
  let vars
  beforeEach(async function() {
    driver = await new Builder().forBrowser('chrome').build()
    vars = {}
  })
  afterEach(async function() {
    await driver.quit();
  })
  it('happypathdesafioaccenture', async function() {
    await driver.get("http://sampleapp.tricentis.com/101/app.php")
    await driver.manage().window().setRect(1382, 744)
    await driver.findElement(By.id("make")).click()
    {
      const dropdown = await driver.findElement(By.id("make"))
      await dropdown.findElement(By.xpath("//option[. = 'Audi']")).click()
    }
    await driver.findElement(By.id("make")).click()
    await driver.findElement(By.id("engineperformance")).click()
    await driver.findElement(By.id("engineperformance")).sendKeys("1000")
    await driver.findElement(By.css("#opendateofmanufacturecalender > .fa")).click()
    await driver.findElement(By.linkText("1")).click()
    await driver.findElement(By.id("numberofseats")).click()
    {
      const dropdown = await driver.findElement(By.id("numberofseats"))
      await dropdown.findElement(By.xpath("//option[. = '6']")).click()
    }
    await driver.findElement(By.id("numberofseats")).click()
    await driver.findElement(By.id("fuel")).click()
    {
      const dropdown = await driver.findElement(By.id("fuel"))
      await dropdown.findElement(By.xpath("//option[. = 'Electric Power']")).click()
    }
    await driver.findElement(By.id("fuel")).click()
    await driver.findElement(By.id("listprice")).click()
    await driver.findElement(By.id("listprice")).click()
    await driver.findElement(By.id("listprice")).sendKeys("10000")
    await driver.findElement(By.id("licenseplatenumber")).click()
    await driver.findElement(By.id("licenseplatenumber")).sendKeys("fgtr3000")
    await driver.findElement(By.id("annualmileage")).click()
    await driver.findElement(By.id("annualmileage")).sendKeys("10000")
    await driver.findElement(By.id("nextenterinsurantdata")).click()
    await driver.findElement(By.id("firstname")).click()
    await driver.findElement(By.id("firstname")).sendKeys("ghost")
    await driver.findElement(By.id("lastname")).click()
    await driver.findElement(By.id("lastname")).sendKeys("writer")
    await driver.findElement(By.css("#opendateofbirthcalender > .fa")).click()
    await driver.findElement(By.css(".ui-datepicker-next")).click()
    await driver.findElement(By.css(".ui-datepicker-next")).click()
    await driver.findElement(By.linkText("13")).click()
    await driver.findElement(By.id("birthdate")).click()
    await driver.findElement(By.id("birthdate")).sendKeys("08/13/1969")
    await driver.findElement(By.css(".group:nth-child(2) > .ideal-radiocheck-label:nth-child(1) > .ideal-radio")).click()
    await driver.findElement(By.id("streetaddress")).click()
    await driver.findElement(By.id("streetaddress")).sendKeys("rua bla bla")
    await driver.findElement(By.id("country")).click()
    {
      const dropdown = await driver.findElement(By.id("country"))
      await dropdown.findElement(By.xpath("//option[. = 'Brazil']")).click()
    }
    await driver.findElement(By.id("country")).click()
    await driver.findElement(By.id("zipcode")).click()
    await driver.findElement(By.id("zipcode")).sendKeys("20000")
    await driver.findElement(By.id("city")).click()
    await driver.findElement(By.id("city")).sendKeys("rio de janeiro")
    await driver.findElement(By.id("occupation")).click()
    {
      const dropdown = await driver.findElement(By.id("occupation"))
      await dropdown.findElement(By.xpath("//option[. = 'Employee']")).click()
    }
    await driver.findElement(By.id("occupation")).click()
    await driver.findElement(By.css(".ideal-radiocheck-label:nth-child(5) > .ideal-check")).click()
    await driver.findElement(By.id("nextenterproductdata")).click()
    await driver.findElement(By.css("#openstartdatecalender > .fa")).click()
    await driver.findElement(By.css(".ui-datepicker-next")).click()
    await driver.findElement(By.css(".ui-datepicker-next")).click()
    await driver.findElement(By.linkText("7")).click()
    await driver.findElement(By.id("insurancesum")).click()
    {
      const dropdown = await driver.findElement(By.id("insurancesum"))
      await dropdown.findElement(By.xpath("//option[. = '3.000.000,00']")).click()
    }
    await driver.findElement(By.id("insurancesum")).click()
    await driver.findElement(By.id("meritrating")).click()
    {
      const dropdown = await driver.findElement(By.id("meritrating"))
      await dropdown.findElement(By.xpath("//option[. = 'Bonus 8']")).click()
    }
    await driver.findElement(By.id("meritrating")).click()
    await driver.findElement(By.id("damageinsurance")).click()
    {
      const dropdown = await driver.findElement(By.id("damageinsurance"))
      await dropdown.findElement(By.xpath("//option[. = 'No Coverage']")).click()
    }
    await driver.findElement(By.id("damageinsurance")).click()
    await driver.findElement(By.css(".field:nth-child(5) .ideal-radiocheck-label:nth-child(2) > .ideal-check")).click()
    await driver.findElement(By.id("courtesycar")).click()
    {
      const dropdown = await driver.findElement(By.id("courtesycar"))
      await dropdown.findElement(By.xpath("//option[. = 'Yes']")).click()
    }
    await driver.findElement(By.id("courtesycar")).click()
    await driver.findElement(By.id("nextselectpriceoption")).click()
    await driver.findElement(By.css(".choosePrice:nth-child(4) > .ideal-radio")).click()
    await driver.findElement(By.id("nextsendquote")).click()
    await driver.findElement(By.id("email")).click()
    await driver.findElement(By.id("email")).sendKeys("andremaia2@yahoo.com.br")
    await driver.findElement(By.id("phone")).sendKeys("21982537912")
    await driver.findElement(By.id("username")).click()
    await driver.findElement(By.id("username")).click()
    await driver.findElement(By.id("username")).sendKeys("ghostW")
    await driver.findElement(By.id("password")).click()
    await driver.findElement(By.id("password")).sendKeys("Aa008980")
    await driver.findElement(By.id("confirmpassword")).click()
    await driver.findElement(By.id("password")).click()
    await driver.findElement(By.id("password")).sendKeys("Qwerty90")
    await driver.findElement(By.id("confirmpassword")).click()
    await driver.findElement(By.id("confirmpassword")).sendKeys("Qwerty90")
    await driver.findElement(By.id("sendemail")).click()
    await driver.findElement(By.css(".confirm")).click()
  })
  it('testenegativodesafioaccenture', async function() {
    await driver.get("http://sampleapp.tricentis.com/101/app.php")
    await driver.manage().window().setRect(1382, 744)
    await driver.findElement(By.id("make")).click()
    {
      const dropdown = await driver.findElement(By.id("make"))
      await dropdown.findElement(By.xpath("//option[. = 'Audi']")).click()
    }
    await driver.findElement(By.id("make")).click()
    await driver.findElement(By.id("engineperformance")).click()
    await driver.findElement(By.id("engineperformance")).sendKeys("10000")
    await driver.findElement(By.css("#opendateofmanufacturecalender > .fa")).click()
    await driver.findElement(By.linkText("1")).click()
    await driver.findElement(By.id("numberofseats")).click()
    {
      const dropdown = await driver.findElement(By.id("numberofseats"))
      await dropdown.findElement(By.xpath("//option[. = '6']")).click()
    }
    await driver.findElement(By.id("numberofseats")).click()
    await driver.findElement(By.id("fuel")).click()
    {
      const dropdown = await driver.findElement(By.id("fuel"))
      await dropdown.findElement(By.xpath("//option[. = 'Electric Power']")).click()
    }
    await driver.findElement(By.id("fuel")).click()
    await driver.findElement(By.id("listprice")).click()
    await driver.findElement(By.id("listprice")).click()
    await driver.findElement(By.id("listprice")).sendKeys("1000")
    await driver.findElement(By.id("licenseplatenumber")).click()
    await driver.findElement(By.id("licenseplatenumber")).sendKeys("fgtr3000")
    await driver.findElement(By.id("annualmileage")).click()
    await driver.findElement(By.id("annualmileage")).sendKeys("10000")
    await driver.findElement(By.id("nextenterinsurantdata")).click()
    await driver.findElement(By.id("firstname")).click()
    await driver.findElement(By.id("firstname")).sendKeys("ghost")
    await driver.findElement(By.id("lastname")).click()
    await driver.findElement(By.id("lastname")).sendKeys("writer")
    await driver.findElement(By.css("#opendateofbirthcalender > .fa")).click()
    await driver.findElement(By.css(".ui-datepicker-next")).click()
    await driver.findElement(By.css(".ui-datepicker-next")).click()
    await driver.findElement(By.linkText("13")).click()
    await driver.findElement(By.id("birthdate")).click()
    await driver.findElement(By.id("birthdate")).sendKeys("08/13/1969")
    await driver.findElement(By.css(".group:nth-child(2) > .ideal-radiocheck-label:nth-child(1) > .ideal-radio")).click()
    await driver.findElement(By.id("streetaddress")).click()
    await driver.findElement(By.id("streetaddress")).sendKeys("rua bla bla")
    await driver.findElement(By.id("country")).click()
    {
      const dropdown = await driver.findElement(By.id("country"))
      await dropdown.findElement(By.xpath("//option[. = 'Brazil']")).click()
    }
    await driver.findElement(By.id("country")).click()
    await driver.findElement(By.id("zipcode")).click()
    await driver.findElement(By.id("zipcode")).sendKeys("20000")
    await driver.findElement(By.id("city")).click()
    await driver.findElement(By.id("city")).sendKeys("rio de janeiro")
    await driver.findElement(By.id("occupation")).click()
    {
      const dropdown = await driver.findElement(By.id("occupation"))
      await dropdown.findElement(By.xpath("//option[. = 'Employee']")).click()
    }
    await driver.findElement(By.id("occupation")).click()
    await driver.findElement(By.css(".ideal-radiocheck-label:nth-child(5) > .ideal-check")).click()
    await driver.findElement(By.id("nextenterproductdata")).click()
    await driver.findElement(By.css("#openstartdatecalender > .fa")).click()
    await driver.findElement(By.css(".ui-datepicker-next")).click()
    await driver.findElement(By.css(".ui-datepicker-next")).click()
    await driver.findElement(By.linkText("7")).click()
    await driver.findElement(By.id("insurancesum")).click()
    {
      const dropdown = await driver.findElement(By.id("insurancesum"))
      await dropdown.findElement(By.xpath("//option[. = '3.000.000,00']")).click()
    }
    await driver.findElement(By.id("insurancesum")).click()
    await driver.findElement(By.id("meritrating")).click()
    {
      const dropdown = await driver.findElement(By.id("meritrating"))
      await dropdown.findElement(By.xpath("//option[. = 'Bonus 8']")).click()
    }
    await driver.findElement(By.id("meritrating")).click()
    await driver.findElement(By.id("damageinsurance")).click()
    {
      const dropdown = await driver.findElement(By.id("damageinsurance"))
      await dropdown.findElement(By.xpath("//option[. = 'No Coverage']")).click()
    }
    await driver.findElement(By.id("damageinsurance")).click()
    await driver.findElement(By.css(".field:nth-child(5) .ideal-radiocheck-label:nth-child(2) > .ideal-check")).click()
    await driver.findElement(By.id("courtesycar")).click()
    {
      const dropdown = await driver.findElement(By.id("courtesycar"))
      await dropdown.findElement(By.xpath("//option[. = 'Yes']")).click()
    }
    await driver.findElement(By.id("courtesycar")).click()
    await driver.findElement(By.id("nextselectpriceoption")).click()
    await driver.findElement(By.css(".choosePrice:nth-child(4) > .ideal-radio")).click()
    await driver.findElement(By.id("nextsendquote")).click()
    await driver.findElement(By.id("email")).click()
    await driver.findElement(By.id("email")).sendKeys("andremaia2@yahoo.com.br")
    await driver.findElement(By.id("phone")).sendKeys("21982537912")
    await driver.findElement(By.id("username")).click()
    await driver.findElement(By.id("username")).click()
    await driver.findElement(By.id("username")).sendKeys("ghostW")
    await driver.findElement(By.id("password")).click()
    await driver.findElement(By.id("password")).sendKeys("Aa008980")
    await driver.findElement(By.id("confirmpassword")).click()
    await driver.findElement(By.id("password")).click()
    await driver.findElement(By.id("password")).sendKeys("Qwerty90")
    await driver.findElement(By.id("confirmpassword")).click()
    await driver.findElement(By.id("confirmpassword")).sendKeys("Qwerty90")
    await driver.findElement(By.id("sendemail")).click()
    await driver.findElement(By.css(".confirm")).click()
  })
})
