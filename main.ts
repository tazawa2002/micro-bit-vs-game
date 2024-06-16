radio.onReceivedNumber(function (receivedNumber) {
    相手の数字 = receivedNumber
})
function 判定 (自分の数字: number, 相手の数字: number) {
    if (自分の数字 > 相手の数字) {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Prelude), music.PlaybackMode.InBackground)
        basic.showString("WIN")
    } else if (自分の数字 == 相手の数字) {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.BaDing), music.PlaybackMode.InBackground)
        basic.showString("DRAW")
    } else if (自分の数字 < 相手の数字) {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Punchline), music.PlaybackMode.InBackground)
        basic.showString("LOSE")
    }
}
function 初期化 () {
    自分の数字 = 0
    相手の数字 = 0
    for (let index = 0; index < 2; index++) {
        basic.showArrow(ArrowNames.West)
        basic.showArrow(ArrowNames.East)
    }
}
input.onButtonPressed(Button.AB, function () {
    自分の数字 = randint(1, 10)
    basic.showNumber(自分の数字)
    radio.sendNumber(自分の数字)
})
let 自分の数字 = 0
let 相手の数字 = 0
radio.setGroup(255)
初期化()
basic.forever(function () {
    if (自分の数字 != 0 && 相手の数字 != 0) {
        判定(自分の数字, 相手の数字)
        初期化()
    }
})
