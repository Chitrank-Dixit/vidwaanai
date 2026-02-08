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

### Verse 1 (Ramayana 0.1406)
- **Original**: 1388 The Ramayana Prayed to the Wind, to calm the ire And soothe the sorrow of the sire. His fiery wrath no longer glowed, And Brahmá's self the boon bestowed That in the brunt of battle none Should slay with steel the Wind-God's son. Lord Indra, sovereign of the skies, Bent on thee all his thousand eyes, And swore that ne'er the bolt which he Hurls from the heaven should injure thee. 'Tis thine, O mighty chief, to share The Wind-God's power, his son and heir. Sprung from that glorious father thou, And thou alone, canst aid us now. This earth of yore, through all her climes, I circled one-and-twenty times, And gathered, as the Gods decreed, Great store of herbs from hill and mead, Which, scattered o'er the troubled wave, The Amrit to the toilers gave.[393] But now my days are wellnigh told, My strength is gone, my limbs are old, And thou, the bravest and the best, Art the sure hope of all the rest. Now, mighty chief, the task assay: Thy matchless power and strength display. Rise up, O prince, our second king, And o'er the flood of ocean spring. So shall the glorious exploit vie With his who stepped through earth and sky.”784 784 VishGu, the God of the Three Steps.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1407)
- **Original**: Canto LXVII. Hanumán's Speech. 1389 He spoke: the younger chieftain heard, His soul to vigorous effort stirred, And stood before their joyous eyes Dilated in gigantic size. Canto LXVII. Hanumán's Speech. Soon as his stature they beheld, Their fear and sorrow were dispelled; And joyous praises loud and long Rang out from all the Vánar throng. On the great chief their eyes they bent In rapture and astonishment, As, when his conquering foot he raised, The Gods upon NáráyaG785 gazed. He stood amid the joyous crowd, Bent to the chiefs, and cried aloud: “The Wind-God, Fire's eternal friend, Whose blasts the mountain summits rend, With boundless force that none may stay, Takes where he lists his viewless way. Sprung from that glorious father, I In power and speed with him may vie, A thousand times with airy leap Can circle loftiest Meru's steep: With my fierce arms can stir the sea Till from their bed the waters flee And rush at my command to drown 785 NáráyaG,“He who moved upon the waters,” is Vishnu. The allusion is to the famous three steps of that God.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1408)
- **Original**: 1390 The Ramayana This land with grove and tower and town. I through the fields of air can spring Far swifter than the feathered King, And leap before him as he flies, On sounding pinions through the skies. I can pursue the Lord of Light Uprising from the eastern height, And reach him ere his course be sped With burning beams engarlanded. I will dry up the mighty main, Shatter the rocks and rend the plain. O'er earth and ocean will I bound, And every flower that grows on ground, And bloom of climbing plants shall show Strewn on the ground, the way I go, Bright as the lustrous path that lies Athwart the region of the skies.786 The Maithil lady will I find,— Thus speaks mine own prophetic mind,— And cast in hideous ruin down The shattered walls of Lanká's town.” Still on the chief in rapt surprise The Vánar legions bent their eyes, And thus again sage Jámbaván Addressed the glorious Hanumán: “Son of the Wind, thy promise cheers The Vánars' hearts, and calms their fears, Who, rescued from their dire distress, With prospering vows thy way will bless. The holy saints their favour lend, And all our chiefs the deed commend Urging thee forward on thy way: 786 The Milky Way.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1409)
- **Original**: Canto LXVII. Hanumán's Speech. 1391 Arise then, and the task assay. Thou art our only refuge; we, Our lives and all, depend on thee.” Then sprang the Wind-God's son the best Of Vánars, on Mahendra's crest, And the great mountain rocked and swayed By that unusual weight dismayed, As reels an elephant beneath The lion's spring and rending teeth. The shady wood that crowned him shook, The trembling birds the boughs forsook, And ape and pard and lion fled From brake and lair disquieted. [394]
- **Translation**: 

---

### Verse 5 (Ramayana 0.1410)
- **Original**: BOOK V. 787 Canto I. Hanumán's Leap. Thus RávaG's foe resolved to trace The captive to her hiding-place Through airy pathways overhead Which heavenly minstrels visited. With straining nerve and eager brows, Like some strong husband of the cows, In ready might he stood prepared For the bold task his soul has dared. O'er gem-like grass that flashed and glowed The Vánar like a lion strode. Roused by the thunder of his tread, The beasts to shady coverts fled. Tall trees he crushed or hurled aside, And every bird was terrified. Around him loveliest lilies grew, Pale pink, and red, and white, and blue, And tints of many a metal lent 787 This Book is called Sundar or the Beatiful. To a European taste it is the most intolerably tedious of the whole poem, abounding in repetition, overloaded description, and long and useless speeches which impede the action of the poem. Manifest interpolations of whole Cantos also occur. I have omitted none of the action of the Book, but have occasionally omitted long passages of common-place description, lamentation, and long stories which have been again and again repeated.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1411)
- **Original**: Canto I. Hanumán's Leap. 1393 The light of varied ornament. Gandharvas, changing forms at will, And Yakshas roamed the lovely hill, And countless Serpent-Gods were seen Where flowers and grass were fresh and green. As some resplendent serpent takes His pastime in the best of lakes, So on the mountain's woody height The Vánar wandered with delight. Then, standing on the flowery sod, He paid his vows to saint and God. Svayambhu 788 and the Sun he prayed, And the swift Wind to lend him aid, And Indra, sovereign of the skies, To bless his hardy enterprise. Then once again the chief addressed The Vánars from the mountain crest: “Swift as a shaft from Ráma's bow To RávaG's city will I go, And if she be not there will fly And seek the lady in the sky; Or, if in heaven she be not found, Will hither bring the giant bound.” He ceased; and mustering his might Sprang downward from the mountain height, While, shattered by each mighty limb, The trees unrooted followed him. The shadow on the ocean cast By his vast form, as on he passed, Flew like a ship before the gale When the strong breeze has filled the sail, And where his course the Vánar held 788 Brahmá the Self-Existent.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1412)
- **Original**: 1394 The Ramayana The sea beneath him raged and swelled. Then Gods and all the heavenly train Poured flowerets down in gentle rain; Their voices glad Gandharvas raised, And saints in heaven the Vánar praised. Fain would the Sea his succour lend And Raghu's noble son befriend. He, moved by zeal for Ráma's sake, The hill Maináka789 thus bespake: “O strong Maináka, heaven's decree In days of old appointed thee To be the Asurs bar, and keep The rebels in the lowest deep. Thou guardest those whom heaven has cursed Lest from their prison-house they burst, And standest by the gates of hell Their limitary sentinel. To thee is given the power to spread Or spring above thy watery bed. Now, best of noble mountains, rise And do the thing that I advise. E'en now above thy buried crest Flies mighty Hanumán, the best Of Vánars, moved for Ráma's sake A wonderous deed to undertake. Lift up thy head that he may stay And rest him on his weary way.” He heard, and from his watery shroud, As bursts the sun from autumn cloud, Rose swifty, crowned with plant and tree, And stood above the foamy sea.790 789 Maináka was the son of Himálaya and Mená or Menaká. 790 Thus Milton makes the hills of heaven self-moving at command:
- **Translation**: 

---

### Verse 8 (Ramayana 0.1413)
- **Original**: Canto I. Hanumán's Leap. 1395 There with his lofty peaks upraised Bright as a hundred suns he blazed, And crest and crag of burnished gold Flashed on the flood that round him rolled. [395] The Vánar thought the mountain rose A hostile bar to interpose, And, like a wind-swept cloud, o'erthrew The glittering mountain as he flew. Then from the falling hill rang out A warning voice and joyful shout. Again he raised him high in air To meet the flying Vánar there, And standing on his topmost peak In human form began to speak:791 “Best of the Vánars' noblest line, A mighty task, O chief, is thine. Here for a while, I pray thee, light And rest upon the breezy height. A prince of Raghu's line was he Who gave his glory to the Sea,792 Who now to Ráma's envoy shows High honour for the debt he owes. He bade me lift my buried head Uprising from my watery bed, And woo the Vánar chief to rest A moment on my glittering crest. Refresh thy weary limbs, and eat “At his command the uprooted hills retired Each to his place, they heard his voice and went Obsequious” 791 The spirit of the mountain is separable from the mountain. Himalaya has also been represented as standing in human form on one of his own peaks. 792 Ságar or the Sea is said to have derived its name from Sagar. The story is fully told in Book I, Cantos XLII, XLIII, and XLIV.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1414)
- **Original**: 1396 The Ramayana My mountain fruits for they are sweet. I too, O chieftain, know thee well; Three worlds thy famous virtues tell; And none, I ween, with thee may vie Who spring impetuous through the sky. To every guest, though mean and low. The wise respect and honour show; And how shall I neglect thee, how Slight the great guest so near me now? Son of the Wind, 'tis thine to share The might of him who shakes the air; And,— for he loves his offspring,— he Is honoured when I honour thee. Of yore, when Krita's age793 was new, The little hills and mountains flew Where'er they listed, borne on wings More rapid than the feathered king's.794 But mighty terror came on all The Gods and saints who feared their fall. And Indra in his anger rent Their pinions with the bolts he sent. When in his ruthless fury he Levelled his flashing bolt at me, The great-souled Wind inclined to save, And laid me neath the ocean's wave. Thus by the favour of the sire I kept my cherished wings entire; And for this deed of kindness done I honour thee his noble son. 793 Kritu is the first of the four ages of the world, the golden age, also called Satya. 794 Parvata means a mountain and in the Vedas a cloud. Hence in later mythology the mountains have taken the place of the clouds as the objects of the attacks of Indra the Sun-God. The feathered king is Garu a.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1415)
- **Original**: Canto I. Hanumán's Leap. 1397 O come, thy weary limbs relieve, And honour due from me receive.” “I may not rest,” the Vánar cried; “I must not stay or turn aside. Yet pleased am I, thou noblest hill, And as the deed accept thy will.” Thus as he spoke he lightly pressed With his broad hand the mountain's crest, Then bounded upward to the height Of heaven, rejoicing in his might, And through the fields of boundless blue, The pathway of his father, flew. Gods, saints, and heavenly bards beheld That flight that none had paralleled, Then to the Nágas' mother795 came And thus addressed the sun-bright dame: “See, Hanumán with venturous leap Would spring across the mighty deep,— A Vánar prince, the Wind-God's seed: Come, Surasá, his course impede. In Rákshas form thy shape disguise, Terrific, like a hill in size: Let thy red eyes with fury glow, And high as heaven thy body grow. With fearful tusks the chief defy, That we his power and strength may try. He will with guile thy hold elude, Or own thy might, by thee subdued.” 795 “The children of Surasá were a thousand mighty many-headed serpents, traversing the sky.” W ILSON 'S{FNS VishGu PuráGa, Vol. II. p. 73.
- **Translation**: 

---

### Verse 11 (Ramayana 0.1416)
- **Original**: 1398 The Ramayana Pleased with the grateful honours paid, The godlike dame their words obeyed, Clad in a shape of terror she Sprang from the middle of the sea, And, with fierce accents that appalled All creatures, to the Vánar called: “Come, prince of Vánars, doomed to be My food this day by heaven's decree. Such boon from ages long ago To Brahmá's favouring will I owe.” She ceased, and Hanumán replied, By shape and threat unterrified: “Brave Ráma with his Maithil spouse Lodged in the shade of DaG ak's boughs, Thence Rávan king of giants stole Sítá the joy of Ráma's soul.[396] By Ráma's high behest to her I go a willing messenger; And never shouldst them hinder one Who toils for Da[aratha's son. First captive Sítá will I see, And him who sent and waits for me, Then come and to thy will submit, Yea, by my truth I promise it.” “Nay, hope not thus thy life to save; Not such the boon that Brahmá gave. Enter my mouth,” was her reply, “Then forward on thy journey hie!”796 796 She means, says the Commentator, pursue thy journey if thou can.
- **Translation**: 

---

### Verse 12 (Ramayana 0.1417)
- **Original**: Canto I. Hanumán's Leap. 1399 “Stretch, wider stretch thy jaws,” exclaimed The Vánar chief, to ire inflamed; And, as the Rákshas near him drew, Ten leagues in height his stature grew. Then straight, her threatening jaws between, A gulf of twenty leagues was seen. To fifty leagues he waxed, and still Her mouth grew wider at her will. Then smaller than a thumb became, Shrunk by his power, the Vánar's frame.797 He leaped within, and turning round Sprang through the portal at a bound. Then hung in air a moment, while He thus addressed her with a smile: “O Daksha's child,798 farewell at last! For I within thy mouth have passed. Thou hast the gift of Brahmá's grace: I go, the Maithil queen to trace.” Then, to her former shape restored, She thus addressed the Vánar lord: “Then forward to the task, and may Success and joy attend thy way! Go, and the rescued lady bring In triumph to her lord and king.” 797 If Milton's spirits are allowed the power of infinite self-extension and com- pression the same must be conceded to Válmíki's supernatural beings. Given the power as in Milton the result in Válmíki is perfectly consistent. 798 “Daksha is the son of Brahmá and one of the Prajápatis or divine pro- genitors. He had sixty daughters, twenty-seven of whom married to Ka[yapa produced, according to one of the Indian cosmogonies, all mundane beings. Does the epithet, Descendant of Daksha, given to Surasá, mean that she is one of those daughters? I think not. This epithet is perhaps an appellation common to all created beings as having sprung from Daksha.” G ORRESSIO {FNS .
- **Translation**: 

---

### Verse 13 (Ramayana 0.1418)
- **Original**: 1400 The Ramayana Then hosts of spirits as they gazed The daring of the Vánar praised. Through the broad fields of ether, fast Garu 's royal self, he passed, The region of the cloud and rain, Loved by the gay Gandharva train, Where mid the birds that came and went Shone Indra's glorious bow unbent, And like a host of wandering stars Flashed the high Gods' celestial cars. Fierce Sinhiká799 who joyed in ill And changed her form to work her will, Descried him on his airy way And marked the Vánar for her prey. “This day at length,” the demon cried, “My hunger shall be satisfied,” And at his passing shadow caught Delighted with the cheering thought. The Vánar felt the power that stayed And held him as she grasped his shade, Like some tall ship upon the main That struggles with the wind in vain. Below, above, his eye he bent And scanned the sea and firmament. High from the briny deep upreared The monster's hideous form appeared, “Sugríva's tale,” he cried,“is true: This is the demon dire to view Of whom the Vánar monarch told, Whose grasp a passing shade can hold.” Then, as a cloud in rain-time grows His form, dilating, swelled and rose. 799 Sinhiká is the mother of Ráhu the dragon's head or ascending node, the chief agent in eclipses.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1419)
- **Original**: Canto I. Hanumán's Leap. 1401 Wide as the space from heaven to hell Her jaws she opened with a yell, And rushed upon her fancied prey With cloud-like roar to seize and slay. The Vánar swift as thought compressed His borrowed bulk of limb and chest, And stood with one quick bound inside The monstrous mouth she opened wide. Hid like the moon when Ráhu draws The orb within his ravening jaws. Within that ample cavern pent The demon's form he tore and rent, And, from the mangled carcass freed, Came forth again with thought-like speed.800 [397] Thus with his skill the fiend he slew, Then to his wonted stature grew. The spirits saw the demon die And hailed the Vánar from the sky: “Well hast thou fought a wondrous fight Nor spared the fiend's terrific might, On, on! perform the blameless deed, And in thine every wish succeed. Ne'er can they fail in whom combine Such valour, thought, and skill as thine.” 800 According to De Gubernatis, the author of the very learned, ingenious, and interesting though too fancifulZoological Mythology. Hanumán here represents the sun entering into and escaping from a cloud. The biblical Jonah, according to him, typifies the same phenomenon. Sá'dí, speaking of sunset, saysYùnas andar-i-dihán-imáhi shud: Jonas was within the fish's mouth. See A DDITIONAL N OTES {FNS .
- **Translation**: 

---

### Verse 15 (Ramayana 0.1420)
- **Original**: 1402 The Ramayana Pleased with their praises as they sang, Again through fields of air he sprang, And now, his travail wellnigh done, The distant shore was almost won. Before him on the margent stood In long dark line a waving wood, And the fair island, bright and green With flowers and trees, was clearly seen, And every babbling brook that gave Her lord the sea a tribute wave. He lighted down on Lamba's peak Which tinted metals stain and streak, And looked where Lanká's splendid town Shone on the mountain like a crown. Canto II. Lanká. The glorious sight a while he viewed, Then to the town his way pursued. Around the Vánar as he went Breathed from the wood delicious scent, And the soft grass beneath his feet With gem-like flowers was bright and sweet. Still as the Vánar nearer drew More clearly rose the town to view. The palm her fan-like leaves displayed, Priyálas801 lent their pleasant shade, And mid the lower greenery far Conspicuous rose the Kovidár.802 801 The Buchanania Latifolia. 802 The Bauhinia Variegata.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1421)
- **Original**: Canto II. Lanká. 1403 A thousand trees mid flowers that glowed Hung down their fruit's delicious load,803 And in their crests that rocked and swayed Sweet birds delightful music made. And there were pleasant pools whereon The glories of the lotus shone; And gleams of sparkling fountains, stirred By many a joyous water-bird. Around, in lovely gardens grew Blooms sweet of scent and bright of hue, And Lanká, seat of RávaG's sway, Before the wondering Vánar lay: With stately domes and turrets tall, Encircled by a golden wall, And moats whose waters were aglow With lily blossoms bright below: For Sítá's sake defended well With bolt and bar and sentinel, And Rákshases who roamed in bands With ready bows in eager hands. He saw the stately mansions rise Like pale-hued clouds in autumn skies; Where noble streets were broad and bright, And banners waved on every height. Her gates were glorious to behold Rich with the shine of burnished gold: A lovely city planned and decked By heaven's creative architect,804 Fairest of earthly cities meet To be the Gods' celestial seat. The Vánar by the northern gate 803 Through the power that RávaG's stern mortifications had won for him his trees bore flowers and fruit simultaneously. 804 Vi[vakarmá is the architect of the Gods.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1422)
- **Original**: 1404 The Ramayana Thus in his heart began debate “Our mightiest host would strive in vain To take this city on the main: A city that may well defy The chosen warriors of the sky; A city never to be won E'en by the arm of Raghu's son. Here is no hope by guile to win The hostile hearts of those within. 'Twere vain to war, or bribe, or sow Dissension mid the Vánar foe. But now my search must I pursue Until the Maithil queen I view: And, when I find the captive dame, Make victory mine only aim. But, if I wear my present shape, How shall I enter and escape The Rákshas troops, their guards and spies, And sleepless watch of cruel eyes? The fiends of giant race who hold This mighty town are strong and bold; And I must labour to elude The fiercely watchful multitude. I in a shape to mock their sight Must steal within the town by night, Blind with my art the demons' eyes, And thus achieve my enterprise. How may I see, myself unseen Of the fierce king, the captive queen, And meet her in some lonely place, With none beside her, face to face?” When the bright sun had left the skies The Vánar dwarfed his mighty size,[398]
- **Translation**: 

---

### Verse 18 (Ramayana 0.1423)
- **Original**: Canto III. The Guardian Goddess. 1405 And, in the straitest bounds restrained, The bigness of a cat retained.805 Then, when the moon's soft light was spread, Within the city's walls he sped. Canto III. The Guardian Goddess. There from the circling rampart's height He gazed upon the wondrous sight; Broad gates with burnished gold displayed, And courts with turkises inlaid; With gleaming silver, gems, and rows Of crystal stairs and porticoes. In semblance of a Rákshas dame The city's guardian Goddess came,— For she with glances sure and keen The entrance of a foe had seen,— And thus with fury in her eye Addressed him with an angry cry: “Who art thou? what has led thee, say, Within these walls to find thy way? Thou mayst not enter here in spite Of RávaG and his warriors' might.” “And who art thou?” the Vánar cried, By form and frown unterrified, “Why hast thou met me by the gate, And chid me thus infuriate?” 805 So in Paradise Lost Satan when he has stealthily entered the garden of Eden assumes the form of a cormorant.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1424)
- **Original**: 1406 The Ramayana He ceased: and Lanká made reply: “The guardian of the town am I, Who watch for ever to fulfil My lord the Rákshas monarch's will. But thou shalt fall this hour, and deep Shall be thy never-ending sleep.” Again he spake:“In spite of thee This golden city will I see. Her gates and towers, and all the pride Of street and square from side to side, And freely wander where I please Amid her groves of flowering trees; On all her beauties sate mine eye. Then, as I came, will homeward hie.” Swift with an angry roar she smote With her huge hand the Vánar's throat. The smitten Vánar, rage-impelled, With fist upraised the monster felled: But quick repented, stirred with shame And pity for a vanquished dame, When with her senses troubled, weak With terror, thus she strove to speak: “O spare me thou whose arm is strong: O spare me, and forgive the wrong. The brave that law will ne'er transgress That spares a woman's helplessness. Hear, best of Vánars, brave and bold, What Brahmá's self of yore foretold; “Beware,” he said,“the fatal hour When thou shalt own a Vánar's power. Then is the giants' day of fear, For terror and defeat are near.”
- **Translation**: 

---

### Verse 20 (Ramayana 0.1425)
- **Original**: Canto IV. Within The City. 1407 Now, Vánar chief, o'ercome by thee, I own the truth of heaven's decree. For Sítá's sake will ruin fall On RávaG, and his town, and all.” Canto IV. Within The City. The guardian goddess thus subdued, The Vánar chief his way pursued, And reached the broad imperial street Where fresh-blown flowers were bright and sweet. The city seemed a fairer sky Where cloud-like houses rose on high, Whence the soft sound of tabors came Through many a latticed window frame, And ever and anon rang out The merry laugh and joyous shout. From house to house the Vánar went And marked each varied ornament, Where leaves and blossoms deftly strung About the crystal columns hung. Then soft and full and sweet and clear The song of women charmed his ear, And, blending with their dulcet tones, Their anklets' chime and tinkling zones. He heard the Rákshas minstrel sing The praises of their matchless king; And softly through the evening air Came murmurings of text and prayer. Here moved a priest with tonsured head, And there an eager envoy sped,
- **Translation**: 

---

