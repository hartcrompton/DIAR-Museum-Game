#NighthawksMLines
default ListenCount = 0

#arnolfini
default b1_ArLines = 0
default b2_ArLines = 0
default b3_ArLines = 0
default b4_ArLines = 0

#davids
default b1_DLines = 0
default b2_DLines = 0
default b3_DLines = 0
default b4_DLines = 0

#gilgamesh
default b1_GiLines = 0
default b2_GiLines = 0
default b3_GiLines = 0
default b4_GiLines = 0

#mona lisa
default b1_MLines = 0
default b2_MLines = 0
default b3_MLines = 0
default b4_MLines = 0

#poster
default b1_PLines = 0
default b2_PLines = 0
default b3_PLines = 0
default b4_PLines = 0

#saint
default b1_StLines = 0
default b2_StLines = 0
default b3_StLines = 0
default b4_StLines = 0

#soup and sunflowers
default b1_SSLines = 0
default b2_SSLines = 0
default b3_SSLines = 0
default b4_SSLines = 0

label conv_Nighthawks:
########sound start hook here (for beat 1-4 specific track) SPECIFICALLY USE MUSIC CHANNEL.
########Using music channel means should not need a STOP MUSIC command.
    scene foyer bg
    play music "music/Nighthawks_ZU_01.wav" fadein 0.4 volume 0.4
    show nighthawks at truecenter
    #p "You're talking to me, the Nighthawks! I'm a side character!"
    menu:
        "[[Chat a little.]":
            p "We're chatting a little now!"
            pc "We sure are."
            jump conv_Nighthawks
        "Bye":
            p "See ya"
            jump FreeRoam

label .beat1:
    "As you make your way to leave, you suddenly catch the sound of whispering. It's the same as last night–though you hadn't been around to catch it that time. "
    n1 angry "…owe me money. You clearly said they were not coming back!"
    n4 surprise "I never said I'd put twenty bucks on it!"
    "Out of the corner of your eye, you spot a painting–the subject: indistinct figures at a moody midnight diner–which was definitely NOT speaking during the day."
    menu:
        "Who are you?":
            pass
        "Another talking painting to keep track of, seriously?":
            pass
    "When you speak up, the painting suddenly falls silent. For a second, it's as if you imagined the sound of furtive muttering emanating from its frame."
    "But then–the second you turn back around to leave–the painting starts whispering again."
    n3 sad "Anyways…"
    #"(Stay silent.)"
    "You stay silent, and try to listen it to the sound. It almost seems like the painting is whispering–to itself?"
    "What clear is they aren't talking to you."
    menu:
        "[[Stay and eavesdrop]":
            pass
        "[[Go home]":
            return
    $ ListenCount += 1
    "After the wild first day you've had, it's not like you're going to be able to fall asleep soon anyways."
    "You strain your ears to listen in to the soft murmuring. As the voices of the Nighthawks become clearer, you realize–"
    n4 neutral "I think we're ALL surprised [they] came back. Anyone hear how [their] first day went? Did they break everything completely?"
    "–they're not talking to you, but they are talking ABOUT you."
    n1 neutral "Hm…I don't know if I'd say broke EVERYTHING, exactly. Here's what I heard went down…"
    call conv_Nighthawks.Arnolfini from _call_conv_Nighthawks_Arnolfini_1
    call conv_Nighthawks.Poster from _call_conv_Nighthawks_Poster_1
    call conv_Nighthawks.MonaLisa from _call_conv_Nighthawks_MonaLisa_1 
    call conv_Nighthawks.Davids from _call_conv_Nighthawks_Davids_1 
    call conv_Nighthawks.Gilgamesh from _call_conv_Nighthawks_Gilgamesh_1
    call conv_Nighthawks.SaintCatherine from _call_conv_Nighthawks_SaintCatherine_1
    call conv_Nighthawks.SoupAndSunflowers from _call_conv_Nighthawks_SoupAndSunflowers_1
    n1 neutral "No, I think that about covers it. Eventful first day, eh?"
    n3 angry "Eh, I wouldn't give them too much credit just yet. It's not like they can solve EVERYONE's problems in four days. It would be folly to try."
    n4 sad "They showed up today, but who's to say they won't no-show tomorrow?"
    n2 sparkle "I don't know. I've got a feeling…"
    "As the Nighthawks fall silent, an uncertain note hanging in the air, you suddenly feel the tiredness set in."
    "What a long first day it's been. "
    "Anything to do with the painting gossiping about you at midnight will have to wait til tomorrow."
    return

label .beat2:
    "Finishing up the day, you realize–there's whispering coming from the Nighthawks. Again. "
    "Honestly, are they always this noisy at the end of day? And how do they not notice anyone listening to them?"
    menu:
        "[[Stay and eavesdrop]":
            pass
        "[[Go home]":
            return
    "With a sigh, you lean in to eavesdrop. (At this rate, you're not going to fall asleep until 2am.)"
    n1 neutral "…does sort of seem like [they] are here to stay."
    n2 happy "I told you!"
    n3 sigh "Does it matter? Charles was here a good long while, and see where that landed us. "
    n4 neutral "Well, let's review, shall we? What did the upstart start up today?"
    call conv_Nighthawks.Arnolfini from _call_conv_Nighthawks_Arnolfini_2
    call conv_Nighthawks.Poster from _call_conv_Nighthawks_Poster_2
    call conv_Nighthawks.MonaLisa from _call_conv_Nighthawks_MonaLisa_2 
    call conv_Nighthawks.Davids from _call_conv_Nighthawks_Davids_2 
    call conv_Nighthawks.Gilgamesh from _call_conv_Nighthawks_Gilgamesh_2
    call conv_Nighthawks.SaintCatherine from _call_conv_Nighthawks_SaintCatherine_2
    call conv_Nighthawks.SoupAndSunflowers from _call_conv_Nighthawks_SoupAndSunflowers_2
    $ ListenCount += 1
    n1 neutral "That's it for today."
    n4 happy "Another eventful day. Honestly, between the crushing job responsibilities and talking paintings, [pc_name] has proven surprisingly resilient.  "
    n2 neutral "I mean…we could assist them with that. If only–"
    n3 angry "No. You know our rule. "
    "At that, the Nighthawks abruptly fall silent. You feel eyes glance over towards where you're skulking–before you can think better of it, you hastily withdraw."
    pc  "Well, that was…odd."
    "As you make your way out of the museum, you can't help but wonder: what's this \"rule\" they're talking about?"
    pc  "{i}Yawn{/i}…"
    "Perhaps a better question for the morning. "
    return

label .beat3:
    "You hear the Nighthawks whisper, in what you are now realizing is a nightly ritual. "
    "The previous night, the Nighthawks mentioned a \"rule\". Something that might have to do with their steadfast refusal to engage with you during the day.  "
    "But what does that mean you should do now? "
    menu:
        "[[Stay and eavesdrop]":
            pass
        "[[Go home]":
            return
    n2 confused "…still think we should try and them to [them], not just ABOUT [them]. "
    n1 neutral "I'm starting to agree."
    n3 neutral "You KNOW why we shouldn't. We're observers. Anything else, and we'll just get….we all know why the rule is in place. Right? "
    n3 questions "Right?"
    "There's a beat of silence, then several sighs of reluctant acceptance."
    n4 sigh "Well, if we're JUST observers…what did we observe?"
    call conv_Nighthawks.Arnolfini from _call_conv_Nighthawks_Arnolfini_3
    call conv_Nighthawks.Poster from _call_conv_Nighthawks_Poster_3
    call conv_Nighthawks.MonaLisa from _call_conv_Nighthawks_MonaLisa_3 
    call conv_Nighthawks.Davids from _call_conv_Nighthawks_Davids_3 
    call conv_Nighthawks.Gilgamesh from _call_conv_Nighthawks_Gilgamesh_3
    call conv_Nighthawks.SaintCatherine from _call_conv_Nighthawks_SaintCatherine_3
    call conv_Nighthawks.SoupAndSunflowers from _call_conv_Nighthawks_SoupAndSunflowers_3
    $ ListenCount += 1
    n1 neutral "That's all she wrote."
    n4 neutral "Well…for good or bad, [pc_name] is certainly making more waves than Charles ever did. He never even knew that we–"
    n3 surprise "Hush. We already went over this. We WANT to be ignored."
    n2 neutral "…Do we?"
    "The Nighthawks fall silent. This time, you're sure there are eyes on you before you move away."
    "You're not sure what to make of it all. There's an odd tension in the air as you leave the museum on the third night. "

label .beat4:
    "Tonight, the Nighthawks' whispering has taken on a different quality. "
    if ListenCount >= 3:
        "You assume it's to do with the grand gala looming on the horizon."
    else:
        "You're not sure if it has to do with the looming gala or the topic they've been dancing around for the past three nights."
    menu:
        "[[Stay and eavesdrop]":
            pass
        "[[Go home]":
            return
    n1 neutral "…more important to talk about soon enough. But first: what's today's roundup?"
    call conv_Nighthawks.Arnolfini from _call_conv_Nighthawks_Arnolfini_4
    call conv_Nighthawks.Poster from _call_conv_Nighthawks_Poster_4
    call conv_Nighthawks.MonaLisa from _call_conv_Nighthawks_MonaLisa_4 
    call conv_Nighthawks.Davids from _call_conv_Nighthawks_Davids_4 
    call conv_Nighthawks.Gilgamesh from _call_conv_Nighthawks_Gilgamesh_4
    call conv_Nighthawks.SaintCatherine from _call_conv_Nighthawks_SaintCatherine_4
    call conv_Nighthawks.SoupAndSunflowers from _call_conv_Nighthawks_SoupAndSunflowers_4
    n1 neutral "That's all that was accomplished today."
    n2 question "Will it be enough for the grand gala, do you think?"
    if ListenCount < 3:
        n3 neutral "I don't know. That's a question for morningl    arks, and we're–"
        n4 neutral "Yes, yes. Pass the coffee, won't you?"
        "The city feels lonelier than usual as you leave that final night. "
        "For a second you wonder: was there something you missed with the Nighthawks? Something that passed in the dead of night, unheard?"
        "For a second you wonder what it could be, but intrusive thoughts of tomorrow quickly overtake you."
        "Tonight doesn't matter in the grand scheme of things. What matters is what morning brings; what stands, proud and terrifying, in the stark light of day."
        "The grand gala awaits."
    elif ListenCount >= 3:
        n3 neutral "I don't know…why don't we ask [pc_name]?"
        menu:
            "Wait, what?":
                n3 laugh "Did you think your eavesdropping went unnoticed, [pc_name]?"
            "You're actually talking to me? ":
                n3 laugh "Yes, we are, [pc_name]. It's rare we do this, so you best enjoy our company!"
        n1 sparkle "Did you know, [pc_name]–our creator once said he wanted nothing more than to paint sunlight on the side of a house. And wouldn't that be wonderful?"
        n4 neutral "But that's not what he painted for us. We're the lonely city; we're the diner open at midnight."
        n4 neutral "We are alone. "
        n2 neutral "Nobody listens to us. Nobody even tries anymore. Except you. "
        pc "I thought YOU had a rule not to talk to people. "
        n3 neutral "We did. Call it…self-preservation."
        n1 neutral "We've moved between many galleries, many museums. For a long time we've been this way, and so we made it our armor. "
        n4 neutral "But you, [pc_name]…it was meaningless gossip, but you stayed each and every night. And for that, we wanted to stop and thank you. "
        n2 neutral "No matter how tomorrow's gala goes, we had fun."
        n2 happy "Thanks for listening."
    return


label .Arnolfini:
    if (beat_Arnolfini == 2) and (b1_ArLines == 0):
        $ b1_ArLines = 1
        n1 "The Arnolfinis are fighting. Again."
        n2 "You'd think they'd eventually run out of things to argue about, but no…honestly, I'm impressed by their mutual devotion to spite."
        n3 "Someone should get them marital counseling. Wait–are they even–"
        n4 "Honestly, who even knows? But enough about that–what else is going on?"
    if (beat_Arnolfini == 3) and (b2_ArLines == 0):
        $ b2_ArLines = 1
        n1 "The Arnolfinis have implored our dear curator to help them sort out their differences. And [they] ARE helping–one of them, at least."
        n2 "Oh, drama! Whose side did the curator take?"
        if if ar_b2_c1 == "a":
            n3 "Missus Arnolfini, she of the many names."
        if ar_b2_c1 == "b":
            n3 "Giovanni, the man himself."
        if ar_b2_c1 == "c":
            n3 "You'll never guess it–the dog! Who apparently can speak!"
        n4 "Well, this ought to be interesting…let's see what comes next for the unhappy couple, eh? Anything else interesting happen today?"
    if (beat_Arnolfini == 4) and (b3_ArLines == 0):
        $ b3_ArLines = 1
        n1 "The Arnolfinis have reached a…well, I don't know if resolution is the right term. An impasse with each other? Let's go with that."
        n2 "Whatever it is, I'm just glad they're not yelling at each other. But how exactly did this even happen?"
        n3 "Our ingenious curator used the oldest trick in the conflict resolution handbook. [they!c] appealed to the Arnolfinis' vanity."
        n4 "Ah, truly…nothing solves issues faster than money. What else?"
    if (beat_Arnolfini == 5) and (b4_ArLines == 0):
        $ b4_ArLines = 1
        if ar_b4_c2 == "a":
            n1 "The curator helped the Arnolfinis define their relationship as husband and wife."
        if ar_b4_c2 == "b":
            n1 "The curator helped the Arnolfinis define their relationship as cousins."
        if ar_b4_c2 == "c":
            n1 "The curator helped the Arnolfinis define their relationship as both spouses AND cousins–which I would rather not think about too much."
        n2 "Whatever their relationship–let's just hope they stay amicable with each other."
        n3 "Wait. If they're not fighting…you realize there is nothing stopping the Arnolfinis from trying to make friends with us again, right?"
        n4 "Oh, dear God. Let's not think about that terrifying possibility. What else is going on?"
    return

label .Davids:
    if (beat_Davids == 2) and (b1_DLines == 0):
        $ b1_DLines = 1
        n1 "Well, I heard the curator spoke with David."
        n2 "That's not all. [they!c] ALSO spoke with David."
        n3 "Oh, and don't forget, [they] ALSO ALSO spoke with–"
        n4 "Yes, yes–you're all very funny. Let's move on."
    if (beat_Davids == 3) and (b2_DLines == 0):
        $ b2_DLines = 1
        n1 "Our dear curator made a CRITICAL mistake–[they] called [b2_DefinitiveDave] the REAL David."
        n2 "Oof. Rookie mistake."
        n3 "Bets on which of the other two Davids is going to 'accidentally' tip over and crush [pc_name] flat?"
        n4 "No betting in the diner! We've been over this…what else?"
    if (beat_Davids == 4) and (b3_DLines == 0):
        $ b3_DLines = 1
        #truth
        if BibleResearched == 1:
            n1 "Stop your sinning, everyone–I hear SOMEONE cracked open the ol' Bible today."
            n2 "Dear old King James. Or was it the flashy New International?"
            n3 "Does it even matter?"
            n4 "More than you might think. But enough about things that should've waited for Sunday–what else?"
        #lie
        if BibleResearched == -1:
            n1 "Stop your sinning, everyone–I hear SOMEONE cracked open the ol' Bible today."
            n2 "Did you? See, I heard different. QUITE different."
            n3 "I heard differently as well. 'Memorized'? My, my, my…"
            n4 "Yes, this should be interesting…what else?"
        #annoyed
        if BibleResearched == 0:
            n1 "Stop your sinning, everyone–I hear SOMEONE cracked open the ol' Bible today."
            n2 "Who cares about that? The Davids got put into separate corners today! Like kindergartners!"
            n3 "Seems…unproductive?"
            n4 "Only time will tell. What else is going on?"
    if (beat_Davids == 5) and (b4_DLines == 0):
        $ b4_DLines = 1
        if BibleResearched == 0:
            n1 "Is there anything else to talk about besides the Davids literally destroying themselves?"
            n2 "I almost feel bad having gossiped about them now. Are we supposed to…hold a funeral or something?"
            n3 "Yes, with all our plentiful shovels and graves. What do you think?"
            n4 "Okay, okay, enough sarcasm. Let's brighten the mood–what else is happening?"
        if BibleResearched == -1:
            n1 "Ding, ding, ding! We have a winner in the contest of the definitive David!"
            n2 "God, finally. Who is it? My bet's on the one with the biggest–"
            if DefinitiveDave == "dm":
                n3 "It's Michelangelo's David!"
            if DefinitiveDave == "dd":
                n3 "It's Donatello's David!"
            if DefinitiveDave == "db":
                n3 "It's Bernini's David!"
            n4 "Hm. Not who I would have chosen, but I respect the decision. What else happened?"
        if BibleResearched == -1:
            n1 "Ding, ding, ding! We have a winner in the contest of the definitive David!"
            n2 "God, finally. Who is it? My bet's on the one with the biggest–"
            n3 "It's all three of them!"
            n4 "Now, isn't that a surprise? I guess the real David is the one we found along the way. What else?” "
    return

label .Gilgamesh:
    if (beat_Gilgamesh == 2) and (b1_GiLines == 0):
        $ b1_GiLines = 1
        n1 "Did you hear [pc_name] talking to Gilgamesh earlier?"
        n2 "Of course we heard. Gil's many things–King of Kings, Master of Beasts, whatever other ridiculous title–but QUIET? Hardly."
        n3 "Do you think they talked about dearly depart–"
        n4 "Hush, now! Don't spoil the fun. What else?"
    if (beat_Gilgamesh == 3) and (b2_GiLines == 0):
        $ b2_GiLines = 1
        n1 "Our new curator has loose lips, it seems. Told Gilgamesh what happened to you-know-who."
        n2 "Oooh, drama! How fun."
        n3 "For us, you mean…and possibly Ea-Nasir. Probably not for old Gil."
        n4 "Oh, CERTAINLY not for him...anything else noteworthy happen today?"
    if (beat_Gilgamesh == 4) and (b3_GiLines == 0):
        $ b3_GiLines = 1
        n1 "Antiquities wing. Inexplicable flooding. Need I say more?"
        n2 "Best if you don't. Gil might start crying again if he hears us talking about him."
        n3 "I doubt that. His conversation with the curator seems to bring him back to his senses...maybe this time he'll finally be able to grieve properly. "
        n4 "Grieving for King Gilgamesh...I shudder to think what that looks like. What else?"
    if (beat_Gilgamesh == 5) and (b4_GiLines == 0):
        $ b4_GiLines = 1
        if SongA > SongB:
            n1 "Did anyone hear a...SONG, coming from Antiquities?"
            n2 "It was Gil, if you can believe it! What do we think he was singing? I don't speak Sumerian, but it certainly sounded...amorous."
            n3 "You know what? Good for him! Wherever he is, I hope Enkidu was listening."
            n4 "I as well. Even if it was...smutty. Anything else?"
        else:
            n1 "Did anyone hear a...SONG, coming from Antiquities?"
            n2 "It was Gil, if you can believe it! What do we think he was singing? I don't speak Sumerian, but it certainly sounded...bloodthirsty."
            n3 "You know what? Good for him! Wherever he is, I hope Enkidu was listening."
            n4 "I as well. An energized Gil is a happy Gil...though I doubt he will be any quieter. Anything else?"
    return

label .MonaLisa:
    if (beat_MonaLisa == 2) and (b1_MLines == 0):
        $ b1_MLines = 1
        n1 "Our curator had the pleasure of speaking with the most famous face ever painted."
        n2 "Ahh, Mona Lisa, so mean, so cold-hearted…I ADORE her."
        n3 "Same. To have the opportunity to talk shit with La Gioconda…truly the highest of honors."
        n4 "Be that as it may…she still can't sit with us. What else?"
    if (beat_MonaLisa == 3) and (b2_MLines == 0):
        $ b2_MLines = 1
        n1 "Did you hear? Mona Lisa wants to return home."
        n2 "Get some new news–Mona's wanted that for centuries. What makes today any different?"
        n3 "Because NOW she finally has someone to listen to her."
        n4 "Well…we must wait and see if [pc_name] truly changes anything. What else?"
    if (beat_MonaLisa == 4) and (b3_MLines == 0):
        $ b3_MLines = 1
        n1 "Mona convinced the curator to restore her eyes in the office."
        n2 "Ah, to be able to see so freely…I mean, we can see Chicago, of course. But imagine having the eyes of a Mona Lisa?"
        n3 "I shudder to think what she'll do with this restored power."
        n4 "Now, now, I'm sure [pc_name] will convince her to use it for good…probably. What else?"
    if (beat_MonaLisa == 5) and (b4_MLines == 0):
        $ b4_MLines = 1
        #alone
        if MonaOutcome == 0:
            n1 "The curator has convinced Mona to remain, it seems."
            n2 "Not an easy feat! How did [they] accomplish that?"
            n3 "Let's just say there's a little bit of bribery going on. A little tit for tat."
            n4 "Who would have thought our dear [pc_name] so ruthless? How far {0}he's{/0}{1}she's{/1}{2}they've{/2} come…what else?"
        #kitsch
        if MonaOutcome == 1:
            n1 "Just in time for the exhibit–the Many Monas, now on display!"
            n2 "Nice pitch. But do we like displaying all the Mona Lisas together, or do we find it…gaudy?"
            n3 "Can't it be both? After all, what's life without a little camp?"
            n4 "Boring–infinitely more boring. And THIS certainly isn't. Now, what else happened today?"
        #heist
        if MonaOutcome == 2:
            n1 "Oh, just a daring heist…a scandal to last generations. Nothing terribly exciting."
            n2 "I'll give our curator this, [they] certainly take[s] RISKS. But will getting rid of the Mona Lisa pay off–or has this museum just lost its crown jewel?"
            n3 "We won't have to wait long. The gala  is just around the corner..."
            n4 "No, now, don't jump to the end so quickly! What else is going on?"

    return

label .Poster:
    if (beat_Poster == 2) and (b1_PLines == 0):
        $ b1_PLines = 1
        n1 "Our dear curator spent a lot of time in the office today. Shirking duties, perhaps?"
        n2 "I can't think of any other reason to be in there. Except that–"
        n3 "Oh, don't mention THEM. 'Motivational art'? Sure. Motivate me to leave the museum."
        n4 "Enough gatekeeping. It's not attractive. What else is happening?"
    if (beat_Poster == 3) and (b2_PLines == 0):
        $ b2_PLines = 1
        n1 "More time in the office for dear [pc_name]. Getting 'motivated'."
        n2 "Honestly. All this fine, priceless art, and [they] choose[s] to spend [their] time chatting with a dollar store poster?"
        n3 "You're going to eat those elitist words of yours. The corgi has a FLAG now."
        n4 "God, the world will never be the same. What else?"
    if (beat_Poster == 4) and (b3_PLines == 0):
        $ b3_PLines = 1
        n1 "I mean, there IS the fact [pc_name] has chosen to–"
        n2 "Ugh, I beg you, don't say it again. It was hard enough to hear the first time that our illustrious, underqualified curator is putting a POSTER out on display."
        n3 "Well, I for one support the idea. Things were getting a little stuffy around here."
        n4 "We'll see. What else?"
    if (beat_Poster == 5) and (b4_PLines == 0):
        $ b4_PLines = 1
        n1 "Well, I can't help but feel quite MOTIVATED for some reason…"
        n2 "You joke, but I think displaying the motivational poster in the museum WORKS. I can't tell if it's the pom-poms, or–"
        n3 "No, no. It's the…SINCERITY of it all. Sometimes it's good to be reminded that not everything needs to be buried under three layers of jaded pretension."
        n4 "Who would have thought–self-growth, right here in the diner! What other surprises do we have in store for today?"
    return

label .SaintCatherine:
    if (beat_SaintCatherine == 2) and (b1_StLines == 0):
        $ b1_StLines = 1
        n1 "Well, the curator met the broken woman."
        n2 "Don't be cruel. Saint Catherine deserves better than being called broken."
        n3 "But is it not accurate? The stained glass needs to be repaired–in more ways than one."
        n4 "Yes–and is that not what a curator is for? Let's see what changes…and in what way. Anything else going on?"
    if (beat_SaintCatherine == 3) and (b2_StLines == 0):
        $ b2_StLines = 1
        n1 "Repairs are underway for St. Catherine. Or, rather–repairs have been planned."
        n2 "Good! But there's multiple ways to repair a crack...which way is our dear curator leaning?"
        n3 "I'm not sure yet. Whatever it is, hopefully it suits the subject in question."
        n4 "And who is the subject, truly? That's the real question…but enough about that for now. What else is going on?"
    if (beat_SaintCatherine == 4) and (b3_StLines == 0):
        $ b3_StLines = 1
        n1 "Identity crisis in Alexandria! Who is the REAL Saint Catherine? More at eleven."
        n2 "You're not funny. But…the question merits examination. Who IS Saint Catherine?"
        n3 "I don't think that's a question we can answer. If there's anyone who COULD, it'd be–"
        n4 "Careful now. We wouldn't want to influence anyone eavesdropping…what else?"
    if (beat_SaintCatherine == 5) and (b4_StLines == 0):
        $ b4_StLines = 1
        if SaintPersonality == 1:
            if st_glass == 0:
                n1 "I hear repairs on Saint Catherine have been completed."
                n2 "Yes, in a rather…unorthodox material."
                n3 "Catherine seems happy enough. Plastic is not what I would have thought of, but perhaps guests might see it as more…approachable?"
                n4 "We won't know for certain until the gala. Anything else?"
            if st_glass == 1:
                n1 "I hear repairs on Saint Catherine have been completed."
                n2 "Yes, in glass, as expected."
                n3 "Catherine seems…conflicted. Will she rise to the mantle she's only recently questioned?"
                n4 "We won't know for certain until the gala. Anything else?"
        if SaintPersonality == 0:
            if st_glass == 0:
                n1 "I hear repairs on Saint Catherine have been completed."
                n2 "Yes, in glass, as expected."
                n3 "Catherine seems happy enough. And the end result is exactly as expected–but is that a GOOD thing?"
                n4 "We won't know for certain until the gala. Anything else?"
            if st_glass == 1:
                n1 "I hear repairs on Saint Catherine have been completed."
                n2 "Yes, in a rather…unorthodox material."
                n3 "Catherine seems…conflicted. And I get it–a holy woman, rendered in plastic? I can't tell if it's utterly daring, or utterly insane."
                n4 "We won't know for certain until the gala. Anything else?"
    return

label .SoupAndSunflowers:
    if (beat_SoupAndSunflowers == 2) and (b1_SSLines == 0):
        $ b1_SSLines = 1
        n1 "Did you hear? Sunflowers tried to trick our dear curator into getting rid of Soup."
        n2 "Wouldn't you? If you were stuck with a stain who also YELLS constantly..."
        n3 "I doubt the 'stain' is happy either. Sunflowers isn't exactly famous for their sparkly conversation."
        n4 "Unlike us, you mean? Don't answer that. What else is happening?"
    if (beat_SoupAndSunflowers == 3) and (b2_SSLines == 0):
        $ b2_SSLines = 1
        if SoloChoice == "Soup":
            n1 "The curator spoke with Soup. Alone."
            n2 "You mean Sunflowers pretended not to hear. How'd it go? Did [they] convince the activist to play nice?"
            n3 "Well, [they] certainly convinced Soup of SOMETHING. All that remains to be seen is if [pc_name] follows through."
            n4 "We'll see…what else?"
        if SoloChoice == "Sunflowers":
            n1 "The curator spoke with Sunflowers. Alone."
            n2 "You mean Soup pretended not to hear. How'd it go? Did [they] convince the wallflower to play nice?"
            n3 "Well, [they] certainly convinced Sunflowers of SOMETHING. All that remains to be seen is if [pc_name] follows through."
            n4 "We'll see…what else?"
    if (beat_SoupAndSunflowers == 4) and (b3_SSLines == 0):
        $ b3_SSLines = 1
        if SoloChoice == "Soup":
            n1 "The curator spoke with Soup. Alone."
            n2 "You mean Sunflowers pretended not to hear. How'd it go? Did [they] convince the activist to play nice?"
            n3 "Well, [they] certainly convinced Soup of SOMETHING. All that remains to be seen is if [pc_name] follows through."
            n4 "We'll see…what else?"
        if SoloChoice == "Sunflowers":
            n1 "The curator spoke with Sunflowers. Alone."
            n2 "You mean Soup pretended not to hear. How'd it go? Did [they] convince the wallflower to play nice?"
            n3 "Well, [they] certainly convinced Sunflowers of SOMETHING. All that remains to be seen is if [pc_name] follows through."
            n4 "We'll see…what else?"
    if (beat_SoupAndSunflowers == 5) and (b4_SSLines == 0):
        $ b4_SSLines = 1
        #merge
        if SSMerged == 1:
            n1 "Soup and Sunflowers are now one and the same!"
            n2 "Multiple characters in the same artwork, coming together to tell a common story…what a novel concept, eh, Nighthawks?"
            n3 "Very funny. But honestly…I'm glad. Soup and Sunflowers have a powerful message together."
            n4 "Agreed. Anything else going on, besides some much-needed self-actualization?"
        elif SoupOutcome == "Remain":
            n1 "Soup remains with Sunflowers. I'm…not sure how to feel about that."
            n2 "Oh, god. Does this mean we have to listen to more of their bickering?"
            n3 "Well…them staying together, even if they're unhappy, is probably better than the alternatives. Maybe?"
            n4 "Only time will tell. What else is happening?"
        #remain
        elif SoupOutcome == "Erase":
            n1 "Soup is gone. The curator has cut through the red tape and administrivia and simply…cleaned off the frame."
            n2 "Ah. THAT'S why it seems so quiet today."
            n3 "I'm going to miss the little miscreant. At least they had something to say."
            n4 "Far be it for us to question the wisdom of our curator…within [their] hearing, that is. What else?"
        elif SoupOutcome == "Detach":
            n1 "Like two children squabbling over a toy, Soup and Sunflowers have been separated."
            n2 "Is that why there's a frame with a stain on display? What an…interesting choice."
            n3 "They each have their own message, I suppose. Perhaps this is for the best."
            n4 "Perhaps…what else?"
        else:
            return
        #erase
        #separate
    return