from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# 如果chromedriver.exe不在项目根目录，则需要设置驱动
browser = webdriver.Chrome("D:\software\chromedriver.exe")

browser.get("http://b-test.zj.com.yc")
# 设置登录账户
browser.find_element_by_id('loginname').send_keys('huxi_hz')
browser.find_element_by_id('password').send_keys('9')

# 点击登录
browser.find_element_by_id("loginbtn").click()

# try:
#     element = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.ID, "myDynamicElement"))
#
#     )
# finally:
#     # browser.quit()
#     print("finally结束了")
time.sleep(2)
windows = browser.window_handles
print("windows窗口数量", windows)
browser.switch_to.window(windows[0])
time.sleep(2)
print(browser.current_url)
# browser.find_element_by_xpath('//*[@id="mainlayout"]/div[3]/div/div/div[2]/div[3]/div/table[1]/tbody/tr[1]/td[3]').click()
print(browser.find_element_by_css_selector("#mainlayout > div.panel.layout-panel.layout-panel-west > div > div > div.sys-menu-text > div:nth-child(3) > div > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(3)").get_attribute("title"))
time.sleep(1)
# browser.execute_script('document.getElementsByClassName("sys-menu-item")[2].classList.add("smti-over")')
# 执行script脚本，显示隐藏的元素，否则无法click
browser.execute_script("document.getElementsByClassName('sys-menu-text')[0].style = 'display: block'")
browser.execute_script("document.getElementsByClassName('sys-menu-sub')[1].style = 'display: block'")
# td = browser.find_element_by_css_selector('#mainlayout > div.panel.layout-panel.layout-panel-west > div > div > div.sys-menu-text > div:nth-child(3) > div > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(3)')
time.sleep(1)
browser.execute_script("document.querySelector('#mainlayout > div.panel.layout-panel.layout-panel-west > div > div > div.sys-menu-text > div:nth-child(3) > div > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(3)').click()")
# td.click()
#td.send_keys(Keys.SPACE)

# 定位到iframe
time.sleep(1)
iframe_path = '//*[@id="37B9D0004E684F78892BD3B43D834ABF"]/iframe'
print(browser.find_element_by_tag_name("iframe").tag_name)
browser.switch_to.frame(browser.find_element_by_xpath(iframe_path))
print(browser.current_url)
time.sleep(1)
# print("无条件搜索%s" % browser.find_element_by_xpath('//*[@id="layui-laypage-1"]/span[4]'))
# 赋值并点击搜索
browser.find_element_by_name("managerName").send_keys("XIAO")
browser.find_element_by_id("btnSearch").click()
time.sleep(2)

js = """
        $("a.layui-btn.layui-btn-danger").each(function() {
            $(this).click();
        })
    """
# browser.execute_script(js)
trs = browser.find_elements_by_css_selector('body > form > div.layui-card > div.layui-card-body > div > div.layui-table-box > div.layui-table-body.layui-table-main > table > tbody > tr')
for tr in trs:
    # print(tr.text)
    td_a = tr.find_element_by_css_selector('td > div > a.layui-btn.layui-btn-danger.layui-btn-xs.layui-bg-red')
    print(td_a.text)
    td_a.click()
    time.sleep(2)





