import subprocess
def run_esrgan(image_name):
    cmd = [
        "python", r"Real-ESRGAN\inference_realesrgan.py",
        "-n", "RealESRGAN_x4plus",
        "-i", f"{image_name}",
        "-o", "results/",
        "--fp32"
    ]
    subprocess.run(cmd)


if __name__ == "__main__":
    run_esrgan(r"img.jpg")