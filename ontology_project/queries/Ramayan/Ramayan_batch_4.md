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

### Verse 1 (Ramayan 0.61)
- **Original**: Canto VII. The Ministers. 43 Governed his fair ancestral state, With every virtue crowned. Like Indra in the skies he reigned In that good town whose wall contained High domes and turrets proud, With gates and arcs of triumph decked, And sturdy barriers to protect Her gay and countless crowd. Canto VII. The Ministers. Two sages, holy saints, had he, His ministers and priests to be: Va [ishmha, faithful to advise, And Vámadeva, Scripture-wise. Eight other lords around him stood, All skilled to counsel, wise and good: Jayanta, Vijay, Dhrishmi bold In fight, affairs of war controlled: Siddhárth and Arthasádhak true Watched o'er expense and revenue, And Dharmapál and wise A[ok Of right and law and justice spoke. With these the sage Sumantra, skilled To urge the car, high station filled. All these in knowledge duly trained Each passion and each sense restrained: With modest manners, nobly bred Each plan and nod and look they read, Upon their neighbours' good intent, Most active and benevolent:
- **Translation**: 

---

### Verse 2 (Ramayan 0.62)
- **Original**: 44 The Ramayana As sit the Vasus79 round their king, They sate around him counselling. They ne'er in virtue's loftier pride Another's lowly gifts decried. In fair and seemly garb arrayed, No weak uncertain plans they made. Well skilled in business, fair and just, They gained the people's love and trust, And thus without oppression stored The swelling treasury of their lord. Bound in sweet friendship each to each, They spoke kind thoughts in gentle speech. They looked alike with equal eye On every caste, on low and high. Devoted to their king, they sought, Ere his tongue spoke, to learn his thought, And knew, as each occasion rose, To hide their counsel or disclose. In foreign lands or in their own Whatever passed, to them was known. By secret spies they timely knew What men were doing or would do. Skilled in the grounds of war and peace They saw the monarch's state increase, Watching his weal with conquering eye That never let occasion by, While nature lent her aid to bless Their labours with unbought success. Never for anger, lust, or gain, Would they their lips with falsehood stain. Inclined to mercy they could scan The weakness and the strength of man. 79 Attendants of Indra, eight Gods whose names signify fire, light and its phenomena.
- **Translation**: 

---

### Verse 3 (Ramayan 0.63)
- **Original**: Canto VIII. Sumantra's Speech. 45 They fairly judged both high and low, And ne'er would wrong a guiltless foe; Yet if a fault were proved, each one Would punish e'en his own dear son. But there and in the kingdom's bound No thief or man impure was found: None of loose life or evil fame, No tempter of another's dame. Contented with their lot each caste [015] Calm days in blissful quiet passed; And, all in fitting tasks employed, Country and town deep rest enjoyed, With these wise lords around his throne The monarch justly reigned, And making every heart his own The love of all men gained. With trusty agents, as beseems, Each distant realm he scanned, As the sun visits with his beams Each corner of the land. Ne'er would he on a mightier foe With hostile troops advance, Nor at an equal strike a blow In war's delusive chance. These lords in council bore their part With ready brain and faithful heart, With skill and knowledge, sense and tact, Good to advise and bold to act. And high and endless fame he won With these to guide his schemes, As, risen in his might, the sun Wins glory with his beams.
- **Translation**: 

---

### Verse 4 (Ramayan 0.64)
- **Original**: 46 The Ramayana Canto VIII. Sumantra's Speech. But splendid, just, and great of mind, The childless king for offspring pined. No son had he his name to grace, Transmitter of his royal race. Long had his anxious bosom wrought, And as he pondered rose the thought: “A votive steed 'twere good to slay, So might a son the gift repay.” Before his lords his plan he laid, And bade them with their wisdom aid: Then with these words Sumantra, best Of royal counsellors, addressed: “Hither, Va[ishmha at their head, Let all my priestly guides be led.” To him Sumantra made reply: “Hear, Sire, a tale of days gone by. To many a sage in time of old, Sanatkumár, the saint, foretold How from thine ancient line, O King, A son, when years came round, should spring. “Here dwells,” 'twas thus the seer began, “Of Ka[yap's80 race, a holy man, VibháGdak named: to him shall spring A son, the famous Rishya[ring. Bred with the deer that round him roam, The wood shall be that hermit's home. To him no mortal shall be known Except his holy sire alone. Still by those laws shall he abide 80 Ka [yap was a grandson of the God Brahmá. He is supposed to have given his name to Kashmír = Ka[yapa-míra, Ka[yap's Lake.
- **Translation**: 

---

### Verse 5 (Ramayan 0.65)
- **Original**: Canto VIII. Sumantra's Speech. 47 Which lives of youthful Bráhmans guide, Obedient to the strictest rule That forms the young ascetic's school: And all the wondering world shall hear Of his stern life and penance drear; His care to nurse the holy fire And do the bidding of his sire. Then, seated on the Angas'81 throne, Shall Lomapád to fame be known. But folly wrought by that great king A plague upon the land shall bring; No rain for many a year shall fall And grievous drought shall ruin all. The troubled king with many a prayer Shall bid the priests some cure declare: “The lore of Heaven 'tis yours to know, Nor are ye blind to things below: Declare, O holy men, the way This plague to expiate and stay.” Those best of Bráhmans shall reply: “By every art, O Monarch, try Hither to bring VibháGdak's child, Persuaded, captured, or beguiled. And when the boy is hither led To him thy daughter duly wed.” 81 The people of Anga.“Anga is said in the lexicons to be Bengal; but here certainly another region is intended situated at the confluence of the Sarjú with the Ganges, and not far distant from Da[aratha's dominions.” G ORRESIO {FNS . It comprised part of Behar and Bhagulpur.
- **Translation**: 

---

### Verse 6 (Ramayan 0.66)
- **Original**: 48 The Ramayana But how to bring that wondrous boy His troubled thoughts will long employ, And hopeless to achieve the task He counsel of his lords will ask, And bid his priests and servants bring With honour saintly Rishya[ring. But when they hear the monarch's speech, All these their master will beseech, With trembling hearts and looks of woe, To spare them, for they fear to go. And many a plan will they declare And crafty plots will frame, And promise fair to show him there, Unforced, with none to blame. On every word his lords shall say, The king will meditate, And on the third returning day Recall them to debate. Then this shall be the plan agreed, That damsels shall be sent Attired in holy hermits' weed, And skilled in blandishment, That they the hermit may beguile With every art and amorous wile[016] Whose use they know so well, And by their witcheries seduce The unsuspecting young recluse To leave his father's cell. Then when the boy with willing feet Shall wander from his calm retreat And in that city stand, The troubles of the king shall end, And streams of blessed rain descend Upon the thirsty land.
- **Translation**: 

---

### Verse 7 (Ramayan 0.67)
- **Original**: Canto IX. Rishyasring. 49 Thus shall the holy Rishya[ring To Lomapád, the mighty king, By wedlock be allied; For Zántá, fairest of the fair, In mind and grace beyond compare, Shall be his royal bride. He, at the Offering of the Steed, The flames with holy oil shall feed, And for King Da[aratha gain Sons whom his prayers have begged in vain.” “I have repeated, Sire, thus far, The words of old Sanatkumár, In order as he spoke them then Amid the crowd of holy men.” Then Da[aratha cried with joy, “Say how they brought the hermit boy.” Canto IX. Rishyasring. The wise Sumantra, thus addressed, Unfolded at the king's behest The plan the lords in council laid To draw the hermit from the shade: “The priest, amid the lordly crowd, To Lomapád thus spoke aloud: “Hear, King, the plot our thoughts have framed, A harmless trick by all unblamed. Far from the world that hermit's child Lives lonely in the distant wild: A stranger to the joys of sense, His bliss is pain and abstinence;
- **Translation**: 

---

### Verse 8 (Ramayan 0.68)
- **Original**: 50 The Ramayana And all unknown are women yet To him, a holy anchoret. The gentle passions we will wake That with resistless influence shake The hearts of men; and he Drawn by enchantment strong and sweet Shall follow from his lone retreat, And come and visit thee. Let ships be formed with utmost care That artificial trees may bear, And sweet fruit deftly made; Let goodly raiment, rich and rare, And flowers, and many a bird be there Beneath the leafy shade. Upon the ships thus decked a band Of young and lovely girls shall stand, Rich in each charm that wakes desire, And eyes that burn with amorous fire; Well skilled to sing, and play, and dance And ply their trade with smile and glance Let these, attired in hermits' dress, Betake them to the wilderness, And bring the boy of life austere A voluntary captive here.” He ended; and the king agreed, By the priest's counsel won. And all the ministers took heed To see his bidding done. In ships with wondrous art prepared Away the lovely women fared, And soon beneath the shade they stood Of the wild, lonely, dreary wood. And there the leafy cot they found Where dwelt the devotee,
- **Translation**: 

---

### Verse 9 (Ramayan 0.69)
- **Original**: Canto IX. Rishyasring. 51 And looked with eager eyes around The hermit's son to see. Still, of VibháGdak sore afraid, They hid behind the creepers' shade. But when by careful watch they knew The elder saint was far from view, With bolder steps they ventured nigh To catch the youthful hermit's eye. Then all the damsels, blithe and gay, At various games began to play. They tossed the flying ball about With dance and song and merry shout, And moved, their scented tresses bound With wreaths, in mazy motion round. Some girls as if by love possessed, Sank to the earth in feigned unrest, Up starting quickly to pursue Their intermitted game anew. It was a lovely sight to see Those fair ones, as they played, While fragrant robes were floating free, And bracelets clashing in their glee A pleasant tinkling made. The anklet's chime, the Koïl's82 cry With music filled the place As 'twere some city in the sky Which heavenly minstrels grace. With each voluptuous art they strove To win the tenant of the grove, And with their graceful forms inspire 82 The Koïl orkokila(Cuculus Indicus) as the harbinger of spring and love is a universal favourite with Indian poets. His voice when first heard in a glorious spring morning is not unpleasant, but becomes in the hot season intolerably wearisome to European ears.
- **Translation**: 

---

### Verse 10 (Ramayan 0.70)
- **Original**: 52 The Ramayana His modest soul with soft desire. With arch of brow, with beck and smile, With every passion-waking wile[017] Of glance and lotus hand, With all enticements that excite The longing for unknown delight Which boys in vain withstand. Forth came the hermit's son to view The wondrous sight to him so new, And gazed in rapt surprise, For from his natal hour till then On woman or the sons of men He ne'er had cast his eyes. He saw them with their waists so slim, With fairest shape and faultless limb, In variegated robes arrayed, And sweetly singing as they played. Near and more near the hermit drew, And watched them at their game, And stronger still the impulse grew To question whence they came. They marked the young ascetic gaze With curious eye and wild amaze, And sweet the long-eyed damsels sang, And shrill their merry laughter rang. Then came they nearer to his side, And languishing with passion cried: “Whose son, O youth, and who art thou, Come suddenly to join us now? And why dost thou all lonely dwell In the wild wood? We pray thee, tell, We wish to know thee, gentle youth; Come, tell us, if thou wilt, the truth.” He gazed upon that sight he ne'er
- **Translation**: 

---

### Verse 11 (Ramayan 0.71)
- **Original**: Canto IX. Rishyasring. 53 Had seen before, of girls so fair, And out of love a longing rose His sire and lineage to disclose: “My father,” thus he made reply, “Is Ka[yap's son, a saint most high, VibháGdak styled; from him I came, And Rishya[ring he calls my name. Our hermit cot is near this place: Come thither, O ye fair of face; There be it mine, with honour due, Ye gentle youths, to welcome you.” They heard his speech, and gave consent, And gladly to his cottage went. VibháGdak's son received them well Beneath the shelter of his cell With guest-gift, water for their feet, And woodland fruit and roots to eat, They smiled, and spoke sweet words like these, Delighted with his courtesies: “We too have goodly fruit in store, Grown on the trees that shade our door; Come, if thou wilt, kind Hermit, haste The produce of our grove to taste; And let, O good Ascetic, first This holy water quench thy thirst.” They spoke, and gave him comfits sweet Prepared ripe fruits to counterfeit; And many a dainty cate beside And luscious mead their stores supplied. The seeming fruits, in taste and look, The unsuspecting hermit took, For, strange to him, their form beguiled The dweller in the lonely wild. Then round his neck fair arms were flung,
- **Translation**: 

---

### Verse 12 (Ramayan 0.72)
- **Original**: 54 The Ramayana And there the laughing damsels clung, And pressing nearer and more near With sweet lips whispered at his ear; While rounded limb and swelling breast The youthful hermit softly pressed. The pleasing charm of that strange bowl, The touch of a tender limb, Over his yielding spirit stole And sweetly vanquished him. But vows, they said, must now be paid; They bade the boy farewell, And, of the aged saint afraid, Prepared to leave the dell. With ready guile they told him where Their hermit dwelling lay: Then, lest the sire should find them there, Sped by wild paths away. They fled and left him there alone By longing love possessed; And with a heart no more his own He roamed about distressed. The aged saint came home, to find The hermit boy distraught, Revolving in his troubled mind One solitary thought. “Why dost thou not, my son,” he cried, “Thy due obeisance pay? Why do I see thee in the tide Of whelming thought to-day? A devotee should never wear A mien so sad and strange. Come, quickly, dearest child, declare The reason of the change.” And Rishya[ring, when questioned thus,
- **Translation**: 

---

### Verse 13 (Ramayan 0.73)
- **Original**: Canto IX. Rishyasring. 55 Made answer in this wise: “O sire, there came to visit us Some men with lovely eyes. About my neck soft arms they wound And kept me tightly held To tender breasts so soft and round, That strangely heaved and swelled. They sing more sweetly as they dance Than e'er I heard till now, And play with many a sidelong glance And arching of the brow.” “My son,” said he,“thus giants roam Where holy hermits are, And wander round their peaceful home Their rites austere to mar. I charge thee, thou must never lay Thy trust in them, dear boy: They seek thee only to betray, And woo but to destroy.” Thus having warned him of his foes That night at home he spent. And when the morrow's sun arose [018] Forth to the forest went. But Rishya[ring with eager pace Sped forth and hurried to the place Where he those visitants had seen Of daintly waist and charming mien. When from afar they saw the son Of Saint VibháGdak toward them run, To meet the hermit boy they hied, And hailed him with a smile, and cried: “O come, we pray, dear lord, behold Our lovely home of which we told Due honour there to thee we'll pay,
- **Translation**: 

---

### Verse 14 (Ramayan 0.74)
- **Original**: 56 The Ramayana And speed thee on thy homeward way.” Pleased with the gracious words they said He followed where the damsels led. As with his guides his steps he bent, That Bráhman high of worth, A flood of rain from heaven was sent That gladdened all the earth. VibháGdak took his homeward road, And wearied by the heavy load Of roots and woodland fruit he bore Entered at last his cottage door. Fain for his son he looked around, But desolate the cell he found. He stayed not then to bathe his feet, Though fainting with the toil and heat, But hurried forth and roamed about Calling the boy with cry and shout, He searched the wood, but all in vain; Nor tidings of his son could gain. One day beyond the forest's bound The wandering saint a village found, And asked the swains and neatherds there Who owned the land so rich and fair, With all the hamlets of the plain, And herds of kine and fields of grain. They listened to the hermit's words, And all the guardians of the herds, With suppliant hands together pressed, This answer to the saint addressed: “The Angas' lord who bears the name Of Lomapád, renowned by fame, Bestowed these hamlets with their kine
- **Translation**: 

---

### Verse 15 (Ramayan 0.75)
- **Original**: Canto IX. Rishyasring. 57 And all their riches, as a sign Of grace, on Rishya[ring: and he VibháGdak's son is said to be.” The hermit with exulting breast The mighty will of fate confessed, By meditation's eye discerned; And cheerful to his home returned. A stately ship, at early morn, The hermit's son away had borne. Loud roared the clouds, as on he sped, The sky grew blacker overhead; Till, as he reached the royal town, A mighty flood of rain came down. By the great rain the monarch's mind The coming of his guest divined. To meet the honoured youth he went, And low to earth his head he bent. With his own priest to lead the train, He gave the gift high guests obtain. And sought, with all who dwelt within The city walls, his grace to win. He fed him with the daintiest fare, He served him with unceasing care, And ministered with anxious eyes Lest anger in his breast should rise; And gave to be the Bráhman's bride His own fair daughter, lotus-eyed. Thus loved and honoured by the king, The glorious Bráhman Rishya[ring Passed in that royal town his life With Zántá his beloved wife.”
- **Translation**: 

---

### Verse 16 (Ramayan 0.76)
- **Original**: 58 The Ramayana Canto X. Rishyasring Invited. “Again, O best of kings, give ear: My saving words attentive hear, And listen to the tale of old By that illustrious Bráhman told. “Of famed Ikshváku's line shall spring ('Twas thus he spoke) a pious king, Named Da [aratha, good and great, True to his word and fortunate. He with the Angas' mighty lord Shall ever live in sweet accord, And his a daughter fair shall be, Zántá of happy destiny. But Lomapád, the Angas' chief, Still pining in his childless grief, To Da[aratha thus shall say: “Give me thy daughter, friend, I pray, Thy Zántá of the tranquil mind, The noblest one of womankind.” The father, swift to feel for woe, Shall on his friend his child bestow; And he shall take her and depart To his own town with joyous heart. The maiden home in triumph led, To Rishya[ring the king shall wed. And he with loving joy and pride Shall take her for his honoured bride. And Da [aratha to a rite That best of Bráhmans shall invite With supplicating prayer, To celebrate the sacrifice
- **Translation**: 

---

### Verse 17 (Ramayan 0.77)
- **Original**: Canto X. Rishyasring Invited. 59 To win him sons and Paradise,83 That he will fain prepare. [019] From him the lord of men at length The boon he seeks shall gain, And see four sons of boundless strength His royal line maintain.” “Thus did the godlike saint of old The will of fate declare, And all that should befall unfold Amid the sages there. O Prince supreme of men, go thou, Consult thy holy guide, And win, to aid thee in thy vow, This Bráhman to thy side.” Sumantra's counsel, wise and good, King Da[aratha heard, Then by Va[ishmha's side he stood And thus with him conferred: “Sumantra counsels thus: do thou My priestly guide, the plan allow.” Va [ishmha gave his glad consent, And forth the happy monarch went With lords and servants on the road That led to Rishya[ring's abode. Forests and rivers duly past, He reached the distant town at last Of Lomapád the Angas' king, And entered it with welcoming. On through the crowded streets he came, And, radiant as the kindled flame, 83 “Sons and Paradise are intimately connected in Indian belief. A man desires above every thing to have a son to perpetuate his race, and to assist with sacrifices and funeral rites to make him worthy to obtain a lofty seat in heaven or to preserve that which he has already obtained.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 18 (Ramayan 0.78)
- **Original**: 60 The Ramayana He saw within the monarch's house The hermit's son most glorious. There Lomapád, with joyful breast, To him all honour paid, For friendship for his royal guest His faithful bosom swayed. Thus entertained with utmost care Seven days, or eight, he tarried there, And then that best of men thus broke His purpose to the king, and spoke: “O King of men, mine ancient friend, (Thus Da[aratha prayed) Thy Zántá with her husband send My sacrifice to aid.” Said he who ruled the Angas, Yea, And his consent was won: And then at once he turned away To warn the hermit's son. He told him of their ties beyond Their old affection's faithful bond: “This king,” he said,“from days of old A well beloved friend I hold. To me this pearl of dames he gave From childless woe mine age to save, The daughter whom he loved so much, Moved by compassion's gentle touch. In him thyZántás father see: As I am even so is he. For sons the childless monarch yearns: To thee alone for help he turns. Go thou, the sacred rite ordain To win the sons he prays to gain: Go, with thy wife thy succour lend, And give his vows a blissful end.”
- **Translation**: 

---

### Verse 19 (Ramayan 0.79)
- **Original**: Canto X. Rishyasring Invited. 61 The hermit's son with quick accord Obeyed the Angas' mighty lord, And with fairZántá at his side To Da[aratha's city hied. Each king, with suppliant hands upheld, Gazed on the other's face: And then by mutual love impelled Met in a close embrace. Then Da[aratha's thoughtful care, Before he parted thence, Bade trusty servants homeward bear The glad intelligence: “Let all the town be bright and gay With burning incense sweet; Let banners wave, and water lay The dust in every street.” Glad were the citizens to learn The tidings of their lord's return, And through the city every man Obediently his task began. And fair and bright Ayodhyá showed, As following his guest he rode Through the full streets where shell and drum Proclaimed aloud the king was come. And all the people with delight Kept gazing on their king, Attended by that youth so bright, The glorious Rishya[ring. When to his home the king had brought The hermit's saintly son, He deemed that all his task was wrought, And all he prayed for won. And lords who saw that stranger dame So beautiful to view,
- **Translation**: 

---

### Verse 20 (Ramayan 0.80)
- **Original**: 62 The Ramayana Rejoiced within their hearts, and came And paid her honour too. There Rishya[ring passed blissful days, Graced like the king with love and praise And shone in glorious light with her, Sweet Zántá, for his minister, As Brahmá's son Va[ishmha, he Who wedded Saint Arundhatí.84 Canto XI. The Sacrifice Decreed. The Dewy Season85 came and went; The spring returned again: Then would the king, with mind intent, His sacrifice ordain.[020] He came to Rishya[ring, and bowed To him of look divine, And bade him aid his offering vowed For heirs, to save his line. Nor would the youth his aid deny: He spake the monarch fair, And prayed him for that rite so high All requisites prepare. The king to wise Sumantra cried Who stood aye ready near; “Go summon quick each holy guide, To counsel and to hear.” 84 One of the Pleiades and generally regarded as the model of wifely excel- lence. 85 The Hindu year is divided into six seasons of two months each, spring, summer, rains, autumn, winter, and dews.
- **Translation**: 

---

