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

### Verse 1 (Ramayana 0.866)
- **Original**: 848 The Ramayana Here for the months, content, he stayed, There for a year his visit paid: Here for four months his home would fix, There, as it chanced, for five or six. Here for eight months and there for three The son of Raghu's stay would be: Here weeks, there fortnights, more or less, He spent in tranquil happiness. As there the hero dwelt at ease Among those holy devotees, In days untroubled o'er his head Ten circling years of pleasure fled. So Raghu's son in duty trained A while in every cot remained, Then with his dame retraced the road To good SutíkshGa's calm abode. Hailed by the saints with honours due Near to the hermit's home he drew, And there the tamer of his foes Dwelt for a time in sweet repose. One day within that holy wood By saint SutíkshGa Ráma stood, And thus the prince with reverence meek To that high sage began to speak: “In the wide woodlands that extend Around us, lord most reverend, As frequent voice of rumour tells, Agastya, saintliest hermit, dwells. So vast the wood, I cannot trace The path to reach his dwelling place, Nor, searching unassisted, find That hermit of the thoughtful mind. I with my wife and brother fain
- **Translation**: 

---

### Verse 2 (Ramayana 0.867)
- **Original**: Canto XI. Agastya. 849 Would go, his favour to obtain, Would seek him in his lone retreat And the great saint with reverence greet. This one desire, O Master, long Cherished within my heart, is strong, That I may pay of free accord My duty to that hermit lord.” As thus the prince whose heart was bent On virtue told his firm intent, The good SutíkshGa's joy rose high, And thus in turn he made reply: “The very thing, O Prince, which thou Hast sought, I wished to urge but now, Bid thee with wife and brother see [241] Agastya, glorious devotee. I count this thing an omen fair That thou shouldst thus thy wish declare, And I, my Prince, will gladly teach The way Agastya's home to reach. Southward, dear son, direct thy feet Eight leagues beyond this still retreat: Agastya's hermit brother there Dwells in a home most bright and fair. 'Tis on a knoll of woody ground, With many a branching Pippal426 crowned: There sweet birds' voices ne'er are mute, And trees are gay with flower and fruit. There many a lake gleams bright and cool, And lilies deck each pleasant pool, While swan, and crane, and mallard's wings Are lovely in the water-springs. There for one night, O Ráma, stay, 426 The holy fig-tree.
- **Translation**: 

---

### Verse 3 (Ramayana 0.868)
- **Original**: 850 The Ramayana And with the dawn pursue thy way. Still farther, bending southward, by The thicket's edge the course must lie, And thou wilt see, two leagues from thence Agastya's lovely residence, Set in the woodland's fairest spot, All varied foliage decks the cot: There Sítá, LakshmaG thou, at ease May spend sweet hours neath shady trees, For all of noblest growth are found Luxuriant on that bosky ground. If it be still thy firm intent To see that saint preëminent, O mighty counsellor, this day Depart upon thine onward way.” The hermit spake, and Ráma bent His head, with LakshmaG, reverent, And then with him and Janak's child Set out to trace the forest wild. He saw dark woods that fringed the road, And distant hills like clouds that showed, And, as the way he followed, met With many a lake and rivulet. So passing on with ease where led The path SutíkshGa bade him tread, The hero with exulting breast His brother in these words addressed: “Here, surely, is the home, in sight, Of that illustrious anchorite: Here great Agastya's brother leads A life intent on holy deeds. Warned of each guiding mark and sign,
- **Translation**: 

---

### Verse 4 (Ramayana 0.869)
- **Original**: Canto XI. Agastya. 851 I see them all herein combine: I see the branches bending low Beneath the flowers and fruit they show. A soft air from the forest springs, Fresh from the odorous grass, and brings A spicy fragrance as it flees O'er the ripe fruit of Pippal trees. See, here and there around us high Piled up in heaps cleft billets lie, And holy grass is gathered, bright As strips of shining lazulite. Full in the centre of the shade The hermits' holy fire is laid: I see its smoke the pure heaven streak Dense as a big cloud's dusky peak. The twice-born men their steps retrace From each sequestered bathing-place, And each his sacred gift has brought Of blossoms which his hands have sought. Of all these signs, dear brother, each Agrees with good SutíkshGa's speech, And doubtless in this holy bound Agastya's brother will be found. Agastya once, the worlds who viewed With love, a Deathlike fiend subdued, And armed with mighty power, obtained By holy works, this grove ordained To be a refuge and defence From all oppressors' violence. In days of yore within this place Two brothers fierce of demon race, Vátápi dire and Ilval, dwelt, And slaughter mid the Bráhmans dealt. A Bráhman's form, the fiend to cloak,
- **Translation**: 

---

### Verse 5 (Ramayana 0.870)
- **Original**: 852 The Ramayana Fierce Ilval wore, and Sanskrit spoke, And twice-born sages would invite To solemnize some funeral rite. His brother's flesh, concealed within A ram's false shape and borrowed skin,— As men are wont at funeral feasts,— He dressed and fed those gathered priests. The holy men, unweeting ill, Took of the food and ate their fill. Then Ilval with a mighty shout Exclaimed“Vátápi, issue out.” Soon as his brother's voice he heard, The fiend with ram-like bleating stirred: Rending in pieces every frame, Forth from the dying priests he came. So they who changed their forms at will Thousands of Bráhmans dared to kill,— Fierce fiends who loved each cruel deed, And joyed on bleeding flesh to feed. Agastya, mighty hermit, pressed To funeral banquet like the rest, Obedient to the Gods' appeal Ate up the monster at a meal. “'Tis done, 'tis done,” fierce Ilval cried, And water for his hands supplied: Then lifting up his voice he spake: “Forth, brother, from thy prison break.” Then him who called the fiend, who long Had wrought the suffering Bráhmans wrong, Thus thoughtful-souled Agastya, best Of hermits, with a smile addressed: “How, Rákshas, is the fiend empowered To issue forth whom I devoured? Thy brother in a ram's disguise
- **Translation**: 

---

### Verse 6 (Ramayana 0.871)
- **Original**: Canto XI. Agastya. 853 Is gone where Yáma's kingdom lies.” [242] When from the words Agastya said He knew his brother fiend was dead, His soul on fire with vengeful rage, Rushed the night-rover at the sage. One lightning glance of fury, hot As fire, the glorious hermit shot, As the fiend neared him in his stride, And straight, consumed to dust, he died. In pity for the Bráhmans' plight Agastya wrought this deed of might: This grove which lakes and fair trees grace In his great brother's dwelling place.” As Ráma thus the tale rehearsed, And with Sumitrá's son conversed, The setting sun his last rays shed, And evening o'er the land was spread. A while the princely brothers stayed And even rites in order paid, Then to the holy grove they drew And hailed the saint with honour due. With courtesy was Ráma met By that illustrious anchoret, And for one night he rested there Regaled with fruit and hermit fare. But when the night had reached its close, And the sun's glorious circle rose, The son of Raghu left his bed And to the hermit's brother said: “Well rested in thy hermit cell, I stand, O saint, to bid farewell; For with thy leave I journey hence Thy brother saint to reverence.”
- **Translation**: 

---

### Verse 7 (Ramayana 0.872)
- **Original**: 854 The Ramayana “Go, Ráma go,” the sage replied: Then from the cot the chieftain hied. And while the pleasant grove he viewed, The path the hermit showed, pursued. Of every leaf, of changing hue. Plants, trees by hundreds round him grew, With joyous eyes he looked on all, Then Jak,427 the wild rice, and Sál;428 He saw the red Hibiscus glow, He saw the flower-tipped creeper throw The glory of her clusters o'er Tall trees that loads of blossom bore. Some, elephants had prostrate laid, In some the monkeys leapt and played, And through the whole wide forest rang The charm of gay birds as they sang. Then Ráma of the lotus eye To LakshmaG turned who followed nigh, And thus the hero youth impressed With Fortune's favouring signs, addressed: “How soft the leaves of every tree, How tame each bird and beast we see! Soon the fair home shall we behold Of that great hermit tranquil-souled. The deed the good Agastya wrought High fame throughout the world has bought: I see, I see his calm retreat That balms the pain of weary feet. Where white clouds rise from flames beneath, Where bark-coats lie with many a wreath, Where silvan things, made gentle, throng, 427 The bread-fruit tree, Artocarpus integrifolia. 428 A fine timber tree, Shorea robusta.
- **Translation**: 

---

### Verse 8 (Ramayana 0.873)
- **Original**: Canto XI. Agastya. 855 And every bird is loud in song. With ruth for suffering creatures filled, A deathlike fiend with might he killed, And gave this southern realm to be A refuge, from oppression free. There stands his home, whose dreaded might Has put the giant crew to flight, Who view with envious eyes afar The peaceful shades they cannot mar. Since that most holy saint has made His dwelling in this lovely shade, Checked by his might the giant brood Have dwelt in peace with souls subdued. And all this southern realm, within Whose bounds no fiend may entrance win, Now bears a name which naught may dim, Made glorious through the worlds by him. When Vindhya, best of hills, would stay The journey of the Lord of Day, Obedient to the saint's behest He bowed for aye his humbled crest. That hoary hermit, world-renowned For holy deeds, within this ground Has set his pure and blessed home, Where gentle silvan creatures roam. Agastya, whom the worlds revere, Pure saint to whom the good are dear, To us his guests all grace will show, Enriched with blessings ere we go. I to this aim each thought will turn, The favour of the saint to earn, That here in comfort may be spent The last years of our banishment. Here sanctities and high saints stand,
- **Translation**: 

---

### Verse 9 (Ramayana 0.874)
- **Original**: 856 The Ramayana Gods, minstrels of the heavenly band; Upon Agastya's will they wait, And serve him, pure and temperate. The liar's tongue, the tyrant's mind Within these bounds no home may find: No cheat, no sinner here can be: So holy and so good is he. Here birds and lords of serpent race, Spirits and Gods who haunt the place, Content with scanty fare remain, As merit's meed they strive to gain. Made perfect here, the saints supreme, On cars that mock the Day-God's gleam,— Their mortal bodies cast aside,— Sought heaven transformed and glorified, Here Gods to living things, who win Their favour, pure from cruel sin, Give royal rule and many a good,[243] Immortal life and spirithood. Now, LakshmaG, we are near the place: Do thou precede a little space, And tell the mighty saint that I With Sítá at my side am nigh.” Canto XII. The Heavenly Bow. He spoke: the younger prince obeyed: Within the bounds his way he made, And thus addressed, whom first he met, A pupil of the anchoret:
- **Translation**: 

---

### Verse 10 (Ramayana 0.875)
- **Original**: Canto XII. The Heavenly Bow. 857 “Brave Ráma, eldest born, who springs, From Da[aratha, hither brings His wife the lady Sítá: he Would fain the holy hermit see. Lakshma G am I— if happy fame E'er to thine ears has brought the name— His younger brother, prompt to do His will, devoted, fond, and true. We, through our royal sire's decree, To the dread woods were forced to flee. Tell the great Master, I entreat, Our earnest wish our lord to greet.” He spoke: the hermit rich in store Of fervid zeal and sacred lore, Sought the pure shrine which held the fire, To bear his message to the sire. Soon as he reached the saint most bright In sanctity's surpassing might, He cried, uplifting reverent hands: “Lord Ráma near thy cottage stands.” Then spoke Agastya's pupil dear The message for his lord to hear: “Ráma and LakshmaG, chiefs who spring From Da[aratha, glorious king, Thy hermitage e'en now have sought, And lady Sítá with them brought. The tamers of the foe are here To see thee, Master, and revere. 'Tis thine thy further will to say: Deign to command, and we obey.”
- **Translation**: 

---

### Verse 11 (Ramayana 0.876)
- **Original**: 858 The Ramayana When from his pupil's lips he knew The presence of the princely two, And Sítá born to fortune high. The glorious hermit made reply: “Great joy at last is mine this day That Ráma hither finds his way, For long my soul has yearned to see The prince who comes to visit me. Go forth, go forth, and hither bring The royal three with welcoming: Lead Ráma in and place him near: Why stands he not already here?” Thus ordered by the hermit, who, Lord of his thought, all duty knew, His reverent hands together laid, The pupil answered and obeyed. Forth from the place with speed he ran, To LakshmaG came and thus began: “Where is he? let not Ráma wait, But speed, the sage to venerate.” Then with the pupil LakshmaG went Across the hermit settlement, And showed him Ráma where he stood With Janak's daughter in the wood. The pupil then his message spake Which the kind hermit bade him take; Then led the honoured Ráma thence And brought him in with reverence. As nigh the royal Ráma came With LakshmaG and the Maithil dame, He viewed the herds of gentle deer Roaming the garden free from fear.
- **Translation**: 

---

### Verse 12 (Ramayana 0.877)
- **Original**: Canto XII. The Heavenly Bow. 859 As through the sacred grove he trod He viewed the seat of many a God, Brahmá and Agni,429 Sun and Moon, And His who sends each golden boon;430 Here VishGu's stood, there Bhaga's431 shrine, And there Mahendra's, Lord divine; Here His who formed this earthly frame,432 His there from whom all beings came.433 Váyu's,434 and His who loves to hold The great noose, VaruG435 mighty-souled: Here was the Vasus'436 shrine to see, Here that of sacred Gáyatrí,437 The king of serpents438 here had place, And he who rules the feathered race.439 Here Kártikeya,440 warrior lord, And there was Justice King adored. Then with disciples girt about The mighty saint himself came out: Through fierce devotion bright as flame Before the rest the Master came: And then to LakshmaG, fortune blest, Ráma these hasty words addressed: “Behold, Agastya's self draws near, 429 The God of fire. 430 Kuvera, the God of riches. 431 The Sun. 432 Brahmá, the creator. 433 Ziva. 434 The Wind-God. 435 The God of the sea. 436 A class of demi-gods, eight in number. 437 The holiest text of the Vedas, deified. 438 Vásuki. 439 Garu . 440 The War-God.
- **Translation**: 

---

### Verse 13 (Ramayana 0.878)
- **Original**: 860 The Ramayana The mighty saint, whom all revere: With spirit raised I meet my lord With richest wealth of penance stored.” The strong-armed hero spake, and ran Forward to meet the sunbright man. Before him, as he came, he bent And clasped his feet most reverent, Then rearing up his stately height Stood suppliant by the anchorite, While LakshmaG's strength and Sítá's grace Stood by the pride of Raghu's race.[244] The sage his arms round Ráma threw And welcomed him with honours due, Asked, was all well, with question sweet, And bade the hero to a seat. With holy oil he fed the flame, He brought the gifts which strangers claim, And kindly waiting on the three With honours due to high degree, He gave with hospitable care A simple hermit's woodland fare. Then sat the reverend father, first Of hermits, deep in duty versed. And thus to suppliant Ráma, bred In all the lore of virtue, said: “Did the false hermit, Prince, neglect To hail his guest with due respect, He must,— the doom the perjured meet,— His proper flesh hereafter eat. A car-borne king, a lord who sways The earth, and virtue's law obeys, Worthy of highest honour, thou Hast sought, dear guest, my cottage now.”
- **Translation**: 

---

### Verse 14 (Ramayana 0.879)
- **Original**: Canto XII. The Heavenly Bow. 861 He spoke: with fruit and hermit fare, With every bloom the branches bare, Agastya graced his honoured guest, And thus with gentle words addressed: “Accept this mighty bow, divine, Whereon red gold and diamonds shine; 'Twas by the Heavenly Artist planned For VishGu's own almighty hand; This God-sent shaft of sunbright hue, Whose deadly flight is ever true, By Lord Mahendra given of yore: This quiver with its endless store. Keen arrows hurtling to their aim Like kindled fires that flash and flame: Accept, in golden sheath encased, This sword with hilt of rich gold graced. Armed with this best of bows Lord VishGu slew his demon foes, And mid the dwellers in the skies Won brilliant glory for his prize. The bow, the quivers, shaft, and sword Received from me, O glorious lord: These conquest to thine arm shall bring, As thunder to the thunder's King.” The splendid hermit bade him take The noble weapons as he spake, And as the prince accepted each In words like these renewed his speech:
- **Translation**: 

---

### Verse 15 (Ramayana 0.880)
- **Original**: 862 The Ramayana Canto XIII. Agastya's Counsel. “O Ráma, great delight I feel, Pleased, LakshmaG, with thy faithful zeal, That you within these shades I see With Sítá come to honour me. But wandering through the rough rude wild Has wearied Janak's gentle child: With labours of the way oppressed The Maithil lady longs for rest. Young, delicate, and soft, and fair, Such toils as these untrained to bear, Her wifely love the dame has led The forest's troubled ways to tread. Here, Ráma, see that naught annoy Her easy hours of tranquil joy: A glorious task has she assayed, To follow thee through woodland shade. Since first from Nature's hand she came, A woman's mood is still the same, When Fortune smiles, her love to show, And leave her lord in want and woe. No pity then her heart can feel, She arms her soul with warrior's steel, Swift as the storm or Feathered King, Uncertain as the lightning's wing. Not so thy spouse: her purer mind Shrinks from the faults of womankind; Like chaste Arundhatí441 above, A paragon of faithful love. Let these blest shades, dear Ráma, be A home for LakshmaG, her, and thee.” 441 One of the Pleiades generally regarded as the model of wifely excellence.
- **Translation**: 

---

### Verse 16 (Ramayana 0.881)
- **Original**: Canto XIII. Agastya's Counsel. 863 With raised hands reverently meek He heard the holy hermit speak, And humbly thus addressed the sire Whose glory shone like kindled fire: “How blest am I, what thanks I owe That our great Master deigns to show His favour, that his heart can be Content with LakshmaG, Sítá, me. Show me, I pray, some spot of ground Where thick trees wave and springs abound, That I may raise my hermit cell And there in tranquil pleasure dwell.” Then thus replied Agastya, best Of hermits, to the chief's request: When for a little he had bent His thoughts, upon that prayer intent: “Beloved son, four leagues away Is Panchavamí bright and gay: Thronged with its deer, most fair it looks With berries, fruit, and water-brooks. There build thee with thy brother's aid A cottage in the quiet shade, And faithful to thy sire's behest, Obedient to the sentence, rest. For well, O sinless chieftain, well I know thy tale, how all befell: Stern penance and the love I bore Thy royal sire supply the lore. To me long rites and fervid zeal The wish that stirs thy heart reveal, And hence my guest I bade thee be, That this pure grove might shelter thee. [245]
- **Translation**: 

---

### Verse 17 (Ramayana 0.882)
- **Original**: 864 The Ramayana So now, thereafter, thus I speak: The shades of Panchavamí seek; That tranquil spot is bright and fair, And Sítá will be happy there. Not far remote from here it lies, A grove to charm thy loving eyes, Godávarí's pure stream is nigh: There Sítá's days will sweetly fly. Pure, lovely, rich in many a charm, O hero of the mighty arm, 'Tis gay with every plant and fruit, And throngs of gay buds never mute. Thou, true to virtue's path, hast might To screen each trusting anchorite, And wilt from thy new home defend The hermits who on thee depend. Now yonder, Prince, direct thine eyes Where dense Madhúka442 woods arise: Pierce their dark shade, and issuing forth Turn to a fig-tree on the north: Then onward up a sloping mead Flanked by a hill the way will lead: There Panchavamí, ever gay With ceaseless bloom, thy steps will stay.” The hermit ceased: the princely two With seemly honours bade adieu: With reverential awe each youth Bowed to the saint whose word was truth, And then, dismissed with Sítá, they To Panchavamí took their way. Thus when each royal prince had grasped 442 The Madhúka, or, as it is now called, Mahuwá, is the Bassia latifolia, a tree from whose blossoms a spirit is extracted.
- **Translation**: 

---

### Verse 18 (Ramayana 0.883)
- **Original**: Canto XIV. Jatáyus. 865 His warrior's mighty bow, and clasped His quiver to his side, With watchful eyes along the road The glorious saint Agastya showed, Dauntless in fight the brothers strode, And Sítá with them hied. Canto XIV. Jatáyus. Then as the son of Raghu made His way to Panchavamí's shade, A mighty vulture he beheld Of size and strength unparalleled. The princes, when the bird they saw, Approached with reverence and awe, And as his giant form they eyed, “Tell who thou art,” in wonder cried. The bird, as though their hearts to gain, Addressed them thus in gentlest strain; “In me, dear sons, the friend behold Your royal father loved of old.” He spoke: nor long did Ráma wait His sire's dear friend to venerate: He bade the bird declare his name And the high race of which he came. When Raghu's son had spoken, he Declared his name and pedigree, His words prolonging to disclose How all the things that be arose:
- **Translation**: 

---

### Verse 19 (Ramayana 0.884)
- **Original**: 866 The Ramayana “List while I tell, O Raghu's son, The first-born Fathers, one by one, Great Lords of Life, whence all in earth And all in heaven derive their birth. First Kardam heads the glorious race Where Vikrit holds the second place, With Zesha, San[ray next in line, And Bahuputra's might divine. Then StháGu and Maríchi came, Atri, and Kratu's forceful frame. Pulastya followed, next to him Angiras' name shall ne'er be dim. Prachetas, Pulah next, and then Daksha, Vivasvat praised of men: Aríshmanemi next, and last Ka [yap in glory unsurpassed. From Daksha,— fame the tale has told— : Three-score bright daughters sprang of old. Of these fair-waisted nymphs the great Lord Ka[yap sought and wedded eight, Aditi, Diti, Kálaká, Támrá, Danú, and Analá, And Krodhavasá swift to ire, And Manu 443 glorious as her sire. 443 “I should have doubted whether Manu could have been the right reading here, but that it occurs again in verse 29, where it is in like manner followed in verse 31 by Analá, so that it would certainly seem that the name Manu is intended to stand for a female, the daughter of Daksha. The Gau a recension, followed by Signor Gorresio (III 20, 12), adopts an entirely different reading at the end of the line, viz.Balám Atibalám api,‘Balá and Atibilá,’instead of Manu and Analá. I see that Professor Roth s.v. adduces the authority of the Amara Kosha and of the Commentator on PáGini for stating that the word sometimes means ‘the wife of Manu.’ In the following text of the Mahábhárata I. 2553. also, Manu appears to be the name of a female:‘Anaradyam ,Manum ,Vañsám , Asurám,Márga Gapriyám,Anúpám ,Subhagám ,Bhásím iti,Prádhá vyajayata.
- **Translation**: 

---

### Verse 20 (Ramayana 0.885)
- **Original**: Canto XIV. Jatáyus. 867 Then when the mighty Ka[yap cried Delighted to each tender bride: “Sons shalt thou bear, to rule the three Great worlds, in might resembling me.” [246] Aditi, Diti, and Danú Obeyed his will as consorts true, And Kálaká; but all the rest Refused to hear their lord's behest. First Aditi conceived, and she, Mother of thirty Gods and three, The Vasus and Ádityas bare, Rudras, and A[vins, heavenly pair. Of Diti sprang the Daityas: fame Delights to laud their ancient name. In days of yore their empire dread O'er earth and woods and ocean spread. Danú was mother of a child, O hero, A[vagríva styled, And Narak next and Kálak came Of Kálaká, celestial dame. Of Támrá, too, five daughters bright In deathless glory sprang to light. Ennobling fame still keeps alive The titles of the lovely five: Immortal honour still she claims For Kraunchí, Bhasí,Zyení's names. And wills not that the world forget Zukí or Dhritaráshtrí yet. Then Kraunchí bare the crane and owl, And Bhásí tribes of water fowl: Vultures and hawks that race through air With storm-fleet pinionsZyení bare. Prádhá (daughter of Daksha) bore Anavadyá, Manu, Van[á, MárgaGapriyá, Anúpá, Subhagá. and Bhásí.’ ”Muir's Sanskrit Text, Vol. I. p. 116.
- **Translation**: 

---

