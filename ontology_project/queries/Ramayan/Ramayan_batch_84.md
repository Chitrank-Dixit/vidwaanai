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

### Verse 1 (Ramayan 0.1661)
- **Original**: Canto LII. Dhúmráksha's Death. 1643 “What?” cried the tyrant,“are my foes Freed from the binding snakes that close With venomed clasp round head and limb, Bright as the sun and fierce like him: The spell a God bestowed of yore, The spell that never failed before? If arts like these be useless, how Shall giant strength avail us now? Go forth, Dhúmráksha, good at need, The bravest of my warriors lead: Force through the foe thy conquering way, And Ráma and the Vánars slay.” Before his king with reverence due Dhúmráksha bowed him, and withdrew. Around him at his summons came Fierce legions led by chiefs of fame. Well armed with sword and spear and mace, They hurried to the gathering place, And rushed to battle, borne at speed By elephant and car and steed. Canto LII. Dhúmráksha's Death. The Vánars saw the giant foe Pour from the gate in gallant show, [466]
- **Translation**: 

---

### Verse 2 (Ramayan 0.1662)
- **Original**: 1644 The Ramayana Rejoiced with warriors' fierce delight And shouted, longing for the fight. Near came the hosts and nearer yet: Dire was the tumult as they met, As, serried line to line opposed, The Vánars and the giants closed. Fierce on the foe the Vánars rushed, And, wielding trees, the foremost crushed; But, feathered from the heron's wing, With eager flight from sounding string, Against them shot with surest aim A ceaseless storm of arrows came: And, pierced in head and chest and side, Full many a Vánar fell and died. They perished slain in fierce attacks With sword and pike and battle-axe; But myriads following undismayed Their valour in the fight displayed. Unnumbered Vánars rent and torn With shaft and spear to earth were borne. But crushed by branchy trees and blocks Of jagged stone and shivered rocks Which the wild Vánars wielded well The bravest of the giants fell. Their trampled banners strewed the fields, And broken swords and spears and shields; And, crushed by blows which none might stay, Cars, elephants, and riders lay. Dhúmráksha turned his furious eye And saw his routed legions fly. Still dauntless, with terrific blows, He struck and slew his foremost foes. At every blow, at every thrust, He laid a Vánar in the dust.
- **Translation**: 

---

### Verse 3 (Ramayan 0.1663)
- **Original**: Canto LII. Dhúmráksha's Death. 1645 So fell they neath the sword and lance In battle's wild Gandharva961 dance, Where clang of bow and clash of sword Did duty for the silvery chord, And hoofs that rang and steeds that neighed Loud concert for the dancers made. So fiercely from Dhúmráksha's bow His arrows rained in ceaseless flow, The Vánar legions turned and fled To all the winds discomfited. Hanúmán saw the Vánars fly; He heaved a mighty rock on high. His keen eyes flashed with wrathful fire, And, rapid as the Wind his sire, Strong as the rushing tempests are, He hurled it at the advancing car. Swift through the air the missile sang: The giant from the chariot sprang, Ere crushed by that terrific blow Lay pole and wheel and flag and bow. Hanúmán's eyes with fury blazed: A mountain's rocky peak he raised, Poised it on high in act to throw, And rushed upon his giant foe. Dhúmráksha saw: he raised his mace And smote Hanúmán on the face, Who maddened by the wound's keen pang Again upon his foeman sprang; And on the giant's head the rock Descended with resistless shock. Crushed was each limb: a shapeless mass He lay upon the blood-stained grass. 961 The Gandharvas are warriors and Minstrels of Indra's heaven.
- **Translation**: 

---

### Verse 4 (Ramayan 0.1664)
- **Original**: 1646 The Ramayana Canto LIII. Vajradanshtra's Sally. When Ráva G in his palace heard The mournful news, his wrath was stirred; And, gasping like a furious snake, To Vajradanshmra thus he spake: “Go forth, my fiercest captain, lead The bravest of the giants' breed. Go forth, the sons of Raghu slay And by their side Sugríva lay.” He ceased: the chieftain bowed his head And forth with gathered troops he sped. Cars, camels, steeds were well arrayed, And coloured banners o'er them played. Rings decked his arms: about his waist The life-protecting mail was braced, And on the chieftain's forehead set Glittered his cap and coronet. Borne on a bannered car that glowed With golden sheen the warrior rode, And footmen marched with spear and sword And bow and mace behind their lord. In pomp and pride of warlike state They sallied from the southern gate, But saw, as on their way they sped, Dread signs around and overhead. For there were meteors falling fast, Though not a cloud its shadow cast; And each ill-omened bird and beast, Forboding death, the fear increased, While many a giant slipped and reeled, Falling before he reached the field.
- **Translation**: 

---

### Verse 5 (Ramayan 0.1665)
- **Original**: Canto LIV. Vajradanshtra's Death. 1647 They met in mortal strife engaged, And long and fierce the battle raged. Spears, swords uplifted, gleamed and flashed, And many a chief to earth was dashed. A ceaseless storm of arrows rained, And limbs were pierced and blood-distained. Terrific was the sound that filled The air, and every heart was chilled, As hurtling o'er the giants flew The rocks and trees which Vánars threw. Fierce as a hungry lion when Unwary deer approach his den, [467] Angad, his eyes with fury red, Waving a tree above his head, Rushed with wild charge which none could stay Where stood the giants' dense array. Like tall trees levelled by the blast Before him fell the giants fast, And earth that streamed with blood was strown With warriors, steeds, and cars o'erthrown. Canto LIV. Vajradanshtra's Death. The giant leader fiercely rained His arrows and the fight maintained. Each time the clanging cord he drew His certain shaft a Vánar slew. Then, as the creatures he has made Fly to the Lord of Life for aid, To Angad for protection fled The Vánar hosts dispirited.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1666)
- **Original**: 1648 The Ramayana Then raged the battle fiercer yet When Angad and the giant met. A hundred thousand arrows, hot With flames of fire, the giant shot; And every shaft he deftly sent His foeman's body pierced and rent. From Angad's limbs ran floods of gore: A stately tree from earth he tore, Which, maddened as his gashes bled, He hurled at his opponent's head. His bow the dauntless giant drew; To meet the tree swift arrows flew, Checked the huge missile's onward way, And harmless on the earth it lay. A while the Vánar chieftain gazed, Then from the earth a rock he raised Rent from a thunder-splitten height, And cast it with resistless might. The giant marked, and, mace in hand, Leapt from his chariot to the sand, Ere the rough mass descending broke The seat, the wheel, the pole and yoke. Then Angad seized a shattered hill, Whereon the trees were flowering still, And with full force the jagged peak Fell crashing on the giant's cheek. He staggered, reeled, and fell: the blood Gushed from the giant in a flood. Reft of his might, each sense astray, A while upon the sand he lay. But strength and wandering sense returned Again his eyes with fury burned, And with his mace upraised on high
- **Translation**: 

---

### Verse 7 (Ramayan 0.1667)
- **Original**: Canto LIV. Vajradanshtra's Death. 1649 He wounded Angad on the thigh. Then from his hand his mace he threw, And closer to his foeman drew. Then with their fists they fought, and smote On brow and cheek and chest and throat. Worn out with toil, their limbs bedewed, With blood, the strife they still renewed, Like Mercury and fiery Mars Met in fierce battle mid the stars. A while the deadly fight was stayed: Each armed him with his trusty blade Whose sheath with tinkling bells supplied, And golden net, adorned his side; And grasped his ponderous leather shield To fight till one should fall or yield. Unnumbered wounds they gave and took: Their wearied bodies reeled and shook. At length upon the sand that drank Streams of their blood the warriors sank, But as a serpent rears his head Sore wounded by a peasant's tread, So Angad, fallen on his knees, Yet gathered strength his sword to seize; And, severed by the glittering blade, The giant's head on earth was laid. [I omit Cantos LV, LVI, LVII, and LVIII, which relate how Akampan and Prahasta sally out and fall. There is little novelty of incident in these Cantos and the results are exactly the same as before. In Canto LV, Akampan, at the command of RávaG, leads forth his troops. Evil omens are seen and heard. The enemies meet, and many fall on each side, the Vánars transfixed with arrows, the Rákshases crushed with rocks and trees.
- **Translation**: 

---

### Verse 8 (Ramayan 0.1668)
- **Original**: 1650 The Ramayana In Canto LVI Akampan sees that the Rákshases are worsted, and fights with redoubled rage and vigour. The Vánars fall fast under his“nets of arrows.” Hanumán comes to the rescue. He throws mountain peaks at the giant which are dexterously stopped with flights of arrows; and at last beats him down and kills him with a tree. In Canto LVII, RávaG is seriously alarmed. He declares that he himself, KumbhakarGa or Prahasta, must go forth. Prahasta sallies out vaunting that the fowls of the air shall eat their fill of Vánar flesh. In Canto LVIII, the two armies meet. Dire is the conflict; ceaseless is the rain of stones and arrows. At last Níla meets Prahasta and breaks his bow. Prahasta leaps from his car, and the giant and the Vánar fight on foot. Níla with a huge tree crushes his opponent who falls like a tree when its roots are cut.] [468] Canto LIX. Rávan's Sally. They told him that the chief was killed, And RávaG's breast with rage was filled. Then, fiercely moved by wrath and pride, Thus to his lords the tyrant cried: “No longer, nobles, may we show This lofty scorn for such a foe By whom our bravest, with his train Of steeds and elephants, is slain. Myself this day will take the field, And Raghu's sons their lives shall yield.”
- **Translation**: 

---

### Verse 9 (Ramayan 0.1669)
- **Original**: Canto LIX. Rávan's Sally. 1651 High on the royal car, that glowed With glory from his face, he rode; And tambour shell and drum pealed out, And joyful was each giant's shout. A mighty host, with eyeballs red Like flames of kindled fire, he led. He passed the city gate, and viewed, Arrayed, the Vánar multitude, Those wielding massy rocks, and these Armed with the stems of uptorn trees, And Ráma with his eyes aglow With warlike ardour viewed the foe, And thus the brave VibhishaG, best Of weapon-wielding chiefs, addressed: “What captain leads this bright array Where lances gleam and banners play, And thousands armed with spear and sword Await the bidding of their lord?” “Seest, thou,” VibhishaG answered,“one Whose face is as the morning sun, Preëminent for hugest frame? Akampan 962 is the giant's name. Behold that chieftain, chariot-borne, Whom Brahmá's chosen gifts adorn. He wields a bow like Indra's own; A lion on his flag is shown, His eyes with baleful fire are lit: 'Tis RávaG's son, 'tis Indrajít. There, brandishing in mighty hands His huge bow, Atikáya stands. And that proud warrior o'er whose head 962 “It is to be understood,” says the commentator,“that this is not the Akampan who has already been slain.”
- **Translation**: 

---

### Verse 10 (Ramayan 0.1670)
- **Original**: 1652 The Ramayana A moon-bright canopy is spread: Whose might, in many a battle tried, Has tamed imperial Indra's pride; Who wears a crown of burnished gold, Is Lanká's lord the lofty-souled.” He ceased: and Ráma knew his foe, And laid an arrow on his bow: “Woe to the wretch,” he cried,“whom fate Abandons to my deadly hate.” He spoke, and, firm by LakshmaG's side, The giant to the fray defied. The lord of Lanká bade his train Of warriors by the gates remain, To guard the city from surprise By Ráma's forest born allies. Then as some monster of the sea Cleaves swift-advancing billows, he Charged with impetuous onset through The foe, and cleft the host in two. Sugríva ran, the king to meet: A hill uprooted from its seat He hurled, with trees that graced the height Against the rover of the night: But cleft with shafts that checked its way Harmless upon the earth it lay. Then fiercer RávaG's fury grew, An arrow from his side he drew, Swift as a thunderbolt, aglow With fire, and launched it at the foe. Through flesh and bone a way it found, And stretched Sugríva on the ground. SusheG and Nala saw him fall, Gaváksha, Gavaya heard their call,
- **Translation**: 

---

### Verse 11 (Ramayan 0.1671)
- **Original**: Canto LIX. Rávan's Sally. 1653 And, poising hills, in act to fling They charged amain the giant king. They charged, they hurled the hills in vain, He checked them with his arrowy rain, And every brave assailant felt The piercing wounds his missiles dealt, Then smitten by the shafts that came Keen, fleet, and thick, with certain aim, They fled to Ráma, sure defence Against the oppressor's violence, Then, reverent palm to palm applied, Thus LakshmaG to his brother cried: “To me, my lord, the task entrust To lay this giant in the dust.” “Go, then,” said Ráma,“bravely fight; Beat down this rover of the night. But he, unmatched in bold emprise, Fears not the Lord of earth and skies, Keep on thy guard: with keenest eye Thy moments of attack espy. Let hand and eye in due accord Protect thee with the bow and sword.” Then LakshmaG round his brother threw His mighty arms in honour due, Bent lowly down his reverent head, And onward to the battle sped. Hanúmán from afar beheld How Ráva G's shafts the Vánars quelled: To meet the giant's car he ran, Raised his right arm and thus began: “If Brahmá's boon thy life has screened From Yaksha, God, Gandharva, fiend, With these contending fear no ill,
- **Translation**: 

---

### Verse 12 (Ramayan 0.1672)
- **Original**: 1654 The Ramayana But tremble at a Vánar still.” With fury flashing from his eye The lord of Lanká made reply: “Strike, Vánar, strike: the fray begin, And hope eternal fame to win. This arm shall prove thee in the strife[469] And end thy glory and thy life.” “Remember, ” cried the Wind-God's son, “Remember all that I have done, My prowess, King, thou knowest well, Shown in the fight when Aksha963 fell.” With heavy hand the giant smote Hanúmán on the chest and throat, Who reeled and staggered to and fro, Stunned for a moment by the blow. Till, mustering strength, his hand he reared And struck the foe whom Indra feared. His huge limbs bent beneath the shock, As mountains, in an earthquake, rock, And from the Gods and sages pealed Shouts of loud triumph as he reeled. But strength returning nerved his frame: His eyeballs flashed with fiercer flame. No living creature might resist That blow of his tremendous fist Which fell upon Hanúmán's flank: And to the ground the Vánar sank, No sign of life his body showed: And RávaG in his chariot rode At Níla; and his arrowy rain Fell on the captain and his train. Fierce Níla stayed his Vánar band, 963 RávaG's son, whom Hanumán killed when he first visited Lanká.
- **Translation**: 

---

### Verse 13 (Ramayan 0.1673)
- **Original**: Canto LIX. Rávan's Sally. 1655 And, heaving with his single hand A mountain peak, with vigorous swing Hurled the huge missile at the king. Hanúmán life and strength regained, Burned for the fight and thus complained: “Why, coward giant, didst thou flee And leave the doubtful fight with me?” Seven mighty arrows keen and fleet The giant launched, the hill to meet; And, all its force and fury stayed, The harmless mass on earth was laid. Enraged the Vánar chief beheld The mountain peak by force repelled, And rained upon the foe a shower Of trees uptorn with branch and flower. Still his keen shafts which pierced and rent Each flying tree the giant sent: Still was the Vánar doomed to feel The tempest of the winged steel. Then, smarting from that arrowy storm, The Vánar chief condensed his form,964 And lightly leaping from the ground On RávaG's standard footing found; Then springing unimpeded down Stood on his bow and golden crown. The Vánar's nimble leaps amazed Ikshváku's son who stood and gazed. The giant, raging in his heart, Laid on his bow a fiery dart; The Vánar on his flagstaff eyed, And thus in tones of fury cried: 964 Níla was the son of Agni the God of Fire, and possessed, like Milton's demons, the power of dilating and condensing his form at pleasure.
- **Translation**: 

---

### Verse 14 (Ramayan 0.1674)
- **Original**: 1656 The Ramayana “Well skilled in magic lore art thou: But will thine art avail thee now? See if thy magic will defend Thy life against the dart I send.” Thus RávaG spake, the giant king, And loosed the arrow from the string. It pierced, with direst fury sped, The Vánar with its flaming head. His father's might, his power innate Preserved him from the threatened fate. Upon his knees he fell, distained With streams of blood, but life remained. Still RávaG for the battle burned: At LakshmaG next his car he turned, And charged amain with furious show, Straining in mighty hands his bow. “Come, ” Lakshma G cried,“assay the fight: Leave foes unworthy of thy might.” Thus LakshmaG spoke: and Lanká's lord Heard the dread thunder of the cord. And mad with burning rage and pride In hasty words like these replied: “Joy, joy is mine, O Raghu's son: Thy fate to-day thou canst not shun. Slain by mine arrows thou shalt tread The gloomy pathway of the dead.”
- **Translation**: 

---

### Verse 15 (Ramayan 0.1675)
- **Original**: Canto LIX. Rávan's Sally. 1657 Thus as he spoke his bow he drew, And seven keen shafts at LakshmaG flew, But Raghu's son with surest aim Cleft every arrow as it came. Thus with fleet shafts each warrior shot Against his foe, and rested not. Then one choice weapon from his store, By Brahmá's self bestowed of yore, Fierce as the flames that end the world, The giant king at LakshmaG hurled. The hero fell, and racked with pain, Scarce could his hand his bow retain. But sense and strength resumed their seat And, lightly springing to his feet, He struck with one tremendous stroke And RávaG's bow in splinters broke. From LakshmaG's cord three arrows flew And pierced the giant monarch through. Sore wounded RávaG closed, and round Ikshváku's son his strong arms wound. With strength unrivalled, Brahmá's gift, He strove from earth his foe to lift. “Shall I,” he cried,“who overthrow Mount Meru and the Lord of Snow, And heaven and all who dwell therein, Be foiled by one of Ráma's kin?” But though he heaved, and toiled, and strained, Unmoved Ikshváku's son remained. His frame by those huge arms compressed The giant's God-given force confessed, But conscious that himself was part [470] Of VishGu, he was firm in heart.
- **Translation**: 

---

### Verse 16 (Ramayan 0.1676)
- **Original**: 1658 The Ramayana The Wind-God's son the fight beheld, And rushed at RávaG, rage-impelled. Down crashed his mighty hand; the foe Full in the chest received the blow. His eyes grew dim, his knees gave way, And senseless on the earth he lay. The Wind-God's son to Ráma bore Deep-wounded LakshmaG stained with gore. He whom no foe might lift or bend Was light as air to such a friend. The dart that LakshmaG's side had cleft, Untouched, the hero's body left, And flashing through the air afar Resumed its place in RávaG's car; And, waxing well though wounded sore, He felt the deadly pain no more. And RávaG, though with deep wounds pained, Slowly his sense and strength regained, And furious still and undismayed On bow and shaft his hand he laid. Then Hanumán to Ráma cried: “Ascend my back, great chief, and ride Like VishGu borne on Garu 's wing, To battle with the giant king.” So, burning for the dire attack, Rode Ráma on the Vánar's back, And with fierce accents loud and slow Thus gave defiance to the foe, While his strained bowstring made a sound Like thunder when it shakes the ground: “Stay, Monarch of the giants, stay, The penalty of sin to pay.
- **Translation**: 

---

### Verse 17 (Ramayan 0.1677)
- **Original**: Canto LIX. Rávan's Sally. 1659 Stay! whither wilt thou fly, and how Escape the death that waits thee now?” No word the giant king returned: His eyes with flames of fury burned. His arm was stretched, his bow was bent, And swift his fiery shafts were sent. Red torrents from the Vánar flowed: Then Ráma near to RávaG strode, And with keen darts that never failed, The chariot of the king assailed. With surest aim his arrows flew: The driver and the steeds he slew. And shattered with the pointed steel Car, flag, and pole and yoke and wheel. As Indra hurls his bolt to smite Mount Meru's heaven-ascending height, So Ráma with a flaming dart Struck Lanká's monarch near the heart, Who reeled and fell beneath the blow And from loose fingers dropped his bow. Bright as the sun, with crescent head, From Ráma's bow an arrow sped, And from his forehead, proud no more, Cleft the bright coronet he wore. Then Ráma stood by RávaG's side And to the conquered giant cried: “Well hast thou fought: thine arm has slain Strong heroes of the Vánar train. I will not strike or slay thee now, For weary, faint with fight art thou. To Lanká's town thy footsteps bend, And there the night securely spend. To-morrow come with car and bow,
- **Translation**: 

---

### Verse 18 (Ramayan 0.1678)
- **Original**: 1660 The Ramayana And then my prowess shalt thou know.” He ceased: the king in humbled pride Rose from the earth and naught replied. With wounded limbs and shattered crown He sought again his royal town. Canto LX. Kumbhakarna Roused. With humbled heart and broken pride Through Lanká's gate the giant hied, Crushed, like an elephant beneath A lion's spring and murderous teeth, Or like a serpent 'neath the wing And talons of the Feathered King. Such was the giant's wild alarm At arrows shot by Ráma's arm; Shafts with red lightning round them curled, Like Brahmá's bolts that end the world.
- **Translation**: 

---

### Verse 19 (Ramayan 0.1679)
- **Original**: Canto LX. Kumbhakarna Roused. 1661 Supported on his golden throne, With failing eye and humbled tone, “Giants,” he cried,“the toil is vain, Fruitless the penance and the pain, If I whom Indra owned his peer, Secure from Gods, a mortal fear. My soul remembers, now too late, Lord Brahmá's words who spoke my fate: “Tremble, proud Giant,” thus they ran, “And dread thy death from slighted man. Secure from Gods and demons live, And serpents, by the boon I give. Against their power thy life is charmed, But against man is still unarmed.” This Ráma is the man foretold By AnaraGya's965 lips of old: “Fear, RávaG, basest of the base: For of mine own imperial race A prince in after time shall spring And thee and thine to ruin bring. And Vedavatí,966 ere she died Slain by my ruthless insult, cried: [471] “A scion of my royal line Shall slay, vile wretch, both thee and thine.” She in a later birth became King Janak's child, now Ráma's dame. 965 An ancient king of Ayodhyá said by some to have been Prithu's father. 966 The daughter of King Ku[adhwaja. She became an ascetic, and being insulted by RávaG in the woods where she was performing penance, destroyed herself by entering fire, but was born again as Sítá to be in turn the destruction of him who had insulted her.
- **Translation**: 

---

### Verse 20 (Ramayan 0.1680)
- **Original**: 1662 The Ramayana Nandí[vara967 foretold this fate, And Umá 968 when I moved her hate, And Rambhá,969 and the lovely child Of VaruG970 by my touch defiled. I know the fated hour is nigh: Hence, captains, to your stations fly. Let warders on the rampart stand: Place at each gate a watchful band; And, terror of immortal eyes, Let mightiest KumbhakarGa rise. He, slumbering, free from care and pain, By Brahmá's curse, for months has lain. But when Prahasta's death he hears, Mine own defeat and doubts and fears, The chief will rise to smite the foe And his unrivalled valour show. Then Raghu's royal sons and all The Vánars neath his might will fall.” The giant lords his hest obeyed, They left him, trembling and afraid, And from the royal palace strode To KumbhakarGa's vast abode. They carried garlands sweet and fresh, And reeking loads of blood and flesh. 967 Nandí[vara wasZiva's chief attendant. RávaG had despised and laughed at him for appearing in the form of a monkey and the irritated Nandí[vara cursed him and foretold his destruction by monkeys. 968 RávaG once upheaved and shook Mount Kailása the favourite dwelling place ofZiva the consort of Umá, and was cursed in consequence by the offended Goddess. 969 Rambhá, who has several times been mentioned in the course of the poem, was one of the nymphs of heaven, and had been insulted by RávaG. 970 Punjikasthalá was the daughter of VaruG. RávaG himself has mentioned in this book his insult to her, and the curse pronounced in consequence by Brahmá.
- **Translation**: 

---

