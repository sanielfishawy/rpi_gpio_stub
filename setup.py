#pylint: disable=invalid-name
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RPi.GPIO",
    version="0.0.1",
    author="Sani Elfishawy",
    author_email="elfishawy.sani@gmail.com",
    description="A stub package to emulate RPi.GPIO for platforms that dont support it. All methods do nothing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sanielfishawy/rpi_gpio_stub",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)