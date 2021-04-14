# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2019-11-14 17:45:03
# @Last Modified by:   Anderson
# @Last Modified time: 2021-04-15 02:15:13
import setuptools


setuptools.setup(
    name="pptx-ea-font",
    version="0.0.1",
    author="MakerBi",
    author_email="andersonby@163.com",
    description="Set east asia font in pptx correctly.",
    long_description_content_type="text/markdown",
    url="https://github.com/AndersonBY/pptx-ea-font",
    packages=setuptools.find_packages(),
    install_requires=['python-pptx'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
