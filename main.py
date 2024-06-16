def on_received_number(receivedNumber):
    global 相手の数字2
    相手の数字2 = receivedNumber
radio.on_received_number(on_received_number)

def 判定(自分の数字: number, 相手の数字: number):
    if 自分の数字 > 相手の数字:
        music._play_default_background(music.built_in_playable_melody(Melodies.PRELUDE),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_string("WIN")
    elif 自分の数字 == 相手の数字:
        music._play_default_background(music.built_in_playable_melody(Melodies.BA_DING),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_string("DRAW")
    elif 自分の数字 < 相手の数字:
        music._play_default_background(music.built_in_playable_melody(Melodies.PUNCHLINE),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_string("LOSE")
def 初期化():
    global 自分の数字2, 相手の数字2
    自分の数字2 = 0
    相手の数字2 = 0
    for index in range(2):
        basic.show_arrow(ArrowNames.WEST)
        basic.show_arrow(ArrowNames.EAST)

def on_button_pressed_ab():
    global 自分の数字2
    自分の数字2 = randint(1, 10)
    basic.show_number(自分の数字2)
    radio.send_number(自分の数字2)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

自分の数字2 = 0
相手の数字2 = 0
radio.set_group(0)
初期化()

def on_forever():
    if 自分の数字2 != 0 and 相手の数字2 != 0:
        判定(自分の数字2, 相手の数字2)
        初期化()
basic.forever(on_forever)
