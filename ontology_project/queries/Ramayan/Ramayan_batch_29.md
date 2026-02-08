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

### Verse 1 (Ramayan 0.561)
- **Original**: Canto LII. The Crossing Of Gangá. 543 Ikshváku's son, the good and brave, This last farewell to Guha gave, And then, with LakshmaG and his bride, Determined, on his way he hied. Soon as he viewed, upon the shore, The bark prepared to waft them o'er Impetuous Gangá's rolling tide, To LakshmaG thus the chieftain cried: “Brother, embark; thy hand extend, Thy gentle aid to Sítá lend: With care her trembling footsteps guide, And place the lady by thy side.” When Lakshma G heard, prepared to aid, His brother's words he swift obeyed. Within the bark he placed the dame, Then to her side the hero came. Next LakshmaG's elder brother, lord Of brightest glory, when on board, Breathing a prayer for blessings, meet For priest or warrior to repeat, Then he and car-borne LakshmaG bent, Well-pleased, their heads, most reverent, Their hands, with Sítá, having dipped, As Scripture bids, and water sipped, Farewell to wise Sumantra said, And Guha, with the train he led. So Ráma took, on board, his stand, And urged the vessel from the land. Then swift by vigorous arms impelled Her onward course the vessel held, And guided by the helmsman through The dashing waves of Gangá flew. Half way across the flood they came, When Sítá, free from spot and blame,
- **Translation**: 

---

### Verse 2 (Ramayan 0.562)
- **Original**: 544 The Ramayana Her reverent hands together pressed, The Goddess of the stream addressed: “May the great chieftain here who springs From Da[aratha, best of kings, Protected by thy care, fulfil His prudent father's royal will. When in the forest he has spent His fourteen years of banishment, With his dear brother and with me His home again my lord shall see. Returning on that blissful day, I will to thee mine offerings pay, Dear Queen, whose waters gently flow, Who canst all blessed gifts bestow. For, three-pathed Queen, though wandering here, Thy waves descend from Brahmá's sphere, Spouse of the God o'er floods supreme, Though rolling here thy glorious stream. To thee, fair Queen, my head shall bend, To thee shall hymns of praise ascend, When my brave lord shall turn again, And, joyful, o'er his kingdom reign. To win thy grace, O Queen divine, A hundred thousand fairest kine, And precious robes and finest meal Among the Bráhmans will I deal. A hundred jars of wine shall flow, When to my home, O Queen, I go; With these, and flesh, and corn, and rice, Will I, delighted, sacrifice. Each hallowed spot, each holy shrine That stands on these fair shores of thine, Each fane and altar on thy banks Shall share my offerings and thanks.
- **Translation**: 

---

### Verse 3 (Ramayan 0.563)
- **Original**: Canto LII. The Crossing Of Gangá. 545 With me and LakshmaG, free from harm, May he the blameless, strong of arm, Reseek Ayodhyá from the wild, O blameless Lady undefiled!” As, praying for her husband's sake, The faultless dame to Gangá spake, To the right bank the vessel flew With her whose heart was right and true. Soon as the bark had crossed the wave, The lion leader of the brave, Leaving the vessel on the strand, With wife and brother leapt to land. Then Ráma thus the prince addressed Who filled with joy Sumitrá's breast: “Be thine alike to guard and aid In peopled spot, in lonely shade. Do thou, Sumitrá's son, precede: Let Sítá walk where thou shalt lead. Behind you both my place shall be, To guard the Maithil dame and thee. For she, to woe a stranger yet, No toil or grief till now has met; The fair Videhan will assay The pains of forest life to-day. To-day her tender feet must tread Rough rocky wilds around her spread: No tilth is there, no gardens grow, No crowding people come and go.”
- **Translation**: 

---

### Verse 4 (Ramayan 0.564)
- **Original**: 546 The Ramayana The hero ceased: and LakshmaG led Obedient to the words he said: And Sítá followed him, and then Came Raghu's pride, the lord of men. With Sítá walking o'er the sand They sought the forest, bow in hand, But still their lingering glances threw Where yet Sumantra stood in view. Sumantra, when his watchful eye The royal youths no more could spy, Turned from the spot whereon he stood Homeward with Guha from the wood.[157] Still on the brothers forced their way Where sweet birds sang on every spray, Though scarce the eye a path could find Mid flowering trees where creepers twined. Far on the princely brothers pressed, And stayed their feet at length to rest Beneath a fig tree's mighty shade With countless pendent shoots displayed. Reclining there a while at ease, They saw, not far, beneath fair trees A lake with many a lotus bright That bore the name of Lovely Sight. Ráma his wife's attention drew, And Lakshma G's, to the charming view: “Look, brother, look how fair the flood Glows with the lotus, flower and bud!” They drank the water fresh and clear, And with their shafts they slew a deer. A fire of boughs they made in haste, And in the flame the meat they placed. So Raghu's sons with Sítá shared
- **Translation**: 

---

### Verse 5 (Ramayan 0.565)
- **Original**: Canto LIII. Ráma's Lament. 547 The hunter's meal their hands prepared, Then counselled that the spreading tree Their shelter and their home should be. Canto LIII. Ráma's Lament. When evening rites were duly paid, Reclined beneath the leafy shade, To LakshmaG thus spake Ráma, best Of those who glad a people's breast: “Now the first night has closed the day That saw us from our country stray, And parted from the charioteer; Yet grieve not thou, my brother dear. Henceforth by night, when others sleep, Must we our careful vigil keep, Watching for Sítá's welfare thus, For her dear life depends on us. Bring me the leaves that lie around, And spread them here upon the ground, That we on lowly beds may lie, And let in talk the night go by.”
- **Translation**: 

---

### Verse 6 (Ramayan 0.566)
- **Original**: 548 The Ramayana So on the ground with leaves o'erspread, He who should press a royal bed, Ráma with LakshmaG thus conversed, And many a pleasant tale rehearsed: “This night the king,” he cried,“alas! In broken sleep will sadly pass. Kaikeyí now content should be, For mistress of her wish is she. So fiercely she for empire yearns, That when her Bharat home returns, She in her greed, may even bring Destruction on our lord the king. What can he do, in feeble eld, Reft of all aid and me expelled, His soul enslaved by love, a thrall Obedient to Kaikeyí's call? As thus I muse upon his woe And all his wisdoms overthrow, Love is, methinks, of greater might To stir the heart than gain and right. For who, in wisdom's lore untaught, Could by a beauty's prayer be bought To quit his own obedient son, Who loves him, as my sire has done! Bharat, Kaikeyí's child, alone Will, with his wife, enjoy the throne, And blissfully his rule maintain O'er happy Ko[ala's domain. To Bharat's single lot will fall The kingdom and the power and all, When fails the king from length of days, And Ráma in the forest strays. Whoe'er, neglecting right and gain, Lets conquering love his soul enchain,
- **Translation**: 

---

### Verse 7 (Ramayan 0.567)
- **Original**: Canto LIII. Ráma's Lament. 549 To him, like Da[aratha's lot, Comes woe with feet that tarry not. Methinks at last the royal dame, Dear LakshmaG, has secured her aim, To see at once her husband dead, Her son enthroned, and Ráma fled. Ah me! I fear, lest borne away By frenzy of success, she slay Kau [alyá, through her wicked hate Of me, bereft, disconsolate; Or her who aye for me has striven Sumitrá, to devotion given. Hence, LakshmaG, to Ayodhyá speed, Returning in the hour of need. With Sítá I my steps will bend Where DaG ak's mighty woods extend. No guardian has Kau[alyá now: O, be her friend and guardian thou. Strong hate may vile Kaikeyí lead To many a base unrighteous deed, Treading my mother 'neath her feet When Bharat holds the royal seat. Sure in some antenatal time Were children, by Kau[alyá's crime, Torn from their mothers' arms away, And hence she mourns this evil day. She for her child no toil would spare Tending me long with pain and care; Now in the hour of fruitage she Has lost that son, ah, woe is me. O Lakshma G, may no matron e'er A son so doomed to sorrow bear As I, my mother's heart who rend With anguish that can never end.
- **Translation**: 

---

### Verse 8 (Ramayan 0.568)
- **Original**: 550 The Ramayana The Sáriká,325 methinks, possessed More love than glows in Ráma's breast. Who, as the tale is told to us, Addressed the stricken parrot thus:[158] “Parrot, the capturer's talons tear, While yet alone thou flutterest there, Before his mouth has closed on me:” So cried the bird, herself to free. Reft of her son, in childless woe, My mother's tears for ever flow: Ill-fated, doomed with grief to strive, What aid can she from me derive? Pressed down by care, she cannot rise From sorrow's flood wherein she lies. In righteous wrath my single arm Could, with my bow, protect from harm Ayodhyá's town and all the earth: But what is hero prowess worth? Lest breaking duty's law I sin, And lose the heaven I strive to win, The forest life today I choose, And kingly state and power refuse.” Thus mourning in that lonely spot The troubled chief bewailed his lot, And filled with tears, his eyes ran o'er; Then silent sat, and spake no more. To him, when ceased his loud lament, Like fire whose brilliant might is spent, Or the great sea when sleeps the wave, Thus LakshmaG consolation gave: “Chief of the brave who bear the bow, E'en now Ayodhyá, sunk in woe, 325 The Mainá or Gracula religiosa, a favourite cage-bird, easily taught to talk.
- **Translation**: 

---

### Verse 9 (Ramayan 0.569)
- **Original**: Canto LIV. Bharadvája's Hermitage. 551 By thy departure reft of light Is gloomy as the moonless night. Unfit it seems that thou, O chief, Shouldst so afflict thy soul with grief, So with thou Sítá's heart consign To deep despair as well as mine. Not I, O Raghu's son, nor she Could live one hour deprived of thee: We were, without thine arm to save, Like fish deserted by the wave. Although my mother dear to meet, Zatrughna, and the king, were sweet, On them, or heaven, to feed mine eye Were nothing, if thou wert not by.” Sitting at ease, their glances fell Upon the beds, constructed well, And there the sons of virtue laid Their limbs beneath the fig tree's shade. Canto LIV. Bharadvája's Hermitage. So there that night the heroes spent Under the boughs that o'er them bent, And when the sun his glory spread, Upstarting, from the place they sped. On to that spot they made their way, Through the dense wood that round them lay, Where Yamuná's326 swift waters glide To blend with Gangá's holy tide. 326 The Jumna.
- **Translation**: 

---

### Verse 10 (Ramayan 0.570)
- **Original**: 552 The Ramayana Charmed with the prospect ever new The glorious heroes wandered through Full many a spot of pleasant ground, Rejoicing as they gazed around, With eager eye and heart at ease, On countless sorts of flowery trees. And now the day was half-way sped When thus to LakshmaG Ráma said: “There, there, dear brother, turn thine eyes; See near Prayág327 that smoke arise: The banner of our Lord of Flames The dwelling of some saint proclaims. Near to the place our steps we bend Where Yamuná and Gangá blend. I hear and mark the deafening roar When chafing floods together pour. See, near us on the ground are left Dry logs, by labouring woodmen cleft, And the tall trees, that blossom near Saint Bharadvája's home, appear.” The bow-armed princes onward passed, And as the sun was sinking fast They reached the hermit's dwelling, set Near where the rushing waters met. The presence of the warrior scared The deer and birds as on he fared, And struck them with unwonted awe: Then Bharadvája's cot they saw. The high-souled hermit soon they found Girt by his dear disciples round: Calm saint, whose vows had well been wrought, Whose fervent rites keen sight had bought. 327 The Hindu name of Allahabad.
- **Translation**: 

---

### Verse 11 (Ramayan 0.571)
- **Original**: Canto LIV. Bharadvája's Hermitage. 553 Duly had flames of worship blazed When Ráma on the hermit gazed: His suppliant hands the hero raised, Drew nearer to the holy man With his companions, and began, Declaring both his name and race And why they sought that distant place: “Saint, Da[aratha's children we, Ráma and LakshmaG, come to thee. This my good wife from Janak springs, The best of fair Videha's kings; Through lonely wilds, a faultless dame, To this pure grove with me she came. My younger brother follows still Me banished by my father's will: Sumitrá's son, bound by a vow,— He roams the wood beside me now. Sent by my father forth to rove, We seek, O Saint, some holy grove, Where lives of hermits we may lead, And upon fruits and berries feed.” When Bharadvája, prudent-souled, Had heard the prince his tale unfold, Water he bade them bring, a bull, And honour-gifts in dishes full, [159] And drink and food of varied taste, Berries and roots, before him placed, And then the great ascetic showed A cottage for the guests' abode. The saint these honours gladly paid To Ráma who had thither strayed, Then compassed sat by birds and deer And many a hermit resting near.
- **Translation**: 

---

### Verse 12 (Ramayan 0.572)
- **Original**: 554 The Ramayana The prince received the service kind, And sat him down rejoiced in mind. Then Bharadvája silence broke, And thus the words of duty spoke: “Kakutstha's royal son, that thou Hadst sought this grove I knew ere now. Mine ears have heard thy story, sent Without a sin to banishment. Behold, O Prince, this ample space Near where the mingling floods embrace, Holy, and beautiful, and clear: Dwell with us, and be happy here.” By Bharadvája thus addressed, Ráma whose kind and tender breast All living things would bless and save, In gracious words his answer gave: “My honoured lord, this tranquil spot, Fair home of hermits, suits me not: For all the neighbouring people here Will seek us when they know me near: With eager wish to look on me, And the Videhan dame to see, A crowd of rustics will intrude Upon the holy solitude. Provide, O gracious lord, I pray, Some quiet home that lies away, Where my Videhan spouse may dwell Tasting the bliss deserved so well.”
- **Translation**: 

---

### Verse 13 (Ramayan 0.573)
- **Original**: Canto LIV. Bharadvája's Hermitage. 555 The hermit heard the prayer he made: A while in earnest thought he stayed, And then in words like these expressed His answer to the chief's request: “Ten leagues away there stands a hill Where thou mayst live, if such thy will: A holy mount, exceeding fair; Great saints have made their dwelling there: There great Langúrs328 in thousands play, And bears amid the thickets stray; Wide-known by Chitrakúma's name, It rivals Gandhamádan's329 fame. Long as the man that hill who seeks Gazes upon its sacred peaks, To holy things his soul he gives And pure from thought of evil lives. There, while a hundred autumns fled, Has many a saint with hoary head Spent his pure life, and won the prize, By deep devotion, in the skies: Best home, I ween, if such retreat, Far from the ways of men, be sweet: Or let thy years of exile flee Here in this hermitage with me.” Thus Bharadvája spake, and trained In lore of duty, entertained The princes and the dame, and pressed His friendly gifts on every guest. 328 The Langúr is a large monkey. 329 A mountain said to lie to the east of Meru.
- **Translation**: 

---

### Verse 14 (Ramayan 0.574)
- **Original**: 556 The Ramayana Thus to Prayág the hero went, Thus saw the saint preëminent, And varied speeches heard and said: Then holy night o'er heaven was spread. And Ráma took, by toil oppressed, With Sítá and his brother, rest; And so the night, with sweet content, In Bharadvája's grove was spent. But when the dawn dispelled the night, Ráma approached the anchorite, And thus addressed the holy sire Whose glory shone like kindled fire: “Well have we spent, O truthful Sage, The night within thy hermitage: Now let my lord his guests permit For their new home his grove to quit.” Then, as he saw the morning break, In answer Bharadvája spake: “Go forth to Chitrakúma's hill, Where berries grow, and sweets distil: Full well, I deem, that home will suit Thee, Ráma, strong and resolute. Go forth, and Chitrakúma seek, Famed mountain of the Varied Peak. In the wild woods that gird him round All creatures of the chase are found: Thou in the glades shalt see appear Vast herds of elephants and deer. With Sítá there shalt thou delight To gaze upon the woody height; There with expanding heart to look On river, table-land, and brook, And see the foaming torrent rave
- **Translation**: 

---

### Verse 15 (Ramayan 0.575)
- **Original**: Canto LV. The Passage Of Yamuná. 557 Impetuous from the mountain cave. Auspicious hill! where all day long The lapwing's cry, the Koïl's song Make all who listen gay: Where all is fresh and fair to see, Where elephants and deer roam free, There, as a hermit, stay.” Canto LV. The Passage Of Yamuná. The princely tamers of their foes Thus passed the night in calm repose, Then to the hermit having bent With reverence, on their way they went. High favour Bharadvája showed, And blessed them ready for the road. [160] With such fond looks as fathers throw On their own sons, before they go. Then spake the saint with glory bright To Ráma peerless in his might: “First, lords of men, direct your feet Where Yamuná and Gangá meet; Then to the swift Kálindí330 go, Whose westward waves to Gangá flow. When thou shalt see her lovely shore Worn by their feet who hasten o'er, Then, Raghu's son, a raft prepare, And cross the Sun born river there. Upon her farther bank a tree, 330 Another name of the Jumna, daughter of the Sun.
- **Translation**: 

---

### Verse 16 (Ramayan 0.576)
- **Original**: 558 The Ramayana Near to the landing wilt thou see. The blessed source of varied gifts, There her green boughs that Fig-tree lifts: A tree where countless birds abide, By Zyáma's name known far and wide. Sítá, revere that holy shade: There be thy prayers for blessing prayed. Thence for a league your way pursue, And a dark wood shall meet your view, Where tall bamboos their foliage show, The Gum-tree and the Jujube grow. To Chitrakúma have I oft Trodden that path so smooth and soft, Where burning woods no traveller scare, But all is pleasant, green, and fair.” When thus the guests their road had learned, Back to his cot the hermit turned, And Ráma, LakshmaG, Sítá paid Their reverent thanks for courteous aid. Thus Ráma spake to LakshmaG, when The saint had left the lords of men: “Great store of bliss in sooth is ours On whom his love the hermit showers.” As each to other wisely talked, The lion lords together walked On to Kálindí's woody shore; And gentle Sítá went before. They reached that flood, whose waters flee With rapid current to the sea; Their minds a while to thought they gave And counselled how to cross the wave. At length, with logs together laid, A mighty raft the brothers made.
- **Translation**: 

---

### Verse 17 (Ramayan 0.577)
- **Original**: Canto LV. The Passage Of Yamuná. 559 Then dry bamboos across were tied, And grass was spread from side to side. And the great hero LakshmaG brought Cane and Rose-Apple boughs and wrought, Trimming the branches smooth and neat, For Sítá's use a pleasant seat. And Ráma placed thereon his dame Touched with a momentary shame, Resembling in her glorious mien All-thought-surpassing Fortune's Queen. Then Ráma hastened to dispose, Each in its place, the skins and bows, And by the fair Videhan laid The coats, the ornaments, and spade. When Sítá thus was set on board, And all their gear was duly stored, The heroes each with vigorous hand, Pushed off the raft and left the land. When half its way the raft had made, Thus Sítá to Kálindí prayed: “Goddess, whose flood I traverse now, Grant that my lord may keep his vow. For thee shall bleed a thousand kine, A hundred jars shall pour their wine, When Ráma sees that town again Where old Ikshváku's children reign.” Thus to Kálindí's stream she sued And prayed in suppliant attitude. Then to the river's bank the dame, Fervent in supplication, came. They left the raft that brought them o'er, And the thick wood that clothed the shore, And to the Fig-treeZyáma made
- **Translation**: 

---

### Verse 18 (Ramayan 0.578)
- **Original**: 560 The Ramayana Their way, so cool with verdant shade. Then Sítá viewed that best of trees, And reverent spake in words like these: “Hail, hail, O mighty tree! Allow My husband to complete his vow; Let us returning, I entreat, Kau [alyá and Sumitrá meet.” Then with her hands together placed Around the tree she duly paced. When Ráma saw his blameless spouse A suppliant under holy boughs, The gentle darling of his heart, He thus to LakshmaG spake apart: “Brother, by thee our way be led; Let Sítá close behind thee tread: I, best of men, will grasp my bow, And hindmost of the three will go. What fruits soe'er her fancy take, Or flowers half hidden in the brake, For Janak's child forget not thou To gather from the brake or bough.” Thus on they fared. The tender dame Asked Ráma, as they walked, the name Of every shrub that blossoms bore, Creeper, and tree unseen before: And Lakshma G fetched, at Sítá's prayer, Boughs of each tree with clusters fair. Then Janak's daughter joyed to see The sand-discoloured river flee, Where the glad cry of many a bird, The sáras and the swan, was heard. A league the brothers travelled through The forest noble game they slew:
- **Translation**: 

---

### Verse 19 (Ramayan 0.579)
- **Original**: Canto LVI. Chitrakúta 561 Beneath the trees their meal they dressed And sat them down to eat and rest. A while in that delightful shade Where elephants unnumbered strayed, Where peacocks screamed and monkeys played, [161] They wandered with delight. Then by the river's side they found A pleasant spot of level ground, Where all was smooth and fair around, Their lodging for the night. Canto LVI. Chitrakúta Then Ráma, when the morning rose, Called LakshmaG gently from repose: “Awake, the pleasant voices hear Of forest birds that warble near. Scourge of thy foes, no longer stay; The hour is come to speed away.”
- **Translation**: 

---

### Verse 20 (Ramayan 0.580)
- **Original**: 562 The Ramayana The slumbering prince unclosed his eyes When thus his brother bade him rise, Compelling, at the timely cry, Fatigue, and sleep, and rest to fly. The brothers rose and Sítá too; Pure water from the stream they drew, Paid morning rites, then followed still The road to Chitrakúma's hill. Then Ráma as he took the road With LakshmaG, while the morning, glowed, To the Videhan lady cried, Sítá the fair, the lotus-eyed: “Look round thee, dear; each flowery tree Touched with the fire of morning see: The Kin[uk, now the Frosts are fled,— How glorious with his wreaths of red! The Bel-trees see, so loved of men, Hanging their boughs in every glen. O'erburthened with their fruit and flowers: A plenteous store of food is ours. See, LakshmaG, in the leafy trees, Where'er they make their home. Down hangs, the work of labouring bees The ponderous honeycomb. In the fair wood before us spread The startled wild-cock cries: Hark, where the flowers are soft to tread, The peacock's voice replies. Where elephants are roaming free, And sweet birds' songs are loud, The glorious Chitrakúma see: His peaks are in the cloud. On fair smooth ground he stands displayed, Begirt by many a tree:
- **Translation**: 

---

