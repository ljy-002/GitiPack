import setuptools

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GitiPack",
    version="1.3.2",
    author="李今越",
    author_email="ljy123ljy123@dingtalk.com",
    description="GITI网站的辅助功能，用于推动GITI的发展",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ljy-002/GitiPack",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    extras_require={"GitiPack": ["python"]},
)