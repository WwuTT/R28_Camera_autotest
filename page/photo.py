import time


from page.main_page import error_into_photo


class PhotoEx:
    photo_sum_info = 'android.widget.TextView'
    photo = "com.freeme.camera:id/thumbnail"
    all_photo_xpath = '//android.widget.TextView[@content-desc=\"Gallery\"]'
    # x y 为相册中长按坐标  进行删除
    x = 100
    y = 300
    select_all_id = 'com.freeme.gallery:id/action_selectall'
    delete_xpath = '//android.widget.TextView[@text=\"删除\"]'
    # 确定删除按钮
    delete_ensure_xpath = '//android.widget.Button[@resource-id=\"android:id/button1\"]'

    def __init__(self, base_obj):
        self.base_obj = base_obj

    def get_photo_sum(self, func = ''):

        try:
            # 进入相册
            time.sleep(2)
            self.base_obj.find_ID(self.photo).click()
            time.sleep(2)
            # 抓取数量按钮
            photo_str = self.base_obj.find_CLASSNAME(self.photo_sum_info)
            time.sleep(2)
            # 提取文本信息 1/10
            photo_sum = photo_str.get_attribute('text')
            # time.sleep(2)
            # 提取总数量 1/10  提取10
            global photo_sum1
            photo_sum1 = photo_sum.split('/')[1]
            # time.sleep(2)
        except:
            self.base_obj.get_screenshot('photo_sum_error.png')
            error_into_photo(self.base_obj, func)
            self.get_photo_sum()

        return photo_sum1

    # 获取相片附带位置信息
    def get_photo_loc_info(self):
        pass

    def get_old_photo_sum(self):
        # 获取原有照片数量
        global old_photo_sum
        # old_photo_sum = Photo(self.driver).get_photo_sum()
        old_photo_sum = self.get_photo_sum()
        print('原有照片数量：', old_photo_sum)

        # 第一次查看原有照片数量需点击返回按钮
        self.base_obj.driver.keyevent(4)

    # 获取现有照片数量
    def get_new_photo_sum(self, test_case_name='', modle=1, loc_info='off', func = ''):
        try:
            time.sleep(3)
            # 获取现有相片数量
            global old_photo_sum
            # 进入相册 获取照片数量
            # time.sleep(2)
            # photo_sum = Photo(self.driver).get_photo_sum()
            photo_sum = self.get_photo_sum(func)
            # time.sleep(2)
            # time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
            local_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
            # time.sleep(2)
            print(test_case_name, '现有照片数量：', photo_sum, local_time)

            if modle == 2:
                new_photo_sum = int(old_photo_sum) + 2
                try:
                    assert int(photo_sum) == new_photo_sum
                except:
                    self.base_obj.get_screenshot('photo_sum_error.png')
                    print('F')
            else:
                new_photo_sum = int(old_photo_sum) + 1
                try:
                    assert int(photo_sum) == new_photo_sum
                except:
                    self.base_obj.get_screenshot('photo_sum_error.png')
                    # time.sleep(2)
                    print('F')
            # if loc_info == 'on':
            #     pass
            old_photo_sum = photo_sum
            # self.photo_sum = photo_sum
            # time.sleep(3)
            # time.sleep(2)
            if int(photo_sum) > 500:
                print('照片数量过多 清空照片数量')
                self.delete_photo()
                old_photo_sum = 1
            # try:
            #     time.sleep(2)
            #     self.base_obj.driver.keyevent(4)
            #     time.sleep(2)
            # except:
            #     time.sleep(3)
            #     self.base_obj.driver.keyevent(4)
            #     time.sleep(2)
            time.sleep(2)
            self.base_obj.driver.keyevent(4)
            time.sleep(2)

            return old_photo_sum
        except:
            self.base_obj.get_screenshot('photo_sum_error.png')

    # 删除现有照片 留一张
    def delete_photo(self):
        # 进入相册
        # time.sleep(2)
        # self.base_obj.find_ID(self.photo).click()
        # 点击相册按钮
        self.base_obj.find_XPATH(self.all_photo_xpath).click()
        time.sleep(3)
        # 长按照片
        self.base_obj.long_press(self.x, self.y)
        # 点击全选
        time.sleep(2)
        self.base_obj.find_ID(self.select_all_id).click()
        time.sleep(2)
        # 取消选择第一张照片
        self.base_obj.tap(self.x, self.y)
        time.sleep(2)
        # 选择删除
        self.base_obj.find_XPATH(self.delete_xpath).click()
        # 确定删除
        self.base_obj.find_XPATH(self.delete_ensure_xpath).click()
        time.sleep(30)
        self.base_obj.driver.keyevent(4)
