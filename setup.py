import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nacos_client_python",
    version="0.0.1",
    author="Hubert Shelley",
    author_email="hubertshelley@163.com",
    description="nacos python client tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/hubert22/nacos_client_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0 License",
        "Operating System :: OS Independent",
    ],
)
