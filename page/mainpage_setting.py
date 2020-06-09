"""
设置界面基本功能
"""
import time


class Main_Setting:
    # 主页上方的设置按钮
    # 设置按钮
    mode_id = 'com.freeme.camera:id/mode'
    # 延时拍照按钮
    timer_icon_id = 'com.freeme.camera:id/self_timer_icon'
    # 闪光灯按钮
    flash_icon_id = 'com.freeme.camera:id/flash_icon'
    # hdr
    hdr_icon_id = 'com.freeme.camera:id/hdr_icon'

    # 延时拍照3s
    timer_3_id = 'com.freeme.camera:id/self_timer_3'
    # 延时拍照10
    timer_10_id = 'com.freeme.camera:id/self_timer_10'
    # 关闭延时
    timer_off_id = 'com.freeme.camera:id/self_timer_off'

    # 关闭闪光灯
    flash_off_id = 'com.freeme.camera:id/flash_off'
    # 闪光灯自动
    flash_auto_id = 'com.freeme.camera:id/flash_auto'
    # 开启闪光灯
    flash_on_id = 'com.freeme.camera:id/flash_on'

    def __init__(self, base_obj):
        self.base_obj = base_obj

    # 延时3s拍照功能
    def timer_3(self):
        # 点击延时拍照功能
        time.sleep(2)
        self.base_obj.find_ID(self.timer_icon_id).click()
        self.base_obj.find_ID(self.timer_3_id).click()
        # time.sleep(2)
        # time.sleep(15)

    # 延时10拍照功能
    def timer_10(self):
        # 点击延时拍照功能
        time.sleep(2)
        self.base_obj.find_ID(self.timer_icon_id).click()

        self.base_obj.find_ID(self.timer_10_id).click()

    # 关闭延时拍照
    def off_timer(self):
        # 点击延时拍照功能
        time.sleep(2)
        self.base_obj.find_ID(self.timer_icon_id).click()
        # 点击关闭延时拍照按钮
        self.base_obj.find_ID(self.timer_off_id).click()

    # 闪光灯功能
    # 关闭闪光灯
    def off_flash(self):
        # 点击闪光灯功能
        time.sleep(2)
        self.base_obj.find_ID(self.flash_icon_id).click()
        # 点击关闭闪光灯
        self.base_obj.find_ID(self.flash_off_id).click()

    # 开启闪光灯
    def on_flash(self):
        # 点击闪光灯功能
        time.sleep(2)
        self.base_obj.find_ID(self.flash_icon_id).click()
        # 点击开启闪光灯
        self.base_obj.find_ID(self.flash_on_id).click()

    # 开启闪光灯自动
    def auto_flash(self):
        # 点击闪光灯功能
        time.sleep(2)
        self.base_obj.find_ID(self.flash_icon_id).click()
        # 点击闪光灯自动
        self.base_obj.find_ID(self.flash_auto_id).click()

    # 开启关闭hdr功能
    def on_off_hdr(self):
        time.sleep(2)
        # 点击HDR开关
        self.base_obj.find_ID(self.hdr_icon_id).click()
