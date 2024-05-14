import pygame.midi
import time

pygame.init()
pygame.midi.init()


def main():
    midi_input = None
    for i in range(pygame.midi.get_count()):
        _interf, name, input_dev, _output_dev, _opened = pygame.midi.get_device_info(i)
        if input_dev and b"yamaha_pss_a50" in name:
            midi_input = pygame.midi.Input(i)

    if midi_input is None:
        print("Yamaha PSS-A50 is not found.")
        exit(1)

    while True:
        if midi_input.poll():
            key_event = midi_input.read(1)[0][0]
            if key_event[0] == 144:
                up_down = "up" if key_event[2] == 80 else "down"
                note_dict = {
                    0: "C",
                    1: "＃C",
                    2: "D",
                    3: "＃D",
                    4: "E",
                    5: "F",
                    6: "＃F",
                    7: "G",
                    8: "＃G",
                    9: "A",
                    10: "♭B",
                    11: "B",
                }
                note = note_dict.get(key_event[1] % 12)
                print(note, up_down)


if __name__ == "__main__":
    main()
