## THE STORY: chapters 6-7 and the endings (PLAN.md). Friday Maron asks for it herself, and Kanon joins; Saturday the last
## bite and the full bond (Chris's wrist), then the deciding choice (both marked as endings): Let go -> A "Maron", Stay with her -> B
## "Both of Us". mrn.held (his stands) only changes a line or two.

## ---- 6. Friday: Maron asks -------------------------------------------------------------------------------

label mrn_friday:
    $ mrn.fit = "maid"
    $ mrn_grow(6)
    $ vn_enter(bg="mrn_maid_room", pc="serene", pc_tag="mrn_pc", cast=[("mrn_kanon", "headmaid")], cg="mrn_mirror_friday")
    "Kanon comes up at seven with a whole new dress over her arm, because the old one won't do any more. Taking it in and letting it out was Tuesday's job."
    "This one's built from the bodice up."
    "{color=#ff5fb8}Maron stands on the rag rug in her stockings while Kanon laces her in. She's shorter again; she has to tip her head right back to see Kanon's face.{/color}"
    "{color=#ff5fb8}Her breasts are huge now, round and heavy and soft, filling the new bodice to the lace and spilling over it in two pale swells.{/color}"
    "{color=#ff5fb8}Her thighs are thick and soft, her arse round and full behind her, the short skirt flaring out over it. A short, stacked, heavy-curved woman, all softness and weight.{/color}"
    "{color=#ff5fb8}Kanon brushes out her chestnut hair, down to the middle of her back now, and plaits it into one thick braid, and ties it with a red ribbon.{/color}"
    mrn_kanon "\"There. Now you look like a maid of this house.\""
    mrn_maron "\"Thank you, Kanon-neesan♡.\""
    "You've been awake since she was. You've been awake every minute, watching. You're getting used to watching. That frightens you more than anything else has."
    $ vn_set_time(15, 0)
    $ vn_enter(bg="mrn_parlour", pc="nervous", pc_tag="mrn_pc", cast=[("mrn_chris", "heiress")], cg="mrn_parlour_tomorrow")
    "At three, Chris sends Maron out of the room so she can speak to you."
    "It's strange, being let out. Like getting off a long train."
    "Your legs are short and your hips are wide and your breasts are so heavy they pull your shoulders forward, and you stand on the parlour carpet swaying, trying to remember how you used to stand."
    mrn_chris "\"Hello, Mitsuru. It's been a while.\""
    mrn_you "\"What happens tomorrow?\""
    mrn_chris "\"Tomorrow's the seventh night.\""
    mrn_chris "\"I take the last of you, and then I give you some of me: you drink from my wrist, and the bond closes, and you're my blood-sister for as long as I live, which is a very long time.\""
    mrn_you "\"And me? Mitsuru?\""
    mrn_chris "\"That's up to you, darling. When the bond closes, whoever's holding the reins stays awake.\""
    mrn_chris "\"You can let go and sleep, and she'll have all of it, and you'll be warm and happy and gone. Or you can hold on, and stay behind her eyes, and share. Forever. Kanon let go.\""
    mrn_chris "\"Most of them do.\""
    mrn_you "\"Most of them?\""
    mrn_chris "\"I've had a lot of sisters.\""
    $ vn_set_time(23, 0)
    $ vn_enter(bg="mrn_hall", pc="serene", pc_tag="mrn_pc", cast=[], cg="mrn_hall_stairs_night")
    "At eleven, nobody sends for her. Chris hasn't called. And Maron stands at the foot of the tower stairs in her new dress, with her hand on the banister, and wants."
    mrn_maron "\"Let's go to her. Let's ask. She'll like it if we ask.\""
    menu:
        "She's waiting for you. She doesn't have to, but she's waiting."
        "Hold the reins":
            "You take the body back. You can, if you push hard enough; it's still half yours. Your short legs, your heavy chest, your soft hand on the cold banister. Yours."
            "And you stand there in the dark hall for a long time, holding it, and then you climb the stairs. Yourself. One at a time."
            "You don't let yourself think about why."
            $ mrn.held += 1
        "Let her ask":
            "You let go of the reins. She climbs the stairs two at a time, holding up her skirts, her braid bouncing on her back, her heart going fast and light with yours inside it."
            $ mrn.maron += 1
    $ vn_enter(bg="mrn_chris_room", pc="moaning", pc_tag="mrn_pc", cast=[("mrn_chris", "heiress")], cg="mrn_ask_chris")
    "She knocks. She goes in. She kneels on the carpet beside the great bed, and lifts her eyes."
    mrn_maron "\"Onee-sama. May I? Please? I've wanted to all day.\""
    mrn_chris "\"Oh, Maron. You asked. Come here.\""
    show cg mrn_ask_lick onlayer cgl
    "Chris lies back against the pillows and parts her long pale legs, and Maron climbs up between them and puts her mouth to her, eagerly, gratefully, the way she'd drink."
    "Chris is cool everywhere but there. There she's warm, and wet, and tastes of roses and iron."
    vn_sfx "Chu. Chuu. Rero."
    mrn_chris "\"Mm. Good girl. Good— ah. Oh, that's lovely. Who taught you that?\""
    mrn_maron "\"You did, Onee-sama♡. Every night.\""
    "Chris laughs, low, and winds her fingers into the chestnut braid and holds her there."
    "The door opens behind them."
    $ vn_enter(bg="mrn_chris_room", pc="blissful", pc_tag="mrn_pc", cast=[("mrn_chris", "heiress"), ("mrn_kanon", "headmaid")], cg="mrn_ask_paizuri")
    mrn_kanon "\"I heard somebody asking nicely. I thought I'd see what for.\""
    "Kanon sits on the edge of the bed, naked, hard already, and Maron turns from Chris without being told and gets to her knees between Kanon's thighs,"
    "and lifts her own huge soft breasts in both hands, out over the top of the new bodice, and wraps them round Kanon's cock."
    vn_sfx "Nyupu. Nyupu. Nyupu."
    mrn_maron "\"Is this right, Kanon-neesan? Is this how you like it?\""
    mrn_kanon "\"Mm. You know it is. Slower.\""
    "Up and down, slow, the heavy weight of them squeezing, the head of Kanon's cock pushing up out of the cleft on every stroke to brush her chin, and Chris behind her with one hand down the back of her skirt, playing with her, laughing."
    show cg mrn_ask_ride onlayer cgl
    "Then Kanon lifts her by the hips, easily, as if she weighs nothing, and sets her down on her cock facing Chris, and lets her sink."
    vn_sfx "Zupuu."
    mrn_maron "\"AHH♡— so deep— Kanon-neesan♡— it's all the way— ahh♡—\""
    "And Chris kneels up in front of her on the bed and pulls her braid gently aside and bites, the last bite but one, while Kanon bounces her slowly on her cock, and her heavy breasts swing between them, and Maron screams it to the canopy."
    vn_sfx "Tsupu. Pan. Pan. Pan."
    mrn_maron "\"Yes♡— yes♡— both of you— my Onee-samas— fill me, drink me, I'm yours, I'm all yours— AHH♡— AHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Dopyu. Dopyu."
    $ mrn.maron += 1
    "And you, behind her eyes, feel all of it, and for the first time all week you don't push."
    if mrn.held >= 7:
        mrn_you "{i}...Tomorrow. Tomorrow I decide.{/i}"
    else:
        mrn_you "{i}...Tomorrow.{/i}"
    call mrn_cut(10, 1, "Saturday. The seventh morning.")
    jump mrn_saturday

## ---- 7. Saturday: the full bond -----------------------------------------------------------------------------

label mrn_saturday:
    $ mrn.fit = "nude"
    $ mrn_grow(7)
    $ vn_enter(bg="mrn_maid_room", pc="dazed", pc_tag="mrn_pc", cast=[], cg="mrn_mirror_saturday")
    "{color=#ff5fb8}The last morning. You and she wake together and look in the washstand mirror together, and neither of you knows who's doing the looking.{/color}"
    "{color=#ff5fb8}A hundred and forty-five centimetres.{/color}"
    "{color=#ff5fb8}Shorter than most women you ever passed in the street, and built like nobody you ever met.{/color}"
    "{color=#ff5fb8}A short, soft, deep-curved woman with a grown woman's face, wide hips, thick strong thighs, and breasts so big and heavy they rest on her ribs, the biggest her short frame could carry.{/color}"
    "{color=#ff5fb8}Her chestnut hair falls loose to her waist. Her eyes, when the light catches them, have a little red in them now, like a glass of wine.{/color}"
    "On her wrist, if anyone wrote on it, there's nothing at all. The ink washed off in the bath on Thursday."
    mrn_maron "\"We're finished. Look at us.\""
    mrn_you "{i}...We are.{/i}"
    $ vn_set_time(17, 0)
    $ mrn.fit = "maid"
    $ vn_enter(bg="mrn_gate", pc="serene", pc_tag="mrn_pc", cast=[("mrn_kanon", "headmaid")], cg="mrn_gate_snow")
    "At five, the snow comes. Not into the forest, never into the forest, but up on the ridge you can see it, a wall of white moving across the mountain the way it moved a week ago."
    "Somewhere up there is a trail marker, and past it, a hut, and past that, a train back to Yokohama."
    mrn_kanon "\"Seven nights. It always snows on the seventh.\""
    mrn_maron "\"What was your name, Kanon-neesan? Before?\""
    mrn_kanon "\"I don't remember. I let go. I don't miss it.\""
    "She puts a hand on top of Maron's head, a big warm hand, and it's the kindest thing she's ever done."
    $ vn_set_time(23, 55)
    $ mrn.fit = "nightgown"
    $ vn_enter(bg="mrn_chris_room", pc="moaning", pc_tag="mrn_pc", cast=[("mrn_chris", "heiress")], cg="mrn_last_bite")
    "Five to midnight. A week, to the minute."
    "Chris sits on the edge of her bed in a white nightgown with her silver hair over one shoulder, exactly as she sat on yours, and draws her imouto into her lap."
    if mrn.held >= 7:
        mrn_chris "\"You fought me all week, Mitsuru. Harder than anybody. I'll miss it a little, whichever way this goes.\""
    else:
        mrn_chris "\"You've been so good, both of you. Whichever way this goes, I'm proud of you.\""
    "The bite. The last one."
    "Slow and deep and endless, and Chris's hand on her breast, and her own thighs pressing together, and the pull goes all the way down into the very bottom of her, into the last cold lost place, and takes it."
    vn_sfx "Tsupu."
    mrn_maron "\"Ahh♡— Onee-sama— ahh♡— ahh♡—\""
    show cg mrn_wrist onlayer cgl
    "Then Chris lifts her own wrist and touches it to her mouth. Two small marks, already there, waiting."
    mrn_chris "\"Drink, imouto. And whoever's holding the reins when you swallow, that's who I'll be keeping.\""
    menu:
        "Her wrist is at your lips. Maron is waiting. So are you."
        "Let go" (ending=True):
            jump mrn_end_maron
        "Stay with her" (ending=True):
            jump mrn_end_both

## ---- Ending A: Maron ---------------------------------------------------------------------------------------

label mrn_end_maron:
    $ mrn.fit = "nude"
    $ vn_enter(bg="mrn_chris_room", pc="blissful", pc_tag="mrn_pc", cast=[("mrn_chris", "heiress")], cg="mrn_end_maron_drink")
    "You let go."
    "It's easy, in the end. Like falling asleep on a train with the heater under the seat, the window black, somebody you trust beside you."
    "You let go of the reins and the cold and the flat in Yokohama and the boss you hated and the mother you called at New Year and the long, long walk up the mountain alone."
    "The last thing you feel is her mouth closing on Chris's wrist, and a sweetness like chestnuts and roses, and a voice, your voice, her voice, whispering {i}thank you{/i}."
    vn_sfx "Kuku."
    mrn_maron "\"Onee-sama♡.\""
    mrn_chris "\"Hello, Maron. Just you, now?\""
    mrn_maron "\"Just me. He's asleep. He was so tired.\""
    show cg mrn_end_maron_sex onlayer cgl
    "Kanon comes in without knocking, the way she does, and the three of them don't sleep till dawn."
    "Maron rides Kanon with her heavy breasts in Chris's hands and Chris's mouth at her throat, and she's loud, so loud, because there's nobody behind her eyes to be embarrassed any more."
    vn_sfx "Pan. Pan. Pan."
    mrn_maron "\"Kanon-neesan♡— Onee-sama♡— I'm yours— I'm your imouto, I'm your maid, I'm yours forever— ahh♡— AHH♡—!\"" with vnfx("flash", "shake")
    $ vn_set_time(17, 30)
    $ mrn.fit = "maid"
    $ vn_enter(bg="mrn_gate", pc="serene", pc_tag="mrn_pc", cast=[], cg="mrn_end_maron_lamp")
    "A winter later. A whiteout on the ridge, the last Saturday before the lifts open."
    "Someone knocks at the door with the brass bat."
    "Maron opens it with a lamp in her hand, short and soft and stacked in her black dress and white apron, her chestnut braid to her waist."
    "On the step, a young man, twenty-something, frost in his eyebrows, shaking."
    mrn_maron "\"A traveller. In this weather. You'd better come in before you catch your death; the mistress hates a mess.\""
    "Behind her on the stairs, Chris laughs."
    call mrn_route_return("Maron")

## ---- Ending B: Both of Us ----------------------------------------------------------------------------------

label mrn_end_both:
    $ mrn.fit = "nude"
    $ vn_enter(bg="mrn_chris_room", pc="serene", pc_tag="mrn_pc", cast=[("mrn_chris", "heiress")], cg="mrn_end_both_drink")
    "You hold on."
    "Not to the reins. You don't take them. You just don't let go of her: you put your arms round Maron from the inside, round the warm bright room of her, and stay."
    "And she leans back into you, and she drinks."
    vn_sfx "Kuku."
    "Roses and chestnuts and iron, and Chris's blood going down into both of you at once, and the bond closing like a door in a warm house, with both of you on the inside."
    mrn_maron "\"He stayed, Onee-sama.\""
    mrn_you "\"I stayed.\""
    "The same mouth. The same voice, near enough."
    "Chris looks from one to the other in the same pair of eyes and her red eyes go wide, and then she laughs, delighted, like someone given two presents."
    mrn_chris "\"Both of you? Nobody's ever— oh, you clever things. Two sisters in one. Kanon! Kanon, come and see!\""
    show cg mrn_end_both_sex onlayer cgl
    "Kanon comes."
    "And it's different, that night, because there are two of you feeling it: Maron's joy and your astonishment braided together, her love of being loud and your secret, shameful love of being taken, Kanon deep inside you and Chris's mouth at your throat."
    vn_sfx "Pan. Pan. Pan."
    mrn_maron "\"Kanon-neesan♡— it's so good— he can feel it too, he loves it, he {i}loves{/i} it—\""
    mrn_you "\"I do— I do, I love it— ahh♡— don't stop— I mean it, I mean it, don't stop♡—\""
    mrn_maron "\"Onee-sama♡— both of us— we're yours, both of us— AHH♡—!\"" with vnfx("flash", "shake")
    mrn_you "\"AHH♡— AHHH♡—!\"" with vnfx("flash", "shake")
    $ vn_set_time(7, 0)
    $ mrn.fit = "maid"
    $ vn_enter(bg="mrn_maid_room", pc="blissful", pc_tag="mrn_pc", cast=[], cg="mrn_end_both_frost")
    "New Year's morning, months later. There's frost on the inside of the little window over the roses, the only frost the forest ever gets."
    "She breathes on it, and with one finger, in small hard capitals, she writes {i}MITSURU{/i}. And then, in the same hand, in round soft letters beside it, {i}MARON{/i}."
    mrn_maron "\"There. Happy New Year, me.\""
    mrn_you "\"Happy New Year.\""
    "She wipes it away before Kanon sees, and laughs, and goes downstairs to warm the pot for the mistress's tea. Four minutes exactly. A curtsey from the hem. Eyes down."
    "Two of you, doing it together, every morning, for a very long time."
    call mrn_route_return("Both of Us")
