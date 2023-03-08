
from  setuptools import setup,find_packages

with open("readme.txt", "r") as fh:
    long_description = fh.read()

setup(
    name="Topsis-Maanya-102003366",
    version="0.1.2",
    author="Maanya Jain",
    author_email="maanya.jain123@gmail.com",
    description="Calculates Topsis Score and Rank them accordingly",
    long_description=long_description,
    keywords=['TOPSIS'],
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/maanya268/Topsis",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires='pandas',
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main"
        ]
    },
)