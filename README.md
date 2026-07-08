<div align="center">

<img src="./Branding/A.jpg" alt="APE-Cloud Logo" width="250" />

<h3>"There is no end, only extending."</h3>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Go Version](https://img.shields.io/badge/Go-1.20+-00ADD8?logo=go)](https://golang.org/)
[![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?logo=vuedotjs)](https://vuejs.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python)](https://www.python.org/)

</div>


# APE - Cloud

APE-Cloud is a mini-workstation server designed for office collaboration and communication within small teams, such as individuals or studios. This project is maintained by Apeiron and integrates several other open-source projects; links to the original projects are listed at the end of this document.

APE-Cloud integrates LAN-based services including cloud storage, image hosting, and chat rooms. You can deploy APE-Cloud on devices such as Mini PCs or Raspberry Pis.

Notably, the image processing capabilities in APE-Cloud have been optimized for BPU hardware on the Xuri (Sunrise) development platform, ensuring an enhanced user experience on RDK series development boards.

**APE-Cloud Features:**

Cloud Storage Service: Supports multi-user file uploading, downloading, and sharing without speed limits.

Image Service: Supports image processing tasks, including text extraction and background removal.

Chat Room Service: Supports online group and channel chats for multiple users.

## Quick Deployment Guide

1. Clone the repository

```bash
git clone https://github.com/ApeironOdin/APE-Cloud.git
```

2. Install Python dependencies

```bash
cd ImageService/
pip install -r requirements.txt
```

3. Install Go dependencies

```bash
cd /FileBrowser
pnpm install
cd /LetChat
npm install
```

4. Run the startup script

```bash
chmod +x APE-Cloud-Startup.sh
./APE-Cloud-Startup.sh
```

Cloud Storage Service: 10.42.0.1:3000

Image Service: 10.42.0.1:4000

Chat Room Service: 10.42.0.1:5000

## Acknowledgments

The creation of APE-Cloud would not have been possible without the thriving open-source community. This project references or integrates the following excellent open-source projects; we extend our sincere gratitude to the developers and teams who contributed them:

* **[FileBrowser](https://github.com/filebrowser/filebrowser)**
* **[EasyOCR](https://github.com/JaidedAI/EasyOCR)**
* **[rembg](https://github.com/danielgatis/rembg)**
* **[Let's Chat](https://github.com/sdelements/lets-chat)**

> **Tip:** We stand on the shoulders of giants. If you find APE-Cloud helpful, please also visit the repositories of the upstream projects mentioned above and give them a ⭐️ Star!
