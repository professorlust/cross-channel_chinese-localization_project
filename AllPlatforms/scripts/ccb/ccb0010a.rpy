label ccb0010a:
    call gl(0,"bgcc0006")
    call vsp(0,1)
    with wipeleft
    pause (500.0/1000.0)
    call gl(1,"evcc0011")
    call vsp(1,1)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    play bgm "bgm/bgm013.ogg"
    "冬子は相変わらず教室でぼんやりしていた。"
    "誰と話すでもない。"
    "部活に参加するでもない。"
    "目的もなく、ただそこにいる。"
    太一 "「……」"
    "正しい。"
    "人としてはまっとうだ。"
    "突然、すべてがなくなったんだ。"
    "慣性をもって自らの動力とするしかない。"
    "考えれば皮肉なものだった。"
    "まともな人間たちが全員そろって滅び去り、俺たちだけが生き残った。"
    太一 "「桐原」"
    冬子 "「……」"
    "ふむん。"
    太一 "「ダイアローグ」"
    voice "vfccb0010afyu001"
    冬子 "「？」"
    "一瞬怪訝な顔をするが、すぐに思索の檻に閉じこもる（フリをする）。"
    太一 "「ダイアローグ！」"
    "ゾンビのように言う。"
    太一 "「ダイアローグ、ダイアローグ」"
    太一 "「ダイアローグ！」"
    voice "vfccb0010afyu002"
    冬子 "「なんなのよもーっ！」"
    "対話の怪物。"
    "いや、怪物的な対話。"
    "……にゅ？"
    "まあいい。"
    太一 "「会話会話。対話対話。必要必要」"
    "身振りをまじえて力説する。"
    voice "vfccb0010afyu003"
    冬子 "「……必要ない」"
    太一 "「対話なくして成立しないのだぞ」"
    voice "vfccb0010afyu004"
    冬子 "「……よくわかんない」"
    voice "vfccb0010afyu005"
    冬子 "「話しかけないでよ」"
    voice "vfccb0010afyu006"
    冬子 "「あんたは私のことなんて、どうだっていいんでしょ！」"
    太一 "「そんなことないよ」"
    太一 "「キレイな桐原は好きさ」"
    voice "vfccb0010afyu007"
    冬子 "「アレが！　好きな相手にすることっ！？」"
    太一 "「そう」"
    voice "vfccb0010afyu008"
    冬子 "「ウソ！」"
    太一 "「ホント」"
    voice "vfccb0010afyu009"
    冬子 "「だって、だってだって……」"
    "言葉に詰まる。"
    voice "vfccb0010afyu010"
    冬子 "「話しかけないで」"
    "まくしたてるのをやめたらしい。"
    "不完全燃焼。"
    "話しかけないでと辛口に言われると、話しかけたくなる。"
    "話しかけると、また、話しかけないでと辛口に言われる。"
    menu:
        太一 "「うーむ」"
        "話しかける":
            $B=1
        "部活に行く":
            $B=2
    return
    #