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

### Verse 1 (Ramayana 0.1386)
- **Original**: 1368 The Ramayana Once on the day when Vritra765 died, We brothers, in ambitious pride, Sought, mounting with adventurous flight, The Day-God garlanded with light. On, ever on we urged our way Where fields of ether round us lay, Till, by the fervent heat assailed, My brother's pinions flagged and failed. I marked his sinking strength, and spread My stronger wings to screen his head, Till, all my feathers burnt away, On Vindhya's hill I fell and lay. There in my lone and helpless state I heard not of my brother's fate.” Thus King Sampáti spoke and sighed: And royal Angad thus replied: “If, brother of Jatáyus, thou Hast heard the tale I told but now, Obedient to mine earnest prayer The dwelling of that fiend declare. O, say where cursed RávaG dwells, Whom folly to his death impels.” 765 Vritra,“the coverer, hider, obstructer (of rain)” is the name of the Vedic personification of an imaginary malignant influence or demon of darkness and drought supposed to take possession of the clouds, causing them to obstruct the clearness of the sky and keep back the waters. Indra is represented as battling with this evil influence, and the pent-up clouds being practically represented as mountains or castles are shattered by his thunderbolt and made to open their receptacles.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1387)
- **Original**: Canto LVIII. Tidings Of Sítá. 1369 He ceased. Again Sampáti spoke, And hope in every breast awoke: “Though lost my wings, and strength decayed, Yet shall my words lend Ráma aid. I know the worlds where VishGu trod,766 I know the realm of Ocean's God; How Asurs fought with heavenly foes, And Amrit from the churning rose.767 A mighty task before me lies, To prosper Ráma's enterprise, A task too hard for one whom length Of days has rifled of his strength. I saw the cruel RávaG bear A gentle lady through the air. Bright was her form, and fresh and young, And sparkling gems about her hung. “O Ráma, Ráma!” cried the dame, And shrieked in terror LakshmaG's name, As, struggling in the giant's hold, She dropped her gauds of gems and gold. Like sun-light on a mountain shone The silken garments she had on, And glistened o'er his swarthy form As lightning flashes through the storm. That giant RávaG, famed of old, Is brother of the Lord of Gold.768 The southern ocean roars and swells Round Lanká, where the robber dwells In his fair city nobly planned 766 Frequent mention has been made of the three steps of VishGu typifying the rising, culmination, and setting of the sun. 767 For theChurning of the Sea, see Book I, Canto XLV. 768 Kuvera, the God of Wealth.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1388)
- **Original**: 1370 The Ramayana And built by Vi[vakarmá's769 hand. Within his bower securely barred, With monsters round her for a guard, Still in her silken vesture clad Lies Sítá, and her heart is sad. A hundred leagues your course must be Beyond this margin of the sea. Still to the south your way pursue, And there the giant RávaG view. Then up, O Vánars, and away! For by my heavenly lore I say, There will you see the lady's face, And hither soon your steps retrace. In the first field of air are borne The doves and birds that feed on corn. The second field supports the crows And birds whose food on branches grows. Along the third in balanced flight Sail the keen osprey and the kite. Swift through the fourth the falcon springs The fifth the slower vulture wings. Up to the sixth the gay swans rise,[388] Where royal Vainateya770 flies. We too, O chiefs, of vulture race, Our line from Vinatá may trace, Condemned, because we wrought a deed Of shame, on flesh and blood to feed. But all SuparGa's771 wondrous powers And length of keenest sight are ours, That we a hundred leagues away Through fields of air descry our prey. 769 The architect of the gods. 770 Garu a, son of Vinatá, the sovereign of the birds. 771 “The well winged one,” Garu a.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1389)
- **Original**: Canto LIX. Sampáti's Story. 1371 Now from this spot my gazing eye Can RávaG and the dame descry. Devise some plan to overleap This barrier of the briny deep. Find the Videhan lady there, And joyous to your home repair. Me too, O Vánars, to the side Of VaruG's772 home the ocean, guide, Where due libations shall be paid To my great-hearted brother's shade.” Canto LIX. Sampáti's Story. They heard his counsel to the close, Then swiftly to their feet they rose; And Jámbaván with joyous breast The vulture king again addressed: “Where, where is Sítá? who has seen, Who borne away the Maithil queen? Who would the lightning flight withstand by LakshmaG's hand?” 772 The god of the sea.
- **Translation**: 

---

### Verse 5 (Ramayana 0.1390)
- **Original**: 1372 The Ramayana Again Sampáti spoke to cheer The Vánars as they bent to hear: “Now listen, and my words shall show What of the Maithil dame I know, And in what distant prison lies The lady of the long dark eyes. Scorched by the fiery God of Day, High on this mighty hill I lay. A long and weary time had passed, And strength and life were failing fast. Yet, ere the breath had left my frame, My son, my dear Supár[va, came. Each morn and eve he brought me food, And filial care my life renewed. But serpents still are swift to ire, Gandharvas slaves to soft desire, And we, imperial vultures, need A full supply our maws to feed. Once he turned at close of day, Stood by my side, but brought no prey. He looked upon my ravenous eye, Heard my complaint and made reply: “Borne on swift wings ere day was light I stood upon Mahendra's773 height, And, far below, the sea I viewed And birds in countless multitude. Before mine eyes a giant flew Whose monstrous form was dark of hue And struggling in his grasp was borne A lady radiant as the morn. Swift to the south his course he bent, And cleft the yielding element. 773 Mahendra is chain of mountains generally identified with part of the Gháts of the Peninsula.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1391)
- **Original**: Canto LX. Sampáti's Story. 1373 The holy spirits of the air Came round me as I marvelled there, And cried as their bright legions met: “O say, is Sítá living yet?” Thus cried the saints and told the name Of him who held the struggling dame. Then while mine eye with eager look Pursued the path the robber took, I marked the lady's streaming hair, And heard her cry of wild despair. I saw her silken vesture rent And stripped of every ornament, Thus, O my father, fled the time: Forgive, I pray, the heedless crime.” In vain the mournful tale I heard My pitying heart to fury stirred, What could a helpless bird of air, Reft of his boasted pinions, dare? Yet can I aid with all that will And words can do, and friendly skill.” Canto LX. Sampáti's Story. Then from the flood Sampáti paid Due offerings to his brother's shade. He bathed him when the rites were done, And spake again to Báli's son: “Now listen, Prince, while I relate How first I learned the lady's fate. Burnt by the sun's resistless might I fell and lay on Vindhya's height.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1392)
- **Original**: 1374 The Ramayana Seven nights in deadly swoon I passed, But struggling life returned at last. Around I bent my wondering view, But every spot was strange and new. I scanned the sea with eager ken, And rock and brook and lake and glen, I saw gay trees their branches wave, And creepers mantling o'er the cave. I heard the wild birds' joyous song, And waters as they foamed along, And knew the lovely hill must be Mount Vindhya by the southern sea.[389] Revered by heavenly beings, stood Near where I lay, a sacred wood, Where great Ni[akar dwelt of yore And pains of awful penance bore. Eight thousand seasons winged their flight Over the toiling anchorite— Upon that hill my days were spent,— And then to heaven the hermit went. At last, with long and hard assay, Down from that height I made my way, And wandered through the mountain pass Rough with the spikes of Darbha grass. I with my misery worn, and faint Was eager to behold the saint: For often with Jamáyus I Had sought his home in days gone by. As nearer to the grove I drew The breeze with cooling fragrance blew, And not a tree that was not fair, With richest flower and fruit was there. With anxious heart a while I stayed Beneath the trees' delightful shade,
- **Translation**: 

---

### Verse 8 (Ramayana 0.1393)
- **Original**: Canto LXI. Sampáti's Story. 1375 And soon the holy hermit, bright With fervent penance, came in sight. Behind him bears and lions, tame As those who know their feeder, came, And tigers, deer, and snakes pursued His steps, a wondrous multitude, And turned obeisant when the sage Had reached his shady hermitage. Then came Ni[akar to my side And looked with wondering eyes, and cried: “I knew thee not, so dire a change Has made thy form and feature strange. Where are thy glossy feathers? where The rapid wings that cleft the air? Two vulture brothers once I knew: Each form at will could they endue. They of the vulture race were kings, And flew with Mátari[va's774 wings. In human shape they loved to greet Their hermit friend, and clasp his feet. The younger was Jamáyus, thou The elder whom I gaze on now. Say, has disease or foeman's hate Reduced thee from thy high estate?” Canto LXI. Sampáti's Story. 774 Mátari[va is identified with Váyu, the wind.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1394)
- **Original**: 1376 The Ramayana “Ah me! o'erwhelmed with shame and weak With wounds,” I cried,“I scarce can speak. My hapless brother once and I Our strength of flight resolved to try. And by our foolish pride impelled Our way through realms of ether held. We vowed before the saints who tread The wilds about Kailása's head, That we with following wings would chase The swift sun to his resting place. Up on our soaring pinions through The fields of cloudless air we flew. Beneath us far, and far away, Like chariot wheels bright cities lay, Whence in wild snatches rose the song Of women mid the gay-clad throng, With sounds of sweetest music blent And many a tinkling ornament. Then as our rapid wings we strained The pathway of the sun we gained. Beneath us all the earth was seen Clad in her garb of tender green, And every river in her bed Meandered like a silver thread. We looked on Meru far below And Vindhya and the Lord of Snow, Like elephants that bend to cool Their fever in a lilied pool. But fervent heat and toil o'ercame The vigour of each yielding frame, Our weary hearts began to quail, And wildered sense to reel and fail. We knew not, fainting and distressed, The north or south or east or west.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1395)
- **Original**: Canto LXII. Sampáti's Story. 1377 With a great strain mine eyes I turned Where the fierce sun before me burned, And seemed to my astonished eyes The equal of the earth in size.775 At length, o'erpowered, Jamáyus fell Without a word to say farewell, And when to earth I saw him hie I followed headlong from the sky.776 With sheltering wings I intervened And from the sun his body screened, But lost, for heedless folly doomed, My pinions which the heat consumed. In Janasthán, I hear them say, My hapless brother fell and lay. I, pinionless and faint and weak, Dropped upon Vindhya's woody peak. Now with my swift wings burnt away, Reft of my brother and my sway, From this tall mountain's summit I Will cast me headlong down and die.” [390] Canto LXII. Sampáti's Story. 775 Of course not equal to the whole earth, says the Commentator, but equal to Janasthán. 776 This appears to be the Indian form of the stories of Phaethon and Dædalus and Icarus.
- **Translation**: 

---

### Verse 11 (Ramayana 0.1396)
- **Original**: 1378 The Ramayana “As to the saint I thus complained My bitter tears fell unrestrained. He pondered for a while, then broke The silence, and thus calmly spoke: “Forth from thy sides again shall spring, O royal bird, each withered wing, And all thine ancient power and might Return to thee with strength of sight. A noble deed has been foretold In prophecy pronounced of old: Nor dark to me are future things, Seen by the light which penance brings. A glorious king shall rise and reign, The pride of old Ikshváku's strain. A good and valiant prince, his heir, Shall the dear name of Ráma bear. With his brave brother LakshmaG he An exile in the woods shall be, Where RávaG, whom no God may slay,777 Shall steal his darling wife away. In vain the captive will be wooed With proffered love and dainty food, She will not hear, she will not taste: But, lest her beauty wane and waste, Lord Indra's self will come to her With heavenly food, and minister. Then envoys of the Vánar race By Ráma sent will seek this place. To them, O roamer of the air, The lady's fate shalt thou declare. Thou must not move— so maimed thou art Thou canst not from this spot depart. 777 According to the promise, given him by Brahmá. See Book I, Canto XIV.
- **Translation**: 

---

### Verse 12 (Ramayana 0.1397)
- **Original**: Canto LXIII. Sampáti's Story. 1379 Await the day and moment due, And thy burnt wings will sprout anew. I might this day the boon bestow And bid again thy pinions grow, But wait until thy saving deed The nations from their fear have freed. Then for this glorious aid of thine The princes of Ikshváku's line, And Gods above and saints below Eternal gratitude shall owe. Fain would mine aged eyes behold That pair of whom my lips have told, Yet wearied here I must not stay, But leave my frame and pass away.” Canto LXIII. Sampáti's Story. “With this and many a speech beside My failing heart he fortified, With glorious hope my breast inspired, And to his holy home retired. I scaled the mountain height, to view The region round, and looked for you. In ceaseless watchings night and day A hundred seasons passed away, And by the sage's words consoled I wait the hour and chance foretold. But since Ni[akar sought the skies. And cast away all earthly ties, Full many a care and doubt has pressed With grievous weight upon my breast.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1398)
- **Original**: 1380 The Ramayana But for the saint who turned aside My purpose I had surely died. Those hopeful words the hermit spake, That bid me live for Ráma's sake, Dispel my anguish as the light Of lamp and torch disperse the night.” He ceased: and in the Vánars' view Forth from his side young pinions grew, And boundless rapture filled his breast As thus the chieftains he addressed: “Joy, joy! the pinions, which the Lord Of Day consumed, are now restored Through the dear grace & boundless might Of that illustrious anchorite. The fire of youth within me burns, And all my wonted strength returns. Onward, ye Vánars, toil strive, And you shall find the dame alive. Look on these new-found wings, and hence Be strong in surest confidence.” Swift from the crag he sprang to try His pinions in his native sky. His words the chieftains' doubts had stilled, And every heart with courage filled.778 778 In the Bengal recension the fourth Book ends here, the remaining Cantos being placed in the fifth.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1399)
- **Original**: Canto LXIV. The Sea. 1381 Canto LXIV. The Sea. Shouts of triumphant joy outrang As to their feet the Vánars sprang: And, on the mighty task intent, Swift to the sea their steps they bent. They stood and gazed upon the deep, Whose billows with a roar and leap On the sea banks ware wildly hurled,— The mirror of the mighty world. There on the strand the Vánars stayed And with sad eyes the deep surveyed, Here, as in play, his billows rose, And there he slumbered in repose. Here leapt the boisterous waters, high As mountains, menacing the sky, And wild infernal forms between The ridges of the waves were seen. [391] They saw the billows rave and swell, And their sad spirits sank and fell; For ocean in their deep despair Seemed boundless as the fields of air. Then noble Angad spake to cheer The Vánars and dispel their fear: “Faint not: despair should never find Admittance to a noble mind. Despair, a serpent's mortal bite, Benumbs the hero's power and might.”
- **Translation**: 

---

### Verse 15 (Ramayana 0.1400)
- **Original**: 1382 The Ramayana Then passed the weary night, and all Assembled at their prince's call, And every lord of high estate Was gathered round him for debate. Bright was the chieftains' glorious band Round Angad on the ocean strand, As when the mighty Storm-Gods meet Round Indra on his golden seat. Then princely Angad looked on each, And thus began his prudent speech: “What chief of all our host will leap A hundred leagues across the deep? Who, O illustrious Vánars, who Will make Sugríva's promise true, And from our weight of fear set free The leaders of our band and me? To whom, O warriors, shall we owe A sweet release from pain and woe, And proud success, and happy lives With our dear children and our wives, Again permitted by his grace To look with joy on Ráma's face, And noble LakshmaG, and our lord The king, to our sweet homes restored?” Thus to the gathered lords he spoke; But no reply the silence broke. Then with a sterner voice he cried: “O chiefs, the nation's boast and pride, Whom valour strength and power adorn, Of most illustrious lineage born, Where'er you will you force a way, And none your rapid course can stay. Now come, your several powers declare.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1401)
- **Original**: Canto LXV. The Council. 1383 And who this desperate leap will dare?” Canto LXV. The Council. But none of all the host was found To clear the sea with desperate bound, Though each, as Angad bade, declared His proper power and what he dared.779 Then spake good Jámbaván the sage, Chief of them all for reverend age; “I, Vánar chieftains, long ago Limbs light to leap could likewise show, But now on frame and spirit weighs The burthen of my length of days. Still task like this I may not slight, When Ráma and our king unite. So listen while I tell, O friends, What lingering strength mine age attends. If my poor leap may aught avail, Of ninety leagues, I will not fail. Far other strength in youth's fresh prime I boasted, in the olden time, When, at Prahláda's780 solemn rite, I circled in my rapid flight Lord VishGu, everlasting God, When through the universe he trod. 779 Each chief comes forward and says how far he can leap. Gaja says he can leap ten yojans. Gavaksha can leap twenty. Gavaya thirty, and so on up to ninety. 780 Prahláda, the son of HiraGyaka[ipu, was a pious Datya remarkable for his devotion to VishGu, and was on this account persecuted by his father.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1402)
- **Original**: 1384 The Ramayana But now my limbs are weak and old, My youth is fled, its fire is cold, And these exhausted nerves to strain In such a task were idle pain.” Then Angad due obeisance paid, And to the chief his answer made: “Then I, ye noble Vánars, I Myself the mighty leap will try: Although perchance the power I lack To leap from Lanká's island back.” Thus the impetuous chieftain cried, And Jámbaván the sage replied: “Whate'er thy power and might may be, This task, O Prince, is not for thee. Kings go not forth themselves, but send The servants who their best attend. Thou art the darling and the boast, The honoured lord of all the host. In thee the root, O Angad, lies Of our appointed enterprise; And thee, on whom our hopes depend, Our care must cherish and defend.” Then Báli's noble son replied: “Needs must I go, whate'er betide, For, if no chief this exploit dare, What waits us all save blank despair,— Upon the ground again to lie In hopeless misery, fast, and die? For not a hope of life I see If we neglect our king's decree.” Then spoke the aged chief again: “Nay our attempt shall not be vain,
- **Translation**: 

---

### Verse 18 (Ramayana 0.1403)
- **Original**: Canto LXVI. Hanumán. 1385 For to the task will I incite A chieftain of sufficient might.” [392] Canto LXVI. Hanumán. The chieftain turned his glances where The legions sat in mute despair; And then to Hanumán, the best Of Vánar lords, these words addressed: “Why still, and silent, and apart, O hero of the dauntless heart? Thou keepest treasured in thy mind The laws that rule the Vánar kind, Strong as our king Sugríva, brave As Ráma's self to slay or save. Through every land thy praise is heard, Famous as that illustrious bird, Aríshmanemi's son,781 the king Of every fowl that plies the wing. Oft have I seen the monarch sweep With sounding pinions o'er the deep, And in his mighty talons bear Huge serpents struggling through the air. Thy arms, O hero, match in might The ample wings he spreads for flight; 781 The Bengal recension calls him Aríshmanemi's brother.“The commentator says‘Aríshmanemi is AruGa.’ AruGa the charioteer of the sun is the son of Ka [yapa and Vinatá and by consequence brother of Garu a, called Vainateya from Vinatá, his mother.” G ORRESSIO {FNS .
- **Translation**: 

---

### Verse 19 (Ramayana 0.1404)
- **Original**: 1386 The Ramayana And thou with him mayest well compare In power to do, in heart to dare. Why, rich in wisdom, power, and skill, O hero, art thou lingering still? An Apsaras782 the fairest found Of nymphs for heavenly charms renowned, Sweet Punjikasthalá, became A noble Vánar's wedded dame. Her heavenly title heard no more, Anjaná was the name she bore, When, cursed by Gods, from heaven she fell In Vánar form on earth to dwell, New-born in mortal shape the child Of Kunjar monarch of the wild. In youthful beauty wondrous fair, A crown of flowers about her hair, In silken robes of richest dye She roamed the hills that kiss the sky. Once in her tinted garments dressed She stood upon the mountain crest, The God of Wind beside her came, And breathed upon the lovely dame. And as he fanned her robe aside The wondrous beauty that he eyed In rounded lines of breast and limb And neck and shoulder ravished him; And captured by her peerless charms He strained her in his amorous arms. Then to the eager God she cried In trembling accents, terrified: “Whose impious love has wronged a spouse So constant in her nuptial vows?” 782 A nymph of Paradise.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1405)
- **Original**: Canto LXVI. Hanumán. 1387 He heard, and thus his answer made: “O, be not troubled, nor afraid, But trust, and thou shalt know ere long My love has done thee, sweet, no wrong, So strong and brave and wise shall be The glorious child I give to thee. Might shall be his that naught can tire, And limbs to spring as springs his sire.” Thus spoke the God; the conquered dame Rejoiced in heart nor feared the shame. Down in a cave beneath the earth The happy mother gave thee birth. Once o'er the summit of the wood Before thine eyes the new sun stood. Thou sprangest up in haste to seize What seemed the fruitage of the trees. Up leapt the child, a wondrous bound, Three hundred leagues above the ground, And, though the angered Day-God shot His fierce beams on him, feared him not. Then from the hand of Indra came A red bolt winged with wrath and flame. The child fell smitten on a rock, His cheek was shattered by the shock, Named Hanumán 783 thenceforth by all In memory of the fearful fall. The wandering Wind-God saw thee lie With bleeding cheek and drooping eye, And stirred to anger by thy woe Forbade each scented breeze to blow. The breath of all the worlds was stilled, And the sad Gods with terror filled 783 Hanu or Hanú means jaw. Hanumán or Hanúmán means properly one with a large jaw.
- **Translation**: 

---

