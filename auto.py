import pyautogui
import time
from datetime import datetime, timedelta

def click_on_image(image_path):
    # 在屏幕上查找指定图像
    image_location = pyautogui.locateOnScreen(image_path)

    # 如果找到了图像
    if image_location:
        # 获取图像中心点坐标
        image_center = pyautogui.center(image_location)

        # 模拟鼠标点击图像中心点
        pyautogui.click(image_center.x, image_center.y)
    else:
        print(f"未找到指定图像: {image_path}")

# 设置每分钟执行一次，允许5秒误差
minutes_interval = 1

while True:
    # 获取当前时间
    now = datetime.now()

    # 判断是否是每分钟的开始，并允许5秒误差
    if now.second <= 5:
        try:
            print(f"执行时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")
            click_on_image('/home/foxing/Desktop/auto_claim/刷新.png')
            time.sleep(15)
            click_on_image('/home/foxing/Desktop/auto_claim/mint.png')
            time.sleep(10)
            click_on_image('/home/foxing/Desktop/auto_claim/approve.png')
        except Exception as e:
            print(f"发生异常: {e}")

    # 等待一秒钟
    time.sleep(1)

