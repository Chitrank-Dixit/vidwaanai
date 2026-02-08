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

### Verse 1 (Ramayana 0.46)
- **Original**: 28 The Ramayana By whose advice he journeyed still And came to Chitrakúma's hill. How there he dwelt and built a cot; How Bharat journeyed to the spot; His earnest supplication made; Drink-offerings to their father paid; The sandals given by Ráma's hand, As emblems of his right, to stand: How from his presence Bharat went And years in Nandigráma spent. How Ráma entered DaG ak wood And in SutíkhGa's presence stood. The favour Anasúyá showed, The wondrous balsam she bestowed. How Zarabhanga's dwelling-place They sought; saw Indra face to face; The meeting with Agastya gained; The heavenly bow from him obtained. How Ráma with Virádha met; Their home in Panchavama set. How ZúrpaGakhá underwent The mockery and disfigurement. Of Tri[irá's and Khara's fall, Of RávaG roused at vengeance call, Márícha doomed, without escape; The fair Videhan55 lady's rape. How Ráma wept and raved in vain, And how the Vulture-king was slain. How Ráma fierce Kabandha slew; Then to the side of Pampá drew, Met Hanumán, and her whose vows Were kept beneath the greenwood boughs. 55 Sítá. Videha was the country of which Míthilá was the capital.
- **Translation**: 

---

### Verse 2 (Ramayana 0.47)
- **Original**: Canto III. The Argument. 29 How Raghu's son, the lofty-souled, On Pampá's bank wept uncontrolled, Then journeyed, Rishyamúk to reach, And of Sugríva then had speech. The friendship made, which both had sought: How Báli and Sugríva fought. How Báli in the strife was slain, And how Sugríva came to reign. The treaty, Tára's wild lament; The rainy nights in watching spent. The wrath of Raghu's lion son; The gathering of the hosts in one. The sending of the spies about, And all the regions pointed out. The ring by Ráma's hand bestowed; The cave wherein the bear abode. The fast proposed, their lives to end; Sampati gained to be their friend. [010] The scaling of the hill, the leap Of Hanumán across the deep. Ocean's command that bade them seek Maináka of the lofty peak. The death of Sinhiká, the sight Of Lanká with her palace bright How Hanumán stole in at eve; His plan the giants to deceive. How through the square he made his way To chambers where the women lay, Within the A[oka garden came And there found Ráma's captive dame. His colloquy with her he sought, And giving of the ring he brought. How Sítá gave a gem o'erjoyed; How Hanumán the grove destroyed.
- **Translation**: 

---

### Verse 3 (Ramayana 0.48)
- **Original**: 30 The Ramayana How giantesses trembling fled, And servant fiends were smitten dead. How Hanumán was seized; their ire When Lanká blazed with hostile fire. His leap across the sea once more; The eating of the honey store. How Ráma he consoled, and how He showed the gem from Sítá's brow. With Ocean, Ráma's interview; The bridge that Nala o'er it threw. The crossing, and the sitting down At night round Lanká's royal town. The treaty with VibhíshaG made: The plan for RávaG's slaughter laid. How Kumbhakar Ga in his pride And Meghanáda fought and died. How Ráva G in the fight was slain, And captive Sítá brought again. VibhíshaG set upon the throne; The flying chariot Pushpak shown. How Brahmá and the Gods appeared, And Sítá's doubted honour cleared. How in the flying car they rode To Bharadvája's cabin abode. The Wind-God's son sent on afar; How Bharat met the flying car. How Ráma then was king ordained; The legions their discharge obtained. How Ráma cast his queen away; How grew the people's love each day. Thus did the saint Válmíki tell Whate'er in Ráma's life befell, And in the closing verses all That yet to come will once befall.
- **Translation**: 

---

### Verse 4 (Ramayana 0.49)
- **Original**: Canto IV. The Rhapsodists. 31 Canto IV. The Rhapsodists. When to the end the tale was brought, Rose in the sage's mind the thought; “Now who throughout this earth will go, And tell it forth that all may know?” As thus he mused with anxious breast, Behold, in hermit's raiment dressed, Ku [á and Lava56 came to greet Their master and embrace his feet. The twins he saw, that princely pair Sweet-voiced, who dwelt beside him there None for the task could be more fit, For skilled were they in Holy Writ; And so the great Rámáyan, fraught With lore divine, to these he taught: The lay whose verses sweet and clear Take with delight the listening ear, That tell of Sítá's noble life And RávaG's fall in battle strife. Great joy to all who hear they bring, Sweet to recite and sweet to sing. For music's sevenfold notes are there, And triple measure,57 wrought with care With melody and tone and time, And flavours58 that enhance the rime; 56 The twin sons of Ráma and Sítá, born after Ráma had repudiated Sítá, and brought up in the hermitage of Válmíki. As they were the first rhapsodists the combined name Ku[ílava signifies a reciter of poems, or an improvisatore, even to the present day. 57 Perhaps the bass, tenor, and treble, or quick, slow and middle times. we know but little of the ancient music of the Hindus. 58 Eight flavours or sentiments are usually enumerated, love, mirth, tender- ness, anger, heroism, terror, disgust, and surprise; tranquility or content, or
- **Translation**: 

---

### Verse 5 (Ramayana 0.50)
- **Original**: 32 The Ramayana Heroic might has ample place, And loathing of the false and base, With anger, mirth, and terror, blent With tenderness, surprise, content. When, half the hermit's grace to gain, And half because they loved the strain, The youth within their hearts had stored The poem that his lips outpoured, Válmíki kissed them on the head, As at his feet they bowed, and said; “Recite ye this heroic song In tranquil shades where sages throng: Recite it where the good resort, In lowly home and royal court.” The hermit ceased. The tuneful pair, Like heavenly minstrels sweet and fair, In music's art divinely skilled, Their saintly master's word fulfilled. Like Ráma's self, from whom they came, They showed their sire in face and frame,[011] As though from some fair sculptured stone Two selfsame images had grown. Sometimes the pair rose up to sing, Surrounded by a holy ring, Where seated on the grass had met Full many a musing anchoret. Then tears bedimmed those gentle eyes, As transport took them and surprise, And as they listened every one Cried in delight, Well done! Well done! paternal tenderness, is sometimes considered the ninth. WILSON {FNS . See the Sáhitya DarpaGa or Mirror of Compositiontranslated by Dr. Ballantyne and Bábú Pramadádása Mittra in theBibliotheca Indica.
- **Translation**: 

---

### Verse 6 (Ramayana 0.51)
- **Original**: Canto IV. The Rhapsodists. 33 Those sages versed in holy lore Praised the sweet minstrels more and more: And wondered at the singers' skill, And the bard's verses sweeter still, Which laid so clear before the eye The glorious deeds of days gone by. Thus by the virtuous hermits praised, Inspirited their voice they raised. Pleased with the song this holy man Would give the youths a water-can; One gave a fair ascetic dress, Or sweet fruit from the wilderness. One saint a black-deer's hide would bring, And one a sacrificial string: One, a clay pitcher from his hoard, And one, a twisted munja cord.59 One in his joy an axe would find, One braid, their plaited locks to bind. One gave a sacrificial cup, One rope to tie their fagots up; While fuel at their feet was laid, Or hermit's stool of fig-tree made. All gave, or if they gave not, none Forgot at least a benison. Some saints, delighted with their lays, Would promise health and length of days; Others with surest words would add Some boon to make their spirit glad. In such degree of honour then That song was held by holy men: That living song which life can give, 59 Saccharum Munja is a plant from whose fibres is twisted the sacred string which a Bráhman wears over one shoulder after he has been initiated by a rite which in some respects answers to confirmation.
- **Translation**: 

---

### Verse 7 (Ramayana 0.52)
- **Original**: 34 The Ramayana By which shall many a minstrel live. In seat of kings, in crowded hall, They sang the poem, praised of all. And Ráma chanced to hear their lay, While he the votive steed60 would slay, And sent fit messengers to bring The minstrel pair before the king. They came, and found the monarch high Enthroned in gold, his brothers nigh; While many a minister below, And noble, sate in lengthened row. The youthful pair awhile he viewed Graceful in modest attitude, And then in words like these addressed His brother LakshmaG and the rest: “Come, listen to the wondrous strain Recited by these godlike twain, Sweet singers of a story fraught With melody and lofty thought.” The pair, with voices sweet and strong, Rolled the full tide of noble song, With tone and accent deftly blent To suit the changing argument. Mid that assembly loud and clear Rang forth that lay so sweet to hear, That universal rapture stole Through each man's frame and heart and soul. “These minstrels, blest with every sign That marks a high and princely line, In holy shades who dwell, Enshrined in Saint Válmíki's lay, 60 A description of an A[vamedha or Horse Sacrifice is given in Canto XIII. of this Book.
- **Translation**: 

---

### Verse 8 (Ramayana 0.53)
- **Original**: Canto V. Ayodhyá. 35 A monument to live for aye, My deeds in song shall tell.” Thus Ráma spoke: their breasts were fired, And the great tale, as if inspired, The youths began to sing, While every heart with transport swelled, And mute and rapt attention held The concourse and the king. Canto V. Ayodhyá. “Ikshváku's sons from days of old Were ever brave and mighty-souled. The land their arms had made their own Was bounded by the sea alone. Their holy works have won them praise, Through countless years, from Manu's days. Their ancient sire was Sagar, he Whose high command dug out the sea:61 With sixty thousand sons to throng Around him as he marched along. From them this glorious tale proceeds: The great Rámáyan tells their deeds. This noble song whose lines contain Lessons of duty, love, and gain, We two will now at length recite, While good men listen with delight. 61 This exploit is related in Canto XL.
- **Translation**: 

---

### Verse 9 (Ramayana 0.54)
- **Original**: 36 The Ramayana On Sarjú's62 bank, of ample size, The happy realm of Ko[al lies,[012] With fertile length of fair champaign And flocks and herds and wealth of grain. There, famous in her old renown, Ayodhyá 63 stands, the royal town, In bygone ages built and planned By sainted Manu's64 princely hand. Imperial seat! her walls extend Twelve measured leagues from end to end, And three in width from side to side, With square and palace beautified. Her gates at even distance stand; Her ample roads are wisely planned. Right glorious is her royal street Where streams allay the dust and heat. On level ground in even row Her houses rise in goodly show: Terrace and palace, arch and gate The queenly city decorate. High are her ramparts, strong and vast, By ways at even distance passed, 62 The Sarjú or Ghaghra, anciently called Sarayú, rises in the Himalayas, and after flowing through the province of Oudh, falls into the Ganges. 63 The ruins of the ancient capital of Ráma and the Children of the Sun may still be traced in the present Ajudhyá near Fyzabad. Ajudhyá is the Jerusalem or Mecca of the Hindus. 64 A legislator and saint, the son of Brahmá or a personification of Brahmá himself, the creator of the world, and progenitor of mankind. Derived from the rootman to think, the word means originallyman , the thinker, and is found in this sense in the Rig-veda. Manu as a legislator is identified with the Cretan Minos, as progenitor of mankind with the German Mannus:“Celebrant carminibus antiquis, quod unum apud illos memoriæ et annalium genus est, Tuisconem deum terra editum, et filium Mannum, originem gentis conditoresque.” TACITUS {FNS ,Germania, Cap. II.
- **Translation**: 

---

### Verse 10 (Ramayana 0.55)
- **Original**: Canto V. Ayodhyá. 37 With circling moat, both deep and wide, And store of weapons fortified. King Da[aratha, lofty-souled, That city guarded and controlled, With towering Sál trees belted round,65 And many a grove and pleasure ground, As royal Indra, throned on high, Rules his fair city in the sky.66 She seems a painted city, fair With chess-board line and even square.67 And cool boughs shade the lovely lake Where weary men their thirst may slake. There gilded chariots gleam and shine, And stately piles the Gods enshrine. There gay sleek people ever throng To festival and dance and song. A mine is she of gems and sheen, The darling home of Fortune's Queen. With noblest sort of drink and meat, The fairest rice and golden wheat, And fragrant with the chaplet's scent With holy oil and incense blent. With many an elephant and steed, And wains for draught and cars for speed. With envoys sent by distant kings, And merchants with their precious things With banners o'er her roofs that play, 65 The Sál (Shorea Robusta) is a valuable timber tree of considerable height. 66 The city of Indra is called Amarávatí or Home of the Immortals. 67 Schlegel thinks that this refers to the marble of different colours with which the houses were adorned. It seems more natural to understand it as implying the regularity of the streets and houses.
- **Translation**: 

---

### Verse 11 (Ramayana 0.56)
- **Original**: 38 The Ramayana And weapons that a hundred slay;68 All warlike engines framed by man, And every class of artisan. A city rich beyond compare With bards and minstrels gathered there, And men and damsels who entrance The soul with play and song and dance. In every street is heard the lute, The drum, the tabret, and the flute, The Veda chanted soft and low, The ringing of the archer's bow; With bands of godlike heroes skilled In every warlike weapon, filled, And kept by warriors from the foe, As Nágas guard their home below.69 There wisest Bráhmans evermore The flame of worship feed, And versed in all the Vedas' lore, Their lives of virtue lead. Truthful and pure, they freely give; They keep each sense controlled, And in their holy fervour live Like the great saints of old. Canto VI. The King. 68 The Zataghní i.e. centicide, or slayer of a hundred, is generally supposed to be a sort of fire-arms, or the ancient Indian rocket; but it is also described as a stone set round with iron spikes. 69 The Nágas (serpents) are demigods with a human face and serpent body. They inhabit Pátála or the regions under the earth. Bhogavatí is the name of their capital city. Serpents are still worshipped in India. See Fergusson'sTree and Serpent Worship.
- **Translation**: 

---

### Verse 12 (Ramayana 0.57)
- **Original**: Canto VI. The King. 39 There reigned a king of name revered, To country and to town endeared, Great Da[aratha, good and sage, Well read in Scripture's holy page: [013] Upon his kingdom's weal intent, Mighty and brave and provident; The pride of old Ikshváku's seed For lofty thought and righteous deed. Peer of the saints, for virtues famed, For foes subdued and passions tamed: A rival in his wealth untold Of Indra and the Lord of Gold. Like Manu first of kings, he reigned, And worthily his state maintained. For firm and just and ever true Love, duty, gain he kept in view, And ruled his city rich and free, Like Indra's Amarávatí. And worthy of so fair a place There dwelt a just and happy race With troops of children blest. Each man contented sought no more, Nor longed with envy for the store By richer friends possessed. For poverty was there unknown, And each man counted as his own Kine, steeds, and gold, and grain. All dressed in raiment bright and clean, And every townsman might be seen With earrings, wreath, or chain. None deigned to feed on broken fare, And none was false or stingy there. A piece of gold, the smallest pay, Was earned by labour for a day.
- **Translation**: 

---

### Verse 13 (Ramayana 0.58)
- **Original**: 40 The Ramayana On every arm were bracelets worn, And none was faithless or forsworn, A braggart or unkind. None lived upon another's wealth, None pined with dread or broken health, Or dark disease of mind. High-souled were all. The slanderous word, The boastful lie, were never heard. Each man was constant to his vows, And lived devoted to his spouse. No other love his fancy knew, And she was tender, kind, and true. Her dames were fair of form and face, With charm of wit and gentle grace, With modest raiment simply neat, And winning manners soft and sweet. The twice-born sages, whose delight Was Scripture's page and holy rite, Their calm and settled course pursued, Nor sought the menial multitude. In many a Scripture each was versed, And each the flame of worship nursed, And gave with lavish hand. Each paid to Heaven the offerings due, And none was godless or untrue In all that holy band. To Bráhmans, as the laws ordain, The Warrior caste were ever fain The reverence due to pay; And these the Vai[yas' peaceful crowd, Who trade and toil for gain, were proud To honour and obey; And all were by theZúdras70 served, 70 The fourth and lowest pure caste whose duty was to serve the three first
- **Translation**: 

---

### Verse 14 (Ramayana 0.59)
- **Original**: Canto VI. The King. 41 Who never from their duty swerved, Their proper worship all addressed To Bráhman, spirits, God, and guest. Pure and unmixt their rites remained, Their race's honour ne'er was stained.71 Cheered by his grandsons, sons, and wife, Each passed a long and happy life. Thus was that famous city held By one who all his race excelled, Blest in his gentle reign, As the whole land aforetime swayed By Manu, prince of men, obeyed Her king from main to main. And heroes kept her, strong and brave, As lions guard their mountain cave: Fierce as devouring flame they burned, And fought till death, but never turned. Horses had she of noblest breed, Like Indra's for their form and speed, From Váhlí's72 hills and Sindhu's73 sand, classes. 71 By forbidden marriages between persons of different castes. 72 Váhlí or Váhlíka is Bactriana; its name is preserved in the modern Balkh. 73 The Sanskrit word Sindhu is in the singular the name of the river Indus, in the plural of the people and territories on its banks. The name appears asHidku in the cuneiform inscription of Darius' son of Hystaspes, in which the nations tributary to that king are enumerated. The Hebrew form isHodda (Esther, I. 1.). In Zend it appears asHendu in a somewhat wider sense. With the Persians later the signification ofHind seems to have co-extended with their increasing acquaintance with the country. The weak Ionic dialect omitted the Persianh, and we find in Hecatæus and Herodotus<½´¿Â and ! 8 ½´¹ºu. In this form the Romans received the names and transmitted them to us. The Arabian geographers in their ignorance that Hind and Sind are two forms of the same word have made of them two brothers and traced their decent from Noah. See Lassen's Indische Alterthumskunde Vol. I. pp. 2, 3.
- **Translation**: 

---

### Verse 15 (Ramayana 0.60)
- **Original**: 42 The Ramayana Vanáyu74 and Kámboja's land.75[014] Her noble elephants had strayed Through Vindhyan and Himálayan shade, Gigantic in their bulk and height, Yet gentle in their matchless might. They rivalled well the world-spread fame Of the great stock from which they came, Of Váman, vast of size, Of Mahápadma's glorious line, Thine, Anjan, and, Airávat, thine.76 Upholders of the skies. With those, enrolled in fourfold class, Who all their mighty kin surpass, Whom men Matangas name, And Mrigas spotted black and white, And Bhadras of unwearied might, And Mandras hard to tame.77 Thus, worthy of the name she bore,78 Ayodhyá for a league or more Cast a bright glory round, Where Da[aratha wise and great 74 The situation of Vanáyu is not exactly determined: it seems to have lain to the north-west of India. 75 Kámboja was probably still further to the north-west. Lassen thinks that the name is etymologically connected withCambyses which in the cuneiform inscription of Behistun is written Ka(m)bujia. 76 The elephants of Indra and other deities who preside over the four points of the compass. 77 “There are four kinds of elephants. 1Bhaddar. It is well proportioned, has an erect head, a broad chest, large ears, a long tail, and is bold and can bear fatigue. 2Mand . It is black, has yellow eyes, a uniformly sized body, and is wild and ungovernable. 3Mirg. It has a whitish skin, with black spots. 4Mir. It has a small head, and obeys readily. It gets frightened when it thunders.” Aín-i-Akbarí.. Translated by H. Blochmann, Aín 41,The Imperial Elephant Stables. 78 Ayodhyá means not to be fought against.
- **Translation**: 

---

### Verse 16 (Ramayana 0.61)
- **Original**: Canto VII. The Ministers. 43 Governed his fair ancestral state, With every virtue crowned. Like Indra in the skies he reigned In that good town whose wall contained High domes and turrets proud, With gates and arcs of triumph decked, And sturdy barriers to protect Her gay and countless crowd. Canto VII. The Ministers. Two sages, holy saints, had he, His ministers and priests to be: Va [ishmha, faithful to advise, And Vámadeva, Scripture-wise. Eight other lords around him stood, All skilled to counsel, wise and good: Jayanta, Vijay, Dhrishmi bold In fight, affairs of war controlled: Siddhárth and Arthasádhak true Watched o'er expense and revenue, And Dharmapál and wise A[ok Of right and law and justice spoke. With these the sage Sumantra, skilled To urge the car, high station filled. All these in knowledge duly trained Each passion and each sense restrained: With modest manners, nobly bred Each plan and nod and look they read, Upon their neighbours' good intent, Most active and benevolent:
- **Translation**: 

---

### Verse 17 (Ramayana 0.62)
- **Original**: 44 The Ramayana As sit the Vasus79 round their king, They sate around him counselling. They ne'er in virtue's loftier pride Another's lowly gifts decried. In fair and seemly garb arrayed, No weak uncertain plans they made. Well skilled in business, fair and just, They gained the people's love and trust, And thus without oppression stored The swelling treasury of their lord. Bound in sweet friendship each to each, They spoke kind thoughts in gentle speech. They looked alike with equal eye On every caste, on low and high. Devoted to their king, they sought, Ere his tongue spoke, to learn his thought, And knew, as each occasion rose, To hide their counsel or disclose. In foreign lands or in their own Whatever passed, to them was known. By secret spies they timely knew What men were doing or would do. Skilled in the grounds of war and peace They saw the monarch's state increase, Watching his weal with conquering eye That never let occasion by, While nature lent her aid to bless Their labours with unbought success. Never for anger, lust, or gain, Would they their lips with falsehood stain. Inclined to mercy they could scan The weakness and the strength of man. 79 Attendants of Indra, eight Gods whose names signify fire, light and its phenomena.
- **Translation**: 

---

### Verse 18 (Ramayana 0.63)
- **Original**: Canto VIII. Sumantra's Speech. 45 They fairly judged both high and low, And ne'er would wrong a guiltless foe; Yet if a fault were proved, each one Would punish e'en his own dear son. But there and in the kingdom's bound No thief or man impure was found: None of loose life or evil fame, No tempter of another's dame. Contented with their lot each caste [015] Calm days in blissful quiet passed; And, all in fitting tasks employed, Country and town deep rest enjoyed, With these wise lords around his throne The monarch justly reigned, And making every heart his own The love of all men gained. With trusty agents, as beseems, Each distant realm he scanned, As the sun visits with his beams Each corner of the land. Ne'er would he on a mightier foe With hostile troops advance, Nor at an equal strike a blow In war's delusive chance. These lords in council bore their part With ready brain and faithful heart, With skill and knowledge, sense and tact, Good to advise and bold to act. And high and endless fame he won With these to guide his schemes, As, risen in his might, the sun Wins glory with his beams.
- **Translation**: 

---

### Verse 19 (Ramayana 0.64)
- **Original**: 46 The Ramayana Canto VIII. Sumantra's Speech. But splendid, just, and great of mind, The childless king for offspring pined. No son had he his name to grace, Transmitter of his royal race. Long had his anxious bosom wrought, And as he pondered rose the thought: “A votive steed 'twere good to slay, So might a son the gift repay.” Before his lords his plan he laid, And bade them with their wisdom aid: Then with these words Sumantra, best Of royal counsellors, addressed: “Hither, Va[ishmha at their head, Let all my priestly guides be led.” To him Sumantra made reply: “Hear, Sire, a tale of days gone by. To many a sage in time of old, Sanatkumár, the saint, foretold How from thine ancient line, O King, A son, when years came round, should spring. “Here dwells,” 'twas thus the seer began, “Of Ka[yap's80 race, a holy man, VibháGdak named: to him shall spring A son, the famous Rishya[ring. Bred with the deer that round him roam, The wood shall be that hermit's home. To him no mortal shall be known Except his holy sire alone. Still by those laws shall he abide 80 Ka [yap was a grandson of the God Brahmá. He is supposed to have given his name to Kashmír = Ka[yapa-míra, Ka[yap's Lake.
- **Translation**: 

---

### Verse 20 (Ramayana 0.65)
- **Original**: Canto VIII. Sumantra's Speech. 47 Which lives of youthful Bráhmans guide, Obedient to the strictest rule That forms the young ascetic's school: And all the wondering world shall hear Of his stern life and penance drear; His care to nurse the holy fire And do the bidding of his sire. Then, seated on the Angas'81 throne, Shall Lomapád to fame be known. But folly wrought by that great king A plague upon the land shall bring; No rain for many a year shall fall And grievous drought shall ruin all. The troubled king with many a prayer Shall bid the priests some cure declare: “The lore of Heaven 'tis yours to know, Nor are ye blind to things below: Declare, O holy men, the way This plague to expiate and stay.” Those best of Bráhmans shall reply: “By every art, O Monarch, try Hither to bring VibháGdak's child, Persuaded, captured, or beguiled. And when the boy is hither led To him thy daughter duly wed.” 81 The people of Anga.“Anga is said in the lexicons to be Bengal; but here certainly another region is intended situated at the confluence of the Sarjú with the Ganges, and not far distant from Da[aratha's dominions.” G ORRESIO {FNS . It comprised part of Behar and Bhagulpur.
- **Translation**: 

---

