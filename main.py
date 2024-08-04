import pygame
import pygame.midi as m
# import time

pygame.init()
m.init()

def main():
    midi_input = None
    for i in range(m.get_count()):
        _interf, name, input_dev, output_dev, _opened = m.get_device_info(i)
        print(m.get_device_info(i))
        if input_dev and b"iCON P1-M V1.05" in name:
            midi_input = m.Input(i)

    if midi_input is None:
        print("iCON P1-M V1.05 is not found.")
        exit(1)

    # time.sleep(1)
    # midi_out = m.Output(m.get_default_output_id())
    # https://qiita.com/Karakuri_Polta/items/dc9aaa5aa6bb901b3439
    # 直前のMIDIポート一覧から仮想デバイスのポート(自分の環境では「IAC Driver My Port」)のIDを確認して、その数値にしてください
    # midi_out.note_on(60, 100)

    while True:
        try:
            if midi_input.poll():
                key_event = midi_input.read(1)
                print(key_event)
            # if key_event[0] == 144:
            #     up_down = "up" if key_event[2] == 80 else "down"
            #     note_dict = {
            #         0: "C",
            #         1: "＃C",
            #         2: "D",
            #         3: "＃D",
            #         4: "E",
            #         5: "F",
            #         6: "＃F",
            #         7: "G",
            #         8: "＃G",
            #         9: "A",
            #         10: "♭B",
            #         11: "B",
            #     }
            #     note = note_dict.get(key_event[1] % 12)
            #     print(note, up_down)
        except KeyboardInterrupt:
            print("\nTerminating Observation...")
            break


if __name__ == "__main__":
    main()
