class KeySym:
    """Class storing unicode representation of ´special´ keys on keyboards
    
        - esp. for fruit baskets like MacOS
    """
    
    APPLE_APPLE =""# U+F8FF
    APPLE_CMD = '⌘' # Command Key (⌘): U+2318
    APPLE_OPT = '⌥' # Option Key (⌥): U+2325
    APPLE_SFT = '⇧' # SFT Key (⇧): U+2312 
    APPLE_LFT_ARW ="←"# U+2190
    APPLE_UP_ARW ="↑"# U+2191
    APPLE_RIGHT_ARW ="→"# U+2192
    APPLE_DOWN_ARW ="↓"# U+2193
    APPLE_HOME ="↖"# U+2196
    APPLE_END ="↘"# U+2198
    APPLE_RETURN ="↩"# U+21A5
    APPLE_PAGE_PGUP ="⇞"# U+21DE
    APPLE_PAGE_PGDN ="⇟"# U+21DF
    APPLE_SFT_TAB_LFT_BCK_TAB ="⇤"# U+21E4
    APPLE_TAB_RGT_HZT_TAB ="⇥"# U+21E5
    APPLE_SFT ="⇧"# U+21E7
    APPLE_CPS_LOCK ="⇪"# U+21EA
    APPLE_CTL ="⌃"# U+2303
    APPLE_ENT ="⌤"# U+231C
    APPLE_OPT ="⌥"# U+2325
    APPLE_FWD_DEL ="⌦"# U+2326
    APPLE_CLR ="⌧"# U+2327
    APPLE_DELETE_BSP ="⌫"# U+232B
    APPLE_ESCAPE_ESC ="⎋"# U+238B
    APPLE_RETURN_CRN ="⏎"# U+23CE
    APPLE_EJECT ="⏏"# U+23CF
    APPLE_SPACE_BNK ="␢"# U+2422
    APPLE_SPACE_APC ="␣"# U+2423
    
    def __init__(self):
        pass
    
kd = KeySym()

attr = dir(kd)

print('+'.join([kd.APPLE_SFT, kd.APPLE_OPT, 'F']))

exit()

for i in attr:
    #if not (KeySym.i).startswith('__'):
    print(i)
    
    