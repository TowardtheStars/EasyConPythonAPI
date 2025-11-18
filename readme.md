# 伊机控 Python API

用于控制伊机控硬件的 Python API。

## 已实现功能

- 通过串口发送手柄动作
- 支持多动作同时进行
- 支持读取并识别伊机控软件生成的图片标签 IL 文件

## 未来功能

- 更方便的 API
- 图形化 IL 调试界面


## 使用方法

### 基本操作

实例： `__main__.py` 文件

1. 使用 `Serial` 打开串口
2. 将串口传入 `api.RealTimeController` 创建操作发送引擎
3. 使用 `RealTimeController.get_command_builder()` 创建命令发送接口
   1. 该接口可以预载操作命令
   2. 命令操作详见源码注释
   3. 命令不会被立即发送，只有主动调用 `await RealTimeCommandBuilder.send()` 命令才会被发送到 `RealTimeController`
4. 使用 `RealTimeController.start(console)` 启动操作发送引擎
   1. console
      1. True 的时候，即使命令队列里没有命令也会继续等待新命令
      2. False 的时候，命令队列里没命令之后会立刻停止
   2. 连接到伊机控之后的首个按键命令会失效
5. 使用 `RealTimeController.stop()` 停止发送引擎

### 使用伊机控 IL 图像标签

1. 使用你的伊机控创建 IL 图像标签文件
2. 用 `cv_module.il.ImageLabel.from_file(path)` 进行读取
3. 用 `cv2.VideoCapture` 获取采集卡句柄，并用其 `read()` 方法读出一帧（记得设置分辨率）
4. 用 `search(frame)` 方法进行匹配
