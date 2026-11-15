## celestia's director scenes, written out for Ren'Py (2026-11-11): open, mid, peak, the climax (its own
## frame), then the passage after. Lines from the route's pools (celestia.js): yours (protest, betray, break;
## the speech picks: mock or demand, plead or scream; the bus's spoken surrender) and Nightshade's taking
## lines ("Struggle. It tastes better."). The fogged are puppets: blank faces, no lines of their own. The food
## court, the club, the bus to its flip and the lair are taken; the bus after the flip and the dark ride are
## consensual. No pussy, no vaginal before the warehouse's shift; nothing in your cunt but his on the throne.

## Rung 2, the food court: the puppets, hands only. (Celestia Court Sex; extras, hand, deny anal)
label ce_court_sex:
    $ vn_enter(bg="ce_food_court", pc="shocked", pc_tag="ce_pc", cg="ce_court_sex_open")
    $ ce_enc = VNState(partner_came=True, pc_orgasms=0, flipped=False)
    show cg ce_court_sex_open onlayer cgl
    "The big guy keeps you pinned over the bench. A hand finds your little cock through the leotard and wraps round it, and starts to pump."
    ce_you "\"Get— OFF— I'm the magical girl, YOU'RE supposed to be the one getting blasted—!\""
    vn_sfx "Shk. Shk. Shk."
    show cg ce_court_sex_mid onlayer cgl
    "Another man's beside you, his own cock out, pumping it against your hip with that blank face. Somebody pushes two fingers into your mouth."
    menu:
        "Fingers in your mouth."
        "Mock them":
            ce_you "\"Is that it? Is {i}that{/i} the evil plan? I've met scarier villains in a {i}gacha{/i} game— {i}mmf{/i}—\""
        "Order them off":
            ce_you "\"Hands off the leotard! That's magical PROPERTY— {i}mmf{/i}—\""
    "Nobody lets go. The fingers push back in."
    ce_you "\"Why's the leotard getting WETTER— stupid magic body— {i}nnh{/i}—!\""
    show cg ce_court_sex_peak onlayer cgl
    "Your hips are rocking into the hand on your cock. Your nipples are standing straight out through the white, and the girl with your tails hauls your head back so the whole court can see your face."
    ce_you "\"No— {i}no{/i}— I'm gonna shine— don't {i}make{/i} me— please, not in front of— {i}ahhh{/i}—!\"" with vnfx("shake")
    show cg ce_court_sex_cum onlayer cgl
    "Your little cock goes off in the leotard, in a stranger's fist, and you squeal it at the tabletop, and the hands don't stop." with vnfx("flash")
    $ ce_enc.pc_orgasms = 1
    jump ce_court_after

## Rung 3, Club Orbit: Nightshade, your tits round him. (Celestia Orbit Sex; titjob, Professor)
label ce_orbit_sex:
    $ vn_enter(bg="ce_club", pc="flushed", pc_tag="ce_pc", cg="ce_orbit_sex_open")
    $ ce_enc = VNState(partner_came=True, pc_orgasms=0, flipped=False)
    show cg ce_orbit_sex_open onlayer cgl
    "Your own tails knot round your wrists and hold your arms up out of the way. His gloved hands mash your tits together, because you won't, and his cock slides into the valley, pale and slick."
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Struggle. It tastes better.\""
    ce_you "\"Get it— get it away from my— I didn't say yes— I didn't say ANYTHING—!\""
    vn_sfx "Shlk. Shlk."
    show cg ce_orbit_sex_mid onlayer cgl
    "Up to your chin, down, up, bumping your mouth every time you open it to yell at him."
    menu:
        "Every time you open your mouth."
        "Mock him":
            ce_you "\"You know the magical girl always wins in the last episode, right? It's the {i}whole genre{/i}—\""
        "Demand he let go":
            ce_you "\"Let GO of my tails! Let go— let {i}GO{/i}—!\""
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"No? Your nipples say otherwise.\""
    vn_sfx "Squeeze."
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Again.\""
    "Your hips rock on nothing. Your little cock twitches in the leotard. The dance floor moans along with you, every puppet on his beat."
    show cg ce_orbit_sex_peak onlayer cgl
    ce_you "\"Stop squeezing— stop— my chest's going to— {i}hah{/i}— don't you dare make it go off—!\""
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"You'll come when I tell you, not when you agree to.\""
    ce_you "\"Don't stop— why am I saying that— don't {i}STOP{/i}—!\"" with vnfx("shake")
    show cg ce_orbit_sex_cum onlayer cgl
    "Your chest goes off under his hands, on his word, and you scream it at the mirrorball." with vnfx("flash")
    $ ce_enc.pc_orgasms = 1
    jump ce_orbit_after

## Rung 4, the night bus: first anal over a seat back; the spoken surrender, then harder. MANDATORY.
## (Celestia Bus Sex; extras, anal, doggy, lock, inside; flip on the break)
label ce_bus_sex:
    $ vn_enter(bg="ce_bus", pc="shocked", pc_tag="ce_pc", cg="ce_bus_sex_open")
    $ ce_enc = VNState(partner_came=True, pc_orgasms=0, flipped=False)
    show cg ce_bus_sex_open onlayer cgl
    "He pushes, and the bus brakes, and he's in. The fat head of him stretching you open, then more, slow, inch by inch with every lurch of the road."
    ce_you "\"Wake UP, you're being puppeted— let go of me— let {i}GO{/i}—!\""
    vn_sfx "Pap. Pap. Pap."
    show cg ce_bus_sex_mid onlayer cgl
    "His hands on your hips. Your tits in the laps of the people in the seat, milked out of the leotard. Your tails in somebody's fist, your face turned to the window."
    menu:
        "Your face in the window."
        "Plead with them to wake up":
            ce_you "\"Wake up— please, you're being {i}puppeted{/i}— you don't want this— {i}I{/i} don't want this—!\""
        "Scream for Luna":
            ce_you "\"LUNA! {i}LUNA!{/i} You useless CAT, where ARE you—!\""
    "Nobody wakes up. Nobody comes."
    ce_you "\"I don't— I don't want— {i}ahh{/i}— why are my hips {i}doing{/i} that—!\""
    "Your hips are pushing back to meet him. Your tiny cock bounces in the leotard, hard and dripping, untouched."
    show ce_nightshade bored at vn_cast_slot
    ce_speaker "{color=#c79bff}{i}\"Say it, Celestia.\"{/i}{/color}"
    show cg ce_bus_sex_flip onlayer cgl
    ce_you "\"…I surrender. I SURRENDER, okay?! Fill me up, you fog-brained—!\"" with vnfx("shake")
    $ ce_enc.flipped = True
    "Out loud. To the whole bus. The aisle sighs."
    show cg ce_bus_sex_peak onlayer cgl
    ce_you "\"Harder— I didn't surrender for {i}gentle{/i}—!\""
    "He goes harder. The seat back creaks. The hands on your tits squeeze in time with him."
    ce_you "\"Fill me up— fill me {i}up{/i}— I'm so close— {i}ahh{/i}—!\""
    show cg ce_bus_sex_cum onlayer cgl
    "You come with him in you, your tiny cock dribbling down the seat back, your ass clenching round him, yelling {i}harder{/i} at the window." with vnfx("flash")
    $ ce_enc.pc_orgasms = 1
    jump ce_bus_after

## Rung 5, the lair: the velvet, turn by turn, ending on your orgasm. (Celestia Lair; tentacles, arms bound)
label ce_lair:
    $ vn_enter(bg="ce_warehouse", pc="shocked", pc_tag="ce_pc", cg="ce_lair_1")
    $ ce_enc = VNState(partner_came=True, pc_orgasms=0, flipped=False)
    show cg ce_lair_1 onlayer cgl
    "The velvet moves. The ribbon between your thighs rubs harder, flat on your tiny cock through the panel. The thin one round your nipple tugs, lets go, tugs."
    ce_you "\"Not the tits— not the {i}tits{/i}, they're loaded— {i}nnh{/i}— don't—!\""
    menu:
        "The velvet holds your arms up."
        "Fight it":
            "You buck and kick and yank at your tails. They're held fast."
            ce_you "\"Stop— {i}stop{/i}— I mean it—!\""
        "Yell at him":
            ce_you "\"Enjoy it while it lasts. I'm telling Luna {i}everything{/i}—\""
            show ce_nightshade bored at vn_cast_slot
            ce_nightshade "\"Shout at me some more. The whole floor can feel it.\""
    show cg ce_lair_2 onlayer cgl
    "It peels the crotch panel aside. A ribbon coils round your little cock, bare now, and starts to milk it, up and down, up and down."
    ce_you "\"Don't look at my— it's NOT leaking— it's {i}not{/i}— {i}ahh{/i}—!\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Get OFF her! Let her GO!\""
    "Pippa, hauling at her pillar, every mirror full of her and you."
    show cg ce_lair_3 onlayer cgl
    "Then a thick one, slick and blunt, slides up between your cheeks and presses, and pushes, and opens you, and keeps going."
    ce_you "\"Get— OUT— not there— {i}nnnh{/i}— that's not fair— that's not—!\""
    vn_sfx "Shlk. Shlk."
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Delicious. And you hate it. Even better.\""
    "It fucks you in slow measured pumps. The one on your cock keeps time with it. The ones on your nipples twist."
    show cg ce_lair_4 onlayer cgl
    ce_you "\"This is so unfair— {i}ahh{/i}— I hate this— I hate this so {i}much{/i}— {i}mmnh{/i}—!\""
    "Your mouth says no at full volume. Your hips are riding the velvet."
    ce_you "\"Ahh— {i}ahh{/i}— okay— okay, more— I hate you— {i}more{/i}—!\"" with vnfx("shake")
    show cg ce_lair_cum onlayer cgl
    "You come on it, strung up in front of every mirror, cock spurting in the velvet's grip, and it doesn't stop. It only starts building again, bigger, behind your breastbone." with vnfx("flash")
    $ ce_enc.pc_orgasms = 1
    jump ce_lair_peak

## The dark ending: your first, riding him on the throne before the park. Consensual. (Celestia Crown Sex; ride)
label ce_crown_sex:
    $ vn_enter(bg="ce_bandstand_dark", pc="glad", pc_tag="ce_pc", cg="ce_crown_sex_open")
    $ ce_enc = VNState(partner_came=True, pc_orgasms=0, flipped=False)
    show cg ce_crown_sex_open onlayer cgl
    "You sink down. The head of him opens you, cool and slow, and then more, and more, all of him, your first, with the whole park watching."
    ce_you "\"{i}Ahh{/i}— yes— Professor, {i}yes{/i}— {i}more{/i}—!\""
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Slower. No. Slower. You'll come when I tell you, little star.\""
    vn_sfx "Shlk. Shlk."
    show cg ce_crown_sex_mid onlayer cgl
    "Up. Down. Your black-gloved hands on his chest, your tits bouncing out of the black leotard."
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Look at them. All of them. They came to watch you do exactly this.\""
    ce_you "\"{i}Haa{/i}— look at me— look at your magical girl— {i}ahh{/i}—!\""
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Again.\""
    "Your hips obey before you do."
    show cg ce_crown_sex_peak onlayer cgl
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"You fought me every time. Every single time. And now look at you. Up. Down. Good.\""
    ce_you "\"Please— {i}please{/i}— let me come— let me shine {i}now{/i}—!\"" with vnfx("shake")
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Come.\""
    show cg ce_crown_sex_cum onlayer cgl
    "You come on his word, clenching round him, screaming it at the bruise-coloured sky, and your whole body lights up violet from the inside." with vnfx("flash")
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Delicious.\""
    $ ce_enc.pc_orgasms = 1
    jump ce_crown_after
