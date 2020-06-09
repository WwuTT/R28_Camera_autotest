import time

# 就从这里开始重构

# 拍照按钮
click_photo_id = "com.freeme.camera:id/shutter_root"
# 相册键
photo = "com.freeme.camera:id/thumbnail"
# 全景确定键
panorama_click_id = 'com.freeme.camera:id/btn_pano_save'
# 视频录制暂停按钮
viedo_pause_id = 'com.freeme.camera:id/btn_pause_resume'
# 视频录制中的拍照按钮
video_photo_id = 'com.freeme.camera:id/btn_vss'
# 视频录制中的结束录制按钮
video_stop_id = 'com.freeme.camera:id/video_shutter_root'
# 前置后置摄像头切换按钮
switch_camera_id = 'com.freeme.camera:id/camera_switcher'
# 美颜功能的xpath定位
beauty_xpath = '//android.widget.TextView[@text=\"美颜\"]'
# 美颜功能中的美颜
beauty_xpath_2 = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/item_list\"]' \
                 '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]'
# 美颜美肤
beauty_skin_xpath = '//android.widget.TextView[@text=\"美肤\"]'
# 美颜瘦脸
beauty_thin_face_xpath = '//android.widget.TextView[@text=\"瘦脸\"]'
# 美颜大眼
beauty_big_eyes_xpath = '//android.widget.TextView[@text=\"大眼\"]'

# 美颜自然
beauty_natural_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/textRoot\"]' \
                       '/android.widget.RelativeLayout[1]'


# 前后置摄像头切换按钮
# front_video_xpath = '//android.widget.RelativeLayout[@resource-id=\"com.freeme.camera:id/shutter_root\"]'
# 后置摄像头的视频按钮
video_xpath = '//android.widget.TextView[@text=\"视频\"]'
# 景深按钮
depth_of_field_xpath = '//android.widget.TextView[@text=\"景深\"]'
# 全景按钮
panorama_xpath = '//android.widget.TextView[@text=\"全景\"]'
# 前后置摄像头的美视按钮
beauty_video_xpath = '//android.widget.TextView[@text=\"美视\"]'
# 前置摄像头拍照按钮
front_facing_xpath = '//android.widget.TextView[@text=\"拍照\"]'

# 人像
portrait_xpath = '//android.widget.TextView[@text=\"人像\"]'

# 儿童模式
kid_xpath = '//android.widget.TextView[@text=\"儿童\"]'
# 婴儿功能
baby_xpath = '//android.widget.TextView[@text=\"婴儿\"]'
# 铃铛功能
bell_xpath = '//android.widget.TextView[@text=\"铃铛\"]'
# 猫咪功能
cat_xpath = '//android.widget.TextView[@text=\"猫咪\"]'
# 小狗功能
dog_xpath = '//android.widget.TextView[@text=\"小狗\"]'
# 大鼓功能
drum_xpath = '//android.widget.TextView[@text=\"大鼓\"]'


# 模特模式
model_pattern_xpath = '//android.widget.TextView[@text=\"模特\"]'
# 男生功能
boy_xpath = '//android.widget.TextView[@resource-id=\"com.freeme.cameraplugin.posemode:id/text\" and @text=\"男生\"]'
# 女生功能
girl_xpath = '//android.widget.TextView[@resource-id=\"com.freeme.cameraplugin.posemode:id/text\" and @text=\"女生\"]'
# 多人功能
many_people_xpath = '//android.widget.TextView[@resource-id=\"com.freeme.cameraplugin.posemode:id' \
                   '/text\" and @text=\"多人\"]'
# 向右更换功能中的图案
right_many_id = 'com.freeme.cameraplugin.posemode:id/watermark_swith_right'


# 水印模式
watermark_xpath = '//android.widget.TextView[@text=\"水印\"]'
# 旅行水印
travel_xpath = '//android.widget.TextView[@text=\"旅行\"]'
# 美食水印
cate_xpath = '//android.widget.TextView[@text=\"美食\"]'
# 潮语水印
tide_language_xpath = '//android.widget.TextView[@text=\"潮语\"]'
# 情意水印
affective_xpath = '//android.widget.TextView[@text=\"情意\"]'
# 自拍水印
selfie_xpath = '//android.widget.TextView[@text=\"自拍\"]'
# 心情水印
mood_xpath = '//android.widget.TextView[@text=\"心情\"]'


# 脸萌模式
myotee_xpath = '//android.widget.TextView[@text=\"脸萌\"]'
# 装饰功能
decoration_id = 'com.freeme.camera:id/decoration'
# 四个装饰功能
decoration_1_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/item_list\"]' \
                     '/android.widget.FrameLayout[1]/android.widget.ImageView[1]'
decoration_2_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/item_list\"]' \
                     '/android.widget.FrameLayout[2]/android.widget.ImageView[1]'
decoration_3_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/item_list\"]' \
                     '/android.widget.FrameLayout[3]/android.widget.ImageView[1]'
decoration_4_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/item_list\"]' \
                     '/android.widget.FrameLayout[4]/android.widget.ImageView[1]'

# 趣味功能
delight_id = 'com.freeme.camera:id/delight'
# 四个趣味功能
delight_1_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/item_list\"]' \
                  '/android.widget.FrameLayout[1]/android.widget.ImageView[1]'
delight_2_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/item_list\"]' \
                  '/android.widget.FrameLayout[2]/android.widget.ImageView[1]'
delight_3_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/item_list\"]' \
                     '/android.widget.FrameLayout[3]/android.widget.ImageView[1]'
delight_4_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/item_list\"]' \
                     '/android.widget.FrameLayout[4]/android.widget.ImageView[1]'

# 卡通功能
cartoon_id = 'com.freeme.camera:id/cartoon'
# 四个卡通功能
cartoon_1_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/item_list\"]' \
                  '/android.widget.FrameLayout[1]/android.widget.ImageView[1]'
cartoon_2_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/item_list\"]' \
                     '/android.widget.FrameLayout[2]/android.widget.ImageView[1]'
cartoon_3_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/item_list\"]' \
                     '/android.widget.FrameLayout[3]/android.widget.ImageView[1]'
cartoon_4_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/item_list\"]' \
                     '/android.widget.FrameLayout[4]/android.widget.ImageView[1]'

# 表情功能
expression_id = 'com.freeme.camera:id/expression'
# 四个表情功能
expression_1_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/item_list\"]' \
                  '/android.widget.FrameLayout[1]/android.widget.ImageView[1]'
expression_2_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/item_list\"]' \
                     '/android.widget.FrameLayout[2]/android.widget.ImageView[1]'
expression_3_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/item_list\"]' \
                     '/android.widget.FrameLayout[3]/android.widget.ImageView[1]'
expression_4_xpath = '//android.widget.LinearLayout[@resource-id=\"com.freeme.camera:id/item_list\"]' \
                     '/android.widget.FrameLayout[4]/android.widget.ImageView[1]'


# 主页上方的设置按钮
# 设置按钮
mode_id = 'com.freeme.camera:id/mode'
# 延时拍照按钮
timer_icon_id = 'com.freeme.camera:id/self_timer_icon'
# 闪光灯按钮
flash_icon_id = 'com.freeme.camera:id/flash_icon'
# hdr
hdr_icon_id = 'com.freeme.camera:id/hdr_icon'


# 首次进入相机的拍照功能
def start_click_photo(base_obj):
    # base_obj.find_ID(base_obj.timer_icon_id).click()
    # 点击拍照
    base_obj.find_ID(click_photo_id).click()


# 拍照按钮
def click_photo(base_obj):
    # 点击拍照
    # time.sleep(1)
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 后置美颜功能
def beauty_photo(base_obj):
    # 点击美颜功能按钮
    # time.sleep(3)
    # base_obj.tap(x1, y1, x2, y2)
    base_obj.find_XPATH(beauty_xpath).click()


# 进入美颜中的美颜
def beauty_beauty(base_obj):
    # 点击美颜
    base_obj.find_XPATH(beauty_xpath_2).click()

# 美颜自然
def beauty_natural(base_obj):
    base_obj.find_XPATH(beauty_natural_xpath).click()

# 美颜美肤
def beauty_skin(base_obj):
    base_obj.find_XPATH(beauty_skin_xpath).click()


# 美颜瘦脸
def beauty_thin_face(base_obj):
    base_obj.find_XPATH(beauty_thin_face_xpath).click()


# 美颜大眼
def beauty_big_eyes(base_obj):
    base_obj.find_XPATH(beauty_big_eyes_xpath).click()


# 景深功能
def depth_of_field_photo(base_obj):

    base_obj.find_XPATH(beauty_video_xpath).click()
    # 点击景深功能按钮
    # time.sleep(3)
    # base_obj.tap(x1, y1, x2, y2)
    base_obj.find_XPATH(depth_of_field_xpath).click()


# 全景功能
def panorama_photo(base_obj):
    # time.sleep(3)
    # base_obj.tap(x1, y1, x2, y2)
    base_obj.find_XPATH(panorama_xpath).click()


# 全景拍照需点击确定按钮
def panorama_click_photo(base_obj):
    # 确定全景拍照
    base_obj.find_ID(panorama_click_id).click()


# 进入视频录制功能
def video(base_obj):
    # time.sleep(3)
    # base_obj.tap(x1, y1, x2, y2)
    base_obj.find_XPATH(video_xpath).click()


# 视频中的功能
def video_in(base_obj):
    # 开始录制
    try:
        base_obj.find_ID(click_photo_id).click()
    except:
        base_obj.keyevent(4)
        time.sleep(2)
        base_obj.find_ID(click_photo_id).click()
    time.sleep(3)
    try:
        # 暂停录制
        time.sleep(2)
        base_obj.find_ID(viedo_pause_id).click()
    except:
        print('暂停失败，再次暂停')
        time.sleep(2)
        # 暂停录制
        base_obj.find_ID(viedo_pause_id).click()
    # time.sleep(2)
    # 继续录制 5s
    base_obj.find_ID(viedo_pause_id).click()
    time.sleep(2)
    # 点击视频录制中的拍照按钮
    base_obj.find_ID(video_photo_id).click()
    time.sleep(2)
    try:
        # 结束录制
        base_obj.find_ID(video_stop_id).click()
    except:
        time.sleep(2)
        # 结束录制
        base_obj.find_ID(video_stop_id).click()
    time.sleep(2)


# 美视功能
def beauty_video(base_obj):
    # time.sleep(3)
    # base_obj.tap(x1, y1, x2, y2)
    base_obj.find_XPATH(beauty_video_xpath).click()


# 景深模式
def depth(base_obj):
    # time.sleep(3)
    # base_obj.tap(x1, y1, x2, y2)
    base_obj.find_XPATH(depth_of_field_xpath).click()
    # 拍照
    base_obj.find_ID(click_photo_id).click()
    # time.sleep(3)


# 切换至视频
def return_video(base_obj):
    # time.sleep(3)
    # 切换至视频
    # base_obj.tap(x1, y1, x2, y2)
    base_obj.find_XPATH(video_xpath).click()


# 点击摄像头前后置转换按钮
def onoff_front_facing(base_obj):
    # time.sleep(2)
    base_obj.find_ID(switch_camera_id).click()
    print('前后置摄像头转换')
    # time.sleep(2)
    # try:
    #     time.sleep(2)
    #     base_obj.find_ID(switch_camera_id).click()
    #     print('前后置摄像头转换')
    #     time.sleep(2)
    # except:
    #     base_obj.get_screenshot('onoff_front_error.png')


# 前置摄像头录制视频功能
def front_facing_video(base_obj):
    # 暂停录制
    time.sleep(3)
    base_obj.find_ID(viedo_pause_id).click()
    time.sleep(3)
    # 继续录制 5s
    base_obj.find_ID(viedo_pause_id).click()
    time.sleep(3)
    # 结束录制
    try:
        base_obj.find_ID(video_stop_id).click()
        time.sleep(2)
    except:
        base_obj.find_ID(video_stop_id).click()
        time.sleep(2)


# 前置摄像头美视功能
def front_facing_video_b(base_obj):
    # 点击美视按钮
    # time.sleep(3)
    # base_obj.tap(x1, y1, x2, y2)
    # base_obj.find_XPATH(beauty_video_xpath).click()
    # time.sleep(3)
    # 开始录制
    # time.sleep(2)
    try:
        base_obj.find_ID(click_photo_id).click()
    except:
        base_obj.driver.keyevent(4)
        time.sleep(2)
        base_obj.find_ID(click_photo_id).click()
    time.sleep(3)
    # 暂停录制
    try:
        base_obj.find_ID(viedo_pause_id).click()
        time.sleep(2)
        # 继续录制 5s
        base_obj.find_ID(viedo_pause_id).click()
    except:
        time.sleep(3)
        base_obj.find_ID(viedo_pause_id).click()
        time.sleep(2)
        # 继续录制 5s
        base_obj.find_ID(viedo_pause_id).click()
    # time.sleep(3)
    # 结束录制
    try:
        base_obj.find_ID(video_stop_id).click()
    except:
        time.sleep(3)
        base_obj.find_ID(video_stop_id).click()
    time.sleep(2)


# 前置摄像头拍照功能
def front_facing_photo(base_obj):
    # 点击拍照按钮 切换回拍照功能
    # time.sleep(3)
    # base_obj.tap(x1, y1, x2, y2)
    base_obj.find_XPATH(front_facing_xpath).click()
    # time.sleep(3)
    # 拍照
    base_obj.find_ID(click_photo_id).click()
    # time.sleep(3)


# 前置美颜功能
def front_beauty_photo(base_obj):
    """
    最后一个功能 需切换回初始界面
    :return:
    """
    # 点击美颜功能按钮
    # time.sleep(3)
    # self.tap(x1, y1, x2, y2)
    base_obj.find_XPATH(beauty_xpath).click()
    # 拍照
    # base_obj.find_ID(click_photo_id).click()

    # 切换回后置摄像头
    # self.onoff_front_facing()


def return_initial(base_obj):
    # 切换回后置摄像头
    # print('前后置摄像头转换')
    # base_obj.find_ID(switch_camera_id).click()
    # 切换至视频
    base_obj.find_XPATH(video_xpath).click()
    # 回到初始拍照功能
    base_obj.find_XPATH(front_facing_xpath).click()
    # base_obj.find_XPATH()


def error_into_photo(base_obj, func = ''):
    # 进入拍照功能
    base_obj.find_XPATH(front_facing_xpath).click()
    # 点击拍照按钮
    base_obj.find_ID(click_photo_id).click()
    # 回到原功能界面
    if func == '后置视频':
        base_obj.find_XPATH(video_xpath).click()
    elif func == '前置视频':
        base_obj.find_XPATH(video_xpath).click()
    elif func == '后置美视':
        base_obj.find_XPATH(beauty_video_xpath).click()
    elif func == '前置美视':
        base_obj.find_XPATH(beauty_video_xpath).click()
    else:
        print('error')


# 进入人像模式
def portrait(base_obj):
    # 进入美视
    base_obj.find_XPATH(beauty_video_xpath).click()
    # 进入人像
    base_obj.find_XPATH(portrait_xpath).click()
    print('人像模式')


# 进入儿童模式
def kid(base_obj):
    # 进入儿童模式
    base_obj.find_XPATH(kid_xpath).click()
    print('儿童模式')


# 进入儿童婴儿模式
def kid_baby(base_obj):
    # 点击婴儿
    base_obj.find_XPATH(baby_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 进入儿童铃铛模式
def kid_bell(base_obj):
    # 点击铃铛
    base_obj.find_XPATH(bell_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 进入儿童猫咪模式
def kid_cat(base_obj):
    # 点击猫咪
    base_obj.find_XPATH(cat_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 进入小狗铃铛模式
def kid_dog(base_obj):
    # 点击小狗
    base_obj.find_XPATH(dog_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 进入儿童大鼓模式
def kid_drum(base_obj):
    # 点击大鼓
    base_obj.find_XPATH(drum_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 进入模特模式
def model_pattern(base_obj):
    # 进入模特模式
    base_obj.find_XPATH(model_pattern_xpath).click()
    print('模特模式')


# 进入模特男生模式
def model_boy(base_obj):
    # 点击男生
    base_obj.find_XPATH(boy_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 进入模特女生模式
def model_girl(base_obj):
    # 点击女生
    base_obj.find_XPATH(girl_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 进入模特多人模式
def model_many_people(base_obj):
    # 点击多人
    base_obj.find_XPATH(many_people_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 模特中下一个模特
def next_model(base_obj):
    # 下一个
    base_obj.find_ID(right_many_id).click()
    time.sleep(2)


# 进入水印模式
def watermark(base_obj):
    # 点击模特模式
    base_obj.find_XPATH(model_pattern_xpath).click()
    # 进入水印模式
    base_obj.find_XPATH(watermark_xpath).click()
    time.sleep(2)


# 水印美食
def watermark_cate(base_obj):
    # 点击美食
    base_obj.find_XPATH(cate_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 水印潮语
def watermark_tide_language(base_obj):
    # 点击潮语
    base_obj.find_XPATH(tide_language_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 水印情意
def watermark_affective(base_obj):
    # 点击情意
    base_obj.find_XPATH(affective_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 水印自拍
def watermark_selfie(base_obj):
    # 点击自拍
    base_obj.find_XPATH(selfie_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 水印心情
def watermark_mood(base_obj):
    # 点击自拍
    base_obj.find_XPATH(mood_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 进入脸萌模式
def myteeo(base_obj):
    # 点击模特模式
    base_obj.find_XPATH(model_pattern_xpath).click()
    # 进入脸萌模式
    base_obj.find_XPATH(myotee_xpath).click()
    time.sleep(2)


# 脸萌装饰1
def decoration_1(base_obj):
    # 点击装饰1
    base_obj.find_XPATH(decoration_1_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 脸萌装饰2
def decoration_2(base_obj):
    # 点击装饰1
    base_obj.find_XPATH(decoration_2_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 脸萌装饰3
def decoration_3(base_obj):
    # 点击装饰1
    base_obj.find_XPATH(decoration_3_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 脸萌装饰4
def decoration_4(base_obj):
    # 点击装饰1
    base_obj.find_XPATH(decoration_4_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 脸萌趣味1
def delight_1(base_obj):
    # 点击趣味
    base_obj.find_ID(delight_id).click()
    # 点击趣味1
    base_obj.find_XPATH(delight_1_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 脸萌趣味2
def delight_2(base_obj):
    # 点击趣味
    base_obj.find_ID(delight_id).click()
    # 点击趣味2
    base_obj.find_XPATH(delight_2_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 脸萌趣味3
def delight_3(base_obj):
    # 点击趣味
    base_obj.find_ID(delight_id).click()
    # 点击趣味3
    base_obj.find_XPATH(delight_3_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 脸萌趣味4
def delight_4(base_obj):
    # 点击趣味
    base_obj.find_ID(delight_id).click()
    # 点击趣味4
    base_obj.find_XPATH(delight_4_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 脸萌卡通1
def cartoon_1(base_obj):
    # 点击卡通
    base_obj.find_ID(cartoon_id).click()
    # 点击卡通1
    base_obj.find_XPATH(cartoon_1_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 脸萌卡通2
def cartoon_2(base_obj):
    # 点击卡通
    base_obj.find_ID(cartoon_id).click()
    # 点击卡通2
    base_obj.find_XPATH(cartoon_2_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 脸萌卡通3
def cartoon_3(base_obj):
    # 点击卡通
    base_obj.find_ID(cartoon_id).click()
    # 点击卡通3
    base_obj.find_XPATH(cartoon_3_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 脸萌卡通4
def cartoon_4(base_obj):
    # 点击卡通
    base_obj.find_ID(cartoon_id).click()
    # 点击卡通4
    base_obj.find_XPATH(cartoon_4_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 脸萌表情1
def expression_1(base_obj):
    # 点击表情
    base_obj.find_ID(expression_id).click()
    # 点击表情1
    base_obj.find_XPATH(expression_1_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 脸萌表情2
def expression_2(base_obj):
    # 点击表情
    base_obj.find_ID(expression_id).click()
    # 点击表情2
    base_obj.find_XPATH(expression_2_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 脸萌表情3
def expression_3(base_obj):
    # 点击表情
    base_obj.find_ID(expression_id).click()
    # 点击表情3
    base_obj.find_XPATH(expression_3_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)


# 脸萌表情4
def expression_4(base_obj):
    # 点击表情
    base_obj.find_ID(expression_id).click()
    # 点击表情4
    base_obj.find_XPATH(expression_4_xpath).click()
    base_obj.find_ID(click_photo_id).click()
    time.sleep(2)