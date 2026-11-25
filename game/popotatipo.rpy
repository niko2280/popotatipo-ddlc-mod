# ############################################################
# ПОПОТАТИПО: ПОБЕГ ИЗ ПОДЪЕЗДА — мод для DDLC
# Файл персонажа и определений
# ############################################################

define p = Character('ПОПОТАТИПО', color="#c93a3a")
define m = Character('Monika', color="#41a24c")
define s = Character('Sayori', color="#dfdc7f")
define n = Character('Natsuki', color="#de76a9")
define y = Character('Yuri', color="#7e4fa1")
define mc = DynamicCharacter('player', color="#42a7da")
define nn = Character(None)

default player = "Сеня"

# --- Фотографии Попотатипо ---
# Положи свои фото в папку game: popo1.png, popo2.png, popo3.png
# Мод сам их подхватит. Если фото нет — будет тёмный экран.

image popo_dark = Solid("#101010")

image popo1 = ConditionSwitch(
    "renpy.loadable('popo1.png')", Image("popo1.png"),
    "renpy.loadable('images/popo1.png')", Image("images/popo1.png"),
    "True", "popo_dark")

image popo2 = ConditionSwitch(
    "renpy.loadable('popo2.png')", Image("popo2.png"),
    "renpy.loadable('images/popo2.png')", Image("images/popo2.png"),
    "True", "popo_dark")

image popo3 = ConditionSwitch(
    "renpy.loadable('popo3.png')", Image("popo3.png"),
    "renpy.loadable('images/popo3.png')", Image("images/popo3.png"),
    "True", "popo_dark")
