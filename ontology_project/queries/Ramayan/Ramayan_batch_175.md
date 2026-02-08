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

### Verse 1 (Ramayana 0.1526)
- **Original**: 1508 The Ramayana In sleepless watch at every gate Unnumbered hosts of giants wait, And, masters of each weapon, rear The threatening pike and sword and spear. My fury hurled those ramparts down, Filled up the moats that gird the town, The piers and portals overturned, And stately Lanká spoiled and burned. Howe'er we Vánars force our way O'er the wide seat of VaruG's899 sway, Be sure that city of the foe Is doomed to sudden overthrow, Nay, why so vast an army lead? Brave Angad, Dwivid good at need, Fierce Mainda, Panas famed in fight, And Níla's skill and Nala's might, And Jámbaván the strong and wise, Will dare the easy enterprise. Assailed by these shall Lanká fall With gate and rampart, tower and wall. Command the gathering, chief: and they In happy hour will haste away.” Canto IV. The March. He ceased; and spurred by warlike pride The impetuous son of Raghu cried: “Soon shall mine arm with wrathful joy That city of the foe destroy. 899 The God of the sea.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1527)
- **Original**: Canto IV. The March. 1509 Now, chieftain, now collect the host, And onward to the southern coast! The sun in his meridian tower Gives glory to the Vánar power. The demon lord who stole my queen By timely flight his life may screen. She, when she knows her lord is near, Will cling to hope and banish fear, Saved like a dying wretch who sips The drink of Gods with fevered lips. Arise, thy troops to battle lead: All happy omens counsel speed. The Lord of Stars in favouring skies Bodes glory to our enterprise. This arm shall slay the fiend; and she, My consort, shall again be free. [429] Mine upward-throbbing eye foreshows The longed-for triumph o'er my foes. Far in the van be Níla's post, To scan the pathway for the host, And let thy bravest and thy best, A hundred thousand, wait his hest. Go forth, O warrior Níla, lead The legions on through wood and mead Where pleasant waters cool the ground, And honey, flowers, and fruit abound. Go, and with timely care prevent The Rákshas foeman's dark intent. With watchful troops each valley guard Ere brooks and fruits and roots be marred And search each glen and leafy shade For hostile troops in ambuscade. But let the weaklings stay behind: For heroes is our task designed.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1528)
- **Original**: 1510 The Ramayana Let thousands of the Vánar breed The vanguard of the armies lead: Fierce and terrific must it be As billows of the stormy sea. There be the hill-huge Gaja's place, And Gavaya's, strongest of his race, And, like the bull that leads the herd, Gaváksha's, by no fears deterred Let Rishabh, matchless in the might Of warlike arms, protect our right, And Gandhamádan next in rank Defend and guide the other flank. I, like the God who rules the sky Borne on Airávat900 mounted high On stout Hanúmán's back will ride, The central host to cheer and guide. Fierce as the God who rules below, On Angad's back let LakshmaG show Like him who wealth to mortals shares,901 The lord whom Sárvabhauma902 bears. The bold SusheG's impetuous might, And Vegadar[í's piercing sight, And Jámbaván whom bears revere, Illustrious three, shall guard the rear.” He ceased, the royal Vánar heard, And swift, obedient to his word, Sprang forth in numbers none might tell From mountain, cave, and bosky dell, From rocky ledge and breezy height, Fierce Vánars burning for the fight. 900 Indra's elephant. 901 Kuvera, God of wealth. 902 Kuvera's elephant.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1529)
- **Original**: Canto IV. The March. 1511 And Ráma's course was southward bent Amid the mighty armament. On, joyous, pressed in close array The hosts who owned Sugríva's sway, With nimble feet, with rapid bound Exploring, ere they passed, the ground, While from ten myriad throats rang out The challenge and the battle shout. On roots and honeycomb they fed, And clusters from the boughs o'erhead, Or from the ground the tall trees tore Rich with the flowery load they bore. Some carried comrades, wild with mirth, Then cast their riders to the earth, Who swiftly to their feet arose And overthrew their laughing foes. While still rang out the general cry, “King RávaG and his fiends shall die,” Still on, exulting in the pride Of conscious strength, the Vánars hied, And gazed where noble Sahya, best Of mountains, raised each towering crest. They looked on lake and streamlet, where The lotus bloom was bright and fair, Nor marched— for Ráma's hest they feared Where town or haunt of men appeared. Still onward, fearful as the waves Of Ocean when he roars and raves, Led by their eager chieftains, went The Vánars' countless armament. Each captain, like a noble steed Urged by the lash to double speed. Pressed onward, filled with zeal and pride, By Ráma's and his brother's side,
- **Translation**: 

---

### Verse 5 (Ramayana 0.1530)
- **Original**: 1512 The Ramayana Who high above the Vánar throng On mighty backs were borne along, Like the great Lords of Day and Night Seized by eclipsing planets might. Then LakshmaG radiant as the morn, On Angad's shoulders high upborne. With sweet consoling words that woke New ardour, to his brother spoke: “Soon shalt thou turn, thy queen regained And impious RávaG's life-blood drained, In happiness and high renown To dear Ayodhyá's happy town. I see around exceeding fair All omens of the earth and air. Auspicious breezes sweet and low To greet the Vánar army blow, And softly to my listening ear Come the glad cries of bird and deer. Bright is the sky around us, bright Without a cloud the Lord of Light, And Zukra903 with propitious love Looks on thee from his throne above. The pole-star and the Sainted Seven904 Shine brightly in the northern heaven, And great Tri[anku,905 glorious king,[430] Ikshváku's son from whom we spring, Beams in unclouded glory near His holy priest906 whom all revere. 903 The planet Venus, or its regent who is regarded as the son of Bhrigu and preceptor of the Daityas. 904 The sevenrishisor saints who form the constellation of the Great Bear. 905 Tri[anku was raised to the skies to form a constellation in the southern hemisphere. The story in told in Book I, Canto LX. 906 The sage Vi[vámitra, who performed for Tri[anku the great sacrifice which
- **Translation**: 

---

### Verse 6 (Ramayana 0.1531)
- **Original**: Canto IV. The March. 1513 Undimmed the two Vi[ákhás907 shine, The strength and glory of our line, And Nairrit's908 influence that aids Our Rákshas foemen faints and fades. The running brooks are fresh and fair, The boughs their ripening clusters bear, And scented breezes gently sway The leaflet of the tender spray. See, with a glory half divine The Vánars' ordered legions shine, Bright as the Gods' exultant train Who saw the demon Tárak slain. O let thine eyes these signs behold, And bid thy heart be glad and bold.” The Vánar squadrons densely spread O'er all the country onward sped, While rising from the rapid beat Of bears' and monkeys' hastening feet. Dust hid the earth with thickest veil, And made the struggling sunbeams pale. Now where Mahendra's peaks arise Came Ráma of the lotus eyes And the long arm's resistless might, And clomb the mountain's wood-crowned height. Thence Da[aratha's son beheld Where billowy Ocean rose and swelled, Past Malaya's peaks and Sahya's chain The Vánar legions reached the main, And stood in many a marshalled band raised him to the heavens. 907 One of the lunar asterisms containing four or originally two stars under the regency of a dual divinity Indrágni, Indra and Agni. 908 The lunar asterism Múla, belonging to the Rákshases.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1532)
- **Original**: 1514 The Ramayana On loud-resounding Ocean's strand. To the fair wood that fringed the tide Came Da [aratha's son, and cried: “At length, my lord Sugríva, we Have reached King VaruG's realm the sea, And one great thought, still-vexing, how To cross the flood, awaits us now. The broad deep ocean, that denies A passage, stretched before us lies. Then let us halt and plan the while How best to storm the giant's isle.” He ceased: Sugríva on the coast By trees o'ershadowed stayed the host, That seemed in glittering lines to be The bright waves of a second sea. Then from the shore the captains gazed On billows which the breezes raised To fury, as they dashed in foam O'er VaruG's realm, the Asurs' home:909 The sea that laughed with foam, and danced With waves whereon the sunbeams glanced: Where, when the light began to fade, Huge crocodiles and monsters played; And, when the moon went up the sky, The troubled billows rose on high From the wild watery world whereon A thousand moons reflected shone: Where awful serpents swam and showed Their fiery crests which flashed and glowed, Illumining the depths of hell, The prison where the demons dwell. The eye, bewildered, sought in vain 909 The Asurs or demons dwell imprisoned in the depths beneath the sea.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1533)
- **Original**: Canto V. Ráma's Lament. 1515 The bounding line of sky and main: Alike in shade, alike in glow Were sky above and sea below. There wave-like clouds by clouds were chased, Here cloud-like billows roared and raced: Then shone the stars, and many a gem That lit the waters answered them. They saw the great-souled Ocean stirred To frenzy by the winds, and heard, Loud as ten thousand drums, the roar Of wild waves dashing on the shore. They saw him mounting to defy With deafening voice the troubled sky. And the deep bed beneath him swell In fury as the billows fell. Canto V. Ráma's Lament. There on the coast in long array The Vánars' marshalled legions lay, Where Níla's care had ordered well The watch of guard and sentinel, And Mainda moved from post to post With Dwivid to protect the host.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1534)
- **Original**: 1516 The Ramayana Then Ráma stood by LakshmaG's side, And mastered by his sorrow cried: “My brother dear, the heart's distress, As days wear on, grows less and less. But my deep-seated grief, alas, Grows fiercer as the seasons pass. Though for my queen my spirit longs, And broods indignant o'er my wrongs, Still wilder is my grief to know That her young life is passed in woe. Breathe, gentle gale, O breathe where she Lies prisoned, and then breathe on me,[431] And, though my love I may not meet, Thy kiss shall be divinely sweet. Ah, by the giant's shape appalled, On her dear lord for help she called, Still in mine ears the sad cry rings And tears my heart with poison stings. Through the long daylight and the gloom Of night wild thoughts of her consume My spirit, and my love supplies The torturing flame which never dies. Leave me, my brother; I will sleep Couched on the bosom of the deep, For the cold wave may bring me peace And bid the fire of passion cease. One only thought my stay must be, That earth, one earth, holds her and me, To hear, to know my darling lives Some life-supporting comfort gives, As streams from distant fountains run O'er meadows parching in the sun. Ah when, my foeman at my feet, Shall I my queen, my glory, meet,
- **Translation**: 

---

### Verse 10 (Ramayana 0.1535)
- **Original**: Canto VI. Rávan's Speech. 1517 The blossom of her dear face raise And on her eyes enraptured gaze, Press her soft lips to mine again, And drink a balm to banish pain! Alas, alas! where lies she now, My darling of the lovely brow? On the cold earth, no help at hand, Forlorn amid the Rákshas band, King Janak's child still calls on me, Her lord and love, to set her free. But soon in glory will she rise A crescent moon in autumn skies, And those dark rovers of the night, Like scattered clouds shall turn in flight.” Canto VI. Rávan's Speech. But when the giant king surveyed His glorious town in ruin laid, And each dire sign of victory won By Hanumán the Wind-God's son, He vailed his angry eyes oppressed By shame, and thus his lords addressed: “The Vánar spy has passed the gate Of Lanká long inviolate, Eluded watch and ward, and seen With his bold eyes the captive queen. My royal roof with flames is red, The bravest of my lords are dead, And the fierce Vánar in his hate Has left our city desolate.
- **Translation**: 

---

### Verse 11 (Ramayana 0.1536)
- **Original**: 1518 The Ramayana Now ponder well the work that lies Before us, ponder and advise. With deep-observing judgment scan The peril, and mature a plan. From counsel, sages say, the root, Springs victory, most glorious fruit. First ranks the king, when woe impends Who seeks the counsel of his friends, Of kinsmen ever faithful found, Or those whose hopes with his are bound, Then with their aid his strength applies, And triumphs in his enterprise. Next ranks the prince who plans alone, No counsel seeks to aid his own, Weighs loss and gain and wrong and right, And seeks success with earnest might. Unwisest he who spurns delays, Who counts no cost, no peril weighs, Speeds to his aim, defying fate, And risks his all, precipitate. Thus too in counsel sages find A best, a worst, a middle kind. When gathered counsellors explore The way by light of holy lore, And all from first to last agree, Is the best counsel of the three. Next, if debate first waxes high, And each his chosen plan would try Till all agree at last, we deem This counsel second in esteem. Worst of the three is this, when each Assails with taunt his fellow's speech; When all debate, and no consent Concludes the angry argument.
- **Translation**: 

---

### Verse 12 (Ramayana 0.1537)
- **Original**: Canto VII. Rávan Encouraged. 1519 Consult then, lords; my task shall be To crown with act your wise decree. With thousands of his wild allies The vengeful Ráma hither hies; With unresisted might and speed Across the flood his troops will lead, Or for the Vánar host will drain The channels of the conquered main.” Canto VII. Rávan Encouraged. He ceased: they scorned, with blinded eyes, The foeman and his bold allies, Raised reverent hands with one accord, And thus made answer to their lord: “Why yield thee, King, to causeless fear? A mighty host with sword and spear And mace and axe and pike and lance Waits but thy signal to advance. Art thou not he who slew of old The Serpent-Gods, and stormed their hold; Scaled Mount Kailása and o'erthrew Kuvera910 and his Yaksha crew, [432] 910 The God of Riches, brother and enemy of RávaG and first possessor of Pushpak the flying car.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1538)
- **Original**: 1520 The Ramayana CompellingZiva's haughty friend Beneath a mightier arm to bend? Didst thou not bring from realms afar The marvel of the magic car, When they who served Kuvera fell Crushed in their mountain citadel? Attracted by thy matchless fame To thee, a suppliant, Maya came, The lord of every Dánav band, And won thee with his daughter's hand. Thy arm in hell itself was felt, Where Vásuki911 and Zankha dwelt, And they and Takshak, overthrown, Were forced thy conquering might to own. The Gods in vain their blessing gave To heroes bravest of the brave, Who strove a year and, sorely pressed, Their victor's peerless might confessed. In vain their magic arts they tried, In vain thy matchless arm defied King VaruG's sons with fourfold force, Cars, elephants, and foot, and horse, But for a while thy power withstood, And, conquered, mourned their hardihood. Thou hast encountered, face to face, King Yáma 912 with his murdering mace. Fierce as the wild tempestuous sea, What terror had his wrath for thee, Though death in every threatening form, And woe and torment, urged the storm? Thine arm a glorious victory won 911 King of the Serpents.Zankha and Takshak are two of the eight Serpent Chiefs. 912 The God of Death, the Pluto of the Hindus.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1539)
- **Original**: Canto VIII. Prahasta's Speech. 1521 O'er the dread king who pities none; And the three worlds, from terror freed, In joyful wonder praised thy deed. The tribe of Warriors, strong and dread As Indra's self, o'er earth had spread; As giant trees that towering stand In mountain glens, they filled the land. Can Raghu's son encounter foes Fierce, numerous, and strong as those? Yet, trained in war and practised well, O'ermatched by thee, they fought and fell, Stay in thy royal home, nor care The battle and the toil to share; But let the easy fight be won By Indrajít913 thy matchless son. All, all shall die, if thou permit, Slain by the hand of Indrajít.” Canto VIII. Prahasta's Speech. Dark as a cloud of autumn, dread Prahasta joined his palms and said: 913 Literally Indra's conqueror, so called from his victory over that God.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1540)
- **Original**: 1522 The Ramayana “Gandharvas, Gods, the hosts who dwell In heaven, in air, in earth, in hell, Have yielded to thy might, and how Shall two weak men oppose thee now? Hanúmán came, a foe disguised, And mocked us heedless and surprised, Or never had he lived to flee And boast that he has fought with me. Command, O King, and this right hand Shall sweep the Vánars from the land, And hill and dale, to Ocean's shore, Shall know the death-doomed race no more. But let my care the means devise To guard thy city from surprise.” Then Durmukh cried, of Rákshas race: “Too long we brook the dire disgrace. He gave our city to the flames, He trod the chambers of thy dames. Ne'er shall so weak and vile a thing Unpunished brave the giants' king. Now shall this single arm attack And drive the daring Vánars back, Till to the winds of heaven they flee, Or seek the depths of earth and sea.” Then, brandishing the mace he bore, Whose horrid spikes were stained with gore, While fury made his eyeballs red, Impetuous Vajradanshmra said:
- **Translation**: 

---

### Verse 16 (Ramayana 0.1541)
- **Original**: Canto VIII. Prahasta's Speech. 1523 “Why waste a thought on one so vile As Hanúmán the Vánar, while Sugríva, LakshmaG, yet remain, And Ráma mightier still, unslain? This mace to-day shall crush the three, And all the host will turn and flee. Listen, and I will speak: incline, O King, to hear these words of mine, For the deep plan that I propose Will swiftly rid thee of thy foes. Let thousands of thy host assume The forms of men in youthful bloom, In war's magnificent array Draw near to Raghu's son, and say: “Thy younger brother Bharat sends This army, and thy cause befriends.” Then let our legions hasten near With bow and mace and sword and spear, And on the Vánar army rain Our steel and stone till all be slain. If Raghu's sons will fain believe, Entangled in the net we weave, The penalty they both must pay, And lose their forfeit lives to-day.” [433] Then with his warrior soul on fire, Nikumbha spoke in burning ire: “I, only I, will take the field, And Raghu's son his life shall yield. Within these walls, O Chiefs, abide, Nor part ye from our monarch's side.”
- **Translation**: 

---

### Verse 17 (Ramayana 0.1542)
- **Original**: 1524 The Ramayana Canto IX. Vibhishan's Counsel. A score of warriors914 forward sprang, And loud the clashing iron rang Of mace and axe and spear and sword, As thus they spake unto their lord: “Their king Sugríva will we slay, And Raghu's sons, ere close of day, And strike the wretch Hanúmán down, The spoiler of our golden town.” But sage VibhishaG strove to calm The chieftains' fury; palm to palm He joined in lowly reverence, pressed915 Before them, and the throng addressed: 914 Their names are Nikumbha, Rabhasa, Súrya[atru, Suptaghna, Yajnakopa, Mahápár[va, Mahodara, Agniketu, Ra[miketu, Durdharsha, Indra[atru, Pra- hasta, Virúpáksha, Vajradanshmra, Dhúmráksha, Durmukha, Mahábala. 915 Similarly Antenor urges the restoration of Helen: “Let Sparta's treasures be this hour restored, And Argive Helen own her ancient lord. As this advice ye practise or reject, So hope success, or dread the dire effect,” POPE 'S{FNS Homer's Iliad, Book VII.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1543)
- **Original**: Canto IX. Vibhishan's Counsel. 1525 “Dismiss the hope of conquering one So stern and strong as Raghu's son. In due control each sense he keeps With constant care that never sleeps. Whose daring heart has e'er conceived The exploit Hanumán achieved, Across the fearful sea to spring, The tributary rivers' king? O Rákshas lords, in time be wise, Nor Ráma's matchless power despise. And say, what evil had the son Of Raghu to our monarch done, Who stole the dame he loved so well And keeps her in his citadel; If Khara in his foolish pride Encountered Ráma, fought, and died, May not the meanest love his life And guard it in the deadly strife? The Maithil dame, O Rákshas King, Sore peril to thy realm will bring. Restore her while there yet is time, Nor let us perish for thy crime. O, let the Maithil lady go Ere the avenger bend his bow To ruin with his arrowy showers Our Lanká with her gates and towers. Let Janak's child again be free Ere the wild Vánars cross the sea, In their resistless might assail Our city and her ramparts scale. Ah, I conjure thee by the ties Of brotherhood, be just and wise. In all my thoughts thy good I seek, And thus my prudent counsel speak.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1544)
- **Original**: 1526 The Ramayana Let captive Sítá be restored Ere, fierce as autumn's sun, her lord Send his keen arrows from the string To drink the life-blood of our king. This fury from thy soul dismiss, The bane of duty, peace, and bliss. Seek duty's path and walk therein, And joy and endless glory win. Restore the captive, ere we feel The piercing point of Ráma's steel. O spare thy city, spare the lives Of us, our friends, our sons and wives.” Thus spake VibhishaG wise and brave: The Rákshas king no answer gave, But bade his lords the council close, And sought his chamber for repose. Canto X. Vibhishan's Counsel. Soon as the light of morning broke, VibhishaG from his slumber woke, And, duty guiding every thought, The palace of his brother sought. Vast as a towering hill that shows His peaks afar, that palace rose. Here stood within the monarch's gate Sage nobles skilful in debate. There strayed in glittering raiment through The courts his royal retinue, Where in wild measure rose and fell
- **Translation**: 

---

### Verse 20 (Ramayana 0.1545)
- **Original**: Canto X. Vibhishan's Counsel. 1527 The music of the drum and shell, And talk grew loud, and many a dame Of fairest feature went and came Through doors a marvel to behold, With pearl inlaid on burning gold: Therein Gandharvas or the fleet Lords of the storm might joy to meet. He passed within the wondrous pile, Chief glory of the giants' isle: Thus, ere his fiery course be done, An autumn cloud admits the sun. [434] He heard auspicious voices raise With loud accord the note of praise, And sages, deep in Scripture, sing Each glorious triumph of the king. He saw the priests in order stand, Curd, oil, in every sacred hand; And by them flowers were laid and grain, Due offerings to the holy train. VibhishaG to the monarch bowed, Raised on a throne above the crowd: Then, skilled in arts of soft address, He raised his voice the king to bless, And sate him on a seat where he Full in his brother's sight should be. The chieftain there, while none could hear, Spoke his true speech for RávaG's ear, And to his words of wisdom lent The force of weightiest argument: “O brother, hear! since Ráma's queen A captive in thy house has been, Disastrous omens day by day Have struck our souls with wild dismay.
- **Translation**: 

---

