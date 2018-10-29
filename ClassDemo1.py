from selenium import webdriver
import time
from src.SeleniumDemo.FillFormUtil import FillFormUtil
"""
    自动注册360图书馆
"""
class BaiduInfo:

    def locate(self):
        fillForm = FillFormUtil("http://www.360doc.com/register.aspx", "form.json", '//*[@id="mainbox"]/div[1]/div[1]')
        fillForm.fill_form()

        time.sleep(100)



if __name__ == "__main__":
    bd = BaiduInfo()
    bd.locate()
