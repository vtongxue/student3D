# -*- coding: utf-8 -*-
"""
 @Date    : 2021/2/3 21:51
 @Author  : Douglee
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="student3D",
    version="0.0.1",
    author="vtongxue",
    description="student3D package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="vtongxue/student3D",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
    'ursina>=3.0.0'
    ]
)
