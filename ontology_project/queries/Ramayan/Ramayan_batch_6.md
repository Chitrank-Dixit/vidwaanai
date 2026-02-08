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

### Verse 1 (Ramayan 0.101)
- **Original**: Canto XIV. Rávan Doomed. 83 When thus the suppliant Gods had prayed, His wise reply NáráyaG108 made: “What task demands my presence there, And whence this dread, ye Gods declare.” The Gods replied:“We fear, O Lord, Fierce RávaG, ravener abhorred. Be thine the glorious task, we pray, In human form this fiend to slay. By thee of all the Blest alone This sinner may be overthrown. He gained by penance long and dire The favour of the mighty Sire. Then He who every gift bestows Guarded the fiend from heavenly foes, And gave a pledge his life that kept From all things living, man except. On him thus armed no other foe Than man may deal the deadly blow. Assume, O King, a mortal birth, And strike the demon to the earth.” Then VishGu, God of Gods, the Lord Supreme by all the worlds adored, To Brahmá and the suppliants spake: “Dismiss your fear: for your dear sake In battle will I smite him dead, The cruel fiend, the Immortal's dread. And lords and ministers and all His kith and kin with him shall fall. Then, in the world of mortal men, 108 One of the most ancient and popular of the numerous names of VishGu. The word has been derived in several ways, and may meanhe who moved on the (primordial) waters, orhe who pervades or influences men or their thoughts.
- **Translation**: 

---

### Verse 2 (Ramayan 0.102)
- **Original**: 84 The Ramayana Ten thousand years and hundreds ten I as a human king will reign, And guard the earth as my domain.” God, saint, and nymph, and minstrel throng With heavenly voices raised their song In hymns of triumph to the God Whose conquering feet on Madhu trod: “Champion of Gods, as man appear, This cruel RávaG slay, The thorn that saints and hermits fear, The plague that none can stay. In savage fury uncontrolled His pride for ever grows: He dares the Lord of Gods to hold Among his deadly foes.” Canto XV. The Nectar. When wisest VishGu thus had given His promise to the Gods of heaven, He pondered in his secret mind A suited place of birth to find, Then he decreed, the lotus-eyed, In four his being to divide, And Da [aratha, gracious king, He chose as sire from whom to spring. That childless prince of high renown, Who smote in war his foemen down, At that same time with utmost care
- **Translation**: 

---

### Verse 3 (Ramayan 0.103)
- **Original**: Canto XV. The Nectar. 85 Prepared the rite that wins an heir.109 Then VishGu, fain on earth to dwell, Bade the Almighty Sire farewell, And vanished while a reverent crowd Of Gods and saints in worship bowed. The monarch watched the sacred rite, When a vast form of awful might, Of matchless splendour, strength, and size Was manifest before his eyes. [027] From forth the sacrificial flame, Dark, robed in red, the being came. His voice was drumlike, loud and low, His face suffused with rosy glow. Like a huge lion's mane appeared The long locks of his hair and beard. He shone with many a lucky sign, And many an ornament divine; A towering mountain in his height, A tiger in his gait and might. No precious mine more rich could be, No burning flame more bright than he. His arms embraced in loving hold, Like a dear wife, a vase of gold Whose silver lining held a draught Of nectar as in heaven is quaffed: A vase so vast, so bright to view, They scarce could count the vision true. Upon the king his eyes he bent, And said:“The Lord of life has sent His servant down, O Prince, to be A messenger from heaven to thee.” The king with all his nobles by 109 The Horse-Sacrifice, just described.
- **Translation**: 

---

### Verse 4 (Ramayan 0.104)
- **Original**: 86 The Ramayana Raised reverent hands and made reply: “Welcome, O glorious being! Say How can my care thy grace repay.” Envoy of Him whom all adore Thus to the king he spake once more: “The Gods accept thy worship: they Give thee the blessed fruit to-day. Approach and take, O glorious King, This heavenly nectar which I bring, For it shall give thee sons and wealth, And bless thee with a store of health. Give it to those fair queens of thine, And bid them quaff the drink divine: And they the princely sons shall bear Long sought by sacrifice and prayer.” “Yea, O my lord,” the monarch said, And took the vase upon his head, The gift of Gods, of fine gold wrought, With store of heavenly liquor fraught. He honoured, filled with transport new, That wondrous being, fair to view, As round the envoy of the God With reverential steps he trod.110 His errand done, that form of light 110 To walk round an object keeping the right side towards it is a mark of great respect. The Sanskrit word for the observance ispradakshiGá, from pra pro, anddaksha right, Greek´µ¾w¿Â, Latin dexter, Gaelic deas-il. A similar ceremony is observed by the Gaels. “In the meantime she traced around him, with wavering steps, the propitia- tion, which some have thought has been derived from the Druidical mythology. It consists, as is well known, in the person who makes thedeasilwalking three times round the person who is the object of the ceremony, taking care to move according to the course of the sun.” SCOTT {FNS .The Two Drovers.
- **Translation**: 

---

### Verse 5 (Ramayan 0.105)
- **Original**: Canto XV. The Nectar. 87 Arose and vanished from the sight. High rapture filled the monarch's soul, Possessed of that celestial bowl, As when a man by want distressed With unexpected wealth is blest. And rays of transport seemed to fall Illuminating bower and hall, As when the autumn moon rides high, And floods with lovely light the sky. Quick to the ladies' bower he sped, And thus to Queen Kau[alyá said: “This genial nectar take and quaff,” He spoke, and gave the lady half. Part of the nectar that remained Sumitrá from his hand obtained. He gave, to make her fruitful too, Kaikeyí half the residue. A portion yet remaining there, He paused awhile to think. Then gave Sumitrá, with her share. The remnant of the drink. Thus on each queen of those fair three A part the king bestowed, And with sweet hope a child to see Their yearning bosoms glowed. The heavenly bowl the king supplied Their longing souls relieved, And soon, with rapture and with pride, Each royal dame conceived. He gazed upon each lady's face, And triumphed as he gazed, As Indra in his royal place By Gods and spirits praised.
- **Translation**: 

---

### Verse 6 (Ramayan 0.106)
- **Original**: 88 The Ramayana Canto XVI. The Vánars. When VishGu thus had gone on earth, From the great king to take his birth, The self-existent Lord of all Addressed the Gods who heard his call: “For VishGu's sake, the strong and true, Who seeks the good of all of you, Make helps, in war to lend him aid, In forms that change at will, arrayed, Of wizard skill and hero might, Outstrippers of the wind in flight, Skilled in the arts of counsel, wise, And VishGu's peers in bold emprise; With heavenly arts and prudence fraught, By no devices to be caught; Skilled in all weapon's lore and use As they who drink the immortal juice.111[028] And let the nymphs supreme in grace, And maidens of the minstrel race, Monkeys and snakes, and those who rove Free spirits of the hill and grove, And wandering Daughters of the Air, In monkey form brave children bear. So erst the lord of bears I shaped, Born from my mouth as wide I gaped.” 111 The Amrit, the nectar of the Indian Gods.
- **Translation**: 

---

### Verse 7 (Ramayan 0.107)
- **Original**: Canto XVI. The Vánars. 89 Thus by the mighty Sire addressed They all obeyed his high behest, And thus begot in countless swarms Brave sons disguised in sylvan forms. Each God, each sage became a sire, Each minstrel of the heavenly quire,112 Each faun,113 of children strong and good Whose feet should roam the hill and wood. Snakes, bards,114 and spirits,115 serpents bold Had sons too numerous to be told. Báli, the woodland hosts who led, High as Mahendra's116 lofty head, Was Indra's child. That noblest fire, The Sun, was great Sugríva's sire, Tára, the mighty monkey, he Was offspring of V[ihaspati:117 Tára the matchless chieftain, boast For wisdom of the Vánar host. Of Gandhamádan brave and bold The father was the Lord of Gold. 112 Gandharvas (Southey's Glendoveers) are celestial musicians inhabiting In- dra's heaven and forming the orchestra at all the banquets of the principal deities. 113 Yakshas, demigods attendant especially on Kuvera, and employed by him in the care of his garden and treasures. 114 Kimpurushas, demigods attached also to the service of Kuvera, celestial musicians, represented like centaurs reversed with human figures and horses' heads. 115 Siddhas, demigods or spirits of undefined attributes, occupying with the Vidyádharasthe middle air or region between the earth and the sun. Schlegel translates:“Divi, Sapientes, Fidicines, Præpetes, illustres Genii, Præconesque procrearunt natos, masculos, silvicolas; angues porro, Hip- pocephali Beati, Aligeri, Serpentesque frequentes alacriter generavere prolem innumerabilem.” 116 A mountain in the south of India. 117 The preceptor of the Gods and regent of the planet Jupiter.
- **Translation**: 

---

### Verse 8 (Ramayan 0.108)
- **Original**: 90 The Ramayana Nala the mighty, dear to fame, Of skilful Vi[vakarmá118 came. From Agni,119 Nila bright as flame, Who in his splendour, might, and worth, Surpassed the sire who gave him birth. The heavenly A[vins,120 swift and fair, Were fathers of a noble pair, Who, Dwivida and Mainda named, For beauty like their sires were famed, VaruG121 was father of SusheG, Of Sarabh, he who sends the rain,122 Hanúmán, best of monkey kind, Was son of him who breathes the wind: Like thunderbolt in frame was he, And swift as Garu 's123 self could flee. These thousands did the Gods create Endowed with might that none could mate, In monkey forms that changed at will; So strong their wish the fiend to kill. In mountain size, like lions thewed, Up sprang the wondrous multitude, Auxiliar hosts in every shape, Monkey and bear and highland ape. In each the strength, the might, the mien Of his own parent God were seen. 118 The celestial architect, the Indian Hephæstus, Mulciber, or Vulcan. 119 The God of Fire. 120 Twin children of the Sun, the physicians of Swarga or Indra's heaven. 121 The deity of the waters. 122 Parjanya, sometimes confounded with Indra. 123 The bird and vehicle of VishGu. He is generally represented as a being something between a man and a bird and considered as the sovereign of the feathered race. He may be compared with the Simurgh of the Persians, the 'Anká of the Arabs, the Griffin of chivalry, the Phœ nix of Egypt, and the bird that sits upon the ash Yggdrasil of the Edda.
- **Translation**: 

---

### Verse 9 (Ramayan 0.109)
- **Original**: Canto XVI. The Vánars. 91 Some chiefs of Vánar mothers came, Some of she-bear and minstrel dame, Skilled in all arms in battle's shock; The brandished tree, the loosened rock; And prompt, should other weapons fail, To fight and slay with tooth and nail. Their strength could shake the hills amain, And rend the rooted trees in twain, Disturb with their impetuous sweep The Rivers' Lord, the Ocean deep, Rend with their feet the seated ground, And pass wide floods with airy bound, Or forcing through the sky their way The very clouds by force could stay. Mad elephants that wander through The forest wilds, could they subdue, And with their furious shout could scare Dead upon earth the birds of air. So were the sylvan chieftains formed; Thousands on thousands still they swarmed. These were the leaders honoured most, The captains of the Vánar host, And to each lord and chief and guide Was monkey offspring born beside. Then by the bears' great monarch stood The other roamers of the wood, [029] And turned, their pathless homes to seek, To forest and to mountain peak. The leaders of the monkey band By the two brothers took their stand, Sugríva, offspring of the Sun And Báli, Indra's mighty one. They both endowed with Garu 's might, And skilled in all the arts of fight,
- **Translation**: 

---

### Verse 10 (Ramayan 0.110)
- **Original**: 92 The Ramayana Wandered in arms the forest through, And lions, snakes, and tigers, slew. But every monkey, ape, and bear Ever was Báli's special care; With his vast strength and mighty arm He kept them from all scathe and harm. And so the earth with hill, wood, seas, Was filled with mighty ones like these, Of various shape and race and kind, With proper homes to each assigned, With Ráma's champions fierce and strong The earth was overspread, High as the hills and clouds, a throng With bodies vast and dread.124 Canto XVII. Rishyasring's Return. Now when the high-souled monarch's rite, The A[vamedh, was finished quite, Their sacrificial dues obtained, The Gods their heavenly homes regained. The lofty-minded saints withdrew, Each to his place, with honour due, And kings and chieftains, one and all, 124 This Canto will appear ridiculous to the European reader. But it should be remembered that the monkeys of an Indian forest, the“bough-deer” as the poets call them, are very different animals from the“turpissima bestia” that accompanies the itinerant organ-grinder or grins in the Zoological Gardens of London. Milton has made his hero, Satan, assume the forms of a cormorant, a toad, and a serpent, and I cannot see that this creation of semi-divine Vánars, or monkeys, is more ridiculous or undignified.
- **Translation**: 

---

### Verse 11 (Ramayan 0.111)
- **Original**: Canto XVII. Rishyasring's Return. 93 Who came to grace the festival. And Da [aratha, ere they went, Addressed them thus benevolent: “Now may you, each with joyful heart, To your own realms, O Kings, depart. Peace and good luck attend you there, And blessing, is my friendly prayer; Let cares of state each mind engage To guard his royal heritage. A monarch from his throne expelled No better than the dead is held. So he who cares for power and might Must guard his realm and royal right. Such care a meed in heaven will bring Better than rites and offering. Such care a king his country owes As man upon himself bestows, When for his body he provides Raiment and every need besides. For future days should kings foresee, And keep the present error-free.” Thus did the king the kings exhort: They heard, and turned them from the court And, each to each in friendship bound, Went forth to all the realms around. The rites were o'er, the guests were sped: The train the best of Bráhmans led, In which the king with joyful soul, With his dear wives, and with the whole Of his imperial host and train Of cars and servants turned again, And, as a monarch dear to fame, Within his royal city came.
- **Translation**: 

---

### Verse 12 (Ramayan 0.112)
- **Original**: 94 The Ramayana Next, Rishya[ring, well-honoured sage, And Zántá, sought their hermitage. The king himself, of prudent mind, Attended him, with troops behind. And all her men the town outpoured With Saint Va[ishmha and their lord. High mounted on a car of state, O'er canopied fairZántá sate. Drawn by white oxen, while a band Of servants marched on either hand. Great gifts of countless price she bore, With sheep and goats and gems in store. Like Beauty's self the lady shone With all the jewels she had on, As, happy in her sweet content, Peerless amid the fair she went. Not Queen Paulomí's125 self could be More loving to her lord than she. She who had lived in happy ease, Honoured with all her heart could please, While dames and kinsfolk ever vied To see her wishes gratified, Soon as she knew her husband's will Again to seek the forest, still Was ready for the hermit's cot, Nor murmured at her altered lot. The king attended to the wild That hermit and his own dear child, And in the centre of a throng Of noble courtiers rode along. The sage's son had let prepare A lodge within the wood, and there 125 The consort of Indra, called alsoZachí and IndráGí.
- **Translation**: 

---

### Verse 13 (Ramayan 0.113)
- **Original**: Canto XVII. Rishyasring's Return. 95 While they lingered blithe and gay. Then, duly honoured, went their way. The glorious hermit Rishya[ring Drew near and thus besought the king: [030] “Return, my honoured lord, I pray, Return, upon thy homeward way.” The monarch, with the waiting crowd, Lifted his voice and wept aloud, And with eyes dripping still to each Of his good queens he spake this speech: “Kau [alyá and Sumitrá dear, And thou, my sweet Kaikeyí, hear. All uponZántá feast your gaze, The last time for a length of days.” To Zántá's arms the ladies leapt, And hung about her neck and wept, And cried,“O, happy be the life Of this great Bráhman and his wife. The Wind, the Fire, the Moon on high, The Earth, the Streams, the circling Sky, Preserve thee in the wood, true spouse, Devoted to thy husband's vows. And O dearZántá, ne'er neglect To pay the dues of meek respect To the great saint, thy husband's sire, With all observance and with fire. And, sweet one, pure of spot and blame, Forget not thou thy husband's claim; In every change, in good and ill, Let thy sweet words delight him still, And let thy worship constant be: Her lord is woman's deity.
- **Translation**: 

---

### Verse 14 (Ramayan 0.114)
- **Original**: 96 The Ramayana To learn thy welfare, dearest friend, The king will many a Bráhman send. Let happy thoughts thy spirit cheer, And be not troubled, daughter dear.” These soothing words the ladies said. And pressed their lips upon her head. Each gave with sighs her last adieu, Then at the king's command withdrew. The king around the hermit went With circling footsteps reverent, And placed at Rishya[ring's command Some soldiers of his royal band. The Bráhman bowed in turn and cried, “May fortune never leave thy side. O mighty King, with justice reign, And still thy people's love retain.” He spoke, and turned away his face, And, as the hermit went, The monarch, rooted to the place, Pursued with eyes intent. But when the sage had past from view King Da[aratha turned him too, Still fixing on his friend each thought. With such deep love his breast was fraught. Amid his people's loud acclaim Home to his royal seat he came, And lived delighted there, Expecting when each queenly dame, Upholder of his ancient fame, Her promised son should bear. The glorious sage his way pursued Till close before his eyes he viewed Sweet Champá, Lomapád's fair town,
- **Translation**: 

---

### Verse 15 (Ramayan 0.115)
- **Original**: Canto XVIII. Rishyasring's Departure. 97 Wreathed with her Champacs'126 leafy crown. Soon as the saint's approach he knew, The king, to yield him honour due, Went forth to meet him with a band Of priests and nobles of the land: “Hail, Sage,” he cried,“O joy to me! What bliss it is, my lord, to see Thee with thy wife and all thy train Returning to my town again. Thy father, honoured Sage, is well, Who hither from his woodland cell Has sent full many a messenger For tidings both of thee and her.” Then joyfully, for due respect, The monarch bade the town be decked. The king and Rishya[ring elate Entered the royal city's gate: In front the chaplain rode. Then, loved and honoured with all care By monarch and by courtier, there The glorious saint abode. Canto XVIII. Rishyasring's Departure. 126 The Michelia champaca. It bears a scented yellow blossom: “The maid of India blest again to hold In her full lap the Champac's leaves of gold.” Lallah Rookh.
- **Translation**: 

---

### Verse 16 (Ramayan 0.116)
- **Original**: 98 The Ramayana The monarch called a Bráhman near And said,“Now speed away To Ka[yap's son,127 the mighty seer, And with all reverence say The holy child he holds so dear, The hermit of the noble mind, Whose equal it were hard to find, Returned, is dwelling here. Go, and instead of me do thou Before that best of hermits bow, That still he may, for his dear son, Show me the favour I have won.” Soon as the king these words had said, To Ka[yap's son the Bráhman sped. Before the hermit low he bent And did obeisance, reverent; Then with meek words his grace to crave The message of his lord he gave: “The high-souled father of his bride Had called thy son his rites to guide: Those rites are o'er, the steed is slain; Thy noble child is come again.” Soon as the saint that speech had heard His spirit with desire was stirred To seek the city of the king And to his cot his son to bring.[031] With young disciples at his side Forth on his way the hermit hied, While peasants from their hamlets ran To reverence the holy man. Each with his little gift of food, Forth came the village multitude, 127 VibháGdak, the father of Rishya[ring
- **Translation**: 

---

### Verse 17 (Ramayan 0.117)
- **Original**: Canto XVIII. Rishyasring's Departure. 99 And, as they humbly bowed the head, “What may we do for thee?” they said. Then he, of Bráhmans first and best, The gathered people thus addressed: “Now tell me for I fain would know, Why is it I am honoured so?” They to the high-souled saint replied: “Our ruler is with thee allied. Our master's order we fulfil; O Bráhman, let thy mind be still.” With joy the saintly hermit heard Each pleasant and delightful word, And poured a benediction down On king and ministers and town. Glad at the words of that high saint Some servants hastened to acquaint Their king, rejoicing to impart The tidings that would cheer his heart. Soon as the joyful tale he knew To meet the saint the monarch flew, The guest-gift in his hand he brought, And bowed before him and besought: “This day by seeing thee I gain Not to have lived my life in vain, Now be not wroth with me, I pray, “Because I wiled thy son away.128 128 A hemi[loka is wanting in Schlegel's text, which he thus fills up in his Latin translation.
- **Translation**: 

---

### Verse 18 (Ramayan 0.118)
- **Original**: 100 The Ramayana The best of Bráhmans answer made: “Be not, great lord of kings, afraid. Thy virtues have not failed to win My favour, O thou pure of sin.” Then in the front the saint was placed, The king came next in joyous haste, And with him entered his abode, Mid glad acclaim as on they rode. To greet the sage the reverent crowd Raised suppliant hands and humbly bowed. Then from the palace many a dame Following well-dressedZántá came, Stood by the mighty saint and cried: “See, honour's source, thy son's dear bride.” The saint, who every virtue knew, His arms around his daughter threw, And with a father's rapture pressed The lady to his wondering breast. Arising from the saint's embrace She bowed her low before his face, And then, with palm to palm applied, Stood by her hermit father's side. He for his son, as laws ordain, Performed the rite that frees from stain,129 And, honoured by the wise and good, With him departed to the wood. Canto XIX. The Birth Of The Princes. 129 Rishya[ring, a Bráhman, had marriedZántá who was of the Kshatriya or Warrior caste and an expiatory ceremony was necessary on account of this violation of the law.
- **Translation**: 

---

### Verse 19 (Ramayan 0.119)
- **Original**: Canto XIX. The Birth Of The Princes. 101 The seasons six in rapid flight Had circled since that glorious rite. Eleven months had passed away; 'Twas Chaitra's ninth returning day.130 The moon within that mansion shone Which Aditi looks kindly on. Raised to their apex in the sky Five brilliant planets beamed on high. Shone with the moon, in Cancer's sign, V [ihaspati131 with light divine. Kau [alyá bore an infant blest With heavenly marks of grace impressed; Ráma, the universe's lord, A prince by all the worlds adored. New glory Queen Kau[alyá won Reflected from her splendid son. So Aditi shone more and more, The Mother of the Gods, when she The King of the Immortals132 bore, The thunder-wielding deity. [032] 130 “The poet no doubt intended to indicate the vernal equinox as the birthday of Ráma. For the monthChaitrais the first of the two months assigned to the spring; it corresponds with the latter half of March and the former half of April in our division of the year.Aditi, the mother of the Gods, is lady of the seventh lunar mansion which is calledPunarvasu. The five planets and their positions in the Zodiac are thus enumerated by both commentators: the Sun in Aries, Mars in Capricorn, Saturn in Libra, Jupiter in Cancer, Venus in Pisces.… I leave to astronomers to examine whether the parts of the description agree with one another, and, if this be the case, thence to deduce the date. The Indians place the nativity of Ráma in the confines of the second age (tretá) and the third (dwápara): but it seems that this should be taken in an allegorical sense.… We may consider that the poet had an eye to the time in which, immediately before his own age, the aspects of the heavenly bodies were such as he has described.” SCHLEGEL {FNS . 131 The regent of the planet Jupiter. 132 Indra = Jupiter Tonans.
- **Translation**: 

---

### Verse 20 (Ramayan 0.120)
- **Original**: 102 The Ramayana The lotus-eyed, the beauteous boy, He came fierce RávaG to destroy; From half of VishGu's vigour born, He came to help the worlds forlorn. And Queen Kaikeyí bore a child Of truest valour, Bharat styled, With every princely virtue blest, One fourth of VishGu manifest. Sumitrá too a noble pair, Called LakshmaG and Zatrughna, bare, Of high emprise, devoted, true, Sharers in VishGu's essence too. 'Neath Pushya's133 mansion, Mina's134 sign, Was Bharat born, of soul benign. The sun had reached the Crab at morn When Queen Sumitrá's babes were born, What time the moon had gone to make His nightly dwelling with the Snake. The high-souled monarch's consorts bore At different times those glorious four, Like to himself and virtuous, bright As Proshmhapadá's135 four-fold light. Then danced the nymphs' celestial throng, The minstrels raised their strain; The drums of heaven pealed loud and long, And flowers came down in rain. Within Ayodhyá, blithe and gay, All kept the joyous holiday. 133 “Pushya is the name of a month; but here it means the eighth mansion. The ninth is calledAsleshá, or the snake. It is evident from this that Bharat, though his birth is mentioned before that of the twins, was the youngest of the four brothers and Ráma's junior by eleven months.” SCHLEGEL {FNS . 134 A fish, the Zodiacal signPisces. 135 One of the constellations, containing stars in the wing of Pegasus.
- **Translation**: 

---

