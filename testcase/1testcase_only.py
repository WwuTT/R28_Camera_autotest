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
1816
"""


class Test_Func():
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
        # 隐式等待
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
        print('driver退出')
        self.driver.quit()
        time.sleep(10)
        # print('driver退出')
        print('')

    # 相机首页拍照 360
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
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置拍照功能：', loc_info=parametrize_info[2])

            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置音量键拍照功能：')

            self.setting.touch_screen()
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置触屏拍照功能：')
            time.sleep(2)

            # 后置延时拍照3s
            # 延时3s
            self.main_setting.timer_3()
            main_page.click_photo(self.base_obj)
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置3s功能：')

            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置音量键3s功能：')

            self.setting.touch_screen()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置触屏3s拍照功能：')
            time.sleep(2)

            # 后置延时10s
            # 延时10s
            self.main_setting.timer_10()
            main_page.click_photo(self.base_obj)
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置10s拍照功能：')

            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置音量键10s拍照功能：')

            self.setting.touch_screen()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置触屏10s拍照功能：')
            time.sleep(2)

            # 关闭延时
            self.main_setting.off_timer()

            # 关闭闪光灯
            self.main_setting.off_flash()
            main_page.click_photo(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置关闭闪光灯拍照功能：')

            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置音量键关闭闪光灯拍照功能：')

            self.setting.touch_screen()
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置触屏关闭闪光灯拍照功能：')
            time.sleep(2)

            # 开启闪光灯
            self.main_setting.on_flash()
            main_page.click_photo(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置开启闪光灯拍照功能：')

            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置音量键开启闪光灯拍照功能：')  # !

            self.setting.touch_screen()
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置触屏开启闪光灯拍照功能：')
            time.sleep(2)

            # 回到闪光灯初始状态 自动
            self.main_setting.auto_flash()

            # 开启HDR
            self.main_setting.on_off_hdr()
            main_page.click_photo(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置开启HDR拍照功能：')

            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置音量键开启HDR拍照功能：')  #

            self.setting.touch_screen()
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置触屏开启HDR拍照功能：')
            time.sleep(2)
            # 回到HDR初始状态
            self.main_setting.on_off_hdr()

            # 一遍功能正常运行完成 状态为T
            state = 'T'
            print(state)
        except:
            # global state
            state = 'F'
            print('后置拍照功能：', state)

    # 前置拍照功能 198
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
            # elif front_parametrize_info == 'selfie_mirror_on':
            #     self.setting.on_off_selfie_mirror()
            #     print('开启自拍镜像')
            # elif front_parametrize_info == 'selfie_mirror_off':
            #     # if state == 'T':
            #     #     self.setting.on_off_selfie_mirror()
            #     print('关闭自拍镜像')
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
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置拍照功能：')

            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置音量键拍照功能：')

            self.setting.touch_screen()
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置触屏拍照功能：')
            time.sleep(2)

            # 延时拍照功能
            # 延时3s
            self.main_setting.timer_3()

            main_page.click_photo(self.base_obj)
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置延时拍照3s功能：')

            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置音量键拍照3s功能：')

            self.setting.touch_screen()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置触屏拍照3s功能：')
            time.sleep(2)

            # 延时10s
            self.main_setting.timer_10()

            main_page.click_photo(self.base_obj)
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置延时拍照10s功能：')

            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置音量键拍照10s功能：')

            self.setting.touch_screen()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置触屏拍照10s功能：')
            time.sleep(2)

            # 关闭延时
            self.main_setting.off_timer()

            # 一遍功能正常运行完成 状态为T
            state = 'T'
        except:
            # global state
            state = 'F'
            print('前置拍照功能：', state)

    # 美颜拍照 440
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
            time.sleep(2)
            # 获取现有照片数量
            self.photo.get_new_photo_sum(test_case_name='后置美颜功能：')

            # 点击音量键拍照
            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='音量键后置美颜功能：')

            self.setting.touch_screen()
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置美颜触屏拍照功能：')
            time.sleep(2)

            # 延时3s
            self.main_setting.timer_3()

            main_page.click_photo(self.base_obj)
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置美颜3s功能：')

            # 点击音量键拍照
            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='音量键后置美颜3s功能：')

            # 触屏拍照
            self.setting.touch_screen()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置美颜触屏3s美颜功能：')
            time.sleep(2)

            # 延时10s
            self.main_setting.timer_10()

            main_page.click_photo(self.base_obj)
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置美颜10s功能：')

            # 点击音量键拍照
            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='音量键后置美颜10s功能：')

            # 触屏拍照
            self.setting.touch_screen()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置美颜触屏10s美颜功能：')
            time.sleep(2)

            # 关闭延时
            self.main_setting.off_timer()

            # 关闭闪光灯
            self.main_setting.off_flash()
            main_page.click_photo(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置关闭闪光灯美颜功能：')

            # 点击音量键拍照
            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置音量键关闭闪光灯美颜功能：')

            # 触屏拍照
            self.setting.touch_screen()
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置触屏关闭闪光灯美颜功能：')
            time.sleep(2)

            # 开启闪光灯
            self.main_setting.on_flash()

            main_page.click_photo(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置开启闪光灯美颜功能：')

            # 点击音量键拍照
            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='音量键后置开启闪光灯美颜功能：')

            # 触屏拍照
            self.setting.touch_screen()
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置美颜触屏开启闪光灯美颜功能：')
            time.sleep(2)

            # 回到闪光灯初始状态 自动
            self.main_setting.auto_flash()

            # HDR功能
            self.main_setting.on_off_hdr()

            main_page.click_photo(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置HDR美颜功能：')

            # 点击音量键拍照
            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='音量键后置HDR美颜功能：')

            # 触屏拍照
            self.setting.touch_screen()
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置触屏HDR美颜功能：')
            time.sleep(2)

            # 回到HDR初始状态
            self.main_setting.on_off_hdr()

            # 美颜内部功能
            # 美颜中的美颜
            # 点击美颜
            main_page.beauty_beauty(self.base_obj)
            main_page.click_photo(self.base_obj)
            time.sleep(2)
            # 获取现有照片数量
            self.photo.get_new_photo_sum(test_case_name='后置美颜功能_美颜：')

            # 点击美肤
            main_page.beauty_skin(self.base_obj)
            main_page.click_photo(self.base_obj)
            time.sleep(2)
            # 获取现有照片数量
            self.photo.get_new_photo_sum(test_case_name='后置美颜功能_美肤：')

            # 点击瘦脸
            main_page.beauty_thin_face(self.base_obj)
            main_page.click_photo(self.base_obj)
            time.sleep(2)
            # 获取现有照片数量
            self.photo.get_new_photo_sum(test_case_name='后置美颜功能_瘦脸：')

            # 点击大眼
            main_page.beauty_big_eyes(self.base_obj)
            main_page.click_photo(self.base_obj)
            time.sleep(2)
            # 获取现有照片数量
            self.photo.get_new_photo_sum(test_case_name='后置美颜功能_大眼：')

            # 一遍功能正常运行完成 状态为T
            state = 'T'
        except:
            # global state
            state = 'F'
            print('后置美颜功能：', state)

    # 美颜前置功能 286
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
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置美颜功能：')

            # 点击音量键拍照
            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置音量键美颜功能：')

            # 触屏拍照
            self.setting.touch_screen()
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置触屏美颜功能：')
            time.sleep(2)

            # 延时3s
            self.main_setting.timer_3()

            main_page.click_photo(self.base_obj)
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置美颜3s功能：')

            # 点击音量键拍照
            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='音量键前置美颜3s功能：')

            # 触屏拍照
            self.setting.touch_screen()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置触屏美颜3s功能：')
            time.sleep(2)

            # 延时10s
            self.main_setting.timer_10()

            main_page.click_photo(self.base_obj)
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置美颜10s功能：')  # !

            # 点击音量键拍照
            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置美颜音量键10s功能：')  # !

            # 触屏拍照
            self.setting.touch_screen()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置触屏美颜10s功能：')
            time.sleep(2)

            # 关闭延时
            self.main_setting.off_timer()

            # 美颜内部功能
            # 美颜中的美颜
            # 点击美颜
            main_page.beauty_beauty(self.base_obj)
            main_page.click_photo(self.base_obj)
            time.sleep(2)
            # 获取现有照片数量
            self.photo.get_new_photo_sum(test_case_name='前置美颜功能_美颜：')

            # 点击美肤
            main_page.beauty_skin(self.base_obj)
            main_page.click_photo(self.base_obj)
            time.sleep(2)
            # 获取现有照片数量
            self.photo.get_new_photo_sum(test_case_name='前置美颜功能_美肤：')

            # 点击瘦脸
            main_page.beauty_thin_face(self.base_obj)
            main_page.click_photo(self.base_obj)
            time.sleep(2)
            # 获取现有照片数量
            self.photo.get_new_photo_sum(test_case_name='前置美颜功能_瘦脸：')

            # 点击大眼
            main_page.beauty_big_eyes(self.base_obj)
            main_page.click_photo(self.base_obj)
            time.sleep(2)
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
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置全景功能：')

            # 点击音量键全景拍照
            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            # 全景拍照确定按钮
            main_page.panorama_click_photo(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='音量键后置全景功能：')

            # 触屏拍照
            self.setting.touch_screen()
            time.sleep(2)
            # 全景拍照确定按钮
            main_page.panorama_click_photo(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置触屏全景功能：')
            time.sleep(2)

            # 一遍功能正常运行完成 状态为T
            state = 'T'
        except:
            # global state
            state = 'F'
            print('后置全景功能：', state)

    # 视频拍摄 104
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
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置视频功能：', modle=2, func ='后置视频' )

            # 关闭闪光灯
            self.main_setting.off_flash()
            main_page.video_in(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置关闭闪光灯视频功能：', modle=2, func ='后置视频')

            # 开启闪光灯
            self.main_setting.on_flash()
            main_page.video_in(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置开启闪光灯视频功能：', modle=2, func ='后置视频')

            # 回到闪光灯初始状态 自动
            self.main_setting.auto_flash()
            # self.main_setting.on_flash()
            main_page.video_in(self.base_obj)
            time.sleep(2)
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
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置视频功能：', func ='前置视频')

            # 一遍功能正常运行完成 状态为T
            state = 'T'
        except:
            # global state
            state = 'F'
            print('前置视频功能：', state)

    # 美视 182
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
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置闪光灯自动美视功能：', modle=2, func ='后置美视')

            # 关闭闪光灯
            self.main_setting.off_flash()
            main_page.video_in(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置关闭闪光灯美视功能：', modle=2, func ='后置美视')

            # 开启闪光灯
            self.main_setting.on_flash()
            main_page.video_in(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置开启闪光灯美视功能：', modle=2, func ='后置美视')

            # 回到闪光灯初始状态 自动
            self.main_setting.auto_flash()

            # 点击美颜
            main_page.beauty_beauty(self.base_obj)
            main_page.video_in(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置美视功能_美颜：', modle=2, func ='后置美视')

            # 点击美肤
            main_page.beauty_skin(self.base_obj)
            main_page.video_in(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置美视功能_美肤：', modle=2, func ='后置美视')

            # 点击瘦脸
            main_page.beauty_thin_face(self.base_obj)
            main_page.video_in(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置美视功能_瘦脸：', modle=2, func ='后置美视')

            # 点击大眼
            main_page.beauty_big_eyes(self.base_obj)
            main_page.video_in(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置美视功能_大眼：', modle=2, func ='后置美视')
            time.sleep(2)

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
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置美视功能：', func ='前置美视')

            # 美颜内部功能
            # 美颜中的美颜
            # 点击美颜
            main_page.beauty_beauty(self.base_obj)
            main_page.front_facing_video_b(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置美视功能_美颜：', func ='前置美视')

            # 点击美肤
            main_page.beauty_skin(self.base_obj)
            main_page.front_facing_video_b(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置美视功能_美肤：', func ='前置美视')

            # 点击瘦脸
            main_page.beauty_thin_face(self.base_obj)
            main_page.front_facing_video_b(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置美视功能_瘦脸：', func ='前置美视')

            # 点击大眼
            main_page.beauty_big_eyes(self.base_obj)
            main_page.front_facing_video_b(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置美视功能_大眼：', func ='前置美视')
            time.sleep(2)

            # 一遍功能正常运行完成 状态为T
            state = 'T'
        except:
            # global state
            state = 'F'
            print('前置美视功能：', state)

    # 后置人像模式
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
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置人像功能：')

            time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置人像音量键拍照功能：')

            self.setting.touch_screen()
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置人像触屏拍照功能：')
            time.sleep(2)

            # 后置延时拍照3s
            # 延时3s
            self.main_setting.timer_3()
            main_page.click_photo(self.base_obj)
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置人像3s功能：')

            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置人像音量键3s功能：')

            self.setting.touch_screen()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='后置人像触屏3s拍照功能：')
            time.sleep(2)

            # 后置延时10s
            # 延时10s
            self.main_setting.timer_10()
            main_page.click_photo(self.base_obj)
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置人像10s拍照功能：')

            time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(40)
            self.photo.get_new_photo_sum(test_case_name='后置人像音量键10s拍照功能：')

            self.setting.touch_screen()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置人像触屏10s拍照功能：')
            time.sleep(2)

            # 关闭延时
            self.main_setting.off_timer()

            # 关闭闪光灯
            self.main_setting.off_flash()
            main_page.click_photo(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置人像关闭闪光灯拍照功能：')

            time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置人像音量键关闭闪光灯拍照功能：')

            self.setting.touch_screen()
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置人像触屏关闭闪光灯拍照功能：')
            time.sleep(2)

            # 开启闪光灯
            self.main_setting.on_flash()
            main_page.click_photo(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置人像开启闪光灯拍照功能：')

            time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置人像音量键开启闪光灯拍照功能：')

            self.setting.touch_screen()
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置人像触屏开启闪光灯拍照功能：')
            time.sleep(2)

            # 回到闪光灯初始状态 自动
            self.main_setting.auto_flash()

            # 开启HDR
            self.main_setting.on_off_hdr()
            main_page.click_photo(self.base_obj)
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置人像开启HDR拍照功能：')

            time.sleep(2)
            self.setting.volume_photos()
            # time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='后置人像音量键开启HDR拍照功能：')

            self.setting.touch_screen()
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='后置人像触屏开启HDR拍照功能：')
            time.sleep(2)
            # 回到HDR初始状态
            self.main_setting.on_off_hdr()

            # 一遍功能正常运行完成 状态为T
            state = 'T'
            print(state)
        except:
            # global state
            state = 'F'
            print('后置人像拍照功能：', state)

    # 前置人像模式
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
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置人像功能：')

            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置人像音量键拍照功能：')

            self.setting.touch_screen()
            time.sleep(2)
            self.photo.get_new_photo_sum(test_case_name='前置人像触屏拍照功能：')
            time.sleep(2)

            # 后置延时拍照3s
            # 延时3s
            self.main_setting.timer_3()
            main_page.click_photo(self.base_obj)
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置人像3s功能：')

            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置人像音量键3s功能：')

            self.setting.touch_screen()
            time.sleep(3)
            self.photo.get_new_photo_sum(test_case_name='前置人像触屏3s拍照功能：')
            time.sleep(2)

            # 后置延时10s
            # 延时10s
            self.main_setting.timer_10()
            main_page.click_photo(self.base_obj)
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置人像10s拍照功能：')

            time.sleep(2)
            self.setting.volume_photos()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置人像音量键10s拍照功能：')

            self.setting.touch_screen()
            time.sleep(10)
            self.photo.get_new_photo_sum(test_case_name='前置人像触屏10s拍照功能：')
            time.sleep(2)

            # 一遍功能正常运行完成 状态为T
            state = 'T'
            print(state)
        except:
            # global state
            state = 'F'
            print('后置人像拍照功能：', state)


if __name__ == '__main__':

    pytest.main(['-s', '-r', '1testcase_only.py'])
    # for i in range(10000):
    #     try:
    #         pytest.main(['-s', '-x', 'testcase_notscreenshot.py'])
    #     except:
    #         # globals()
    #         print('error')
    #         time.sleep(300)
