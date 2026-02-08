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

### Verse 1 (Ramayan 0.1501)
- **Original**: Canto XLIX. Rávan. 1483 Canto XLIX. Rávan. On the fierce king Hanúmán turned His angry eyes that glowed and burned. He saw him decked with wealth untold Of diamond and pearl and gold, And priceless was each wondrous gem That sparkled in his diadem. About his neck rich chains were twined, The best that fancy e'er designed, And a fair robe with pearls bestrung Down from his mighty shoulders hung. Ten heads he reared,880 as Mandar's hill Lifts woody peaks which tigers fill, Bright were his eyes, and bright, beneath, The flashes of his awful teeth. His brawny arms of wondrous size Were decked with rings and scented dyes. His hands like snakes with five long heads Descending from their mountain beds. He sat upon a crystal throne Inlaid with wealth of precious stone, Whereon, of noblest work, was set A gold-embroidered coverlet. Behind the monarch stood the best Of beauteous women gaily dressed, And each her giant master fanned, Or waved a chourie in her hand. 880 The ten heads of RávaG have provoked much ridicule from European critics. It should be remembered that Spenser tells us of“two brethren giants, the one of which had two heads, the other three;” and Milton speaks of the“four-fold visaged Four,” the four Cherubic shapes each of whom had four faces.
- **Translation**: 

---

### Verse 2 (Ramayan 0.1502)
- **Original**: 1484 The Ramayana Four noble courtiers881 wise and good In counsel, near the monarch stood, As the four oceans ever stand About the sea-encompassed land. Still, though his heart with rage was fired, The Vánar marvelled and admired: “O what a rare and wondrous sight! What beauty, majesty, and might! All regal pomp combines to grace This ruler of the Rákshas race. He, if he scorned not right and law, Might guide the world with tempered awe: Yea, Indra and the Gods on high Might on his saving power rely.” Canto L. Prahasta's Questions. Then fierce the giant's fury blazed As on Hanúmán's form he gazed, And shaken by each wild surmise He spake aloud with flashing eyes: “Can this be Nandi882 standing here, The mighty one whom all revere? Who once on high Kailása's hill Pronounced the curse that haunts me still? Or is the woodland creature one 881 Durdhar, or as the Bengal recension reads Mahodara, Prahasta, Mahápár[va, and Nikumbha. 882 The chief attendant ofZiva.
- **Translation**: 

---

### Verse 3 (Ramayan 0.1503)
- **Original**: Canto L. Prahasta's Questions. 1485 Of Asur race, or Bali's883 son? The wretch with searching question try: Learn who he is, and whence; and why He marred the glory of the grove, And with my captains fiercely strove.” [422] Prahasta heard his lord's behest, And thus the Vánar chief addressed: “O monkey stranger be consoled: Fear not, and let thy heart be bold. If thou by Indra's mandate sent Thy steps to Lanká's isle hast bent, With fearless words the cause explain, And freedom thou shalt soon regain. Or if thou comest as a spy Despatched by VishGu in the sky, Or sent by Yáma, or the Lord Of Riches, hast our town explored; Proved by the prowess thou hast shown No monkey save in form alone; Speak boldly all the truth, and be Released from bonds, unharmed and free. But falsehood spoken to our king Swift punishment of death will bring.” He ceased: the Vánar made reply; “Not Indra's messenger am I, Nor came I hither to fulfil Kuvera's hest or VishGu's will. I stand before the giants here A Vánar e'en as I appear. I longed to see the king: 'twas hard 883 Bali, not to be confounded with Báli the Vánar, was a celebrated Daitya or demon who had usurped the empire of the three worlds, and who was deprived of two thirds of his dominions by VishGu in the Dwarf-incarnation.
- **Translation**: 

---

### Verse 4 (Ramayan 0.1504)
- **Original**: 1486 The Ramayana To win my way through gate and guard. And so to gain my wish I laid In ruin that delightful shade. No fiend, no God of heavenly kind With bond or chain these limbs may bind. The Eternal Sire himself of old Vouchsafed the boon that makes me bold, From Brahmá's magic shaft released884 I knew the captor's power had ceased, The fancied bonds I freely brooked, And thus upon the king have looked. My way to Lanká have I won, A messenger from Raghu's son.” Canto LI. Hanumán's Reply. “My king Sugríva greets thee fair, And bids me thus his rede declare. Son of the God of Wind, by name Hanumán, to this isle I came. To set the Maithil lady free I crossed the barrier of the sea. I roamed in search of her and found Her weeping in that lovely ground. Thou in the lore of duty trained, Who hast by stern devotion gained This wondrous wealth and power and fame Shouldst fear to wrong another's dame. 884 When Hanumán was bound with cords, Indrajít released his captive from the spell laid upon him by the magic weapon.
- **Translation**: 

---

### Verse 5 (Ramayan 0.1505)
- **Original**: Canto LI. Hanumán's Reply. 1487 Hear thou my counsel, and be wise: No fiend, no dweller in the skies Can bear the shafts by LakshmaG shot, Or Ráma when his wrath is hot. O Giant King, repent the crime And soothe him while there yet is time. Now be the Maithil queen restored Uninjured to her sorrowing lord. Soon wilt thou rue thy dire mistake: She is no woman but a snake, Whose very deadly bite will be The ruin of thy house and thee. Thy pride has led thy thoughts astray, That fancy not a hand may slay The monarch of the giants, screened From mortal blow of God and fiend. Sugríva still thy death may be: No Yaksha, fiend, or God is he, And Ráma from a woman springs, The mortal seed of mortal kings. O think how Báli fell subdued; Think on thy slaughtered multitude. Respect those brave and strong allies; Consult thy safety, and be wise. I, even I, no helper need To overthrow, with car and steed, Thy city Lanká half divine: The power but not the will is mine. For Raghu's son, before his friend The Vánar monarch, swore to end With his own conquering arm the life Of him who stole his darling wife. Turn, and be wise, O RávaG turn; Or thou wilt see thy Lanká burn,
- **Translation**: 

---

### Verse 6 (Ramayan 0.1506)
- **Original**: 1488 The Ramayana And with thy wives, friends, kith and kin Be ruined for thy senseless sin.” Canto LII. Vibhishan's Speech. Then RávaG spake with flashing eye: “Hence with the Vánar: let him die.” VibhishaG heard the stern behest, And pondered in his troubled breast; Then, trained in arts that soothe and please Addressed the king in words like these: “Revoke, my lord, thy fierce decree, And hear the words I speak to thee. Kings wise and noble ne'er condemn To death the envoys sent to them. Such deed the world's contempt would draw On him who breaks the ancient law.885 Observe the mean where justice lies, And spare his life but still chastise.”[423] Then forth the tyrant's fury broke, And thus in angry words he spoke: “O hero, when the wicked bleed No sin or shame attends the deed. The Vánar's blood must needs be spilt, The penalty of heinous guilt.” 885 “One who murders an ambassador (rája bhata) goes to Taptakumbha, the hell of heated caldrons.” W ILSON 'S{FNS VishGu PuraGa, Vol. II. p. 217.
- **Translation**: 

---

### Verse 7 (Ramayan 0.1507)
- **Original**: Canto LIII. The Punishment. 1489 Again VibhishaG made reply: “Nay, hear me, for he must not die. Hear the great law the wise declare: “Thy foeman's envoy thou shalt spare.” 'Tis true he comes an open foe: 'Tis true his hands have wrought us woe, But law allows thee, if thou wilt, A punishment to suit the guilt. The mark of shame, the scourge, the brand, The shaven head, the wounded hand. Yea, were the Vánar envoy slain, Where, King of giants, were the gain? On them alone, on them who sent The message, be the punishment. For spake he well or spake he ill, He spake obedient to their will, And, if he perish, who can bear Thy challenge to the royal pair? Who, cross the ocean and incite Thy death-doomed enemies to fight?” Canto LIII. The Punishment. King RávaG, by his pleading moved, The counsel of the chief approved: “Thy words are wise and true: to kill An envoy would beseem us ill. Yet must we for his crime invent Some fitting mode of punishment. The tail, I fancy, is the part Most cherished by a monkey's heart.
- **Translation**: 

---

### Verse 8 (Ramayan 0.1508)
- **Original**: 1490 The Ramayana Make ready: set his tail aflame, And let him leave us as he came, And thus disfigured and disgraced Back to his king and people haste.” The giants heard their monarch's speech; And, filled with burning fury, each Brought strips of cotton cloth, and round The monkey's tail the bandage wound. As round his tail the bands they drew His mighty form dilating grew Vast as the flame that bursts on high Where trees are old and grass is dry. Each band and strip they soaked in oil, And set on fire the twisted coil. Delighted as they viewed the blaze, The cruel demons stood at gaze: And mid loud drums and shells rang out The triumph of their joyful shout. They pressed about him thick and fast As through the crowded streets he passed, Observing with attentive care Each rich and wondrous structure there, Still heedless of the eager cry That rent the air, The spy! the spy! Some to the captive lady ran, And thus in joyous words began: “That copper-visaged monkey, he Who in the garden talked with thee, Through Lanká's town is led a show, And round his tail the red flames glow.” The mournful news the lady heard That with fresh grief her bosom stirred.
- **Translation**: 

---

### Verse 9 (Ramayan 0.1509)
- **Original**: Canto LIV. The Burning Of Lanká. 1491 Swift to the kindled fire she went And prayed before it reverent: “If I my husband have obeyed, And kept the ascetic vows I made, Free, ever free, from stain and blot, O spare the Vánar; harm him not.” Then leapt on high the flickering flame And shone in answer to the dame. The pitying fire its rage forbore: The Vánar felt the heat no more. Then, to minutest size reduced, The bonds that bound his limbs he loosed, And, freed from every band and chain, Rose to his native size again. He seized a club of ponderous weight That lay before him by the gate, Rushed at the fiends that hemmed him round, And laid them lifeless on the ground. Through Lanká's town again he strode, And viewed each street and square and road,— Still wreathed about with harmless blaze, A sun engarlanded with rays. [424] Canto LIV. The Burning Of Lanká.
- **Translation**: 

---

### Verse 10 (Ramayan 0.1510)
- **Original**: 1492 The Ramayana “What further deed remains to do To vex the Rákshas king anew? The beauty of his grove is marred, Killed are the bravest of his guard. The captains of his host are slain; But forts and palaces remain, Swift is the work and light the toil Each fortress of the foe to spoil.” Reflecting thus, his tail ablaze As through the cloud red lightning plays, He scaled the palaces and spread The conflagration where he sped. From house to house he hurried on, And the wild flames behind him shone. Each mansion of the foe he scaled, And furious fire its roof assailed Till all the common ruin shared: VibhishaG's house alone was spared. From blazing pile to pile he sprang, And loud his shout of triumph rang, As roars the doomsday cloud when all The worlds in dissolution fall. The friendly wind conspired to fan The hungry flames that leapt and ran, And spreading in their fury caught The gilded walls with pearls inwrought, Till each proud palace reeled and fell As falls a heavenly citadel.
- **Translation**: 

---

### Verse 11 (Ramayan 0.1511)
- **Original**: Canto LV. Fear For Sítá. 1493 Loud was the roar the demons raised Mid walls that split and beams that blazed, As each with vain endeavour strove To stay the flames in house or grove. The women, with dishevelled hair, Flocked to the roofs in wild despair, Shrieked out for succour, wept aloud, And fell, like lightning from a cloud. He saw the flames ascend and curl Round turkis, diamond, and pearl, While silver floods and molten gold From ruined wall and latice rolled. As fire grows fiercer as he feeds On wood and grass and crackling reeds, So Hanúmán the ruin eyed With fury still unsatisfied. Canto LV. Fear For Sítá. But other thoughts resumed their sway When Lanká's town in ruin lay; And, as his bosom felt their weight He stood a while to meditate. “What have I done?”, he thought with shame, “Destroyed the town with hostile flame. O happy they whose firm control Checks the wild passion of the soul; Who on the fires of anger throw The cooling drops that check their glow. But woe is me, whom wrath could lead To do this senseless shameless deed.
- **Translation**: 

---

### Verse 12 (Ramayan 0.1512)
- **Original**: 1494 The Ramayana The town to fire and death I gave, Nor thought of her I came to save,— Doomed by my own rash folly, doomed To perish in the flames consumed. If I, when anger drove me wild, Have caused the death of Janak's child, The kindled flame shall end my woe, Or the deep fires that burn below,886 Or my forsaken corse shall be Food for the monsters of the sea. How can I meet Sugríva? how Before the royal brothers bow,— I whose rash deed has madly foiled, The noble work in which we toiled? Or has her own bright virtue shed Its guardian influence round her head? She lives untouched,— the peerless dame; Flame has no fury for the flame.887 The very fire would ne'er consent To harm a queen so excellent,— The high-souled Ráma's faithful wife, Protected by her holy life. She lives, she lives. Why should I fear For one whom Raghu's sons hold dear? Has not the pitying fire that spared The Vánar for the lady cared?” Such were his thoughts: he pondered long, And fear grew faint and hope grew strong. Then round him heavenly voices rang, And, sweetly tuned, his praises sang: “O glorious is the exploit done 886 The fire which is supposed to burn beneath the sea. 887 Sítá is likened to the fire which is an emblem of purity.
- **Translation**: 

---

### Verse 13 (Ramayan 0.1513)
- **Original**: Canto LVI. Mount Arishta. 1495 By Hanumán the Wind-God's son. The flames o'er Lanká's city rise: The giants' home in ruin lies. O'er roof and wall the fires have spread, Nor harmed a hair of Sítá's head.” Canto LVI. Mount Arishta. He looked upon the burning waste, Then sought the queen in joyous haste, With words of hope consoled her heart, And made him ready to depart. [425] He scaled Arishma's glorious steep Whose summits beetled o'er the deep. The woods in varied beauty dressed Hung like a garland round his crest, And clouds of ever changing hue A robe about his shoulders threw. On him the rays of morning fell To wake the hill they loved so well, And bid unclose those splendid eyes That glittered in his mineral dyes. He woke to hear the music made By thunders of the white cascade, While every laughing rill that sprang From crag to crag its carol sang. For arms, he lifted to the stars His towering stems of Deodárs, And morning heard his pealing call In tumbling brook and waterfall. He trembled when his woods were pale
- **Translation**: 

---

### Verse 14 (Ramayan 0.1514)
- **Original**: 1496 The Ramayana And bowed beneath the autumn gale, And when his vocal reeds were stirred His melancholy moan was heard. Far down against the mountain's feet The Vánar heard the wild waves beat; Then turned his glances to the north. Sprang from the peak and bounded forth, The mountain felt the fearful shock And trembled through his mass of rock. The tallest trees were crushed and rent And headlong to the valley sent, And as the rocking shook each cave Loud was the roar the lions gave. Forth from the shaken cavern came Fierce serpents with their tongues aflame; And every Yaksha, wild with dread, And Kinnar and Gandharva, fled. Canto LVII. Hanumán's Return. Still, like a winged mountain, he Sprang forward through the airy sea,888 888 I omit two stanzas which continue the metaphor of the sea or lake of air. The moon is its lotus, the sun its wild-duck, the clouds are its water-weeds, Mars is its shark and so on. Gorresio remarks:“This comparison of a great lake to the sky and of celestial to aquatic objects is one of those ideas which the view and qualities of natural scenery awake in lively fancies. Imagine one of those grand and splendid lakes of India covered with lotus blossoms, furrowed by wild-ducks of the most vivid colours, mantled over here and there with flowers and water weeds &c. and it will be understood how the fancy of the poet could readily compare to the sky radiant with celestial azure the blue expanse of the
- **Translation**: 

---

### Verse 15 (Ramayan 0.1515)
- **Original**: Canto LVII. Hanumán's Return. 1497 And rushing through the ether drew The clouds to follow as he flew, Through the great host around him spread, Grey, golden, dark, and white, and red. Now in a sable cloud immersed, Now from its gloomy pall he burst, Like the bright Lord of Stars concealed A moment, and again revealed. Sunábha889 passed, he neared the coast Where waited still the Vánar host. They heard a rushing in the skies, And lifted up their wondering eyes. His wild triumphant shout they knew That louder still and louder grew, And Jámbaván with eager voice Called on the Vánars to rejoice: “Look he returns, the Wind-God's son, And full success his toils have won; Triumphant is the shout that comes Like music of a thousand drums.” Up sprang the Vánars from the ground And listened to the wondrous sound Of hurtling arm and thigh as through The region of the air he flew, Loud as the wind, when tempests rave, Roars in the prison of the cave. From crag to crag, from height to height; They bounded in their mad delight, And when he touched the mountain's crest, water, to the soft light of the moon the inner hue of the lotus, to the splendour of the sun the brilliant colours of the wild-fowl, to the stars the flowers, to the cloud the weeds that float upon the water &c.” 889 Sunábha is the mountain that rose from the sea when Hanumán passed over to Lanká.
- **Translation**: 

---

### Verse 16 (Ramayan 0.1516)
- **Original**: 1498 The Ramayana With reverent welcome round him pressed. They brought him of their woodland fruits, They brought him of the choicest roots, And laughed and shouted in their glee The noblest of their chiefs to see. Nor Hanumán delayed to greet Sage Jámbaván with reverence meet; To Angad and the chiefs he bent For age and rank preëminent, And briefly spoke:“These eyes have seen, These lips addressed, the Maithil queen.” They sat beneath the waving trees, And Angad spoke in words like these: “O noblest of the Vánar kind For valour power and might combined, To thee triumphant o'er the foe Our hopes, our lives and all we owe. O faithful heart in perils tried,[426] Which toil nor fear could turn aside, Thy deed the lady will restore, And Ráma's heart will ache no more.”890 Canto LVIII. The Feast Of Honey. They rose in air: the region grew Dark with their shadow as they flew. Swift to a lovely grove891 they came That rivalled heavenly Nandan's892 fame; 890 Three Cantos of repetition are omitted. 891 Madhuvan the“honey-wood.” 892 Indra's pleasure-ground or elysium.
- **Translation**: 

---

### Verse 17 (Ramayan 0.1517)
- **Original**: Canto LVIII. The Feast Of Honey. 1499 Where countless bees their honey stored,— The pleasance of the Vánars' lord, To every creature fenced and barred, Which Dadhimukh was set to guard, A noble Vánar, brave and bold, Sugríva's uncle lofty-souled. To Angad came with one accord The Vánars, and besought their lord That they those honeyed stores might eat That made the grove so passing sweet. He gave consent: they sought the trees Thronged with innumerable bees. They rifled all the treasured store, And ate the fruit the branches bore, And still as they prolonged the feast Their merriment and joy increased. Drunk with the sweets, they danced and bowed, They wildly sang, they laughed aloud, Some climbed and sprang from tree to tree, Some sat and chattered in their glee. Some scaled the trees which creepers crowned, And rained the branches to the ground. There with loud laugh a Vánar sprang Close to his friend who madly sang, In doleful mood another crept To mix his tears with one who wept. Then Dadhimukh with fury viewed The intoxicated multitude. He looked upon the rifled shade, And all the ruin they had made; Then called with angry voice, and strove To save the remnant of the grove.
- **Translation**: 

---

### Verse 18 (Ramayan 0.1518)
- **Original**: 1500 The Ramayana But warning cries and words were spurned, And angry taunt and threat returned. Then fierce and wild contention rose: With furious words he mingled blows. They by no shame or fear withheld, By drunken mood and ire impelled, Used claws, and teeth, and hands, and beat The keeper under trampling feet. [Three Cantos consisting of little but repetitions are omitted. Dadhimukh escapes from the infuriated monkeys and hastens to Sugríva to report their misconduct. Sugríva infers that Hanumán and his band have been successful in their search, and that the exuberance of spirits and the mischief complained of, are but the natural expression of their joy. Dadhimukh obtains little sympa- thy from Sugríva, and is told to return and send the monkeys on with all possible speed.] Canto LXV. The Tidings. On to Pra[ravaG's hill they sped Where blooming trees their branches spread. To Raghu's sons their heads they bent And did obeisance reverent. Then to their king, by Angad led, Each Vánar chieftain bowed his head; And Hanumán the brave and bold His tidings to the monarch told; But first in Ráma's hand he placed The gem that Sítá's brow had graced: “I crossed the sea: I searched a while For Sítá in the giants' isle.
- **Translation**: 

---

### Verse 19 (Ramayan 0.1519)
- **Original**: Canto LXVI. Ráma's Speech. 1501 I found her vext with taunt and threat By demon guards about her set. Her tresses twined in single braid, On the bare earth her limbs were laid. Sad were her eyes: her cheeks were pale As shuddering flowers in winter's gale. I stood beside the weeping dame, And gently whispered Ráma's name: With cheering words her grief consoled, And then the whole adventure told. She weeps afar beyond the sea, And her true heart is still with thee. She gave a sign that thou wouldst know, She bids thee think upon the crow, And bright mark pressed upon her brow When none was nigh but she and thou. She bids thee take this precious stone, The sea-born gem thou long hast known. “And I,” she said,“will dull the sting Of woe by gazing on the ring. One little month shall I sustain This life oppressed with woe and pain: And when the month is ended, I The giants' prey must surely die.’ ” [427] Canto LXVI. Ráma's Speech.
- **Translation**: 

---

### Verse 20 (Ramayan 0.1520)
- **Original**: 1502 The Ramayana There ceased the Vánar: Ráma pressed The treasured jewel to his breast, And from his eyes the waters broke As to the Vánar king he spoke: “As o'er her babe the mother weeps, This flood of tears the jewel steeps. This gem that shone on Sítá's head Was Janak's gift when we were wed, And the pure brow that wore it lent New splendour to the ornament. This gem, bright offspring of the wave, The King of Heaven to Janak gave, Whose noble sacrificial rite Had filled the God with new delight. Now, as I gaze upon the prize, Methinks I see my father's eyes. Methinks I see before me stand The ruler of Videha's land.893 Methinks mine arms are folded now Round her who wore it on her brow. Speak, Hanumán, O say, dear friend, What message did my darling send? O speak, and let thy words impart Their gentle dew to cool my heart. Ah, 'tis the crown of woe to see This gem and ask“Where, where is she?” If for one month her heart be strong, Her days of life will yet be long. But I, with naught to lend relief, This very day must die of grief. Come, Hanumán, and quickly guide The mourner to his darling's side. 893 Janak was king of Videha or Mithilá in Behar.
- **Translation**: 

---

