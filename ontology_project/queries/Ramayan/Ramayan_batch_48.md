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

### Verse 1 (Ramayan 0.941)
- **Original**: Canto XXVIII. Khara Dismounted. 923 Canto XXVIII. Khara Dismounted. But when he turned his eye where bled Both Tri[irás and DúshaG dead, Fear o'er the giant's spirit came Of Ráma's might which naught could tame. He saw his savage legions, those Whose force no creature dared oppose,— He saw the leader of his train By Ráma's single prowess slain. With burning grief he marked the few Still left him of his giant crew. As Namuchi473 on Indra, so Rushed the dread demon on his foe. His mighty bow the monster strained, And angrily on Ráma rained His mortal arrows in a flood, Like serpent fangs athirst for blood. Skilled in the bowman's warlike art, He plied the string and poised the dart. Here, on his car, and there, he rode, And passages of battle showed, While all the skyey regions grew Dark with his arrows as they flew. Then Ráma seized his ponderous bow, And straight the heaven was all aglow With shafts whose stroke no life might bear That filled with flash and flame the air, 473 “This Asura was a friend of Indra, and taking advantage of his friend's confidence, he drank up Indra's strength along with a draught of wine and Soma. Indra then told the A[vins and Sarasvatí that Namuchi had drunk up his strength. The A[vins in consequence gave Indra a thunderbolt in the form of a foam, with which he smote off the head of Namuchi.” G ARRETT 'S{FNS Classical Dictionary of India. See also Book I. p. 39.
- **Translation**: 

---

### Verse 2 (Ramayan 0.942)
- **Original**: 924 The Ramayana Thick as the blinding torrents sent Down from Parjanya's474 firmament. In space itself no space remained, But all was filled with arrows rained Incessantly from each great bow Wielded by Ráma and his foe. As thus in furious combat, wrought To mortal hate, the warriors fought, The sun himself grew faint and pale, Obscured behind that arrowy veil. As when beneath the driver's steel An elephant is forced to kneel, So from the hard and pointed head Of many an arrow Ráma bled. High on his car the giant rose Prepared in deadly strife to close,[262] And all the spirits saw him stand Like Yáma with his noose in hand. For Khara deemed in senseless pride That he, beneath whose hand had died The giant legions, failed at length Slow sinking with exhausted strength. But Ráma, like a lion, when A trembling deer comes nigh his den, Feared not the demon mad with hate,— Of lion might and lion gait. Then in his lofty car that glowed With sunlike brilliance Khara rode At Ráma: madly on he came Like a poor moth that seeks the flame. His archer skill the fiend displayed, And at the place where Ráma laid 474 Indra.
- **Translation**: 

---

### Verse 3 (Ramayan 0.943)
- **Original**: Canto XXVIII. Khara Dismounted. 925 His hand, an arrow cleft in two The mighty bow the hero drew. Seven arrows by the giant sent, Bright as the bolts of Indra, rent Their way through mail and harness joints, And pierced him with their iron points. On Ráma, hero unsurpassed, A thousand shafts smote thick and fast, While as each missile struck, rang out The giant's awful battle-shout. His knotted arrows pierced and tore The sunbright mail the hero wore, Till, band and buckle rent away, Glittering on the ground it lay. Then pierced in shoulder, breast, and side, Till every limb with blood was dyed, The chieftain in majestic ire Shone glorious as the smokeless fire. Then loud and long the war-cry rose Of Ráma, terror of his foes, As, on the giant's death intent, A ponderous bow he strung and bent,— Lord VishGu's own, of wondrous size,— Agastya gave the heavenly prize. Then rushing on the demon foe, He raised on high that mighty bow, And with his well-wrought shafts, whereon Bright gold between the feathers shone, He struck the pennon fluttering o'er The chariot, and it waved no more. That glorious flag whose every fold Was rich with blazonry and gold, Fell as the sun himself by all The Gods' decree might earthward fall.
- **Translation**: 

---

### Verse 4 (Ramayan 0.944)
- **Original**: 926 The Ramayana From wrathful Khara's hand, whose art Well knew each vulnerable part, Four keenly-piercing arrows flew, And blood in Ráma's bosom drew, With every limb distained with gore From deadly shafts which rent and tore, From Khara's clanging bowstring shots, The prince's wrath waxed wondrous hot. His hand upon his bow that best Of mighty archers firmly pressed, And from the well-drawn bowstring, true Each to its mark, six arrows flew. One quivered in the giant's head, With two his brawny shoulders bled; Three, with the crescent heads they bore, Deep in his breast a passage tore. Thirteen, to which the stone had lent The keenest point, were swiftly sent On the fierce giant, every one Destructive, gleaming like the sun. With four the dappled steeds he slew; One cleft the chariot yoke in two, One, in the heat of battle sped, Smote from the neck the driver's head. The poles were rent apart by three; Two broke the splintered axle-tree. Then from the hand of Ráma, while Across his lips there came a smile, The twelfth, like thunderbolt impelled, Cut the great hand and bow it held. Then, scarce by Indra's self surpassed, He pierced the giant with the last. The bow he trusted cleft in twain, His driver and his horses slain,
- **Translation**: 

---

### Verse 5 (Ramayan 0.945)
- **Original**: Canto XXIX. Khara's Defeat. 927 Down sprang the giant, mace in hand, On foot against the foe to stand. The Gods and saints in bright array Close gathered in the skies, The prince's might in battle-fray Beheld with joyful eyes. Uprising from their golden seats, Their hands in honour raised, They looked on Ráma's noble feats, And blessed him as they praised. Canto XXIX. Khara's Defeat. When Ráma saw the giant nigh, On foot, alone, with mace reared high, In mild reproof at first he spoke, Then forth his threatening anger broke: “Thou with the host 'twas thine to lead, With elephant and car and steed, Hast wrought an act of sin and shame, An act which all who live must blame. Know that the wretch whose evil mind Joys in the grief of human kind, Though the three worlds confess him lord, Must perish dreaded and abhorred. Night-rover, when a villain's deeds Distress the world he little heeds, Each hand is armed his life to take, And crush him like a deadly snake. The end is near when men begin Through greed or lust a life of sin,
- **Translation**: 

---

### Verse 6 (Ramayan 0.946)
- **Original**: 928 The Ramayana E'en as a Bráhman's dame, unwise, Eats of the fallen hail475 and dies.[263] Thy hand has slain the pure and good, The hermit saints of DaG ak wood, Of holy life, the heirs of bliss; And thou shalt reap the fruit of this. Not long shall they whose cruel breasts Joy in the sin the world detests Retain their guilty power and pride, But fade like trees whose roots are dried. Yes, as the seasons come and go, Each tree its kindly fruit must show, And sinners reap in fitting time The harvest of each earlier crime. As those must surely die who eat Unwittingly of poisoned meat, They too whose lives in sin are spent Receive ere long the punishment. And know, thou rover of the night, That I, a king, am sent to smite The wicked down, who court the hate Of men whose laws they violate. This day my vengeful hand shall send Shafts bright with gold to tear and rend, And pass with fury through thy breast As serpents pierce an emmet's nest. Thou with thy host this day shalt be Among the dead below, and see The saints beneath thy hand who bled, Whose flesh thy cruel maw has fed. They, glorious on their seats of gold, Their slayer shall in hell behold. 475 Popularly supposed to cause death.
- **Translation**: 

---

### Verse 7 (Ramayan 0.947)
- **Original**: Canto XXIX. Khara's Defeat. 929 Fight with all strength thou callest thine, Mean scion of ignoble line, Still, like the palm-tree's fruit, this day My shafts thy head in dust shall lay.” Such were the words that Ráma said: Then Khara's eyes with wrath glowed red, Who, maddened by the rage that burned Within him, with a smile returned: “Thou Da[aratha's son, hast slain The meaner giants of my train: And canst thou idly vaunt thy might And claim the praise not thine by right? Not thus in self-laudation rave The truly great, the nobly brave: No empty boasts like thine disgrace The foremost of the human race. The mean of soul, unknown to fame, Who taint their warrior race with shame, Thus speak in senseless pride as thou, O Raghu's son, hast boasted now. What hero, when the war-cry rings, Vaunts the high race from which he springs, Or seeks, when warriors meet and die, His own descent to glorify? Weakness and folly show confessed In every vaunt thou utterest, As when the flames fed high with grass Detect the simulating brass. Dost thou not see me standing here Armed with the mighty mace I rear, Firm as an earth upholding hill Whose summit veins of metal fill?
- **Translation**: 

---

### Verse 8 (Ramayan 0.948)
- **Original**: 930 The Ramayana Lo, here I stand before thy face To slay thee with my murderous mace, As Death, the universal lord, Stands threatening with his fatal cord. Enough of this. Much more remains That should be said: but time constrains. Ere to his rest the sun descend, And shades of night the combat end, The twice seven thousand of my band Who fell beneath thy bloody hand Shall have their tears all wiped away And triumph in thy fall to-day.” He spoke, and loosing from his hold His mighty mace ringed round with gold, Like some red bolt alive with fire Hurled it at Ráma, mad with ire. The ponderous mace which Khara threw Sent fiery flashes as it flew. Trees, shrubs were scorched beneath the blast, As onward to its aim it passed. But Ráma, watching as it sped Dire as His noose who rules the dead, Cleft it with arrows as it came On rushing with a hiss and flame. Its fury spent and burnt away, Harmless upon the ground it lay Like a great snake in furious mood By herbs of numbing power subdued.
- **Translation**: 

---

### Verse 9 (Ramayan 0.949)
- **Original**: Canto XXX. Khara's Death. 931 Canto XXX. Khara's Death. When Ráma, pride of Raghu's race, Virtue's dear son, had cleft the mace, Thus with superior smile the best Of chiefs the furious fiend addressed: “Thou, worst of giant blood, at length Hast shown the utmost of thy strength, And forced by greater might to bow, Thy vaunting threats are idle now. My shafts have cut thy club in twain: Useless it lies upon the plain, And all thy pride and haughty trust Lie with it levelled in the dust. The words that thou hast said to-day, That thou wouldst wipe the tears away Of all the giants I have slain, My deeds shall render void and vain. Thou meanest of the giants' breed, Evil in thought and word and deed, My hand shall take that life of thine As Garu 476 seized the juice divine. [264] Thou, rent by shafts, this day shalt die: Low on the ground thy corse shall lie, And bubbles from the cloven neck With froth and blood thy skin shall deck. With dust and mire all rudely dyed, Thy torn arms lying by thy side, While streams of blood each limb shall steep, Thou on earth's breast shalt take thy sleep 476 Garu , the King of Birds, carried off the Amrit or drink of Paradise from Indra's custody.
- **Translation**: 

---

### Verse 10 (Ramayan 0.950)
- **Original**: 932 The Ramayana Like a fond lover when he strains The beauty whom at length he gains. Now when thy heavy eyelids close For ever in thy deep repose, Again shall DaG ak forest be Safe refuge for the devotee. Thou slain, and all thy race who held The realm of Janasthán expelled, Again shall happy hermits rove, Fearing no danger, through the grove. Within those bounds, their brethren slain, No giant shall this day remain, But all shall fly with many a tear And fearing, rid the saints of fear. This bitter day shall misery bring On all the race that calls thee king. Fierce as their lord, thy dames shall know, Bereft of joys, the taste of woe. Base, cruel wretch, of evil mind, Plaguer of Bráhmans and mankind, With trembling hands each devotee Feeds holy fires in dread of thee.” Thus with wild fury unrepressed Raghu's brave son the fiend addressed; And Khara, as his wrath grew high, Thus thundered forth his fierce reply: “By senseless pride to madness wrought, By danger girt thou fearest naught, Nor heedest, numbered with the dead, What thou shouldst say and leave unsaid. When Fate's tremendous coils enfold The captive in resistless hold,
- **Translation**: 

---

### Verse 11 (Ramayan 0.951)
- **Original**: Canto XXX. Khara's Death. 933 He knows not right from wrong, each sense Numbed by that deadly influence.” He spoke, and when his speech was done Bent his fierce brows on Raghu's son. With eager eyes he looked around If lethal arms might yet be found. Not far away and full in view A Sál-tree towering upward grew. His lips in mighty strain compressed, He tore it up with root and crest, With huge arms waved it o'er his head And hurled it shouting, Thou art dead. But Ráma, unsurpassed in might, Stayed with his shafts its onward flight, And furious longing seized his soul The giant in the dust to roll. Great drops of sweat each limb bedewed, His red eyes showed his wrathful mood. A thousand arrows, swiftly sent, The giant's bosom tore and rent. From every gash his body showed The blood in foamy torrents flowed, As springing from their caverns leap Swift rivers down the mountain steep. When Khara felt each deadened power Yielding beneath that murderous shower, He charged, infuriate with the scent Of blood, in dire bewilderment. But Ráma watched, with ready bow, The onset of his bleeding foe, And ere the monster reached him, drew Backward in haste a yard or two. Then from his side a shaft he took
- **Translation**: 

---

### Verse 12 (Ramayan 0.952)
- **Original**: 934 The Ramayana Whose mortal stroke no life might brook: Of peerless might, it bore the name Of Brahmá's staff, and glowed with flame: Lord Indra, ruler of the skies, Himself had given the glorious prize. His bow the virtuous hero drew, And at the fiend the arrow flew. Hissing and roaring like the blast Of tempest through the air it passed, And fixed, by Ráma's vigour sped, In the foe's breast its pointed head. Then fell the fiend: the quenchless flame Burnt furious in his wounded frame. So burnt by Rudra Andhak477 fell InZvetáraGya's silvery dell: So Namuchi and Vritra478 died By steaming bolts that tamed their pride: So Bala479 fell by lightning sent By Him who rules the firmament. Then all the Gods in close array With the bright hosts who sing and play, Filled full of rapture and amaze, Sang hymns of joy in Ráma's praise, Beat their celestial drums and shed Rain of sweet flowers upon his head. For three short hours had scarcely flown, And by his pointed shafts o'erthrown The twice seven thousand fiends, whose will 477 A demon, son of Ka[yap and Diti, slain by Rudra orZiva when he attempted to carry off the tree of Paradise. 478 Namuchi and Vritra were two demons slain by Indra. Vritra personifies drought, the enemy of Indra, who imprisons the rain in the cloud. 479 Another demon slain by Indra.
- **Translation**: 

---

### Verse 13 (Ramayan 0.953)
- **Original**: Canto XXX. Khara's Death. 935 Could change their shapes, in death were still, With Tri[irás and DúshaG slain, And Khara, leader of the train. “O wondrous deed,” the bards began, “The noblest deed of virtuous man! Heroic strength that stood alone, And firmness e'en as VishGu's own!” Thus having sung, the shining train Turned to their heavenly homes again. [265] Then the high saints of royal race And loftiest station sought the place, And by the great Agastya led, With reverence to Ráma said: “For this, Lord Indra, glorious sire, Majestic as the burning fire, Who crushes cities in his rage, SoughtZarabhanga's hermitage. Thou wast, this great design to aid, Led by the saints to seek this shade, And with thy mighty arm to kill The giants who delight in ill. Thou Da[aratha's noble son, The battle for our sake hast won, And saints in DaG ak's wild who live Their days to holy tasks can give.”
- **Translation**: 

---

### Verse 14 (Ramayan 0.954)
- **Original**: 936 The Ramayana Forth from the mountain cavern came The hero LakshmaG with the dame. And rapture beaming from his face, Resought the hermit dwelling-place. Then when the mighty saints had paid Due honour for the victor's aid, The glorious Ráma honoured too By LakshmaG to his cot withdrew. When Sítá looked upon her lord, His foemen slain, the saints restored, In pride and rapture uncontrolled She clasped him in her loving hold. On the dead fiends her glances fell: She saw her lord alive and well, Victorious after toil and pain, And Janak's child was blest again. Once more, once more with new delight Her tender arms she threw Round Ráma whose victorious might Had crushed the demon crew. Then as his grateful reverence paid Each saint of lofty soul, O'er her sweet face, all fears allayed, The flush of transport stole. Canto XXXI. Rávan. But of the host of giants one, Akampan, from the field had run And sped to Lanká480 to relate 480 The capital of the giant king RávaG.
- **Translation**: 

---

### Verse 15 (Ramayan 0.955)
- **Original**: Canto XXXI. Rávan. 937 In RávaG's ear the demons' fate: “King, many a giant from the shade Of Janasthán in death is laid: Khara the chief is slain, and I Could scarcely from the battle fly.” Fierce anger, as the monarch heard, Inflamed his look, his bosom stirred, And while with scorching glance he eyed The messenger, he thus replied: “What fool has dared, already dead, Strike Janasthán, the general dread? Who is the wretch shall vainly try In earth, heaven, hell, from me to fly? Vai[ravaG,481 Indra, VishGu, He Who rules the dead, must reverence me; For not the mightiest lord of these Can brave my will and live at ease. Fate finds in me a mightier fate To burn the fires that devastate. With unresisted influence I Can force e'en Death himself to die, With all-surpassing might restrain The fury of the hurricane, And burn in my tremendous ire The glory of the sun and fire.” 481 Kuvera, the God of gold.
- **Translation**: 

---

### Verse 16 (Ramayan 0.956)
- **Original**: 938 The Ramayana As thus the fiend's hot fury blazed, His trembling hands Akampan raised, And with a voice which fear made weak, Permission craved his tale to speak. King RávaG gave the leave he sought, And bade him tell the news he brought. His courage rose, his voice grew bold, And thus his mournful tale he told: “A prince with mighty shoulders, sprung From Da[aratha, brave and young, With arms well moulded, bears the name Of Ráma with a lion's frame. Renowned, successful, dark of limb, Earth has no warrior equals him. He fought in Janasthán and slew DúshaG the fierce and Khara too.” RávaG the giants' royal chief. Received Akampan's tale of grief. Then, panting like an angry snake, These words in turn the monarch spake: “Say quick, did Ráma seek the shade Of Janasthán with Indra's aid, And all the dwellers in the skies To back his hardy enterprise?” Akampan heard, and straight obeyed His master, and his answer made. Then thus the power and might he told Of Raghu's son the lofty-souled:
- **Translation**: 

---

### Verse 17 (Ramayan 0.957)
- **Original**: Canto XXXI. Rávan. 939 “Best is that chief of all who know With deftest art to draw the bow. His are strange arms of heavenly might, And none can match him in the fight. His brother LakshmaG brave as he, Fair as the rounded moon to see, With eyes like night and voice that comes Deep as the roll of beaten drums, By Ráma's side stands ever near, Like wind that aids the flame's career. That glorious chief, that prince of kings, On Janasthán this ruin brings. No Gods were there,— dismiss the thought No heavenly legions came and fought. His swift-winged arrows Ráma sent, Each bright with gold and ornament. To serpents many-faced they turned: [266] The giant hosts they ate and burned. Where'er these fled in wild dismay Ráma was there to strike and slay. By him O King of high estate, Is Janasthán left desolate.” Akampan ceased: in angry pride The giant monarch thus replied: “To Janasthán myself will go And lay these daring brothers low.” Thus spoke the king in furious mood: Akampan then his speech renewed: “O listen while I tell at length The terror of the hero's strength. No power can check, no might can tame Ráma, a chief of noblest fame.
- **Translation**: 

---

### Verse 18 (Ramayan 0.958)
- **Original**: 940 The Ramayana He with resistless shafts can stay The torrent foaming on its way. Sky, stars, and constellations, all To his fierce might would yield and fall. His power could earth itself uphold Down sinking as it sank of old.482 Or all its plains and cities drown, Breaking the wild sea's barrier down; Crush the great deep's impetuous will, Or bid the furious wind be still. He glorious in his high estate The triple world could devastate, And there, supreme of men, could place His creatures of a new-born race. Never can mighty Ráma be O'ercome in fight, my King, by thee. Thy giant host the day might win From him, if heaven were gained by sin. If Gods were joined with demons, they Could ne'er, I ween, that hero slay, But guile may kill the wondrous man; Attend while I disclose the plan. His wife, above all women graced, Is Sítá of the dainty waist, With limbs to fair proportion true, And a soft skin of lustrous hue, Round neck and arm rich gems are twined: She is the gem of womankind. With her no bright Gandharví vies, No nymph or Goddess in the skies; And none to rival her would dare 'Mid dames who part the long black hair. 482 In the great deluge.
- **Translation**: 

---

### Verse 19 (Ramayan 0.959)
- **Original**: Canto XXXI. Rávan. 941 That hero in the wood beguile, And steal his lovely spouse the while. Reft of his darling wife, be sure, Brief days the mourner will endure.” With flattering hope of triumph moved The giant king that plan approved, Pondered the counsel in his breast, And then Akampan thus addressed: “Forth in my car I go at morn, None but the driver with me borne, And this fair Sítá will I bring Back to my city triumphing.” Forth in his car by asses drawn The giant monarch sped at dawn, Bright as the sun, the chariot cast Light through the sky as on it passed. Then high in air that best of cars Traversed the path of lunar stars, Sending a fitful radiance pale As moonbeams shot through cloudy veil. Far on his airy way he flew: Near Tá akeya's483 grove he drew. Márícha welcomed him, and placed Before him food which giants taste, With honour led him to a seat, And brought him water for his feet; And then with timely words addressed Such question to his royal guest: 483 The giant Márícha, son of Tá aká. Tá aká was slain by Ráma. See p. 39.
- **Translation**: 

---

### Verse 20 (Ramayan 0.960)
- **Original**: 942 The Ramayana “Speak, is it well with thee whose sway The giant multitudes obey? I know not all, and ask in fear The cause, O King, why thou art here.” Ráva, the giants' mighty king, Heard wise Márícha's questioning, And told with ready answer, taught In eloquence, the cause he sought: “My guards, the bravest of my band, Are slain by Ráma's vigorous hand, And Janasthán, that feared no hate Of foes, is rendered desolate. Come, aid me in the plan I lay To steal the conqueror's wife away.” Márícha heard the king's request, And thus the giant chief addressed: “What foe in friendly guise is he Who spoke of Sítá's name to thee? Who is the wretch whose thought would bring Destruction on the giants' king? Whose is the evil counsel, say, That bids thee bear his wife away, And careless of thy life provoke Earth's loftiest with threatening stroke? A foe is he who dared suggest This hopeless folly to thy breast, Whose ill advice would bid thee draw The venomed fang from serpent's jaw. By whose unwise suggestion led Wilt thou the path of ruin tread? Whence falls the blow that would destroy Thy gentle sleep of ease and joy?
- **Translation**: 

---

