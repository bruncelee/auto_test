from selenium import webdriver
from selenium.webdriver.common.by import By
import json, time


class FillFormUtil:
    # 浏览器对象 webdriver.Chrome()
    # browser = webdriver.Chrome()
    browser = None
    # form表单的选择器
    form_selector = ""
    # json文件路径
    json_data = {}

    def __init__(self, browser_path, json_path, form_selector):
        self.browser = webdriver.Chrome("D:\software\chromedriver.exe")
        self.browser.get(browser_path)
        print(self.browser.page_source)
        self.json_path = json_path
        self.form_selector = form_selector
        # 获取json数据
        self.json_data = self._read_json_data(json_path)

    '''
        form表单填充数据
    '''
    def fill_form(self):
        print("查找表单%s" % self.form_selector)
        form = self.browser.find_element_by_xpath(self.form_selector)
        print("form的class属性%s" % form.get_attribute("class"))
        if form is None:
            print("查询不到form选择器%s" % self.form_selector)
            return

        # form.find_element_by_id("selectedCountry").click()
        # time.sleep(1)
        # form.find_element_by_id("allCountry").click()
        # self.browser.execute_script("document.getElementById('allCountry').style = 'display: block'")
        # form.find_element_by_id('Taiwan').click()


        inputs = form.find_elements_by_tag_name("input")
        # input元素赋值
        self._fill_input(inputs)

        # select元素赋值
        selects = form.find_elements_by_tag_name("select")
        self._fill_select(selects)
        # time.sleep(2)
        form.find_element_by_id("loginbtn").click()

    """
        跳转至iframe
    """
    def step_info_frame(self, iframe_path="iframe"):
        if iframe_path == "iframe":
            self.browser.switch_to.frame(self.browser.find_element_by_tag_name(iframe_path))
        else:
            self.browser.switch_to.frame(self.browser.find_element_by_xpath(iframe_path))

    '''
        input元素填充数据
    '''
    def _fill_input(self, inputs):
        if len(inputs) != 0:
            for input in inputs:
                try:
                    name = input.get_attribute("name")
                    type = input.get_attribute("type")
                    print("input的name=%s, type=%s" % (name, type))
                    if type == 'text' or type == 'password':
                        input.send_keys(self.json_data[name])
                    elif type == 'number':
                        input.send_keys(self.json_data[name])
                    else:
                        print("%s不知道什么类型" % name)
                except Exception as e:
                    print("input出错了", input)

        else:
            print("没有input元素")

    '''
        select元素赋值
    '''
    def _fill_select(self, selects):
        if (len(selects) > 0):
            for select in selects:
                try:
                    name = select.get_attribute("name")
                    print("select的name=%s" % name)
                except Exception as e:
                    print("select出错", input)

    '''
        读取json数据
    '''
    def _read_json_data(self, json_path):
        form_datas = {}
        try:
            with open(json_path, mode='r', encoding="UTF-8") as load_f:
                form_datas = json.load(load_f)
                print(form_datas)
        finally:
            return form_datas

    """
        显示所有不可见的div
    """
    def _show_all_element(self):
        js = """
                var divs = document.querySelectorAll("div");
                for (div of divs) {
                    if(div.style.display == 'none') {
                        div.style.display = "block";
                    }
                }
            """
        self.browser.execute_script(js)
        divs = self.browser.find_element_by_xpath(self.form_selector).find_elements_by_tag_name("div")
        for div in divs:
            if div.is_displayed():
                print("可见")
            else:
                print("不可见")


