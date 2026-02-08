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

### Verse 1 (Ramayana 0.1166)
- **Original**: 1148 The Ramayana How shall I dare her sire to greet Whose lips have never known deceit? How stand before the childless king And meet his eager questioning? When banished by my sire's decree, In low estate, she followed me. So pure, so true to every vow, Where is my gentle darling now? How can I bear my widowed lot, And linger on where she is not, Who followed when from home I fled Distracted, disinherited? My spirit sinks in hopeless pain When my fond glances yearn in vain For that dear face with whose bright eye The worshipped lotus scarce can vie. Ah when, my brother, shall I hear That voice that rang so soft and clear, When, sweetly smiling as she spoke, From her dear lips gay laughter broke? When worn with toil and love I strayed With Sítá through the forest shade, No trace of grief was seen in her, My kind and thoughtful comforter. How shall my faltering tongue relate To Queen Kau[alyá Sítá's fate? How answer when in wild despair She questions, Where is Sítá, where? Haste, brother, haste: to Bharat hie, On whose fond love I still rely. My life can be no longer borne, Since Sítá from my side is torn.”
- **Translation**: 

---

### Verse 2 (Ramayana 0.1167)
- **Original**: Canto I. Ráma's Lament. 1149 Thus like a helpless mourner, bent By sorrow, Ráma made lament; And with wise counsel LakshmaG tried To soothe his care, and thus replied: “O best of men, thy grief oppose, Nor sink beneath thy weight of woes. Not thus despond the great and pure And brave like thee, but still endure. Reflect what anguish wrings the heart When loving souls are forced to part; And, mindful of the coming pain, Thy love within thy breast restrain. For earth, though cooled by wandering streams, Lies scorched beneath the midday beams. RávaG his steps to hell may bend, Or lower yet in flight descend; But be thou sure, O Raghu's son, Avenging death he shall not shun. Rise, Ráma, rise: the search begin, And track the giant foul with sin. Then shall the fiend, though far he fly, Resign his prey or surely die. Yea, though the trembling monster hide With Sítá close to Diti's535 side, E'en there, unless he yield the prize, Slain by this wrathful hand he dies. Thy heart with strength and courage stay, And cast this weakling mood away. Our fainting hopes in vain revive Unless with firm resolve we strive. The zeal that fires the toiler's breast 535 A daughter of Daksha who became one of the wives of Ka[yapa and mother of the Daityas. She is termed the general mother of Titans and malignant beings. See Book I Cantos XLV, XLVI.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1168)
- **Original**: 1150 The Ramayana Mid earthly powers is first and best. Zeal every check and bar defies, And wins at length the loftiest prize, In woe and danger, toil and care, Zeal never yields to weak despair. With zealous heart thy task begin, And thou once more thy spouse shalt win. Cast fruitless sorrow from thy soul, Nor let this love thy heart control. Forget not all thy sacred lore, But be thy noble self once more.” He heard, his bosom rent by grief, The counsel of his brother chief; Crushed in his heart the maddening pain, And rose resolved and strong again. Then forth upon his journey went The hero on his task intent, Nor thought of Pampá's lovely brook,[324] Or trees which murmuring breezes shook, Though on dark woods his glances fell, On waterfall and cave and dell; And still by many a care distressed The son of Raghu onward pressed. As some wild elephant elate Moves through the woods in pride, So LakshmaG with majestic gait Strode by his brother's side. He, for his lofty spirit famed, Admonished and consoled; Showed Raghu's son what duty claimed, And bade his heart be bold. Then as the brothers strode apace To Rishyamúka's height,
- **Translation**: 

---

### Verse 4 (Ramayana 0.1169)
- **Original**: Canto II. Sugríva's Alarm. 1151 The sovereign of the Vánar race536 Was troubled at the sight. As on the lofty hill he strayed He saw the chiefs draw near: A while their glorious forms surveyed, And mused in restless fear. His slow majestic step he stayed And gazed upon the pair. And all his spirit sank dismayed By fear too great to bear. When in their glorious might the best Of royal chiefs came nigh, The Vánars in their wild unrest Prepared to turn and fly. They sought the hermit's sacred home537 For peace and bliss ordained, And there, where Vánars loved to roam, A sure asylum gained. Canto II. Sugríva's Alarm. Sugríva moved by wondering awe The high-souled sons of Raghu saw, In all their glorious arms arrayed; And grief upon his spirit weighed. 536 Sugríva, the ex-king of the Vánars, foresters, or monkeys, an exile from his home, wandering about the mountain Rishyamúka with his four faithful ex-ministers. 537 The hermitage of the Saint Matanga which his curse prevented Báli, the present king of the Vánars, from entering. The story is told at length in Canto XI of this Book.
- **Translation**: 

---

### Verse 5 (Ramayana 0.1170)
- **Original**: 1152 The Ramayana To every quarter of the sky He turned in fear his anxious eye, And roving still from spot to spot With troubled steps he rested not. He durst not, as he viewed the pair, Resolve to stand and meet them there; And drooping cheer and quailing breast The terror of the chief confessed. While the great fear his bosom shook, Brief counsel with his lords he took; Each gain and danger closely scanned, What hope in flight, what power to stand, While doubt and fear his bosom rent, On Raghu's sons his eyes he bent, And with a spirit ill at ease Addressed his lords in words like these: “Those chiefs with wandering steps invade The shelter of our pathless shade, And hither come in fair disguise Of hermit garb as Báli's spies.” Each lord beheld with troubled heart Those masters of the bowman's art, And left the mountain side to seek Sure refuge on a loftier peak. The Vánar chief in rapid flight Found shelter on a towering height, And all the band with one accord Were closely gathered round their lord. Their course the same, with desperate leap Each made his way from steep to steep, And speeding on in wild career Filled every height with sudden fear.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1171)
- **Original**: Canto II. Sugríva's Alarm. 1153 Each heart was struck with mortal dread, As on their course the Vánars sped, While trees that crowned the steep were bent And crushed beneath them as they went. As in their eager flight they pressed For safety to each mountain crest, The wild confusion struck with fear Tiger and cat and wandering deer. The lords who watched Sugríva's will Were gathered on the royal hill, And all with reverent hands upraised Upon their king and leader gazed. Sugríva feared some evil planned, Some train prepared by Báli's hand. But, skilled in words that charm and teach, Thus Hanumán 538 began his speech: “Dismiss, dismiss thine idle fear, Nor dread the power of Báli here. For this is Malaya's glorious hill539 Where Báli's might can work no ill. I look around but nowhere see The hated foe who made thee flee, Fell Báli, fierce in form and face: Then fear not, lord of Vánar race. Alas, in thee I clearly find The weakness of the Vánar kind, [325] That loves from thought to thought to range, Fix no belief and welcome change. Mark well each hint and sign and scan, Discreet and wise, thine every plan. 538 Hanumán, Sugríva's chief general, was the son of the God of Wind. See Book I, Canto XVI. 539 A range of hills in Malabar; the Western Ghats in the Deccan.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1172)
- **Original**: 1154 The Ramayana How may a king, with sense denied, The subjects of his sceptre guide?” Hanúmán, 540 wise in hour of need, Urged on the chief his prudent rede. His listening ear Sugríva bent, And spake in words more excellent: “Where is the dauntless heart that free From terror's chilling touch can see Two stranger warriors, strong as those, Equipped with swords and shafts and bows, With mighty arms and large full eyes, Like glorious children of the skies? Báli my foe, I ween, has sent These chiefs to aid his dark intent. Hence doubt and fear disturb me still, For thousands serve a monarch's will, In borrowed garb they come, and those Who walk disguised are counted foes. With secret thoughts they watch their time, And wound fond hearts that fear no crime. My foe in state affairs is wise, And prudent kings have searching eyes. By other hands they strike the foe: By meaner tools the truth they know. Now to those stranger warriors turn, And, less than king, their purpose learn. Mark well the trick and look of each; Observe his form and note his speech. With care their mood and temper sound, 540 Válmíki makes the second vowel in this name long or short to suit the exigencies of the verse. Other Indian poets have followed his example, and the same licence will be used in this translation.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1173)
- **Original**: Canto III. Hanumán's Speech. 1155 And, if their minds be friendly found, With courteous looks and words begin Their confidence and love to win. Then as my friend and envoy speak, And question what the strangers seek. Ask why equipped with shaft and bow Through this wild maze of wood they go. If they, O chief, at first appear Pure of all guile, in heart sincere, Detect in speech and look the sin And treachery that lurk within.” He spoke: the Wind-God's son obeyed. With ready zeal he sought the shade, And reached with hasty steps the wood Where Raghu's son and LakshmaG stood.541 Canto III. Hanumán's Speech. The envoy in his faithful breast Pondered Sugríva's high behest. From Rishyamúka's peak he hied And placed him by the princes' side. The Wind-God's son with cautious art Had laid his Vánar form apart, And wore, to cheat the strangers eyes, 541 I omit a recapitulatory and interpolated verse in a different metre, which is as follows:— Reverencing with the words, So be it, the speech of the greatly terrified and unequalled monkey king, the magnanimous Hanumán then went where (stood) the very mighty Ráma with LakshmaG.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1174)
- **Original**: 1156 The Ramayana A wandering mendicant's disguise.542 Before the heroes' feet he bent And did obeisance reverent, And spoke, the glorious pair to praise, His words of truth in courteous phrase, High honour duly paid, the best Of all the Vánar kind addressed, With free accord and gentle grace, Those glories of their warrior race: “O hermits, blest in vows, who shine Like royal saints or Gods divine, O best of young ascetics, say How to this spot you found your way, Scaring the troops of wandering deer And silvan things that harbour here Searching amid the trees that grow Where Pampá's gentle waters flow. And lending from your brows a gleam Of glory to the lovely stream. Who are you, say, so brave and fair, Clad in the bark which hermits wear? I see you heave the frequent sigh, I see the deer before you fly. While you, for strength and valour dread, The earth, like lordly lions, tread, Each bearing in his hand a bow, Like Indra's own, to slay the foe. With the grand paces of a bull, 542 The semi divine Hanumán possesses, like the Gods and demons, the power of wearing all shapes at will. He is one of theKámarúpís. Like Milton's good and bad angels“as they please They limb themselves, and colour, shape, or size Assume as likes them best, condense or rare.”
- **Translation**: 

---

### Verse 10 (Ramayana 0.1175)
- **Original**: Canto III. Hanumán's Speech. 1157 So bright and young and beautiful. The mighty arms you raise appear Like trunks which elephants uprear, And as you move this mountain-king543 Is glorious with the light you bring. How have you reached, like Gods in face, Best lords of earth, this lonely place, [326] With tresses coiled in hermit guise,544 And splendours of those lotus eyes? As Gods who leave their heavenly sphere, Alike your beauteous forms appear. The Lords of Day and Night545 might thus Stray from the skies to visit us. Heroic youth, so broad of chest, Fair with the beauty of the Blest, With lion shoulders, tall and strong, Like bulls who lead the lowing throng, Your arms, unmatched for grace and length, With massive clubs may vie in strength. Why do no gauds those limbs adorn Where priceless gems were meetly worn? Each noble youth is fit, I deem, To guard this earth, as lord supreme, With all her woods and seas, to reign From Meru's peak to Vindhya's chain. Your smooth bows decked with dyes and gold Are glorious in their masters' hold, And with the arms of Indra546 vie Which diamond splendours beautify. 543 Himálaya is of coursepar excellencethe Monarch of mountains, but the complimentary title is frequently given to other hills as here to Malaya. 544 Twisted up in a matted coil as was the custom of ascetics. 545 The sun and moon. 546 The rainbow.
- **Translation**: 

---

### Verse 11 (Ramayana 0.1176)
- **Original**: 1158 The Ramayana Your quivers glow with golden sheen, Well stored with arrows fleet and keen, Each gleaming like a fiery snake That joys the foeman's life to take. As serpents cast their sloughs away And all their new born sheen display, So flash your mighty swords inlaid With burning gold on hilt and blade. Why are you silent, heroes? Why My questions hear nor deign reply? Sugríva, lord of virtuous mind, The foremost of the Vánar kind, An exile from his royal state, Roams through the land disconsolate. I, Hanumán, of Vánar race, Sent by the king have sought this place, For he, the pious, just, and true, In friendly league would join with you. Know, godlike youths, that I am one Of his chief lords, the Wind-God's son. With course unchecked I roam at will, And now from Rishyamúka's hill, To please his heart, his hope to speed, I came disguised in beggar's weed.” Thus Hanúmán, well trained in lore Of language, spoke, and said no more. The son of Raghu joyed to hear The envoy's speech, and bright of cheer He turned to LakshmaG by his side, And thus in words of transport cried:
- **Translation**: 

---

### Verse 12 (Ramayana 0.1177)
- **Original**: Canto III. Hanumán's Speech. 1159 “The counselor we now behold Of King Sugríva righteous-souled. His face I long have yearned to see, And now his envoy comes to me With sweetest words in courteous phrase Answer this mighty lord who slays His foemen, by Sugríva sent, This Vánar chief most eloquent. For one whose words so sweetly flow The whole Rig-veda547 needs must know, And in his well-trained memory store The Yajush and the Sáman's lore. He must have bent his faithful ear All grammar's varied rules to hear. For his long speech how well he spoke! In all its length no rule he broke. In eye, on brow, in all his face The keenest look no guile could trace. No change of hue, no pose of limb Gave sign that aught was false in him. Concise, unfaltering, sweet and clear, Without a word to pain the ear. From chest to throat, nor high nor low, His accents came in measured flow. How well he spoke with perfect art That wondrous speech that charmed the heart, With finest skill and order graced In words that knew nor pause nor haste! That speech, with consonants that spring From the three seats of uttering,548 547 The Vedas are four in number, the Rich or Rig-veda, the Yajush or Yajur- veda; the Sáman or Sáma-veda, and the Atharvan or Atharva-veda. See p. 3. Note. 548 The chest, the throat, and the head.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1178)
- **Original**: 1160 The Ramayana Would charm the spirit of a foe Whose sword is raised for mortal blow. How may a ruler's plan succeed Who lacks such envoy good at need? How fail, if one whose mind is stored With gifts so rare assist his lord? What plans can fail, with wisest speech Of envoy's lips to further each?” Thus Ráma spoke; and LakshmaG taught In all the art that utters thought, To King Sugríva's learned spy Thus made his eloquent reply: “Full well we know the gifts that grace Sugríva, lord of Vánar race, And hither turn our wandering feet That we that high-souled king may meet. So now our pleasant task shall be To do the words he speaks by thee.” His prudent speech the Vánar heard, And all his heart with joy was stirred. And hope that league with them would bring Redress and triumph to his king. [327] Canto IV. Lakshman's Reply.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1179)
- **Original**: Canto IV. Lakshman's Reply. 1161 Cheered by the words that Ráma spoke, Joy in the Vánar's breast awoke, And, as his friendly mood he knew, His thoughts to King Sugríva flew: “Again,” he mused,“my high-souled lord Shall rule, to kingly state restored; Since one so mighty comes to save, And freely gives the help we crave.” Then joyous Hanumán, the best Of all the Vánar kind, addressed These words to Ráma, trained of yore In all the arts of speakers' lore:549 “Why do your feet this forest tread By silvan life inhabited, This awful maze of tree and thorn Which Pampá's flowering groves adorn?” 549 “In our own metrical romances, or wherever a poem is meant not for readers but for chanters and oral reciters, theseformulæ, to meet the same recurring case, exist by scores. Thus every woman in these metrical romances who happens to be young, is described as‘so bright of ble,’or complexion; always a man goes‘the mountenance of a mile’ before he overtakes or is overtaken. And so on through a vast bead-roll of cases. In the same spirit Homer has his eternalÄ¿½ ´'±Á'QÀ¿´Á± ¹´É½, orÄ¿½ ´'±À±¼µ¹²¿¼µ½¿Â ÀÁ¿ÃÆ·, &c. To a reader of sensibility, such recurrences wear an air of child-like sim- plicity, beautifully recalling the features of Homer's primitive age. But they would have appeared faults to all commonplace critics in literary ages.” D E Q UINCEY {FNS .Homer and the Homeridæ.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1180)
- **Original**: 1162 The Ramayana He spoke: obedient to the eye Of Ráma, LakshmaG made reply, The name and fortune to unfold Of Raghu's son the lofty-souled: “True to the law, of fame unstained, The glorious Da[aratha reigned, And, steadfast in his duty, long Kept the four castes550 from scathe and wrong. Through his wide realm his will was done, And, loved by all, he hated none. Just to each creature great and small, Like the Good Sire he cared for all. The Ágnishmom,551 as priests advised, And various rites he solemnized, Where ample largess ever paid The Bráhmans for their holy aid. Here Ráma stands, his heir by birth, Whose name is glorious in the earth: Sure refuge he of all oppressed, Most faithful to his sire's behest. He, Da[aratha's eldest born Whom gifts above the rest adorn, Lord of each high imperial sign,552 The glory of his kingly line, Reft of his right, expelled from home, Came forth with me the woods to roam. And Sítá too, his faithful dame, Forth with her virtuous husband came, Like the sweet light when day is done 550 Bráhmans the sacerdotal caste. Kshatriyas the royal and military, Vai[yas the mercantile, andZúdras the servile. 551 A protracted sacrifice extending over several days. See Book I, p. 24 Note. 552 Possessed of all the auspicious personal marks that indicate capacity of universal sovereignty. See Book I. p. 2, and Note 3.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1181)
- **Original**: Canto IV. Lakshman's Reply. 1163 Still cleaving to her lord the sun. And me his sweet perfections drew To follow as his servant true. Named Lakshma G, brother of my lord Of grateful heart with knowledge stored Most meet is he all bliss to share, Who makes the good of all his care. While, power and lordship cast away, In the wild wood he chose to stay, A giant came,— his name unknown,— And stole the princess left alone. Then Diti's son553 who, cursed of yore, The semblance of a Rákshas wore, To King Sugríva bade us turn The robber's name and home to learn. For he, the Vánar chief, would know The dwelling of our secret foe. Such words of hope spake Diti's son, And sought the heaven his deeds had won. Thou hast my tale. From first to last Thine ears have heard whate'er has past. Ráma the mighty lord and I For refuge to Sugríva fly. The prince whose arm bright glory gained, O'er the whole earth as monarch reigned, And richest gifts to others gave, Is come Sugríva's help to crave; Son of a king the surest friend Of virtue, him who loved to lend His succour to the suffering weak, Is come Sugríva's aid to seek. Yes, Raghu's son whose matchless hand 553 Kabandha. See Book III. Canto LXXIII.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1182)
- **Original**: 1164 The Ramayana Protected all this sea-girt land, The virtuous prince, my holy guide, For refuge seeks Sugríva's side. His favour sent on great and small Should ever save and prosper all. He now to win Sugríva's grace Has sought his woodland dwelling-place.[328] Son of a king of glorious fame;— Who knows not Da[aratha's name?— From whom all princes of the earth Received each honour due to worth;— Heir of that best of earthly kings, Ráma the prince whose glory rings Through realms below and earth and skies, For refuge to Sugríva flies. Nor should the Vánar king refuse The boon for which the suppliant sues, But with his forest legions speed To save him in his utmost need.” Sumitrá's son, his eyes bedewed With piteous tears, thus sighed and sued. Then, trained in all the arts that guide The speaker, Hanumán replied: “Yea, lords like you of wisest thought, Whom happy fate has hither brought, Who vanquish ire and rule each sense, Must of our lord have audience. Reft of his kingdom, sad, forlorn, Once Báli's hate now Báli's scorn, Defeated, severed from his spouse, Wandering under forest boughs, Child of the Sun, our lord and king
- **Translation**: 

---

### Verse 18 (Ramayana 0.1183)
- **Original**: Canto IV. Lakshman's Reply. 1165 Sugríva will his succours bring, And all our Vánar hosts combined Will trace the dame you long to find.” With gentle tone and winning grace Thus spake the chief of Vánar race, And then to Raghu's son he cried: “Come, haste we to Sugríva's side.” He spoke, and for his words so sweet Good Lakshma G paid all honour meet; Then turned and cried to Raghu's son: “Now deem thy task already done, Because this chief of Vánar kind, Son of the God who rules the wind, Declares Sugríva's self would be Assisted in his need by thee. Bright gleams of joy his cheek o'erspread As each glad word of hope he said; And ne'er will one so valiant deign To cheer our hearts with hope in vain.” He spoke, and Hanumán the wise Cast off his mendicant disguise, And took again his Vánar form, Son of the God of wind and storm. High on his ample back in haste Raghu's heroic sons he placed, And turned with rapid steps to find The sovereign of the Vánar kind.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1184)
- **Original**: 1166 The Ramayana Canto V. The League. From Rishyamúka's rugged side To Malaya's hill the Vánar hied, And to his royal chieftain there Announced the coming of the pair: “See, here with LakshmaG Ráma stands Illustrious in a hundred lands. Whose valiant heart will never quail Although a thousand foes assail; King Da[aratha's son, the grace And glory of Ikshváku's race. Obedient to his father's will He cleaves to sacred duty still. With rites of royal pomp and pride His sire the Fire-God gratified; Ten hundred thousand kine he freed, And priests enriched with ample meed; And the broad land protected, famed For truthful lips and passions tamed. Through woman's guile his son has made His dwelling in the forest shade, Where, as he lived with every sense Subdued in hermit abstinence, Fierce RávaG stole his wife, and he Is come a suppliant, lord, to thee. Now let all honour due be paid To these great chiefs who seek thine aid.”
- **Translation**: 

---

### Verse 20 (Ramayana 0.1185)
- **Original**: Canto V. The League. 1167 Thus spake the Vánar prince, and, stirred With friendly thoughts, Sugríva heard. The light of joy his face o'erspread, And thus to Raghu's son he said: “O Prince, in rules of duty trained, Caring for all with love unfeigned, Hanúmán's tongue has truly shown The virtues that are thine alone. My chiefest glory, gain, and bliss, O stranger Prince, I reckon this, That Raghu's son will condescend To seek the Vánar for his friend. If thou my true ally wouldst be Accept the pledge I offer thee, This hand in sign of friendship take, And bind the bond we ne'er will break.” He spoke, and joy thrilled Ráma's breast; Sugríva's hand he seized and pressed And, transport beaming from his eye, Held to his heart his new ally. In wanderer's weed disguised no more, His proper form Hanúmán wore. Then, wood with wood engendering,554 came Neath his deft hands the kindled flame. 554 Fire for sacred purposes is produced by the attrition of two pieces of wood. In marriage and other solemn covenants fire is regarded as the holy witness in whose presence the agreement is made. Spenser in a description of a marriage, has borrowed from the Roman rite what he calls the housling, or“matrimonial rite.” “His owne two hands the holy knots did knit That none but death forever can divide. His owne two hands, for such a turn most fit, The housling fire did kindle and provide.” Faery Queen, Book I. XII.{FNS 37.
- **Translation**: 

---

