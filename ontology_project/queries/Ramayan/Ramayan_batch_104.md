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

### Verse 1 (Ramayana 0.106)
- **Original**: 88 The Ramayana Canto XVI. The Vánars. When VishGu thus had gone on earth, From the great king to take his birth, The self-existent Lord of all Addressed the Gods who heard his call: “For VishGu's sake, the strong and true, Who seeks the good of all of you, Make helps, in war to lend him aid, In forms that change at will, arrayed, Of wizard skill and hero might, Outstrippers of the wind in flight, Skilled in the arts of counsel, wise, And VishGu's peers in bold emprise; With heavenly arts and prudence fraught, By no devices to be caught; Skilled in all weapon's lore and use As they who drink the immortal juice.111[028] And let the nymphs supreme in grace, And maidens of the minstrel race, Monkeys and snakes, and those who rove Free spirits of the hill and grove, And wandering Daughters of the Air, In monkey form brave children bear. So erst the lord of bears I shaped, Born from my mouth as wide I gaped.” 111 The Amrit, the nectar of the Indian Gods.
- **Translation**: 

---

### Verse 2 (Ramayana 0.107)
- **Original**: Canto XVI. The Vánars. 89 Thus by the mighty Sire addressed They all obeyed his high behest, And thus begot in countless swarms Brave sons disguised in sylvan forms. Each God, each sage became a sire, Each minstrel of the heavenly quire,112 Each faun,113 of children strong and good Whose feet should roam the hill and wood. Snakes, bards,114 and spirits,115 serpents bold Had sons too numerous to be told. Báli, the woodland hosts who led, High as Mahendra's116 lofty head, Was Indra's child. That noblest fire, The Sun, was great Sugríva's sire, Tára, the mighty monkey, he Was offspring of V[ihaspati:117 Tára the matchless chieftain, boast For wisdom of the Vánar host. Of Gandhamádan brave and bold The father was the Lord of Gold. 112 Gandharvas (Southey's Glendoveers) are celestial musicians inhabiting In- dra's heaven and forming the orchestra at all the banquets of the principal deities. 113 Yakshas, demigods attendant especially on Kuvera, and employed by him in the care of his garden and treasures. 114 Kimpurushas, demigods attached also to the service of Kuvera, celestial musicians, represented like centaurs reversed with human figures and horses' heads. 115 Siddhas, demigods or spirits of undefined attributes, occupying with the Vidyádharasthe middle air or region between the earth and the sun. Schlegel translates:“Divi, Sapientes, Fidicines, Præpetes, illustres Genii, Præconesque procrearunt natos, masculos, silvicolas; angues porro, Hip- pocephali Beati, Aligeri, Serpentesque frequentes alacriter generavere prolem innumerabilem.” 116 A mountain in the south of India. 117 The preceptor of the Gods and regent of the planet Jupiter.
- **Translation**: 

---

### Verse 3 (Ramayana 0.108)
- **Original**: 90 The Ramayana Nala the mighty, dear to fame, Of skilful Vi[vakarmá118 came. From Agni,119 Nila bright as flame, Who in his splendour, might, and worth, Surpassed the sire who gave him birth. The heavenly A[vins,120 swift and fair, Were fathers of a noble pair, Who, Dwivida and Mainda named, For beauty like their sires were famed, VaruG121 was father of SusheG, Of Sarabh, he who sends the rain,122 Hanúmán, best of monkey kind, Was son of him who breathes the wind: Like thunderbolt in frame was he, And swift as Garu 's123 self could flee. These thousands did the Gods create Endowed with might that none could mate, In monkey forms that changed at will; So strong their wish the fiend to kill. In mountain size, like lions thewed, Up sprang the wondrous multitude, Auxiliar hosts in every shape, Monkey and bear and highland ape. In each the strength, the might, the mien Of his own parent God were seen. 118 The celestial architect, the Indian Hephæstus, Mulciber, or Vulcan. 119 The God of Fire. 120 Twin children of the Sun, the physicians of Swarga or Indra's heaven. 121 The deity of the waters. 122 Parjanya, sometimes confounded with Indra. 123 The bird and vehicle of VishGu. He is generally represented as a being something between a man and a bird and considered as the sovereign of the feathered race. He may be compared with the Simurgh of the Persians, the 'Anká of the Arabs, the Griffin of chivalry, the Phœ nix of Egypt, and the bird that sits upon the ash Yggdrasil of the Edda.
- **Translation**: 

---

### Verse 4 (Ramayana 0.109)
- **Original**: Canto XVI. The Vánars. 91 Some chiefs of Vánar mothers came, Some of she-bear and minstrel dame, Skilled in all arms in battle's shock; The brandished tree, the loosened rock; And prompt, should other weapons fail, To fight and slay with tooth and nail. Their strength could shake the hills amain, And rend the rooted trees in twain, Disturb with their impetuous sweep The Rivers' Lord, the Ocean deep, Rend with their feet the seated ground, And pass wide floods with airy bound, Or forcing through the sky their way The very clouds by force could stay. Mad elephants that wander through The forest wilds, could they subdue, And with their furious shout could scare Dead upon earth the birds of air. So were the sylvan chieftains formed; Thousands on thousands still they swarmed. These were the leaders honoured most, The captains of the Vánar host, And to each lord and chief and guide Was monkey offspring born beside. Then by the bears' great monarch stood The other roamers of the wood, [029] And turned, their pathless homes to seek, To forest and to mountain peak. The leaders of the monkey band By the two brothers took their stand, Sugríva, offspring of the Sun And Báli, Indra's mighty one. They both endowed with Garu 's might, And skilled in all the arts of fight,
- **Translation**: 

---

### Verse 5 (Ramayana 0.110)
- **Original**: 92 The Ramayana Wandered in arms the forest through, And lions, snakes, and tigers, slew. But every monkey, ape, and bear Ever was Báli's special care; With his vast strength and mighty arm He kept them from all scathe and harm. And so the earth with hill, wood, seas, Was filled with mighty ones like these, Of various shape and race and kind, With proper homes to each assigned, With Ráma's champions fierce and strong The earth was overspread, High as the hills and clouds, a throng With bodies vast and dread.124 Canto XVII. Rishyasring's Return. Now when the high-souled monarch's rite, The A[vamedh, was finished quite, Their sacrificial dues obtained, The Gods their heavenly homes regained. The lofty-minded saints withdrew, Each to his place, with honour due, And kings and chieftains, one and all, 124 This Canto will appear ridiculous to the European reader. But it should be remembered that the monkeys of an Indian forest, the“bough-deer” as the poets call them, are very different animals from the“turpissima bestia” that accompanies the itinerant organ-grinder or grins in the Zoological Gardens of London. Milton has made his hero, Satan, assume the forms of a cormorant, a toad, and a serpent, and I cannot see that this creation of semi-divine Vánars, or monkeys, is more ridiculous or undignified.
- **Translation**: 

---

### Verse 6 (Ramayana 0.111)
- **Original**: Canto XVII. Rishyasring's Return. 93 Who came to grace the festival. And Da [aratha, ere they went, Addressed them thus benevolent: “Now may you, each with joyful heart, To your own realms, O Kings, depart. Peace and good luck attend you there, And blessing, is my friendly prayer; Let cares of state each mind engage To guard his royal heritage. A monarch from his throne expelled No better than the dead is held. So he who cares for power and might Must guard his realm and royal right. Such care a meed in heaven will bring Better than rites and offering. Such care a king his country owes As man upon himself bestows, When for his body he provides Raiment and every need besides. For future days should kings foresee, And keep the present error-free.” Thus did the king the kings exhort: They heard, and turned them from the court And, each to each in friendship bound, Went forth to all the realms around. The rites were o'er, the guests were sped: The train the best of Bráhmans led, In which the king with joyful soul, With his dear wives, and with the whole Of his imperial host and train Of cars and servants turned again, And, as a monarch dear to fame, Within his royal city came.
- **Translation**: 

---

### Verse 7 (Ramayana 0.112)
- **Original**: 94 The Ramayana Next, Rishya[ring, well-honoured sage, And Zántá, sought their hermitage. The king himself, of prudent mind, Attended him, with troops behind. And all her men the town outpoured With Saint Va[ishmha and their lord. High mounted on a car of state, O'er canopied fairZántá sate. Drawn by white oxen, while a band Of servants marched on either hand. Great gifts of countless price she bore, With sheep and goats and gems in store. Like Beauty's self the lady shone With all the jewels she had on, As, happy in her sweet content, Peerless amid the fair she went. Not Queen Paulomí's125 self could be More loving to her lord than she. She who had lived in happy ease, Honoured with all her heart could please, While dames and kinsfolk ever vied To see her wishes gratified, Soon as she knew her husband's will Again to seek the forest, still Was ready for the hermit's cot, Nor murmured at her altered lot. The king attended to the wild That hermit and his own dear child, And in the centre of a throng Of noble courtiers rode along. The sage's son had let prepare A lodge within the wood, and there 125 The consort of Indra, called alsoZachí and IndráGí.
- **Translation**: 

---

### Verse 8 (Ramayana 0.113)
- **Original**: Canto XVII. Rishyasring's Return. 95 While they lingered blithe and gay. Then, duly honoured, went their way. The glorious hermit Rishya[ring Drew near and thus besought the king: [030] “Return, my honoured lord, I pray, Return, upon thy homeward way.” The monarch, with the waiting crowd, Lifted his voice and wept aloud, And with eyes dripping still to each Of his good queens he spake this speech: “Kau [alyá and Sumitrá dear, And thou, my sweet Kaikeyí, hear. All uponZántá feast your gaze, The last time for a length of days.” To Zántá's arms the ladies leapt, And hung about her neck and wept, And cried,“O, happy be the life Of this great Bráhman and his wife. The Wind, the Fire, the Moon on high, The Earth, the Streams, the circling Sky, Preserve thee in the wood, true spouse, Devoted to thy husband's vows. And O dearZántá, ne'er neglect To pay the dues of meek respect To the great saint, thy husband's sire, With all observance and with fire. And, sweet one, pure of spot and blame, Forget not thou thy husband's claim; In every change, in good and ill, Let thy sweet words delight him still, And let thy worship constant be: Her lord is woman's deity.
- **Translation**: 

---

### Verse 9 (Ramayana 0.114)
- **Original**: 96 The Ramayana To learn thy welfare, dearest friend, The king will many a Bráhman send. Let happy thoughts thy spirit cheer, And be not troubled, daughter dear.” These soothing words the ladies said. And pressed their lips upon her head. Each gave with sighs her last adieu, Then at the king's command withdrew. The king around the hermit went With circling footsteps reverent, And placed at Rishya[ring's command Some soldiers of his royal band. The Bráhman bowed in turn and cried, “May fortune never leave thy side. O mighty King, with justice reign, And still thy people's love retain.” He spoke, and turned away his face, And, as the hermit went, The monarch, rooted to the place, Pursued with eyes intent. But when the sage had past from view King Da[aratha turned him too, Still fixing on his friend each thought. With such deep love his breast was fraught. Amid his people's loud acclaim Home to his royal seat he came, And lived delighted there, Expecting when each queenly dame, Upholder of his ancient fame, Her promised son should bear. The glorious sage his way pursued Till close before his eyes he viewed Sweet Champá, Lomapád's fair town,
- **Translation**: 

---

### Verse 10 (Ramayana 0.115)
- **Original**: Canto XVIII. Rishyasring's Departure. 97 Wreathed with her Champacs'126 leafy crown. Soon as the saint's approach he knew, The king, to yield him honour due, Went forth to meet him with a band Of priests and nobles of the land: “Hail, Sage,” he cried,“O joy to me! What bliss it is, my lord, to see Thee with thy wife and all thy train Returning to my town again. Thy father, honoured Sage, is well, Who hither from his woodland cell Has sent full many a messenger For tidings both of thee and her.” Then joyfully, for due respect, The monarch bade the town be decked. The king and Rishya[ring elate Entered the royal city's gate: In front the chaplain rode. Then, loved and honoured with all care By monarch and by courtier, there The glorious saint abode. Canto XVIII. Rishyasring's Departure. 126 The Michelia champaca. It bears a scented yellow blossom: “The maid of India blest again to hold In her full lap the Champac's leaves of gold.” Lallah Rookh.
- **Translation**: 

---

### Verse 11 (Ramayana 0.116)
- **Original**: 98 The Ramayana The monarch called a Bráhman near And said,“Now speed away To Ka[yap's son,127 the mighty seer, And with all reverence say The holy child he holds so dear, The hermit of the noble mind, Whose equal it were hard to find, Returned, is dwelling here. Go, and instead of me do thou Before that best of hermits bow, That still he may, for his dear son, Show me the favour I have won.” Soon as the king these words had said, To Ka[yap's son the Bráhman sped. Before the hermit low he bent And did obeisance, reverent; Then with meek words his grace to crave The message of his lord he gave: “The high-souled father of his bride Had called thy son his rites to guide: Those rites are o'er, the steed is slain; Thy noble child is come again.” Soon as the saint that speech had heard His spirit with desire was stirred To seek the city of the king And to his cot his son to bring.[031] With young disciples at his side Forth on his way the hermit hied, While peasants from their hamlets ran To reverence the holy man. Each with his little gift of food, Forth came the village multitude, 127 VibháGdak, the father of Rishya[ring
- **Translation**: 

---

### Verse 12 (Ramayana 0.117)
- **Original**: Canto XVIII. Rishyasring's Departure. 99 And, as they humbly bowed the head, “What may we do for thee?” they said. Then he, of Bráhmans first and best, The gathered people thus addressed: “Now tell me for I fain would know, Why is it I am honoured so?” They to the high-souled saint replied: “Our ruler is with thee allied. Our master's order we fulfil; O Bráhman, let thy mind be still.” With joy the saintly hermit heard Each pleasant and delightful word, And poured a benediction down On king and ministers and town. Glad at the words of that high saint Some servants hastened to acquaint Their king, rejoicing to impart The tidings that would cheer his heart. Soon as the joyful tale he knew To meet the saint the monarch flew, The guest-gift in his hand he brought, And bowed before him and besought: “This day by seeing thee I gain Not to have lived my life in vain, Now be not wroth with me, I pray, “Because I wiled thy son away.128 128 A hemi[loka is wanting in Schlegel's text, which he thus fills up in his Latin translation.
- **Translation**: 

---

### Verse 13 (Ramayana 0.118)
- **Original**: 100 The Ramayana The best of Bráhmans answer made: “Be not, great lord of kings, afraid. Thy virtues have not failed to win My favour, O thou pure of sin.” Then in the front the saint was placed, The king came next in joyous haste, And with him entered his abode, Mid glad acclaim as on they rode. To greet the sage the reverent crowd Raised suppliant hands and humbly bowed. Then from the palace many a dame Following well-dressedZántá came, Stood by the mighty saint and cried: “See, honour's source, thy son's dear bride.” The saint, who every virtue knew, His arms around his daughter threw, And with a father's rapture pressed The lady to his wondering breast. Arising from the saint's embrace She bowed her low before his face, And then, with palm to palm applied, Stood by her hermit father's side. He for his son, as laws ordain, Performed the rite that frees from stain,129 And, honoured by the wise and good, With him departed to the wood. Canto XIX. The Birth Of The Princes. 129 Rishya[ring, a Bráhman, had marriedZántá who was of the Kshatriya or Warrior caste and an expiatory ceremony was necessary on account of this violation of the law.
- **Translation**: 

---

### Verse 14 (Ramayana 0.119)
- **Original**: Canto XIX. The Birth Of The Princes. 101 The seasons six in rapid flight Had circled since that glorious rite. Eleven months had passed away; 'Twas Chaitra's ninth returning day.130 The moon within that mansion shone Which Aditi looks kindly on. Raised to their apex in the sky Five brilliant planets beamed on high. Shone with the moon, in Cancer's sign, V [ihaspati131 with light divine. Kau [alyá bore an infant blest With heavenly marks of grace impressed; Ráma, the universe's lord, A prince by all the worlds adored. New glory Queen Kau[alyá won Reflected from her splendid son. So Aditi shone more and more, The Mother of the Gods, when she The King of the Immortals132 bore, The thunder-wielding deity. [032] 130 “The poet no doubt intended to indicate the vernal equinox as the birthday of Ráma. For the monthChaitrais the first of the two months assigned to the spring; it corresponds with the latter half of March and the former half of April in our division of the year.Aditi, the mother of the Gods, is lady of the seventh lunar mansion which is calledPunarvasu. The five planets and their positions in the Zodiac are thus enumerated by both commentators: the Sun in Aries, Mars in Capricorn, Saturn in Libra, Jupiter in Cancer, Venus in Pisces.… I leave to astronomers to examine whether the parts of the description agree with one another, and, if this be the case, thence to deduce the date. The Indians place the nativity of Ráma in the confines of the second age (tretá) and the third (dwápara): but it seems that this should be taken in an allegorical sense.… We may consider that the poet had an eye to the time in which, immediately before his own age, the aspects of the heavenly bodies were such as he has described.” SCHLEGEL {FNS . 131 The regent of the planet Jupiter. 132 Indra = Jupiter Tonans.
- **Translation**: 

---

### Verse 15 (Ramayana 0.120)
- **Original**: 102 The Ramayana The lotus-eyed, the beauteous boy, He came fierce RávaG to destroy; From half of VishGu's vigour born, He came to help the worlds forlorn. And Queen Kaikeyí bore a child Of truest valour, Bharat styled, With every princely virtue blest, One fourth of VishGu manifest. Sumitrá too a noble pair, Called LakshmaG and Zatrughna, bare, Of high emprise, devoted, true, Sharers in VishGu's essence too. 'Neath Pushya's133 mansion, Mina's134 sign, Was Bharat born, of soul benign. The sun had reached the Crab at morn When Queen Sumitrá's babes were born, What time the moon had gone to make His nightly dwelling with the Snake. The high-souled monarch's consorts bore At different times those glorious four, Like to himself and virtuous, bright As Proshmhapadá's135 four-fold light. Then danced the nymphs' celestial throng, The minstrels raised their strain; The drums of heaven pealed loud and long, And flowers came down in rain. Within Ayodhyá, blithe and gay, All kept the joyous holiday. 133 “Pushya is the name of a month; but here it means the eighth mansion. The ninth is calledAsleshá, or the snake. It is evident from this that Bharat, though his birth is mentioned before that of the twins, was the youngest of the four brothers and Ráma's junior by eleven months.” SCHLEGEL {FNS . 134 A fish, the Zodiacal signPisces. 135 One of the constellations, containing stars in the wing of Pegasus.
- **Translation**: 

---

### Verse 16 (Ramayana 0.121)
- **Original**: Canto XIX. The Birth Of The Princes. 103 The spacious square, the ample road With mimes and dancers overflowed, And with the voice of music rang Where minstrels played and singers sang, And shone, a wonder to behold, With dazzling show of gems and gold. Nor did the king his largess spare, For minstrel, driver, bard, to share; Much wealth the Bráhmans bore away, And many thousand dine that day. Soon as each babe was twelve days old 'Twas time the naming rite to hold. When Saint Va[ishmha, rapt with joy, Assigned a name to every boy. Ráma, to him the high-souled heir, Bharat, to him Kaikeyí bare: Of Queen Sumitrá one fair son Was Lakshma G, andZatrughna136 one Ráma, his sire's supreme delight, Like some proud banner cheered his sight, And to all creatures seemed to be The self-existent deity. All heroes, versed in holy lore, To all mankind great love they bore. Fair stores of wisdom all possessed, With princely graces all were blest. But mid those youths of high descent, With lordly light preëminent. Like the full moon unclouded, shone Ráma, the world's dear paragon. 136 Ráma means the Delight (of the World); Bharat, the Supporter; LakshmaG, the Auspicious;Zatrughna, the Slayer of Foes.
- **Translation**: 

---

### Verse 17 (Ramayana 0.122)
- **Original**: 104 The Ramayana He best the elephant could guide.137 Urge the fleet car, the charger ride: A master he of bowman's skill, Joying to do his father's will. The world's delight and darling, he Loved LakshmaG best from infancy And Lakshma G, lord of lofty fate, Upon his elder joyed to wait, Striving his second self to please With friendship's sweet observances. His limbs the hero ne'er would rest Unless the couch his brother pressed; Except beloved Ráma shared He could not taste the meal prepared. When Ráma, pride of Reghu's race, Sprang on his steed to urge the chase, Behind him LakshmaG loved to go And guard him with his trusty bow. As Ráma was to LakshmaG dear More than his life and ever near, So fondZatrughna prized above His very life his Bharat's love. Illustrious heroes, nobly kind In mutual love they all combined, And gave their royal sire delight With modest grace and warrior might: Supported by the glorious four Shone Da[aratha more and more, As though, with every guardian God 137 Schlegel, in theIndische Bibliothek, remarks that the proficiency of the Indians in this art early attracted the attention of Alexander's successors, and natives of India were so long exclusively employed in this service that the name Indian was applied to any elephant-driver, to whatever country he might belong.
- **Translation**: 

---

### Verse 18 (Ramayana 0.123)
- **Original**: Canto XX. Visvámitra's Visit. 105 Who keeps the land and skies, The Father of all creatures trod The earth before men's eyes. Canto XX. Visvámitra's Visit. Now Da [aratha's pious mind Meet wedlock for his sons designed; [033] With priests and friends the king began To counsel and prepare his plan. Such thoughts engaged his bosom, when, To see Ayodhyá's lord of men, A mighty saint of glorious fame, The hermit Vi[vámitra138 came. For evil fiends that roam by night Disturbed him in each holy rite, And in their strength and frantic rage Assailed with witcheries the sage. He came to seek the monarch's aid To guard the rites the demons stayed, Unable to a close to bring One unpolluted offering. Seeking the king in this dire strait He said to those who kept the gate: “Haste, warders, to your master run, And say that here stands Gádhi's son.” 138 The story of this famous saint is given at sufficient length in Cantos LI-LV. This saint has given his name to the district and city to the east of Benares. The original name, preserved in a land-grant on copper now in the Museum of the Benares College, has been Moslemized into Ghazeepore (the City of the Soldier-martyr).
- **Translation**: 

---

### Verse 19 (Ramayana 0.124)
- **Original**: 106 The Ramayana Soon as they heard the holy man, To the king's chamber swift they ran With minds disordered all, and spurred To wildest zeal by what they heard. On to the royal hall they sped, There stood and lowly bowed the head, And made the lord of men aware That the great saint was waiting there. The king with priest and peer arose And ran the sage to meet, As Indra from his palace goes Lord Brahmá's self to greet. When glowing with celestial light The pious hermit was in sight, The king, whose mien his transport showed, The honoured gift for guests bestowed. Nor did the saint that gift despise, Offered as holy texts advise; He kindly asked the earth's great king How all with him was prospering. The son of Ku[ik139 bade him tell If all in town and field were well, All well with friends, and kith and kin, And royal treasure stored within: “Do all thy neighbours own thy sway? Thy foes confess thee yet? Dost thou continue still to pay To Gods and men each debt?” Then he, of hermits first and best, Va [ishmha with a smile140 addressed, And asked him of his welfare too, Showing him honour as was due. 139 The son of Ku[ik is Vi[vámitra. 140 At the recollection of their former enmity, to be described hereafter.
- **Translation**: 

---

### Verse 20 (Ramayana 0.125)
- **Original**: Canto XX. Visvámitra's Visit. 107 Then with the sainted hermit all Went joyous to the monarch's hall, And sate them down by due degree, Each one, of rank and dignity. Joy filled the noble prince's breast Who thus bespoke the honoured guest: “As amrit141 by a mortal found, As rain upon the thirsty ground, As to an heirless man a son Born to him of his precious one, As gain of what we sorely miss, As sudden dawn of mighty bliss, So is thy coming here to me: All welcome, mighty Saint, to thee. What wish within thy heart hast thou? If I can please thee, tell me how. Hail, Saint, from whom all honours flow, Worthy of all I can bestow. Blest is my birth with fruit to-day, Nor has my life been thrown away. I see the best of Bráhman race And night to glorious morn gives place. Thou, holy Sage, in days of old Among the royal saints enrolled, Didst, penance-glorified, within The Bráhman caste high station win. 'Tis meet and right in many a way That I to thee should honour pay. This seems a marvel to mine eyes: All sin thy visit purifies; And I by seeing thee, O Sage, Have reaped the fruit of pilgrimage. 141 The Indian nectar or drink of the Gods.
- **Translation**: 

---

