#MAIN MENUS
menu00 = ("===========Menu 00 (One Piece)===========\n\n","Play","Create","Edit","List","Exit")

menu02 = ("=============Menu02 Create=============\n\n","Create Character","Create Weapon","Go Back")

menu03 = ("========Menu03 (Edit Menu)========\n\n","Edit Character","Edit Weapon","Go Back")

menu04 = ("============Menu04 (List)=============\n\n","List Characters","List Weapons","List Side","List Range","Go Back")

menu041 = ("======Menu041 (List Characters)======\n\n","List by ID","List by Name","List by Strength","List by Speed","Go Back")

menu042 = ("======Menu042 (List Weapons)======\n\n","List by ID","List by Name","List by Strength","List by Speed","Go Back")

menu032X = ("===Menu 032X (Weapon Feature to Edit) ===\n\n","Name","Plus Strength","Plus speed","Go back")

#CABECERAS

cabecera_armas = 'Available Weapons'.center(40, '=') + '\n' + 'None'.center(40,'-') + '\n' + 'Character weapons:'.center(40, '=')

menuCharactersID = "=" * 19 + "Characters ordered by Id" + "=" * 19 + "\n" + "ID".ljust(10) + "Name".ljust(
                15) + "Strength".ljust(13) + "Speed".ljust(14) + "Experience\n" + "*" * 62

menuCharactersName = "=" * 19 + "Characters ordered by Name" + "=" * 19 + "\n" + "ID".ljust(
                10) + "Name".ljust(15) \
                                 + "Strength".ljust(13) + "Speed".ljust(14) + "Experience\n" + "*" * 62

menuCharactersStrength = "Characters ordered by Strength".center(62,'=') + "\n" + "ID".ljust(
                10) + "Name".ljust(15) \
                                     + "Strength".ljust(13) + "Speed".ljust(14) + "Experience\n" + "*" * 62

menuCharactersSpeed = "Characters ordered by Speed".center(62,'=')+ "\n" + "ID".ljust(
                10) + "Name".ljust(15) \
                                  + "Strength".ljust(13) + "Speed".ljust(14) + "Experience\n" + "*" * 62

cabecera_list_weapons = ('Weapons ordered by ID'.center(60, '=')
                                     + '\n' + 'ID'.ljust(10)
                                     + 'Name'.ljust(13)
                                     + 'Strength'.rjust(10) + 'Speed'.rjust(10)
                                     + 'Two_hand'.rjust(17)) + '\n' + '*' * 60 + '\n'


cabecera2 = "Add Weapons:\n" + "- Enter Id) to add Weapon\n" + "- Enter 0 to finish add weapons\n" + \
                "- Enter  '-Id' to delete weapon in character"

cabecera_side = "Side of the new character:\n" + "1)Marine\n" + "2)Pirates"

cabecera_range_marine = "Range of the new character:\n" + "1) Admirant\n" + "2) Viceadmirant\n3)Lieutenant\n"

cabecera_crew_pirate = "Crew of the new character:\n" + "1) Straw hat\n" + "2) Pirates Buggy\n" + "3) Pirates Rocks\n"

kind_Weapon = "\nKind of weapon\n1)One hand\n2)Two hand"
menu_ad_weapon = 'Add Weapons:\nid Weapon) To add Weapon id\n0)Finish add Weapons\n- Weapon Id ) Delete weapon id'
