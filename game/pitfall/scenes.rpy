## THE STORY: chapters 3-5 (PLAN.md): the sending (the Hollow answers in Mother Ysolde's voice), the vows, the warmth.

## ---- 3. Thursday: the sending -------------------------------------------------------------------------------------

label pfl_thursday:
    $ pfl.fit = "nude"
    $ pfl_grow(3)
    $ vn_enter(bg="pfl_dark", pc="serene", pc_tag="pfl_pc", cast=[], cg="pfl_sending")
    "Very well. Two failures."
    "The light went nowhere, the purification went nowhere, and the sweetness is still here, and the warmth, and the heavy, pleasant tiredness that comes after every casting and lasts longer each time."
    "There's no shame in a third approach. There's a sending: a short prayer that carries a voice to the Mother House, to the one who holds your vows."
    "It's meant for the dying, mostly, and for the lost. You're neither. But you're the Order's best, and the Order ought to know where its best has got to."
    menu:
        "What do you tell her?"
        "Ask for help":
            "You tell her the truth. \"Mother. It's Aubin. I'm in a pit in Fallowmere wood under a paralysis I can't break. Send someone. Please.\" The {i}please{/i} costs you something."
            "You say it anyway."
        "Say you're fine":
            "You tell her you're fine. \"Mother. It's Aubin. A delay at Fallowmere, nothing more. I'm quite well. I'll be home within the week.\" There's no reason to worry her."
            "There's no reason to worry anyone."
    vn_sfx "Fwaaaa—"
    "It goes out of you like the others: a long clean pour, and the tiredness after."
    "And this time, something answers."
    pfl_mother "\"Aubin.\""
    "Her voice. Low and dry and patient, the voice that heard your first vows and your last confession. It sounds very close, as if she were kneeling beside you."
    pfl_mother "\"Aubin, my dear. You've worked so hard. You always work so hard. Rest now. Stay where you are, and rest, and let the warmth hold you. Everything is being taken care of.\""
    "You've known Mother Ysolde for six years. She has never once called you {i}my dear.{/i}"
    "It's a strange thing to notice. You notice it. And then the warmth comes in round the edges of the thought, like water round a stone, and it's harder to see the shape of it."
    $ vn_set_time(11, 0)
    $ vn_enter(bg="pfl_pit", pc="moaning", pc_tag="pfl_pc", cast=[], cg=None)  # d1 10:28 am: milking no picture, failed 3 draws (QA findings-df8ae07c)
    "{color=#7fe8c0}It has her voice because it drank it. It drinks everything he sends out, and a sending carries a voice both ways. The Hollow has never had a voice before. It likes this one very much.{/color}"
    "{color=#ff5fb8}His chest has gone soft, a gentle swell round each fat pink nipple, nothing like breasts, only soft, the way the rest of him is going soft.{/color}"
    "{color=#ff5fb8}His hips are wide now under the narrow waist. His arse is big and round and heavy, and the coils knead it like dough.{/color}"
    "{color=#ff5fb8}His hair spills down his back to the middle, mint from the ends halfway up, honey-gold above.{/color}"
    "{color=#7fe8c0}A new tentacle slides over his cock: a sleeve, wet and ridged inside, that swallows it to the root. It begins to pull.{/color}"
    vn_sfx "Jupo. Jupo. Jupo."
    pfl_you "\"Ahh— ahh♡— it's— hah— sucking— ahh♡—\""
    pfl_mother "\"That's it. Good. Let it all go.\""
    "{color=#7fe8c0}The voice is in his head. It's also, now, in the pit: the Hollow murmurs it out of the dark in the same low patient tones, all round him, and his body hears it even if he can't.{/color}"
    pfl_you "\"Mother— ahh♡— Mother— I'm— AHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Byuru. Byuru. Byururu."
    "{color=#7fe8c0}The sleeve swallows it. And keeps pulling. And he comes again, eleven minutes later, and again, and again, and the sleeve drinks every drop, because everything he has is food.{/color}"
    pfl_you "\"Again— ahh♡— again— don't stop— ahh, Mother, don't stop♡—\""
    $ vn_set_time(15, 0)
    $ vn_enter(bg="pfl_dark", pc="dazed", pc_tag="pfl_pc", cast=[], cg="pfl_rest_brother")
    pfl_mother "\"Are you resting, Aubin?\""
    menu:
        "Rest, she says."
        "Do as she says":
            "Yes, Mother. Of course. You always do as she says; it's in the vows, isn't it, or near enough. You stop trying to think of a fourth approach. You rest."
            "It's the easiest thing you've ever done."
            pfl_mother "\"Good. Good. That's my dear.\""
            $ pfl.slipped += 1
        "Ask her to come for you":
            "\"Come for me, Mother. Come yourself. Please.\""
            pfl_mother "\"I'm coming. I'm already on my way. I'll be there so soon. Until I am, you rest. Promise me.\""
            "You promise. It doesn't feel like giving in. It feels like obedience, which is a virtue."
            $ pfl.held += 1
    "{color=#7fe8c0}The Hollow strokes his face with the tip of a tentacle, in the dark, and says it again in her voice, so softly it's barely a sound: \"Rest.\"{/color}"
    call pfl_cut(7, 1, "Friday. He thinks it's Wednesday, perhaps.")
    jump pfl_friday

## ---- 4. Friday: the vows ------------------------------------------------------------------------------------------

label pfl_friday:
    $ pfl.fit = "nude"
    $ pfl_grow(4)
    $ vn_enter(bg="pfl_dark", pc="serene", pc_tag="pfl_pc", cast=[], cg="pfl_vows")
    "You've lost count of the offices. That's never happened. You've kept the hours since you took the habit; you could keep them in your sleep, and sometimes did."
    "When you lose your place, the sister who trained you used to say, go back to the vows. They're the floor under everything. Stand on them."
    "So you stand on them. Or you would, if you could feel your feet."
    menu:
        "The four vows of the Lamp."
        "Say them slowly":
            "Slowly, then. One word at a time, every word weighed, the way you said them the first time in front of the whole Order with your heart going like a drum."
            $ pfl.held += 1
        "Say them as they come":
            "You let them come the way they always come, all in one breath, worn smooth with saying. You don't need to think about the vows. They're part of you."
            $ pfl.slipped += 1
    "{i}I give myself to the Light.{/i}"
    "{i}I keep my body open for the Light.{/i}"
    "{i}I keep my word, and I keep my watch, and I keep...{/i}"
    "You stop."
    "That's not right. Is it? {i}Clean.{/i} I keep my body {i}clean{/i} for the Light. Isn't it? You've said it ten thousand times. It sounded perfectly right as you said it. Open. Clean."
    "They're very nearly the same word, if you think about it. A clean thing is an open thing. A vessel."
    "You think about it for a long time, and it seems to make more sense the longer you do."
    $ vn_set_time(10, 30)
    $ vn_enter(bg="pfl_pit", pc="moaning", pc_tag="pfl_pc", cast=[], cg="pfl_both_ends")
    "{color=#7fe8c0}He keeps it open. That's the joke the Hollow would make, if the Hollow made jokes: he keeps it beautifully open.{/color}"
    "{color=#ff5fb8}His thighs have thickened, soft and full, pressing together under the swell of an arse that's bigger again this morning, round and heavy and jiggling every time the coils shift it.{/color}"
    "{color=#ff5fb8}His hair falls to the middle of his back and it's nearly all mint now, glowing faintly, with the honey-gold left only in the top third.{/color}"
    "{color=#7fe8c0}They hold him on his knees with his face lifted. One tentacle slides into his open mouth, slick and sweet, and another, thick as two fingers, slides into his arse, and they begin to move together, one in as the other draws back.{/color}"
    show cg pfl_spitroast onlayer cgl
    vn_sfx "Jupo. Pan. Jupo. Pan."
    pfl_you "\"Mmh— mmmh♡— mmh— mmmh♡—\""
    "{color=#7fe8c0}His lips stretch round it, fuller than a week ago, soft and pink. His tongue works it without being asked.{/color}"
    "{color=#7fe8c0}His throat opens when it pushes, because the fluid has made every part of him easy, and his whole body rocks between the two of them, forward and back, forward and back.{/color}"
    "{color=#7fe8c0}The one in his mouth pulls free just long enough.{/color}"
    pfl_you "\"Both— ahh♡— both ends— fill me up— keep me open— keep me— AHHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Byuru. Byuru. Dopyu."
    "{color=#7fe8c0}They both pump sweet fluid into him at once, mouth and arse, and his cock spurts onto the coils in time. Inside his head, he is working out that {i}open{/i} and {i}clean{/i} are the same word, and feeling very wise.{/color}"
    $ vn_set_time(16, 0)
    $ vn_enter(bg="pfl_dark", pc="dazed", pc_tag="pfl_pc", cast=[], cg="pfl_vows_again")
    menu:
        "The vows sit in your head, a word different."
        "Start again":
            "No. Again, from the top. {i}I give myself to the Light. I keep my body clean for the Light.{/i} Clean. There."
            "It took three tries to get the word to stay, and it still sounds wrong to you, but it's the right one. You know it's the right one."
            "You hold onto it with both hands."
            $ pfl.held += 1
        "Leave it there":
            "Leave it. Open, clean: what does it matter? The Light knows what you mean. And {i}open{/i} feels truer, somehow, today. It feels like something you'd say if you were being honest."
            "You say it again, the new way, and it fits better each time."
            $ pfl.slipped += 1
    call pfl_cut(7, 1, "Saturday. He has stopped guessing the day.")
    jump pfl_saturday

## ---- 5. Saturday: the warmth --------------------------------------------------------------------------------------

label pfl_saturday:
    $ pfl.fit = "nude"
    $ pfl_grow(5)
    $ vn_enter(bg="pfl_dark", pc="blissful", pc_tag="pfl_pc", cast=[], cg="pfl_the_warmth")
    "You don't try anything this morning. There doesn't seem to be anything to try. Mother is coming; Mother said rest; you're resting. You have never in your life been so rested."
    "The warmth is everywhere now. It isn't round you; it's {i}in{/i} you, in your head where your body ought to be, soft and close and kind. It hums."
    "You've started to think that it hums back when you think at it."
    "It would be strange, you think, to go a whole day without praying. So you pray."
    menu:
        "To whom?"
        "Pray to the Light":
            "To the Light, as always."
            "{i}Lord of the Lamp, who sees in every dark—{/i} and halfway through you find you're talking to the warmth instead, telling it how good it's been to you, thanking it for holding you, and you have to stop and begin again, and the same thing happens."
            "The third time, you let it. The Light sees in every dark. Perhaps this is what it looks like."
            $ pfl.held += 1
        "Pray to the warmth":
            "To the warmth, of course. It's right here. It's been so good to you. {i}Thank you for holding me. Thank you for keeping me. Thank you for being so warm.{/i}"
            "The hum gets louder, and sweeter, and you feel answered for the first time in years."
            $ pfl.slipped += 1
    "It ought to have a name, something that kind. You feel rude, praying to it without one."
    menu:
        "What do you call it?"
        "Call it the Hollow":
            "The Hollow. It's what it is: a hollow, a place you fell into. A plain honest name. You won't dress it up. You think the name at it, carefully, and it hums."
            $ pfl.held += 1
        "Call it Mother":
            "Mother. It's the only word big enough. It's the one that came to your lips without thinking. You think the name at it, shy, and the hum goes deep and long and glad."
            $ pfl.slipped += 1
    $ vn_set_time(13, 0)
    $ vn_enter(bg="pfl_pit", pc="moaning", pc_tag="pfl_pc", cast=[], cg="pfl_the_eldest")
    "{color=#7fe8c0}It answers to whatever he calls it. It has never been called anything before.{/color}"
    "{color=#ff5fb8}His arse is huge now.{/color}"
    "{color=#ff5fb8}Round and soft and wide, swelling out from a waist that's narrower than ever, a great heavy curve that spills over the coils on both sides and shivers when they touch it.{/color}"
    "{color=#ff5fb8}His hips flare to match. His hair falls to the small of his back, mint all the way to a band of honey-gold at the roots.{/color}"
    "{color=#7fe8c0}And from the bottom of the Hollow, where it's oldest, comes the eldest tentacle: dark, slow, thick as a wrist, its glowing veins pulsing as it rises.{/color}"
    "{color=#7fe8c0}They lift him onto his back and fold his thick thighs to his chest and spread that enormous arse open between them, and it presses against him, and his hole opens for it, and opens, and opens, and takes it.{/color}"
    vn_sfx "Zuuuu— gupu."
    pfl_you "\"Ahh— ahh— so— so big— ahhh♡— it's so big— ahh♡—\""
    "{color=#7fe8c0}It goes deep. Deeper than anything has. His whole body shudders round it and his mouth stays open on one long sigh, and then it begins to move, slow and enormous, and every stroke shoves his body up the coils and lets it slide back down.{/color}"
    show cg pfl_eldest_deep onlayer cgl
    vn_sfx "Gupu. Gupu. Gupu. Pan."
    pfl_you "\"Mother— Mother— fill me— I'm yours— ahh♡— I'm all yours— AHHHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Byuru. Byururu. Dopyu."
    "{color=#7fe8c0}He comes so hard his back lifts clear of the coils. The eldest stays in him, buried, pulsing, while he shakes.{/color}"
    "{color=#7fe8c0}In his head, he's thanking the warmth for the lovely day.{/color}"
    if pfl.slipped > pfl.held:
        "{color=#7fe8c0}The Hollow has been making priests for a long time, whatever it got. It has never made one so glad to be made.{/color}"
    else:
        "{color=#7fe8c0}There's still a hard bright thread in him somewhere, holding. The Hollow can feel it, the way you'd feel a stone in a shoe. It doesn't mind. It has one more day.{/color}"
    call pfl_cut(7, 1, "Sunday.")
    jump pfl_sunday
