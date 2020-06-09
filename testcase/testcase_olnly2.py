import os
import time

from appium import webdriver

from base.base import Base
from page import main_page
from page.photo import PhotoEx
from page.mainpage_setting import Main_Setting
from page.setting_page import Setting
import pytest

# import logging
# import logging.config




"""
相机中必须至少要有一张相片
5944
"""


class Test_func():
    state = 'T'
    parametrize_info = [
        'face_recognition_off', 'face_recognition_on',
        'grid_lines_on', 'grid_lines_off',
        'time_delay_off', 'time_delay_on',
        'shutter_sound_off', 'shutter_sound_on',
        'avodi_flashing_auto', 'avodi_flashing_off', 'avodi_flashing_60hz', 'avodi_flashing_50hz',
        'Focus_sound_off', 'Focus_sound_on',
        'logo_on', 'logo_off',
        'position_logo_on', 'position_logo_off',
        'time_logo_on', 'time_logo_off',
        'photo_size_16m_4_3', 'photo_size_16m_18_9', 'photo_size_8m_18_9', 'photo_size_8m_4_3',
        'loc_info_on', 'loc_info_off'
    ]
    front_parametrize_info = [
        'face_recognition_off', 'face_recognition_on',
        'face_attribute_on', 'face_attribute_off',
        'grid_lines_on', 'grid_lines_off',
        'time_delay_off', 'time_delay_on',
        'shutter_sound_off', 'shutter_sound_on',
        'avodi_flashing_auto', 'avodi_flashing_off', 'avodi_flashing_60hz', 'avodi_flashing_50hz',
        'logo_on', 'logo_off',
        'position_logo_on', 'position_logo_off',
        'time_logo_on', 'time_logo_off',
        'photo_size_8m_18_9',  'photo_size_2m_16_9', 'photo_size_2m_4_3','photo_size_8m_4_3',
        'loc_info_on', 'loc_info_off'
    ]
    video_parametrize_info = [
        'grid_lines_on', 'grid_lines_off',
        'avodi_flashing_auto', 'avodi_flashing_off', 'avodi_flashing_60hz', 'avodi_flashing_50hz',
        'Focus_sound_off', 'Focus_sound_on',
        'stabilization_on', 'stabilization_off',
        'FHD', 'VGA', 'HD',
        'loc_info_on', 'loc_info_off'
    ]
    front_video_parametrize_info = [
        'grid_lines_on', 'grid_lines_off',
        'avodi_flashing_auto', 'avodi_flashing_off', 'avodi_flashing_60hz', 'avodi_flashing_50hz',
        'FHD', 'VGA', 'HD',
        'loc_info_on', 'loc_info_off'
    ]

    depth_parametrize_info = [
        'face_recognition_off', 'face_recognition_on',
        'grid_lines_on', 'grid_lines_off',
        'time_delay_off', 'time_delay_on',
        'shutter_sound_off', 'shutter_sound_on',
        'avodi_flashing_auto', 'avodi_flashing_off', 'avodi_flashing_60hz', 'avodi_flashing_50hz',
        'Focus_sound_off', 'Focus_sound_on',
        'loc_info_on', 'loc_info_off'
    ]

    portrait_parametrize_info = [
        'face_recognition_off', 'face_recognition_on',
        'grid_lines_on', 'grid_lines_off',
        'time_delay_off', 'time_delay_on',
        'shutter_sound_off', 'shutter_sound_on',
        'avodi_flashing_auto', 'avodi_flashing_off', 'avodi_flashing_60hz', 'avodi_flashing_50hz',
        'Focus_sound_off', 'Focus_sound_on',
        'logo_on', 'logo_off',
        'position_logo_on', 'position_logo_off',
        'time_logo_on', 'time_logo_off',
        'loc_info_on', 'loc_info_off'
    ]
    front_portrait_parametrize_info = [
        'face_recognition_off', 'face_recognition_on',
        'grid_lines_on', 'grid_lines_off',
        'time_delay_off', 'time_delay_on',
        'shutter_sound_off', 'shutter_sound_on',
        'avodi_flashing_auto', 'avodi_flashing_off', 'avodi_flashing_60hz', 'avodi_flashing_50hz',
        'logo_on', 'logo_off',
        'position_logo_on', 'position_logo_off',
        'time_logo_on', 'time_logo_off',
        'loc_info_on', 'loc_info_off'
    ]
    front_kid_parametrize_info = [
        'face_recognition_off', 'face_recognition_on',
        'grid_lines_on', 'grid_lines_off',
        'time_delay_off', 'time_delay_on',
        'shutter_sound_off', 'shutter_sound_on',
        'avodi_flashing_auto', 'avodi_flashing_off', 'avodi_flashing_60hz', 'avodi_flashing_50hz',
        'logo_on', 'logo_off',
        'position_logo_on', 'position_logo_off',
        'time_logo_on', 'time_logo_off',
        'photo_size_8m_18_9', 'photo_size_2m_16_9', 'photo_size_2m_4_3', 'photo_size_8m_4_3',
        'loc_info_on', 'loc_info_off'
    ]

    watermark_parametrize_info = [
        'face_recognition_off', 'face_recognition_on',
        'grid_lines_on', 'grid_lines_off',
        'time_delay_off', 'time_delay_on',
        'shutter_sound_off', 'shutter_sound_on',
        'avodi_flashing_auto', 'avodi_flashing_off', 'avodi_flashing_60hz', 'avodi_flashing_50hz',
        'Focus_sound_off', 'Focus_sound_on',
        'logo_on', 'logo_off',
        'position_logo_on', 'position_logo_off',
        'loc_info_on', 'loc_info_off'
    ]
    front_watermark_parametrize_info = [
        'face_recognition_off', 'face_recognition_on',
        'grid_lines_on', 'grid_lines_off',
        'time_delay_off', 'time_delay_on',
        'shutter_sound_off', 'shutter_sound_on',
        'avodi_flashing_auto', 'avodi_flashing_off', 'avodi_flashing_60hz', 'avodi_flashing_50hz',
        'logo_on', 'logo_off',
        'position_logo_on', 'position_logo_off',
        'loc_info_on', 'loc_info_off'
    ]

    def setup(self):
        # server 启动参数
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.1'

        desired_caps['deviceName'] = 'MNPBYLSKGICQCIGA'
        # desired_caps['deviceName'] = 'EQBMZ5INHMCYCA55'
        # app信息
        desired_caps['appPackage'] = 'com.freeme.camera'
        desired_caps['appActivity'] = '.CameraLauncher t84'
        desired_caps['automationName'] = 'UIAutomator2'
        # desired_caps['automationName'] = 'Uiautomator1'
        # desired_caps['newCommandTimeout'] = '2000'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['noSign'] = True
        desired_caps['systemPort'] = '8200'
        desired_caps['noReset'] = 'False'

        # 解决中文输入问题
        # desired_caps['unicodeKeyboard'] = True
        # desired_caps['resetKeyboard'] = True

        try:
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            print('driver初始化')
        except:
            os.system('adb kill-server')
            time.sleep(3)
            os.system('adb start-server')
            time.sleep(3)
            try:
                self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
                print('driver初始化')
            except:
                os.system('adb kill-server')
                time.sleep(3)
                os.system('adb start-server')
                time.sleep(3)
                self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
                print('driver初始化')
        self.driver.implicitly_wait(20)

        # 弹框处理 权限同意
        self.driver.switch_to.alert.accept()

        # 实例化基类
        self.base_obj = Base(self.driver)

        # 实例化照片类
        self.photo = PhotoEx(self.base_obj)

        # 实例化设置
        self.main_setting = Main_Setting(self.base_obj)
        # 实例化设置界面
        self.setting = Setting(self.base_obj)

        # 获取原有照片数量
        self.photo.get_old_photo_sum()
        # 打开触屏拍照
        self.setting.touch_screen_switch()

    def teardown(self):
        # 删除遗留照片
        # photo_sum = self.photo.get_photo_sum()
        # if int(photo_sum) > 500:
        #     self.photo.delete_photo()
        #     time.sleep(20)
        print('driver退出')
        self.driver.quit()
        time.sleep(10)
        print('driver退出')
        print('')

    # 相机首页拍照 468
    @pytest.mark.parametrize("parametrize_info", parametrize_info)
    def test_1_click_photo(self, parametrize_info):
        global state
        try:
            # 开关
            if parametrize_info == 'face_recognition_off':
                self.setting.ace_recognition()
                print('关闭人脸识别')
            elif parametrize_info == 'face_recognition_on':
                # print(state)
                # if state == 'F':
                #     self.setting.ace_recognition()
                print('开启人脸识别')
            elif parametrize_info == 'grid_lines_on':
                self.setting.Grid_lines()
                print('开启网格线')
            elif parametrize_info == 'grid_lines_off':
                # if state == 'T':
                #     self.setting.Grid_lines()
                print('关闭网格线')
            elif parametrize_info == 'time_delay_off':
                self.setting.time_delay()
                print('关闭零延时')
            elif parametrize_info == 'time_delay_on':
                # self.setting.time_delay()
                print('开启零延时')
            elif parametrize_info == 'shutter_sound_off':
                self.setting.shutter_sound()
                print('关闭快门声音')
            elif parametrize_info == 'shutter_sound_on':
                # if state == 'T':
                #     self.setting.shutter_sound()
                print('开启快门声音')
            elif parametrize_info == 'avodi_flashing_auto':
                self.setting.avodi_flashing_auto()
                print('避免闪烁自动')
            elif parametrize_info == 'avodi_flashing_off':
                self.setting.avodi_flashing_off()
                print('避免闪烁关闭')
            elif parametrize_info == 'avodi_flashing_60hz':
                self.setting.avodi_flashing_60hz()
                print('避免闪烁60hz')
            elif parametrize_info == 'avodi_flashing_50hz':
                self.setting.avodi_flashing_50hz()
                print('避免闪烁50hz')
            elif parametrize_info == 'Focus_sound_off':
                self.setting.Focus_sound()
                print('关闭对焦声音')
            elif parametrize_info == 'Focus_sound_on':
                # if state == 'T':
                #     self.setting.Focus_sound()
                print('开启对焦声音')

            elif parametrize_info == 'logo_on':
                self.setting.on_off_logo()
                print('开启品牌水印')
            elif parametrize_info == 'logo_off':
                # self.setting.on_off_logo()
                print('关闭品牌水印')
            elif parametrize_info == 'position_logo_on':
                self.setting.on_off_position_logo()
                print('开启地理位置水印')
            elif parametrize_info == 'position_logo_off':
                # self.setting.on_off_position_logo()
                print('关闭地理位置水印')
            elif parametrize_info == 'time_logo_on':
                self.setting.on_off_time_logo()
                print('开启时间水印')
            elif parametrize_info == 'time_logo_off':
                # self.setting.on_off_time_logo()
                print('关闭时间水印')

            elif parametrize_info == 'photo_size_16m_4_3':
                self.setting.photo_size_16m_4_3()
                print('照片大小16M（4:3）')
            elif parametrize_info == 'photo_size_16m_18_9':
                self.setting.photo_size_16m_18_9()
                print('照片大小16M（18:9）')
            elif parametrize_info == 'photo_size_8m_18_9':
                self.setting.photo_size_8m_18_9()
                print('照片大小8M（18:9）')
            elif parametrize_info == 'photo_size_8m_4_3':
                self.setting.photo_size_8m_4_3()
                print('照片大小8M（4:3）')
            elif parametrize_info == 'loc_info_on':
                self.setting.save_location_information()
                print('开启保存位置信息')
            elif parametrize_info == 'loc_info_off':
                # if state == 'T':
                #     self.setting.save_location_information()
                print('关闭保存位置信息')

            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置拍照功能：', loc_info=parametrize_info[2])

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置音量键拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置触屏拍照功能：')
            # time.sleep(2)

            # 后置延时拍照3s
            # 延时3s
            self.main_setting.timer_3()
            main_page.click_photo(self.base_obj)
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置3s功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置音量键3s功能：')

            self.setting.touch_screen()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置触屏3s拍照功能：')
            # time.sleep(2)

            # 后置延时10s
            # 延时10s
            self.main_setting.timer_10()
            main_page.click_photo(self.base_obj)
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置10s拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置音量键10s拍照功能：')

            self.setting.touch_screen()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置触屏10s拍照功能：')
            # time.sleep(2)

            # 关闭延时
            self.main_setting.off_timer()

            # 关闭闪光灯
            self.main_setting.off_flash()
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置关闭闪光灯拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置音量键关闭闪光灯拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置触屏关闭闪光灯拍照功能：')
            # time.sleep(2)
            #
            # 开启闪光灯
            self.main_setting.on_flash()
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置开启闪光灯拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置音量键开启闪光灯拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置触屏开启闪光灯拍照功能：')
            # time.sleep(2)

            # 回到闪光灯初始状态 自动
            self.main_setting.auto_flash()

            # 开启HDR
            self.main_setting.on_off_hdr()
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置开启HDR拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置音量键开启HDR拍照功能：')  #

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置触屏开启HDR拍照功能：')
            # time.sleep(2)
            # 回到HDR初始状态
            self.main_setting.on_off_hdr()

            # 一遍功能正常运行完成 状态为T
            state = 'T'
            print(state)
        except:
            # global state
            state = 'F'
            print('后置拍照功能：', state)

    # 前置拍照功能 234
    @pytest.mark.parametrize("front_parametrize_info", front_parametrize_info)
    def test_1_click_photo_on_facing(self, front_parametrize_info):

        # 切换至前置摄像头
        main_page.onoff_front_facing(self.base_obj)

        global state
        try:
            # 开关人脸识别
            if front_parametrize_info == 'face_recognition_off':
                self.setting.on_off_face_recognition()
                print('关闭人脸识别')
            elif front_parametrize_info == 'face_recognition_on':
                # if state == 'T':
                #     self.setting.on_off_face_recognition()
                print('开启人脸识别')
            elif front_parametrize_info == 'face_attribute_on':
                self.setting.on_off_face_attribute()
                print('开启人脸属性')
            elif front_parametrize_info == 'face_attribute_off':
                # if state == 'T':
                #     self.setting.on_off_face_attribute()
                print('关闭人脸属性')
            elif front_parametrize_info == 'grid_lines_on':
                self.setting.Grid_lines()
                print('开启网格线')
            elif front_parametrize_info == 'grid_lines_off':
                # if state == 'T':
                #     self.setting.Grid_lines()
                print('关闭网格线')
            elif front_parametrize_info == 'time_delay_off':
                self.setting.time_delay()
                print('关闭零延时')
            elif front_parametrize_info == 'time_delay_on':
                # self.setting.time_delay()
                print('开启零延时')
            elif front_parametrize_info == 'shutter_sound_off':
                self.setting.shutter_sound()
                print('关闭快门声音')
            elif front_parametrize_info == 'shutter_sound_on':
                # if state == 'T':
                #     self.setting.shutter_sound()
                print('开启快门声音')
            elif front_parametrize_info == 'avodi_flashing_auto':
                self.setting.avodi_flashing_auto()
                print('避免闪烁自动')
            elif front_parametrize_info == 'avodi_flashing_off':
                self.setting.avodi_flashing_off()
                print('避免闪烁关闭')
            elif front_parametrize_info == 'avodi_flashing_60hz':
                self.setting.avodi_flashing_60hz()
                print('避免闪烁60hz')
            elif front_parametrize_info == 'avodi_flashing_50hz':
                self.setting.avodi_flashing_50hz()
                print('避免闪烁50hz')
            elif front_parametrize_info == 'logo_on':
                self.setting.on_off_logo()
                print('开启品牌水印')
            elif front_parametrize_info == 'logo_off':
                # self.setting.on_off_logo()
                print('关闭品牌水印')
            elif front_parametrize_info == 'position_logo_on':
                self.setting.on_off_position_logo()
                print('开启地理位置水印')
            elif front_parametrize_info == 'position_logo_off':
                # self.setting.on_off_position_logo()
                print('关闭地理位置水印')
            elif front_parametrize_info == 'time_logo_on':
                self.setting.on_off_time_logo()
                print('开启时间水印')
            elif front_parametrize_info == 'time_logo_off':
                # self.setting.on_off_time_logo()
                print('关闭时间水印')

            elif front_parametrize_info == 'photo_size_8m_18_9':
                self.setting.photo_size_8m_18_9()
                print('照片大小8M（18:9）')
            elif front_parametrize_info == 'photo_size_2m_16_9':
                self.setting.photo_size_2m_16_9()
                print('照片大小2M（18:9）')
            elif front_parametrize_info == 'photo_size_2m_4_3':
                self.setting.photo_size_2m_4_3()
                print('照片大小2M（4:3）')
            elif front_parametrize_info == 'photo_size_8m_4_3':
                self.setting.photo_size_8m_4_3()
                print('照片大小8M（4:3）')
            elif front_parametrize_info == 'loc_info_on':
                self.setting.save_location_information()
                print('开启保存位置信息')
            elif front_parametrize_info == 'loc_info_off':
                # if state == 'T':
                #     self.setting.save_location_information()
                print('关闭保存位置信息')

            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置音量键拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置触屏拍照功能：')
            # time.sleep(2)

            # 延时拍照功能
            # 延时3s
            self.main_setting.timer_3()

            main_page.click_photo(self.base_obj)
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置延时拍照3s功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置音量键拍照3s功能：')

            self.setting.touch_screen()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置触屏拍照3s功能：')
            # time.sleep(2)

            # 延时10s
            self.main_setting.timer_10()

            main_page.click_photo(self.base_obj)
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置延时拍照10s功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置音量键拍照10s功能：')

            self.setting.touch_screen()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置触屏拍照10s功能：')
            # time.sleep(2)

            # 关闭延时
            self.main_setting.off_timer()

            # 一遍功能正常运行完成 状态为T
            state = 'T'
        except:
            # global state
            state = 'F'
            print('前置拍照功能：', state)

    # 美颜拍照 572
    @pytest.mark.parametrize("parametrize_info", parametrize_info)
    def test_2_beauty_photo(self, parametrize_info):

        # 美颜坐标 (425, 1160),(495, 1232)
        main_page.beauty_photo(self.base_obj)

        global state
        try:
            # 开关
            if parametrize_info == 'face_recognition_off':
                self.setting.ace_recognition()
                print('关闭人脸识别')
            elif parametrize_info == 'face_recognition_on':
                # if state == 'T':
                #     self.setting.ace_recognition()
                print('开启人脸识别')
            elif parametrize_info == 'grid_lines_on':
                self.setting.Grid_lines()
                print('开启网格线')
            elif parametrize_info == 'grid_lines_off':
                # if state == 'T':
                #     self.setting.Grid_lines()
                print('关闭网格线')
            elif parametrize_info == 'time_delay_off':
                self.setting.time_delay()
                print('关闭零延时')
            elif parametrize_info == 'time_delay_on':
                # self.setting.time_delay()
                print('开启零延时')
            elif parametrize_info == 'shutter_sound_off':
                self.setting.shutter_sound()
                print('关闭快门声音')
            elif parametrize_info == 'shutter_sound_on':
                # if state == 'T':
                #     self.setting.shutter_sound()
                print('开启快门声音')
            elif parametrize_info == 'avodi_flashing_auto':
                self.setting.avodi_flashing_auto()
                print('避免闪烁自动')
            elif parametrize_info == 'avodi_flashing_off':
                self.setting.avodi_flashing_off()
                print('避免闪烁关闭')
            elif parametrize_info == 'avodi_flashing_60hz':
                self.setting.avodi_flashing_60hz()
                print('避免闪烁60hz')
            elif parametrize_info == 'avodi_flashing_50hz':
                self.setting.avodi_flashing_50hz()
                print('避免闪烁50hz')
            elif parametrize_info == 'Focus_sound_off':
                self.setting.Focus_sound()
                print('关闭对焦声音')
            elif parametrize_info == 'Focus_sound_on':
                # if state == 'T':
                #     self.setting.Focus_sound()
                print('开启对焦声音')

            elif parametrize_info == 'logo_on':
                self.setting.on_off_logo()
                print('开启品牌水印')
            elif parametrize_info == 'logo_off':
                # self.setting.on_off_logo()
                print('关闭品牌水印')
            elif parametrize_info == 'position_logo_on':
                self.setting.on_off_position_logo()
                print('开启地理位置水印')
            elif parametrize_info == 'position_logo_off':
                # self.setting.on_off_position_logo()
                print('关闭地理位置水印')
            elif parametrize_info == 'time_logo_on':
                self.setting.on_off_time_logo()
                print('开启时间水印')
            elif parametrize_info == 'time_logo_off':
                # self.setting.on_off_time_logo()
                print('关闭时间水印')

            elif parametrize_info == 'photo_size_16m_4_3':
                self.setting.photo_size_16m_4_3()
                print('照片大小16M（4:3）')
            elif parametrize_info == 'photo_size_16m_18_9':
                self.setting.photo_size_16m_18_9()
                print('照片大小16M（18:9）')
            elif parametrize_info == 'photo_size_8m_18_9':
                self.setting.photo_size_8m_18_9()
                print('照片大小8M（18:9）')
            elif parametrize_info == 'photo_size_8m_4_3':
                self.setting.photo_size_8m_4_3()
                print('照片大小8M（4:3）')
            elif parametrize_info == 'loc_info_on':
                self.setting.save_location_information()
                print('开启保存位置信息')
            elif parametrize_info == 'loc_info_off':
                # if state == 'T':
                #     self.setting.save_location_information()
                print('关闭保存位置信息')

            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            # 获取现有照片数量
            self.photo.get_new_photo_sum(test_case_name='后置美颜功能：')

            # 点击音量键拍照
            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='音量键后置美颜功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置美颜触屏拍照功能：')
            # time.sleep(2)

            # 延时3s
            self.main_setting.timer_3()

            main_page.click_photo(self.base_obj)
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置美颜3s功能：')

            # 点击音量键拍照
            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='音量键后置美颜3s功能：')

            # 触屏拍照
            self.setting.touch_screen()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置美颜触屏3s美颜功能：')
            # time.sleep(2)

            # 延时10s
            self.main_setting.timer_10()

            main_page.click_photo(self.base_obj)
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置美颜10s功能：')

            # 点击音量键拍照
            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='音量键后置美颜10s功能：')

            # 触屏拍照
            self.setting.touch_screen()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置美颜触屏10s美颜功能：')
            # time.sleep(2)

            # 关闭延时
            self.main_setting.off_timer()

            # 关闭闪光灯
            self.main_setting.off_flash()
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置关闭闪光灯美颜功能：')

            # 点击音量键拍照
            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置音量键关闭闪光灯美颜功能：')

            # 触屏拍照
            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置触屏关闭闪光灯美颜功能：')
            # time.sleep(2)

            # 开启闪光灯
            self.main_setting.on_flash()

            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置开启闪光灯美颜功能：')

            # 点击音量键拍照
            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='音量键后置开启闪光灯美颜功能：')

            # 触屏拍照
            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置美颜触屏开启闪光灯美颜功能：')
            # time.sleep(2)

            # 回到闪光灯初始状态 自动
            self.main_setting.auto_flash()

            # HDR功能
            self.main_setting.on_off_hdr()

            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置HDR美颜功能：')

            # 点击音量键拍照
            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='音量键后置HDR美颜功能：')

            # 触屏拍照
            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置触屏HDR美颜功能：')
            # time.sleep(2)

            # 回到HDR初始状态
            self.main_setting.on_off_hdr()

            # 美颜内部功能
            # 美颜中的美颜
            # 点击美颜
            main_page.beauty_beauty(self.base_obj)
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            # 获取现有照片数量
            self.photo.get_new_photo_sum(test_case_name='后置美颜功能_美颜：')

            # 点击美肤
            main_page.beauty_skin(self.base_obj)
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            # 获取现有照片数量
            self.photo.get_new_photo_sum(test_case_name='后置美颜功能_美肤：')

            # 点击瘦脸
            main_page.beauty_thin_face(self.base_obj)
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            # 获取现有照片数量
            self.photo.get_new_photo_sum(test_case_name='后置美颜功能_瘦脸：')

            # 点击大眼
            main_page.beauty_big_eyes(self.base_obj)
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            # 获取现有照片数量
            self.photo.get_new_photo_sum(test_case_name='后置美颜功能_大眼：')

            # 一遍功能正常运行完成 状态为T
            state = 'T'
        except:
            # global state
            state = 'F'
            print('后置美颜功能：', state)

    # 美颜前置功能 312
    @pytest.mark.parametrize("front_parametrize_info", front_parametrize_info)
    def test_2_beauty_photo_facing(self, front_parametrize_info):

        # 美颜坐标 (425, 1160),(495, 1232)
        main_page.beauty_photo(self.base_obj)
        # 切换至前置摄像头
        main_page.onoff_front_facing(self.base_obj)

        global state
        try:
            # 开关人脸识别
            if front_parametrize_info == 'face_recognition_off':
                self.setting.on_off_face_recognition()
                print('关闭人脸识别')
            elif front_parametrize_info == 'face_recognition_on':
                # if state == 'T':
                #     self.setting.on_off_face_recognition()
                print('开启人脸识别')
            elif front_parametrize_info == 'face_attribute_on':
                self.setting.on_off_face_attribute()
                print('开启人脸属性')
            elif front_parametrize_info == 'face_attribute_off':
                # if state == 'T':
                #     self.setting.on_off_face_attribute()
                print('关闭人脸属性')
            elif front_parametrize_info == 'grid_lines_on':
                self.setting.Grid_lines()
                print('开启网格线')
            elif front_parametrize_info == 'grid_lines_off':
                # if state == 'T':
                #     self.setting.Grid_lines()
                print('关闭网格线')
            elif front_parametrize_info == 'time_delay_off':
                self.setting.time_delay()
                print('关闭零延时')
            elif front_parametrize_info == 'time_delay_on':
                # self.setting.time_delay()
                print('开启零延时')
            elif front_parametrize_info == 'shutter_sound_off':
                self.setting.shutter_sound()
                print('关闭快门声音')
            elif front_parametrize_info == 'shutter_sound_on':
                # if state == 'T':
                #     self.setting.shutter_sound()
                print('开启快门声音')
            elif front_parametrize_info == 'avodi_flashing_auto':
                self.setting.avodi_flashing_auto()
                print('避免闪烁自动')
            elif front_parametrize_info == 'avodi_flashing_off':
                self.setting.avodi_flashing_off()
                print('避免闪烁关闭')
            elif front_parametrize_info == 'avodi_flashing_60hz':
                self.setting.avodi_flashing_60hz()
                print('避免闪烁60hz')
            elif front_parametrize_info == 'avodi_flashing_50hz':
                self.setting.avodi_flashing_50hz()
                print('避免闪烁50hz')

            elif front_parametrize_info == 'logo_on':
                self.setting.on_off_logo()
                print('开启品牌水印')
            elif front_parametrize_info == 'logo_off':
                # self.setting.on_off_logo()
                print('关闭品牌水印')
            elif front_parametrize_info == 'position_logo_on':
                self.setting.on_off_position_logo()
                print('开启地理位置水印')
            elif front_parametrize_info == 'position_logo_off':
                # self.setting.on_off_position_logo()
                print('关闭地理位置水印')
            elif front_parametrize_info == 'time_logo_on':
                self.setting.on_off_time_logo()
                print('开启时间水印')
            elif front_parametrize_info == 'time_logo_off':
                # self.setting.on_off_time_logo()
                print('关闭时间水印')

            elif front_parametrize_info == 'photo_size_8m_18_9':
                self.setting.photo_size_8m_18_9()
                print('照片大小8M（18:9）')
            elif front_parametrize_info == 'photo_size_2m_16_9':
                self.setting.photo_size_2m_16_9()
                print('照片大小2M（18:9）')
            elif front_parametrize_info == 'photo_size_2m_4_3':
                self.setting.photo_size_2m_4_3()
                print('照片大小2M（4:3）')
            elif front_parametrize_info == 'photo_size_8m_4_3':
                self.setting.photo_size_8m_4_3()
                print('照片大小8M（4:3）')
            elif front_parametrize_info == 'loc_info_on':
                self.setting.save_location_information()
                print('开启保存位置信息')
            elif front_parametrize_info == 'loc_info_off':
                # if state == 'T':
                #     self.setting.save_location_information()
                print('关闭保存位置信息')

            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置美颜功能：')

            # 点击音量键拍照
            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置音量键美颜功能：')

            # 触屏拍照
            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置触屏美颜功能：')
            # time.sleep(2)

            # 延时3s
            self.main_setting.timer_3()

            main_page.click_photo(self.base_obj)
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置美颜3s功能：')

            # 点击音量键拍照
            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='音量键前置美颜3s功能：')

            # 触屏拍照
            self.setting.touch_screen()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置触屏美颜3s功能：')
            # time.sleep(2)

            # 延时10s
            self.main_setting.timer_10()

            main_page.click_photo(self.base_obj)
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置美颜10s功能：')  # !

            # 点击音量键拍照
            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置美颜音量键10s功能：')  # !

            # 触屏拍照
            self.setting.touch_screen()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置触屏美颜10s功能：')
            # time.sleep(2)

            # 关闭延时
            self.main_setting.off_timer()

            # 美颜内部功能
            # 美颜中的美颜
            # 点击美颜
            main_page.beauty_beauty(self.base_obj)
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            # 获取现有照片数量
            self.photo.get_new_photo_sum(test_case_name='前置美颜功能_美颜：')

            # 点击美肤
            main_page.beauty_skin(self.base_obj)
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            # 获取现有照片数量
            self.photo.get_new_photo_sum(test_case_name='前置美颜功能_美肤：')

            # 点击瘦脸
            main_page.beauty_thin_face(self.base_obj)
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            # 获取现有照片数量
            self.photo.get_new_photo_sum(test_case_name='前置美颜功能_瘦脸：')

            # 点击大眼
            main_page.beauty_big_eyes(self.base_obj)
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            # 获取现有照片数量
            self.photo.get_new_photo_sum(test_case_name='前置美颜功能_大眼：')

            # 一遍功能正常运行完成 状态为T
            state = 'T'
        except:
            # global state
            state = 'F'
            print('前置美颜拍照功能：', state)

    # 全景拍照 12
    @pytest.mark.parametrize("panorama_parametrize_info",
                             ['grid_lines_on', 'grid_lines_off', 'shutter_sound_off', 'shutter_sound_on'])
    def test_3_panorama(self, panorama_parametrize_info):
        global state
        try:
            # 开关网格线
            if panorama_parametrize_info == 'grid_lines_on':
                self.setting.panorama_Grid_lines()
                print('开启网格线')
            elif panorama_parametrize_info == 'grid_lines_off':
                # if state == 'T':
                #     self.setting.panorama_Grid_lines()
                main_page.panorama_photo(self.base_obj)
                print('关闭网格线')
            elif panorama_parametrize_info == 'shutter_sound_off':
                self.setting.panorama_shutter_sound()
                print('关闭快门声音')
            elif panorama_parametrize_info == 'shutter_sound_on':
                # if state == 'T':
                #     self.setting.panorama_shutter_sound()
                main_page.panorama_photo(self.base_obj)
                print('开启快门声音')

            # 拍照
            main_page.click_photo(self.base_obj)
            # 全景拍照确定按钮
            main_page.panorama_click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置全景功能：')

            # 点击音量键全景拍照
            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(3)
            # 全景拍照确定按钮
            main_page.panorama_click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='音量键后置全景功能：')

            # 触屏拍照
            self.setting.touch_screen()
            time.sleep(2)
            # 全景拍照确定按钮
            main_page.panorama_click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置触屏全景功能：')
            # time.sleep(2)

            # 一遍功能正常运行完成 状态为T
            state = 'T'
        except:
            # global state
            state = 'F'
            print('后置全景功能：', state)

    # 视频拍摄 120
    @pytest.mark.parametrize("video_parametrize_info", video_parametrize_info)
    def test_4_video(self, video_parametrize_info):
        # 视频坐标 [225,1160][295,1232]
        # 进入视频功能
        main_page.video(self.base_obj)

        global state
        try:
            # 开关网格线
            if video_parametrize_info == 'grid_lines_on':
                self.setting.Grid_lines()
                print('开启网格线')
            elif video_parametrize_info == 'grid_lines_on_off':
                # if state == 'T':
                #     self.setting.Grid_lines()
                print('关闭网格线')
            elif video_parametrize_info == 'avodi_flashing_auto':
                self.setting.avodi_flashing_auto()
                print('避免闪烁自动')
            elif video_parametrize_info == 'avodi_flashing_off':
                self.setting.avodi_flashing_off()
                print('避免闪烁关闭')
            elif video_parametrize_info == 'avodi_flashing_60hz':
                self.setting.avodi_flashing_60hz()
                print('避免闪烁60hz')
            elif video_parametrize_info == 'avodi_flashing_50hz':
                self.setting.avodi_flashing_50hz()
                print('避免闪烁50hz')
            elif video_parametrize_info == 'Focus_sound_off':
                self.setting.Focus_sound()
                print('关闭对焦声音')
            elif video_parametrize_info == 'Focus_sound_on':
                # if state == 'T':
                #     self.setting.Focus_sound()
                print('开启对焦声音')
            elif video_parametrize_info == 'stabilization_on':
                self.setting.on_off_stabilization()
                print('开启防抖')
            elif video_parametrize_info == 'stabilization_off':
                # self.setting.on_off_stabilization()
                print('关闭防抖')

            if video_parametrize_info == 'FHD':
                self.setting.video_quality()
                self.setting.video_fhd()
                print('视频画质FHD')
            elif video_parametrize_info == 'VGA':
                self.setting.video_quality()
                self.setting.video_vga()
                print('视频画质VGA')
            elif video_parametrize_info == 'HD':
                self.setting.video_quality()
                self.setting.video_hd()
                print('视频画质HD')
            elif video_parametrize_info == 'loc_info_on':
                self.setting.less_save_location_information()
                print('开启保存位置信息')
            elif video_parametrize_info == 'loc_info_off':
                # if state == 'T':
                #     self.setting.save_location_information()
                print('关闭保存位置信息')

            # 点击开始录制
            main_page.video_in(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置视频功能：', modle=2, func ='后置视频' )

            # 关闭闪光灯
            self.main_setting.off_flash()
            main_page.video_in(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置关闭闪光灯视频功能：', modle=2, func ='后置视频')

            # 开启闪光灯
            self.main_setting.on_flash()
            main_page.video_in(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置开启闪光灯视频功能：', modle=2, func ='后置视频')

            # 回到闪光灯初始状态 自动
            self.main_setting.auto_flash()
            # self.main_setting.on_flash()
            main_page.video_in(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置闪光灯自动视频功能：', modle=2, func ='后置视频')

            # 一遍功能正常运行完成 状态为T
            state = 'T'
        except:
            # global state
            state = 'F'
            print('后置视频功能：', state)

    # 前置录制视频 11
    @pytest.mark.parametrize("front_video_parametrize_info", front_video_parametrize_info)
    def test_4_video_facing(self, front_video_parametrize_info):

        # 进入视频功能
        main_page.video(self.base_obj)
        # 切换至前置摄像头
        main_page.onoff_front_facing(self.base_obj)

        global state
        try:
            # 开关网格线
            if front_video_parametrize_info == 'grid_lines_on':
                self.setting.Grid_lines()
                print('开启网格线')
            elif front_video_parametrize_info == 'grid_lines_off':
                # if state == 'T':
                #     self.setting.Grid_lines()
                print('关闭网格线')
            elif front_video_parametrize_info == 'avodi_flashing_auto':
                # self.setting.avodi_flashing_auto()
                print('避免闪烁自动')
            elif front_video_parametrize_info == 'avodi_flashing_off':
                self.setting.avodi_flashing_off()
                print('避免闪烁关闭')
            elif front_video_parametrize_info == 'avodi_flashing_60hz':
                self.setting.avodi_flashing_60hz()
                print('避免闪烁60hz')
            elif front_video_parametrize_info == 'avodi_flashing_50hz':
                self.setting.avodi_flashing_50hz()
                print('避免闪烁50hz')
            elif front_video_parametrize_info == 'FHD':
                self.setting.video_quality()
                self.setting.video_fhd()
                print('视频画质FHD')
            elif front_video_parametrize_info == 'VGA':
                self.setting.video_quality()
                self.setting.video_vga()
                print('视频画质VGA')
            elif front_video_parametrize_info == 'HD':
                self.setting.video_quality()
                self.setting.video_hd()
                print('视频画质HD')
            elif front_video_parametrize_info == 'loc_info_on':
                self.setting.less_save_location_information()
                print('开启保存位置信息')
            elif front_video_parametrize_info == 'loc_info_off':
                # if state == 'T':
                #     self.setting.save_location_information()
                print('关闭保存位置信息')

            # 点击视频录制按钮
            main_page.click_photo(self.base_obj)
            main_page.front_facing_video(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置视频功能：', func ='前置视频')

            # 一遍功能正常运行完成 状态为T
            state = 'T'
        except:
            # global state
            state = 'F'
            print('前置视频功能：', state)

    # 美视 210
    @pytest.mark.parametrize("video_parametrize_info", video_parametrize_info)
    def test_5_apparent(self, video_parametrize_info):

        # 美视坐标 [225,1160][295,1232]
        main_page.beauty_video(self.base_obj)

        global state
        try:
            # 开关网格线
            if video_parametrize_info == 'grid_lines_on':
                self.setting.Grid_lines()
                print('开启网格线')
            elif video_parametrize_info == 'grid_lines_off':
                # if state == 'T':
                #     self.setting.Grid_lines()
                print('关闭网格线')
            elif video_parametrize_info == 'avodi_flashing_auto':
                self.setting.avodi_flashing_auto()
                print('避免闪烁自动')
            elif video_parametrize_info == 'avodi_flashing_off':
                self.setting.avodi_flashing_off()
                print('避免闪烁关闭')
            elif video_parametrize_info == 'avodi_flashing_60hz':
                self.setting.avodi_flashing_60hz()
                print('避免闪烁60hz')
            elif video_parametrize_info == 'avodi_flashing_50hz':
                self.setting.avodi_flashing_50hz()
                print('避免闪烁50hz')
            elif video_parametrize_info == 'Focus_sound_off':
                self.setting.Focus_sound()
                print('关闭对焦声音')
            elif video_parametrize_info == 'Focus_sound_on':
                # if state == 'T':
                #     self.setting.Focus_sound()
                print('开启对焦声音')
            elif video_parametrize_info == 'stabilization_on':
                self.setting.on_off_stabilization()
                print('开启防抖')
            elif video_parametrize_info == 'stabilization_off':
                # self.setting.on_off_stabilization()
                print('关闭防抖')
            elif video_parametrize_info == 'FHD':
                self.setting.video_quality()
                self.setting.video_fhd()
                print('视频画质FHD')
            elif video_parametrize_info == 'VGA':
                self.setting.video_quality()
                self.setting.video_vga()
                print('视频画质VGA')
            elif video_parametrize_info == 'HD':
                self.setting.video_quality()
                self.setting.video_hd()
                print('视频画质HD')
            elif video_parametrize_info == 'loc_info_on':
                self.setting.less_save_location_information()
                print('开启保存位置信息')
            elif video_parametrize_info == 'loc_info_off':
                # if state == 'T':
                #     self.setting.save_location_information()
                print('关闭保存位置信息')

            main_page.video_in(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置闪光灯自动美视功能：', modle=2, func ='后置美视')

            # 关闭闪光灯
            self.main_setting.off_flash()
            main_page.video_in(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置关闭闪光灯美视功能：', modle=2, func ='后置美视')

            # 开启闪光灯
            self.main_setting.on_flash()
            main_page.video_in(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置开启闪光灯美视功能：', modle=2, func ='后置美视')

            # 回到闪光灯初始状态 自动
            self.main_setting.auto_flash()

            # 点击美颜
            main_page.beauty_beauty(self.base_obj)
            main_page.video_in(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置美视功能_美颜：', modle=2, func ='后置美视')

            # 点击美肤
            main_page.beauty_skin(self.base_obj)
            main_page.video_in(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置美视功能_美肤：', modle=2, func ='后置美视')

            # 点击瘦脸
            main_page.beauty_thin_face(self.base_obj)
            main_page.video_in(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置美视功能_瘦脸：', modle=2, func ='后置美视')

            # 点击大眼
            main_page.beauty_big_eyes(self.base_obj)
            main_page.video_in(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置美视功能_大眼：', modle=2, func ='后置美视')
            # time.sleep(2)

            # 一遍功能正常运行完成 状态为T
            state = 'T'
        except:
            # global state
            state = 'F'
            print('后置美视功能：', state)

    # 前置摄像头美视功能 55
    @pytest.mark.parametrize("front_video_parametrize_info", front_video_parametrize_info)
    def test_5_apparent_facing(self, front_video_parametrize_info):

        # 美视坐标 [225,1160][295,1232]
        main_page.beauty_video(self.base_obj)
        # 切换至前置摄像头
        main_page.onoff_front_facing(self.base_obj)

        global state
        try:
            # 开关网格线
            if front_video_parametrize_info == 'grid_lines_on':
                self.setting.Grid_lines()
                print('开启网格线')
            elif front_video_parametrize_info == 'grid_lines_off':
                # if state == 'T':
                #     self.setting.Grid_lines()
                print('关闭网格线')
            elif front_video_parametrize_info == 'avodi_flashing_auto':
                self.setting.avodi_flashing_auto()
                print('避免闪烁自动')
            elif front_video_parametrize_info == 'avodi_flashing_off':
                self.setting.avodi_flashing_off()
                print('避免闪烁关闭')
            elif front_video_parametrize_info == 'avodi_flashing_60hz':
                self.setting.avodi_flashing_60hz()
                print('避免闪烁60hz')
            elif front_video_parametrize_info == 'avodi_flashing_50hz':
                self.setting.avodi_flashing_50hz()
                print('避免闪烁50hz')
            elif front_video_parametrize_info == 'FHD':
                self.setting.video_quality()
                self.setting.video_fhd()
                print('视频画质FHD')
            elif front_video_parametrize_info == 'VGA':
                self.setting.video_quality()
                self.setting.video_vga()
                print('视频画质VGA')
            elif front_video_parametrize_info == 'HD':
                self.setting.video_quality()
                self.setting.video_hd()
                print('视频画质HD')
            elif front_video_parametrize_info == 'loc_info_on':
                self.setting.less_save_location_information()
                print('开启保存位置信息')
            elif front_video_parametrize_info == 'loc_info_off':
                # if state == 'T':
                #     self.setting.save_location_information()
                print('关闭保存位置信息')

            # self.photo.get_old_photo_sum()
            # 点击前置美视功能
            main_page.front_facing_video_b(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置美视功能：', func ='前置美视')

            # 美颜内部功能
            # 美颜中的美颜
            # 点击美颜
            main_page.beauty_beauty(self.base_obj)
            main_page.front_facing_video_b(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置美视功能_美颜：', func ='前置美视')

            # 点击美肤
            main_page.beauty_skin(self.base_obj)
            main_page.front_facing_video_b(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置美视功能_美肤：', func ='前置美视')

            # 点击瘦脸
            main_page.beauty_thin_face(self.base_obj)
            main_page.front_facing_video_b(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置美视功能_瘦脸：', func ='前置美视')

            # 点击大眼
            main_page.beauty_big_eyes(self.base_obj)
            main_page.front_facing_video_b(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置美视功能_大眼：', func ='前置美视')
            # time.sleep(2)

            # 一遍功能正常运行完成 状态为T
            state = 'T'
        except:
            # global state
            state = 'F'
            print('前置美视功能：', state)

    # 后置人像模式 396
    @pytest.mark.parametrize("portrait_parametrize_info", portrait_parametrize_info)
    def test_6_portrait(self, portrait_parametrize_info):
        # 美视坐标 [225,1160][295,1232]
        main_page.beauty_video(self.base_obj)
        # 进入人像模式
        main_page.portrait(self.base_obj)

        global state
        try:
            # 开关
            if portrait_parametrize_info == 'face_recognition_off':
                self.setting.ace_recognition()
                print('关闭人脸识别')
            elif portrait_parametrize_info == 'face_recognition_on':
                # print(state)
                # if state == 'F':
                #     self.setting.ace_recognition()
                print('开启人脸识别')
            elif portrait_parametrize_info == 'grid_lines_on':
                self.setting.Grid_lines()
                print('开启网格线')
            elif portrait_parametrize_info == 'grid_lines_off':
                # if state == 'T':
                #     self.setting.Grid_lines()
                print('关闭网格线')
            elif portrait_parametrize_info == 'time_delay_off':
                self.setting.time_delay()
                print('关闭零延时')
            elif portrait_parametrize_info == 'time_delay_on':
                # self.setting.time_delay()
                print('开启零延时')
            elif portrait_parametrize_info == 'shutter_sound_off':
                self.setting.shutter_sound()
                print('关闭快门声音')
            elif portrait_parametrize_info == 'shutter_sound_on':
                # if state == 'T':
                #     self.setting.shutter_sound()
                print('开启快门声音')
            elif portrait_parametrize_info == 'avodi_flashing_auto':
                self.setting.avodi_flashing_auto()
                print('避免闪烁自动')
            elif portrait_parametrize_info == 'avodi_flashing_off':
                self.setting.avodi_flashing_off()
                print('避免闪烁关闭')
            elif portrait_parametrize_info == 'avodi_flashing_60hz':
                self.setting.avodi_flashing_60hz()
                print('避免闪烁60hz')
            elif portrait_parametrize_info == 'avodi_flashing_50hz':
                self.setting.avodi_flashing_50hz()
                print('避免闪烁50hz')
            elif portrait_parametrize_info == 'Focus_sound_off':
                self.setting.Focus_sound()
                print('关闭对焦声音')
            elif portrait_parametrize_info == 'Focus_sound_on':
                # if state == 'T':
                #     self.setting.Focus_sound()
                print('开启对焦声音')

            elif portrait_parametrize_info == 'logo_on':
                self.setting.on_off_logo()
                print('开启品牌水印')
            elif portrait_parametrize_info == 'logo_off':
                # self.setting.on_off_logo()
                print('关闭品牌水印')
            elif portrait_parametrize_info == 'position_logo_on':
                self.setting.on_off_position_logo()
                print('开启地理位置水印')
            elif portrait_parametrize_info == 'position_logo_off':
                # self.setting.on_off_position_logo()
                print('关闭地理位置水印')
            elif portrait_parametrize_info == 'time_logo_on':
                self.setting.on_off_time_logo()
                print('开启时间水印')
            elif portrait_parametrize_info == 'time_logo_off':
                # self.setting.on_off_time_logo()
                print('关闭时间水印')

            elif portrait_parametrize_info == 'loc_info_on':
                self.setting.save_location_information()
                print('开启保存位置信息')
            elif portrait_parametrize_info == 'loc_info_off':
                # if state == 'T':
                #     self.setting.save_location_information()
                print('关闭保存位置信息')

            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置人像功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置人像音量键拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置人像触屏拍照功能：')
            # time.sleep(2)

            # 后置延时拍照3s
            # 延时3s
            self.main_setting.timer_3()
            main_page.click_photo(self.base_obj)
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置人像3s功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置人像音量键3s功能：')

            self.setting.touch_screen()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置人像触屏3s拍照功能：')
            # time.sleep(2)

            # 后置延时10s
            # 延时10s
            self.main_setting.timer_10()
            main_page.click_photo(self.base_obj)
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置人像10s拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(15)
            self.photo.get_new_photo_sum(test_case_name='后置人像音量键10s拍照功能：')

            self.setting.touch_screen()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置人像触屏10s拍照功能：')
            # time.sleep(2)

            # 关闭延时
            self.main_setting.off_timer()

            # 关闭闪光灯
            self.main_setting.off_flash()
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置人像关闭闪光灯拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置人像音量键关闭闪光灯拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置人像触屏关闭闪光灯拍照功能：')
            # time.sleep(2)

            # 开启闪光灯
            self.main_setting.on_flash()
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置人像开启闪光灯拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置人像音量键开启闪光灯拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置人像触屏开启闪光灯拍照功能：')
            # time.sleep(2)

            # 回到闪光灯初始状态 自动
            self.main_setting.auto_flash()

            # 开启HDR
            self.main_setting.on_off_hdr()
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置人像开启HDR拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置人像音量键开启HDR拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置人像触屏开启HDR拍照功能：')
            # time.sleep(2)
            # 回到HDR初始状态
            self.main_setting.on_off_hdr()

            # 一遍功能正常运行完成 状态为T
            state = 'T'
            print(state)
        except:
            # global state
            state = 'F'
            print('后置人像拍照功能：', state)

    # 前置人像模式 180
    @pytest.mark.parametrize("front_portrait_parametrize_info", front_portrait_parametrize_info)
    def test_6_portrait_facing(self, front_portrait_parametrize_info):
        # 转换前置摄像头
        main_page.onoff_front_facing(self.base_obj)
        # 进入人像模式
        main_page.portrait(self.base_obj)
        #

        global state
        try:
            # 开关
            if front_portrait_parametrize_info == 'face_recognition_off':
                self.setting.ace_recognition()
                print('关闭人脸识别')
            elif front_portrait_parametrize_info == 'face_recognition_on':
                # print(state)
                # if state == 'F':
                #     self.setting.ace_recognition()
                print('开启人脸识别')
            elif front_portrait_parametrize_info == 'grid_lines_on':
                self.setting.Grid_lines()
                print('开启网格线')
            elif front_portrait_parametrize_info == 'grid_lines_off':
                # if state == 'T':
                #     self.setting.Grid_lines()
                print('关闭网格线')
            elif front_portrait_parametrize_info == 'time_delay_off':
                self.setting.time_delay()
                print('关闭零延时')
            elif front_portrait_parametrize_info == 'time_delay_on':
                # self.setting.time_delay()
                print('开启零延时')
            elif front_portrait_parametrize_info == 'shutter_sound_off':
                self.setting.shutter_sound()
                print('关闭快门声音')
            elif front_portrait_parametrize_info == 'shutter_sound_on':
                # if state == 'T':
                #     self.setting.shutter_sound()
                print('开启快门声音')
            elif front_portrait_parametrize_info == 'avodi_flashing_auto':
                self.setting.avodi_flashing_auto()
                print('避免闪烁自动')
            elif front_portrait_parametrize_info == 'avodi_flashing_off':
                self.setting.avodi_flashing_off()
                print('避免闪烁关闭')
            elif front_portrait_parametrize_info == 'avodi_flashing_60hz':
                self.setting.avodi_flashing_60hz()
                print('避免闪烁60hz')
            elif front_portrait_parametrize_info == 'avodi_flashing_50hz':
                self.setting.avodi_flashing_50hz()
                print('避免闪烁50hz')
            elif front_portrait_parametrize_info == 'logo_on':
                self.setting.on_off_logo()
                print('开启品牌水印')
            elif front_portrait_parametrize_info == 'logo_off':
                # self.setting.on_off_logo()
                print('关闭品牌水印')
            elif front_portrait_parametrize_info == 'position_logo_on':
                self.setting.on_off_position_logo()
                print('开启地理位置水印')
            elif front_portrait_parametrize_info == 'position_logo_off':
                # self.setting.on_off_position_logo()
                print('关闭地理位置水印')
            elif front_portrait_parametrize_info == 'time_logo_on':
                self.setting.on_off_time_logo()
                print('开启时间水印')
            elif front_portrait_parametrize_info == 'time_logo_off':
                # self.setting.on_off_time_logo()
                print('关闭时间水印')

            elif front_portrait_parametrize_info == 'loc_info_on':
                self.setting.save_location_information()
                print('开启保存位置信息')
            elif front_portrait_parametrize_info == 'loc_info_off':
                # if state == 'T':
                #     self.setting.save_location_information()
                print('关闭保存位置信息')

            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置人像功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置人像音量键拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置人像触屏拍照功能：')
            # time.sleep(2)

            # 后置延时拍照3s
            # 延时3s
            self.main_setting.timer_3()
            main_page.click_photo(self.base_obj)
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置人像3s功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置人像音量键3s功能：')

            self.setting.touch_screen()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置人像触屏3s拍照功能：')
            # time.sleep(2)

            # 后置延时10s
            # 延时10s
            self.main_setting.timer_10()
            main_page.click_photo(self.base_obj)
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置人像10s拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置人像音量键10s拍照功能：')

            self.setting.touch_screen()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置人像触屏10s拍照功能：')
            # time.sleep(2)

            # 一遍功能正常运行完成 状态为T
            state = 'T'
            print(state)
        except:
            # global state
            state = 'F'
            print('后置人像拍照功能：', state)

    # 后置儿童模式 600
    @pytest.mark.parametrize("parametrize_info", parametrize_info)
    def test_6_kid(self, parametrize_info):
        # 进入儿童模式
        main_page.kid(self.base_obj)

        global state
        try:
            # 开关
            if parametrize_info == 'face_recognition_off':
                self.setting.ace_recognition()
                print('关闭人脸识别')
            elif parametrize_info == 'face_recognition_on':
                # print(state)
                # if state == 'F':
                #     self.setting.ace_recognition()
                print('开启人脸识别')
            elif parametrize_info == 'grid_lines_on':
                self.setting.Grid_lines()
                print('开启网格线')
            elif parametrize_info == 'grid_lines_off':
                # if state == 'T':
                #     self.setting.Grid_lines()
                print('关闭网格线')
            elif parametrize_info == 'time_delay_off':
                self.setting.time_delay()
                print('关闭零延时')
            elif parametrize_info == 'time_delay_on':
                # self.setting.time_delay()
                print('开启零延时')
            elif parametrize_info == 'shutter_sound_off':
                self.setting.shutter_sound()
                print('关闭快门声音')
            elif parametrize_info == 'shutter_sound_on':
                # if state == 'T':
                #     self.setting.shutter_sound()
                print('开启快门声音')
            elif parametrize_info == 'avodi_flashing_auto':
                self.setting.avodi_flashing_auto()
                print('避免闪烁自动')
            elif parametrize_info == 'avodi_flashing_off':
                self.setting.avodi_flashing_off()
                print('避免闪烁关闭')
            elif parametrize_info == 'avodi_flashing_60hz':
                self.setting.avodi_flashing_60hz()
                print('避免闪烁60hz')
            elif parametrize_info == 'avodi_flashing_50hz':
                self.setting.avodi_flashing_50hz()
                print('避免闪烁50hz')
            elif parametrize_info == 'Focus_sound_off':
                self.setting.Focus_sound()
                print('关闭对焦声音')
            elif parametrize_info == 'Focus_sound_on':
                # if state == 'T':
                #     self.setting.Focus_sound()
                print('开启对焦声音')

            elif parametrize_info == 'logo_on':
                self.setting.on_off_logo()
                print('开启品牌水印')
            elif parametrize_info == 'logo_off':
                # self.setting.on_off_logo()
                print('关闭品牌水印')
            elif parametrize_info == 'position_logo_on':
                self.setting.on_off_position_logo()
                print('开启地理位置水印')
            elif parametrize_info == 'position_logo_off':
                # self.setting.on_off_position_logo()
                print('关闭地理位置水印')
            elif parametrize_info == 'time_logo_on':
                self.setting.on_off_time_logo()
                print('开启时间水印')
            elif parametrize_info == 'time_logo_off':
                # self.setting.on_off_time_logo()
                print('关闭时间水印')

            elif parametrize_info == 'photo_size_16m_4_3':
                self.setting.photo_size_16m_4_3()
                print('照片大小16M（4:3）')
            elif parametrize_info == 'photo_size_16m_18_9':
                self.setting.photo_size_16m_18_9()
                print('照片大小16M（18:9）')
            elif parametrize_info == 'photo_size_8m_18_9':
                self.setting.photo_size_8m_18_9()
                print('照片大小8M（18:9）')
            elif parametrize_info == 'photo_size_8m_4_3':
                self.setting.photo_size_8m_4_3()
                print('照片大小8M（4:3）')
            elif parametrize_info == 'loc_info_on':
                self.setting.save_location_information()
                print('开启保存位置信息')
            elif parametrize_info == 'loc_info_off':
                # if state == 'T':
                #     self.setting.save_location_information()
                print('关闭保存位置信息')

            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置儿童拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置儿童音量键拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置儿童触屏拍照功能：')
            # time.sleep(2)

            # 后置延时拍照3s
            # 延时3s
            self.main_setting.timer_3()
            main_page.click_photo(self.base_obj)
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置儿童3s功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置儿童音量键3s功能：')

            self.setting.touch_screen()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置儿童触屏3s拍照功能：')
            # time.sleep(2)

            # 后置延时10s
            # 延时10s
            self.main_setting.timer_10()
            main_page.click_photo(self.base_obj)
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置儿童10s拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置儿童音量键10s拍照功能：')

            self.setting.touch_screen()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置儿童触屏10s拍照功能：')
            # time.sleep(2)

            # 关闭延时
            self.main_setting.off_timer()

            # 关闭闪光灯
            self.main_setting.off_flash()
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置儿童关闭闪光灯拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置儿童音量键关闭闪光灯拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置儿童触屏关闭闪光灯拍照功能：')
            # time.sleep(2)
            #
            # 开启闪光灯
            self.main_setting.on_flash()
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置儿童开启闪光灯拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置儿童音量键开启闪光灯拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置儿童触屏开启闪光灯拍照功能：')
            # time.sleep(2)

            # 回到闪光灯初始状态 自动
            self.main_setting.auto_flash()

            # 开启HDR
            self.main_setting.on_off_hdr()
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置儿童开启HDR拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置儿童音量键开启HDR拍照功能：')  #

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置儿童触屏开启HDR拍照功能：')
            # time.sleep(2)
            # 回到HDR初始状态
            self.main_setting.on_off_hdr()

            main_page.kid_baby(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置儿童婴儿功能：')

            main_page.kid_bell(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置儿童铃铛功能：')

            main_page.kid_cat(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置儿童猫咪功能：')

            main_page.kid_dog(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置儿童小狗功能：')

            main_page.kid_drum(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置儿童大鼓功能：')

            # 一遍功能正常运行完成 状态为T
            state = 'T'
            print(state)
        except:
            # global state
            state = 'F'
            print('后置儿童拍照功能：', state)

    # 前置儿童模式 336
    @pytest.mark.parametrize("front_kid_parametrize_info", front_kid_parametrize_info)
    def test_6_kid_facing(self, front_kid_parametrize_info):
        # 进入儿童模式
        main_page.kid(self.base_obj)

        # 切换至前置摄像头
        main_page.onoff_front_facing(self.base_obj)

        global state
        try:
            # 开关人脸识别
            if front_kid_parametrize_info == 'face_recognition_off':
                self.setting.on_off_face_recognition()
                print('关闭人脸识别')
            elif front_kid_parametrize_info == 'face_recognition_on':
                # if state == 'T':
                #     self.setting.on_off_face_recognition()
                print('开启人脸识别')
            elif front_kid_parametrize_info == 'grid_lines_on':
                self.setting.Grid_lines()
                print('开启网格线')
            elif front_kid_parametrize_info == 'grid_lines_off':
                # if state == 'T':
                #     self.setting.Grid_lines()
                print('关闭网格线')
            elif front_kid_parametrize_info == 'time_delay_off':
                self.setting.time_delay()
                print('关闭零延时')
            elif front_kid_parametrize_info == 'time_delay_on':
                # self.setting.time_delay()
                print('开启零延时')
            elif front_kid_parametrize_info == 'shutter_sound_off':
                self.setting.shutter_sound()
                print('关闭快门声音')
            elif front_kid_parametrize_info == 'shutter_sound_on':
                # if state == 'T':
                #     self.setting.shutter_sound()
                print('开启快门声音')
            elif front_kid_parametrize_info == 'avodi_flashing_auto':
                self.setting.avodi_flashing_auto()
                print('避免闪烁自动')
            elif front_kid_parametrize_info == 'avodi_flashing_off':
                self.setting.avodi_flashing_off()
                print('避免闪烁关闭')
            elif front_kid_parametrize_info == 'avodi_flashing_60hz':
                self.setting.avodi_flashing_60hz()
                print('避免闪烁60hz')
            elif front_kid_parametrize_info == 'avodi_flashing_50hz':
                self.setting.avodi_flashing_50hz()
                print('避免闪烁50hz')
            elif front_kid_parametrize_info == 'logo_on':
                self.setting.on_off_logo()
                print('开启品牌水印')
            elif front_kid_parametrize_info == 'logo_off':
                # self.setting.on_off_logo()
                print('关闭品牌水印')
            elif front_kid_parametrize_info == 'position_logo_on':
                self.setting.on_off_position_logo()
                print('开启地理位置水印')
            elif front_kid_parametrize_info == 'position_logo_off':
                # self.setting.on_off_position_logo()
                print('关闭地理位置水印')
            elif front_kid_parametrize_info == 'time_logo_on':
                self.setting.on_off_time_logo()
                print('开启时间水印')
            elif front_kid_parametrize_info == 'time_logo_off':
                # self.setting.on_off_time_logo()
                print('关闭时间水印')

            elif front_kid_parametrize_info == 'photo_size_8m_18_9':
                self.setting.photo_size_8m_18_9()
                print('照片大小8M（18:9）')
            elif front_kid_parametrize_info == 'photo_size_2m_16_9':
                self.setting.photo_size_2m_16_9()
                print('照片大小2M（18:9）')
            elif front_kid_parametrize_info == 'photo_size_2m_4_3':
                self.setting.photo_size_2m_4_3()
                print('照片大小2M（4:3）')
            elif front_kid_parametrize_info == 'photo_size_8m_4_3':
                self.setting.photo_size_8m_4_3()
                print('照片大小8M（4:3）')
            elif front_kid_parametrize_info == 'loc_info_on':
                self.setting.save_location_information()
                print('开启保存位置信息')
            elif front_kid_parametrize_info == 'loc_info_off':
                # if state == 'T':
                #     self.setting.save_location_information()
                print('关闭保存位置信息')

            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置儿童拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置儿童音量键拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置儿童触屏拍照功能：')
            # time.sleep(2)

            # 后置延时拍照3s
            # 延时3s
            self.main_setting.timer_3()
            main_page.click_photo(self.base_obj)
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置儿童3s功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置儿童音量键3s功能：')

            self.setting.touch_screen()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置儿童触屏3s拍照功能：')
            # time.sleep(2)

            # 后置延时10s
            # 延时10s
            self.main_setting.timer_10()
            main_page.click_photo(self.base_obj)
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置儿童10s拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置儿童音量键10s拍照功能：')

            self.setting.touch_screen()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置儿童触屏10s拍照功能：')
            # time.sleep(2)

            # 关闭延时
            self.main_setting.off_timer()


            main_page.kid_baby(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置儿童婴儿功能：')

            main_page.kid_bell(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置儿童铃铛功能：')

            main_page.kid_cat(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置儿童猫咪功能：')

            main_page.kid_dog(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置儿童小狗功能：')

            main_page.kid_drum(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置儿童大鼓功能：')

            # 一遍功能正常运行完成 状态为T
            state = 'T'
            print(state)
        except:
            # global state
            state = 'F'
            print('后置儿童拍照功能：', state)

    # 后置模特模式 520
    @pytest.mark.parametrize("parametrize_info", parametrize_info)
    def test_6_model_pattern(self, parametrize_info):
        # 进模特模式
        main_page.model_pattern(self.base_obj)

        global state
        try:
            # 开关
            if parametrize_info == 'face_recognition_off':
                self.setting.ace_recognition()
                print('关闭人脸识别')
            elif parametrize_info == 'face_recognition_on':
                # print(state)
                # if state == 'F':
                #     self.setting.ace_recognition()
                print('开启人脸识别')
            elif parametrize_info == 'grid_lines_on':
                self.setting.Grid_lines()
                print('开启网格线')
            elif parametrize_info == 'grid_lines_off':
                # if state == 'T':
                #     self.setting.Grid_lines()
                print('关闭网格线')
            elif parametrize_info == 'time_delay_off':
                self.setting.time_delay()
                print('关闭零延时')
            elif parametrize_info == 'time_delay_on':
                # self.setting.time_delay()
                print('开启零延时')
            elif parametrize_info == 'shutter_sound_off':
                self.setting.shutter_sound()
                print('关闭快门声音')
            elif parametrize_info == 'shutter_sound_on':
                # if state == 'T':
                #     self.setting.shutter_sound()
                print('开启快门声音')
            elif parametrize_info == 'avodi_flashing_auto':
                self.setting.avodi_flashing_auto()
                print('避免闪烁自动')
            elif parametrize_info == 'avodi_flashing_off':
                self.setting.avodi_flashing_off()
                print('避免闪烁关闭')
            elif parametrize_info == 'avodi_flashing_60hz':
                self.setting.avodi_flashing_60hz()
                print('避免闪烁60hz')
            elif parametrize_info == 'avodi_flashing_50hz':
                self.setting.avodi_flashing_50hz()
                print('避免闪烁50hz')
            elif parametrize_info == 'Focus_sound_off':
                self.setting.Focus_sound()
                print('关闭对焦声音')
            elif parametrize_info == 'Focus_sound_on':
                # if state == 'T':
                #     self.setting.Focus_sound()
                print('开启对焦声音')

            elif parametrize_info == 'logo_on':
                self.setting.on_off_logo()
                print('开启品牌水印')
            elif parametrize_info == 'logo_off':
                # self.setting.on_off_logo()
                print('关闭品牌水印')
            elif parametrize_info == 'position_logo_on':
                self.setting.on_off_position_logo()
                print('开启地理位置水印')
            elif parametrize_info == 'position_logo_off':
                # self.setting.on_off_position_logo()
                print('关闭地理位置水印')
            elif parametrize_info == 'time_logo_on':
                self.setting.on_off_time_logo()
                print('开启时间水印')
            elif parametrize_info == 'time_logo_off':
                # self.setting.on_off_time_logo()
                print('关闭时间水印')

            elif parametrize_info == 'photo_size_16m_4_3':
                self.setting.photo_size_16m_4_3()
                print('照片大小16M（4:3）')
            elif parametrize_info == 'photo_size_16m_18_9':
                self.setting.photo_size_16m_18_9()
                print('照片大小16M（18:9）')
            elif parametrize_info == 'photo_size_8m_18_9':
                self.setting.photo_size_8m_18_9()
                print('照片大小8M（18:9）')
            elif parametrize_info == 'photo_size_8m_4_3':
                self.setting.photo_size_8m_4_3()
                print('照片大小8M（4:3）')
            elif parametrize_info == 'loc_info_on':
                self.setting.save_location_information()
                print('开启保存位置信息')
            elif parametrize_info == 'loc_info_off':
                # if state == 'T':
                #     self.setting.save_location_information()
                print('关闭保存位置信息')

            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置模特男生拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置模特男生音量键拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置模特男生触屏拍照功能：')
            # time.sleep(2)

            # 后置延时拍照3s
            # 延时3s
            self.main_setting.timer_3()
            main_page.click_photo(self.base_obj)
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置模特男生3s功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置模特男生音量键3s功能：')

            self.setting.touch_screen()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置模特男生触屏3s拍照功能：')
            # time.sleep(2)

            # 后置延时10s
            # 延时10s
            self.main_setting.timer_10()
            main_page.click_photo(self.base_obj)
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置模特男生10s拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置模特男生音量键10s拍照功能：')

            self.setting.touch_screen()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置模特男生触屏10s拍照功能：')
            # time.sleep(2)

            # 关闭延时
            self.main_setting.off_timer()

            # 关闭闪光灯
            self.main_setting.off_flash()
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置模特男生关闭闪光灯拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置模特男生音量键关闭闪光灯拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置模特男生触屏关闭闪光灯拍照功能：')
            # time.sleep(2)
            #
            # 开启闪光灯
            self.main_setting.on_flash()
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置模特男生开启闪光灯拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置模特男生音量键开启闪光灯拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置模特男生触屏开启闪光灯拍照功能：')
            # time.sleep(2)

            # 回到闪光灯初始状态 自动
            self.main_setting.auto_flash()

            # 开启HDR
            self.main_setting.on_off_hdr()
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置模特男生开启HDR拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置模特男生音量键开启HDR拍照功能：')  #

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置模特男生触屏开启HDR拍照功能：')
            # time.sleep(2)
            # 回到HDR初始状态
            self.main_setting.on_off_hdr()

            # # 男生模式第二个模特
            # main_page.next_model(self.base_obj)
            # main_page.click_photo(self.base_obj)
            # self.photo.get_new_photo_sum(test_case_name='后置模特男生2拍照功能：')
            #
            # # 男生模式第三个模特
            # main_page.next_model(self.base_obj)
            # main_page.next_model(self.base_obj)
            # main_page.click_photo(self.base_obj)
            # self.photo.get_new_photo_sum(test_case_name='后置模特男生3拍照功能：')

            # 点击女生模式 拍照
            main_page.model_girl(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置模特女生拍照功能：')

            # 点击多人模式 拍照
            main_page.model_many_people(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置模特多人拍照功能：')

            # 一遍功能正常运行完成 状态为T
            state = 'T'
            print(state)
        except:
            # global state
            state = 'F'
            print('后置模特拍照功能：', state)

    # 后置水印模式 460
    @pytest.mark.parametrize("watermark_parametrize_info", watermark_parametrize_info)
    def test_6_watermark(self, watermark_parametrize_info):

        # 进入水印模式
        main_page.watermark(self.base_obj)

        global state
        try:
            # 开关
            if watermark_parametrize_info == 'face_recognition_off':
                self.setting.ace_recognition()
                print('关闭人脸识别')
            elif watermark_parametrize_info == 'face_recognition_on':
                # print(state)
                # if state == 'F':
                #     self.setting.ace_recognition()
                print('开启人脸识别')
            elif watermark_parametrize_info == 'grid_lines_on':
                self.setting.Grid_lines()
                print('开启网格线')
            elif watermark_parametrize_info == 'grid_lines_off':
                # if state == 'T':
                #     self.setting.Grid_lines()
                print('关闭网格线')
            elif watermark_parametrize_info == 'time_delay_off':
                self.setting.time_delay()
                print('关闭零延时')
            elif watermark_parametrize_info == 'time_delay_on':
                # self.setting.time_delay()
                print('开启零延时')
            elif watermark_parametrize_info == 'shutter_sound_off':
                self.setting.shutter_sound()
                print('关闭快门声音')
            elif watermark_parametrize_info == 'shutter_sound_on':
                # if state == 'T':
                #     self.setting.shutter_sound()
                print('开启快门声音')
            elif watermark_parametrize_info == 'avodi_flashing_auto':
                self.setting.avodi_flashing_auto()
                print('避免闪烁自动')
            elif watermark_parametrize_info == 'avodi_flashing_off':
                self.setting.avodi_flashing_off()
                print('避免闪烁关闭')
            elif watermark_parametrize_info == 'avodi_flashing_60hz':
                self.setting.avodi_flashing_60hz()
                print('避免闪烁60hz')
            elif watermark_parametrize_info == 'avodi_flashing_50hz':
                self.setting.avodi_flashing_50hz()
                print('避免闪烁50hz')
            elif watermark_parametrize_info == 'Focus_sound_off':
                self.setting.Focus_sound()
                print('关闭对焦声音')
            elif watermark_parametrize_info == 'Focus_sound_on':
                # if state == 'T':
                #     self.setting.Focus_sound()
                print('开启对焦声音')

            elif watermark_parametrize_info == 'logo_on':
                self.setting.on_off_logo()
                print('开启品牌水印')
            elif watermark_parametrize_info == 'logo_off':
                # self.setting.on_off_logo()
                print('关闭品牌水印')
            elif watermark_parametrize_info == 'position_logo_on':
                self.setting.on_off_position_logo()
                print('开启地理位置水印')
            elif watermark_parametrize_info == 'position_logo_off':
                # self.setting.on_off_position_logo()
                print('关闭地理位置水印')

            elif watermark_parametrize_info == 'loc_info_on':
                self.setting.less_save_location_information()
                print('开启保存位置信息')
            elif watermark_parametrize_info == 'loc_info_off':
                # if state == 'T':
                #     self.setting.save_location_information()
                print('关闭保存位置信息')

            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置水印旅行拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置水印旅行音量键拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置水印旅行触屏拍照功能：')
            # time.sleep(2)

            # 后置延时拍照3s
            # 延时3s
            self.main_setting.timer_3()
            main_page.click_photo(self.base_obj)
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置水印旅行3s功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置水印旅行音量键3s功能：')

            self.setting.touch_screen()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置水印旅行触屏3s拍照功能：')
            # time.sleep(2)

            # 后置延时10s
            # 延时10s
            self.main_setting.timer_10()
            main_page.click_photo(self.base_obj)
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置水印旅行10s拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置水印旅行10s音量键拍照功能：')

            self.setting.touch_screen()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置水印旅行10s触屏拍照功能：')
            # time.sleep(2)

            # 关闭延时
            self.main_setting.off_timer()

            # 关闭闪光灯
            self.main_setting.off_flash()
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置水印旅行关闭闪光灯拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置水印旅行音量键关闭闪光灯拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置水印旅行触屏关闭闪光灯拍照功能：')
            # time.sleep(2)
            #
            # 开启闪光灯
            self.main_setting.on_flash()
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置水印旅行开启闪光灯拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置水印旅行开启闪光灯音量键拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置水印旅行开启闪光灯触屏拍照功能：')
            # time.sleep(2)

            # 回到闪光灯初始状态 自动
            self.main_setting.auto_flash()

            # 开启HDR
            self.main_setting.on_off_hdr()
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置水印旅行开启HDR拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置水印旅行音量键开启HDR拍照功能：')  #

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置水印旅行触屏开启HDR拍照功能：')
            # time.sleep(2)
            # 回到HDR初始状态
            self.main_setting.on_off_hdr()

            # 水印 美食
            main_page.watermark_cate(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置水印美食拍照功能：')

            # 水印 潮语
            main_page.watermark_tide_language(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置水印潮语拍照功能：')

            # 水印 情意
            main_page.watermark_affective(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置水印情意拍照功能：')

            # 水印 自拍
            main_page.watermark_selfie(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置水印自拍拍照功能：')

            # # 水印 心情
            # main_page.watermark_mood(self.base_obj)
            # self.photo.get_new_photo_sum(test_case_name='后置水印心情拍照功能：')

            # 一遍功能正常运行完成 状态为T
            state = 'T'
            print(state)

        except:
            # global state
            state = 'F'
            print('后置水印拍照功能：', state)

    # 前置水印模式 252
    @pytest.mark.parametrize("front_watermark_parametrize_info", front_watermark_parametrize_info)
    def test_6_watermark_facing(self, front_watermark_parametrize_info):

        # 进入水印模式
        main_page.watermark(self.base_obj)
        # 转换前置摄像头
        main_page.onoff_front_facing(self.base_obj)

        global state
        try:
            # 开关
            if front_watermark_parametrize_info == 'face_recognition_off':
                self.setting.ace_recognition()
                print('关闭人脸识别')
            elif front_watermark_parametrize_info == 'face_recognition_on':
                # print(state)
                # if state == 'F':
                #     self.setting.ace_recognition()
                print('开启人脸识别')
            elif front_watermark_parametrize_info == 'grid_lines_on':
                self.setting.Grid_lines()
                print('开启网格线')
            elif front_watermark_parametrize_info == 'grid_lines_off':
                # if state == 'T':
                #     self.setting.Grid_lines()
                print('关闭网格线')
            elif front_watermark_parametrize_info == 'time_delay_off':
                self.setting.time_delay()
                print('关闭零延时')
            elif front_watermark_parametrize_info == 'time_delay_on':
                # self.setting.time_delay()
                print('开启零延时')
            elif front_watermark_parametrize_info == 'shutter_sound_off':
                self.setting.shutter_sound()
                print('关闭快门声音')
            elif front_watermark_parametrize_info == 'shutter_sound_on':
                # if state == 'T':
                #     self.setting.shutter_sound()
                print('开启快门声音')
            elif front_watermark_parametrize_info == 'avodi_flashing_auto':
                self.setting.avodi_flashing_auto()
                print('避免闪烁自动')
            elif front_watermark_parametrize_info == 'avodi_flashing_off':
                self.setting.avodi_flashing_off()
                print('避免闪烁关闭')
            elif front_watermark_parametrize_info == 'avodi_flashing_60hz':
                self.setting.avodi_flashing_60hz()
                print('避免闪烁60hz')
            elif front_watermark_parametrize_info == 'avodi_flashing_50hz':
                self.setting.avodi_flashing_50hz()
                print('避免闪烁50hz')

            elif front_watermark_parametrize_info == 'logo_on':
                self.setting.on_off_logo()
                print('开启品牌水印')
            elif front_watermark_parametrize_info == 'logo_off':
                # self.setting.on_off_logo()
                print('关闭品牌水印')
            elif front_watermark_parametrize_info == 'position_logo_on':
                self.setting.on_off_position_logo()
                print('开启地理位置水印')
            elif front_watermark_parametrize_info == 'position_logo_off':
                # self.setting.on_off_position_logo()
                print('关闭地理位置水印')

            elif front_watermark_parametrize_info == 'loc_info_on':
                self.setting.less_save_location_information()
                print('开启保存位置信息')
            elif front_watermark_parametrize_info == 'loc_info_off':
                # if state == 'T':
                #     self.setting.save_location_information()
                print('关闭保存位置信息')


            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置水印旅行拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置水印旅行音量键拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置水印旅行触屏拍照功能：')
            # time.sleep(2)

            # 后置延时拍照3s
            # 延时3s
            self.main_setting.timer_3()
            main_page.click_photo(self.base_obj)
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置水印旅行3s功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置水印旅行音量键3s功能：')

            self.setting.touch_screen()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置水印旅行触屏3s拍照功能：')
            # time.sleep(2)

            # 后置延时10s
            # 延时10s
            self.main_setting.timer_10()
            main_page.click_photo(self.base_obj)
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置水印旅行10s拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置水印旅行10s音量键拍照功能：')

            self.setting.touch_screen()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置水印旅行10s触屏拍照功能：')
            # time.sleep(2)

            # 关闭延时
            self.main_setting.off_timer()

            # 水印 美食
            main_page.watermark_cate(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置水印美食拍照功能：')

            # 水印 潮语
            main_page.watermark_tide_language(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置水印潮语拍照功能：')

            # 水印 情意
            main_page.watermark_affective(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置水印情意拍照功能：')

            # 水印 自拍
            main_page.watermark_selfie(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置水印自拍拍照功能：')

            # # 水印 心情
            # main_page.watermark_mood(self.base_obj)
            # self.photo.get_new_photo_sum(test_case_name='前置水印心情拍照功能：')

            # 一遍功能正常运行完成 状态为T
            state = 'T'
            print(state)

        except:
            # global state
            state = 'F'
            print('前置水印拍照功能：', state)

    # 后置脸萌模式 726
    @pytest.mark.parametrize("myotee_parametrize_info", portrait_parametrize_info)
    def test_6_myotee(self, myotee_parametrize_info):

        # 进入脸萌模式
        main_page.myteeo(self.base_obj)

        global state
        try:
            # 开关
            if myotee_parametrize_info == 'face_recognition_off':
                self.setting.ace_recognition()
                print('关闭人脸识别')
            elif myotee_parametrize_info == 'face_recognition_on':
                # print(state)
                # if state == 'F':
                #     self.setting.ace_recognition()
                print('开启人脸识别')
            elif myotee_parametrize_info == 'grid_lines_on':
                self.setting.Grid_lines()
                print('开启网格线')
            elif myotee_parametrize_info == 'grid_lines_off':
                # if state == 'T':
                #     self.setting.Grid_lines()
                print('关闭网格线')
            elif myotee_parametrize_info == 'time_delay_off':
                self.setting.time_delay()
                print('关闭零延时')
            elif myotee_parametrize_info == 'time_delay_on':
                # self.setting.time_delay()
                print('开启零延时')
            elif myotee_parametrize_info == 'shutter_sound_off':
                self.setting.shutter_sound()
                print('关闭快门声音')
            elif myotee_parametrize_info == 'shutter_sound_on':
                # if state == 'T':
                #     self.setting.shutter_sound()
                print('开启快门声音')
            elif myotee_parametrize_info == 'avodi_flashing_auto':
                self.setting.avodi_flashing_auto()
                print('避免闪烁自动')
            elif myotee_parametrize_info == 'avodi_flashing_off':
                self.setting.avodi_flashing_off()
                print('避免闪烁关闭')
            elif myotee_parametrize_info == 'avodi_flashing_60hz':
                self.setting.avodi_flashing_60hz()
                print('避免闪烁60hz')
            elif myotee_parametrize_info == 'avodi_flashing_50hz':
                self.setting.avodi_flashing_50hz()
                print('避免闪烁50hz')
            elif myotee_parametrize_info == 'Focus_sound_off':
                self.setting.Focus_sound()
                print('关闭对焦声音')
            elif myotee_parametrize_info == 'Focus_sound_on':
                # if state == 'T':
                #     self.setting.Focus_sound()
                print('开启对焦声音')

            elif myotee_parametrize_info == 'logo_on':
                self.setting.on_off_logo()
                print('开启品牌水印')
            elif myotee_parametrize_info == 'logo_off':
                # self.setting.on_off_logo()
                print('关闭品牌水印')
            elif myotee_parametrize_info == 'position_logo_on':
                self.setting.on_off_position_logo()
                print('开启地理位置水印')
            elif myotee_parametrize_info == 'position_logo_off':
                # self.setting.on_off_position_logo()
                print('关闭地理位置水印')
            elif myotee_parametrize_info == 'time_logo_on':
                self.setting.on_off_time_logo()
                print('开启时间水印')
            elif myotee_parametrize_info == 'time_logo_off':
                # self.setting.on_off_time_logo()
                print('关闭时间水印')

            elif myotee_parametrize_info == 'loc_info_on':
                self.setting.save_location_information()
                print('开启保存位置信息')
            elif myotee_parametrize_info == 'loc_info_off':
                # if state == 'T':
                #     self.setting.save_location_information()
                print('关闭保存位置信息')

            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰1拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰1音量键拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰1触屏拍照功能：')
            # time.sleep(2)

            # 后置延时拍照3s
            # 延时3s
            self.main_setting.timer_3()
            main_page.click_photo(self.base_obj)
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰1拍照3s功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰1音量键3s功能：')

            self.setting.touch_screen()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰1触屏3s拍照功能：')
            # time.sleep(2)

            # 后置延时10s
            # 延时10s
            self.main_setting.timer_10()
            main_page.click_photo(self.base_obj)
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰1_10s拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰1_10s音量键拍照功能：')

            self.setting.touch_screen()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰1_10s触屏拍照功能：')
            # time.sleep(2)

            # 关闭延时
            self.main_setting.off_timer()

            # 关闭闪光灯
            self.main_setting.off_flash()
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰1关闭闪光灯拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰1音量键关闭闪光灯拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰1触屏关闭闪光灯拍照功能：')
            # time.sleep(2)
            #
            # 开启闪光灯
            self.main_setting.on_flash()
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰1开启闪光灯拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰1开启闪光灯音量键拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰1开启闪光灯触屏拍照功能：')
            # time.sleep(2)

            # 回到闪光灯初始状态 自动
            self.main_setting.auto_flash()

            # 开启HDR
            self.main_setting.on_off_hdr()
            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰1开启HDR拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰1音量键开启HDR拍照功能：')  #

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰1触屏开启HDR拍照功能：')
            # time.sleep(2)
            # 回到HDR初始状态
            self.main_setting.on_off_hdr()

            # 脸萌装饰2
            main_page.decoration_2(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰2拍照功能：')
            # 脸萌装饰3
            main_page.decoration_3(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰3拍照功能：')
            # 脸萌装饰4
            main_page.decoration_4(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌装饰4拍照功能：')

            # 脸萌趣味
            main_page.delight_1(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌趣味1拍照功能：')

            main_page.delight_2(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌趣味2拍照功能：')

            main_page.delight_3(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌趣味3拍照功能：')

            main_page.delight_4(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌趣味4拍照功能：')

            # 脸萌卡通
            main_page.cartoon_1(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌卡通1拍照功能：')

            main_page.cartoon_2(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌卡通2拍照功能：')

            main_page.cartoon_3(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌卡通3拍照功能：')

            main_page.cartoon_4(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌卡通4拍照功能：')

            # 脸萌表情
            main_page.expression_1(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌表情1拍照功能：')

            main_page.expression_2(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌表情2拍照功能：')

            main_page.expression_3(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌表情3拍照功能：')

            main_page.expression_4(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='后置脸萌表情4拍照功能：')

        except:
            # global state
            state = 'F'
            print('后置脸萌拍照功能：', state)

    # 前置脸萌模式 480
    @pytest.mark.parametrize("front_myotee_parametrize_info", front_portrait_parametrize_info)
    def test_6_myotee_facing(self, front_myotee_parametrize_info):

        # 进入脸萌模式
        main_page.myteeo(self.base_obj)
        # 切换至前置摄像头
        main_page.onoff_front_facing(self.base_obj)

        global state
        try:
            # 开关
            if front_myotee_parametrize_info == 'face_recognition_off':
                self.setting.ace_recognition()
                print('关闭人脸识别')
            elif front_myotee_parametrize_info == 'face_recognition_on':
                # print(state)
                # if state == 'F':
                #     self.setting.ace_recognition()
                print('开启人脸识别')
            elif front_myotee_parametrize_info == 'grid_lines_on':
                self.setting.Grid_lines()
                print('开启网格线')
            elif front_myotee_parametrize_info == 'grid_lines_off':
                # if state == 'T':
                #     self.setting.Grid_lines()
                print('关闭网格线')
            elif front_myotee_parametrize_info == 'time_delay_off':
                self.setting.time_delay()
                print('关闭零延时')
            elif front_myotee_parametrize_info == 'time_delay_on':
                # self.setting.time_delay()
                print('开启零延时')
            elif front_myotee_parametrize_info == 'shutter_sound_off':
                self.setting.shutter_sound()
                print('关闭快门声音')
            elif front_myotee_parametrize_info == 'shutter_sound_on':
                # if state == 'T':
                #     self.setting.shutter_sound()
                print('开启快门声音')
            elif front_myotee_parametrize_info == 'avodi_flashing_auto':
                self.setting.avodi_flashing_auto()
                print('避免闪烁自动')
            elif front_myotee_parametrize_info == 'avodi_flashing_off':
                self.setting.avodi_flashing_off()
                print('避免闪烁关闭')
            elif front_myotee_parametrize_info == 'avodi_flashing_60hz':
                self.setting.avodi_flashing_60hz()
                print('避免闪烁60hz')
            elif front_myotee_parametrize_info == 'avodi_flashing_50hz':
                self.setting.avodi_flashing_50hz()
                print('避免闪烁50hz')

            elif front_myotee_parametrize_info == 'logo_on':
                self.setting.on_off_logo()
                print('开启品牌水印')
            elif front_myotee_parametrize_info == 'logo_off':
                # self.setting.on_off_logo()
                print('关闭品牌水印')
            elif front_myotee_parametrize_info == 'position_logo_on':
                self.setting.on_off_position_logo()
                print('开启地理位置水印')
            elif front_myotee_parametrize_info == 'position_logo_off':
                # self.setting.on_off_position_logo()
                print('关闭地理位置水印')
            elif front_myotee_parametrize_info == 'time_logo_on':
                self.setting.on_off_time_logo()
                print('开启时间水印')
            elif front_myotee_parametrize_info == 'time_logo_off':
                # self.setting.on_off_time_logo()
                print('关闭时间水印')

            elif front_myotee_parametrize_info == 'loc_info_on':
                self.setting.save_location_information()
                print('开启保存位置信息')
            elif front_myotee_parametrize_info == 'loc_info_off':
                # if state == 'T':
                #     self.setting.save_location_information()
                print('关闭保存位置信息')

            main_page.click_photo(self.base_obj)
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌装饰1拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌装饰1音量键拍照功能：')

            self.setting.touch_screen()
            # time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌装饰1触屏拍照功能：')
            # time.sleep(2)

            # 后置延时拍照3s
            # 延时3s
            self.main_setting.timer_3()
            main_page.click_photo(self.base_obj)
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌装饰1拍照3s功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌装饰1音量键3s功能：')

            self.setting.touch_screen()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌装饰1触屏3s拍照功能：')
            # time.sleep(2)

            # 后置延时10s
            # 延时10s
            self.main_setting.timer_10()
            main_page.click_photo(self.base_obj)
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌装饰1_10s拍照功能：')

            # time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌装饰1_10s音量键拍照功能：')

            self.setting.touch_screen()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌装饰1_10s触屏拍照功能：')
            # time.sleep(2)

            # 关闭延时
            self.main_setting.off_timer()

            # 脸萌装饰2
            main_page.decoration_2(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌装饰2拍照功能：')
            # 脸萌装饰3
            main_page.decoration_3(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌装饰3拍照功能：')
            # 脸萌装饰4
            main_page.decoration_4(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌装饰4拍照功能：')

            # 脸萌趣味
            main_page.delight_1(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌趣味1拍照功能：')

            main_page.delight_2(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌趣味2拍照功能：')

            main_page.delight_3(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌趣味3拍照功能：')

            main_page.delight_4(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌趣味4拍照功能：')

            # 脸萌卡通
            main_page.cartoon_1(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌卡通1拍照功能：')

            main_page.cartoon_2(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌卡通2拍照功能：')

            main_page.cartoon_3(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌卡通3拍照功能：')

            main_page.cartoon_4(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌卡通4拍照功能：')

            # 脸萌表情
            main_page.expression_1(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌表情1拍照功能：')

            main_page.expression_2(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌表情2拍照功能：')

            main_page.expression_3(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌表情3拍照功能：')

            main_page.expression_4(self.base_obj)
            self.photo.get_new_photo_sum(test_case_name='前置脸萌表情4拍照功能：')

        except:
            # global state
            state = 'F'
            print('前置脸萌拍照功能：', state)


if __name__ == '__main__':
    # state = 'T'
    pytest.main(['-s', '-r', 'testcase_only2.py'])
    # for i in range(10000):
    #     try:
    #         pytest.main(['-s', '-x', 'testcase_notscreenshot.py'])
    #     except:
    #         # globals()
    #         print('error')
    #         time.sleep(300)
