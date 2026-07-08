from setuptools import find_packages, setup

def readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content

if __name__ == '__main__':
    setup(
        name='rembg',
        long_description=readme(),
        include_package_data=True,
        packages=find_packages(),
    )
