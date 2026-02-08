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

### Verse 1 (Ramayana 0.566)
- **Original**: 548 The Ramayana So on the ground with leaves o'erspread, He who should press a royal bed, Ráma with LakshmaG thus conversed, And many a pleasant tale rehearsed: “This night the king,” he cried,“alas! In broken sleep will sadly pass. Kaikeyí now content should be, For mistress of her wish is she. So fiercely she for empire yearns, That when her Bharat home returns, She in her greed, may even bring Destruction on our lord the king. What can he do, in feeble eld, Reft of all aid and me expelled, His soul enslaved by love, a thrall Obedient to Kaikeyí's call? As thus I muse upon his woe And all his wisdoms overthrow, Love is, methinks, of greater might To stir the heart than gain and right. For who, in wisdom's lore untaught, Could by a beauty's prayer be bought To quit his own obedient son, Who loves him, as my sire has done! Bharat, Kaikeyí's child, alone Will, with his wife, enjoy the throne, And blissfully his rule maintain O'er happy Ko[ala's domain. To Bharat's single lot will fall The kingdom and the power and all, When fails the king from length of days, And Ráma in the forest strays. Whoe'er, neglecting right and gain, Lets conquering love his soul enchain,
- **Translation**: 

---

### Verse 2 (Ramayana 0.567)
- **Original**: Canto LIII. Ráma's Lament. 549 To him, like Da[aratha's lot, Comes woe with feet that tarry not. Methinks at last the royal dame, Dear LakshmaG, has secured her aim, To see at once her husband dead, Her son enthroned, and Ráma fled. Ah me! I fear, lest borne away By frenzy of success, she slay Kau [alyá, through her wicked hate Of me, bereft, disconsolate; Or her who aye for me has striven Sumitrá, to devotion given. Hence, LakshmaG, to Ayodhyá speed, Returning in the hour of need. With Sítá I my steps will bend Where DaG ak's mighty woods extend. No guardian has Kau[alyá now: O, be her friend and guardian thou. Strong hate may vile Kaikeyí lead To many a base unrighteous deed, Treading my mother 'neath her feet When Bharat holds the royal seat. Sure in some antenatal time Were children, by Kau[alyá's crime, Torn from their mothers' arms away, And hence she mourns this evil day. She for her child no toil would spare Tending me long with pain and care; Now in the hour of fruitage she Has lost that son, ah, woe is me. O Lakshma G, may no matron e'er A son so doomed to sorrow bear As I, my mother's heart who rend With anguish that can never end.
- **Translation**: 

---

### Verse 3 (Ramayana 0.568)
- **Original**: 550 The Ramayana The Sáriká,325 methinks, possessed More love than glows in Ráma's breast. Who, as the tale is told to us, Addressed the stricken parrot thus:[158] “Parrot, the capturer's talons tear, While yet alone thou flutterest there, Before his mouth has closed on me:” So cried the bird, herself to free. Reft of her son, in childless woe, My mother's tears for ever flow: Ill-fated, doomed with grief to strive, What aid can she from me derive? Pressed down by care, she cannot rise From sorrow's flood wherein she lies. In righteous wrath my single arm Could, with my bow, protect from harm Ayodhyá's town and all the earth: But what is hero prowess worth? Lest breaking duty's law I sin, And lose the heaven I strive to win, The forest life today I choose, And kingly state and power refuse.” Thus mourning in that lonely spot The troubled chief bewailed his lot, And filled with tears, his eyes ran o'er; Then silent sat, and spake no more. To him, when ceased his loud lament, Like fire whose brilliant might is spent, Or the great sea when sleeps the wave, Thus LakshmaG consolation gave: “Chief of the brave who bear the bow, E'en now Ayodhyá, sunk in woe, 325 The Mainá or Gracula religiosa, a favourite cage-bird, easily taught to talk.
- **Translation**: 

---

### Verse 4 (Ramayana 0.569)
- **Original**: Canto LIV. Bharadvája's Hermitage. 551 By thy departure reft of light Is gloomy as the moonless night. Unfit it seems that thou, O chief, Shouldst so afflict thy soul with grief, So with thou Sítá's heart consign To deep despair as well as mine. Not I, O Raghu's son, nor she Could live one hour deprived of thee: We were, without thine arm to save, Like fish deserted by the wave. Although my mother dear to meet, Zatrughna, and the king, were sweet, On them, or heaven, to feed mine eye Were nothing, if thou wert not by.” Sitting at ease, their glances fell Upon the beds, constructed well, And there the sons of virtue laid Their limbs beneath the fig tree's shade. Canto LIV. Bharadvája's Hermitage. So there that night the heroes spent Under the boughs that o'er them bent, And when the sun his glory spread, Upstarting, from the place they sped. On to that spot they made their way, Through the dense wood that round them lay, Where Yamuná's326 swift waters glide To blend with Gangá's holy tide. 326 The Jumna.
- **Translation**: 

---

### Verse 5 (Ramayana 0.570)
- **Original**: 552 The Ramayana Charmed with the prospect ever new The glorious heroes wandered through Full many a spot of pleasant ground, Rejoicing as they gazed around, With eager eye and heart at ease, On countless sorts of flowery trees. And now the day was half-way sped When thus to LakshmaG Ráma said: “There, there, dear brother, turn thine eyes; See near Prayág327 that smoke arise: The banner of our Lord of Flames The dwelling of some saint proclaims. Near to the place our steps we bend Where Yamuná and Gangá blend. I hear and mark the deafening roar When chafing floods together pour. See, near us on the ground are left Dry logs, by labouring woodmen cleft, And the tall trees, that blossom near Saint Bharadvája's home, appear.” The bow-armed princes onward passed, And as the sun was sinking fast They reached the hermit's dwelling, set Near where the rushing waters met. The presence of the warrior scared The deer and birds as on he fared, And struck them with unwonted awe: Then Bharadvája's cot they saw. The high-souled hermit soon they found Girt by his dear disciples round: Calm saint, whose vows had well been wrought, Whose fervent rites keen sight had bought. 327 The Hindu name of Allahabad.
- **Translation**: 

---

### Verse 6 (Ramayana 0.571)
- **Original**: Canto LIV. Bharadvája's Hermitage. 553 Duly had flames of worship blazed When Ráma on the hermit gazed: His suppliant hands the hero raised, Drew nearer to the holy man With his companions, and began, Declaring both his name and race And why they sought that distant place: “Saint, Da[aratha's children we, Ráma and LakshmaG, come to thee. This my good wife from Janak springs, The best of fair Videha's kings; Through lonely wilds, a faultless dame, To this pure grove with me she came. My younger brother follows still Me banished by my father's will: Sumitrá's son, bound by a vow,— He roams the wood beside me now. Sent by my father forth to rove, We seek, O Saint, some holy grove, Where lives of hermits we may lead, And upon fruits and berries feed.” When Bharadvája, prudent-souled, Had heard the prince his tale unfold, Water he bade them bring, a bull, And honour-gifts in dishes full, [159] And drink and food of varied taste, Berries and roots, before him placed, And then the great ascetic showed A cottage for the guests' abode. The saint these honours gladly paid To Ráma who had thither strayed, Then compassed sat by birds and deer And many a hermit resting near.
- **Translation**: 

---

### Verse 7 (Ramayana 0.572)
- **Original**: 554 The Ramayana The prince received the service kind, And sat him down rejoiced in mind. Then Bharadvája silence broke, And thus the words of duty spoke: “Kakutstha's royal son, that thou Hadst sought this grove I knew ere now. Mine ears have heard thy story, sent Without a sin to banishment. Behold, O Prince, this ample space Near where the mingling floods embrace, Holy, and beautiful, and clear: Dwell with us, and be happy here.” By Bharadvája thus addressed, Ráma whose kind and tender breast All living things would bless and save, In gracious words his answer gave: “My honoured lord, this tranquil spot, Fair home of hermits, suits me not: For all the neighbouring people here Will seek us when they know me near: With eager wish to look on me, And the Videhan dame to see, A crowd of rustics will intrude Upon the holy solitude. Provide, O gracious lord, I pray, Some quiet home that lies away, Where my Videhan spouse may dwell Tasting the bliss deserved so well.”
- **Translation**: 

---

### Verse 8 (Ramayana 0.573)
- **Original**: Canto LIV. Bharadvája's Hermitage. 555 The hermit heard the prayer he made: A while in earnest thought he stayed, And then in words like these expressed His answer to the chief's request: “Ten leagues away there stands a hill Where thou mayst live, if such thy will: A holy mount, exceeding fair; Great saints have made their dwelling there: There great Langúrs328 in thousands play, And bears amid the thickets stray; Wide-known by Chitrakúma's name, It rivals Gandhamádan's329 fame. Long as the man that hill who seeks Gazes upon its sacred peaks, To holy things his soul he gives And pure from thought of evil lives. There, while a hundred autumns fled, Has many a saint with hoary head Spent his pure life, and won the prize, By deep devotion, in the skies: Best home, I ween, if such retreat, Far from the ways of men, be sweet: Or let thy years of exile flee Here in this hermitage with me.” Thus Bharadvája spake, and trained In lore of duty, entertained The princes and the dame, and pressed His friendly gifts on every guest. 328 The Langúr is a large monkey. 329 A mountain said to lie to the east of Meru.
- **Translation**: 

---

### Verse 9 (Ramayana 0.574)
- **Original**: 556 The Ramayana Thus to Prayág the hero went, Thus saw the saint preëminent, And varied speeches heard and said: Then holy night o'er heaven was spread. And Ráma took, by toil oppressed, With Sítá and his brother, rest; And so the night, with sweet content, In Bharadvája's grove was spent. But when the dawn dispelled the night, Ráma approached the anchorite, And thus addressed the holy sire Whose glory shone like kindled fire: “Well have we spent, O truthful Sage, The night within thy hermitage: Now let my lord his guests permit For their new home his grove to quit.” Then, as he saw the morning break, In answer Bharadvája spake: “Go forth to Chitrakúma's hill, Where berries grow, and sweets distil: Full well, I deem, that home will suit Thee, Ráma, strong and resolute. Go forth, and Chitrakúma seek, Famed mountain of the Varied Peak. In the wild woods that gird him round All creatures of the chase are found: Thou in the glades shalt see appear Vast herds of elephants and deer. With Sítá there shalt thou delight To gaze upon the woody height; There with expanding heart to look On river, table-land, and brook, And see the foaming torrent rave
- **Translation**: 

---

### Verse 10 (Ramayana 0.575)
- **Original**: Canto LV. The Passage Of Yamuná. 557 Impetuous from the mountain cave. Auspicious hill! where all day long The lapwing's cry, the Koïl's song Make all who listen gay: Where all is fresh and fair to see, Where elephants and deer roam free, There, as a hermit, stay.” Canto LV. The Passage Of Yamuná. The princely tamers of their foes Thus passed the night in calm repose, Then to the hermit having bent With reverence, on their way they went. High favour Bharadvája showed, And blessed them ready for the road. [160] With such fond looks as fathers throw On their own sons, before they go. Then spake the saint with glory bright To Ráma peerless in his might: “First, lords of men, direct your feet Where Yamuná and Gangá meet; Then to the swift Kálindí330 go, Whose westward waves to Gangá flow. When thou shalt see her lovely shore Worn by their feet who hasten o'er, Then, Raghu's son, a raft prepare, And cross the Sun born river there. Upon her farther bank a tree, 330 Another name of the Jumna, daughter of the Sun.
- **Translation**: 

---

### Verse 11 (Ramayana 0.576)
- **Original**: 558 The Ramayana Near to the landing wilt thou see. The blessed source of varied gifts, There her green boughs that Fig-tree lifts: A tree where countless birds abide, By Zyáma's name known far and wide. Sítá, revere that holy shade: There be thy prayers for blessing prayed. Thence for a league your way pursue, And a dark wood shall meet your view, Where tall bamboos their foliage show, The Gum-tree and the Jujube grow. To Chitrakúma have I oft Trodden that path so smooth and soft, Where burning woods no traveller scare, But all is pleasant, green, and fair.” When thus the guests their road had learned, Back to his cot the hermit turned, And Ráma, LakshmaG, Sítá paid Their reverent thanks for courteous aid. Thus Ráma spake to LakshmaG, when The saint had left the lords of men: “Great store of bliss in sooth is ours On whom his love the hermit showers.” As each to other wisely talked, The lion lords together walked On to Kálindí's woody shore; And gentle Sítá went before. They reached that flood, whose waters flee With rapid current to the sea; Their minds a while to thought they gave And counselled how to cross the wave. At length, with logs together laid, A mighty raft the brothers made.
- **Translation**: 

---

### Verse 12 (Ramayana 0.577)
- **Original**: Canto LV. The Passage Of Yamuná. 559 Then dry bamboos across were tied, And grass was spread from side to side. And the great hero LakshmaG brought Cane and Rose-Apple boughs and wrought, Trimming the branches smooth and neat, For Sítá's use a pleasant seat. And Ráma placed thereon his dame Touched with a momentary shame, Resembling in her glorious mien All-thought-surpassing Fortune's Queen. Then Ráma hastened to dispose, Each in its place, the skins and bows, And by the fair Videhan laid The coats, the ornaments, and spade. When Sítá thus was set on board, And all their gear was duly stored, The heroes each with vigorous hand, Pushed off the raft and left the land. When half its way the raft had made, Thus Sítá to Kálindí prayed: “Goddess, whose flood I traverse now, Grant that my lord may keep his vow. For thee shall bleed a thousand kine, A hundred jars shall pour their wine, When Ráma sees that town again Where old Ikshváku's children reign.” Thus to Kálindí's stream she sued And prayed in suppliant attitude. Then to the river's bank the dame, Fervent in supplication, came. They left the raft that brought them o'er, And the thick wood that clothed the shore, And to the Fig-treeZyáma made
- **Translation**: 

---

### Verse 13 (Ramayana 0.578)
- **Original**: 560 The Ramayana Their way, so cool with verdant shade. Then Sítá viewed that best of trees, And reverent spake in words like these: “Hail, hail, O mighty tree! Allow My husband to complete his vow; Let us returning, I entreat, Kau [alyá and Sumitrá meet.” Then with her hands together placed Around the tree she duly paced. When Ráma saw his blameless spouse A suppliant under holy boughs, The gentle darling of his heart, He thus to LakshmaG spake apart: “Brother, by thee our way be led; Let Sítá close behind thee tread: I, best of men, will grasp my bow, And hindmost of the three will go. What fruits soe'er her fancy take, Or flowers half hidden in the brake, For Janak's child forget not thou To gather from the brake or bough.” Thus on they fared. The tender dame Asked Ráma, as they walked, the name Of every shrub that blossoms bore, Creeper, and tree unseen before: And Lakshma G fetched, at Sítá's prayer, Boughs of each tree with clusters fair. Then Janak's daughter joyed to see The sand-discoloured river flee, Where the glad cry of many a bird, The sáras and the swan, was heard. A league the brothers travelled through The forest noble game they slew:
- **Translation**: 

---

### Verse 14 (Ramayana 0.579)
- **Original**: Canto LVI. Chitrakúta 561 Beneath the trees their meal they dressed And sat them down to eat and rest. A while in that delightful shade Where elephants unnumbered strayed, Where peacocks screamed and monkeys played, [161] They wandered with delight. Then by the river's side they found A pleasant spot of level ground, Where all was smooth and fair around, Their lodging for the night. Canto LVI. Chitrakúta Then Ráma, when the morning rose, Called LakshmaG gently from repose: “Awake, the pleasant voices hear Of forest birds that warble near. Scourge of thy foes, no longer stay; The hour is come to speed away.”
- **Translation**: 

---

### Verse 15 (Ramayana 0.580)
- **Original**: 562 The Ramayana The slumbering prince unclosed his eyes When thus his brother bade him rise, Compelling, at the timely cry, Fatigue, and sleep, and rest to fly. The brothers rose and Sítá too; Pure water from the stream they drew, Paid morning rites, then followed still The road to Chitrakúma's hill. Then Ráma as he took the road With LakshmaG, while the morning, glowed, To the Videhan lady cried, Sítá the fair, the lotus-eyed: “Look round thee, dear; each flowery tree Touched with the fire of morning see: The Kin[uk, now the Frosts are fled,— How glorious with his wreaths of red! The Bel-trees see, so loved of men, Hanging their boughs in every glen. O'erburthened with their fruit and flowers: A plenteous store of food is ours. See, LakshmaG, in the leafy trees, Where'er they make their home. Down hangs, the work of labouring bees The ponderous honeycomb. In the fair wood before us spread The startled wild-cock cries: Hark, where the flowers are soft to tread, The peacock's voice replies. Where elephants are roaming free, And sweet birds' songs are loud, The glorious Chitrakúma see: His peaks are in the cloud. On fair smooth ground he stands displayed, Begirt by many a tree:
- **Translation**: 

---

### Verse 16 (Ramayana 0.581)
- **Original**: Canto LVI. Chitrakúta 563 O brother, in that holy shade How happy shall we be!”331 Then Ráma, LakshmaG, Sítá, each Spoke raising suppliant hands this speech To him, in woodland dwelling met, Válmíki, ancient anchoret: “O Saint, this mountain takes the mind, With creepers, trees of every kind, With fruit and roots abounding thus, A pleasant life it offers us: Here for a while we fain would stay, And pass a season blithe and gay.” Then the great saint, in duty trained, With honour gladly entertained: He gave his guests a welcome fair, And bade them sit and rest them there, Ráma of mighty arm and chest His faithful LakshmaG then addressed: “Brother, bring hither from the wood Selected timber strong and good, And build therewith a little cot; My heart rejoices in the spot That lies beneath the mountain's side, Remote, with water well supplied.” 331 “We have often looked on that green hill: it is the holiest spot of that sect of the Hindu faith who devote themselves to this incarnation of VishGu. The whole neighbourhood is Ráma's country. Every headland has some legend, every cavern is connected with his name; some of the wild fruits are still calledSítáphal, being the reputed food of the exile. Thousands and thousands annually visit the spot, and round the hill is a raised foot-path, on which the devotee, with naked feet, treads full of pious awe.” Calcutta Review, Vol. XXIII.
- **Translation**: 

---

### Verse 17 (Ramayana 0.582)
- **Original**: 564 The Ramayana Sumitrá's son his words obeyed, Brought many a tree, and deftly made, With branches in the forest cut, As Ráma bade, a leafy hut. Then Ráma, when the cottage stood Fair, firmly built, and walled with wood, To LakshmaG spake, whose eager mind To do his brother's will inclined: “Now, LakshmaG as our cot is made, Must sacrifice be duly paid By us, for lengthened life who hope, With venison of the antelope. Away, O bright-eyed LakshmaG, speed: Struck by thy bow a deer must bleed: As Scripture bids, we must not slight The duty that commands the rite.” Lakshma G, the chief whose arrows laid His foemen low, his word obeyed; And Ráma thus again addressed The swift performer of his hest: “Prepare the venison thou hast shot, To sacrifice for this our cot. Haste, brother dear, for this the hour, And this the day of certain power.” Then glorious LakshmaG took the buck His arrow in the wood had struck; Bearing his mighty load he came, And laid it in the kindled flame.[162] Soon as he saw the meat was done, And that the juices ceased to run From the broiled carcass, LakshmaG then Spoke thus to Ráma best of men: “The carcass of the buck, entire,
- **Translation**: 

---

### Verse 18 (Ramayana 0.583)
- **Original**: Canto LVI. Chitrakúta 565 Is ready dressed upon the fire. Now be the sacred rites begun To please the God, thou godlike one.” Ráma the good, in ritual trained, Pure from the bath, with thoughts restrained, Hasted those verses to repeat Which make the sacrifice complete. The hosts celestial came in view, And Ráma to the cot withdrew, While a sweet sense of rapture stole Through the unequalled hero's soul. He paid the Vi[vedevas332 due. And Rudra's right, and VishGu's too, Nor wonted blessings, to protect Their new-built home, did he neglect. With voice repressed he breathed the prayer, Bathed duly in the river fair, And gave good offerings that remove The stain of sin, as texts approve. And many an altar there he made, And shrines, to suit the holy shade, All decked with woodland chaplets sweet, And fruit and roots and roasted meat, With muttered prayer, as texts require, Water, and grass and wood and fire. So Ráma, LakshmaG, Sítá paid Their offerings to each God and shade, And entered then their pleasant cot That bore fair signs of happy lot. They entered, the illustrious three, 332 Deities of a particular class in which five or ten are enumerated. They are worshipped particularly at the funeral obsequies in honour of deceased progenitors.
- **Translation**: 

---

### Verse 19 (Ramayana 0.584)
- **Original**: 566 The Ramayana The well-set cottage, fair to see, Roofed with the leaves of many a tree, And fenced from wind and rain: So, at their Father Brahmá's call, The Gods of heaven, assembling all, To their own glorious council hall Advance in shining train. So, resting on that lovely hill, Near the fair lily-covered rill, The happy prince forgot, Surrounded by the birds and deer, The woe, the longing, and the fear That gloom the exile's lot. Canto LVII. Sumantra's Return. When Ráma reached the southern bank, King Guha's heart with sorrow sank: He with Sumantra talked, and spent With his deep sorrow, homeward went. Sumantra, as the king decreed, Yoked to the car each noble steed, And to Ayodhyá's city sped With his sad heart disquieted. On lake and brook and scented grove His glances fell, as on he drove: City and village came in view As o'er the road his coursers flew. On the third day the charioteer, When now the hour of night was near, Came to Ayodhyá's gate, and found
- **Translation**: 

---

### Verse 20 (Ramayana 0.585)
- **Original**: Canto LVII. Sumantra's Return. 567 The city all in sorrow drowned. To him, in spirit quite cast down, Forsaken seemed the silent town, And by the rush of grief oppressed He pondered in his mournful breast: “Is all Ayodhyá burnt with grief, Steed, elephant, and man, and chief? Does her loved Ráma's exile so Afflict her with the fires of woe?” Thus as he mused, his steeds flew fast, And swiftly through the gate he passed. On drove the charioteer, and then In hundreds, yea in thousands, men Ran to the car from every side, And, “Ráma, where is Ráma?” cried. Sumantra said:“My chariot bore The duteous prince to Gangá's shore; I left him there at his behest, And homeward to Ayodhyá pressed.” Soon as the anxious people knew That he was o'er the flood they drew Deep sighs, and crying, Ráma! all Wailed, and big tears began to fall. He heard the mournful words prolonged, As here and there the people thronged: “Woe, woe for us, forlorn, undone, No more to look on Raghu's son! His like again we ne'er shall see, Of heart so true, of hand so free, In gifts, in gatherings for debate, When marriage pomps we celebrate, What should we do? What earthly thing Can rest, or hope, or pleasure bring?”
- **Translation**: 

---

