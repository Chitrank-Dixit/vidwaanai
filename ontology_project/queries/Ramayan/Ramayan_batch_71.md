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

### Verse 1 (Ramayan 0.1401)
- **Original**: Canto LXV. The Council. 1383 And who this desperate leap will dare?” Canto LXV. The Council. But none of all the host was found To clear the sea with desperate bound, Though each, as Angad bade, declared His proper power and what he dared.779 Then spake good Jámbaván the sage, Chief of them all for reverend age; “I, Vánar chieftains, long ago Limbs light to leap could likewise show, But now on frame and spirit weighs The burthen of my length of days. Still task like this I may not slight, When Ráma and our king unite. So listen while I tell, O friends, What lingering strength mine age attends. If my poor leap may aught avail, Of ninety leagues, I will not fail. Far other strength in youth's fresh prime I boasted, in the olden time, When, at Prahláda's780 solemn rite, I circled in my rapid flight Lord VishGu, everlasting God, When through the universe he trod. 779 Each chief comes forward and says how far he can leap. Gaja says he can leap ten yojans. Gavaksha can leap twenty. Gavaya thirty, and so on up to ninety. 780 Prahláda, the son of HiraGyaka[ipu, was a pious Datya remarkable for his devotion to VishGu, and was on this account persecuted by his father.
- **Translation**: 

---

### Verse 2 (Ramayan 0.1402)
- **Original**: 1384 The Ramayana But now my limbs are weak and old, My youth is fled, its fire is cold, And these exhausted nerves to strain In such a task were idle pain.” Then Angad due obeisance paid, And to the chief his answer made: “Then I, ye noble Vánars, I Myself the mighty leap will try: Although perchance the power I lack To leap from Lanká's island back.” Thus the impetuous chieftain cried, And Jámbaván the sage replied: “Whate'er thy power and might may be, This task, O Prince, is not for thee. Kings go not forth themselves, but send The servants who their best attend. Thou art the darling and the boast, The honoured lord of all the host. In thee the root, O Angad, lies Of our appointed enterprise; And thee, on whom our hopes depend, Our care must cherish and defend.” Then Báli's noble son replied: “Needs must I go, whate'er betide, For, if no chief this exploit dare, What waits us all save blank despair,— Upon the ground again to lie In hopeless misery, fast, and die? For not a hope of life I see If we neglect our king's decree.” Then spoke the aged chief again: “Nay our attempt shall not be vain,
- **Translation**: 

---

### Verse 3 (Ramayan 0.1403)
- **Original**: Canto LXVI. Hanumán. 1385 For to the task will I incite A chieftain of sufficient might.” [392] Canto LXVI. Hanumán. The chieftain turned his glances where The legions sat in mute despair; And then to Hanumán, the best Of Vánar lords, these words addressed: “Why still, and silent, and apart, O hero of the dauntless heart? Thou keepest treasured in thy mind The laws that rule the Vánar kind, Strong as our king Sugríva, brave As Ráma's self to slay or save. Through every land thy praise is heard, Famous as that illustrious bird, Aríshmanemi's son,781 the king Of every fowl that plies the wing. Oft have I seen the monarch sweep With sounding pinions o'er the deep, And in his mighty talons bear Huge serpents struggling through the air. Thy arms, O hero, match in might The ample wings he spreads for flight; 781 The Bengal recension calls him Aríshmanemi's brother.“The commentator says‘Aríshmanemi is AruGa.’ AruGa the charioteer of the sun is the son of Ka [yapa and Vinatá and by consequence brother of Garu a, called Vainateya from Vinatá, his mother.” G ORRESSIO {FNS .
- **Translation**: 

---

### Verse 4 (Ramayan 0.1404)
- **Original**: 1386 The Ramayana And thou with him mayest well compare In power to do, in heart to dare. Why, rich in wisdom, power, and skill, O hero, art thou lingering still? An Apsaras782 the fairest found Of nymphs for heavenly charms renowned, Sweet Punjikasthalá, became A noble Vánar's wedded dame. Her heavenly title heard no more, Anjaná was the name she bore, When, cursed by Gods, from heaven she fell In Vánar form on earth to dwell, New-born in mortal shape the child Of Kunjar monarch of the wild. In youthful beauty wondrous fair, A crown of flowers about her hair, In silken robes of richest dye She roamed the hills that kiss the sky. Once in her tinted garments dressed She stood upon the mountain crest, The God of Wind beside her came, And breathed upon the lovely dame. And as he fanned her robe aside The wondrous beauty that he eyed In rounded lines of breast and limb And neck and shoulder ravished him; And captured by her peerless charms He strained her in his amorous arms. Then to the eager God she cried In trembling accents, terrified: “Whose impious love has wronged a spouse So constant in her nuptial vows?” 782 A nymph of Paradise.
- **Translation**: 

---

### Verse 5 (Ramayan 0.1405)
- **Original**: Canto LXVI. Hanumán. 1387 He heard, and thus his answer made: “O, be not troubled, nor afraid, But trust, and thou shalt know ere long My love has done thee, sweet, no wrong, So strong and brave and wise shall be The glorious child I give to thee. Might shall be his that naught can tire, And limbs to spring as springs his sire.” Thus spoke the God; the conquered dame Rejoiced in heart nor feared the shame. Down in a cave beneath the earth The happy mother gave thee birth. Once o'er the summit of the wood Before thine eyes the new sun stood. Thou sprangest up in haste to seize What seemed the fruitage of the trees. Up leapt the child, a wondrous bound, Three hundred leagues above the ground, And, though the angered Day-God shot His fierce beams on him, feared him not. Then from the hand of Indra came A red bolt winged with wrath and flame. The child fell smitten on a rock, His cheek was shattered by the shock, Named Hanumán 783 thenceforth by all In memory of the fearful fall. The wandering Wind-God saw thee lie With bleeding cheek and drooping eye, And stirred to anger by thy woe Forbade each scented breeze to blow. The breath of all the worlds was stilled, And the sad Gods with terror filled 783 Hanu or Hanú means jaw. Hanumán or Hanúmán means properly one with a large jaw.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1406)
- **Original**: 1388 The Ramayana Prayed to the Wind, to calm the ire And soothe the sorrow of the sire. His fiery wrath no longer glowed, And Brahmá's self the boon bestowed That in the brunt of battle none Should slay with steel the Wind-God's son. Lord Indra, sovereign of the skies, Bent on thee all his thousand eyes, And swore that ne'er the bolt which he Hurls from the heaven should injure thee. 'Tis thine, O mighty chief, to share The Wind-God's power, his son and heir. Sprung from that glorious father thou, And thou alone, canst aid us now. This earth of yore, through all her climes, I circled one-and-twenty times, And gathered, as the Gods decreed, Great store of herbs from hill and mead, Which, scattered o'er the troubled wave, The Amrit to the toilers gave.[393] But now my days are wellnigh told, My strength is gone, my limbs are old, And thou, the bravest and the best, Art the sure hope of all the rest. Now, mighty chief, the task assay: Thy matchless power and strength display. Rise up, O prince, our second king, And o'er the flood of ocean spring. So shall the glorious exploit vie With his who stepped through earth and sky.”784 784 VishGu, the God of the Three Steps.
- **Translation**: 

---

### Verse 7 (Ramayan 0.1407)
- **Original**: Canto LXVII. Hanumán's Speech. 1389 He spoke: the younger chieftain heard, His soul to vigorous effort stirred, And stood before their joyous eyes Dilated in gigantic size. Canto LXVII. Hanumán's Speech. Soon as his stature they beheld, Their fear and sorrow were dispelled; And joyous praises loud and long Rang out from all the Vánar throng. On the great chief their eyes they bent In rapture and astonishment, As, when his conquering foot he raised, The Gods upon NáráyaG785 gazed. He stood amid the joyous crowd, Bent to the chiefs, and cried aloud: “The Wind-God, Fire's eternal friend, Whose blasts the mountain summits rend, With boundless force that none may stay, Takes where he lists his viewless way. Sprung from that glorious father, I In power and speed with him may vie, A thousand times with airy leap Can circle loftiest Meru's steep: With my fierce arms can stir the sea Till from their bed the waters flee And rush at my command to drown 785 NáráyaG,“He who moved upon the waters,” is Vishnu. The allusion is to the famous three steps of that God.
- **Translation**: 

---

### Verse 8 (Ramayan 0.1408)
- **Original**: 1390 The Ramayana This land with grove and tower and town. I through the fields of air can spring Far swifter than the feathered King, And leap before him as he flies, On sounding pinions through the skies. I can pursue the Lord of Light Uprising from the eastern height, And reach him ere his course be sped With burning beams engarlanded. I will dry up the mighty main, Shatter the rocks and rend the plain. O'er earth and ocean will I bound, And every flower that grows on ground, And bloom of climbing plants shall show Strewn on the ground, the way I go, Bright as the lustrous path that lies Athwart the region of the skies.786 The Maithil lady will I find,— Thus speaks mine own prophetic mind,— And cast in hideous ruin down The shattered walls of Lanká's town.” Still on the chief in rapt surprise The Vánar legions bent their eyes, And thus again sage Jámbaván Addressed the glorious Hanumán: “Son of the Wind, thy promise cheers The Vánars' hearts, and calms their fears, Who, rescued from their dire distress, With prospering vows thy way will bless. The holy saints their favour lend, And all our chiefs the deed commend Urging thee forward on thy way: 786 The Milky Way.
- **Translation**: 

---

### Verse 9 (Ramayan 0.1409)
- **Original**: Canto LXVII. Hanumán's Speech. 1391 Arise then, and the task assay. Thou art our only refuge; we, Our lives and all, depend on thee.” Then sprang the Wind-God's son the best Of Vánars, on Mahendra's crest, And the great mountain rocked and swayed By that unusual weight dismayed, As reels an elephant beneath The lion's spring and rending teeth. The shady wood that crowned him shook, The trembling birds the boughs forsook, And ape and pard and lion fled From brake and lair disquieted. [394]
- **Translation**: 

---

### Verse 10 (Ramayan 0.1410)
- **Original**: BOOK V. 787 Canto I. Hanumán's Leap. Thus RávaG's foe resolved to trace The captive to her hiding-place Through airy pathways overhead Which heavenly minstrels visited. With straining nerve and eager brows, Like some strong husband of the cows, In ready might he stood prepared For the bold task his soul has dared. O'er gem-like grass that flashed and glowed The Vánar like a lion strode. Roused by the thunder of his tread, The beasts to shady coverts fled. Tall trees he crushed or hurled aside, And every bird was terrified. Around him loveliest lilies grew, Pale pink, and red, and white, and blue, And tints of many a metal lent 787 This Book is called Sundar or the Beatiful. To a European taste it is the most intolerably tedious of the whole poem, abounding in repetition, overloaded description, and long and useless speeches which impede the action of the poem. Manifest interpolations of whole Cantos also occur. I have omitted none of the action of the Book, but have occasionally omitted long passages of common-place description, lamentation, and long stories which have been again and again repeated.
- **Translation**: 

---

### Verse 11 (Ramayan 0.1411)
- **Original**: Canto I. Hanumán's Leap. 1393 The light of varied ornament. Gandharvas, changing forms at will, And Yakshas roamed the lovely hill, And countless Serpent-Gods were seen Where flowers and grass were fresh and green. As some resplendent serpent takes His pastime in the best of lakes, So on the mountain's woody height The Vánar wandered with delight. Then, standing on the flowery sod, He paid his vows to saint and God. Svayambhu 788 and the Sun he prayed, And the swift Wind to lend him aid, And Indra, sovereign of the skies, To bless his hardy enterprise. Then once again the chief addressed The Vánars from the mountain crest: “Swift as a shaft from Ráma's bow To RávaG's city will I go, And if she be not there will fly And seek the lady in the sky; Or, if in heaven she be not found, Will hither bring the giant bound.” He ceased; and mustering his might Sprang downward from the mountain height, While, shattered by each mighty limb, The trees unrooted followed him. The shadow on the ocean cast By his vast form, as on he passed, Flew like a ship before the gale When the strong breeze has filled the sail, And where his course the Vánar held 788 Brahmá the Self-Existent.
- **Translation**: 

---

### Verse 12 (Ramayan 0.1412)
- **Original**: 1394 The Ramayana The sea beneath him raged and swelled. Then Gods and all the heavenly train Poured flowerets down in gentle rain; Their voices glad Gandharvas raised, And saints in heaven the Vánar praised. Fain would the Sea his succour lend And Raghu's noble son befriend. He, moved by zeal for Ráma's sake, The hill Maináka789 thus bespake: “O strong Maináka, heaven's decree In days of old appointed thee To be the Asurs bar, and keep The rebels in the lowest deep. Thou guardest those whom heaven has cursed Lest from their prison-house they burst, And standest by the gates of hell Their limitary sentinel. To thee is given the power to spread Or spring above thy watery bed. Now, best of noble mountains, rise And do the thing that I advise. E'en now above thy buried crest Flies mighty Hanumán, the best Of Vánars, moved for Ráma's sake A wonderous deed to undertake. Lift up thy head that he may stay And rest him on his weary way.” He heard, and from his watery shroud, As bursts the sun from autumn cloud, Rose swifty, crowned with plant and tree, And stood above the foamy sea.790 789 Maináka was the son of Himálaya and Mená or Menaká. 790 Thus Milton makes the hills of heaven self-moving at command:
- **Translation**: 

---

### Verse 13 (Ramayan 0.1413)
- **Original**: Canto I. Hanumán's Leap. 1395 There with his lofty peaks upraised Bright as a hundred suns he blazed, And crest and crag of burnished gold Flashed on the flood that round him rolled. [395] The Vánar thought the mountain rose A hostile bar to interpose, And, like a wind-swept cloud, o'erthrew The glittering mountain as he flew. Then from the falling hill rang out A warning voice and joyful shout. Again he raised him high in air To meet the flying Vánar there, And standing on his topmost peak In human form began to speak:791 “Best of the Vánars' noblest line, A mighty task, O chief, is thine. Here for a while, I pray thee, light And rest upon the breezy height. A prince of Raghu's line was he Who gave his glory to the Sea,792 Who now to Ráma's envoy shows High honour for the debt he owes. He bade me lift my buried head Uprising from my watery bed, And woo the Vánar chief to rest A moment on my glittering crest. Refresh thy weary limbs, and eat “At his command the uprooted hills retired Each to his place, they heard his voice and went Obsequious” 791 The spirit of the mountain is separable from the mountain. Himalaya has also been represented as standing in human form on one of his own peaks. 792 Ságar or the Sea is said to have derived its name from Sagar. The story is fully told in Book I, Cantos XLII, XLIII, and XLIV.
- **Translation**: 

---

### Verse 14 (Ramayan 0.1414)
- **Original**: 1396 The Ramayana My mountain fruits for they are sweet. I too, O chieftain, know thee well; Three worlds thy famous virtues tell; And none, I ween, with thee may vie Who spring impetuous through the sky. To every guest, though mean and low. The wise respect and honour show; And how shall I neglect thee, how Slight the great guest so near me now? Son of the Wind, 'tis thine to share The might of him who shakes the air; And,— for he loves his offspring,— he Is honoured when I honour thee. Of yore, when Krita's age793 was new, The little hills and mountains flew Where'er they listed, borne on wings More rapid than the feathered king's.794 But mighty terror came on all The Gods and saints who feared their fall. And Indra in his anger rent Their pinions with the bolts he sent. When in his ruthless fury he Levelled his flashing bolt at me, The great-souled Wind inclined to save, And laid me neath the ocean's wave. Thus by the favour of the sire I kept my cherished wings entire; And for this deed of kindness done I honour thee his noble son. 793 Kritu is the first of the four ages of the world, the golden age, also called Satya. 794 Parvata means a mountain and in the Vedas a cloud. Hence in later mythology the mountains have taken the place of the clouds as the objects of the attacks of Indra the Sun-God. The feathered king is Garu a.
- **Translation**: 

---

### Verse 15 (Ramayan 0.1415)
- **Original**: Canto I. Hanumán's Leap. 1397 O come, thy weary limbs relieve, And honour due from me receive.” “I may not rest,” the Vánar cried; “I must not stay or turn aside. Yet pleased am I, thou noblest hill, And as the deed accept thy will.” Thus as he spoke he lightly pressed With his broad hand the mountain's crest, Then bounded upward to the height Of heaven, rejoicing in his might, And through the fields of boundless blue, The pathway of his father, flew. Gods, saints, and heavenly bards beheld That flight that none had paralleled, Then to the Nágas' mother795 came And thus addressed the sun-bright dame: “See, Hanumán with venturous leap Would spring across the mighty deep,— A Vánar prince, the Wind-God's seed: Come, Surasá, his course impede. In Rákshas form thy shape disguise, Terrific, like a hill in size: Let thy red eyes with fury glow, And high as heaven thy body grow. With fearful tusks the chief defy, That we his power and strength may try. He will with guile thy hold elude, Or own thy might, by thee subdued.” 795 “The children of Surasá were a thousand mighty many-headed serpents, traversing the sky.” W ILSON 'S{FNS VishGu PuráGa, Vol. II. p. 73.
- **Translation**: 

---

### Verse 16 (Ramayan 0.1416)
- **Original**: 1398 The Ramayana Pleased with the grateful honours paid, The godlike dame their words obeyed, Clad in a shape of terror she Sprang from the middle of the sea, And, with fierce accents that appalled All creatures, to the Vánar called: “Come, prince of Vánars, doomed to be My food this day by heaven's decree. Such boon from ages long ago To Brahmá's favouring will I owe.” She ceased, and Hanumán replied, By shape and threat unterrified: “Brave Ráma with his Maithil spouse Lodged in the shade of DaG ak's boughs, Thence Rávan king of giants stole Sítá the joy of Ráma's soul.[396] By Ráma's high behest to her I go a willing messenger; And never shouldst them hinder one Who toils for Da[aratha's son. First captive Sítá will I see, And him who sent and waits for me, Then come and to thy will submit, Yea, by my truth I promise it.” “Nay, hope not thus thy life to save; Not such the boon that Brahmá gave. Enter my mouth,” was her reply, “Then forward on thy journey hie!”796 796 She means, says the Commentator, pursue thy journey if thou can.
- **Translation**: 

---

### Verse 17 (Ramayan 0.1417)
- **Original**: Canto I. Hanumán's Leap. 1399 “Stretch, wider stretch thy jaws,” exclaimed The Vánar chief, to ire inflamed; And, as the Rákshas near him drew, Ten leagues in height his stature grew. Then straight, her threatening jaws between, A gulf of twenty leagues was seen. To fifty leagues he waxed, and still Her mouth grew wider at her will. Then smaller than a thumb became, Shrunk by his power, the Vánar's frame.797 He leaped within, and turning round Sprang through the portal at a bound. Then hung in air a moment, while He thus addressed her with a smile: “O Daksha's child,798 farewell at last! For I within thy mouth have passed. Thou hast the gift of Brahmá's grace: I go, the Maithil queen to trace.” Then, to her former shape restored, She thus addressed the Vánar lord: “Then forward to the task, and may Success and joy attend thy way! Go, and the rescued lady bring In triumph to her lord and king.” 797 If Milton's spirits are allowed the power of infinite self-extension and com- pression the same must be conceded to Válmíki's supernatural beings. Given the power as in Milton the result in Válmíki is perfectly consistent. 798 “Daksha is the son of Brahmá and one of the Prajápatis or divine pro- genitors. He had sixty daughters, twenty-seven of whom married to Ka[yapa produced, according to one of the Indian cosmogonies, all mundane beings. Does the epithet, Descendant of Daksha, given to Surasá, mean that she is one of those daughters? I think not. This epithet is perhaps an appellation common to all created beings as having sprung from Daksha.” G ORRESSIO {FNS .
- **Translation**: 

---

### Verse 18 (Ramayan 0.1418)
- **Original**: 1400 The Ramayana Then hosts of spirits as they gazed The daring of the Vánar praised. Through the broad fields of ether, fast Garu 's royal self, he passed, The region of the cloud and rain, Loved by the gay Gandharva train, Where mid the birds that came and went Shone Indra's glorious bow unbent, And like a host of wandering stars Flashed the high Gods' celestial cars. Fierce Sinhiká799 who joyed in ill And changed her form to work her will, Descried him on his airy way And marked the Vánar for her prey. “This day at length,” the demon cried, “My hunger shall be satisfied,” And at his passing shadow caught Delighted with the cheering thought. The Vánar felt the power that stayed And held him as she grasped his shade, Like some tall ship upon the main That struggles with the wind in vain. Below, above, his eye he bent And scanned the sea and firmament. High from the briny deep upreared The monster's hideous form appeared, “Sugríva's tale,” he cried,“is true: This is the demon dire to view Of whom the Vánar monarch told, Whose grasp a passing shade can hold.” Then, as a cloud in rain-time grows His form, dilating, swelled and rose. 799 Sinhiká is the mother of Ráhu the dragon's head or ascending node, the chief agent in eclipses.
- **Translation**: 

---

### Verse 19 (Ramayan 0.1419)
- **Original**: Canto I. Hanumán's Leap. 1401 Wide as the space from heaven to hell Her jaws she opened with a yell, And rushed upon her fancied prey With cloud-like roar to seize and slay. The Vánar swift as thought compressed His borrowed bulk of limb and chest, And stood with one quick bound inside The monstrous mouth she opened wide. Hid like the moon when Ráhu draws The orb within his ravening jaws. Within that ample cavern pent The demon's form he tore and rent, And, from the mangled carcass freed, Came forth again with thought-like speed.800 [397] Thus with his skill the fiend he slew, Then to his wonted stature grew. The spirits saw the demon die And hailed the Vánar from the sky: “Well hast thou fought a wondrous fight Nor spared the fiend's terrific might, On, on! perform the blameless deed, And in thine every wish succeed. Ne'er can they fail in whom combine Such valour, thought, and skill as thine.” 800 According to De Gubernatis, the author of the very learned, ingenious, and interesting though too fancifulZoological Mythology. Hanumán here represents the sun entering into and escaping from a cloud. The biblical Jonah, according to him, typifies the same phenomenon. Sá'dí, speaking of sunset, saysYùnas andar-i-dihán-imáhi shud: Jonas was within the fish's mouth. See A DDITIONAL N OTES {FNS .
- **Translation**: 

---

### Verse 20 (Ramayan 0.1420)
- **Original**: 1402 The Ramayana Pleased with their praises as they sang, Again through fields of air he sprang, And now, his travail wellnigh done, The distant shore was almost won. Before him on the margent stood In long dark line a waving wood, And the fair island, bright and green With flowers and trees, was clearly seen, And every babbling brook that gave Her lord the sea a tribute wave. He lighted down on Lamba's peak Which tinted metals stain and streak, And looked where Lanká's splendid town Shone on the mountain like a crown. Canto II. Lanká. The glorious sight a while he viewed, Then to the town his way pursued. Around the Vánar as he went Breathed from the wood delicious scent, And the soft grass beneath his feet With gem-like flowers was bright and sweet. Still as the Vánar nearer drew More clearly rose the town to view. The palm her fan-like leaves displayed, Priyálas801 lent their pleasant shade, And mid the lower greenery far Conspicuous rose the Kovidár.802 801 The Buchanania Latifolia. 802 The Bauhinia Variegata.
- **Translation**: 

---

