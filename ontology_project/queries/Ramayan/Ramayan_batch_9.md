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

### Verse 1 (Ramayan 0.161)
- **Original**: Canto XXXI. The Perfect Hermitage. 143 He spoke; and soon the anchorite, With joyous looks that beamed delight, With Ráma and his brother stood Within the consecrated wood. Soon as they saw the holy man, With one accord together ran The dwellers in the sacred shade, And to the saint their reverence paid, And offered water for his feet, The gift of honour and a seat; And next with hospitable care They entertained the princely pair. The royal tamers of their foes Rested awhile in sweet repose: Then to the chief of hermits sued Standing in suppliant attitude: “Begin, O best of saints, we pray, Initiatory rites to-day. This Perfect Grove shall be anew Made perfect, and thy words be true.” Then, thus addressed, the holy man, The very glorious sage, began The high preliminary rite. Restraining sense and appetite. Calmly the youths that night reposed, And rose when morn her light disclosed, Their morning worship paid, and took Of lustral water from the brook. Thus purified they breathed the prayer, Then greeted Vi[vámitra where As celebrant he sate beside The flame with sacred oil supplied.
- **Translation**: 

---

### Verse 2 (Ramayan 0.162)
- **Original**: 144 The Ramayana Canto XXXII. Visvámitra's Sacrifice. That conquering pair, of royal race, Skilled to observe due time and place, To Ku[ik's hermit son addressed, In timely words, their meet request: “When must we, lord, we pray thee tell, Those Rovers of the Night repel? Speak, lest we let the moment fly, And pass the due occasion by.” Thus longing for the strife, they prayed, And thus the hermits answer made: “Till the fifth day be come and past, O Raghu's sons, your watch must last. The saint his Dikshá170 has begun, And all that time will speak to none.” Soon as the steadfast devotees Had made reply in words like these, The youths began, disdaining sleep, Six days and nights their watch to keep. The warrior pair who tamed the foe, Unrivalled benders of the bow, Kept watch and ward unwearied still To guard the saint from scathe and ill. 'Twas now the sixth returning day, The hour foretold had past away. Then Ráma cried:“O Lakshma G, now Firm, watchful, resolute be thou. The fiends as yet have kept afar From the pure grove in which we are: Yet waits us, ere the day shall close, Dire battle with the demon foes.” 170 Certain ceremonies preliminary to a sacrifice.
- **Translation**: 

---

### Verse 3 (Ramayan 0.163)
- **Original**: Canto XXXII. Visvámitra's Sacrifice. 145 While thus spoke Ráma borne away By longing for the deadly fray, See! bursting from the altar came The sudden glory of the flame. Round priest and deacon, and upon Grass, ladles, flowers, the splendour shone, And the high rite, in order due, With sacred texts began anew. But then a loud and fearful roar Re-echoed through the sky; And like vast clouds that shadow o'er The heavens in dark July, Involved in gloom of magic might Two fiends rushed on amain, Márícha, Rover of the Night, Suváhu, and their train. As on they came in wild career Thick blood in rain they shed; And Ráma saw those things of fear Impending overhead. Then soon as those accursed two Who showered down blood be spied, Thus to his brother brave and true Spoke Ráma lotus-eyed: “Now, LakshmaG, thou these fiends shalt see, Man-eaters, foul of mind, Before my mortal weapon flee Like clouds before the wind.” He spoke. An arrow, swift as thought, Upon his bow he pressed, And smote, to utmost fury wrought, Márícha on the breast. Deep in his flesh the weapon lay Winged by the mystic spell, [045]
- **Translation**: 

---

### Verse 4 (Ramayan 0.164)
- **Original**: 146 The Ramayana And, hurled a hundred leagues away, In ocean's flood he fell. Then Ráma, when he saw the foe Convulsed and mad with pain Neath the chill-pointed weapon's blow, To LakshmaG spoke again: “See, LakshmaG, see! this mortal dart That strikes a numbing chill, Hath struck him senseless with the smart, But left him breathing still. But these who love the evil way, And drink the blood they spill, Rejoicing holy rites to stay, Fierce plagues, my hand shall kill.” He seized another shaft, the best, Aglow with living flame; It struck Suváhu on the chest, And dead to earth he came. Again a dart, the Wind-God's own, Upon his string he laid, And all the demons were o'erthrown, The saints no more afraid. When thus the fiends were slain in fight, Disturbers of each holy rite, Due honour by the saints was paid To Ráma for his wondrous aid: So Indra is adored when he Has won some glorious victory. Success at last the rite had crowned, And Vi[vámitra gazed around, And seeing every side at rest, The son of Raghu thus addressed: “My joy, O Prince, is now complete: Thou hast obeyed my will:
- **Translation**: 

---

### Verse 5 (Ramayan 0.165)
- **Original**: Canto XXXIII. The Sone. 147 Perfect before, this calm retreat Is now more perfect still.” Canto XXXIII. The Sone. Their task achieved, the princes spent That night with joy and full content. Ere yet the dawn was well displayed Their morning rites they duly paid, And sought, while yet the light was faint, The hermits and the mighty saint. They greeted first that holy sire Resplendent like the burning fire, And then with noble words began Their sweet speech to the sainted man: “Here stand, O Lord, thy servants true: Command what thou wouldst have us do.” The saints, by Vi[vámitra led, To Ráma thus in answer said: “Janak the king who rules the land Of fertile Míthilá has planned A noble sacrifice, and we Will thither go the rite to see. Thou, Prince of men, with us shalt go, And there behold the wondrous bow, Terrific, vast, of matchless might, Which, splendid at the famous rite, The Gods assembled gave the king. No giant, fiend, or God can string That gem of bows, no heavenly bard:
- **Translation**: 

---

### Verse 6 (Ramayan 0.166)
- **Original**: 148 The Ramayana Then, sure, for man the task were hard. When lords of earth have longed to know The virtue of that wondrous bow, The strongest sons of kings in vain Have tried the mighty cord to strain. This famous bow thou there shalt view, And wondrous rites shalt witness too. The high-souled king who lords it o'er The realm of Míthilá of yore Gained from the Gods this bow, the price Of his imperial sacrifice. Won by the rite the glorious prize Still in the royal palace lies, Laid up in oil of precious scent With aloe-wood and incense blent.” Then Ráma answering, Be it so, Made ready with the rest to go. The saint himself was now prepared, But ere beyond the grove he fared, He turned him and in words like these Addressed the sylvan deities: “Farewell! each holy rite complete, I leave the hermits' perfect seat: To Gangá's northern shore I go Beneath Himálaya's peaks of snow.” With reverent steps he paced around The limits of the holy ground, And then the mighty saint set forth And took his journey to the north. His pupils, deep in Scripture's page, Followed behind the holy sage, And servants from the sacred grove A hundred wains for convoy drove.
- **Translation**: 

---

### Verse 7 (Ramayan 0.167)
- **Original**: Canto XXXIV. Brahmadatta. 149 The very birds that winged that air, The very deer that harboured there, Forsook the glade and leafy brake And followed for the hermit's sake. They travelled far, till in the west The sun was speeding to his rest, And made, their portioned journey o'er, Their halt onZona's171 distant shore. The hermits bathed when sank the sun, And every rite was duly done, Oblations paid to Fire, and then Sate round their chief the holy men. Ráma and LakshmaG lowly bowed In reverence to the hermit crowd, And Ráma, having sate him down Before the saint of pure renown, [046] With humble palms together laid His eager supplication made: “What country, O my lord, is this, Fair-smiling in her wealth and bliss? Deign fully, O thou mighty Seer, To tell me, for I long to hear.” Moved by the prayer of Ráma, he Told forth the country's history. Canto XXXIV. Brahmadatta. 171 A river which rises in Budelcund and falls into the Ganges near Patna. It is called alsoHiraGyaráhu, Golden-armed, andHiraGyaráha, Auriferous.
- **Translation**: 

---

### Verse 8 (Ramayan 0.168)
- **Original**: 150 The Ramayana “A king of Brahmá's seed who bore The name of Ku[a reigned of yore. Just, faithful to his vows, and true, He held the good in honour due. His bride, a queen of noble name, Of old Vidarbha's172 monarchs came. Like their own father, children four, All valiant boys, the lady bore. In glorious deeds each nerve they strained, And well their Warrior part sustained. To them most just, and true, and brave, Their father thus his counsel gave: “Beloved children, ne'er forget Protection is a prince's debt: The noble work at once begin, High virtue and her fruits to win.” The youths, to all the people dear, Received his speech with willing ear; And each went forth his several way, Foundations of a town to lay. Ku [ámba, prince of high renown, Was builder of Kau[ámbí's town, And Ku [anábha, just and wise, Bade high Mahodaya's towers arise. Amúrtarajas chose to dwell In DharmáraGya's citadel, And Vasu bade his city fair The name of Girivraja bear.173 172 The modern Berar. 173 According to the Bengal recension the first (Ku[ámba) is called Ku[á[va, and his city Kau[á[ví. This name does not occur elsewhere. The reading of the northern recension is confirmed by Foê Kouê Ki; p. 385, where the cityKiaoshangmi is mentioned. It lay 500listo the south-west ofPrayága, on the south bank of the Jumna.Mahodaya is another name of Kanyakubja: Dharmára Gya, the wood to which the God of Justice is said to have fled
- **Translation**: 

---

### Verse 9 (Ramayan 0.169)
- **Original**: Canto XXXIV. Brahmadatta. 151 This fertile spot whereon we stand Was once the high-souled Vasu's land. Behold! as round we turn our eyes, Five lofty mountain peaks arise. See! bursting from her parent hill, Sumágadhí, a lovely rill, Bright gleaming as she flows between The mountains, like a wreath is seen, And then through Magadh's plains and groves With many a fair mæander roves. And this was Vasu's old domain, The fertile Magadh's broad champaign, Which smiling fields of tilth adorn And diadem with golden corn. The queen Ghritáchí, nymph most fair, Married to Ku[anábha, bare A hundred daughters, lovely-faced, With every charm and beauty graced. It chanced the maidens, bright and gay As lightning-flashes on a day Of rain time, to the garden went With song and play and merriment, And there in gay attire they strayed, And danced, and laughed, and sang, and played. The God of Wind who roves at will All places, as he lists, to fill, Saw the young maidens dancing there, Of faultless shape and mien most fair. “I love you all, sweet girls,” he cried, “And each shall be my darling bride. Forsake, forsake your mortal lot, through fear of Soma the Moon-God was in Magadh. Girivraja was in the same neighbourhood. See Lasson's I, A. Vol. I. p. 604.
- **Translation**: 

---

### Verse 10 (Ramayan 0.170)
- **Original**: 152 The Ramayana And gain a life that withers not. A fickle thing is youth's brief span, And more than all in mortal man. Receive unending youth, and be Immortal, O my loves, with me.” The hundred girls, to wonder stirred, The wooing of the Wind-God heard, Laughed, as a jest, his suit aside, And with one voice they thus replied: “O mighty Wind, free spirit who All life pervadest, through and through, Thy wondrous power we maidens know; Then wherefore wilt thou mock us so? Our sire is Ku[anábha, King; And we, forsooth, have charms to bring A God to woo us from the skies; But honour first we maidens prize. Far may the hour, we pray, be hence, When we, O thou of little sense, Our truthful father's choice refuse, And for ourselves our husbands choose. Our honoured sire our lord we deem, He is to us a God supreme, And they to whom his high decree May give us shall our husbands be.” He heard the answer they returned, And mighty rage within him burned. On each fair maid a blast he sent: Each stately form he bowed and bent. Bent double by the Wind-God's ire They sought the palace of their sire,[047]
- **Translation**: 

---

### Verse 11 (Ramayan 0.171)
- **Original**: Canto XXXIV. Brahmadatta. 153 There fell upon the ground with sighs, While tears and shame were in their eyes. The king himself, with troubled brow, Saw his dear girls so fair but now, A mournful sight all bent and bowed, And grieving thus he cried aloud: “What fate is this, and what the cause? What wretch has scorned all heavenly laws? Who thus your forms could curve and break? You struggle, but no answer make.” They heard the speech of that wise king Of their misfortune questioning. Again the hundred maidens sighed, Touched with their heads his feet, and cried: “The God of Wind, pervading space, Would bring on us a foul disgrace, And choosing folly's evil way From virtue's path in scorn would stray. But we in words like these reproved The God of Wind whom passion moved: “Farewell, O Lord! A sire have we, No women uncontrolled and free. Go, and our sire's consent obtain If thou our maiden hands wouldst gain. No self-dependent life we live: If we offend, our fault forgive.” But led by folly as a slave, He would not hear the rede we gave, And even as we gently spoke We felt the Wind-God's crushing stroke.”
- **Translation**: 

---

### Verse 12 (Ramayan 0.172)
- **Original**: 154 The Ramayana The pious king, with grief distressed, The noble hundred thus addressed: “With patience, daughters, bear your fate, Yours was a deed supremely great When with one mind you kept from shame The honour of your father's name. Patience, when men their anger vent, Is woman's praise and ornament; Yet when the Gods inflict the blow Hard is it to support the woe. Patience, my girls, exceeds all price: 'Tis alms, and truth, and sacrifice. Patience is virtue, patience fame: Patience upholds this earthly frame. And now, I think, is come the time To wed you in your maiden prime. Now, daughters, go where'er you will: Thoughts for your good my mind shall fill.” The maidens went, consoled, away: The best of kings, that very day, Summoned his ministers of state About their marriage to debate. Since then, because the Wind-God bent The damsels' forms for punishment, That royal town is known to fame By Kanyákubja's174 borrowed name. 174 That is, the City of the Bent Virgins, the modern Kanauj or Canouge.
- **Translation**: 

---

### Verse 13 (Ramayan 0.173)
- **Original**: Canto XXXIV. Brahmadatta. 155 There lived a sage called Chúli then, Devoutest of the sons of men; His days in penance rites he spent, A glorious saint, most continent. To him absorbed in tasks austere The child of Urmilá drew near, Sweet Somadá, the heavenly maid And lent the saint her pious aid. Long time near him the maiden spent, And served him meek and reverent, Till the great hermit, pleased with her, Thus spoke unto his minister: “Grateful am I for all thy care: Blest maiden, speak, thy wish declare.” The sweet-voiced nymph rejoiced to see The favour of the devotee, And to that eloquent old man, Most eloquent she thus began: “Thou hast, by heavenly grace sustained, Close union with the Godhead gained. I long, O Saint, to see a son By force of holy penance won. Unwed, a maiden life I live: A son to me, thy suppliant, give.” The saint with favour heard her prayer, And gave a son exceeding fair. Him, Chúli's spiritual child, His mother Brahmadatta175 styled. King Brahmadatta, rich and great, In Kámpilí maintained his state, Ruling, like Indra in his bliss, His fortunate metropolis. 175 Literally, Given byBrahma or devout contemplation.
- **Translation**: 

---

### Verse 14 (Ramayan 0.174)
- **Original**: 156 The Ramayana King Ku[anábha planned that he His hundred daughters' lord should be. To him, obedient to his call, The happy monarch gave them all. Like Indra then he took the hand Of every maiden of the band. Soon as the hand of each young maid In Brahmadatta's palm was laid, Deformity and cares away, She shone in beauty bright and gay. Their freedom from the Wind-God's might Saw Ku [anábha with delight. Each glance that on their forms he threw Filled him with raptures ever new. Then when the rites were all complete, With highest marks of honour meet The bridegroom with his brides he sent To his great seat of government. The nymph received with pleasant speech Her daughters; and, embracing each, Upon their forms she fondly gazed, And royal Ku[anábha praised. [048] Canto XXXV. Visvámitra's Lineage.
- **Translation**: 

---

### Verse 15 (Ramayan 0.175)
- **Original**: Canto XXXV. Visvámitra's Lineage. 157 “The rites were o'er, the maids were wed, The bridegroom to his home was sped. The sonless monarch bade prepare A sacrifice to gain an heir. Then Ku[a, Brahmá's son, appeared, And thus King Ku[anábha cheered: “Thou shalt, my child, obtain a son Like thine own self, O holy one. Through him for ever, Gádhi named, Shalt thou in all the worlds be famed.” He spoke, and vanished from the sight To Brahmá's world of endless light. Time fled, and, as the saint foretold, Gádhi was born, the holy-souled. My sire was he; through him I trace My line from royal Ku[a's race. My sister— elder-born was she— The pure and good Satyavatí,176 Was to the great Richíka wed. Still faithful to her husband dead, She followed him, most noble dame, And, raised to heaven in human frame, A pure celestial stream became. Down from Himálaya's snowy height, In floods for ever fair and bright, My sister's holy waves are hurled To purify and glad the world. Now on Himálaya's side I dwell Because I love my sister well. 176 Now called Ko[í (Cosy) corrupted from Kau[ikí, daughter of Ku[]a. “This is one of those personifications of rivers so frequent in the Grecian mythology, but in the similar myths is seen the impress of the genius of each people, austere and profoundly religious in India, graceful and devoted to the worship of external beauty in Greece.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 16 (Ramayan 0.176)
- **Original**: 158 The Ramayana She, for her faith and truth renowned, Most loving to her husband found, High-fated, firm in each pure vow, Is queen of all the rivers now. Bound by a vow I left her side And to the Perfect convent hied. There, by the aid 'twas thine to lend, Made perfect, all my labours end. Thus, mighty Prince, I now have told My race and lineage, high and old, And local tales of long ago Which thou, O Ráma, fain wouldst know. As I have sate rehearsing thus The midnight hour is come on us. Now, Ráma, sleep, that nothing may Our journey of to-morrow stay. No leaf on any tree is stirred: Hushed in repose are beast and bird: Where'er you turn, on every side, Dense shades of night the landscape hide, The light of eve is fled: the skies, Thick-studded with their host of eyes, Seem a star-forest overhead, Where signs and constellations spread. Now rises, with his pure cold ray, The moon that drives the shades away, And with his gentle influence brings Joy to the hearts of living things. Now, stealing from their lairs, appear The beasts to whom the night is dear. Now spirits walk, and every power That revels in the midnight hour.”
- **Translation**: 

---

### Verse 17 (Ramayan 0.177)
- **Original**: Canto XXXVI. The Birth Of Gangá. 159 The mighty hermit's tale was o'er, He closed his lips and spoke no more. The holy men on every side, “Well done! well done,” with reverence cried; “The mighty men of Ku[a's seed Were ever famed for righteous deed. Like Brahmá's self in glory shine The high-souled lords of Ku[a's line, And thy great name is sounded most, O Saint, amid the noble host. And thy dear sister— fairest she Of streams, the high-born Kau[ikí— Diffusing virtue where she flows, New splendour on thy lineage throws.” Thus by the chief of saints addressed The son of Gádhi turned to rest; So, when his daily course is done, Sinks to his rest the beaming sun. Ráma with LakshmaG, somewhat stirred To marvel by the tales they heard, Turned also to his couch, to close His eyelids in desired repose. Canto XXXVI. The Birth Of Gangá. The hours of night now waning fast On Zona's pleasant shore they passed. Then, when the dawn began to break, To Ráma thus the hermit spake: “The light of dawn is breaking clear, The hour of morning rites is near.
- **Translation**: 

---

### Verse 18 (Ramayan 0.178)
- **Original**: 160 The Ramayana Rise, Ráma, rise, dear son, I pray, And make thee ready for the way.” Then Ráma rose, and finished all His duties at the hermit's call, Prepared with joy the road to take, And thus again in question spake: “Here fair and deep theZona flows, And many an isle its bosom shows: What way, O Saint, will lead us o'er And land us on the farther shore?” The saint replied:“The way I choose Is that which pious hermits use.”[049] For many a league they journeyed on Till, when the sun of mid-day shone, The hermit-haunted flood was seen Of Jáhnaví,177 the Rivers' Queen. Soon as the holy stream they viewed, Thronged with a white-winged multitude Of sárases178 and swans,179 delight Possessed them at the lovely sight; And then prepared the hermit band To halt upon that holy strand. They bathed as Scripture bids, and paid Oblations due to God and shade. To Fire they burnt the offerings meet, And sipped the oil, like Amrit sweet. Then pure and pleased they sate around Saint Vi[vámitra on the ground. The holy men of lesser note, 177 One of the names of the Ganges considered as the daughter of Jahnu. See Canto XLIV. 178 The Indian Crane. 179 Or, rather, geese.
- **Translation**: 

---

### Verse 19 (Ramayan 0.179)
- **Original**: Canto XXXVI. The Birth Of Gangá. 161 In due degree, sate more remote, While Raghu's sons took nearer place By virtue of their rank and race. Then Ráma said:“O Saint, I yearn The three-pathed Gangá's tale to learn.” Thus urged, the sage recounted both The birth of Gangá and her growth: “The mighty hill with metals stored, Himálaya, is the mountains' lord, The father of a lovely pair Of daughters fairest of the fair: Their mother, offspring of the will Of Meru, everlasting hill, Mená, Himálaya's darling, graced With beauty of her dainty waist. Gangá was elder-born: then came The fair one known by Umá's name. Then all the Gods of heaven, in need Of Gangá's help their vows to speed, To great Himálaya came and prayed The mountain King to yield the maid. He, not regardless of the weal Of the three worlds, with holy zeal His daughter to the Immortals gave, Gangá whose waters cleanse and save, Who roams at pleasure, fair and free, Purging all sinners, to the sea. The three-pathed Gangá thus obtained, The Gods their heavenly homes regained. Long time the sister Umá passed In vows austere and rigid fast, And the king gave the devotee
- **Translation**: 

---

### Verse 20 (Ramayan 0.180)
- **Original**: 162 The Ramayana Immortal Rudra's180 bride to be, Matching with that unequalled Lord His Umá through the worlds adored. So now a glorious station fills Each daughter of the King of Hills: One honoured as the noblest stream, One mid the Goddesses supreme. Thus Gangá, King Himálaya's child, The heavenly river, undefiled, Rose bearing with her to the sky Her waves that bless and purify.” [I am compelled to omit Cantos XXXVII and XXXVIII, THE G LORY OF U MÁ , andTHE B IRTH OF K ÁRTIKEYA , as both in subject and language offensive to modern taste. They will be found in Schlegel's Latin translation.] Canto XXXIX. The Sons Of Sagar. The saint in accents sweet and clear Thus told his tale for Ráma's ear, And thus anew the holy man A legend to the prince began: “There reigned a pious monarch o'er Ayodhyá in the days of yore: Sagar his name: no child had he, And children much he longed to see. His honoured consort, fair of face, Sprang from Vidarbha's royal race, Ke [ini, famed from early youth 180 A name of the GodZiva.
- **Translation**: 

---

