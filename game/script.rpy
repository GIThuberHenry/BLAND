# Characters declaration start
define e = Character("Eileen")
define claire = Character("Claire", style="clairestyle", image="claire_profile")
define nava = Character("Nava", style="navastyle", image="nava_profile")
define ciel = Character("Ciel", style="cielstyle",image="ciel_profile")
define theo = Character("Theo", style="theostyle", image="theo_profile")
define you = Character("[defname]",style="mcstyle", image="you")
# Character declaration end

# NVL characters are used for the phone texting
define n_nvl = Character("", kind=nvl, callback=Phone_SendSound)
define nvl_theo = Character("Theo", kind=nvl, callback=Phone_ReceiveSound)
define nvl_ciel = Character("Ciel", kind=nvl, callback=Phone_ReceiveSound)
define nvl_claire = Character("Claire", kind=nvl, callback=Phone_ReceiveSound)
define nvl_nava = Character("Nava", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)
# NVL end

# Char style start
style mcstyle:
    xpos 90
    ypos 10
    outlines [ (2, "#fff", absolute(0), absolute(0)) ]
    color "#000000"
    bold True
    size 50
    font "fonts/Bryndan_Write.ttf"
style clairestyle:
    xpos 90
    ypos 10
    outlines [ (2, "#fff", absolute(0), absolute(0)) ]
    color "#5D4D6C"
    size 50
    font "fonts/Bryndan_Write.ttf"
style navastyle:
    xpos 90
    ypos 10
    outlines [ (2, "#fff", absolute(0), absolute(0)) ]
    color "#C4BBED"
    bold True
    size 50
    font "fonts/Bryndan_Write.ttf"
style cielstyle:
    xpos 90
    ypos 10
    outlines [ (2, "#fff", absolute(0), absolute(0)) ]
    color "#896160"
    bold True
    size 50
    font "fonts/Bryndan_Write.ttf"
style theostyle:
    xpos 90
    ypos 10
    outlines [ (2, "#fff", absolute(0), absolute(0)) ]
    color "#D58D3B"
    bold True
    size 50
    font "fonts/Bryndan_Write.ttf"
transform boystyle:
    zoom 0.5
    xalign 0.5
    yalign 1.0
transform girlstyle:
    zoom 0.5
    xalign 0.5
    yalign 1.0
transform shake:
        ease .04 yoffset 16
        ease .04 yoffset -16
        ease .03 yoffset 12
        ease .03 yoffset -12
        ease .02 yoffset 8
        ease .02 yoffset -8
        ease .01 yoffset 4
        ease .01 yoffset -4
        ease .01 yoffset 0
# Char style end

# setting transisi side img
transform change_transform(old,new):
    contains:
        old
        alpha 1.0
        xalign 0.0 yalign 1.0
        linear 0.3 alpha 0.0
    contains:
        new
        alpha 0.0
        xalign 0.0 yalign 1.0
        linear 0.3 alpha 1.0
define config.side_image_change_transform = change_transform


# Variable declaration start
default persistent.ending = 0
default persistent.test = 0
default loop = 0
define nameinput = VariableInputValue(variable = "defname", returnable = True)
define defname = "Jack"
default ending_desc = 0
default optimisme = 0
# Variable declaration end

# Change main menu img start
image main_menu_check:
    At("gui/main_menu2.png") 
    pause 2
    At("gui/main_menu2.png", glitch) 
    pause 2
    At("gui/main_menu.png", chromatic_offset)
    pause 0.05
    At("gui/main_menu2.png", glitch)
    pause 0.1
    At("gui/main_menu.png", chromatic_offset)
    pause 0.05
    At("gui/main_menu.png", glitch)
    pause 0.5
    At("gui/main_menu2.png", chromatic_offset)
    pause 1.5
    repeat
# Change main menu img end

# image class start
image claire glitched:
    At("claire base", glitch)
    pause 0.2
    At("claire glitch", chromatic_offset)
    pause 0.05
    At("claire dead", glitch)
    pause 0.1
    At("claire glitch", chromatic_offset)
    pause 0.05
    At("claire glitch", glitch)
    pause 0.1
    At("claire dead", chromatic_offset)
    pause 0.5
    At("claire base")
image nava glitched:
    At("nava base", glitch)
    pause 0.2
    At("nava glitch", chromatic_offset)
    pause 0.05
    At("nava dead", glitch)
    pause 0.1
    At("nava glitch", chromatic_offset)
    pause 0.05
    At("nava glitch", glitch)
    pause 0.1
    At("nava glitch", chromatic_offset)
    pause 0.5
    At("nava base")
image ciel glitched:
    At("ciel base", glitch)
    pause 0.2
    At("ciel glitch", chromatic_offset)
    pause 0.05
    At("ciel dead", glitch)
    pause 0.1
    At("ciel dead", chromatic_offset)
    pause 0.05
    At("ciel glitch", glitch)
    pause 0.1
    At("ciel glitch", chromatic_offset)
    pause 0.5
    At("ciel base")
image side you = "images/chara/you/side you profile.png"
image side you angry = "images/chara/you/side you angry.png"
image side you basetalk = "images/chara/you/side you basetalk.png"
image side you blush= "images/chara/you/side you blush.png"
image side you crazy= "images/chara/you/side you crazy.png"
image side you exited= "images/chara/you/side you exited.png"
image side you sad = "images/chara/you/side you sad.png" 
# image class end

# screens start

# screen viewport_walkthrough():
#     # modal True
#     frame:
#         xalign 0.5
#         background "box"
#         area(1420,100,500,200)    
#         viewport:
#             mousewheel True
#             scrollbars "vertical"
#             draggable True      
#             vbox:
#                 text "{size=20}Ending 'Ignorance is a bliss' (Neutral Ending){/size}"
#                 text "{size=20}Cara:{/size}"
#                 text "{size=20}jangan menghadiri rapat sama sekali{/size}"
#                 text ""

#                 text "{size=20}Ending 'Am i Dreaming' (Neutral ending){/size}"
#                 text "{size=20}Cara:{/size}"
#                 text "{size=20}Sarapan terlebih dahulu, dan tetap masuk rapat {/size}"
#                 text ""

#                 text "{size=20}Ending 'Hero' (Good Ending){/size}"
#                 text "{size=20}Cara: {/size}"
#                 text "{size=20}-menjawab 3 choice yang optimis{/size}"
#                 text "{size=20}-menjawab 2 choice yang optimis dan menerima bantuan ciel saat kamu sakit{/size}"
#                 text ""
                    
#                 text "{size=20}Ending 'Consequences Of Neglection' (Bad Ending){/size}"
#                 text "{size=20}Cara:{/size}"
#                 text "{size=20}-tidak menerima bantuan ciel saat kamu sakit{/size}"
#                 text "{size=20}-tidak mengerjakan tugas saat di rumah{/size}"
#                 text ""

#                 text "{size=20}True ending{/size}"
#                 text "{size=20}Cara:{/size}"
#                 text "{size=20}menjawab 1 atau kurang choice yang optimis dan menerima bantuan ciel saat kamu sakit{/size}"

screen dabutton():
    zorder 100
    hbox xalign 1.0 yalign 0.0:
        imagebutton auto "gui/button/setting/save_%s.png" action [Play("sound","audio/click.ogg"),ShowMenu("save")]
        imagebutton auto "gui/button/setting/load_%s.png" action [Play("sound","audio/click.ogg"),ShowMenu("load")]
        imagebutton auto "gui/button/setting/setting_%s.png" action [Play("sound","audio/click.ogg"),ShowMenu("preferences")]
    vbox:
            xalign 0.88
            ypos 840
            imagebutton auto "gui/button/setting/history_%s.png" action [Play("sound","audio/click.ogg"),ShowMenu('history')]
            imagebutton auto "gui/button/setting/auto_%s.png" action [Play("sound","audio/click.ogg"),Preference("auto-forward", "toggle")]
            imagebutton auto "gui/button/setting/skip_%s.png" action Skip() alternate Skip(fast=True, confirm=True)
screen reset_var():
    textbutton "Aku menyesal":
        xalign 0.3
        yalign 0.5
        text_color "ffffff"
        text_hover_color "0000FF"
        action [SetVariable('persistent.test',0),Jump('ending_check')] 
# screeen ends

label splashscreen: 
    scene black with Pause(1)
    if persistent.test == 0:
        # play sound start2
        # centered "{size=+10}{color=#FFFFFF}{font=fonts/Bryndan_Write.ttf}{color=#fd5800}{b}BLAND{/b}{/color}{/font} bukanlah permainan untuk anak-anak atau orang yang mudah ketakutan.{/color}{/size}{w=4.0}{nw}" with dissolve 
        play music start
        centered "{size=+40}{color=#FFFFFF}{font=fonts/Bryndan_Write.ttf}{color=#fd5800}{b}BLAND{/b}{/color}{/font} merupakan game bertemakan \n{font=fonts/bloody.ttf}{color=#be0000}{i}PSYCHOLOGICAL HORROR{/i}{/color}{/font}!{/color}{/size}{fast}{w=3.0}{nw}" with dissolve
        play music start2
        centered "{font=fonts/helpme.ttf}{size=+50}{color=#FFFFFF}{color=#be0000}{size=+10}You{/size}{/color} have been warned{/color}{/size}{/font}{fast}{w=3.0}{nw}" with dissolve
        $ config.main_menu_music = "audio/Rabbit_prince.wav"
    elif persistent.test == 1:
        $ config.main_menu_music = "audio/glitchterror.wav"
        centered "{color=#ffffff}Selamat datang kembali, Kamu tidak perlu akau peringati lagi....{/color}{w=5.0}{nw}"
    else:
        $ config.main_menu_music = "audio/glitchterror.wav"
        centered "{color=#ffffff}im concerned now...what happened?{/color}{w=4.0}{nw}"
    return

screen input_name():
    text "Siapa namaku?":
        xalign 0.5 
        yalign 0.3 
    input:
        xalign 0.5
        yalign 0.4
        pixel_width 160
        value nameinput
        default_focus True
        size 42

    textbutton "OK":
        xalign 0.5
        yalign 0.5
        text_size 60
        action [Play("sound","audio/click.ogg"),Return()]

label start:
    call intro from _call_intro
    if persistent.test == 1:
        jump epilogue
    call prologue from _call_prologue
    call chapter1a from _call_chapter1a
    call chapter1b from _call_chapter1b
    call chapter2a from _call_chapter2a
    call chapter2b from _call_chapter2b
    call kamar from _call_kamar
    # menu:
    #     "testground":
    #         jump testground
    #     "dont":
    #         "ok"
    #         call kamar
    return

label intro:
    stop music fadeout 1.5
    scene black
    pause 2.0
    if persistent.test == 1:
        nvl_narrator "Kampus... "
        nvl_narrator "Sekarang...."
        nvl_narrator "Juga"
        return
    nvl_narrator "{size=30}Theo is on the line{/size}"
    nvl_theo "{size=30}Hey! ini Theo{/size}"
    nvl_theo "{size=30}Aku mau umumin, besok kita ada rapat di kampus{/size}"
    nvl_theo "{size=30}Tempatnya di kelas kita kemarin.{/size}"
    nvl_theo "{size=30}Jangan lupa datang ya!{/size}"
    n_nvl "{size=30}Ok!"
    nvl_theo "{size=30}Maaf banget nih nomor kamu aku baru save{/size}"
    nvl_theo "{size=30}Padahal kita udah agak lama kenalan.{/size}"
    n_nvl "{size=30}Gapapa, santai aja{/size}"
    n_nvl "{size=30}Kita sebelumnya tidak pernah sempat tukar nomor juga.{/size}"
    nvl_theo "{size=30}Nomor kamu mau aku namain apa?{/size}"
    nvl_theo "{size=30}Hehe{/size}"
    n_nvl "{size=30}hmm...{/size}"
    call screen input_name()
    if defname == "Jack":
        n_nvl "{size=30}Pakai nama asliku saja.{/size}"
        nvl_theo "{size=30}'Jack' aja?{/size}"
    else:
        n_nvl "{size=30}'[defname]', Simpan pakai '[defname]' aja.{/size}"
        nvl_theo "{size=30}Hmm...{/size}"
        nvl_theo "{size=30}Namanya keren juga.{/size}"
        nvl_theo "{size=30}Mulai sekarang aku panggil '[defname]' aja gimana? hehe.{/size}"
        n_nvl "{size=30}haha, terserah kamu aja deh.{/size}"
    nvl_theo "{size=30}Baiklah kalau begitu{/size}"
    nvl_theo "{size=30}Aku mau hubungi teman-teman lainnya{/size}"
    nvl_theo "{size=30}Makasih ya! Sampai ketemu besok.{/size}"
    nvl_narrator "{size=30}Theo logged off{/size}"
    "Theo mengajakku untuk mengikuti rapat."
    "Mungkin ini rapat untuk projek gamenya yang aku janji bantu kemarin."
    centered "{size=+50}{color=#FFFFFF}Keesokan Harinya{/color}{/size}"
    return
screen tes():
        text "STAY HERE!":
            text_align 0.5
            xalign 0.5
            yalign 0.2
            size 300
            color "#bd0202ff"
            outlines [ (10, "#500000", 5, 10) ]
            font "fonts/BLOODY.ttf"
label firstmenu():
    if persistent.test == 1:
        stop music
        menu:
            "Apa yang harus kulakukan sekarang?{fast}"
            "Mencari sarapan sebelum rapat":
                show screen tes()
                show bg outside_glitch
                call firstmenu() from _call_firstmenu
            "Langsung ke kelas menemui Theo":
                stop music
                hide screen tes
                hide entity3
                show bg outside
                "Aku sudah berjanji untuk menemui Theo hari ini"
                "Sebaiknya tidak membuatnya menunggu."
            "Balik kerumah aja":
                show screen tes()
                play sound whisper1
                show bg outside_glitch
                show entity3
                call firstmenu() from _call_firstmenu_1
    else:
        menu:
            "Apa yang harus kulakukan sekarang?"
            "Mencari sarapan sebelum rapat":
                "Mungkin sebaiknya aku pergi mencari makanan terlebih dahulu"
                "Rapat Theo bisa menunggu, sebaiknya aku mencari makan dahulu"
                play sound footstep volume 1.0
                scene bg canteen with Dissolve(4)
                "Antrian yang cukup panjang{w=0.05}.{w=0.05}.{w=0.05}."
                "Aku harap mereka masih dalam kelas"
                play sound footstep volume 1.0
                scene black with fade
                play music afternoon_waltz fadein 5.0
                "Phew... Sarapan tadi membuatku merasa bersemangat"
                "Aku harus bergegas ke kelas sekarang-"
                stop music
                play audio opendoor2
                "! ! !"
                "Aku melihat sesorang gadis masuk kedalam kelas yang dipakai buat rapat."
                play music heartbeat volume 0.5
                scene bg classhall with Dissolve(2.5)
                jump secondmenu
            "Langsung ke kelas menemui Theo":
                "Aku sudah berjanji untuk menemui Theo hari ini"
                "Sebaiknya tidak membuatnya menunggu."
            "Balik kerumah aja":
                "Ugh, apa yang kupikirkan kemarin?"
                "Kenapa aku ingin membantu Theo?"
                "Aku juga tidak yakin aku bisa membantunya, Sebaiknya aku pulang saja"
                $ ending_desc = 1
                jump ending_check
    return

label epilogue:
    scene bg outside with Dissolve(3)
    "Sesampainya aku di kampus."
    call firstmenu from _call_firstmenu_2
    play sound opendoor
    play music glitchmenu fadein 5.0
    scene black with fade
    scene bg class2 with ImageDissolve("open_door1.png", 4.5, ramplen=256)
    # show screen dabutton()

    "Tidak ada siapa-siapa disini..."
    "Huh? kenapa aku kesini?"
    "Aku tidak mengingat mempunyai urusan disini."
    jump timeloop

label timeloop:
    hide screen reset_var
    scene black 
    if loop == 0:
        scene bg garden with dissolve
    if loop == 0:
        "Aku melihat seorang wanita di depanku...."
    show claire base at girlstyle 
    if loop == 0:
        "Hey...{w=0.5}{nw}"
    window hide
    show claire glitched
    play sound glitch1
    "???" "Dasar pembunuh!{w=0.2}{nw}"
    
    scene black 
    if loop == 0:
        scene bg canteen with dissolve
    if loop == 0:
        "Aku melihat seorang wanita di depanku...."
    show nava base at girlstyle 
    if loop == 0:
        "Hey...{w=0.5}{nw}"
    window hide
    show nava glitched
    play sound glitch2
    "???" "Psikopat!{w=0.2}{nw}"

    scene black 
    if loop == 0:
        scene bg bridge with dissolve
    show ciel base at girlstyle 
    window hide
    show ciel glitched
    play sound glitch3
    if loop == 0:
        "Gimana? sudah sadar? atau masih belum tau apa-apa?"
    elif loop == 1:
        "Kamu sebenarnya cuman berhalusinasi. Hal-hal yang kamu lakukan bersama Theo, Claire, Ciel, Nava, Tugas-Tugasmu, bahkan Ending-ending lainnya, Semuanya halusinasi"
    elif loop == 2:
        "Tapi... Mayat yang ada dikamarmu, si Hendry... bukanlah halusinasi."
    elif loop == 3:
        "Keirianmu membunuh seseorang yang dicintai 'teman-temanmu'. Berharap kamu dipilih sebagai penggantinya untuk mengerjakan Projek tersebut."
    elif loop == 4:
        "Mungkin kau hanya cemburu kalau orang tersebut memiliki kemampuan yang jauh lebih tinggi daripadamu."
    elif loop == 5:
        "Dengan terbunuhnya orang tersebut kamu harap, kamu akan menjadi penggantinya?"
    elif loop == 6:
        "Mereka telah membatalkan projek tersebut dan semua yang telah kamu lewati hanyalah halusinasi saja."
    elif loop == 7:
        "Apakah kamu sudah sadar akan perbuatanmu?"
    elif loop == 8:
        "Apakah kamu menyesal?"
    elif loop == 9:
        "Mungkin aku akan memberikanmu kesempatan untuk enyah dari game ini dan melupakan semua apa yang terjadi, tunggu loop berikutnya lagi."
    elif loop == 10:
        $ ending_desc = 3
        show screen reset_var()
        "ku beri kamu 10 detik...{w=1}{nw}"
        "9{w=1}{nw}"
        "8{w=1}{nw}"
        "7{w=1}{nw}"
        "6{w=1}{nw}"
        "5{w=1}{nw}"
        "4{w=1}{nw}"
        "3{w=1}{nw}"
        "2{w=1}{nw}"
        "1{w=1}{nw}"
        "0{w=1}{nw}"
    elif loop == 11:
        "tampaknya kamu melewati kesempatanmu, kuharap kamu bisa menunggu dari awal lagi"
        $ loop = 0
        
    $ loop = loop + 1
    call timeloop from _call_timeloop

label prologue:
    scene bg outside with Dissolve(3)
    "Sesampainya aku di kampus."
    call firstmenu from _call_firstmenu_3
    play sound opendoor
    play music childhood_memories fadein 5.0
    scene black with fade
    scene bg class2 with ImageDissolve("open_door1.png", 4.5, ramplen=256)
    show screen dabutton()
    # show screen viewport_walkthrough()

    "Di dalam kelas aku melihat Theo dan dua orang lainnya"
    "Salah satu dari mereka mungkin aku kenal, tapi aku tidak terlalu ingat."
    "tetapi seorang lagi..."
    "Aku tidak begitu mengenalnya,"
    "Akupun tidak pernah melihatnya di kelas juga."
    "Apa mungkin dia murid baru?"

    
    show theo base at boystyle with dissolve
    theo "Hey [defname]! Selamat datang!"
    theo "Makasih banyak sudah mau bantu loh!"

    show theo sad at boystyle
    theo "Nyari orang yang mau posisi role ini sulit banget."
    theo "Kami hampir saja menyerah."
    you basetalk "Senang bisa membantu, Theo."

    show theo happy 
    theo "Berkatmu, proyek kami bisa dilanjuti lagi!"

    show theo idle with move:
        xoffset -650
    
    show claire idle at girlstyle with Dissolve(1.0)
    show claire exited
    "???" "Wah! Akhirnya datang juga!"

    show claire basetalk
    "???" "Kami baru saja membicarakan tentangmu dan kami telah mendengar banyak tentangmu dari Theo."
    claire "Kenalin, namaku Claire!"

    show claire idle
    you basetalk "Hai Claire! Salam kenal!"
    you basetalk "hmm.. Apakah kita pernah bertemu sebelumnya?"

    show claire basetalk
    claire "Huh.. sepertinya tidak"
    claire "Sama sepertimu dan Theo, kita seumuran hanya saja aku dari kelas lain."
    claire "Mungkin kamu pernah melihatku di suatu tempat sebelumnya."
    claire "tapi..."

    show claire happy
    claire "Aku harap kita bisa kenal lebih dekat~"
    
    show claire idle
    you blush  "te-tentu saja.."

    show claire idle with move:
        xalign 1.1

    show ciel idle at girlstyle with Dissolve(1.0)
    show ciel base
    "???" "hmm?"
    show ciel happy
    "???" "Pengganti programmer baru yah?"

    show ciel idle
    you basetalk "Mhm."

    show ciel excited
    ciel "Aku Ciel, senang bisa berkenalan denganmu."
    ciel "Akhirnya dengan kedatanganmu, beban pekerjaan akan berkurang."

    show ciel idle
    you basetalk "berkurang? apakah kamu programmer juga?"

    show ciel basetalk
    ciel "Yep, aku juga programmer di projek ini sama sepertimu."
    show ciel uneasy
    ciel "Tapi aku masih belum mahir dalam bidang ini."
    show ciel idle

    show theo basetalk
    theo "haha, sebagai murid baru kamu sudah melampaui banyak teman-teman kelas kamu."
    theo "Dan seperti kita ketahui juga, bidang kamu memiliki pekerjaan yang paling berat diantara kami."
    show theo happy
    theo "Oleh karena itu, aku mengajak [defname] untuk membantu dalam pekerjaanmu"
    
    menu:
        theo "Kamu pun bersedia untuk mengajari Ciel juga kan, [defname]?"
        "Tentu Saja! (optimis)":
            show theo idle
            you exited "Tentu saja, kamu dapat mengandalkan aku, Ciel!"
            show ciel blush
            ciel "Ma-makasih, mohon bantuannya, [defname]."
            $ optimisme = optimisme + 1
        "Aku juga masih belajar (pesimis)":
            show theo idle
            you basetalk "Aku juga masih belajar, semoga kita dapat saling membantu kedepannya."
            show ciel happy
            ciel "Tentu saja!"
    
    show ciel happy
    ciel "Kuharap kita dapat bekerja sama dengan baik kedepannya."
    show ciel idle
    return

label chapter1a:
    show theo basetalk 
    theo "Baiklah, kita seharusnya sudah mulai bahas terkait projek, tapi..."
    show theo idle

    show claire angry
    claire "Nava terlambat lagi."
    claire "Atau mungkin kamu lupa memberitahu Nava tentang rapat hari ini, Theo?"
    show claire angryidle

    show theo sad
    theo "Aku yakin banget aku memberitahu Nava tentang rapat ini"
    theo "Tapi..."
    theo "Dia hanya membaca pesanku saja, tidak ada balasan apapun."
    theo "Apa mungkin dia lupa?"
    show theo sadidle

    show ciel uneasy
    ciel "Nava emang gitu, dia suka terlambat walaupun udah janjian."
    show ciel basetalk
    ciel "Haruskah kita mencarinya? kalau jam gini biasanya dia ada di kantin sih."
    show ciel idle
    
    "Nava? apakah dia anggota projek ini juga?"
    "Namanya tidak begitu famiiar jug-"
    play sound lapar
    pause 1.0
    "Sial, hari ini aku lupa sarapan."
    "Mungkin aku bisa menggunakan kesempatan ini untuk..."
    "Membeli makan dan mencari si Nava di kantin"
    you basetalk "Mungkin aku bisa bantu mencari si Nava."
    show theo idle
    show claire idle

    show ciel happy
    ciel "Oh! kita semua bisa mencarinya bersama."
    show ciel idle

    show theo basetalk
    theo "Hmm, sebaiknya kita tunggu aja, aku takut kita akan kelamaan mencarinya."
    show theo idle

    you basetalk "Aku bisa mencarinya sendiri kok, tidak apa-apa."

    show claire uneasy
    claire "Kamu yakin?"
    claire "Emangnya kamu tahu Nava orangnya yang mana?"
    show claire uneasyidle

    you basetalk "Serahkan padaku, aku hanya perlu tau karakteristik Nava aja."

    show theo basetalk
    theo "Hmm, yaudah kalau begitu."
    theo "Nava harusnya ada dikantin seperti kata Ciel."
    show theo idle

    show ciel basetalk
    ciel "Nava memiliki rambut berwarna ungu,"
    ciel "Dan... rambutnya panjang"
    ciel "Dan umm..."
    show ciel idle

    show theo basetalk
    theo "Jangan lupa matanya,"
    theo "Nava memiliki mata yang unik"
    theo "mata cerah seperti emas yang berkilau"
    show theo idle

    show claire basetalk
    claire "Dengan keunikan itu, mungkin kamu dapat menemukannya dengan mudah."
    show claire happy
    claire "Semangat mencari ya~"
    show claire happyidle
    you basetalk "Baiklah aku akan pergi mencari Nava Sekarang."
    return
label chapter1b:
    play sound opendoor
    scene black with fade
    stop music fadeout 5.0
    scene bg classhall with ImageDissolve("open_door3.png",4.5,ramplen=256)
    "Rambut ikat dua dengan warna ungu "
    "Dan mata yang unik."
    "Orang yang cukup menarik..."
    "Tapi sebaiknya aku membeli makan aja dulu"
    scene black with fade
    pause 1.0
    play music tea_time fadein 5.0
    scene bg canteen with Dissolve(4.5)
    play sound chatters fadein 10.0 loop
    "Hmm... Makan apa ya.."
    "Aku harus bergegas, aku tidak mau membuat yang lain menunggu di kelas."
    "Mungkin aku akan membeli roti sambil mencari orang dengan rambut warna... mata warna..."
    "Duh, warna apa ya?"
    "Sial aku lupa"
    "Mungkin dengan melihat sekeliling aku bisa mengingat kembali."
    stop music fadeout 1.0
    play audio bump
    show bg canteen with hpunch
    "!!!"
    "Seseorang menabrakku."
    play music biscuit_town fadein 5.0
    show nava uneasy at girlstyle with moveinright
    you sad "Uh-Hai, kamu baik baik saja?"
    nava "ah-uh iya aku baik-baik saja, haha-ha..."
    nava "{size=30}Sial rotiku jatuh{/size}"
    show nava sad
    nava "{size=30}Aku gak mau membelinya lagi...{/size}"
    "Gadis itu tampak kecewa, aku mulai merasa bersalah."
    hide nava sad with moveoutbottom
    show bg canteen with vpunch
    "!!!"
    "Gadis itu mengambil kembali roti miliknya yang sudah jatuh di lantai."
    "Tetapi tidak dibuang ke tempat sampah."
    show nava sad at girlstyle with moveinbottom
    you sad "Umm... "
    you sad "Bukankah rotinya sudah kotor? Jangan bilang kamu berencana untuk memakannya."
    nava "Aku gak mau membelinya lagi, lebih baik aku makan daripada kebuang sia-sia."

    "Aku bergegas merebut roti tersebut dari tangannya dan membuangnya ke tempat sampah."
    show nava angry at shake
    nava "HEY! ROTIKU!-"
    you angry "Aku akan membelikanmu roti yang baru, kamu tidak perlu memakan roti kotor yang ini."
    show nava uneasy
    nava "Tapi- Tapi-"
    you sad "Aku merasa bersalah juga, tidak apa-apa."
    nava "Tapikan- Aku yang-"
    hide nava uneasy with moveoutleft
    "Aku meninggalkannya dan segera membelikan dua roti yang sama seperti roti yang jatuh milik gadis itu."
    show bg canteen with fade
    show nava uneasy at girlstyle with moveinright
    nava "Hey-uhh... Kamu tidak perlu-"
    "Aku langsung memberikan roti yang telah kubeli ke gadis tersebut."
    you basetalk "Nih roti kamu."
    show nava uneasy with move:
        yoffset 120
    pause 0.2
    show nava uneasy with move:
        yoffset 0
    nava "Te-terima kasih..."
    you exited"Sama-sama."
    you basetalk"Aku harus pergi mencari seseorang, sampai bertemu lag-"
    show nava uneasy with vpunch:
        zoom 0.55
    nava "TUNGGU!"
    show nava blush at girlstyle
    nava "Umm... Nama Kamu siapa?"
    you basetalk "Huh? oh-uhh.. [defname]."
    you basetalk"Kalau kamu?"
    nava "Nava, namaku Nava."
    "Na...va,{w=1} Na..va{w=1}, Nava....{w=1} Na....{w=1}Va...{nw}"
    play audio ping 
    show bg canteen with vpunch
    you basetalk "OH! Akhirnya ketemu kamu juga!"
    show nava uneasy 
    nava "ketemu...{w=0.5}aku? Maksud kamu?"
    you "Kamulah orang yang ku cari!"
    nava "A..ku? kenapa?"
    you "Rapat, aku datang untuk mengajakmu ikut rapat terkait projek kita"
    nava "Oh, jadi kamu anggota baru itu ya?"
    show nava sad
    nava "{size=30}Aku sebenarnya gak mau ikut rapat{/size}"
    you "hmm? kenapa?"
    show nava uneasy at shake
    nava "Eh-Uh... Tidak apa-apa."
    show nava basetalk
    nava "Ayo kita langsung ke kelas!"
    you basetalk "Kamu tidak mau makan rotinya dulu?"
    show nava uneasy
    nava "Umm... kita bisa memakannya sambil jalan."
    you basetalk "Baiklah."
    "Aku dan Nava pun bergegas pergi kembali ke kelas"
    scene black with fade
    stop music fadeout 3.5
    scene bg classhall with Dissolve(3.0)
    return

label chapter2a:
    play sound opendoor
    play music afternoon_waltz fadein 5.0
    scene black with fade
    scene bg class2 with ImageDissolve("open_door1.png", 4.5, ramplen=256)

    show theo idle at boystyle with dissolve
    show theo happy
    theo "Hey [defname]! Selamat datang kembali!"
    theo "Kami baru saja selesai membahas beberapa hal."
    play audio ping
    theo "Oh! kamu menemukan Nava!"
    show theo idle with move:
        xoffset -650
    show nava uneasy at girlstyle with dissolve
    nava "h-hi... Maaf aku telat semuanya."
    play sound footstep volume 1.0
    hide nava uneasy with dissolve
    show theo idle with move:
        xoffset 0
    play sound pullchair 
    pause 1.0
    "Aku dan Nava langsung bergegas duduk."
    "Nava tampaknya agak canggung dengan teman-teman lainnya."
    "Apakah Nava memiliki masalah dengan mereka?"
    show theo basetalk
    theo "Baiklah, karena semua sudah berkumpul kita mulai aja rapatnya."
    show theo happy
    theo "Sebelum itu aku ingin mengucapkan selamat datang di tim kami, [defname]!"
    show theo base
    menu:
        "Senang bisa bekerja sama dengan kalian! (optimis)":
            you basetalk "Senang bisa bekerja sama dengan kalian!"
            $ optimisme = optimisme + 1
        "Mohon bantuannya semua!":
            you basetalk "Mohon bantuannya semua... (pesimis)"
    
    show theo basetalk
    theo "Karena [defname] masih baru di sini, mungkin akan lebih baik jika aku sekali lagi memperkenalkan semua anggota tim kita."
    theo "Perkenalkan aku Theo, Ketua dan sekaligus {b}Sound Engineer{/b}"
    theo "Aku bertanggung jawab dalam bagian musik dan efek-efek suara dari game kita."
    theo "Ini Claire, Wakil ketua dan juga {b}Story Writter{/b} kita."
    show theo base with move:
        xoffset -550
    show claire base at girlstyle with moveinright:
        xalign 0.65
    theo "Claire bertanggung jawab dalam menyusun cerita game."
    theo "Dan ini adalah Nava, {b}Artist & Illustrator{/b} game."
    hide claire base with moveoutright
    show nava base at girlstyle with moveinright:
        xalign 0.65
    theo "Nava bertugas dalam membuat desain karakter maupun tampilan game."
    theo "Berikutnya Ciel, {b}Programmer{/b} junior."
    hide nava base with moveoutright
    show ciel base at girlstyle with moveinright:
        xalign 0.65
    theo "Ciel pada awalnya bertugas untuk menyusun tampilan dari aplikasi game kita."
    hide ciel base with moveoutright
    show theo sad with move:
        xoffset 0
    theo "Tetapi karena anggota kita sebelumnya, si {b}Hendry{/b}, telah pergi meninggalkan kita dan tidak memberikan kabar apapun."
    theo "Semua tugas dia harus dibebankan kepada Ciel seorang diri,"
    show theo happy
    theo "tetapi berkatmu, Ciel dapat membagikan tugasnya lagi."
    theo "Dengan ini, penyusunan program game akan berjalan sesuai rencana awal."
    "Hendry? siapa dia..."
    "Kayaknya aku pernah mendengar nama itu sebelumnya."
    "Tapi dimana...?"
    menu:
        "Haruskah aku menanyakan lebih lanjut tentang Hendry kepada Theo dan lain-lain?"
        "Tidak perlu":
            pass
        "Siapa Hendry?":
            call hendry from _call_hendry
    show theo basetalk
    theo "Oh iya! [defname]." 
    theo "Saat kamu pergi mencari Nava tadi, kami sebenarnya sudah membahas beberapa tugas tambahan buat kita masing-masing."
    theo "Untuk tugas kamu dan Ciel sudah ku kelaskan kepada Ciel."
    theo "Mungkin nanti kalian bisa membahasnya bersama."
    show theo base
    you "Baiklah!"
    show theo basetalk
    play audio ping
    theo "Ah! satu hal lagi..."
    theo "Nava!"
    show nava base at girlstyle with dissolve:
        xoffset -500
    show nava uneasy
    show theo idle
    nava "Y-ya?"
    show nava uneasyidle
    show theo basetalk
    theo "Terkait tugas kamu..."
    show theo sad
    theo "Sebelumnya aku minta maaf atas kelalaianku."
    theo "Seharusnya kami sadar lebih awal."
    show claire base at girlstyle with dissolve:
        xalign 1.1
    show theo sadidle
    show claire uneasy
    claire "Mungkin kamu merasa gelisah karena kami sering membebanimu dengan permintaan-permintaan kami."
    show claire happy
    show theo happyidle
    claire "Oleh karena itu, Aku telah memutuskan untuk membantumu dalam peranmu sebagai ilustrator."
    show claire happyidle
    show nava happy
    nava "Wahhh! beneran nih?"
    show nava sad
    nava "Hiks- makasih banyak kak Claire!"
    show nava sadidle
    show claire happy
    claire "Iya bener kok hehe~"
    show claire basetalk
    claire "Walaupun aku tidak begitu mahir dalam bidang ini, tetapi aku bisa membantumu dalam desain tampilan."
    claire "Supaya kamu bisa lebih fokus pada desain karakter aja."
    show claire idle
    show theo happy
    theo "Haha, senang bisa melihatmu ceria kembali, Nava,"
    return
label chapter2b:
    scene bg class2 with dissolve
    show theo basetalk at boystyle with dissolve 
    theo "Hmm... mungkin itu saja untuk rapat hari ini."
    show theo happy
    theo "Makasih semuanya sudah mau hadir."
    theo "Ku harap semuanya bisa mengerjakan tugasnya masing-masing dengan lancar."
    theo "Sampai ketemu lagi!"
    hide theo happy with dissolve
    show nava happy at girlstyle with dissolve:
        xoffset -400
    show claire basetalk at girlstyle with dissolve:
        xalign 1.0
    claire "Aku pamit ya~"
    nava "Makasih banyak teman-teman."
    hide nava happy with dissolve
    hide claire basetalk with dissolve
    play audio opendoor
    pause 2.0
    "Semua tampaknya sudah pulang, aku sebaiknya menyusul merek-"
    stop music fadeout 1.5
    show bg class2 with vpunch 
    "! ! !"
    show ciel angry at girlstyle with moveinbottom
    play music cold_brew
    ciel "Hey! tunggu dulu!"
    ciel "Kita perlu membahas tugas kita!"
    "Oh... aku lupa tentang itu..."
    show ciel basetalk 
    ciel "Aku akan mengirimkan file kerjaan milik Hendry kepadamu."
    ciel "di dalam file tersebut ada catatan TOD0-List milik Hendry, mungkin itu bisa membantumu dalam mengerjakan tugasmu."
    play audio ping
    "Aku menerima file milik Hendry dari Ciel"
    show ciel happy
    ciel "Oh iya, besok kalau kita ketemuan di kelas lagi gimana?"
    show ciel blush
    menu:
        ciel "Mungkin kita bisa mengerjakannya bersama"
        "Tentu saja bisa! (optimis)":
            you exited"Tentu saja bisa! Aku akan menunggumu besok pagi!"
            show ciel excited
            ciel "Hehe, Jangan sampai lupa ya!"
            $ optimisme = optimisme + 1
        "Aku bisa kapan pun kamu bisa... (pesimis)":
            you basetalk "Terserah kamu aja ciel, aku bisa kapan aja"
            show ciel uneasy 
            ciel "B-baiklah, Besok kita ketemuan pagi aja ya?"
            you basetalk "Ok!"
    show ciel basetalk 
    ciel "Aku pamit dulu ya! Makasih banyak atas hari ini!"
    hide ciel basetalk with dissolve
    hide screen dabutton with dissolve
    stop music fadeout 3.0
    return
    
label hendry:
    you "Hendry? dia siapa?"
    show theo sad
    theo "huh? kamu tidak mengenalnya?"
    theo "Kukira kalian berdua sebelumnya teman sekelas."
    you sad "Aku tidak begitu ingat tentangnya."
    show theo sadidle
    show claire base at girlstyle with dissolve:
        xoffset -500
    show claire sad
    claire  "Hendry adalah kenalan lamaku yang cukup mahir dibidang pemograman."
    claire "Bersama Nava, aku yang mengajaknya untuk bergabung di tim ini."
    claire "Dia jugalah orang yang mengajarkan dan mengajak Ciel untuk bergabung di tim ini."
    claire "Merupakan suatu kebetulan juga kalau dia merupakan teman dekat Theo."
    claire "Bukankah begitu Theo?"
    show claire idle
    show theo sad
    theo "Iya, tapi sangat disayangkan Hendry sudah tidak pernah membalas pesan-pesanku."
    theo "Mungkin dia mulai sibuk dengan berbagai hal di luar kampus."
    theo "Aku pun masih mengkhawatirkannya hingga sekarang."
    hide claire idle with dissolve
    return

label kamar:
    "Sebaiknya aku bergegas pulang juga, aku masih memiliki banyak pekerjaan."
    play sound footstep
    scene bg outside with fade
    scene black with fade
    pause 2.0
    play sound opendoor
    play music for_piano fadein 5.0
    scene bed night with ImageDissolve("open_door2.png", 4.5, ramplen=256)
    show screen dabutton()
    "Akhirnya aku sampai di rumah"
    "Aku merasa lelah dari semua hal yang terjadi hari ini."
    "Aku ingin beristirahat, tetapi aku ingin melihat file yang telah dikirim Ciel tadi."
    menu:
        "Apa yang harus kulakukan?"
        "Mungkin Sebaiknya aku istirahat":
            "Aku telah melalui banyak hal hari ini."
            "Mungkin sebaiknya aku istirahat."
            jump nightmare
        "Melanjutkan pekerjaan yang ditinggal Hendry":
            "Aku tidak bisa meninggalkan pekerjaanku begitu saja"
            "Ciel sangatlah bergantung kepadaku akan pekerjaan ini"
            "Sebaiknya aku kerjakan setidaknya sedikit saja."
            $ renpy.music.set_pause(True, channel="music")
            scene black with fade
            scene bed night with fade
            play audio wind
            pause 0.2
            scene black with fade
            scene bed night with fade
            $ renpy.music.set_pause(False, channel="music")
            "Yawn... Aku mulai merasa ngantuk..."
            "Sebaiknya aku membuat kopi."
            scene black with fade
            play audio pourcoffee
            pause 4.0
            scene bed night with fade
            play sound ping
            "Kopi telah siap!"
            play audio pullchair
            "Aku mengambil file yang telah dibagikan oleh Ciel."
            play audio drinkcoffee
            "Hmm..."
            jump check_kamar
    return

label check_kamar:
    if optimisme >= 2:
        ". . ."
        scene black with fade 
        scene bed night with fade
        play audio ping       
        "Aku mengerjakan pekerjaanku dengan sangat baik."
        "Dengan begini besok aku hanya perlu membantu Ciel saja."
        "Dan menga-{w=1}{nw}"
        $ renpy.music.set_pause(True, channel="music")
        scene black with fade
        scene bed night with fade
        play audio wind
        pause 0.2
        scene black with fade
        scene bed night with fade
        $ renpy.music.set_pause(False, channel="music")
        "Yaawn... Mungkin akan ku akhiri disini saja."
        "Aku sudah tidak kuat menahan kantuk ini."
        "Selamat malam..."
        $ ending_desc = 4
    else:
        "Pekerjaan dari Hendry Cukup rumit..."
        "Mungkin besok aku harus berdiskusi bersama Ciel."
        scene black with fade
        scene bed night with fade
        play audio wind
        pause 0.1
        scene black with fade
        scene bed night with fade
        "Yawn... Mungkin akan ku akhiri disini saja."
        "Semoga Ciel bisa membantuku besok."
        "Aku sudah tidak sanggup melanjuti pekerjaan ini."
        $ ending_desc = 3
    #bertemu ciel
    scene black with ImageDissolve("images/pattern4.jpg",4.5,reverse=True,ramplen=256)
    scene black 
    centered "{size=+50}{color=#FFFFFF}Keesokan Harinya{/color}{/size}"
    stop music fadeout 4.0
    scene bg outside with Dissolve(3)
    "Sesampainya aku di kampus."
    show white with Dissolve(0.1)
    scene bg outside with vpunch
    play sound wind
    "! ! !"
    "Kepala ku mendadak pusing..."
    "Ugh"
    "Apakah ini karena aku kurang tidur?"
    "Tapi..."
    "Aku tidak merasakan lelah sama sekali..."
    "Mungkin Penyakitku lamaku kambuh lagi."
    "Jika iya, maka aku harusnya tidak apa-apa."
    "Aku Sebaiknya menemui Ciel dalam kelas. Dia pasti sudah menunggu."
    play music romance fadein 3.0
    play sound opendoor
    scene black with fade
    scene bg class2 with ImageDissolve("open_door1.png", 4.5, ramplen=256)
    "Huft... Akhirnya sampai juga"
    "Untung aku tidak kenapa-kenapa saat di jalan"
    "Mungkin hari ini aku harus tidur lebih banyak dari biasanya."
    ". . ."
    "huh?"
    $ renpy.music.set_pause(True, channel="music")
    "Aku tidak melihat siapa-siapa..."
    "Umm"
    "Apa mungkin aku terlambat? atau ciel sudah pulang? tapi bukankah kita{nw}kemarin sudah janji untuk kesini kemarin?"
    play audio bump
    show black with ImageDissolve("black.jpg",0.1)
    show bg class2 with vpunch
    play sound heartbeat
    you crazy "{size=100}{b}AHHH!!!{b}{w=0.3}{nw}{/size}"
    hide black
    "???" "Hey! kamu kenapa?{w=1}{nw}"
    show ciel happy at girlstyle with moveinbottom
    "Huft... untung saja aku bukan di cerita game horror"
    "Aku merasa kayak dikejutkan oleh sebuah mahkluk aneh saja"
    "Tenang [defname], Tenang..."
    stop sound
    "Tenang..."
    $ renpy.music.set_pause(False, channel="music")
    you sad "Ya ampun Ciel, jangan bikin aku terkejud gitu..."
    show ciel sad
    ciel "Hah? aku dari tadi menyapamu tapi kamu tidak menyapaku balik..."
    ciel "Kamu..{w=0.5}Tidak apa-apa kan?"
    you sad "Uhm.... mungkin aku pusing aja, semalampun aku tidak mendapatkan waktu tidur yang cukup."
    ciel "Umm... mungkin kamu sebaiknya kamu pulang saja hari ini..."
    ciel "Muka kamu juga terlihat pucat."
    you sad "T-tapi bagaimanan dengan kerjaan kita?"
    ciel "Kita bisa mengerjakannya setelah kamu baikan, tenang saja [defname]."
    you sad "B-baiklah aku akan pulang sekarang"
    show ciel uneasy 
    ciel "Ah..umm...{w=0.5} Kamu yakin mau pulang sendirian?"
    if optimisme >= 3:
        menu:
            ciel "Apakah kamu mau aku anterin sampai kerumahmu?"
            "Tidak perlu":
                you sad "Tidak, tidak usah."
                you sad "Aku pulang sendiri."
                you sad "Terima kasih Ciel."
                show ciel sad
                ciel "Ba-baiklah jika itu yang kamu mau, hati-hati di jalan."
                "Aku merasa tidak enak badan, Sebaiknya aku pulang segera."
                "Maafkan aku, Ciel."
                play sound footstep
                stop music fadeout 4.0
                play sound opendoor
                scene bg outside with ImageDissolve("open_door3.png",4.5, ramplen=256) 
                play sound footstep
                scene black with fade
                pause 3.0
                play sound opendoor
                scene bed night with ImageDissolve("open_door2.png",4.5, ramplen=256)
                jump nightmare   
    else:
        menu:
            ciel "Apakah kamu mau aku anterin sampai kerumahmu?"
            "Tidak perlu":
                you sad "Tidak, tidak usah."
                you sad "Aku pulang sendiri."
                you sad "Terima kasih Ciel."
                show ciel sad
                ciel "Ba-baiklah jika itu yang kamu mau, hati-hati di jalan."
                "Aku merasa tidak enak badan, Sebaiknya aku pulang segera."
                "Maafkan aku, Ciel."
                play sound footstep
                stop music fadeout 4.0
                play sound opendoor
                scene bg outside with ImageDissolve("open_door3.png",4.5, ramplen=256) 
                play sound footstep
                scene black with fade
                pause 3.0
                play sound opendoor
                scene bed night with ImageDissolve("open_door2.png",4.5, ramplen=256)
                jump nightmare
            "Kumohon, Anterin aku pulang":
                you sad "Tolong anterin aku Ciel."
                you sad "Kumohon."
                show ciel sad
                ciel "B-baiklah ayo kita pulang."
                jump daymare
    return

label daymare:
    play sound opendoor
    scene bg classhall with ImageDissolve("open_door3.png",4.5, ramplen=256)
    play sound footstep
    scene bg outside with ImageDissolve("black.jpg",4.5, ramplen=256)
    scene black with fade
    play music late_night_love_letter fadein 5.0
    scene bg home with dissolve
    "Sudah sampainya kami di depan rumahku"
    show ciel base at girlstyle with dissolve
    show ciel basetalk
    ciel "Apakah ini rumahmu, [defname]?"
    you sad "iya..."
    you sad "Terima kasih sudah mau mengantariku pulang Ciel."
    you sad "Maafkan aku sudah terlalu merepotkanmu."
    show ciel uneasy
    ciel "Ka-kamu tidak perlu berterima kasih, yang kulakukan hanyalah menemanimu pulang."
    show ciel sad
    ciel "Dan jika sesuatu terjadi padamu, aku akan merasa bersalah karena akulah yang mengajakmu untuk ke kampus hari ini."
    you sad "Soal janji kita, aku minta maaf sekali lagi-{w=0.8}{nw}"
    show ciel angry
    ciel "Kamu tidak perlu mencemaskan itu lagi!"
    show ciel sad
    ciel "Kamu membutuhkan istirahat."
    you sad "Tapi- tapi..."
    if ending_desc == 3:
        you sad "Apakah besok kamu bisa kekampus lagi?"
        you sad "Aku yakin besok keadaanku akan membaik lagi."
        you sad "Ada... {w=0.5}Sesuatu yang ingin aku bahas."
        you sad "Aku juga ingin meminta bantuanmu."
        show ciel angry
        ciel "Huft..."
        ciel "Dasar keras kepala..."
        ciel "Apakah kamu keberatan jika aku mampir kerumahmu sampai malam ini?"
        you sad "Te-tentu tidak, emangnya kenapa?"
        show ciel sad
        ciel "Aku telah menduga bahwa pekerjaanmu akan sangat berat."
        ciel "Oleh karena itu, aku memutuskan untuk membantumu mengerjakannya di rumahmu."
        ciel "Juga berusaha sebisaku untuk merawatmu... "
        ciel" Aku yakin kamu kekurangan tidur karena menghabiskan semalam untuk mencoba mengerjakannya,"
        show ciel angry
        ciel "Bukankah begitu?"
        you sad "I-iya... aku rasa aku terlalu memaksakan diriku."
        you sad "Terima kasih sudah mau membantuku...{w=0.2}dan sudah mau merawatku."
        hide ciel angry with dissolve
        "Aku dan Claire segera Masuk kedalam rumahku."
        scene black with fade
        ciel "Aku akan mengantarmu kekamarmu..."
        play sound footstep
        "Aku membawa ciel kedepan pintu kamarku."
        stop music
        "...?"
        ciel "Sniff- Sniff..."
        ciel "{size=30}Aku mencium bau yang aneh...{/size}"
        ciel "{size=30}Bau ini seperti-{/size}{w=0.7}{nw}"
        you sad "Ciel? Apakah kamu baik-baik saja?"
        ciel "I-iya, aku baik-baik saja."
        "Aku membuka pintu kamarku."
        play sound opendoor
        pause 2.0
        ciel "I-Itu..."
        ciel "Bukankah itu........................{w=2}ma{w=2}yat??{w=0.5}{nw}"
        ciel "!!!"
        ciel "He....{w=2}{nw}"
        ciel "Hen....{w=2}{nw}"
        ciel "HEENDRY!!!???{w=0.8}{nw}"
        menu:
            "jelaskan semuanya":
                $ persistent.test = persistent.test + 1
                python:
                    import os
                    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
                    name = os.path.join(desktop, 'hallucination'+".txt") 
                    f = open(name,'w')
                    f.write('Kamu tahu apa? Apa yang mau dijelaskan? \nLagipula semua ini hanyalah halusinasimu.\n\nApa yang terjadi barusan...\nTidaklah nyata\n\n\n\nSadarlah...')
                    f.close()
                $ renpy.quit()
    elif ending_desc == 4:
        you sad "Aku hanya ingin memberitahumu kalau..."
        you sad "Semalam aku telah menyelesaikan semua pekerjaanku."
        show ciel basetalk
        ciel "Baiklah, terima kasih banyak, [defname]."
        ciel "Aku akan memberitahukan yang lain juga."
        ciel "Untuk sekarang kamu tidak perlu memikiran apapun lagi, termasuk projek ini."
        ciel "Pergilah istirahat."
        you sad "Baiklah, Sekali lagi terima kasih banyak, Ciel."
        ciel "Sama-sama, Sampai jumpa nanti."
        hide ciel basetalk with moveoutright
        "Ciel tampak sedang terburu-buru"
        "Aku sebaiknya masuk ke kamarku sekarang"
        play sound footstep
        scene black with fade
        play sound opendoor
        scene bed day with ImageDissolve("open_door2.png", 4.5, ramplen=256)
        "Aku sudah tidak kuat lagi."
        "Aku bergegas untuk tidur"
        scene black with fade
        scene bed day with fade
        play audio wind
        pause 0.2
        scene black with fade
        scene bed night with fade
    jump ending_check
    return

label nightmare:
    play music late_night_love_letter volume 0.3
    "Aku tidak tahan lagi..."
    "Aku mau tidur..."
    hide screen dabutton
    stop sound
    scene black with fade
    scene bed night with fade
    stop music fadeout 5.0
    scene bed night with fade
    scene black with ImageDissolve("images/black.jpg",4.0,ramplen=256)
    pause 5.0
    play sound doorknock
    "???"
    "Suara apa itu?"
    "Apakah ada yang mengetuk pintu?"
    scene bed glitch with ImageDissolve("images/black.jpg",4.0,ramplen=256) 
    "Haruskan aku pergi melihatnya?"
    "Mungkin ada seseorang yang ingin meminta tolong..."
    play sound footstep
    scene hall with ImageDissolve("images/black.jpg",2.0,ramplen=256)
    "Hmm..."
    "Mungkin hanya khayalanku saja."
    "{w=1}Haus."
    "Aku ingin kedapur untuk mengambil secangkir air."
    scene black with ImageDissolve("images/black.jpg",2.0,ramplen=256)
    play sound drinkcoffee
    "Gulp...Gulp"
    "Lega rasanya, Saatnya aku untuk kembali kekamarku dan lanjut{nw}}"
    play sound doorbang
    show black with ImageDissolve("black.jpg",0.1)
    show hall5 at shake
    centered"{b}{color=#FFFFFF}{size=100}AHHHHHH!!!{/size}{/color}{/b}{fast}{w=0.2}{nw}"
    play music heartbeat
    play audio panting
    pause 2.0
    "SUARA APA ITU?"
    "I-i-itu suara ketuk pintu kan??"
    "Oh tidak..."
    "SIAL!"
    "{size=70}{color=#ffffff}SIAL!{/color}{/size}{w=0.1}{nw}"
    "{size=80}{color=#ffffff}SIAL!{/color}{/size}{w=0.1}{nw}"
    "{size=90}{color=#ffffff}SIAL!{/color}{/size}{w=0.1}{nw}"
    "{size=100}{color=#ffffff}SIAL!{/color}{/size}{w=0.1}{nw}"
    "{size=200}{color=#ffffff}SIAL!{/color}{/size}{w=0.1}{nw}"
    "{size=60}SIAL!{/size}"
    "Ok, {w=0.2}Tenang, tenang"
    play sound breath
    scene black with fade 
    show hall with ImageDissolve("images/black.jpg",2.0,ramplen=256)
    "Tenang...{w=2}{nw}"
    play sound doorbang2
    show black with ImageDissolve("black.jpg",0.1)
    show hall3 at shake 
    "!!!"
    "Penglihatanku mulai aneh."
    "Ini cuman mimpi, {w=0.05} Aku yakin ini pasti mimpi"
    play sound breath
    stop music
    "Tenang, Tenang, {w=0.5}Tenang."
    "ini cuman mimpi"
    "Aku mencoba mencubit tanganku-"
    play audio bump
    show hall2 at shake with dissolve
    "Ouw!"
    "ini bukanlah mimpi..."
    "Aku harus cepat cepat balik tidur."
    "Pikiranku mulai aneh."
    play sound footstep
    scene black with fade 
    show hall4 
    play sound doorbang3
    pause 0.1
    scene black 
    scene bed glitch with ImageDissolve("images/black.jpg",4.0,ramplen=256)
    play music heartbeat fadein 1.0 volume 0.3
    "Malam yang aneh..." 
    "Kalau ada keanehan lagi, aku harap itu hanyalah sebuah mimpi."
    stop music fadeout 3.0
    scene black with fade
    pause 0.3
    play sound tapglass
    pause 1.0
    "itu apaan lagi..?"
    "Apakah aku mulai gila?{w=0.5}{nw}"
    scene bed glitch with fade
    scene black with fade
    play sound whoosh
    show entity2 
    pause 0.2
    hide entity2
    pause 5.0
    $ ending_desc = 5
    jump ending_check

label secondmenu:
    menu:
        "Haruskah aku mengikutinya masuk?"
        "Cek apakah itu beneran kelas untuk rapat":
            play sound footstep volume 1.0
            show bg classhallclose with fade
            "Aku mencoba untuk mendengar percakapan dari pintu"
            "Suara 1" "SUDAH KU BILANG JANGAN MENGHUBUNGIKU LAGI!!!"
            "Pria 1" "Tapi Nava..."
            "Suara tersebut terdengar tidak asing..."
            "Itu suara Theo"
            "Theo" "Kita sudah berjuang sampai sini"
            "Nava?" "ADILKAH? adilkah pekerjaan Ciel dibagi dengan ANAK BARU ITU?"
            "Ciel?" "Kamu pikir pekerjaan programmer mudah? emangnya kamu paham dengan pekerjaanku?"
            "Anak baru? apakah itu...{w=0.5}Aku?"
            "Nava?" "KALIAN PIKIR PEKERJAAN KU MUDAH? KALIAN PIKIR MENGGAMBAR ITU MUDAH?"
            "Nava?" "DENGAN PERMINTAAN KALIAN YANG BANYAK, KALIAN HARAP AKU SEORANG DIRI-"
            "Nava?" "Hiks- aku tidak mau berurusan dengan kalian lagi selamat tinggal."
            play sound footstep volume 1.0
            pause 1.5 
            "SIAL! aku mendengar suara kaki mendekati pintu"
            "Aku bergegas pergi dari kelas tersebut"
            play sound run volume 1.0
            scene black with fade
            scene bg outside with Dissolve(2.5)
            stop sound
            "Aku tidak tau apa yang terjadi disana..."
            "Tapi aku tidak yakin aku akan diterima dengan ramah disana"
            "Sebaiknya aku pulang saja"
            $ending_desc = 1
            jump ending_check
        "Langsung Masuk":
            "Aku membuka pintu kelas tersebut"
            play sound footstep
            play sound opendoor
            scene black with fade
            scene bg class2 with ImageDissolve("open_door1.png", 4.5, ramplen=256)
            "Huh..."
            "Kosong?"
            "Mungkin Theo sudah pulang."
            "Tapi..."
            "Perempuan yang masuk tadi..."
            "Mungkin aku mulai ngantuk karena makan..."
            "Sebaiknya aku pulang saja"
            $ ending_desc = 2
            jump ending_check
            
label ending_check:
    stop music
    hide screen dabutton
    if ending_desc == 1:
        play sound footstep
        play sound opendoor
        scene bed day with ImageDissolve("open_door2.png",4.5, ramplen=256)
        "Sampainya aku di rumah"
        "Mungkin sebaiknya aku istirahat aja."
        scene bed night with Dissolve(5)
        play sound vibration
        pause 1.0
        "Pesan masuk?"
        nvl_narrator "Theo is on the line"
        nvl_theo "{size=30}Hai [defname]{/size}"
        nvl_theo "{size=30}Soal rapat tadi...{/size}"
        nvl_theo "{size=30}Kamu mungkin sedang sibuk sampai gak bisa datang{/size}"
        nvl_theo "{size=30}tapi...{/size}"
        nvl_theo "{size=30}Kami telah memutuskan untuk membatali projek kami{/size}"
        n_nvl "{size=30}Maaf Theo, aku tadi mendadak sakit, akupun tidak sempat mengabarimu{/size}"
        nvl_theo "{size=30}Tidak apa-apa [defname], aku rasa projek ini juga bukanlah ide yang bagus.{/size}"
        nvl_theo "{size=30}Sorry ya, selamat tinggal{/size}"
        nvl_narrator "Theo logged off"
        scene black with dissolve
        centered "{color=#fbff00}{size=35}Ending 1{/color}{/size}\n{size=100}{b}{color=#FFFFFF}Ignorance is a bliss{/color}{/b}{/size}\n\n\n{color=#ce6600}{size=65}Kamu memutuskan untuk tidak mengikuti rapat dan tidak membantu Theo dengan projeknya.\n Apa mungkin ini merupakan pilihan terbaik?{/size}{/color}{fast}"
    elif ending_desc == 2:
        play sound footstep
        play sound opendoor
        scene bed day with ImageDissolve("open_door2.png",4.5, ramplen=256)
        "Sampainya aku di rumah"
        "Sniff...{w=0.5}Sniff..."
        "Bau ini sangatlah menggangu..."
        "Bau seperti daging kadarluarsa, tapi aku tidak mengingat membeli daging apapun."
        "Mungkin aku harus memanggil seseorang untuk membersihkan kamarku besok..."
        "Sekarang mungkin sebaiknya aku istirahat aja..."
        scene bed night with Dissolve(5)
        scene black with dissolve
        centered "{color=#fbff00}{size=35}Ending 2{/color}{/size}\n{size=100}{b}{color=#FFFFFF}Am i dreaming?{/color}{/b}{/size}\n\n\n{color=#ce6600}{size=65}Tampaknya semuanya hanyalah mimpi.{fast}\n{w=3}{color=#d00114}{font=fonts/bloody.ttf}{size=90}Atau apakah ini nyata?{/size}{/fonts}{/color}{/size}{/color}"
    elif ending_desc == 3:
        stop music
        hide ciel base
        hide screen reset_var
        play music credit fadein 0.5
        centered "{color=#ffffff}{b}{size=60}Terima kasih sudah bermain{/color}{/size}{\b}{fast}{w=5}{nw}"
        centered "{color=#ffffff}{b}{size=60}Create by Kelompok 10 - Lorem Ipsum{/color}{/size}{\b}{fast}{w=5}{nw}"
        centered "{color=#ffffff}{b}{size=60}Credits to Music producers\n Luxid\nParkbird and Mellow Blush\nChance Thrash\npastels\nTaku Matsushiba\nHikaru Shirosu{/color}{/size}{\b}{fast}{w=10}{nw}"
        centered "{color=#ffffff}{b}{size=60}Rabbit Prince - Luxid\n Childhood Memories - Luxid\nRomance - Luxid\nWatercolor Paint - Luxid\nLate Night Love Letter - Luxid\nWill You Marry Me? - Luxid{/color}{/size}{\b}{fast}{w=13}{nw}"
        centered "{color=#ffffff}{b}{size=60}biscuit town - Park bird & Chance Thrash\nGhost Everything - Park bird & Mellow Blush\n Tea Time - Chance Thrash{/color}{/size}{\b}{fast}{w=10}{nw}"
        centered "{color=#ffffff}{b}{size=60}Cold Brew - pastels\n Afternoon Waltz - Taku Matsushiba\n . . . . For Piano - Hikaru Shirosu{/color}{/size}{\b}{fast}{w=10}{nw}"
        centered "{color=#ffffff}{b}{size=60}Special Thanks to\nGDC\n Game Development Club{/color}{/size}{fast}{w=10}{nw}"
        stop music fadeout 5.0
        $ persistent.test = 0
    elif ending_desc == 4:
        stop music
        scene black with dissolve
        centered "{color=#fbff00}{size=35}Ending 4{/color}{/size}\n{size=100}{b}{color=#FFFFFF}Hero{/color}{/b}{/size}\n\n\n{color=#ce6600}{size=65}Dengan mengorbankan kesehatanmu, kamu telah menyelesaikan tugas terberat dari projek ini.{/size}{/color}{fast}\n{w=3}{color=#d00114}{size=90}Tampaknya kamu tidak akan terbangun lagiR{/size}{/color}{w=3}{nw}"
    elif ending_desc == 5:
        centered "{color=#fbff00}{size=35}Ending 3{/color}{/size}\n{size=100}{b}{color=#FFFFFF}Consequence Of Neglection{/color}{/b}{/size}\n\n\n{color=#ce6600}{size=65}Kamu tidak hanya melupakan tugasmu, kamu lupa dengan dirimu sendiri{fast}\n{w=3}{color=#d00114}{size=90}Cepat atau lambat kamu harus sadar.{/size}{/color}{/size}{/color}{w=3}{nw}"
        python:
            import os
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
            name = os.path.join(desktop, 'WhoAmI'+".txt") 
            f = open(name,'w')
            f.write('Skizofrenia adalah gangguan kejiwaan kronis ketika pengidapnya mengalami halusinasi, delusi, kekacauan dalam berpikir, dan perubahan sikap. Umumnya pengidap skizofrenia mengalami gejala psikosis, yaitu kesulitan membedakan antara kenyataan dengan pikiran pada diri sendiri.')
            f.close()
        centered "{size=100}{b}{color=#FFFFFF}A friendly .txt reminder has been sent to your desktop{/color}{/b}{/size}{w=3}{nw}"
        centered "{size=100}{b}{color=#FFFFFF}Don't forget to check them{/color}{/b}{/size}{w=7}{nw}"
        $ renpy.quit() 
    $ MainMenu(confirm=False)()

    
# MC yang membunuh member pertama supaya role dia bisa digantikan sama MC,
# member pertama pernah merupakan senior claire dan nava, juga teman kelas MC
#setelah ketahuan membunuh, mc menjelaskan bahwa ciel hanyalah berhalusinasi
#seketika membuat mc sadar dan pingsan
#game mulai dengan tema creepy


# label testground:
#     scene bg garden
#     with dissolve
#     show claire base:
#         zoom 1.5
#         xalign 0.5
#         yalign 1.5
#     claire "hi"
#     show screen reset_var()
#     menu:
#         "gimana?"
#         "option 1":
#             $ persistent.test = persistent.test + 1
#             python:
#                 import os
#                 desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
#                 name = os.path.join(desktop, 'hallucination'+".txt") 
#                 f = open(name,'w')
#                 f.write('its not real')
#                 f.close()
#             $ renpy.quit() 
#         "option 2":
#             window hide
#             show claire glitched:
#                 zoom 1.5
#                 xalign 0.5
#                 yalign 1.5
#             play sound glitch1
#             pause 1.5
    
#     scene bg canteen
#     show nava base:
#         zoom 1.5
#         xalign 0.5
#         yalign 1.5
#     nava "hello"
#     window hide
#     show nava glitched:
#         zoom 1.5
#         xalign 0.5
#         yalign 1.5
#     play sound glitch2
#     pause 1.5
#     scene bg bridge
#     show ciel base:
#         zoom 1.5
#         xalign 0.5
#         yalign 1.5
#     ciel "oi"
#     window hide
#     show ciel glitched:
#         zoom 1.5
#         xalign 0.5
#         yalign 1.5
#     play sound glitch3
#     pause 1.5
#     scene bg classhall
#     show theo base:
#         zoom 1.5
#         xalign 0.5
#         yalign 1.0
#     theo "Looks like they're{w=1.0}{nw}"
#     show theo basetalk:
#         zoom 1.5
#         xalign 0.5
#         yalign 1.0
#     theo "Looks like they're playing with their trebuchet again."
#     return
