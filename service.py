import streamlit as st
import easyocr
import subprocess
import os
from rembg import remove, new_session
import cv2
import numpy as np

st.set_page_config(
    page_title="APE-Cloud✧",
    page_icon=".img/branding/favicon.ico",
    layout="centered"
)


headimg, headname = st.columns([1,5])
with headimg:
    st.image(".img/branding/A.jpg")
with headname:
    st.title("APE-Cloud ✧ ImageSurvice ✧")

load_image = st.file_uploader("Load Image", type=['jpg', 'jpeg', 'png'], accept_multiple_files=True)

def resiz(img, target_width=640):
    h, w = img.shape[:2]
    target_height = int(h * (target_width / w))

    resized_img = cv2.resize(img, (target_width, target_height), interpolation=cv2.INTER_AREA)
    return resized_img

def download(load_image):
    os.system('del /q ".img/inputs\\*"')
    os.system('del /q ".img/outputs\\*"')

    idx = 1
    for img in load_image:
        img.name = f"img{idx}.jpg"
        idx = idx + 1
    for img in load_image:
        bytes_data = img.read()
        file_bytes = np.frombuffer(bytes_data, np.uint8)
        cv_img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        resiz_data = resiz(cv_img)
        save_path = f".img/inputs/{img.name}"
        cv2.imwrite(save_path, resiz_data)


########## EasyOCR ##########
ocr_model = easyocr.Reader(['ch_sim', 'en'])
with st.container(border=True):
    bt, img = st.columns([2, 2])
    with bt:
        st.markdown('''
        ## EasyOCR Image2Text
        ##### EasyOCR 图片提取文字
        
        提取上传的图片中的文字
        
        ''')
        ocr_button = st.button(label="EasyOCR Image2Text", help="图片提取文字", type="primary")

    with img:
        st.image(".img/branding/Image2Text.png")

process1 = st.empty()
if ocr_button:
    process1.warning("OCR Image2Text ......")
    download(load_image)
    for img in load_image:
        result = ocr_model.readtext(f".img/inputs/{img.name}")
        res = ""
        for it in result:
            res += it[1] + "\n"

        st.text_area(label=f"{img.name}", value=res, height=300)
    process1.warning("OCR Image2Text is success")


########## PaddleOCR ##########
with st.container(border=True):
    bt, img = st.columns([2, 2])
    with bt:
        st.markdown('''
        ## PaddleOCR Image2Text
        ##### PaddleOCR 图片提取文字

        提取上传的图片中的文字（使用BPU加速）

        ''')
        ocr2_button = st.button(label="PaddleOCR Image2Text", help="图片提取文字", type="primary")

    with img:
        st.image(".img/branding/Image2Text_bin.png")

process2 = st.empty()
if ocr2_button:
    process2.warning("OCR Image2Text ......")
    download(load_image)
    for img in load_image:
        cmd = [
            "python3",  "main.py",
            "--test-img", os.path.abspath(f".img/inputs/{img.name}")
        ]
        subprocess.run(
            cmd, 
            cwd="/home/sunrise/Desktop/APE-Cloud/ImageSurvice/PaddleOCR/runtime/python" 
        )
        res = ""
        with open("/home/sunrise/Desktop/APE-Cloud/ImageSurvice/PaddleOCR/runtime/python/output.txt", "r", encoding="utf-8") as file:
            res = file.read()

        st.text_area(label=f"{img.name}", value=res, height=300)
    process2.warning("OCR Image2Text is success")


########## REMBG ##########
with st.container(border=True):
    bt, img = st.columns([2, 2])
    with bt:
        st.markdown('''
        ## REMBG RemoveBackground
        ##### REMBG 图片去除背景

        提取图片中心的形象，去除周围背景

        ''')
        rembg_button = st.button(label="REMBG Remove Background", help="图片去除背景", type="primary")

    with img:
        st.image(".img/branding/RemoveBackground.png")

process3 = st.empty()
if rembg_button:
    download(load_image)
    process3.warning("REMBG Remove Background......")
    for img in load_image:
        with open(f".img/inputs/{img.name}", 'rb') as i:
            with open(f".img/outputs/{img.name}", 'wb') as o:
                input = i.read()
                output = remove(input, session=new_session('u2netp'))
                o.write(output)
        st.image(f".img/outputs/{img.name}")
    process3.warning("REMBG Remove is success")


########## ModNet ##########
with st.container(border=True):
    bt, img = st.columns([2, 2])
    with bt:
        st.markdown('''
        ## ModNet RemoveBackground
        ##### ModNet 图片去除背景

        提取图片中心的形象，去除周围背景（使用BPU加速）

        ''')
        modnet_button = st.button(label="ModNet Remove Background", help="图片去除背景", type="primary")

    with img:
        st.image(".img/branding/RemoveBackground_bin.png")

process4 = st.empty()
if modnet_button:
    download(load_image)
    process4.warning("ModNet Remove Background......")
    for img in load_image:
        cmd = [
            "python", "/home/sunrise/Desktop/APE-Cloud/ImageSurvice/ModNET/runtime/python/main.py",
            "--test-img", f".img/inputs/{img.name}"
        ]
        subprocess.run(cmd)
        st.image("/home/sunrise/Desktop/APE-Cloud/ImageSurvice/ModNET/test_data/result.png")
    process4.warning("ModNet Remove is success")


########## ESRGAN ##########
with st.container(border=True):
    bt, img = st.columns([2, 2])
    with bt:
        st.markdown('''
        ## ESRGAN ImageEnhance
        ##### ESRGAN 图片增强画质

        提升上传的图片的分辨率清晰度
        （RDK好像性能带不动，此功能还在维修中qwq）

        ''')
        # esrgan_button = st.button(label="ESRGAN Image Enhance", help="图片增强画质", type="primary")
        esrgan_button = st.button(label="ESRGAN Image Enhance", help="RDK好像性能带不动，此功能还在维修中qwq", type="secondary")

    with img:
        st.image(".img/branding/ImageEnhance.png")

process5 = st.empty()
if esrgan_button:
    download(load_image)
    process5.warning("ESRGAN Image Enhance ......")
    for img in load_image:
        cmd = [
            "python", r"Real-ESRGAN/inference_realesrgan.py",
            "-n", "RealESRGAN_x4plus",
            "-i", f".img/inputs/{img.name}",
            "--fp32",
            "-o", f".img/outputs/"
        ]
        subprocess.run(cmd)
        st.image(f".img/outputs/{img.name}")
    process5.warning("ESRGAN Image Enhance is success")



