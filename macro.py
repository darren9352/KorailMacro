from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.chrome.options import Options

while True:
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    url = "http://www.letskorail.com/ebizprd/prdMain.do"
    chrome_driver_path = './chromedriver.exe'
    driver = webdriver.Chrome(chrome_options=chrome_options ,executable_path=chrome_driver_path)
    #driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(url)

    driver.find_element_by_xpath("//*[@id='header']/div[1]/div/ul/li[2]/a").click();

    kid = driver.find_element_by_id("txtMember")
    kid.clear()
    kid.send_keys("KORAILID")

    kpss = driver.find_element_by_id("txtPwd")
    kpss.clear()
    kpss.send_keys("KORAILPW")

    driver.find_element_by_xpath("//*[@id='loginDisplay1']/ul/li[3]/a").click()

    go = driver.find_element_by_id("txtGoStart")
    go.clear()
    go.send_keys("부산")

    to = driver.find_element_by_id("txtGoEnd")
    to.clear()
    to.send_keys("서울")
    # window_before = driver.current_window_handle
    #
    # driver.find_element_by_xpath("//*[@id='res_cont_tab01']/form/div/fieldset/ul[2]/li[1]/a").click()
    # for handle in driver.window_handles:
    #     if handle != window_before:
    #         select_page = handle
    #
    # driver.switch_to.window(select_page)
    # # driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[3]/td[1]/a").click()
    # # driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[4]/td[4]/a").click()
    # # driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[3]/td[5]/a").click()
    # driver.switch_to.window(window_before)
    select = Select(driver.find_element_by_id('time'))

    # select by value
    select.select_by_value('18')
    driver.find_element_by_xpath("//*[@id='res_cont_tab01']/form/div/fieldset/p/a").click()

    sleep(2)
    try:
        driver.execute_script("javascript:infochk(1,0)");
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
        driver.get("http://www.naver.com")
        break;
    except Exception as e:
        driver.close()
        print(e)
    # try:
    # driver.find_element_by_xpath("//*[@id='tableResult']/tbody/tr[5]/td[6]/a[1]").click()
    # except Exception as e:
    #     driver.close()
    #     print(e)


