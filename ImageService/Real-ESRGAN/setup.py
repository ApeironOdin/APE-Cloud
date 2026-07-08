from setuptools import find_packages, setup

import os
import subprocess
import time

def readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content

if __name__ == '__main__':
    setup(
        name='realesrgan',
        description='Real-ESRGAN aims at developing Practical Algorithms for General Image Restoration',
        long_description=readme(),
        long_description_content_type='text/markdown',
        author='Xintao Wang',
        author_email='xintao.wang@outlook.com',
        keywords='computer vision, pytorch, image restoration, super-resolution, esrgan, real-esrgan',
        url='https://github.com/xinntao/Real-ESRGAN',
        include_package_data=True,
        packages=find_packages(exclude=('options', 'datasets', 'experiments', 'results', 'tb_logger', 'wandb')),
        classifiers=[
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
        ],
        license='BSD-3-Clause License',
        setup_requires=['cython', 'numpy'],
        zip_safe=False)
