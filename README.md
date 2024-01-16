## Factility Required
### For refreshable display
```shell
arduino*1
breadboard*1
dupont line*many
magnet wire*6
nail*6
6-channel relay*1
3v battery*6
battery box*6
```
<div align="center">
    <a href="./">
        <img src="./figure/arduino.png" width="59%"/>
    </a>
</div>

### For braille typewriter
```shell
a 3d printer
```

## Setup instructions for working environments
```shell
pip install Pillow
pip install keras
pip install tqdm
pip install transformers
pip install torch
```

## Code execution instructions
### For refreshable display
1. install arduino IDE
https://www.arduino.cc/en/software

2. open [braille.ino] through arduino IDE
3. input command in anaconda prompt
```shell
python ImagetoBrailleDisplay.py [your_picture_file] [the model you want to use]
```

example to use model 1:
```shell
python ImagetoBrailleDisplay.py test 1
```

### For braille typewriter
1. input command in anaconda prompt
```shell
flask run
```
2. open the local website
http://127.0.0.1:5000

3. upload the image file
<div align="center">
    <a href="./">
        <img src="./figure/1.png" width="59%"/>
    </a>
</div>

4. convert and download
<div align="center">
    <a href="./">
        <img src="./figure/2.png" width="59%"/>
    </a>
</div>
<div align="center">
    <a href="./">
        <img src="./figure/3.png" width="59%"/>
    </a>
</div>

## Performance details

## Output examples
| Text Input | Braille Typewritter | Char per Second |
| :-- | :-: | :-: |
| i love u | <div align="center"><a href="./"><img src="./figure/refreshable.jpg" width="20%"/></a></div> | 0.375 |

| Text Input | Braille Typewritter | Char per Second |
| :-- | :-: | :-: |
| It was the middle of winter, and the snowflakes were falling like feathers from the sky, and a queen sat at her window working, and her embroidery-frame was of ebony.  a window with snow on it| <div align="center"><a href="./"><img src="./figure/braille_dot.jpg" width="59%"/></a></div> | 0.325 |

## Demo video
For refreshable braille display

https://github.com/Sen1127/Image-Caption-Braille-Display/assets/119402514/299c4f27-5a2f-4671-a8de-dad0b67be1b0

For braille typewriter

https://github.com/Sen1127/Image-Caption-Braille-Display/assets/119402514/175bb788-e69b-4461-a216-ee4ae170d7d6


