# rpi_gpio_stub

## Description
A stub library for RPi.GPIO. This allows installation on non-raspberry pi platforms of code that relies on RPi.GPIO.

All methods in the GPIO module do nothing.

## Installation
### Direct
```
pip install git+https://github.com/sanielfishawy/rpio_gpio_stub
```

### Typical pattern
Typical pattern is to specify this package requirements conditionally based on platform:

requirements.txt
```
git+git://github.com/sanielfishawy/rpio/package-two@master#egg=package-two; sys_platform != 'raspberry'
RPi.GPIO == 0.7.0; sys_platform == 'raspberry'
```

```
pip install -r requirements.txt
```

## Usage
Same as RPi.GPIO except that all methods on GPIO do nothing.

```python
from RPi import GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
```


[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)