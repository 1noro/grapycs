#package languages __init__
#by boot1110001

### IMPORTS ####################################################################
from . import en

### EDITABLE VARIABLES #########################################################
default_lang = en.EN

### FUNCTIONS ##################################################################
def set_lang(str):
    lang = default_lang
    if str == "en.EN":
        print("[INFO] "+lang.set_lang_info+" '"+str+"'")
        lang = en.EN
    else:
        print("[FAIL] '"+str+"' "+lang.set_lang_error)
    return lang
