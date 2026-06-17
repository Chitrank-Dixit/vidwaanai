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

### Verse 1 (Ramayan 0.1561)
- **Original**: Canto XVI. Rávan's Speech. 1543 The glittering rain that gems its leaves, But each bright drop remains apart: So is it still with heart and heart. Deceitful as an autumn cloud Which, though its thunderous voice be loud, On the dry earth no torrent sends, Such is the race of faithless friends. No riches of the bloomy spray Will tempt the wandering bee to stay That loves from flower to flower to range; And friends like thee are swift to change. Thou blot upon thy glorious line, If any giant's tongue but thine Had dared to give this base advice, He should not live to shame me twice.” Then just VibhishaG in the heat Of anger started from his seat, And with four captains of the band Sprang forward with his mace in hand; Then, fury flashing from his eye, Looked on the king and made reply: “Thy rights, O RávaG, I allow: My brother and mine elder thou. Such, though from duty's path they stray, We love like fathers and obey, But still too bitter to be borne Is thy harsh speech of cruel scorn. The rash like thee, who spurn control, Nor check one longing of the soul, Urged by malignant fate repel The faithful friend who counsels well. A thousand courtiers wilt thou meet,
- **Translation**: 

---

### Verse 2 (Ramayan 0.1562)
- **Original**: 1544 The Ramayana With flattering lips of smooth deceit: But rare are they whose tongue or ear Will speak the bitter truth, or hear. Unclose thy blinded eyes and see That snares of death encompass thee. I dread, my brother, to behold The shafts of Ráma, bright with gold, Flash fury through the air, and red With fires of vengeance strike thee dead. Lord, brother, King, again reflect, Nor this mine earnest prayer reject, O, save thyself, thy royal town, Thy people and thine old renown.” Canto XVII. Vibhishan's Flight. Soon as his bitter words were said, To Raghu's sons VibhishaG fled.927 Their eyes the Vánar leaders raised And on the air-borne Rákhshas gazed, Bright as a thunderbolt, in size Like Meru's peak that cleaves the skies. In gorgeous panoply arrayed Like Indra's self he stood displayed, And four attendants brave and bold 927 This desertion to the enemy is somewhat abrupt, and is narrated with brevity not usual with Válmíki. In the Bengal recension the preceding speakers and speeches differ considerably from those given in the text which I follow. VibhishaG is kicked from his seat by RávaG, and then, after telling his mother what has happened, he flies to Mount Kailása where he has an interview with Ziva, and by his advice seeks Ráma and the Vánar army.
- **Translation**: 

---

### Verse 3 (Ramayan 0.1563)
- **Original**: Canto XVII. Vibhishan's Flight. 1545 Shone by their chief in mail and gold. Sugríva then with dark surmise Bent on their forms his wondering eyes, And thus in hasty words confessed The anxious doubt that moved his breast: “Look, look ye Vánars, and beware: That giant chief sublime in air With other four in bright array Comes armed to conquer and to slay.” [439] Soon as his warning speech they heard, The Vánar chieftains undeterred Seized fragments of the rock and trees, And made reply in words like these: “We wait thy word: the order give, And these thy foes shall cease to live. Command us, mighty King, and all Lifeless upon the earth shall fall.” Meanwhile VibhishaG with the four Stood high above the ocean shore. Sugríva and the chiefs he spied, And raised his mighty voice and cried: “From RávaG, lord of giants, I His brother, named VibhishaG, fly. From Janasthán he stole the child Of Janak by his art beguiled, And in his palace locked and barred Surrounds her with a Rákshas guard. I bade him, plied with varied lore, His hapless prisoner restore. But he, by Fate to ruin sent, No credence to my counsel lent, Mad as the fevered wretch who sees
- **Translation**: 

---

### Verse 4 (Ramayan 0.1564)
- **Original**: 1546 The Ramayana And scorns the balm to bring him ease. He scorned the sage advice I gave, He spurned me like a base-born slave. I left my children and my wife, And fly to Raghu's son for life. I pray thee, Vánar chieftain, speed To him who saves in hour of need, And tell him famed in distant lands That suppliant here VibhishaG stands.” The Rákshas ceased: Sugríva hied To Raghu's noble son and cried: “A stranger from the giant host, Borne o'er the sea, has reached the coast; A secret foe, he comes to slay, As owls attack their heedless prey. 'Tis thine, O King, in time of need To watch, to counsel, and to lead, Our Vánar legions to dispose, And guard us from our crafty foes. VibhishaG from the giants' isle, King RávaG's brother, comes with guile And, feigning from his king to flee, Seeks refuge, Raghu's son, with thee. Arise, O Ráma, and prevent By bold attack his dark intent. Who comes in friendly guise prepared To slay thee by his arts ensnared.”
- **Translation**: 

---

### Verse 5 (Ramayan 0.1565)
- **Original**: Canto XVII. Vibhishan's Flight. 1547 Thus urged Sugríva famed for lore Of moving words, and spoke no more. Then Ráma thus in turn addressed The bold Hanúmán and the rest: “Chiefs of the Vánar legions each Of you heard Sugríva's speech. What think ye now in time of fear, When peril and distress are near, In every doubt the wise depend For counsel on a faithful friend.” They heard his gracious words, and then Spake reverent to the lord of men: “O Raghu's son, thou knowest well All things of heaven and earth and hell. 'Tis but thy friendship bids us speak The counsel Ráma need not seek. So duteous, brave, and true art thou, Heroic, faithful to thy vow. Deep in the scriptures, trained and tried, Still in thy friends wilt thou confide. Let each of us in turn impart The secret counsel of his heart, And strive to win his chief's assent, By force of wisest argument.” They ceased and Angad thus began: “With jealous eye the stranger scan: Not yet with trusting heart receive VibhishaG, nor his tale believe. These giants wandering far and wide Their evil nature falsely hide, And watching with malignant skill Assail us when we fear no ill.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1566)
- **Original**: 1548 The Ramayana Well ponder every hope and fear Until thy doubtful course be clear; Then own his merit or detect His guile, and welcome or reject.” Then Zarabha the bold and brave In turn his prudent sentence gave: “Yea, Ráma, send a skilful spy With keenest tact to test and try. Then let the stranger, as is just, Obtain or be refused thy trust.” Then he whose heart was rich in store Of scripture's life-directing lore, King Jámbaván, stood forth and cried: “Suspect, suspect a foe allied With RávaG lord of Lanká's isle, And Rákshas sin and Rákshas guile.” Then Mainda, wisest chief, who knew The wrong, the right, the false, the true, Pondered a while, then silence broke, And thus his sober counsel spoke: “Let one with gracious speech draw near And gently charm VibhishaG's ear, Till he the soothing witchery feel And all his secret heart reveal. So thou his aims and hopes shalt know, And hail the friend or shun the foe.”
- **Translation**: 

---

### Verse 7 (Ramayan 0.1567)
- **Original**: Canto XVII. Vibhishan's Flight. 1549 “Not he,” Hanúmán cried,“not he Who taught the Gods928 may rival thee, Supreme in power of quickest sense, First in the art of eloquence. But hear me soothly speak, O King, And learn the hope to which I cling. VibhishaG comes no crafty spy: Urged by his brother's fault to fly. With righteous soul that loathes the sin, He fled from Lanká and his kin. [440] If strangers question, doubt will rise And chill the heart of one so wise. Marred by distrust the parle will end, And thou wilt lose a faithful friend. Nor let it seem so light a thing To sound a stranger's heart, O King. And he, I ween, whate'er he say, Will ne'er an evil thought betray. He comes a friend in happy time, Loathing his brother for his crime. His ear has heard thine old renown, The might that struck King Báli down, And set Sugríva on the throne. And looking now to thee alone He comes thy matchless aid to win And punish RávaG for his sin. Thus have I tried thy heart to move, And thus VibhishaG's truth to prove. Still in his friendship I confide; But ponder, wisest, and decide.” 928 V [ihaspati the preceptor of the Gods.
- **Translation**: 

---

### Verse 8 (Ramayan 0.1568)
- **Original**: 1550 The Ramayana Canto XVIII. Ráma's Speech. Then Ráma's rising doubt was stilled, And friendly thoughts his bosom filled. Thus, deep in Scripture's lore, he spake: “The suppliant will I ne'er forsake, Nor my protecting aid refuse When one in name of friendship sues. Though faults and folly blot his fame, Pity and help he still may claim.” He ceased: Sugríva bowed his head And pondered for a while, and said: “Past number be his faults or few, What think ye of the Rákshas who, When threatening clouds of danger rise, Deserts his brother's side and flies? Say, Vánars, who may hope to find True friendship in his faithless kind?”
- **Translation**: 

---

### Verse 9 (Ramayan 0.1569)
- **Original**: Canto XVIII. Ráma's Speech. 1551 The son of Raghu heard his speech: He cast a hasty look on each Of those brave Vánar chiefs, and while Upon his lips there played a smile, To LakshmaG turned and thus expressed The thoughts that moved his gallant breast: “Well versed in Scripture's lore, and sage And duly reverent to age, Is he, with long experience stored, Who counsels like this Vánar lord. Yet here, methinks, for searching eyes Some deeper, subtler matter lies. To you and all the world are known The perils of a monarch's throne, While foe and stranger, kith and kin By his misfortune trust to win. By hope of such advantage led, VibhishaG o'er the sea has fled. He in his brother's stead would reign, And our alliance seeks to gain; And we his offer may embrace, A stranger and of alien race. But if he comes a spy and foe, What power has he to strike a blow In furtherance of his close design? What is his strength compared with mine? And can I, Vánar King, forget The great, the universal debt, Ever to aid and welcome those Who pray for shelter, friends or foes? Hast thou not heard the deathless praise Won by the dove in olden days, Who conquering his fear and hate Welcomed the slayer of his mate,
- **Translation**: 

---

### Verse 10 (Ramayan 0.1570)
- **Original**: 1552 The Ramayana And gave a banquet, to refresh The weary fowler, of his flesh? Now hear me, Vánar King, rehearse What KaGdu929 spoke in ancient verse, Saint KaGva's son who loved the truth And clave to virtue from his youth: “Strike not the suppliant when he stands And asks thee with beseeching hands For shelter: strike him not although He were thy father's mortal foe. No, yield him, be he proud or meek, The shelter which he comes to seek, And save thy foeman, if the deed Should cost thy life, in desperate need.” And shall I hear the wretched cry, And my protecting aid deny? Shall I a suppliant's prayer refuse, And heaven and glory basely lose? No, I will do for honour sake E'en as the holy KaGdu spake, Preserve a hero's name from stain, And bliss in heaven and glory gain. Bound by a solemn vow I sware That all my saving help should share Who sought me in distress and cried, “Thou art my hope, and none beside.” Then go, I pray thee, Vánar King, VibhishaG to my presence bring, Yea, were he RávaG's self, my vow Forbids me to reject him now.” 929 In Book II, Canto XXI, KaGdu is mentioned by Ráma as an example of filial obedience. At the command of his father he is said to have killed a cow.
- **Translation**: 

---

### Verse 11 (Ramayan 0.1571)
- **Original**: Canto XIX. Vibhishan's Counsel. 1553 He ceased: the Vánar king approved; And Ráma toward VibhishaG moved. So moves, a brother God to greet, Lord Indra from his heavenly seat. [441] Canto XIX. Vibhishan's Counsel. When Raghu's son had owned his claim Down from the air VibhishaG came, And with his four attendants bent At Ráma's feet most reverent. “O Ráma,” thus he cried,“in me VibhishaG, RávaG's brother see. By him disgraced thine aid I seek, Sure refuge of the poor and weak. From Lanká, friends, and wealth I fly, And reft of all on thee rely. On thee, the wretch's firmest friend, My kingdom, joys, and life depend.” With glance of favour Ráma eyed The Rákshas chief and thus replied: “First from thy lips I fain would hear Each brighter hope, each darker fear. Speak, stranger, that I well may know The strength and weakness of the foe.”
- **Translation**: 

---

### Verse 12 (Ramayan 0.1572)
- **Original**: 1554 The Ramayana He ceased: the Rákshas chief obeyed, And thus in turn his answer made: “O Prince, the Self-existent gave This boon to RávaG; he may brave All foes in fight; no fiend or snake, Gandharva, God, his life may take. His brother KumbhakarGa vies In might with him who rules the skies. The captain of his armies— fame Perhaps has taught the warrior's name— Is terrible Prahasta, who King MaGibhadra's930 self o'erthrew. Where is the warrior found to face Young Indrajít, when armed with brace And guard931 and bow he stands in mail And laughs at spear and arrowy hail? Within his city Lanká dwell Ten million giants fierce and fell, Who wear each varied shape at will And eat the flesh of those they kill. These hosts against the Gods he led, And heavenly might discomfited.” Then Ráma cried:“I little heed Gigantic strength or doughty deed. In spite of all their might has done The king, the captain, and the son Shall fall beneath my fury dead, And thou shalt reign in RávaG's stead. He, though in depths of earth he dwell, 930 A King of the Yakshas, or Kuvera himself, the God of Gold. 931 The brace protects the left arm from injury from the bow-string, and the guard protects the fingers of the right hand.
- **Translation**: 

---

### Verse 13 (Ramayan 0.1573)
- **Original**: Canto XIX. Vibhishan's Counsel. 1555 Or seek protection down in hell, Or kneel before the Sire supreme, His forfeit life shall ne'er redeem. Yea, by my brothers' lives I swear, I will not to my home repair Till RávaG and his kith and kin Have paid in death the price of sin.” VibhishaG bowed his head and cried: “Thy conquering army will I guide To storm the city of the foe, And aid the tyrant's overthrow.” Thus spake VibhishaG: Ráma pressed The Rákshas chieftain to his breast, And cried to LakshmaG:“Haste and bring Sea-water for the new-made king.” He spoke, and o'er VibhishaG's head The consecrating drops were shed Mid shouts that hailed with one accord The giants' king and Lanká's lord. “Is there no way,” Hanúmán cried, “No passage o'er the boisterous tide? How may we lead the Vánar host In triumph to the farther coast?” “Thus,” said VibhishaG,“I advise: Let Raghu's son in suppliant guise Entreat the mighty Sea to lend His succour and this cause befriend. His channels, as the wise have told, By Sagar's sons were dug of old,932 Nor will high-thoughted Ocean scorn A prince of Sagar's lineage born.” 932 The story is told in Book I, Cantos XL, XLI, XLII.
- **Translation**: 

---

### Verse 14 (Ramayan 0.1574)
- **Original**: 1556 The Ramayana He ceased; the prudent counsel won The glad assent of Raghu's son. Then on the ocean shore a bed Of tender sacred grass was spread, Where Ráma at the close of day Like fire upon an altar lay. Canto XX. The Spies. Zárdúla, RávaG's spy, surveyed The legions on the strand arrayed. And bore, his bosom racked with fear, These tidings to the monarch's ear: “They come, they come. A rushing tide, Ten leagues they spread from side to side, And on to storm thy city press, Fierce rovers of the wilderness. Rich in each princely power and grace, The pride of Da[aratha's race, Ráma and LakshmaG lead their bands, And halt them on the ocean sands. O Monarch, rise, this peril meet; Risk not the danger of defeat.[442]
- **Translation**: 

---

### Verse 15 (Ramayan 0.1575)
- **Original**: Canto XX. The Spies. 1557 First let each wiser art be tried; Bribe them, or win them, or divide.” Such was the counsel of the spy: And RávaG called toZuka:“Fly, Sugríva lord of Vánars seek, And thus my kingly message speak: “Great power and might and fame are thine, Brave scion of a royal line, King Riksharajas' son, in thee A brother and a friend I see. How wronged by me canst thou complain? What profit here pretend to gain? If from the wood the wife I stole Of Ráma of the prudent soul, What cause hast thou to mourn the theft? Thou art not injured or bereft. Return, O King, thy steps retrace And seek thy mountain dwelling-place. No, never may thy hosts within My Lanká's walls a footing win. A mighty town whose strength defies The gathered armies of the skies.” He ceased: obedientZuka heard; With wings and plumage of a bird He rose in eager speed and through The air upon his errand flew. Borne o'er the sea with rapid wing He stood above the Vánar king, And spoke aloud, sublime in air, The message he was charged to bear. The Vánar heard the words he spoke, And quick redoubling stroke on stroke On head and pinions hemmed him round
- **Translation**: 

---

### Verse 16 (Ramayan 0.1576)
- **Original**: 1558 The Ramayana And bore him struggling to the ground. The Rákshas wounded and distressed These words to Raghu's son addressed: “Quick, quick! This Vánar host restrain, For heralds never must be slain. To him alone, a wretch untrue, The punishment of death is due Who leaves his master's speech unsaid And speaks another in its stead.” Moved by the suppliant speech and prayer Up sprang the prince and cried, forbear. Saved from his wild assailant's blows Again the Rákshas herald rose And borne on light wings to the sky Addressed Sugríva from on high: “O Vánar Monarch, chief endued With power and wonderous fortitude, What answer is my king, the fear And scourge of weeping worlds, to hear?” “Go tell thy lord,” Sugríva cried, “Thou, Ráma's foe, art thus defied. His arm the guilty Báli slew; Thus, tyrant, shalt thou perish too. Thy sons, thy friends, proud King, and all Thy kith and kin with thee shall fall; And, emptied of the giant's brood, Burnt Lanká be a solitude. Fly to the Sun-God's pathway, go And hide thee deep in hell below: In vain from Ráma shalt thou flee Though heavenly warriors fight for thee. Thine arm subdued, securely bold, The Vulture-king infirm and old:
- **Translation**: 

---

### Verse 17 (Ramayan 0.1577)
- **Original**: Canto XX. The Spies. 1559 But will thy puny strength avail When Raghu's wrathful sons assail? A captive in thy palace lies The lady of the lotus eyes: Thou knowest not how fierce and strong Is he whom thou hast dared to wrong. The best of Raghu's lineage, he Whose conquering hand shall punish thee.” He ceased: and Angad raised a cry; “This is no herald but a spy. Above thee from his airy post His rapid eye surveyed our host, Where with advantage he might scan Our gathered strength from rear to van. Bind him, Vánars, bind the spy, Nor let him back to Lanká fly.” They hurled the Rákshas to the ground, They grasped his neck, his pinions bound, And firmly held him while in vain His voice was lifted to complain. But Ráma's heart inclined to spare, He listened to his plaint and prayer, And cried aloud:“O Vánars, cease; The captive from his bonds release.”
- **Translation**: 

---

### Verse 18 (Ramayan 0.1578)
- **Original**: 1560 The Ramayana Canto XXI. Ocean Threatened. His hands in reverence Ráma raised And southward o'er the ocean gazed; Then on the sacred grass that made His lowly couch his limbs he laid. His head on that strong arm reclined Which Sítá, best of womankind, Had loved in happier days to hold With soft arms decked with pearls and gold. Then rising from his bed of grass, “This day,” he cried,“the host shall pass Triumphant to the southern shore, Or Ocean's self shall be no more.” Thus vowing in his constant breast Again he turned him to his rest, And there, his eyes in slumber closed, Silent beside the sea reposed. Thrice rose the Day-God thrice he set, The lord of Ocean came not yet, Thrice came the night, but Raghu's son No answer by his service won. To LakshmaG thus the hero cried, His eyes aflame with wrath and pride: “In vain the softer gifts that grace The good are offered to the base. Long-suffering, patience, gentle speech[443]
- **Translation**: 

---

### Verse 19 (Ramayan 0.1579)
- **Original**: Canto XXI. Ocean Threatened. 1561 Their thankless hearts can never reach. The world to him its honour pays Whose ready tongue himself can praise, Who scorns the true, and hates the right, Whose hand is ever raised to smite. Each milder art is tried in vain: It wins no glory, but disdain. And victory owns no softer charm Than might which nerves a warrior's arm. My humble suit is still denied By Ocean's overweening pride. This day the monsters of the deep In throes of death shall wildly leap. My shafts shall rend the serpents curled In caverns of the watery world, Disclose each sunless depth and bare The tangled pearl and coral there. Away with mercy! at a time Like this compassion is a crime. Welcome, the battle and the foe! My bow! my arrows and my bow! This day the Vánars' feet shall tread The conquered Sea's exhausted bed, And he who never feared before Shall tremble to his farthest shore.” Red flashed his eyes with angry glow: He stood and grasped his mighty bow, Terrific as the fire of doom Whose quenchless flames the world consume. His clanging cord the archer drew, And swift the fiery arrows flew Fierce as the flashing levin sent By him who rules the firmament.
- **Translation**: 

---

### Verse 20 (Ramayan 0.1580)
- **Original**: 1562 The Ramayana Down through the startled waters sped Each missile with its flaming head. The foamy billows rose and sank, And dashed upon the trembling bank. Sea monsters of tremendous form With crash and roar of thunder storm. Still the wild waters rose and fell Crowned with white foam and pearl and shell. Each serpent, startled from his rest, Raised his fierce eyes and glowing crest. And prisoned Dánavs933 where they dwelt In depths below the terror felt. Again upon his string he laid A flaming shaft, but LakshmaG stayed His arm, with gentle reasoning tried To soothe his angry mood, and cried: “Brother, reflect: the wise control The rising passions of the soul. Let Ocean grant, without thy threat, The boon on which thy heart is set. That gracious lord will ne'er refuse When Ráma son of Raghu sues.” He ceased: and voices from the air Fell clear and loud, Spare, Ráma, spare. Canto XXII. Ocean Threatened. 933 Fiends and enemies of the Gods.
- **Translation**: 

---

