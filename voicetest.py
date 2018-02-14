from psonic import *
from threading import Thread

def bass():
    for i in range(3):
        sample(LOOP_AMEN)
        sleep(1.75)
    sample(AMBI_DRONE, sustain=2)


def melody():
    for i in range(3):
        use_synth(DSAW)
        play(66)
        sleep(1.75)
    use_synth(DSAW)
    play(78, sustain=2)


def win():
    use_synth(PRETTY_BELL)
    play(68)
    sleep(0.25)
    play(68)
    sleep(0.125)
    play(68)
    sleep(0.125)
    play(68)
    sleep(0.25)
    play(70)
    sleep(0.25)
    play(68)
    sleep(0.25)
    play(70)
    sleep(0.25)
    play(72, sustain=1)


def lose():
    use_synth(TECHSAWS)
    play(68)
    sleep(0.5)
    play(64)
    sleep(0.5)
    play(60, sustain=1)


def what():
    use_synth(TB303)
    play(54, release=1)


if __name__ == '__main__':
    bass_thread = Thread(target=bass)
    mel_thread = Thread(target=melody)
    what()
