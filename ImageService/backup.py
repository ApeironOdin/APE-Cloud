import streamlit as st
import easyocr
import subprocess
import os
from rembg import remove, new_session

st.set_page_config(
    page_title="APE-Cloud ✧ImageSurvice",
    page_icon=".img/branding/favicon.ico",
    layout="centered"
)


headimg, headname, headempty = st.columns([1, 3, 5])
with headimg:
    st.image(".img/branding/A.jpg")
with headname:
    st.title("APE-Cloud")

load_image = st.file_uploader("Load Image", type=['jpg', 'jpeg', 'png'], accept_multiple_files=True)


def download(load_image):
    os.system('del /q ".img/inputs\\*"')
    os.system('del /q ".img/outputs\\*"')

    idx = 1
    for img in load_image:
        img.name = f"img{idx}.jpg"
        idx = idx + 1
    for img in load_image:
        bytes_data = img.read()
        with open(f".img/inputs/{img.name}", "wb") as f:
            f.write(bytes_data)



ocr_model = easyocr.Reader(['ch_sim', 'en'])
with st.container(border=True):
    bt, img = st.columns([2, 2])
    with bt:
        st.markdown('''
        ## EASYOCR Image2Text
        ##### EASYOCR 图片提取文字
        
        提取上传的图片中的文字
        
        ''')
        ocr_button = st.button(label="EASYOCR Image2Text", help="图片提取文字", type="primary")

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



with st.container(border=True):
    bt, img = st.columns([2, 2])
    with bt:
        st.markdown('''
        ## ESRGAN ImageEnhance
        ##### ESRGAN 图片增强画质

        提升上传的图片的分辨率清晰度

        ''')
        # esrgan_button = st.button(label="ESRGAN Image Enhance", help="图片增强画质", type="primary")
        esrgan_button = st.button(label="ESRGAN Image Enhance", help="功能维修中qwq", type="secondary")

    with img:
        st.image(".img/branding/ImageEnhance.png")

process2 = st.empty()
if esrgan_button:
    download(load_image)
    process2.warning("ESRGAN Image Enhance ......")
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
    process2.warning("ESRGAN Image Enhance is success")



with st.container(border=True):
    bt, img = st.columns([2,2])
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
