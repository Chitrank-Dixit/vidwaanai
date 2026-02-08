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

### Verse 1 (Ramayan 0.1481)
- **Original**: Canto XXXVII. Sítá's Speech. 1463 If lovely flowers or fruit he sees, Which women love, upon the trees, To thee, to thee his fancy flies. And ‘Sítá! O my love!’he cries.” Canto XXXVII. Sítá's Speech. “Thou bringest me,” she cried again, “A mingled draught of bliss and pain: Bliss, that he wears me in his heart, Pain, that he wakes and weeps apart, O, see how Fate is king of all, Now lifts us high, now bids us fall, And leads a captive bound with cord The meanest slave, the proudest lord, Thus even now Fate's stern decree Has struck with grief my lord and me. Say, how shall Ráma reach the shore Of sorrow's waves that rise and roar, A shipwrecked sailor, well nigh drowned In the wild sea that foams around? When will he smite the demon down, Lay low in dust the giants' town, And, glorious from his foes' defeat, His wife, his long-lost Sítá, meet? Go, bid him speed to smite his foes Before the year shall reach its close. Ten months are fled but two remain, Then RávaG's captive must be slain. Oft has VibhishaG,863 just and wise, 863 VibhishaG is the wicked RávaG's good brother.
- **Translation**: 

---

### Verse 2 (Ramayan 0.1482)
- **Original**: 1464 The Ramayana Besought him to restore his prize. But deaf is RávaG's senseless ear: His brother's rede he will not hear. VibhishaG's daughter864 loves me well: From her I learnt the tale I tell. Avindhva865 prudent, just, and old, The giant's fall has oft foretold; But Fate impels him to despise His word on whom he most relies. In Ráma's love I rest secure, For my fond heart is true and pure, And him, my noblest lord, I deem In valour, power, and might supreme.” As from her eyes the waters ran, The Vánar chief again began: “Yea, Ráma, when he hears my tale, Will with our hosts these walls assail. Or I myself, O Queen, this day Will bear thee from the fiend away, Will lift thee up, and take thee hence To him thy refuge and defence; Will take thee in my arms, and flee To Ráma far beyond the sea; Will place thee on Pra[ravaG hill Where Raghu's son is waiting still.”[416] “How canst thou bear me hence?” she cried, “The way is long, the sea is wide. To bear my very weight would be A task too hard for one like thee.”866 864 Her name is Kalá, or in the Bengal recension Nandá. 865 One of RávaG's chief councillors. 866 Hanumán when he entered the city had in order to escape observation condensed himself to the size of a cat.
- **Translation**: 

---

### Verse 3 (Ramayan 0.1483)
- **Original**: Canto XXXVII. Sítá's Speech. 1465 Swift rose before her startled eyes The Vánar in his native size, Like Mandar's hill or Meru's height, Encircled with a blaze of light. “O come,” he cried,“thy fears dispel, Nor doubt that I will bear thee well. Come, in my strength and care confide, And sit in joy by Ráma's side.” Again she spake:“I know thee now, Brave, resolute, and strong art thou; In glory like the Lord of Fire With storm-swift feet which naught may tire But yet with thee I may not fly: For, borne so swiftly through the sky, Mine eyes would soon grow faint and dim, My dizzy brain would reel and swim, My yielding arms relax their hold, And I in terror uncontrolled Should fall into the raging sea Where hungry sharks would feed on me. Nor can I touch, of free accord, The limbs of any save my lord. If, by the giant forced away, In his enfolding arms I lay, Not mine, O Vánar, was the blame; What could I do, a helpless dame? Go, to my lord my message bear, And bid him end my long despair.”
- **Translation**: 

---

### Verse 4 (Ramayan 0.1484)
- **Original**: 1466 The Ramayana Canto XXXVIII. Sítá's Gem. Again the Vánar chief replied, With her wise answer satisfied: “Well hast thou said: thou canst not brave The rushing wind, the roaring wave. Thy woman's heart would sink with fear Before the ocean shore were near. And for thy dread lest limb of thine Should for a while be touched by mine, The modest fear is worthy one Whose cherished lord is Raghu's son. Yet when I sought to bear thee hence I spoke the words of innocence, Impelled to set the captive free By friendship for thy lord and thee. But if with me thou wilt not try The passage of the windy sky, Give me a gem that I may show, Some token which thy lord may know.” Again the Maithil lady spoke, While tears and sobs her utterance broke: “The surest of all signs is this, To tell the tale of vanished bliss. Thus in my name to Ráma speak: “Remember Chitrakúma's peak And the green margin of the rill867 That flows beside that pleasant hill, Where thou and I together strayed Delighting in the tangled shade. 867 The brook Mandákiní, not far from Chitrakúma where Ráma sojourned for a time.
- **Translation**: 

---

### Verse 5 (Ramayan 0.1485)
- **Original**: Canto XXXVIII. Sítá's Gem. 1467 There on the grass I sat with thee And laid my head upon thy knee. There came a greedy crow and pecked The meat I waited to protect And, heedless of the clods I threw, About my head in circles flew, Until by darling hunger pressed He boldly pecked me on the breast. I ran to thee in rage and grief And prayed for vengeance on the thief. Then Ráma 868 from his slumber rose And smiled with pity at my woes. Upon my bleeding breast he saw The scratches made by beak and claw. He laid an arrow on his bow, And launched it at the shameless crow. That shaft, with magic power endued, The bird, where'er he flew, pursued, Till back to Raghu's son he fled And bent at Ráma's feet his head.869 Couldst thou for me with anger stirred Launch that dire shaft upon a bird, And yet canst pardon him who stole The darling of thy heart and soul? Rise up, O bravest of the brave, And come in all thy might to save. Come with the thunders of thy bow, And smite to earth the Rákshas foe.” She ceased; and from her glorious hair She took a gem that sparkled there 868 The poet here changes from the second person to the third. 869 The whole long story is repeated with some slight variations and additions from Book II, Canto XCVI. I give here only the outline.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1486)
- **Original**: 1468 The Ramayana A token which her husband's eyes With eager love would recognize. His head the Vánar envoy bent In low obeisance reverent. And on his finger bound the gem She loosened from her diadem. [I omit two Cantos of dialogue. Sítá tells Hanumán again to convey her message to Ráma and bid him hasten to rescue her. Hanumán replies as before that there is no one on earth equal to Ráma, who will soon come and destroy RávaG. There is not a new idea in the two Cantos: all is reiteration.] [417] Canto XLI. The Ruin Of The Grove. Dismissed with every honour due The Vánar from the spot withdrew. Then joyous thought the Wind-God's son: “The mighty task is wellnigh done. The three expedients I must leave; The fourth alone can I achieve.870 These dwellers in the giants' isle No arts of mine can reconcile. I cannot bribe: I cannot sow Dissension mid the Rákshas foe. Arts, gifts, address, these fiends despise; 870 The expedients to vanquish an enemy or to make him come to terms are said to be four: conciliation, gifts, disunion, and force or punishment. Hanumán considers it useless to employ the first three and resolves to punish RávaG by destroying his pleasure-grounds.
- **Translation**: 

---

### Verse 7 (Ramayan 0.1487)
- **Original**: Canto XLI. The Ruin Of The Grove. 1469 But force shall yet their king chastise. Perchance he may relent when all The bravest of his chieftains fall. This lovely grove will I destroy, The cruel RávaG's pride and joy. The garden where he takes his ease Mid climbing plants and flowery trees That lift their proud tops to the skies, Dear to the tyrant as his eyes. Then will he rouse in wrath, and lead His legions with the car and steed And elephants in long array, And seek me thirsty for the fray. The Rákshas legions will I meet, And all his bravest host defeat; Then, glorious from the bloody plain, Turn to my lord the king again.” Then every lovely tree that bore Fair blossoms, from the soil he tore, Till each green bough that lent its shade To singing birds on earth was laid. The wilderness he left a waste, The fountains shattered and defaced: O'erthrew and levelled with the ground Each shady seat and pleasure-mound. Each arbour clad with climbing bloom, Each grotto, cell, and picture room, Each lawn by beast and bird enjoyed, Each walk and terrace was destroyed. And all the place that was so fair Was left a ruin wild and bare, As if the fury of the blast Or raging fire had o'er it passed.
- **Translation**: 

---

### Verse 8 (Ramayan 0.1488)
- **Original**: 1470 The Ramayana Canto XLII. The Giants Roused. The cries of startled birds, the sound Of tall trees crashing to the ground, Struck with amaze each giant's ear, And filled the isle with sudden fear. Then, wakened by the crash and cries, The fierce shefiends unclosed their eyes, And saw the Vánar where he stood Amid the devastated wood. The more to scare them with the view To size immense the Vánar grew; And straight the Rákshas warders cried Janak's daughter terrified “Whose envoy, whence, and who is he, Why has he come to talk with thee? Speak, lady of the lovely eyes, And let not fear thy joy disguise.” Then thus replied the Maithil dame Of noble soul and perfect frame. “Can I discern, with scanty skill, These fiends who change their forms at will? 'Tis yours to say: your kin you meet; A serpent knows a serpent's feet.
- **Translation**: 

---

### Verse 9 (Ramayan 0.1489)
- **Original**: Canto XLII. The Giants Roused. 1471 I weet not who he is: the sight Has filled my spirit with affright.” Some pressed round Sítá in a ring; Some bore the story to their king: “A mighty creature of our race, In monkey form, has reached the place. He came within the grove,” they cried, “He stood and talked by Sítá's side, He comes from Indra's court to her, Or is Kuvera's messenger; Or Ráma sent the spy to seek His consort, and her wrongs to wreak. His crushing arm, his trampling feet Have marred and spoiled that dear retreat, And all the pleasant place which thou So lovest is a ruin now. The tree where Sítá sat alone Is spared where all are overthrown. Perchance he saved the dame from harm: Perchance the toil had numbed his arm.” Then flashed the giant's eye with fire Like that which lights the funeral pyre. He bade his bravest Kinkars871 speed [418] And to his feet the spoiler lead. Forth from the palace, at his hest, Twice forty thousand warriors pressed. Burning for battle, strong and fierce, With clubs to crush and swords to pierce, They saw Hanúmán near a porch, And, thick as moths around a torch, 871 Kinkar means the special servant of a sovereign, who receives his orders immediately from his master. The Bengal recension gives these Rákshases an epithet which the Commentator explains“as generated in the mind of Brahmá.”
- **Translation**: 

---

### Verse 10 (Ramayan 0.1490)
- **Original**: 1472 The Ramayana Rushed on the foe with wild attacks Of mace and club and battle-axe. As round him pressed the Rákshas crowd, The wondrous monkey roared aloud, That birds fell headlong from the sky: Then spake he with a mighty cry: “Long life to Da[aratha's heir, And Lakshma G, ever-glorious pair! Long life to him who rules our race, Preserved by noblest Ráma's grace! I am the slave of Ko[al's king,872 Whose wondrous deeds the minstrels sing. Hanúmán I, the Wind-God's seed: Beneath this arm the foemen bleed. I fear not, unapproached in might, A thousand RávaG's ranged for fight, Although in furious hands they rear The hill and tree for sword and spear, I will, before the giants' eyes, Their city and their king chastise; And, having communed with the dame, Depart in triumph as I came.” At that terrific roar and yell The heart of every giant fell. But still their king's command they feared And pressed around with arms upreared. Beside the porch a club was laid: The Vánar caught it up, and swayed The weapon round his head, and slew The foremost of the Rákshas crew. Thus Indra vanquished, thousand-eyed, The Daityas who the Gods defied. 872 Ráma de jureKing of Ko[al of which Ayodhyá was the capital.
- **Translation**: 

---

### Verse 11 (Ramayan 0.1491)
- **Original**: Canto XLIII. The Ruin Of The Temple. 1473 Then on the porch Hanúmán sprang, And loud his shout of triumph rang. The giants looked upon the dead, And turning to their monarch fled. And RávaG with his spirit wrought To frenzy by the tale they brought, Urged to the fight Prahasta's son, Of all his chiefs the mightiest one. Canto XLIII. The Ruin Of The Temple. The Wind-God's son a temple873 scaled Which, by his fury unassailed, High as the hill of Meru, stood Amid the ruins of the wood; And in his fury thundered out Again his haughty battle-shout: “I am the slave of Ko[al's King Whose wondrous deeds the minstrels sing.” Forth hurried, by that shout alarmed, The warders of the temple armed With every weapon haste supplied, And closed him in on every side, With bands that strove to pierce and strike With shaft and axe and club and pike. Then from its base the Vánar tore A pillar with the weight it bore. Against the wall the mass he dashed, 873 Chaityaprásádais explained by the Commentator as the place where the Gods of the Rákshases were kept. Gorresio translates it by“un grande edificio.”
- **Translation**: 

---

### Verse 12 (Ramayan 0.1492)
- **Original**: 1474 The Ramayana And forth the flames in answer flashed, That wildly ran o'er roofs and wall In hungry rage consuming all. He whirled the pillar round his head And struck a hundred giants dead. Then high upheld on air he rose And called in thunder to his foes: “A thousand Vánar chiefs like me Roam at their will o'er land and sea, Terrific might we all possess: Our stormy speed is limitless. And all, unconquered in the fray, Our king Sugríva's word obey. Backed by his bravest myriads, he Our warrior lord will cross the sea. Then Lanká's lofty towers, and all Your hosts and RávaG's self shall fall. None shall be left unslaughtered; none Who braves the wrath of Raghu's son.” Canto XLIV. Jambumáli's Death. Then Jambumáli, pride and boast For valour of the Rákshas host, Prahasta's son supremely brave, Obeyed the hest that RávaG gave: Fierce warrior with terrific teeth, With saguine robes and brilliant wreath. A bow like Indra's own874, and store[419] 874 The bow of Indra is the rainbow.
- **Translation**: 

---

### Verse 13 (Ramayan 0.1493)
- **Original**: Canto XLIV. Jambumáli's Death. 1475 Of glittering shafts the chieftain bore. And ever as the string he tried The weapon with a roar replied, Loud as the crashing thunder sent By him who rules the firmament. Soon as the foeman came in view Borne on a car which asses drew, The Vánar chieftain mighty-voiced Shouted in triumph and rejoiced. Prahasta's son his bow-string drew, And swift the winged arrows flew, One in the face the Vánar smote, Another quivered in his throat. Ten from the deadly weapon sent His brawny arms and shoulders rent. Then as he felt each galling shot The Vánar's rage waxed fiercely hot. He looked, and saw a mass of stone That lay before his feet o'erthrown. The mighty block he raised and threw, And crashing through the air it flew. But Jambumáli shunned the blow, And rained fresh arrows from his bow. The Vánar's limbs were red with gore: A Sál tree from the earth he tore, And, ere he hurled it undismayed, Above his head the missile swayed. But shafts from Jambumáli's bow Cut through it ere his hand could throw. And thigh and arm and chest and side With streams of rushing blood were dyed. Still unsubdued though wounded oft The shattered trunk he raised aloft, And down with well-directed aim
- **Translation**: 

---

### Verse 14 (Ramayan 0.1494)
- **Original**: 1476 The Ramayana On Jambumáli's chest it came. There crushed upon the trampled grass He lay an undistinguished mass, The foeman's eye no more could see His head or chest or arm or knee. And bow and car and steeds875 and store Of glittering shafts were seen no more. When Jambumáli's death he heard, King RávaG's heart with rage was stirred And forth his general's sons he sent, For power and might preeminent. Canto XLV. The Seven Defeated. Forth went the seven in brave attire, In glory brilliant as the fire, Impetuous chiefs with massive bows, The quellers of a host of foes: Trained from their youth in martial lore, And masters of the arms they bore: Each emulous and fiercely bold, And banners wrought with glittering gold Waved o'er their chariots, drawn at speed By coursers of the noblest breed. On through the ruins of the grove At Hanumán they fiercely drove, And from the ponderous bows they strained 875 We were told a few lines before that the chariot of Jambumáli was drawn by asses. Here horses are spoken of. The Commentator notices the discrepancy and says that by horses asses are meant.
- **Translation**: 

---

### Verse 15 (Ramayan 0.1495)
- **Original**: Canto XLV. The Seven Defeated. 1477 A shower of deadly arrows rained. Then scarce was seen the Vánar's form Enveloped in the arrowy storm. So stands half veiled the Mountains' King When rainy clouds about him cling. By nimble turn, by rapid bound He shunned the shafts that rained around, Eluding, as in air he rose, The rushing chariots of his foes. The mighty Vánar undismayed Amid his archer foemen played, As plays the frolic wind on high Mid bow-armed876 clouds that fill the sky. He raised a mighty roar and yell That fear on all the army fell, And then, his warrior soul aglow With fury, rushed upon the foe, Some with his open hand he beat To death and trampled with his feet; Some with fierce nails he rent and slew, And others with his fists o'erthrew; Some with his legs, as on he rushed, Some with his bulky chest he crushed; While some struck senseless by his roar Dropped on the ground and breathed no more, The remnant, seized with sudden dread, Turned from the grove and wildly fled. The trampled earth was thickly strown With steed and car and flag o'erthrown, And the red blood in rivers flowed From slaughtered fiends o'er path and road. 876 Armed with the bow of Indra, the rainbow.
- **Translation**: 

---

### Verse 16 (Ramayan 0.1496)
- **Original**: 1478 The Ramayana Canto XLVI. The Captains. Mad with the rage of injured pride King RávaG summoned to his side The valiant five who led his host, Supreme in war and honoured most. “Go forth,” he cried,“with car and steed, And to my feet this monkey lead, But watch each chance of time and place To seize this thing of silvan race. For from his wondrous exploits he No monkey of the woods can be,[420] But some new kind of creature meant To work us woe, by Indra sent. Gandharvas, Nágas, and the best Of Yakshas have our might confessed. Have we not challenged and subdued The whole celestial multitude? Yet will you not, if you are wise, A chief of monkey race despise. For I myself have Báli known, And King Sugríva's power I own. But none of all their woodland throng Was half so terrible and strong.” Obedient to the words he spake They hastened forth the foe to take. Swift were the cars whereon they rode, And bright their weapons flashed and glowed. They saw: they charged in wild career With sword and mace and axe and spear. From Durdhar's bow five arrows sped And quivered in the Vánar's head. He rose and roared: the fearful sound
- **Translation**: 

---

### Verse 17 (Ramayan 0.1497)
- **Original**: Canto XLVII. The Death Of Aksha. 1479 Made all the region echo round. Then from above his weight he threw On Durdhar's car that near him drew. The weight that came with lightning speed Crushed pole and axle, car and steed. It shattered Durdhar's head and neck, And left him lifeless mid the wreck. Yúpáksha saw the warrior die, And Virúpáksha heard his cry, And, mad for vengeance for the slain, They charged their Vánar foe again. He rose in air: they onward pressed And fiercely smote him on the breast. In vain they struck his iron frame: With eagle swoop to earth he came, Tore from the ground a tree that grew Beside him, and the demons slew. Then Bhásakama raised his spear, And Praghas with a laugh drew near, And, maddened at the sight, the two Against the undaunted Vánar flew. As from his wounds the torrents flowed, Like a red sun the Vánar showed. He turned, a mountain peak to seize With all its beasts and snakes and trees. He hurled it on the pair: and they Crushed, overwhelmed, beneath it lay. Canto XLVII. The Death Of Aksha.
- **Translation**: 

---

### Verse 18 (Ramayan 0.1498)
- **Original**: 1480 The Ramayana But RávaG, as his fury burned, His eyes on youthful Aksha877 turned, Who rose impetuous at his glance And shouted for his bow and lance. He rode upon a glorious car That shot the light of gems afar. His pennon waved mid glittering gold And bright the wheels with jewels rolled, By long and fierce devotion won That car was splendid as the sun. With rows of various weapons stored; And thought-swift horses whirled their lord Racing along the earth, or rose High through the clouds whene'er he chose. Then fierce and fearful war between The Vánar and the fiend was seen. The Gods and Asurs stood amazed, And on the wondrous combat gazed. A cry from earth rose long and shrill, The wind was hushed, the sun grew chill. The thunder bellowed from the sky, And troubled ocean roared reply. Thrice Aksha strained his dreadful bow, Thrice smote his arrow on the foe, And with full streams of crimson bled Three gashes in the Vánar's head. Then rose Hanúmán in the air To shun the shafts no life could bear. But Aksha in his car pursued, And from on high the fight renewed With storm of arrows, thick as hail When angry clouds some hill assail. 877 RávaG's son.
- **Translation**: 

---

### Verse 19 (Ramayan 0.1499)
- **Original**: Canto XLVIII. Hanumán Captured. 1481 Impatient of that arrowy shower The Vánar chief put forth his power, Again above his chariot rose And smote him with repeated blows. Terrific came each deadly stroke: Breast neck and arm and back he broke; And Aksha fell to earth, and lay With all his life-blood drained away. Canto XLVIII. Hanumán Captured. To Indrajít878 the bold and brave The giant king his mandate gave: “O trained in warlike science, best In arms of all our mightiest, Whose valour in the conflict shown To Asurs and to Gods is known, The Kinkars whom I sent are slain, And Jambumálí and his train; The lords who led our giant bands Have fallen by the monkey's hands; With shattered cars the ground is spread, And Aksha lies amid the dead. Thou art my best and bravest: go, Unmatched in power, and slay the foe.” [421] He heard the hest: he bent his head; Athirst for battle forth he sped. Four tigers fierce, of tawny hue, With fearful teeth, his chariot drew. 878 Conqueror of Indra, another of RávaG's sons.
- **Translation**: 

---

### Verse 20 (Ramayan 0.1500)
- **Original**: 1482 The Ramayana Hanúmán heard his strong bow clang, And swiftly from the earth he sprang, While weak and ineffective fell The archer's shafts though pointed well. The Rákshas saw that naught might kill The wondrous foe who mocked his skill, And launched a magic shaft to throw A binding spell about his foe. Forth flew the shaft: the mystic charm Stayed his swift feet and numbed his arm, Through all his frame he felt the spell, And motionless to earth he fell. Nor would the reverent Vánar loose The bonds that bound him as a noose. He knew that Brahmá's self had charmed The weapon that his might disarmed. They saw him helpless on the ground, And all the giants pressed around, And bonds of hemp and bark were cast About his limbs to hold him fast. They drew the ropes round feet and wrists; They beat him with their hands and fists, And dragged him as they strained the cord With shouts of triumph to their lord.879 879 The [lokawhich follows is probably an interpolation, as it is inconsistent with the questioning in Canto L.: He looked on RávaG in his pride, And boldly to the monarch cried: “I came an envoy to this place From him who rules the Vánar race.”
- **Translation**: 

---

