## THE STORY: chapters 6-7 and the endings (PLAN.md). Thursday the name at noon and the wine-yard dance; Friday, the new moon,
## the Double Figure and the deciding choice (both marked as endings): Dance with Lys -> A "Sealed", Dance for them -> B
## "Enslaved". dnc.held and dnc.asked only change a line or two.

## ---- 6. Thursday: the wine yard -------------------------------------------------------------------------------

label dnc_thursday:
    $ dnc.fit = "shift"
    $ dnc_grow(6)
    $ vn_enter(bg="dnc_temple_cell", pc="dazed", pc_tag="dnc_pc", cast=[], cg="dnc_mirror_thursday")
    "{color=#ff5fb8}Your breasts are big now. Heavy, round, soft, full enough to spill over your arm when you hug yourself, swaying with every step. Your hips are wide, your waist is narrow between them, and your arse is round and high and full; the shift catches on it.{/color}"
    "{color=#ff5fb8}You're shorter than you were, half a head nearer the floor. Rose-gold hair falls to the middle of your back in soft waves. When you walk, your hips sway on their own, the way a dancer's do.{/color}"
    $ vn_set_time(12, 0)
    $ dnc.fit = "guard"
    $ vn_enter(bg="dnc_market", pc="nervous", pc_tag="dnc_pc", cast=[("dnc_corvin", "merchant")], cg="dnc_market_noon")
    "You go down to the market at noon for Senna, for silver filings, in a borrowed cloak with the hood up. The guard's tabard won't close over your chest any more."
    "Corvin passes you at the cheese stall. He doesn't stop. He doesn't look at you. He just says it, under his breath, in passing, like a man remarking on the weather."
    dnc_corvin "\"{b}Ysmeral.{/b} The yard tonight. For the street, this time.\""
    "{color=#ff5fb8}The crest takes it and holds it, a warm hum under your navel all afternoon, and it doesn't let go. You go back up the hill. You give Senna her silver. You sit through supper. And at a quarter to nine you find yourself in Lys's veils, at the bottom of the hill, walking.{/color}"
    $ vn_set_time(21, 0)
    $ dnc.fit = "dancer"
    $ vn_enter(bg="dnc_wine_yard", pc="flustered", pc_tag="dnc_pc", cast=[("dnc_corvin", "merchant")], cg="dnc_yard_dance")
    "The yard behind the wine house is ringed with lamps tonight, like the court on Spring Eve. The back gate's open."
    "And behind it, in the lane, the street: forty people, fifty, more, faces you know, holding cups, waiting."
    dnc_corvin "\"The dancer of the Veil, ladies and gentlemen. Seven figures.\""
    "{color=#ff5fb8}You dance. Your big breasts sway under the thin silk, your hips roll, a veil comes off at every figure, and the crowd at the gate goes quiet the way the crowd on the hill went quiet, except it isn't the same quiet at all.{/color}"
    menu:
        "Fifty people are watching you dance naked in a wine yard."
        "Look at the crowd":
            "You look. You can't help it. The baker's wife with her hand over her mouth. The bailiff's man, red to the ears."
            "Faces that bought bread from you, saluted you, called you sword-brother. All of them watching your breasts bounce. The crest drinks that too, somehow, and you get wetter."
            $ dnc.asked += 1
        "Close your eyes":
            "You close your eyes and dance blind, the way you'd stand watch on a cold night, counting steps, thinking of Lys on the rock under the willows. It's the only thing that stays yours."
            $ dnc.held += 1
    $ vn_enter(bg="dnc_wine_yard", pc="moaning", pc_tag="dnc_pc", cast=[("dnc_corvin", "merchant"), ("dnc_senna", "mage")], cg="dnc_yard_senna")
    "When the last veil's down, Senna comes through the side gate with her coat open and her cock hard and her eyes wide and wet with the name, and Corvin smiles."
    dnc_corvin "\"Our mage came looking for you. Wasn't that thoughtful. {b}Ysmeral.{/b} Both of you, on the bench. The street's waiting.\""
    show cg dnc_yard_dp onlayer cgl
    "Senna sits on the long bench and pulls you down into her lap, facing the gate, facing the street, and her cock slides up into your wet pussy."
    "And Corvin kneels up behind you and pushes into your arse, and the two of them fill you, both at once, so full you can't breathe."
    vn_sfx "Zupuu. Zuchu."
    dnc_senna "\"Aren— Aren, I'm sorry, I'm— oh gods, I can feel him through you—\""
    dnc_you "\"AHH♡— both of you— both— it's too much— it's so much, I'm so full, I'm so full♡—\""
    vn_sfx "Pan. Pan. Pan. Pan."
    "The bench creaks. The lamps swing. Your heavy breasts bounce in front of fifty faces, and you're screaming and you don't care who hears, because everybody does."
    dnc_you "\"Look at me— everyone's looking— AHH♡— I'm coming— I'm coming in front of all of you— AHHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Dopyu. Dopyu. Dopyu."
    "And as you come, with Senna's face pressed into your back, she breathes something against your skin that isn't a moan."
    dnc_senna "{i}\"I found it. Last night. The Double Figure. Two daughters of the Veil can dance the seal shut together, and the crests bind to each other instead of the name. You and Lys. Tomorrow. The new moon.\"{/i}"
    call dnc_cut(5, 1, "Friday. The seventh morning. The new moon.")
    jump dnc_friday

## ---- 7. Friday: the new moon ----------------------------------------------------------------------------------

label dnc_friday:
    $ dnc.fit = "shift"
    $ dnc_grow(7)
    $ vn_enter(bg="dnc_temple_cell", pc="stern", pc_tag="dnc_pc", cast=[], cg="dnc_mirror_friday")
    "{color=#ff5fb8}The last morning. You stand in front of the shaving mirror you haven't needed all week and look at a woman.{/color}"
    "{color=#ff5fb8}A hundred and sixty-five centimetres, a dancer's body: long legs, strong thighs, round hips and a round arse, a narrow waist, and big, heavy breasts, full and soft and riding high, swaying when you breathe.{/color}"
    "{color=#ff5fb8}Rose-gold hair falls in waves to your waist. Your face is a woman's face, with your own eyes in it. The crest sits low under your navel, rose gold, warm, complete.{/color}"
    "Your sword's still on its peg. You touch the hilt. You leave it there."
    $ vn_set_time(5, 30)
    $ dnc.fit = "dancer"
    $ vn_enter(bg="dnc_dance_court", pc="flustered", pc_tag="dnc_pc", cast=[("dnc_lys", "dancer"), ("dnc_senna", "mage")], cg="dnc_double_rehearsal")
    "At dawn, on the empty court, with Senna reading from the roll, Lys teaches you the Double Figure."
    "It's the same seven figures, only for two, mirrored, hand to hand, two dancers turning round one another the way the moon turns round the earth."
    "Lys is in her own veils for the first time in a week. You're in a set Senna found in the vestry, a shade deeper rose."
    dnc_lys "\"Hands here. No, here. You're not the guard any more, you don't have to hold me up. Let me hold you.\""
    menu:
        "Her hands are warm in yours. The crests are warming each other through the silk."
        "Follow Lys":
            "You let her lead. You've watched her dance for three years, and now you're inside it, following her turn for turn, and it's like being carried by water."
            dnc_lys "\"There. There you are. Aren, you're beautiful at this.\""
            $ dnc.held += 1
        "Take the lead":
            "You take the lead. You know the steps; your body knows them too well now."
            "Lys follows you, surprised, then laughing, and you turn her round the court like the Unveiled turned you."
            dnc_lys "\"...Where did you learn to move like that?\""
            "You don't answer. You both know."
    $ vn_set_time(23, 0)
    $ vn_enter(bg="dnc_dance_court", pc="nervous", pc_tag="dnc_pc", cast=[("dnc_lys", "dancer"), ("dnc_corvin", "merchant")], cg="dnc_new_moon")
    "The new moon. No moon at all. The lamps round the court are lit, and Senna's at the ward line, and Lys is beside you in her veils."
    "And up the hill, with lanterns, come the Unveiled. Twenty men. Thirty. Corvin at the front in a black cloak, smiling."
    dnc_corvin "\"The seventh night. You've kept your bargain, and I've kept mine: not a finger on her.\""
    dnc_corvin "\"Now come here and finish it, and the crest closes on my name for good, and the dancer is mine for good. {b}Ysmeral.{/b}\""
    "{color=#ff5fb8}The crest pulls. Towards him, towards the cellar, towards every man on that slope. Your feet take a step on their own.{/color}"
    "And Lys's hand tightens on yours, and her crest pulls the other way."
    if dnc.held >= 7:
        dnc_lys "\"You fought them all week, my love. One more figure. Fight with me.\""
    elif dnc.asked >= 5:
        dnc_lys "\"I know what it's done to you. I know what you want now. I still want you. Dance with me.\""
    else:
        dnc_lys "\"Aren. Look at me, not at him. Dance with me.\""
    menu:
        "Two pulls. One crest. Seven figures."
        "Dance with Lys" (ending=True):
            jump dnc_end_sealed
        "Dance for them" (ending=True):
            jump dnc_end_enslaved

## ---- Ending A: Sealed ----------------------------------------------------------------------------------------

label dnc_end_sealed:
    $ vn_enter(bg="dnc_dance_court", pc="stern", pc_tag="dnc_pc", cast=[("dnc_lys", "dancer"), ("dnc_corvin", "merchant")], cg="dnc_sealed_dance")
    "You turn your back on him. You take both of Lys's hands. And you dance."
    "The first figure. Corvin says the name, louder, and it slides off you like rain off oiled cloth. The second. The third. Hand to hand, turning round one another."
    "Your crest is listening to hers, and hers to yours, and neither of them can hear anything else."
    dnc_corvin "\"{b}Ysmeral!{/b} {b}YSMERAL!{/b}\""
    "The fifth figure, the hard one. Both of you on one heel, all fourteen veils flying. The sixth. The seventh: you kneel together and press four palms flat to the stone."
    vn_sfx "Vwoom."
    "The rose light goes down this time. Down into the hill, all of it, like water into sand. Something under the stone sighs in its sleep and turns over and is quiet. Sealed."
    "Properly, for the first time in three hundred years."
    "When you look up, the town's on the slope, everyone, with lanterns. They saw it all."
    "Mother Aud is standing at the court gate with the bailiff and six guards, pointing at Corvin Hale, and for once in his life Corvin has nothing to say."
    $ vn_set_time(2, 0)
    $ dnc.fit = "nude"
    $ vn_enter(bg="dnc_lys_room", pc="blissful", pc_tag="dnc_pc", cast=[("dnc_lys", "dancer")], cg="dnc_sealed_lys")
    "Lys's room above the vestry, with the shutters open on the dark and a single candle. Her veils on the floor with yours."
    "Her brown skin and your pale, her black curls and your rose gold."
    show cg dnc_sealed_love onlayer cgl
    "She lays you down and kisses you everywhere: your mouth, your throat, your heavy new breasts, slow, the way you used to kiss her."
    "Then she climbs over you and fits her thigh between yours and yours between hers, and presses down, crest to crest, wet to wet."
    vn_sfx "Kuchu. Kuchu."
    dnc_lys "\"Mine. You're mine, not theirs. Say it.\""
    dnc_you "\"Yours♡— Lys, I'm yours, I'm all yours— ahh♡— oh, oh, it's— they're glowing, Lys, look—\""
    "The two crests glow together, rose and rose, brighter with every roll of her hips, and you can feel what she feels through them, her pleasure stacking on yours, doubling, doubling again."
    dnc_lys "\"Aren— Aren♡— I can feel you— I can feel you coming— ahh♡—\""
    dnc_you "\"Lys♡— Lys♡— LYS♡— AHHH♡—!\"" with vnfx("flash", "shake")
    "You come together. Of course you do. The crests won't have it any other way."
    $ vn_set_time(20, 0)
    $ vn_clock.day += 358
    $ dnc.fit = "dancer"
    $ vn_enter(bg="dnc_dance_court", pc="blissful", pc_tag="dnc_pc", cast=[("dnc_lys", "dancer"), ("dnc_senna", "mage")], cg="dnc_sealed_epilogue")
    "Spring Eve, a year on. The whole town up the hill with lanterns, and the court ringed with gold lamps, and Senna Dray, who stayed, at the ward line. Her crest went quiet."
    "The rest of the change didn't go anywhere, and she's decided she doesn't mind."
    "And on the court, for the first time in Hollin's history, two dancers. Two sets of seven veils, two shades of rose."
    "Lys, and the woman everyone in town still calls Sword-Sister Vale."
    "You dance the Double Figure, hand in hand, and the crowd sighs on the fifth, and nobody falls."
    if dnc.held >= 7:
        "Afterwards, your old sword hangs on the wall above your shared bed. You still oil it every month. You don't need to. You like to."
    call dnc_route_return("Sealed")

## ---- Ending B: Enslaved -------------------------------------------------------------------------------------

label dnc_end_enslaved:
    $ vn_enter(bg="dnc_dance_court", pc="blissful", pc_tag="dnc_pc", cast=[("dnc_lys", "dancer"), ("dnc_corvin", "merchant")], cg="dnc_enslaved_turn")
    "You let go of her hand."
    dnc_lys "\"Aren—\""
    "You don't look back. You can't. The crest is singing and the slope is full of men who've had you every night for a week, and that's where the hunger points, and you follow it."
    "You dance the seven figures for them. Not on the stone over the hill: in front of Corvin. Your hips rolling, your breasts swaying, a veil off at every figure."
    "The seventh figure, the kneel and the reach, and you kneel to him, and press your palms flat to his boots."
    vn_sfx "Vwoom."
    "{color=#ff5fb8}The crest closes. You feel it lock, low and deep, on his voice, on that one word. The hill sleeps on, the dance was finished on Spring Eve and the seal holds. But the dancer doesn't belong to the Veil any more.{/color}"
    dnc_corvin "\"Good girl. Lys, my dear, as promised: go home. Nobody will touch you. She bought that, fair and square.\""
    $ vn_set_time(1, 0)
    $ dnc.fit = "nude"
    $ vn_enter(bg="dnc_wine_cellar", pc="blissful", pc_tag="dnc_pc", cast=[("dnc_corvin", "merchant"), ("dnc_senna", "mage")], cg="dnc_enslaved_cellar")
    "The cellar, at one in the morning, full to the vaults. Your cellar now."
    "Senna's there too, with her crest on the same leash as yours, and her cock hard, and her eyes soft with the name."
    show cg dnc_enslaved_all onlayer cgl
    "Corvin in your pussy and Senna in your arse, and a cock in each hand, and one at your lips when you can spare your mouth from screaming. You can't spare it often."
    vn_sfx "Pan. Pan. Juppu. Pan."
    dnc_you "\"More♡— more, all of you, I'm yours, I'm the Unveiled's dancer, I'm yours every night— AHH♡—\""
    dnc_senna "\"Aren♡— Aren, I'm— together, come with me—\""
    dnc_you "\"Fill me♡— fill me up, Corvin, Senna, everyone, I don't want to stop, I never want to stop— AHHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Dopyu. Dopyu. Dopyu."
    $ vn_set_time(21, 0)
    $ vn_clock.day += 30
    $ dnc.fit = "dancer"
    $ vn_enter(bg="dnc_wine_yard", pc="blissful", pc_tag="dnc_pc", cast=[("dnc_corvin", "merchant")], cg="dnc_enslaved_epilogue")
    "A month later. The wine house does better trade than it has in thirty years."
    "Every night at nine the yard lamps are lit, and the back gate is opened, and the street comes to watch the dancer of the Unveiled dance her seven figures."
    "She's very good. She smiles the whole time. She's loud, after."
    if dnc.held >= 7:
        "Sometimes, on the turn in the fifth figure, she looks up the hill. There's a lantern at the temple gate, every night, burning till dawn. She never mentions it, and nobody ever asks."
    else:
        "Up on the hill, there's a lantern at the temple gate every night, burning till dawn. The dancer doesn't look up at it. The crest doesn't let her want to."
    call dnc_route_return("Enslaved")
