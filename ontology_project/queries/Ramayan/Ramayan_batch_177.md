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

### Verse 1 (Ramayana 0.1566)
- **Original**: 1548 The Ramayana Well ponder every hope and fear Until thy doubtful course be clear; Then own his merit or detect His guile, and welcome or reject.” Then Zarabha the bold and brave In turn his prudent sentence gave: “Yea, Ráma, send a skilful spy With keenest tact to test and try. Then let the stranger, as is just, Obtain or be refused thy trust.” Then he whose heart was rich in store Of scripture's life-directing lore, King Jámbaván, stood forth and cried: “Suspect, suspect a foe allied With RávaG lord of Lanká's isle, And Rákshas sin and Rákshas guile.” Then Mainda, wisest chief, who knew The wrong, the right, the false, the true, Pondered a while, then silence broke, And thus his sober counsel spoke: “Let one with gracious speech draw near And gently charm VibhishaG's ear, Till he the soothing witchery feel And all his secret heart reveal. So thou his aims and hopes shalt know, And hail the friend or shun the foe.”
- **Translation**: 

---

### Verse 2 (Ramayana 0.1567)
- **Original**: Canto XVII. Vibhishan's Flight. 1549 “Not he,” Hanúmán cried,“not he Who taught the Gods928 may rival thee, Supreme in power of quickest sense, First in the art of eloquence. But hear me soothly speak, O King, And learn the hope to which I cling. VibhishaG comes no crafty spy: Urged by his brother's fault to fly. With righteous soul that loathes the sin, He fled from Lanká and his kin. [440] If strangers question, doubt will rise And chill the heart of one so wise. Marred by distrust the parle will end, And thou wilt lose a faithful friend. Nor let it seem so light a thing To sound a stranger's heart, O King. And he, I ween, whate'er he say, Will ne'er an evil thought betray. He comes a friend in happy time, Loathing his brother for his crime. His ear has heard thine old renown, The might that struck King Báli down, And set Sugríva on the throne. And looking now to thee alone He comes thy matchless aid to win And punish RávaG for his sin. Thus have I tried thy heart to move, And thus VibhishaG's truth to prove. Still in his friendship I confide; But ponder, wisest, and decide.” 928 V [ihaspati the preceptor of the Gods.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1568)
- **Original**: 1550 The Ramayana Canto XVIII. Ráma's Speech. Then Ráma's rising doubt was stilled, And friendly thoughts his bosom filled. Thus, deep in Scripture's lore, he spake: “The suppliant will I ne'er forsake, Nor my protecting aid refuse When one in name of friendship sues. Though faults and folly blot his fame, Pity and help he still may claim.” He ceased: Sugríva bowed his head And pondered for a while, and said: “Past number be his faults or few, What think ye of the Rákshas who, When threatening clouds of danger rise, Deserts his brother's side and flies? Say, Vánars, who may hope to find True friendship in his faithless kind?”
- **Translation**: 

---

### Verse 4 (Ramayana 0.1569)
- **Original**: Canto XVIII. Ráma's Speech. 1551 The son of Raghu heard his speech: He cast a hasty look on each Of those brave Vánar chiefs, and while Upon his lips there played a smile, To LakshmaG turned and thus expressed The thoughts that moved his gallant breast: “Well versed in Scripture's lore, and sage And duly reverent to age, Is he, with long experience stored, Who counsels like this Vánar lord. Yet here, methinks, for searching eyes Some deeper, subtler matter lies. To you and all the world are known The perils of a monarch's throne, While foe and stranger, kith and kin By his misfortune trust to win. By hope of such advantage led, VibhishaG o'er the sea has fled. He in his brother's stead would reign, And our alliance seeks to gain; And we his offer may embrace, A stranger and of alien race. But if he comes a spy and foe, What power has he to strike a blow In furtherance of his close design? What is his strength compared with mine? And can I, Vánar King, forget The great, the universal debt, Ever to aid and welcome those Who pray for shelter, friends or foes? Hast thou not heard the deathless praise Won by the dove in olden days, Who conquering his fear and hate Welcomed the slayer of his mate,
- **Translation**: 

---

### Verse 5 (Ramayana 0.1570)
- **Original**: 1552 The Ramayana And gave a banquet, to refresh The weary fowler, of his flesh? Now hear me, Vánar King, rehearse What KaGdu929 spoke in ancient verse, Saint KaGva's son who loved the truth And clave to virtue from his youth: “Strike not the suppliant when he stands And asks thee with beseeching hands For shelter: strike him not although He were thy father's mortal foe. No, yield him, be he proud or meek, The shelter which he comes to seek, And save thy foeman, if the deed Should cost thy life, in desperate need.” And shall I hear the wretched cry, And my protecting aid deny? Shall I a suppliant's prayer refuse, And heaven and glory basely lose? No, I will do for honour sake E'en as the holy KaGdu spake, Preserve a hero's name from stain, And bliss in heaven and glory gain. Bound by a solemn vow I sware That all my saving help should share Who sought me in distress and cried, “Thou art my hope, and none beside.” Then go, I pray thee, Vánar King, VibhishaG to my presence bring, Yea, were he RávaG's self, my vow Forbids me to reject him now.” 929 In Book II, Canto XXI, KaGdu is mentioned by Ráma as an example of filial obedience. At the command of his father he is said to have killed a cow.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1571)
- **Original**: Canto XIX. Vibhishan's Counsel. 1553 He ceased: the Vánar king approved; And Ráma toward VibhishaG moved. So moves, a brother God to greet, Lord Indra from his heavenly seat. [441] Canto XIX. Vibhishan's Counsel. When Raghu's son had owned his claim Down from the air VibhishaG came, And with his four attendants bent At Ráma's feet most reverent. “O Ráma,” thus he cried,“in me VibhishaG, RávaG's brother see. By him disgraced thine aid I seek, Sure refuge of the poor and weak. From Lanká, friends, and wealth I fly, And reft of all on thee rely. On thee, the wretch's firmest friend, My kingdom, joys, and life depend.” With glance of favour Ráma eyed The Rákshas chief and thus replied: “First from thy lips I fain would hear Each brighter hope, each darker fear. Speak, stranger, that I well may know The strength and weakness of the foe.”
- **Translation**: 

---

### Verse 7 (Ramayana 0.1572)
- **Original**: 1554 The Ramayana He ceased: the Rákshas chief obeyed, And thus in turn his answer made: “O Prince, the Self-existent gave This boon to RávaG; he may brave All foes in fight; no fiend or snake, Gandharva, God, his life may take. His brother KumbhakarGa vies In might with him who rules the skies. The captain of his armies— fame Perhaps has taught the warrior's name— Is terrible Prahasta, who King MaGibhadra's930 self o'erthrew. Where is the warrior found to face Young Indrajít, when armed with brace And guard931 and bow he stands in mail And laughs at spear and arrowy hail? Within his city Lanká dwell Ten million giants fierce and fell, Who wear each varied shape at will And eat the flesh of those they kill. These hosts against the Gods he led, And heavenly might discomfited.” Then Ráma cried:“I little heed Gigantic strength or doughty deed. In spite of all their might has done The king, the captain, and the son Shall fall beneath my fury dead, And thou shalt reign in RávaG's stead. He, though in depths of earth he dwell, 930 A King of the Yakshas, or Kuvera himself, the God of Gold. 931 The brace protects the left arm from injury from the bow-string, and the guard protects the fingers of the right hand.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1573)
- **Original**: Canto XIX. Vibhishan's Counsel. 1555 Or seek protection down in hell, Or kneel before the Sire supreme, His forfeit life shall ne'er redeem. Yea, by my brothers' lives I swear, I will not to my home repair Till RávaG and his kith and kin Have paid in death the price of sin.” VibhishaG bowed his head and cried: “Thy conquering army will I guide To storm the city of the foe, And aid the tyrant's overthrow.” Thus spake VibhishaG: Ráma pressed The Rákshas chieftain to his breast, And cried to LakshmaG:“Haste and bring Sea-water for the new-made king.” He spoke, and o'er VibhishaG's head The consecrating drops were shed Mid shouts that hailed with one accord The giants' king and Lanká's lord. “Is there no way,” Hanúmán cried, “No passage o'er the boisterous tide? How may we lead the Vánar host In triumph to the farther coast?” “Thus,” said VibhishaG,“I advise: Let Raghu's son in suppliant guise Entreat the mighty Sea to lend His succour and this cause befriend. His channels, as the wise have told, By Sagar's sons were dug of old,932 Nor will high-thoughted Ocean scorn A prince of Sagar's lineage born.” 932 The story is told in Book I, Cantos XL, XLI, XLII.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1574)
- **Original**: 1556 The Ramayana He ceased; the prudent counsel won The glad assent of Raghu's son. Then on the ocean shore a bed Of tender sacred grass was spread, Where Ráma at the close of day Like fire upon an altar lay. Canto XX. The Spies. Zárdúla, RávaG's spy, surveyed The legions on the strand arrayed. And bore, his bosom racked with fear, These tidings to the monarch's ear: “They come, they come. A rushing tide, Ten leagues they spread from side to side, And on to storm thy city press, Fierce rovers of the wilderness. Rich in each princely power and grace, The pride of Da[aratha's race, Ráma and LakshmaG lead their bands, And halt them on the ocean sands. O Monarch, rise, this peril meet; Risk not the danger of defeat.[442]
- **Translation**: 

---

### Verse 10 (Ramayana 0.1575)
- **Original**: Canto XX. The Spies. 1557 First let each wiser art be tried; Bribe them, or win them, or divide.” Such was the counsel of the spy: And RávaG called toZuka:“Fly, Sugríva lord of Vánars seek, And thus my kingly message speak: “Great power and might and fame are thine, Brave scion of a royal line, King Riksharajas' son, in thee A brother and a friend I see. How wronged by me canst thou complain? What profit here pretend to gain? If from the wood the wife I stole Of Ráma of the prudent soul, What cause hast thou to mourn the theft? Thou art not injured or bereft. Return, O King, thy steps retrace And seek thy mountain dwelling-place. No, never may thy hosts within My Lanká's walls a footing win. A mighty town whose strength defies The gathered armies of the skies.” He ceased: obedientZuka heard; With wings and plumage of a bird He rose in eager speed and through The air upon his errand flew. Borne o'er the sea with rapid wing He stood above the Vánar king, And spoke aloud, sublime in air, The message he was charged to bear. The Vánar heard the words he spoke, And quick redoubling stroke on stroke On head and pinions hemmed him round
- **Translation**: 

---

### Verse 11 (Ramayana 0.1576)
- **Original**: 1558 The Ramayana And bore him struggling to the ground. The Rákshas wounded and distressed These words to Raghu's son addressed: “Quick, quick! This Vánar host restrain, For heralds never must be slain. To him alone, a wretch untrue, The punishment of death is due Who leaves his master's speech unsaid And speaks another in its stead.” Moved by the suppliant speech and prayer Up sprang the prince and cried, forbear. Saved from his wild assailant's blows Again the Rákshas herald rose And borne on light wings to the sky Addressed Sugríva from on high: “O Vánar Monarch, chief endued With power and wonderous fortitude, What answer is my king, the fear And scourge of weeping worlds, to hear?” “Go tell thy lord,” Sugríva cried, “Thou, Ráma's foe, art thus defied. His arm the guilty Báli slew; Thus, tyrant, shalt thou perish too. Thy sons, thy friends, proud King, and all Thy kith and kin with thee shall fall; And, emptied of the giant's brood, Burnt Lanká be a solitude. Fly to the Sun-God's pathway, go And hide thee deep in hell below: In vain from Ráma shalt thou flee Though heavenly warriors fight for thee. Thine arm subdued, securely bold, The Vulture-king infirm and old:
- **Translation**: 

---

### Verse 12 (Ramayana 0.1577)
- **Original**: Canto XX. The Spies. 1559 But will thy puny strength avail When Raghu's wrathful sons assail? A captive in thy palace lies The lady of the lotus eyes: Thou knowest not how fierce and strong Is he whom thou hast dared to wrong. The best of Raghu's lineage, he Whose conquering hand shall punish thee.” He ceased: and Angad raised a cry; “This is no herald but a spy. Above thee from his airy post His rapid eye surveyed our host, Where with advantage he might scan Our gathered strength from rear to van. Bind him, Vánars, bind the spy, Nor let him back to Lanká fly.” They hurled the Rákshas to the ground, They grasped his neck, his pinions bound, And firmly held him while in vain His voice was lifted to complain. But Ráma's heart inclined to spare, He listened to his plaint and prayer, And cried aloud:“O Vánars, cease; The captive from his bonds release.”
- **Translation**: 

---

### Verse 13 (Ramayana 0.1578)
- **Original**: 1560 The Ramayana Canto XXI. Ocean Threatened. His hands in reverence Ráma raised And southward o'er the ocean gazed; Then on the sacred grass that made His lowly couch his limbs he laid. His head on that strong arm reclined Which Sítá, best of womankind, Had loved in happier days to hold With soft arms decked with pearls and gold. Then rising from his bed of grass, “This day,” he cried,“the host shall pass Triumphant to the southern shore, Or Ocean's self shall be no more.” Thus vowing in his constant breast Again he turned him to his rest, And there, his eyes in slumber closed, Silent beside the sea reposed. Thrice rose the Day-God thrice he set, The lord of Ocean came not yet, Thrice came the night, but Raghu's son No answer by his service won. To LakshmaG thus the hero cried, His eyes aflame with wrath and pride: “In vain the softer gifts that grace The good are offered to the base. Long-suffering, patience, gentle speech[443]
- **Translation**: 

---

### Verse 14 (Ramayana 0.1579)
- **Original**: Canto XXI. Ocean Threatened. 1561 Their thankless hearts can never reach. The world to him its honour pays Whose ready tongue himself can praise, Who scorns the true, and hates the right, Whose hand is ever raised to smite. Each milder art is tried in vain: It wins no glory, but disdain. And victory owns no softer charm Than might which nerves a warrior's arm. My humble suit is still denied By Ocean's overweening pride. This day the monsters of the deep In throes of death shall wildly leap. My shafts shall rend the serpents curled In caverns of the watery world, Disclose each sunless depth and bare The tangled pearl and coral there. Away with mercy! at a time Like this compassion is a crime. Welcome, the battle and the foe! My bow! my arrows and my bow! This day the Vánars' feet shall tread The conquered Sea's exhausted bed, And he who never feared before Shall tremble to his farthest shore.” Red flashed his eyes with angry glow: He stood and grasped his mighty bow, Terrific as the fire of doom Whose quenchless flames the world consume. His clanging cord the archer drew, And swift the fiery arrows flew Fierce as the flashing levin sent By him who rules the firmament.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1580)
- **Original**: 1562 The Ramayana Down through the startled waters sped Each missile with its flaming head. The foamy billows rose and sank, And dashed upon the trembling bank. Sea monsters of tremendous form With crash and roar of thunder storm. Still the wild waters rose and fell Crowned with white foam and pearl and shell. Each serpent, startled from his rest, Raised his fierce eyes and glowing crest. And prisoned Dánavs933 where they dwelt In depths below the terror felt. Again upon his string he laid A flaming shaft, but LakshmaG stayed His arm, with gentle reasoning tried To soothe his angry mood, and cried: “Brother, reflect: the wise control The rising passions of the soul. Let Ocean grant, without thy threat, The boon on which thy heart is set. That gracious lord will ne'er refuse When Ráma son of Raghu sues.” He ceased: and voices from the air Fell clear and loud, Spare, Ráma, spare. Canto XXII. Ocean Threatened. 933 Fiends and enemies of the Gods.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1581)
- **Original**: Canto XXII. Ocean Threatened. 1563 With angry menace Ráma, best Of Raghu's sons, the Sea addressed: “With fiery flood of arrowy rain Thy channels will I dry and drain. And I and all the Vánar host Will reach on foot the farther coast. Thou shalt not from destruction save The creatures of the teeming wave, And lapse of time shall ne'er efface The memory of the dire disgrace.” Thus spoke the warrior, and prepared The mortal shaft which never spared, Known mystic weapon, by the name Of Brahmá, red with quenchless flame. Great terror, as he strained the bow, Struck heaven above and earth below. Through echoing skies the thunder pealed, And startled mountains rocked and reeled, The earth was black with sudden night And heaven was blotted from the sight. Then ever and anon the glare Of meteors shot through murky air, And with a wild terrific sound Red lightnings struck the trembling ground. In furious gusts the fierce wind blew: Tall trees it shattered and o'erthrew, And, smiting with a giant's stroke, Huge masses from the mountain broke. A cry of terror long and shrill Came from each valley, plain, and hill. Each ruined dale, each riven peak Re-echoed with a wail or shriek.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1582)
- **Original**: 1564 The Ramayana While Raghu's son undaunted gazed, The waters of the deep were raised, And, still uplifted more and more, Leapt in wild flood upon the shore. Still Ráma looked upon the tide And kept his post unterrified. Then from the seething flood upreared Majestic Ocean's form appeared, As rising from his eastern height Springs through the sky the Lord of Light. Attendant on their monarch came Sea serpents with their eyes aflame. Like lazulite mid burning gold His form was wondrous to behold. Bright with each fairest precious stone A chain about his neck was thrown. Calm shone his lotus eyes beneath The blossoms of his heavenly wreath, And many a pearl and sea-born gem Flashed in the monarch's diadem. There Gangá, tributary queen, And Sindhu934 by his lord, were seen,[444] And every stream and brook renowned In ancient story girt him round. Then, as the waters rose and swelled, The king with suppliant hands upheld, His glorious head to Ráma bent And thus addressed him reverent: “Air, ether, fire, earth, water, true To nature's will, their course pursue; And I, as ancient laws ordain, Unfordable must still remain. 934 The Indus.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1583)
- **Original**: Canto XXII. Ocean Threatened. 1565 Yet, Raghu's son, my counsel hear: I ne'er for love or hope or fear Will pile my waters in a heap And leave a pathway through the deep. Still shall my care for thee provide An easy passage o'er the tide, And like a city's paven street Shall be the road beneath thy feet.” He ceased: and Ráma spoke again: “This spell is ne'er invoked in vain. Where shall the magic shaft, to spend The fury of its might, descend?” “Shoot,” Ocean cried,“thine arrow forth With all its fury to the north, Where sacred Drumakulya lies, Whose glory with thy glory vies. There dwells a wild Abhíra935 race, As vile in act as foul of face, Fierce Dasyus936 who delight in ill, And drink my tributary rill. My soul no longer may endure Their neighbourhood and touch impure. At these, O son of Raghu, aim Thine arrow with the quenchless flame.” Swift from the bow, as Ráma drew His cord, the fiery arrow flew. Earth groaned to feel the wound, and sent A rush of water through the rent; And famed for ever is the well Of VraGa937 where the arrow fell. 935 Cowherds, sprung from a Bráhman and a woman of the medical tribe, the modern Ahírs. 936 Barbarians or outcasts. 937 VraGa means wound or rent.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1584)
- **Original**: 1566 The Ramayana Then every brook and lake beside Throughout the region Ráma dried. But yet he gave a boon to bless And fertilize the wilderness: No fell disease should taint the air, And sheep and kine should prosper there: Earth should produce each pleasant root, The stately trees should bend with fruit; Oil, milk, and honey should abound, And fragrant herbs should clothe the ground. Then spake the king of brooks and seas To Raghu's son in words like these: “Now let a wondrous task be done By Nala, Vi[vakarmá's son, Who, born of one of Vánar race, Inherits by his father's grace A share of his celestial art. Call Nala to perform his part, And he, divinely taught and skilled, A bridge athwart the sea shall build.” He spoke and vanished. Nala, best Of Vánar chiefs, the king addressed: “O'er the deep sea where monsters play A bridge, O Ráma, will I lay; For, sharer of my father's skill, Mine is the power and mine the will. 'Tis vain to try each gentler art To bribe and soothe the thankless heart; In vain on such is mercy spent; It yields to naught but punishment. Through fear alone will Ocean now A passage o'er his waves allow. My mother, ere she bore her son,
- **Translation**: 

---

### Verse 20 (Ramayana 0.1585)
- **Original**: Canto XXII. Ocean Threatened. 1567 This boon from Vi[vakarmá won: “O Mandarí, thy child shall be In skill and glory next to me.” But why unbidden should I fill Thine ear with praises of my skill? Command the Vánar hosts to lay Foundations for the bridge to-day.” He spoke: and swift at Ráma's hest Up sprang the Vánars from their rest, The mandate of the king obeyed And sought the forest's mighty shade. Unrooted trees to earth they threw, And to the sea the timber drew. The stately palm was bowed and bent, A [okas from the ground were rent, And towering Sáls and light bamboos, And trees with flowers of varied hues, With loveliest creepers wreathed and crowned, Shook, reeled, and fell upon the ground. With mighty engines piles of stone And seated hills were overthrown: Unprisoned waters sprang on high, In rain descending from the sky: And ocean with a roar and swell Heaved wildly when the mountains fell. Then the great bridge of wondrous strength Was built, a hundred leagues in length. Rocks huge as autumn clouds bound fast With cordage from the shore were cast, And fragments of each riven hill, And trees whose flowers adorned them still. Wild was the tumult, loud the din As ponderous rocks went thundering in.
- **Translation**: 

---

