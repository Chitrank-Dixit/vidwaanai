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

### Verse 1 (Ramayana 0.1506)
- **Original**: 1488 The Ramayana And with thy wives, friends, kith and kin Be ruined for thy senseless sin.” Canto LII. Vibhishan's Speech. Then RávaG spake with flashing eye: “Hence with the Vánar: let him die.” VibhishaG heard the stern behest, And pondered in his troubled breast; Then, trained in arts that soothe and please Addressed the king in words like these: “Revoke, my lord, thy fierce decree, And hear the words I speak to thee. Kings wise and noble ne'er condemn To death the envoys sent to them. Such deed the world's contempt would draw On him who breaks the ancient law.885 Observe the mean where justice lies, And spare his life but still chastise.”[423] Then forth the tyrant's fury broke, And thus in angry words he spoke: “O hero, when the wicked bleed No sin or shame attends the deed. The Vánar's blood must needs be spilt, The penalty of heinous guilt.” 885 “One who murders an ambassador (rája bhata) goes to Taptakumbha, the hell of heated caldrons.” W ILSON 'S{FNS VishGu PuraGa, Vol. II. p. 217.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1507)
- **Original**: Canto LIII. The Punishment. 1489 Again VibhishaG made reply: “Nay, hear me, for he must not die. Hear the great law the wise declare: “Thy foeman's envoy thou shalt spare.” 'Tis true he comes an open foe: 'Tis true his hands have wrought us woe, But law allows thee, if thou wilt, A punishment to suit the guilt. The mark of shame, the scourge, the brand, The shaven head, the wounded hand. Yea, were the Vánar envoy slain, Where, King of giants, were the gain? On them alone, on them who sent The message, be the punishment. For spake he well or spake he ill, He spake obedient to their will, And, if he perish, who can bear Thy challenge to the royal pair? Who, cross the ocean and incite Thy death-doomed enemies to fight?” Canto LIII. The Punishment. King RávaG, by his pleading moved, The counsel of the chief approved: “Thy words are wise and true: to kill An envoy would beseem us ill. Yet must we for his crime invent Some fitting mode of punishment. The tail, I fancy, is the part Most cherished by a monkey's heart.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1508)
- **Original**: 1490 The Ramayana Make ready: set his tail aflame, And let him leave us as he came, And thus disfigured and disgraced Back to his king and people haste.” The giants heard their monarch's speech; And, filled with burning fury, each Brought strips of cotton cloth, and round The monkey's tail the bandage wound. As round his tail the bands they drew His mighty form dilating grew Vast as the flame that bursts on high Where trees are old and grass is dry. Each band and strip they soaked in oil, And set on fire the twisted coil. Delighted as they viewed the blaze, The cruel demons stood at gaze: And mid loud drums and shells rang out The triumph of their joyful shout. They pressed about him thick and fast As through the crowded streets he passed, Observing with attentive care Each rich and wondrous structure there, Still heedless of the eager cry That rent the air, The spy! the spy! Some to the captive lady ran, And thus in joyous words began: “That copper-visaged monkey, he Who in the garden talked with thee, Through Lanká's town is led a show, And round his tail the red flames glow.” The mournful news the lady heard That with fresh grief her bosom stirred.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1509)
- **Original**: Canto LIV. The Burning Of Lanká. 1491 Swift to the kindled fire she went And prayed before it reverent: “If I my husband have obeyed, And kept the ascetic vows I made, Free, ever free, from stain and blot, O spare the Vánar; harm him not.” Then leapt on high the flickering flame And shone in answer to the dame. The pitying fire its rage forbore: The Vánar felt the heat no more. Then, to minutest size reduced, The bonds that bound his limbs he loosed, And, freed from every band and chain, Rose to his native size again. He seized a club of ponderous weight That lay before him by the gate, Rushed at the fiends that hemmed him round, And laid them lifeless on the ground. Through Lanká's town again he strode, And viewed each street and square and road,— Still wreathed about with harmless blaze, A sun engarlanded with rays. [424] Canto LIV. The Burning Of Lanká.
- **Translation**: 

---

### Verse 5 (Ramayana 0.1510)
- **Original**: 1492 The Ramayana “What further deed remains to do To vex the Rákshas king anew? The beauty of his grove is marred, Killed are the bravest of his guard. The captains of his host are slain; But forts and palaces remain, Swift is the work and light the toil Each fortress of the foe to spoil.” Reflecting thus, his tail ablaze As through the cloud red lightning plays, He scaled the palaces and spread The conflagration where he sped. From house to house he hurried on, And the wild flames behind him shone. Each mansion of the foe he scaled, And furious fire its roof assailed Till all the common ruin shared: VibhishaG's house alone was spared. From blazing pile to pile he sprang, And loud his shout of triumph rang, As roars the doomsday cloud when all The worlds in dissolution fall. The friendly wind conspired to fan The hungry flames that leapt and ran, And spreading in their fury caught The gilded walls with pearls inwrought, Till each proud palace reeled and fell As falls a heavenly citadel.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1511)
- **Original**: Canto LV. Fear For Sítá. 1493 Loud was the roar the demons raised Mid walls that split and beams that blazed, As each with vain endeavour strove To stay the flames in house or grove. The women, with dishevelled hair, Flocked to the roofs in wild despair, Shrieked out for succour, wept aloud, And fell, like lightning from a cloud. He saw the flames ascend and curl Round turkis, diamond, and pearl, While silver floods and molten gold From ruined wall and latice rolled. As fire grows fiercer as he feeds On wood and grass and crackling reeds, So Hanúmán the ruin eyed With fury still unsatisfied. Canto LV. Fear For Sítá. But other thoughts resumed their sway When Lanká's town in ruin lay; And, as his bosom felt their weight He stood a while to meditate. “What have I done?”, he thought with shame, “Destroyed the town with hostile flame. O happy they whose firm control Checks the wild passion of the soul; Who on the fires of anger throw The cooling drops that check their glow. But woe is me, whom wrath could lead To do this senseless shameless deed.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1512)
- **Original**: 1494 The Ramayana The town to fire and death I gave, Nor thought of her I came to save,— Doomed by my own rash folly, doomed To perish in the flames consumed. If I, when anger drove me wild, Have caused the death of Janak's child, The kindled flame shall end my woe, Or the deep fires that burn below,886 Or my forsaken corse shall be Food for the monsters of the sea. How can I meet Sugríva? how Before the royal brothers bow,— I whose rash deed has madly foiled, The noble work in which we toiled? Or has her own bright virtue shed Its guardian influence round her head? She lives untouched,— the peerless dame; Flame has no fury for the flame.887 The very fire would ne'er consent To harm a queen so excellent,— The high-souled Ráma's faithful wife, Protected by her holy life. She lives, she lives. Why should I fear For one whom Raghu's sons hold dear? Has not the pitying fire that spared The Vánar for the lady cared?” Such were his thoughts: he pondered long, And fear grew faint and hope grew strong. Then round him heavenly voices rang, And, sweetly tuned, his praises sang: “O glorious is the exploit done 886 The fire which is supposed to burn beneath the sea. 887 Sítá is likened to the fire which is an emblem of purity.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1513)
- **Original**: Canto LVI. Mount Arishta. 1495 By Hanumán the Wind-God's son. The flames o'er Lanká's city rise: The giants' home in ruin lies. O'er roof and wall the fires have spread, Nor harmed a hair of Sítá's head.” Canto LVI. Mount Arishta. He looked upon the burning waste, Then sought the queen in joyous haste, With words of hope consoled her heart, And made him ready to depart. [425] He scaled Arishma's glorious steep Whose summits beetled o'er the deep. The woods in varied beauty dressed Hung like a garland round his crest, And clouds of ever changing hue A robe about his shoulders threw. On him the rays of morning fell To wake the hill they loved so well, And bid unclose those splendid eyes That glittered in his mineral dyes. He woke to hear the music made By thunders of the white cascade, While every laughing rill that sprang From crag to crag its carol sang. For arms, he lifted to the stars His towering stems of Deodárs, And morning heard his pealing call In tumbling brook and waterfall. He trembled when his woods were pale
- **Translation**: 

---

### Verse 9 (Ramayana 0.1514)
- **Original**: 1496 The Ramayana And bowed beneath the autumn gale, And when his vocal reeds were stirred His melancholy moan was heard. Far down against the mountain's feet The Vánar heard the wild waves beat; Then turned his glances to the north. Sprang from the peak and bounded forth, The mountain felt the fearful shock And trembled through his mass of rock. The tallest trees were crushed and rent And headlong to the valley sent, And as the rocking shook each cave Loud was the roar the lions gave. Forth from the shaken cavern came Fierce serpents with their tongues aflame; And every Yaksha, wild with dread, And Kinnar and Gandharva, fled. Canto LVII. Hanumán's Return. Still, like a winged mountain, he Sprang forward through the airy sea,888 888 I omit two stanzas which continue the metaphor of the sea or lake of air. The moon is its lotus, the sun its wild-duck, the clouds are its water-weeds, Mars is its shark and so on. Gorresio remarks:“This comparison of a great lake to the sky and of celestial to aquatic objects is one of those ideas which the view and qualities of natural scenery awake in lively fancies. Imagine one of those grand and splendid lakes of India covered with lotus blossoms, furrowed by wild-ducks of the most vivid colours, mantled over here and there with flowers and water weeds &c. and it will be understood how the fancy of the poet could readily compare to the sky radiant with celestial azure the blue expanse of the
- **Translation**: 

---

### Verse 10 (Ramayana 0.1515)
- **Original**: Canto LVII. Hanumán's Return. 1497 And rushing through the ether drew The clouds to follow as he flew, Through the great host around him spread, Grey, golden, dark, and white, and red. Now in a sable cloud immersed, Now from its gloomy pall he burst, Like the bright Lord of Stars concealed A moment, and again revealed. Sunábha889 passed, he neared the coast Where waited still the Vánar host. They heard a rushing in the skies, And lifted up their wondering eyes. His wild triumphant shout they knew That louder still and louder grew, And Jámbaván with eager voice Called on the Vánars to rejoice: “Look he returns, the Wind-God's son, And full success his toils have won; Triumphant is the shout that comes Like music of a thousand drums.” Up sprang the Vánars from the ground And listened to the wondrous sound Of hurtling arm and thigh as through The region of the air he flew, Loud as the wind, when tempests rave, Roars in the prison of the cave. From crag to crag, from height to height; They bounded in their mad delight, And when he touched the mountain's crest, water, to the soft light of the moon the inner hue of the lotus, to the splendour of the sun the brilliant colours of the wild-fowl, to the stars the flowers, to the cloud the weeds that float upon the water &c.” 889 Sunábha is the mountain that rose from the sea when Hanumán passed over to Lanká.
- **Translation**: 

---

### Verse 11 (Ramayana 0.1516)
- **Original**: 1498 The Ramayana With reverent welcome round him pressed. They brought him of their woodland fruits, They brought him of the choicest roots, And laughed and shouted in their glee The noblest of their chiefs to see. Nor Hanumán delayed to greet Sage Jámbaván with reverence meet; To Angad and the chiefs he bent For age and rank preëminent, And briefly spoke:“These eyes have seen, These lips addressed, the Maithil queen.” They sat beneath the waving trees, And Angad spoke in words like these: “O noblest of the Vánar kind For valour power and might combined, To thee triumphant o'er the foe Our hopes, our lives and all we owe. O faithful heart in perils tried,[426] Which toil nor fear could turn aside, Thy deed the lady will restore, And Ráma's heart will ache no more.”890 Canto LVIII. The Feast Of Honey. They rose in air: the region grew Dark with their shadow as they flew. Swift to a lovely grove891 they came That rivalled heavenly Nandan's892 fame; 890 Three Cantos of repetition are omitted. 891 Madhuvan the“honey-wood.” 892 Indra's pleasure-ground or elysium.
- **Translation**: 

---

### Verse 12 (Ramayana 0.1517)
- **Original**: Canto LVIII. The Feast Of Honey. 1499 Where countless bees their honey stored,— The pleasance of the Vánars' lord, To every creature fenced and barred, Which Dadhimukh was set to guard, A noble Vánar, brave and bold, Sugríva's uncle lofty-souled. To Angad came with one accord The Vánars, and besought their lord That they those honeyed stores might eat That made the grove so passing sweet. He gave consent: they sought the trees Thronged with innumerable bees. They rifled all the treasured store, And ate the fruit the branches bore, And still as they prolonged the feast Their merriment and joy increased. Drunk with the sweets, they danced and bowed, They wildly sang, they laughed aloud, Some climbed and sprang from tree to tree, Some sat and chattered in their glee. Some scaled the trees which creepers crowned, And rained the branches to the ground. There with loud laugh a Vánar sprang Close to his friend who madly sang, In doleful mood another crept To mix his tears with one who wept. Then Dadhimukh with fury viewed The intoxicated multitude. He looked upon the rifled shade, And all the ruin they had made; Then called with angry voice, and strove To save the remnant of the grove.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1518)
- **Original**: 1500 The Ramayana But warning cries and words were spurned, And angry taunt and threat returned. Then fierce and wild contention rose: With furious words he mingled blows. They by no shame or fear withheld, By drunken mood and ire impelled, Used claws, and teeth, and hands, and beat The keeper under trampling feet. [Three Cantos consisting of little but repetitions are omitted. Dadhimukh escapes from the infuriated monkeys and hastens to Sugríva to report their misconduct. Sugríva infers that Hanumán and his band have been successful in their search, and that the exuberance of spirits and the mischief complained of, are but the natural expression of their joy. Dadhimukh obtains little sympa- thy from Sugríva, and is told to return and send the monkeys on with all possible speed.] Canto LXV. The Tidings. On to Pra[ravaG's hill they sped Where blooming trees their branches spread. To Raghu's sons their heads they bent And did obeisance reverent. Then to their king, by Angad led, Each Vánar chieftain bowed his head; And Hanumán the brave and bold His tidings to the monarch told; But first in Ráma's hand he placed The gem that Sítá's brow had graced: “I crossed the sea: I searched a while For Sítá in the giants' isle.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1519)
- **Original**: Canto LXVI. Ráma's Speech. 1501 I found her vext with taunt and threat By demon guards about her set. Her tresses twined in single braid, On the bare earth her limbs were laid. Sad were her eyes: her cheeks were pale As shuddering flowers in winter's gale. I stood beside the weeping dame, And gently whispered Ráma's name: With cheering words her grief consoled, And then the whole adventure told. She weeps afar beyond the sea, And her true heart is still with thee. She gave a sign that thou wouldst know, She bids thee think upon the crow, And bright mark pressed upon her brow When none was nigh but she and thou. She bids thee take this precious stone, The sea-born gem thou long hast known. “And I,” she said,“will dull the sting Of woe by gazing on the ring. One little month shall I sustain This life oppressed with woe and pain: And when the month is ended, I The giants' prey must surely die.’ ” [427] Canto LXVI. Ráma's Speech.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1520)
- **Original**: 1502 The Ramayana There ceased the Vánar: Ráma pressed The treasured jewel to his breast, And from his eyes the waters broke As to the Vánar king he spoke: “As o'er her babe the mother weeps, This flood of tears the jewel steeps. This gem that shone on Sítá's head Was Janak's gift when we were wed, And the pure brow that wore it lent New splendour to the ornament. This gem, bright offspring of the wave, The King of Heaven to Janak gave, Whose noble sacrificial rite Had filled the God with new delight. Now, as I gaze upon the prize, Methinks I see my father's eyes. Methinks I see before me stand The ruler of Videha's land.893 Methinks mine arms are folded now Round her who wore it on her brow. Speak, Hanumán, O say, dear friend, What message did my darling send? O speak, and let thy words impart Their gentle dew to cool my heart. Ah, 'tis the crown of woe to see This gem and ask“Where, where is she?” If for one month her heart be strong, Her days of life will yet be long. But I, with naught to lend relief, This very day must die of grief. Come, Hanumán, and quickly guide The mourner to his darling's side. 893 Janak was king of Videha or Mithilá in Behar.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1521)
- **Original**: Canto LXVI. Ráma's Speech. 1503 O lead me— thou hast learnt the way— I cannot and I will not stay. How can my gentle love endure, So timid, delicate, and pure, The dreadful demons fierce and vile Who watch her in the guarded isle? No more the light of beauty shines From Sítá as she weeps and pines. But pain and sorrow, cloud on cloud Her moonlight glory dim and shroud. O speak, dear Hanumán, and tell Each word that from her sweet lips fell, Her words, her words alone can give The healing balm to make me live.”894 894 The original contains two more Cantos which end the Book. Canto LXVII begins thus:“Hanumán thus addressed by the great-souled son of Raghu related to the son of Raghu all that Sítá had said.” And the two Cantos contain nothing but Hanumán's account of his interview with Sítá, and the report of his own speeches as well as of hers.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1522)
- **Original**: BOOK VI. 895 Canto I. Ráma's Speech. The son of Raghu heard, consoled, The wondrous tale Hanumán told; And, as his joyous hope grew high, In friendly words he made reply: “Behold a mighty task achieved, Which never heart but his conceived. Who else across the sea can spring, Save Váyu896 and the Feathered King?897 Who, pass the portals strong and high Which Nágas,898 Gods, and fiends defy, Where RávaG's hosts their station keep,— And come uninjured o'er the deep? By such a deed the Wind-God's son Good service to the king has done, And saved from ruin and disgrace Lakshma G and me and Raghu's race. Well has he planned and bravely fought, 895 The Sixth Book is called in SanskritYuddha-KáG a or The War , and Lanká-KáGda. It is generally known at the present day by the latter title. 896 Váyu is the God of Wind. 897 Garu a the King of Birds. 898 Serpent-Gods.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1523)
- **Original**: Canto II. Sugríva's Speech. 1505 And with due care my lady sought. But of the sea I sadly think, And the sweet hopes that cheered me sink. How can we cross the leagues of foam That keep us from the giant's home? What can the Vánar legions more Than muster on the ocean shore?” Canto II. Sugríva's Speech. He ceased: and King Sugríva tried To calm his grief, and thus replied: “'Be to thy nobler nature true, Nor let despair thy soul subdue. This cloud of causeless woe dispel, For all as yet has prospered well, And we have traced thy queen, and know The dwelling of our Rákshas foe. Arise, consult: thy task must be To cast a bridge athwart the sea, The city of our foe to reach That crowns the mountain by the beach; [428] And when our feet that isle shall tread, Rejoice and deem thy foeman dead. The sea unbridged, his walls defy Both fiends and children of the sky, Though at the fierce battalions' head Lord Indra's self the onset led. Yea, victory is thine before The long bridge touch the farther shore, So fleet and fierce and strong are these
- **Translation**: 

---

### Verse 19 (Ramayana 0.1524)
- **Original**: 1506 The Ramayana Who limb them as their fancies please. Away with grief and sad surmise That mar the noblest enterprise, And with their weak suspicion blight The sage's plan, the hero's might. Come, this degenerate weakness spurn, And bid thy dauntless heart return, For each fair hope by grief is crossed When those we love are dead or lost. Arise, O best of those who know, Arm for the giant's overthrow. None in the triple world I see Who in the fight may equal thee; None who before thy face may stand And brave the bow that arms thy hand, Trust to these mighty Vánars: they With full success thy trust will pay, When thou shalt reach the robber's hold, And loving arms round Sítá fold.” Canto III. Lanká. He ceased: and Raghu's son gave heed, Attentive to his prudent rede: Then turned again, with hope inspired, To Hanumán, and thus inquired:
- **Translation**: 

---

### Verse 20 (Ramayana 0.1525)
- **Original**: Canto III. Lanká. 1507 “Light were the task for thee, I ween, To bridge the sea that gleams between The mainland and the island shore. Or dry the deep and guide as o'er. Fain would I learn from thee whose feet Have trod the stones of every street, Of fenced Lanká's towers and forts, And walls and moats and guarded ports, And castles where the giants dwell, And battlemented citadel. O Váyu's son, describe it all, With palace, fort, and gate, and wall.” He ceased: and, skilled in arts that guide The eloquent, the chief replied: “Vast is the city, gay and strong, Where elephants unnumbered throng, And countless hosts of Rákshas breed Stand ready by the car and steed. Four massive gates, securely barred, All entrance to the city guard, With murderous engines fixt to throw Bolt, arrow, rock to check the foe, And many a mace with iron head That strikes at once a hundred dead. Her golden ramparts wide and high With massy strength the foe defy, Where inner walls their rich inlay Of coral, turkis, pearl display. Her circling moats are broad and deep, Where ravening monsters dart and leap. By four great piers each moat is spanned Where lines of deadly engines stand.
- **Translation**: 

---

