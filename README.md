<div align="center">

![logo](./Branding/A.jpg)

<div align="center">
    <h3>"There is no end, only extending."</h3>
</div>
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Go Version](https://img.shields.io/badge/Go-1.20+-00ADD8?logo=go)](https://golang.org/) [![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?logo=vuedotjs)](https://vuejs.org/) [![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python)](https://www.python.org/)


# APE - Cloud

APE-Cloud 是一个适用于个人、工作室等小型团队办公交流的迷你工作站服务器。本项目由 Apeiron 维护，其中集成了其他一些开源项目，原项目链接将在文末列出

APE-Cloud 集成了在局域网下的 网盘服务、图像服务、聊天室服务。你可以将 APE-Cloud 部署在你的 MINI PC、 Raspberry 等设备上

特别地，APE-Cloud 上关于图像上的处理工作在旭日开发平台上针对BPU硬件进行优化，在RDK系列开发板上将会有更好的体验

**APE-Cloud 功能：**

网盘服务：APE-Cloud 支持多用户不限速地上传、下载、分享文件等

图像服务：APE-Cloud 支持图片处理，包括图片提取文字、图片去除背景等

聊天室服务：APE-Cloud 支持在线多人的群组、频道聊天





## 快速部署教程

1. 克隆仓库

    ```bash
    git clone https://github.com/ApeironOdin/APE-Cloud.git
    ```

2. 安装python库依赖

    ```bash
    cd ImageService/
    pip install -r requirements.txt
    ```

3. 安装go依赖

    ```bash
    cd /FileBrowser
    pnpm install
    cd /LetChat
    npm install
    ```

4. 运行脚本启动服务

    ```bash
    chmod -x APE-Cloud-Startup.sh
    ./APE-Cloud-Startup.sh
    ```

    

网盘服务：10.42.0.1:3000

图像服务：10.42.0.1.4000

聊天室服务：10.42.0.1.5000
