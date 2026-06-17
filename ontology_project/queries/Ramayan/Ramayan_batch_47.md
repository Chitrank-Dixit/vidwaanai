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

### Verse 1 (Ramayan 0.921)
- **Original**: Canto XXIII. The Omens. 903 These feeble signs I laugh to scorn. I could bring down the stars that shine In heaven with these keen shafts of mine. Impelled by warlike fury I Could cause e'en Death himself to die. [256] I will not seek my home again Until my pointed shafts have slain This Raghu's son so fierce in pride, And Lakshma G by his brother's side. And she, my sister, she for whom These sons of Raghu meet their doom, She with delighted lips shall drain The lifeblood of her foemen slain. Fear not for me: I ne'er have known Defeat, in battle overthrown. Fear not for me, O giants; true Are the proud words I speak to you. The king of Gods who rules on high, If wild Airávat bore him nigh, Should fall before me bolt in hand: And shall these two my wrath withstand!” He ended and the giant host Who heard their chief's triumphant boast, Rejoiced with equal pride elate, Entangled in the noose of Fate. Then met on high in bright array, With eyes that longed to see the fray, God and Gandharva, sage and saint, With beings pure from earthly taint. Blest for good works aforetime wrought, Thus each to other spake his thought: “Now joy to Bráhmans, joy to kine,
- **Translation**: 

---

### Verse 2 (Ramayan 0.922)
- **Original**: 904 The Ramayana And all whom world count half divine! May Raghu's offspring slay in fight Pulastya's sons who roam by night!” In words like these and more, the best Of high-souled saints their hopes expressed, Bending their eager eyes from where Car-borne with Gods they rode in air. Beneath them stretching far, they viewed The giants' death-doomed multitude. They saw where, urged with fury, far Before the host rolled Khara's car, And close beside their leader came Twelve giant peers of might and fame. Four other chiefs463 before the rest Behind their leader DúshaG pressed. Impetuous, cruel, dark, and dread, All thirsting for the fray, The hosts of giant warriors sped Onward upon their way. With eager speed they reached the spot Where dwelt the princely two,— Like planets in a league to blot The sun and moon from view. Canto XXIV. The Host In Sight. 463 Mahákapála, Sthúláksha, Pramátha, Tri[iras.
- **Translation**: 

---

### Verse 3 (Ramayan 0.923)
- **Original**: Canto XXIV. The Host In Sight. 905 While Khara, urged by valiant rage, Drew near that little hermitage, Those wondrous signs in earth and sky Smote on each prince's watchful eye. When Ráma saw those signs of woe Fraught with destruction to the foe, With bold impatience scarce repressed His brother chief he thus addressed: “These fearful signs, my brother bold, Which threaten all our foes, behold: All laden, as they strike the view, With ruin to the fiendish crew. The angry clouds are gathering fast, Their skirts with dusty gloom o'ercast, And harsh with loud-voiced thunder, rain Thick drops of blood upon the plain. See, burning for the coming fight, My shafts with wreaths of smoke are white, And my great bow embossed with gold Throbs eager for the master's hold. Each bird that through the forest flies Sends out its melancholy cries. All signs foretell the dangerous strife, The jeopardy of limb and life. Each sight, each sound gives warning clear That foemen meet and death is near. But courage, valiant brother! well The throbbings of mine arm foretell That ruin waits the hostile powers, And triumph in the fight is ours. I hail the welcome omen: thou Art bright of face and clear of brow. For LakshmaG, when the eye can trace
- **Translation**: 

---

### Verse 4 (Ramayan 0.924)
- **Original**: 906 The Ramayana A cloud upon the warrior's face Stealing the cheerful light away, His life is doomed in battle fray. List, brother, to that awful cry: With shout and roar the fiends draw nigh. With thundering beat of many a drum The savage-hearted giants come. The wise who value safety know To meet, prepared, the coming blow: In paths of prudence trained aright They watch the stroke before it smite. Take thou thine arrows and thy bow, And with the Maithil lady go For shelter to the mountain cave Where thickest trees their branches wave. I will not have thee, LakshmaG, say One word in answer, but obey. By all thy honour for these feet Of mine, dear brother, I entreat. Thy warlike arm, I know could, smite To death these rovers of the night; But I this day would fight alone Till all the fiends be overthrown.”[257] He spake: and LakshmaG answered naught: His arrows and his bow he brought, And then with Sítá following hied For shelter to the mountain side. As LakshmaG and the lady through The forest to the cave withdrew, “'Tis well,” cried Ráma. Then he braced His coat of mail around his waist. When, bright as blazing fire, upon His mighty limbs that armour shone, The hero stood like some great light
- **Translation**: 

---

### Verse 5 (Ramayan 0.925)
- **Original**: Canto XXIV. The Host In Sight. 907 Uprising in the dark of night. His dreadful shafts were by his side; His trusty bow he bent and plied, Prepared he stood: the bowstring rang, Filling the welkin with the clang. The high-souled Gods together drew The wonder of the fight to view, The saints made free from spot and stain, And bright Gandharvas' heavenly train. Each glorious sage the assembly sought, Each saint divine of loftiest thought, And filled with zeal for Ráma's sake. Thus they whose deeds were holy spake: “Now be it well with Bráhmans, now Well with the worlds and every cow! Let Ráma in the deadly fray The fiends who walk in darkness slay, As He who bears the discus464 slew The chieftains of the Asur crew.” Then each with anxious glances viewed His fellow and his speech renewed: “There twice seven thousand giants stand With impious heart and cruel hand: Here Ráma stands, by virtue known: How can the hero fight alone?” 464 VishGu, who bears achakraor discus.
- **Translation**: 

---

### Verse 6 (Ramayan 0.926)
- **Original**: 908 The Ramayana Thus royal sage and Bráhman saint, Spirit, and Virtue free from taint, And all the Gods of heaven who rode On golden cars, their longing showed. Their hearts with doubt and terror rent, They saw the giants' armament, And Ráma clothed in warrior might, Forth standing in the front of fight. Lord of the arm no toil might tire, He stood majestic in his ire, Matchless in form as Rudra465 when His wrath is fierce on Gods or men. While Gods and saints in close array Held converse of the coming fray, The army of the fiends drew near With sight and sound that counselled fear. Long, loud and deep their war-cry pealed, As on they rushed with flag and shield, Each, of his proper valour proud, Urging to fight the demon crowd. His ponderous bow each warrior tried, And swelled his bulk with martial pride. 'Mid shout and roar and trampling feet, And thunder of the drums they beat, Loud and more loud the tumult went Throughout the forest's vast extent, And all the life that moved within The woodland trembled at the din. In eager haste all fled to find Some tranquil spot, nor looked behind. 465 Ziva.
- **Translation**: 

---

### Verse 7 (Ramayan 0.927)
- **Original**: Canto XXIV. The Host In Sight. 909 With every arm of war supplied, On-rushing wildly like the tide Of some deep sea, the giant host Approached where Ráma kept his post. Then he, in battle skilled and tried, Bent his keen eye on every side, And viewed the host of Khara face To face before his dwelling-place. He drew his arrows forth, and reared And strained that bow which foemen feared, And yielded to the vengeful sway Of fierce desire that host to slay. Terrific as the ruinous fire That ends the worlds, he glowed in ire, And his tremendous form dismayed The Gods who roam the forest shade. For in the furious wrath that glowed Within his soul the hero showed LikeZiva when his angry might Stayed Daksha's sacrificial rite.466 Like some great cloud at dawn of day When first the sun upsprings, And o'er the gloomy mass each ray A golden radiance flings: Thus showed the children of the night, Whose mail and chariots threw, With gleam of bows and armlets bright, Flashes of flamy hue. 466 See Additional Notes— D AKSHA 'S SACRIFICE {FNS .
- **Translation**: 

---

### Verse 8 (Ramayan 0.928)
- **Original**: 910 The Ramayana Canto XXV. The Battle. When Khara with the hosts he led Drew near to Ráma's leafy shed, He saw that queller of the foe Stand ready with his ordered bow. He saw, and burning at the view His clanging bow he raised and drew, And bade his driver urge apace His car to meet him face to face. Obedient to his master's hest His eager steeds the driver pressed On to the spot where, none to aid, The strong-armed chief his weapon swayed. Soon as the children of the night Saw Khara rushing to the fight,[258] His lords with loud unearthly cry Followed their chief and gathered nigh. As in his car the leader rode With all his lords around, he showed Like the red planet fiery Mars Surrounded by the lesser stars. Then with a horrid yell that rent The air, the giant chieftain sent A thousand darts in rapid shower On Ráma matchless in his power. The rovers of the night, impelled By fiery rage which naught withheld, Upon the unconquered prince, who strained His fearful bow, their arrows rained. With sword and club, with mace and pike, With spear and axe to pierce and strike, Those furious fiends on every side The unconquerable hero plied.
- **Translation**: 

---

### Verse 9 (Ramayan 0.929)
- **Original**: Canto XXV. The Battle. 911 The giant legions huge and strong, Like clouds the tempest drives along, Rushed upon Ráma with the speed Of whirling car, and mounted steed, And hill-like elephant, to slay The matchless prince in battle fray. Then upon Ráma thick and fast The rain of mortal steel they cast, As labouring clouds their torrents shed Upon the mountain-monarch's467 head. As near and nearer round him drew The warriors of the giant crew, He showed likeZiva girt by all His spirits when night's shadows fall. As the great deep receives each rill And river rushing from the hill, He bore that flood of darts, and broke With well-aimed shaft each murderous stroke. By stress of arrowy storm assailed, And wounded sore, he never failed, Like some high mountain which defies The red bolts flashing from the skies. With ruddy streams each limb was dyed From gaping wounds in breast and side, Showing the hero like the sun 'Mid crimson clouds ere day is done. Then, at that sight of terror, faint Grew God, Gandharva, sage, and saint, Trembling to see the prince oppose His single might to myriad foes. But waxing wroth, with force unspent, He strained his bow to utmost bent, 467 Himálaya.
- **Translation**: 

---

### Verse 10 (Ramayan 0.930)
- **Original**: 912 The Ramayana And forth his arrows keen and true In hundreds, yea in thousands flew,— Shafts none could ward, and none endure: Death's fatal noose was scarce so sure. As 'twere in playful ease he shot His gilded shafts, and rested not. With swiftest flight and truest aim Upon the giant hosts they came. Each smote, each stayed a foeman's breath As fatal as the coil of Death. Each arrow through a giant tore A passage, and besmeared with gore, Pursued its onward way and through The air with flamy brilliance flew. Unnumbered were the arrows sent From the great bow which Ráma bent, And every shaft with iron head The lifeblood of a giant shed. Their pennoned bows were cleft, nor mail Nor shield of hide could aught avail. For Ráma's myriad arrows tore Through arms, and bracelets which they wore, And severed mighty warriors' thighs Like trunks of elephants in size, And cut resistless passage sheer Through gold-decked horse and charioteer, Slew elephant and rider, slew The horseman and the charger too, And infantry unnumbered sent To dwell 'neath Yáma's government. Then rose on high a fearful yell Of rovers of the night, who fell Beneath that iron torrent, sore Wounded by shafts that rent and tore.
- **Translation**: 

---

### Verse 11 (Ramayan 0.931)
- **Original**: Canto XXV. The Battle. 913 So mangled by the ceaseless storm Of shafts of every kind and form, Such joy they found, as forests feel When scorched by flame, from Ráma's steel. The mightiest still the fight maintained, And furious upon Ráma rained Dart, arrow, spear, with wild attacks Of mace, and club, and battle-axe. But the great chief, unconquered yet, Their weapons with his arrows met, Which severed many a giant's head, And all the plain with corpses spread. With sundered bow and shattered shield Headless they sank upon the field, As the tall trees, that felt the blast Of Garu 's wing, to earth were cast. The giants left unslaughtered there Where filled with terror and despair, And to their leader Khara fled Faint, wounded, and discomfited. These fiery DúshaG strove to cheer, And poised his bow to calm their fear; Then fierce as He who rules the dead, When wroth, on angered Ráma sped. By DúshaG cheered, the demons cast Their dread aside and rallied fast With Sáls, rocks, palm-trees in their hands With nooses, maces, pikes, and brands, Again upon the godlike man The mighty fiends infuriate ran, These casting rocks like hail, and these A whelming shower of leafy trees. Wild, wondrous fight, the eye to scare, And raise on end each shuddering hair, [259]
- **Translation**: 

---

### Verse 12 (Ramayan 0.932)
- **Original**: 914 The Ramayana As with the fiends who loved to rove By night heroic Ráma strove! The giants in their fury plied Ráma with darts on every side. Then, by the gathering demons pressed From north and south and east and west, By showers of deadly darts assailed From every quarter fiercely hailed, Girt by the foes who swarmed around, He raised a mighty shout whose sound Struck terror. On the giant crew His great Gandharva468 arrow flew. A thousand mortal shafts were rained From the orbed bow the hero strained, Till east and west and south and north Were filled with arrows volleyed forth. They heard the fearful shout: they saw His mighty hand the bowstring draw, Yet could no wounded giant's eye See the swift storm of arrows fly. Still firm the warrior stood and cast His deadly missiles thick and fast. Dark grew the air with arrowy hail Which hid the sun as with a veil. Fiends wounded, falling, fallen, slain, All in a moment, spread the plain, And thousands scarce alive were left Mangled, and gashed, and torn, and cleft. Dire was the sight, the plain o'erspread With trophies of the mangled dead. There lay, by Ráma's missiles rent, Full many a priceless ornament, 468 One of the mysterious weapons given to Ráma.
- **Translation**: 

---

### Verse 13 (Ramayan 0.933)
- **Original**: Canto XXVI. Dúshan's Death. 915 With severed limb and broken gem, Hauberk and helm and diadem. There lay the shattered car, the steed, The elephant of noblest breed, The splintered spear, the shivered mace, Chouris and screens to shade the face. The giants saw with bitterest pain Their warriors weltering on the plain, Nor dared again his might oppose Who scourged the cities of his foes. Canto XXVI. Dúshan's Death. When Dúsha G saw his giant band Slaughtered by Ráma's conquering hand, He called five thousand fiends, and gave His orders. Bravest of the brave, Invincible, of furious might, Ne'er had they turned their backs in flight. They, as their leader bade them seize Spears, swords, and clubs, and rocks, and trees, Poured on the dauntless prince again A ceaseless shower of deadly rain. The virtuous Ráma, undismayed, Their missiles with his arrows stayed, And weakened, ere it fell, the shock Of that dire hail of tree and rock, And like a bull with eyelids closed, The pelting of the storm opposed.
- **Translation**: 

---

### Verse 14 (Ramayan 0.934)
- **Original**: 916 The Ramayana Then blazed his ire: he longed to smite To earth the rovers of the night. The wrath that o'er his spirit came Clothed him with splendour as of flame, While showers of mortal darts he poured Fierce on the giants and their lord. DúshaG, the foeman's dusky dread, By frenzied rage inspirited, On Raghu's son his missiles cast Like Indra's bolts which rend and blast. But Ráma with a trenchant dart Cleft DúshaG's ponderous bow apart. And then the gold-decked steeds who drew The chariot, with four shafts he slew. One crescent dart he aimed which shred Clean from his neck the driver's head; Three more with deadly skill addressed Stood quivering in the giant's breast. Hurled from his car, steeds, driver slain, The bow he trusted cleft in twain, He seized his mace, strong, heavy, dread, High as a mountain's towering head. With plates of gold adorned and bound, Embattled Gods it crushed and ground. Its iron spikes yet bore the stains Of mangled foemen's blood and brains. Its heavy mass of jagged steel Was like a thunderbolt to feel. It shattered, as on foes it fell, The city where the senses dwell.469 Fierce DúshaG seized that ponderous mace Like monstrous form of serpent race, 469 A periphrasis for the body.
- **Translation**: 

---

### Verse 15 (Ramayan 0.935)
- **Original**: Canto XXVI. Dúshan's Death. 917 And all his savage soul aglow With fury, rushed upon the foe. But Raghu's son took steady aim, And as the rushing giant came, Shore with two shafts the arms whereon The demon's glittering bracelets shone. His arm at each huge shoulder lopped, The mighty body reeled and dropped, And the great mace to earth was thrown Like Indra's staff when storms have blown. As some vast elephant who lies Shorn of his tusks, and bleeding dies, So, when his arms were rent away, Low on the ground the giant lay. The spirits saw the monster die, And loudly rang their joyful cry, “Honour to Ráma! nobly done! Well hast thou fought, Kakutstha's son!” [260] But the great three, the host who led, Enraged to see their chieftain dead, As though Death's toils were round them cast, Rushed upon Ráma fierce and fast, Mahákapála seized, to strike His foeman down, a ponderous pike: Sthúláksha charged with spear to fling, Pramáthi with his axe to swing. When Ráma saw, with keen darts he Received the onset of the three, As calm as though he hailed a guest In each, who came for shade and rest. Mahákapála's monstrous head Fell with the trenchant dart he sped. His good right hand in battle skilled Sthúláksha's eyes with arrows filled,
- **Translation**: 

---

### Verse 16 (Ramayan 0.936)
- **Original**: 918 The Ramayana And trusting still his ready bow He laid the fierce Pramáthi low, Who sank as some tall tree falls down With bough and branch and leafy crown. Then with five thousand shafts he slew The rest of DúshaG's giant crew: Five thousand demons, torn and rent, To Yáma's gloomy realm he sent. When Khara knew the fate of all The giant band and DúshaG's fall, He called the mighty chiefs who led His army, and in fury said: “Now Dúsha G and his armèd train Lie prostrate on the battle plain. Lead forth an army mightier still, Ráma this wretched man, to kill. Fight ye with darts of every shape, Nor let him from your wrath escape.” Thus spoke the fiend, by rage impelled, And straight his course toward Ráma held. With Zyenagámí and the rest Of his twelve chiefs he onward pressed, And every giant as he went A storm of well-wrought arrows sent. Then with his pointed shafts that came With gold and diamond bright as flame, Dead to the earth the hero threw The remnant of the demon crew. Those shafts with feathers bright as gold, Like flames which wreaths of smoke enfold, Smote down the fiends like tall trees rent By red bolts from the firmament.
- **Translation**: 

---

### Verse 17 (Ramayan 0.937)
- **Original**: Canto XXVI. Dúshan's Death. 919 A hundred shafts he pointed well: By their keen barbs a hundred fell: A thousand,— and a thousand more In battle's front lay drenched in gore. Of all defence and guard bereft, With sundered bows and harness cleft. Their bodies red with bloody stain Fell the night-rovers on the plain, Which, covered with the loosened hair Of bleeding giants prostrate there, Like some great altar showed, arrayed For holy rites with grass o'erlaid. The darksome wood, each glade and dell Where the wild demons fought and fell Was like an awful hell whose floor Is thick with mire and flesh and gore. Thus twice seven thousand fiends, a band With impious heart and bloody hand, By Raghu's son were overthrown, A man, on foot, and all alone. Of all who met on that fierce day, Khara, great chief, survived the fray, The monster of the triple head,470 And Raghu's son, the foeman's dread. The other demon warriors, all Skilful and brave and strong and tall, In front of battle, side by side, Struck down by LakshmaG's brother died. When Khara saw the host he led Triumphant forth to fight Stretched on the earth, all smitten dead, By Ráma's nobler might, 470 Tri[irás.
- **Translation**: 

---

### Verse 18 (Ramayan 0.938)
- **Original**: 920 The Ramayana Upon his foe he fiercely glared, And drove against him fast, Like Indra when his arm is bared His thundering bolt to cast. Canto XXVII. The Death Of Trisirás. But Tri[irás,471 a chieftain dread, Marked Khara as he onward sped. And met his car and cried, to stay The giant from the purposed fray: “Mine be the charge: let me attack, And turn thee from the contest back. Let me go forth, and thou shalt see The strong-armed Ráma slain by me. True are the words I speak, my lord: I swear it as I touch my sword: That I this Ráma's blood will spill, Whom every giant's hand should kill. This Ráma will I slay, or he In battle fray shall conquer me. Restrain thy spirit: check thy car, And view the combat from afar. Thou, joying o'er the prostrate foe, To Janasthán again shalt go, Or, if I fall in battle's chance, Against my conqueror advance.” 471 The Three-headed.
- **Translation**: 

---

### Verse 19 (Ramayan 0.939)
- **Original**: Canto XXVII. The Death Of Trisirás. 921 Thus Tri[irás for death who yearned: And Khara from the conflict turned, “Go forth to battle,” Khara cried; And toward his foe the giant hied. Borne on a car of glittering hue Which harnessed coursers fleetly drew, Like some huge hill with triple peak He onward rushed the prince to seek. [261] Still, like a big cloud, sending out His arrowy rain with many a shout Like the deep sullen roars that come Discordant from a moistened drum. But Raghu's son, whose watchful eye Beheld the demon rushing nigh, From the great bow he raised and bent A shower of shafts to meet him sent. Wild grew the fight and wilder yet As fiend and man in combat met, As when in some dark wood's retreat An elephant and a lion meet. The giant bent his bow, and true To Ráma's brow three arrows flew. Then, raging as he felt the stroke, These words in anger Ráma spoke: “Heroic chief! is such the power Of fiends who rove at midnight hour? Soft as the touch of flowers I feel The gentle blows thine arrows deal. Receive in turn my shafts, and know What arrows fly from Ráma's bow.” Thus as he spoke his wrath grew hot, And twice seven deadly shafts he shot, Which, dire as serpent's deadly fang,
- **Translation**: 

---

### Verse 20 (Ramayan 0.940)
- **Original**: 922 The Ramayana Straight to the giant's bosom sprang. Four arrows more,— each shaped to deal A mortal wound with barbèd steel,— The glorious hero shot, and slew The four good steeds the car that drew. Eight other shafts flew straight and fleet, And hurled the driver from his seat, And in the dust the banner laid That proudly o'er the chariot played. Then as the fiend prepared to bound Forth from his useless car to ground, The hero smote him to the heart, And numbed his arm with deadly smart. Again the chieftain, peerless-souled, Sent forth three rapid darts, and rolled With each keen arrow, deftly sped, Low in the dust a monstrous head. Then yielding to each deadly stroke, Forth spouting streams of blood and smoke, The headless trunk bedrenched with gore Fell to the ground and moved no more. The fiends who yet were left with life, Routed and crushed in battle strife, To Khara's side, like trembling deer Scared by the hunter, fled in fear. King Khara saw with furious eye His scattered giants turn and fly; Then rallying his broken train At Raghu's son he drove amain, Like Ráhu472 when his deadly might Comes rushing on the Lord of Night. 472 The demon who causes eclipses.
- **Translation**: 

---

