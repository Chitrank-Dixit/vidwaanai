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

### Verse 1 (Ramayana 0.1546)
- **Original**: 1528 The Ramayana No longer still and strong and clear The flames of sacrifice appear, But, restless with the frequent spark, Neath clouds of smoke grow faint and dark. Our ministering priests turn pale To see their wonted offerings fail, And ants and serpents creep and crawl Within the consecrated hall.916 Dried are the udders of our cows, Our elephants have juiceless brows,917 Nor can the sweetest pasture stay The charger's long unquiet neigh. Big tears from mules and camels flow Whose staring coats their trouble show, Nor can the leech's art restore Their health and vigour as before. Rapacious birds are fierce and bold: Not single hunters as of old, In banded troops they chase the prey, Or gathering on our temples stay. Through twilight hours with shriek and howl Around the city jackals prowl, And wolves and foul hyænas wait Athirst for blood at every gate. One sole atonement still may cure These evils, and our weal assure. Restore the Maithil dame, and win An easy pardon for thy sin.” 916 The Agnisáláor room where the sacrificial fire was kept. 917 The exudation of a fragrant fluid from the male elephant's temples, espe- cially at certain seasons, is frequently spoken of in Sanskrit poetry. It is said to deceive and attract the bees, and is regarded as a sign of health and masculine vigour.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1547)
- **Original**: Canto XI. The Summons. 1529 The Rákshas monarch heard, and moved To sudden wrath his speech reproved: “No danger, brother, can I see: The Maithil dame I will not free. Though all the Gods for Ráma fight, He yields to my superior might.” Thus the tremendous king who broke The ranks of heavenly warriors spoke, And, sternly purposed to resist, His brother from the hall dismissed. Canto XI. The Summons. Still RávaG's haughty heart rebelled, The counsel of the wise repelled, And, as his breast with passion burned, His thoughts again to Sítá turned. Thus, to each sign of danger blind, To love and war he still inclined. Then mounted he his car that glowed With gems and golden net, and rode Where, gathered at the monarch's call, The nobles filled the council hall. A host of warriors bright and gay With coloured robes and rich array, With shield and mace and spear and sword, Followed the chariot of their lord. Mid the loud voice of shells and beat Of drums he raced along the street, And, ere he came, was heard afar
- **Translation**: 

---

### Verse 3 (Ramayana 0.1548)
- **Original**: 1530 The Ramayana The rolling thunder of his car. He reached the doors: the nobles bent Their heads before him reverent: And, welcomed with their loud acclaim, Within the glorious hall he came. He sat upon a royal seat With golden steps beneath his feet, And bade the heralds summon all His captains to the council hall. The heralds heard the words he spake, And sped from house to house to wake The giants where they slept or spent The careless hours in merriment. These heard the summons and obeyed: From chamber, grove, and colonnade, On elephants or cars they rode, Or through the streets impatient strode. As birds on rustling pinions fly Through regions of the darkened sky, Thus cars and mettled coursers through The crowded streets of Lanká flew. The council hall was reached, and then, As lions seek their mountain den, Through massy doors that opened wide, With martial stalk the captains hied. Welcomed with honour as was meet They stooped to press their monarch's feet,[435] And each a place in order found On stool, on cushion, or the ground. Nor did the sage VibhishaG long Delay to join the noble throng. High on a car that shone like flame With gold and flashing gems he came, Drew near and spoke his name aloud,
- **Translation**: 

---

### Verse 4 (Ramayana 0.1549)
- **Original**: Canto XII. Rávan's Speech. 1531 And reverent to his brother bowed. Canto XII. Rávan's Speech. The king in counsel unsurpassed His eye around the synod cast, And fierce Prahasta, first and best Of all his captains, thus addressed: “Brave master of each warlike art, Arouse thee and perform thy part. Array thy fourfold forces918 well To guard our isle and citadel.” The captain of the hosts obeyed, The troops with prudent skill arrayed; Then to the hall again he hied, And stood before the king and cried: “Each inlet to the town is closed Without, within, are troops disposed. With fearless heart thine aim pursue And do the deed thou hast in view.” 918 Consisting of warriors on elephants, warriors in chariots, charioteers, and infantry.
- **Translation**: 

---

### Verse 5 (Ramayana 0.1550)
- **Original**: 1532 The Ramayana Thus spoke Prahasta in the zeal That moved him for the kingdom's weal. And thus the monarch, who pursued His own delight, his speech renewed: “In ease and bliss, in toil and pain, In doubts of duty, pleasure, gain, Your proper path I need not tell, For of yourselves ye know it well. The Storm-Gods, Moon, and planets bring New glory to their heavenly king,919 And, ranged about your monarch, ye Give joy and endless fame to me. My secret counsel have I kept, While senseless KumbhakarGa slept. Six months the warrior's slumbers last And bind his torpid senses fast; But now his deep repose he breaks, The best of all our champions wakes. I captured, Ráma's heart to wring, This daughter of Videha's king. And brought her from that distant land920 Where wandered many a Rákshas band. Disdainful still my love she spurns, Still from each prayer and offering turns, Yet in all lands beneath the sun No dame may rival Sítá, none, Her dainty waist is round and slight, Her cheek like autumn's moon is bright, And she like fruit in graven gold Mocks her921 whom Maya framed of old. 919 Indra, generally represented as surrounded by the Maruts or Storm-Gods. 920 Janasthán, where Ráma lived as an ascetic. 921 Máyá, regarded as the paragon of female beauty, was the creation of Maya the chief artificer of the Daityas or Dánavs.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1551)
- **Original**: Canto XII. Rávan's Speech. 1533 Faultless in form, how firmly tread Her feet whose soles are rosy red! Ah, as I gaze her beauty takes My spirit, and my passion wakes. Looking for Ráma far away She sought with tears a year's delay Nor gazing on her love-lit eye Could I that earnest prayer deny. But baffled hopes and vain desire At length my patient spirit tire. How shall the sons of Raghu sweep To vengeance o'er the pathless deep? How shall they lead the Vánar train Across the monster-teeming main? One Vánar yet could find a way To Lanká's town, and burn and slay. Take counsel then, remembering still That we from men need fear no ill; And give your sentence in debate, For matchless is the power of fate. Assailed by you the Gods who dwell In heaven beneath our fury fell. And shall we fear these creatures bred In forests, by Sugríva led? E'en now on ocean's farther strand, The sons of Da[aratha stand, And follow, burning to attack Their giant foes, on Sítá's track. Consult then, lords for ye are wise: A seasonable plan devise. The captive lady to retain, And triumph when the foes are slain. No power can bring across the foam Those Vánars to our island home;
- **Translation**: 

---

### Verse 7 (Ramayana 0.1552)
- **Original**: 1534 The Ramayana Or if they madly will defy Our conquering might, they needs must die.” Then KumbhakarGa's anger woke, And wroth at RávaG's words he spoke: “O Monarch, when thy ravished eyes First looked upon thy lovely prize, Then was the time to bid us scan Each peril and mature a plan. Blest is the king who acts with heed, And ne'er repents one hasty deed; And hapless he whose troubled soul Mourns over days beyond control.[436] Thou hast, in beauty's toils ensnared, A desperate deed of boldness dared; By fortune saved ere Ráma's steel One wound, thy mortal bane, could deal. But, RávaG, as the deed is done, The toil of war I will not shun. This arm, O rover of the night, Thy foemen to the earth shall smite, Though Indra with the Lord of Flame, The Sun and Storms, against me came. E'en Indra, monarch of the skies, Would dread my club and mountain size, Shrink from these teeth and quake to hear The thunders of my voice of fear. No second dart shall Ráma cast: The first he aims shall be the last. He falls, and these dry lips shall drain The blood of him my hand has slain; And Sítá, when her champion dies, Shall be thine undisputed prize.”
- **Translation**: 

---

### Verse 8 (Ramayana 0.1553)
- **Original**: Canto XIII. Rávan's Speech. 1535 Canto XIII. Rávan's Speech. But Mahápár[va saw the sting Of keen reproach had galled the king; And humbly, eager to appease His anger, spoke in words like these: “And breathes there one so cold and weak The forest and the gloom to seek Where savage beasts abound, and spare To taste the luscious honey there? Art thou not lord? and who is he Shall venture to give laws to thee? Love thy Videhan still, and tread Upon thy prostrate foeman's head. O'er Sítá's will let thine prevail, And strength achieve if flattery fail. What though the lady yet be coy And turn her from the proffered joy? Soon shall her conquered heart relent And yield to love and blandishment. With us let KumbhakarGa fight, And Indrajít of matchless might: We need not other champions, they Shall lead us forth to rout and slay. Not ours to bribe or soothe or part The foeman's force with gentle art, Doomed, conquered by our might, to feel The vengeance of the warrior's steel.” The Rákshas monarch heard, and moved By flattering hopes the speech approved:
- **Translation**: 

---

### Verse 9 (Ramayana 0.1554)
- **Original**: 1536 The Ramayana “Hear me,” he cried,“great chieftain, tell What in the olden time befell,— A secret tale which, long suppressed, Lies prisoned only in my breast. One day— a day I never forget— Fair Punjikasthalá922 I met, When, radiant as a flame of fire, She sought the palace of the Sire. In passion's eager grasp I tore From her sweet limbs the robes she wore, And heedless of her prayers and cries Strained to my breast the vanquised prize. Like Naliní923 with soil distained, The mansion of the Sire she gained, And weeping made the outrage known To Brahmá on his heavenly throne. He in his wrath pronounced a curse,— That lord who made the universe: “If, RávaG, thou a second time Be guilty of so foul a crime, Thy head in shivers shall be rent: Be warned, and dread the punishment.” Awed by the threat of vengeance still I force not Sítá's stubborn will. Terrific as the sea in might: My steps are like the Storm-Gods' flight; But Ráma knows not this, or he Had never sought to war with me. Where is the man would idly brave The lion in his mountain cave, And wake him when with slumbering eyes Grim, terrible as Death, he lies? 922 One of the Nymphs of Indra's heaven. 923 The Lotus River, a branch of the heavenly Gangá.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1555)
- **Original**: Canto XIV. Vibhishan's Speech. 1537 No, blinded Ráma knows me not: Ne'er has he seen mine arrows shot; Ne'er marked them speeding to their aim Like snakes with cloven tongues of flame. On him those arrows will I turn, Whose fiery points shall rend and burn. Quenched by my power when I assail The glory of his might shall fail, As stars before the sun grow dim And yield their feeble light to him.” Canto XIV. Vibhishan's Speech. He ceased: VibhishaG ill at ease Addressed the king in words like these: “O RávaG, O my lord, beware Of Sítá dangerous as fair, Nor on thy heedless bosom hang This serpent with a deadly fang. O King, the Maithil dame restore To Raghu's matchless son before Those warriors of the woodlands, vast As mountain peaks, approaching fast, Armed with fierce teeth and claws, enclose Thy city with unsparing foes. O, be the Maithil dame restored Ere loosened from the clanging cord [437]
- **Translation**: 

---

### Verse 11 (Ramayana 0.1556)
- **Original**: 1538 The Ramayana The vengeful shafts of Ráma fly, And low in death thy princes lie. In all thy legions hast thou one A match in war for Raghu's son? Can KumbhakarGa's self withstand, Or Indrajít, that mighty hand? In vain with Ráma wilt thou strive: Thou wilt not save thy soul alive Though guarded by the Lord of Day And Storm-Gods' terrible array, In vain to Indra wilt thou fly, Or seek protection in the sky, In Yáma's gloomy mansion dwell, Or hide thee in the depths of hell.” He ceased; and when his lips were closed Prahasta thus his rede opposed: “O timid heart, to counsel thus! What terrors have the Gods for us? Can snake, Gandharva, fiend appal The giants' sons who scorn them all? And shall we now our birth disgrace, And dread a king of human race?” Thus fierce Prahasta counselled ill: But sage VibhishaG's constant will The safety of the realm ensued; Who thus in turn his speech renewed:
- **Translation**: 

---

### Verse 12 (Ramayana 0.1557)
- **Original**: Canto XV. Indrajít's Speech. 1539 “Yes, when a soul defiled with sin Shall mount to heaven and enter in, Then, chieftain, will experience teach The truth of thy disdainful speech. Can I, or thou, or these or all Our bravest compass Ráma's fall, The chief in whom all virtues shine, The pride of old Ikshváku'a line, With whom the Gods may scarce compare In skill to act, in heart to dare? Yea, idly mayst thou vaunt thee, till Sharp arrows winged with matchless skill From Ráma's bowstring, fleet and fierce As lightning's flame, thy body pierce. Nikumbha shall not save thee then, Nor RávaG, from the lord of men. O Monarch, hear my last appeal, My counsel for thy kingdom's weal. This sentence I again declare: O giant King, beware, beware! Save from the ruin that impends Thy town, thy people, and thy friends; O hear the warning urged once more: To Raghu's son the dame restore.” Canto XV. Indrajít's Speech. He ceased: and Indrajít the pride Of Rákshas warriors thus replied:
- **Translation**: 

---

### Verse 13 (Ramayana 0.1558)
- **Original**: 1540 The Ramayana “Is this a speech our king should hear, This counsel of ignoble fear? A scion of our glorious race Should ne'er conceive a thought so base, But one mid all our kin we find, VibhishaG, whose degenerate mind No spark of gallant pride retains, Whose coward soul his lineage stains. Against one giant what can two Unhappy sons of Raghu do? Away with idle fears, away! Matched with our meanest, what are they? Beneath my conquering prowess fell The Lord of earth and heaven and hell.924 Through every startled region dread Of my resistless fury spread; And Gods in each remotest sphere Confessed the universal fear. Rending the air with roar and groan, Airávat925 to the earth was thrown. From his huge head the tusks I drew, And smote the Gods with fear anew. Shall I who tame celestials' pride, By whom the fiends are terrified, Now prove a weakling little worth, And fail to slay those sons of earth?” He ceased: VibhishaG trained and tried In war and counsel thus replied 924 Trilokanátha, Lord of the Three Worlds, is a title of Indra. 925 The celestial elephant that carries Indra.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1559)
- **Original**: Canto XVI. Rávan's Speech. 1541 “Thy speech is marked with scorn of truth, With rashness and the pride of youth. Yea, to thy ruin like a child Thou pratest, and thy words are wild. Most dear, O Indrajít, to thee Should RávaG's weal and safety be, For thou art called his son, but thou Art proved his direst foeman now, When warned by me thou hast not tried To turn the coming woe aside. Both thee and him 'twere meet to slay, Who brought thee to this hall to-day, And dared so rash a youth admit To council where the wisest sit. Presumptuous, wild, devoid of sense, Filled full of pride and insolence, Thy reckless tongue thou wilt not rule That speaks the counsel of a fool. Who in the fight may brook or shun The arrows shot by Raghu's son With flame and fiery vengeance sped, Dire as his staff who rules the dead? O RávaG, let thy people live, And to the son of Raghu give Fair robes and gems and precious ore, And Sítá to his arms restore.” [438] Canto XVI. Rávan's Speech.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1560)
- **Original**: 1542 The Ramayana Then, while his breast with fury swelled, Thus RávaG spoke, as fate impelled: “Better with foes thy dwelling make, Or house thee with the venomed snake, Than live with false familiar friends Who further still thy foeman's ends. I know their treacherous mood, I know Their secret triumph at thy woe. They in their inward hearts despise The brave, the noble, and the wise, Grieve at their bliss with rancorous hate, And for their sorrows watch and wait: Scan every fault with curious eye, And each slight error magnify. Ask elephants who roam the wild How were their captive friends beguiled. “For fire,” they cry,“we little care, For javelin and shaft and snare: Our foes are traitors, taught to bind The trusting creatures of their kind.” Still, still, shall blessings flow from cows,926 And Bráhmans love their rigorous vows; Still woman change her restless will, And friends perfidious work us ill. What though with conquering feet I tread On every prostrate foeman's head; What though the worlds in abject fear Their mighty lord in me revere? This thought my peace of mind destroys And robs me of expected joys. The lotus of the lake receives 926 As producers of theghi, clarified butter or sacrificial oil, used in fire-offer- ings.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1561)
- **Original**: Canto XVI. Rávan's Speech. 1543 The glittering rain that gems its leaves, But each bright drop remains apart: So is it still with heart and heart. Deceitful as an autumn cloud Which, though its thunderous voice be loud, On the dry earth no torrent sends, Such is the race of faithless friends. No riches of the bloomy spray Will tempt the wandering bee to stay That loves from flower to flower to range; And friends like thee are swift to change. Thou blot upon thy glorious line, If any giant's tongue but thine Had dared to give this base advice, He should not live to shame me twice.” Then just VibhishaG in the heat Of anger started from his seat, And with four captains of the band Sprang forward with his mace in hand; Then, fury flashing from his eye, Looked on the king and made reply: “Thy rights, O RávaG, I allow: My brother and mine elder thou. Such, though from duty's path they stray, We love like fathers and obey, But still too bitter to be borne Is thy harsh speech of cruel scorn. The rash like thee, who spurn control, Nor check one longing of the soul, Urged by malignant fate repel The faithful friend who counsels well. A thousand courtiers wilt thou meet,
- **Translation**: 

---

### Verse 17 (Ramayana 0.1562)
- **Original**: 1544 The Ramayana With flattering lips of smooth deceit: But rare are they whose tongue or ear Will speak the bitter truth, or hear. Unclose thy blinded eyes and see That snares of death encompass thee. I dread, my brother, to behold The shafts of Ráma, bright with gold, Flash fury through the air, and red With fires of vengeance strike thee dead. Lord, brother, King, again reflect, Nor this mine earnest prayer reject, O, save thyself, thy royal town, Thy people and thine old renown.” Canto XVII. Vibhishan's Flight. Soon as his bitter words were said, To Raghu's sons VibhishaG fled.927 Their eyes the Vánar leaders raised And on the air-borne Rákhshas gazed, Bright as a thunderbolt, in size Like Meru's peak that cleaves the skies. In gorgeous panoply arrayed Like Indra's self he stood displayed, And four attendants brave and bold 927 This desertion to the enemy is somewhat abrupt, and is narrated with brevity not usual with Válmíki. In the Bengal recension the preceding speakers and speeches differ considerably from those given in the text which I follow. VibhishaG is kicked from his seat by RávaG, and then, after telling his mother what has happened, he flies to Mount Kailása where he has an interview with Ziva, and by his advice seeks Ráma and the Vánar army.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1563)
- **Original**: Canto XVII. Vibhishan's Flight. 1545 Shone by their chief in mail and gold. Sugríva then with dark surmise Bent on their forms his wondering eyes, And thus in hasty words confessed The anxious doubt that moved his breast: “Look, look ye Vánars, and beware: That giant chief sublime in air With other four in bright array Comes armed to conquer and to slay.” [439] Soon as his warning speech they heard, The Vánar chieftains undeterred Seized fragments of the rock and trees, And made reply in words like these: “We wait thy word: the order give, And these thy foes shall cease to live. Command us, mighty King, and all Lifeless upon the earth shall fall.” Meanwhile VibhishaG with the four Stood high above the ocean shore. Sugríva and the chiefs he spied, And raised his mighty voice and cried: “From RávaG, lord of giants, I His brother, named VibhishaG, fly. From Janasthán he stole the child Of Janak by his art beguiled, And in his palace locked and barred Surrounds her with a Rákshas guard. I bade him, plied with varied lore, His hapless prisoner restore. But he, by Fate to ruin sent, No credence to my counsel lent, Mad as the fevered wretch who sees
- **Translation**: 

---

### Verse 19 (Ramayana 0.1564)
- **Original**: 1546 The Ramayana And scorns the balm to bring him ease. He scorned the sage advice I gave, He spurned me like a base-born slave. I left my children and my wife, And fly to Raghu's son for life. I pray thee, Vánar chieftain, speed To him who saves in hour of need, And tell him famed in distant lands That suppliant here VibhishaG stands.” The Rákshas ceased: Sugríva hied To Raghu's noble son and cried: “A stranger from the giant host, Borne o'er the sea, has reached the coast; A secret foe, he comes to slay, As owls attack their heedless prey. 'Tis thine, O King, in time of need To watch, to counsel, and to lead, Our Vánar legions to dispose, And guard us from our crafty foes. VibhishaG from the giants' isle, King RávaG's brother, comes with guile And, feigning from his king to flee, Seeks refuge, Raghu's son, with thee. Arise, O Ráma, and prevent By bold attack his dark intent. Who comes in friendly guise prepared To slay thee by his arts ensnared.”
- **Translation**: 

---

### Verse 20 (Ramayana 0.1565)
- **Original**: Canto XVII. Vibhishan's Flight. 1547 Thus urged Sugríva famed for lore Of moving words, and spoke no more. Then Ráma thus in turn addressed The bold Hanúmán and the rest: “Chiefs of the Vánar legions each Of you heard Sugríva's speech. What think ye now in time of fear, When peril and distress are near, In every doubt the wise depend For counsel on a faithful friend.” They heard his gracious words, and then Spake reverent to the lord of men: “O Raghu's son, thou knowest well All things of heaven and earth and hell. 'Tis but thy friendship bids us speak The counsel Ráma need not seek. So duteous, brave, and true art thou, Heroic, faithful to thy vow. Deep in the scriptures, trained and tried, Still in thy friends wilt thou confide. Let each of us in turn impart The secret counsel of his heart, And strive to win his chief's assent, By force of wisest argument.” They ceased and Angad thus began: “With jealous eye the stranger scan: Not yet with trusting heart receive VibhishaG, nor his tale believe. These giants wandering far and wide Their evil nature falsely hide, And watching with malignant skill Assail us when we fear no ill.
- **Translation**: 

---

