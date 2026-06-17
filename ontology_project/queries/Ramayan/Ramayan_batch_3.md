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

### Verse 1 (Ramayan 0.41)
- **Original**: Canto II. Brahmá's Visit 23 Then glorious Brahmá,47 Lord Most High, Creator of the earth and sky, [008] The four-faced God, to meet the sage Came to Válmíki's hermitage. Soon as the mighty God he saw, Up sprang the saint in wondering awe. Mute, with clasped hands, his head he bent, And stood before him reverent. His honoured guest he greeted well, Who bade him of his welfare tell; Gave water for his blessed feet, Brought offerings,48 and prepared a seat. In honoured place the God Most High Sate down, and bade the saint sit nigh. There sate before Válmíki's eyes The Father of the earth and skies; But still the hermit's thoughts were bent On one thing only, all intent On that poor curlew's mournful fate Lamenting for her slaughtered mate; And still his lips, in absent mood, The verse that told his grief, renewed: 47 Brahmá, the Creator, is usually regarded as the first person of the divine triad of India. The four heads with which he is represented are supposed to have allusion to the four corners of the earth which he is sometimes considered to personify. As an object of adoration Brahmá has been entirely superseded by Ziva and VishGu. In the whole of India there is, I believe, but one temple dedicated to his worship. In this point the first of the Indian triad curiously resembles the last of the divine fraternity of Greece, Aïdes the brother of Zeus and Poseidon.“In all Greece, says Pausanias, there is no single temple of Aïdes, except at a single spot in Elis.” See Gladstone's Juventus Mundi, p. 253. 48 The argha or arghya was a libation or offering to a deity, a Bráhman, or other venerable personage. According to one authority it consisted of water, milk, the points of Kúsa-grass, curds, clarified butter, rice, barley, and white mustard, according to another, of saffron, bel, unbroken grain, flowers, curds, dúrbá-grass, kúsa-grass, and sesamum.
- **Translation**: 

---

### Verse 2 (Ramayan 0.42)
- **Original**: 24 The Ramayana “Woe to the fowler's impious hand That did the deed that folly planned; That could to needless death devote The curlew of the tuneful throat!” The heavenly Father smiled in glee, And said,“O best of hermits, see, A verse, unconscious, thou hast made; No longer be the task delayed. Seek not to trace, with labour vain, The unpremeditated strain. The tuneful lines thy lips rehearsed Spontaneous from thy bosom burst. Then come, O best of seers, relate The life of Ráma good and great, The tale that saintly Nárad told, In all its glorious length unfold. Of all the deeds his arm has done Upon this earth, omit not one, And thus the noble life record Of that wise, brave, and virtuous lord. His every act to day displayed, His secret life to none betrayed: How Lakshma G, how the giants fought; With high emprise and hidden thought: And all that Janak's child49 befell Where all could see, where none could tell. The whole of this shall truly be Made known, O best of saints, to thee. In all thy poem, through my grace, No word of falsehood shall have place. Begin the story, and rehearse The tale divine in charming verse. 49 Sítá, daughter of Janak king of Míthilá.
- **Translation**: 

---

### Verse 3 (Ramayan 0.43)
- **Original**: Canto II. Brahmá's Visit 25 As long as in this firm-set land The streams shall flow, the mountains stand, So long throughout the world, be sure, The great Rámáyan shall endure.50 While the Rámáyan's ancient strain Shall glorious in the earth remain, To higher spheres shalt thou arise And dwell with me above the skies.” He spoke, and vanished into air, And left Válmíki wondering there. The pupils of the holy man, Moved by their love of him, began To chant that verse, and ever more They marvelled as they sang it o'er: “Behold, the four-lined balanced rime, Repeated over many a time, In words that from the hermit broke In shock of grief, becomes a[loke.” This measure now Válmíki chose Wherein his story to compose. In hundreds of such verses, sweet With equal lines and even feet, The saintly poet, lofty-souled, The glorious deeds of Ráma told. 50 “I congratulate myself,” says Schlegel in the preface to his, alas, unfinished edition of the Rámáyan,“that, by the favour of the Supreme Deity, I have been allowed to begin so great a work; I glory and make my boast that I too after so many ages have helped to confirm that ancient oracle declared to Válmíki by the Father of Gods and men: Dum stabunt montes, campis dum flumina current, Usque tuum toto carmen celebrabitur orbe.”
- **Translation**: 

---

### Verse 4 (Ramayan 0.44)
- **Original**: 26 The Ramayana Canto III. The Argument. The hermit thus with watchful heed Received the poem's pregnant seed, And looked with eager thought around If fuller knowledge might be found.[009] His lips with water first bedewed,51 He sate, in reverent attitude On holy grass,52 the points all bent Together toward the orient;53 And thus in meditation he Entered the path of poesy. Then clearly, through his virtue's might, All lay discovered to his sight, Whate'er befell, through all their life, Ráma, his brother, and his wife: And Da [aratha and each queen At every time, in every scene: His people too, of every sort; The nobles of his princely court: Whate'er was said, whate'er decreed, Each time they sate each plan and deed: For holy thought and fervent rite Had so refined his keener sight That by his sanctity his view The present, past, and future knew, And he with mental eye could grasp, Like fruit within his fingers clasp, 51 “The sipping of water is a requisite introduction of all rites: without it, says the Sámha Purána, all acts of religion are vain.” C OLEBROOKE .{FNS 52 The darhha orku[a (Pea cynosuroides), a kind of grass used in sacrifice by the Hindus ascerbenawas by the Romans. 53 The direction in which the grass should be placed upon the ground as a seat for the Gods, on occasion of offerings made to them.
- **Translation**: 

---

### Verse 5 (Ramayan 0.45)
- **Original**: Canto III. The Argument. 27 The life of Ráma, great and good, Roaming with Sítá in the wood. He told, with secret-piercing eyes, The tale of Ráma's high emprise, Each listening ear that shall entice, A sea of pearls of highest price. Thus good Válmíki, sage divine, Rehearsed the tale of Raghu's line, As Nárad, heavenly saint, before Had traced the story's outline o'er. He sang of Ráma's princely birth, His kindness and heroic worth; His love for all, his patient youth, His gentleness and constant truth, And many a tale and legend old By holy Vi[vámitra told. How Janak's child he wooed and won, And broke the bow that bent to none. How he with every virtue fraught His namesake Ráma54 met and fought. The choice of Ráma for the throne; The malice by Kaikeyí shown, Whose evil counsel marred the plan And drove him forth a banisht man. How the king grieved and groaned, and cried, And swooned away and pining died. The subjects' woe when thus bereft; And how the following crowds he left: With Guha talked, and firmly stern Ordered his driver to return. How Gangá's farther shore he gained; By Bharadvája entertained, 54 Para[uráma or Ráma with the Axe. See Canto LXXIV.
- **Translation**: 

---

### Verse 6 (Ramayan 0.46)
- **Original**: 28 The Ramayana By whose advice he journeyed still And came to Chitrakúma's hill. How there he dwelt and built a cot; How Bharat journeyed to the spot; His earnest supplication made; Drink-offerings to their father paid; The sandals given by Ráma's hand, As emblems of his right, to stand: How from his presence Bharat went And years in Nandigráma spent. How Ráma entered DaG ak wood And in SutíkhGa's presence stood. The favour Anasúyá showed, The wondrous balsam she bestowed. How Zarabhanga's dwelling-place They sought; saw Indra face to face; The meeting with Agastya gained; The heavenly bow from him obtained. How Ráma with Virádha met; Their home in Panchavama set. How ZúrpaGakhá underwent The mockery and disfigurement. Of Tri[irá's and Khara's fall, Of RávaG roused at vengeance call, Márícha doomed, without escape; The fair Videhan55 lady's rape. How Ráma wept and raved in vain, And how the Vulture-king was slain. How Ráma fierce Kabandha slew; Then to the side of Pampá drew, Met Hanumán, and her whose vows Were kept beneath the greenwood boughs. 55 Sítá. Videha was the country of which Míthilá was the capital.
- **Translation**: 

---

### Verse 7 (Ramayan 0.47)
- **Original**: Canto III. The Argument. 29 How Raghu's son, the lofty-souled, On Pampá's bank wept uncontrolled, Then journeyed, Rishyamúk to reach, And of Sugríva then had speech. The friendship made, which both had sought: How Báli and Sugríva fought. How Báli in the strife was slain, And how Sugríva came to reign. The treaty, Tára's wild lament; The rainy nights in watching spent. The wrath of Raghu's lion son; The gathering of the hosts in one. The sending of the spies about, And all the regions pointed out. The ring by Ráma's hand bestowed; The cave wherein the bear abode. The fast proposed, their lives to end; Sampati gained to be their friend. [010] The scaling of the hill, the leap Of Hanumán across the deep. Ocean's command that bade them seek Maináka of the lofty peak. The death of Sinhiká, the sight Of Lanká with her palace bright How Hanumán stole in at eve; His plan the giants to deceive. How through the square he made his way To chambers where the women lay, Within the A[oka garden came And there found Ráma's captive dame. His colloquy with her he sought, And giving of the ring he brought. How Sítá gave a gem o'erjoyed; How Hanumán the grove destroyed.
- **Translation**: 

---

### Verse 8 (Ramayan 0.48)
- **Original**: 30 The Ramayana How giantesses trembling fled, And servant fiends were smitten dead. How Hanumán was seized; their ire When Lanká blazed with hostile fire. His leap across the sea once more; The eating of the honey store. How Ráma he consoled, and how He showed the gem from Sítá's brow. With Ocean, Ráma's interview; The bridge that Nala o'er it threw. The crossing, and the sitting down At night round Lanká's royal town. The treaty with VibhíshaG made: The plan for RávaG's slaughter laid. How Kumbhakar Ga in his pride And Meghanáda fought and died. How Ráva G in the fight was slain, And captive Sítá brought again. VibhíshaG set upon the throne; The flying chariot Pushpak shown. How Brahmá and the Gods appeared, And Sítá's doubted honour cleared. How in the flying car they rode To Bharadvája's cabin abode. The Wind-God's son sent on afar; How Bharat met the flying car. How Ráma then was king ordained; The legions their discharge obtained. How Ráma cast his queen away; How grew the people's love each day. Thus did the saint Válmíki tell Whate'er in Ráma's life befell, And in the closing verses all That yet to come will once befall.
- **Translation**: 

---

### Verse 9 (Ramayan 0.49)
- **Original**: Canto IV. The Rhapsodists. 31 Canto IV. The Rhapsodists. When to the end the tale was brought, Rose in the sage's mind the thought; “Now who throughout this earth will go, And tell it forth that all may know?” As thus he mused with anxious breast, Behold, in hermit's raiment dressed, Ku [á and Lava56 came to greet Their master and embrace his feet. The twins he saw, that princely pair Sweet-voiced, who dwelt beside him there None for the task could be more fit, For skilled were they in Holy Writ; And so the great Rámáyan, fraught With lore divine, to these he taught: The lay whose verses sweet and clear Take with delight the listening ear, That tell of Sítá's noble life And RávaG's fall in battle strife. Great joy to all who hear they bring, Sweet to recite and sweet to sing. For music's sevenfold notes are there, And triple measure,57 wrought with care With melody and tone and time, And flavours58 that enhance the rime; 56 The twin sons of Ráma and Sítá, born after Ráma had repudiated Sítá, and brought up in the hermitage of Válmíki. As they were the first rhapsodists the combined name Ku[ílava signifies a reciter of poems, or an improvisatore, even to the present day. 57 Perhaps the bass, tenor, and treble, or quick, slow and middle times. we know but little of the ancient music of the Hindus. 58 Eight flavours or sentiments are usually enumerated, love, mirth, tender- ness, anger, heroism, terror, disgust, and surprise; tranquility or content, or
- **Translation**: 

---

### Verse 10 (Ramayan 0.50)
- **Original**: 32 The Ramayana Heroic might has ample place, And loathing of the false and base, With anger, mirth, and terror, blent With tenderness, surprise, content. When, half the hermit's grace to gain, And half because they loved the strain, The youth within their hearts had stored The poem that his lips outpoured, Válmíki kissed them on the head, As at his feet they bowed, and said; “Recite ye this heroic song In tranquil shades where sages throng: Recite it where the good resort, In lowly home and royal court.” The hermit ceased. The tuneful pair, Like heavenly minstrels sweet and fair, In music's art divinely skilled, Their saintly master's word fulfilled. Like Ráma's self, from whom they came, They showed their sire in face and frame,[011] As though from some fair sculptured stone Two selfsame images had grown. Sometimes the pair rose up to sing, Surrounded by a holy ring, Where seated on the grass had met Full many a musing anchoret. Then tears bedimmed those gentle eyes, As transport took them and surprise, And as they listened every one Cried in delight, Well done! Well done! paternal tenderness, is sometimes considered the ninth. WILSON {FNS . See the Sáhitya DarpaGa or Mirror of Compositiontranslated by Dr. Ballantyne and Bábú Pramadádása Mittra in theBibliotheca Indica.
- **Translation**: 

---

### Verse 11 (Ramayan 0.51)
- **Original**: Canto IV. The Rhapsodists. 33 Those sages versed in holy lore Praised the sweet minstrels more and more: And wondered at the singers' skill, And the bard's verses sweeter still, Which laid so clear before the eye The glorious deeds of days gone by. Thus by the virtuous hermits praised, Inspirited their voice they raised. Pleased with the song this holy man Would give the youths a water-can; One gave a fair ascetic dress, Or sweet fruit from the wilderness. One saint a black-deer's hide would bring, And one a sacrificial string: One, a clay pitcher from his hoard, And one, a twisted munja cord.59 One in his joy an axe would find, One braid, their plaited locks to bind. One gave a sacrificial cup, One rope to tie their fagots up; While fuel at their feet was laid, Or hermit's stool of fig-tree made. All gave, or if they gave not, none Forgot at least a benison. Some saints, delighted with their lays, Would promise health and length of days; Others with surest words would add Some boon to make their spirit glad. In such degree of honour then That song was held by holy men: That living song which life can give, 59 Saccharum Munja is a plant from whose fibres is twisted the sacred string which a Bráhman wears over one shoulder after he has been initiated by a rite which in some respects answers to confirmation.
- **Translation**: 

---

### Verse 12 (Ramayan 0.52)
- **Original**: 34 The Ramayana By which shall many a minstrel live. In seat of kings, in crowded hall, They sang the poem, praised of all. And Ráma chanced to hear their lay, While he the votive steed60 would slay, And sent fit messengers to bring The minstrel pair before the king. They came, and found the monarch high Enthroned in gold, his brothers nigh; While many a minister below, And noble, sate in lengthened row. The youthful pair awhile he viewed Graceful in modest attitude, And then in words like these addressed His brother LakshmaG and the rest: “Come, listen to the wondrous strain Recited by these godlike twain, Sweet singers of a story fraught With melody and lofty thought.” The pair, with voices sweet and strong, Rolled the full tide of noble song, With tone and accent deftly blent To suit the changing argument. Mid that assembly loud and clear Rang forth that lay so sweet to hear, That universal rapture stole Through each man's frame and heart and soul. “These minstrels, blest with every sign That marks a high and princely line, In holy shades who dwell, Enshrined in Saint Válmíki's lay, 60 A description of an A[vamedha or Horse Sacrifice is given in Canto XIII. of this Book.
- **Translation**: 

---

### Verse 13 (Ramayan 0.53)
- **Original**: Canto V. Ayodhyá. 35 A monument to live for aye, My deeds in song shall tell.” Thus Ráma spoke: their breasts were fired, And the great tale, as if inspired, The youths began to sing, While every heart with transport swelled, And mute and rapt attention held The concourse and the king. Canto V. Ayodhyá. “Ikshváku's sons from days of old Were ever brave and mighty-souled. The land their arms had made their own Was bounded by the sea alone. Their holy works have won them praise, Through countless years, from Manu's days. Their ancient sire was Sagar, he Whose high command dug out the sea:61 With sixty thousand sons to throng Around him as he marched along. From them this glorious tale proceeds: The great Rámáyan tells their deeds. This noble song whose lines contain Lessons of duty, love, and gain, We two will now at length recite, While good men listen with delight. 61 This exploit is related in Canto XL.
- **Translation**: 

---

### Verse 14 (Ramayan 0.54)
- **Original**: 36 The Ramayana On Sarjú's62 bank, of ample size, The happy realm of Ko[al lies,[012] With fertile length of fair champaign And flocks and herds and wealth of grain. There, famous in her old renown, Ayodhyá 63 stands, the royal town, In bygone ages built and planned By sainted Manu's64 princely hand. Imperial seat! her walls extend Twelve measured leagues from end to end, And three in width from side to side, With square and palace beautified. Her gates at even distance stand; Her ample roads are wisely planned. Right glorious is her royal street Where streams allay the dust and heat. On level ground in even row Her houses rise in goodly show: Terrace and palace, arch and gate The queenly city decorate. High are her ramparts, strong and vast, By ways at even distance passed, 62 The Sarjú or Ghaghra, anciently called Sarayú, rises in the Himalayas, and after flowing through the province of Oudh, falls into the Ganges. 63 The ruins of the ancient capital of Ráma and the Children of the Sun may still be traced in the present Ajudhyá near Fyzabad. Ajudhyá is the Jerusalem or Mecca of the Hindus. 64 A legislator and saint, the son of Brahmá or a personification of Brahmá himself, the creator of the world, and progenitor of mankind. Derived from the rootman to think, the word means originallyman , the thinker, and is found in this sense in the Rig-veda. Manu as a legislator is identified with the Cretan Minos, as progenitor of mankind with the German Mannus:“Celebrant carminibus antiquis, quod unum apud illos memoriæ et annalium genus est, Tuisconem deum terra editum, et filium Mannum, originem gentis conditoresque.” TACITUS {FNS ,Germania, Cap. II.
- **Translation**: 

---

### Verse 15 (Ramayan 0.55)
- **Original**: Canto V. Ayodhyá. 37 With circling moat, both deep and wide, And store of weapons fortified. King Da[aratha, lofty-souled, That city guarded and controlled, With towering Sál trees belted round,65 And many a grove and pleasure ground, As royal Indra, throned on high, Rules his fair city in the sky.66 She seems a painted city, fair With chess-board line and even square.67 And cool boughs shade the lovely lake Where weary men their thirst may slake. There gilded chariots gleam and shine, And stately piles the Gods enshrine. There gay sleek people ever throng To festival and dance and song. A mine is she of gems and sheen, The darling home of Fortune's Queen. With noblest sort of drink and meat, The fairest rice and golden wheat, And fragrant with the chaplet's scent With holy oil and incense blent. With many an elephant and steed, And wains for draught and cars for speed. With envoys sent by distant kings, And merchants with their precious things With banners o'er her roofs that play, 65 The Sál (Shorea Robusta) is a valuable timber tree of considerable height. 66 The city of Indra is called Amarávatí or Home of the Immortals. 67 Schlegel thinks that this refers to the marble of different colours with which the houses were adorned. It seems more natural to understand it as implying the regularity of the streets and houses.
- **Translation**: 

---

### Verse 16 (Ramayan 0.56)
- **Original**: 38 The Ramayana And weapons that a hundred slay;68 All warlike engines framed by man, And every class of artisan. A city rich beyond compare With bards and minstrels gathered there, And men and damsels who entrance The soul with play and song and dance. In every street is heard the lute, The drum, the tabret, and the flute, The Veda chanted soft and low, The ringing of the archer's bow; With bands of godlike heroes skilled In every warlike weapon, filled, And kept by warriors from the foe, As Nágas guard their home below.69 There wisest Bráhmans evermore The flame of worship feed, And versed in all the Vedas' lore, Their lives of virtue lead. Truthful and pure, they freely give; They keep each sense controlled, And in their holy fervour live Like the great saints of old. Canto VI. The King. 68 The Zataghní i.e. centicide, or slayer of a hundred, is generally supposed to be a sort of fire-arms, or the ancient Indian rocket; but it is also described as a stone set round with iron spikes. 69 The Nágas (serpents) are demigods with a human face and serpent body. They inhabit Pátála or the regions under the earth. Bhogavatí is the name of their capital city. Serpents are still worshipped in India. See Fergusson'sTree and Serpent Worship.
- **Translation**: 

---

### Verse 17 (Ramayan 0.57)
- **Original**: Canto VI. The King. 39 There reigned a king of name revered, To country and to town endeared, Great Da[aratha, good and sage, Well read in Scripture's holy page: [013] Upon his kingdom's weal intent, Mighty and brave and provident; The pride of old Ikshváku's seed For lofty thought and righteous deed. Peer of the saints, for virtues famed, For foes subdued and passions tamed: A rival in his wealth untold Of Indra and the Lord of Gold. Like Manu first of kings, he reigned, And worthily his state maintained. For firm and just and ever true Love, duty, gain he kept in view, And ruled his city rich and free, Like Indra's Amarávatí. And worthy of so fair a place There dwelt a just and happy race With troops of children blest. Each man contented sought no more, Nor longed with envy for the store By richer friends possessed. For poverty was there unknown, And each man counted as his own Kine, steeds, and gold, and grain. All dressed in raiment bright and clean, And every townsman might be seen With earrings, wreath, or chain. None deigned to feed on broken fare, And none was false or stingy there. A piece of gold, the smallest pay, Was earned by labour for a day.
- **Translation**: 

---

### Verse 18 (Ramayan 0.58)
- **Original**: 40 The Ramayana On every arm were bracelets worn, And none was faithless or forsworn, A braggart or unkind. None lived upon another's wealth, None pined with dread or broken health, Or dark disease of mind. High-souled were all. The slanderous word, The boastful lie, were never heard. Each man was constant to his vows, And lived devoted to his spouse. No other love his fancy knew, And she was tender, kind, and true. Her dames were fair of form and face, With charm of wit and gentle grace, With modest raiment simply neat, And winning manners soft and sweet. The twice-born sages, whose delight Was Scripture's page and holy rite, Their calm and settled course pursued, Nor sought the menial multitude. In many a Scripture each was versed, And each the flame of worship nursed, And gave with lavish hand. Each paid to Heaven the offerings due, And none was godless or untrue In all that holy band. To Bráhmans, as the laws ordain, The Warrior caste were ever fain The reverence due to pay; And these the Vai[yas' peaceful crowd, Who trade and toil for gain, were proud To honour and obey; And all were by theZúdras70 served, 70 The fourth and lowest pure caste whose duty was to serve the three first
- **Translation**: 

---

### Verse 19 (Ramayan 0.59)
- **Original**: Canto VI. The King. 41 Who never from their duty swerved, Their proper worship all addressed To Bráhman, spirits, God, and guest. Pure and unmixt their rites remained, Their race's honour ne'er was stained.71 Cheered by his grandsons, sons, and wife, Each passed a long and happy life. Thus was that famous city held By one who all his race excelled, Blest in his gentle reign, As the whole land aforetime swayed By Manu, prince of men, obeyed Her king from main to main. And heroes kept her, strong and brave, As lions guard their mountain cave: Fierce as devouring flame they burned, And fought till death, but never turned. Horses had she of noblest breed, Like Indra's for their form and speed, From Váhlí's72 hills and Sindhu's73 sand, classes. 71 By forbidden marriages between persons of different castes. 72 Váhlí or Váhlíka is Bactriana; its name is preserved in the modern Balkh. 73 The Sanskrit word Sindhu is in the singular the name of the river Indus, in the plural of the people and territories on its banks. The name appears asHidku in the cuneiform inscription of Darius' son of Hystaspes, in which the nations tributary to that king are enumerated. The Hebrew form isHodda (Esther, I. 1.). In Zend it appears asHendu in a somewhat wider sense. With the Persians later the signification ofHind seems to have co-extended with their increasing acquaintance with the country. The weak Ionic dialect omitted the Persianh, and we find in Hecatæus and Herodotus<½´¿Â and ! 8 ½´¹ºu. In this form the Romans received the names and transmitted them to us. The Arabian geographers in their ignorance that Hind and Sind are two forms of the same word have made of them two brothers and traced their decent from Noah. See Lassen's Indische Alterthumskunde Vol. I. pp. 2, 3.
- **Translation**: 

---

### Verse 20 (Ramayan 0.60)
- **Original**: 42 The Ramayana Vanáyu74 and Kámboja's land.75[014] Her noble elephants had strayed Through Vindhyan and Himálayan shade, Gigantic in their bulk and height, Yet gentle in their matchless might. They rivalled well the world-spread fame Of the great stock from which they came, Of Váman, vast of size, Of Mahápadma's glorious line, Thine, Anjan, and, Airávat, thine.76 Upholders of the skies. With those, enrolled in fourfold class, Who all their mighty kin surpass, Whom men Matangas name, And Mrigas spotted black and white, And Bhadras of unwearied might, And Mandras hard to tame.77 Thus, worthy of the name she bore,78 Ayodhyá for a league or more Cast a bright glory round, Where Da[aratha wise and great 74 The situation of Vanáyu is not exactly determined: it seems to have lain to the north-west of India. 75 Kámboja was probably still further to the north-west. Lassen thinks that the name is etymologically connected withCambyses which in the cuneiform inscription of Behistun is written Ka(m)bujia. 76 The elephants of Indra and other deities who preside over the four points of the compass. 77 “There are four kinds of elephants. 1Bhaddar. It is well proportioned, has an erect head, a broad chest, large ears, a long tail, and is bold and can bear fatigue. 2Mand . It is black, has yellow eyes, a uniformly sized body, and is wild and ungovernable. 3Mirg. It has a whitish skin, with black spots. 4Mir. It has a small head, and obeys readily. It gets frightened when it thunders.” Aín-i-Akbarí.. Translated by H. Blochmann, Aín 41,The Imperial Elephant Stables. 78 Ayodhyá means not to be fought against.
- **Translation**: 

---

