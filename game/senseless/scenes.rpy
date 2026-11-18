## THE STORY: chapters 3-5 (PLAN.md). Tuesday the reveal in the hour (Hesper at the desk), Wednesday the honest rune and
## Hesper's glass cock, Thursday why he raced her and the tentacles at both ends.

## ---- 3. Tuesday: the hand in the dark ----------------------------------------------------------------------------

label sns_tuesday:
    $ sns.fit = "nude"
    $ sns_grow(3)
    $ vn_enter(bg="sns_cradle_room", pc="dazed", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_third_morning")
    "{color=#ff5fb8}In the mirror: black hair to your jaw now, soft, and at the roots a sheen of violet when the light catches it, the colour of the flask on the plinth.{/color}"
    "{color=#ff5fb8}Your face is a woman's face with your eyes in it.{/color}"
    "{color=#ff5fb8}Down there, from last night, you know there's a real weight to your chest, two soft breasts that sway when the tentacles move you, and your hips have started to flare.{/color}"
    sns_you "\"I've got tits, haven't I.\""
    sns_hesper "\"How would I know? I can't see down there either.\""
    "She says it to the daybook. She turns a page that doesn't need turning."
    call sns_rune("\"Morning three,\" Hesper says. \"Four to go. Which one?\"")
    "She goes down at ten with her lamp and her daybook. \"The drain, today. I think I've nearly found the way into the pit room.\" She's gone all day."
    $ vn_set_time(16, 0)
    $ vn_enter(bg="sns_cradle_room", pc="smug", pc_tag="sns_pc", cast=[], cg="sns_alone")
    "You spend the afternoon talking to the flask on the plinth. It's the only thing in the room to talk to."
    sns_you "\"You know what, I'm still getting you.\""
    sns_you "\"I'm getting out of this, and I'm walking over there, and I'm putting you in my bag, and I'm selling you to the Hall for more money than Vane's made in her whole life.\""
    sns_you "\"That's what's happening. That's the plan.\""
    "The flask glows on, violet and patient. Under the floor, things you can't feel go on doing things you can't feel to a body you can't see."
    $ vn_set_time(21, 0)
    $ vn_enter(bg="sns_cradle_room", pc="moaning", pc_tag="sns_pc", cast=[], cg="sns_hour_tuesday")
    "Nine o'clock. Hesper isn't back. The stone chimes, and everything comes back."
    call sns_hour_part
    show cg sns_the_hand onlayer cgl
    "And then something touches your hip that isn't a tentacle."
    "Five fingers. Warm and dry. A callus across the palm, the one you get from a rope."
    "It rests on the new swell of your hip and squeezes, testing, the way you'd test a melon at market."
    "And a voice, from the dark beneath you, right by your belly. Calm. Pleased. Hers."
    sns_hesper_below "\"Again. The hip key. Hold it there— there. Good. Now the second one.\""
    vn_sfx "Click."
    "Brass, turning in a lock."
    "And every tentacle under the floor moves at once, like an orchestra at a nod, and a second one pushes into your arse beside the first, and you scream."
    sns_you "\"HESPER?!\""
    "Silence below. Then, unbothered:"
    sns_hesper_below "\"Hello, Rook.\""
    vn_sfx "Click. Click."
    sns_you "\"You— it's {i}you{/i}— you're down there, you're— AHH♡— don't you dare turn that— AHH♡—\""
    sns_hesper_below "\"This one's the nipples. And this one—\""
    vn_sfx "Click."
    sns_you "\"AHHHH♡— Hesper— Hesper you bitch— you— I'm coming— I'm coming, you're making me come, you— AHHHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Byuru. Byuru."
    "She doesn't let up. Not for the rest of the hour."
    "She plays the desk like an organ, key by key, and she talks you through every one, and you come four more times in her hands, or its hands, which turn out to be the same thing."
    $ vn_set_time(22, 10)
    $ vn_enter(bg="sns_cradle_room", pc="angry", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_the_key")
    "At ten past ten she comes up the stair with her lamp, quite calm, and sits down cross-legged at the rim, and holds up a ring of brass keys."
    sns_hesper "\"Quist's desk is in the pit room. Five keys for the five works, and a sixth for the lever. One pull, and the Cradle opens. I found it on Saturday afternoon. I had my hand on the lever.\""
    sns_hesper "\"And then it was nine o'clock, and there's a grate in the desk you can look through, and I looked.\""
    menu:
        "Four days. She could have pulled it four days ago."
        "Swear at her":
            sns_you "\"You lying, sneaking, back-stabbing— you {i}cheat{/i}— you absolute— four {i}days{/i}, Vane—\""
            "You run through every word you know and some you make up. She lets you."
            "She sits there with her chin on her fist and lets you, and when you run out of breath she nods, as if you've made a fair point."
            sns_hesper "\"Two years, Rook. Two years of you taking my maps and my finds and my evenings at the Hall, and laughing. I was owed something.\""
            sns_hesper "\"And then I saw what it was doing to you, and I heard you, and I didn't want to stop.\""
            $ sns.brat += 1
        "Ask her why":
            sns_you "\"...Why?\""
            "She thinks about it properly. That's the thing about Hesper: she always thinks about it properly."
            sns_hesper "\"Revenge, at first. Two years of you, Rook. I thought I'd let it run one hour and then pull the lever and tell everyone at the Hall. And then I heard you. And I watched you.\""
            sns_hesper "\"And I didn't want to stop. I don't want to stop now.\""
            $ sns.soft += 1
    sns_you "\"The runes. The 'seal'. You said they thinned the seal.\""
    sns_hesper "\"They're the same five works as the keys downstairs. You've been choosing, every morning. I just never told you what for. I read you the first half of the sentence.\""
    sns_hesper "\"No more of that. Tomorrow I'll ask you properly. And you'll answer me properly.\""
    "She puts her coat round your shoulders, same as every night, and goes to sleep by the stair. You lie awake in the collar and think about her voice in the dark."
    "You think about it a lot longer than you think about the lever."
    call sns_cut(8, 1, "Wednesday. The fourth morning.")
    jump sns_wednesday

## ---- 4. Wednesday: asked properly ----------------------------------------------------------------------------

label sns_wednesday:
    $ sns.fit = "nude"
    $ sns_grow(4)
    $ vn_enter(bg="sns_cradle_room", pc="flustered", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_told_true")
    "This morning she tells you the truth, all of it, kneeling at the rim with the lamp, describing what she sees through the grate like a surveyor describing a site."
    "She's a very good surveyor."
    sns_hesper "\"Breasts. Real ones. A good handful each, round, high, the nipples dark and puffy. Your waist goes in like an hourglass. Your hips go out. And your arse, Rook.\""
    sns_hesper "\"Your arse is round and soft and I could lose a hand in it.\""
    "{color=#ff5fb8}Your hair brushes your shoulders when you turn your head. Your lips are soft and full; you can feel them, at least.{/color}"
    "{color=#ff5fb8}Everything else you've only ever felt in the dark, an hour at a time, and now she's saying it out loud in the morning and you're going red to your collarbones.{/color}"
    sns_hesper "\"And your cock's still there. Smaller than it was. Very, very sensitive. I've checked.\""
    sns_you "\"You've {i}checked{/i}.\""
    sns_hesper "\"Thoroughly. So.\""
    call sns_rune("She sets the key ring down by your hand. \"No lies. Chest, nipples, hips, cock, mouth. Where do you want them today?\"")
    sns_hesper "\"Good choice.\""
    "And she goes down the stair humming."
    $ vn_set_time(21, 0)
    $ vn_enter(bg="sns_pit", pc="moaning", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_pit_lamp")
    "Nine o'clock, and everything comes back, and for the first time there's light down there: her lamp on Quist's desk, a violet-black room, the walls alive with tentacles, slow and glossy as eels."
    "You can't see it. But she tells you."
    call sns_hour_part
    show cg sns_glass_cock onlayer cgl
    "Then the tentacles turn you, gently, all of you below the collar, and spread your thighs, and lift your round new arse up into the lamplight. And a hand on your hip."
    "And something cool and smooth and hard nudging at your arse, which is already slick and open from all day."
    sns_hesper "\"Quist's cabinet. He kept implements. This one's glass, and it's warm now, and it's strapped on very securely. Breathe out.\""
    vn_sfx "Zupu."
    sns_you "\"Hesper— Hesper, it's— it's {i}you{/i}— you're fucking me— AHH♡—\""
    sns_hesper "\"I'm fucking you. And they're holding you for me. Say something rude, Rook. You always do.\""
    menu:
        "Her hips against your arse. Her hands on your waist. Her glass cock all the way in."
        "Call her a cheat":
            sns_you "\"You— you cheat— you dirty, cheating— AHH♡— you couldn't beat me to a single— single find— so you— hhh♡— so you—\""
            sns_hesper "\"So I found you instead. Say it again.\""
            sns_you "\"CHEAT♡—\""
            $ sns.brat += 1
        "Call her name":
            sns_you "\"Hesper— Hesper— Hesper♡—\""
            "It's all you can say. You say it every time she pushes in, and she makes a sound you've never heard her make, and pushes harder."
            $ sns.soft += 1
    vn_sfx "Pan. Pan. Pan. Nuchu."
    "She fucks you with long, hard, steady strokes, and the tentacles milk your cock and suck your nipples in time with her, and your new breasts bounce and sway in the coils, and you can't see any of it and you can feel all of it."
    sns_you "\"I'm— Hesper I'm— don't stop don't stop don't— AHHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Byuru. Byuru. Byuru."
    "She doesn't stop. She told you she wouldn't."
    call sns_cut(8, 1, "Thursday. The fifth morning.")
    jump sns_thursday

## ---- 5. Thursday: why you raced her -----------------------------------------------------------------------------

label sns_thursday:
    $ sns.fit = "nude"
    $ sns_grow(5)
    $ vn_enter(bg="sns_cradle_room", pc="dazed", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_fifth_morning")
    "{color=#ff5fb8}Hair past your shoulders, black, the violet sheen running all the way down it now.{/color}"
    "{color=#ff5fb8}Hesper says your breasts are full and heavy, big enough to fill both her hands and spill, your thighs thick and soft, your hips wide.{/color}"
    "{color=#ff5fb8}You're shorter, too; the collar sits higher round you than it did. The rim's been adjusting.{/color}"
    call sns_rune("\"Day five,\" Hesper says, and puts her chin in her hand. \"Where?\"")
    $ vn_set_time(15, 0)
    $ vn_enter(bg="sns_cradle_room", pc="flustered", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_honest_talk")
    "She doesn't go down in the afternoon."
    "She sits with her back against the collar's rim, next to your shoulder, and you can feel the heat of her through her shirt against your arm, which is about the only part of you that feels anything in daylight."
    sns_hesper "\"Can I ask you something? Why my maps? Why always mine? There are forty delvers at the Hall, and you could have beaten any of them. You always came after me.\""
    menu:
        "She's not looking at you. She's looking very hard at the flask on the plinth."
        "Keep it a joke":
            sns_you "\"Because yours were the best maps. Obviously. I've got taste.\""
            sns_hesper "\"Right.\""
            sns_you "\"And because your face when I beat you was the best thing in Brackwater. The pint was worth it.\""
            "She laughs, despite herself. Then she turns and looks at you, very close, and you stop being funny."
            $ sns.brat += 1
        "Tell her why you raced her":
            sns_you "\"Because you're the only one worth racing.\""
            sns_you "\"Because you're better than me and everyone knows it but you, and the only way I could get you to look at me was to take something of yours and run.\""
            sns_you "\"I took your maps so you'd come after me. Every time. Two years. And you always came.\""
            "Hesper is very quiet."
            sns_hesper "\"You complete idiot.\""
            $ sns.soft += 1
    hide cg onlayer cgl  # d1 9:17 am: no picture, first-kiss failed 3 draws (SCENES.md senseless v3)
    "And she kisses you. On the mouth, which is the one part of you the Cradle never took away."
    "Your new lips are soft and they're sensitive, and she kisses you like she's been planning it for a lot longer than five days, and you kiss her back like you've been waiting for it for two years, which you have."
    $ vn_set_time(21, 0)
    $ vn_enter(bg="sns_cradle_room", pc="moaning", pc_tag="sns_pc", cast=[], cg="sns_hour_thursday")
    "Tonight she's at the desk, and you're alone up top. At nine the stone chimes, and her voice comes up through the floor, through you."
    sns_hesper_below "\"Both ends tonight.\""
    call sns_hour_part
    show cg sns_both_ends onlayer cgl
    "A tentacle slides up through the gap at the rim, glossy and violet in the lamplight, and slides between your lips, and you open for it."
    "And below, in the dark she's lit for you, two more push into your arse together, and another wraps your cock, and the mouths fasten on your heavy nipples, and the coils round your breasts squeeze."
    vn_sfx "Juppu. Juppu. Nuchu. Chuu."
    sns_you "\"Mmmh♡— mmmmh♡— mmh— MMMH♡—\""
    sns_hesper_below "\"I can hear you. Even with your mouth full. Gods, Rook, I can hear you through the {i}floor{/i}.\""
    "The one in your mouth pulls out just long enough for you to breathe."
    sns_you "\"Don't stop— Hesper, both ends, both— everything— fuck me at both ends, I'm coming, I'm— AHHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Byuru. Byuru. Dopyu."
    "Then it's back between your lips, and the hour goes on, and she plays every key there is."
    call sns_cut(8, 1, "Friday. The sixth morning.")
    jump sns_friday
