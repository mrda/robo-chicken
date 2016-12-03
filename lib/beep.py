
# See http://wiki.micropython.org/Play-Tone for inspiration

# See https://learn.adafruit.com/adafruit-feather-huzzah-esp8266/pinouts
# for Huzzah ESP8266 pinouts

from machine import Pin, PWM
import time

PIEZO_PIN = 14
TEMPO = 5

tones = {
    'B0': 31,
    'C1': 33,
    'CS1': 35,
    'D1': 37,
    'DS1': 39,
    'E1': 41,
    'F1': 44,
    'FS1': 46,
    'G1': 49,
    'GS1': 52,
    'A1': 55,
    'AS1': 58,
    'B1': 62,
    'C2': 65,
    'CS2': 69,
    'D2': 73,
    'DS2': 78,
    'E2': 82,
    'F2': 87,
    'FS2': 93,
    'G2': 98,
    'GS2': 104,
    'A2': 110,
    'AS2': 117,
    'B2': 123,
    'C3': 131,
    'CS3': 139,
    'D3': 147,
    'DS3': 156,
    'E3': 165,
    'F3': 175,
    'FS3': 185,
    'G3': 196,
    'GS3': 208,
    'A3': 220,
    'AS3': 233,
    'B3': 247,
    'C4': 262,
    'CS4': 277,
    'D4': 294,
    'DS4': 311,
    'E4': 330,
    'F4': 349,
    'FS4': 370,
    'G4': 392,
    'GS4': 415,
    'A4': 440,
    'AS4': 466,
    'B4': 494,
    'C5': 523,
    'CS5': 554,
    'D5': 587,
    'DS5': 622,
    'E5': 659,
    'F5': 698,
    'FS5': 740,
    'G5': 784,
    'GS5': 831,
    'A5': 880,
    'AS5': 932,
    'B5': 988,
}


def play_notes(notes):
    n = notes.split(',')
    r = [8] * len(n)
    _play_song(n, r)


def play_mockingjay(dummy):
    notes = ['G5', 'AS5', 'A5', 'D5']
    rhythm = [8, 8, 8, 8]
    _play_song(notes, rhythm)


def _play_song(notes, rhythm):
    try:
        beeper = PWM(Pin(PIEZO_PIN, Pin.OUT), freq=440, duty=512)
        for tone, length in zip(notes, rhythm):
            beeper.freq(tones[tone.upper()])
            time.sleep(TEMPO/length)
    finally:
        beeper.deinit()
