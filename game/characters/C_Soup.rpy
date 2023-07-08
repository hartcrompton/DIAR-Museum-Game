#Soup

default beat_Soup = 1

label conv_Soup:
    p "You're talking to me, the Soup!"
    menu:
        "[[Chat a little.]":
            p "We're chatting a little now!"
            pc "We sure are."
            jump conv_Soup
        "[[Use an action.]" if actions > 0 and beat_Soup < 7:
            p "Whoa, sure you want to use an action?"
            jump .use_action
        "Bye":
            p "See ya"
            jump free_roam

label .use_action:
    menu:
        p "Whoa, sure you want to use an action?"
        "Yeah, why not.":
            $ actions = actions - 1
            jump expression "conv_Soup" + "." + "beat" + "%d" % beat_Soup
        "No, not really.":
            p "Understandable."
            jump conv_Soup
    return

label .beat1:
    p "This is the first beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Soup += 1
            $ if d_Soup < 6: d_Soup + 1
            jump conv_Soup
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Soup += 1
            $ if d_Soup > 0: d_Soup - 1
            jump conv_Soup
    return
label .beat2:
    p "This is the second beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Soup += 1
            $ if d_Soup < 6: d_Soup + 1
            jump conv_Soup
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Soup += 1
            $ if d_Soup > 0: d_Soup - 1
            jump conv_Soup
    return
label .beat3:
    p "This is the third beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Soup += 1
            $ if d_Soup < 6: d_Soup + 1
            jump conv_Soup
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Soup += 1
            $ if d_Soup > 0: d_Soup - 1
            jump conv_Soup
    return
label .beat4:
    p "This is the fourth beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Soup += 1
            $ if d_Soup < 6: d_Soup + 1
            jump conv_Soup
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Soup += 1
            $ if d_Soup > 0: d_Soup - 1
            jump conv_Soup
    return
label .beat5:
    p "This is the fifth beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Soup += 1
            $ if d_Soup < 6: d_Soup + 1
            jump conv_Soup
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Soup += 1
            $ if d_Soup > 0: d_Soup - 1
            jump conv_Soup
    return
label .beat6:
    p "This is the sixth beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Soup += 1
            $ if d_Soup < 6: d_Soup + 1
            jump conv_Soup
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Soup += 1
            $ if d_Soup > 0: d_Soup - 1
            jump conv_Soup
    return
label .beat7:
    p "This is the seventh and final beat of my story!"
    menu:
        "You rock.":
            p "That raises my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Soup += 1
            $ if d_Soup < 6: d_Soup + 1
            jump conv_Soup
        "You suck.":
            p "That lowers my disposition."
            p "You have [actions] action(s) left."
            pc "I did an action."
            $ beat_Soup += 1
            $ if d_Soup > 0: d_Soup - 1
            jump conv_Soup
    return