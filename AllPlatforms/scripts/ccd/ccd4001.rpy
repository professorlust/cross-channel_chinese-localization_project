label ccd4001:
    call gl(0,"bgcc0014")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    play bgm "bgm/bgm016.ogg"
    "通過して、美希の住んでいる団地方面に向かう。"
    "坂の下から小走りに駆けてくる美希。"
    "俺を見つける。"
    "駆け出す。"
    "こっちに向かって。"
    "蹴つまずきながら。"
    voice "vfCCD0001mki000"
    美希 "「うわ～～～～～～んっ！！」"
    "泣く。"
    "胸に飛び込んできた。"
    call gl(0,"evcc0040")
    call vsp(0,1)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    "受け止めた。"
    voice "vfCCD0001mki001"
    美希 "「せんぱい、せんぱいせんぱいせんぱーーーーーいっ！！」"
    voice "vfCCD0001mki002"
    美希 "「誰もいないよ～～～～～～っ！　おかしいよ～～～～～～っ、こんなの絶対おかしいよ～～～～～～っ！！」"
    太一 "「……う、うん」"
    voice "vfCCD0001mki003"
    美希 "「どこの家にも誰もいないです！　ほんとに誰もいないんです、いなくなっちゃってます！！」"
    太一 "「そうだな。困ったな」"
    "背を叩いてなだめる。"
    voice "vfCCD4001mki000"
    美希 "「どういうことっすか……こんなこと、あったらだめです……」"
    "小さいやつ。"
    "無敵の美希に育つのに、どれだけの幸福と偶然と時間が必要なのだろう。"
    太一 "「俺がいるだろ」"
    voice "vfCCD0001mki005"
    美希 "「……うううっ、はい……よかった……いてくれて……」"
    voice "vfCCD0001mki006"
    美希 "「朝おきて、お母さんとかいなくて、ごはんもなくて……そんでみんなまでいなくなってたらって考えたら……」"
    太一 "「恐くなっちゃったか」"
    "額をすりつけるよう、こくこくと頷く。"
    voice "vfCCD0001mki007"
    美希 "「いやです、こんなの……わたし、いや……」"
    太一 "「やっぱり人がいないと寂しいよな」"
    voice "vfCCD0001mki008"
    美希 "「……帰りたい……」"
    太一 "「帰りたいか」"
    voice "vfCCD0001mki009"
    美希 "「帰りたい、帰りたい……」"
    太一 "「そうか、帰りたいか」"
    voice "vfCCD4001mki001"
    美希 "「霧ちんに会いたい……他のみんなにも……」"
    "ハンカチを渡す。"
    "みるみる染みを作った。"
    "こぼれる少女の涙は、張力に丸まって真珠のよう。"
    太一 "「霧ちんかぁ」"
    "一週間。"
    "すべては日曜日だ。"
    call gl(0,"bgcc0011")
    call vsp(0,1)
    with wipeleft
    call gl(1,"TCYM0002|TCYM0002")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki002"
    美希 "「えぐえぐえぐ」"
    "ずっと泣きっぱなしだ。"
    "手を繋いで学校に来てしまった。"
    太一 "「あのさ、俺はちょっと用事があるんだけど、美希はどうする？」"
    voice "vfCCD4001mki003"
    美希 "「ここで霧待ちします」"
    太一 "「……そう」"
    太一 "「じゃあまた」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki004"
    美希 "「あ、用事終わったあと、まだ用事あるんですか？」"
    "腕振り振り、そう言う。"
    太一 "「ないよ」"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki005"
    美希 "「じゃ、ここで待ってるんで……ここに……」"
    太一 "「どうせなら教室で待ってたら？」"
    voice "vfCCD4001mki006"
    美希 "「……人のいない建物に、入りたくないんです……息が、詰まりそうで」"
    太一 "「わかった。じゃすぐ済ませるから」"
    voice "vfCCD4001mki007"
    美希 "「あ、ハンカチも……弁償します、お金以外で」"
    "何でだ。"
    "ついセクハラ魂がわきあがる。"
    太一 "「いいさ。女の子を泣かせたままにしておくハンカチじゃないんだよ」"
    voice "vfCCD4001mki008"
    美希 "「……ぐす」"
    "効果覿面だ。"
    stop bgm
    call gl(0,"bgcc0006")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    "教室。"
    call gl(5,"evcc0027s")
    call vsp(5,1)
    with dissolve
    call vsp(0,1)
    call vsp(5,0)
    with Dissolve(500.0/1000.0)
    play bgm "bgm/bgm021.ogg"
    "霧はいない。"
    "もう、いない。"
    "何度繰り返そうが、霧があらわれることは永遠にない。"
    "永遠という言葉さえ矛盾に追いやって、俺と霧は繋がる術さえない。"
    "彼女たちを利用して心に糧をたくわえる俺に科せられた、当然の罰。"
    "罰。"
    "×。"
    "ＣＲＯＳＳ。"
    "けどもう、交差はできないんだ―――"
    太一 "「けど……どう説明する？」"
    "美希に。"
    "頭が痛い。"
    stop bgm
    call gl(0,"bgcc0011")
    call vsp(0,1)
    with wipeleft
    play bgm "bgm/bgm015.ogg"
    "正門に戻る。"
    "美希は膝頭に頭を入れて、うずくまっていた。"
    太一 "「……美希、来たよ」"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki009"
    美希 "「…………先輩、霧が来ません」"
    太一 "「休みなんじゃないかなあ」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki010"
    美希 "「じゃあ家に……いる？」"
    太一 "「さあ、どうだろう、出かけているかもしれない」"
    voice "vfCCD4001mki011"
    menu:
        美希 "「……行きます」"
        "デートに誘う":
            $B=1
        "霧の家につきあう":
            $B=2
    return
    #