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

### Verse 1 (Ramayan 0.1581)
- **Original**: Canto XXII. Ocean Threatened. 1563 With angry menace Ráma, best Of Raghu's sons, the Sea addressed: “With fiery flood of arrowy rain Thy channels will I dry and drain. And I and all the Vánar host Will reach on foot the farther coast. Thou shalt not from destruction save The creatures of the teeming wave, And lapse of time shall ne'er efface The memory of the dire disgrace.” Thus spoke the warrior, and prepared The mortal shaft which never spared, Known mystic weapon, by the name Of Brahmá, red with quenchless flame. Great terror, as he strained the bow, Struck heaven above and earth below. Through echoing skies the thunder pealed, And startled mountains rocked and reeled, The earth was black with sudden night And heaven was blotted from the sight. Then ever and anon the glare Of meteors shot through murky air, And with a wild terrific sound Red lightnings struck the trembling ground. In furious gusts the fierce wind blew: Tall trees it shattered and o'erthrew, And, smiting with a giant's stroke, Huge masses from the mountain broke. A cry of terror long and shrill Came from each valley, plain, and hill. Each ruined dale, each riven peak Re-echoed with a wail or shriek.
- **Translation**: 

---

### Verse 2 (Ramayan 0.1582)
- **Original**: 1564 The Ramayana While Raghu's son undaunted gazed, The waters of the deep were raised, And, still uplifted more and more, Leapt in wild flood upon the shore. Still Ráma looked upon the tide And kept his post unterrified. Then from the seething flood upreared Majestic Ocean's form appeared, As rising from his eastern height Springs through the sky the Lord of Light. Attendant on their monarch came Sea serpents with their eyes aflame. Like lazulite mid burning gold His form was wondrous to behold. Bright with each fairest precious stone A chain about his neck was thrown. Calm shone his lotus eyes beneath The blossoms of his heavenly wreath, And many a pearl and sea-born gem Flashed in the monarch's diadem. There Gangá, tributary queen, And Sindhu934 by his lord, were seen,[444] And every stream and brook renowned In ancient story girt him round. Then, as the waters rose and swelled, The king with suppliant hands upheld, His glorious head to Ráma bent And thus addressed him reverent: “Air, ether, fire, earth, water, true To nature's will, their course pursue; And I, as ancient laws ordain, Unfordable must still remain. 934 The Indus.
- **Translation**: 

---

### Verse 3 (Ramayan 0.1583)
- **Original**: Canto XXII. Ocean Threatened. 1565 Yet, Raghu's son, my counsel hear: I ne'er for love or hope or fear Will pile my waters in a heap And leave a pathway through the deep. Still shall my care for thee provide An easy passage o'er the tide, And like a city's paven street Shall be the road beneath thy feet.” He ceased: and Ráma spoke again: “This spell is ne'er invoked in vain. Where shall the magic shaft, to spend The fury of its might, descend?” “Shoot,” Ocean cried,“thine arrow forth With all its fury to the north, Where sacred Drumakulya lies, Whose glory with thy glory vies. There dwells a wild Abhíra935 race, As vile in act as foul of face, Fierce Dasyus936 who delight in ill, And drink my tributary rill. My soul no longer may endure Their neighbourhood and touch impure. At these, O son of Raghu, aim Thine arrow with the quenchless flame.” Swift from the bow, as Ráma drew His cord, the fiery arrow flew. Earth groaned to feel the wound, and sent A rush of water through the rent; And famed for ever is the well Of VraGa937 where the arrow fell. 935 Cowherds, sprung from a Bráhman and a woman of the medical tribe, the modern Ahírs. 936 Barbarians or outcasts. 937 VraGa means wound or rent.
- **Translation**: 

---

### Verse 4 (Ramayan 0.1584)
- **Original**: 1566 The Ramayana Then every brook and lake beside Throughout the region Ráma dried. But yet he gave a boon to bless And fertilize the wilderness: No fell disease should taint the air, And sheep and kine should prosper there: Earth should produce each pleasant root, The stately trees should bend with fruit; Oil, milk, and honey should abound, And fragrant herbs should clothe the ground. Then spake the king of brooks and seas To Raghu's son in words like these: “Now let a wondrous task be done By Nala, Vi[vakarmá's son, Who, born of one of Vánar race, Inherits by his father's grace A share of his celestial art. Call Nala to perform his part, And he, divinely taught and skilled, A bridge athwart the sea shall build.” He spoke and vanished. Nala, best Of Vánar chiefs, the king addressed: “O'er the deep sea where monsters play A bridge, O Ráma, will I lay; For, sharer of my father's skill, Mine is the power and mine the will. 'Tis vain to try each gentler art To bribe and soothe the thankless heart; In vain on such is mercy spent; It yields to naught but punishment. Through fear alone will Ocean now A passage o'er his waves allow. My mother, ere she bore her son,
- **Translation**: 

---

### Verse 5 (Ramayan 0.1585)
- **Original**: Canto XXII. Ocean Threatened. 1567 This boon from Vi[vakarmá won: “O Mandarí, thy child shall be In skill and glory next to me.” But why unbidden should I fill Thine ear with praises of my skill? Command the Vánar hosts to lay Foundations for the bridge to-day.” He spoke: and swift at Ráma's hest Up sprang the Vánars from their rest, The mandate of the king obeyed And sought the forest's mighty shade. Unrooted trees to earth they threw, And to the sea the timber drew. The stately palm was bowed and bent, A [okas from the ground were rent, And towering Sáls and light bamboos, And trees with flowers of varied hues, With loveliest creepers wreathed and crowned, Shook, reeled, and fell upon the ground. With mighty engines piles of stone And seated hills were overthrown: Unprisoned waters sprang on high, In rain descending from the sky: And ocean with a roar and swell Heaved wildly when the mountains fell. Then the great bridge of wondrous strength Was built, a hundred leagues in length. Rocks huge as autumn clouds bound fast With cordage from the shore were cast, And fragments of each riven hill, And trees whose flowers adorned them still. Wild was the tumult, loud the din As ponderous rocks went thundering in.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1586)
- **Original**: 1568 The Ramayana Ere set of sun, so toiled each crew, Ten leagues and four the structure grew; The labours of the second day Gave twenty more of ready way, And on the fifth, when sank the sun, The whole stupendous work was done. O'er the broad way the Vánars sped, Nor swayed it with their countless tread.[445] Exultant on the ocean strand VibhishaG stood, and, mace in hand, Longed eager for the onward way, And chafed impatient at delay. Then thus to Ráma trained and tried In battle King Sugríva cried: “Come, Hanumán's broad back ascend; Let Angad help to LakshmaG lend. These high above the sea shall bear Their burthen through the ways of air.” So, with Sugríva, borne o'erhead Ikshváku's sons the legions led. Behind, the Vánar hosts pursued Their march in endless multitude. Some skimmed the surface of the wave, To some the air a passage gave. Amid their ceaseless roar the sound Of Ocean's fearful voice was drowned, As o'er the bridge by Nala planned They hastened on to Lanká's strand, Where, by the pleasant brooks, mid trees Loaded with fruit, they took their ease.
- **Translation**: 

---

### Verse 7 (Ramayan 0.1587)
- **Original**: Canto XXIII. The Omens. 1569 Canto XXIII. The Omens. Then Ráma, peerless in the skill That marks each sign of good and ill, Strained his dear brother to his breast, And thus with prudent words addressed: “Now, LakshmaG, by the water's side In fruitful groves the host divide, That warriors of each woodland race May keep their own appointed place. Dire is the danger: loss of friends, Of Vánars and of bears, impends. Distained with dust the breezes blow, And earth is shaken from below. The tall hills rock from foot to crown, And stately trees come toppling down. In threatening shape, with voice of fear, The clouds like cannibals appear, And rain in fitful torrents, red With sanguinary drops, is shed. Long streaks of lurid light invest The evening skies from east to west. And from the sun at times a ball Of angry fire is seen to fall. From every glen and brake is heard The boding voice of beast and bird: From den and lair night-prowlers run And shriek against the falling sun. Up springs the moon, but hot and red Kills the sad night with woe and dread; No gentle lustre, but the gloom That heralds universal doom. A cloud of dust and vapour mars The beauty of the evening stars,
- **Translation**: 

---

### Verse 8 (Ramayan 0.1588)
- **Original**: 1570 The Ramayana And wild and fearful is the sky As though the wreck of worlds were nigh. Around our heads in boding flight Wheel hawk and vulture, crow and kite; And every bird of happy note Shrieks terror from his altered throat. Sword, spear and shaft shall strew the plain Dyed red with torrents of the slain. To-day the Vánar troops shall close Around the city of our foes.” Canto XXIV. The Spy's Return. As shine the heavens with autumn's moon Refulgent in the height of noon, So shone with light which Ráma gave That army of the bold and brave, As from the sea it marched away In war's magnificent array, And earth was shaken by the beat And trampling of unnumbered feet. Then to the giants' ears were borne, The mingled notes of drum and horn, And clash of tambours smote the sky, And shouting and the battle cry. The sound of martial strains inspired Each chieftain, and his bosom fired: While giants from their walls replied, And answering shouts the foe defied, Then Ráma looked on Lanká where Bright banners floated in the air,
- **Translation**: 

---

### Verse 9 (Ramayan 0.1589)
- **Original**: Canto XXIV. The Spy's Return. 1571 And, pierced with anguish at the view, His loving thoughts to Sítá flew. “There, prisoned by the giant, lies My lady of the tender eyes, Like RohiGí the queen of stars O'erpowered by the fiery Mars.” Then turned he to his brother chief And cried in agony of grief: “See on the hill, divinely planned And built by Vi[vakarmá's hand, The towers and domes of Lanká rise In peerless beauty to the skies. Bright from afar the city shines With gleam of palaces and shrines, Like pale clouds through the region spread By VishGu's self inhabited. Fair gardens grow, and woods between The stately domes are fresh and green, Where trees their bloom and fruit display, And sweet birds sing on every spray. Each bird is mad with joy, and bees Sing labouring in the bloomy trees On branches by the breezes bowed, Where the gay Koïl's voice is loud.” This said, he ranged with warlike art Each body of the host apart. [446] “There in the centre,” Ráma cried, “Be Angad's place by Níla's side. Let Rishabh of impetuous might Be lord and leader on the right, And Gandhamádan, next in rank, Be captain of the farther flank. Lakshma G and I the hosts will lead,
- **Translation**: 

---

### Verse 10 (Ramayan 0.1590)
- **Original**: 1572 The Ramayana And Jámbaván of ursine breed, With bold SusheG unused to fear, And Vegadar[í, guide the rear.” Thus Ráma spoke: the chiefs obeyed; And all the Vánar hosts arrayed Showed awful as the autumn sky When clouds embattled form on high. Their arms were mighty trees o'erthrown, And massy blocks of mountain stone. One hope in every warlike breast, One firm resolve, they onward pressed, To die in fight or batter down The walls and towers of Lanká's town. Those marshalled legions Ráma eyed, And thus to King Sugríva cried: “Now, Monarch, ere the hosts proceed, LetZuka, RávaG's spy, be freed.” He spoke: the Vánar gave consent And loosed him from imprisonment: And Zuka, trembling and afraid, His homeward way to RávaG made. Loud laughed the lord of Lanká's isle: “Where hast thou stayed this weary while? Why is thy plumage marred, and why Do twisted cords thy pinions tie? Say, comest thou in evil plight The victim of the Vánars' spite?”
- **Translation**: 

---

### Verse 11 (Ramayan 0.1591)
- **Original**: Canto XXIV. The Spy's Return. 1573 He ceased: the spy his fear controlled, And to the king his story told: “I reached the ocean's distant shore, Thy message to the king I bore. In sudden wrath the Vánars rose, They struck me down with furious blows; They seized me helpless on the ground, My plumage rent, my pinions bound. They would not, headlong in their ire, Consider, listen, or inquire; So fickle, wrathful, rough and rude Is the wild forest multitude. There, marshalling the Vánar bands, King Ráma with Sugríva stands, Ráma the matchless warrior, who Virádha and Kabandha slew, Khara, and countless giants more, And tracks his queen to Lanká's shore. A bridge athwart the sea was cast, And o'er it have his legions passed. Hark! heralded by horns and drums The terrible avenger comes. E'en now the giants' isle he fills With warriors huge as clouds and hills, And burning with vindictive hate Will thunder soon at Lanká's gate. Yield or oppose him: choose between Thy safety and the Maithil queen.” He ceased: the tyrant's eyeballs blazed With fury as his voice he raised: “No, if the dwellers of the sky, Gandharvas, fiends assail me, I Will keep the Maithil lady still,
- **Translation**: 

---

### Verse 12 (Ramayan 0.1592)
- **Original**: 1574 The Ramayana Nor yield her back for fear of ill. When shall my shafts with iron hail My foeman, Raghu's son, assail, Thick as the bees with eager wing Beat on the flowery trees of spring? O, let me meet my foe at length, And strip him of his vaunted strength, Fierce as the sun who shines afar Stealing the light of every star. Strong as the sea's impetuous might My ways are like the tempest's flight; But Ráma knows not this, or he In terror from my face would flee.” Canto XXV. Rávan's Spies.938 When Ráma and the host he led Across the sea had safely sped, Thus RávaG, moved by wrath and pride, To Zuka and to SáraG cried: “O counsellors, the Vánar host Has passed the sea from coast to coast, And Da [aratha's son has wrought A wondrous deed surpassing thought. And now in truth I needs must know The strength and number of the foe. Go ye, to Ráma's host repair And count me all the legions there. Learn well what power each captain leads 938 Here in the Bengal recension (Gorresio's edition), begins Book VI.
- **Translation**: 

---

### Verse 13 (Ramayan 0.1593)
- **Original**: Canto XXV. Rávan's Spies. 1575 His name and fame for warlike deeds. Learn by what artist's wondrous aid That bridge athwart the sea was made; Learn how the Vánar host came o'er And halted on the island shore. Mark Ráma son of Raghu well; His valour, strength, and weapons tell. Watch his advisers one by one, And Lakshma G, Raghu's younger son. Learn with observant eyes, and bring “Unerring tidings to your king. He ceased: then swift in Vánar guise Forth on their errand sped the spies. They reached the Vánars, and, dismayed, Their never-ending lines surveyd: Nor would they try, in mere despair, To count the countless legions there, [447] That crowded valley, plain and hill, That pressed about each cave and rill. Though sea-like o'er the land were spread The endless hosts which Ráma led, The bridge by thousands yet was lined, And eager myriads pressed behind. But sage VibhishaG's watchful eyes Had marked the giants in disguise. He gave command the pair to seize, And told the tale in words like these: “O Ráma these, well known erewhile, Are giant sons of Lanká's isle, Two counsellors of RávaG sent To watch the invading armament.”
- **Translation**: 

---

### Verse 14 (Ramayan 0.1594)
- **Original**: 1576 The Ramayana VibhishaG ceased: at Ráma's look The Rákshas envoys quailed and shook; Then suppliant hand to hand they pressed And thus Ikshváku's son addressed: “O Ráma, bear the truth we speak: Our monarch RávaG bade us seek The Vánar legions and survey Their numbers, strength, and vast array.” Then Ráma, friend and hope and guide Of suffering creatures, thus replied: “Now giants, if your eyes have scanned Our armies, numbering every band, Marked lord and chief, and gazed their fill, Return to RávaG when ye will. If aught remain, if aught anew Ye fain would scan with closer view, VibhishaG, ready at your call, Will lead you forth and show you all. Think not of bonds and capture; fear No loss of life, no peril here: For, captive, helpless and unarmed, An envoy never should be harmed. Again to Lanká's town repair, Speed to the giant monarch there, And be these words to RávaG told, Fierce brother of the Lord of Gold: “Now, tyrant, tremble for thy sin: Call up thy friends, thy kith and kin, And let the power and might be seen Which made thee bold to steal my queen. To-morrow shall thy mournful eye Behold thy bravest warriors die,
- **Translation**: 

---

### Verse 15 (Ramayan 0.1595)
- **Original**: Canto XXV. Rávan's Spies. 1577 And Lanká's city, tower and wall, Struck by my fiery shafts, will fall. Then shall my vengeful blow descend Its rage on thee and thine to spend, Fierce as the fiery bolt that flew From heaven against the Dánav crew, Mid those rebellious demons sent By him who rules the firmament.” Thus spake Ikshváku's son, and ceased: The giants from their bonds released Lauded the King with glad accord, And hasted homeward to their lord. Before the tyrant side by side Zuka and SáraG stood and cried: “VibhishaG seized us, King, and fain His helpless captives would have slain. But glorious Ráma saw us; he, Great-hearted hero, made us free. There in one spot our eyes beheld Four chiefs on earth unparalleled, Who with the guardian Gods may vie Who rule the regions of the sky. There Ráma stood, the boast and pride Of Raghu's race, by LakshmaG's side. There stood the sage VibhishaG, there Sugríva strong beyond compare. These four alone can batter down Gate, rampart, wall, and Lanká's town. Nay, Ráma matchless in his form, A single foe, thy town would storm: So wondrous are his weapons, he Needs not the succour of the three. Why speak we of the countless train
- **Translation**: 

---

### Verse 16 (Ramayan 0.1596)
- **Original**: 1578 The Ramayana That fills the valley, hill and plain, The millions of the Vánar breed Whom Ráma and Sugríva lead? O King, be wise, contend no more, And Sítá to her lord restore.” Canto XXVI. The Vánar Chiefs. “Not if the Gods in heaven who dwell, Gandharvas, and the fiends of hell In banded opposition rise Against me, will I yield my prize. Still trembling from the ungentle touch Of Vánar hands ye fear too much, And bid me, heedless of the shame, Give to her lord the Maithil dame.” Thus spoke the king in stern reproof; Then mounted to his palace roof Aloft o'er many a story raised, And on the lands beneath him gazed. There by his faithful spies he stood And looked on sea and hill and wood. There stretched before him far away The Vánars' numberless array: Scarce could the meadows' tender green Beneath their trampling feet be seen. He looked a while with furious eye, Then questioned thus the nearer spy: “Bend, SáraG, bend thy gaze, and show The leaders of the Vánar foe.
- **Translation**: 

---

### Verse 17 (Ramayan 0.1597)
- **Original**: Canto XXVI. The Vánar Chiefs. 1579 Tell me their heroes' names, and teach The valour, power and might of each.” Obedient SáraG eyed the van, The leaders marked, and thus began: “That chief conspicuous at the head Of warriors in the forest bred, Who hither bends his ruthless eye And shouts his fearful battle cry: [448] Whose voice with pealing thunder shakes All Lanká, with the groves and lakes And hills that tremble at the sound, Is Níla, for his might renowned: First of the Vánar lords controlled By King Sugríva lofty-souled. He who his mighty arm extends, And his fierce eye on Lanká bends, In stature like a stately tower, In colour like a lotus flower, Who with his wild earth-shaking cries Thee, RávaG, to the field defies, Is Angad, by Sugríva's care Anointed his imperial heir: In wondrous strength, in martial fire Peer of King Báli's self, his sire; For Ráma's sake in arms arrayed Like VaruG called toZakra's aid. Behind him, girt by warlike bands, Nala the mighty Vánar stands, The son of Vi[vakarmá, he Who built the bridge athwart the sea. Look farther yet, O King, and mark That chieftain clothed in Sandal bark. 'TisZweta, famed among his peers,
- **Translation**: 

---

### Verse 18 (Ramayan 0.1598)
- **Original**: 1580 The Ramayana A sage whom all his race reveres. See, in Sugríva's ear he speaks, Then, hasting back, his post reseeks, And turns his practised eye to view The squadrons he has formed anew. Next Kumud stands who roamed of yore On Gomatí's939 delightful shore, Feared where the waving woods invest His seat on Mount Sanrochan's crest. Next him a chieftain strong and dread, Comes Cha G a at his legions' head; Exulting in his warrior might He hastens, burning for the fight, And boasts that his unaided powers Shall cast to earth thy walls and towers. Mark, mark that chief of lion gait, Who views thee with a glance of hate As though his very eyes would burn The city walls to which they turn: 'Tis Rambha, Vánar king; he dwells In KrishGagiri's tangled dells, Where Vindhya's pleasant slopes are spread And fair Sudar[an lifts his head. There, listening with erected ears, Zarabha, mighty chief, appears. His soul is burning for the strife, Nor dreads the jeopardy of life. He trembles as he moves, for ire, And bends around his glance of fire. Next, like a cloud that veils the skies, A chieftain of terrific size, Conspicuous mid the Vánars, comes 939 The Goomtee.
- **Translation**: 

---

### Verse 19 (Ramayan 0.1599)
- **Original**: Canto XXVII. The Vánar Chiefs. 1581 With battle shout like rolling drums, 'Tis Panas, trained in war and tried, Who dwells on Páriyátra's side. He, far away, the chief who throws A glory o'er the marshalled rows That ranged behind their captain stand Exulting on the ocean strand, Is Vinata the fierce in fight, Preëminent like Dardur's height. That chieftain bending down to drink On lovely VeGá's verdant brink, Is Krathan; now he lifts his eyes And thee to mortal fray defies. Next Gavaya comes, whose haughty mind Scorns all the warriors of his kind. He comes to trample— such his boast— On Lanká with his single host.” Canto XXVII. The Vánar Chiefs. “Yet more remain, brave chiefs who stake Their noble lives for Ráma's sake. See, glorious, golden-coated, one Who glisters like the morning sun, Whom thousands of his race surround, 'Tis Hara for his strength renowned. Next comes a mighty chieftain, he Whose legions, armed with rock and tree, Press on, in numbers passing tale, The ramparts of our town to scale. O RávaG, see the king advance
- **Translation**: 

---

### Verse 20 (Ramayan 0.1600)
- **Original**: 1582 The Ramayana Terrific with his fiery glance, Girt by the bravest of his train, Majestic as the God of Rain, Parjanya, when his host of clouds About the king, embattled, crowds: On Rikshaván's high mountain nursed, In Narmadá940 he slakes his thirst, Dhúmra, proud ursine chief, who leads Wild warriors whom the forest breeds. His brother, next in strength and age, In Jámbaván the famous sage. Of yore his might and skill he lent To him who rules the firmament, And Indra's liberal boons repaid The chieftain for the timely aid. There like a gloomy cloud that flies Borne by the tempest through the skies, Pramáthí stands: he roamed of yore The forest wilds on Gangá's shore, Where elephants were struck with dread And trembling at his coming fled. There on his foes he loved to sate The old hereditary hate.941[449] Look, Gaja and Gaváksha show Their lust of battle with the foe. See Nala burning for the fray, And Níla chafing at delay. Behind the eager captains press Wild hosts in numbers numberless, And each for Ráma's sake would fall 940 The Anglicized Nerbudda. 941 According to a Pauranik legend Ke[arí Hanumán's putative father had killed an Asur or demon who appeared in the form of an elephant, and hence arose the hostility between Vánars and elephants.
- **Translation**: 

---

