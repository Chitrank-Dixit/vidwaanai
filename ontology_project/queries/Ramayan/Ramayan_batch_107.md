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

### Verse 1 (Ramayana 0.166)
- **Original**: 148 The Ramayana Then, sure, for man the task were hard. When lords of earth have longed to know The virtue of that wondrous bow, The strongest sons of kings in vain Have tried the mighty cord to strain. This famous bow thou there shalt view, And wondrous rites shalt witness too. The high-souled king who lords it o'er The realm of Míthilá of yore Gained from the Gods this bow, the price Of his imperial sacrifice. Won by the rite the glorious prize Still in the royal palace lies, Laid up in oil of precious scent With aloe-wood and incense blent.” Then Ráma answering, Be it so, Made ready with the rest to go. The saint himself was now prepared, But ere beyond the grove he fared, He turned him and in words like these Addressed the sylvan deities: “Farewell! each holy rite complete, I leave the hermits' perfect seat: To Gangá's northern shore I go Beneath Himálaya's peaks of snow.” With reverent steps he paced around The limits of the holy ground, And then the mighty saint set forth And took his journey to the north. His pupils, deep in Scripture's page, Followed behind the holy sage, And servants from the sacred grove A hundred wains for convoy drove.
- **Translation**: 

---

### Verse 2 (Ramayana 0.167)
- **Original**: Canto XXXIV. Brahmadatta. 149 The very birds that winged that air, The very deer that harboured there, Forsook the glade and leafy brake And followed for the hermit's sake. They travelled far, till in the west The sun was speeding to his rest, And made, their portioned journey o'er, Their halt onZona's171 distant shore. The hermits bathed when sank the sun, And every rite was duly done, Oblations paid to Fire, and then Sate round their chief the holy men. Ráma and LakshmaG lowly bowed In reverence to the hermit crowd, And Ráma, having sate him down Before the saint of pure renown, [046] With humble palms together laid His eager supplication made: “What country, O my lord, is this, Fair-smiling in her wealth and bliss? Deign fully, O thou mighty Seer, To tell me, for I long to hear.” Moved by the prayer of Ráma, he Told forth the country's history. Canto XXXIV. Brahmadatta. 171 A river which rises in Budelcund and falls into the Ganges near Patna. It is called alsoHiraGyaráhu, Golden-armed, andHiraGyaráha, Auriferous.
- **Translation**: 

---

### Verse 3 (Ramayana 0.168)
- **Original**: 150 The Ramayana “A king of Brahmá's seed who bore The name of Ku[a reigned of yore. Just, faithful to his vows, and true, He held the good in honour due. His bride, a queen of noble name, Of old Vidarbha's172 monarchs came. Like their own father, children four, All valiant boys, the lady bore. In glorious deeds each nerve they strained, And well their Warrior part sustained. To them most just, and true, and brave, Their father thus his counsel gave: “Beloved children, ne'er forget Protection is a prince's debt: The noble work at once begin, High virtue and her fruits to win.” The youths, to all the people dear, Received his speech with willing ear; And each went forth his several way, Foundations of a town to lay. Ku [ámba, prince of high renown, Was builder of Kau[ámbí's town, And Ku [anábha, just and wise, Bade high Mahodaya's towers arise. Amúrtarajas chose to dwell In DharmáraGya's citadel, And Vasu bade his city fair The name of Girivraja bear.173 172 The modern Berar. 173 According to the Bengal recension the first (Ku[ámba) is called Ku[á[va, and his city Kau[á[ví. This name does not occur elsewhere. The reading of the northern recension is confirmed by Foê Kouê Ki; p. 385, where the cityKiaoshangmi is mentioned. It lay 500listo the south-west ofPrayága, on the south bank of the Jumna.Mahodaya is another name of Kanyakubja: Dharmára Gya, the wood to which the God of Justice is said to have fled
- **Translation**: 

---

### Verse 4 (Ramayana 0.169)
- **Original**: Canto XXXIV. Brahmadatta. 151 This fertile spot whereon we stand Was once the high-souled Vasu's land. Behold! as round we turn our eyes, Five lofty mountain peaks arise. See! bursting from her parent hill, Sumágadhí, a lovely rill, Bright gleaming as she flows between The mountains, like a wreath is seen, And then through Magadh's plains and groves With many a fair mæander roves. And this was Vasu's old domain, The fertile Magadh's broad champaign, Which smiling fields of tilth adorn And diadem with golden corn. The queen Ghritáchí, nymph most fair, Married to Ku[anábha, bare A hundred daughters, lovely-faced, With every charm and beauty graced. It chanced the maidens, bright and gay As lightning-flashes on a day Of rain time, to the garden went With song and play and merriment, And there in gay attire they strayed, And danced, and laughed, and sang, and played. The God of Wind who roves at will All places, as he lists, to fill, Saw the young maidens dancing there, Of faultless shape and mien most fair. “I love you all, sweet girls,” he cried, “And each shall be my darling bride. Forsake, forsake your mortal lot, through fear of Soma the Moon-God was in Magadh. Girivraja was in the same neighbourhood. See Lasson's I, A. Vol. I. p. 604.
- **Translation**: 

---

### Verse 5 (Ramayana 0.170)
- **Original**: 152 The Ramayana And gain a life that withers not. A fickle thing is youth's brief span, And more than all in mortal man. Receive unending youth, and be Immortal, O my loves, with me.” The hundred girls, to wonder stirred, The wooing of the Wind-God heard, Laughed, as a jest, his suit aside, And with one voice they thus replied: “O mighty Wind, free spirit who All life pervadest, through and through, Thy wondrous power we maidens know; Then wherefore wilt thou mock us so? Our sire is Ku[anábha, King; And we, forsooth, have charms to bring A God to woo us from the skies; But honour first we maidens prize. Far may the hour, we pray, be hence, When we, O thou of little sense, Our truthful father's choice refuse, And for ourselves our husbands choose. Our honoured sire our lord we deem, He is to us a God supreme, And they to whom his high decree May give us shall our husbands be.” He heard the answer they returned, And mighty rage within him burned. On each fair maid a blast he sent: Each stately form he bowed and bent. Bent double by the Wind-God's ire They sought the palace of their sire,[047]
- **Translation**: 

---

### Verse 6 (Ramayana 0.171)
- **Original**: Canto XXXIV. Brahmadatta. 153 There fell upon the ground with sighs, While tears and shame were in their eyes. The king himself, with troubled brow, Saw his dear girls so fair but now, A mournful sight all bent and bowed, And grieving thus he cried aloud: “What fate is this, and what the cause? What wretch has scorned all heavenly laws? Who thus your forms could curve and break? You struggle, but no answer make.” They heard the speech of that wise king Of their misfortune questioning. Again the hundred maidens sighed, Touched with their heads his feet, and cried: “The God of Wind, pervading space, Would bring on us a foul disgrace, And choosing folly's evil way From virtue's path in scorn would stray. But we in words like these reproved The God of Wind whom passion moved: “Farewell, O Lord! A sire have we, No women uncontrolled and free. Go, and our sire's consent obtain If thou our maiden hands wouldst gain. No self-dependent life we live: If we offend, our fault forgive.” But led by folly as a slave, He would not hear the rede we gave, And even as we gently spoke We felt the Wind-God's crushing stroke.”
- **Translation**: 

---

### Verse 7 (Ramayana 0.172)
- **Original**: 154 The Ramayana The pious king, with grief distressed, The noble hundred thus addressed: “With patience, daughters, bear your fate, Yours was a deed supremely great When with one mind you kept from shame The honour of your father's name. Patience, when men their anger vent, Is woman's praise and ornament; Yet when the Gods inflict the blow Hard is it to support the woe. Patience, my girls, exceeds all price: 'Tis alms, and truth, and sacrifice. Patience is virtue, patience fame: Patience upholds this earthly frame. And now, I think, is come the time To wed you in your maiden prime. Now, daughters, go where'er you will: Thoughts for your good my mind shall fill.” The maidens went, consoled, away: The best of kings, that very day, Summoned his ministers of state About their marriage to debate. Since then, because the Wind-God bent The damsels' forms for punishment, That royal town is known to fame By Kanyákubja's174 borrowed name. 174 That is, the City of the Bent Virgins, the modern Kanauj or Canouge.
- **Translation**: 

---

### Verse 8 (Ramayana 0.173)
- **Original**: Canto XXXIV. Brahmadatta. 155 There lived a sage called Chúli then, Devoutest of the sons of men; His days in penance rites he spent, A glorious saint, most continent. To him absorbed in tasks austere The child of Urmilá drew near, Sweet Somadá, the heavenly maid And lent the saint her pious aid. Long time near him the maiden spent, And served him meek and reverent, Till the great hermit, pleased with her, Thus spoke unto his minister: “Grateful am I for all thy care: Blest maiden, speak, thy wish declare.” The sweet-voiced nymph rejoiced to see The favour of the devotee, And to that eloquent old man, Most eloquent she thus began: “Thou hast, by heavenly grace sustained, Close union with the Godhead gained. I long, O Saint, to see a son By force of holy penance won. Unwed, a maiden life I live: A son to me, thy suppliant, give.” The saint with favour heard her prayer, And gave a son exceeding fair. Him, Chúli's spiritual child, His mother Brahmadatta175 styled. King Brahmadatta, rich and great, In Kámpilí maintained his state, Ruling, like Indra in his bliss, His fortunate metropolis. 175 Literally, Given byBrahma or devout contemplation.
- **Translation**: 

---

### Verse 9 (Ramayana 0.174)
- **Original**: 156 The Ramayana King Ku[anábha planned that he His hundred daughters' lord should be. To him, obedient to his call, The happy monarch gave them all. Like Indra then he took the hand Of every maiden of the band. Soon as the hand of each young maid In Brahmadatta's palm was laid, Deformity and cares away, She shone in beauty bright and gay. Their freedom from the Wind-God's might Saw Ku [anábha with delight. Each glance that on their forms he threw Filled him with raptures ever new. Then when the rites were all complete, With highest marks of honour meet The bridegroom with his brides he sent To his great seat of government. The nymph received with pleasant speech Her daughters; and, embracing each, Upon their forms she fondly gazed, And royal Ku[anábha praised. [048] Canto XXXV. Visvámitra's Lineage.
- **Translation**: 

---

### Verse 10 (Ramayana 0.175)
- **Original**: Canto XXXV. Visvámitra's Lineage. 157 “The rites were o'er, the maids were wed, The bridegroom to his home was sped. The sonless monarch bade prepare A sacrifice to gain an heir. Then Ku[a, Brahmá's son, appeared, And thus King Ku[anábha cheered: “Thou shalt, my child, obtain a son Like thine own self, O holy one. Through him for ever, Gádhi named, Shalt thou in all the worlds be famed.” He spoke, and vanished from the sight To Brahmá's world of endless light. Time fled, and, as the saint foretold, Gádhi was born, the holy-souled. My sire was he; through him I trace My line from royal Ku[a's race. My sister— elder-born was she— The pure and good Satyavatí,176 Was to the great Richíka wed. Still faithful to her husband dead, She followed him, most noble dame, And, raised to heaven in human frame, A pure celestial stream became. Down from Himálaya's snowy height, In floods for ever fair and bright, My sister's holy waves are hurled To purify and glad the world. Now on Himálaya's side I dwell Because I love my sister well. 176 Now called Ko[í (Cosy) corrupted from Kau[ikí, daughter of Ku[]a. “This is one of those personifications of rivers so frequent in the Grecian mythology, but in the similar myths is seen the impress of the genius of each people, austere and profoundly religious in India, graceful and devoted to the worship of external beauty in Greece.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 11 (Ramayana 0.176)
- **Original**: 158 The Ramayana She, for her faith and truth renowned, Most loving to her husband found, High-fated, firm in each pure vow, Is queen of all the rivers now. Bound by a vow I left her side And to the Perfect convent hied. There, by the aid 'twas thine to lend, Made perfect, all my labours end. Thus, mighty Prince, I now have told My race and lineage, high and old, And local tales of long ago Which thou, O Ráma, fain wouldst know. As I have sate rehearsing thus The midnight hour is come on us. Now, Ráma, sleep, that nothing may Our journey of to-morrow stay. No leaf on any tree is stirred: Hushed in repose are beast and bird: Where'er you turn, on every side, Dense shades of night the landscape hide, The light of eve is fled: the skies, Thick-studded with their host of eyes, Seem a star-forest overhead, Where signs and constellations spread. Now rises, with his pure cold ray, The moon that drives the shades away, And with his gentle influence brings Joy to the hearts of living things. Now, stealing from their lairs, appear The beasts to whom the night is dear. Now spirits walk, and every power That revels in the midnight hour.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.177)
- **Original**: Canto XXXVI. The Birth Of Gangá. 159 The mighty hermit's tale was o'er, He closed his lips and spoke no more. The holy men on every side, “Well done! well done,” with reverence cried; “The mighty men of Ku[a's seed Were ever famed for righteous deed. Like Brahmá's self in glory shine The high-souled lords of Ku[a's line, And thy great name is sounded most, O Saint, amid the noble host. And thy dear sister— fairest she Of streams, the high-born Kau[ikí— Diffusing virtue where she flows, New splendour on thy lineage throws.” Thus by the chief of saints addressed The son of Gádhi turned to rest; So, when his daily course is done, Sinks to his rest the beaming sun. Ráma with LakshmaG, somewhat stirred To marvel by the tales they heard, Turned also to his couch, to close His eyelids in desired repose. Canto XXXVI. The Birth Of Gangá. The hours of night now waning fast On Zona's pleasant shore they passed. Then, when the dawn began to break, To Ráma thus the hermit spake: “The light of dawn is breaking clear, The hour of morning rites is near.
- **Translation**: 

---

### Verse 13 (Ramayana 0.178)
- **Original**: 160 The Ramayana Rise, Ráma, rise, dear son, I pray, And make thee ready for the way.” Then Ráma rose, and finished all His duties at the hermit's call, Prepared with joy the road to take, And thus again in question spake: “Here fair and deep theZona flows, And many an isle its bosom shows: What way, O Saint, will lead us o'er And land us on the farther shore?” The saint replied:“The way I choose Is that which pious hermits use.”[049] For many a league they journeyed on Till, when the sun of mid-day shone, The hermit-haunted flood was seen Of Jáhnaví,177 the Rivers' Queen. Soon as the holy stream they viewed, Thronged with a white-winged multitude Of sárases178 and swans,179 delight Possessed them at the lovely sight; And then prepared the hermit band To halt upon that holy strand. They bathed as Scripture bids, and paid Oblations due to God and shade. To Fire they burnt the offerings meet, And sipped the oil, like Amrit sweet. Then pure and pleased they sate around Saint Vi[vámitra on the ground. The holy men of lesser note, 177 One of the names of the Ganges considered as the daughter of Jahnu. See Canto XLIV. 178 The Indian Crane. 179 Or, rather, geese.
- **Translation**: 

---

### Verse 14 (Ramayana 0.179)
- **Original**: Canto XXXVI. The Birth Of Gangá. 161 In due degree, sate more remote, While Raghu's sons took nearer place By virtue of their rank and race. Then Ráma said:“O Saint, I yearn The three-pathed Gangá's tale to learn.” Thus urged, the sage recounted both The birth of Gangá and her growth: “The mighty hill with metals stored, Himálaya, is the mountains' lord, The father of a lovely pair Of daughters fairest of the fair: Their mother, offspring of the will Of Meru, everlasting hill, Mená, Himálaya's darling, graced With beauty of her dainty waist. Gangá was elder-born: then came The fair one known by Umá's name. Then all the Gods of heaven, in need Of Gangá's help their vows to speed, To great Himálaya came and prayed The mountain King to yield the maid. He, not regardless of the weal Of the three worlds, with holy zeal His daughter to the Immortals gave, Gangá whose waters cleanse and save, Who roams at pleasure, fair and free, Purging all sinners, to the sea. The three-pathed Gangá thus obtained, The Gods their heavenly homes regained. Long time the sister Umá passed In vows austere and rigid fast, And the king gave the devotee
- **Translation**: 

---

### Verse 15 (Ramayana 0.180)
- **Original**: 162 The Ramayana Immortal Rudra's180 bride to be, Matching with that unequalled Lord His Umá through the worlds adored. So now a glorious station fills Each daughter of the King of Hills: One honoured as the noblest stream, One mid the Goddesses supreme. Thus Gangá, King Himálaya's child, The heavenly river, undefiled, Rose bearing with her to the sky Her waves that bless and purify.” [I am compelled to omit Cantos XXXVII and XXXVIII, THE G LORY OF U MÁ , andTHE B IRTH OF K ÁRTIKEYA , as both in subject and language offensive to modern taste. They will be found in Schlegel's Latin translation.] Canto XXXIX. The Sons Of Sagar. The saint in accents sweet and clear Thus told his tale for Ráma's ear, And thus anew the holy man A legend to the prince began: “There reigned a pious monarch o'er Ayodhyá in the days of yore: Sagar his name: no child had he, And children much he longed to see. His honoured consort, fair of face, Sprang from Vidarbha's royal race, Ke [ini, famed from early youth 180 A name of the GodZiva.
- **Translation**: 

---

### Verse 16 (Ramayana 0.181)
- **Original**: Canto XXXIX. The Sons Of Sagar. 163 For piety and love of truth. Aríshmanemi's daughter fair, With whom no maiden might compare In beauty, though the earth is wide, Sumati, was his second bride. With his two queens afar he went, And weary days in penance spent, Fervent, upon Himálaya's hill Where springs the stream called Bhrigu' rill. Nor did he fail that saint to please With his devout austerities. And, when a hundred years had fled, Thus the most truthful Bhrigu said: “From thee, O Sagar, blameless King, A mighty host of sons shall spring, And thou shalt win a glorious name Which none, O Chief, but thou shall claim. One of thy queens a son shall bear, Maintainer of thy race and heir; And of the other there shall be Sons sixty thousand born to thee.” Thus as he spake, with one accord, To win the grace of that high lord, The queens, with palms together laid, In humble supplication prayed: “Which queen, O Bráhman, of the pair, The many, or the one shall bear? Most eager, Lord, are we to know, And as thou sayest be it so.” [050] With his sweet speech the saint replied: “Yourselves, O Queens, the choice decide. Your own discretion freely use Which shall the one or many choose:
- **Translation**: 

---

### Verse 17 (Ramayana 0.182)
- **Original**: 164 The Ramayana One shall the race and name uphold, The host be famous, strong, and bold. Which will have which?” Then Ke[ini The mother of one heir would be. Sumati, sister of the king181 Of all the birds that ply the wing, To that illustrious Bráhman sued That she might bear the multitude Whose fame throughout the world should sound For mighty enterprise renowned. Around the saint the monarch went, Bowing his head, most reverent. Then with his wives, with willing feet, Resought his own imperial seat. Time passed. The elder consort bare A son called Asamanj, the heir. Then Sumati, the younger, gave Birth to a gourd,182 O hero brave, Whose rind, when burst and cleft in two, Gave sixty thousand babes to view. All these with care the nurses laid In jars of oil; and there they stayed, Till, youthful age and strength complete, Forth speeding from each dark retreat, All peers in valour, years, and might, The sixty thousand came to light. Prince Asamanj, brought up with care, Scourge of his foes, was made the heir. But liegemen's boys he used to cast To Sarjú's waves that hurried past, Laughing the while in cruel glee 181 Garu a. 182 Ikshváku, the name of a king of Ayodhyá who is regarded as the founder of the Solar race, means also agourd. Hence, perhaps, the myth.
- **Translation**: 

---

### Verse 18 (Ramayana 0.183)
- **Original**: Canto XL. The Cleaving Of The Earth. 165 Their dying agonies to see. This wicked prince who aye withstood The counsel of the wise and good, Who plagued the people in his hate, His father banished from the state. His son, kind-spoken, brave, and tall, Was An [umán, beloved of all. Long years flew by. The king decreed To slay a sacrificial steed. Consulting with his priestly band He vowed the rite his soul had planned, And, Veda skilled, by their advice Made ready for the sacrifice. Canto XL. The Cleaving Of The Earth. The hermit ceased: the tale was done: Then in a transport Raghu's son Again addressed the ancient sire Resplendent as a burning fire: “O holy man, I fain would hear The tale repeated full and clear How he from whom my sires descend Brought the great rite to happy end.” The hermit answered with a smile: “Then listen, son of Raghu, while My legendary tale proceeds To tell of high-souled Sagar's deeds. Within the spacious plain that lies From where Himálaya's heights arise
- **Translation**: 

---

### Verse 19 (Ramayana 0.184)
- **Original**: 166 The Ramayana To where proud Vindhya's rival chain Looks down upon the subject plain— A land the best for rites declared183. — His sacrifice the king prepared. And An [umán the prince— for so Sagar advised— with ready bow Was borne upon a mighty car To watch the steed who roamed afar. But Indra, monarch of the skies, Veiling his form in demon guise, Came down upon the appointed day And drove the victim horse away. Reft of the steed the priests, distressed, The master of the rite addressed: “Upon the sacred day by force A robber takes the victim horse. Haste, King! now let the thief be slain; Bring thou the charger back again: The sacred rite prevented thus Brings scathe and woe to all of us. Rise, monarch, and provide with speed That naught its happy course impede.” 183 “The region here spoken of is called in the Laws of ManuMadhyade [a or the middle region.‘The region situated between the Himálaya and the Vindhya Mountains… is calledMadhyade [a, or the middle region; the space comprised between these two mountains from the eastern to the western sea is called by sages Áryávartta,the seat of honourable men.’(M ANU {FNS , II, 21, 22.) The Sanskrit Indians called themselves Áryans, which meanshonourable,noble, to distinguish themselves from the surrounding nations of different origin.” G ORRESIO {FNS
- **Translation**: 

---

### Verse 20 (Ramayana 0.185)
- **Original**: Canto XL. The Cleaving Of The Earth. 167 King Sagar in his crowded court Gave ear unto the priests' report. He summoned straightway to his side His sixty thousand sons, and cried: “Brave sons of mine, I knew not how These demons are so mighty now: The priests began the rite so well All sanctified with prayer and spell. If in the depths of earth he hide, Or lurk beneath the ocean's tide, [051] Pursue, dear sons, the robber's track; Slay him and bring the charger back. The whole of this broad earth explore, Sea-garlanded, from shore to shore: Yea, dig her up with might and main Until you see the horse again. Deep let your searching labour reach, A league in depth dug out by each. The robber of our horse pursue, And please your sire who orders you. My grandson, I, this priestly train, Till the steed comes, will here remain.” Their eager hearts with transport burned As to their task the heroes turned. Obedient to their father, they Through earth's recesses forced their way. With iron arms' unflinching toil Each dug a league beneath the soil. Earth, cleft asunder, groaned in pain, As emulous they plied amain Sharp-pointed coulter, pick, and bar, Hard as the bolts of Indra are. Then loud the horrid clamour rose
- **Translation**: 

---

