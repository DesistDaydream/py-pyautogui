# 根据图片定位位置
import pyautogui

# 获取图片在现在屏幕上面的坐标
# 注意：要使用这类函数，必须使用 `pip install pillow` 命令安装 pillow 包
location = pyautogui.locateCenterOnScreen("locate/win.png")

print(location.x, location.y)

# 找到图片位置后，用鼠标左键点击一下
pyautogui.click(location.x, location.y, clicks=1, button="left")
