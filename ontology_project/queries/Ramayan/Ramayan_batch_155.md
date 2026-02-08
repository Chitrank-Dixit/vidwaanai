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

