import csv

rumorList = ["A fierce troll dwells at the bottom of the old well on Thief's Close","Ghouls are gathering in the crypts beneath the Pantheon of Lights","A spectral dragon has been seen in the Arbhukkhil Highlands","The Confectioners Guild is looking for mercenaries","The Forge of the Gods lies somewhere beneath the Talon Hills","The king plans to start using orcish mercenaries for tax collection","An order of elemental cultists has attacked Barad Egos and murdered its lord","An order of demonic cultists has re-opened the Lair of the Vampire Princess","An air elemental has escaped from the workshop of Lympe the Sorcerer","Lord Fansa is conspiring to overthrow the king","Lord Anertz is dying of an incurable affliction","Sige the beggar has been missing for days, and was last seen hiding a purse of coins on Barrow Rise","Magic is altered in strange ways within the Restow Woods","The ale at the Cracked Cask has been cursed by a sorceress","There's a magical portal in the highest tower of Simundua Stronghold","Eahrert the sawyer was killed by wolves in the woods outside town","The town was built on top of a battlefield of the Crusade of Angels","The reeve is conspiring to overthrow the king","The spiders of the Tomb of Vile Doom are powerful spellcasters","The town was built on top of an ancient necropolis","The Silver Thorns are held captive within the Temple of Hano the Dire, charmed by a seductive devil","The chancellor of the watch is also the master of the Assassins Guild","The infamous tyrant Alanias is held imprisoned within the Secret Dungeon of Kariashuu, bound by chains of magical ice","The Warrens of Nama is haunted by the ghosts of dragons","Mysterious lights have appeared in the Hammerfall Hills","The chancellor of the guilds is the real power behind the throne","The dragon Susaru has burned the Heli Vale to ash and cinders","The chancellor of the guilds is also the master of the Assassins Guild","Scores of dragons have been gathering in the Spiderweb Vale","A spectral dragon has been seen in the Troll Hills","A spectral dragon has been seen in the Ganua Steppe","A vast cavern filled with glowing crystals and bizarre creatures lies somewhere beneath the Tata Hills","A vampire still lurks in the crypts beneath the ruins of Baluk Keep","A group of pilgrims has stumbled upon the secret temple of an ancient cult in the Talon Hills","Strange shadows are cast in the town square at night","The chancellor of arcana has been seen near the Sepulcher of Demonic Secrets with a company of adventurers","Scores of dragons have been gathering in the Ciethy Forest","The Council of the Blessed Ring are held captive within the Forsaken Tomb of Abaric, frozen in time by an evil lich","There's a magical portal in the highest tower of the Bastion of Zeiram the Lich","The dragon Mardaga has destroyed the dwarven town of Gudrefell","A spectral dragon has been seen in the Cawli Forest","A pack of flesh-eating ghouls lurks in the sewers and tunnels beneath the town","The reeve accepts bribes from adventurers for exceptions and favors","A spectral dragon has been seen in the Dawa Steppe","The master of the Furriers Guild is conspiring to overthrow the king","The trees of the Caerphy Woods have gained sentience and speech","The Crossed Candles has mysteriously moved to the other side of town","Agents of Nezzuhuu the Ghastly have attacked Bryley Keep and murdered its lord","The innkeeper's daughter disappeared when the old inn burned down","Scores of dragons have been gathering in the Yiman Plains","The trees of the Fangwood Forest have gained sentience and speech","Dwarven miners have uncovered a terrible secret in the Bada Downs","An empire of trolls and hags lies somewhere beneath the Khundusharbh Spires","The town magistrate is also the master of the Assassins Guild","The town magistrate accepts bribes from adventurers for exceptions and favors","Scores of dragons have been gathering in the Shadow Downs","A band of orcs is in town looking for mercenary work","An undead knight in the ruins of Horison's Deep still stands watch over the tomb of his queen","A magical portal to the Province of Angels lies somewhere within the Lost Sanctum of Madness","The illustrious archmage Prataleo is held captive within the Dread Cyst of Evil, trapped at the center of a shifting labyrinth","The elves of the Llanfech Woods are savage and eat dwarves","An order of demonic cultists has stolen an ancient artifact from the Lost Cyst of Lord Greywulf","A spectral dragon has been seen in the Nala Spires","An order of elemental cultists has re-opened the Tunnels of Demonic Evil","A lake of quicksilver lies deep within the Aphotic Swamp","The girls at the Foolish Hunter are cheap and friendly if you're drunk","The trees of the Hano Vale have gained sentience and speech","The dragon Bhheshbelshuu has destroyed the city of Neham","Ealbert was murdered by thieves in an alleyway near the Stout Scoundrel","Cece has been searching the area near the Cathedral of Angels","A perpetual storm rages over Hellgate Island","A coven of cruel hags prowls through the Desolation of Amummas","The avatar of a Goddess of Law is held captive within the Cyst of Gouththeusi the Terrible, frozen in time by an evil lich","Inelm the messenger was killed by wolves in the woods outside town","Geatio has been spending strange coins, each marked with an evil rune","The silver dragon of the Dread Pit of Devastation holds a powerful arch-devil imprisoned","The reeve is dying of an incurable affliction","Lady Aelior is actually a cruel werewolf","The boss of the Heralds Guild is a descendant of Sarossu the Ghastly","The boss of the Woodcutters Guild is also the master of the Assassins Guild","Brebealdthr was murdered by thieves in an alleyway near the Knave and Flask","Rica the peddler deals in stolen goods","A fierce troll dwells in the ruined tower on Goldendale Lane","The silver dragon of the Lost Vaults of Ruin may help adventurers for a price","The town magistrate is conspiring to overthrow the king","A perpetual storm rages over the Yurer Veldt","The king plans to start using orcish mercenaries for tax collection","The silver dragon of the Forsaken Barrow of Ruin sometimes helps adventurers","A spectral dragon has been seen in the Desolation of Dagoni","The old cat at the Archer's Flask is actually a polymorphed troll","A spectral dragon has been seen in the Trackless Veldt","The silver dragon of the Shrine of Grim Souls holds a powerful arch-devil imprisoned","The girls at the Pilgrim and Spear are cheap and friendly if you're drunk","Scores of dragons have been gathering in the Ravencrag Mountains","The tomb of the legendary hero Ausan lies deep within the Incan Place Name Jungle","The chancellor of arcana is dying of an incurable affliction","The sausages at the Hunting Harlequin are made with goblin guts","A secret dwarven city lies somewhere beneath the Scarlet Jungle","Lord Bertzia has been murdered and replaced by a Doppelganger","There's a magical portal in the highest tower of the Citadel of the Gargoyle Princess","An undead knight in the ruins of Watun Castle still stands watch over the tomb of his queen","A caravan is expected to arrive this week, carrying elixirs to ward against lycanthropy and vampirism","A star has fallen into the Island of Spiders","Scores of dragons have been gathering in the Plains of Wrath","A war devil with two heads has been summoned into the Nogey Plains","Scores of dragons have been gathering in the Incan Place Name Jungle","The chancellor of the guilds is actually a blood-thirsty vampire","The goblins of the Black Shrine of Malice are as strong as giants","Lady Sane is also the master of the Assassins Guild","A caravan is expected to arrive this week, carrying pyrotechnics from the distant lands of Luanyi","A company of adventurers has unwittingly unleashed an evil curse in the Zari Waste","The town of Latun secretly serves Tharica","The town of Madun secretly serves Bapha the Enchantress","Lady Aenor is the real power behind the throne","A star has fallen into the Island of Torresi","The Sanctuary of the Eternal Lords is a front for the Thieves Guild","The spiders of the Forsaken Sanctum of Malice are powerful spellcasters","The town magistrate is dying of an incurable affliction","The tomb of the legendary hero James Page lies deep within the Scepter March","Someone has been looting tombs at the Sanctuary of Gardens","A star has fallen into the Dragon's Vale","Feiusi saw a swarm of goblins lurking in the woods outside town","The trees of the Glyphwood Forest have gained sentience and speech","An evil curse has befallen the elven town of Bressiriath","An order of demonic cultists has attacked Berica Keep and murdered its lord","Dwarven miners have stumbled into a sealed cyst beneath the Labyrinth of Thorns, and their eyes have become orbs of flame","A colossal ooze-like demon has been summoned into the Tatill Forest","An undead knight in the ruins of Haley Tower guards the artifact weapon Luminous Executioner","Agents of Shiva the Destroyer have stolen an ancient artifact from the lost city of Deheath in the Woeful Moor","Scores of dragons have been gathering in the Desolation of Sumerka","There are still many undiscovered chambers in the Tomb of Omor","The reeve has been murdered by a red-robed assassin","The boss of the Barbers Guild is conspiring to overthrow the king","An order of evil cultists lurks in the sewers and tunnels beneath the town","The ale at the Flying Cock has been cursed by a witch","Doaca the stonemason was once an adventurer but was maimed by a dragon","Sabenn has been seen near the Dungeon of Adamant Terror with a company of adventurers","A perpetual storm rages over the Thunder Mountains","The trees of the Lanfech Forest have gained sentience and speech","Runa was heard boasting that she has discovered a derelict hut filled with swords and arrows","The reeve accepts bribes from adventurers for exceptions and favors","Anyone who takes a stone from the ruined tower on Rampart Street is transformed into a fire elemental","The boss of the Maids Guild has been murdered and replaced by a Doppelganger","The boss of the Woodcutters Guild is dying of an incurable affliction","A dwarven caravan is expected to arrive, carrying exotic weapons from the distant lands of Arish","Frobern the quartermaster lost all his gold gambling at the Lively Serpent","The spiders of the Lair of Poisonous Ages are powerful spellcasters","Magic is altered in strange ways within the Doomblade March","The Sanctuary of the Celestial Lords is a front for the Thieves Guild","A caravan is expected to arrive this week, carrying kobold slaves from the Barrow Downs","Lady Bile is also the master of the Assassins Guild","Scores of dragons have been gathering in the Sanguine Jungle","Heburg lost all her silver gambling at the Warrior and Chain","The old monastery on Blackstone Bluff is haunted by ghosts","Eryn was once a lady but her lands were overrun by savage monsters","A deadly plague is spreading from the dwarven town of Guthrelundr","A swarm of aberrant horrors has gathered in the Lair of Abrax","The innkeeper's daughter disappeared when all the ravens left","The spiders of the Raha Desert are as large as horses","The chancellor of the watch is conspiring to overthrow the king","The spiders of the Raven Downs are as large as horses","The warehouse on Demon's Lane contains a secret cache of magical weapons","A seductive devil prowls through the Gabuzadd Highlands","An order of infernal cultists has re-opened the Undercrypt of the Wyrm Duchess","A horde of demons has been summoned into the Shrine of Malevolent Madness","A deadly plague is spreading from the city of Galeah","Mysterious lights have appeared in the Orcmoor Fen","The town of Llandy has mysteriously disappeared","The dragon Nakila has burned the Ardiff Forest to ash and cinders","A wounded dragon lurks in the ruins of Badun Stronghold","The Barrow of the Wyrm Emperor is haunted by the ghosts of dragons","Something has been delving a network of tunnels beneath the town","The boss of the Innkeepers Guild is also the master of the Assassins Guild","A gang of thieves accidentally set fire to the Pantheon of Angels","The Barrow of Fallen Nightmares is haunted by the ghosts of dragons","Edow was heard boasting that the boss of the Blacksmiths Guild owes her a great debt","The legendary hero Phera is held imprisoned within the Chambers of the Demon Countess, charmed by a seductive devil","Lysev Tower is beseiged by the armies of Abon the Insane","An elven princess is held imprisoned within the Black Crypts of Belpha","The spiders of the Hive of Sidala are powerful spellcasters","The dragon Gama has laid ruin to the Citadel of Olabus","A clan of wererats lurks in the sewers and tunnels beneath the town","A perpetual storm rages over the Berka Veldt","The reeve is the real power behind the throne","A swarm of aberrant horrors has gathered in the Forsaken Caverns of Horror","The reeve has been murdered by a red-robed assassin","A gang of thieves accidentally set fire to the Abbey of Gardens","The ruins of a draconic monastery lies deep within the Tegel Forest","The reeve has been murdered and replaced by a Doppelganger","Exam the linkmaker was once a lord but lost his lands and title in a duel","The Tomb of the Wyrm Queen is haunted by the ghosts of dragons","Lafa the harlot has been seen picking pockets in the market","Scores of dragons have been gathering in the Dark Mire","Dwarven miners have uncovered a terrible secret in the Shadow Downs","A fair princess is held captive within the Dread Tunnels of Horror","The town of Camor has mysteriously disappeared","Gethwe saw a swarm of goblins lurking in the woods outside town","The silver dragon of the Tunnels of Eharer the Treacherous sometimes helps adventurers","An elven princess is held captive within the Black Dungeon of Sorrows","The Company of the Jade Raven are held imprisoned within the Forsaken Halls of Muresu, entombed at the heart of a massive crystal","A giant scorpion-like devil has been summoned into the Witchlight Moor","Magic is altered in strange ways within the Bizaram Spires","A wounded dragon lurks in the ruins of Aykthorp Stronghold","The trees of the Faerie Woods have gained sentience and speech","The stone gargoyles of Barad Gilgildor come to life at night","Ghosts walk the ramparts of Caer Elmingond during the full moon","A horde of demons has been summoned into the Sepulcher of Awesome Chaos","A company of adventurers has uncovered a terrible secret in the Muke Heath","Hundreds of bats were seen eating a goat alive in Feola's field","An order of infernal cultists has re-opened the Caverns of Malign Necromancy","A coven of cruel hags lurks in the ruins of Bloodfen Stronghold","The Sapphire Falcons are held imprisoned within the Labyrinth of Dire Terror, charmed by a seductive devil","A perpetual storm rages over the Tabo Veldt","The legendary hero Artis Daney is held imprisoned within the Vaults of Zeiram the Lich, charmed by a seductive devil","An undead knight in the ruins of Bleakmoor Keep holds a demon imprisoned for eternity","A clan of wererats lurks in the sewers and tunnels beneath the town","Magic is altered in strange ways within the Tatyn Forest","Someone has been looting tombs at the Cathedral of Lights","The chancellor of the treasury has been seen near the Dread Temple of Kas the Betrayer with a company of adventurers","Gery Breyne the poulter has spent all his gold on alchemy and potions","An order of elemental cultists has stolen an ancient artifact from the lost city of Tony in the Blue Mountains","Hearda has been seen picking pockets in the market","Magic is altered in strange ways within the Incan Place Name Jungle","The chancellor of the courts is the real power behind the throne","Dwarven miners have discovered a strange gemstone in the Geani Downs, and they now transform into giant insects at night","Dwarven miners have discovered a lost city in the Brigand Hills","The goblins of the Black Shrine of the Demon Knight are as strong as giants","A silver dragon is held captive within the Chambers of the Wraith Empress, trapped at the center of a shifting labyrinth","Lord Amon has been beguiled by an elven enchantress","The boss of the Tapsters Guild is dying of an incurable affliction","Algald the peddler deals in stolen goods","A band of malicious sidhe lurks in the ruins of Cotte Keep","There are still many undiscovered chambers in the Dark Tomb of Vaculs the Adamant","A caravan is expected to arrive this week, carrying pyrotechnics from the distant lands of Huzhou","Strange shadows are cast in the town square at night","An undead knight in the ruins of Varidotr's Deep sometimes helps worthy adventurers","Aethelm has been seen picking pockets in the market","Something has been delving a network of tunnels beneath the town","An order of elemental cultists has re-opened the Black Hive of Horror","The master of the Bowyers Guild is the real power behind the throne","A demonic cloud of dark lightning has been summoned into the Incan Place Name Jungle","The town of Cracot secretly serves Eusoyn","The chancellor of the guilds is also the master of the Assassins Guild","The town of Badun has mysteriously disappeared","Most of the town guards are wererats","Walda the merchant deals in monstrous pets and slaves","A pack of flesh-eating ghouls lurks in the sewers and tunnels beneath the town","An insane lich prowls through the Sunless Jungle","Agents of Gildo have captured the king and replaced him with a doppelganger","Agents of Nininga have captured the king and replaced him with a doppelganger","The Pantheon of the Cerulean Sky is a front for the Thieves Guild","There's a mad hermit who lives in the Eldritch Downs","Mysterious lights have appeared in the Chata Veldt","The Forsaken Caverns of Doom is haunted by the ghosts of dragons","The Company of the Silver Bear are held captive within the Chambers of Black Horror, trapped behind a magical door with nine seals","A spectral dragon has been seen in the Incan Place Name Jungle","A patrol of soldiers has mysteriously disappeared in the Shrouded Jungle","Leda saw a gang of brigands and murderers lurking in the woods outside town","A wounded dragon lurks in the ruins of Anes Tower","Something has been delving a network of tunnels beneath the town","A lake of quicksilver lies deep within the Titan's Jungle","Lord Gaston has been murdered by a red-robed assassin","The town magistrate is also the master of the Assassins Guild","The old monastery on Tine Hill is haunted by ghosts","The town magistrate is actually a blood-thirsty vampire","An order of infernal cultists has re-opened the Secret Tomb of Souls","Eared hasn't been seen outside her house for a month","A castle frozen in time lies deep within the Spiderweb Vale","Agents of the Wraith Duke have captured the king and replaced him with a doppelganger","Geltheahr the potter hasn't been seen outside his house for a month","An ancient weapon of the gods lies somewhere within the Lost Prison of Bosa the Insane","Mysterious lights have appeared in the Bere Woods","There's a magical portal in the highest tower of Chapool Keep","The barmaid at the Sage and Scroll tried to poison the boss of the Beggars Guild","Anyone who enters the Briarwall Forest at dusk will find their purse filled with strange dice","The statue on North Bank Passage is actually a petrified adventurer","The Lair of Terrible Annihilation is haunted by the ghosts of dragons","The Council of the Azure Scepter are held imprisoned within the Lost Cyst of Horror, trapped at the center of a shifting labyrinth","The chancellor of the treasury has been seen near the Dark Pit of Shiva the Destroyer with a company of adventurers","An air elemental has escaped from the workshop of Eicen the Enchanter","Freda is enslaved by faerie folk","The dragon Ahares has slain a host of adventurers in the Grey Waste","An ancient weapon of the gods lies somewhere within the Hive of Gruesome Doom","A band of slave-trading ogres lurks in the ruins of Iorkvirson's Hold","A perpetual storm rages over the Scorched Earth","Ellyn's Daggers are held captive within the Crypts of Gruesome Necromancy, trapped behind a magical door with nine seals","The smallest cornerstone of Teham Tower is actually the phylactery of an ancient lich","Ered the cook was killed by wolves in the woods outside town","Dwarven miners have discovered an underground river in the Mina Downs","Mysterious lights have appeared in the Crimson Jungle","Bruna was once an adventurer but fell in love and retired","Lady Billie has been seen near the Vaults of Gothmog of Udun with a company of adventurers","Scores of dragons have been gathering in the Zere Desert","The reeve is dying of an incurable affliction","A vast cavern filled with glowing crystals and bizarre creatures lies somewhere beneath the Dungeon of Merkadea the Sinister","Dwarven miners have discovered an underground river in the Brothi Downs","The demonic army of Amas the Treacherous has gathered in the Forsaken Gauntlet of Terror","Errith the merchant deals in monstrous pets and slaves","Thiliam Gere the moneylender mysteriously disappeared last week in the Rotting Swamp","A group of pilgrims has mysteriously disappeared in the Slate Hills","Geatio hasn't been seen outside his house for a month","A vampire still lurks in the crypts beneath the ruins of Castow Castle","The ghosts of a party of adventurers wanders the Llethy Forest","Cuthwy saw a band of orcs and ogres lurking in the woods outside town","The trees of the Risca Vale have gained sentience and speech","The dragon Ninyasu has slain a host of adventurers in the Blue Mountains","Strange shadows are cast in the town square at night","One of the farms outside town was destroyed by a pack of flesh-eating ghouls","Tery the mercer murdered the town magistrate and then disappeared","The old monastery on Raven's Hill is haunted by ghosts","The Abbey of Angels is a front for the Thieves Guild","The old monastery on Cairn Hill is haunted by ghosts","One of the farms outside town was destroyed by a band of orcs and ogres","Here the steward was once an adventurer but stumbled into a fortune and retired","Eantwith the assassin mysteriously disappeared last night on Scarp Alley","Lady Sanne has been seen near the Crypts of Ulfang the Black with a company of adventurers","Lord Rotgo has been murdered by a red-robed assassin","The boss of the Beggars Guild is conspiring to overthrow the king","A volcanic city of fire giants lies somewhere beneath the Graven Hills","One of the farms outside town was destroyed by a band of orcs and ogres","Mysterious lights have appeared in the Negu Heath","Strange shadows are cast in the town square at night","The boss of the Heralds Guild is actually a greedy dragon","The golem in the town square will answer questions, but only in the draconic tongue","The boss of the Maids Guild is also the master of the Assassins Guild","Lord Algais is conspiring to overthrow the king","The spiders of the Lost Gauntlet of Worms are powerful spellcasters","Someone has stolen a ring of keys from the Thieves Guild","Lord Raimo accepts bribes from adventurers for exceptions and favors","Geoffry the spearman was once a lord but his lands were overrun by savage monsters","A band of orcs is in town looking for mercenary work","A swarm of aberrant horrors has gathered in the Dread Prison of Madness","The old monastery on Aefcasuc Hill is haunted by ghosts","A gold dragon is held imprisoned within the Black Tomb of Madness, entombed at the heart of a massive crystal","The golem in the town square will answer questions, but only in riddles","There is a secret entrance to the Catacombs of Treacherous Ages in the cellar beneath the Half-full Chalice on Knight's Lane","The master of the Pikemen Guild is conspiring to overthrow the king","The city of Brafeld has been destroyed by fire","The spiders of the Dark Tunnels of the Lich Baron are powerful spellcasters","A horde of demons has been summoned into the Secret Chambers of Malice","The reeve is the real power behind the throne","The legendary hero Ecin Hylle is held captive within the Dread Tomb of the Vampire Duke, entombed at the heart of a massive crystal","There is a secret entrance to the Black Chambers of the Goblin King in the crypts beneath the Abbey of White Light","Georguy the fishmonger mysteriously disappeared last week in the Sentinel Peaks","The illustrious archmage Istatos is held captive within the Cyst of Merciless Madness, charmed by a seductive devil","A caravan is expected to arrive this week, carrying pyrotechnics from the distant lands of Hanyi","The town of Wrastow has mysteriously disappeared","There are still many undiscovered chambers in the Sepulcher of Emirkol the Chaotic","A noble djinni is held imprisoned within the Dungeon of the Shadow Count, trapped behind a magical door with nine seals","A fell demon lurks in the ruined tower on Fox's Passage","Teowy the beggar was once an adventurer but was maimed by trolls in the Pit of Treacherous Devastation","The dragon Ebash has laid ruin to Ridero Castle","The warehouse on Ravensarch Avenue contains a flying ship","The Council of the Whispering Dagger are held captive within the Caverns of Berwintha the Eldritch, entombed at the heart of a massive crystal","Mysterious lights have appeared in the Muke March","A lake of quicksilver lies deep within the Ghoulfen Mire","Mysterious lights have appeared in the Tuma Veldt","The Dread Chambers of the Shadow Duchess is haunted by the ghosts of dragons","The Undercrypt of the Goblin King is haunted by the ghosts of dragons","The keystone of the gate on Quarry Close is actually the phylactery of an ancient lich","The town of Haritoft has mysteriously disappeared","Bely Hydaye has been seen dealing with orcs and ogres outside the town walls","The renowned warrior Wige is held imprisoned within the Lost Pit of Woe, trapped behind a magical door with nine seals","The chancellor of the treasury is conspiring to overthrow the king","The barmaid at the Pilgrim's Alehouse tried to poison the town magistrate","The girls at the Crossed Hammers are cheap and friendly if you're drunk","The master of the Sheathers Guild is the real power behind the throne","A horde of demons has been summoned into the Delve of Terrible Worms","A star has fallen into the Incan Place Name Jungle","Sabil Keep is beseiged by the armies of Amos the Black","An order of infernal cultists has captured the king and replaced him with a doppelganger","Lady Ailent is actually a cruel werewolf","Scores of dragons have been gathering in the Marsh of Pestilence","The king plans to levy a new tax on adventurers","An empire of trolls and hags lies somewhere beneath the Desolation of Sinidu","An infernal cloud of whirling blades has been summoned into the Incan Place Name Jungle","A vampire still lurks in the crypts beneath the ruins of Minas Gonore","There's a mad hermit who lives in the Bateoda Hills","The dragon Bera has laid ruin to Hastow Stronghold","Ealfled the potter was heard boasting that the reeve owes him a great debt","Agents of the Gargoyle Knight have slain the bronze dragon which guarded the artifact weapon Malevolent Violence","A swarm of gargoyles lurks in the ruins of Aelfith Tower","The king plans to start using orcish mercenaries for tax collection","The reeve has become possessed by a malevolent spirit","Something has been delving a network of tunnels beneath the town","The Sanctuary of Eternal Light is a front for the Thieves Guild","The ale at the Bloody Arrow has been cursed by a hag","The town magistrate has been beguiled by an elven enchantress","Tiny the linkmaker lost all his gold gambling at the Crossed Axes","The goblins of the Forsaken Sepulcher of Doom are as strong as giants","The goblins of the Dark Chambers of Chaos are as strong as giants","The master of the Vintners Guild is also the master of the Assassins Guild","The boss of the Barbers Guild is dying of an incurable affliction","The golem in the town square will answer questions, but always lies","Cece has spent all her gold on alchemy and potions","A spectral dragon has been seen in the Shadowy Swamp","A band of orcs is in town looking for mercenary work","The avatar of a Goddess of Shadows is held captive within the Secret Tomb of Biumuabi the Merciless, bound by chains of magical jade","The Glassblowers Guild is looking for mercenaries","Egold the sawyer saw a gang of brigands and murderers lurking in the woods outside town","A vast cavern filled with glowing crystals and bizarre creatures lies somewhere beneath the Dark Dungeon of Terror","Rither has been missing for days, and was last seen hiding a purse of coins on Orchard Row","The legendary hero Rancent Arrer is held captive within the Cyst of Gothmog of Udun, trapped behind a magical door with nine seals","Lady Elient is also the master of the Assassins Guild","A castle frozen in time lies deep within the Incan Place Name Jungle","Dwarven miners have stumbled through an entombed gate beneath the Faela Bluffs, and they now transform into giant insects at night","Coaford Stronghold is beseiged by the armies of Mastu the Arcane","A water elemental has escaped from the workshop of Aris the Conjurer","Aefrick the steward has been missing for days, and was last seen headed towards the Black Mire","A coven of vampires prowls through the Lina Bluffs","The reeve is a descendant of Sheani the Insane","The infamous tyrant Sarekas is held imprisoned within the Lost Prison of Worms, charmed by a seductive devil","The old monastery on Hynca Bluff is haunted by ghosts","Gyles Byne the quartermaster was once a lord but his lands were destroyed by a dragon","The town magistrate has become possessed by a malevolent spirit","The chancellor of the watch is actually a scheming devil","The boss of the Woodcarvers Guild is also the master of the Assassins Guild","A vampire still lurks in the crypts beneath the ruins of Minas Engos","A deadly plague is spreading from the town of Tostone","Magic is altered in strange ways within the Gatharbar Crags","Aedwed saw a gang of brigands and murderers lurking in the woods outside town","The innkeeper's daughter disappeared when all the ravens left","Bretha was heard boasting that she killed the Horror of Heodoro with a hammer","An iron golem has escaped from the workshop of Prome the Enchanter","A wretched hag dwells in the woods outside town","Lord Gere is conspiring to overthrow the king","A water elemental has escaped from the workshop of Prene the Alchemist","An earth elemental has escaped from the workshop of Ipysia the Sorcerer","Dwarven miners have stumbled upon the secret temple of an ancient cult in the Fang Hills","There is a secret entrance to the Dread Sepulcher of Ulfang the Black somewhere within Kjarve's Deep","The reeve is a descendant of Berica the Elemental","The boss of the Link Boys Guild is actually a scheming devil","A perpetual storm rages over the Manfon Forest","The bridge across the Orcmoor River has been destroyed by brigands","The chancellor of arcana is conspiring to overthrow the king","Someone has been looting tombs at the Monastery of Gardens","Most of the town guards are wererats","An ancient sunken city lies somewhere beneath the Jungle of Thorns","The goblins of the Lost Temple of Sorrows are as strong as giants","The chancellor of the watch is conspiring to overthrow the king","Lord Tiberts is also the master of the Assassins Guild","Agents of Gothmog of Udun have re-opened the Pit of Treacherous Devastation","Strange shadows are cast in the town square at night","Dwarven miners have discovered a strange gemstone in the Crica Downs, and they are slowly becoming incorporeal","Gerey the founder mysteriously disappeared last week in the Incan Place Name Jungle","Anyone who drops a stone into the old well on Bank Road will find their purse filled with thieves' tools","The town of Hildidalr has mysteriously disappeared","A band of orcs is in town looking for mercenary work","The city of Smepool has been decimated by a deadly plague","A pack of flesh-eating ghouls lurks in the sewers and tunnels beneath the town","A malevolent devil is giving eldritch powers to common street waifs","Ghosts walk the ramparts of Ernard Castle during the full moon","One of the farms outside town was destroyed by a gang of brigands and murderers","Walda the girdler mysteriously disappeared last night on Great Sword Court","The girls at the Hunter and Axe are cheap and friendly if you're drunk","The innkeeper's daughter disappeared when all the ravens left","The village of Wabrycg has been decimated by a deadly plague","Wine is enslaved by faerie folk","The brigands of the Najra Waste have stumbled upon an ancient cache of magical weapons and armor","Jaenbert the woodcutter lost all his silver gambling at the Crossed Axes","Aulfker's Hold is beseiged by the trolls of the Khathurak Highlands","The goblins of the Forsaken Labyrinth of the Goblin King are as strong as giants","Ukat's Hold is beseiged by the armies of Ales","An elemental army has gathered in the Sanctum of Arcane Malice","The chancellor of the courts has been seen near the Secret Undercrypt of Madness with a company of adventurers","The town was built on top of an ancient necropolis","A perpetual storm rages over the Dismal Mire","The silver dragon of the Dread Labyrinth of Ulfang the Black will trade magic items from his hoard","A vampire still lurks in the crypts beneath the ruins of Bygate Castle","The dragon Balshalu has destroyed the village of Baymoor","Anyone who kills an alley goblin will be cursed with old age","The reeve has been murdered by a red-robed assassin","A caravan is expected to arrive this week, carrying kobold slaves from the Ashwood Forest","A wounded dragon lurks in the ruins of Barad Mota","The spiders of the Dread Undercrypt of Horror are powerful spellcasters","A star has fallen into the Deadfen Marsh","The cavernous lair of an ancient dragon lies somewhere beneath the Incan Place Name Jungle","A swarm of giant centipedes lurks in the sewers and tunnels beneath the town","Scores of dragons have been gathering in the Dark Moor","The reeve accepts bribes from adventurers for exceptions and favors","An order of elemental cultists has stolen an ancient artifact from the ruins of Caer Akilin","A spectral dragon has been seen in the Ogre Vale","The chancellor of the watch has been seen near the Delve of Indomitable Madness with a company of adventurers","Here the peddler deals in stolen goods","A swarm of gargoyles lurks in the ruins of Ziri's Deep","Jane lost all her gold gambling at the Wicked Scoundrel","A perpetual storm rages over the Island of Guila","The old monastery on Citadel Hill is haunted by ghosts","Ealded was once an adventurer but was maimed by trolls in the Warrens of Sinister Devastation","The Tower of the Goblin King lies deep within the Plains of the Fallen","Scores of dragons have been gathering in the Plains of Wrath","The old monastery on Tempest Hill is haunted by ghosts","An army of giants has gathered in the Sanctum of Dire Evil","The dwarven town of Arkillvik is besieged by murderous ravens","The spiders of the Crystal Desert are as large as horses","The trees of the Mostypr Woods have gained sentience and speech","A pack of aberrant monsters lurks in the ruins of Parre Keep","The dwarven town of Zarazir is besieged by awakened farm animals","The barmaid at the Wizard and Cup tried to poison a company of adventurers","A war golem has escaped from the workshop of Cothe the Alchemist"]

with open('rummors.csv', 'w', newline='') as csvfile:
    rowWriter = csv.writer(csvfile, delimiter='\t')
    for rumor in rumorList:
        print(rumor)
        rowWriter.writerow([rumor.strip()])