# **ultraArm智能分拣套装软件使用说明**
<img src="./resourse/sorting_kit/ultrarm_sorting_kit.jpg" style="zoom:80%;" />

# 1 设备清单
| 设备名称 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  |  数量 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|-------------------|-|
| 奥创机械臂   | 2  |
|  舵机  | 2   |
|  吸泵 | 2   | 
| USB 2D相机   | 2   |
| 相机支架   | 2   |
| 传送带   | 1  | 
| 传送带控制盒   | 1   |
|  12V电源  | 2   |
|  24V电源  | 1   |
|  数据线 | 3   |
|  USB拓展坞  | 1   |
|  拼接底板  | 4   |
|  木块  | 18   |
|  二维码贴纸  | 1   |
|  压线夹  | 10   |

# 2 硬件搭建
## 2.1 底盘拼接
将底板按照下图参考拼接起来
<img src="./resourse/sorting_kit/diban.png" style="zoom:80%;" />

## 2.2 机械臂安装
将机械臂固定在底板上，单个机械臂需要用四颗内六角螺丝固定
<img src="./resourse/sorting_kit/jixiebianzhuang.png" style="zoom:80%;" />

接上电源线和数据线
<img src="./resourse/sorting_kit/jixiebidianyuan.png" style="zoom:80%;" />


## 2.3 相机支架拼接
先将船帽螺母放进型材上
![](./resourse/3-VisionPickingKit/00.png)
然后用内六角将底座安装到最长的型材上，按照下图，两侧都要上用内六角固定住
![](./resourse/sorting_kit/xianjidizuo.png)
再利用一个角码将2根型材拼接起来
![](./resourse/3-VisionPickingKit/02.png)
然后将相机固定在型材上,安装时注意相机与型材保持水平垂直，否则会影响相机抓取精度
![](./resourse/3-VisionPickingKit/03.png)
相机支架组装最终的样子
![](./resourse/sorting_kit/xiangji.png)
将相机支架安装到底板板上
![](./resourse/sorting_kit/xiangjiguding.png)

## 2.4 传送带主控盒安装
将主控盒固定在底版上
![](./resourse/sorting_kit/chuansongdaikzh.png)
将传送带的电机线接到传送带上
<img src="./resourse/sorting_kit/dianjixian.png" style="zoom:80%;" />

给传送带主控接上24V电源
<img src="./resourse/sorting_kit/chuansongdaidianyuan.png" style="zoom:80%;" />

将数据线接到传送带主控上
<img src="./resourse/sorting_kit/chuansongdaishujuxian.png" style="zoom:80%;" />

## 2.5 气泵盒固定架安装
将气泵盒固定架固定在底板上
<img src="./resourse/sorting_kit/qibengjaizi.png" style="zoom:80%;" />

将气泵盒固定在气泵盒固定架上
<img src="./resourse/sorting_kit/qibenganzhuang.png" style="zoom:100%;" />

将4pin线接到吸泵盒上
<img src="./resourse/sorting_kit/qibengxian.png" style="zoom:100%;" />

## 2.6 舵机与末端吸泵拼接
将舵机线插入舵机的任意一侧
<img src="./resourse/sorting_kit/duojixian.png" style="zoom:80%;" />

将乐高连接件插入末端吸盘连接处
<img src="./resourse/sorting_kit/legao.png" style="zoom:80%;" />

将舵机和末端吸盘拼接起来
<img src="./resourse/sorting_kit/duoji+xipan.png" style="zoom:80%;" />

将舵机线和吸泵盒的线接到机械臂末端
<img src="./resourse/sorting_kit/duoji+xibeng.png" style="zoom:80%;" />

**码垛机器人末端吸盘安装注意事项**
拆垛机器人无特殊要求，码垛机器人需要先装舵机后，先使用myblockly对机器人进行回零操作后，将θ角设置成-38，之后再安装吸盘，安装时，吸盘的气管端要朝着机器人底座，线管可用魔术贴粘住。
<img src="./resourse/33.png" style="zoom:100%; " />
<img src="./resourse/34.png" style="zoom:100%; " />
<img src="./resourse/35.jpg" style="zoom:100%; " />


## 2.7 线束整理
可以在底板上贴压线夹，便于整理线束
<img src="./resourse/sorting_kit/yaxianjia.png" style="zoom:80%;" />

也可以用魔术贴接舵机线和气管固定在机械臂上
<img src="./resourse/sorting_kit/moshutie.png" style="zoom:80%;" />

## 2.8 二维码木块制作
用打印机将二维码按照实际大小打印出来
<img src="./resourse/sorting_kit/erweimadaying.png" style="zoom:80%;" />

将打印出来的二维码用剪刀裁剪下来，用固体胶贴到木块上
<img src="./resourse/sorting_kit/mukuai.png" style="zoom:80%;" />

## 2.8 最终搭建效果
<img src="./resourse/sorting_kit/ultrarm_sorting_kit.jpg" style="zoom:80%;" />

# 3 软件搭建
## 3.1 python安装

myBlockly是基于Python环境以及pymycobot依赖库的拼图式编程软件，因此需要下载Python和安装pymycobot

> **注意：**安装之前，请先确认您的电脑是64位还是32位。右键点击`我的电脑`，选择`属性`。如下图显示是64位的操作系统，所以选择64位的Python安装包。

<img src="./resourse/3-myblockly/pythoninstall/电脑位数1.jpg" style="zoom: 67%;" />

<img src="./resourse/3-myblockly/pythoninstall/电脑位数2.jpg" style="zoom: 67%;" />

- **Step 1：** Python的下载和安装（建议安装python3.7版本以上）
  - Python官方下载地址： https://www.python.org/downloads/
  - 点击`Downloads`选项，开始下载Python，点击`Add Python 3.10 to PATH`,点击`Install Now`，开始安装Python
  <img src="./resourse/3-myblockly/pythoninstall/pythondownload1.jpg" style="zoom: 33%;" />
  <img src="./resourse/3-myblockly/pythoninstall/pythondownload2.jpg" style="zoom: 50%;" />
  <img src="./resourse/3-myblockly/pythoninstall/pythondownload3.jpg" style="zoom: 50%;" />
  
  - 出现“Setup was successful”提示，说明安装完成 
  <img src="./resourse/3-myblockly/pythoninstall/pythondownload4.jpg" style="zoom: 50%;" />

  - **Step 2：** pymycobot安装
- 指令直接安装，无需克隆下载代码，打开一个控制台终端(快捷键Win+R,输入cmd进入终端)，输入以下命令后按下键盘回车键：

  ```python
  pip install pymycobot ==3.2.4
  ```

  <!-- <img src="./resourse/3-myblockly/firsttimeuse/pymycobot1.png" > -->

 
**注意：pymycobot的版本需要安装v3.2.4及以上的，此外按照相同方法，用pip install numpy安装numpy库，和用pip install pyserial安装串口库**
   - **Step 3：** 串口驱动下载和安装

串口驱动程序用于机械臂通信，以接收指令，因此使用myStudio烧录固件之前需要下载串口驱动程序。ultraArm需要安装**CP34X** （适用于CH9102版本）驱动程序压缩包。

*注意：对于 Mac OS，在安装之前确保系统 "偏好设置->安全性和隐私->通用" ，并允许从 App Store 和被认可的开发者。*

* ultraArm串口驱动程序：
  * **CP34X**
    * [Windows10](https://download.elephantrobotics.com/software/drivers/CH9102_VCP_SER_Windows.exe)
    * [MACOS](https://download.elephantrobotics.com/software/drivers/CH9102_VCP_MacOS.zip)

  下载完成后点击“安装”。

  <img src="./resourse/1-myStudio/1-studioinstallation/驱动安装1.png" style="zoom: 67%;" >

  安装成功后会有提示。

  <img src="./resourse/1-myStudio/1-studioinstallation/驱动安装2.png" style="zoom: 67%;" >
- **Step 4：** 安装opencv
  OpenCV-Python是基于Python的库，旨在解决计算机视觉问题。安装之前需确保Python环境已完成搭建。

打开一个控制台终端(快捷键Win+R,输入cmd进入终端)，输入以下命令：

```bash
# 二者版本号需保持一致，这里安装4.5.5.62版本
pip install opencv-python==4.5.5.62
pip install opencv-contrib-python==4.5.5.62
```

<img src =./resourse/3-VisionPickingKit/opencv安装1.png
width ="500"  align = "center">

<img src =./resourse/3-VisionPickingKit/opencv安装2.png
width ="500"  align = "center">

安装成功后，可通过下面的命令查看具体安装的版本以及安装位置：

```bash
# 也可查看其他python库  格式：pip show 库名称
pip show opencv-python
pip show opencv-contrib-python
```

<img src =./resourse/3-VisionPickingKit/opencv安装3.png
width ="500"  align = "center">

<img src =./resourse/3-VisionPickingKit/opencv安装4.png
width ="500"  align = "center">


## 3.2 myBlockly下载

点击[myBlockly](https://download.elephantrobotics.com/software/myblockly/myblockly-Setup-latest.exe)下载。按照提示进行安装即可。
**注意**：我们只需用myblockly进行回零操作和简单调试即可
### 3.2.1 myBlockly界面展示

<img src="./resourse/3-myblockly/firsttimeuse/界面展示.png" style="zoom: 33%;" />

- 模块栏：

  - 包含程序编写所需的方法模块，可以通过鼠标放入程序编辑区进行拼接

- 小工具栏：

  点击右上角粉红色按钮会出现一个小工具栏，此处可以选择正确的机型、串口号以及波特率。也可以通过点击“读取角度”或“读取坐标”按钮获取机械臂实时关节角度和坐标。点击关节控制或坐标控制栏中的“+/-”可以控制机械臂移动。

- 程序编辑区域：

  - 运行程序之前需要在初始化模块中或者小工具栏内选择正确的机型、端口以及波特率，否则程序无法正常运行。
  - 把所需的模块方法拖拽到该区域拼接起来实现自己的程序。

**注意**:

1. ultraArm的波特率为115200；
2. 当程序无法运行的时候请检查小工具栏是否断开链接，如下图所示。

<img src="./resourse/3-myblockly/firsttimeuse/串口关闭.png" style="zoom: 33%;" />

<img src="./resourse/3-myblockly/firsttimeuse/串口打开.png" style="zoom: 33%;" />

### 3.2.2 连接电脑

- 如图所示，使用提供的串口线分别连接电脑和机械臂

![](./resourse/1-Connect/1-PC/PC-connect-1.png)

![](./resourse/1-Connect/1-PC/PC-connect-2.png)


### 3.2.3 程序运行

<img src="./resourse/3-myblockly/firsttimeuse/运行键.png" style="zoom: 50%;" />

拖动想要的方法模块，编辑自己的程序（如上图所示），每个模块结构相结合在一起后再点击“运行”就可以将代码上传到机械臂当中运行了。

**注意**：ultraArm每次运动之前必须回零，回零之后须加上一个`延迟`模块，给机械臂回零时间再进行下一个运动。

点击左上角“Python”选项可以查阅对应的Python代码，如下图所示。

<img src="./resourse/3-myblockly/firsttimeuse/python代码.png" style="zoom: 33%;" />

### 3.2.4 程序保存和载入

myBlockly的程序以*.json格式保存，点击界面右上角蓝色方框，出现“保存”选项点击后，即可保存程序。

<img src="./resourse/3-myblockly/firsttimeuse/程序保存.png" style="zoom: 67%;" />

同样点击蓝色方框，点击”加载“选项，可以导入已保存的程序。

<img src="./resourse/3-myblockly/firsttimeuse/程序载入.png" style="zoom: 67%;" />

# 4 工程介绍
## 4.1 核心文件
<img src =./resourse/7.png align = "center">

## 4.2 辅助调试文件
<img src =./resourse/8.png align = "center">

# 5 工程调试
## 5.1 设备连接
### 5.1.1串口设备
打开设备管理器，将2台机械臂和传送带的串口线按顺序插入电脑，电脑会给设备分配一个串口号，记录好每一台设备的串口号，建议每个设备连接到固定的USB接口上，否则串口号需要重新确认。设备与PC通过串口通信，所有要保证设备与串口号对应上，否则程序不能正常运行。
<img src =./resourse/9.png align = "center">

### 5.1.2 USB设备
打开设备管理器，设备会给2个USB相机分配一个不同的编号，在程序中通过切换相机编号，从而获取不同相机间采集的图像，建议每个设备连接到固定的USB接口上
**注意事项**
一个USB拓展坞只能接一个USB相机，若将两个相机都接入到同一个USB拓展坞，会导致相机之间的数据流有冲突，导致程序出错
<img src =./resourse/10.png align = "center">

## 5.2 机械臂回零
打开myblockly,除了串口号根据实际的设备选择，其余按照红框1配置，然后点击回零键，机械臂会进行回零操作，待回零操作结束后，便可对机械臂操作。机械臂重新启动后，都需要进行回零操作
<img src =./resourse/11.png align = "center">

**注意**
<img src =./resourse/12.png align = "center">

## 5.3 手眼标定
**注意:两台机械臂已经过手眼标定，只需确定相机编号，看实际偏差，根据机械臂基坐标系进行微小调整**
### 5.3.1 二维码检测
打开Aruco_test.py脚本，确定2个相机的相机编号。笔记本电脑给相机分配的编号为1和2，在变量cam_num切换1和2来确定哪个是拆垛相机和码垛相机
<img src =./resourse/14.png align = "center">

拆垛相机画面
<img src =./resourse/15.png align = "center">

码垛相机画面
<img src =./resourse/16.png align = "center">

### 5.3.2 手眼标定
运行demo脚本，观察末端吸盘距离木块有多少位移，pump_x为木块对应机械臂基座标系的X方向偏移，pump_y为木块对应机械臂基座标系下的y方向偏移。记录下pump_x和pump_y的值，重新运行程序，观察吸盘能否到达木块中心点，若能到达。则标定结束，标定结束后，不能移动相机和机械臂位置。
<img src =./resourse/sorting_kit/zb.png align = "center">


**码垛相机标定示例**

运行demo.py前确定好每个设备的串口号和相机编号后，填入到对应类的参数上。然后运行程序即可
<img src =./resourse/27.png align = "center">

先用尺子测量吸盘末端和木块中心点在X轴的差值，在本次实验中，X轴的差值为30mm左右。Y轴的差值也是按照同样方法测量
<img src =./resourse/20.jpg align = "center">
Y轴差值为5mm左右
<img src =./resourse/24.jpg align = "center">
最终效果。pump_x和pump_y根据尺子的测量的值进行微调，确保吸盘末端与木块中心点尽量重合
<img src =./resourse/sorting_kit/handeye.png align = "center">
拆垛相机与拆垛机器人的手眼标定也是按照以上步骤进行操作。



### 5.3.3 场景联调

运行demo.py前确定好每个设备的串口号和相机编号后，填入到对应类的参数上。然后运行程序即可
<img src =./resourse/27.png align = "center">

确保拆垛区域能完整拍到并识别6个二维码

<img src =./resourse/15.png align = "center">

程序结束后，码垛区域效果

<img src =./resourse/28.jpg align = "center">


场景完整运行视频

<video id="my-video" class="video-js" controls preload="auto" width="100%"
poster="" data-setup='{"aspectRatio":"16:9"}'>
  <source src="https://static.elephantrobotics.com/wp-content/uploads/2023/11/%E5%A5%A5%E5%88%9B%E6%99%BA%E8%83%BD%E5%88%86%E6%A0%8B%E5%A5%97%E8%A3%857.mp4"></video>

### 6 注意事项
程序正常运行后，不要再移动拆垛区域的木块，码垛区域的码垛顺序取决于拆垛区域木块的叠放顺序，因为18个木块上的二维码ID号是唯一的。ID从1-18，码垛机械臂会将木块按照1-3，4-6，7-9，10-12，13-15，16-18，三个木块为一组进行叠放。


