# Merged Batch 10 (Files 145-160)
# Assigned Agent: Perplexity



--- Start of Ramayan_batch_145.md ---

# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Ramayana 0.926)
- **Original**: 908 The Ramayana Thus royal sage and Bráhman saint, Spirit, and Virtue free from taint, And all the Gods of heaven who rode On golden cars, their longing showed. Their hearts with doubt and terror rent, They saw the giants' armament, And Ráma clothed in warrior might, Forth standing in the front of fight. Lord of the arm no toil might tire, He stood majestic in his ire, Matchless in form as Rudra465 when His wrath is fierce on Gods or men. While Gods and saints in close array Held converse of the coming fray, The army of the fiends drew near With sight and sound that counselled fear. Long, loud and deep their war-cry pealed, As on they rushed with flag and shield, Each, of his proper valour proud, Urging to fight the demon crowd. His ponderous bow each warrior tried, And swelled his bulk with martial pride. 'Mid shout and roar and trampling feet, And thunder of the drums they beat, Loud and more loud the tumult went Throughout the forest's vast extent, And all the life that moved within The woodland trembled at the din. In eager haste all fled to find Some tranquil spot, nor looked behind. 465 Ziva.
- **Translation**: 

---

### Verse 2 (Ramayana 0.927)
- **Original**: Canto XXIV. The Host In Sight. 909 With every arm of war supplied, On-rushing wildly like the tide Of some deep sea, the giant host Approached where Ráma kept his post. Then he, in battle skilled and tried, Bent his keen eye on every side, And viewed the host of Khara face To face before his dwelling-place. He drew his arrows forth, and reared And strained that bow which foemen feared, And yielded to the vengeful sway Of fierce desire that host to slay. Terrific as the ruinous fire That ends the worlds, he glowed in ire, And his tremendous form dismayed The Gods who roam the forest shade. For in the furious wrath that glowed Within his soul the hero showed LikeZiva when his angry might Stayed Daksha's sacrificial rite.466 Like some great cloud at dawn of day When first the sun upsprings, And o'er the gloomy mass each ray A golden radiance flings: Thus showed the children of the night, Whose mail and chariots threw, With gleam of bows and armlets bright, Flashes of flamy hue. 466 See Additional Notes— D AKSHA 'S SACRIFICE {FNS .
- **Translation**: 

---

### Verse 3 (Ramayana 0.928)
- **Original**: 910 The Ramayana Canto XXV. The Battle. When Khara with the hosts he led Drew near to Ráma's leafy shed, He saw that queller of the foe Stand ready with his ordered bow. He saw, and burning at the view His clanging bow he raised and drew, And bade his driver urge apace His car to meet him face to face. Obedient to his master's hest His eager steeds the driver pressed On to the spot where, none to aid, The strong-armed chief his weapon swayed. Soon as the children of the night Saw Khara rushing to the fight,[258] His lords with loud unearthly cry Followed their chief and gathered nigh. As in his car the leader rode With all his lords around, he showed Like the red planet fiery Mars Surrounded by the lesser stars. Then with a horrid yell that rent The air, the giant chieftain sent A thousand darts in rapid shower On Ráma matchless in his power. The rovers of the night, impelled By fiery rage which naught withheld, Upon the unconquered prince, who strained His fearful bow, their arrows rained. With sword and club, with mace and pike, With spear and axe to pierce and strike, Those furious fiends on every side The unconquerable hero plied.
- **Translation**: 

---

### Verse 4 (Ramayana 0.929)
- **Original**: Canto XXV. The Battle. 911 The giant legions huge and strong, Like clouds the tempest drives along, Rushed upon Ráma with the speed Of whirling car, and mounted steed, And hill-like elephant, to slay The matchless prince in battle fray. Then upon Ráma thick and fast The rain of mortal steel they cast, As labouring clouds their torrents shed Upon the mountain-monarch's467 head. As near and nearer round him drew The warriors of the giant crew, He showed likeZiva girt by all His spirits when night's shadows fall. As the great deep receives each rill And river rushing from the hill, He bore that flood of darts, and broke With well-aimed shaft each murderous stroke. By stress of arrowy storm assailed, And wounded sore, he never failed, Like some high mountain which defies The red bolts flashing from the skies. With ruddy streams each limb was dyed From gaping wounds in breast and side, Showing the hero like the sun 'Mid crimson clouds ere day is done. Then, at that sight of terror, faint Grew God, Gandharva, sage, and saint, Trembling to see the prince oppose His single might to myriad foes. But waxing wroth, with force unspent, He strained his bow to utmost bent, 467 Himálaya.
- **Translation**: 

---

### Verse 5 (Ramayana 0.930)
- **Original**: 912 The Ramayana And forth his arrows keen and true In hundreds, yea in thousands flew,— Shafts none could ward, and none endure: Death's fatal noose was scarce so sure. As 'twere in playful ease he shot His gilded shafts, and rested not. With swiftest flight and truest aim Upon the giant hosts they came. Each smote, each stayed a foeman's breath As fatal as the coil of Death. Each arrow through a giant tore A passage, and besmeared with gore, Pursued its onward way and through The air with flamy brilliance flew. Unnumbered were the arrows sent From the great bow which Ráma bent, And every shaft with iron head The lifeblood of a giant shed. Their pennoned bows were cleft, nor mail Nor shield of hide could aught avail. For Ráma's myriad arrows tore Through arms, and bracelets which they wore, And severed mighty warriors' thighs Like trunks of elephants in size, And cut resistless passage sheer Through gold-decked horse and charioteer, Slew elephant and rider, slew The horseman and the charger too, And infantry unnumbered sent To dwell 'neath Yáma's government. Then rose on high a fearful yell Of rovers of the night, who fell Beneath that iron torrent, sore Wounded by shafts that rent and tore.
- **Translation**: 

---

### Verse 6 (Ramayana 0.931)
- **Original**: Canto XXV. The Battle. 913 So mangled by the ceaseless storm Of shafts of every kind and form, Such joy they found, as forests feel When scorched by flame, from Ráma's steel. The mightiest still the fight maintained, And furious upon Ráma rained Dart, arrow, spear, with wild attacks Of mace, and club, and battle-axe. But the great chief, unconquered yet, Their weapons with his arrows met, Which severed many a giant's head, And all the plain with corpses spread. With sundered bow and shattered shield Headless they sank upon the field, As the tall trees, that felt the blast Of Garu 's wing, to earth were cast. The giants left unslaughtered there Where filled with terror and despair, And to their leader Khara fled Faint, wounded, and discomfited. These fiery DúshaG strove to cheer, And poised his bow to calm their fear; Then fierce as He who rules the dead, When wroth, on angered Ráma sped. By DúshaG cheered, the demons cast Their dread aside and rallied fast With Sáls, rocks, palm-trees in their hands With nooses, maces, pikes, and brands, Again upon the godlike man The mighty fiends infuriate ran, These casting rocks like hail, and these A whelming shower of leafy trees. Wild, wondrous fight, the eye to scare, And raise on end each shuddering hair, [259]
- **Translation**: 

---

### Verse 7 (Ramayana 0.932)
- **Original**: 914 The Ramayana As with the fiends who loved to rove By night heroic Ráma strove! The giants in their fury plied Ráma with darts on every side. Then, by the gathering demons pressed From north and south and east and west, By showers of deadly darts assailed From every quarter fiercely hailed, Girt by the foes who swarmed around, He raised a mighty shout whose sound Struck terror. On the giant crew His great Gandharva468 arrow flew. A thousand mortal shafts were rained From the orbed bow the hero strained, Till east and west and south and north Were filled with arrows volleyed forth. They heard the fearful shout: they saw His mighty hand the bowstring draw, Yet could no wounded giant's eye See the swift storm of arrows fly. Still firm the warrior stood and cast His deadly missiles thick and fast. Dark grew the air with arrowy hail Which hid the sun as with a veil. Fiends wounded, falling, fallen, slain, All in a moment, spread the plain, And thousands scarce alive were left Mangled, and gashed, and torn, and cleft. Dire was the sight, the plain o'erspread With trophies of the mangled dead. There lay, by Ráma's missiles rent, Full many a priceless ornament, 468 One of the mysterious weapons given to Ráma.
- **Translation**: 

---

### Verse 8 (Ramayana 0.933)
- **Original**: Canto XXVI. Dúshan's Death. 915 With severed limb and broken gem, Hauberk and helm and diadem. There lay the shattered car, the steed, The elephant of noblest breed, The splintered spear, the shivered mace, Chouris and screens to shade the face. The giants saw with bitterest pain Their warriors weltering on the plain, Nor dared again his might oppose Who scourged the cities of his foes. Canto XXVI. Dúshan's Death. When Dúsha G saw his giant band Slaughtered by Ráma's conquering hand, He called five thousand fiends, and gave His orders. Bravest of the brave, Invincible, of furious might, Ne'er had they turned their backs in flight. They, as their leader bade them seize Spears, swords, and clubs, and rocks, and trees, Poured on the dauntless prince again A ceaseless shower of deadly rain. The virtuous Ráma, undismayed, Their missiles with his arrows stayed, And weakened, ere it fell, the shock Of that dire hail of tree and rock, And like a bull with eyelids closed, The pelting of the storm opposed.
- **Translation**: 

---

### Verse 9 (Ramayana 0.934)
- **Original**: 916 The Ramayana Then blazed his ire: he longed to smite To earth the rovers of the night. The wrath that o'er his spirit came Clothed him with splendour as of flame, While showers of mortal darts he poured Fierce on the giants and their lord. DúshaG, the foeman's dusky dread, By frenzied rage inspirited, On Raghu's son his missiles cast Like Indra's bolts which rend and blast. But Ráma with a trenchant dart Cleft DúshaG's ponderous bow apart. And then the gold-decked steeds who drew The chariot, with four shafts he slew. One crescent dart he aimed which shred Clean from his neck the driver's head; Three more with deadly skill addressed Stood quivering in the giant's breast. Hurled from his car, steeds, driver slain, The bow he trusted cleft in twain, He seized his mace, strong, heavy, dread, High as a mountain's towering head. With plates of gold adorned and bound, Embattled Gods it crushed and ground. Its iron spikes yet bore the stains Of mangled foemen's blood and brains. Its heavy mass of jagged steel Was like a thunderbolt to feel. It shattered, as on foes it fell, The city where the senses dwell.469 Fierce DúshaG seized that ponderous mace Like monstrous form of serpent race, 469 A periphrasis for the body.
- **Translation**: 

---

### Verse 10 (Ramayana 0.935)
- **Original**: Canto XXVI. Dúshan's Death. 917 And all his savage soul aglow With fury, rushed upon the foe. But Raghu's son took steady aim, And as the rushing giant came, Shore with two shafts the arms whereon The demon's glittering bracelets shone. His arm at each huge shoulder lopped, The mighty body reeled and dropped, And the great mace to earth was thrown Like Indra's staff when storms have blown. As some vast elephant who lies Shorn of his tusks, and bleeding dies, So, when his arms were rent away, Low on the ground the giant lay. The spirits saw the monster die, And loudly rang their joyful cry, “Honour to Ráma! nobly done! Well hast thou fought, Kakutstha's son!” [260] But the great three, the host who led, Enraged to see their chieftain dead, As though Death's toils were round them cast, Rushed upon Ráma fierce and fast, Mahákapála seized, to strike His foeman down, a ponderous pike: Sthúláksha charged with spear to fling, Pramáthi with his axe to swing. When Ráma saw, with keen darts he Received the onset of the three, As calm as though he hailed a guest In each, who came for shade and rest. Mahákapála's monstrous head Fell with the trenchant dart he sped. His good right hand in battle skilled Sthúláksha's eyes with arrows filled,
- **Translation**: 

---

### Verse 11 (Ramayana 0.936)
- **Original**: 918 The Ramayana And trusting still his ready bow He laid the fierce Pramáthi low, Who sank as some tall tree falls down With bough and branch and leafy crown. Then with five thousand shafts he slew The rest of DúshaG's giant crew: Five thousand demons, torn and rent, To Yáma's gloomy realm he sent. When Khara knew the fate of all The giant band and DúshaG's fall, He called the mighty chiefs who led His army, and in fury said: “Now Dúsha G and his armèd train Lie prostrate on the battle plain. Lead forth an army mightier still, Ráma this wretched man, to kill. Fight ye with darts of every shape, Nor let him from your wrath escape.” Thus spoke the fiend, by rage impelled, And straight his course toward Ráma held. With Zyenagámí and the rest Of his twelve chiefs he onward pressed, And every giant as he went A storm of well-wrought arrows sent. Then with his pointed shafts that came With gold and diamond bright as flame, Dead to the earth the hero threw The remnant of the demon crew. Those shafts with feathers bright as gold, Like flames which wreaths of smoke enfold, Smote down the fiends like tall trees rent By red bolts from the firmament.
- **Translation**: 

---

### Verse 12 (Ramayana 0.937)
- **Original**: Canto XXVI. Dúshan's Death. 919 A hundred shafts he pointed well: By their keen barbs a hundred fell: A thousand,— and a thousand more In battle's front lay drenched in gore. Of all defence and guard bereft, With sundered bows and harness cleft. Their bodies red with bloody stain Fell the night-rovers on the plain, Which, covered with the loosened hair Of bleeding giants prostrate there, Like some great altar showed, arrayed For holy rites with grass o'erlaid. The darksome wood, each glade and dell Where the wild demons fought and fell Was like an awful hell whose floor Is thick with mire and flesh and gore. Thus twice seven thousand fiends, a band With impious heart and bloody hand, By Raghu's son were overthrown, A man, on foot, and all alone. Of all who met on that fierce day, Khara, great chief, survived the fray, The monster of the triple head,470 And Raghu's son, the foeman's dread. The other demon warriors, all Skilful and brave and strong and tall, In front of battle, side by side, Struck down by LakshmaG's brother died. When Khara saw the host he led Triumphant forth to fight Stretched on the earth, all smitten dead, By Ráma's nobler might, 470 Tri[irás.
- **Translation**: 

---

### Verse 13 (Ramayana 0.938)
- **Original**: 920 The Ramayana Upon his foe he fiercely glared, And drove against him fast, Like Indra when his arm is bared His thundering bolt to cast. Canto XXVII. The Death Of Trisirás. But Tri[irás,471 a chieftain dread, Marked Khara as he onward sped. And met his car and cried, to stay The giant from the purposed fray: “Mine be the charge: let me attack, And turn thee from the contest back. Let me go forth, and thou shalt see The strong-armed Ráma slain by me. True are the words I speak, my lord: I swear it as I touch my sword: That I this Ráma's blood will spill, Whom every giant's hand should kill. This Ráma will I slay, or he In battle fray shall conquer me. Restrain thy spirit: check thy car, And view the combat from afar. Thou, joying o'er the prostrate foe, To Janasthán again shalt go, Or, if I fall in battle's chance, Against my conqueror advance.” 471 The Three-headed.
- **Translation**: 

---

### Verse 14 (Ramayana 0.939)
- **Original**: Canto XXVII. The Death Of Trisirás. 921 Thus Tri[irás for death who yearned: And Khara from the conflict turned, “Go forth to battle,” Khara cried; And toward his foe the giant hied. Borne on a car of glittering hue Which harnessed coursers fleetly drew, Like some huge hill with triple peak He onward rushed the prince to seek. [261] Still, like a big cloud, sending out His arrowy rain with many a shout Like the deep sullen roars that come Discordant from a moistened drum. But Raghu's son, whose watchful eye Beheld the demon rushing nigh, From the great bow he raised and bent A shower of shafts to meet him sent. Wild grew the fight and wilder yet As fiend and man in combat met, As when in some dark wood's retreat An elephant and a lion meet. The giant bent his bow, and true To Ráma's brow three arrows flew. Then, raging as he felt the stroke, These words in anger Ráma spoke: “Heroic chief! is such the power Of fiends who rove at midnight hour? Soft as the touch of flowers I feel The gentle blows thine arrows deal. Receive in turn my shafts, and know What arrows fly from Ráma's bow.” Thus as he spoke his wrath grew hot, And twice seven deadly shafts he shot, Which, dire as serpent's deadly fang,
- **Translation**: 

---

### Verse 15 (Ramayana 0.940)
- **Original**: 922 The Ramayana Straight to the giant's bosom sprang. Four arrows more,— each shaped to deal A mortal wound with barbèd steel,— The glorious hero shot, and slew The four good steeds the car that drew. Eight other shafts flew straight and fleet, And hurled the driver from his seat, And in the dust the banner laid That proudly o'er the chariot played. Then as the fiend prepared to bound Forth from his useless car to ground, The hero smote him to the heart, And numbed his arm with deadly smart. Again the chieftain, peerless-souled, Sent forth three rapid darts, and rolled With each keen arrow, deftly sped, Low in the dust a monstrous head. Then yielding to each deadly stroke, Forth spouting streams of blood and smoke, The headless trunk bedrenched with gore Fell to the ground and moved no more. The fiends who yet were left with life, Routed and crushed in battle strife, To Khara's side, like trembling deer Scared by the hunter, fled in fear. King Khara saw with furious eye His scattered giants turn and fly; Then rallying his broken train At Raghu's son he drove amain, Like Ráhu472 when his deadly might Comes rushing on the Lord of Night. 472 The demon who causes eclipses.
- **Translation**: 

---

### Verse 16 (Ramayana 0.941)
- **Original**: Canto XXVIII. Khara Dismounted. 923 Canto XXVIII. Khara Dismounted. But when he turned his eye where bled Both Tri[irás and DúshaG dead, Fear o'er the giant's spirit came Of Ráma's might which naught could tame. He saw his savage legions, those Whose force no creature dared oppose,— He saw the leader of his train By Ráma's single prowess slain. With burning grief he marked the few Still left him of his giant crew. As Namuchi473 on Indra, so Rushed the dread demon on his foe. His mighty bow the monster strained, And angrily on Ráma rained His mortal arrows in a flood, Like serpent fangs athirst for blood. Skilled in the bowman's warlike art, He plied the string and poised the dart. Here, on his car, and there, he rode, And passages of battle showed, While all the skyey regions grew Dark with his arrows as they flew. Then Ráma seized his ponderous bow, And straight the heaven was all aglow With shafts whose stroke no life might bear That filled with flash and flame the air, 473 “This Asura was a friend of Indra, and taking advantage of his friend's confidence, he drank up Indra's strength along with a draught of wine and Soma. Indra then told the A[vins and Sarasvatí that Namuchi had drunk up his strength. The A[vins in consequence gave Indra a thunderbolt in the form of a foam, with which he smote off the head of Namuchi.” G ARRETT 'S{FNS Classical Dictionary of India. See also Book I. p. 39.
- **Translation**: 

---

### Verse 17 (Ramayana 0.942)
- **Original**: 924 The Ramayana Thick as the blinding torrents sent Down from Parjanya's474 firmament. In space itself no space remained, But all was filled with arrows rained Incessantly from each great bow Wielded by Ráma and his foe. As thus in furious combat, wrought To mortal hate, the warriors fought, The sun himself grew faint and pale, Obscured behind that arrowy veil. As when beneath the driver's steel An elephant is forced to kneel, So from the hard and pointed head Of many an arrow Ráma bled. High on his car the giant rose Prepared in deadly strife to close,[262] And all the spirits saw him stand Like Yáma with his noose in hand. For Khara deemed in senseless pride That he, beneath whose hand had died The giant legions, failed at length Slow sinking with exhausted strength. But Ráma, like a lion, when A trembling deer comes nigh his den, Feared not the demon mad with hate,— Of lion might and lion gait. Then in his lofty car that glowed With sunlike brilliance Khara rode At Ráma: madly on he came Like a poor moth that seeks the flame. His archer skill the fiend displayed, And at the place where Ráma laid 474 Indra.
- **Translation**: 

---

### Verse 18 (Ramayana 0.943)
- **Original**: Canto XXVIII. Khara Dismounted. 925 His hand, an arrow cleft in two The mighty bow the hero drew. Seven arrows by the giant sent, Bright as the bolts of Indra, rent Their way through mail and harness joints, And pierced him with their iron points. On Ráma, hero unsurpassed, A thousand shafts smote thick and fast, While as each missile struck, rang out The giant's awful battle-shout. His knotted arrows pierced and tore The sunbright mail the hero wore, Till, band and buckle rent away, Glittering on the ground it lay. Then pierced in shoulder, breast, and side, Till every limb with blood was dyed, The chieftain in majestic ire Shone glorious as the smokeless fire. Then loud and long the war-cry rose Of Ráma, terror of his foes, As, on the giant's death intent, A ponderous bow he strung and bent,— Lord VishGu's own, of wondrous size,— Agastya gave the heavenly prize. Then rushing on the demon foe, He raised on high that mighty bow, And with his well-wrought shafts, whereon Bright gold between the feathers shone, He struck the pennon fluttering o'er The chariot, and it waved no more. That glorious flag whose every fold Was rich with blazonry and gold, Fell as the sun himself by all The Gods' decree might earthward fall.
- **Translation**: 

---

### Verse 19 (Ramayana 0.944)
- **Original**: 926 The Ramayana From wrathful Khara's hand, whose art Well knew each vulnerable part, Four keenly-piercing arrows flew, And blood in Ráma's bosom drew, With every limb distained with gore From deadly shafts which rent and tore, From Khara's clanging bowstring shots, The prince's wrath waxed wondrous hot. His hand upon his bow that best Of mighty archers firmly pressed, And from the well-drawn bowstring, true Each to its mark, six arrows flew. One quivered in the giant's head, With two his brawny shoulders bled; Three, with the crescent heads they bore, Deep in his breast a passage tore. Thirteen, to which the stone had lent The keenest point, were swiftly sent On the fierce giant, every one Destructive, gleaming like the sun. With four the dappled steeds he slew; One cleft the chariot yoke in two, One, in the heat of battle sped, Smote from the neck the driver's head. The poles were rent apart by three; Two broke the splintered axle-tree. Then from the hand of Ráma, while Across his lips there came a smile, The twelfth, like thunderbolt impelled, Cut the great hand and bow it held. Then, scarce by Indra's self surpassed, He pierced the giant with the last. The bow he trusted cleft in twain, His driver and his horses slain,
- **Translation**: 

---

### Verse 20 (Ramayana 0.945)
- **Original**: Canto XXIX. Khara's Defeat. 927 Down sprang the giant, mace in hand, On foot against the foe to stand. The Gods and saints in bright array Close gathered in the skies, The prince's might in battle-fray Beheld with joyful eyes. Uprising from their golden seats, Their hands in honour raised, They looked on Ráma's noble feats, And blessed him as they praised. Canto XXIX. Khara's Defeat. When Ráma saw the giant nigh, On foot, alone, with mace reared high, In mild reproof at first he spoke, Then forth his threatening anger broke: “Thou with the host 'twas thine to lead, With elephant and car and steed, Hast wrought an act of sin and shame, An act which all who live must blame. Know that the wretch whose evil mind Joys in the grief of human kind, Though the three worlds confess him lord, Must perish dreaded and abhorred. Night-rover, when a villain's deeds Distress the world he little heeds, Each hand is armed his life to take, And crush him like a deadly snake. The end is near when men begin Through greed or lust a life of sin,
- **Translation**: 

---



--- End of Ramayan_batch_145.md ---


--- Start of Ramayan_batch_146.md ---

# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Ramayana 0.946)
- **Original**: 928 The Ramayana E'en as a Bráhman's dame, unwise, Eats of the fallen hail475 and dies.[263] Thy hand has slain the pure and good, The hermit saints of DaG ak wood, Of holy life, the heirs of bliss; And thou shalt reap the fruit of this. Not long shall they whose cruel breasts Joy in the sin the world detests Retain their guilty power and pride, But fade like trees whose roots are dried. Yes, as the seasons come and go, Each tree its kindly fruit must show, And sinners reap in fitting time The harvest of each earlier crime. As those must surely die who eat Unwittingly of poisoned meat, They too whose lives in sin are spent Receive ere long the punishment. And know, thou rover of the night, That I, a king, am sent to smite The wicked down, who court the hate Of men whose laws they violate. This day my vengeful hand shall send Shafts bright with gold to tear and rend, And pass with fury through thy breast As serpents pierce an emmet's nest. Thou with thy host this day shalt be Among the dead below, and see The saints beneath thy hand who bled, Whose flesh thy cruel maw has fed. They, glorious on their seats of gold, Their slayer shall in hell behold. 475 Popularly supposed to cause death.
- **Translation**: 

---

### Verse 2 (Ramayana 0.947)
- **Original**: Canto XXIX. Khara's Defeat. 929 Fight with all strength thou callest thine, Mean scion of ignoble line, Still, like the palm-tree's fruit, this day My shafts thy head in dust shall lay.” Such were the words that Ráma said: Then Khara's eyes with wrath glowed red, Who, maddened by the rage that burned Within him, with a smile returned: “Thou Da[aratha's son, hast slain The meaner giants of my train: And canst thou idly vaunt thy might And claim the praise not thine by right? Not thus in self-laudation rave The truly great, the nobly brave: No empty boasts like thine disgrace The foremost of the human race. The mean of soul, unknown to fame, Who taint their warrior race with shame, Thus speak in senseless pride as thou, O Raghu's son, hast boasted now. What hero, when the war-cry rings, Vaunts the high race from which he springs, Or seeks, when warriors meet and die, His own descent to glorify? Weakness and folly show confessed In every vaunt thou utterest, As when the flames fed high with grass Detect the simulating brass. Dost thou not see me standing here Armed with the mighty mace I rear, Firm as an earth upholding hill Whose summit veins of metal fill?
- **Translation**: 

---

### Verse 3 (Ramayana 0.948)
- **Original**: 930 The Ramayana Lo, here I stand before thy face To slay thee with my murderous mace, As Death, the universal lord, Stands threatening with his fatal cord. Enough of this. Much more remains That should be said: but time constrains. Ere to his rest the sun descend, And shades of night the combat end, The twice seven thousand of my band Who fell beneath thy bloody hand Shall have their tears all wiped away And triumph in thy fall to-day.” He spoke, and loosing from his hold His mighty mace ringed round with gold, Like some red bolt alive with fire Hurled it at Ráma, mad with ire. The ponderous mace which Khara threw Sent fiery flashes as it flew. Trees, shrubs were scorched beneath the blast, As onward to its aim it passed. But Ráma, watching as it sped Dire as His noose who rules the dead, Cleft it with arrows as it came On rushing with a hiss and flame. Its fury spent and burnt away, Harmless upon the ground it lay Like a great snake in furious mood By herbs of numbing power subdued.
- **Translation**: 

---

### Verse 4 (Ramayana 0.949)
- **Original**: Canto XXX. Khara's Death. 931 Canto XXX. Khara's Death. When Ráma, pride of Raghu's race, Virtue's dear son, had cleft the mace, Thus with superior smile the best Of chiefs the furious fiend addressed: “Thou, worst of giant blood, at length Hast shown the utmost of thy strength, And forced by greater might to bow, Thy vaunting threats are idle now. My shafts have cut thy club in twain: Useless it lies upon the plain, And all thy pride and haughty trust Lie with it levelled in the dust. The words that thou hast said to-day, That thou wouldst wipe the tears away Of all the giants I have slain, My deeds shall render void and vain. Thou meanest of the giants' breed, Evil in thought and word and deed, My hand shall take that life of thine As Garu 476 seized the juice divine. [264] Thou, rent by shafts, this day shalt die: Low on the ground thy corse shall lie, And bubbles from the cloven neck With froth and blood thy skin shall deck. With dust and mire all rudely dyed, Thy torn arms lying by thy side, While streams of blood each limb shall steep, Thou on earth's breast shalt take thy sleep 476 Garu , the King of Birds, carried off the Amrit or drink of Paradise from Indra's custody.
- **Translation**: 

---

### Verse 5 (Ramayana 0.950)
- **Original**: 932 The Ramayana Like a fond lover when he strains The beauty whom at length he gains. Now when thy heavy eyelids close For ever in thy deep repose, Again shall DaG ak forest be Safe refuge for the devotee. Thou slain, and all thy race who held The realm of Janasthán expelled, Again shall happy hermits rove, Fearing no danger, through the grove. Within those bounds, their brethren slain, No giant shall this day remain, But all shall fly with many a tear And fearing, rid the saints of fear. This bitter day shall misery bring On all the race that calls thee king. Fierce as their lord, thy dames shall know, Bereft of joys, the taste of woe. Base, cruel wretch, of evil mind, Plaguer of Bráhmans and mankind, With trembling hands each devotee Feeds holy fires in dread of thee.” Thus with wild fury unrepressed Raghu's brave son the fiend addressed; And Khara, as his wrath grew high, Thus thundered forth his fierce reply: “By senseless pride to madness wrought, By danger girt thou fearest naught, Nor heedest, numbered with the dead, What thou shouldst say and leave unsaid. When Fate's tremendous coils enfold The captive in resistless hold,
- **Translation**: 

---

### Verse 6 (Ramayana 0.951)
- **Original**: Canto XXX. Khara's Death. 933 He knows not right from wrong, each sense Numbed by that deadly influence.” He spoke, and when his speech was done Bent his fierce brows on Raghu's son. With eager eyes he looked around If lethal arms might yet be found. Not far away and full in view A Sál-tree towering upward grew. His lips in mighty strain compressed, He tore it up with root and crest, With huge arms waved it o'er his head And hurled it shouting, Thou art dead. But Ráma, unsurpassed in might, Stayed with his shafts its onward flight, And furious longing seized his soul The giant in the dust to roll. Great drops of sweat each limb bedewed, His red eyes showed his wrathful mood. A thousand arrows, swiftly sent, The giant's bosom tore and rent. From every gash his body showed The blood in foamy torrents flowed, As springing from their caverns leap Swift rivers down the mountain steep. When Khara felt each deadened power Yielding beneath that murderous shower, He charged, infuriate with the scent Of blood, in dire bewilderment. But Ráma watched, with ready bow, The onset of his bleeding foe, And ere the monster reached him, drew Backward in haste a yard or two. Then from his side a shaft he took
- **Translation**: 

---

### Verse 7 (Ramayana 0.952)
- **Original**: 934 The Ramayana Whose mortal stroke no life might brook: Of peerless might, it bore the name Of Brahmá's staff, and glowed with flame: Lord Indra, ruler of the skies, Himself had given the glorious prize. His bow the virtuous hero drew, And at the fiend the arrow flew. Hissing and roaring like the blast Of tempest through the air it passed, And fixed, by Ráma's vigour sped, In the foe's breast its pointed head. Then fell the fiend: the quenchless flame Burnt furious in his wounded frame. So burnt by Rudra Andhak477 fell InZvetáraGya's silvery dell: So Namuchi and Vritra478 died By steaming bolts that tamed their pride: So Bala479 fell by lightning sent By Him who rules the firmament. Then all the Gods in close array With the bright hosts who sing and play, Filled full of rapture and amaze, Sang hymns of joy in Ráma's praise, Beat their celestial drums and shed Rain of sweet flowers upon his head. For three short hours had scarcely flown, And by his pointed shafts o'erthrown The twice seven thousand fiends, whose will 477 A demon, son of Ka[yap and Diti, slain by Rudra orZiva when he attempted to carry off the tree of Paradise. 478 Namuchi and Vritra were two demons slain by Indra. Vritra personifies drought, the enemy of Indra, who imprisons the rain in the cloud. 479 Another demon slain by Indra.
- **Translation**: 

---

### Verse 8 (Ramayana 0.953)
- **Original**: Canto XXX. Khara's Death. 935 Could change their shapes, in death were still, With Tri[irás and DúshaG slain, And Khara, leader of the train. “O wondrous deed,” the bards began, “The noblest deed of virtuous man! Heroic strength that stood alone, And firmness e'en as VishGu's own!” Thus having sung, the shining train Turned to their heavenly homes again. [265] Then the high saints of royal race And loftiest station sought the place, And by the great Agastya led, With reverence to Ráma said: “For this, Lord Indra, glorious sire, Majestic as the burning fire, Who crushes cities in his rage, SoughtZarabhanga's hermitage. Thou wast, this great design to aid, Led by the saints to seek this shade, And with thy mighty arm to kill The giants who delight in ill. Thou Da[aratha's noble son, The battle for our sake hast won, And saints in DaG ak's wild who live Their days to holy tasks can give.”
- **Translation**: 

---

### Verse 9 (Ramayana 0.954)
- **Original**: 936 The Ramayana Forth from the mountain cavern came The hero LakshmaG with the dame. And rapture beaming from his face, Resought the hermit dwelling-place. Then when the mighty saints had paid Due honour for the victor's aid, The glorious Ráma honoured too By LakshmaG to his cot withdrew. When Sítá looked upon her lord, His foemen slain, the saints restored, In pride and rapture uncontrolled She clasped him in her loving hold. On the dead fiends her glances fell: She saw her lord alive and well, Victorious after toil and pain, And Janak's child was blest again. Once more, once more with new delight Her tender arms she threw Round Ráma whose victorious might Had crushed the demon crew. Then as his grateful reverence paid Each saint of lofty soul, O'er her sweet face, all fears allayed, The flush of transport stole. Canto XXXI. Rávan. But of the host of giants one, Akampan, from the field had run And sped to Lanká480 to relate 480 The capital of the giant king RávaG.
- **Translation**: 

---

### Verse 10 (Ramayana 0.955)
- **Original**: Canto XXXI. Rávan. 937 In RávaG's ear the demons' fate: “King, many a giant from the shade Of Janasthán in death is laid: Khara the chief is slain, and I Could scarcely from the battle fly.” Fierce anger, as the monarch heard, Inflamed his look, his bosom stirred, And while with scorching glance he eyed The messenger, he thus replied: “What fool has dared, already dead, Strike Janasthán, the general dread? Who is the wretch shall vainly try In earth, heaven, hell, from me to fly? Vai[ravaG,481 Indra, VishGu, He Who rules the dead, must reverence me; For not the mightiest lord of these Can brave my will and live at ease. Fate finds in me a mightier fate To burn the fires that devastate. With unresisted influence I Can force e'en Death himself to die, With all-surpassing might restrain The fury of the hurricane, And burn in my tremendous ire The glory of the sun and fire.” 481 Kuvera, the God of gold.
- **Translation**: 

---

### Verse 11 (Ramayana 0.956)
- **Original**: 938 The Ramayana As thus the fiend's hot fury blazed, His trembling hands Akampan raised, And with a voice which fear made weak, Permission craved his tale to speak. King RávaG gave the leave he sought, And bade him tell the news he brought. His courage rose, his voice grew bold, And thus his mournful tale he told: “A prince with mighty shoulders, sprung From Da[aratha, brave and young, With arms well moulded, bears the name Of Ráma with a lion's frame. Renowned, successful, dark of limb, Earth has no warrior equals him. He fought in Janasthán and slew DúshaG the fierce and Khara too.” RávaG the giants' royal chief. Received Akampan's tale of grief. Then, panting like an angry snake, These words in turn the monarch spake: “Say quick, did Ráma seek the shade Of Janasthán with Indra's aid, And all the dwellers in the skies To back his hardy enterprise?” Akampan heard, and straight obeyed His master, and his answer made. Then thus the power and might he told Of Raghu's son the lofty-souled:
- **Translation**: 

---

### Verse 12 (Ramayana 0.957)
- **Original**: Canto XXXI. Rávan. 939 “Best is that chief of all who know With deftest art to draw the bow. His are strange arms of heavenly might, And none can match him in the fight. His brother LakshmaG brave as he, Fair as the rounded moon to see, With eyes like night and voice that comes Deep as the roll of beaten drums, By Ráma's side stands ever near, Like wind that aids the flame's career. That glorious chief, that prince of kings, On Janasthán this ruin brings. No Gods were there,— dismiss the thought No heavenly legions came and fought. His swift-winged arrows Ráma sent, Each bright with gold and ornament. To serpents many-faced they turned: [266] The giant hosts they ate and burned. Where'er these fled in wild dismay Ráma was there to strike and slay. By him O King of high estate, Is Janasthán left desolate.” Akampan ceased: in angry pride The giant monarch thus replied: “To Janasthán myself will go And lay these daring brothers low.” Thus spoke the king in furious mood: Akampan then his speech renewed: “O listen while I tell at length The terror of the hero's strength. No power can check, no might can tame Ráma, a chief of noblest fame.
- **Translation**: 

---

### Verse 13 (Ramayana 0.958)
- **Original**: 940 The Ramayana He with resistless shafts can stay The torrent foaming on its way. Sky, stars, and constellations, all To his fierce might would yield and fall. His power could earth itself uphold Down sinking as it sank of old.482 Or all its plains and cities drown, Breaking the wild sea's barrier down; Crush the great deep's impetuous will, Or bid the furious wind be still. He glorious in his high estate The triple world could devastate, And there, supreme of men, could place His creatures of a new-born race. Never can mighty Ráma be O'ercome in fight, my King, by thee. Thy giant host the day might win From him, if heaven were gained by sin. If Gods were joined with demons, they Could ne'er, I ween, that hero slay, But guile may kill the wondrous man; Attend while I disclose the plan. His wife, above all women graced, Is Sítá of the dainty waist, With limbs to fair proportion true, And a soft skin of lustrous hue, Round neck and arm rich gems are twined: She is the gem of womankind. With her no bright Gandharví vies, No nymph or Goddess in the skies; And none to rival her would dare 'Mid dames who part the long black hair. 482 In the great deluge.
- **Translation**: 

---

### Verse 14 (Ramayana 0.959)
- **Original**: Canto XXXI. Rávan. 941 That hero in the wood beguile, And steal his lovely spouse the while. Reft of his darling wife, be sure, Brief days the mourner will endure.” With flattering hope of triumph moved The giant king that plan approved, Pondered the counsel in his breast, And then Akampan thus addressed: “Forth in my car I go at morn, None but the driver with me borne, And this fair Sítá will I bring Back to my city triumphing.” Forth in his car by asses drawn The giant monarch sped at dawn, Bright as the sun, the chariot cast Light through the sky as on it passed. Then high in air that best of cars Traversed the path of lunar stars, Sending a fitful radiance pale As moonbeams shot through cloudy veil. Far on his airy way he flew: Near Tá akeya's483 grove he drew. Márícha welcomed him, and placed Before him food which giants taste, With honour led him to a seat, And brought him water for his feet; And then with timely words addressed Such question to his royal guest: 483 The giant Márícha, son of Tá aká. Tá aká was slain by Ráma. See p. 39.
- **Translation**: 

---

### Verse 15 (Ramayana 0.960)
- **Original**: 942 The Ramayana “Speak, is it well with thee whose sway The giant multitudes obey? I know not all, and ask in fear The cause, O King, why thou art here.” Ráva, the giants' mighty king, Heard wise Márícha's questioning, And told with ready answer, taught In eloquence, the cause he sought: “My guards, the bravest of my band, Are slain by Ráma's vigorous hand, And Janasthán, that feared no hate Of foes, is rendered desolate. Come, aid me in the plan I lay To steal the conqueror's wife away.” Márícha heard the king's request, And thus the giant chief addressed: “What foe in friendly guise is he Who spoke of Sítá's name to thee? Who is the wretch whose thought would bring Destruction on the giants' king? Whose is the evil counsel, say, That bids thee bear his wife away, And careless of thy life provoke Earth's loftiest with threatening stroke? A foe is he who dared suggest This hopeless folly to thy breast, Whose ill advice would bid thee draw The venomed fang from serpent's jaw. By whose unwise suggestion led Wilt thou the path of ruin tread? Whence falls the blow that would destroy Thy gentle sleep of ease and joy?
- **Translation**: 

---

### Verse 16 (Ramayana 0.961)
- **Original**: Canto XXXI. Rávan. 943 Like some wild elephant is he That rears his trunk on high, Lord of an ancient pedigree, Huge tusks, and furious eye. RávaG, no rover of the night With bravest heart can brook, Met in the front of deadly fight, On Raghu's son to look. [267] The giant hosts were brave and strong, Good at the bow and spear: But Ráma slew the routed throng, A lion 'mid the deer. No lion's tooth can match his sword, Or arrows fiercely shot: He sleeps, he sleeps— the lion lord; Be wise and rouse him not. O Monarch of the giants, well Upon my counsel think, Lest thou for ever in the hell Of Ráma's vengeance sink: A hell, where deadly shafts are sent From his tremendous-bow, While his great arms all flight prevent, Like deepest mire below: Where the wild floods of battle rave Above the foeman's head, And each with many a feathery wave Of shafts is garlanded. O, quench the flames that in thy breast With raging fury burn; And pacified and self-possessed To Lanká's town return. Rest thou in her imperial bowers With thine own wives content,
- **Translation**: 

---

### Verse 17 (Ramayana 0.962)
- **Original**: 944 The Ramayana And in the wood let Ráma's hours With Sítá still be spent.” The lord of Lanká's isle obeyed The counsel, and his purpose stayed. Borne on his car he parted thence And gained his royal residence. Canto XXXII. Rávan Roused. But ZúrpaGakhá saw the plain Spread with the fourteen thousand slain, Doers of cruel deeds o'erthrown By Ráma's mighty arm alone, Add Tri[irás and DúshaG dead, And Khara, with the hosts they led. Their death she saw, and mad with pain, Roared like a cloud that brings the rain, And fled in anger and dismay To Lanká, seat of RávaG's sway. There on a throne of royal state Exalted sat the potentate, Begirt with counsellor and peer, Like Indra with the Storm Gods near. Bright as the sun's full splendour shone The glorious throne he sat upon, As when the blazing fire is red Upon a golden altar fed. Wide gaped his mouth at every breath, Tremendous as the jaws of Death. With him high saints of lofty thought,
- **Translation**: 

---

### Verse 18 (Ramayana 0.963)
- **Original**: Canto XXXII. Rávan Roused. 945 Gandharvas, Gods, had vainly fought. The wounds were on his body yet From wars where Gods and demons met. And scars still marked his ample chest By fierce Airávat's484 tusk impressed. A score of arms, ten necks, had he, His royal gear was brave to see. His massive form displayed each sign That marks the heir of kingly line. In stature like a mountain height, His arms were strong, his teeth were white, And all his frame of massive mould Seemed lazulite adorned with gold. A hundred seams impressed each limp Where VishGu's arm had wounded him, And chest and shoulder bore the print Of sword and spear and arrow dint, Where every God had struck a blow In battle with the giant foe. His might to wildest rage could wake The sea whose faith naught else can shake, Hurl towering mountains to the earth, And crush e'en foes of heavenly birth. The bonds of law and right he spurned: To others' wives his fancy turned. Celestial arms he used in fight, And loved to mar each holy rite. He went to Bhogavatí's town,485 Where Vásuki was beaten down, And stole, victorious in the strife, Lord Takshaka's beloved wife. 484 Indra's elephant. 485 Bhogavatí, in Pátála in the regions under the earth, is the capital of the serpent race whose king is Vásuki.
- **Translation**: 

---

### Verse 19 (Ramayana 0.964)
- **Original**: 946 The Ramayana Kailása's lofty crest he sought, And when in vain Kuvera fought, Stole Pushpak thence, the car that through The air, as willed the master, flew. Impelled by furious anger, he Spoiled Nandan's486 shade and Naliní, And Chaitraratha's heavenly grove, The haunts where Gods delight to rove. Tall as a hill that cleaves the sky, He raised his mighty arms on high To check the blessed moon, and stay The rising of the Lord of Day. Ten thousand years the giant spent On dire austerities intent, And of his heads an offering, laid Before the Self-existent, made. No God or fiend his life could take, Gandharva, goblin, bird, or snake: Safe from all fears of death, except From human arm, that life was kept. Oft when the priests began to raise Their consecrating hymns of praise, He spoiled the Soma's sacred juice Poured forth by them in solemn use.[268] The sacrifice his hands o'erthrew, And cruelly the Bráhmans slew. His was a heart that naught could melt, Joying in woes which others felt. She saw the ruthless monster there, Dread of the worlds, unused to spare. In robes of heavenly texture dressed, Celestial wreaths adorned his breast. 486 the grove of Indra.
- **Translation**: 

---

### Verse 20 (Ramayana 0.965)
- **Original**: Canto XXXIII. Súrpanakhá's Speech. 947 He sat a shape of terror, like Destruction ere the worlds it strike. She saw him in his pride of place, The joy of old Pulastya's487 race, Begirt by counsellor and peer, RávaG, the foeman's mortal fear, And terror in her features shown, The giantess approached the throne. Then ZúrpaGakhá bearing yet Each deeply printed trace Where the great-hearted chief had set A mark upon her face, Impelled by terror and desire, Still fierce, no longer bold, To RávaG of the eyes of fire Her tale, infuriate, told. Canto XXXIII. Súrpanakhá's Speech. Burning with anger, in the ring Of counsellors who girt their king, To RávaG, ravener of man, With bitter words she thus began: 487 Pulastya is considered as the ancestor of the Rakshases or giants, as he is the father of Vi[ravas, the father of RávaG and his brethren.
- **Translation**: 

---



--- End of Ramayan_batch_146.md ---


--- Start of Ramayan_batch_147.md ---

# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Ramayana 0.966)
- **Original**: 948 The Ramayana “Wilt thou absorbed in pleasure, still Pursue unchecked thy selfish will: Nor turn thy heedless eyes to see The coming fate which threatens thee? The king who days and hours employs In base pursuit of vulgar joys Must in his people's sight be vile As fire that smokes on funeral pile. He who when duty calls him spares No time for thought of royal cares, Must with his realm and people all Involved in fatal ruin fall. As elephants in terror shrink From the false river's miry brink, Thus subjects from a monarch flee Whose face their eyes may seldom see, Who spends the hours for toil ordained In evil courses unrestrained. He who neglects to guard and hold His kingdom by himself controlled, Sinks nameless like a hill whose head Is buried in the ocean's bed. Thy foes are calm and strong and wise, Fiends, Gods, and warriors of the skies,— How, heedless, wicked, weak, and vain, Wilt thou thy kingly state maintain? Thou, lord of giants, void of sense, Slave of each changing influence, Heedless of all that makes a king, Destruction on thy head wilt bring. O conquering chief, the prince, who boasts, Of treasury and rule and hosts, By others led, though lord of all, Is meaner than the lowest thrall.
- **Translation**: 

---

### Verse 2 (Ramayana 0.967)
- **Original**: Canto XXXIII. Súrpanakhá's Speech. 949 For this are monarchs said to be Long-sighted, having power to see Things far away by faithful eyes Of messengers and loyal spies. But aid from such thou wilt not seek: Thy counsellors are blind and weak, Or thou from these hadst surely known Thy legions and thy realm o'erthrown. Know, twice seven thousand, fierce in might, Are slain by Ráma in the fight, And they, the giant host who led, Khara and DúshaG, both are dead. Know, Ráma with his conquering arm Has freed the saints from dread of harm, Has smitten Janasthán and made Asylum safe in DaG ak's shade. Enslaved and dull, of blinded sight, Intoxicate with vain delight, Thou closest still thy heedless eyes To dangers in thy realm that rise. A king besotted, mean, unkind, Of niggard hand and slavish mind. Will find no faithful followers heed Their master in his hour of need. The friend on whom he most relies, In danger, from a monarch flies, Imperious in his high estate, Conceited, proud, and passionate; Who ne'er to state affairs attends With wholesome fear when woe impends Most weak and worthless as the grass, Soon from his sway the realm will pass. For rotting wood a use is found, For clods and dust that strew the ground,
- **Translation**: 

---

### Verse 3 (Ramayana 0.968)
- **Original**: 950 The Ramayana But when a king has lost his sway, Useless he falls, and sinks for aye. As raiment by another worn, As faded garland crushed and torn, So is, unthroned, the proudest king, Though mighty once, a useless thing. But he who every sense subdues And each event observant views, Rewards the good and keeps from wrong, Shall reign secure and flourish long. Though lulled in sleep his senses lie He watches with a ruler's eye, Untouched by favour, ire, and hate, And him the people celebrate. O weak of mind, without a trace[269] Of virtues that a king should grace, Who hast not learnt from watchful spy That low in death the giants lie. Scorner of others, but enchained By every base desire, By thee each duty is disdained Which time and place require. Soon wilt thou, if thou canst not learn, Ere yet it be too late, The good from evil to discern, Fall from thy high estate.” As thus she ceased not to upbraid The king with cutting speech, And every fault to view displayed, Naming and marking each, The monarch of the sons of night, Of wealth and power possessed, And proud of his imperial might, Long pondered in his breast.
- **Translation**: 

---

### Verse 4 (Ramayana 0.969)
- **Original**: Canto XXXIV. Súrpanakhá's Speech. 951 Canto XXXIV. Súrpanakhá's Speech. Then forth the giant's fury broke As ZúrpaGakhá harshly spoke. Girt by his lords the demon king Looked on her, fiercely questioning: “Who is this Ráma, whence, and where? His form, his might, his deeds declare. His wandering steps what purpose led To DaG ak forest, hard to tread? What arms are his that he could smite In fray the rovers of the night, And Tri[irás and DúshaG lay Low on the earth, and Khara slay? Tell all, my sister, and declare Who maimed thee thus, of form most fair.” Thus by the giant king addressed, While burnt her fury unrepressed, The giantess declared at length The hero's form and deeds and strength:
- **Translation**: 

---

### Verse 5 (Ramayana 0.970)
- **Original**: 952 The Ramayana “Long are his arms and large his eyes: A black deer's skin his dress supplies. King Da[aratha's son is he, Fair as Kandarpa's self to see. Adorned with many a golden band, A bow, like Indra's, arms his hand, And shoots a flood of arrows fierce As venomed snakes to burn and pierce. I looked, I looked, but never saw His mighty hand the bowstring draw That sent the deadly arrows out, While rang through air his battle-shout. I looked, I looked, and saw too well How with that hail the giants fell, As falls to earth the golden grain, Struck by the blows of Indra's rain. He fought, and twice seven thousand, all Terrific giants, strong and tall, Fell by the pointed shafts o'erthrown Which Ráma shot on foot, alone. Three little hours had scarcely fled,— Khara and DúshaG both were dead, And he had freed the saints and made Asylum sure in DaG ak's shade. Me of his grace the victor spared, Or I the giants' fate had shared. The high-souled Ráma would not deign His hand with woman's blood to stain. The glorious LakshmaG, justly dear, In gifts and warrior might his peer, Serves his great brother with the whole Devotion of his faithful soul: Impetuous victor, bold and wise, First in each hardy enterprise,
- **Translation**: 

---

### Verse 6 (Ramayana 0.971)
- **Original**: Canto XXXIV. Súrpanakhá's Speech. 953 Still ready by his side to stand, A second self or better hand. And Ráma has a large-eyed spouse, Pure as the moon her cheek and brows, Dearer than life in Ráma's sight, Whose happiness is her delight. With beauteous hair and nose the dame From head to foot has naught to blame. She shines the wood's bright Goddess, Queen Of beauty with her noble mien. First in the ranks of women placed Is Sítá of the dainty waist. In all the earth mine eyes have ne'er Seen female form so sweetly fair. Goddess nor nymph can vie with her, Nor bride of heavenly chorister. He who might call this dame his own, Her eager arms about him thrown, Would live more blest in Sítá's love Than Indra in the world above. She, peerless in her form and face And rich in every gentle grace, Is worthy bride, O King, for thee, As thou art meet her lord to be. I even I, will bring the bride In triumph to her lover's side— This beauty fairer than the rest, With rounded limb and heaving breast. Each wound upon my face I owe To cruel LakshmaG's savage blow. But thou, O brother, shalt survey Her moonlike loveliness to-day, And Káma's piercing shafts shall smite Thine amorous bosom at the sight.
- **Translation**: 

---

### Verse 7 (Ramayana 0.972)
- **Original**: 954 The Ramayana If in thy breast the longing rise To make thine own the beauteous prize, Up, let thy better foot begin The journey and the treasure win. If, giant Lord, thy favouring eyes Regard the plan which I advise, Up, cast all fear and doubt away And execute the words I say Come, giant King, this treasure seek, For thou art strong and they are weak.[270] Let Sítá of the faultless frame Be borne away and be thy dame. Thy host in Janasthán who dwelt Forth to the battle hied. And by the shafts which Ráma dealt They perished in their pride. DúshaG and Khara breathe no more, Laid low upon the plain. Arise, and ere the day be o'er Take vengeance for the slain.” Canto XXXV. Rávan's Journey. When Ráva G, by her fury spurred, That terrible advice had heard, He bade his nobles quit his side, And to the work his thought applied. He turned his anxious mind to scan On every side the hardy plan: The gain against the risk he laid, Each hope and fear with care surveyed,
- **Translation**: 

---

### Verse 8 (Ramayana 0.973)
- **Original**: Canto XXXV. Rávan's Journey. 955 And in his heart at length decreed To try performance of the deed. Then steady in his dire intent The giant to the courtyard went. There to his charioteer he cried, “Bring forth the car whereon I ride.” Aye ready at his master's word The charioteer the order heard, And yoked with active zeal the best Of chariots at his lord's behest. Asses with heads of goblins drew That wondrous car where'er it flew. Obedient to the will it rolled Adorned with gems and glistering gold. Then mounting, with a roar as loud As thunder from a labouring cloud, The mighty monarch to the tide Of Ocean, lord of rivers, hied. White was the shade above him spread, White chouris waved around his head, And he with gold and jewels bright Shone like the glossy lazulite. Ten necks and twenty arms had he: His royal gear was good to see. The heavenly Gods' insatiate foe, Who made the blood of hermits flow, He like the Lord of Hills appeared With ten huge heads to heaven upreared. In the great car whereon he rode, Like some dark cloud the giant showed, When round it in their close array The cranes 'mid wreaths of lightning play. He looked, and saw, from realms of air, The rocky shore of ocean, where
- **Translation**: 

---

### Verse 9 (Ramayana 0.974)
- **Original**: 956 The Ramayana Unnumbered trees delightful grew With flower and fruit of every hue. He looked on many a lilied pool With silvery waters fresh and cool, And shores like spacious altars meet For holy hermits' lone retreat. The graceful palm adorned the scene, The plantain waved her glossy green. There grew the sál and betel, there On bending boughs the flowers were fair. There hermits dwelt who tamed each sense By strictest rule of abstinence: Gandharvas, Kinnars,488 thronged the place, Nágas and birds of heavenly race. Bright minstrels of the ethereal quire, And saints exempt from low desire, With Ájas, sons of Brahmá's line, Maríchipas of seed divine, Vaikhánasas and Máshas strayed, And Bálakhilyas489 in the shade. The lovely nymphs of heaven were there, Celestial wreaths confined their hair, And to each form new grace was lent By wealth of heavenly ornament. Well skilled was each in play and dance And gentle arts of dalliance. The glorious wife of many a God Those beautiful recesses trod, There Gods and Dánavs, all who eat The food of heaven, rejoiced to meet. The swan and Sáras thronged each bay 488 Beings with the body of a man and the head of a horse. 489 Ájas, Maríchipas, Vaikhánasas, Máshas, and Bálakhilyas are classes of supernatural beings who lead the lives of hermits.
- **Translation**: 

---

### Verse 10 (Ramayana 0.975)
- **Original**: Canto XXXV. Rávan's Journey. 957 With curlews, ducks, and divers gay, Where the sea spray rose soft and white O'er rocks of glossy lazulite. As his swift way the fiend pursued Pale chariots of the Gods he viewed, Bearing each lord whose rites austere Had raised him to the heavenly sphere. Thereon celestial garlands hung, There music played and songs were sung. Then bright Gandharvas met his view, And heavenly nymphs, as on he flew. He saw the sandal woods below, And precious trees of odorous flow, That to the air around them lent Their riches of delightful scent; Nor failed his roving eye to mark Tall aloe trees in grove and park. He looked on wood with cassias filled, And plants which balmy sweets distilled, Where her fair flowers the betel showed And the bright pods of pepper glowed. The pearls in many a silvery heap Lay on the margin of the deep. And grey rocks rose amid the red Of coral washed from ocean's bed. [271] High soared the mountain peaks that bore Treasures of gold and silver ore, And leaping down the rocky walls Came wild and glorious waterfalls. Fair towns which grain and treasure held, And dames who every gem excelled, He saw outspread beneath him far, With steed, and elephant, and car. That ocean shore he viewed that showed
- **Translation**: 

---

### Verse 11 (Ramayana 0.976)
- **Original**: 958 The Ramayana Fair as the blessed Gods' abode Where cool delightful breezes played O'er levels in the freshest shade. He saw a fig-tree like a cloud With mighty branches earthward bowed. It stretched a hundred leagues and made For hermit bands a welcome shade. Thither the feathered king of yore An elephant and tortoise bore, And lighted on a bough to eat The captives of his taloned feet. The bough unable to sustain The crushing weight and sudden strain, Loaded with sprays and leaves of spring Gave way beneath the feathered king. Under the shadow of the tree Dwelt many a saint and devotee, Ájas, the sons of Brahmá's line, Máshas, Maríchipas divine. Vaikhánasas, and all the race Of Bálakhilyas, loved the place. But pitying their sad estate The feathered monarch raised the weight Of the huge bough, and bore away The loosened load and captured prey. A hundred leagues away he sped, Then on his monstrous booty fed, And with the bough he smote the lands Where dwell the wild Nisháda bands. High joy was his because his deed From jeopardy the hermits freed. That pride for great deliverance wrought A double share of valour brought. His soul conceived the high emprise
- **Translation**: 

---

### Verse 12 (Ramayana 0.977)
- **Original**: Canto XXXV. Rávan's Journey. 959 To snatch the Amrit from the skies. He rent the nets of iron first, Then through the jewel chamber burst, And bore the drink of heaven away That watched in Indra's palace lay. Such was the hermit-sheltering tree Which RávaG turned his eye to see. Still marked where Garu sought to rest, The fig-tree bore the name of Blest. When Ráva G stayed his chariot o'er The ocean's heart-enchanting shore, He saw a hermitage that stood Sequestered in the holy wood. He saw the fiend Márícha there With deerskin garb, and matted hair Coiled up in hermit guise, who spent His days by rule most abstinent. As guest and host are wont to meet, They met within that lone retreat. Before the king Márícha placed Food never known to human taste. He entertained his guest with meat And gave him water for his feet, And then addressed the giant king With timely words of questioning: “Lord, is it well with thee, and well With those in Lanká's town who dwell? What sudden thought, what urgent need Has brought thee with impetuous speed?”
- **Translation**: 

---

### Verse 13 (Ramayana 0.978)
- **Original**: 960 The Ramayana The fiend Márícha thus addressed RávaG the king, his mighty guest, And he, well skilled in arts that guide The eloquent, in turn replied: Canto XXXVI. Rávan's Speech. “Hear me, Márícha, while I speak, And tell thee why thy home I seek. Sick and distressed am I, and see My surest hope and help in thee. Of Janasthán I need not tell, Where ZúrpaGakhá, Khara, dwell, And DúshaG with the arm of might, And Tri[irás, the fierce in fight, Who feeds on human flesh and gore, And many noble giants more, Who roam in dark of midnight through The forest, brave and strong and true. By my command they live at ease And slaughter saints and devotees. Those twice seven thousand giants, all Obedient to their captain's call, Joying in war and ruthless deeds Follow where mighty Khara leads. Those fearless warrior bands who roam Through Janasthán their forest home, In all their terrible array Met Ráma in the battle fray. Girt with all weapons forth they sped With Khara at the army's head.
- **Translation**: 

---

### Verse 14 (Ramayana 0.979)
- **Original**: Canto XXXVI. Rávan's Speech. 961 The front of battle Ráma held: With furious wrath his bosom swelled. Without a word his hate to show He launched the arrows from his bow. On the fierce hosts the missiles came, Each burning with destructive flame, The twice seven thousand fell o'erthrown By him, a man, on foot, alone. Khara the army's chief and pride, And DúshaG, fearless warrior, died, And Tri[irás the fierce was slain, And Da G ak wood was free again. He, banished by his angry sire, Roams with his wife in mean attire. This wretch, his Warrior tribe's disgrace Has slain the best of giant race. [272] Harsh, wicked, fierce and greedy-souled, A fool, with senses uncontrolled, No thought of duty stirs his breast: He joys to see the world distressed. He sought the wood with fair pretence Of truthful life and innocence, But his false hand my sister left Mangled, of nose and ears bereft. This Ráma's wife who bears the name Of Sítá, in her face and frame Fair as a daughter of the skies,— Her will I seize and bring the prize Triumphant from the forest shade: For this I seek thy willing aid. If thou, O mighty one, wilt lend Thy help and stand beside thy friend, I with my brothers may defy
- **Translation**: 

---

### Verse 15 (Ramayana 0.980)
- **Original**: 962 The Ramayana All Gods embattled in the sky. Come, aid me now, for thine the power To succour in the doubtful hour. Thou art in war and time of fear, For heart and hand, without a peer. For thou art skilled in art and wile, A warrior brave and trained in guile. With this one hope, this only aim, O Rover of the Night, I came. Now let me tell what aid I ask To back me in my purposed task. In semblance of a golden deer Adorned with silver spots appear. Go, seek his dwelling: in the way Of Ráma and his consort stray. Doubt not the lady, when she sees The wondrous deer amid the trees, Will bid her lord and LakshmaG take The creature for its beauty's sake. Then when the chiefs have parted thence, And left her lone, without defence, As Ráhu storms the moonlight, I Will seize the lovely dame and fly. Her lord will waste away and weep For her his valour could not keep. Then boldly will I strike the blow And wreak my vengeance on the foe.” When wise Márícha heard the tale His heart grew faint, his cheek was pale, He stared with open orbs, and tried To moisten lips which terror dried, And grief, like death, his bosom rent As on the king his look he bent.
- **Translation**: 

---

### Verse 16 (Ramayana 0.981)
- **Original**: Canto XXXVII. Márícha's Speech. 963 The monarch's will he strove to stay, Distracted with alarm, For well he knew the might that lay In Ráma's matchless arm. With suppliant hands Márícha stood And thus began to tell His counsel for the tyrant's good, And for his own as well: Canto XXXVII. Márícha's Speech. Márícha gave attentive ear The ruler of the fiends to hear: Then, trained in all the rules that teach The eloquent, began his speech: “'Tis easy task, O King, to find Smooth speakers who delight the mind. But they who urge and they who do Distasteful things and wise, are few. Thou hast not learnt, by proof untaught, And borne away by eager thought, That Ráma, formed for high emprise, With VaruG or with Indra vies. Still let thy people live in peace, Nor let their name and lineage cease, For Ráma with his vengeful hand Can sweep the giants from the land. O, let not Janak's daughter bring Destruction on the giant king. Let not the lady Sítá wake A tempest, on thy head to break.
- **Translation**: 

---

### Verse 17 (Ramayana 0.982)
- **Original**: 964 The Ramayana Still let the dame, by care untried, Be happy by her husband's side, Lest swift avenging ruin fall On glorious Lanká, thee, and all. Men such as thou with wills unchained, Advised by sin and unrestrained, Destroy themselves, the king, the state, And leave the people desolate. Ráma, in bonds of duty held, Was never by his sire expelled. He is no wretch of greedy mind, Dishonour of his Warrior kind. Free from all touch of rancorous spite, All creatures' good is his delight. He saw his sire of truthful heart Deceived by Queen Kaikeyí's art, And said, a true and duteous son, “What thou hast promised shall be done.” To gratify the lady's will, His father's promise to fulfil, He left his realm and all delight For DaG ak wood, an anchorite. No cruel wretch, no senseless fool Is Ráma, unrestrained by rule. This groundless charge has ne'er been heard, Nor shouldst thou speak the slanderous word. Ráma in truth and goodness bold Is Virtue's self in human mould, The sovereign of the world confessed As Indra rules among the Blest. And dost thou plot from him to rend The darling whom his arms defend? Less vain the hope to steal away The glory of the Lord of Day.[273]
- **Translation**: 

---

### Verse 18 (Ramayana 0.983)
- **Original**: Canto XXXVII. Márícha's Speech. 965 O RávaG, guard thee from the fire Of vengeful Ráma's kindled ire,— Each spark a shaft with deadly aim, While bow and falchion feed the flame. Cast not away in hopeless strife Thy realm, thy bliss, thine own dear life. O RávaG of his might beware, A God of Death who will not spare. That bow he knows so well to draw Is the destroyer's flaming jaw, And with his shafts which flash and glow He slays the armies of the foe. Thou ne'er canst win— the thought forego— From the safe guard of shaft and bow King Janak's child, the dear delight Of Ráma unapproached in might. The spouse of Raghu's son, confessed Lion of men with lion chest,— Dearer than life, through good and ill Devoted to her husband's will, The slender-waisted, still must be From thy polluting touches free. Far better grasp with venturous hand The flame to wildest fury fanned. What, King of giants, canst thou gain From this attempt so wild and vain? If in the fight his eye he bend Upon thee, Lord, thy days must end, So life and bliss and royal sway, Lost beyond hope, will pass away. Summon each lord of high estate, And chief, VibhishaG490 to debate. 490 “The younger brother of the giant RávaG; when he and his brother had practiced austerities for a long series of years, Brahmá appeared to offer
- **Translation**: 

---

### Verse 19 (Ramayana 0.984)
- **Original**: 966 The Ramayana With peers in lore of counsel tried Consider, reason, and decide Scan strength and weakness, count the cost, What may be gained and what be lost. Examine and compare aright Thy proper power and Ráma's might, Then if thy weal be still thy care, Thou wilt be prudent and forbear. O giant King, the contest shun, Thy force is all too weak The lord of Kosál's mighty son In deadly fray to seek. King of the hosts that rove at night, O hear what I advise: My prudent counsel do not slight; Be patient and be wise.” Canto XXXVIII. Márícha's Speech. them boons: VibhishaGa asked that he might never meditate any unrighteous- ness.… On the death of RávaG VibhishaGa was installed as Rája of Lanká.” G ARRETT 'S{FNS Classical Dictionary of India.
- **Translation**: 

---

### Verse 20 (Ramayana 0.985)
- **Original**: Canto XXXVIII. Márícha's Speech. 967 “Once in my strength and vigour's pride I roamed this earth from side to side, And towering like a mountain's crest, A thousand Nágas'491 might possessed. Like some vast sable cloud I showed: My golden armlets flashed and glowed. A crown I wore, an axe I swayed, And all I met were sore afraid. I roved where DaG ak wood is spread; On flesh of slaughtered saints I fed. Then Vi[vámitra, sage revered, Holy of heart, my fury feared. To Da[aratha's court he sped And went before the king and said:492 “With me, my lord, thy Ráma send On holy days his aid to lend. Márícha fills my soul with dread And keeps me sore disquieted.” The monarch heard the saint's request And thus the glorious sage addressed: “My boy as yet in arms untrained The age of twelve has scarce attained. But I myself a host will lead To guard thee in the hour of need. My host with fourfold troops complete, The rover of the night shall meet, And I, O best of saints, will kill Thy foeman and thy prayer fulfil.” The king vouchsafed his willing aid: The saint again this answer made: 491 Serpent-gods. 492 See p. 33.
- **Translation**: 

---



--- End of Ramayan_batch_147.md ---


--- Start of Ramayan_batch_148.md ---

# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Ramayana 0.986)
- **Original**: 968 The Ramayana “By Ráma's might, and his alone, Can this great fiend be overthrown. I know in days of yore the Blest Thy saving help in fight confessed. Still of thy famous deeds they tell In heaven above, in earth, and hell, A mighty host obeys thy hest: Here let it still, I pray thee, rest. Thy glorious son, though yet a boy, Will in the fight that fiend destroy. Ráma alone with me shall go: Be happy, victor of the foe.” He spoke: the monarch gave assent, And Ráma to the hermit lent. So to his woodland home in joy Went Vi[vámitra with the boy. With ready bow the champion stood To guard the rites in DaG ak wood. With glorious eyes, most bright to view, Beardless as yet and dark of hue; A single robe his only wear, His temples veiled with waving hair,[274] Around his neck a chain of gold, He grasped the bow he loved to hold; And the young hero's presence made A glory in the forest shade. Thus Ráma with his beauteous mien, Like the young rising moon was seen, I, like a cloud which tempest brings, My arms adorned with golden rings, Proud of the boon which lent me might, Approached where dwelt the anchorite. But Ráma saw me venturing nigh,
- **Translation**: 

---

### Verse 2 (Ramayana 0.987)
- **Original**: Canto XXXVIII. Márícha's Speech. 969 Raising my murderous axe on high; He saw, and fearless of the foe, Strung with calm hand his trusty bow. By pride of conscious strength beguiled, I scorned him as a feeble child, And rushed with an impetuous bound On Vi[vámitra's holy ground. A keen swift shaft he pointed well, The foeman's rage to check and quell, And hurled a hundred leagues away Deep in the ocean waves I lay. He would not kill, but, nobly brave, My forfeit life he chose to save. So there I lay with wandering sense Dazed by that arrow's violence. Long in the sea I lay: at length Slowly returned my sense and strength, And rising from my watery bed To Lanká's town again I sped. Thus was I spared, but all my band Fell slain by Ráma's conquering hand,— A boy, untrained in warrior's skill, Of iron arm and dauntless will. If thou with Ráma still, in spite Of warning and of prayer, wilt fight, I see terrific woes impend, And dire defeat thy days will end. Thy giants all will feel the blow And share the fatal overthrow, Who love the taste of joy and play, The banquet and the festal day. Thine eyes will see destruction take Thy Lanká, lost for Sítá's sake, And stately pile and palace fall
- **Translation**: 

---

### Verse 3 (Ramayana 0.988)
- **Original**: 970 The Ramayana With terrace, dome, and jewelled wall. The good will die: the crime of kings Destruction on the people brings: The sinless die, as in the lake The fish must perish with the snake. The prostrate giants thou wilt see Slain for this folly wrought by thee, Their bodies bright with precious scent And sheen of heavenly ornament; Or see the remnant of thy train Seek refuge far, when help is vain And with their wives, or widowed, fly To every quarter of the sky; Thy mournful eyes, where'er they turn, Will see thy stately city burn, When royal homes with fire are red, And arrowy nets around are spread. A sin that tops all sins in shame Is outrage to another's dame, A thousand wives thy palace fill, And countless beauties wait thy will. O rest contented with thine own, Nor let thy race be overthrown. If thou, O King, hast still delight In rank and wealth and power and might, In noble wives, in troops of friends, In all that royal state attends, I warn thee, cast not all away, Nor challenge Ráma to the fray. If deaf to every friendly prayer, Thou still wilt seek the strife, And from the side of Ráma tear His lovely Maithil wife, Soon will thy life and empire end
- **Translation**: 

---

### Verse 4 (Ramayana 0.989)
- **Original**: Canto XXXIX. Márícha's Speech. 971 Destroyed by Ráma's bow, And thou, with kith and kin and friend, To Yáma's realm must go.” Canto XXXIX. Márícha's Speech. “I told thee of that dreadful day When Ráma smote and spared to slay. Now hear me, RávaG, while I tell What in the after time befell. At length, restored to strength and pride, I and two mighty fiends beside Assumed the forms of deer and strayed Through DaG ak wood in lawn and glade, I reared terrific horns: beneath Were flaming tongue and pointed teeth. I roamed where'er my fancy led, And on the flesh of hermits fed, In sacred haunt, by hallowed tree, Where'er the ritual fires might be. A fearful shape, I wandered through The wood, and many a hermit slew. With ruthless rage the saints I killed Who in the grove their tasks fulfilled. When smitten to the earth they sank, Their flesh I ate, their blood I drank, And with my cruel deeds dismayed All dwellers in the forest shade, Spoiling their rites in bitter hate, With human blood inebriate. Once in the wood I chanced to see
- **Translation**: 

---

### Verse 5 (Ramayana 0.990)
- **Original**: 972 The Ramayana Ráma again, a devotee, A hermit, fed on scanty fare, Who made the good of all his care. His noble wife was by his side, And Lakshma G in the battle tried. In senseless pride I scorned the might Of that illustrious anchorite, And heedless of a hermit foe, Recalled my earlier overthrow.[275] I charged him in my rage and scorn To slay him with my pointed horn, In heedless haste, to fury wrought As on my former wounds I thought. Then from the mighty bow he drew Three foe-destroying arrows flew, Keen-pointed, leaping from the string, Swift as the wind or feathered king. Dire shafts, on flesh of foemen fed, Like rushing thunderbolts they sped, With knots well smoothed and barbs well bent, Shot e'en as one, the arrows went. But I who Ráma's might had felt, And knew the blows the hero dealt, Escaped by rapid flight. The two Who lingered on the spot, he slew. I fled from mortal danger, freed From the dire shaft by timely speed. Now to deep thought my days I give, And as a humble hermit live. In every shrub, in every tree I view that noblest devotee. In every knotted trunk I mark His deerskin and his coat of bark, And see the bow-armed Ráma stand
- **Translation**: 

---

### Verse 6 (Ramayana 0.991)
- **Original**: Canto XXXIX. Márícha's Speech. 973 Like Yáma with his noose in hand. I tell thee RávaG, in my fright A thousand Rámas mock my sight, This wood with every bush and bough Seems all one fearful Ráma now. Throughout the grove there is no spot So lonely where I see him not. He haunts me in my dreams by night, And wakes me with the wild affright. The letter that begins his name Sends terror through my startled frame. The rapid cars whereon we ride, The rich rare jewels, once my pride, Have names493 that strike upon mine ear With hated sound that counsels fear. His mighty strength too well I know, Nor art thou match for such a foe. Too strong were Raghus's son in fight For Namuchi or Bali's might. Then Ráma to the battle dare, Or else be patient and forbear; But, wouldst thou see me live in peace, Let mention of the hero cease. The good whose holy lives were spent In deepest thought, most innocent, With all their people many a time Have perished through another's crime. So in the common ruin, I Must for another's folly die, Do all thy strength and courage can, But ne'er will I approve the plan. For he, in might supremely great, 493 The Sanskrit words for car and jewels begin withra.
- **Translation**: 

---

### Verse 7 (Ramayana 0.992)
- **Original**: 974 The Ramayana The giant world could extirpate, Since, when impetuous Khara sought The grove of Janasthán and fought For ZúrpaGakhá's sake, he died By Ráma's hand in battle tried. How has he wronged thee? Soothly swear, And Ráma's fault and sin declare. I warn thee, and my words are wise, I seek thy people's weal: But if this rede thou wilt despise, Nor hear my last appeal, Thou with thy kin and all thy friends In fight this day wilt die, When his great bow the hero bends, And shafts unerring fly.” Canto XL. Rávan's Speech. But RávaG scorned the rede he gave In timely words to warn and save, E'en as the wretch who hates to live Rejects the herb the leeches give. By fate to sin and ruin spurred, That sage advice the giant heard, Then in reproaches hard and stern Thus to Márícha spoke in turn:
- **Translation**: 

---

### Verse 8 (Ramayana 0.993)
- **Original**: Canto XL. Rávan's Speech. 975 “Is this thy counsel, weak and base, Unworthy of thy giant race? Thy speech is fruitless, vain, thy toil Like casting seed on barren soil. No words of thine shall drive me back From Ráma and the swift attack. A fool is he, inured to sin, And more, of human origin. The craven, at a woman's call To leave his sire, his mother, all The friends he loved, the power and sway, And hasten to the woods away! But now his anger will I rouse, Stealing away his darling spouse. I in thy sight will ravish her From Khara's cruel murderer. Upon this plan my soul is bent, And naught shall move my firm intent, Not if the way through demons led And Gods with Indra at their head. 'Tis thine, when questioned, to explain The hope and fear, the loss and gain, And, when thy king thy thoughts would know, The triumph or the danger show. A prudent counsellor should wait, And speak when ordered in debate, With hands uplifted, calm and meek, If honour and reward he seek. Or, when some prudent course he sees Which, spoken, may his king displease [276] He should by hints of dexterous art His counsel to his lord impart. But prudent words are said in vain When the blunt speech brings grief and pain.
- **Translation**: 

---

### Verse 9 (Ramayana 0.994)
- **Original**: 976 The Ramayana A high-souled king will scarcely thank The man who shames his royal rank. Five are the shapes that kings assume, Of majesty, of grace, and gloom: Like Indra now, or Agni, now Like the dear Moon, with placid brow: Like mighty VaruG now they show, Now fierce as He who rules below. O giant, monarchs lofty-souled Are kind and gentle, stern and bold, With gracious love their gifts dispense And swiftly punish each offence. Thus subjects should their rulers view With all respect and honour due. But folly leads thy heart to slight Thy monarch and neglect his right. Thou hast in lawless pride addressed With bitter words thy royal guest. I asked thee not my strength to scan, Or loss and profit in the plan. I only spoke to tell the deed O mighty one, by me decreed, And bid thee in the peril lend Thy succour to support thy friend. Hear me again, and I will tell How thou canst aid my venture well. In semblance of a golden deer Adorned with silver drops, appear: And near the cottage in the way Of Ráma and his consort stray. Draw nigh, and wandering through the brake With thy strange form her fancy take. The Maithil dame with wondering eyes Will took upon thy fair disguise,
- **Translation**: 

---

### Verse 10 (Ramayana 0.995)
- **Original**: Canto XL. Rávan's Speech. 977 And quickly bid her husband go And bring the deer that charms her so, When Raghu's son has left the place, Still pressing onward in the chase, Cry out,“O Lakshma G! Ah, mine own!” With voice resembling Ráma's tone. When Lakshma G hears his brother's cry, Impelled by Sítá he will fly, Restless with eager love, to aid The hunter in the distant shade. When both her guards have left her side, Even as Indra, thousand-eyed, ClaspsZachí, will I bear away The Maithil dame an easy prey. When thou, my friend, this aid hast lent, Go where thou wilt and live content. True servant, faithful to thy vow, With half my realm I thee endow. Go forth, may luck thy way attend That leads thee to the happy end. I in my car will quickly be In DaG ak wood, and follow thee. So will I cheat this Ráma's eyes And win without a blow the prize; And safe return to Lanká's town With thee, my friend, this day shall crown. But if thou wilt not aid my will, My hand this day thy blood shall spill. Yea, thou must share the destined task, For force will take the help I ask. No bliss that rebel's life attends Whose stubborn will his lord offends. Thy life, if thou the task assay, In jeopardy may stand;
- **Translation**: 

---

### Verse 11 (Ramayana 0.996)
- **Original**: 978 The Ramayana Oppose me, and this very day Thou diest by this hand. Now ponder all that thou hast heard Within thy prudent breast: Reflect with care on every word, And do what seems the best.” Canto XLI. Márícha's Reply. Against his judgment sorely pressed By his imperious lord's behest, Márícha threats of death defied And thus with bitter words replied: “Ah, who, my King, with sinful thought This wild and wicked counsel taught, By which destruction soon will fall On thee, thy sons, thy realm and all? Who is the guilty wretch who sees With envious eye thy blissful ease, And by this plan, so falsely shown, Death's gate for thee has open thrown? With souls impelled by mean desire Thy foes against thy life conspire. They urge thee to destruction's brink, And gladly would they see thee sink. Who with base thought to work thee woe This fatal road has dared to show, And, triumph in his wicked eye, Would see thee enter in and die? To all thy counsellors, untrue, The punishment of death is due,
- **Translation**: 

---

### Verse 12 (Ramayana 0.997)
- **Original**: Canto XLI. Márícha's Reply. 979 Who see thee tempt the dangerous way, Nor strain each nerve thy foot to stay. Wise lords, whose king, by passion led, The path of sin begins to tread, Restrain him while there yet is time: But thine,— they see nor heed the crime. These by their master's will obtain Merit and fame and joy and gain. 'Tis only by their master's grace That servants hold their lofty place. But when the monarch stoops to sin They lose each joy they strive to win, And all the people people high and low Fall in the common overthrow. [277] Merit and fame and honour spring, Best of the mighty, from the king. So all should strive with heart and will To keep the king from every ill. Pride, violence, and sullen hate Will ne'er maintain a monarch's state, And those who cruel deeds advise Must perish when their master dies, Like drivers with their cars o'erthrown In places rough with root and stone. The good whose holy lives were spent On duty's highest laws intent, With wives and children many a time Have perished for another's crime. Hapless are they whose sovereign lord, Opposed to all, by all abhorred, Is cruel-hearted, harsh, severe: Thus might a jackal tend the deer. Now all the giant race await, Destroyed by thee, a speedy fate,
- **Translation**: 

---

### Verse 13 (Ramayana 0.998)
- **Original**: 980 The Ramayana Ruled by a king so cruel-souled, Foolish in heart and uncontrolled. Think not I fear the sudden blow That threatens now to lay me low: I mourn the ruin that I see Impending o'er thy host and thee. Me first perchance will Ráma kill, But soon his hand thy blood will spill. I die, and if by Ráma slain And not by thee, I count it gain. Soon as the hero's face I see His angry eyes will murder me, And if on her thy hands thou lay Thy friends and thou are dead this day. If with my help thou still must dare The lady from her lord to tear, Farewell to all our days are o'er, Lanká and giants are no more. In vain, in vain, an earnest friend, I warn thee, King, and pray. Thou wilt not to my prayers attend, Or heed the words I say So men, when life is fleeting fast And death's sad hour is nigh, Heedless and blinded to the last Reject advice and die.” Canto XLII. Márícha Transformed.
- **Translation**: 

---

### Verse 14 (Ramayana 0.999)
- **Original**: Canto XLII. Márícha Transformed. 981 Márícha thus in wild unrest With bitter words the king addressed. Then to his giant lord in dread, “Arise, and let us go,” he said. “Ah, I have met that mighty lord Armed with his shafts and bow and sword, And if again that bow he bend Our lives that very hour will end. For none that warrior can provoke And think to fly his deadly stroke. Like Yáma with his staff is he, And his dread hand will slaughter thee. What can I more? My words can find No passage to thy stubborn mind. I go, great King, thy task to share, And may success attend thee there.” With that reply and bold consent The giant king was well content. He strained Márícha to his breast And thus with joyful words addressed: “There spoke a hero dauntless still, Obedient to his master's will, Márícha's proper self once more: Some other took thy shape before. Come, mount my jewelled car that flies. Will-governed, through the yielding skies. These asses, goblin-faced, shall bear Us quickly through the fields of air. Attract the lady with thy shape, Then through the wood, at will, escape. And I, when she has no defence, Will seize the dame and bear her thence.”
- **Translation**: 

---

### Verse 15 (Ramayana 0.1000)
- **Original**: 982 The Ramayana Again Márícha made reply, Consent and will to signify. With rapid speed the giants two From the calm hermit dwelling flew, Borne in that wondrous chariot, meet For some great God's celestial seat. They from their airy path looked down On many a wood and many a town, On lake and river, brook and rill, City and realm and towering hill. Soon he whom giant hosts obeyed, Márícha by his side, surveyed The dark expanse of DaG ak wood Where Ráma's hermit cottage stood. They left the flying car, whereon The wealth of gold and jewels shone, And thus the giant king addressed Márícha as his hand he pressed: “Márícha, look! before our eyes Round Ráma's home the plantains rise. His hermitage is now in view: Quick to the work we came to do!” Thus RávaG spoke, Márícha heard Obedient to his master's word, Threw off his giant shape and near The cottage strayed a beauteous deer. With magic power, by rapid change, His borrowed form was fair and strange. A sapphire tipped each horn with light; His face was black relieved with white. The turkis and the ruby shed A glory from his ears and head.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1001)
- **Original**: Canto XLII. Márícha Transformed. 983 His arching neck was proudly raised, And lazulites beneath it blazed. With roseate bloom his flanks were dyed, And lotus tints adorned his hide. His shape was fair, compact, and slight; [278] His hoofs were carven lazulite. His tail with every changing glow Displayed the hues of Indra's bow. With glossy skin so strangely flecked, With tints of every gem bedecked. A light o'er Ráma's home he sent, And through the wood, where'er he went. The giant clad in that strange dress That took the soul with loveliness, To charm the fair Videhan's eyes With mingled wealth of mineral dyes, Moved onward, cropping in his way, The grass and grain and tender spray. His coat with drops of silver bright, A form to gaze on with delight, He raised his fair neck as he went To browse on bud and filament. Now in the Cassia grove he strayed, Now by the cot in plantains' shade. Slowly and slowly on he came To catch the glances of the dame, And the tall deer of splendid hue Shone full at length in Sítá's view. He roamed where'er his fancy chose Where Ráma's leafy cottage rose. Now near, now far, in careless ease, He came and went among the trees. Now with light feet he turned to fly, Now, reassured, again drew nigh:
- **Translation**: 

---

### Verse 17 (Ramayana 0.1002)
- **Original**: 984 The Ramayana Now gambolled close with leap and bound, Now lay upon the grassy ground: Now sought the door, devoid of fear, And mingled with the troop of deer; Led them a little way, and thence Again returned with confidence. Now flying far, now turning back Emboldened on his former track, Seeking to win the lady's glance He wandered through the green expanse. Then thronging round, the woodland deer Gazed on his form with wondering fear; A while they followed where he led, Then snuffed the tainted gale and fled. The giant, though he longed to slay The startled quarry, spared the prey, And mindful of the shape he wore To veil his nature, still forbore. Then Sítá of the glorious eye, Returning from her task drew nigh; For she had sought the wood to bring Each loveliest flower of early spring. Now would the bright-eyed lady choose Some gorgeous bud with blending hues, Now plucked the mango's spray, and now The bloom from an A[oka bough. She with her beauteous form, unmeet For woodland life and lone retreat, That wondrous dappled deer beheld Gemmed with rich pearls, unparalleled, His silver hair the lady saw, His radiant teeth and lips and jaw, And gazed with rapture as her eyes Expanded in their glad surprise.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1003)
- **Original**: Canto XLIII. The Wondrous Deer. 985 And when the false deer's glances fell On her whom Ráma loved so well, He wandered here and there, and cast A luminous beauty as he passed; And Janak's child with strange delight Kept gazing on the unwonted sight. Canto XLIII. The Wondrous Deer. She stooped, her hands with flowers to fill, But gazed upon the marvel still: Gazed on its back and sparkling side Where silver hues with golden vied. Joyous was she of faultless mould, With glossy skin like polished gold. And loudly to her husband cried And bow-armed LakshmaG by his side: Again, again she called in glee: “O come this glorious creature see; Quick, quick, my lord, this deer to view. And bring thy brother LakshmaG too.” As through the wood her clear tones rang, Swift to her side the brothers sprang. With eager eyes the grove they scanned, And saw the deer before them stand. But doubt was strong in LakshmaG's breast, Who thus his thought and fear expressed:
- **Translation**: 

---

### Verse 19 (Ramayana 0.1004)
- **Original**: 986 The Ramayana “Stay, for the wondrous deer we see The fiend Márícha's self may be. Ere now have kings who sought this place To take their pastime in the chase, Met from his wicked art defeat, And fallen slain by like deceit. He wears, well trained in magic guile, The figure of a deer a while, Bright as the very sun, or place Where dwell the gay Gandharva race. No deer, O Ráma, e'er was seen Thus decked with gold and jewels' sheen. 'Tis magic, for the world has ne'er, Lord of the world, shown aught so fair.” But Sítá of the lovely smile, A captive to the giant's wile, Turned LakshmaG's prudent speech aside And thus with eager words replied: “My honoured lord, this deer I see With beauty rare enraptures me. Go, chief of mighty arm, and bring For my delight this precious thing. Fair creatures of the woodland roam Untroubled near our hermit home. The forest cow and stag are there, The fawn, the monkey, and the bear, Where spotted deer delight to play,[279] And strong and beauteous Kinnars494 stray. But never, as they wandered by, Has such a beauty charmed mine eye As this with limbs so fair and slight, 494 A race of beings of human shape but with the heads of horses, like centaurs reversed.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1005)
- **Original**: Canto XLIII. The Wondrous Deer. 987 So gentle, beautiful and bright. O see, how fair it is to view With jewels of each varied hue: Bright as the rising moon it glows, Lighting the wood where'er it goes. Ah me, what form and grace are there! Its limbs how fine, its hues how fair! Transcending all that words express, It takes my soul with loveliness. O, if thou would, to please me, strive To take the beauteous thing alive, How thou wouldst gaze with wondering eyes Delighted on the lovely prize! And when our woodland life is o'er, And we enjoy our realm once more, The wondrous animal will grace The chambers of my dwelling-place, And a dear treasure will it be To Bharat and the queens and me, And all with rapture and amaze Upon its heavenly form will gaze. But if the beauteous deer, pursued, Thine arts to take it still elude, Strike it, O chieftain, and the skin Will be a treasure, laid within. O, how I long my time to pass Sitting upon the tender grass, With that soft fell beneath me spread Bright with its hair of golden thread! This strong desire, this eager will, Befits a gentle lady ill: But when I first beheld, its look My breast with fascination took. See, golden hair its flank adorns,
- **Translation**: 

---



--- End of Ramayan_batch_148.md ---


--- Start of Ramayan_batch_149.md ---

# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Ramayana 0.1006)
- **Original**: 988 The Ramayana And sapphires tip its branching horns. Resplendent as the lunar way, Or the first blush of opening day, With graceful form and radiant hue It charmed thy heart, O chieftain, too.” He heard her speech with willing ear, He looked again upon the deer. Its lovely shape his breast beguiled Moved by the prayer of Janak's child, And yielding for her pleasure's sake, To LakshmaG Ráma turned and spake: “Mark, LakshmaG, mark how Sítá's breast With eager longing is possessed. To-day this deer of wondrous breed Must for his passing beauty bleed, Brighter than e'er in Nandan strayed, Or Chaitraratha's heavenly shade. How should the groves of earth possess Such all-surpassing loveliness! The hair lies smooth and bright and fine, Or waves upon each curving line, And drops of living gold bedeck The beauty of his side and neck. O look, his crimson tongue between His teeth like flaming fire is seen, Flashing, whene'er his lips he parts, As from a cloud the lightning darts. O see his sunlike forehead shine With emerald tints and almandine, While pearly light and roseate glow Of shells adorn his neck below. No eye on such a deer can rest
- **Translation**: 

---

### Verse 2 (Ramayana 0.1007)
- **Original**: Canto XLIII. The Wondrous Deer. 989 But soft enchantment takes the breast: No man so fair a thing behold Ablaze with light of radiant gold, Celestial, bright with jewels' sheen, Nor marvel when his eyes have seen. A king equipped with bow and shaft Delights in gentle forest craft, And as in boundless woods he strays The quarry for the venison slays. There as he wanders with his train A store of wealth he oft may gain. He claims by right the precious ore, He claims the jewels' sparkling store. Such gains are dearer in his eyes Than wealth that in his chamber lies, The dearest things his spirit knows, Dear as the bliss whichZukra chose. But oft the rich expected gain Which heedless men pursue in vain, The sage, who prudent counsels know, Explain and in a moment show. This best of deer, this gem of all, To yield his precious spoils must fall, And tender Sítá by my side Shall sit upon the golden hide. Ne'er could I find so rich a coat On spotted deer or sheep or goat. No buck or antelope has such, So bright to view, so soft to touch. This radiant deer and one on high That moves in glory through the sky, Alike in heavenly beauty are, One on the earth and one a star. But, brother, if thy fears be true,
- **Translation**: 

---

### Verse 3 (Ramayana 0.1008)
- **Original**: 990 The Ramayana And this bright creature that we view Be fierce Márícha in disguise, Then by this hand he surely dies. For that dire fiend who spurns control With bloody hand and cruel soul, Has roamed this forest and dismayed The holiest saints who haunt the shade. Great archers, sprung of royal race, Pursuing in the wood the chase, Have fallen by his wicked art, And now my shaft shall strike his heart. Vatápi, by his magic power[280] Made heedless saints his flesh devour, Then, from within their frames he rent Forth bursting from imprisonment. But once his art in senseless pride Upon the mightiest saint he tried, Agastya's self, and caused him taste The baited meal before him placed. Vátápi, when the rite was o'er, Would take the giant form he wore, But Saint Agastya knew his wile And checked the giant with smile. “Vátápi, thou with cruel spite Hast conquered many an anchorite The noblest of the Bráhman caste,— And now thy ruin comes at last.” Now if my power he thus defies, This giant, like Vátápi dies, Daring to scorn a man like me, A self subduing devotee. Yea, as Agastya slew the foe, My hand shall lay Márícha low Clad in thine arms thy bow in hand,
- **Translation**: 

---

### Verse 4 (Ramayana 0.1009)
- **Original**: Canto XLIV. Márícha's Death. 991 To guard the Maithil lady stand, With watchful eye and thoughtful breast Keeping each word of my behest I go, and hunting through the brake This wondrous deer will bring or take. Yea surely I will bring the spoil Returning from my hunter's toil See, LakshmaG how my consort's eyes Are longing for the lovely prize. This day it falls, that I may win The treasure of so fair a skin. Do thou and Sítá watch with care Lest danger seize you unaware. Swift from my bow one shaft will fly; The stricken deer will fall and die Then quickly will I strip the game And bring the trophy to my dame. Jamáyus, guardian good and wise, Our old and faithful friend, The best and strongest bird that flies, His willing aid will lend The Maithil lady well protect, For every chance provide, And in thy tender care suspect A foe on every side.” Canto XLIV. Márícha's Death.
- **Translation**: 

---

### Verse 5 (Ramayana 0.1010)
- **Original**: 992 The Ramayana Thus having warned his brother bold He grasped his sword with haft of gold, And bow with triple flexure bent, His own delight and ornament; Then bound two quivers to his side, And hurried forth with eager stride. Soon as the antlered monarch saw The lord of monarchs near him draw, A while with trembling heart he fled, Then turned and showed his stately head. With sword and bow the chief pursued Where'er the fleeing deer he viewed Sending from dell and lone recess The splendour of his loveliness. Now full in view the creature stood Now vanished in the depth of wood; Now running with a languid flight, Now like a meteor lost to sight. With trembling limbs away he sped; Then like the moon with clouds o'erspread Gleamed for a moment bright between The trees, and was again unseen. Thus in the magic deer's disguise Márícha lured him to the prize, And seen a while, then lost to view, Far from his cot the hero drew. Still by the flying game deceived The hunter's heart was wroth and grieved, And wearied with the fruitless chase He stayed him in a shady place. Again the rover of the night Enraged the chieftain, full in sight, Slow moving in the coppice near, Surrounded by the woodland deer.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1011)
- **Original**: Canto XLIV. Márícha's Death. 993 Again the hunter sought the game That seemed a while to court his aim: But seized again with sudden dread, Beyond his sight the creature fled. Again the hero left the shade, Again the deer before him strayed. With surer hope and stronger will The hunter longed his prey to kill. Then as his soul impatient grew, An arrow from his side he drew, Resplendent at the sunbeam's glow, The crusher of the smitten foe. With skillful heed the mighty lord Fixed well shaft and strained the cord. Upon the deer his eyes he bent, And like a fiery serpent went The arrow Brahma's self had framed, Alive with sparks that hissed and flamed, Like Indra's flashing levin, true To the false deer the missile flew Cleaving his flesh that wonderous dart Stood quivering in Márícha's heart. Scarce from the ground one foot he sprang, Then stricken fell with deadly pang. Half lifeless, as he pressed the ground, He gave a roar of awful sound And ere the wounded giant died He threw his borrowed form aside Remembering still his lord's behest He pondered in his heart how best Sítá might send her guard away, And RávaG seize the helpless prey. The monster knew the time was nigh, And called aloud with eager cry,
- **Translation**: 

---

### Verse 7 (Ramayana 0.1012)
- **Original**: 994 The Ramayana “Ho, Sítá, LakshmaG” and the tone[281] He borrowed was like Ráma's own. So by that matchless arrow cleft, The deer's bright form Márícha left, Resumed his giant shape and size And closed in death his languid eyes. When Ráma saw his awful foe Gasp, smeared with blood, in deadly throe, His anxious thoughts to Sítá sped, And the wise words that LakshmaG said, That this was false Márícha's art, Returned again upon his heart. He knew the foe he triumphed o'er The name of great Márícha bore. “The fiend,” he pondered, 'ere he died, “Ho, LakshmaG! ho, my Sítá!” cried Ah, if that cry has reached her ear, How dire must be my darling's fear! And Lakshma G of the mighty arm, What thinks he in his wild alarm? As thus he thought in sad surmise, Each startled hair began to rise, And when he saw the giant slain And thought upon that cry again, His spirit sank and terror pressed Full sorely on the hero's breast. Another deer he chased and struck, He bore away the the fallen buck, To Janasthán then turned his face And hastened to his dwelling place.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1013)
- **Original**: Canto XLV. Lakshman's Departure. 995 Canto XLV. Lakshman's Departure. But Sítá hearing as she thought, Her husband's cry with anguish fraught, Called to her guardian,“Lakshma G, run And in the wood seek Raghu's son. Scarce can my heart retain its throne, Scarce can my life be called mine own, As all my powers and senses fail At that long, loud and bitter wail. Haste to the wood with all thy speed And save thy brother in his need. Go, save him in the distant glade Where loud he calls, for timely aid. He falls beneath some giant foe— A bull whom lions overthrow.” Deaf to her prayer, no step he stirred Obedient to his mother's word, Then Janak's child, with ire inflamed, In words of bitter scorn exclaimed exclaimed “Sumitrá's son, a friend in show, Thou art in truth thy brother's foe, Who canst at such any hour deny Thy succour and neglect his cry. Yes, LakshmaG, smit with love of me Thy brother's death thou fain wouldst see. This guilty love thy heart has swayed And makes thy feet so loth to aid. Thou hast no love for Ráma, no: Thy joy is vice, thy thoughts are low Hence thus unmoved thou yet canst stay While my dear lord is far away.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1014)
- **Original**: 996 The Ramayana If aught of ill my lord betide Who led thee here, thy chief and guide, Ah, what will be my hapless fate Left in the wild wood desolate!” Thus spoke the lady sad with fear, With many a sigh and many a tear, Still trembling like a captured doe: And Lakshma G spoke to calm her woe: “Videhan Queen, be sure of this,— And at the thought thy fear dismiss,— Thy husband's mightier power defies All Gods and angels of the skies, Gandharvas, and the sons of light, Serpents, and rovers of the night. I tell thee, of the sons of earth, Of Gods who boast celestial birth, Of beasts and birds and giant hosts, Of demigods, Gandharvas, ghosts, Of awful fiends, O thou most fair, There lives not one whose heart would dare To meet thy Ráma in the fight, Like Indra's self unmatched in might. Such idle words thou must not say Thy Ráma lives whom none may slay. I will not, cannot leave thee here In the wild wood till he be near. The mightiest strength can ne'er withstand His eager force, his vigorous hand. No, not the triple world allied With all the immortal Gods beside. Dismiss thy fear, again take heart, Let all thy doubt and woe depart.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1015)
- **Original**: Canto XLV. Lakshman's Departure. 997 Thy lord, be sure, will soon be here And bring thee back that best of deer. Not his, not his that mournful cry, Nor haply came it from the sky. Some giant's art was busy there And framed a castle based on air. A precious pledge art thou, consigned To me by him of noblest mind, Nor can I fairest dame, forsake The pledge which Ráma bade me take. Upon our heads, O Queen, we drew The giants' hate when Ráma slew Their chieftain Khara, and the shade Of Janasthán in ruin laid. Through all this mighty wood they rove With varied cries from grove to grove On rapine bent they wander here: But O, dismiss thy causeless fear.” Bright flashed her eye as LakshmaG spoke And forth her words of fury broke Upon her truthful guardian, flung With bitter taunts that pierced and stung: “Shame on such false compassion, base Defiler of thy glorious race! 'Twere joyous sight I ween to thee [282] My lord in direst strait to see. Thou knowest Ráma sore bested, Or word like this thou ne'er hadst said. No marvel if we find such sin In rivals false to kith and kin. Wretches like thee of evil kind, Concealing crime with crafty mind. Thou, wretch, thine aid wilt still deny,
- **Translation**: 

---

### Verse 11 (Ramayana 0.1016)
- **Original**: 998 The Ramayana And leave my lord alone to die. Has love of me unnerved thy hand, Or Bharat's art this ruin planned? But be the treachery his or thine, In vain, in vain the base design. For how shall I, the chosen bride Of dark-hued Ráma, lotus-eyed, The queen who once called Ráma mine, To love of other men decline? Believe me, LakshmaG, Ráma's wife Before thine eyes will quit this life, And not a moment will she stay If her dear lord have passed away.” The lady's bitter speech, that stirred Each hair upon his frame, he heard. With lifted hands together laid, His calm reply he gently made: “No words have I to answer now: My deity, O Queen, art thou. But 'tis no marvel, dame, to find Such lack of sense in womankind. Throughout this world, O Maithil dame, Weak women's hearts are still the same. Inconstant, urged by envious spite, They sever friends and hate the right. I cannot brook, Videhan Queen, Thy words intolerably keen. Mine ears thy fierce reproaches pain As boiling water seethes the brain. And now to bear me witness all The dwellers in the wood I call, That, when with words of truth I plead,
- **Translation**: 

---

### Verse 12 (Ramayana 0.1017)
- **Original**: Canto XLV. Lakshman's Departure. 999 This harsh reply is all my meed. Ah, woe is thee! Ah, grief, that still Eager to do my brother's will, Mourning thy woman's nature, I Must see thee doubt my truth and die. I fly to Ráma's side, and Oh, May bliss attend thee while I go! May all attendant wood-gods screen Thy head from harm, O large-eyed Queen! And though dire omens meet my sight And fill my soul with wild affright, May I return in peace and see The son of Raghu safe with thee!” The child of Janak heard him speak, And the hot tear-drops down her cheek, Increasing to a torrent, ran, As thus once more the dame began: “O Lakshma G, if I widowed be Godávarí's flood shall cover me, Or I will die by cord, or leap, Life weary, from yon rocky steep; Or deadly poison will I drink, Or 'neath the kindled flames will sink, But never, reft of Ráma, can Consent to touch a meaner man.” The Maithil dame with many sighs, And torrents pouring from her eyes, The faithful LakshmaG thus addressed, And smote her hands upon her breast. >Sumitrá's son, o'erwhelmed by fears, Looked on the large-eyed queen: He saw that flood of burning tears,
- **Translation**: 

---

### Verse 13 (Ramayana 0.1018)
- **Original**: 1000 The Ramayana He saw that piteous mien. He yearned sweet comfort to afford, He strove to soothe her pain; But to the brother of her lord She spoke no word again. His reverent hands once more he raised, His head he slightly bent, Upon her face he sadly gazed, And then toward Ráma went. Canto XLVI. The Guest. The angry LakshmaG scarce could brook Her bitter words, her furious look. With dark forebodings in his breast To Ráma's side he quickly pressed. Then ten necked RávaG saw the time Propitious for his purposed crime. A mendicant in guise he came And stood before the Maithil dame. His garb was red, with tufted hair And sandalled feet a shade he bare, And from the fiend's left shoulder slung A staff and water-vessel hung. Near to the lovely dame he drew, While both the chiefs were far from view, As darkness takes the evening air When neither sun nor moon is there. He bent his eye upon the dame, A princess fair, of spotless fame:
- **Translation**: 

---

### Verse 14 (Ramayana 0.1019)
- **Original**: Canto XLVI. The Guest. 1001 So might some baleful planet be Near Moon-forsaken RohiGí.495 As the fierce tyrant nearer drew, The trees in Janasthán that grew Waved not a leaf for fear and woe, And the hushed wind forbore to blow. Godávarí's waters as they fled, Saw his fierce eye-balls flashing red, And from each swiftly-gliding wave A melancholy murmur gave. Then RávaG, when his eager eye Beheld the longed-for moment nigh, In mendicant's apparel dressed Near to the Maithil lady pressed. [283] In holy guise, a fiend abhorred, He found her mourning for her lord. Thus threatening drawsZani[char496 nigh To Chitrá497 in the evening sky; Thus the deep well by grass concealed Yawns treacherous in the verdant field. He stood and looked upon the dame Of Ráma, queen of spotless fame With her bright teeth and each fair limb Like the full moon she seemed to him, Sitting within her leafy cot, Weeping for woe that left her not. Thus, while with joy his pulses beat, He saw her in her lone retreat, Eyed like the lotus, fair to view In silken robes of amber hue. Pierced to the core by Káma's dart 495 The favourite wife of the Moon. 496 The planet Saturn. 497 Another favourite of the Moon; one of the lunar mansions.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1020)
- **Original**: 1002 The Ramayana He murmured texts with lying art, And questioned with a soft address The lady in her loneliness. The fiend essayed with gentle speech The heart of that fair dame to reach, Pride of the worlds, like Beauty's Queen Without her darling lotus seen: “O thou whose silken robes enfold A form more fair than finest gold, With lotus garland on thy head, Like a sweet spring with bloom o'erspread, Who art thou, fair one, what thy name, Beauty, or Honour, Fortune, Fame, Spirit, or nymph, or Queen of love Descended from thy home above? Bright as the dazzling jasmine shine Thy small square teeth in level line. Like two black stars aglow with light Thine eyes are large and pure and bright. Thy charms of smile and teeth and hair And winning eyes, O thou most fair, Steal all my spirit, as the flow Of rivers mines the bank below. How bright, how fine each flowing tress! How firm those orbs beneath thy dress! That dainty waist with ease were spanned, Sweet lady, by a lover's hand. Mine eyes, O beauty, ne'er have seen Goddess or nymph so fair of mien, Or bright Gandharva's heavenly dame, Or woman of so perfect frame. In youth's soft prime thy years are few, And earth has naught so fair to view.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1021)
- **Original**: Canto XLVI. The Guest. 1003 I marvel one like thee in face Should make the woods her dwelling-place. Leave, lady, leave this lone retreat In forest wilds for thee unmeet, Where giants fierce and strong assume All shapes and wander in the gloom. These dainty feet were formed to tread Some palace floor with carpets spread, Or wander in trim gardens where Each opening bud perfumes the air. The richest robe thy form should deck, The rarest gems adorn thy neck, The sweetest wreath should bind thy hair, The noblest lord thy bed should share. Art thou akin, O fair of form, To Rudras,498 or the Gods of storm,499 Or to the glorious Vasus500? How Can less than these be bright as thou? But never nymph or heavenly maid Or Goddess haunts this gloomy shade. Here giants roam, a savage race; What led thee to so dire a place? Here monkeys leap from tree to tree, And bears and tigers wander free; Here ravening lions prowl, and fell Hyenas in the thickets yell, And elephants infuriate roam, Mighty and fierce, their woodland home. Dost thou not dread, so soft and fair, Tiger and lion, wolf and bear? 498 The Rudras, agents in creation, are eight in number; they sprang from the forehead of Brahmá. 499 Maruts, the attendants of Indra. 500 Radiant demi-gods.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1022)
- **Original**: 1004 The Ramayana Hast thou, O beauteous dame, no fear In the wild wood so lone and drear? Whose and who art thou? whence and why Sweet lady, with no guardian nigh, Dost thou this awful forest tread By giant bands inhabited?” The praise the high-souled RávaG spoke No doubt within her bosom woke. His saintly look and Bráhman guise Deceived the lady's trusting eyes. With due attention on the guest Her hospitable rites she pressed. She bade the stranger to a seat, And gave him water for his feet. The bowl and water-pot he bare, And garb which wandering Bráhmans wear Forbade a doubt to rise. Won by his holy look she deemed The stranger even as he seemed To her deluded eyes. Intent on hospitable care, She brought her best of woodland fare, And showed her guest a seat. She bade the saintly stranger lave His feet in water which she gave, And sit and rest and eat. He kept his eager glances bent On her so kindly eloquent, Wife of the noblest king; And longed in heart to steal her thence, Preparing by the dire offence, Death on his head to bring.[284]
- **Translation**: 

---

### Verse 18 (Ramayana 0.1023)
- **Original**: Canto XLVII. Rávan's Wooing. 1005 The lady watched with anxious face For Ráma coming from the chase With LakshmaG by his side: But nothing met her wandering glance Save the wild forest's green expanse Extending far and wide. Canto XLVII. Rávan's Wooing. As, clad in mendicant's disguise, He questioned thus his destined prize, She to the seeming saintly man The story of her life began. “My guest is he,” she thought,“and I, To 'scape his curse, must needs reply:” “Child of a noble sire I spring From Janak, fair Videha's king. May every good be thine! my name Is Sítá, Ráma's cherished dame. Twelve winters with my lord I spent Most happily with sweet content In the rich home of Raghu's line, And every earthly joy was mine. Twelve pleasant years flew by, and then His peers advised the king of men, Ráma, my lord, to consecrate Joint ruler of his ancient state. But when the rites were scarce begun, To consecrate Ikshváku's son, The queen Kaikeyí, honoured dame, Sought of her lord an ancient claim.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1024)
- **Original**: 1006 The Ramayana Her plea of former service pressed, And made him grant her new request, To banish Ráma to the wild And consecrate instead her child. This double prayer on him, the best And truest king, she strongly pressed: “Mine eyes in sleep I will not close, Nor eat, nor drink, nor take repose. This very day my death shall bring If Ráma be anointed king.” As thus she spake in envious ire, The aged king, my husband's sire, Besought with fitting words; but she Was cold and deaf to every plea. As yet my days are few; eighteen The years of life that I have seen; And Ráma, best of all alive, Has passed of years a score and five— Ráma the great and gentle, through All region famed as pure and true, Large-eyed and mighty-armed and tall, With tender heart that cares for all. But Da[aratha, led astray By woman's wile and passion's sway, By his strong love of her impelled, The consecrating rites withheld. When, hopeful of the promised grace, My Ráma sought his father's face, The queen Kaikeyí, ill at ease, Spoke to my lord brief words like these: “Hear, son of Raghu, hear from me The words thy father says to thee: “I yield this day to Bharat's hand, Free from all foes, this ancient land.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1025)
- **Original**: Canto XLVII. Rávan's Wooing. 1007 Fly from this home no longer thine, And dwell in woods five years and nine. Live in the forest and maintain Mine honour pure from falsehood's stain.’ ” Then Ráma spoke, untouched by dread: “Yea, it shall be as thou hast said.” And answered, faithful to his vows, Obeying Da[aratha's spouse: “The offered realm I would not take, But still keep true the words he spake.” Thus, gentle Bráhman, Ráma still Clung to his vow with firmest will. And valiant LakshmaG, dear to fame, His brother by a younger dame, Bold victor in the deadly fray, Would follow Ráma on his way. On sternest vows his heart was set, And he, a youthful anchoret, Bound up in twisted coil his hair And took the garb which hermits wear; Then with his bow to guard us, he Went forth with Ráma and with me. By Queen Kaikeyí's art bereft The kingdom and our home we left, And bound by stern religious vows We sought this shade of forest boughs. Now, best of Bráhmans, here we tread These pathless regions dark and dread. But come, refresh thy soul, and rest Here for a while an honoured guest, For he, my lord, will soon be here With fresh supply of woodland cheer, Large store of venison of the buck, Or some great boar his hand has struck.
- **Translation**: 

---



--- End of Ramayan_batch_149.md ---


--- Start of Ramayan_batch_150.md ---

# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Ramayana 0.1026)
- **Original**: 1008 The Ramayana Meanwhile, O stranger, grant my prayer: Thy name, thy race, thy birth declare, And why with no companion thou Roamest in DaG ak forest now.” Thus questioned Sítá, Ráma's dame. Then fierce the stranger's answer came: “Lord of the giant legions, he From whom celestial armies flee,— The dread of hell and earth and sky, RávaG the Rákshas king am I. Now when thy gold-like form I view Arrayed in silks of amber hue, My love, O thou of perfect mould, For all my dames is dead and cold. A thousand fairest women, torn From many a land my home adorn. But come, loveliest lady, be The queen of every dame and me. My city Lanká, glorious town, Looks from a mountain's forehead down[285] Where ocean with his flash and foam Beats madly on mine island home. With me, O Sítá, shalt thou rove Delighted through each shady grove, Nor shall thy happy breast retain Fond memory of this life of pain. In gay attire, a glittering band, Five thousand maids shall round thee stand, And serve thee at thy beck and sign, If thou, fair Sítá, wilt be mine.”
- **Translation**: 

---

### Verse 2 (Ramayana 0.1027)
- **Original**: Canto XLVII. Rávan's Wooing. 1009 Then forth her noble passion broke As thus in turn the lady spoke: “Me, me the wife of Ráma, him The lion lord with lion's limb, Strong as the sea, firm as the rock, Like Indra in the battle shock. The lord of each auspicious sign, The glory of his princely line, Like some fair Bodh tree strong and tall, The noblest and the best of all, Ráma, the heir of happy fate Who keeps his word inviolate, Lord of the lion gait, possessed Of mighty arm and ample chest, Ráma the lion-warrior, him Whose moon bright face no fear can dim, Ráma, his bridled passions' lord, The darling whom his sire adored,— Me, me the true and loving dame Of Ráma, prince of deathless fame— Me wouldst thou vainly woo and press? A jackal woo a lioness! Steal from the sun his glory! such Thy hope Lord Ráma's wife to touch. Ha! Thou hast seen the trees of gold, The sign which dying eyes behold, Thus seeking, weary of thy life, To win the love of Ráma's wife. Fool! wilt thou dare to rend away The famished lion's bleeding prey, Or from the threatening jaws to take The fang of some envenomed snake? What, wouldst thou shake with puny hand
- **Translation**: 

---

### Verse 3 (Ramayana 0.1028)
- **Original**: 1010 The Ramayana Mount Mandar,501 towering o'er the land, Put poison to thy lips and think The deadly cup a harmless drink? With pointed needle touch thine eye, A razor to thy tongue apply, Who wouldst pollute with impious touch The wife whom Ráma loves so much? Be round thy neck a millstone tied, And swim the sea from side to side; Or raising both thy hands on high Pluck sun and moon from yonder sky; Or let the kindled flame be pressed, Wrapt in thy garment, to thy breast; More wild the thought that seeks to win Ráma's dear wife who knows not sin. The fool who thinks with idle aim To gain the love of Ráma's dame, With dark and desperate footing makes His way o'er points of iron stakes. As Ocean to a bubbling spring, The lion to a fox, the king Of all the birds that ply the wing To an ignoble crow As gold to lead of little price, As to the drainings of the rice The drink they quaff in Paradise, The Amrit's heavenly flow, As sandal dust with perfume sweet Is to the mire that soils our feet, A tiger to a cat, As the white swan is to the owl, The peacock to the waterfowl, 501 The mountain which was used by the Gods as a churning stick at the Churning of the Ocean.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1029)
- **Original**: Canto XLVIII. Rávan's Speech. 1011 An eagle to a bat, Such is my lord compared with thee; And when with bow and arrows he, Mighty as Indra's self shall see His foeman, armed to slay, Thou, death-doomed like the fly that sips The oil that on the altar drips, Shalt cast the morsel from thy lips And lose thy half-won prey.” Thus in high scorn the lady flung The biting arrows of her tongue In bitter words that pierced and stung The rover of the night. She ceased. Her gentle cheek grew pale, Her loosened limbs began to fail, And like a plantain in the gale She trembled with affright. He terrible as Death stood nigh, And watched with fierce exulting eye The fear that shook her frame. To terrify the lady more, He counted all his triumphs o'er, Proclaimed the titles that he bore, His pedigree and name. Canto XLVIII. Rávan's Speech. With knitted brow and furious eye The stranger made his fierce reply: “In me O fairest dame, behold The brother of the King of Gold.
- **Translation**: 

---

### Verse 5 (Ramayana 0.1030)
- **Original**: 1012 The Ramayana The Lord of Ten Necks my title, named RávaG, for might and valour famed. Gods and Gandharva hosts I scare; Snakes, spirits, birds that roam the air Fly from my coming, wild with fear, Trembling like men when Death is near. Vai[ravaG once, my brother, wrought To ire, encountered me and fought,[286] But yielding to superior might Fled from his home in sore affright. Lord of the man-drawn chariot, still He dwells on famed Kailása's hill. I made the vanquished king resign The glorious car which now is mine,— Pushpak, the far-renowned, that flies Will-guided through the buxom skies. Celestial hosts by Indra led Flee from my face disquieted, And where my dreaded feet appear The wind is hushed or breathless is fear. Where'er I stand, where'er I go The troubled waters cease to flow, Each spell-bound wave is mute and still And the fierce sun himself is chill. Beyond the sea my Lanká stands Filled with fierce forms and giant bands, A glorious city fair to see As Indra's Amarávatí. A towering height of solid wall, Flashing afar, surrounds it all, Its golden courts enchant the sight, And gates aglow with lazulite. Steeds, elephants, and cars are there, And drums' loud music fills the air,
- **Translation**: 

---

### Verse 6 (Ramayana 0.1031)
- **Original**: Canto XLVIII. Rávan's Speech. 1013 Fair trees in lovely gardens grow Whose boughs with varied fruitage glow. Thou, beauteous Queen, with me shalt dwell In halls that suit a princess well, Thy former fellows shall forget Nor think of women with regret, No earthly joy thy soul shall miss, And take its fill of heavenly bliss. Of mortal Ráma think no more, Whose terms of days will soon be o'er. King Da[aratha looked in scorn On Ráma though the eldest born, Sent to the woods the weakling fool, And set his darling son to rule. What, O thou large-eyed dame, hast thou To do with fallen Ráma now, From home and kingdom forced to fly, A wretched hermit soon to die? Accept thy lover, nor refuse The giant king who fondly woos. O listen, nor reject in scorn A heart by Káma's arrows torn. If thou refuse to hear my prayer, Of grief and coming woe beware; For the sad fate will fall on thee Which came on hapless Urva[í, When with her foot she chanced to touch Purúravas, and sorrowed much.502. My little finger raised in fight Were more than match for Ráma's might. O fairest, blithe and happy be With him whom fortune sends to thee.” 502 The story will be found in GARRETT 'S{FNS Classical Dictionary. See A DDITIONAL N OTES {FNS
- **Translation**: 

---

### Verse 7 (Ramayana 0.1032)
- **Original**: 1014 The Ramayana Such were the words the giant said, And Sítá's angry eyes were red. She answered in that lonely place The monarch of the giant race: “Art thou the brother of the Lord Of Gold by all the world adored, And sprung of that illustrious seed Wouldst now attempt this evil deed? I tell thee, impious Monarch, all The giants by thy sin will fall, Whose reckless lord and king thou art, With foolish mind and lawless heart. Yea, one may hope to steal the wife Of Indra and escape with life. But he who Ráma's dame would tear From his loved side must needs despair. Yea, one may steal fairZachí, dame Of Him who shoots the thunder flame, May live successful in his aim And length of day may see; But hope, O giant King, in vain, Though cups of Amrit thou may drain, To shun the penalty and pain Of wronging one like me.” Canto XLIX. The Rape Of Sítá.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1033)
- **Original**: Canto XLIX. The Rape Of Sítá. 1015 The Rákshas monarch, thus addressed, His hands a while together pressed, And straight before her startled eyes Stood monstrous in his giant size. Then to the lady, with the lore Of eloquence, he spoke once more: “Thou scarce,” he cried,“hast heard aright The glories of my power and might. I borne sublime in air can stand And with these arms upheave the land, Drink the deep flood of Ocean dry And Death with conquering force defy, Pierce the great sun with furious dart And to her depths cleave earth apart. See, thou whom love and beauty blind, I wear each form as wills my mind.” As thus he spake in burning ire His glowing eyes were red with fire. His gentle garb aside was thrown And all his native shape was shown. Terrific, monstrous, wild, and dread As the dark God who rules the dead, His fiery eyes in fury rolled, His limbs were decked with glittering gold. Like some dark cloud the monster showed, And his fierce breast with fury glowed. The ten-faced rover of the night, With twenty arms exposed to sight, His saintly guise aside had laid And all his giant height displayed. [287] Attired in robes of crimson dye He stood and watched with angry eye The lady in her bright array
- **Translation**: 

---

### Verse 9 (Ramayana 0.1034)
- **Original**: 1016 The Ramayana Resplendent as the dawn of day When from the east the sunbeams break, And to the dark-haired lady spake: “If thou would call that lord thine own Whose fame in every world is known, Look kindly on my love, and be Bride of a consort meet for thee. With me let blissful years be spent, For ne'er thy choice shalt thou repent. No deed of mine shall e'er displease My darling as she lives at ease. Thy love for mortal man resign, And to a worthier lord incline. Ah foolish lady, seeming wise In thine own weak and partial eyes, By what fair graces art thou held To Ráma from his realm expelled? Misfortunes all his life attend, And his brief days are near their end. Unworthy prince, infirm of mind! A woman spoke and he resigned His home and kingdom and withdrew From troops of friends and retinue. And sought this forest dark and dread By savage beasts inhabited.” Thus RávaG urged the lady meet For love, whose words were soft and sweet. Near and more near the giant pressed As love's hot fire inflamed his breast. The leader of the giant crew His arm around the lady threw: Thus Budha503 with ill-omened might 503 Mercury: to be carefully distinguished from Buddha.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1035)
- **Original**: Canto XLIX. The Rape Of Sítá. 1017 Steals RohiGí's delicious light. One hand her glorious tresses grasped, One with its ruthless pressure clasped The body of his lovely prize, The Maithil dame with lotus eyes. The silvan Gods in wild alarm Marked his huge teeth and ponderous arm, And from that Death-like presence fled, Of mountain size and towering head. Then seen was RávaG's magic car Aglow with gold which blazed afar,— The mighty car which asses drew Thundering as it onward flew. He spared not harsh rebuke to chide The lady as she moaned and cried, Then with his arm about her waist His captive in the car he placed. In vain he threatened: long and shrill Rang out her lamentation still, O Ráma! which no fear could stay: But her dear lord was far away. Then rose the fiend, and toward the skies Bore his poor helpless struggling prize: Hurrying through the air above The dame who loathed his proffered love. So might a soaring eagle bear A serpent's consort through the air. As on he bore her through the sky She shrieked aloud her bitter cry. As when some wretch's lips complain In agony of maddening pain; “O Lakshma G, thou whose joy is still To do thine elder brother's will, This fiend, who all disguises wears,
- **Translation**: 

---

### Verse 11 (Ramayana 0.1036)
- **Original**: 1018 The Ramayana From Ráma's side his darling tears. Thou who couldst leave bliss, fortune, all, Yea life itself at duty's call, Dost thou not see this outrage done To hapless me, O Raghu's son? 'Tis thine, O victor of the foe, To bring the haughtiest spirit low, How canst thou such an outrage see And let the guilty fiend go free? Ah, seldom in a moment's time Comes bitter fruit of sin and crime, But in the day of harvest pain Comes like the ripening of the grain. So thou whom fate and folly lead To ruin for this guilty deed, Shalt die by Ráma's arm ere long A dreadful death for hideous wrong. Ah, too successful in their ends Are Queen Kaikeyí and her friends, When virtuous Ráma, dear to fame, Is mourning for his ravished dame. Ah me, ah me! a long farewell To lawn and glade and forest dell In Janasthán's wild region, where The Cassia trees are bright and fair With all your tongues to Ráma say That RávaG bears his wife away. Farewell, a long farewell to thee, O pleasant stream Godávarí, Whose rippling waves are ever stirred By many a glad wild water-bird! All ye to Ráma's ear relate The giant's deed and Sítá's fate. O all ye Gods who love this ground
- **Translation**: 

---

### Verse 12 (Ramayana 0.1037)
- **Original**: Canto XLIX. The Rape Of Sítá. 1019 Where trees of every leaf abound, Tell Ráma I am stolen hence, I pray you all with reverence. On all the living things beside That these dark boughs and coverts hide, Ye flocks of birds, ye troops of deer, I call on you my prayer to hear. All ye to Ráma's ear proclaim That RávaG tears away his dame With forceful arms,— his darling wife, Dearer to Ráma than his life. O, if he knew I dwelt in hell, My mighty lord, I know full well, Would bring me, conqueror, back to-day, Though Yáma's self reclaimed his prey.” Thus from the air the lady sent [288] With piteous voice her last lament, And as she wept she chanced to see The vulture on a lofty tree. As RávaG bore her swiftly by, On the dear bird she bent her eye, And with a voice which woe made faint Renewed to him her wild complaint: “O see, the king who rules the race Of giants, cruel, fierce and base, RávaG the spoiler bears me hence The helpless prey of violence. This fiend who roves in midnight shade By thee, dear bird, can ne'er be stayed, For he is armed and fierce and strong Triumphant in the power to wrong. For thee remains one only task,
- **Translation**: 

---

### Verse 13 (Ramayana 0.1038)
- **Original**: 1020 The Ramayana To do, kind friend, the thing I ask. To Ráma's ear by thee be borne How Sítá from her home is torn, And to the valiant LakshmaG tell The giant's deed and what befell.” Canto L. Jatáyus. The vulture from his slumber woke And heard the words which Sítá spoke He raised his eye and looked on her, Looked on her giant ravisher. That noblest bird with pointed beak, Majestic as a mountain peak, High on the tree addressed the king Of giants, wisely counselling: “O Ten-necked lord, I firmly hold To faith and laws ordained of old, And thou, my brother, shouldst refrain From guilty deeds that shame and stain. The vulture king supreme in air, Jamáyus is the name I bear. Thy captive, known by Sítá's name, Is the dear consort and the dame Of Ráma, Da[aratha's heir Who makes the good of all his care. Lord of the world in might he vies With the great Gods of seas and skies. The law he boasts to keep allows No king to touch another's spouse, And, more than all, a prince's dame
- **Translation**: 

---

### Verse 14 (Ramayana 0.1039)
- **Original**: Canto L. Jatáyus. 1021 High honour and respect may claim. Back to the earth thy way incline, Nor think of one who is not thine. Heroic souls should hold it shame To stoop to deeds which others blame, And all respect by them is shown To dames of others as their own. Not every case of bliss and gain The Scripture's holy texts explain, And subjects, when that light is dim, Look to their prince and follow him. The king is bliss and profit, he Is store of treasures fair to see, And all the people's fortunes spring, Their joy and misery, from the king. If, lord of giant race, thy mind Be fickle, false, to sin inclined, How wilt thou kingly place retain? High thrones in heaven no sinners gain. The soul which gentle passions sway Ne'er throws its nobler part away, Nor will the mansion of the base Long be the good man's dwelling-place. Prince Ráma, chief of high renown, Has wronged thee not in field or town. Ne'er has he sinned against thee: how Canst thou resolve to harm him now? If moved byZúrpaGakhá's prayer The giant Khara sought him there, And fighting fell with baffled aim, His and not Ráma's is the blame. Say, mighty lord of giants, say What fault on Ráma canst thou lay? What has the world's great master done
- **Translation**: 

---

### Verse 15 (Ramayana 0.1040)
- **Original**: 1022 The Ramayana That thou should steal his precious one? Quick, quick the Maithil dame release; Let Ráma's consort go in peace, Lest scorched by his terrific eye Beneath his wrath thou fall and die Like Vritra when Lord Indra threw The lightning flame that smote and slew. Ah fool, with blinded eyes to take Home to thy heart a venomed snake! Ah foolish eyes, too blind to see That Death's dire coils entangle thee! The prudent man his strength will spare, Nor lift a load too great to bear. Content is he with wholesome food Which gives him life and strength renewed, But who would dare the guilty deed That brings no fame or glorious meed, Where merit there is none to win And vengeance soon o'ertakes the sin? My course of life, Pulastya's son, For sixty thousand years has run. Lord of my kind I still maintain Mine old hereditary reign. I, worn by years, am older far Than thou, young lord of bow and car, In coat of glittering mail encased And armed with arrows at thy waist, But not unchallenged shalt thou go, Or steal the dame without a blow. Thou canst not, King, before mine eyes Bear off unchecked thy lovely prize, Safe as the truth of Scripture bent By no close logic's argument. Stay if thy courage let thee, stay
- **Translation**: 

---

### Verse 16 (Ramayana 0.1041)
- **Original**: Canto LI. The Combat. 1023 And meet me in the battle fray, And thou shalt stain the earth with gore Falling as Khara fell before. Soon Ráma, clothed in bark, shall smite [289] Thee, his proud foe, in deadly fight,— Ráma, from whom have oft times fled The Daitya hosts discomfited. No power have I to kill or slay: The princely youths are far away, But soon shalt thou with fearful eye Struck down beneath their arrows lie. But while I yet have life and sense, Thou shalt not, tyrant, carry hence Fair Sítá, Ramá's honoured queen, With lotus eyes and lovely mien. Whate'er the pain, whate'er the cost, Though in the struggle life be lost, The will of Raghu's noblest son And Da [aratha must be done. Stay for a while, O RávaG, stay, One hour thy flying car delay, And from that glorious chariot thou Shalt fall like fruit from shaken bough, For I to thee, while yet I live, The welcome of a foe will give.” Canto LI. The Combat.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1042)
- **Original**: 1024 The Ramayana RávaG's red eyes in fury rolled: Bright with his armlets' flashing gold, In high disdain, by passion stirred He rushed against the sovereign bird. With clash and din and furious blows Of murderous battle met the foes: Thus urged by winds two clouds on high Meet warring in the stormy sky. Then fierce the dreadful combat raged As fiend and bird in war engaged, As if two winged mountains sped To dire encounter overhead. Keen pointed arrows thick and fast, In never ceasing fury cast, Rained hurtling on the vulture king And smote him on the breast and wing. But still that noblest bird sustained The cloud of shafts which RávaG rained, And with strong beak and talons bent The body of his foeman rent. Then wild with rage the ten-necked king Laid ten swift arrows on his string,— Dread as the staff of Death were they, So terrible and keen to slay. Straight to his ear the string he drew, Straight to the mark the arrows flew, And pierced by every iron head The vulture's mangled body bled. One glance upon the car he bent Where Sítá wept with shrill lament, Then heedless of his wounds and pain Rushed at the giant king again. Then the brave vulture with the stroke Of his resistless talons broke
- **Translation**: 

---

### Verse 18 (Ramayana 0.1043)
- **Original**: Canto LI. The Combat. 1025 The giant's shafts and bow whereon The fairest pearls and jewels shone. The monster paused, by rage unmanned: A second bow soon armed his hand, Whence pointed arrows swift and true In hundreds, yea in thousands, flew. The monarch of the vultures, plied With ceaseless darts on every side, Showed like a bird that turns to rest Close covered by the branch-built nest. He shook his pinions to repel The storm of arrows as it fell; Then with his talons snapped in two The mighty bow which RávaG drew. Next with terrific wing he smote So fiercely on the giant's coat, The harness, glittering with the glow Of fire, gave way beneath the blow. With storm of murderous strokes he beat The harnessed asses strong and fleet,— Each with a goblin's monstrous face And plates of gold his neck to grace. Then on the car he turned his ire,— The will-moved car that shone like fire, And broke the glorious chariot, broke The golden steps and pole and yoke. The chouris and the silken shade Like the full moon to view displayed, Together with the guards who held Those emblems, to the ground he felled. The royal vulture hovered o'er The driver's head, and pierced and tore With his strong beak and dreaded claws His mangled brow and cheek and jaws.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1044)
- **Original**: 1026 The Ramayana With broken car and sundered bow, His charioteer and team laid low, One arm about the lady wound, Sprang the fierce giant to the ground. Spectators of the combat, all The spirits viewed the monster's fall: Lauding the vulture every one Cried with glad voice, Well done! well done! But weak with length of days, at last The vulture's strength was failing fast. The fiend again assayed to bear The lady through the fields of air. But when the vulture saw him rise Triumphant with his trembling prize, Bearing the sword that still was left When other arms were lost or cleft, Once more, impatient of repose, Swift from the earth her champion rose, Hung in the way the fiend would take, And thus addressing RávaG spake: “Thou, King of giants, rash and blind, Wilt be the ruin of thy kind, Stealing the wife of Ráma, him With lightning scars on chest and limb. A mighty host obeys his will And troops of slaves his palace fill;[290] His lords of state are wise and true, Kinsmen has he and retinue. As thirsty travellers drain the cup, Thou drinkest deadly poison up. The rash and careless fool who heeds No coming fruit of guilty deeds, A few short years of life shall see, And perish doomed to death like thee.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1045)
- **Original**: Canto LI. The Combat. 1027 Say whither wilt thou fly to loose Thy neck from Death's entangling noose, Caught like the fish that finds too late The hook beneath the treacherous bait? Never, O King— of this be sure— Will Raghu's fiery sons endure, Terrific in their vengeful rage, This insult to their hermitage. Thy guilty hands this day have done A deed which all reprove and shun, Unworthly of a noble chief, The pillage loved by coward thief. Stay, if thy heart allow thee, stay And meet me in the deadly fray. Soon shall thou stain the earth with gore, And fall as Khara fell before. The fruits of former deeds o'erpower The sinner in his dying hour: And such a fate on thee, O King, Thy tyranny and madness bring. Not e'en the Self-existent Lord, Who reigns by all the worlds adored, Would dare attempt a guilty deed Which the dire fruits of crime succeed.” Thus brave Jamáyus, best of birds, Addressed the fiend with moving words, Then ready for the swift attack Swooped down upon the giant's back. Down to the bone the talons went; With many a wound the flesh was rent: Such blows infuriate drivers deal Their elephants with pointed steel. Fixed in his back the strong beak lay,
- **Translation**: 

---



--- End of Ramayan_batch_150.md ---


--- Start of Ramayan_batch_151.md ---

# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Ramayana 0.1046)
- **Original**: 1028 The Ramayana The talons stripped the flesh away. He fought with claws and beak and wing, And tore the long hair of the king. Still as the royal vulture beat The giant with his wings and feet, Swelled the fiend's lips, his body shook With furious rage too great to brook. About the Maithil dame he cast One huge left arm and held her fast. In furious rage to frenzy fanned He struck the vulture with his hand. Jatáyus mocked the vain assay, And rent his ten left arms away. Down dropped the severed limbs: anew Ten others from his body grew: Thus bright with pearly radiance glide Dread serpents from the hillock side, Again in wrath the giant pressed The lady closer to his breast, And foot and fist sent blow on blow In ceaseless fury at the foe. So fierce and dire the battle, waged Between those mighty champions, raged: Here was the lord of giants, there The noblest of the birds of air. Thus, as his love of Ráma taught, The faithful vulture strove and fought. But RávaG seized his sword and smote His wings and side and feet and throat. At mangled side and wing he bled; He fell, and life was almost fled. The lady saw her champion lie, His plumes distained with gory dye, And hastened to the vulture's side
- **Translation**: 

---

### Verse 2 (Ramayana 0.1047)
- **Original**: Canto LII. Rávan's Flight. 1029 Grieving as though a kinsman died. The lord of Lanká's island viewed The vulture as he lay: Whose back like some dark cloud was hued, His breast a paly grey, Like ashes, when by none renewed, The flame has died away. The lady saw with mournful eye, Her champion press the plain,— The royal bird, her true ally Whom Ráva G's might had slain. Her soft arms locked in strict embrace Around his neck she kept, And lovely with her moon-bright face Bent o'er her friend and wept. Canto LII. Rávan's Flight. Fair as the lord of silvery rays Whom every star in heaven obeys, The Maithil dame her plaint renewed O'er him by RávaG's might subdued: “Dreams, omens, auguries foreshow Our coming lot of weal and woe: But thou, my Ráma, couldst not see The grievous blow which falls on thee. The birds and deer desert the brakes And show the path my captor takes, And thus e'en now this royal bird Flew to mine aid by pity stirred. Slain for my sake in death he lies,
- **Translation**: 

---

### Verse 3 (Ramayana 0.1048)
- **Original**: 1030 The Ramayana The broad-winged rover of the skies. O Ráma, haste, thine aid I crave: O Lakshma G, why delay to save? Brave sons of old Ikshváku, hear And rescue in this hour of fear.” Her flowery wreath was torn and rent, Crushed was each sparkling ornament. She with weak arms and trembling knees Clung like a creeper to the trees, And like some poor deserted thing With wild shrieks made the forest ring. But swift the giant reached her side,[291] As loud on Ráma's name she cried. Fierce as grim Death one hand he laid Upon her tresses' lovely braid. “That touch, thou impious King, shall be The ruin of thy race and thee.” The universal world in awe That outrage on the lady saw, All nature shook convulsed with dread, And darkness o'er the land was spread. The Lord of Day grew dark and chill, And every breath of air was still. The Eternal Father of the sky Beheld the crime with heavenly eye, And spake with solemn voice,“The deed, The deed is done, of old decreed.” Sad were the saints within the grove, But triumph with their sorrow strove. They wept to see the Maithil dame Endure the outrage, scorn, and shame: They joyed because his life should pay The penalty incurred that day.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1049)
- **Original**: Canto LII. Rávan's Flight. 1031 Then RávaG raised her up, and bare His captive through the fields of air, Calling with accents loud and shrill On Ráma and on LakshmaG still. With sparkling gems on arm and breast, In silk of paly amber dressed, High in the air the Maithil dame Gleamed like the lightning's flashing flame. The giant, as the breezes blew Upon her robes of amber hue, And round him twined that gay attire, Showed like a mountain girt with fire. The lady, fairest of the fair, Had wreathed a garland round her hair; Its lotus petals bright and sweet Rained down about the giant's feet. Her vesture, bright as burning gold, Gave to the wind each glittering fold, Fair as a gilded cloud that gleams Touched by the Day-God's tempered beams. Yet struggling in the fiend's embrace, The lady with her sweet pure face, Far from her lord, no longer wore The light of joy that shone before. Like some sad lily by the side Of waters which the sun has dried; Like the pale moon uprising through An autumn cloud of darkest hue, So was her perfect face between The arms of giant RávaG seen: Fair with the charm of braided tress And forehead's finished loveliness; Fair with the ivory teeth that shed White lustre through the lips' fine red,
- **Translation**: 

---

### Verse 5 (Ramayana 0.1050)
- **Original**: 1032 The Ramayana Fair as the lotus when the bud Is rising from the parent flood. With faultless lip and nose and eye, Dear as the moon that floods the sky With gentle light, of perfect mould, She seemed a thing of burnished gold, Though on her cheek the traces lay Of tears her hand had brushed away. But as the moon-beams swiftly fade Ere the great Day-God shines displayed, So in that form of perfect grace Still trembling in the fiend's embrace, From her beloved Ráma reft, No light of pride or joy was left. The lady with her golden hue O'er the swart fiend a lustre threw, As when embroidered girths enfold An elephant with gleams of gold. Fair as the lily's bending stem,— Her arms adorned with many a gem, A lustre to the fiend she lent Gleaming from every ornament, As when the cloud-shot flashes light The shadows of a mountain height. Whene'er the breezes earthward bore The tinkling of the zone she wore, He seemed a cloud of darkness hue Sending forth murmurs as it flew. As on her way the dame was sped From her sweet neck fair flowers were shed, The swift wind caught the flowery rain And poured it o'er the fiend again. The wind-stirred blossoms, sweet to smell, On the dark brows of RávaG fell,
- **Translation**: 

---

### Verse 6 (Ramayana 0.1051)
- **Original**: Canto LII. Rávan's Flight. 1033 Like lunar constellations set On Meru for a coronet. From her small foot an anklet fair With jewels slipped, and through the air, Like a bright circlet of the flame Of thunder, to the valley came. The Maithil lady, fair to see As the young leaflet of a tree Clad in the tender hues of spring, Flashed glory on the giant king, As when a gold-embroidered zone Around an elephant is thrown. While, bearing far the lady, through The realms of sky the giant flew, She like a gleaming meteor cast A glory round her as she passed. Then from each limb in swift descent Dropped many a sparkling ornament: On earth they rested dim and pale Like fallen stars when virtues fail.504 Around her neck a garland lay Bright as the Star-God's silvery ray: It fell and flashed like Gangá sent From heaven above the firmament.505 The birds of every wing had flocked To stately trees by breezes rocked: [292] These bowed their wind-swept heads and said: “My lady sweet, be comforted.” With faded blooms each brook within Whose waters moved no gleamy fin, Stole sadly through the forest dell 504 The spirits of the good dwell in heaven until their store of accumulated merit is exhausted. Then they redescend to earth in the form of falling stars. 505 See The Descent of Gangá, Book I Canto XLIV.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1052)
- **Original**: 1034 The Ramayana Mourning the dame it loved so well. From every woodland region near Came lions, tigers, birds, and deer, And followed, each with furious look, The way her flying shadow took. For Sítá's loss each lofty hill Whose tears were waterfall, and rill, Lifting on high each arm-like steep, Seemed in the general woe to weep. When the great sun, the lord of day, Saw RávaG tear the dame away, His glorious light began to fail And all his disk grew cold and pale. “If RávaG from the forest flies With Ráma's Sítá as his prize, Justice and truth have vanished hence, Honour and right and innocence.” Thus rose the cry of wild despair From spirits as they gathered there. In trembling troops in open lawns Wept, wild with woe, the startled fawns, And a strange terror changed the eyes They lifted to the distant skies. On silvan Gods who love the dell A sudden fear and trembling fell, As in the deepest woe they viewed The lady by the fiend subdued. Still in loud shrieks was heard afar That voice whose sweetness naught could mar, While eager looks of fear and woe She bent upon the earth below. The lady of each winning wile With pearly teeth and lovely smile, Seized by the lord of Lanká's isle,
- **Translation**: 

---

### Verse 8 (Ramayana 0.1053)
- **Original**: Canto LIII. Sítá's Threats. 1035 Looked down for friends in vain. She saw no friend to aid her, none, Not Ráma nor the younger son Of Da[aratha, and undone She swooned with fear and pain. Canto LIII. Sítá's Threats. Soon as the Maithil lady knew That high through air the giant flew, Distressed with grief and sore afraid Her troubled spirit sank dismayed. Then, as anew the waters welled From those red eyes which sorrow swelled, Forth in keen words her passion broke, And to the fierce-eyed fiend she spoke: “Canst thou attempt a deed so base, Untroubled by the deep disgrace,— To steal me from my home and fly, When friend or guardian none was nigh? Thy craven soul that longed to steal, Fearing the blows that warriors deal, Upon a magic deer relied To lure my husband from my side, Friend of his sire, the vulture king Lies low on earth with mangled wing, Who gave his aged life for me And died for her he sought to free. Ah, glorious strength indeed is thine, Thou meanest of thy giant line, Whose courage dared to tell thy name
- **Translation**: 

---

### Verse 9 (Ramayana 0.1054)
- **Original**: 1036 The Ramayana And conquer in the fight a dame. Does the vile deed that thou hast done Cause thee no shame, thou wicked one— A woman from her home to rend When none was near his aid to lend? Through all the worlds, O giant King, The tidings of this deed will ring, This deed in law and honour's spite By one who claims a hero's might. Shame on thy boasted valour, shame! Thy prowess is an empty name. Shame, giant, on this cursed deed For which thy race is doomed to bleed! Thou fliest swifter than the gale, For what can strength like thine avail? Stay for one hour, O RávaG, stay; Thou shalt not flee with life away. Soon as the royal chieftains' sight Falls on the thief who roams by night, Thou wilt not, tyrant, live one hour Though backed by all thy legions' power. Ne'er can thy puny strength sustain The tempest of their arrowy rain: Have e'er the trembling birds withstood The wild flames raging in the wood? Hear me, O RávaG, let me go, And save thy soul from coming woe. Or if thou wilt not set me free, Wroth for this insult done to me. With his brave brother's aid my lord Against thy life will raise his sword. A guilty hope inflames thy breast His wife from Ráma's home to wrest. Ah fool, the hope thou hast is vain;
- **Translation**: 

---

### Verse 10 (Ramayana 0.1055)
- **Original**: Canto LIII. Sítá's Threats. 1037 Thy dreams of bliss shall end in pain. If torn from all I love by thee My godlike lord no more I see, Soon will I die and end my woes, Nor live the captive of my foes. Ah fool, with blinded eyes to choose The evil and the good refuse! So the sick wretch with stubborn will Turns fondly to the cates that kill, And madly draws his lips away From medicine that would check decay. About thy neck securely wound [293] The deadly coil of Fate is bound, And thou, O RávaG, dost not fear Although the hour of death is near. With death-doomed sight thine eyes behold The gleaming of the trees of gold,— See dread VaitaraGi, the flood That rolls a stream of foamy blood,— See the dark wood by all abhorred— Its every leaf a threatening sword. The tangled thickets thou shall tread Where thorns with iron points are spread. For never can thy days be long, Base plotter of this shame and wrong To Ráma of the lofty soul: He dies who drinks the poisoned bowl. The coils of death around thee lie: They hold thee and thou canst not fly. Ah whither, tyrant, wouldst thou run The vengeance of my lord to shun? By his unaided arm alone Were twice seven thousand fiends o'erthrown: Yes, in the twinkling of an eye
- **Translation**: 

---

### Verse 11 (Ramayana 0.1056)
- **Original**: 1038 The Ramayana He forced thy mightiest fiends to die. And shall that lord of lion heart, Skilled in the bow and spear and dart, Spare thee, O fiend, in battle strife, The robber of his darling wife?” These were her words, and more beside, By wrath and bitter hate supplied. Then by her woe and fear o'erthrown She wept again and made her moan. As long she wept in grief and dread, Scarce conscious of the words she said, The wicked giant onward fled And bore her through the air. As firm he held the Maithil dame, Still wildly struggling, o'er her frame With grief and bitter misery came The trembling of despair. Canto LIV. Lanká. He bore her on in rapid flight, And not a friend appeared in sight. But on a hill that o'er the wood Raised its high top five monkeys stood. From her fair neck her scarf she drew, And down the glittering vesture flew. With earring, necklet, chain, and gem, Descending in the midst of them: “For these,” she thought,“my path may show, And tell my lord the way I go.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.1057)
- **Original**: Canto LIV. Lanká. 1039 Nor did the fiend, in wild alarm, Mark when she drew from neck and arm And foot the gems and gold, and sent To earth each gleaming ornament. The monkeys raised their tawny eyes That closed not in their first surprise, And saw the dark-eyed lady, where She shrieked above them in the air. High o'er their heads the giant passed Holding the weeping lady fast. O'er Pampa's flashing flood he sped And on to Lanká's city fled. He bore away in senseless joy The prize that should his life destroy, Like the rash fool who hugs beneath His robe a snake with venomed teeth. Swift as an arrow from a bow, Speeding o'er lands that lay below, Sublime in air his course he took O'er wood and rock and lake and brook. He passed at length the sounding sea Where monstrous creatures wander free,— Seat of Lord VaruG's ancient reign, Controller of the eternal main. The angry waves were raised and tossed As RávaG with the lady crossed, And fish and snake in wild unrest Showed flashing fin and gleaming crest. Then from the blessed troops who dwell In air celestial voices fell: “O ten-necked King,” they cried,“attend: This guilty deed will bring thine end.”
- **Translation**: 

---

### Verse 13 (Ramayana 0.1058)
- **Original**: 1040 The Ramayana Then RávaG speeding like the storm, Bearing his death in human form, The struggling Sítá, lighted down In royal Lanká's glorious town; A city bright and rich, that showed Well-ordered street and noble road; Arranged with just division, fair With multitudes in court and square. Thus, all his journey done, he passed Within his royal home at last. There in a queenly bower he placed The black-eyed dame with dainty waist: Thus in her chamber Máyá laid The lovely Máyá, demon maid. Then RávaG gave command to all The dread she-fiends who filled the hall: “This captive lady watch and guard From sight of man and woman barred. But all the fair one asks beside Be with unsparing hand supplied: As though 'twere I that asked, withhold No pearls or dress or gems or gold. And she among you that shall dare Of purpose or through want of care One word to vex her soul to say, Throws her unvalued life away.” Thus spake the monarch of their race To those she-fiends who thronged the place, And pondering on the course to take Went from the chamber as he spake. He saw eight giants, strong and dread, On flesh of bleeding victims fed, Proud in the boon which Brahmá gave,[294]
- **Translation**: 

---

### Verse 14 (Ramayana 0.1059)
- **Original**: Canto LIV. Lanká. 1041 And trusting in its power to save. He thus the mighty chiefs addressed Of glorious power and strength possessed: “Arm, warriors, with the spear and bow; With all your speed from Lanká go, For Janasthán, our own no more, Is now defiled with giants' gore; The seat of Khara's royal state Is left unto us desolate. In your brave hearts and might confide, And cast ignoble fear aside. Go, in that desert region dwell Where the fierce giants fought and fell. A glorious host that region held, For power and might unparalleled, By DúshaG and brave Khara led,— All, slain by Ráma's arrows, bled. Hence boundless wrath that spurns control Reigns paramount within my soul, And naught but Ráma's death can sate The fury of my vengeful hate. I will not close my slumbering eyes Till by this hand my foeman dies. And when mine arm has slain the foe Who laid those giant princes low, Long will I triumph in the deed, Like one enriched in utmost need. Now go; that I this end may gain, In Janasthán, O chiefs, remain. Watch Ráma there with keenest eye, And all his deeds and movements spy. Go forth, no helping art neglect, Be brave and prompt and circumspect, And be your one endeavour still
- **Translation**: 

---

### Verse 15 (Ramayana 0.1060)
- **Original**: 1042 The Ramayana To aid mine arm this foe to kill. Oft have I seen your warrior might Proved in the forehead of the fight, And sure of strength I know so well Send you in Janasthán to dwell.” The giants heard with prompt assent The pleasant words he said, And each before his master bent For meet salute, his head. Then as he bade, without delay, From Lanká's gate they passed, And hurried forward on their way Invisible and fast. Canto LV. Sítá In Prison. Thus RávaG his commandment gave To those eight giants strong and brave, So thinking in his foolish pride Against all dangers to provide. Then with his wounded heart aflame With love he thought upon the dame, And took with hasty steps the way To the fair chamber where she lay. He saw the gentle lady there Weighed down by woe too great to bear, Amid the throng of fiends who kept Their watch around her as she wept: A pinnace sinking neath the wave When mighty winds around her rave: A lonely herd-forsaken deer,
- **Translation**: 

---

### Verse 16 (Ramayana 0.1061)
- **Original**: Canto LV. Sítá In Prison. 1043 When hungry dogs are pressing near. Within the bower the giant passed: Her mournful looks were downward cast. As there she lay with streaming eyes The giant bade the lady rise, And to the shrinking captive showed The glories of his rich abode, Where thousand women spent their days In palaces with gold ablaze; Where wandered birds of every sort, And jewels flashed in hall and court. Where noble pillars charmed the sight With diamond and lazulite, And others glorious to behold With ivory, crystal, silver, gold. There swelled on high the tambour's sound, And burnished ore was bright around He led the mournful lady where Resplendent gold adorned the stair, And showed each lattice fair to see With silver work and ivory: Showed his bright chambers, line on line, Adorned with nets of golden twine. Beyond he showed the Maithil dame His gardens bright as lightning's flame, And many a pool and lake he showed Where blooms of gayest colour glowed. Through all his home from view to view The lady sunk in grief he drew. Then trusting in her heart to wake Desire of all she saw, he spake: “Three hundred million giants, all Obedient to their master's call, Not counting young and weak and old,
- **Translation**: 

---

### Verse 17 (Ramayana 0.1062)
- **Original**: 1044 The Ramayana Serve me with spirits fierce and bold. A thousand culled from all of these Wait on the lord they long to please. This glorious power, this pomp and sway, Dear lady, at thy feet I lay: Yea, with my life I give the whole, O dearer than my life and soul. A thousand beauties fill my hall: Be thou my wife and rule them all. O hear my supplication! why This reasonable prayer deny? Some pity to thy suitor show, For love's hot flames within me glow. This isle a hundred leagues in length, Encompassed by the ocean's strength, Would all the Gods and fiends defy Though led by Him who rules the sky. No God in heaven, no sage on earth, No minstrel of celestial birth,[295] No spirit in the worlds I see A match in power and might for me. What wilt thou do with Ráma, him Whose days are short, whose light is dim, Expelled from home and royal sway, Who treads on foot his weary way? Leave the poor mortal to his fate, And wed thee with a worthier mate. My timid love, enjoy with me The prime of youth before it flee. Do not one hour the hope retain To look on Ráma's face again. For whom would wildest thought beguile To seek thee in the giants' isle? Say who is he has power to bind
- **Translation**: 

---

### Verse 18 (Ramayana 0.1063)
- **Original**: Canto LV. Sítá In Prison. 1045 In toils of net the rushing wind. Whose is the mighty hand will tame And hold the glory of the flame? In all the worlds above, below, Not one, O fair of form, I know Who from this isle in fight could rend The lady whom these arms defend. Fair Queen, o'er Lanká's island reign, Sole mistress of the wide domain. Gods, rovers of the night like me, And all the world thy slaves will be. O'er thy fair brows and queenly head Let consecrating balm be shed, And sorrow banished from thy breast, Enjoy my love and take thy rest. Here never more thy soul shall know The memory of thy former woe, And here shall thou enjoy the meed Deserved by every virtuous deed. Here garlands glow of flowery twine, With gorgeous hues and scent divine. Take gold and gems and rich attire: Enjoy with me thy heart's desire. There stand, of chariots far the best, The car my brother once possessed. Which, victor in the stricken field, I forced the Lord of Gold to yield. 'Tis wide and high and nobly wrought, Bright as the sun and swift as thought. Therein O Sítá, shalt thou ride Delighted by thy lover's side. But sorrow mars with lingering trace The splendour of thy lotus face. A cloud of woe is o'er it spread,
- **Translation**: 

---

### Verse 19 (Ramayana 0.1064)
- **Original**: 1046 The Ramayana And all the light of joy is fled.” The lady, by her woe distressed, One corner of her raiment pressed To her sad cheek like moonlight clear, And wiped away a falling tear. The rover of the night renewed His eager pleading as he viewed The lady stand like one distraught, Striving to fix her wandering thought: “Think not, sweet lady, of the shame Of broken vows, nor fear the blame. The saints approve with favouring eyes This union knit with marriage ties. O beauty, at thy radiant feet I lay my heads, and thus entreat. One word of grace, one look I crave: Have pity on thy prostrate slave. These idle words I speak are vain, Wrung forth by love's consuming pain, And ne'er of RávaG be it said He wooed a dame with prostrate head.” Thus to the Maithil lady sued The monarch of the giant brood, And “She is now mine own,” he thought, In Death's dire coils already caught.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1065)
- **Original**: Canto LVI. Sítá's Disdain. 1047 Canto LVI. Sítá's Disdain. His words the Maithil lady heard Oppressed by woe but undeterred. Fear of the fiend she cast aside, And thus in noble scorn replied: “His word of honour never stained King Da[aratha nobly reigned, The bridge of right, the friend of truth. His eldest son, a noble youth, Is Ráma, virtue's faithful friend, Whose glories through the worlds extend. Long arms and large full eyes has he, My husband, yea a God to me. With shoulders like the forest king's, From old Ikshváku's line he springs. He with his brother LakshmaG's aid Will smite thee with the vengeful blade. Hadst thou but dared before his eyes To lay thine hand upon the prize, Thou stretched before his feet hadst lain In Janasthán like Khara slain. Thy boasted rovers of the night With hideous shapes and giant might,— Like serpents when the feathered king Swoops down with his tremendous wing,— Will find their useless venom fail When Ráma's mighty arms assail. The rapid arrows bright with gold, Shot from the bow he loves to hold, Will rend thy frame from flank to flank As Gangá's waves erode the bank. Though neither God nor fiend have power To slay thee in the battle hour,
- **Translation**: 

---



--- End of Ramayan_batch_151.md ---


--- Start of Ramayan_batch_152.md ---

# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Ramayana 0.1066)
- **Original**: 1048 The Ramayana Yet from his hand shall come thy fate, Struck down before his vengeful hate. That mighty lord will strike and end The days of life thou hast to spend. Thy days are doomed, thy life is sped Like victims to the pillar led. Yea, if the glance of Ráma bright With fury on thy form should light, Thou scorched this day wouldst fall and die[296] Like Káma slain by Rudra's eye.506 He who from heaven the moon could throw, Or bid its bright rays cease to glow,— He who could drain the mighty sea Will set his darling Sítá free. Fled is thy life, thy glory, fled Thy strength and power: each sense is dead. Soon Lanká widowed by thy guilt Will see the blood of giants spilt. This wicked deed, O cruel King, No triumph, no delight will bring. Thou with outrageous might and scorn A woman from her lord hast torn. My glorious husband far away, Making heroic strength his stay, Dwells with his brother, void of fear, In DaG ak forest lone and drear. No more in force of arms confide: That haughty strength, that power and pride My hero with his arrowy rain From all thy bleeding limbs will drain. When urged by fate's dire mandate, nigh Comes the fixt hour for men to die. 506 See Book I Canto XXV.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1067)
- **Original**: Canto LVI. Sítá's Disdain. 1049 Caught in Death's toils their eyes are blind, And folly takes each wandering mind. So for the outrage thou hast done The fate is near thou canst not shun,— The fate that on thyself and all Thy giants and thy town shall fall. I spurn thee: can the altar dight With vessels for the sacred rite, O'er which the priest his prayer has said, Be sullied by an outcaste's tread? So me, the consort dear and true Of him who clings to virtue too, Thy hated touch shall ne'er defile, Base tyrant lord of Lanká's isle. Can the white swan who floats in pride Through lilies by her consort's side, Look for one moment, as they pass, On the poor diver in the grass? This senseless body waits thy will, To torture, chain, to wound or kill. I will not, King of giants, strive To keep this fleeting soul alive But never shall they join the name Of Sítá with reproach and shame.” Thus as her breast with fury burned Her bitter speech the dame returned. Such words of rage and scorn, the last She uttered, at the fiend she cast. Her taunting speech the giant heard, And every hair with anger stirred. Then thus with fury in his eye He made in threats his fierce reply: “Hear Maithil lady, hear my speech:
- **Translation**: 

---

### Verse 3 (Ramayana 0.1068)
- **Original**: 1050 The Ramayana List to my words and ponder each. If o'er thy head twelve months shall fly And thou thy love wilt still deny, My cooks shall mince thy flesh with steel And serve it for my morning meal.” Thus with terrific threats to her Spake RávaG, cruel ravener. Mad with the rage her answer woke He called the fiendish train and spoke: “Take her, ye Rákshas dames, who fright With hideous form and mien the sight, Who make the flesh of men your food,— And let her pride be soon subdued.” He spoke, and at his word the band Of fiendish monsters raised each hand In reverence to the giant king, And pressed round Sítá in a ring. RávaG once more with stern behest To those she-fiends his speech addressed: Shaking the earth beneath his tread, He stamped his furious foot and said: “To the A[oka garden bear The dame, and guard her safely there Until her stubborn pride be bent By mingled threat and blandishment. See that ye watch her well, and tame, Like some she-elephant, the dame.”
- **Translation**: 

---

### Verse 4 (Ramayana 0.1069)
- **Original**: Canto LVII. Sítá Comforted. 1051 They led her to that garden where The sweetest flowers perfumed the air, Where bright trees bore each rarest fruit, And birds, enamoured, ne'er were mute. Bowed down with terror and distress, Watched by each cruel giantess,— Like a poor solitary deer When ravening tigresses are near,— The hapless lady lay distraught Like some wild thing but newly caught, And found no solace, no relief From agonizing fear and grief; Not for one moment could forget Each terrifying word and threat, Or the fierce eyes upon her set By those who watched around. She thought of Ráma far away, She mourned for LakshmaG as she lay In grief and terror and dismay Half fainting on the ground. Canto LVII. Sítá Comforted. Soon as the fiend had set her down Within his home in Lanká's town Triumph and joy filled Indra's breast, Whom thus the Eternal Sire addressed:
- **Translation**: 

---

### Verse 5 (Ramayana 0.1070)
- **Original**: 1052 The Ramayana “This deed will free the worlds from woe And cause the giants' overthrow. The fiend has borne to Lanká's isle The lady of the lovely smile, True consort born to happy fate With features fair and delicate.[297] She looks and longs for Ráma's face, But sees a crowd of demon race, And guarded by the giant's train Pines for her lord and weeps in vain. But Lanká founded on a steep Is girdled by the mighty deep, And how will Ráma know his fair And blameless wife is prisoned there? She on her woe will sadly brood And pine away in solitude, And heedless of herself, will cease To live, despairing of release. Yes, pondering on her fate, I see Her gentle life in jeopardy. Go, Indra, swiftly seek the place, And look upon her lovely face. Within the city make thy way: Let heavenly food her spirit stay.” Thus Brahma spake: and He who slew The cruel demon Páka, flew Where Lanká's royal city lay, And Sleep went with him on his way. “Sleep,” cried the heavenly Monarch,“close Each giant's eye in deep repose.”
- **Translation**: 

---

### Verse 6 (Ramayana 0.1071)
- **Original**: Canto LVII. Sítá Comforted. 1053 Thus Indra spoke, and Sleep fulfilled With joy his mandate, as he willed, To aid the plan the Gods proposed, The demons' eyes in sleep she closed. Then Zachí's lord, the Thousand-eyed, To the A[oka garden hied. He came and stood where Sítá lay, And gently thus began to say: “Lord of the Gods who hold the sky, Dame of the lovely smile, am I. Weep no more, lady, weep no more; Thy days of woe will soon be o'er. I come, O Janak's child, to be The helper of thy lord and thee. He through my grace, with hosts to aid, This sea-girt land will soon invade. 'Tis by my art that slumbers close The eyelids of thy giant foes. Now I, with Sleep, this place have sought, Videhan lady, and have brought A gift of heaven's ambrosial food To stay thee in thy solitude. Receive it from my hand, and taste, O lady of the dainty waist: For countless ages thou shall be From pangs of thirst and hunger free.” But doubt within her bosom woke As to the Lord of Gods she spoke: “How may I know for truth that thou Whose form I see before me now Art verily the King adored By heavenly Gods, andZachí's lord? With Raghu's sons I learnt to know
- **Translation**: 

---

### Verse 7 (Ramayana 0.1072)
- **Original**: 1054 The Ramayana The certain signs which Godhead show. These marks before mine eyes display If o'er the Gods thou bear the sway.” The heavenly lord ofZachí heard, And did according to her word. Above the ground his feet were raised; With eyelids motionless he gazed. No dust upon his raiment lay, And his bright wreath was fresh and gay. Nor was the lady's glad heart slow The Monarch of the Gods to know, And while the tears unceasing ran From her sweet eyes she thus began: “My lord has gained a friend in thee, And I this day thy presence see Shown clearly to mine eyes, as when Ráma and LakshmaG, lords of men, Beheld it, and their sire the king, And Janak too from whom I spring. Now I, O Monarch of the Blest, Will eat this food at thy behest, Which thou hast brought me, of thy grace, To aid and strengthen Raghu's race.” She spoke, and by his words relieved, The food from Indra's hand received, Yet ere she ate the balm he brought, On Lakshma G and her lord she thought. “If my brave lord be still alive, If valiant LakshmaG yet survive, May this my taste of heavenly food Bring health to them and bliss renewed!” She ate, and that celestial food
- **Translation**: 

---

### Verse 8 (Ramayana 0.1073)
- **Original**: Canto LVIII. The Brothers' Meeting. 1055 Stayed hunger, thirst, and lassitude, And all her strength restored. Great joy her hopeful spirit stirred At the glad tidings newly heard Of LakshmaG and her lord. And Indra's heart was joyful too: He bade the Maithil dame adieu, His saving errand done. With Sleep beside him parting thence He sought his heavenly residence To prosper Raghu's son. Canto LVIII. The Brothers' Meeting. When Ráma's deadly shaft had struck The giant in the seeming buck, The chieftain turned him from the place His homeward way again to trace. Then as he hastened onward, fain To look upon his spouse again, Behind him from a thicket nigh Rang out a jackal's piercing cry. Alarmed he heard the startling shriek That raised his hair and dimmed his cheek, And all his heart was filled with doubt As the shrill jackal's cry rang out: “Alas, some dire disaster seems Portended by the jackal's screams. O may the Maithil dame be screened From outrage of each hungry fiend! [298]
- **Translation**: 

---

### Verse 9 (Ramayana 0.1074)
- **Original**: 1056 The Ramayana Alas, if LakshmaG chanced to hear That bitter cry of woe and fear What time Márícha, as he died, With voice that mocked my accents cried, Swift to my side the prince would flee And quit the dame to succour me. Too well I see the demon band The slaughter of my love have planned. Me far from home and Sítá's view The seeming deer Márícha drew. He led me far through brake and dell Till wounded by my shaft he fell, And as he sank rang out his cry, “O save me, LakshmaG, or I die.” May it be well with both who stayed In the great wood with none to aid, For every fiend is now my foe For Janasthán's great overthrow, And many an omen seen to-day Has filled my heart with sore dismay.” Such were the thoughts and sad surmise Of Ráma at the jackal's cries, And all his heart within him burned As to his cot his steps he turned. He pondered on the deer that led His feet to follow where it fled, And sad with many a bitter thought His home in Janasthán he sought. His soul was dark with woe and fear When flocks of birds and troops of deer Move round him from the left, and raised Discordant voices as they gazed. The omens which the chieftain viewed
- **Translation**: 

---

### Verse 10 (Ramayana 0.1075)
- **Original**: Canto LVIII. The Brothers' Meeting. 1057 The terror of his soul renewed, When lo, to meet him LakshmaG sped With brows whence all the light had fled. Near and more near the princes came, Each brother's heart and look the same; Alike on each sad visage lay The signs of misery and dismay, Then Ráma by his terror moved His brother for his fault reproved In leaving Sítá far from aid In the wild wood where giants strayed. Lakshma G's left hand he took, and then In gentle tones the prince of men, Though sharp and fierce their tenour ran, Thus to his brother chief began: “O Lakshma G, thou art much to blame Leaving alone the Maithil dame, And flying hither to my side: O, may no ill my spouse betide! But ah, I know my wife is dead, And giants on her limbs have fed, So strange, so terrible are all The omens which my heart appal. O Lakshma G, may we yet return The safety of my love to learn. To find the child of Janak still Alive and free from scathe and ill! Each bird with notes of warning screams, Though the hot sun still darts his beams. The moan of deer, the jackal's yell Of some o'erwhelming misery tell. O mighty brother, still may she, My princess, live from danger free!
- **Translation**: 

---

### Verse 11 (Ramayana 0.1076)
- **Original**: 1058 The Ramayana That semblance of a golden deer Allured me far away, I followed nearer and more near, And longed to take the prey. I followed where the quarry fled: My deadly arrow flew, And as the dying creature bled, The giant met my view. Great fear and pain oppress my heart That dreads the coming blow, And through my left eye keenly dart The throbs that herald woe. Ah Lakshma G, all these signs dismay, My soul that sinks with dread, I know my love is torn away, Or, haply, she is dead.” Canto LIX. Ráma's Return. When Ráma saw his brother stand With none beside him, all unmanned, Eager he questioned why he came So far without the Maithil dame: “Where is my wife, my darling, she Who to the wild wood followed me? Where hast thou left my lady, where The dame who chose my lot to share? Where is my love who balms my woe As through the forest wilds I go, Unkinged and banished and disgraced,— My darling of the dainty waist?
- **Translation**: 

---

### Verse 12 (Ramayana 0.1077)
- **Original**: Canto LIX. Ráma's Return. 1059 She nerves my spirit for the strife, She, only she gives zest to life, Dear as my breath is she who vies In charms with daughters of the skies. If Janak's child be mine no more, In splendour fair as virgin ore, The lordship of the skies and earth To me were prize of little worth. Ah, lives she yet, the Maithil dame, Dear as the soul within this frame? O, let not all my toil be vain, The banishment, the woe and pain! O, let not dark Kaikeyí win The guerdon of her treacherous sin, If, Sítá lost, my days I end, And thou without me homeward wend! O, let not good Kau[alyá shed Her bitter tears to mourn me dead, Nor her proud rival's hest obey, Strong in her son and queenly sway! Back to my cot will I repair If Sítá live to greet me there, [299] But if my wife have perished, I Reft of my love will surely die. O Lakshma G, if I seek my cot, Look for my love and find her not Sweet welcome with her smile to give, I tell thee, I will cease to live. O answer,— let thy words be plain,— Lives Sítá yet, or is she slain? Didst thou thy sacred trust betray Till ravening giants seized the prey? Ah me, so young, so soft and fair, Lapped in all bliss, untried by care,
- **Translation**: 

---

### Verse 13 (Ramayana 0.1078)
- **Original**: 1060 The Ramayana Rent from her own dear husband, how Will she support her misery now? That voice, O LakshmaG smote thine ear, And filled, I ween, thy heart with fear, When on thy name for succour cried The treacherous giant ere he died. That voice too like mine own, I ween, Was heard by the Videhan queen. She bade thee seek my side to aid, And quickly was the hest obeyed, But ah, thy fault I needs must blame, To leave alone the helpless dame, And let the cruel giants sate The fury of their murderous hate. Those blood-devouring demons all Grieve in their souls for Khara's fall, And Sítá, none to guard her side, Torn by their cruel hands has died. I sink, O tamer of thy foes, Deep in the sea of whelming woes. What can I now? I must endure The mighty grief that mocks at cure.” Thus, all his thoughts on Sítá bent, To Janasthán the chieftain went, Hastening on with eager stride, And Lakshma G hurried by his side. With toil and thirst and hunger worn, His breast with doubt and anguish torn, He sought the well-known spot. Again, again he turned to chide With quivering lips which terror dried: He looked, and found her not. Within his leafy home he sped,
- **Translation**: 

---

### Verse 14 (Ramayana 0.1079)
- **Original**: Canto LX. Lakshman Reproved. 1061 Each pleasant spot he visited Where oft his darling strayed. “'Tis as I feared,” he cried, and there, Yielding to pangs too great to bear, He sank by grief dismayed. Canto LX. Lakshman Reproved. But Ráma ceased not to upbraid, His brother for untimely aid, And thus, while anguish wrung his breast, The chief with eager question pressed: “Why, LakshmaG, didst thou hurry hence And leave my wife without defence? I left her in the wood with thee, And deemed her safe from jeopardy. When first thy form appeared in view, I marked that Sítá came not too. With woe my troubled soul was rent, Prophetic of the dire event. Thy coming steps afar I spied, I saw no Sítá by thy side, And felt a sudden throbbing dart Through my left eye, and arm, and heart.”
- **Translation**: 

---

### Verse 15 (Ramayana 0.1080)
- **Original**: 1062 The Ramayana Lakshma G, with Fortune's marks impressed, His brother mournfully addressed: “Not by my heart's free impulse led, Leaving thy wife to thee I sped; But by her keen reproaches sent, O Ráma, to thine aid I went. She heard afar a mournful cry, “O save me, LakshmaG, or I die.” The voice that spoke in moving tone Smote on her ear and seemed thine own. Soon as those accents reached her ear She yielded to her woe and fear, She wept o'ercome by grief, and cried, “Fly, LakshmaG, fly to Ráma's side.” Though many a time she bade me speed, Her urgent prayer I would not heed. I bade her in thy strength confide, And thus with tender words replied: “No giant roams the forest shade From whom thy lord need shrink dismayed. No human voice, believe me, spoke Those words thy causeless fear that woke. Can he whose might can save in woe The heavenly Gods e'er stoop so low, And with those piteous accents call For succour like a caitiff thrall? And why should wandering giants choose The accents of thy lord to use, In alien tones my help to crave, And cry aloud, O LakshmaG, save? Now let my words thy spirit cheer, Compose thy thoughts and banish fear. In hell, in earth, or in the skies There is not, and there cannot rise
- **Translation**: 

---

### Verse 16 (Ramayana 0.1081)
- **Original**: Canto LX. Lakshman Reproved. 1063 A champion whose strong arm can slay Thy Ráma in the battle fray. To heavenly hosts he ne'er would yield Though Indra led them to the field.” To soothe her thus I vainly sought: Her heart with woe was still distraught. While from her eyes the waters ran Her bitter speech she thus began: “Too well I see thy dark intent: Thy lawless thoughts on me are bent. Thou hopest, but thy hope is vain, To win my love, thy brother slain. Not love, but Bharat's dark decree To share his exile counselled thee, [300] Or hearing now his bitter cry Thou surely to his aid wouldst fly. For love of me, a stealthy foe Thou choosest by his side to go, And now thou longest that my lord Should die, and wilt no help afford.” Such were the words the lady said: With angry fire my eyes were red. With pale lips quivering in my rage I hastened from the hermitage.” He ceased; and frenzied by his pain The son of Raghu spoke again: “O brother, for thy fault I grieve, The Maithil dame alone to leave. Thou knowest that my arm is strong To save me from the giant throng, And yet couldst leave the cottage, spurred To folly by her angry word. For this thy deed I praise thee not,—
- **Translation**: 

---

### Verse 17 (Ramayana 0.1082)
- **Original**: 1064 The Ramayana To leave her helpless in the cot, And thus thy sacred charge forsake For the wild words a woman spake. Yea thou art all to blame herein, And very grievous is thy sin. That anger swayed thy faithless breast And made thee false to my behest. An arrow speeding from my bow Has laid the treacherous giant low, Who lured me eager for the chase Far from my hermit dwelling-place. The string with easy hand I drew, The arrow as in pastime flew, The wounded quarry bled. The borrowed form was cast away, Before mine eye a giant lay With bright gold braceleted. My arrow smote him in the chest: The giant by the pain distressed Raised his loud voice on high. Far rang the mournful sound: mine own, It seemed, were accent, voice, and tone, They made thee leave my spouse alone And to my rescue fly.” Canto LXI. Ráma's Lament. As Ráma sought his leafy cot Through his left eye keen throbbings shot, His wonted strength his frame forsook, And all his body reeled and shook.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1083)
- **Original**: Canto LXI. Ráma's Lament. 1065 Still on those dreadful signs he thought,— Sad omens with disaster fraught, And from his troubled heart he cried, “O, may no ill my spouse betide!” Longing to gaze on Sítá's face He hastened to his dwelling-place, Then sinking neath his misery's weight, He looked and found it desolate. Tossing his mighty arms on high He sought her with an eager cry, From spot to spot he wildly ran Each corner of his home to scan. He looked, but Sítá was not there; His cot was disolate and bare, Like streamlet in the winter frost, The glory of her lilies lost. With leafy tears the sad trees wept As a wild wind their branches swept. Mourned bird and deer, and every flower Drooped fainting round the lonely bower. The silvan deities had fled The spot where all the light was dead, Where hermit coats of skin displayed, And piles of sacred grass were laid. He saw, and maddened by his pain Cried in lament again, again: “Where is she, dead or torn away, Lost, or some hungry giant's prey? Or did my darling chance to rove For fruit and blossoms though the grove? Or has she sought the pool or rill, Her pitcher from the wave to fill?” His eager eyes on fire with pain He roamed about with maddened brain.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1084)
- **Original**: 1066 The Ramayana Each grove and glade he searched with care, He sought, but found no Sítá there. He wildly rushed from hill to hill; From tree to tree, from rill to rill, As bitter woe his bosom rent Still Ráma roamed with fond lament: “O sweet Kadamba say has she Who loved thy bloom been seen by thee? If thou have seen her face most fair, Say, gentle tree, I pray thee, where. O Bel tree with thy golden fruit Round as her breast, no more be mute, Where is my radiant darling, gay In silk that mocks thy glossy spray? O Arjun, say, where is she now Who loved to touch thy scented bough? Do not thy graceful friend forget, But tell me, is she living yet? Speak, Basil, thou must surely know, For like her limbs thy branches show,— Most lovely in thy fair array Of twining plant and tender spray. Sweet Tila, fairest of the trees, Melodious with the hum of bees, Where is my darling Sítá, tell,— The dame who loved thy flowers so well? A [oka, act thy gentle part,— Named Heartsease,507 give me what thou art, To these sad eyes my darling show And free me from this load of woe. O Palm, in rich ripe fruitage dressed Round as the beauties of her breast,[301] 507 A[oka is compounded ofa not and[oka grief.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1085)
- **Original**: Canto LXI. Ráma's Lament. 1067 If thou have heart to know and feel, My peerless consort's fate reveal. Hast thou, Rose-apple, chanced to view My darling bright with golden hue? If thou have seen her quickly speak, Where is the dame I wildly seek? O glorious Cassia, thou art gay With all thy loveliest bloom to-day, Where is my dear who loved to hold In her full lap thy flowery gold?” To many a tree and plant beside, To Jasmin, Mango, Sál, he cried. “Say, hast thou seen, O gentle deer, The fawn-eyed Sítá wandering here? It may be that my love has strayed To sport with fawns beneath the shade, If thou, great elephant, have seen My darling of the lovely mien, Whose rounded limbs are soft and fine As is that lissome trunk of thine, O noblest of wild creatures, show Where is the dame thou needs must know. O tiger, hast thou chanced to see My darling? very fair is she, Cast all thy fear away, declare, Where is my moon-faced darling, where? There, darling of the lotus eye, I see thee, and 'tis vain to fly, Wilt thou not speak, dear love? I see Thy form half hidden by the tree. Stay if thou love me, Sítá, stay In pity cease thy heartless play. Why mock me now? thy gentle breast Was never prone to cruel jest.
- **Translation**: 

---



--- End of Ramayan_batch_152.md ---


--- Start of Ramayan_batch_153.md ---

# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Ramayana 0.1086)
- **Original**: 1068 The Ramayana 'Tis vain behind yon bush to steal: Thy shimmering silks thy path reveal. Fly not, mine eyes pursue thy way; For pity's sake, dear Sítá, stay. Ah me, ah me, my words are vain; My gentle love is lost or slain. How could her tender bosom spurn Her husband on his home-return? Ah no, my love is surely dead, Fierce giants on her flesh have fed, Rending the soft limbs of their prey When I her lord was far away. That moon-bright face, that polished brow, Red lips, bright teeth— what are they now? Alas, my darling's shapely neck She loved with chains of gold to deck,— That neck that mocked the sandal scent, The ruthless fiends have grasped and rent. Alas, 'twas vain those arms to raise Soft as the young tree's tender sprays. Ah, dainty meal for giants' lips Were arms and quivering finger tips. Ah, she who counted many a friend Was left for fiends to seize and rend, Was left by me without defence From ravening giants' violence. O Lakshma G of the arm of might, Say, is my darling love in sight? O dearest Sítá. where art thou? Where is my darling consort now?” Thus as he cried in wild lament From grove to grove the mourner went, Here for a moment sank to rest,
- **Translation**: 

---

### Verse 2 (Ramayana 0.1087)
- **Original**: Canto LXII. Ráma's Lament. 1069 Then started up and onward pressed. Thus roaming on like one distraught Still for his vanished love he sought, He searched in wood and hill and glade, By rock and brook and wild cascade. Through groves with restless step he sped And left no spot unvisited. Through lawns and woods of vast extent Still searching for his love he went With eager steps and fast. For many a weary hour he toiled, Still in his fond endeavour foiled, Yet hoping to the last. Canto LXII. Ráma's Lament. When all the toil and search was vain He sought his leafy home again. 'Twas empty still: all scattered lay The seats of grass in disarray. He raised his shapely arms on high And spoke aloud with bitter cry: “Where is the Maithil dame?” he said, “O, whither has my darling fled? Who can have borne away my dame, Or feasted on her tender frame? If, Sítá hidden by some tree, Thou joyest still to mock at me, Cease, cease thy cruel sport, and take Compassion, or my heart will break. Bethink thee, love, the gentle fawns
- **Translation**: 

---

### Verse 3 (Ramayana 0.1088)
- **Original**: 1070 The Ramayana With whom thou playest on the lawns, Impatient for thy coming wait With streaming eyes disconsolate. Reft of my love, I needs must go Hence to the shades weighed down by woe. The king our sire will see me there, And cry,“O perjured Ráma, where, Where is thy faith, that thou canst speed From exile ere the time decreed?” Ah Sítá, whither hast thou fled And left me here disquieted, A hapless mourner, reft of hope, Too feeble with my woe to cope? E'en thus indignant Glory flies The wretch who stains his soul with lies. If thou, my love, art lost to view, I in my woe must perish too.” Thus Ráma by his grief distraught Wept for the wife he vainly sought, And Lakshma G whose fraternal breast Longed for his weal, the chief addressed[302] Whose soul gave way beneath the pain When all his eager search was vain, Like some great elephant who stands Sinking upon the treacherous sands: “Not yet, O wisest chief, despair; Renew thy toil with utmost care. This noble hill where trees are green Has many a cave and dark ravine. The Maithil lady day by day Delighted in the woods to stray, Deep in the grove she wanders still,
- **Translation**: 

---

### Verse 4 (Ramayana 0.1089)
- **Original**: Canto LXII. Ráma's Lament. 1071 Or walks by blossom-covered rill, Or fish-loved river stealing through Tall clusters of the dark bamboo. Or else the dame with arch design To prove thy mood, O Prince, and mine, Far in some sheltering thicket lies To frighten ere she meet our eyes. Then come, renew thy labour, trace The lady to her lurking-place, And search the wood from side to side To know where Sítá loves to bide. Collect thy thoughts, O royal chief, Nor yield to unavailing grief.” Thus LakshmaG, by attention stirred, To fresh attempts his brother spurred, And Ráma, as he ceased, began With LakshmaG's aid each spot to scan. In eager search their way they took Through wood, o'er hill, by pool and brook, They roamed each mount, nor spared to seek On ridge and crag and towering peak. They sought the dame in every spot; But all in vain; they found her not. Above, below, on every side They ranged the hill, and Ráma cried, “O Lakshma G, O my brother still No trace of Sítá on the hill!” Then LakshmaG as he roamed the wood Beside his glorious brother stood, And while fierce grief his bosom burned This answer to the chief returned: “Thou, Ráma, after toil and pain Wilt meet the Maithil dame again,
- **Translation**: 

---

### Verse 5 (Ramayana 0.1090)
- **Original**: 1072 The Ramayana As VishGu, Bali's might subdued, His empire of the earth renewed.”508 Then Ráma cried in mournful tone, His spirit by his woe o'erthrown; “The wood is searched from side to side, No distant spot remains untried, No lilied pool, no streamlet where The lotus buds are fresh and fair. Our eyes have searched the hill with all His caves and every waterfall,— But ah, not yet I find my wife, More precious than the breath of life.” As thus he mourned his vanished dame A mighty trembling seized his frame, And by o'erpowering grief assailed, His troubled senses reeled and failed. Too great to bear his misery grew, And many a long hot sigh he drew, Then as he wept and sobbed and sighed, “O Sítá, O my love!” he cried. Then LakshmaG, joining palm to palm, Tried every art his woe to calm. But Ráma in his anguish heard Or heeded not one soothing word, Still for his spouse he mourned, and shrill Rang out his lamentation still. 508 See Book I Canto XXXI.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1091)
- **Original**: Canto LXIII. Ráma's Lament. 1073 Canto LXIII. Ráma's Lament. Thus for his wife in vain he sought: Then, his sad soul with pain distraught, The hero of the lotus eyes Filled all the air with frantic cries. O'erpowered by love's strong influence, he His absent wife still seemed to see, And thus with accents weak and faint Renewed with tears his wild complaint: “Thou, fairer than their bloom, my spouse, Art hidden by A[oka boughs. Those blooms have power to banish care, But now they drive me to despair. Thine arms are like the plantain's stem: Why let the plantain cover them? Thou art not hidden, love; thy feet Betray thee in thy dark retreat. Thou runnest in thy girlish sport To flowery trees, thy dear resort. But cease, O cease, my love, I pray, To vex me with thy cruel play. Such mockery in a holy spot Where hermits dwell beseems thee not. Ah, now I see thy fickle mind To scornful mood too much inclined, Come, large-eyed beauty, I implore; Lone is the cot so dear before.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1092)
- **Original**: 1074 The Ramayana No, she is slain by giants; they Have stolen or devoured their prey, Or surely at my mournful cry My darling to her lord would fly. O Lakshma G, see those troops of deer: In each sad eye there gleams a tear. Those looks of woe too clearly say My consort is the giants' prey. O noblest, fairest of the fair, Where art thou, best of women, where? This day will dark Kaikeyí find Fresh triumph for her evil mind, When I, who with my Sítá came Return alone, without my dame. But ne'er can I return to see Those chambers where my queen should be And hear the scornful people speak[303] Of Ráma as a coward weak. For mine will be the coward's shame Who let the foeman steal his dame. How can I seek my home, or brook Upon Videha's king to look? How listen, when he bids me tell, My wanderings o'er, that all is well? He, when I meet his eager view, Will mark that Sítá comes not too, And when he hears the mournful tale His wildered sense will reel and fail. “O Da [aratha” will he cry, “Blest in thy mansion in the sky!” Ne'er to that town my steps shall bend, That town which Bharat's arms defend, For e'en the blessed homes above Would seem a waste without my love.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1093)
- **Original**: Canto LXIV. Ráma's Lament. 1075 Leave me, my brother, here, I pray; To fair Ayodhyá bend thy way. Without my love I cannot bear To live one hour in blank despair. Round Bharat's neck thy fond arms twine, And greet him with these words of mine: “Dear brother, still the power retain, And o'er the land as monarch reign.” With salutation next incline Before thy mother, his, and mine. Still, brother, to my words attend, And with all care each dame befriend. To my dear mother's ear relate My mournful tale and Sítá's fate.” Thus Ráma gave his sorrow vent, And from a heart which anguish rent, Mourned for his wife in loud lament,— Her of the glorious hair, From LakshmaG's cheek the colour fled, And o'er his heart came sudden dread, Sick, faint, and sore disquieted By woe too great to bear. Canto LXIV. Ráma's Lament. Reft of his love, the royal chief, Weighed down beneath his whelming grief, Desponding made his brother share His grievous burden of despair. Over his sinking bosom rolled The flood of sorrow uncontrolled.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1094)
- **Original**: 1076 The Ramayana And as he wept and sighed, In mournful accents faint and slow With words congenial to his woe, To LakshmaG thus he cried: “Brother, I ween, beneath the sun, Of all mankind there lives not one So full of sin, whose hand has done Such cursed deeds as mine. For my sad heart with misery bleeds, As, guerdon of those evil deeds, Still greater woe to woe succeeds In never-ending line. A life of sin I freely chose, And from my past transgression flows A ceaseless flood of bitter woes My folly to repay. The fruit of sin has ripened fast, Through many a sorrow have I passed, And now the crowning grief at last Falls on my head to-day. From all my faithful friends I fled, My sire is numbered with the dead, My royal rank is forfeited, My mother far away. These woes on which I sadly think Fill, till it raves above the brink, The stream of grief in which I sink,— The flood which naught can stay. Ne'er, brother, ne'er have I complained; Though long by toil and trouble pained, Without a murmur I sustained The woes of woodland life. But fiercer than the flames that rise
- **Translation**: 

---

### Verse 10 (Ramayana 0.1095)
- **Original**: Canto LXIV. Ráma's Lament. 1077 When crackling wood the food supplies,— Flashing a glow through evening skies,— This sorrow for my wife. Some cruel fiend has seized the prey And torn my trembling love away, While, as he bore her through the skies, She shrieked aloud with frantic cries, In tones of fear which, wild and shrill, Retained their native sweetness still. Ah me, that breast so soft and sweet, For sandal's precious perfume meet, Now all detained with dust and gore, Shall meet my fond caress no more. That face, whose lips with tones so clear Made pleasant music, sweet to hear,— With soft locks plaited o'er the brow,— Some giant's hand is on it now. It smiles not, as the dear light fails When Ráhu's jaw the moon assails. Ah, my true love! that shapely neck She loved with fairest chains to deck, The cruel demons rend, and drain The lifeblood from each mangled vein. Ah, when the savage monsters came And dragged away the helpless dame, The lady of the long soft eye Called like a lamb with piteous cry. Beneath this rock, O LakshmaG, see, My peerless consort sat with me, And gently talked to thee the while, Her sweet lips opening with a smile. Here is that fairest stream which she Loved ever, bright Godávarí. Ne'er can the dame have passed this way:
- **Translation**: 

---

### Verse 11 (Ramayana 0.1096)
- **Original**: 1078 The Ramayana So far alone she would not stray, Nor has my darling, lotus-eyed, Sought lilies by the river's side, For without me she ne'er would go[304] To streamlets where the wild flowers grow, Tell me not, brother, she has strayed To the dark forest's distant shade Where blooming boughs are gay and sweet, And bright birds love the cool retreat. Alone my love would never dare,— My timid love,— to wander there. O Lord of Day whose eye sees all We act and plan, on thee I call: For naught is hidden from thy sight,— Great witness thou of wrong and right. Where is she, lost or torn away? Dispel my torturing doubt and say. And O thou Wind who blowest free, The worlds have naught concealed from thee. List to my prayer, reveal one trace Of her, the glory of her race. Say, is she stolen hence, or dead, Or do her feet the forest tread?” Thus with disordered senses, faint With woe he poured his sad complaint, And then, a better way to teach, Wise LakshmaG spoke in seemly speech: “Up, brother dear, thy grief subdue, With heart and soul thy search renew. When woes oppress and dangers threat Brave effort ne'er was fruitless yet.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.1097)
- **Original**: Canto LXV. Ráma's Wrath. 1079 He spoke, but Ráma gave no heed To valiant LakshmaG's prudent rede. With double force the flood of pain Rushed o'er his yielding soul again. Canto LXV. Ráma's Wrath. With piteous voice, by woe subdued, Thus Raghu's son his speech renewed: “Thy steps, my brother, quickly turn To bright Godávarí and learn If Sítá to the stream have hied To cull the lilies on its side.” Obedient to the words he said, His brother to the river sped. The shelving banks he searched in vain, And then to Ráma turned again. “I searched, but found her not,” he cried; “I called aloud, but none replied. Where can the Maithil lady stray, Whose sight would chase our cares away? I know not where, her steps untraced, Roams Sítá of the dainty waist.”
- **Translation**: 

---

### Verse 13 (Ramayana 0.1098)
- **Original**: 1080 The Ramayana When Ráma heard the words he spoke Again he sank beneath the stroke, And with a bosom anguish-fraught Himself the lovely river sought. There standing on the shelving side, “O Sítá, where art thou?” he cried. No spirit voice an answer gave, No murmur from the trembling wave Of sweet Godávarí declared The outrage which the fiend had dared. “O speak!” the pitying spirits cried, But yet the stream their prayer denied, Nor dared she, coldly mute, relate To the sad chief his darling's fate Of RávaG's awful form she thought, And the dire deed his arm had wrought, And still withheld by fear dismayed, The tale for which the mourner prayed. When hope was none, his heart to cheer, That the bright stream his cry would hear While sorrow for his darling tore His longing soul he spake once more: “Though I have sought with tears and sighs Godárvarí no word replies, O say, what answer can I frame To Janak, father of my dame? Or how before her mother stand Leading no Sítá by the hand? Where is my loyal love who went Forth with her lord to banishment? Her faith to me she nobly held Though from my realm and home expelled,— A hermit, nursed on woodland fare,— She followed still and soothed my care.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1099)
- **Original**: Canto LXV. Ráma's Wrath. 1081 Of all my friends am I bereft, Nor is my faithful consort left. How slowly will the long nights creep While comfortless I wake and weep! O, if my wife may yet be found, With humble love I'll wander round This Janasthán, Pra[ravaG's hill, Mandákiní's delightful rill. See how the deer with gentle eyes Look on my face and sympathize. I mark their soft expression: each Would soothe me, if it could, with speech.” A while the anxious throng he eyed. And “Where is Sítá, where?” he cried. Thus while hot tears his utterance broke The mourning son of Raghu spoke. The deer in pity for his woes Obeyed the summons and arose. Upon his right thy stood, and raised Their sad eyes up to heaven and gazed Each to that quarter bent her look Which RávaG with his captive took. Then Raghu's son again they viewed, And toward that point their way pursued. Then LakshmaG watched their looks intent As moaning on their way they went, And marked each sign which struck his sense With mute expressive influence, Then as again his sorrow woke Thus to his brother chief he spoke: “Those deer thy eager question heard [305]
- **Translation**: 

---

### Verse 15 (Ramayana 0.1100)
- **Original**: 1082 The Ramayana And rose at once by pity stirred: See, in thy search their aid they lend, See, to the south their looks they bend. Arise, dear brother, let us go The way their eager glances show, If haply sign or trace descried Our footsteps in the search may guide.” The son of Raghu gave assent, And quickly to the south they went; With eager eyes the earth he scanned, And Lakshma G followed close at hand. As each to other spake his thought, And round with anxious glances sought, Scattered before them in the way, Blooms of a fallen garland lay. When Ráma saw that flowery rain He spoke once more with bitterest pain: “O Lakshma G every flower that lies Here on the ground I recognize. I culled them in the grove, and there My darling twined them in her hair. The sun, the earth, the genial breeze Have spared these flowers my soul to please.” Then to that woody hill he prayed, Whence flashed afar each wild cascade: “O best of mountains, hast thou seen A dame of perfect form and mien In some sweet spot with trees o'ergrown,— My darling whom I left alone?” Then as a lion threats a deer He thundered with a voice of fear: “Reveal her, mountain, to my view
- **Translation**: 

---

### Verse 16 (Ramayana 0.1101)
- **Original**: Canto LXV. Ráma's Wrath. 1083 With golden limbs and golden hue. Where is my darling Sítá? speak Before I rend thee peak from peak.” The mountain seemed her track to show, But told not all he sought to know. Then Da[aratha's son renewed His summons as the mount he viewed: “Soon as my flaming arrows fly, Consumed to ashes shall thou lie Without a herb or bud or tree, And birds no more shall dwell in thee. And if this stream my prayer deny, My wrath this day her flood shall dry, Because she lends no aid to trace My darling of the lotus face.” Thus Ráma spake as though his ire Would scorch them with his glance of fire; Then searching farther on the ground The footprint of a fiend he found, And small light traces here and there, Where Sítá in her great despair, Shrieking for Ráma's help, had fled Before the giant's mighty tread. His careful eye each trace surveyed Which Sítá and the fiend had made,— The quivers and the broken bow And ruined chariot of the foe,— And told, distraught by fear and grief, His tidings to his brother chief: “O Lakshma G, here,” he cried“behold My Sítá's earrings dropped with gold. Here lie her garlands torn and rent,
- **Translation**: 

---

### Verse 17 (Ramayana 0.1102)
- **Original**: 1084 The Ramayana Here lies each glittering ornament. O look, the ground on every side With blood-like drops of gold is dyed. The fiends who wear each strange disguise Have seized, I ween, the helpless prize. My lady, by their hands o'erpowered, Is slaughtered, mangled, and devoured. Methinks two fearful giants came And waged fierce battle for the dame. Whose, LakshmaG, was this mighty bow With pearls and gems in glittering row? Cast to the ground the fragments lie, And still their glory charms the eye. A bow so mighty sure was planned For heavenly God or giant's hand. Whose was this coat of golden mail Which, though its lustre now is pale, Shone like the sun of morning, bright With studs of glittering lazulite? Whose, LakshmaG, was this bloom-wreathed shade With all its hundred ribs displayed? This screen, most meet for royal brow, With broken staff lies useless now. And these tall asses, goblin-faced, With plates of golden harness graced, Whose hideous forms are stained with gore Who is the lord whose yoke they bore? Whose was this pierced and broken car That shoots a flame-like blaze afar? Whose these spent shafts at random spread, Each fearful with its iron head,— With golden mountings fair to see, Long as a chariot's axle-tree? These quivers see, which, rent in twain,
- **Translation**: 

---

### Verse 18 (Ramayana 0.1103)
- **Original**: Canto LXV. Ráma's Wrath. 1085 Their sheaves of arrows still contain. Whose was this driver? Dead and cold, His hands the whip and reins still hold. See, LakshmaG, here the foot I trace Of man, nay, one of giant race. The hatred that I nursed of old Grows mightier now a hundred fold Against these giants, fierce of heart, Who change their forms by magic art. Slain, eaten by the giant press, Or stolen is the votaress, Nor could her virtue bring defence To Sítá seized and hurried hence. O, if my love be slain or lost All hope of bliss for me is crossed. The power of all the worlds were vain To bring one joy to soothe my pain. The spirits with their blinded eyes Would look in wonder, and despise The Lord who made the worlds, the great Creator when compassionate. And so, I ween, the Immortals turn Cold eyes upon me now, and spurn [306] The weakling prompt at pity's call, Devoted to the good of all. But from this day behold me changed, From every gentle grace estranged. Now be it mine all life to slay, And sweep these cursed fiends away. As the great sun leaps up the sky, And the cold moonbeams fade and die, So vengeance rises in my breast, One passion conquering all the rest. Gandharvas in their radiant place,
- **Translation**: 

---

### Verse 19 (Ramayana 0.1104)
- **Original**: 1086 The Ramayana The Yakshas, and the giant race, Kinnars and men shall look in vain For joy they ne'er shall see again. The anguish of my great despair, O Lakshma G, fills the heaven and air; And I in wrath all life will slay Within the triple world to-day. Unless the Gods in heaven who dwell Restore my Sítá safe and well, I armed with all the fires of Fate, The triple world will devastate. The troubled stars from heaven shall fall, The moon be wrapped in gloomy pall, The fire be quenched, the wind be stilled, The radiant sun grow dark and chilled; Crushed every mountain's towering pride, And every lake and river dried, Dead every creeper, plant, and tree, And lost for aye the mighty sea. Thou shalt the world this day behold In wild disorder uncontrolled, With dying life which naught defends From the fierce storm my bowstring sends. My shafts this day, for Sítá's sake, The life of every fiend shall take. The Gods this day shall see the force That wings my arrows on their course, And mark how far that course is held, By my unsparing wrath impelled. No God, not one of Daitya strain, Goblin or Rákshas shall remain. My wrath shall end the worlds, and all Demons and Gods therewith shall fall. Each world which Gods, the Dánav race,
- **Translation**: 

---

### Verse 20 (Ramayana 0.1105)
- **Original**: Canto LXV. Ráma's Wrath. 1087 And giants make their dwelling place, Shall fall beneath my arrows sent In fury when my bow is bent. The arrows loosened from my string Confusion on the worlds shall bring. For she is lost or breathes no more, Nor will the Gods my love restore. Hence all on earth with life and breath This day I dedicate to death. All, till my darling they reveal, The fury of my shafts shall feel.” Thus as he spake by rage impelled, Red grew his eyes, his fierce lips swelled. His bark coat round his form he drew And coiled his hermit braids anew, Like Rudra when he yearned to slay The demon Tripur509 in the fray. So looked the hero brave and wise, The fury flashing from his eyes. Then Ráma, conqueror of the foe, From LakshmaG's hand received his bow, Strained the great string, and laid thereon A deadly dart that flashed and shone, And spake these words as fierce in ire As He who ends the worlds with fire: 509 An Asur or demon, king of Tripura, the modern Tipperah.
- **Translation**: 

---



--- End of Ramayan_batch_153.md ---


--- Start of Ramayan_batch_154.md ---

# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Ramayana 0.1106)
- **Original**: 1088 The Ramayana “As age and time and death and fate All life with checkless power await, So LakshmaG in my wrath to-day My vengeful might shall brook no stay, Unless this day I see my dame In whose sweet form is naught to blame,— Yea, as before, my love behold Fair with bright teeth and perfect mould, This world shall feel a deadly blow Destroyed with ruthless overthrow, And serpent lords and Gods of air, Gandharvas, men, the doom shall share.” Canto LXVI. Lakshman's Speech. He stood incensed with eyes of flame, Still mourning for his ravished dame, Determined, like the fire of Fate, To leave the wide world desolate. His ready bow the hero eyed, And as again, again he sighed, The triple world would fain consume Like Hara510 in the day of doom. Then LakshmaG moved with sorrow viewed His brother in unwonted mood, And reverent palm to palm applied, Thus spoke with lips which terror dried “Thy heart was ever soft and kind, To every creature's good inclined. 510 Ziva.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1107)
- **Original**: Canto LXVI. Lakshman's Speech. 1089 Cast not thy tender mood away, Nor yield to anger's mastering sway. The moon for gentle grace is known, The sun has splendour all his own, The restless wind is free and fast, And earth in patience unsurpassed. So glory with her noble fruit Is thine eternal attribute. O, let not, for the sin of one, The triple world be all undone. I know not whose this car that lies In fragments here before our eyes, Nor who the chiefs who met and fought, Nor what the prize the foemen sought; Who marked the ground with hoof and wheel, [307] Or whose the hand that plied the steel Which left this spot, the battle o'er, Thus sadly dyed with drops of gore. Searching with utmost care I view The signs of one and not of two. Where'er I turn mine eyes I trace No mighty host about the place. Then mete not out for one offence This all-involving recompense. For kings should use the sword they bear, But mild in time should learn to spare, Thou, ever moved by misery's call, Wast the great hope and stay of all. Throughout this world who would not blame This outrage on thy ravished dame? Gandharvas, Dánavs, Gods, the trees, The rocks, the rivers, and the seas, Can ne'er in aught thy soul offend, As one whom holiest rites befriend.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1108)
- **Original**: 1090 The Ramayana But him who dared to steal the dame Pursue, O King, with ceaseless aim, With me, the hermits' holy band, And thy great bow to arm thy hand By every mighty flood we'll seek, Each wood, each hill from base to peak. To the fair homes of Gods we'll fly, And bright Gandharvas in the sky, Until we reach, where'er he be, The wretch who stole thy spouse from thee. Then if the Gods will not restore Thy Sítá when the search is o'er, Then, royal lord of Ko[al's land, No longer hold thy vengeful hand. If meekness, prayer, and right be weak To bring thee back the dame we seek, Up, brother, with a deadly shower Of gold-bright shafts thy foes o'erpower, Fierce as the flashing levin sent From King Mahendra's firmament. Canto LXVII. Ráma Appeased. As Ráma, pierced by sorrow's sting, Lamented like a helpless thing, And by his mighty woe distraught Was lost in maze of troubled thought, Sumitrá's son with loving care Consoled him in his wild despair, And while his feet he gently pressed With words like these the chief addressed:
- **Translation**: 

---

### Verse 4 (Ramayana 0.1109)
- **Original**: Canto LXVII. Ráma Appeased. 1091 “For sternest vow and noblest deed Was Da [aratha blessed with seed. Thee for his son the king obtained, Like Amrit by the Gods regained. Thy gentle graces won his heart, And all too weak to live apart The monarch died, as Bharat told, And lives on high mid Gods enrolled. If thou, O Ráma, wilt not bear This grief which fills thee with despair, How shall a weaker man e'er hope, Infirm and mean, with woe to cope? Take heart, I pray thee, noblest chief: What man who breathes is free from grief? Misfortunes come and burn like flame, Then fly as quickly as they came. Yayáti son of Nahush reigned With Indra on the throne he gained. But falling for a light offence He mourned a while the consequence. Va [ishmha, reverend saint and sage, Priest of our sire from youth to age, Begot a hundred sons, but they Were smitten in a single day.511 And she, the queen whom all revere, The mother whom we hold so dear, The earth herself not seldom feels Fierce fever when she shakes and reels. And those twin lights, the world's great eyes, On which the universe relies,— Does not eclipse at times assail Their brilliance till their fires grow pale? 511 See Book I, Canto LIX.
- **Translation**: 

---

### Verse 5 (Ramayana 0.1110)
- **Original**: 1092 The Ramayana The mighty Powers, the Immortal Blest Bend to a law which none contest. No God, no bodied life is free From conquering Fate's supreme decree. E'enZakra's self must reap the meed Of virtue and of sinful deed. And O great lord of men, wilt thou Helpless beneath thy misery bow? No, if thy dame be lost or dead, O hero, still be comforted, Nor yield for ever to thy woe O'ermastered like the mean and low. Thy peers, with keen far-reaching eyes, Spend not their hours in ceaseless sighs; In dire distress, in whelming ill Their manly looks are hopeful still. To this, great chief, thy reason bend, And earnestly the truth perpend. By reason's aid the wisest learn The good and evil to discern. With sin and goodness scarcely known Faint light by chequered lives is shown; Without some clear undoubted deed We mark not how the fruits succeed. In time of old, O thou most brave, To me thy lips such counsel gave. V [ihaspati512 can scarcely find New wisdom to instruct thy mind. For thine is wit and genius high Meet for the children of the sky. I rouse that heart benumbed by pain And call to vigorous life again. 512 The preceptor of the Gods.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1111)
- **Original**: Canto LXVIII. Jatáyus. 1093 Be manly godlike vigour shown; Put forth that noblest strength, thine own. [308] Strive, best of old Ikshváku's strain, Strive till the conquered foe be slain. Where is the profit or the joy If thy fierce rage the worlds destroy? Search till thou find the guilty foe, Then let thy hand no mercy show.” Canto LXVIII. Jatáyus. Thus faithful LakshmaG strove to cheer The prince with counsel wise and clear. Who, prompt to seize the pith of all, Let not that wisdom idly fall. With vigorous effort he restrained The passion in his breast that reigned, And leaning on his bow for rest His brother LakshmaG thus addressed: “How shall we labour now, reflect; Whither again our search direct? Brother, what plan canst thou devise To bring her to these longing eyes?”
- **Translation**: 

---

### Verse 7 (Ramayana 0.1112)
- **Original**: 1094 The Ramayana To him by toil and sorrow tried The prudent LakshmaG thus replied: “Come, though our labour yet be vain, And search through Janasthán again,— A realm where giant foes abound, And trees and creepers hide the ground. For there are caverns deep and dread, By deer and wild birds tenanted, And hills with many a dark abyss, Grotto and rock and precipice. There bright Gandharvas love to dwell, And Kinnars in each bosky dell. With me thy eager search to aid Be every hill and cave surveyed. Great chiefs like thee, the best of men, Endowed with sense and piercing ken, Though tried by trouble never fail, Like rooted hills that mock the gale.” Then Ráma, pierced by anger's sting, Laid a keen arrow on his string, And by the faithful LakshmaG's side Roamed through the forest far and wide. Jamáyus there with blood-drops dyed, Lying upon the ground he spied, Huge as a mountain's shattered crest, Mid all the birds of air the best. In wrath the mighty bird he eyed, And thus the chief to LakshmaG cried:
- **Translation**: 

---

### Verse 8 (Ramayana 0.1113)
- **Original**: Canto LXVIII. Jatáyus. 1095 “Ah me, these signs the truth betray; My darling was the vulture's prey. Some demon in the bird's disguise Roams through the wood that round us lies. On large-eyed Sítá he has fed, And rests him now with wings outspread. But my keen shafts whose flight is true, Shall pierce the ravenous monster through.” An arrow on the string he laid, And rushing near the bird surveyed, While earth to ocean's distant side Trembled beneath his furious stride. With blood and froth on neck and beak The dying bird essayed to speak, And with a piteous voice, distressed, Thus Da[aratha's son addressed: “She whom like some sweet herb of grace Thou seekest in this lonely place, Fair lady, is fierce RávaG's prey, Who took, beside, my life away. Lakshma G and thou had parted hence And left the dame without defence. I saw her swiftly borne away By RávaG's might which none could stay. I hurried to the lady's aid, I crushed his car and royal shade, And putting forth my warlike might Hurled RávaG to the earth in fight. Here, Ráma, lies his broken bow, Here lie the arrows of the foe. There on the ground before thee are The fragments of his battle car.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1114)
- **Original**: 1096 The Ramayana There bleeds the driver whom my wings Beat down with ceaseless buffetings. When toil my aged strength subdued, His sword my weary pinions hewed. Then lifting up the dame he bare His captive through the fields of air. Thy vengeful blows from me restrain, Already by the giant slain.” When Ráma heard the vulture tell The tale that proved his love so well, His bow upon the ground he placed, And tenderly the bird embraced: Then to the earth he fell o'erpowered, And burning tears both brothers showered, For double pain and anguish pressed Upon the patient hero's breast. The solitary bird he eyed Who in the lone wood gasped and sighed, And as again his anguish woke Thus Ráma to his brother spoke: “Expelled from power the woods I tread, My spouse is lost, the bird is dead. A fate so sad, I ween, would tame The vigour of the glorious flame. If I to cool my fever tried To cross the deep from side to side, The sea,— so hard my fate,— would dry His waters as my feet came nigh. In all this world there lives not one So cursed as I beneath the sun; So strong a net of misery cast Around me holds the captive fast,
- **Translation**: 

---

### Verse 10 (Ramayana 0.1115)
- **Original**: Canto LXIX. The Death Of Jatáyus. 1097 Best of all birds that play the wing, Loved, honoured by our sire the king, The vulture, in my fate enwound, Lies bleeding, dying on the ground.” Then Ráma and his brother stirred [309] By pity mourned the royal bird, And, as their hands his limbs caressed, Affection for a sire expressed. And Ráma to his bosom strained The bird with mangled wings distained, With crimson blood-drops dyed. He fell, and shedding many a tear, “Where is my spouse than life more dear? Where is my love?” he cried. Canto LXIX. The Death Of Jatáyus. As Ráma viewed with heart-felt pain The vulture whom the fiend had slain, In words with tender love impressed His brother chief he thus addressed:
- **Translation**: 

---

### Verse 11 (Ramayana 0.1116)
- **Original**: 1098 The Ramayana “This royal bird with faithful thought For my advantage strove and fought. Slain by the fiend in mortal strife For me he yields his noble life. See, LakshmaG, how his wounds have bled; His struggling breath will soon have fled. Faint is his voice, and near to die, He scarce can lift his trembling eye. Jamáyus, if thou still can speak, Give, give the answer that I seek. The fate of ravished Sítá tell, And how thy mournful chance befell. Say why the giant stole my dame: What have I done that he could blame? What fault in me has RávaG seen That he should rob me of my queen? How looked the lady's moon-bright cheek? What were the words she found to speak? His strength, his might, his deeds declare: And tell the form he loves to wear. To all my questions make reply: Where does the giant's dwelling lie?” The noble bird his glances bent On Ráma as he made lament, And in low accents faint and weak With anguish thus began to speak: “Fierce RávaG, king of giant race, Stole Sítá from thy dwelling-place. He calls his magic art to aid With wind and cloud and gloomy shade. When in the fight my power was spent My wearied wings he cleft and rent. Then round the dame his arms he threw,
- **Translation**: 

---

### Verse 12 (Ramayana 0.1117)
- **Original**: Canto LXIX. The Death Of Jatáyus. 1099 And to the southern region flew. O Raghu's son, I gasp for breath, My swimming sight is dim in death. E'en now before my vision pass Bright trees of gold with hair of grass, The hour the impious robber chose Brings on the thief a flood of woes. The giant in his haste forgot 'Twas Vinda's hour,513 or heeded not. Those robbed at such a time obtain Their plundered store and wealth again. He, like a fish that takes the bait, In briefest time shall meet his fate. Now be thy troubled heart controlled And for thy lady's loss consoled, For thou wilt slay the fiend in fight And with thy dame have new delight.” With senses clear, though sorely tried, The royal vulture thus replied, While as he sank beneath his pain Forth rushed the tide of blood again. “Him,514 brother of the Lord of Gold, Vi[ravas' self begot of old.” Thus spoke the bird, and stained with gore Resigned the breath that came no more. “Speak, speak again!” thus Ráma cried, With reverent palm to palm applied, But from the frame the spirit fled And to the skiey regions sped. The breath of life had passed away. Stretched on the ground the body lay. 513 From the rootvid, to find. 514 RávaG.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1118)
- **Original**: 1100 The Ramayana When Ráma saw the vulture lie, Huge as a hill, with darksome eye, With many a poignant woe distressed His brother chief he thus addressed: “Amid these haunted shades content Full many a year this bird has spent. His life in home of giants passed, In DaG ak wood he dies at last. The years in lengthened course have fled Untroubled o'er the vulture's head, And now he lies in death, for none The stern decrees of Fate may shun. See, LakshmaG, how the vulture fell While for my sake he battled well. And strove to free with onset bold My Sítá from the giant's hold. Supreme amid the vulture kind His ancient rule the bird resigned, And conquered in the fruitless strife Gave for my sake his noble life. O Lakshma G, many a time we see Great souls who keep the law's decree, With whom the weak sure refuge find, In creatures of inferior kind. The loss of her, my darling queen, Strikes with a pang less fiercely keen Than now this slaughtered bird to see Who nobly fought and died for me. As Da[aratha, good and great, Was glorious in his high estate, Honoured by all, to all endeared, So was this royal bird revered. Bring fuel for the funeral rite: These hands the solemn fire shall light[310]
- **Translation**: 

---

### Verse 14 (Ramayana 0.1119)
- **Original**: Canto LXIX. The Death Of Jatáyus. 1101 And on the burning pyre shall lay The bird who died for me to-day. Now on the gathered wood shall lie The lord of all the birds that fly, And I will burn with honours due My champion whom the giant slew. O royal bird of noblest heart, Graced with all funeral rites depart To bright celestial seats above, Rewarded for thy faithful love. Dwell in thy happy home with those Whose constant fires of worship rose. Live blest amid the unyielding brave, And those who land in largess gave.” Sore grief upon his bosom weighed As on the pyre the bird he laid, And bade the kindled flame ascend To burn the body of his friend. Then with his brother by his side The hero to the forest hied. There many a stately deer he slew, The flesh around the bird to strew. The venison into balls he made, And on fair grass before him laid. Then that the parted soul might rise And find free passage to the skies, Each solemn word and text he said Which Bráhmans utter o'er the dead. Then hastening went the princely pair To bright Godávarí, and there Libations of the stream they poured In honour of the vulture lord, With solemn ritual to the slain,
- **Translation**: 

---

### Verse 15 (Ramayana 0.1120)
- **Original**: 1102 The Ramayana As scripture's holy texts ordain. Thus offerings to the bird they gave And bathed their bodies in the wave. The vulture monarch having wrought A hard and glorious feat, Honoured by Ráma sage in thought, Soared to his blissful seat. The brothers, when each rite was paid To him of birds supreme, Their hearts with new-found comfort stayed, And turned them from the stream. Like sovereigns of celestial race Within the wood they came, Each pondering the means to trace, The captor of the dame. Canto LXX. Kabandha. When every rite was duly paid The princely brothers onward strayed, And eager in the lady's quest They turned their footsteps to the west. Through lonely woods that round them lay Ikshváku's children made their way, And armed with bow and shaft and brand Pressed onward to the southern land. Thick trees and shrubs and creepers grew In the wild grove they hurried through. 'Twas dark and drear and hard to pass For tangled thorns and matted grass.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1121)
- **Original**: Canto LXX. Kabandha. 1103 Still onward with a southern course They made their way with vigorous force, And passing through the mazes stood Beyond that vast and fearful wood. With toil and hardship yet unspent Three leagues from Janasthán they went, And speeding on their way at last Within the wood of Krauncha515 passed: A fearful forest wild and black As some huge pile of cloudy rack, Filled with all birds and beasts, where grew Bright blooms of every varied hue. On Sítá bending every thought Through all the mighty wood they sought, And at the lady's loss dismayed Here for a while and there they stayed. Then turning farther eastward they Pursued three leagues their weary way, Passed Krauncha's wood and reached the grove Where elephants rejoiced to rove. The chiefs that awful wood surveyed Where deer and wild birds filled each glade, Where scarce a step the foot could take For tangled shrub and tree and brake. There in a mountain's woody side A cave the royal brothers spied, With dread abysses deep as hell, Where darkness never ceased to dwell. When, pressing on, the lords of men Stood near the entrance of the den, They saw within the dark recess A huge misshapen giantess; 515 Or Curlews' Wood.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1122)
- **Original**: 1104 The Ramayana A thing the timid heart that shook With fearful shape and savage look. Terrific fiend, her voice was fierce, Long were her teeth to rend and pierce. The monster gorged her horrid feast Of flesh of many a savage beast, While her long locks, at random flung, Dishevelled o'er her shoulders hung. Their eyes the royal brothers raised, And on the fearful monster gazed. Forth from her den she came and glanced At LakshmaG as he first advanced, Her eager arms to hold him spread, And “Come and be my love” she said, Then as she held him to her breast, The prince in words like these addressed: “Behold thy treasure fond and fair: Ayomukhi 516 the name I bear.[311] In thickets of each lofty hill, On islets of each brook and rill, With me delighted shalt thou play, And live for many a lengthened day.” Enraged he heard the monster woo; His ready sword he swiftly drew, And the sharp steel that quelled his foes Cut through her breast and ear and nose. Thus mangled by his vengeful sword In rage and pain the demon roared, And hideous with her awful face Sped to her secret dwelling place. Soon as the fiend had fled from sight, The brothers, dauntless in their might, 516 Iron-faced.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1123)
- **Original**: Canto LXX. Kabandha. 1105 Reached a wild forest dark and dread Whose tangled ways were hard to tread. Then bravest LakshmaG, virtuous youth, The friend of purity and truth, With reverent palm to palm applied Thus to his glorious brother cried: “My arm presaging throbs amain, My troubled heart is sick with pain, And cheerless omens ill portend Where'er my anxious eyes I bend. Dear brother, hear my words: advance Resolved and armed for every chance, For every sign I mark to-day Foretells a peril in the way. This bird of most ill-omened note, Loud screaming with discordant throat, Announces with a warning cry That strife and victory are nigh.” Then as the chiefs their search pursued Throughout the dreary solitude, They heard amazed a mighty sound That broke the very trees around, As though a furious tempest passed Crushing the wood beneath its blast. Then Ráma raised his trusty sword, And both the hidden cause explored. There stood before their wondering eyes A fiend broad-chested, huge of size. A vast misshapen trunk they saw In height surpassing nature's law. It stood before them dire and dread Without a neck, without a head.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1124)
- **Original**: 1106 The Ramayana Tall as some hill aloft in air, Its limbs were clothed with bristling hair, And deep below the monster's waist His vast misshapen mouth was placed. His form was huge, his voice was loud As some dark-tinted thunder cloud. Forth from his ample chest there came A brilliance as of gushing flame. Beneath long lashes, dark and keen The monster's single eye was seen. Deep in his chest, long, fiercely bright, It glittered with terrific light. He swallowed down his savage fare Of lion, bird, and slaughtered bear, And with huge teeth exposed to view O'er his great lips his tongue he drew. His arms unshapely, vast and dread, A league in length, he raised and spread. He seized with monstrous hands a herd Of deer and many a bear and bird. Among them all he picked and chose, Drew forward these, rejected those. Before the princely pair he stood Barring their passage through the wood. A league of shade the chiefs had passed When on the fiend their eyes they cast. A monstrous shape without a head With mighty arms before him spread, They saw that hideous trunk appear That struck the trembling eye with fear. Then, stretching to their full extent His awful arms with fingers bent, Round Raghu's princely sons he cast Each grasping limb and held them fast.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1125)
- **Original**: Canto LXX. Kabandha. 1107 Though strong of arm and fierce in fight, Each armed with bow and sword to smite, The royal brothers, brave and bold, Were helpless in the giant's hold. Then Raghu's son, heroic still, Felt not a pang his bosom thrill; But young, with no protection near, His brother's heart was sad with fear, And thus with trembling tongue he said To Ráma, sore disquieted: “Ah me, ah me, my days are told: O see me in the giant's hold. Fly, son of Raghu, swiftly flee, And thy dear self from danger free. Me to the fiend an offering give; Fly at thine ease thyself and live. Thou, great Kakutstha's son, I ween, Wilt find ere long thy Maithil queen, And when thou holdest, throned again, Thine old hereditary reign, With servants prompt to do thy will, O think upon thy brother still.” As thus the trembling LakshmaG cried, The dauntless Ráma thus replied: “Brother, from causeless dread forbear. A chief like thee should scorn despair.” He spoke to soothe his wild alarm: Then fierce Kabandha517 long of arm, Among the Dánavs518 first and best, The sons of Raghu thus addressed: 517 Kabandha means a trunk. 518 A class of mythological giants. In the Epic period they were probably personifications of the aborigines of India.
- **Translation**: 

---



--- End of Ramayan_batch_154.md ---


--- Start of Ramayan_batch_155.md ---

# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Ramayana 0.1126)
- **Original**: 1108 The Ramayana “What men are you, whose shoulders show Broad as a bull's, with sword and bow, Who roam this dark and horrid place, Brought by your fate before my face? Declare by what occasion led These solitary wilds you tread, With swords and bows and shafts to pierce,[312] Like bulls whose horns are strong and fierce. Why have you sought this forest land Where wild with hunger's pangs I stand? Now as your steps my path have crossed Esteem your lives already lost.” The royal brothers heard with dread The words which fierce Kabandha said. And Ráma to his brother cried, Whose cheek by blanching fear was dried: “Alas, we fall, O valiant chief, From sorrow into direr grief, Still mourning her I hold so dear We see our own destruction near. Mark, brother, mark what power has time O'er all that live, in every clime. Now, lord of men, thyself and me Involved in fatal danger see. 'Tis not, be sure, the might of Fate That crushes all with deadly weight. Ne'er can the brave and strong, who know The use of spear and sword and bow, The force of conquering time withstand, But fall like barriers built of sand.”
- **Translation**: 

---

### Verse 2 (Ramayana 0.1127)
- **Original**: Canto LXXI. Kabandha's Speech. 1109 Thus in calm strength which naught could shake The son of Da[aratha spake, With glory yet unstained Upon Sumitrá's son he bent His eyes, and firm in his intent His dauntless heart maintained. Canto LXXI. Kabandha's Speech. Kabandha saw each chieftain stand Imprisoned by his mighty hand, Which like a snare around him pressed And thus the royal pair addressed: “Why, warriors, are your glances bent On me whom hungry pangs torment? Why stand with wildered senses? Fate Has brought you now my maw to sate.” When Lakshma G heard, a while appalled, His ancient courage he recalled, And to his brother by his side With seasonable counsel cried:
- **Translation**: 

---

### Verse 3 (Ramayana 0.1128)
- **Original**: 1110 The Ramayana “This vilest of the giant race Will draw us to his side apace. Come, rouse thee; let the vengeful sword Smite off his arms, my honoured lord. This awful giant, vast of size, On his huge strength of arm relies, And o'er the world victorious, thus With mighty force would slaughter us. But in cold blood to slay, O King, Discredit on the brave would bring, As when some victim in the rite Shuns not the hand upraised to smite.” The monstrous fiend, to anger stirred, The converse of the brothers heard. His horrid mouth he opened wide And drew the princes to his side. They, skilled due time and place to note Unsheathed their glittering swords and smote, Till from the giant's shoulders they Had hewn the mighty arms away. His trenchant falchion Ráma plied And smote him on the better side, While valiant LakshmaG on the left The arm that held him prisoned cleft. Then to the earth dismembered fell The monster with a hideous yell, And like a cloud's his deep roar went Through earth and air and firmament. Then as the giant's blood flowed fast, On his cleft limbs his eye he cast, And called upon the princely pair Their names and lineage to declare. Him then the noble LakshmaG, blest
- **Translation**: 

---

### Verse 4 (Ramayana 0.1129)
- **Original**: Canto LXXI. Kabandha's Speech. 1111 With fortune's favouring marks, addressed, And told the fiend his brother's name And the high blood of which he came: “Ikshváku's heir here Ráma stands, Illustrious through a hundred lands. I, younger brother of the heir, O fiend, the name of LakshmaG bear. His mother stole his realm away And drove him forth in woods to stray. Thus through the mighty forest he Roamed with his royal wife and me. While glorious as a God he made His dwelling in the greenwood shade, Some giant stole away his dame, And seeking her we hither came. But tell me who thou art, and why With headless trunk that towered so high, With flaming face beneath thy chest, Thou liest crushed in wild unrest.” He heard the words that LakshmaG spoke, And memory in his breast awoke, Recalling Indra's words to mind He spoke in gentle tones and kind: “O welcome best of men, are ye Whom, blest by fate, this day I see. A blessing on each trenchant blade That low on earth these arms has laid! Thou, lord of men, incline thine ear The story of my woe to hear, While I the rebel pride declare Which doomed me to the form I wear.”
- **Translation**: 

---

### Verse 5 (Ramayana 0.1130)
- **Original**: 1112 The Ramayana Canto LXXII. Kabandha's Tale. “Lord of the mighty arm, of yore A shape transcending thought I wore, And through the triple world's extent My fame for might and valour went.[313] Scarce might the sun and moon on high, ScarceZakra, with my beauty vie. Then for a time this form I took, And the great world with trembling shook. The saints in forest shades who dwelt The terror of my presence felt. But once I stirred to furious rage Great Sthúla[iras, glorious sage. Culling in woods his hermit food My hideous shape with fear he viewed. Then forth his words of anger burst That bade me live a thing accursed: “Thou, whose delight is others' pain, This grisly form shalt still retain.” Then when I prayed him to relent And fix some term of punishment,— Prayed that the curse at length might cease, He bade me thus expect release: “Let Ráma cleave thine arms away And on the pyre thy body lay, And then shalt thou, set free from doom, Thine own fair shape once more assume.” O Lakshma G, hear my words: in me The world-illustrious Danu see. By Indra's curse, subdued in fight, I wear this form which scares the sight. By sternest penance long maintained
- **Translation**: 

---

### Verse 6 (Ramayana 0.1131)
- **Original**: Canto LXXII. Kabandha's Tale. 1113 The mighty Father's grace I gained. When length of days the God bestowed, With foolish pride my bosom glowed. My life, of lengthened years assured, I deemed fromZakra's might secured. Let by my senseless pride astray I challenged Indra to the fray. A flaming bolt with many a knot With his terrific arm he shot, And straight my head and thighs compressed Were buried in my bulky chest. Deaf to each prayer and piteous call He sent me not to Yáma's hall. “Thy prayers and cries,” he said“are vain: The Father's word must true remain.” “But how may lengthened life be spent By one the bolt has torn and rent? How can I live,” I cried,“unfed, With shattered face and thighs and head?” As thus I spoke his grace to crave, Arms each a league in length he gave, And opened in my chest beneath This mouth supplied with fearful teeth. So my huge arms I used to cast Round woodland creatures as they passed, And fed within the forest here On lion, tiger, pard, and deer. Then Indra spake to soothe my grief: “When Ráma and his brother chief From thy huge bulk those arms shall cleave, Then shall the skies thy soul receive.” Disguised in this terrific shape I let no woodland thing escape, And still my longing soul was pleased
- **Translation**: 

---

### Verse 7 (Ramayana 0.1132)
- **Original**: 1114 The Ramayana Whene'er my arms a victim seized, For in these arms I fondly thought Would Ráma's self at last be caught. Thus hoping, toiling many a day I yearned to cast my life away, And here, my lord, thou standest now: Blessings be thine! for none but thou Could cleave my arms with trenchant stroke: True are the words the hermit spoke. Now let me, best of warriors, lend My counsel, and thy plans befriend, And aid thee with advice in turn If thou with fire my corse wilt burn.” As thus the mighty Danu prayed With offer of his friendly aid, While LakshmaG gazed with anxious eye, The virtuous Ráma made reply: “Lakshma G and I through forest shade From Janasthán a while had strayed. When none was near her, RávaG came And bore away my glorious dame, The giant's form and size unknown, I learn as yet his name alone. Not yet the power and might we know Or dwelling of the monstrous foe. With none our helpless feet to guide We wander here by sorrow tried. Let pity move thee to requite Our service in the funeral rite. Our hands shall bring the boughs that, dry Where elephants have rent them, lie, Then dig a pit, and light the fire To burn thee as the laws require.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1133)
- **Original**: Canto LXXII. Kabandha's Tale. 1115 Do thou as meed of this declare Who stole my spouse, his dwelling where. O, if thou can, I pray thee say, And let this grace our deeds repay.” Danu had lent attentive ear The words which Ráma spoke to hear, And thus, a speaker skilled and tried, To that great orator replied: “No heavenly lore my soul endows, Naught know I of thy Maithil spouse. Yet will I, when my shape I wear, Him who will tell thee all declare. Then, Ráma, will my lips disclose His name who well that giant knows. But till the flames my corse devour This hidden knowledge mocks my power. For through that curse's withering taint My knowledge now is small and faint. Unknown the giant's very name Who bore away the Maithil dame. Cursed for my evil deeds I wore A shape which all the worlds abhor. Now ere with wearied steeds the sun Through western skies his course have run, Deep in a pit my body lay [314] And burn it in the wonted way. When in the grave my corse is placed, With fire and funeral honours graced, Then I, great chief, his name will tell Who knows the giant robber well. With him, who guides his life aright, In league of trusting love unite, And he, O valiant prince, will be
- **Translation**: 

---

### Verse 9 (Ramayana 0.1134)
- **Original**: 1116 The Ramayana A faithful friend and aid to thee. For, Ráma, to his searching eyes The triple world uncovered lies. For some dark cause of old, I ween, Through all the spheres his ways have been.” Canto LXXIII. Kabandha's Counsel. The monster ceased: the princely pair Heard great Kabandha's eager prayer. Within a mountain cave they sped, Where kindled fire with care they fed. Then LakshmaG in his mighty hands Brought ample store of lighted brands, And to a pile of logs applied The flame that ran from side to side. The spreading glow with gentle force Consumed Kabandha's mighty corse, Till the unresting flames had drunk The marrow of the monstrous trunk, As balls of butter melt away Amid the fires that o'er them play. Then from the pyre, like flame that glows Undimmed by cloudy smoke, he rose, In garments pure of spot or speck, A heavenly wreath about his neck. Resplendent in his bright attire He sprang exultant from the pyre. While from neck, arm, and foot was sent The flash of gold and ornament. High on a chariot, bright of hue,
- **Translation**: 

---

### Verse 10 (Ramayana 0.1135)
- **Original**: Canto LXXIII. Kabandha's Counsel. 1117 Which swans of fairest pinion drew, He filled each region of the air With splendid glow reflected there. Then in the sky he stayed his car And called to Ráma from afar: “Hear, chieftain, while my lips explain The means to win thy spouse again. Six plans, O prince, the wise pursue To reach the aims we hold in view.519 When evils ripening sorely press They load the wretch with new distress, So thou and LakshmaG, tried by woe, Have felt at last a fiercer blow, And plunged in bitterest grief to-day Lament thy consort torn away. There is no course but this: attend; Make, best of friends, that chief thy friend. Unless his prospering help thou gain Thy plans and hopes must all be vain. O Ráma, hear my words, and seek, Sugríva, for of him I speak. His brother Báli, Indra's son, Expelled him when the fight was won. With four great chieftains, faithful still, He dwells on Rishyamúka's hill.— Fair mountain, lovely with the flow Of Pampá's waves that glide below,— Lord of the Vánars520 just and true, Strong, very glorious, bright to view, Unmatched in counsel, firm and meek, Bound by each word his lips may speak, Good, splendid, mighty, bold and brave, 519 Peace, war, marching, halting, sowing dissensions, and seeking protection. 520 See Book I, Canto XVI.
- **Translation**: 

---

### Verse 11 (Ramayana 0.1136)
- **Original**: 1118 The Ramayana Wise in each plan to guide and save. His brother, fired by lust of sway, Drove forth the prince in woods to stray. In all thy search for Sítá he Thy ready friend and help will be. With him to aid thee in thy quest Dismiss all sorrow from thy breast. Time is a mighty power, and none His fixed decree can change or shun. So rich reward thy toil shall bless, And naught can stay thy sure success. Speed hence, O chief, without delay, To strong Sugríva take thy way. This hour thy footsteps onward bend, And make that mighty prince thy friend. With him before the attesting flame In solemn truth alliance frame. Nor wilt thou, if thy heart be wise, Sugríva, Vánar king, despise. Of boundless strength, all shapes he wears, He hearkens to a suppliant's prayers, And, grateful for each kindly deed, Will help and save in hour of need. And you, I ween, the power possess To aid his hopes and give redress. He, let his cause succeed or fail, Will help you, and you must prevail. A banished prince, in fear and woe He roams where Pampá's waters flow, True offspring of the Lord of Light Expelled by Báli's conquering might. Go, Raghu's son, that chieftain seek Who dwells on Rishyamúka's peak. Before the flame thy weapons cast
- **Translation**: 

---

### Verse 12 (Ramayana 0.1137)
- **Original**: Canto LXXIV. Kabandha's Death. 1119 And bind the bonds of friendship fast. For, prince of all the Vánar race, He in his wisdom knows each place Where dwell the fierce gigantic brood Who make the flesh of man their food. To him, O Raghu's son, to him Naught in the world is dark or dim, Where'er the mighty Day-God gleams Resplendent with a thousand beams. [315] He over rocky height and hill, Through gloomy cave, by lake and rill, Will with his Vánars seek the prize, And tell thee where thy lady lies. And he will send great chieftains forth To east and west and south and north, To seek the distant spot where she All desolate laments for thee. He even in RávaG's halls would find Thy Sítá, gem of womankind. Yea, if the blameless lady lay On Meru's loftiest steep, Or, far removed from light of day, Where hell is dark and deep, That chief of all the Vánar race His way would still explore, Meet the cowed giants face to face And thy dear spouse restore.” Canto LXXIV. Kabandha's Death.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1138)
- **Original**: 1120 The Ramayana When wise Kabandha thus had taught The means to find the dame they sought, And urged them onward in the quest, He thus again the prince addressed: “This path, O Raghu's son, pursue Where those fair trees which charm the view, Extending westward far away, The glory of their bloom display, Where their bright leaves Rose-apples show, And the tall Jak and Mango grow. Whene'er you will, those trees ascend, Or the long branches shake and bend, Their savoury fruit like Amrit eat, Then onward speed with willing feet. Beyond this shady forest, decked With flowering trees, your course direct. Another grove you then will find With every joy to take the mind, Like Nandan with its charms displayed, Or Northern Kuru's blissful shade; Where trees distil their balmy juice, And fruit through all the year produce; Where shades with seasons ever fair With Chaitraratha may compare: Where trees whose sprays with fruit are bowed Rise like a mountain or a cloud. There, when you list, from time to time, The loaded trees may LakshmaG climb, Or from the shaken boughs supply Sweet fruit that may with Amrit vie. The onward path pursuing still From wood to wood, from hill to hill, Your happy eyes at length will rest
- **Translation**: 

---

### Verse 14 (Ramayana 0.1139)
- **Original**: Canto LXXIV. Kabandha's Death. 1121 On Pampá's lotus-covered breast. Her banks with gentle slope descend, Nor stones nor weed the eyes offend, And o'er smooth beds of silver sand Lotus and lily blooms expand. There swans and ducks and curlews play, And keen-eyed ospreys watch their prey, And from the limpid waves are heard Glad notes of many a water-bird. Untaught a deadly foe to fear They fly not when a man is near, And fat as balls of butter they Will, when you list, your hunger stay. Then LakshmaG with his shafts will take The fish that swim the brook and lake, Remove each bone and scale and fin, Or strip away the speckled skin, And then on iron skewers broil For thy repast the savoury spoil. Thou on a heap of flowers shalt rest And eat the meal his hands have dressed, There shalt thou lie on Pampá's brink, And Lakshma G's hand shall give thee drink, Filling a lotus leaf with cool Pure water from the crystal pool, To which the opening blooms have lent The riches of divinest scent. Beside thee at the close of day Will LakshmaG through the woodland stray, And show thee where the monkeys sleep In caves beneath the mountain steep. Loud-voiced as bulls they forth will burst And seek the flood, oppressed by thirst; Then rest a while, their wants supplied,
- **Translation**: 

---

### Verse 15 (Ramayana 0.1140)
- **Original**: 1122 The Ramayana Their well-fed bands on Pampá's side. Thou roving there at eve shalt see Rich clusters hang on shrub and tree, And Pampá flushed with roseate glow, And at the view forget thy woe. There shalt thou mark with strange delight Each loveliest flower that blooms by night, While lily buds that shrink from day Their tender loveliness display. In that far wild no hand but thine Those peerless flowers in wreaths shall twine: Immortal in their changeless pride, Ne'er fade those blooms and ne'er are dried. There erst on holy thoughts intent Their days Matanga's pupils spent. Once for their master food they sought, And store of fruit and berries brought. Then as they laboured through the dell From limb and brow the heat-drops fell: Thence sprang and bloomed those wondrous trees: Such holy power have devotees. Thus, from the hermits' heat-drops sprung, Their growth is ever fresh and young. ThereZavarí is dwelling yet, Who served each vanished anchoret.[316] Beneath the shade of holy boughs That ancient votaress keeps her vows. Her happy eyes on thee will fall, O godlike prince, adored by all, And she, whose life is pure from sin, A blissful seat in heaven will win. But cross, O son of Raghu, o'er, And stand on Pampá's western shore. A tranquil hermitage that lies
- **Translation**: 

---

### Verse 16 (Ramayana 0.1141)
- **Original**: Canto LXXIV. Kabandha's Death. 1123 Deep in the woods will meet thine eyes. No wandering elephants invade The stillness of that holy shade, But checked by saint Matanga's power They spare each consecrated bower. Through many an age those trees have stood World-famous as Matanga's wood Still, Raghu's son, pursue thy way: Through shades where birds are vocal stray, Fair as the blessed wood where rove Immortal Gods, or Nandan's grove. Near Pampá eastward, full in sight, Stands Rishyamúka's wood-crowned height. 'Tis hard to climb that towering steep Where serpents unmolested sleep. The free and bounteous, formed of old By Brahmá of superior mould, Who sink when day is done to rest Reclining on that mountain crest,— What wealth or joy in dreams they view, Awaking find the vision true. But if a villain stained with crime That holy hill presume to climb, The giants in their fury sweep From the hill top the wretch asleep. There loud and long is heard the roar Of elephants on Pampá's shore, Who near Matanga's dwelling stray And in those waters bathe and play. A while they revel by the flood, Their temples stained with streams like blood, Then wander far away dispersed, Dark as huge clouds before they burst. But ere they part they drink their fill
- **Translation**: 

---

### Verse 17 (Ramayana 0.1142)
- **Original**: 1124 The Ramayana Of bright pure water from the rill, Delightful to the touch, where meet Scents of all flowers divinely sweet, Then speeding from the river side Deep in the sheltering thicket hide. Then bears and tigers shalt thou view Whose soft skins show the sapphire's hue, And silvan deer that wander nigh Shall harmless from thy presence fly. High in that mountain's wooded side Is a fair cavern deep and wide, Yet hard to enter: piles of rock The portals of the cavern block.521 Fast by the eastern door a pool Gleams with broad waters fresh and cool, Where stores of roots and fruit abound, And thick trees shade the grassy ground. This mountain cave the virtuous-souled Sugríva, and his Vánars hold, And oft the mighty chieftain seeks The summits of those towering peaks.” Thus spake Kabandha high in air His counsel to the royal pair. Still on his neck that wreath he bore, And radiance like the sun's he wore. Their eyes the princely brothers raised And on that blissful being gazed: “Behold, we go: no more delay; Begin,” they cried,“thy heavenward way.” “Depart,” Kabandha's voice replied, “Pursue your search, and bliss betide.” 521 Or as the commentator Tírtha says,Zilápidháná, rock-covered, may be the name of the cavern.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1143)
- **Original**: Canto LXXV. Savarí. 1125 Thus to the happy chiefs he said, Then on his heavenward journey sped. Thus once again Kabandha won A shape that glittered like the sun Without a spot or stain. Thus bade he Ráma from the air To great Sugríva's side repair His friendly love to gain. Canto LXXV. Savarí. Thus counselled by their friendly guide On through the wood the princes hied, Pursuing still the eastern road To Pampá which Kabandha showed, Where trees that on the mountains grew With fruit like honey charmed the view. They rested weary for the night Upon a mountain's wooded height, Then onward with the dawn they hied And stood on Pampá's western side, Where Zavarí's fair home they viewed Deep in that shady solitude. The princes reached the holy ground Where noble trees stood thick around, And joying in the lovely view Near to the aged votaress drew. To meet the sons of Raghu came, With hands upraised, the pious dame, And bending low with reverence meet Welcomed them both and pressed their feet.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1144)
- **Original**: 1126 The Ramayana Then water, as beseems, she gave, Their lips to cool, their feet to lave. To that pure saint who never broke One law of duty Ráma spoke: “I trust no cares invade thy peace, While holy works and zeal increase; That thou content with scanty food All touch of ire hast long subdued; That all thy vows are well maintained[317] While peace of mind is surely gained, That reverence of the saints who taught Thy faithful heart due fruit has brought.” The aged votaress pure of taint, Revered by every perfect saint, Rose to her feet by Ráma's side And thus in gentle tones replied: “My penance meed this day I see Complete, my lord, in meeting thee. This day the fruit of birth I gain, Nor have I served the saints in vain. I reap rich fruits of toil and vow, And heaven itself awaits me now, When I, O chief of men, have done Honour to thee the godlike one. I feel, great lord, thy gentle eye My earthly spirit purify, And I, brave tamer of thy foes, Shall through thy grace in bliss repose. Thy feet by Chitrakúma strayed When those great saints whom I obeyed, In dazzling chariots bright of hue, Hence to their heavenly mansions flew.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1145)
- **Original**: Canto LXXV. Savarí. 1127 As the high saints were borne away I heard their holy voices say: “In this pure grove, O devotee, Prince Ráma soon will visit thee. When he and LakshmaG seek this shade, Be to thy guests all honour paid. Him shalt thou see, and pass away To those blest worlds which ne'er decay.” To me, O mighty chief, the best Of lofty saints these words addressed. Laid up within my dwelling lie Fruits of each sort which woods supply,— Food culled for thee in endless store From every tree on Pampá's shore.” Thus to her virtuous guest she sued And he, with heavenly lore endued, Words such as these in turn addressed To her with equal knowledge blest: “Danu himself the power has told Of thy great masters lofty-souled. Now if thou will, mine eyes would fain Assurance of their glories gain.” She heard the prince his wish declare: Then rose she, and the royal pair Of brothers through the wood she led That round her holy dwelling spread. “Behold Matanga's wood” she cried, “A grove made famous far and wide. Dark as thick clouds and filled with herds Of wandering deer, and joyous birds. In this pure spot each reverend sire With offerings fed the holy fire.
- **Translation**: 

---



--- End of Ramayan_batch_155.md ---


--- Start of Ramayan_batch_156.md ---

# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Ramayana 0.1146)
- **Original**: 1128 The Ramayana See here the western altar stands Where daily with their trembling hands The aged saints, so long obeyed By me, their gifts of blossoms laid. The holy power, O Raghu's son, By their ascetic virtue won, Still keeps their well-loved altar bright, Filling the air with beams of light. And those seven neighbouring lakes behold Which, when the saints infirm and old, Worn out by fasts, no longer sought, Moved hither drawn by power of thought. Look, Ráma, where the devotees Hung their bark mantles on the trees, Fresh from the bath: those garments wet Through many a day are dripping yet. See, through those aged hermits' power The tender spray, this bright-hued flower With which the saints their worship paid, Fresh to this hour nor change nor fade. Here thou hast seen each lawn and dell, And heard the tale I had to tell: Permit thy servant, lord, I pray, To cast this mortal shell away, For I would dwell, this life resigned, With those great saints of lofty mind, Whom I within this holy shade With reverential care obeyed.” When Ráma and his brother heard The pious prayer the dame preferred, Filled full of transport and amazed They marvelled as her words they praised. Then Ráma to the votaress said
- **Translation**: 

---

### Verse 2 (Ramayana 0.1147)
- **Original**: Canto LXXVI. Pampá. 1129 Whose holy vows were perfected: “Go, lady, where thou fain wouldst be, O thou who well hast honoured me.” Her locks in hermit fashion tied, Clad in bark coat and black deer-hide, When Ráma gave consent, the dame Resigned her body to the flame. Then like the fire that burns and glows, To heaven the sainted lady rose, In all her heavenly garments dressed, Immortal wreaths on neck and breast, Bright with celestial gems she shone Most beautiful to look upon, And like the flame of lightning sent A glory through the firmament. That holy sphere the dame attained, By depth of contemplation gained, Where roam high saints with spirits pure In bliss that shall for aye endure. Canto LXXVI. Pampá. When Zavarí had sought the skies And gained her splendid virtue's prize, Ráma with LakshmaG stayed to brood O'er the strange scenes their eyes had viewed. His mind upon those saints was bent, For power and might preëminent And he to musing LakshmaG spoke The thoughts that in his bosom woke: [318]
- **Translation**: 

---

### Verse 3 (Ramayana 0.1148)
- **Original**: 1130 The Ramayana “Mine eyes this wondrous home have viewed Of those great saints with souls subdued, Where peaceful tigers dwell and birds, And deer abound in heedless herds. Our feet upon the banks have stood Of those seven lakes within the wood, Where we have duly dipped, and paid Libations to each royal shade. Forgotten now are thoughts of ill And joyful hopes my bosom fill. Again my heart is light and gay And grief and care have passed away. Come, brother, let us hasten where Bright Pampá's flood is fresh and fair, And towering in their beauty near Mount Rishyamúka's heights appear, Which, offspring of the Lord of Light, Still fearing Báli's conquering might, With four brave chiefs of Vánar race Sugríva makes his dwelling-place. I long with eager heart to find That leader of the Vánar kind, For on that chief my hopes depend That this our quest have prosperous end.” Thus Ráma spoke, in battle tried, And thus Sumitrá's son replied: “Come, brother, come, and speed away: My spirit brooks no more delay.” Thus spake Sumitrá's son, and then Forth from the grove the king of men With his dear brother by his side To Pampá's lucid waters hied. He gazed upon the woods where grew
- **Translation**: 

---

### Verse 4 (Ramayana 0.1149)
- **Original**: Canto LXXVI. Pampá. 1131 Trees rich in flowers of every hue. From brake and dell on every side The curlew and the peacock cried, And flocks of screaming parrots made Shrill music in the bloomy shade. His eager eyes, as on he went, On many a pool and tree were bent. Inflamed with love he journeyed on Till a fair flood before him shone. He stood upon the water's side Which streams from distant hills supplied: Matanga's name that water bore: There bathed he from the shelving shore. Then, each on earnest thoughts intent, Still farther on their way they went. But Ráma's heart once more gave way Beneath his grief and wild dismay. Before him lay the noble flood Adorned with many a lotus bud. On its fair banks A[oka glowed, And all bright trees their blossoms showed. Green banks that silver waves confined With lovely groves were fringed and lined. The crystal waters in their flow Showed level sands that gleamed below. There glittering fish and tortoise played, And bending trees gave pleasant shade. There creepers on the branches hung With lover-like embraces clung. There gay Gandharvas loved to meet, And Kinnars sought the calm retreat. There wandering Yakshas found delight, Snake-gods and rovers of the night. Cool were the pleasant waters, gay
- **Translation**: 

---

### Verse 5 (Ramayana 0.1150)
- **Original**: 1132 The Ramayana Each tree with creeper, flower, and spray. There flushed the lotus darkly red, Here their white glory lilies spread, Here sweet buds showed their tints of blue: So carpets gleam with many a hue. A grove of Mangoes blossomed nigh, Echoing with the peacock's cry. When Ráma by his brother's side The lovely flood of Pampá eyed, Decked like a beauty, fair to see With every charm of flower and tree, His mighty heart with woe was rent And thus he spoke in wild lament “Here, LakshmaG, on this beauteous shore, Stands, dyed with tints of many an ore, The mountain Rishyamúka bright With flowery trees that crown each height. Sprung from the chief who, famed of yore, The name of Riksharajas bore, Sugríva, chieftain strong and dread, Dwells on that mountain's towering head. Go to him, best of men, and seek That prince of Vánars on the peak, I cannot longer brook my pain, Or, Sítá lost, my life retain.” Thus by the pangs of love distressed, His thoughts on Sítá bent, His faithful brother he addressed, And cried in wild lament. He reached the lovely ground that lay On Pampá's wooded side, And told in anguish and dismay, The grief he could not hide.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1151)
- **Original**: Canto LXXVI. Pampá. 1133 With listless footsteps faint and slow His way the chief pursued, Till Pampá with her glorious show Of flowering woods he viewed. Through shades where every bird was found The prince with LakshmaG passed, And Pampá with her groves around Burst on his eyes at last. [319]
- **Translation**: 

---

### Verse 7 (Ramayana 0.1152)
- **Original**: BOOK IV. Canto I. Ráma's Lament. The princes stood by Pampá's side522 Which blooming lilies glorified. With troubled heart and sense o'erthrown There Ráma made his piteous moan. As the fair flood before him lay The reason of the chief gave way; And tender thoughts within him woke, As to Sumitrá's son he spoke: 522 Pampá is said by the commentator to be the name both of a lake and a brook which flows into it. The brook is said to rise in the hill Rishyamúka.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1153)
- **Original**: Canto I. Ráma's Lament. 1135 “How lovely Pampá's waters show, Where streams of lucid crystal flow! What glorious trees o'erhang the flood Which blooms of opening lotus stud! Look on the banks of Pampá where Thick groves extend divinely fair; And piles of trees, like hills in size, Lift their proud summits to the skies. But thought of Bharat's523 pain and toil, And my dear spouse the giant's spoil, Afflict my tortured heart and press My spirit down with heaviness. Still fair to me though sunk in woe Bright Pampá and her forest show. Where cool fresh waters charm the sight, And flowers of every hue are bright. The lotuses in close array Their passing loveliness display, And pard and tiger, deer and snake Haunt every glade and dell and brake. Those grassy spots display the hue Of topazes and sapphires' blue, And, gay with flowers of every dye, With richly broidered housings vie. What loads of bloom the high trees crown, Or weigh the bending branches down! And creepers tipped with bud and flower Each spray and loaded limb o'erpower. Now cool delicious breezes blow, And kindle love's voluptuous glow, When balmy sweetness fills the air, And fruit and flowers and trees are fair. 523 Who was acting as Regent for Ráma and leading an ascetic life while he mourned for his absent brother.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1154)
- **Original**: 1136 The Ramayana Those waving woods, that shine with bloom, Each varied tint in turn assume. Like labouring clouds they pour their showers In rain or ever-changing flowers. Behold, those forest trees, that stand High upon rock and table-land, As the cool gales their branches bend, Their floating blossoms downward send. See, LakshmaG, how the breezes play With every floweret on the spray. And sport in merry guise with all The fallen blooms and those that fall. See, brother, where the merry breeze Shakes the gay boughs of flowery trees, Disturbed amid their toil a throng Of bees pursue him, loud in song. The Koïls,524 mad with sweet delight, The bending trees to dance invite; And in its joy the wild wind sings As from the mountain cave he springs. On speed the gales in rapid course, And bend the woods beneath their force, Till every branch and spray they bind In many a tangled knot entwined. What balmy sweets those gales dispense With cool and sacred influence! Fatigue and trouble vanish: such The magic of their gentle touch. Hark, when the gale the boughs has bent In woods of honey redolent, Through all their quivering sprays the trees Are vocal with the murmuring bees. 524 The Indian Cuckoo.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1155)
- **Original**: Canto I. Ráma's Lament. 1137 The hills with towering summits rise, And with their beauty charm the eyes, Gay with the giant trees which bright With blossom spring from every height: And as the soft wind gently sways The clustering blooms that load the sprays, The very trees break forth and sing With startled wild bees' murmuring. Thine eyes to yonder Cassias525 turn Whose glorious clusters glow and burn. [320] Those trees in yellow robes behold, Like giants decked with burnished gold. Ah me, Sumitrá's son, the spring Dear to sweet birds who love and sing, Wakes in my lonely breast the flame Of sorrow as I mourn my dame. Love strikes me through with darts of fire, And wakes in vain the sweet desire. Hark, the loud Koïl swells his throat, And mocks me with his joyful note. I hear the happy wild-cock call Beside the shady waterfall. His cry of joy afflicts my breast By love's absorbing might possessed. My darling from our cottage heard One morn in spring this shrill-toned bird, And called me in her joy to hear The happy cry that charmed her ear. 525 The Cassia Fistula or Amaltás is a splendid tree like a giant laburnum covered with a profusion of chains and tassels of gold. Dr. Roxburgh well describes it as“uncommonly beautiful when in flower, few trees surpassing it in the elegance of its numerous long pendulous racemes of large bright-yellow flowers intermixed with the young lively green foliage.” It is remarkable also for its curious cylindrical black seed-pods about two feet long, which are called monkeys' walking-sticks.
- **Translation**: 

---

### Verse 11 (Ramayana 0.1156)
- **Original**: 1138 The Ramayana See, birds of every varied voice Around us in the woods rejoice, On creeper, shrub, and plant alight, Or wing from tree to tree their flight. Each bird his kindly mate has found, And loud their notes of triumph sound, Blending in sweetest music like The distant warblings of the shrike. See how the river banks are lined With birds of every hue and kind. Here in his joy the Koïl sings, There the glad wild-cock flaps his wings. The blooms of bright A[okas526 where The song of wild bees fills the air, And the soft whisper of the boughs Increase my longing for my spouse. The vernal flush of flower and spray Will burn my very soul away. What use, what care have I for life If I no more may see my wife Soft speaker with the glorious hair, And eyes with silken lashes fair? Now is the time when all day long 526 “The Jonesia Asoca is a tree of considerable size, native of southern India. It blossoms in February and March with large erect compact clusters of flowers, varying in colour from pale-orange to scarlet, almost to be mistaken, on a hasty glance, for immense trusses of bloom of an Ixora. Mr. Fortune considered this tree, when in full bloom, superior in beauty even to the Amherstia. The first time I saw the Asoc in flower was on the hill where the famous rock-cut temple of Kárlí is situated, and a large concourse of natives had assembled for the celebration of some Hindoo festival. Before proceeding to the temple the Mahratta women gathered from two trees, which were flowering somewhat below, each a fine truss of blossom, and inserted it in the hair at the back of her head.… As they moved about in groups it is impossible to imagine a more delightful effect than the rich scarlet bunches of flowers presented on their fine glossy jet-black hair.” FIRMINGER {FNS ,Gardening for India.
- **Translation**: 

---

### Verse 12 (Ramayana 0.1157)
- **Original**: Canto I. Ráma's Lament. 1139 The Koïls fill the woods with song. And gardens bloom at spring's sweet touch Which my beloved loved so much. Ah me, Sumitrá's son, the fire Of sorrow, sprung from soft desire, Fanned by the charms the spring time shows, Will burn my heart and end my woes, Whose sad eyes look on each fair tree, But my sweet love no more may see. Ah me, Ah me, from hour to hour Love in my soul will wax in power, And spring, upon whose charms I gaze, Whose breath the heat of toil allays, With thoughts of her for whom I strain My hopeless eyes, increase my pain. As fire in summer rages through The forests thick with dry bamboo, So will my fawn eyed love consume My soul o'erwhelmed with thoughts of gloom. Behold, beneath each spreading tree The peacocks dance527 in frantic glee, And, stirred by all the gales that blow, Their tails with jewelled windows glow, Each bird, in happy love elate, Rejoices with his darling mate. But sights like these of joy and peace My pangs of hopeless love increase. See on the mountain slope above The peahen languishing with love. Behold her now in amorous dance Close to her consort's side advance. 527 No other word can express the movements of peafowl under the influence of pleasing excitement, especially when after the long drought they hear the welcome roar of the thunder and feel that the rain is near.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1158)
- **Original**: 1140 The Ramayana He with a laugh of joy and pride Displays his glittering pinions wide; And follows through the tangled dell The partner whom he loves so well. Ah happy bird! no giant's hate Has robbed him of his tender mate; And still beside his loved one he Dances beneath the shade in glee. Ah, in this month when flowers are fair My widowed woe is hard to bear. See, gentle love a home may find In creatures of inferior kind. See how the peahen turns to meet Her consort now with love-drawn feet.[321] So, LakshmaG, if my large-eyed dear, The child of Janak still were here, She, by love's thrilling influence led, Upon my breast would lay her head. These blooms I gathered from the bough Without my love are useless now. A thousand blossoms fair to see With passing glory clothe each tree That hangs its cluster-burthened head Now that the dewy months528 are fled, But, followed by the bees that ply Their fragrant task, they fall and die. A thousand birds in wild delight Their rapture-breathing notes unite; Bird calls to bird in joyous strain, And turns my love to frenzied pain. O, if beneath those alien skies, There be a spring where Sítá lies, 528 The Dewy Season is one of the six ancient seasons of the Indian year, lasting from the middle of January to the middle of March.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1159)
- **Original**: Canto I. Ráma's Lament. 1141 I know my prisoned love must be Touched with like grief, and mourn with me. But ah, methinks that dreary clime Knows not the touch of spring's sweet time. How could my black eyed love sustain, Without her lord, so dire a pain? Or if the sweet spring come to her In distant lands a prisoner, How may his advent and her met On every side with taunt and threat? Ah, if the springtide's languor came With soft enchantment o'er my dame, My darling of the lotus eye, My gently speaking love, would die; For well my spirit knows that she Can never live bereft of me With love that never wavered yet My Sítá's heart, on me is set, Who, with a soul that ne'er can stray, With equal love her love repay. In vain, in vain the soft wind brings Sweet blossoms on his balmy wings; Delicious from his native snow, To me like fire he seems to glow. O, how I loved a breeze like this When darling Sítá shared the bliss! But now in vain for me it blows To fan the fury of my woes. That dark-winged bird that sought the skies Foretelling grief with warning cries, Sits on the tree where buds are gay, And pours glad music from the spray. That rover of the fields of air Will aid my love with friendly care,
- **Translation**: 

---

### Verse 15 (Ramayana 0.1160)
- **Original**: 1142 The Ramayana And me with gracious pity guide To my large-eyed Videhan's side.529 Hark, LakshmaG, how the woods around With love-inspiring chants resound, Where birds in every bloom-crowned tree Pour forth their amorous minstrelsy. As though an eager gallant wooed A gentle maid by love subdued, Enamoured of her flowers the bee Darts at the wind-rocked Tila tree.530 A [oka, brightest tree that grows, That lends a pang to lovers' woes, Hangs out his gorgeous bloom in scorn And mocks me as I weep forlorn. O Lakshma G, turn thine eye and see Each blossom-laden Mango tree, Like a young lover gaily dressed Whom fond desire forbids to rest. Look, son of Queen Sumitrá through The forest glades of varied hue, Where blooms are bright and grass is green The Kinnars531 with their loves are seen. See, brother, see where sweet and bright Those crimson lilies charm the sight, And o'er the flood a radiance throw Fair as the morning's roseate glow. See, Pampá, most divinely sweet, 529 Ráma appears to mean that on a former occasion a crow flying high over- head was an omen that indicated his approaching separation from Sítá; and that now the same bird's perching on a tree near him may be regarded as a happy augury that she will soon be restored to her husband. 530 A tree with beautiful and fragrant blossoms. 531 A race of semi-divine musicians attached to the service of Kuvera, repre- sented as centaurs reversed with human figures and horses' heads.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1161)
- **Original**: Canto I. Ráma's Lament. 1143 The swan's and mallard's loved retreat, Shows her glad waters bright and clear, Where lotuses their heads uprear From the pure wave, and charm the view With mingled tints of red and blue. Each like the morning's early beams Reflected in the crystal gleams; And bees on their sweet toil intent Weigh down each tender filament. There with gay lawns the wood recedes; There wildfowl sport amid the reeds, There roedeer stand upon the brink, And elephants descend to drink. The rippling waves which winds make fleet Against the bending lilies beat, And opening bud and flower and stem Gleam with the drops that hang on them. Life has no pleasure left for me While my dear queen I may not see, [322] Who loved so well those blooms that vie With the full splendour of her eye. O tyrant Love, who will not let My bosom for one hour forget The lost one whom I yearn to meet, Whose words were ever kind and sweet. Ah, haply might my heart endure This hopeless love that knows not cure, If spring with all his trees in flower Assailed me not with ruthless power. Each lovely scene, each sound and sight Wherein, with her, I found delight, Has lost the charm so sweet of yore, And glads my widowed heart no more. On lotus buds I seem to gaze,
- **Translation**: 

---

### Verse 17 (Ramayana 0.1162)
- **Original**: 1144 The Ramayana Or blooms that deck Palá[a532 sprays;533 But to my tortured memory rise The glories of my darling's eyes. Cool breezes through the forest stray Gathering odours on their way, Enriched with all the rifled scent Of lotus flower and filament. Their touch upon my temples falls And Sítá's fragrant breath recalls. Now look, dear brother, on the right Of Pampá towers a mountain height Where fairest Cassia trees unfold The treasures of their burnished gold. Proud mountain king! his woody side With myriad ores is decked and dyed, And as the wind-swept blossoms fall Their fragrant dust is stained with all. To yon high lands thy glances turn: With pendent fire they flash and burn, Where in their vernal glory blaze Palá[a flowers on leafless sprays. O Lakshma G, look! on Pampá's side What fair trees rise in blooming pride! 532 Butea Frondosa. A tree that bears a profusion of brilliant red flowers which appear before the leaves. 533 I omit five[lokaswhich contain nothing but a list of trees for which, with one or two exceptions, there are no equivalent names in English. The following is Gorresio's translation of the corresponding passage in the Bengal recension:— “Oh come risplendono in questa stagione di primavera i vitici, le galedupe, le bassie, le dalbergie, i diospyri… le tile, le michelie, le rottlerie, le pentaptere ed i pterospermi, i bombaci, le grislee, gli abri, gli amaranti e le dalbergie; i sirii, le galedupe, le barringtonie ed i palmizi, i xanthocymi, il pepebetel, le verbosine e le ticaie, le nauclee le erythrine, gli asochi, e le tapie fanno d'ogni intorno pompa de' lor fiori.”
- **Translation**: 

---

### Verse 18 (Ramayana 0.1163)
- **Original**: Canto I. Ráma's Lament. 1145 What climbing plants above them show Or hang their flowery garlands low! See how the amorous creeper rings The wind-rocked trees to which she clings, As though a dame by love impelled With clasping arms her lover held. Drunk with the varied scents that fill The balmy air, from hill to hill, From grove to grove, from tree to tree, The joyous wind is wandering free. These gay trees wave their branches bent By blooms, of honey redolent. There, slowly opening to the day, Buds with dark lustre deck the spray. The wild bee rests a moment where Each tempting flower is sweet and fair, Then, coloured by the pollen dyes, Deep in some odorous blossom lies. Soon from his couch away he springs: To other trees his course he wings, And tastes the honeyed blooms that grow Where Pampá's lucid waters flow. See, LakshmaG, see, how thickly spread With blossoms from the trees o'erhead, That grass the weary traveller woos With couches of a thousand hues, And beds on every height arrayed With red and yellow tints are laid, No longer winter chills the earth: A thousand flowerets spring to birth, And trees in rivalry assume Their vernal garb of bud and bloom. How fair they look, how bright and gay With tasselled flowers on every spray!
- **Translation**: 

---

### Verse 19 (Ramayana 0.1164)
- **Original**: 1146 The Ramayana While each to each proud challenge flings Borne in the song the wild bee sings. That mallard by the river edge Has bathed amid the reeds and sedge: Now with his mate he fondly plays And fires my bosom as I gaze. Mandákiní534 is far renowned: No lovelier flood on earth is found; But all her fairest charms combined In this sweet stream enchant the mind. O, if my love were here to look With me upon this lovely brook, Never for Ayodhyá would I pine, Or wish that Indra's lot were mine. If by my darling's side I strayed O'er the soft turf which decks the glade, Each craving thought were sweetly stilled, Each longing of my soul fulfilled. But, now my love is far away, Those trees which make the woods so gay, In all their varied beauty dressed, Wake thoughts of anguish in my breast. That lotus-covered stream behold Whose waters run so fresh and cold,[323] 534 A sacred stream often mentioned in the course of the poem. See Book II, Canto XCV.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1165)
- **Original**: Canto I. Ráma's Lament. 1147 Sweet rill, the wildfowl's loved resort, Where curlew, swan, and diver sport; Where with his consort plays the drake, And tall deer love their thirst to slake, While from each woody bank is heard The wild note of each happy bird. The music of that joyous quire Fills all my soul with soft desire; And, as I hear, my sad thoughts fly To Sítá of the lotus eye, Whom, lovely with her moonbright cheek, In vain mine eager glances seek. Now turn, those chequered lawns survey Where hart and hind together stray. Ah, as they wander at their will My troubled breast with grief they fill, While torn by hopeless love I sigh For Sítá of the fawn-like eye. If in those glades where, touched by spring, Gay birds their amorous ditties sing, Mine own beloved I might see, Then, brother, it were well with me: If by my side she wandered still, And this cool breeze that stirs the rill Touched with its gentle breath the brows Of mine own dear Videhan spouse. For, LakshmaG, O how blest are those On whom the breath of Pampá blows, Dispelling all their care and gloom With sweets from where the lilies bloom! How can my gentle love remain Alive amid the woe and pain, Where prisoned far away she lies,— My darling of the lotus eyes?
- **Translation**: 

---



--- End of Ramayan_batch_156.md ---


--- Start of Ramayan_batch_157.md ---

# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Ramayana 0.1166)
- **Original**: 1148 The Ramayana How shall I dare her sire to greet Whose lips have never known deceit? How stand before the childless king And meet his eager questioning? When banished by my sire's decree, In low estate, she followed me. So pure, so true to every vow, Where is my gentle darling now? How can I bear my widowed lot, And linger on where she is not, Who followed when from home I fled Distracted, disinherited? My spirit sinks in hopeless pain When my fond glances yearn in vain For that dear face with whose bright eye The worshipped lotus scarce can vie. Ah when, my brother, shall I hear That voice that rang so soft and clear, When, sweetly smiling as she spoke, From her dear lips gay laughter broke? When worn with toil and love I strayed With Sítá through the forest shade, No trace of grief was seen in her, My kind and thoughtful comforter. How shall my faltering tongue relate To Queen Kau[alyá Sítá's fate? How answer when in wild despair She questions, Where is Sítá, where? Haste, brother, haste: to Bharat hie, On whose fond love I still rely. My life can be no longer borne, Since Sítá from my side is torn.”
- **Translation**: 

---

### Verse 2 (Ramayana 0.1167)
- **Original**: Canto I. Ráma's Lament. 1149 Thus like a helpless mourner, bent By sorrow, Ráma made lament; And with wise counsel LakshmaG tried To soothe his care, and thus replied: “O best of men, thy grief oppose, Nor sink beneath thy weight of woes. Not thus despond the great and pure And brave like thee, but still endure. Reflect what anguish wrings the heart When loving souls are forced to part; And, mindful of the coming pain, Thy love within thy breast restrain. For earth, though cooled by wandering streams, Lies scorched beneath the midday beams. RávaG his steps to hell may bend, Or lower yet in flight descend; But be thou sure, O Raghu's son, Avenging death he shall not shun. Rise, Ráma, rise: the search begin, And track the giant foul with sin. Then shall the fiend, though far he fly, Resign his prey or surely die. Yea, though the trembling monster hide With Sítá close to Diti's535 side, E'en there, unless he yield the prize, Slain by this wrathful hand he dies. Thy heart with strength and courage stay, And cast this weakling mood away. Our fainting hopes in vain revive Unless with firm resolve we strive. The zeal that fires the toiler's breast 535 A daughter of Daksha who became one of the wives of Ka[yapa and mother of the Daityas. She is termed the general mother of Titans and malignant beings. See Book I Cantos XLV, XLVI.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1168)
- **Original**: 1150 The Ramayana Mid earthly powers is first and best. Zeal every check and bar defies, And wins at length the loftiest prize, In woe and danger, toil and care, Zeal never yields to weak despair. With zealous heart thy task begin, And thou once more thy spouse shalt win. Cast fruitless sorrow from thy soul, Nor let this love thy heart control. Forget not all thy sacred lore, But be thy noble self once more.” He heard, his bosom rent by grief, The counsel of his brother chief; Crushed in his heart the maddening pain, And rose resolved and strong again. Then forth upon his journey went The hero on his task intent, Nor thought of Pampá's lovely brook,[324] Or trees which murmuring breezes shook, Though on dark woods his glances fell, On waterfall and cave and dell; And still by many a care distressed The son of Raghu onward pressed. As some wild elephant elate Moves through the woods in pride, So LakshmaG with majestic gait Strode by his brother's side. He, for his lofty spirit famed, Admonished and consoled; Showed Raghu's son what duty claimed, And bade his heart be bold. Then as the brothers strode apace To Rishyamúka's height,
- **Translation**: 

---

### Verse 4 (Ramayana 0.1169)
- **Original**: Canto II. Sugríva's Alarm. 1151 The sovereign of the Vánar race536 Was troubled at the sight. As on the lofty hill he strayed He saw the chiefs draw near: A while their glorious forms surveyed, And mused in restless fear. His slow majestic step he stayed And gazed upon the pair. And all his spirit sank dismayed By fear too great to bear. When in their glorious might the best Of royal chiefs came nigh, The Vánars in their wild unrest Prepared to turn and fly. They sought the hermit's sacred home537 For peace and bliss ordained, And there, where Vánars loved to roam, A sure asylum gained. Canto II. Sugríva's Alarm. Sugríva moved by wondering awe The high-souled sons of Raghu saw, In all their glorious arms arrayed; And grief upon his spirit weighed. 536 Sugríva, the ex-king of the Vánars, foresters, or monkeys, an exile from his home, wandering about the mountain Rishyamúka with his four faithful ex-ministers. 537 The hermitage of the Saint Matanga which his curse prevented Báli, the present king of the Vánars, from entering. The story is told at length in Canto XI of this Book.
- **Translation**: 

---

### Verse 5 (Ramayana 0.1170)
- **Original**: 1152 The Ramayana To every quarter of the sky He turned in fear his anxious eye, And roving still from spot to spot With troubled steps he rested not. He durst not, as he viewed the pair, Resolve to stand and meet them there; And drooping cheer and quailing breast The terror of the chief confessed. While the great fear his bosom shook, Brief counsel with his lords he took; Each gain and danger closely scanned, What hope in flight, what power to stand, While doubt and fear his bosom rent, On Raghu's sons his eyes he bent, And with a spirit ill at ease Addressed his lords in words like these: “Those chiefs with wandering steps invade The shelter of our pathless shade, And hither come in fair disguise Of hermit garb as Báli's spies.” Each lord beheld with troubled heart Those masters of the bowman's art, And left the mountain side to seek Sure refuge on a loftier peak. The Vánar chief in rapid flight Found shelter on a towering height, And all the band with one accord Were closely gathered round their lord. Their course the same, with desperate leap Each made his way from steep to steep, And speeding on in wild career Filled every height with sudden fear.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1171)
- **Original**: Canto II. Sugríva's Alarm. 1153 Each heart was struck with mortal dread, As on their course the Vánars sped, While trees that crowned the steep were bent And crushed beneath them as they went. As in their eager flight they pressed For safety to each mountain crest, The wild confusion struck with fear Tiger and cat and wandering deer. The lords who watched Sugríva's will Were gathered on the royal hill, And all with reverent hands upraised Upon their king and leader gazed. Sugríva feared some evil planned, Some train prepared by Báli's hand. But, skilled in words that charm and teach, Thus Hanumán 538 began his speech: “Dismiss, dismiss thine idle fear, Nor dread the power of Báli here. For this is Malaya's glorious hill539 Where Báli's might can work no ill. I look around but nowhere see The hated foe who made thee flee, Fell Báli, fierce in form and face: Then fear not, lord of Vánar race. Alas, in thee I clearly find The weakness of the Vánar kind, [325] That loves from thought to thought to range, Fix no belief and welcome change. Mark well each hint and sign and scan, Discreet and wise, thine every plan. 538 Hanumán, Sugríva's chief general, was the son of the God of Wind. See Book I, Canto XVI. 539 A range of hills in Malabar; the Western Ghats in the Deccan.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1172)
- **Original**: 1154 The Ramayana How may a king, with sense denied, The subjects of his sceptre guide?” Hanúmán, 540 wise in hour of need, Urged on the chief his prudent rede. His listening ear Sugríva bent, And spake in words more excellent: “Where is the dauntless heart that free From terror's chilling touch can see Two stranger warriors, strong as those, Equipped with swords and shafts and bows, With mighty arms and large full eyes, Like glorious children of the skies? Báli my foe, I ween, has sent These chiefs to aid his dark intent. Hence doubt and fear disturb me still, For thousands serve a monarch's will, In borrowed garb they come, and those Who walk disguised are counted foes. With secret thoughts they watch their time, And wound fond hearts that fear no crime. My foe in state affairs is wise, And prudent kings have searching eyes. By other hands they strike the foe: By meaner tools the truth they know. Now to those stranger warriors turn, And, less than king, their purpose learn. Mark well the trick and look of each; Observe his form and note his speech. With care their mood and temper sound, 540 Válmíki makes the second vowel in this name long or short to suit the exigencies of the verse. Other Indian poets have followed his example, and the same licence will be used in this translation.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1173)
- **Original**: Canto III. Hanumán's Speech. 1155 And, if their minds be friendly found, With courteous looks and words begin Their confidence and love to win. Then as my friend and envoy speak, And question what the strangers seek. Ask why equipped with shaft and bow Through this wild maze of wood they go. If they, O chief, at first appear Pure of all guile, in heart sincere, Detect in speech and look the sin And treachery that lurk within.” He spoke: the Wind-God's son obeyed. With ready zeal he sought the shade, And reached with hasty steps the wood Where Raghu's son and LakshmaG stood.541 Canto III. Hanumán's Speech. The envoy in his faithful breast Pondered Sugríva's high behest. From Rishyamúka's peak he hied And placed him by the princes' side. The Wind-God's son with cautious art Had laid his Vánar form apart, And wore, to cheat the strangers eyes, 541 I omit a recapitulatory and interpolated verse in a different metre, which is as follows:— Reverencing with the words, So be it, the speech of the greatly terrified and unequalled monkey king, the magnanimous Hanumán then went where (stood) the very mighty Ráma with LakshmaG.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1174)
- **Original**: 1156 The Ramayana A wandering mendicant's disguise.542 Before the heroes' feet he bent And did obeisance reverent, And spoke, the glorious pair to praise, His words of truth in courteous phrase, High honour duly paid, the best Of all the Vánar kind addressed, With free accord and gentle grace, Those glories of their warrior race: “O hermits, blest in vows, who shine Like royal saints or Gods divine, O best of young ascetics, say How to this spot you found your way, Scaring the troops of wandering deer And silvan things that harbour here Searching amid the trees that grow Where Pampá's gentle waters flow. And lending from your brows a gleam Of glory to the lovely stream. Who are you, say, so brave and fair, Clad in the bark which hermits wear? I see you heave the frequent sigh, I see the deer before you fly. While you, for strength and valour dread, The earth, like lordly lions, tread, Each bearing in his hand a bow, Like Indra's own, to slay the foe. With the grand paces of a bull, 542 The semi divine Hanumán possesses, like the Gods and demons, the power of wearing all shapes at will. He is one of theKámarúpís. Like Milton's good and bad angels“as they please They limb themselves, and colour, shape, or size Assume as likes them best, condense or rare.”
- **Translation**: 

---

### Verse 10 (Ramayana 0.1175)
- **Original**: Canto III. Hanumán's Speech. 1157 So bright and young and beautiful. The mighty arms you raise appear Like trunks which elephants uprear, And as you move this mountain-king543 Is glorious with the light you bring. How have you reached, like Gods in face, Best lords of earth, this lonely place, [326] With tresses coiled in hermit guise,544 And splendours of those lotus eyes? As Gods who leave their heavenly sphere, Alike your beauteous forms appear. The Lords of Day and Night545 might thus Stray from the skies to visit us. Heroic youth, so broad of chest, Fair with the beauty of the Blest, With lion shoulders, tall and strong, Like bulls who lead the lowing throng, Your arms, unmatched for grace and length, With massive clubs may vie in strength. Why do no gauds those limbs adorn Where priceless gems were meetly worn? Each noble youth is fit, I deem, To guard this earth, as lord supreme, With all her woods and seas, to reign From Meru's peak to Vindhya's chain. Your smooth bows decked with dyes and gold Are glorious in their masters' hold, And with the arms of Indra546 vie Which diamond splendours beautify. 543 Himálaya is of coursepar excellencethe Monarch of mountains, but the complimentary title is frequently given to other hills as here to Malaya. 544 Twisted up in a matted coil as was the custom of ascetics. 545 The sun and moon. 546 The rainbow.
- **Translation**: 

---

### Verse 11 (Ramayana 0.1176)
- **Original**: 1158 The Ramayana Your quivers glow with golden sheen, Well stored with arrows fleet and keen, Each gleaming like a fiery snake That joys the foeman's life to take. As serpents cast their sloughs away And all their new born sheen display, So flash your mighty swords inlaid With burning gold on hilt and blade. Why are you silent, heroes? Why My questions hear nor deign reply? Sugríva, lord of virtuous mind, The foremost of the Vánar kind, An exile from his royal state, Roams through the land disconsolate. I, Hanumán, of Vánar race, Sent by the king have sought this place, For he, the pious, just, and true, In friendly league would join with you. Know, godlike youths, that I am one Of his chief lords, the Wind-God's son. With course unchecked I roam at will, And now from Rishyamúka's hill, To please his heart, his hope to speed, I came disguised in beggar's weed.” Thus Hanúmán, well trained in lore Of language, spoke, and said no more. The son of Raghu joyed to hear The envoy's speech, and bright of cheer He turned to LakshmaG by his side, And thus in words of transport cried:
- **Translation**: 

---

### Verse 12 (Ramayana 0.1177)
- **Original**: Canto III. Hanumán's Speech. 1159 “The counselor we now behold Of King Sugríva righteous-souled. His face I long have yearned to see, And now his envoy comes to me With sweetest words in courteous phrase Answer this mighty lord who slays His foemen, by Sugríva sent, This Vánar chief most eloquent. For one whose words so sweetly flow The whole Rig-veda547 needs must know, And in his well-trained memory store The Yajush and the Sáman's lore. He must have bent his faithful ear All grammar's varied rules to hear. For his long speech how well he spoke! In all its length no rule he broke. In eye, on brow, in all his face The keenest look no guile could trace. No change of hue, no pose of limb Gave sign that aught was false in him. Concise, unfaltering, sweet and clear, Without a word to pain the ear. From chest to throat, nor high nor low, His accents came in measured flow. How well he spoke with perfect art That wondrous speech that charmed the heart, With finest skill and order graced In words that knew nor pause nor haste! That speech, with consonants that spring From the three seats of uttering,548 547 The Vedas are four in number, the Rich or Rig-veda, the Yajush or Yajur- veda; the Sáman or Sáma-veda, and the Atharvan or Atharva-veda. See p. 3. Note. 548 The chest, the throat, and the head.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1178)
- **Original**: 1160 The Ramayana Would charm the spirit of a foe Whose sword is raised for mortal blow. How may a ruler's plan succeed Who lacks such envoy good at need? How fail, if one whose mind is stored With gifts so rare assist his lord? What plans can fail, with wisest speech Of envoy's lips to further each?” Thus Ráma spoke; and LakshmaG taught In all the art that utters thought, To King Sugríva's learned spy Thus made his eloquent reply: “Full well we know the gifts that grace Sugríva, lord of Vánar race, And hither turn our wandering feet That we that high-souled king may meet. So now our pleasant task shall be To do the words he speaks by thee.” His prudent speech the Vánar heard, And all his heart with joy was stirred. And hope that league with them would bring Redress and triumph to his king. [327] Canto IV. Lakshman's Reply.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1179)
- **Original**: Canto IV. Lakshman's Reply. 1161 Cheered by the words that Ráma spoke, Joy in the Vánar's breast awoke, And, as his friendly mood he knew, His thoughts to King Sugríva flew: “Again,” he mused,“my high-souled lord Shall rule, to kingly state restored; Since one so mighty comes to save, And freely gives the help we crave.” Then joyous Hanumán, the best Of all the Vánar kind, addressed These words to Ráma, trained of yore In all the arts of speakers' lore:549 “Why do your feet this forest tread By silvan life inhabited, This awful maze of tree and thorn Which Pampá's flowering groves adorn?” 549 “In our own metrical romances, or wherever a poem is meant not for readers but for chanters and oral reciters, theseformulæ, to meet the same recurring case, exist by scores. Thus every woman in these metrical romances who happens to be young, is described as‘so bright of ble,’or complexion; always a man goes‘the mountenance of a mile’ before he overtakes or is overtaken. And so on through a vast bead-roll of cases. In the same spirit Homer has his eternalÄ¿½ ´'±Á'QÀ¿´Á± ¹´É½, orÄ¿½ ´'±À±¼µ¹²¿¼µ½¿Â ÀÁ¿ÃÆ·, &c. To a reader of sensibility, such recurrences wear an air of child-like sim- plicity, beautifully recalling the features of Homer's primitive age. But they would have appeared faults to all commonplace critics in literary ages.” D E Q UINCEY {FNS .Homer and the Homeridæ.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1180)
- **Original**: 1162 The Ramayana He spoke: obedient to the eye Of Ráma, LakshmaG made reply, The name and fortune to unfold Of Raghu's son the lofty-souled: “True to the law, of fame unstained, The glorious Da[aratha reigned, And, steadfast in his duty, long Kept the four castes550 from scathe and wrong. Through his wide realm his will was done, And, loved by all, he hated none. Just to each creature great and small, Like the Good Sire he cared for all. The Ágnishmom,551 as priests advised, And various rites he solemnized, Where ample largess ever paid The Bráhmans for their holy aid. Here Ráma stands, his heir by birth, Whose name is glorious in the earth: Sure refuge he of all oppressed, Most faithful to his sire's behest. He, Da[aratha's eldest born Whom gifts above the rest adorn, Lord of each high imperial sign,552 The glory of his kingly line, Reft of his right, expelled from home, Came forth with me the woods to roam. And Sítá too, his faithful dame, Forth with her virtuous husband came, Like the sweet light when day is done 550 Bráhmans the sacerdotal caste. Kshatriyas the royal and military, Vai[yas the mercantile, andZúdras the servile. 551 A protracted sacrifice extending over several days. See Book I, p. 24 Note. 552 Possessed of all the auspicious personal marks that indicate capacity of universal sovereignty. See Book I. p. 2, and Note 3.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1181)
- **Original**: Canto IV. Lakshman's Reply. 1163 Still cleaving to her lord the sun. And me his sweet perfections drew To follow as his servant true. Named Lakshma G, brother of my lord Of grateful heart with knowledge stored Most meet is he all bliss to share, Who makes the good of all his care. While, power and lordship cast away, In the wild wood he chose to stay, A giant came,— his name unknown,— And stole the princess left alone. Then Diti's son553 who, cursed of yore, The semblance of a Rákshas wore, To King Sugríva bade us turn The robber's name and home to learn. For he, the Vánar chief, would know The dwelling of our secret foe. Such words of hope spake Diti's son, And sought the heaven his deeds had won. Thou hast my tale. From first to last Thine ears have heard whate'er has past. Ráma the mighty lord and I For refuge to Sugríva fly. The prince whose arm bright glory gained, O'er the whole earth as monarch reigned, And richest gifts to others gave, Is come Sugríva's help to crave; Son of a king the surest friend Of virtue, him who loved to lend His succour to the suffering weak, Is come Sugríva's aid to seek. Yes, Raghu's son whose matchless hand 553 Kabandha. See Book III. Canto LXXIII.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1182)
- **Original**: 1164 The Ramayana Protected all this sea-girt land, The virtuous prince, my holy guide, For refuge seeks Sugríva's side. His favour sent on great and small Should ever save and prosper all. He now to win Sugríva's grace Has sought his woodland dwelling-place.[328] Son of a king of glorious fame;— Who knows not Da[aratha's name?— From whom all princes of the earth Received each honour due to worth;— Heir of that best of earthly kings, Ráma the prince whose glory rings Through realms below and earth and skies, For refuge to Sugríva flies. Nor should the Vánar king refuse The boon for which the suppliant sues, But with his forest legions speed To save him in his utmost need.” Sumitrá's son, his eyes bedewed With piteous tears, thus sighed and sued. Then, trained in all the arts that guide The speaker, Hanumán replied: “Yea, lords like you of wisest thought, Whom happy fate has hither brought, Who vanquish ire and rule each sense, Must of our lord have audience. Reft of his kingdom, sad, forlorn, Once Báli's hate now Báli's scorn, Defeated, severed from his spouse, Wandering under forest boughs, Child of the Sun, our lord and king
- **Translation**: 

---

### Verse 18 (Ramayana 0.1183)
- **Original**: Canto IV. Lakshman's Reply. 1165 Sugríva will his succours bring, And all our Vánar hosts combined Will trace the dame you long to find.” With gentle tone and winning grace Thus spake the chief of Vánar race, And then to Raghu's son he cried: “Come, haste we to Sugríva's side.” He spoke, and for his words so sweet Good Lakshma G paid all honour meet; Then turned and cried to Raghu's son: “Now deem thy task already done, Because this chief of Vánar kind, Son of the God who rules the wind, Declares Sugríva's self would be Assisted in his need by thee. Bright gleams of joy his cheek o'erspread As each glad word of hope he said; And ne'er will one so valiant deign To cheer our hearts with hope in vain.” He spoke, and Hanumán the wise Cast off his mendicant disguise, And took again his Vánar form, Son of the God of wind and storm. High on his ample back in haste Raghu's heroic sons he placed, And turned with rapid steps to find The sovereign of the Vánar kind.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1184)
- **Original**: 1166 The Ramayana Canto V. The League. From Rishyamúka's rugged side To Malaya's hill the Vánar hied, And to his royal chieftain there Announced the coming of the pair: “See, here with LakshmaG Ráma stands Illustrious in a hundred lands. Whose valiant heart will never quail Although a thousand foes assail; King Da[aratha's son, the grace And glory of Ikshváku's race. Obedient to his father's will He cleaves to sacred duty still. With rites of royal pomp and pride His sire the Fire-God gratified; Ten hundred thousand kine he freed, And priests enriched with ample meed; And the broad land protected, famed For truthful lips and passions tamed. Through woman's guile his son has made His dwelling in the forest shade, Where, as he lived with every sense Subdued in hermit abstinence, Fierce RávaG stole his wife, and he Is come a suppliant, lord, to thee. Now let all honour due be paid To these great chiefs who seek thine aid.”
- **Translation**: 

---

### Verse 20 (Ramayana 0.1185)
- **Original**: Canto V. The League. 1167 Thus spake the Vánar prince, and, stirred With friendly thoughts, Sugríva heard. The light of joy his face o'erspread, And thus to Raghu's son he said: “O Prince, in rules of duty trained, Caring for all with love unfeigned, Hanúmán's tongue has truly shown The virtues that are thine alone. My chiefest glory, gain, and bliss, O stranger Prince, I reckon this, That Raghu's son will condescend To seek the Vánar for his friend. If thou my true ally wouldst be Accept the pledge I offer thee, This hand in sign of friendship take, And bind the bond we ne'er will break.” He spoke, and joy thrilled Ráma's breast; Sugríva's hand he seized and pressed And, transport beaming from his eye, Held to his heart his new ally. In wanderer's weed disguised no more, His proper form Hanúmán wore. Then, wood with wood engendering,554 came Neath his deft hands the kindled flame. 554 Fire for sacred purposes is produced by the attrition of two pieces of wood. In marriage and other solemn covenants fire is regarded as the holy witness in whose presence the agreement is made. Spenser in a description of a marriage, has borrowed from the Roman rite what he calls the housling, or“matrimonial rite.” “His owne two hands the holy knots did knit That none but death forever can divide. His owne two hands, for such a turn most fit, The housling fire did kindle and provide.” Faery Queen, Book I. XII.{FNS 37.
- **Translation**: 

---



--- End of Ramayan_batch_157.md ---


--- Start of Ramayan_batch_158.md ---

# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Ramayana 0.1186)
- **Original**: 1168 The Ramayana Between the chiefs that fire he placed[329] With wreaths of flowers and worship graced. And round its blazing glory went The friends with slow steps reverent. Thus each to other pledged and bound In solemn league new transport found, And bent upon his dear ally The gaze he ne'er could satisfy. “Friend of my soul art thou: we share Each other's joy, each other's care;” Thus in the bliss that thrilled his breast Sugríva Raghu's son addressed. From a high Sál a branch he tore Which many a leaf and blossom bore, And the fine twigs beneath them laid A seat for him and Ráma made. Then Hanumán with joyous mind, Son of the God who rules the wind, To LakshmaG gave, his seat to be, The gay branch of a Sandal tree. Then King Sugríva with his eyes Still trembling with the sweet surprise Of the great joy he could not hide, To Raghu's noblest scion cried: “O Ráma, racked with woe and fear, Spurned by my foes, I wander here. Reft of my spouse, forlorn I dwell Here in my forest citadel. Or wild with terror and distress Roam through the distant wilderness. Vext by my brother Báli long My soul has borne the scathe and wrong. Do thou, whose virtues all revere,
- **Translation**: 

---

### Verse 2 (Ramayana 0.1187)
- **Original**: Canto V. The League. 1169 Release me from my woe and fear. From dire distress thy friend to free Is a high task and worthy thee.” He spoke, and Raghu's son who knew All sacred duties men should do. The friend of justice, void of guile, Thus answered with a gentle smile: “Great Vánar, friends who seek my aid Still find their trust with fruit repaid. Báli, thy foe, who stole away Thy wife this vengeful hand shall slay. These shafts which sunlike flash and burn, Winged with the feathers of the hern, Each swift of flight and sure and dread, With even knot and pointed head, Fierce as the crashing fire-bolt sent By him who rules the firmament,555 Shall reach thy wicked foe and like Infuriate serpents hiss and strike. Thou, Vánar King, this day shalt see The foe who long has injured thee Lie, like a shattered mountain, low, Slain by the tempest of my bow.” Thus Ráma spake: Sugríva heard, And mighty joy his bosom stirred: As thus his champion he addressed: “Now by thy favour, first and best Of heroes, shall thy friend obtain His realm and darling wife again Recovered from the foe. Check thou mine elder brother's might; 555 Indra.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1188)
- **Original**: 1170 The Ramayana That ne'er again his deadly spite May rob me of mine ancient right, Or vex my soul with woe.” The league was struck, a league to bring To Sítá fiends, and Vánar king556 Apportioned bliss and bale. Through her left eye quick throbbings shot,557 Glad signs the lady doubted not, That told their hopeful tale. The bright left eye of Báli felt An inauspicious throb that dealt A deadly blow that day. The fiery left eyes of the crew Of demons felt the throb, and knew The herald of dismay. Canto VI. The Tokens. With joy that sprang from hope restored To Ráma spake the Vánar lord: “I know, by wise Hanúmán taught, Why thou the lonely wood hast sought. Where with thy brother LakshmaG thou Hast sojourned, bound by hermit vow; Have heard how Sítá, Janak's child, Was stolen in the pathless wild, How by a roving Rákshas she 556 Báli the kingde facto. 557 With the Indians, as with the ancient Greeks, the throbbing of the right eye in a man is an auspicious sign, the throbbing of the left eye is the opposite. In a woman the significations of signs are reversed.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1189)
- **Original**: Canto VI. The Tokens. 1171 Weeping was reft from him and thee; How, bent on death, the giant slew The vulture king, her guardian true, And gave thy widowed breast to know A solitary mourner's woe. But soon, dear Prince, thy heart shall be From every trace of sorrow free; [330] For I thy darling will restore, Lost like the prize of holy lore.558 Yea, though in heaven the lady dwell, Or prisoned in the depths of hell, My friendly care her way shall track And bring thy ransomed darling back. Let this my promise soothe thy care, Nor doubt the words I truly swear. Saints, fiends, and dwellers of the skies Shall find thy wife a bitter prize, Like the rash child who rues too late The treacherous lure of poisoned cate. No longer, Prince, thy loss deplore: Thy darling wife will I restore. 'Twas she I saw: my heart infers That shrinking form was doubtless hers, Which gaint RávaG, fierce and dread, Bore swiftly through the clouds o'erhead Still writhing in his strict embrace 558 The Vedas stolen by the demons Madhu and Kaimabha. “The text has [Sanskrit text] which signifies literally‘the lost vedic tradi- tion.’It seems that allusion is here made to the Vedas submerged in the depth of the sea, but promptly recovered by VishGu in one of his incarnations, as the brahmanic legend relates, with which the orthodoxy of the Bráhmans intended perhaps to allude to the prompt restoration and uninterrupted continuity of the ancient vedic tradition.” G ORRESIO .{FNS
- **Translation**: 

---

### Verse 5 (Ramayana 0.1190)
- **Original**: 1172 The Ramayana Like helpless queen of serpent race,559 And from her lips that sad voice came Shrieking thine own and LakshmaG's name. High on a hill she saw me stand With comrades twain on either hand. Her outer robe to earth she threw, And with it sent her anklets too. We saw the glittering tokens fall, We found them there and kept them all. These will I bring: perchance thine eyes The treasured spoils will recognize.” He ceased: then Raghu's son replied To the glad tale, and eager cried: “Bring them with all thy speed: delay No more, dear friend, but haste away.” Thus Ráma spoke. Sugríva hied Within the mountain's caverned side, Impelled by love that stirred each thought The precious tokens quickly brought, And said to Raghu's son: Behold This garment and these rings of gold. In Ráma's hand with friendly haste The jewels and the robe he placed. Then, like the moon by mist assailed, The tear-dimmed eyes of Ráma failed; That burst of woe unmanned his frame, Woe sprung from passion for his dame, And with his manly strength o'erthrown, 559 Like the wife of a Nága or Serpent-God carried off by an eagle. The enmity between the King of birds and the serpent is of very frequent occurrence. It seems to be a modification of the strife between the Vedic Indra and the Ahi, the serpent or drought-fiend; between Apollôn and the Python, Adam and the Serpent.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1191)
- **Original**: Canto VI. The Tokens. 1173 He fell and cried, Ah me! mine own! Again, again close to his breast The ornaments and robe he pressed, While the quick pants that shook his frame As from a furious serpent came. On his dear brother standing nigh He turned at length his piteous eye; And, while his tears increasing ran, In bitter wail he thus began: “Look, brother, and behold once more The ornaments and robe she wore, Dropped while the giant bore away In cruel arras his struggling prey, Dropped in some quiet spot, I ween, Where the young grass was soft and green; For still untouched by spot or stain Their former beauty all retain.” He spoke with many a tear and sigh, And thus his brother made reply: “The bracelets thou hast fondly shown, And earrings, are to me unknown, But by long service taught I greet The anklets of her honoured feet.”560 Then to Sugríva Ráma, best Of Raghu's sons, these words addressed: 560 He means that he has never ventured to raise his eyes to her arms and face, though he has ever been her devoted servant.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1192)
- **Original**: 1174 The Ramayana “Say to what quarter of the sky The cruel fiend was seen to fly, Bearing afar my captured wife, My darling dearer than my life. Speak, Vánar King, that I may know Where dwells the cause of all my woe; The fiend for whose transgression all The giants by this hand shall fall. He who the Maithil lady stole And kindled fury in my soul, Has sought his fate in senseless pride And opened Death's dark portal wide. Then tell me, Vánar lord, I pray, The dwelling of my foe, And he, beneath this hand, to-day To Yáma's halls shall go.” [331] Canto VII. Ráma Consoled. With longing love and woe oppressed The Vánar chief he thus addressed: And he, while sobs his utterance broke, Raised up his reverent hands and spoke:
- **Translation**: 

---

### Verse 8 (Ramayana 0.1193)
- **Original**: Canto VII. Ráma Consoled. 1175 “O Raghu's son, I cannot tell Where now that cruel fiend may dwell, Declare his power and might, or trace The author of his cursed race. Still trust the promise that I make And let thy breast no longer ache. So will I toil, nor toil in vain, That thou thy consort mayst regain. So will I work with might and skill That joy anew thy heart shall fill: The valour of my soul display, And RávaG and his legions slay. Awake, awake! unmanned no more Recall the strength was thine of yore. Beseems not men like thee to wear A weak heart yielding to despair. Like troubles, too, mine eyes have seen, Lamenting for a long-lost queen; But, by despair unconquered yet, My strength of mind I ne'er forget. Far more shouldst thou of lofty soul Thy passion and thy tears control, When I, of Vánar's humbler strain, Weep not for her in ceaseless pain. Be firm, be patient, nor forget The bounds the brave of heart have set In loss, in woe, in strife, in fear, When the dark hour of death is near. Up! with thine own brave heart advise: Not thus despond the firm and wise. But he who gives his childish heart To choose the coward's weakling part, Sinks, like a foundered vessel, deep In waves of woe that o'er him sweep.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1194)
- **Original**: 1176 The Ramayana See, suppliant hand to hand I lay, And, moved by faithful love, I pray. Give way no more to grief and gloom, But all thy native strength resume. No joy on earth, I ween, have they Who yield their souls to sorrow's sway. Their glory fades in slow decline: 'Tis not for thee to grieve and pine. I do but hint with friendly speech The wiser part I dare not teach. This better path, dear friend, pursue, And let not grief thy soul subdue.” Sugríva thus with gentle art And sweet words soothed the mourner's heart, Who brushed off with his mantle's hem Tears from the eyes bedewed with them. Sugríva's words were not in vain, And Ráma was himself again, Around the king his arms he threw And thus began his speech anew: “Whate'er a friend most wise and true, Who counsels for the best, should do, Whate'er his gentle part should be, Has been performed, dear friend, by thee. Taught by thy counsel, O my lord, I feel my native strength restored. A friend like thee is hard to gain, Most rare in time of grief and pain. Now strain thine utmost power to trace The Maithil lady's dwelling place, And aid me in my search to find Fierce RávaG of the impious mind.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1195)
- **Original**: Canto VIII. Ráma's Promise. 1177 Trust thou, in turn, thy loyal friend, And say what aid this arm can lend To speed thy hopes, as fostering rain Quickens in earth the scattered grain. Deem not those words, that seemed to spring From pride, are false, O Vánar King. None from these lips has ever heard, None e'er shall hear, one lying word. Again I promise and declare, Yea, by my truth, dear friend, I swear.” Then glad was King Sugríva's breast, And all his lords their joy confessed, Stirred by sure hope of Ráma's aid, And promise which the prince had made. Canto VIII. Ráma's Promise. Doubt from Sugríva's heart had fled, And thus to Raghu's son he said: “No bliss the Gods of heaven deny. Each views me with a favouring eye, When thou, whom all good gifts attend, Hast sought me and become my friend. Leagued, friend, with thee in bold emprise My arm might win the conquered skies; And shall our banded strength be weak To gain the realm which now I seek? A happy fate was mine above My kith and kin and all I love, When, near the witness fire, I won
- **Translation**: 

---

### Verse 11 (Ramayana 0.1196)
- **Original**: 1178 The Ramayana Thy friendship, Raghu's glorious son. Thou too in ripening time shall see Thy friend not all unworthy thee. What gifts I have shall thus be shown: Not mine the tongue to make them known. Strong is the changeless bond that binds The friendly faith of noble minds, In woe, in danger, firm and sure Their constancy and love endure. Gold, silver, jewels rich and rare They count as wealth for friends to share.[332] Yea, be they rich or poor and low, Blest with all joys or sunk in woe, Stained with each fault or pure of blame, Their friends the nearest place may claim; For whom they leave, at friendship's call, Their gold, their bliss, their homes and all.” He spoke by generous impulse moved, And Raghu's son his speech approved Glancing at LakshmaG by his side, Like Indra in his beauty's pride. The Vánar monarch saw the pair Of mighty brothers standing there, And turned his rapid eye to view The forest trees that near him grew. He saw, not far from where he stood, A Sál tree towering o'er the wood. Amid the thick leaves many a bee Graced the scant blossoms of the tree, From whose dark shade a bough, that bore A load of leafy twigs, he tore, Which on the grassy ground he laid And seats for him and Ráma made.
- **Translation**: 

---

### Verse 12 (Ramayana 0.1197)
- **Original**: Canto VIII. Ráma's Promise. 1179 Hanúmán saw them sit, he sought A Sál tree's leafy bough and brought The burthen, and with meek request Entreated LakshmaG, too, to rest. There on the noble mountain's brow, Strewn with the young leaves of the bough, Sat Raghu's son in placid ease Calm as the sea when sleeps the breeze. Sugríva's heart with rapture swelled, And thus, by eager love impelled, He spoke in gracious tone, that, oft Checked by his joy, was low and soft: “I, by my brother's might oppressed, By ceaseless woe and fear distressed, Mourning my consort far away, On Rishyamúka's mountain stray. Expelled by Báli's cruel hate I wander here disconsolate. Do thou to whom all sufferers flee, From his dread hand deliver me.” He spoke, and Ráma, just and brave, Whose pious soul to virtue clave, Smiled as in conscious might he eyed The king of Vánars, and replied: “Best fruit of friendship is the deed That helps the friend in hour of need; And this mine arm in death shall lay Thy robber ere the close of day. For see, these feathered darts of mine Whose points so fiercely flash and shine, And shafts with golden emblem, came From dark woods known by Skanda's name,561 561 The wood in which Skanda or Kártikeva was brought up:
- **Translation**: 

---

### Verse 13 (Ramayana 0.1198)
- **Original**: 1180 The Ramayana Winged from the pinion of the hern Like Indra's bolts they strike and burn. With even knots and piercing head Each like a furious snake is sped; With these, to-day, before thine eye Shall, like a shattered mountain, lie Báli, thy dread and wicked foe, O'erwhelmed in hideous overthrow.” He spoke: Sugríva's bosom swelled With hope and joy unparalleled. Then his glad voice the Vánar raised, And thus the son of Raghu praised: “Long have I pined in depth of grief; Thou art the hope of all, O chief. Now, Raghu's son, I hail thee friend, And bid thee to my woes attend; For, by my truth I swear it, now Not life itself is dear as thou, Since by the witness fire we met And friendly hand in hand was set. Friend communes now with friend, and hence I tell with surest confidence, How woes that on my spirit weigh Consume me through the night and day.” “The Warrior-God Whose infant steps amid the thickets strayed Where the reeds wave over the holy sod.” See also Book I, Canto XXIX.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1199)
- **Original**: Canto VIII. Ráma's Promise. 1181 For sobs and sighs he scarce could speak, And his sad voice came low and weak, As, while his eyes with tears o'erflowed, The burden of his soul he showed. Then by strong effort, bravely made, The torrent of his tears he stayed, Wiped his bright eyes, his grief subdued, And thus, more calm, his speech renewed: “By Báli's conquering might oppressed, Of power and kingship dispossessed, Loaded with taunts of scorn and hate I left my realm and royal state. He tore away my consort: she Was dearer than my life to me, And many a friend to me and mine In hopeless chains was doomed to pine. With wicked thoughts, unsated still, Me whom he wrongs he yearns to kill; And spies of Vánar race, who tried To slay me, by this hand have died. Moved by this constant doubt and fear I saw thee, Prince, and came not near. When woe and peril gather round A foe in every form is found. Save Hanumán, O Raghu's son, And these, no friend is left me, none. Through their kind aid, a faithful band Who guard their lord from hostile hand, Rest when their chieftain rests and bend Their steps where'er he lists to wend,— Through them alone, in toil and pain, My wretched life I still sustain. [333]
- **Translation**: 

---

### Verse 15 (Ramayana 0.1200)
- **Original**: 1182 The Ramayana Enough, for thou hast heard in brief The story of my pain and grief. His mighty strength all regions know, My brother, but my deadly foe. Ah, if the proud oppressor fell, His death would all my woe dispel. Yea, on my cruel conqueror's fall My joy depends, my life, my all. This were the end and sure relief, O Ráma, of my tale of grief. Fair be his lot or dark with woe, No comfort like a friend I know.” Then Ráma spoke:“O friend, relate Whence sprang fraternal strife and hate, That duly taught by thee, I may Each foeman's strength and weakness weigh: And skilled in every chance restore The blissful state thou hadst before. For, when I think of all the scorn And bitter woe thou long hast borne, My soul indignant swells with pain Like waters flushed with furious rain. Then, ere I string this bended bow, Tell me the tale I long to know, Ere from the cord my arrow fly, And low in death thy foeman lie.” He spoke: Sugríva joyed to hear, Nor less his lords were glad of cheer: And thus to Ráma mighty-souled The cause that moved their strife he told:
- **Translation**: 

---

### Verse 16 (Ramayana 0.1201)
- **Original**: Canto IX. Sugríva's Story. 1183 Canto IX. Sugríva's Story.562 “My brother, known by Báli's name, Had won by might a conqueror's fame. My father's eldest-born was he, Well honoured by his sire and me. My father died, and each sage lord Named Báli king with one accord; And he, by right of birth ordained, The sovereign of the Vánars reigned. He in his royal place controlled The kingdom of our sires of old, And I all faithful service lent To aid my brother's government. The fiend Máyáví,— him of yore To Dundubhi563 his mother bore,— For woman's love in strife engaged, A deadly war with Báli waged. When sleep had chained each weary frame To vast Kishkindhá564 gates he came, And, shouting through the shades of night, Challenged his foeman to the fight. My brother heard the furious shout, And wild with rage rushed madly out, Though fain would I and each sad wife Detain him from the deadly strife. He burned his demon foe to slay, 562 “Sugríva's story paints in vivid colours the manners, customs and ideas of the wild mountain tribes which inhabited Kishkindhya or the southern hills of the Deccan, of the people whom the poem calls monkeys, tribes altogether different in origin and civilization from the Indo-Sanskrit race.” G ORRESIO {FNS . 563 A fiend slain by Báli. 564 Báli's mountain city.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1202)
- **Original**: 1184 The Ramayana And rushed impetuous to the fray. His weeping wives he thrust aside, And forth, impelled by fury, hied; While, by my love and duty led, I followed where my brother sped. Máyáví looked, and at the sight Fled from his foes in wild affright. The flying fiend we quickly viewed, And with swift feet his steps pursued. Then rose the moon, whose friendly ray Cast light upon our headlong way. By the soft beams was dimly shown A mighty cave with grass o'ergrown. Within its depths he sprang, and we The demon's form no more might see. My brother's breast was all aglow With fury when he missed the foe, And, turning, thus to me he said With senses all disquieted: “Here by the cavern's mouth remain; Keep ear and eye upon the strain, While I the dark recess explore And dip my brand in foeman's gore.” I heard his angry speech, and tried To turn him from his plan aside. He made me swear by both his feet, And sped within the dark retreat. While in the cave he stayed, and I Watched at the mouth, a year went by. For his return I looked in vain, And, moved by love, believed him slain. I mourned, by doubt and fear distressed, And greater horror seized my breast When from the cavern rolled a flood,
- **Translation**: 

---

### Verse 18 (Ramayana 0.1203)
- **Original**: Canto IX. Sugríva's Story. 1185 A carnage stream of froth and blood; And from the depths a sound of fear, The roar of demons, smote mine ear; But never rang my brother's shout Triumphant in the battle rout. I closed the cavern with a block, Huge as a hill, of shattered rock. Gave offerings due to Báli's shade, And sought Kishkindhá, sore dismayed. Long time with anxious care I tried From Báli's lords his fate to hide, But they, when once the tale was known, Placed me as king on Báli's throne. There for a while I justly reigned [334] And all with equal care ordained, When joyous from the demon slain My brother Báli came again. He found me ruling in his stead, And, fired with rage, his eyes grew red. He slew the lords who made me king, And spoke keen words to taunt and sting. The kingly rank and power I held My brother's rage with ease had quelled, But still, restrained by old respect For claims of birth, the thought I checked. Thus having struck the demon down Came Báli to his royal town. With meek respect, with humble speech, His haughty heart I strove to reach. But all my arts were tried in vain, No gentle word his lips would deign, Though to the ground I bent and set His feet upon my coronet: Still Báli in his rage and pride
- **Translation**: 

---

### Verse 19 (Ramayana 0.1204)
- **Original**: 1186 The Ramayana All signs of grace and love denied.” Canto X. Sugríva's Story. “I strove to soothe and lull to rest The fury of his troubled breast: “Well art thou come, dear lord,” I cried. “By whose strong arm thy foe has died. Forlorn I languished here, but now My saviour and defence art thou. Once more receive this regal shade565 Like the full moon in heaven displayed; And let the chouries,566 thus restored, Wave glorious o'er the rightful lord. I kept my watch, thy word obeyed, And by the cave a year I stayed. But when I saw that stream of blood Rush from the cavern in a flood, My sad heart broken with dismay, And every wandering sense astray, I barred the entrance with a stone,— A crag from some high mountain thrown— Turned from the spot I watched in vain, And to Kishkindhá came again. My deep distress and downcast mien By citizen and lord were seen. They made me king against my will: Forgive me if the deed was ill. 565 The canopy or royal umbrella, one of the usual Indian regalia. 566 Whisks made of the hair of the Yak or Bos grunniers, also regal insignia.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1205)
- **Original**: Canto X. Sugríva's Story. 1187 True as I ever was I see My honoured king once more in thee; I only ruled a while the state When thou hadst left us desolate. This town with people, lords, and lands, Lay as a trust in guardian hands: And now, my gracious lord, accept The kingdom which thy servant kept. Forgive me, victor of the foe, Nor let thy wrath against me glow. See joining suppliant hands I pray, And at thy feet my head I lay. Believe my words: against my will The royal seat they made me fill. Unkinged they saw the city, hence They made me lord for her defence.” But Báli, though I humbly sued, Reviled me in his furious mood: “Out on thee, wretch!” in wrath he cried With many a bitter taunt beside. He summoned every lord, and all His subjects gathered at his call. Then forth his burning anger broke, And thus amid his friends he spoke: “I need not tell, for well ye know, How fierce Máyáví, fiend and foe, Came to Kishkindhá's gate by night, And dared me in his wrath to fight. I heard each word the demon said: Forth from my royal hall I sped; And, foe in brother's guise concealed, Sugríva followed to the field. The mighty demon through the shade
- **Translation**: 

---



--- End of Ramayan_batch_158.md ---


--- Start of Ramayan_batch_159.md ---

# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Ramayana 0.1206)
- **Original**: 1188 The Ramayana Beheld me come with one to aid: Then shrinking from unequal fight, He turned his back in swiftest flight. From vengeful foes his life to save He sought the refuge of a cave. Then when I saw the fiend had fled Within that cavern dark and dread, Thus to my brother cruel-eyed, Impatient in my wrath, I cried: “I seek no more my royal town Till I have struck the demon down. Here by the cavern's mouth remain Until my hand the foe have slain.” Upon his faith my heart relied, And swift within the depths I hied. A year went by: in every spot I sought the fiend, but found him not. At length my foe I saw and slew, Whom long I feared when lost to view; And all his kinsmen by his side Beneath my vengeful fury died. The monster, as he reeled and fell, Poured forth his blood with roar and yell; And, filling all the cavern, dyed The portal with the crimson tide. Upon my foeman slain at last One look, one pitying look, I cast. I sought again the light of day: The cave was closed and left no way. To the barred mouth I sadly came, And called aloud Sugríva's name. But all was still: no voice replied,[335] And hope within my bosom died. With furious efforts, vain at first,
- **Translation**: 

---

### Verse 2 (Ramayana 0.1207)
- **Original**: Canto X. Sugríva's Story. 1189 Through bars of rock my way I burst. Then, free once more, the path that brought My feet in safety home I sought. 'Twas thus Sugríva dared despise The claim of brothers' friendly ties. With crags of rock he barred me in, And for himself the realm would win.” Thus Báli spoke in words severe; And then, unmoved by ruth or fear, Left me a single robe and sent His brother forth in banishment. He cast me out with scathe and scorn, And from my side my wife was torn. Now in great fear and ill at ease I roam this land with woods and seas, Or dwell on Rishyamúka's hill, And sorrow for my consort still. Thou hast the tale how first arose This bitter hate of brother foes. Such are the griefs neath which I pine, And all without a fault of mine. O swift to save in hour of fear, My prayer who dread this Báli, hear With gracious love assistance deign, And mine oppressor's arm restrain.” Then Raghu's son, the good and brave, With a gay laugh his answer gave: “These shafts of mine which ne'er can fail, Before whose sheen the sun grows pale, Winged by my fury, fleet and fierce, The wicked Báli's heart shall pierce. Yea, mark the words I speak, so long
- **Translation**: 

---

### Verse 3 (Ramayana 0.1208)
- **Original**: 1190 The Ramayana Shall live that wretch who joys in wrong, Until these angered eyes have seen The robber of thy darling queen. I, taught by equal suffering, know What waves of grief above thee flow. This hand thy captive wife shall free, And give thy kingdom back to thee.” Sugríva joyed as Ráma spoke, And valour in his breast awoke. His eye grew bright, his heart grew bold, And thus his wondrous tale he told: Canto XI. Dundubhi. “I doubt not, Prince, thy peerless might, Armed with these shafts so keen and bright, Like all-destroying fires of fate, The worlds could burn and devastate. But lend thou first thy mind and ear Of Báli's power and might to hear. How bold, how firm, in battle tried, Is Báli's heart; and then decide. From east to west, from south to north On restless errand hurrying forth, From farthest sea to sea he flies Before the sun has lit the skies. A mountain top he oft will seek, Tear from its root a towering peak, Hurl it aloft, as 'twere a ball, And catch it ere to earth it fall.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1209)
- **Original**: Canto XI. Dundubhi. 1191 And many a tree that long has stood In health and vigour in the wood, His single arm to earth will throw, The marvels of his might to show. Shaped like a bull, a monster bore The name of Dundubhi of yore: He matched in size a mountain height, A thousand elephants in might. By pride of wondrous gifts impelled, And strength he deemed unparalleled, To Ocean, lord of stream and brook, Athirst for war, his way he took. He reached the king of rolling waves Whose gems are piled in sunless caves, And threw his challenge to the sea; “Come forth, O King, and fight with me.” He spoke, and from his ocean bed The righteous567 monarch heaved his head, And gave, sedate, his calm reply To him whom fate impelled to die: “Not mine, not mine the power,” he cried, “To cope with thee in battle tried; But listen to my voice, and seek The worthier foe of whom I speak. The Lord of Hills, where hermits live And love the home his forests give, Whose child isZankar's darling queen,568 The King of Snows is he I mean. Deep caves has he, and dark boughs shade 567 Righteous because he never transgresses his bounds, and “over his great tides Fidelity presides.” 568 Himálaya, the Lord of Snow, is the father of Umá the wife ofZiva orZankar.
- **Translation**: 

---

### Verse 5 (Ramayana 0.1210)
- **Original**: 1192 The Ramayana The torrent and the wild cascade. From him expect the fierce delight Which heroes feel in equal fight.” He deemed that fear checked ocean's king, And, like an arrow from the string, To the wild woods that clothe the side Of Lord Himálaya's hills he hied. Then Dundubhi, with hideous roar, Huge fragments from the summit tore Vast as Airávat,569 white with snow, And hurled them to the plains below. Then like a white cloud soft, serene, The Lord of Mountains' form was seen. It sat upon a lofty crest, And thus the furious fiend addressed: “Beseems thee not, O virtue's friend, My mountain tops to rive and rend;[336] For I, the hermit's calm retreat, For deeds of war am all unmeet.” The demon's eye with rage grew red, And thus in furious tone he said: “If thou from fear or sloth decline To match thy strength in war with mine, Where shall I find a champion, say, To meet me burning for the fray?” He spoke: Himálaya, skilled in lore Of eloquence, replied once more, And, angered in his righteous mind, Addressed the chief of demon kind: “The Vánar Báli, brave and wise, 569 Indra's celestial elephant.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1211)
- **Original**: Canto XI. Dundubhi. 1193 Son of the God who rules the skies,570 Sways, glorious in his high renown, Kishkindhá his imperial town. Well may that valiant lord who knows Each art of war his might oppose To thine, in equal battle set, As Namuehi571 and Indra met. Go, if thy soul desire the fray; To Báli's city speed away, And that unconquered hero meet Whose fame is high for warlike feat.” He listened to the Lord of Snow, And, his proud heart with rage aglow, Sped swift away and lighted down By vast Kishkindhá, Báli's town. With pointed horns to strike and gore The semblance of a bull he bore, Huge as a cloud that downward bends Ere the full flood of rain descends. Impelled by pride and rage and hate, He thundered at Kishkindhá's gate; And with his bellowing, like the sound Of pealing drums, he shook the ground, He rent the earth and prostrate threw The trees that near the portal grew. King Báli from the bowers within Indignant heard the roar and din. Then, moonlike mid the stars, with all His dames he hurried to the wall; And to the fiend this speech, expressed In clear and measured words, addressed: 570 Báli was the son of Indra. See p. 28. 571 An Asur slain by Indra. See p. 261 Note. He is, like Vritra, a form of the demon of drought destroyed by the beneficent God of the firmament.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1212)
- **Original**: 1194 The Ramayana “Know me for monarch. Báli styled, Of Vánar tribes that roam the wild. Say why dost thou this gate molest, And bellowing thus disturb our rest? I know thee, mighty fiend: beware And guard thy life with wiser care.” He spoke: and thus the fiend returned, While red with rage his eyeballs burned: “What! speak when all thy dames are nigh And hero-like thy foe defy? Come, meet me in the fight this day, And learn my strength by bold assay. Or shall I spare thee, and relent Until the coming night be spent? Take then the respite of a night And yield thee to each soft delight. Then, monarch of the Vánar race With loving arms thy friends embrace. Gifts on thy faithful lords bestow, Bid each and all farewell, and go. Show in the streets once more thy face, Install thy son to fill thy place. Dally a while with each dear dame; And then my strength thy pride shall tame For, should I smite thee drunk with wine Enamoured of those dames of thine, Beneath diseases bowed and bent, Or weak, unarmed, or negligent, My deed would merit hate and scorn As his who slays the child unborn.” Then Báli's soul with rage was fired, Queen Tára and the dames retired; And slowly, with a laugh of pride, The king of Vánars thus replied:
- **Translation**: 

---

### Verse 8 (Ramayana 0.1213)
- **Original**: Canto XI. Dundubhi. 1195 “Me, fiend, thou deemest drunk with wine: Unless thy fear the fight decline, Come, meet me in the fray, and test The spirit of my valiant breast.” He spoke in wrath and high disdain; And, laying down his golden chain, Gift of his sire Mahendra, dared The demon, for the fray prepared; Seized by the horns the monster, vast As a huge hill, and held him fast, Then fiercely dragged him round and round, And, shouting, hurled him to the ground. Blood streaming from his ears, he rose, And wild with fury strove the foes. Then Báli, match for Indra's might, With every arm renewed the fight. He fought with fists, and feet, and knees, With fragments of the rock, and trees. At last the monster's strength, assailed By Zakra's572 conquering offspring, failed. Him Báli raised with mighty strain And dashed upon the ground again; Where, bruised and shattered, in a tide Of rushing blood, the demon died. King Báli saw the lifeless corse, And bending, with tremendous force Raised the huge bulk from where it lay, And hurled it full a league away. As through the air the body flew, Some blood-drops, caught by gales that blew, Welled from his shattered jaw and fell By Saint Matanga's hermit cell: 572 Another name of Indra or Mahendra.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1214)
- **Original**: 1196 The Ramayana Matanga saw, illustrious sage, Those drops defile his hermitage,[337] And, as he marvelled whence they came, Fierce anger filled his soul with flame: “Who is the villain, evil-souled, With childish thoughts unwise and bold, Who is the impious wretch,” he cried, “By whom my grove with blood is dyed?” Thus spoke Matanga in his rage, And hastened from the hermitage, When lo, before his wondering eyes Lay the dead bull of mountain size. His hermit soul was nothing slow The doer of the deed to know, And thus the Vánar in a burst Of wild tempestuous wrath he cursed: “Ne'er let that Vánar wander here, For, if he come, his death is near, Whose impious hand with blood has dyed The holy place where I abide, Who threw this demon corse and made A ruin of the pleasant shade. If e'er he plant his wicked feet Within one league of my retreat; Yea, if the villain come so nigh That very hour he needs must die. And let the Vánar lords who dwell In the dark woods that skirt my cell Obey my words, and speeding hence Find them some meeter residence. Here if they dare to stay, on all The terrors of my curse shall fall. They spoil the tender saplings, dear
- **Translation**: 

---

### Verse 10 (Ramayana 0.1215)
- **Original**: Canto XI. Dundubhi. 1197 As children which I cherish here, Mar root and branch and leaf and spray, And steal the ripening fruit away. One day I grant, no further hour, To-morrow shall my curse have power, And then each Vánar I may see A stone through countless years shall be.” The Vánars heard the curse and hied From sheltering wood and mountain side. King Báli marked their haste and dread, And to the flying leaders said: “Speak, Vánar chiefs, and tell me why From Saint Matanga's grove ye fly To gather round me: is it well With all who in those woodlands dwell?” He spoke: the Vánar leaders told King Báli with his chain of gold What curse the saint had on them laid, Which drove them from their ancient shade. Then royal Báli sought the sage, With reverent hands to soothe his rage. The holy man his suppliant spurned, And to his cell in anger turned. That curse on Báli sorely pressed, And long his conscious soul distressed. Him still the curse and terror keep Afar from Rishyamúka's steep. He dares not to the grove draw nigh, Nay scarce will hither turn his eye. We know what terrors warm him hence, And roam these woods in confidence. Look, Prince, before thee white and dry The demon's bones uncovered lie, Who, like a hill in bulk and length,
- **Translation**: 

---

### Verse 11 (Ramayana 0.1216)
- **Original**: 1198 The Ramayana Fell ruind for his pride of strength. See those high Sál trees seven in row That droop their mighty branches low, These at one grasp would Báli seize, And leafless shake the trembling trees. These tales I tell, O Prince, to show The matchless power that arms the foe. How canst thou hope to slay him? how Meet Báli in the battle now?” Sugríva spoke and sadly sighed: And Lakshma G with a laugh replied: “What show of power, what proof and test May still the doubts that fill thy breast?” He spoke. Sugríva thus replied: “See yonder Sál trees side by side. King Báli here would take his stand Grasping his bow with vigorous hand, And every arrow, keen and true, Would strike its tree and pierce it through. If Ráma now his bow will bend, And through one trunk an arrow send; Or if his arm can raise and throw Two hundred measures of his bow, Grasped by a foot and hurled through air, The demon bull that moulders there, My heart will own his might and fain Believe my foe already slain.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.1217)
- **Original**: Canto XI. Dundubhi. 1199 Sugríva spoke inflamed with ire, Scanned Ráma with a glance of fire, Pondered a while in silent mood. And thus again his speech renewed: “All lands with Báli's glories ring, A valiant, strong, and mighty king; In conscious power unused to yield, A hero first in every field. His wondrous deeds his might declare, Deeds Gods might scarcely do or dare; And on this power reflecting still I roam on Rishyamúka's hill. Awed by my brother's might I rove, In doubt and fear, from grove to grove, While Hanumán, my chosen friend, And faithful lords my steps attend; And now, O true to friendship's tie, I hail in thee my best ally. My surest refuge from my foes, And steadfast as the Lord of Snows. Still, when I muse how strong and bold Is cruel Báli, evil-souled, But ne'er, O chief of Raghu's line, Have seen what strength in war is thine, Though in my heart I may not dare Doubt thy great might, despise, compare, Thoughts of his fearful deeds will rise And fill my soul with sad surmise. Speech, form, and trust which naught may move [338] Thy secret strength and glory prove, As smouldering ashes dimly show The dormant fires that live below.”
- **Translation**: 

---

### Verse 13 (Ramayana 0.1218)
- **Original**: 1200 The Ramayana He ceased: and Ráma answered, while Played o'er his lips a gracious smile: “Not yet convinced? This clear assay Shall drive each lingering doubt away.” Thus Ráma spoke his heart to cheer, To Dundubhi's vast frame drew near: He touched it with his foot in play And sent it twenty leagues away. Sugríva marked what easy force Hurled through the air that demon's corse Whose mighty bones were white and dried, And to the son of Raghu cried: “My brother Báli, when his might Was drunk and weary from the fight, Hurled forth the monster body, fresh With skin and sinews, blood and flesh. Now flesh and blood are dried away, The crumbling bones are light as hay, Which thou, O Raghu's son, hast sent Flying through air in merriment. This test alone is weak to show If thou be stronger or the foe. By thee a heap of mouldering bone, By him the recent corse was thrown. Thy strength, O Prince, is yet untried: Come, pierce one tree: let this decide. Prepare thy ponderous bow and bring Close to thine ear the straining string. On yonder Sál tree fix thine eye, And let the mighty arrow fly, I doubt not, chief, that I shall see Thy pointed shaft transfix the tree. Then come, assay the easy task, And do for love the thing I ask.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1219)
- **Original**: Canto XII. The Palm Trees. 1201 Best of all lights, the Day-God fills With glory earth and sky: Himálaya is the lord of hills That heave their heads on high. The royal lion is the best Of beasts that tread the earth; And thou, O hero, art confessed First in heroic worth.” Canto XII. The Palm Trees. Then Ráma, that his friend might know His strength unrivalled, grasped his bow, That mighty bow the foe's dismay,— And on the string an arrow lay. Next on the tree his eye he bent, And forth the hurtling weapon went. Loosed from the matchless hero's hold, That arrow, decked with burning gold, Cleft the seven palms in line, and through The hill that rose behind them flew: Six subterranean realms it passed, And reached the lowest depth at last, Whence speeding back through earth and air It sought the quiver, and rested there.573 Upon the cloven trees amazed, The sovereign of the Vánars gazed. With all his chains and gold outspread Prostrate on earth he laid his head. 573 The Bengal recension makes it return in the form of a swan.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1220)
- **Original**: 1202 The Ramayana Then, rising, palm to palm he laid In reverent act, obeisance made, And joyously to Ráma, best Of war-trained chiefs, these words addressed: “What champion, Raghu's son, may hope With thee in deadly fight to cope, Whose arrow, leaping from the bow, Cleaves tree and hill and earth below? Scarce might the Gods, arrayed for strife By Indra's self, escape, with life Assailed by thy victorious hand: And how may Báli hope to stand? All grief and care are past away, And joyous thoughts my bosom sway, Who have in thee a friend, renowned, As VaruG574 or as Indra, found. Then on! subdue,— 'tis friendship's claim,— My foe who bears a brother's name. Strike Báli down beneath thy feet: With suppliant hands I thus entreat.” Sugríva ceased, and Ráma pressed The grateful Vánar to his breast; And thoughts of kindred feeling woke In LakshmaG's bosom, as he spoke: “On to Kishkindhá, on with speed! Thou, Vánar King, our way shalt lead, Then challenge Báli forth to fight. 574 VaruGa is one of the oldest of the Vedic Gods, corresponding in name and partly in character to thePÁ±½yÂ of the Greeks and is often regarded as the supreme deity. He upholds heaven and earth, possesses extraordinary power and wisdom, sends his messengers through both worlds, numbers the very winkings of men's eyes, punishes transgressors whom he seizes with his deadly noose, and pardons the sins of those who are penitent. In later mythology he has become the God of the sea.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1221)
- **Original**: Canto XII. The Palm Trees. 1203 Thy foe who scorns a brother's right.” They sought Kishkindhá's gate and stood Concealed by trees in densest wood, Sugríva, to the fight addressed, More closely drew his cinctured vest, And raised a wild sky-piercing shout [339] To call the foeman Báli out. Forth came impetuous Báli, stirred To fury by the shout he heard. So the great sun, ere night has ceased, Springs up impatient to the east. Then fierce and wild the conflict raged As hand to hand the foes engaged, As though in battle mid the stars Fought Mercury and fiery Mars.575 To highest pitch of frenzy wrought With fists like thunderbolts they fought, While near them Ráma took his stand, And viewed the battle, bow in hand. Alike they stood in form and might, Like heavenly A[vins576 paired in fight, Nor might the son of Raghu know Where fought the friend and where the foe; 575 Budha, not to be confounded with the great reformer Buddha, is the son of Soma or the Moon, and regent of the planet Mercury. Angára is the regent of Mars who is called the red or the fiery planet. The encounter between Michael and Satan is similarly said to have been as if “Two planets rushing from aspect malign Of fiercest opposition in midsky Should combat, and their jarring spheres compound.” Paradise Lost.Book VI. 576 The A[vins or Heavenly Twins, the Dioskuri or Castor and Pollux of the Hindus, have frequently been mentioned. See p. 36, Note.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1222)
- **Original**: 1204 The Ramayana So, while his bow was ready bent, No life-destroying shaft he sent. Crushed down by Báli's mightier stroke Sugríva's force now sank and broke, Who, hoping naught from Ráma's aid, To Rishyamúka fled dismayed, Weary, and faint, and wounded sore, His body bruised and dyed with gore, From Báli's blows, in rage and dread, Afar to sheltering woods he fled. Nor Báli farther dared pursue, The curbing curse too well he knew. “Fled from thy death!” the victor cried, And home the mighty warrior hied. Hanúmán, LakshmaG, Raghu's son Beheld the conquered Vánar run, And followed to the sheltering shade Where yet Sugríva stood dismayed. Near and more near the chieftains came, Then, for intolerable shame, Not daring yet to lift his eyes, Sugríva spoke with burning sighs: “Thy matchless strength I first beheld, And dared my foe, by thee impelled. Why hast thou tried me with deceit And urged me to a sure defeat? Thou shouldst have said,“I will not slay Thy foeman in the coming fray.” For had I then thy purpose known I had not waged the fight alone.”
- **Translation**: 

---

### Verse 18 (Ramayana 0.1223)
- **Original**: Canto XII. The Palm Trees. 1205 The Vánar sovereign, lofty-souled, In plaintive voice his sorrows told. Then Ráma spake:“Sugríva, list, All anger from thy heart dismissed, And I will tell the cause that stayed Mine arrow, and withheld the aid. In dress, adornment, port, and height, In splendour, battle-shout, and might, No shade of difference could I see Between thy foe, O King, and thee. So like was each, I stood at gaze, My senses lost in wildering maze, Nor loosened from my straining bow A deadly arrow at the foe, Lest in my doubt the shaft should send To sudden death our surest friend. O, if this hand in heedless guilt And rash resolve thy blood had spilt, Through every land, O Vánar King, My wild and foolish act would ring. Sore weight of sin on him must lie By whom a friend is made to die; And Lakshma G, I, and Sítá, best Of dames, on thy protection rest. On, warrior! for the fight prepare; Nor fear again thy foe to dare. Within one hour thine eye shall view My arrow strike thy foeman through; Shall see the stricken Báli lie Low on the earth, and gasp and die. But come, a badge about thee bind, O monarch of the Vánar kind, That in the battle shock mine eyes The friend and foe may recognize.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1224)
- **Original**: 1206 The Ramayana Come, LakshmaG, let that creeper deck With brightest bloom Sugríva's neck, And be a happy token, twined Around the chief of lofty mind.” Upon the mountain slope there grew A threading creeper fair to view, And Lakshma G plucked the bloom and round Sugríva's neck a garland wound. Graced with the flowery wreath he wore, The Vánar chief the semblance bore Of a dark cloud at close of day Engarlanded with cranes at play, In glorious light the Vánar glowed As by his comrade's side he strode, And, still on Ráma's word intent, His steps to great Kishkindhá bent. [340] Canto XIII. The Return To Kishkindhá. Thus with Sugríva, from the side Of Rishyamúka, Ráma hied, And stood before Kishkindhá's gate Where Báli kept his regal state. The hero in his warrior hold Raised his great bow adorned with gold, And drew his pointed arrow bright As sunbeams, finisher of fight. Strong-necked Sugríva led the way With LakshmaG mighty in the fray.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1225)
- **Original**: Canto XIII. The Return To Kishkindhá. 1207 Nala and Níla came behind With Hanumán of lofty mind, And valiant Tára, last in place, A leader of the Vánar race. They gazed on many a tree that showed The glory of its pendent load, And brook and limpid rill that made Sweet murmurs as they seaward strayed. They looked on caverns dark and deep, On bower and glen and mountain steep, And saw the opening lotus stud With roseate cup the crystal flood, While crane and swan and coot and drake Made pleasant music on the lake, And from the reedy bank was heard The note of many a happy bird. In open lawns, in tangled ways, They saw the tall deer stand at gaze, Or marked them free and fearless roam, Fed with sweet grass, their woodland home. At times two flashing tusks between The wavings of the wood were seen, And some mad elephant, alone, Like a huge moving hill, was shown. And scarcely less in size appeared Great monkeys all with dust besmeared. And various birds that roam the skies, And silvan creatures, met their eyes, As through the wood the chieftains sped, And followed where Sugríva led. Then Ráma, as their way they made, Saw near at hand a lovely shade, And, as he gazed upon the trees,
- **Translation**: 

---



--- End of Ramayan_batch_159.md ---


--- Start of Ramayan_batch_160.md ---

# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Ramayana 0.1226)
- **Original**: 1208 The Ramayana Spake to Sugríva words like these; “Those stately trees in beauty rise, Fair as a cloud in autumn skies. I fain, my friend, would learn from thee What pleasant grove is that I see.” Thus Ráma spake, the mighty souled; And thus his tale Sugríva told: “That, Ráma, is a wide retreat That brings repose to weary feet. Bright streams and fruit and roots are there, And shady gardens passing fair. There, neath the roof of hanging boughs, The sacred Seven maintained their vows. Their heads in dust were lowly laid, In streams their nightly beds were made. Each seventh night they broke their fast, But air was still their sole repast, And when seven hundred years were spent To homes in heaven the hermits went. Their glory keeps the garden yet, With walls of stately trees beset. Scarce would the Gods and demons dare, By Indra led, to enter there. No beast that roams the wood is found, No bird of air, within the bound; Or, thither if they idly stray, They find no more their homeward way. You hear at times mid dulcet tones The chime of anklets, rings, and zones. You hear the song and music sound, And heavenly fragrance breathes around,
- **Translation**: 

---

### Verse 2 (Ramayana 0.1227)
- **Original**: Canto XIII. The Return To Kishkindhá. 1209 There duly burn the triple fires577 Where mounts the smoke in curling spires, And, in a dun wreath, hangs above The tall trees, like a brooding dove. Round branch and crest the vapours close Till every tree enveloped shows A hill of lazulite when clouds Hang round it with their misty shrouds. With LakshmaG, lord of Raghu's line, In reverent guise thine head incline, And with fixt heart and suppliant hand Give honour to the sainted band. They who with faithful hearts revere The holy Seven who harboured here, Shall never, son of Raghu, know In all their lives an hour of woe.” Then Ráma and his brother bent, And did obeisance reverent With suppliant hand and lowly head, Then with Sugríva onward sped. Beyond the sainted Seven's abode Far on their way the chieftains strode, And great Kishkindhá's portal gained, The royal town where Báli reigned. Then by the gate they took their stand All ready armed a noble band, And burning every one To slay in battle, hand to hand, Their foeman, Indra's son. 577 Called respectively Gárhapatya, Áhavaniya, and DakshiGa, household, sacrificial, and southern.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1228)
- **Original**: 1210 The Ramayana Canto XIV. The Challenge. They stood where trees of densest green Wove round their forms a veiling screen. O'er all the garden's pleasant shade The eyes of King Sugríva strayed,[341] And, as on grass and tree he gazed, The fires of wrath within him blazed. Then like a mighty cloud on high, When roars the tempest through the sky, Girt by his friends he thundered out His dread sky-rending battle-shout Like some proud lion in his gait, Or as the sun begins his state, Sugríva let his quick glance rest On Ráma whom he thus addressed: “There is the seat of Báli's sway, Where flags on wall and turret play, Which mighty bands of Vánars hold, Rich in all arms and store of gold. Thy promise to thy mind recall That Báli by thy hand shall fall. As kindly fruits adorn the bough. So give my hopes their harvest now.” In suppliant tone the Vánar prayed, And Raghu's son his answer made: “By LakshmaG's hand this flowery twine Was wound about thee for a sign. The wreath of giant creeper throws About thy form its brillant glows, As though about the sun were set The bright stars for a coronet. One shaft of mine this day, dear friend,
- **Translation**: 

---

### Verse 4 (Ramayana 0.1229)
- **Original**: Canto XIV. The Challenge. 1211 Thy sorrow and thy fear shall end. And, from the bowstring freed, shall be Giver of freedom, King, to thee. Then come, Sugríva, quickly show, Where'er he lie, thy bitter foe; And let my glance the wretch descry Whose deeds, a brother's name belie. Yea, soon in dust and blood o'erthrown Shall Báli fall and gasp and groan. Once let this eye the foeman see, Then, if he live to turn and flee, Despise my puny strength, and shame With foul opprobrium Ráma's name. Hast thou not seen his hand, O King, Through seven tall trees one arrow wing? Still in that strength securely trust, And deem thy foeman in the dust. In all my days, though surely tried By grief and woe, I ne'er have lied; And still by duty's law restrained Will ne'er with falsehood's charge be stained. Cast doubt away: the oath I sware Its kindly fruit shall quickly bear, As smiles the land with golden grain By mercy of the Lord of rain. Oh, warrior to the gate I defy Thy foe with shout and battle-cry, Till Báli with his chain of gold Come speeding from his royal hold. Proud hearts, with warlike fire aglow, Brook not the challenge of a foe: Each on his power and might relies, And most before his ladies eyes. King Báli loves the fray too well
- **Translation**: 

---

### Verse 5 (Ramayana 0.1230)
- **Original**: 1212 The Ramayana To linger in his citadel, And, when he hears thy battle-shout, All wild for war will hasten out.” He spoke. Sugríva raised a cry That shook and rent the echoing sky, A shout so fierce and loud and dread That stately bulls in terror fled, Like dames who fly from threatened stain In some ignoble monarch's reign. The deer in wild confusion ran Like horses turned in battle's van. Down fell the birds, like Gods who fall When merits fail,578 at that dread call. So fiercely, boldened for the fray, The offspring of the Lord of Day Sent forth his furious shout as loud As thunder from a labouring cloud, Or, where the gale blows fresh and free, The roaring of the troubled sea. Canto XV. Tárá. 578 The store of merit accumulated by a holy or austere life secures only a temporary seat in the mansion of bliss. When by the lapse of time this store is exhausted, return to earth is unavoidable.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1231)
- **Original**: Canto XV. Tárá. 1213 That shout, which shook the land with fear, In thunder smote on Báli's ear, Where in the chamber barred and closed The sovereign with his dame reposed. Each amorous thought was rudely stilled, And pride and rage his bosom filled. His angry eyes flashed darkly red, And all his native brightness fled, As when, by swift eclipse assailed, The glory of the sun has failed. While in his fury uncontrolled He ground his teeth, his eyeballs rolled, He seemed a lake wherein no gem Of blossom decks the lotus stem. He heard, and with indignant pride Forth from the bower the Vánar hied. And the earth trembled at the beat And fury of his hastening feet. But Tárá to her consort flew, Her loving arms around him threw, And trembling and bewildered, gave Wise counsel that might heal and save: “O dear my lord, this rage control That like a torrent floods thy soul, And cast these idle thoughts away Like faded wreath of yesterday, O tarry till the morning light, Then, if thou wilt, go forth and fight. [342] Think not I doubt thy valour, no; Or deem thee weaker than thy foe, Yet for a while would have thee stay Nor see thee tempt the fight to-day. Now list, my loving lord, and learn The reason why I bid thee turn.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1232)
- **Original**: 1214 The Ramayana Thy foeman came in wrath and pride, And thee to deadly fight defied. Thou wentest out: he fought, and fled Sore wounded and discomfited. But yet, untaught by late defeat, He comes his conquering foe to meet, And calls thee forth with cry and shout: Hence spring, my lord, this fear and doubt. A heart so bold that will not yield, But yearns to tempt the desperate field, Such loud defiance, fiercely pressed, On no uncertain hope can rest. So lately by thine arm o'erthrown, He comes not back, I ween, alone. Some mightier comrade guards his side, And spurs him to this burst of pride. For nature made the Vánar wise: On arms of might his hope relies; And never will Sugríva seek A friend whose power to save is weak. Now listen while my lips unfold The wondrous tale my Angad told. Our child the distant forest sought, And, learnt from spies, the tidings brought. Two sons of Da[aratha, sprung From old Ikshváku, brave and young, Renowned in arms, in war untamed— Ráma and LakshmaG are they named— Have with thy foe Sugríva made A league of love and friendly aid. Now Ráma, famed for exploit high, Is bound thy brother's firm ally,
- **Translation**: 

---

### Verse 8 (Ramayana 0.1233)
- **Original**: Canto XV. Tárá. 1215 Like fires of doom579 that ruin all He makes each foe before him fall. He is the suppliant's sure defence, The tree that shelters innocence. The poor and wretched seek his feet: In him the noblest glories meet. With skill and knowledge vast and deep His sire's commands he loved to keep; With princely gifts and graces stored As metals deck the Mountains' Lord.580 Thou canst not, O my hero, stand Before the might of Ráma's hand; For none may match his powers or dare With him in deeds of war compare. Hear, I entreat, the words I say, Nor lightly turn my rede away. O let fraternal discord cease, And link you in the bonds of peace. Let consecrating rites ordain Sugríva partner of thy reign. Let war and thoughts of conflict end, And be thou his and Ráma's friend, Each soft approach of love begin, And to thy soul thy brother win; For whether here or there he be, Thy brother still, dear lord, is he. Though far and wide these eyes I strain A friend like him I seek in vain. Let gentle words his heart incline, And gifts and honours make him thine, Till, foes no more, in love allied, You stand as brothers side by side. 579 The conflagration which destroys the world at the end of a Yuga or age. 580 Himálaya.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1234)
- **Original**: 1216 The Ramayana Thou in high rank wast wont to hold Sugríva, formed in massive mould; Then come, thy brother's love regain, For other aids are weak and vain. If thou would please my soul, and still Preserve me from all fear and ill, I pray thee by thy love be wise And do the thing which I advise. Assuage thy fruitless wrath, and shun The mightier arms of Raghu's son; For Indra's peer in might is he, A foe too strong, my lord, for thee.” Canto XVI. The Fall Of Báli. Thus Tárá with the starry eyes581 Her counsel gave with burning sighs. But Báli, by her prayers unmoved, Spurned her advice, and thus reproved: “How may this insult, scathe, and scorn By me, dear love, be tamely born? My brother, yea my foe, comes nigh And dares me forth with shout and cry. Learn, trembler! that the valiant, they Who yield no step in battle fray, Will die a thousand deaths but ne'er An unavenged dishonour bear. Nor, O my love, be thou dismayed 581 Tárá means“star.” The poet plays upon the name by comparing her beauty to that of the Lord of stars, the Moon.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1235)
- **Original**: Canto XVI. The Fall Of Báli. 1217 Though Ráma lend Sugríva aid, For one so pure and duteous, one Who loves the right, all sin will shun, Release me from thy soft embrace, And with thy dames thy steps retrace: Enough already, O mine own, Of love and sweet devotion shown. Drive all thy fear and doubt away; I seek Sugríva in the fray His boisterous rage and pride to still, And tame the foe I would not kill. My fury, armed with brandished trees, Shall strike Sugríva to his knees: [343] Nor shall the humbled foe withstand The blows of my avenging hand, When, nerved by rage and pride, I beat The traitor down beneath my feet. Thou, love, hast lent thine own sweet aid, And all thy tender care displayed; Now by my life, by these who yearn To serve thee well, I pray thee turn. But for a while, dear dame, I go To come triumphant o'er the foe.” Thus Báli spake in gentlest tone: Soft arms about his neck were thrown; Then round her lord the lady went With sad steps slow and reverent. She stood in solemn guise to bless With prayers for safety and success, Then with her train her chamber sought By grief and racking fear distraught.
- **Translation**: 

---

### Verse 11 (Ramayana 0.1236)
- **Original**: 1218 The Ramayana With serpent's pantings fierce and fast King Báli from the city passed. His glance, as each quick breath he drew, Around to find the foe he threw, And saw where fierce Sugríva showed His form with golden hues that glowed, And, as a fire resplendent, stayed To meet his foe in arms arrayed. When Báli, long-armed chieftain, found Sugríva stationed on the ground, Impelled by warlike rage he braced His warrior garb about his waist, And with his mighty arm raised high Rushed at Sugríva with a cry. But when Sugríva, fierce and bold, Saw Báli with his chain of gold, His arm he heaved, his hand he closed, And face to face his foe opposed. To him whose eyes with fury shone, In charge impetuous rushing on, Skilled in each warlike art and plan, Báli with hasty words began: “My ponderous hand, to fight addressed With fingers clenched and arm compressed Shall on thy death doomed brow descend And, crashing down, thy life shall end.” He spoke; and wild with rage and pride, The fierce Sugríva thus replied: “Thus let my arm begin the strife And from thy body crush the life.” Then Báli, wounded and enraged, With furious blows the battle waged. Sugríva seemed, with blood-streams dyed,
- **Translation**: 

---

### Verse 12 (Ramayana 0.1237)
- **Original**: Canto XVI. The Fall Of Báli. 1219 A hill with fountains in his side. But with his native force unspent A Sál tree from the earth he rent, And like the bolt of Indra smote On Báli's head and chest and throat. Bruised by the blows he could not shield, Half vanquished Báli sank and reeled, As sinks a vessel with her freight Borne down by overwhelming weight. Swift as SuparGa's582 swiftest flight In awful strength they rushed to fight: So might the sun and moon on high Encountering battle in the sky. Fierce and more fierce, as fought the foes, The furious rage of combat rose. They warred with feet and arms and knees, With nails and stones and boughs and trees, And blows descending fast as rain Dyed each dark form with crimson stain, While like two thunder-clouds they met With battle-cry and shout and threat. Then Ráma saw Sugríva quail, Marked his worn strength grow weak and fail. Saw how he turned his wistful eye To every quarter of the sky. His friend's defeat he could not brook, Bent on his shaft an eager look, Then burned to slay the conquering foe, And laid his arrow on the bow. As to an orb the bow he drew Forth from the string the arrow flew Like Fate's tremendous discus hurled 582 SuparGa, the Well-winged, is another name of Garu a the King of Birds. See p. 28, Note.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1238)
- **Original**: 1220 The Ramayana By Yáma 583 forth to end the world. So loud the din that every bird The bow-string's clans with terror heard, And wildly fled the affrighted deer As though the day of doom were near. So, deadly as the serpent's fang, Forth from the string the arrow sprang. Like the red lightning's flash and flame It flew unerring to its aim, And, hissing murder through the air, Pierced Báli's breast, and quivered there. Struck by the shaft that flew so well The mighty Vánar reeled and fell, As earthward Indra's flag they pull When A [víní's fair moon is full.584 Canto XVII. Báli's Speech. Like some proud tree before the blast Brave Báli to the ground was cast, Where prostrate in the dust he rolled Clad in the sheen of glistening gold,[344] 583 The God of Death. 584 The flag-staff erected in honour of the God Indra is lowered when the festival is over. A[víní in astronomy is the head of Aries or the first of the twenty-eight lunar mansions or asterisms.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1239)
- **Original**: Canto XVII. Báli's Speech. 1221 As when uptorn the standard lies Of the great God who rules the skies. When low upon the earth was laid The lord whom Vánar tribes obeyed, Dark as a moonless sky no more His land her joyous aspect wore. Though low in dust and mire was rolled The form of Báli lofty-souled, Still life and valour, might and grace Clung to their well-loved dwelling-place. That golden chain with rich gems set, The choicest gift of Sákra,585 yet Preserved his life nor let decay Steal strength and beauty's light away. Still from that chain divinely wrought His dusky form a glory caught, As a dark cloud, when day is done, Made splendid by the dying sun. As fell the hero, crushed in fight, There beamed afar a triple light From limbs, from chain, from shaft that drank His life-blood as the warrior sank. The never-failing shaft, impelled By the great bow which Ráma held, Brought bliss supreme, and lit the way To Brahmá's worlds which ne'er decay.586 Ráma and LakshmaG nearer drew The mighty fallen foe to view, Mahendra's son, the brave and bold, 585 Indra the father of Báli. 586 It is believed that every creature killed by Ráma obtained in consequence immediate beatitude. “And blessed the hand that gave so dear a death.”
- **Translation**: 

---

### Verse 15 (Ramayana 0.1240)
- **Original**: 1222 The Ramayana The monarch with his chain of gold, With lustrous face and tawny eyes, Broad chest, and arms of wondrous size, Like Lord Mahendra fierce in fight, Or VishGu's never-conquered might, Now fallen like Yayáti587 sent From heaven, his store of merit spent, Like the bright flame that pales and dies, Like the great sun who fires the skies, Doomed in the general doom to fall When time shall end and ruin all. The wounded Báli, when he saw Ráma and LakshmaG nearer draw, Keen words to Raghu's son, impressed With justice' holy stamp, addressed: “What fame, from one thou hast not slain In front of battle, canst thou gain, Whose secret hand has laid me low When madly fighting with my foe? From every tongue thy glory rings, A scion of a line of kings, True to thy vows, of noblest race, With every gentle gift and grace: Whose tender heart for woe can feel, And joy in every creature's weal: Whose breast with high ambition swells, Knows duty's claim and ne'er rebels. They praise thy valour, patience, ruth, 587 “Yayáti was invited to heaven by Indra, and conveyed on the way thither by Mátali, Indra's charioteer. He afterwards returned to earth where, by his virtuous administration he rendered all his subjects exempt from passion and decay.” G ARRETT 'S C. D.OF INDIA {FNS .
- **Translation**: 

---

### Verse 16 (Ramayana 0.1241)
- **Original**: Canto XVII. Báli's Speech. 1223 Thy firmness, self-restraint, and truth: Thy hand prepared for sin's control, All virtues of a princely soul. I thought of all these gifts of thine, And glories of an ancient line, I set my Tárá's tears at naught, I met Sugríva and we fought. O Ráma, till this fatal morn I held that thou wouldst surely scorn To strike me as I fought my foe And thought not of a stranger's blow, But now thine evil heart is shown, A yawning well with grass o'ergrown. Thou wearest virtue's badge,588 but guile And meanest sin thy soul defile. I took thee not for treacherous fire, A sinner clad in saint's attire; Nor deemed thou idly wouldst profess The show and garb of righteousness. In fenced town, in open land, Ne'er hast thou suffered at this hand, Nor canst of proud contempt complain: Then wherefore is the guiltless slain? My harmless life in woods I lead, On forest fruits and roots I feed. My foeman in the field I sought, And ne'er with thee, O Ráma, fought. Upon thy limbs, O King, I see The raiment of a devotee; And how can one like thee, who springs From a proud line of ancient kings, Beneath fair virtue's mask, disgrace 588 The ascetic's dress which he wore during his exile.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1242)
- **Original**: 1224 The Ramayana His lineage by a deed so base? From Raghu is thy long descent, For duteous deeds prëeminent: Why, sinner clad in saintly dress, Roamest thou through the wilderness? Truth, valour, justice free from spot, The hand that gives and grudges not, The might that strikes the sinner down, These bring a prince his best renown. Here in the woods, O King, we live On roots and fruit which branches give.589[345] Thus nature framed our harmless race: Thou art a man supreme in place. Silver and gold and land provoke The fierce attack, the robber's stroke, Canst thou desire this wild retreat, The berries and the fruit we eat? 'Tis not for mighty kings to tread The flowery path, by pleasure led. Theirs be the arm that crushes sin, Theirs the soft grace to woo and win: The steadfast will that guides the state, Wise favour to the good and great; And for all time are kings renowned Who blend these arts and ne'er confound. But thou art weak and swift to ire, Unstable, slave of each desire. Thou tramplest duty in the dust, And in thy bow is all thy trust. 589 There is much inconsistency in the passages of the poem in which the Vánars are spoken of, which seems to point to two widely different legends. The Vánars are generally represented as semi-divine beings with preternatural powers, living in houses and eating and drinking like men sometimes as here, as monkeys pure and simple, living is woods and eating fruit and roots.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1243)
- **Original**: Canto XVII. Báli's Speech. 1225 Thou carest naught for noble gain, And treatest virtue with disdain, While every sense its captive draws To follow pleasure's changing laws. I wronged thee not in word or deed, But by thy deadly dart I bleed. What wilt thou, mid the virtuous, say To purge thy lasting stain away? All these, O King, must sink to hell, The regicide, the infidel, He who in blood and slaughter joys, A Bráhman or a cow destroys, Untimely weds in law's despite Scorning an elder brother's right,590 Who dares his Teacher's bed ascend, The miser, spy, and treacherous friend. These impious wretches, one and all, Must to the hell of sinners fall. My skin the holy may not wear, Useless to thee my bones and hair; Nor may my slaughtered body be The food of devotees like thee. These five-toed things a man may slay And feed upon the fallen prey; The mailed rhinoceros may die, And, with the hare his food supply. Iguanas he may kill and eat, 590 For a younger brother to marry before the elder is a gross violation of Indian law and duty. The same law applied to daughters with the Hebrews:“It must not be so done in our country to give the younger before the first-born.” G ENESIS {FNS xix. 26.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1244)
- **Original**: 1226 The Ramayana With porcupine and tortoise meat.591 But all the wise account it sin To touch my bones and hair and skin. My flesh they may not eat; and I A useless prey, O Ráma, die. In vain my Tárá reasoned well, On dull deaf ears her counsel fell. I scorned her words though sooth and sweet, And hither rushed my fate to meet. Ah for the land thou rulest! she Finds no protection, lord, from thee, Neglected like some noble dame By a vile husband dead to shame. Mean-hearted coward, false and vile, Whose cruel soul delights in guile, Could Da[aratha, noblest king, Beget so mean and base a thing? Alas! an elephant, in form Of Ráma, in a maddening storm Of passion casting to the ground The girth of law592 that clipped him round, Too wildly passionate to feel The prick of duty's guiding steel,593 Has charged me unawares, and dead I fall beneath his murderous tread. How, stained with this my base defeat, 591 “The hedgehog and porcupine, the lizard, the rhinoceros, the tortoise, and the rabbit or hare, wise legislators declare lawful food among five-toed animals.” M ANU {FNS , v. 18. 592 “He can not buckle his distempered cause Within the belt of rule.” M ACBETH {FNS . 593 The Anku[ or iron hook with which an elephant is driven and guided.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1245)
- **Original**: Canto XVII. Báli's Speech. 1227 How wilt thou dare, where good men meet, To speak, when every tongue will blame With keen reproach this deed of shame? Such hero strength and valour, shown Upon the innocent alone, Thou hast not proved in manly strife On him who robbed thee of thy wife. Hadst thou but fought in open field And met me boldly unconcealed, This day had been thy fate to fall, Slain by this hand, to Yáma's hall. In vain I strove, and struck by thee Fell by a hand I could not see. Thus bites a snake, for sins of yore, A sleeping man who wakes no more. Sugríva's foeman thou hast killed, And thus his heart's desire fulfilled; But, Ráma, hadst thou sought me first, And told the hope thy soul has nursed, That very day had I restored The Maithil lady to her lord; And, binding RávaG with a chain, Had laid him at thy feet unslain. [346] Yea, were she sunk in deepest hell, Or whelmed beneath the ocean's swell, I would have followed on her track And brought the rescued lady back, As Hayagríva594 once set free 594 Hayagríva, Horse-necked, is a form of VishGu.
- **Translation**: 

---



--- End of Ramayan_batch_160.md ---
