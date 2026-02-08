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

### Verse 1 (Ramayan 0.1181)
- **Original**: Canto IV. Lakshman's Reply. 1163 Still cleaving to her lord the sun. And me his sweet perfections drew To follow as his servant true. Named Lakshma G, brother of my lord Of grateful heart with knowledge stored Most meet is he all bliss to share, Who makes the good of all his care. While, power and lordship cast away, In the wild wood he chose to stay, A giant came,— his name unknown,— And stole the princess left alone. Then Diti's son553 who, cursed of yore, The semblance of a Rákshas wore, To King Sugríva bade us turn The robber's name and home to learn. For he, the Vánar chief, would know The dwelling of our secret foe. Such words of hope spake Diti's son, And sought the heaven his deeds had won. Thou hast my tale. From first to last Thine ears have heard whate'er has past. Ráma the mighty lord and I For refuge to Sugríva fly. The prince whose arm bright glory gained, O'er the whole earth as monarch reigned, And richest gifts to others gave, Is come Sugríva's help to crave; Son of a king the surest friend Of virtue, him who loved to lend His succour to the suffering weak, Is come Sugríva's aid to seek. Yes, Raghu's son whose matchless hand 553 Kabandha. See Book III. Canto LXXIII.
- **Translation**: 

---

### Verse 2 (Ramayan 0.1182)
- **Original**: 1164 The Ramayana Protected all this sea-girt land, The virtuous prince, my holy guide, For refuge seeks Sugríva's side. His favour sent on great and small Should ever save and prosper all. He now to win Sugríva's grace Has sought his woodland dwelling-place.[328] Son of a king of glorious fame;— Who knows not Da[aratha's name?— From whom all princes of the earth Received each honour due to worth;— Heir of that best of earthly kings, Ráma the prince whose glory rings Through realms below and earth and skies, For refuge to Sugríva flies. Nor should the Vánar king refuse The boon for which the suppliant sues, But with his forest legions speed To save him in his utmost need.” Sumitrá's son, his eyes bedewed With piteous tears, thus sighed and sued. Then, trained in all the arts that guide The speaker, Hanumán replied: “Yea, lords like you of wisest thought, Whom happy fate has hither brought, Who vanquish ire and rule each sense, Must of our lord have audience. Reft of his kingdom, sad, forlorn, Once Báli's hate now Báli's scorn, Defeated, severed from his spouse, Wandering under forest boughs, Child of the Sun, our lord and king
- **Translation**: 

---

### Verse 3 (Ramayan 0.1183)
- **Original**: Canto IV. Lakshman's Reply. 1165 Sugríva will his succours bring, And all our Vánar hosts combined Will trace the dame you long to find.” With gentle tone and winning grace Thus spake the chief of Vánar race, And then to Raghu's son he cried: “Come, haste we to Sugríva's side.” He spoke, and for his words so sweet Good Lakshma G paid all honour meet; Then turned and cried to Raghu's son: “Now deem thy task already done, Because this chief of Vánar kind, Son of the God who rules the wind, Declares Sugríva's self would be Assisted in his need by thee. Bright gleams of joy his cheek o'erspread As each glad word of hope he said; And ne'er will one so valiant deign To cheer our hearts with hope in vain.” He spoke, and Hanumán the wise Cast off his mendicant disguise, And took again his Vánar form, Son of the God of wind and storm. High on his ample back in haste Raghu's heroic sons he placed, And turned with rapid steps to find The sovereign of the Vánar kind.
- **Translation**: 

---

### Verse 4 (Ramayan 0.1184)
- **Original**: 1166 The Ramayana Canto V. The League. From Rishyamúka's rugged side To Malaya's hill the Vánar hied, And to his royal chieftain there Announced the coming of the pair: “See, here with LakshmaG Ráma stands Illustrious in a hundred lands. Whose valiant heart will never quail Although a thousand foes assail; King Da[aratha's son, the grace And glory of Ikshváku's race. Obedient to his father's will He cleaves to sacred duty still. With rites of royal pomp and pride His sire the Fire-God gratified; Ten hundred thousand kine he freed, And priests enriched with ample meed; And the broad land protected, famed For truthful lips and passions tamed. Through woman's guile his son has made His dwelling in the forest shade, Where, as he lived with every sense Subdued in hermit abstinence, Fierce RávaG stole his wife, and he Is come a suppliant, lord, to thee. Now let all honour due be paid To these great chiefs who seek thine aid.”
- **Translation**: 

---

### Verse 5 (Ramayan 0.1185)
- **Original**: Canto V. The League. 1167 Thus spake the Vánar prince, and, stirred With friendly thoughts, Sugríva heard. The light of joy his face o'erspread, And thus to Raghu's son he said: “O Prince, in rules of duty trained, Caring for all with love unfeigned, Hanúmán's tongue has truly shown The virtues that are thine alone. My chiefest glory, gain, and bliss, O stranger Prince, I reckon this, That Raghu's son will condescend To seek the Vánar for his friend. If thou my true ally wouldst be Accept the pledge I offer thee, This hand in sign of friendship take, And bind the bond we ne'er will break.” He spoke, and joy thrilled Ráma's breast; Sugríva's hand he seized and pressed And, transport beaming from his eye, Held to his heart his new ally. In wanderer's weed disguised no more, His proper form Hanúmán wore. Then, wood with wood engendering,554 came Neath his deft hands the kindled flame. 554 Fire for sacred purposes is produced by the attrition of two pieces of wood. In marriage and other solemn covenants fire is regarded as the holy witness in whose presence the agreement is made. Spenser in a description of a marriage, has borrowed from the Roman rite what he calls the housling, or“matrimonial rite.” “His owne two hands the holy knots did knit That none but death forever can divide. His owne two hands, for such a turn most fit, The housling fire did kindle and provide.” Faery Queen, Book I. XII.{FNS 37.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1186)
- **Original**: 1168 The Ramayana Between the chiefs that fire he placed[329] With wreaths of flowers and worship graced. And round its blazing glory went The friends with slow steps reverent. Thus each to other pledged and bound In solemn league new transport found, And bent upon his dear ally The gaze he ne'er could satisfy. “Friend of my soul art thou: we share Each other's joy, each other's care;” Thus in the bliss that thrilled his breast Sugríva Raghu's son addressed. From a high Sál a branch he tore Which many a leaf and blossom bore, And the fine twigs beneath them laid A seat for him and Ráma made. Then Hanumán with joyous mind, Son of the God who rules the wind, To LakshmaG gave, his seat to be, The gay branch of a Sandal tree. Then King Sugríva with his eyes Still trembling with the sweet surprise Of the great joy he could not hide, To Raghu's noblest scion cried: “O Ráma, racked with woe and fear, Spurned by my foes, I wander here. Reft of my spouse, forlorn I dwell Here in my forest citadel. Or wild with terror and distress Roam through the distant wilderness. Vext by my brother Báli long My soul has borne the scathe and wrong. Do thou, whose virtues all revere,
- **Translation**: 

---

### Verse 7 (Ramayan 0.1187)
- **Original**: Canto V. The League. 1169 Release me from my woe and fear. From dire distress thy friend to free Is a high task and worthy thee.” He spoke, and Raghu's son who knew All sacred duties men should do. The friend of justice, void of guile, Thus answered with a gentle smile: “Great Vánar, friends who seek my aid Still find their trust with fruit repaid. Báli, thy foe, who stole away Thy wife this vengeful hand shall slay. These shafts which sunlike flash and burn, Winged with the feathers of the hern, Each swift of flight and sure and dread, With even knot and pointed head, Fierce as the crashing fire-bolt sent By him who rules the firmament,555 Shall reach thy wicked foe and like Infuriate serpents hiss and strike. Thou, Vánar King, this day shalt see The foe who long has injured thee Lie, like a shattered mountain, low, Slain by the tempest of my bow.” Thus Ráma spake: Sugríva heard, And mighty joy his bosom stirred: As thus his champion he addressed: “Now by thy favour, first and best Of heroes, shall thy friend obtain His realm and darling wife again Recovered from the foe. Check thou mine elder brother's might; 555 Indra.
- **Translation**: 

---

### Verse 8 (Ramayan 0.1188)
- **Original**: 1170 The Ramayana That ne'er again his deadly spite May rob me of mine ancient right, Or vex my soul with woe.” The league was struck, a league to bring To Sítá fiends, and Vánar king556 Apportioned bliss and bale. Through her left eye quick throbbings shot,557 Glad signs the lady doubted not, That told their hopeful tale. The bright left eye of Báli felt An inauspicious throb that dealt A deadly blow that day. The fiery left eyes of the crew Of demons felt the throb, and knew The herald of dismay. Canto VI. The Tokens. With joy that sprang from hope restored To Ráma spake the Vánar lord: “I know, by wise Hanúmán taught, Why thou the lonely wood hast sought. Where with thy brother LakshmaG thou Hast sojourned, bound by hermit vow; Have heard how Sítá, Janak's child, Was stolen in the pathless wild, How by a roving Rákshas she 556 Báli the kingde facto. 557 With the Indians, as with the ancient Greeks, the throbbing of the right eye in a man is an auspicious sign, the throbbing of the left eye is the opposite. In a woman the significations of signs are reversed.
- **Translation**: 

---

### Verse 9 (Ramayan 0.1189)
- **Original**: Canto VI. The Tokens. 1171 Weeping was reft from him and thee; How, bent on death, the giant slew The vulture king, her guardian true, And gave thy widowed breast to know A solitary mourner's woe. But soon, dear Prince, thy heart shall be From every trace of sorrow free; [330] For I thy darling will restore, Lost like the prize of holy lore.558 Yea, though in heaven the lady dwell, Or prisoned in the depths of hell, My friendly care her way shall track And bring thy ransomed darling back. Let this my promise soothe thy care, Nor doubt the words I truly swear. Saints, fiends, and dwellers of the skies Shall find thy wife a bitter prize, Like the rash child who rues too late The treacherous lure of poisoned cate. No longer, Prince, thy loss deplore: Thy darling wife will I restore. 'Twas she I saw: my heart infers That shrinking form was doubtless hers, Which gaint RávaG, fierce and dread, Bore swiftly through the clouds o'erhead Still writhing in his strict embrace 558 The Vedas stolen by the demons Madhu and Kaimabha. “The text has [Sanskrit text] which signifies literally‘the lost vedic tradi- tion.’It seems that allusion is here made to the Vedas submerged in the depth of the sea, but promptly recovered by VishGu in one of his incarnations, as the brahmanic legend relates, with which the orthodoxy of the Bráhmans intended perhaps to allude to the prompt restoration and uninterrupted continuity of the ancient vedic tradition.” G ORRESIO .{FNS
- **Translation**: 

---

### Verse 10 (Ramayan 0.1190)
- **Original**: 1172 The Ramayana Like helpless queen of serpent race,559 And from her lips that sad voice came Shrieking thine own and LakshmaG's name. High on a hill she saw me stand With comrades twain on either hand. Her outer robe to earth she threw, And with it sent her anklets too. We saw the glittering tokens fall, We found them there and kept them all. These will I bring: perchance thine eyes The treasured spoils will recognize.” He ceased: then Raghu's son replied To the glad tale, and eager cried: “Bring them with all thy speed: delay No more, dear friend, but haste away.” Thus Ráma spoke. Sugríva hied Within the mountain's caverned side, Impelled by love that stirred each thought The precious tokens quickly brought, And said to Raghu's son: Behold This garment and these rings of gold. In Ráma's hand with friendly haste The jewels and the robe he placed. Then, like the moon by mist assailed, The tear-dimmed eyes of Ráma failed; That burst of woe unmanned his frame, Woe sprung from passion for his dame, And with his manly strength o'erthrown, 559 Like the wife of a Nága or Serpent-God carried off by an eagle. The enmity between the King of birds and the serpent is of very frequent occurrence. It seems to be a modification of the strife between the Vedic Indra and the Ahi, the serpent or drought-fiend; between Apollôn and the Python, Adam and the Serpent.
- **Translation**: 

---

### Verse 11 (Ramayan 0.1191)
- **Original**: Canto VI. The Tokens. 1173 He fell and cried, Ah me! mine own! Again, again close to his breast The ornaments and robe he pressed, While the quick pants that shook his frame As from a furious serpent came. On his dear brother standing nigh He turned at length his piteous eye; And, while his tears increasing ran, In bitter wail he thus began: “Look, brother, and behold once more The ornaments and robe she wore, Dropped while the giant bore away In cruel arras his struggling prey, Dropped in some quiet spot, I ween, Where the young grass was soft and green; For still untouched by spot or stain Their former beauty all retain.” He spoke with many a tear and sigh, And thus his brother made reply: “The bracelets thou hast fondly shown, And earrings, are to me unknown, But by long service taught I greet The anklets of her honoured feet.”560 Then to Sugríva Ráma, best Of Raghu's sons, these words addressed: 560 He means that he has never ventured to raise his eyes to her arms and face, though he has ever been her devoted servant.
- **Translation**: 

---

### Verse 12 (Ramayan 0.1192)
- **Original**: 1174 The Ramayana “Say to what quarter of the sky The cruel fiend was seen to fly, Bearing afar my captured wife, My darling dearer than my life. Speak, Vánar King, that I may know Where dwells the cause of all my woe; The fiend for whose transgression all The giants by this hand shall fall. He who the Maithil lady stole And kindled fury in my soul, Has sought his fate in senseless pride And opened Death's dark portal wide. Then tell me, Vánar lord, I pray, The dwelling of my foe, And he, beneath this hand, to-day To Yáma's halls shall go.” [331] Canto VII. Ráma Consoled. With longing love and woe oppressed The Vánar chief he thus addressed: And he, while sobs his utterance broke, Raised up his reverent hands and spoke:
- **Translation**: 

---

### Verse 13 (Ramayan 0.1193)
- **Original**: Canto VII. Ráma Consoled. 1175 “O Raghu's son, I cannot tell Where now that cruel fiend may dwell, Declare his power and might, or trace The author of his cursed race. Still trust the promise that I make And let thy breast no longer ache. So will I toil, nor toil in vain, That thou thy consort mayst regain. So will I work with might and skill That joy anew thy heart shall fill: The valour of my soul display, And RávaG and his legions slay. Awake, awake! unmanned no more Recall the strength was thine of yore. Beseems not men like thee to wear A weak heart yielding to despair. Like troubles, too, mine eyes have seen, Lamenting for a long-lost queen; But, by despair unconquered yet, My strength of mind I ne'er forget. Far more shouldst thou of lofty soul Thy passion and thy tears control, When I, of Vánar's humbler strain, Weep not for her in ceaseless pain. Be firm, be patient, nor forget The bounds the brave of heart have set In loss, in woe, in strife, in fear, When the dark hour of death is near. Up! with thine own brave heart advise: Not thus despond the firm and wise. But he who gives his childish heart To choose the coward's weakling part, Sinks, like a foundered vessel, deep In waves of woe that o'er him sweep.
- **Translation**: 

---

### Verse 14 (Ramayan 0.1194)
- **Original**: 1176 The Ramayana See, suppliant hand to hand I lay, And, moved by faithful love, I pray. Give way no more to grief and gloom, But all thy native strength resume. No joy on earth, I ween, have they Who yield their souls to sorrow's sway. Their glory fades in slow decline: 'Tis not for thee to grieve and pine. I do but hint with friendly speech The wiser part I dare not teach. This better path, dear friend, pursue, And let not grief thy soul subdue.” Sugríva thus with gentle art And sweet words soothed the mourner's heart, Who brushed off with his mantle's hem Tears from the eyes bedewed with them. Sugríva's words were not in vain, And Ráma was himself again, Around the king his arms he threw And thus began his speech anew: “Whate'er a friend most wise and true, Who counsels for the best, should do, Whate'er his gentle part should be, Has been performed, dear friend, by thee. Taught by thy counsel, O my lord, I feel my native strength restored. A friend like thee is hard to gain, Most rare in time of grief and pain. Now strain thine utmost power to trace The Maithil lady's dwelling place, And aid me in my search to find Fierce RávaG of the impious mind.
- **Translation**: 

---

### Verse 15 (Ramayan 0.1195)
- **Original**: Canto VIII. Ráma's Promise. 1177 Trust thou, in turn, thy loyal friend, And say what aid this arm can lend To speed thy hopes, as fostering rain Quickens in earth the scattered grain. Deem not those words, that seemed to spring From pride, are false, O Vánar King. None from these lips has ever heard, None e'er shall hear, one lying word. Again I promise and declare, Yea, by my truth, dear friend, I swear.” Then glad was King Sugríva's breast, And all his lords their joy confessed, Stirred by sure hope of Ráma's aid, And promise which the prince had made. Canto VIII. Ráma's Promise. Doubt from Sugríva's heart had fled, And thus to Raghu's son he said: “No bliss the Gods of heaven deny. Each views me with a favouring eye, When thou, whom all good gifts attend, Hast sought me and become my friend. Leagued, friend, with thee in bold emprise My arm might win the conquered skies; And shall our banded strength be weak To gain the realm which now I seek? A happy fate was mine above My kith and kin and all I love, When, near the witness fire, I won
- **Translation**: 

---

### Verse 16 (Ramayan 0.1196)
- **Original**: 1178 The Ramayana Thy friendship, Raghu's glorious son. Thou too in ripening time shall see Thy friend not all unworthy thee. What gifts I have shall thus be shown: Not mine the tongue to make them known. Strong is the changeless bond that binds The friendly faith of noble minds, In woe, in danger, firm and sure Their constancy and love endure. Gold, silver, jewels rich and rare They count as wealth for friends to share.[332] Yea, be they rich or poor and low, Blest with all joys or sunk in woe, Stained with each fault or pure of blame, Their friends the nearest place may claim; For whom they leave, at friendship's call, Their gold, their bliss, their homes and all.” He spoke by generous impulse moved, And Raghu's son his speech approved Glancing at LakshmaG by his side, Like Indra in his beauty's pride. The Vánar monarch saw the pair Of mighty brothers standing there, And turned his rapid eye to view The forest trees that near him grew. He saw, not far from where he stood, A Sál tree towering o'er the wood. Amid the thick leaves many a bee Graced the scant blossoms of the tree, From whose dark shade a bough, that bore A load of leafy twigs, he tore, Which on the grassy ground he laid And seats for him and Ráma made.
- **Translation**: 

---

### Verse 17 (Ramayan 0.1197)
- **Original**: Canto VIII. Ráma's Promise. 1179 Hanúmán saw them sit, he sought A Sál tree's leafy bough and brought The burthen, and with meek request Entreated LakshmaG, too, to rest. There on the noble mountain's brow, Strewn with the young leaves of the bough, Sat Raghu's son in placid ease Calm as the sea when sleeps the breeze. Sugríva's heart with rapture swelled, And thus, by eager love impelled, He spoke in gracious tone, that, oft Checked by his joy, was low and soft: “I, by my brother's might oppressed, By ceaseless woe and fear distressed, Mourning my consort far away, On Rishyamúka's mountain stray. Expelled by Báli's cruel hate I wander here disconsolate. Do thou to whom all sufferers flee, From his dread hand deliver me.” He spoke, and Ráma, just and brave, Whose pious soul to virtue clave, Smiled as in conscious might he eyed The king of Vánars, and replied: “Best fruit of friendship is the deed That helps the friend in hour of need; And this mine arm in death shall lay Thy robber ere the close of day. For see, these feathered darts of mine Whose points so fiercely flash and shine, And shafts with golden emblem, came From dark woods known by Skanda's name,561 561 The wood in which Skanda or Kártikeva was brought up:
- **Translation**: 

---

### Verse 18 (Ramayan 0.1198)
- **Original**: 1180 The Ramayana Winged from the pinion of the hern Like Indra's bolts they strike and burn. With even knots and piercing head Each like a furious snake is sped; With these, to-day, before thine eye Shall, like a shattered mountain, lie Báli, thy dread and wicked foe, O'erwhelmed in hideous overthrow.” He spoke: Sugríva's bosom swelled With hope and joy unparalleled. Then his glad voice the Vánar raised, And thus the son of Raghu praised: “Long have I pined in depth of grief; Thou art the hope of all, O chief. Now, Raghu's son, I hail thee friend, And bid thee to my woes attend; For, by my truth I swear it, now Not life itself is dear as thou, Since by the witness fire we met And friendly hand in hand was set. Friend communes now with friend, and hence I tell with surest confidence, How woes that on my spirit weigh Consume me through the night and day.” “The Warrior-God Whose infant steps amid the thickets strayed Where the reeds wave over the holy sod.” See also Book I, Canto XXIX.
- **Translation**: 

---

### Verse 19 (Ramayan 0.1199)
- **Original**: Canto VIII. Ráma's Promise. 1181 For sobs and sighs he scarce could speak, And his sad voice came low and weak, As, while his eyes with tears o'erflowed, The burden of his soul he showed. Then by strong effort, bravely made, The torrent of his tears he stayed, Wiped his bright eyes, his grief subdued, And thus, more calm, his speech renewed: “By Báli's conquering might oppressed, Of power and kingship dispossessed, Loaded with taunts of scorn and hate I left my realm and royal state. He tore away my consort: she Was dearer than my life to me, And many a friend to me and mine In hopeless chains was doomed to pine. With wicked thoughts, unsated still, Me whom he wrongs he yearns to kill; And spies of Vánar race, who tried To slay me, by this hand have died. Moved by this constant doubt and fear I saw thee, Prince, and came not near. When woe and peril gather round A foe in every form is found. Save Hanumán, O Raghu's son, And these, no friend is left me, none. Through their kind aid, a faithful band Who guard their lord from hostile hand, Rest when their chieftain rests and bend Their steps where'er he lists to wend,— Through them alone, in toil and pain, My wretched life I still sustain. [333]
- **Translation**: 

---

### Verse 20 (Ramayan 0.1200)
- **Original**: 1182 The Ramayana Enough, for thou hast heard in brief The story of my pain and grief. His mighty strength all regions know, My brother, but my deadly foe. Ah, if the proud oppressor fell, His death would all my woe dispel. Yea, on my cruel conqueror's fall My joy depends, my life, my all. This were the end and sure relief, O Ráma, of my tale of grief. Fair be his lot or dark with woe, No comfort like a friend I know.” Then Ráma spoke:“O friend, relate Whence sprang fraternal strife and hate, That duly taught by thee, I may Each foeman's strength and weakness weigh: And skilled in every chance restore The blissful state thou hadst before. For, when I think of all the scorn And bitter woe thou long hast borne, My soul indignant swells with pain Like waters flushed with furious rain. Then, ere I string this bended bow, Tell me the tale I long to know, Ere from the cord my arrow fly, And low in death thy foeman lie.” He spoke: Sugríva joyed to hear, Nor less his lords were glad of cheer: And thus to Ráma mighty-souled The cause that moved their strife he told:
- **Translation**: 

---

