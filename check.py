from random import randint
from PIL import Image
from threading import Thread
import tensorflow as tf
import numpy as np
import time
import cv2
import voicetest

pHand = []


def camcheck():
    # Connect to camera
    camera = cv2.VideoCapture(0)
    # Take picture
    time.sleep(0.2)
    return_value, image = camera.read()
    # Convert to Pillow-usable format
    cv2im = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pilim = Image.fromarray(cv2im)
    pilim.show()
    # Disconnect from camera
    del (camera)
    # Convert to Tensorflow-usable format
    bmp = pilim.convert('L').resize([60, 60])
    hand = np.asarray(bmp).flatten().tolist()
    pHand.append(hand)
    ch_np = np.matrix(pHand).astype(np.float32)
    return ch_np


def check():
    # Intro music
    bass_thread = Thread(target=voicetest.bass)
    mel_thread = Thread(target=voicetest.melody)
    bass_thread.start()
    mel_thread.start()
    time.sleep(7)

    # Import data
    check_img = camcheck()
    real_hand = 0
    cpu_hand = randint(1, 3)
    if cpu_hand == 1:
        rock = Image.open("Hands/Test/Rock/WIN_20171206_18_56_57_Pro.jpg")
        rock.show()
    elif cpu_hand == 2:
        paper = Image.open("Hands/Test/Paper/WIN_20171206_19_15_36_Pro.jpg")
        paper.show()
    else:
        scissors = Image.open("Hands/Test/Scissors/WIN_20171206_18_44_51_Pro.jpg")
        scissors.show()

    # Recreate model
    x = tf.placeholder(tf.float32, [None, 3600])
    w = tf.Variable(tf.zeros([3600, 3]), name='w')
    b = tf.Variable(tf.zeros([3]), name='b')
    y = tf.matmul(x, w) + b

    # Initialize saver
    saver = tf.train.Saver()

    # Check image(s)
    with tf.Session() as sess:
        saver.restore(sess, 'model\my_training-1100')  # TODO Mod source file for previous file changes in handparser.py
        sr = sess.run(y, feed_dict={x: check_img})
        prediction = (sess.run(tf.argmax(sr, 1)))
        if prediction[0] == 0:
            real_hand = 1
        elif prediction[0] == 1:
            real_hand = 2
        else:
            real_hand = 3

    print(real_hand)
    print(cpu_hand)

    def hand_name():
        if real_hand == 1:
            return "ROCK"
        elif real_hand == 2:
            return "PAPER"
        else:
            return "SCISSORS"

    def roshanbo():
        if real_hand == 1 and cpu_hand == 2:
            voicetest.lose()
            print("PAPER BEATS ROCK ... I WIN")
        elif real_hand == 1 and cpu_hand == 3:
            voicetest.win()
            print("ROCK BEATS SCISSORS ... YOU WIN")
        elif real_hand == 2 and cpu_hand == 1:
            voicetest.win()
            print("PAPER BEATS ROCK ... YOU WIN")
        elif real_hand == 2 and cpu_hand == 3:
            voicetest.lose()
            print("SCISSORS BEATS PAPER ... I WIN")
        elif real_hand == 3 and cpu_hand == 1:
            voicetest.lose()
            print("ROCK BEATS SCISSORS ... I WIN")
        elif real_hand == 3 and cpu_hand == 2:
            voicetest.win()
            print("SCISSORS BEATS PAPER ... YOU WIN")
        else:
            voicetest.what()
            print("A %s TIE" % hand_name())

    roshanbo()


if __name__ == '__main__':
    check()
