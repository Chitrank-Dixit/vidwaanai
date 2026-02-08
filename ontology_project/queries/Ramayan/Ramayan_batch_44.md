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

### Verse 1 (Ramayan 0.861)
- **Original**: Canto X. Ráma's Reply. 843 Of Bráhman race declared their grief. I heard, and from my lips there fell The words which thou rememberest well: I listened as the hermits cried, And to their prayers I thus replied: “Your favour, gracious lords, I claim, O'erwhelmed with this enormous shame That Bráhmans, great and pure as you, Who should be sought, to me should sue.” And then before the saintly crowd, “What can I do?” I cried aloud. Then from the trembling hermits broke One long sad cry, and thus they spoke: “Fiends of the wood, who wear at will Each varied shape, afflict us still. To thee in our distress we fly: O help us, Ráma, or we die. When sacred rites of fire are due, When changing moons are full or new, These fiends who bleeding flesh devour Assail us with resistless power. They with their cruel might torment The hermits on their vows intent: We look around for help and see Our surest refuge, Prince, in thee. We, armed with powers of penance, might Destroy the rovers of the night: But loth were we to bring to naught The merit years of toil have bought. Our penance rites are grown too hard, By many a check and trouble barred, But though our saints for food are slain The withering curse we yet restrain.
- **Translation**: 

---

### Verse 2 (Ramayan 0.862)
- **Original**: 844 The Ramayana Thus many a weary day distressed By giants who this wood infest, We see at length deliverance, thou With LakshmaG art our guardian now.” As thus the troubled hermits prayed, I promised, dame, my ready aid, And now — for truth I hold most dear— Still to my word must I adhere. My love, I might endure to be Deprived of LakshmaG, life, and thee, But ne'er deny my promise, ne'er To Bráhmans break the oath I sware. I must, enforced by high constraint, Protect them all. Each suffering saint In me, unasked, his help had found; Still more in one by promise bound. I know thy words, mine own dear dame, From thy sweet heart's affection came: I thank thee for thy gentle speech, For those we love are those we teach. 'Tis like thyself, O fair of face, 'Tis worthy of thy noble race: Dearer than life, thy feet are set In righteous paths they ne'er forget.” Thus to the Maithil monarch's child, His own dear wife, in accents mild The high-souled hero said: Then to the holy groves which lay Beyond them fair to see, their way The bow-armed chieftain led.
- **Translation**: 

---

### Verse 3 (Ramayan 0.863)
- **Original**: Canto XI. Agastya. 845 Canto XI. Agastya. Ráma went foremost of the three, Next Sítá, followed, fair to see, And Lakshma G with his bow in hand Walked hindmost of the little band. As onward through the wood they went, With great delight their eyes were bent On rocky heights beside the way And lofty trees with blossoms gay; And streamlets running fair and fast The royal youths with Sítá passed. They watched the sáras and the drake On islets of the stream and lake, And gazed delighted on the floods Bright with gay birds and lotus buds. They saw in startled herds the roes, The passion-frenzied buffaloes, Wild elephants who fiercely tore The tender trees, and many a boar. A length of woodland way they passed, And when the sun was low at last A lovely stream-fed lake they spied, Two leagues across from side to side. Tall elephants fresh beauty gave To grassy bank and lilied wave, [240] By many a swan and sáras stirred, Mallard, and gay-winged water-bird. From those sweet waters, loud and long, Though none was seen to wake the song, Swelled high the singer's music blent With each melodious instrument. Ráma and car-borne LakshmaG heard The charming strain, with wonder stirred,
- **Translation**: 

---

### Verse 4 (Ramayan 0.864)
- **Original**: 846 The Ramayana Turned on the margent of the lake To Dharmabhrit424 the sage, and spake: “Our longing souls, O hermit, burn This music of the lake to learn: We pray thee, noblest sage, explain The cause of the mysterious strain.” He, as the son of Raghu prayed, With swift accord his answer made, And thus the hermit, virtuous-souled, The story of the fair lake told: “Through every age 'tis known to fame, Panchápsaras425 its glorious name, By holy MáG akarGi wrought With power his rites austere had bought. For he, great votarist, intent On strictest rule his stern life spent. Ten thousand years the stream his bed, Ten thousand years on air he fed. Then on the blessed Gods who dwell In heavenly homes great terror fell: They gathered all, by Agni led, And counselled thus disquieted: “The hermit by ascetic pain The seat of one of us would gain.” Thus with their hearts by fear oppressed In full assembly spoke the Blest, And bade five loveliest nymphs, as fair As lightning in the evening air, Armed with their winning wiles, seduce From his stern vows the great recluse. 424 One of the hermits who had followed Ráma. 425 The lake of the five nymphs.
- **Translation**: 

---

### Verse 5 (Ramayan 0.865)
- **Original**: Canto XI. Agastya. 847 Though lore of earth and heaven he knew, The hermit from his task they drew, And made the great ascetic slave To conquering love, the Gods to save. Each of the heavenly five became, Bound to the sage, his wedded dame; And he, for his beloved's sake, Formed a fair palace neath the lake. Under the flood the ladies live, To joy and ease their days they give, And lap in bliss the hermit wooed From penance rites to youth renewed. So when the sportive nymphs within Those secret bowers their play begin, You hear the singers' dulcet tones Blend sweetly with their tinkling zones.” “How wondrous are these words of thine!” Cried the famed chiefs of Raghu's line, As thus they heard the sage unfold The marvels of the tale he told. As Ráma spake, his eyes were bent Upon a hermit settlement With light of heavenly lore endued, With sacred grass and vesture strewed. His wife and brother by his side, Within the holy bounds he hied, And there, with honour entertained By all the saints, a while remained. In time, by due succession led, Each votary's cot he visited, And then the lord of martial lore, Returned where he had lodged before.
- **Translation**: 

---

### Verse 6 (Ramayan 0.866)
- **Original**: 848 The Ramayana Here for the months, content, he stayed, There for a year his visit paid: Here for four months his home would fix, There, as it chanced, for five or six. Here for eight months and there for three The son of Raghu's stay would be: Here weeks, there fortnights, more or less, He spent in tranquil happiness. As there the hero dwelt at ease Among those holy devotees, In days untroubled o'er his head Ten circling years of pleasure fled. So Raghu's son in duty trained A while in every cot remained, Then with his dame retraced the road To good SutíkshGa's calm abode. Hailed by the saints with honours due Near to the hermit's home he drew, And there the tamer of his foes Dwelt for a time in sweet repose. One day within that holy wood By saint SutíkshGa Ráma stood, And thus the prince with reverence meek To that high sage began to speak: “In the wide woodlands that extend Around us, lord most reverend, As frequent voice of rumour tells, Agastya, saintliest hermit, dwells. So vast the wood, I cannot trace The path to reach his dwelling place, Nor, searching unassisted, find That hermit of the thoughtful mind. I with my wife and brother fain
- **Translation**: 

---

### Verse 7 (Ramayan 0.867)
- **Original**: Canto XI. Agastya. 849 Would go, his favour to obtain, Would seek him in his lone retreat And the great saint with reverence greet. This one desire, O Master, long Cherished within my heart, is strong, That I may pay of free accord My duty to that hermit lord.” As thus the prince whose heart was bent On virtue told his firm intent, The good SutíkshGa's joy rose high, And thus in turn he made reply: “The very thing, O Prince, which thou Hast sought, I wished to urge but now, Bid thee with wife and brother see [241] Agastya, glorious devotee. I count this thing an omen fair That thou shouldst thus thy wish declare, And I, my Prince, will gladly teach The way Agastya's home to reach. Southward, dear son, direct thy feet Eight leagues beyond this still retreat: Agastya's hermit brother there Dwells in a home most bright and fair. 'Tis on a knoll of woody ground, With many a branching Pippal426 crowned: There sweet birds' voices ne'er are mute, And trees are gay with flower and fruit. There many a lake gleams bright and cool, And lilies deck each pleasant pool, While swan, and crane, and mallard's wings Are lovely in the water-springs. There for one night, O Ráma, stay, 426 The holy fig-tree.
- **Translation**: 

---

### Verse 8 (Ramayan 0.868)
- **Original**: 850 The Ramayana And with the dawn pursue thy way. Still farther, bending southward, by The thicket's edge the course must lie, And thou wilt see, two leagues from thence Agastya's lovely residence, Set in the woodland's fairest spot, All varied foliage decks the cot: There Sítá, LakshmaG thou, at ease May spend sweet hours neath shady trees, For all of noblest growth are found Luxuriant on that bosky ground. If it be still thy firm intent To see that saint preëminent, O mighty counsellor, this day Depart upon thine onward way.” The hermit spake, and Ráma bent His head, with LakshmaG, reverent, And then with him and Janak's child Set out to trace the forest wild. He saw dark woods that fringed the road, And distant hills like clouds that showed, And, as the way he followed, met With many a lake and rivulet. So passing on with ease where led The path SutíkshGa bade him tread, The hero with exulting breast His brother in these words addressed: “Here, surely, is the home, in sight, Of that illustrious anchorite: Here great Agastya's brother leads A life intent on holy deeds. Warned of each guiding mark and sign,
- **Translation**: 

---

### Verse 9 (Ramayan 0.869)
- **Original**: Canto XI. Agastya. 851 I see them all herein combine: I see the branches bending low Beneath the flowers and fruit they show. A soft air from the forest springs, Fresh from the odorous grass, and brings A spicy fragrance as it flees O'er the ripe fruit of Pippal trees. See, here and there around us high Piled up in heaps cleft billets lie, And holy grass is gathered, bright As strips of shining lazulite. Full in the centre of the shade The hermits' holy fire is laid: I see its smoke the pure heaven streak Dense as a big cloud's dusky peak. The twice-born men their steps retrace From each sequestered bathing-place, And each his sacred gift has brought Of blossoms which his hands have sought. Of all these signs, dear brother, each Agrees with good SutíkshGa's speech, And doubtless in this holy bound Agastya's brother will be found. Agastya once, the worlds who viewed With love, a Deathlike fiend subdued, And armed with mighty power, obtained By holy works, this grove ordained To be a refuge and defence From all oppressors' violence. In days of yore within this place Two brothers fierce of demon race, Vátápi dire and Ilval, dwelt, And slaughter mid the Bráhmans dealt. A Bráhman's form, the fiend to cloak,
- **Translation**: 

---

### Verse 10 (Ramayan 0.870)
- **Original**: 852 The Ramayana Fierce Ilval wore, and Sanskrit spoke, And twice-born sages would invite To solemnize some funeral rite. His brother's flesh, concealed within A ram's false shape and borrowed skin,— As men are wont at funeral feasts,— He dressed and fed those gathered priests. The holy men, unweeting ill, Took of the food and ate their fill. Then Ilval with a mighty shout Exclaimed“Vátápi, issue out.” Soon as his brother's voice he heard, The fiend with ram-like bleating stirred: Rending in pieces every frame, Forth from the dying priests he came. So they who changed their forms at will Thousands of Bráhmans dared to kill,— Fierce fiends who loved each cruel deed, And joyed on bleeding flesh to feed. Agastya, mighty hermit, pressed To funeral banquet like the rest, Obedient to the Gods' appeal Ate up the monster at a meal. “'Tis done, 'tis done,” fierce Ilval cried, And water for his hands supplied: Then lifting up his voice he spake: “Forth, brother, from thy prison break.” Then him who called the fiend, who long Had wrought the suffering Bráhmans wrong, Thus thoughtful-souled Agastya, best Of hermits, with a smile addressed: “How, Rákshas, is the fiend empowered To issue forth whom I devoured? Thy brother in a ram's disguise
- **Translation**: 

---

### Verse 11 (Ramayan 0.871)
- **Original**: Canto XI. Agastya. 853 Is gone where Yáma's kingdom lies.” [242] When from the words Agastya said He knew his brother fiend was dead, His soul on fire with vengeful rage, Rushed the night-rover at the sage. One lightning glance of fury, hot As fire, the glorious hermit shot, As the fiend neared him in his stride, And straight, consumed to dust, he died. In pity for the Bráhmans' plight Agastya wrought this deed of might: This grove which lakes and fair trees grace In his great brother's dwelling place.” As Ráma thus the tale rehearsed, And with Sumitrá's son conversed, The setting sun his last rays shed, And evening o'er the land was spread. A while the princely brothers stayed And even rites in order paid, Then to the holy grove they drew And hailed the saint with honour due. With courtesy was Ráma met By that illustrious anchoret, And for one night he rested there Regaled with fruit and hermit fare. But when the night had reached its close, And the sun's glorious circle rose, The son of Raghu left his bed And to the hermit's brother said: “Well rested in thy hermit cell, I stand, O saint, to bid farewell; For with thy leave I journey hence Thy brother saint to reverence.”
- **Translation**: 

---

### Verse 12 (Ramayan 0.872)
- **Original**: 854 The Ramayana “Go, Ráma go,” the sage replied: Then from the cot the chieftain hied. And while the pleasant grove he viewed, The path the hermit showed, pursued. Of every leaf, of changing hue. Plants, trees by hundreds round him grew, With joyous eyes he looked on all, Then Jak,427 the wild rice, and Sál;428 He saw the red Hibiscus glow, He saw the flower-tipped creeper throw The glory of her clusters o'er Tall trees that loads of blossom bore. Some, elephants had prostrate laid, In some the monkeys leapt and played, And through the whole wide forest rang The charm of gay birds as they sang. Then Ráma of the lotus eye To LakshmaG turned who followed nigh, And thus the hero youth impressed With Fortune's favouring signs, addressed: “How soft the leaves of every tree, How tame each bird and beast we see! Soon the fair home shall we behold Of that great hermit tranquil-souled. The deed the good Agastya wrought High fame throughout the world has bought: I see, I see his calm retreat That balms the pain of weary feet. Where white clouds rise from flames beneath, Where bark-coats lie with many a wreath, Where silvan things, made gentle, throng, 427 The bread-fruit tree, Artocarpus integrifolia. 428 A fine timber tree, Shorea robusta.
- **Translation**: 

---

### Verse 13 (Ramayan 0.873)
- **Original**: Canto XI. Agastya. 855 And every bird is loud in song. With ruth for suffering creatures filled, A deathlike fiend with might he killed, And gave this southern realm to be A refuge, from oppression free. There stands his home, whose dreaded might Has put the giant crew to flight, Who view with envious eyes afar The peaceful shades they cannot mar. Since that most holy saint has made His dwelling in this lovely shade, Checked by his might the giant brood Have dwelt in peace with souls subdued. And all this southern realm, within Whose bounds no fiend may entrance win, Now bears a name which naught may dim, Made glorious through the worlds by him. When Vindhya, best of hills, would stay The journey of the Lord of Day, Obedient to the saint's behest He bowed for aye his humbled crest. That hoary hermit, world-renowned For holy deeds, within this ground Has set his pure and blessed home, Where gentle silvan creatures roam. Agastya, whom the worlds revere, Pure saint to whom the good are dear, To us his guests all grace will show, Enriched with blessings ere we go. I to this aim each thought will turn, The favour of the saint to earn, That here in comfort may be spent The last years of our banishment. Here sanctities and high saints stand,
- **Translation**: 

---

### Verse 14 (Ramayan 0.874)
- **Original**: 856 The Ramayana Gods, minstrels of the heavenly band; Upon Agastya's will they wait, And serve him, pure and temperate. The liar's tongue, the tyrant's mind Within these bounds no home may find: No cheat, no sinner here can be: So holy and so good is he. Here birds and lords of serpent race, Spirits and Gods who haunt the place, Content with scanty fare remain, As merit's meed they strive to gain. Made perfect here, the saints supreme, On cars that mock the Day-God's gleam,— Their mortal bodies cast aside,— Sought heaven transformed and glorified, Here Gods to living things, who win Their favour, pure from cruel sin, Give royal rule and many a good,[243] Immortal life and spirithood. Now, LakshmaG, we are near the place: Do thou precede a little space, And tell the mighty saint that I With Sítá at my side am nigh.” Canto XII. The Heavenly Bow. He spoke: the younger prince obeyed: Within the bounds his way he made, And thus addressed, whom first he met, A pupil of the anchoret:
- **Translation**: 

---

### Verse 15 (Ramayan 0.875)
- **Original**: Canto XII. The Heavenly Bow. 857 “Brave Ráma, eldest born, who springs, From Da[aratha, hither brings His wife the lady Sítá: he Would fain the holy hermit see. Lakshma G am I— if happy fame E'er to thine ears has brought the name— His younger brother, prompt to do His will, devoted, fond, and true. We, through our royal sire's decree, To the dread woods were forced to flee. Tell the great Master, I entreat, Our earnest wish our lord to greet.” He spoke: the hermit rich in store Of fervid zeal and sacred lore, Sought the pure shrine which held the fire, To bear his message to the sire. Soon as he reached the saint most bright In sanctity's surpassing might, He cried, uplifting reverent hands: “Lord Ráma near thy cottage stands.” Then spoke Agastya's pupil dear The message for his lord to hear: “Ráma and LakshmaG, chiefs who spring From Da[aratha, glorious king, Thy hermitage e'en now have sought, And lady Sítá with them brought. The tamers of the foe are here To see thee, Master, and revere. 'Tis thine thy further will to say: Deign to command, and we obey.”
- **Translation**: 

---

### Verse 16 (Ramayan 0.876)
- **Original**: 858 The Ramayana When from his pupil's lips he knew The presence of the princely two, And Sítá born to fortune high. The glorious hermit made reply: “Great joy at last is mine this day That Ráma hither finds his way, For long my soul has yearned to see The prince who comes to visit me. Go forth, go forth, and hither bring The royal three with welcoming: Lead Ráma in and place him near: Why stands he not already here?” Thus ordered by the hermit, who, Lord of his thought, all duty knew, His reverent hands together laid, The pupil answered and obeyed. Forth from the place with speed he ran, To LakshmaG came and thus began: “Where is he? let not Ráma wait, But speed, the sage to venerate.” Then with the pupil LakshmaG went Across the hermit settlement, And showed him Ráma where he stood With Janak's daughter in the wood. The pupil then his message spake Which the kind hermit bade him take; Then led the honoured Ráma thence And brought him in with reverence. As nigh the royal Ráma came With LakshmaG and the Maithil dame, He viewed the herds of gentle deer Roaming the garden free from fear.
- **Translation**: 

---

### Verse 17 (Ramayan 0.877)
- **Original**: Canto XII. The Heavenly Bow. 859 As through the sacred grove he trod He viewed the seat of many a God, Brahmá and Agni,429 Sun and Moon, And His who sends each golden boon;430 Here VishGu's stood, there Bhaga's431 shrine, And there Mahendra's, Lord divine; Here His who formed this earthly frame,432 His there from whom all beings came.433 Váyu's,434 and His who loves to hold The great noose, VaruG435 mighty-souled: Here was the Vasus'436 shrine to see, Here that of sacred Gáyatrí,437 The king of serpents438 here had place, And he who rules the feathered race.439 Here Kártikeya,440 warrior lord, And there was Justice King adored. Then with disciples girt about The mighty saint himself came out: Through fierce devotion bright as flame Before the rest the Master came: And then to LakshmaG, fortune blest, Ráma these hasty words addressed: “Behold, Agastya's self draws near, 429 The God of fire. 430 Kuvera, the God of riches. 431 The Sun. 432 Brahmá, the creator. 433 Ziva. 434 The Wind-God. 435 The God of the sea. 436 A class of demi-gods, eight in number. 437 The holiest text of the Vedas, deified. 438 Vásuki. 439 Garu . 440 The War-God.
- **Translation**: 

---

### Verse 18 (Ramayan 0.878)
- **Original**: 860 The Ramayana The mighty saint, whom all revere: With spirit raised I meet my lord With richest wealth of penance stored.” The strong-armed hero spake, and ran Forward to meet the sunbright man. Before him, as he came, he bent And clasped his feet most reverent, Then rearing up his stately height Stood suppliant by the anchorite, While LakshmaG's strength and Sítá's grace Stood by the pride of Raghu's race.[244] The sage his arms round Ráma threw And welcomed him with honours due, Asked, was all well, with question sweet, And bade the hero to a seat. With holy oil he fed the flame, He brought the gifts which strangers claim, And kindly waiting on the three With honours due to high degree, He gave with hospitable care A simple hermit's woodland fare. Then sat the reverend father, first Of hermits, deep in duty versed. And thus to suppliant Ráma, bred In all the lore of virtue, said: “Did the false hermit, Prince, neglect To hail his guest with due respect, He must,— the doom the perjured meet,— His proper flesh hereafter eat. A car-borne king, a lord who sways The earth, and virtue's law obeys, Worthy of highest honour, thou Hast sought, dear guest, my cottage now.”
- **Translation**: 

---

### Verse 19 (Ramayan 0.879)
- **Original**: Canto XII. The Heavenly Bow. 861 He spoke: with fruit and hermit fare, With every bloom the branches bare, Agastya graced his honoured guest, And thus with gentle words addressed: “Accept this mighty bow, divine, Whereon red gold and diamonds shine; 'Twas by the Heavenly Artist planned For VishGu's own almighty hand; This God-sent shaft of sunbright hue, Whose deadly flight is ever true, By Lord Mahendra given of yore: This quiver with its endless store. Keen arrows hurtling to their aim Like kindled fires that flash and flame: Accept, in golden sheath encased, This sword with hilt of rich gold graced. Armed with this best of bows Lord VishGu slew his demon foes, And mid the dwellers in the skies Won brilliant glory for his prize. The bow, the quivers, shaft, and sword Received from me, O glorious lord: These conquest to thine arm shall bring, As thunder to the thunder's King.” The splendid hermit bade him take The noble weapons as he spake, And as the prince accepted each In words like these renewed his speech:
- **Translation**: 

---

### Verse 20 (Ramayan 0.880)
- **Original**: 862 The Ramayana Canto XIII. Agastya's Counsel. “O Ráma, great delight I feel, Pleased, LakshmaG, with thy faithful zeal, That you within these shades I see With Sítá come to honour me. But wandering through the rough rude wild Has wearied Janak's gentle child: With labours of the way oppressed The Maithil lady longs for rest. Young, delicate, and soft, and fair, Such toils as these untrained to bear, Her wifely love the dame has led The forest's troubled ways to tread. Here, Ráma, see that naught annoy Her easy hours of tranquil joy: A glorious task has she assayed, To follow thee through woodland shade. Since first from Nature's hand she came, A woman's mood is still the same, When Fortune smiles, her love to show, And leave her lord in want and woe. No pity then her heart can feel, She arms her soul with warrior's steel, Swift as the storm or Feathered King, Uncertain as the lightning's wing. Not so thy spouse: her purer mind Shrinks from the faults of womankind; Like chaste Arundhatí441 above, A paragon of faithful love. Let these blest shades, dear Ráma, be A home for LakshmaG, her, and thee.” 441 One of the Pleiades generally regarded as the model of wifely excellence.
- **Translation**: 

---

