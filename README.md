# 网络设备配置备份程序

## 简要描述
本程序用来备份网络设备的配置。使用场景为：不支持api的网络设备或运维人员不会调用api的场景。

备份方式说明：
交换机备份是使用pexpect模块以及NetDevices模块进行备份操作。
防火墙备份是使用paramiko模块进行备份操作，不依赖NetDevices模块。

目前支持备份：cisco ios交换机设备，华为quidway系列交换机设备，飞塔fortigate防火墙设备。

## 程序目录结构说明：
├── firewalls_cfg 用于存放防火墙的配置信息(账号、密码、ip、主机名、操作系统)
├── fw_cfg_backup.py 备份防火墙的主程序
├── requirements.txt python库
├── NetDevices 模块目录
│   ├── Device.py 所有模块的父类
│   ├── FortiOS.py 该文件用于测试，不作实际用途
│   ├── __init__.py 模块入口
│   ├── IOS.py Cisco交换机子类
│   ├── __pycache__ 缓存目录
│   │   ├── Device.cpython-35.pyc
│   │   ├── FortiOS.cpython-35.pyc
│   │   ├── __init__.cpython-35.pyc
│   │   ├── IOS.cpython-35.pyc
│   │   └── Quidway.cpython-35.pyc
│   ├── Quidway.py 华为交换机子类
│   └── test.py 该文件用于测试，不作实际用途
├── README.md 说明文件
├── sw_cfg_backup.py 备份交换机的主程序
└── switches_cfg 用于存放交换机的配置信息(账号、密码、ip、主机名、操作系统)

## 环境要求：
- python3.5以上
- 任意版本linux系统

## 初始化设置：
1. git clone本项目，然后进入目录，创建python3虚拟开发环境
python3 -m venv py3
2. 进入虚拟环境
source ./py3/bin/activate
3. 安装所需模块
pip install -r requirements.txt

## 编辑配置文件：
分别编辑switches_cfg和firewalls_cfg配置文件，写入你的设备账号密码等信息，文件里面有详细说明。

## 程序运行方法
参数说明：python后的第一个参数是备份交换机的主程序，第二个参数是交换机设备文件
1. 备份交换机配置
python /home/NetDevOps/sw_cfg_backup.py /home/NetDevOps/switches_cfg
2. 备份防火墙配置
python /home/NetDevOps/fw_cfg_backup.py /home/NetDevOps/firewalls_cfg
把上述两条命令用crontab定时运行，即完成全部设置。

## 程序运行结果说明：
程序会自动把配置文件备份到服务器的/home/NetBackup目录下

