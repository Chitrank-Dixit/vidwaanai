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

### Verse 1 (Ramayan 0.1121)
- **Original**: Canto LXX. Kabandha. 1103 Still onward with a southern course They made their way with vigorous force, And passing through the mazes stood Beyond that vast and fearful wood. With toil and hardship yet unspent Three leagues from Janasthán they went, And speeding on their way at last Within the wood of Krauncha515 passed: A fearful forest wild and black As some huge pile of cloudy rack, Filled with all birds and beasts, where grew Bright blooms of every varied hue. On Sítá bending every thought Through all the mighty wood they sought, And at the lady's loss dismayed Here for a while and there they stayed. Then turning farther eastward they Pursued three leagues their weary way, Passed Krauncha's wood and reached the grove Where elephants rejoiced to rove. The chiefs that awful wood surveyed Where deer and wild birds filled each glade, Where scarce a step the foot could take For tangled shrub and tree and brake. There in a mountain's woody side A cave the royal brothers spied, With dread abysses deep as hell, Where darkness never ceased to dwell. When, pressing on, the lords of men Stood near the entrance of the den, They saw within the dark recess A huge misshapen giantess; 515 Or Curlews' Wood.
- **Translation**: 

---

### Verse 2 (Ramayan 0.1122)
- **Original**: 1104 The Ramayana A thing the timid heart that shook With fearful shape and savage look. Terrific fiend, her voice was fierce, Long were her teeth to rend and pierce. The monster gorged her horrid feast Of flesh of many a savage beast, While her long locks, at random flung, Dishevelled o'er her shoulders hung. Their eyes the royal brothers raised, And on the fearful monster gazed. Forth from her den she came and glanced At LakshmaG as he first advanced, Her eager arms to hold him spread, And “Come and be my love” she said, Then as she held him to her breast, The prince in words like these addressed: “Behold thy treasure fond and fair: Ayomukhi 516 the name I bear.[311] In thickets of each lofty hill, On islets of each brook and rill, With me delighted shalt thou play, And live for many a lengthened day.” Enraged he heard the monster woo; His ready sword he swiftly drew, And the sharp steel that quelled his foes Cut through her breast and ear and nose. Thus mangled by his vengeful sword In rage and pain the demon roared, And hideous with her awful face Sped to her secret dwelling place. Soon as the fiend had fled from sight, The brothers, dauntless in their might, 516 Iron-faced.
- **Translation**: 

---

### Verse 3 (Ramayan 0.1123)
- **Original**: Canto LXX. Kabandha. 1105 Reached a wild forest dark and dread Whose tangled ways were hard to tread. Then bravest LakshmaG, virtuous youth, The friend of purity and truth, With reverent palm to palm applied Thus to his glorious brother cried: “My arm presaging throbs amain, My troubled heart is sick with pain, And cheerless omens ill portend Where'er my anxious eyes I bend. Dear brother, hear my words: advance Resolved and armed for every chance, For every sign I mark to-day Foretells a peril in the way. This bird of most ill-omened note, Loud screaming with discordant throat, Announces with a warning cry That strife and victory are nigh.” Then as the chiefs their search pursued Throughout the dreary solitude, They heard amazed a mighty sound That broke the very trees around, As though a furious tempest passed Crushing the wood beneath its blast. Then Ráma raised his trusty sword, And both the hidden cause explored. There stood before their wondering eyes A fiend broad-chested, huge of size. A vast misshapen trunk they saw In height surpassing nature's law. It stood before them dire and dread Without a neck, without a head.
- **Translation**: 

---

### Verse 4 (Ramayan 0.1124)
- **Original**: 1106 The Ramayana Tall as some hill aloft in air, Its limbs were clothed with bristling hair, And deep below the monster's waist His vast misshapen mouth was placed. His form was huge, his voice was loud As some dark-tinted thunder cloud. Forth from his ample chest there came A brilliance as of gushing flame. Beneath long lashes, dark and keen The monster's single eye was seen. Deep in his chest, long, fiercely bright, It glittered with terrific light. He swallowed down his savage fare Of lion, bird, and slaughtered bear, And with huge teeth exposed to view O'er his great lips his tongue he drew. His arms unshapely, vast and dread, A league in length, he raised and spread. He seized with monstrous hands a herd Of deer and many a bear and bird. Among them all he picked and chose, Drew forward these, rejected those. Before the princely pair he stood Barring their passage through the wood. A league of shade the chiefs had passed When on the fiend their eyes they cast. A monstrous shape without a head With mighty arms before him spread, They saw that hideous trunk appear That struck the trembling eye with fear. Then, stretching to their full extent His awful arms with fingers bent, Round Raghu's princely sons he cast Each grasping limb and held them fast.
- **Translation**: 

---

### Verse 5 (Ramayan 0.1125)
- **Original**: Canto LXX. Kabandha. 1107 Though strong of arm and fierce in fight, Each armed with bow and sword to smite, The royal brothers, brave and bold, Were helpless in the giant's hold. Then Raghu's son, heroic still, Felt not a pang his bosom thrill; But young, with no protection near, His brother's heart was sad with fear, And thus with trembling tongue he said To Ráma, sore disquieted: “Ah me, ah me, my days are told: O see me in the giant's hold. Fly, son of Raghu, swiftly flee, And thy dear self from danger free. Me to the fiend an offering give; Fly at thine ease thyself and live. Thou, great Kakutstha's son, I ween, Wilt find ere long thy Maithil queen, And when thou holdest, throned again, Thine old hereditary reign, With servants prompt to do thy will, O think upon thy brother still.” As thus the trembling LakshmaG cried, The dauntless Ráma thus replied: “Brother, from causeless dread forbear. A chief like thee should scorn despair.” He spoke to soothe his wild alarm: Then fierce Kabandha517 long of arm, Among the Dánavs518 first and best, The sons of Raghu thus addressed: 517 Kabandha means a trunk. 518 A class of mythological giants. In the Epic period they were probably personifications of the aborigines of India.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1126)
- **Original**: 1108 The Ramayana “What men are you, whose shoulders show Broad as a bull's, with sword and bow, Who roam this dark and horrid place, Brought by your fate before my face? Declare by what occasion led These solitary wilds you tread, With swords and bows and shafts to pierce,[312] Like bulls whose horns are strong and fierce. Why have you sought this forest land Where wild with hunger's pangs I stand? Now as your steps my path have crossed Esteem your lives already lost.” The royal brothers heard with dread The words which fierce Kabandha said. And Ráma to his brother cried, Whose cheek by blanching fear was dried: “Alas, we fall, O valiant chief, From sorrow into direr grief, Still mourning her I hold so dear We see our own destruction near. Mark, brother, mark what power has time O'er all that live, in every clime. Now, lord of men, thyself and me Involved in fatal danger see. 'Tis not, be sure, the might of Fate That crushes all with deadly weight. Ne'er can the brave and strong, who know The use of spear and sword and bow, The force of conquering time withstand, But fall like barriers built of sand.”
- **Translation**: 

---

### Verse 7 (Ramayan 0.1127)
- **Original**: Canto LXXI. Kabandha's Speech. 1109 Thus in calm strength which naught could shake The son of Da[aratha spake, With glory yet unstained Upon Sumitrá's son he bent His eyes, and firm in his intent His dauntless heart maintained. Canto LXXI. Kabandha's Speech. Kabandha saw each chieftain stand Imprisoned by his mighty hand, Which like a snare around him pressed And thus the royal pair addressed: “Why, warriors, are your glances bent On me whom hungry pangs torment? Why stand with wildered senses? Fate Has brought you now my maw to sate.” When Lakshma G heard, a while appalled, His ancient courage he recalled, And to his brother by his side With seasonable counsel cried:
- **Translation**: 

---

### Verse 8 (Ramayan 0.1128)
- **Original**: 1110 The Ramayana “This vilest of the giant race Will draw us to his side apace. Come, rouse thee; let the vengeful sword Smite off his arms, my honoured lord. This awful giant, vast of size, On his huge strength of arm relies, And o'er the world victorious, thus With mighty force would slaughter us. But in cold blood to slay, O King, Discredit on the brave would bring, As when some victim in the rite Shuns not the hand upraised to smite.” The monstrous fiend, to anger stirred, The converse of the brothers heard. His horrid mouth he opened wide And drew the princes to his side. They, skilled due time and place to note Unsheathed their glittering swords and smote, Till from the giant's shoulders they Had hewn the mighty arms away. His trenchant falchion Ráma plied And smote him on the better side, While valiant LakshmaG on the left The arm that held him prisoned cleft. Then to the earth dismembered fell The monster with a hideous yell, And like a cloud's his deep roar went Through earth and air and firmament. Then as the giant's blood flowed fast, On his cleft limbs his eye he cast, And called upon the princely pair Their names and lineage to declare. Him then the noble LakshmaG, blest
- **Translation**: 

---

### Verse 9 (Ramayan 0.1129)
- **Original**: Canto LXXI. Kabandha's Speech. 1111 With fortune's favouring marks, addressed, And told the fiend his brother's name And the high blood of which he came: “Ikshváku's heir here Ráma stands, Illustrious through a hundred lands. I, younger brother of the heir, O fiend, the name of LakshmaG bear. His mother stole his realm away And drove him forth in woods to stray. Thus through the mighty forest he Roamed with his royal wife and me. While glorious as a God he made His dwelling in the greenwood shade, Some giant stole away his dame, And seeking her we hither came. But tell me who thou art, and why With headless trunk that towered so high, With flaming face beneath thy chest, Thou liest crushed in wild unrest.” He heard the words that LakshmaG spoke, And memory in his breast awoke, Recalling Indra's words to mind He spoke in gentle tones and kind: “O welcome best of men, are ye Whom, blest by fate, this day I see. A blessing on each trenchant blade That low on earth these arms has laid! Thou, lord of men, incline thine ear The story of my woe to hear, While I the rebel pride declare Which doomed me to the form I wear.”
- **Translation**: 

---

### Verse 10 (Ramayan 0.1130)
- **Original**: 1112 The Ramayana Canto LXXII. Kabandha's Tale. “Lord of the mighty arm, of yore A shape transcending thought I wore, And through the triple world's extent My fame for might and valour went.[313] Scarce might the sun and moon on high, ScarceZakra, with my beauty vie. Then for a time this form I took, And the great world with trembling shook. The saints in forest shades who dwelt The terror of my presence felt. But once I stirred to furious rage Great Sthúla[iras, glorious sage. Culling in woods his hermit food My hideous shape with fear he viewed. Then forth his words of anger burst That bade me live a thing accursed: “Thou, whose delight is others' pain, This grisly form shalt still retain.” Then when I prayed him to relent And fix some term of punishment,— Prayed that the curse at length might cease, He bade me thus expect release: “Let Ráma cleave thine arms away And on the pyre thy body lay, And then shalt thou, set free from doom, Thine own fair shape once more assume.” O Lakshma G, hear my words: in me The world-illustrious Danu see. By Indra's curse, subdued in fight, I wear this form which scares the sight. By sternest penance long maintained
- **Translation**: 

---

### Verse 11 (Ramayan 0.1131)
- **Original**: Canto LXXII. Kabandha's Tale. 1113 The mighty Father's grace I gained. When length of days the God bestowed, With foolish pride my bosom glowed. My life, of lengthened years assured, I deemed fromZakra's might secured. Let by my senseless pride astray I challenged Indra to the fray. A flaming bolt with many a knot With his terrific arm he shot, And straight my head and thighs compressed Were buried in my bulky chest. Deaf to each prayer and piteous call He sent me not to Yáma's hall. “Thy prayers and cries,” he said“are vain: The Father's word must true remain.” “But how may lengthened life be spent By one the bolt has torn and rent? How can I live,” I cried,“unfed, With shattered face and thighs and head?” As thus I spoke his grace to crave, Arms each a league in length he gave, And opened in my chest beneath This mouth supplied with fearful teeth. So my huge arms I used to cast Round woodland creatures as they passed, And fed within the forest here On lion, tiger, pard, and deer. Then Indra spake to soothe my grief: “When Ráma and his brother chief From thy huge bulk those arms shall cleave, Then shall the skies thy soul receive.” Disguised in this terrific shape I let no woodland thing escape, And still my longing soul was pleased
- **Translation**: 

---

### Verse 12 (Ramayan 0.1132)
- **Original**: 1114 The Ramayana Whene'er my arms a victim seized, For in these arms I fondly thought Would Ráma's self at last be caught. Thus hoping, toiling many a day I yearned to cast my life away, And here, my lord, thou standest now: Blessings be thine! for none but thou Could cleave my arms with trenchant stroke: True are the words the hermit spoke. Now let me, best of warriors, lend My counsel, and thy plans befriend, And aid thee with advice in turn If thou with fire my corse wilt burn.” As thus the mighty Danu prayed With offer of his friendly aid, While LakshmaG gazed with anxious eye, The virtuous Ráma made reply: “Lakshma G and I through forest shade From Janasthán a while had strayed. When none was near her, RávaG came And bore away my glorious dame, The giant's form and size unknown, I learn as yet his name alone. Not yet the power and might we know Or dwelling of the monstrous foe. With none our helpless feet to guide We wander here by sorrow tried. Let pity move thee to requite Our service in the funeral rite. Our hands shall bring the boughs that, dry Where elephants have rent them, lie, Then dig a pit, and light the fire To burn thee as the laws require.
- **Translation**: 

---

### Verse 13 (Ramayan 0.1133)
- **Original**: Canto LXXII. Kabandha's Tale. 1115 Do thou as meed of this declare Who stole my spouse, his dwelling where. O, if thou can, I pray thee say, And let this grace our deeds repay.” Danu had lent attentive ear The words which Ráma spoke to hear, And thus, a speaker skilled and tried, To that great orator replied: “No heavenly lore my soul endows, Naught know I of thy Maithil spouse. Yet will I, when my shape I wear, Him who will tell thee all declare. Then, Ráma, will my lips disclose His name who well that giant knows. But till the flames my corse devour This hidden knowledge mocks my power. For through that curse's withering taint My knowledge now is small and faint. Unknown the giant's very name Who bore away the Maithil dame. Cursed for my evil deeds I wore A shape which all the worlds abhor. Now ere with wearied steeds the sun Through western skies his course have run, Deep in a pit my body lay [314] And burn it in the wonted way. When in the grave my corse is placed, With fire and funeral honours graced, Then I, great chief, his name will tell Who knows the giant robber well. With him, who guides his life aright, In league of trusting love unite, And he, O valiant prince, will be
- **Translation**: 

---

### Verse 14 (Ramayan 0.1134)
- **Original**: 1116 The Ramayana A faithful friend and aid to thee. For, Ráma, to his searching eyes The triple world uncovered lies. For some dark cause of old, I ween, Through all the spheres his ways have been.” Canto LXXIII. Kabandha's Counsel. The monster ceased: the princely pair Heard great Kabandha's eager prayer. Within a mountain cave they sped, Where kindled fire with care they fed. Then LakshmaG in his mighty hands Brought ample store of lighted brands, And to a pile of logs applied The flame that ran from side to side. The spreading glow with gentle force Consumed Kabandha's mighty corse, Till the unresting flames had drunk The marrow of the monstrous trunk, As balls of butter melt away Amid the fires that o'er them play. Then from the pyre, like flame that glows Undimmed by cloudy smoke, he rose, In garments pure of spot or speck, A heavenly wreath about his neck. Resplendent in his bright attire He sprang exultant from the pyre. While from neck, arm, and foot was sent The flash of gold and ornament. High on a chariot, bright of hue,
- **Translation**: 

---

### Verse 15 (Ramayan 0.1135)
- **Original**: Canto LXXIII. Kabandha's Counsel. 1117 Which swans of fairest pinion drew, He filled each region of the air With splendid glow reflected there. Then in the sky he stayed his car And called to Ráma from afar: “Hear, chieftain, while my lips explain The means to win thy spouse again. Six plans, O prince, the wise pursue To reach the aims we hold in view.519 When evils ripening sorely press They load the wretch with new distress, So thou and LakshmaG, tried by woe, Have felt at last a fiercer blow, And plunged in bitterest grief to-day Lament thy consort torn away. There is no course but this: attend; Make, best of friends, that chief thy friend. Unless his prospering help thou gain Thy plans and hopes must all be vain. O Ráma, hear my words, and seek, Sugríva, for of him I speak. His brother Báli, Indra's son, Expelled him when the fight was won. With four great chieftains, faithful still, He dwells on Rishyamúka's hill.— Fair mountain, lovely with the flow Of Pampá's waves that glide below,— Lord of the Vánars520 just and true, Strong, very glorious, bright to view, Unmatched in counsel, firm and meek, Bound by each word his lips may speak, Good, splendid, mighty, bold and brave, 519 Peace, war, marching, halting, sowing dissensions, and seeking protection. 520 See Book I, Canto XVI.
- **Translation**: 

---

### Verse 16 (Ramayan 0.1136)
- **Original**: 1118 The Ramayana Wise in each plan to guide and save. His brother, fired by lust of sway, Drove forth the prince in woods to stray. In all thy search for Sítá he Thy ready friend and help will be. With him to aid thee in thy quest Dismiss all sorrow from thy breast. Time is a mighty power, and none His fixed decree can change or shun. So rich reward thy toil shall bless, And naught can stay thy sure success. Speed hence, O chief, without delay, To strong Sugríva take thy way. This hour thy footsteps onward bend, And make that mighty prince thy friend. With him before the attesting flame In solemn truth alliance frame. Nor wilt thou, if thy heart be wise, Sugríva, Vánar king, despise. Of boundless strength, all shapes he wears, He hearkens to a suppliant's prayers, And, grateful for each kindly deed, Will help and save in hour of need. And you, I ween, the power possess To aid his hopes and give redress. He, let his cause succeed or fail, Will help you, and you must prevail. A banished prince, in fear and woe He roams where Pampá's waters flow, True offspring of the Lord of Light Expelled by Báli's conquering might. Go, Raghu's son, that chieftain seek Who dwells on Rishyamúka's peak. Before the flame thy weapons cast
- **Translation**: 

---

### Verse 17 (Ramayan 0.1137)
- **Original**: Canto LXXIV. Kabandha's Death. 1119 And bind the bonds of friendship fast. For, prince of all the Vánar race, He in his wisdom knows each place Where dwell the fierce gigantic brood Who make the flesh of man their food. To him, O Raghu's son, to him Naught in the world is dark or dim, Where'er the mighty Day-God gleams Resplendent with a thousand beams. [315] He over rocky height and hill, Through gloomy cave, by lake and rill, Will with his Vánars seek the prize, And tell thee where thy lady lies. And he will send great chieftains forth To east and west and south and north, To seek the distant spot where she All desolate laments for thee. He even in RávaG's halls would find Thy Sítá, gem of womankind. Yea, if the blameless lady lay On Meru's loftiest steep, Or, far removed from light of day, Where hell is dark and deep, That chief of all the Vánar race His way would still explore, Meet the cowed giants face to face And thy dear spouse restore.” Canto LXXIV. Kabandha's Death.
- **Translation**: 

---

### Verse 18 (Ramayan 0.1138)
- **Original**: 1120 The Ramayana When wise Kabandha thus had taught The means to find the dame they sought, And urged them onward in the quest, He thus again the prince addressed: “This path, O Raghu's son, pursue Where those fair trees which charm the view, Extending westward far away, The glory of their bloom display, Where their bright leaves Rose-apples show, And the tall Jak and Mango grow. Whene'er you will, those trees ascend, Or the long branches shake and bend, Their savoury fruit like Amrit eat, Then onward speed with willing feet. Beyond this shady forest, decked With flowering trees, your course direct. Another grove you then will find With every joy to take the mind, Like Nandan with its charms displayed, Or Northern Kuru's blissful shade; Where trees distil their balmy juice, And fruit through all the year produce; Where shades with seasons ever fair With Chaitraratha may compare: Where trees whose sprays with fruit are bowed Rise like a mountain or a cloud. There, when you list, from time to time, The loaded trees may LakshmaG climb, Or from the shaken boughs supply Sweet fruit that may with Amrit vie. The onward path pursuing still From wood to wood, from hill to hill, Your happy eyes at length will rest
- **Translation**: 

---

### Verse 19 (Ramayan 0.1139)
- **Original**: Canto LXXIV. Kabandha's Death. 1121 On Pampá's lotus-covered breast. Her banks with gentle slope descend, Nor stones nor weed the eyes offend, And o'er smooth beds of silver sand Lotus and lily blooms expand. There swans and ducks and curlews play, And keen-eyed ospreys watch their prey, And from the limpid waves are heard Glad notes of many a water-bird. Untaught a deadly foe to fear They fly not when a man is near, And fat as balls of butter they Will, when you list, your hunger stay. Then LakshmaG with his shafts will take The fish that swim the brook and lake, Remove each bone and scale and fin, Or strip away the speckled skin, And then on iron skewers broil For thy repast the savoury spoil. Thou on a heap of flowers shalt rest And eat the meal his hands have dressed, There shalt thou lie on Pampá's brink, And Lakshma G's hand shall give thee drink, Filling a lotus leaf with cool Pure water from the crystal pool, To which the opening blooms have lent The riches of divinest scent. Beside thee at the close of day Will LakshmaG through the woodland stray, And show thee where the monkeys sleep In caves beneath the mountain steep. Loud-voiced as bulls they forth will burst And seek the flood, oppressed by thirst; Then rest a while, their wants supplied,
- **Translation**: 

---

### Verse 20 (Ramayan 0.1140)
- **Original**: 1122 The Ramayana Their well-fed bands on Pampá's side. Thou roving there at eve shalt see Rich clusters hang on shrub and tree, And Pampá flushed with roseate glow, And at the view forget thy woe. There shalt thou mark with strange delight Each loveliest flower that blooms by night, While lily buds that shrink from day Their tender loveliness display. In that far wild no hand but thine Those peerless flowers in wreaths shall twine: Immortal in their changeless pride, Ne'er fade those blooms and ne'er are dried. There erst on holy thoughts intent Their days Matanga's pupils spent. Once for their master food they sought, And store of fruit and berries brought. Then as they laboured through the dell From limb and brow the heat-drops fell: Thence sprang and bloomed those wondrous trees: Such holy power have devotees. Thus, from the hermits' heat-drops sprung, Their growth is ever fresh and young. ThereZavarí is dwelling yet, Who served each vanished anchoret.[316] Beneath the shade of holy boughs That ancient votaress keeps her vows. Her happy eyes on thee will fall, O godlike prince, adored by all, And she, whose life is pure from sin, A blissful seat in heaven will win. But cross, O son of Raghu, o'er, And stand on Pampá's western shore. A tranquil hermitage that lies
- **Translation**: 

---

