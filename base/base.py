import os
import time

# from functools import wraps

# import logging

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait


class Base():
    """
    这个类最好只允许实例化一次
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        """
        定位元素,定位正确后返回元素的信息,外部调用传入元组参数必须有*,
        例如:
        find_element(*self.native_caixun)
        :param loc: 元组类型,结构必须是(By.NAME, u'财讯')
        :return: element
        """
        try:
            element = WebDriverWait(self.driver, 30).until(lambda x: x.find_element(*loc))
            return element
        except:
            print('Error details')

            # NoSuchElementException, e:
            # print
            # 'Error details :%s' % (e.args[0])

    def find_elements(self, *loc):
        """
        定位元素,定位正确后返回元素的信息,外部调用传入元组参数必须有*,
        例如:
        find_elements(*self.native_caixun)
        :param loc: 元组类型,结构必须是(By.NAME, u'财讯')
        :return: elements
        """
        try:
            # return self.driver.find_elements(*loc)
            elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*loc))
            return elements
        except:
            print('Error details')
        # except NoSuchElementException, e:
        #     print
        #     'Error details :%s' % (e.args[0])

    def find_ID(self, ID):
        # time.sleep(2)
        # return self.driver.find_element_by_id(ID)
        try:
            time.sleep(2)
            return self.driver.find_element_by_id(ID)
        except:
            self.get_screenshot('find_id_error.png')
        # driver = self.driver
        # return WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(ID))

    def find_XPATH(self, XPATH):
        # time.sleep(2)
        # return self.driver.find_element_by_xpath(XPATH)
        try:
            time.sleep(2)
            return self.driver.find_element_by_xpath(XPATH)
        except:
            self.get_screenshot('find_xpath_error.png')
        # return WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(XPATH))

    def find_CLASSNAME(self, CLASSNAME):
        # time.sleep(2)
        # return self.driver.find_element_by_class_name(CLASSNAME)

        try:
            time.sleep(2)
            return self.driver.find_element_by_class_name(CLASSNAME)
        except:
            self.get_screenshot('find_classname_error.png')
        # return WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(CLASSNAME))

    # 点击坐标按钮
    def tap(self, x1, y1):
        # 获取绝对坐标
        # 获取当前分辨率
        el_x = self.driver.get_window_size()['width']
        el_y = self.driver.get_window_size()['height']

        # 绝对坐标转换为相对坐标，假设当前分辨率为720x1424，绝对坐标为(120, 200)
        xd_x1 = (x1 / 720) * el_x
        xd_y1 = (y1 / 1424) * el_y
        # self.driver.tap([(425, 1160),(495, 1232)],100)
        # self.driver.tap([(xd_x1, xd_y1), (xd_x2, xd_y2)], 100)
        # TouchAction(self.driver).tap(x=350, y=700).perform()
        TouchAction(self.driver).tap(x=xd_x1, y=xd_y1).perform()

    # 长按操作
    def long_press(self, x, y):
        TouchAction(self.driver).long_press(x = x, y = y).perform()

    # 获取手机截图
    def get_screenshot(self, filename):
        img_folder = os.path.dirname(__file__)
        now = time.strftime("%Y-%m-%d-%H-%M-%S")
        files = img_folder + '\\' + 'error' + '\\' + now + filename
        self.driver.get_screenshot_as_file(files)

