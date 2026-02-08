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

### Verse 1 (Ramayan 0.1541)
- **Original**: Canto VIII. Prahasta's Speech. 1523 “Why waste a thought on one so vile As Hanúmán the Vánar, while Sugríva, LakshmaG, yet remain, And Ráma mightier still, unslain? This mace to-day shall crush the three, And all the host will turn and flee. Listen, and I will speak: incline, O King, to hear these words of mine, For the deep plan that I propose Will swiftly rid thee of thy foes. Let thousands of thy host assume The forms of men in youthful bloom, In war's magnificent array Draw near to Raghu's son, and say: “Thy younger brother Bharat sends This army, and thy cause befriends.” Then let our legions hasten near With bow and mace and sword and spear, And on the Vánar army rain Our steel and stone till all be slain. If Raghu's sons will fain believe, Entangled in the net we weave, The penalty they both must pay, And lose their forfeit lives to-day.” [433] Then with his warrior soul on fire, Nikumbha spoke in burning ire: “I, only I, will take the field, And Raghu's son his life shall yield. Within these walls, O Chiefs, abide, Nor part ye from our monarch's side.”
- **Translation**: 

---

### Verse 2 (Ramayan 0.1542)
- **Original**: 1524 The Ramayana Canto IX. Vibhishan's Counsel. A score of warriors914 forward sprang, And loud the clashing iron rang Of mace and axe and spear and sword, As thus they spake unto their lord: “Their king Sugríva will we slay, And Raghu's sons, ere close of day, And strike the wretch Hanúmán down, The spoiler of our golden town.” But sage VibhishaG strove to calm The chieftains' fury; palm to palm He joined in lowly reverence, pressed915 Before them, and the throng addressed: 914 Their names are Nikumbha, Rabhasa, Súrya[atru, Suptaghna, Yajnakopa, Mahápár[va, Mahodara, Agniketu, Ra[miketu, Durdharsha, Indra[atru, Pra- hasta, Virúpáksha, Vajradanshmra, Dhúmráksha, Durmukha, Mahábala. 915 Similarly Antenor urges the restoration of Helen: “Let Sparta's treasures be this hour restored, And Argive Helen own her ancient lord. As this advice ye practise or reject, So hope success, or dread the dire effect,” POPE 'S{FNS Homer's Iliad, Book VII.
- **Translation**: 

---

### Verse 3 (Ramayan 0.1543)
- **Original**: Canto IX. Vibhishan's Counsel. 1525 “Dismiss the hope of conquering one So stern and strong as Raghu's son. In due control each sense he keeps With constant care that never sleeps. Whose daring heart has e'er conceived The exploit Hanumán achieved, Across the fearful sea to spring, The tributary rivers' king? O Rákshas lords, in time be wise, Nor Ráma's matchless power despise. And say, what evil had the son Of Raghu to our monarch done, Who stole the dame he loved so well And keeps her in his citadel; If Khara in his foolish pride Encountered Ráma, fought, and died, May not the meanest love his life And guard it in the deadly strife? The Maithil dame, O Rákshas King, Sore peril to thy realm will bring. Restore her while there yet is time, Nor let us perish for thy crime. O, let the Maithil lady go Ere the avenger bend his bow To ruin with his arrowy showers Our Lanká with her gates and towers. Let Janak's child again be free Ere the wild Vánars cross the sea, In their resistless might assail Our city and her ramparts scale. Ah, I conjure thee by the ties Of brotherhood, be just and wise. In all my thoughts thy good I seek, And thus my prudent counsel speak.
- **Translation**: 

---

### Verse 4 (Ramayan 0.1544)
- **Original**: 1526 The Ramayana Let captive Sítá be restored Ere, fierce as autumn's sun, her lord Send his keen arrows from the string To drink the life-blood of our king. This fury from thy soul dismiss, The bane of duty, peace, and bliss. Seek duty's path and walk therein, And joy and endless glory win. Restore the captive, ere we feel The piercing point of Ráma's steel. O spare thy city, spare the lives Of us, our friends, our sons and wives.” Thus spake VibhishaG wise and brave: The Rákshas king no answer gave, But bade his lords the council close, And sought his chamber for repose. Canto X. Vibhishan's Counsel. Soon as the light of morning broke, VibhishaG from his slumber woke, And, duty guiding every thought, The palace of his brother sought. Vast as a towering hill that shows His peaks afar, that palace rose. Here stood within the monarch's gate Sage nobles skilful in debate. There strayed in glittering raiment through The courts his royal retinue, Where in wild measure rose and fell
- **Translation**: 

---

### Verse 5 (Ramayan 0.1545)
- **Original**: Canto X. Vibhishan's Counsel. 1527 The music of the drum and shell, And talk grew loud, and many a dame Of fairest feature went and came Through doors a marvel to behold, With pearl inlaid on burning gold: Therein Gandharvas or the fleet Lords of the storm might joy to meet. He passed within the wondrous pile, Chief glory of the giants' isle: Thus, ere his fiery course be done, An autumn cloud admits the sun. [434] He heard auspicious voices raise With loud accord the note of praise, And sages, deep in Scripture, sing Each glorious triumph of the king. He saw the priests in order stand, Curd, oil, in every sacred hand; And by them flowers were laid and grain, Due offerings to the holy train. VibhishaG to the monarch bowed, Raised on a throne above the crowd: Then, skilled in arts of soft address, He raised his voice the king to bless, And sate him on a seat where he Full in his brother's sight should be. The chieftain there, while none could hear, Spoke his true speech for RávaG's ear, And to his words of wisdom lent The force of weightiest argument: “O brother, hear! since Ráma's queen A captive in thy house has been, Disastrous omens day by day Have struck our souls with wild dismay.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1546)
- **Original**: 1528 The Ramayana No longer still and strong and clear The flames of sacrifice appear, But, restless with the frequent spark, Neath clouds of smoke grow faint and dark. Our ministering priests turn pale To see their wonted offerings fail, And ants and serpents creep and crawl Within the consecrated hall.916 Dried are the udders of our cows, Our elephants have juiceless brows,917 Nor can the sweetest pasture stay The charger's long unquiet neigh. Big tears from mules and camels flow Whose staring coats their trouble show, Nor can the leech's art restore Their health and vigour as before. Rapacious birds are fierce and bold: Not single hunters as of old, In banded troops they chase the prey, Or gathering on our temples stay. Through twilight hours with shriek and howl Around the city jackals prowl, And wolves and foul hyænas wait Athirst for blood at every gate. One sole atonement still may cure These evils, and our weal assure. Restore the Maithil dame, and win An easy pardon for thy sin.” 916 The Agnisáláor room where the sacrificial fire was kept. 917 The exudation of a fragrant fluid from the male elephant's temples, espe- cially at certain seasons, is frequently spoken of in Sanskrit poetry. It is said to deceive and attract the bees, and is regarded as a sign of health and masculine vigour.
- **Translation**: 

---

### Verse 7 (Ramayan 0.1547)
- **Original**: Canto XI. The Summons. 1529 The Rákshas monarch heard, and moved To sudden wrath his speech reproved: “No danger, brother, can I see: The Maithil dame I will not free. Though all the Gods for Ráma fight, He yields to my superior might.” Thus the tremendous king who broke The ranks of heavenly warriors spoke, And, sternly purposed to resist, His brother from the hall dismissed. Canto XI. The Summons. Still RávaG's haughty heart rebelled, The counsel of the wise repelled, And, as his breast with passion burned, His thoughts again to Sítá turned. Thus, to each sign of danger blind, To love and war he still inclined. Then mounted he his car that glowed With gems and golden net, and rode Where, gathered at the monarch's call, The nobles filled the council hall. A host of warriors bright and gay With coloured robes and rich array, With shield and mace and spear and sword, Followed the chariot of their lord. Mid the loud voice of shells and beat Of drums he raced along the street, And, ere he came, was heard afar
- **Translation**: 

---

### Verse 8 (Ramayan 0.1548)
- **Original**: 1530 The Ramayana The rolling thunder of his car. He reached the doors: the nobles bent Their heads before him reverent: And, welcomed with their loud acclaim, Within the glorious hall he came. He sat upon a royal seat With golden steps beneath his feet, And bade the heralds summon all His captains to the council hall. The heralds heard the words he spake, And sped from house to house to wake The giants where they slept or spent The careless hours in merriment. These heard the summons and obeyed: From chamber, grove, and colonnade, On elephants or cars they rode, Or through the streets impatient strode. As birds on rustling pinions fly Through regions of the darkened sky, Thus cars and mettled coursers through The crowded streets of Lanká flew. The council hall was reached, and then, As lions seek their mountain den, Through massy doors that opened wide, With martial stalk the captains hied. Welcomed with honour as was meet They stooped to press their monarch's feet,[435] And each a place in order found On stool, on cushion, or the ground. Nor did the sage VibhishaG long Delay to join the noble throng. High on a car that shone like flame With gold and flashing gems he came, Drew near and spoke his name aloud,
- **Translation**: 

---

### Verse 9 (Ramayan 0.1549)
- **Original**: Canto XII. Rávan's Speech. 1531 And reverent to his brother bowed. Canto XII. Rávan's Speech. The king in counsel unsurpassed His eye around the synod cast, And fierce Prahasta, first and best Of all his captains, thus addressed: “Brave master of each warlike art, Arouse thee and perform thy part. Array thy fourfold forces918 well To guard our isle and citadel.” The captain of the hosts obeyed, The troops with prudent skill arrayed; Then to the hall again he hied, And stood before the king and cried: “Each inlet to the town is closed Without, within, are troops disposed. With fearless heart thine aim pursue And do the deed thou hast in view.” 918 Consisting of warriors on elephants, warriors in chariots, charioteers, and infantry.
- **Translation**: 

---

### Verse 10 (Ramayan 0.1550)
- **Original**: 1532 The Ramayana Thus spoke Prahasta in the zeal That moved him for the kingdom's weal. And thus the monarch, who pursued His own delight, his speech renewed: “In ease and bliss, in toil and pain, In doubts of duty, pleasure, gain, Your proper path I need not tell, For of yourselves ye know it well. The Storm-Gods, Moon, and planets bring New glory to their heavenly king,919 And, ranged about your monarch, ye Give joy and endless fame to me. My secret counsel have I kept, While senseless KumbhakarGa slept. Six months the warrior's slumbers last And bind his torpid senses fast; But now his deep repose he breaks, The best of all our champions wakes. I captured, Ráma's heart to wring, This daughter of Videha's king. And brought her from that distant land920 Where wandered many a Rákshas band. Disdainful still my love she spurns, Still from each prayer and offering turns, Yet in all lands beneath the sun No dame may rival Sítá, none, Her dainty waist is round and slight, Her cheek like autumn's moon is bright, And she like fruit in graven gold Mocks her921 whom Maya framed of old. 919 Indra, generally represented as surrounded by the Maruts or Storm-Gods. 920 Janasthán, where Ráma lived as an ascetic. 921 Máyá, regarded as the paragon of female beauty, was the creation of Maya the chief artificer of the Daityas or Dánavs.
- **Translation**: 

---

### Verse 11 (Ramayan 0.1551)
- **Original**: Canto XII. Rávan's Speech. 1533 Faultless in form, how firmly tread Her feet whose soles are rosy red! Ah, as I gaze her beauty takes My spirit, and my passion wakes. Looking for Ráma far away She sought with tears a year's delay Nor gazing on her love-lit eye Could I that earnest prayer deny. But baffled hopes and vain desire At length my patient spirit tire. How shall the sons of Raghu sweep To vengeance o'er the pathless deep? How shall they lead the Vánar train Across the monster-teeming main? One Vánar yet could find a way To Lanká's town, and burn and slay. Take counsel then, remembering still That we from men need fear no ill; And give your sentence in debate, For matchless is the power of fate. Assailed by you the Gods who dwell In heaven beneath our fury fell. And shall we fear these creatures bred In forests, by Sugríva led? E'en now on ocean's farther strand, The sons of Da[aratha stand, And follow, burning to attack Their giant foes, on Sítá's track. Consult then, lords for ye are wise: A seasonable plan devise. The captive lady to retain, And triumph when the foes are slain. No power can bring across the foam Those Vánars to our island home;
- **Translation**: 

---

### Verse 12 (Ramayan 0.1552)
- **Original**: 1534 The Ramayana Or if they madly will defy Our conquering might, they needs must die.” Then KumbhakarGa's anger woke, And wroth at RávaG's words he spoke: “O Monarch, when thy ravished eyes First looked upon thy lovely prize, Then was the time to bid us scan Each peril and mature a plan. Blest is the king who acts with heed, And ne'er repents one hasty deed; And hapless he whose troubled soul Mourns over days beyond control.[436] Thou hast, in beauty's toils ensnared, A desperate deed of boldness dared; By fortune saved ere Ráma's steel One wound, thy mortal bane, could deal. But, RávaG, as the deed is done, The toil of war I will not shun. This arm, O rover of the night, Thy foemen to the earth shall smite, Though Indra with the Lord of Flame, The Sun and Storms, against me came. E'en Indra, monarch of the skies, Would dread my club and mountain size, Shrink from these teeth and quake to hear The thunders of my voice of fear. No second dart shall Ráma cast: The first he aims shall be the last. He falls, and these dry lips shall drain The blood of him my hand has slain; And Sítá, when her champion dies, Shall be thine undisputed prize.”
- **Translation**: 

---

### Verse 13 (Ramayan 0.1553)
- **Original**: Canto XIII. Rávan's Speech. 1535 Canto XIII. Rávan's Speech. But Mahápár[va saw the sting Of keen reproach had galled the king; And humbly, eager to appease His anger, spoke in words like these: “And breathes there one so cold and weak The forest and the gloom to seek Where savage beasts abound, and spare To taste the luscious honey there? Art thou not lord? and who is he Shall venture to give laws to thee? Love thy Videhan still, and tread Upon thy prostrate foeman's head. O'er Sítá's will let thine prevail, And strength achieve if flattery fail. What though the lady yet be coy And turn her from the proffered joy? Soon shall her conquered heart relent And yield to love and blandishment. With us let KumbhakarGa fight, And Indrajít of matchless might: We need not other champions, they Shall lead us forth to rout and slay. Not ours to bribe or soothe or part The foeman's force with gentle art, Doomed, conquered by our might, to feel The vengeance of the warrior's steel.” The Rákshas monarch heard, and moved By flattering hopes the speech approved:
- **Translation**: 

---

### Verse 14 (Ramayan 0.1554)
- **Original**: 1536 The Ramayana “Hear me,” he cried,“great chieftain, tell What in the olden time befell,— A secret tale which, long suppressed, Lies prisoned only in my breast. One day— a day I never forget— Fair Punjikasthalá922 I met, When, radiant as a flame of fire, She sought the palace of the Sire. In passion's eager grasp I tore From her sweet limbs the robes she wore, And heedless of her prayers and cries Strained to my breast the vanquised prize. Like Naliní923 with soil distained, The mansion of the Sire she gained, And weeping made the outrage known To Brahmá on his heavenly throne. He in his wrath pronounced a curse,— That lord who made the universe: “If, RávaG, thou a second time Be guilty of so foul a crime, Thy head in shivers shall be rent: Be warned, and dread the punishment.” Awed by the threat of vengeance still I force not Sítá's stubborn will. Terrific as the sea in might: My steps are like the Storm-Gods' flight; But Ráma knows not this, or he Had never sought to war with me. Where is the man would idly brave The lion in his mountain cave, And wake him when with slumbering eyes Grim, terrible as Death, he lies? 922 One of the Nymphs of Indra's heaven. 923 The Lotus River, a branch of the heavenly Gangá.
- **Translation**: 

---

### Verse 15 (Ramayan 0.1555)
- **Original**: Canto XIV. Vibhishan's Speech. 1537 No, blinded Ráma knows me not: Ne'er has he seen mine arrows shot; Ne'er marked them speeding to their aim Like snakes with cloven tongues of flame. On him those arrows will I turn, Whose fiery points shall rend and burn. Quenched by my power when I assail The glory of his might shall fail, As stars before the sun grow dim And yield their feeble light to him.” Canto XIV. Vibhishan's Speech. He ceased: VibhishaG ill at ease Addressed the king in words like these: “O RávaG, O my lord, beware Of Sítá dangerous as fair, Nor on thy heedless bosom hang This serpent with a deadly fang. O King, the Maithil dame restore To Raghu's matchless son before Those warriors of the woodlands, vast As mountain peaks, approaching fast, Armed with fierce teeth and claws, enclose Thy city with unsparing foes. O, be the Maithil dame restored Ere loosened from the clanging cord [437]
- **Translation**: 

---

### Verse 16 (Ramayan 0.1556)
- **Original**: 1538 The Ramayana The vengeful shafts of Ráma fly, And low in death thy princes lie. In all thy legions hast thou one A match in war for Raghu's son? Can KumbhakarGa's self withstand, Or Indrajít, that mighty hand? In vain with Ráma wilt thou strive: Thou wilt not save thy soul alive Though guarded by the Lord of Day And Storm-Gods' terrible array, In vain to Indra wilt thou fly, Or seek protection in the sky, In Yáma's gloomy mansion dwell, Or hide thee in the depths of hell.” He ceased; and when his lips were closed Prahasta thus his rede opposed: “O timid heart, to counsel thus! What terrors have the Gods for us? Can snake, Gandharva, fiend appal The giants' sons who scorn them all? And shall we now our birth disgrace, And dread a king of human race?” Thus fierce Prahasta counselled ill: But sage VibhishaG's constant will The safety of the realm ensued; Who thus in turn his speech renewed:
- **Translation**: 

---

### Verse 17 (Ramayan 0.1557)
- **Original**: Canto XV. Indrajít's Speech. 1539 “Yes, when a soul defiled with sin Shall mount to heaven and enter in, Then, chieftain, will experience teach The truth of thy disdainful speech. Can I, or thou, or these or all Our bravest compass Ráma's fall, The chief in whom all virtues shine, The pride of old Ikshváku'a line, With whom the Gods may scarce compare In skill to act, in heart to dare? Yea, idly mayst thou vaunt thee, till Sharp arrows winged with matchless skill From Ráma's bowstring, fleet and fierce As lightning's flame, thy body pierce. Nikumbha shall not save thee then, Nor RávaG, from the lord of men. O Monarch, hear my last appeal, My counsel for thy kingdom's weal. This sentence I again declare: O giant King, beware, beware! Save from the ruin that impends Thy town, thy people, and thy friends; O hear the warning urged once more: To Raghu's son the dame restore.” Canto XV. Indrajít's Speech. He ceased: and Indrajít the pride Of Rákshas warriors thus replied:
- **Translation**: 

---

### Verse 18 (Ramayan 0.1558)
- **Original**: 1540 The Ramayana “Is this a speech our king should hear, This counsel of ignoble fear? A scion of our glorious race Should ne'er conceive a thought so base, But one mid all our kin we find, VibhishaG, whose degenerate mind No spark of gallant pride retains, Whose coward soul his lineage stains. Against one giant what can two Unhappy sons of Raghu do? Away with idle fears, away! Matched with our meanest, what are they? Beneath my conquering prowess fell The Lord of earth and heaven and hell.924 Through every startled region dread Of my resistless fury spread; And Gods in each remotest sphere Confessed the universal fear. Rending the air with roar and groan, Airávat925 to the earth was thrown. From his huge head the tusks I drew, And smote the Gods with fear anew. Shall I who tame celestials' pride, By whom the fiends are terrified, Now prove a weakling little worth, And fail to slay those sons of earth?” He ceased: VibhishaG trained and tried In war and counsel thus replied 924 Trilokanátha, Lord of the Three Worlds, is a title of Indra. 925 The celestial elephant that carries Indra.
- **Translation**: 

---

### Verse 19 (Ramayan 0.1559)
- **Original**: Canto XVI. Rávan's Speech. 1541 “Thy speech is marked with scorn of truth, With rashness and the pride of youth. Yea, to thy ruin like a child Thou pratest, and thy words are wild. Most dear, O Indrajít, to thee Should RávaG's weal and safety be, For thou art called his son, but thou Art proved his direst foeman now, When warned by me thou hast not tried To turn the coming woe aside. Both thee and him 'twere meet to slay, Who brought thee to this hall to-day, And dared so rash a youth admit To council where the wisest sit. Presumptuous, wild, devoid of sense, Filled full of pride and insolence, Thy reckless tongue thou wilt not rule That speaks the counsel of a fool. Who in the fight may brook or shun The arrows shot by Raghu's son With flame and fiery vengeance sped, Dire as his staff who rules the dead? O RávaG, let thy people live, And to the son of Raghu give Fair robes and gems and precious ore, And Sítá to his arms restore.” [438] Canto XVI. Rávan's Speech.
- **Translation**: 

---

### Verse 20 (Ramayan 0.1560)
- **Original**: 1542 The Ramayana Then, while his breast with fury swelled, Thus RávaG spoke, as fate impelled: “Better with foes thy dwelling make, Or house thee with the venomed snake, Than live with false familiar friends Who further still thy foeman's ends. I know their treacherous mood, I know Their secret triumph at thy woe. They in their inward hearts despise The brave, the noble, and the wise, Grieve at their bliss with rancorous hate, And for their sorrows watch and wait: Scan every fault with curious eye, And each slight error magnify. Ask elephants who roam the wild How were their captive friends beguiled. “For fire,” they cry,“we little care, For javelin and shaft and snare: Our foes are traitors, taught to bind The trusting creatures of their kind.” Still, still, shall blessings flow from cows,926 And Bráhmans love their rigorous vows; Still woman change her restless will, And friends perfidious work us ill. What though with conquering feet I tread On every prostrate foeman's head; What though the worlds in abject fear Their mighty lord in me revere? This thought my peace of mind destroys And robs me of expected joys. The lotus of the lake receives 926 As producers of theghi, clarified butter or sacrificial oil, used in fire-offer- ings.
- **Translation**: 

---

