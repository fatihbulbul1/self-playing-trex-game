from keras.models import load_model
import numpy as np
from PIL import Image
import keyboard
import time
from mss import mss

mon = {"top":390, "left":730, "width":250, "height":100}
sct = mss()

width = 250
height = 100

model = load_model("trex3.h5")

i = 0
delay = 0.2
while True:
    
    img = sct.grab(mon)
    im = Image.frombytes("RGB", img.size, img.rgb)
    im2 = np.array(im.convert("L").resize((width, height)))
    im2 = im2 / 255
    
    X =np.array([im2])
    X = X.reshape(X.shape[0], width, height, 1)
    r = model.predict(X)
    result = np.argmax(r)
    i+=1
    time.sleep(delay)
    if(i % 40 == 0):
        delay -= 0.05
        if delay < 0.1:
            delay = 0.1
    if result == 0:
        keyboard.press(keyboard.KEY_DOWN)
        
    elif result == 2:
        keyboard.press(keyboard.KEY_UP)