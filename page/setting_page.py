"""
设置界面
"""
import time

from page import main_page


class Setting:
    # 相机设置功能
    # 设置按钮
    mode_id = 'com.freeme.camera:id/mode'
    # 音量键拍照开关  均为xpath
    on_off_volume_photos_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id' \
                                 '/volumecapture_setting\"]/android.widget.LinearLayout[1]/android.widget.Switch[1]'
    # 触屏拍照开关
    on_off_touch_screen = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id' \
                          '/touchcapture_setting\"]/android.widget.LinearLayout[1]/android.widget.Switch[1]'
    # 人脸识别开关
    on_off_Face_recognition = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id' \
                              '/facedetection_setting\"]/android.widget.LinearLayout[1]/android.widget.Switch[1]'

    # 网格线开关
    on_off_Grid_lines = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id' \
                        '/gridline_setting\"]/android.widget.LinearLayout[1]/android.widget.Switch[1]'

    # 快门声音开关
    on_off_shutter_sound = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id' \
                           '/shuttersound_setting\"]/android.widget.LinearLayout[1]/android.widget.Switch[1]'
    # 避免闪烁
    into_avoid_flashing = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id' \
                          '/anti_flicker_setting\"]/android.widget.RelativeLayout[1]'
    # 对焦声音开关
    on_off_Focus_sound = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id' \
                         '/focussound_setting\"]/android.widget.LinearLayout[1]/android.widget.Switch[1]'
    # 防抖开关
    on_off_stabilization_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id' \
                           '/eis_setting\"]/android.widget.LinearLayout[1]/android.widget.Switch[1]'

    # 零延时开关
    on_off_time_delay = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id' \
                        '/zsd_setting\"]/android.widget.LinearLayout[1]/android.widget.Switch[1]'

    # 通用
    # 照片大小
    into_photo_size = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id' \
                      '/picture_size_setting\"]/android.widget.RelativeLayout[1]'
    # 保存信息位置开关
    on_off_save_location_information = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id' \
                                       '/savelocation_setting\"]/android.widget.LinearLayout[1]/android.widget.Switch[1]'
    # 两分钟无操作退出相机开关
    on_off_Two_minutes_exit = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id' \
                              '/autoexit_setting\"]/android.widget.LinearLayout[1]/android.widget.Switch[1]'
    # 关于相机
    About_the_camera = '//android.widget.ListView[@resource-id=\"android:id/list\"]' \
                       '/android.widget.LinearLayout[11]/android.widget.RelativeLayout[1]'

    # 全景确定键
    panorama_click_id = 'com.freeme.camera:id/btn_pano_save'
    # 避免闪烁50hz
    avodi_flashing_50hz_xpath = '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.' \
                                'widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.RadioButton[1]'
    # 避免闪烁自动
    avodi_flashing_auto_xpath = '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.' \
                                'widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RadioButton[1]'
    # 避免闪烁关闭
    avodi_flashing_off_xpath = '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.' \
                               'widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.RadioButton[1]'
    # 避免闪烁60hz
    avodi_flashing_60hz_xpath = '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.' \
                                'widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.RadioButton[1]'
    # 照片大小16M(4:3)
    rear_photo_size_16m_4_3_xpath = '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.' \
                               'widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.RadioButton[1]'
    # 照片大小16M(18:9)
    rear_photo_size_16m_18_9_xpath = '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.' \
                                'widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RadioButton[1]'

    # 照片大小8M（18:9）
    rear_photo_size_8m_18_9_xpath = '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.' \
                                    'widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.RadioButton[1]'
    # 照片大小8M（4:3）
    rear_photo_size_8m_4_3_xpath = '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.' \
                                   'widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.RadioButton[1]'



    # 照片大小2M(18:9)
    front_photo_size_2m_16_9_xpath = '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.' \
                               'widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.RadioButton[1]'
    # 照片大小2M(4:3)
    front_photo_size_2m_4_3_xpath = '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.' \
                              'widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.RadioButton[1]'

    # 前置照片8M(18:9)
    front_photo_size_8m_18_9_xpath = '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.' \
                               'widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RadioButton[1]'

    # 前置照片8M(4:3)
    front_photo_size_8m_4_3_xpath = '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.' \
                              'widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.RadioButton[1]'

    # 前置人脸识别开关
    on_off_face_recognition_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id' \
                                    '/facedetection_setting\"]/android.widget.LinearLayout[1]/android.widget.Switch[1]'
    # 前置人脸属性开关
    on_off_face_attribute_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id' \
                                  '/faceproperty_setting\"]/android.widget.LinearLayout[1]/android.widget.Switch[1]'
    # 前置自拍镜像开关
    on_off_selfie_mirror_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id' \
                                 '/mirrorcapture_setting\"]/android.widget.LinearLayout[1]/android.widget.Switch[1]'

    # 后置视频画质
    video_quality_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id' \
                          '/video_quality_setting\"]/android.widget.RelativeLayout[1]'

    # FHD
    FHD_xpath = '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.widget.LinearLayout[1]' \
                '/android.widget.LinearLayout[1]/android.widget.RadioButton[1]'
    # HD
    HD_xpath = '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.widget.LinearLayout[2]' \
               '/android.widget.LinearLayout[1]/android.widget.RadioButton[1]'
    # VGA
    VGA_xpath = '//android.widget.ListView[@resource-id=\"android:id/list\"]/android.widget.LinearLayout[3]' \
                '/android.widget.LinearLayout[1]/android.widget.RadioButton[1]'
    # 品牌水印
    logo_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/brandwater_setting\"]' \
                 '/android.widget.LinearLayout[1]/android.widget.Switch[1]'
    # 地理位置
    position_logo_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/locationwater_setting\"]' \
                     '/android.widget.LinearLayout[1]/android.widget.Switch[1]'
    # 时间水印
    time_logo_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/timewater_setting\"]' \
                      '/android.widget.LinearLayout[1]/android.widget.Switch[1]'

    def __init__(self, base_obj):
        self.base_obj = base_obj

    # 音量键拍照开关
    def volume_photos_switch(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        # 点击音量键拍照开关
        self.base_obj.find_XPATH(self.on_off_volume_photos_xpath).click()
        self.base_obj.driver.keyevent(4)

    # 点击音量键
    def volume_photos(self):
        # 点击
        # print('vloume_1')
        time.sleep(2)
        # self.base_obj.driver.keyevent(24)
        self.base_obj.driver.keyevent(25)
        time.sleep(3)
        # print('volume_2')
        # 点击音量键拍照开关

    # 触屏拍照开关
    def touch_screen_switch(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        # 点击触屏拍照开关
        self.base_obj.find_XPATH(self.on_off_touch_screen).click()
        self.base_obj.driver.keyevent(4)

    # 触屏拍照
    def touch_screen(self):
        time.sleep(2)
        self.base_obj.tap(350, 450)
        time.sleep(3)

    # 人脸识别开关
    def ace_recognition(self):
        time.sleep(2)
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        # 点击人脸识别开关
        self.base_obj.find_XPATH(self.on_off_Face_recognition).click()
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    # 网格线开关
    def Grid_lines(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        # 点击网格线开关
        self.base_obj.find_XPATH(self.on_off_Grid_lines).click()
        # time.sleep(2)
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)
        # time.sleep(3)

    def panorama_Grid_lines(self):
        # 切换至美颜
        main_page.beauty_photo(self.base_obj)
        # 开关网格线
        self.Grid_lines()
        # 全景坐标 [125,1160][195,1232]
        main_page.panorama_photo(self.base_obj)

    # 全景快门声音
    def panorama_shutter_sound(self):
        # 切换至美颜
        main_page.beauty_photo(self.base_obj)
        # 开关快门声音
        self.shutter_sound()
        # 全景坐标 [125,1160][195,1232]
        main_page.panorama_photo(self.base_obj)

    # 快门声音开关
    def shutter_sound(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        # 点击快门声音开关
        self.base_obj.find_XPATH(self.on_off_shutter_sound).click()
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    # 避免闪烁
    def avoid_flashing(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        # 点击避免闪烁
        self.base_obj.find_XPATH(self.into_avoid_flashing).click()

    # 避免闪烁50hz
    def avodi_flashing_50hz(self):
        self.avoid_flashing()
        self.base_obj.find_XPATH(self.avodi_flashing_50hz_xpath).click()
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    # 避免闪烁自动
    def avodi_flashing_auto(self):
        self.avoid_flashing()
        self.base_obj.find_XPATH(self.avodi_flashing_auto_xpath).click()
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    # 避免闪烁关闭
    def avodi_flashing_off(self):
        self.avoid_flashing()
        self.base_obj.find_XPATH(self.avodi_flashing_off_xpath).click()
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    # 避免闪烁60hz
    def avodi_flashing_60hz(self):
        self.avoid_flashing()
        self.base_obj.find_XPATH(self.avodi_flashing_60hz_xpath).click()
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    # 对焦声音开关
    def Focus_sound(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        # 点击对焦声音开关
        self.base_obj.find_XPATH(self.on_off_Focus_sound).click()
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    # 点击照片大小
    def photo_size(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        # 上划至底部
        self.score_end()
        # 点击照片大小
        self.base_obj.find_XPATH(self.into_photo_size).click()

    # 照片大小16M(4:3)
    def photo_size_16m_4_3(self):
        # 点击照片大小
        self.photo_size()
        # 选择16M
        self.base_obj.find_XPATH(self.rear_photo_size_16m_4_3_xpath).click()
        # 返回
        self.base_obj.driver.keyevent(4)

    # 照片大小16M(18:9)
    def photo_size_16m_18_9(self):
        # 点击照片大小
        self.photo_size()
        # 选择16M
        self.base_obj.find_XPATH(self.rear_photo_size_16m_18_9_xpath).click()
        # 返回
        self.base_obj.driver.keyevent(4)

    # 照片大小2M(16:9)
    def photo_size_2m_16_9(self):
        # 点击照片大小
        self.photo_size()
        # 选择16M
        self.base_obj.find_XPATH(self.front_photo_size_2m_16_9_xpath).click()
        # 返回
        self.base_obj.driver.keyevent(4)

    # 照片大小2M(4:3)
    def photo_size_2m_4_3(self):
        # 点击照片大小
        self.photo_size()
        # 选择16M
        self.base_obj.find_XPATH(self.front_photo_size_2m_4_3_xpath).click()
        # 返回
        self.base_obj.driver.keyevent(4)

    # 前置照片大小8M(4:3)
    def photo_size_8m_4_3(self):
        # 点击照片大小
        self.photo_size()
        # 选择8m_4_3
        self.base_obj.find_XPATH(self.front_photo_size_8m_4_3_xpath).click()
        # 返回
        self.base_obj.driver.keyevent(4)

    # 前置照片大小8M(18:9)
    def photo_size_8m_18_9(self):
        # 点击照片大小
        self.photo_size()
        # 选择8m_18_9
        self.base_obj.find_XPATH(self.front_photo_size_8m_18_9_xpath).click()
        # 返回
        self.base_obj.driver.keyevent(4)

    # 功能过长点击保存位置信息开关
    def save_location_information(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()

        # 上划至底部
        self.score_end()

        # 点击保存位置信息开关
        self.base_obj.find_XPATH(self.on_off_save_location_information).click()
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)
        # time.sleep(2)

    # 正常数量功能点击保存位置信息开关
    def less_save_location_information(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()

        # 点击保存位置信息开关
        self.base_obj.find_XPATH(self.on_off_save_location_information).click()
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    # 点击两分钟无操作退出相机开关
    def Two_minutes_exit(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        # 点击两分钟无操作退出相机开关
        self.base_obj.find_XPATH(self.on_off_Two_minutes_exit).click()
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    # 点击关于相机
    def about_the_camera(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        # 点击关于相机
        self.base_obj.find_XPATH(self.About_the_camera).click()

    # 开关前置人脸识别
    def on_off_face_recognition(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        self.base_obj.find_XPATH(self.on_off_face_recognition_xpath).click()
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    # 开关人脸属性
    def on_off_face_attribute(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        self.base_obj.find_XPATH(self.on_off_face_attribute_xpath).click()
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    # 开关自拍镜像
    def on_off_selfie_mirror(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        self.base_obj.find_XPATH(self.on_off_selfie_mirror_xpath).click()
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    def video_quality(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        # 进入视频画质
        self.base_obj.find_XPATH(self.video_quality_xpath).click()

    def video_fhd(self):
        # 选择fhd
        self.base_obj.find_XPATH(self.FHD_xpath).click()
        time.sleep(1)
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    def video_hd(self):
        # 选择fhd
        self.base_obj.find_XPATH(self.HD_xpath).click()
        time.sleep(1)
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    def video_vga(self):
        # 选择fhd
        self.base_obj.find_XPATH(self.VGA_xpath).click()
        time.sleep(1)
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    # 打开关闭的功能
    def open_all_function(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        # 点击触屏拍照开关
        self.base_obj.find_XPATH(self.on_off_touch_screen).click()

    # 零延时功能开关
    def time_delay(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        # 点击零延时开关
        self.base_obj.find_XPATH(self.on_off_time_delay).click()
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    # 品牌水印开关
    def on_off_logo(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        # 点击品牌水印开关
        self.base_obj.find_XPATH(self.logo_xpath).click()
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    # 地理位置水印开关
    def on_off_position_logo(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        # 点击地理位置水印开关
        self.base_obj.find_XPATH(self.position_logo_xpath).click()
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    # 时间水印开关
    def on_off_time_logo(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        # 点击时间水印开关
        self.base_obj.find_XPATH(self.time_logo_xpath).click()
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    # 防抖开关
    def on_off_stabilization(self):
        # 点击设置按钮
        self.base_obj.find_ID(self.mode_id).click()
        # 点击防抖开关
        self.base_obj.find_XPATH(self.on_off_stabilization_xpath).click()
        # 返回拍照界面
        self.base_obj.driver.keyevent(4)

    # 滑动至底部
    def score_end(self):
        # 对焦按钮
        # foucs = self.base_obj.find_XPATH(self.on_off_Focus_sound)

        # 网格线
        grid = self.base_obj.find_XPATH(self.on_off_Grid_lines)

        # 快门声音
        sound = self.base_obj.find_XPATH(self.on_off_shutter_sound)

        # 触屏拍照按钮
        touch = self.base_obj.find_XPATH(self.on_off_touch_screen)
        # 由快门声音上划至触屏
        self.base_obj.driver.scroll(sound, touch)
