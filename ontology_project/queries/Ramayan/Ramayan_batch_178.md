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

### Verse 1 (Ramayana 0.1586)
- **Original**: 1568 The Ramayana Ere set of sun, so toiled each crew, Ten leagues and four the structure grew; The labours of the second day Gave twenty more of ready way, And on the fifth, when sank the sun, The whole stupendous work was done. O'er the broad way the Vánars sped, Nor swayed it with their countless tread.[445] Exultant on the ocean strand VibhishaG stood, and, mace in hand, Longed eager for the onward way, And chafed impatient at delay. Then thus to Ráma trained and tried In battle King Sugríva cried: “Come, Hanumán's broad back ascend; Let Angad help to LakshmaG lend. These high above the sea shall bear Their burthen through the ways of air.” So, with Sugríva, borne o'erhead Ikshváku's sons the legions led. Behind, the Vánar hosts pursued Their march in endless multitude. Some skimmed the surface of the wave, To some the air a passage gave. Amid their ceaseless roar the sound Of Ocean's fearful voice was drowned, As o'er the bridge by Nala planned They hastened on to Lanká's strand, Where, by the pleasant brooks, mid trees Loaded with fruit, they took their ease.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1587)
- **Original**: Canto XXIII. The Omens. 1569 Canto XXIII. The Omens. Then Ráma, peerless in the skill That marks each sign of good and ill, Strained his dear brother to his breast, And thus with prudent words addressed: “Now, LakshmaG, by the water's side In fruitful groves the host divide, That warriors of each woodland race May keep their own appointed place. Dire is the danger: loss of friends, Of Vánars and of bears, impends. Distained with dust the breezes blow, And earth is shaken from below. The tall hills rock from foot to crown, And stately trees come toppling down. In threatening shape, with voice of fear, The clouds like cannibals appear, And rain in fitful torrents, red With sanguinary drops, is shed. Long streaks of lurid light invest The evening skies from east to west. And from the sun at times a ball Of angry fire is seen to fall. From every glen and brake is heard The boding voice of beast and bird: From den and lair night-prowlers run And shriek against the falling sun. Up springs the moon, but hot and red Kills the sad night with woe and dread; No gentle lustre, but the gloom That heralds universal doom. A cloud of dust and vapour mars The beauty of the evening stars,
- **Translation**: 

---

### Verse 3 (Ramayana 0.1588)
- **Original**: 1570 The Ramayana And wild and fearful is the sky As though the wreck of worlds were nigh. Around our heads in boding flight Wheel hawk and vulture, crow and kite; And every bird of happy note Shrieks terror from his altered throat. Sword, spear and shaft shall strew the plain Dyed red with torrents of the slain. To-day the Vánar troops shall close Around the city of our foes.” Canto XXIV. The Spy's Return. As shine the heavens with autumn's moon Refulgent in the height of noon, So shone with light which Ráma gave That army of the bold and brave, As from the sea it marched away In war's magnificent array, And earth was shaken by the beat And trampling of unnumbered feet. Then to the giants' ears were borne, The mingled notes of drum and horn, And clash of tambours smote the sky, And shouting and the battle cry. The sound of martial strains inspired Each chieftain, and his bosom fired: While giants from their walls replied, And answering shouts the foe defied, Then Ráma looked on Lanká where Bright banners floated in the air,
- **Translation**: 

---

### Verse 4 (Ramayana 0.1589)
- **Original**: Canto XXIV. The Spy's Return. 1571 And, pierced with anguish at the view, His loving thoughts to Sítá flew. “There, prisoned by the giant, lies My lady of the tender eyes, Like RohiGí the queen of stars O'erpowered by the fiery Mars.” Then turned he to his brother chief And cried in agony of grief: “See on the hill, divinely planned And built by Vi[vakarmá's hand, The towers and domes of Lanká rise In peerless beauty to the skies. Bright from afar the city shines With gleam of palaces and shrines, Like pale clouds through the region spread By VishGu's self inhabited. Fair gardens grow, and woods between The stately domes are fresh and green, Where trees their bloom and fruit display, And sweet birds sing on every spray. Each bird is mad with joy, and bees Sing labouring in the bloomy trees On branches by the breezes bowed, Where the gay Koïl's voice is loud.” This said, he ranged with warlike art Each body of the host apart. [446] “There in the centre,” Ráma cried, “Be Angad's place by Níla's side. Let Rishabh of impetuous might Be lord and leader on the right, And Gandhamádan, next in rank, Be captain of the farther flank. Lakshma G and I the hosts will lead,
- **Translation**: 

---

### Verse 5 (Ramayana 0.1590)
- **Original**: 1572 The Ramayana And Jámbaván of ursine breed, With bold SusheG unused to fear, And Vegadar[í, guide the rear.” Thus Ráma spoke: the chiefs obeyed; And all the Vánar hosts arrayed Showed awful as the autumn sky When clouds embattled form on high. Their arms were mighty trees o'erthrown, And massy blocks of mountain stone. One hope in every warlike breast, One firm resolve, they onward pressed, To die in fight or batter down The walls and towers of Lanká's town. Those marshalled legions Ráma eyed, And thus to King Sugríva cried: “Now, Monarch, ere the hosts proceed, LetZuka, RávaG's spy, be freed.” He spoke: the Vánar gave consent And loosed him from imprisonment: And Zuka, trembling and afraid, His homeward way to RávaG made. Loud laughed the lord of Lanká's isle: “Where hast thou stayed this weary while? Why is thy plumage marred, and why Do twisted cords thy pinions tie? Say, comest thou in evil plight The victim of the Vánars' spite?”
- **Translation**: 

---

### Verse 6 (Ramayana 0.1591)
- **Original**: Canto XXIV. The Spy's Return. 1573 He ceased: the spy his fear controlled, And to the king his story told: “I reached the ocean's distant shore, Thy message to the king I bore. In sudden wrath the Vánars rose, They struck me down with furious blows; They seized me helpless on the ground, My plumage rent, my pinions bound. They would not, headlong in their ire, Consider, listen, or inquire; So fickle, wrathful, rough and rude Is the wild forest multitude. There, marshalling the Vánar bands, King Ráma with Sugríva stands, Ráma the matchless warrior, who Virádha and Kabandha slew, Khara, and countless giants more, And tracks his queen to Lanká's shore. A bridge athwart the sea was cast, And o'er it have his legions passed. Hark! heralded by horns and drums The terrible avenger comes. E'en now the giants' isle he fills With warriors huge as clouds and hills, And burning with vindictive hate Will thunder soon at Lanká's gate. Yield or oppose him: choose between Thy safety and the Maithil queen.” He ceased: the tyrant's eyeballs blazed With fury as his voice he raised: “No, if the dwellers of the sky, Gandharvas, fiends assail me, I Will keep the Maithil lady still,
- **Translation**: 

---

### Verse 7 (Ramayana 0.1592)
- **Original**: 1574 The Ramayana Nor yield her back for fear of ill. When shall my shafts with iron hail My foeman, Raghu's son, assail, Thick as the bees with eager wing Beat on the flowery trees of spring? O, let me meet my foe at length, And strip him of his vaunted strength, Fierce as the sun who shines afar Stealing the light of every star. Strong as the sea's impetuous might My ways are like the tempest's flight; But Ráma knows not this, or he In terror from my face would flee.” Canto XXV. Rávan's Spies.938 When Ráma and the host he led Across the sea had safely sped, Thus RávaG, moved by wrath and pride, To Zuka and to SáraG cried: “O counsellors, the Vánar host Has passed the sea from coast to coast, And Da [aratha's son has wrought A wondrous deed surpassing thought. And now in truth I needs must know The strength and number of the foe. Go ye, to Ráma's host repair And count me all the legions there. Learn well what power each captain leads 938 Here in the Bengal recension (Gorresio's edition), begins Book VI.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1593)
- **Original**: Canto XXV. Rávan's Spies. 1575 His name and fame for warlike deeds. Learn by what artist's wondrous aid That bridge athwart the sea was made; Learn how the Vánar host came o'er And halted on the island shore. Mark Ráma son of Raghu well; His valour, strength, and weapons tell. Watch his advisers one by one, And Lakshma G, Raghu's younger son. Learn with observant eyes, and bring “Unerring tidings to your king. He ceased: then swift in Vánar guise Forth on their errand sped the spies. They reached the Vánars, and, dismayed, Their never-ending lines surveyd: Nor would they try, in mere despair, To count the countless legions there, [447] That crowded valley, plain and hill, That pressed about each cave and rill. Though sea-like o'er the land were spread The endless hosts which Ráma led, The bridge by thousands yet was lined, And eager myriads pressed behind. But sage VibhishaG's watchful eyes Had marked the giants in disguise. He gave command the pair to seize, And told the tale in words like these: “O Ráma these, well known erewhile, Are giant sons of Lanká's isle, Two counsellors of RávaG sent To watch the invading armament.”
- **Translation**: 

---

### Verse 9 (Ramayana 0.1594)
- **Original**: 1576 The Ramayana VibhishaG ceased: at Ráma's look The Rákshas envoys quailed and shook; Then suppliant hand to hand they pressed And thus Ikshváku's son addressed: “O Ráma, bear the truth we speak: Our monarch RávaG bade us seek The Vánar legions and survey Their numbers, strength, and vast array.” Then Ráma, friend and hope and guide Of suffering creatures, thus replied: “Now giants, if your eyes have scanned Our armies, numbering every band, Marked lord and chief, and gazed their fill, Return to RávaG when ye will. If aught remain, if aught anew Ye fain would scan with closer view, VibhishaG, ready at your call, Will lead you forth and show you all. Think not of bonds and capture; fear No loss of life, no peril here: For, captive, helpless and unarmed, An envoy never should be harmed. Again to Lanká's town repair, Speed to the giant monarch there, And be these words to RávaG told, Fierce brother of the Lord of Gold: “Now, tyrant, tremble for thy sin: Call up thy friends, thy kith and kin, And let the power and might be seen Which made thee bold to steal my queen. To-morrow shall thy mournful eye Behold thy bravest warriors die,
- **Translation**: 

---

### Verse 10 (Ramayana 0.1595)
- **Original**: Canto XXV. Rávan's Spies. 1577 And Lanká's city, tower and wall, Struck by my fiery shafts, will fall. Then shall my vengeful blow descend Its rage on thee and thine to spend, Fierce as the fiery bolt that flew From heaven against the Dánav crew, Mid those rebellious demons sent By him who rules the firmament.” Thus spake Ikshváku's son, and ceased: The giants from their bonds released Lauded the King with glad accord, And hasted homeward to their lord. Before the tyrant side by side Zuka and SáraG stood and cried: “VibhishaG seized us, King, and fain His helpless captives would have slain. But glorious Ráma saw us; he, Great-hearted hero, made us free. There in one spot our eyes beheld Four chiefs on earth unparalleled, Who with the guardian Gods may vie Who rule the regions of the sky. There Ráma stood, the boast and pride Of Raghu's race, by LakshmaG's side. There stood the sage VibhishaG, there Sugríva strong beyond compare. These four alone can batter down Gate, rampart, wall, and Lanká's town. Nay, Ráma matchless in his form, A single foe, thy town would storm: So wondrous are his weapons, he Needs not the succour of the three. Why speak we of the countless train
- **Translation**: 

---

### Verse 11 (Ramayana 0.1596)
- **Original**: 1578 The Ramayana That fills the valley, hill and plain, The millions of the Vánar breed Whom Ráma and Sugríva lead? O King, be wise, contend no more, And Sítá to her lord restore.” Canto XXVI. The Vánar Chiefs. “Not if the Gods in heaven who dwell, Gandharvas, and the fiends of hell In banded opposition rise Against me, will I yield my prize. Still trembling from the ungentle touch Of Vánar hands ye fear too much, And bid me, heedless of the shame, Give to her lord the Maithil dame.” Thus spoke the king in stern reproof; Then mounted to his palace roof Aloft o'er many a story raised, And on the lands beneath him gazed. There by his faithful spies he stood And looked on sea and hill and wood. There stretched before him far away The Vánars' numberless array: Scarce could the meadows' tender green Beneath their trampling feet be seen. He looked a while with furious eye, Then questioned thus the nearer spy: “Bend, SáraG, bend thy gaze, and show The leaders of the Vánar foe.
- **Translation**: 

---

### Verse 12 (Ramayana 0.1597)
- **Original**: Canto XXVI. The Vánar Chiefs. 1579 Tell me their heroes' names, and teach The valour, power and might of each.” Obedient SáraG eyed the van, The leaders marked, and thus began: “That chief conspicuous at the head Of warriors in the forest bred, Who hither bends his ruthless eye And shouts his fearful battle cry: [448] Whose voice with pealing thunder shakes All Lanká, with the groves and lakes And hills that tremble at the sound, Is Níla, for his might renowned: First of the Vánar lords controlled By King Sugríva lofty-souled. He who his mighty arm extends, And his fierce eye on Lanká bends, In stature like a stately tower, In colour like a lotus flower, Who with his wild earth-shaking cries Thee, RávaG, to the field defies, Is Angad, by Sugríva's care Anointed his imperial heir: In wondrous strength, in martial fire Peer of King Báli's self, his sire; For Ráma's sake in arms arrayed Like VaruG called toZakra's aid. Behind him, girt by warlike bands, Nala the mighty Vánar stands, The son of Vi[vakarmá, he Who built the bridge athwart the sea. Look farther yet, O King, and mark That chieftain clothed in Sandal bark. 'TisZweta, famed among his peers,
- **Translation**: 

---

### Verse 13 (Ramayana 0.1598)
- **Original**: 1580 The Ramayana A sage whom all his race reveres. See, in Sugríva's ear he speaks, Then, hasting back, his post reseeks, And turns his practised eye to view The squadrons he has formed anew. Next Kumud stands who roamed of yore On Gomatí's939 delightful shore, Feared where the waving woods invest His seat on Mount Sanrochan's crest. Next him a chieftain strong and dread, Comes Cha G a at his legions' head; Exulting in his warrior might He hastens, burning for the fight, And boasts that his unaided powers Shall cast to earth thy walls and towers. Mark, mark that chief of lion gait, Who views thee with a glance of hate As though his very eyes would burn The city walls to which they turn: 'Tis Rambha, Vánar king; he dwells In KrishGagiri's tangled dells, Where Vindhya's pleasant slopes are spread And fair Sudar[an lifts his head. There, listening with erected ears, Zarabha, mighty chief, appears. His soul is burning for the strife, Nor dreads the jeopardy of life. He trembles as he moves, for ire, And bends around his glance of fire. Next, like a cloud that veils the skies, A chieftain of terrific size, Conspicuous mid the Vánars, comes 939 The Goomtee.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1599)
- **Original**: Canto XXVII. The Vánar Chiefs. 1581 With battle shout like rolling drums, 'Tis Panas, trained in war and tried, Who dwells on Páriyátra's side. He, far away, the chief who throws A glory o'er the marshalled rows That ranged behind their captain stand Exulting on the ocean strand, Is Vinata the fierce in fight, Preëminent like Dardur's height. That chieftain bending down to drink On lovely VeGá's verdant brink, Is Krathan; now he lifts his eyes And thee to mortal fray defies. Next Gavaya comes, whose haughty mind Scorns all the warriors of his kind. He comes to trample— such his boast— On Lanká with his single host.” Canto XXVII. The Vánar Chiefs. “Yet more remain, brave chiefs who stake Their noble lives for Ráma's sake. See, glorious, golden-coated, one Who glisters like the morning sun, Whom thousands of his race surround, 'Tis Hara for his strength renowned. Next comes a mighty chieftain, he Whose legions, armed with rock and tree, Press on, in numbers passing tale, The ramparts of our town to scale. O RávaG, see the king advance
- **Translation**: 

---

### Verse 15 (Ramayana 0.1600)
- **Original**: 1582 The Ramayana Terrific with his fiery glance, Girt by the bravest of his train, Majestic as the God of Rain, Parjanya, when his host of clouds About the king, embattled, crowds: On Rikshaván's high mountain nursed, In Narmadá940 he slakes his thirst, Dhúmra, proud ursine chief, who leads Wild warriors whom the forest breeds. His brother, next in strength and age, In Jámbaván the famous sage. Of yore his might and skill he lent To him who rules the firmament, And Indra's liberal boons repaid The chieftain for the timely aid. There like a gloomy cloud that flies Borne by the tempest through the skies, Pramáthí stands: he roamed of yore The forest wilds on Gangá's shore, Where elephants were struck with dread And trembling at his coming fled. There on his foes he loved to sate The old hereditary hate.941[449] Look, Gaja and Gaváksha show Their lust of battle with the foe. See Nala burning for the fray, And Níla chafing at delay. Behind the eager captains press Wild hosts in numbers numberless, And each for Ráma's sake would fall 940 The Anglicized Nerbudda. 941 According to a Pauranik legend Ke[arí Hanumán's putative father had killed an Asur or demon who appeared in the form of an elephant, and hence arose the hostility between Vánars and elephants.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1601)
- **Original**: Canto XXVIII. The Chieftains. 1583 Or force his way through Lanká's wall.” Canto XXVIII. The Chieftains. There SáraG ceased: thenZuka broke The silence and to RávaG spoke: “O Monarch, yonder chiefs survey: Like elephants in size are they, And tower like stately trees that grow Where Gangá's nursing waters flow; Yea, tall as mountain pines that fling Long shadows o'er the snow-crowned king. They all in wild Kishkindhá dwell And serve their lord Sugríva well. The Gods' and bright Gandharvas' seed, They take each form that suits their need. Now farther look, O Monarch, where Those chieftains stand, a glorious pair, Conspicuous for their godlike frames; Dwivid and Mainda are their names. Their lips the drink of heaven have known, And Brahmá claims them for his own. That chieftain whom thine eyes behold Refulgent like a hill of gold, Before whose wrathful might the sea Roused from his rest would turn and flee, The peerless Vánar, he who came To Lanká for the Maithil dame, The Wind-God's son Hanumán; thou Hast seen him once, behold him now. Still nearer let thy glance be bent,
- **Translation**: 

---

### Verse 17 (Ramayana 0.1602)
- **Original**: 1584 The Ramayana And mark that prince preëminent Mid chieftains for his strength and size And splendour of his lotus eyes. Far through the worlds his virtues shine, The glory of Ikshváku's line. The path of truth he never leaves, And still through all to duty cleaves. Deep in the Vedas, skilled to wield The mystic shafts to him revealed: Whose flaming darts to heaven ascend, And through the earth a passage rend: In might like him who rules the sky; Like Yáma, when his wrath grows high: Whose queen, the darling of his soul, Thy magic art deceived and stole: There royal Ráma stands and longs For battle to avenge his wrongs. Near on his right a prince, in hue Like pure gold freshly burnished, view: Broad is his chest, his eye is red, His black hair curls about his head: 'Tis LakshmaG, faithful friend, who shares His brother's joys, his brother's cares. By Ráma's side he loves to stand And serve him as his better hand, For whose dear sake without a sigh The warrior youth would gladly die. On Ráma's left VibhishaG view, With giants for his retinue: King-making drops have dewed his head, Appointed monarch in thy stead. Behold that chieftain sternly still, High towering like a rooted hill, Supreme in power and pride of place,
- **Translation**: 

---

### Verse 18 (Ramayana 0.1603)
- **Original**: Canto XXIX. Sárdúla Captured. 1585 The monarch of the Vánar race. Raised high above his woodland kind, In might and glory, frame and mind, His head above his host he shows Conspicuous as the Lord of Snows. His home is far from hostile eyes Where deep in woods Kishkindhá lies. A glistering chain which flowers bedeck With burnished gold adorns his neck. Queen Fortune, loved by Gods and kings, To him her chosen favourite clings. That chain he owes to Ráma's grace, And Tárá and his kingly place. In him the great Sugríva know, Whom Ráma rescued from his foe.”942 Canto XXIX. Sárdúla Captured. The giant viewed with earnest ken The Vánars and the lords of men; Then thus, with grief and anger moved, In bitter tone the spies reproved: “Can faithful servants hope to please Their master with such fates as these? Or hope ye with wild words to wring The bosom of your lord and king? Such words were better said by those Who come arrayed our mortal foes. 942 Here follows the enumeration of Sugríva's forces which I do not attempt to follow. It soon reaches a hundred thousand billions.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1604)
- **Original**: 1586 The Ramayana In vain your ears have heard the sage, And listened to the lore of age, Untaught, though lectured many a day, The first great lesson, to obey, 'Tis marvel RávaG reigns and rules Whose counsellors are blind and fools. Has death no terrors that ye dare To tempt your monarch to despair,[450] From whose imperial mandate flow Disgrace and honour, weal and woe? Yea, forest trees, when flames are fanned About their scorching trunks, may stand; But naught can set the sinner free When kings the punishment decree. I would not in mine anger spare The traitorous foe-praising pair, But years of faithful service plead For pardon, and they shall not bleed. Henceforth to me be dead: depart, Far from my presence and my heart.” Thus spoke the angry king: the two Cried, Long live RávaG, and withdrew, The giant monarch turned and cried To strong Mahodar at his side: “Go thou, and spies more faithful bring. More duteous to their lord the king.” Swift at his word Mahodar shed, And came returning at the head Of long tried messengers, who bent Before their monarch reverent. “Go quickly hence,” said RávaG “scan With keenest eyes the foeman's plan.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1605)
- **Original**: Canto XXIX. Sárdúla Captured. 1587 Learn who, as nearest friends, advise And mould each secret enterprise. Learn when he wakes and goes to rest, Sound every purpose of his breast. Learn what the prince intends to-day: Watch keenly all, and come away.” With joy they heard the words he said: Then withZárdúla at their head About the giant king they went With circling paces reverent. By fair Suvela's grassy side The chiefs of Raghu's race they spied, Where, shaded by the waving wood, VibhishaG and Sugríva stood. A while they rested there and viewed The Vánars' countless multitude. VibhishaG with observant eyes Knew at a glance the giant spies, And bade the warriors of his train Bind the rash foes with cord and chain: “Zárdúla's is the sin,” he cried. He neath the Vánars' hands had died, But Ráma from their fury freed The captive in his utmost need, And, merciful at sight of woe, Loosed all the spies and bade them go. Then home to Lanká's monarch fled The giant chiefs discomfited.
- **Translation**: 

---

