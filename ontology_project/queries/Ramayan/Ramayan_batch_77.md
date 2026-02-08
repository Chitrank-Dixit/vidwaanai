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

### Verse 1 (Ramayan 0.1521)
- **Original**: Canto LXVI. Ráma's Speech. 1503 O lead me— thou hast learnt the way— I cannot and I will not stay. How can my gentle love endure, So timid, delicate, and pure, The dreadful demons fierce and vile Who watch her in the guarded isle? No more the light of beauty shines From Sítá as she weeps and pines. But pain and sorrow, cloud on cloud Her moonlight glory dim and shroud. O speak, dear Hanumán, and tell Each word that from her sweet lips fell, Her words, her words alone can give The healing balm to make me live.”894 894 The original contains two more Cantos which end the Book. Canto LXVII begins thus:“Hanumán thus addressed by the great-souled son of Raghu related to the son of Raghu all that Sítá had said.” And the two Cantos contain nothing but Hanumán's account of his interview with Sítá, and the report of his own speeches as well as of hers.
- **Translation**: 

---

### Verse 2 (Ramayan 0.1522)
- **Original**: BOOK VI. 895 Canto I. Ráma's Speech. The son of Raghu heard, consoled, The wondrous tale Hanumán told; And, as his joyous hope grew high, In friendly words he made reply: “Behold a mighty task achieved, Which never heart but his conceived. Who else across the sea can spring, Save Váyu896 and the Feathered King?897 Who, pass the portals strong and high Which Nágas,898 Gods, and fiends defy, Where RávaG's hosts their station keep,— And come uninjured o'er the deep? By such a deed the Wind-God's son Good service to the king has done, And saved from ruin and disgrace Lakshma G and me and Raghu's race. Well has he planned and bravely fought, 895 The Sixth Book is called in SanskritYuddha-KáG a or The War , and Lanká-KáGda. It is generally known at the present day by the latter title. 896 Váyu is the God of Wind. 897 Garu a the King of Birds. 898 Serpent-Gods.
- **Translation**: 

---

### Verse 3 (Ramayan 0.1523)
- **Original**: Canto II. Sugríva's Speech. 1505 And with due care my lady sought. But of the sea I sadly think, And the sweet hopes that cheered me sink. How can we cross the leagues of foam That keep us from the giant's home? What can the Vánar legions more Than muster on the ocean shore?” Canto II. Sugríva's Speech. He ceased: and King Sugríva tried To calm his grief, and thus replied: “'Be to thy nobler nature true, Nor let despair thy soul subdue. This cloud of causeless woe dispel, For all as yet has prospered well, And we have traced thy queen, and know The dwelling of our Rákshas foe. Arise, consult: thy task must be To cast a bridge athwart the sea, The city of our foe to reach That crowns the mountain by the beach; [428] And when our feet that isle shall tread, Rejoice and deem thy foeman dead. The sea unbridged, his walls defy Both fiends and children of the sky, Though at the fierce battalions' head Lord Indra's self the onset led. Yea, victory is thine before The long bridge touch the farther shore, So fleet and fierce and strong are these
- **Translation**: 

---

### Verse 4 (Ramayan 0.1524)
- **Original**: 1506 The Ramayana Who limb them as their fancies please. Away with grief and sad surmise That mar the noblest enterprise, And with their weak suspicion blight The sage's plan, the hero's might. Come, this degenerate weakness spurn, And bid thy dauntless heart return, For each fair hope by grief is crossed When those we love are dead or lost. Arise, O best of those who know, Arm for the giant's overthrow. None in the triple world I see Who in the fight may equal thee; None who before thy face may stand And brave the bow that arms thy hand, Trust to these mighty Vánars: they With full success thy trust will pay, When thou shalt reach the robber's hold, And loving arms round Sítá fold.” Canto III. Lanká. He ceased: and Raghu's son gave heed, Attentive to his prudent rede: Then turned again, with hope inspired, To Hanumán, and thus inquired:
- **Translation**: 

---

### Verse 5 (Ramayan 0.1525)
- **Original**: Canto III. Lanká. 1507 “Light were the task for thee, I ween, To bridge the sea that gleams between The mainland and the island shore. Or dry the deep and guide as o'er. Fain would I learn from thee whose feet Have trod the stones of every street, Of fenced Lanká's towers and forts, And walls and moats and guarded ports, And castles where the giants dwell, And battlemented citadel. O Váyu's son, describe it all, With palace, fort, and gate, and wall.” He ceased: and, skilled in arts that guide The eloquent, the chief replied: “Vast is the city, gay and strong, Where elephants unnumbered throng, And countless hosts of Rákshas breed Stand ready by the car and steed. Four massive gates, securely barred, All entrance to the city guard, With murderous engines fixt to throw Bolt, arrow, rock to check the foe, And many a mace with iron head That strikes at once a hundred dead. Her golden ramparts wide and high With massy strength the foe defy, Where inner walls their rich inlay Of coral, turkis, pearl display. Her circling moats are broad and deep, Where ravening monsters dart and leap. By four great piers each moat is spanned Where lines of deadly engines stand.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1526)
- **Original**: 1508 The Ramayana In sleepless watch at every gate Unnumbered hosts of giants wait, And, masters of each weapon, rear The threatening pike and sword and spear. My fury hurled those ramparts down, Filled up the moats that gird the town, The piers and portals overturned, And stately Lanká spoiled and burned. Howe'er we Vánars force our way O'er the wide seat of VaruG's899 sway, Be sure that city of the foe Is doomed to sudden overthrow, Nay, why so vast an army lead? Brave Angad, Dwivid good at need, Fierce Mainda, Panas famed in fight, And Níla's skill and Nala's might, And Jámbaván the strong and wise, Will dare the easy enterprise. Assailed by these shall Lanká fall With gate and rampart, tower and wall. Command the gathering, chief: and they In happy hour will haste away.” Canto IV. The March. He ceased; and spurred by warlike pride The impetuous son of Raghu cried: “Soon shall mine arm with wrathful joy That city of the foe destroy. 899 The God of the sea.
- **Translation**: 

---

### Verse 7 (Ramayan 0.1527)
- **Original**: Canto IV. The March. 1509 Now, chieftain, now collect the host, And onward to the southern coast! The sun in his meridian tower Gives glory to the Vánar power. The demon lord who stole my queen By timely flight his life may screen. She, when she knows her lord is near, Will cling to hope and banish fear, Saved like a dying wretch who sips The drink of Gods with fevered lips. Arise, thy troops to battle lead: All happy omens counsel speed. The Lord of Stars in favouring skies Bodes glory to our enterprise. This arm shall slay the fiend; and she, My consort, shall again be free. [429] Mine upward-throbbing eye foreshows The longed-for triumph o'er my foes. Far in the van be Níla's post, To scan the pathway for the host, And let thy bravest and thy best, A hundred thousand, wait his hest. Go forth, O warrior Níla, lead The legions on through wood and mead Where pleasant waters cool the ground, And honey, flowers, and fruit abound. Go, and with timely care prevent The Rákshas foeman's dark intent. With watchful troops each valley guard Ere brooks and fruits and roots be marred And search each glen and leafy shade For hostile troops in ambuscade. But let the weaklings stay behind: For heroes is our task designed.
- **Translation**: 

---

### Verse 8 (Ramayan 0.1528)
- **Original**: 1510 The Ramayana Let thousands of the Vánar breed The vanguard of the armies lead: Fierce and terrific must it be As billows of the stormy sea. There be the hill-huge Gaja's place, And Gavaya's, strongest of his race, And, like the bull that leads the herd, Gaváksha's, by no fears deterred Let Rishabh, matchless in the might Of warlike arms, protect our right, And Gandhamádan next in rank Defend and guide the other flank. I, like the God who rules the sky Borne on Airávat900 mounted high On stout Hanúmán's back will ride, The central host to cheer and guide. Fierce as the God who rules below, On Angad's back let LakshmaG show Like him who wealth to mortals shares,901 The lord whom Sárvabhauma902 bears. The bold SusheG's impetuous might, And Vegadar[í's piercing sight, And Jámbaván whom bears revere, Illustrious three, shall guard the rear.” He ceased, the royal Vánar heard, And swift, obedient to his word, Sprang forth in numbers none might tell From mountain, cave, and bosky dell, From rocky ledge and breezy height, Fierce Vánars burning for the fight. 900 Indra's elephant. 901 Kuvera, God of wealth. 902 Kuvera's elephant.
- **Translation**: 

---

### Verse 9 (Ramayan 0.1529)
- **Original**: Canto IV. The March. 1511 And Ráma's course was southward bent Amid the mighty armament. On, joyous, pressed in close array The hosts who owned Sugríva's sway, With nimble feet, with rapid bound Exploring, ere they passed, the ground, While from ten myriad throats rang out The challenge and the battle shout. On roots and honeycomb they fed, And clusters from the boughs o'erhead, Or from the ground the tall trees tore Rich with the flowery load they bore. Some carried comrades, wild with mirth, Then cast their riders to the earth, Who swiftly to their feet arose And overthrew their laughing foes. While still rang out the general cry, “King RávaG and his fiends shall die,” Still on, exulting in the pride Of conscious strength, the Vánars hied, And gazed where noble Sahya, best Of mountains, raised each towering crest. They looked on lake and streamlet, where The lotus bloom was bright and fair, Nor marched— for Ráma's hest they feared Where town or haunt of men appeared. Still onward, fearful as the waves Of Ocean when he roars and raves, Led by their eager chieftains, went The Vánars' countless armament. Each captain, like a noble steed Urged by the lash to double speed. Pressed onward, filled with zeal and pride, By Ráma's and his brother's side,
- **Translation**: 

---

### Verse 10 (Ramayan 0.1530)
- **Original**: 1512 The Ramayana Who high above the Vánar throng On mighty backs were borne along, Like the great Lords of Day and Night Seized by eclipsing planets might. Then LakshmaG radiant as the morn, On Angad's shoulders high upborne. With sweet consoling words that woke New ardour, to his brother spoke: “Soon shalt thou turn, thy queen regained And impious RávaG's life-blood drained, In happiness and high renown To dear Ayodhyá's happy town. I see around exceeding fair All omens of the earth and air. Auspicious breezes sweet and low To greet the Vánar army blow, And softly to my listening ear Come the glad cries of bird and deer. Bright is the sky around us, bright Without a cloud the Lord of Light, And Zukra903 with propitious love Looks on thee from his throne above. The pole-star and the Sainted Seven904 Shine brightly in the northern heaven, And great Tri[anku,905 glorious king,[430] Ikshváku's son from whom we spring, Beams in unclouded glory near His holy priest906 whom all revere. 903 The planet Venus, or its regent who is regarded as the son of Bhrigu and preceptor of the Daityas. 904 The sevenrishisor saints who form the constellation of the Great Bear. 905 Tri[anku was raised to the skies to form a constellation in the southern hemisphere. The story in told in Book I, Canto LX. 906 The sage Vi[vámitra, who performed for Tri[anku the great sacrifice which
- **Translation**: 

---

### Verse 11 (Ramayan 0.1531)
- **Original**: Canto IV. The March. 1513 Undimmed the two Vi[ákhás907 shine, The strength and glory of our line, And Nairrit's908 influence that aids Our Rákshas foemen faints and fades. The running brooks are fresh and fair, The boughs their ripening clusters bear, And scented breezes gently sway The leaflet of the tender spray. See, with a glory half divine The Vánars' ordered legions shine, Bright as the Gods' exultant train Who saw the demon Tárak slain. O let thine eyes these signs behold, And bid thy heart be glad and bold.” The Vánar squadrons densely spread O'er all the country onward sped, While rising from the rapid beat Of bears' and monkeys' hastening feet. Dust hid the earth with thickest veil, And made the struggling sunbeams pale. Now where Mahendra's peaks arise Came Ráma of the lotus eyes And the long arm's resistless might, And clomb the mountain's wood-crowned height. Thence Da[aratha's son beheld Where billowy Ocean rose and swelled, Past Malaya's peaks and Sahya's chain The Vánar legions reached the main, And stood in many a marshalled band raised him to the heavens. 907 One of the lunar asterisms containing four or originally two stars under the regency of a dual divinity Indrágni, Indra and Agni. 908 The lunar asterism Múla, belonging to the Rákshases.
- **Translation**: 

---

### Verse 12 (Ramayan 0.1532)
- **Original**: 1514 The Ramayana On loud-resounding Ocean's strand. To the fair wood that fringed the tide Came Da [aratha's son, and cried: “At length, my lord Sugríva, we Have reached King VaruG's realm the sea, And one great thought, still-vexing, how To cross the flood, awaits us now. The broad deep ocean, that denies A passage, stretched before us lies. Then let us halt and plan the while How best to storm the giant's isle.” He ceased: Sugríva on the coast By trees o'ershadowed stayed the host, That seemed in glittering lines to be The bright waves of a second sea. Then from the shore the captains gazed On billows which the breezes raised To fury, as they dashed in foam O'er VaruG's realm, the Asurs' home:909 The sea that laughed with foam, and danced With waves whereon the sunbeams glanced: Where, when the light began to fade, Huge crocodiles and monsters played; And, when the moon went up the sky, The troubled billows rose on high From the wild watery world whereon A thousand moons reflected shone: Where awful serpents swam and showed Their fiery crests which flashed and glowed, Illumining the depths of hell, The prison where the demons dwell. The eye, bewildered, sought in vain 909 The Asurs or demons dwell imprisoned in the depths beneath the sea.
- **Translation**: 

---

### Verse 13 (Ramayan 0.1533)
- **Original**: Canto V. Ráma's Lament. 1515 The bounding line of sky and main: Alike in shade, alike in glow Were sky above and sea below. There wave-like clouds by clouds were chased, Here cloud-like billows roared and raced: Then shone the stars, and many a gem That lit the waters answered them. They saw the great-souled Ocean stirred To frenzy by the winds, and heard, Loud as ten thousand drums, the roar Of wild waves dashing on the shore. They saw him mounting to defy With deafening voice the troubled sky. And the deep bed beneath him swell In fury as the billows fell. Canto V. Ráma's Lament. There on the coast in long array The Vánars' marshalled legions lay, Where Níla's care had ordered well The watch of guard and sentinel, And Mainda moved from post to post With Dwivid to protect the host.
- **Translation**: 

---

### Verse 14 (Ramayan 0.1534)
- **Original**: 1516 The Ramayana Then Ráma stood by LakshmaG's side, And mastered by his sorrow cried: “My brother dear, the heart's distress, As days wear on, grows less and less. But my deep-seated grief, alas, Grows fiercer as the seasons pass. Though for my queen my spirit longs, And broods indignant o'er my wrongs, Still wilder is my grief to know That her young life is passed in woe. Breathe, gentle gale, O breathe where she Lies prisoned, and then breathe on me,[431] And, though my love I may not meet, Thy kiss shall be divinely sweet. Ah, by the giant's shape appalled, On her dear lord for help she called, Still in mine ears the sad cry rings And tears my heart with poison stings. Through the long daylight and the gloom Of night wild thoughts of her consume My spirit, and my love supplies The torturing flame which never dies. Leave me, my brother; I will sleep Couched on the bosom of the deep, For the cold wave may bring me peace And bid the fire of passion cease. One only thought my stay must be, That earth, one earth, holds her and me, To hear, to know my darling lives Some life-supporting comfort gives, As streams from distant fountains run O'er meadows parching in the sun. Ah when, my foeman at my feet, Shall I my queen, my glory, meet,
- **Translation**: 

---

### Verse 15 (Ramayan 0.1535)
- **Original**: Canto VI. Rávan's Speech. 1517 The blossom of her dear face raise And on her eyes enraptured gaze, Press her soft lips to mine again, And drink a balm to banish pain! Alas, alas! where lies she now, My darling of the lovely brow? On the cold earth, no help at hand, Forlorn amid the Rákshas band, King Janak's child still calls on me, Her lord and love, to set her free. But soon in glory will she rise A crescent moon in autumn skies, And those dark rovers of the night, Like scattered clouds shall turn in flight.” Canto VI. Rávan's Speech. But when the giant king surveyed His glorious town in ruin laid, And each dire sign of victory won By Hanumán the Wind-God's son, He vailed his angry eyes oppressed By shame, and thus his lords addressed: “The Vánar spy has passed the gate Of Lanká long inviolate, Eluded watch and ward, and seen With his bold eyes the captive queen. My royal roof with flames is red, The bravest of my lords are dead, And the fierce Vánar in his hate Has left our city desolate.
- **Translation**: 

---

### Verse 16 (Ramayan 0.1536)
- **Original**: 1518 The Ramayana Now ponder well the work that lies Before us, ponder and advise. With deep-observing judgment scan The peril, and mature a plan. From counsel, sages say, the root, Springs victory, most glorious fruit. First ranks the king, when woe impends Who seeks the counsel of his friends, Of kinsmen ever faithful found, Or those whose hopes with his are bound, Then with their aid his strength applies, And triumphs in his enterprise. Next ranks the prince who plans alone, No counsel seeks to aid his own, Weighs loss and gain and wrong and right, And seeks success with earnest might. Unwisest he who spurns delays, Who counts no cost, no peril weighs, Speeds to his aim, defying fate, And risks his all, precipitate. Thus too in counsel sages find A best, a worst, a middle kind. When gathered counsellors explore The way by light of holy lore, And all from first to last agree, Is the best counsel of the three. Next, if debate first waxes high, And each his chosen plan would try Till all agree at last, we deem This counsel second in esteem. Worst of the three is this, when each Assails with taunt his fellow's speech; When all debate, and no consent Concludes the angry argument.
- **Translation**: 

---

### Verse 17 (Ramayan 0.1537)
- **Original**: Canto VII. Rávan Encouraged. 1519 Consult then, lords; my task shall be To crown with act your wise decree. With thousands of his wild allies The vengeful Ráma hither hies; With unresisted might and speed Across the flood his troops will lead, Or for the Vánar host will drain The channels of the conquered main.” Canto VII. Rávan Encouraged. He ceased: they scorned, with blinded eyes, The foeman and his bold allies, Raised reverent hands with one accord, And thus made answer to their lord: “Why yield thee, King, to causeless fear? A mighty host with sword and spear And mace and axe and pike and lance Waits but thy signal to advance. Art thou not he who slew of old The Serpent-Gods, and stormed their hold; Scaled Mount Kailása and o'erthrew Kuvera910 and his Yaksha crew, [432] 910 The God of Riches, brother and enemy of RávaG and first possessor of Pushpak the flying car.
- **Translation**: 

---

### Verse 18 (Ramayan 0.1538)
- **Original**: 1520 The Ramayana CompellingZiva's haughty friend Beneath a mightier arm to bend? Didst thou not bring from realms afar The marvel of the magic car, When they who served Kuvera fell Crushed in their mountain citadel? Attracted by thy matchless fame To thee, a suppliant, Maya came, The lord of every Dánav band, And won thee with his daughter's hand. Thy arm in hell itself was felt, Where Vásuki911 and Zankha dwelt, And they and Takshak, overthrown, Were forced thy conquering might to own. The Gods in vain their blessing gave To heroes bravest of the brave, Who strove a year and, sorely pressed, Their victor's peerless might confessed. In vain their magic arts they tried, In vain thy matchless arm defied King VaruG's sons with fourfold force, Cars, elephants, and foot, and horse, But for a while thy power withstood, And, conquered, mourned their hardihood. Thou hast encountered, face to face, King Yáma 912 with his murdering mace. Fierce as the wild tempestuous sea, What terror had his wrath for thee, Though death in every threatening form, And woe and torment, urged the storm? Thine arm a glorious victory won 911 King of the Serpents.Zankha and Takshak are two of the eight Serpent Chiefs. 912 The God of Death, the Pluto of the Hindus.
- **Translation**: 

---

### Verse 19 (Ramayan 0.1539)
- **Original**: Canto VIII. Prahasta's Speech. 1521 O'er the dread king who pities none; And the three worlds, from terror freed, In joyful wonder praised thy deed. The tribe of Warriors, strong and dread As Indra's self, o'er earth had spread; As giant trees that towering stand In mountain glens, they filled the land. Can Raghu's son encounter foes Fierce, numerous, and strong as those? Yet, trained in war and practised well, O'ermatched by thee, they fought and fell, Stay in thy royal home, nor care The battle and the toil to share; But let the easy fight be won By Indrajít913 thy matchless son. All, all shall die, if thou permit, Slain by the hand of Indrajít.” Canto VIII. Prahasta's Speech. Dark as a cloud of autumn, dread Prahasta joined his palms and said: 913 Literally Indra's conqueror, so called from his victory over that God.
- **Translation**: 

---

### Verse 20 (Ramayan 0.1540)
- **Original**: 1522 The Ramayana “Gandharvas, Gods, the hosts who dwell In heaven, in air, in earth, in hell, Have yielded to thy might, and how Shall two weak men oppose thee now? Hanúmán came, a foe disguised, And mocked us heedless and surprised, Or never had he lived to flee And boast that he has fought with me. Command, O King, and this right hand Shall sweep the Vánars from the land, And hill and dale, to Ocean's shore, Shall know the death-doomed race no more. But let my care the means devise To guard thy city from surprise.” Then Durmukh cried, of Rákshas race: “Too long we brook the dire disgrace. He gave our city to the flames, He trod the chambers of thy dames. Ne'er shall so weak and vile a thing Unpunished brave the giants' king. Now shall this single arm attack And drive the daring Vánars back, Till to the winds of heaven they flee, Or seek the depths of earth and sea.” Then, brandishing the mace he bore, Whose horrid spikes were stained with gore, While fury made his eyeballs red, Impetuous Vajradanshmra said:
- **Translation**: 

---

