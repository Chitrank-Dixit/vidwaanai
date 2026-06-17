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

### Verse 1 (Ramayan 0.1161)
- **Original**: Canto I. Ráma's Lament. 1143 The swan's and mallard's loved retreat, Shows her glad waters bright and clear, Where lotuses their heads uprear From the pure wave, and charm the view With mingled tints of red and blue. Each like the morning's early beams Reflected in the crystal gleams; And bees on their sweet toil intent Weigh down each tender filament. There with gay lawns the wood recedes; There wildfowl sport amid the reeds, There roedeer stand upon the brink, And elephants descend to drink. The rippling waves which winds make fleet Against the bending lilies beat, And opening bud and flower and stem Gleam with the drops that hang on them. Life has no pleasure left for me While my dear queen I may not see, [322] Who loved so well those blooms that vie With the full splendour of her eye. O tyrant Love, who will not let My bosom for one hour forget The lost one whom I yearn to meet, Whose words were ever kind and sweet. Ah, haply might my heart endure This hopeless love that knows not cure, If spring with all his trees in flower Assailed me not with ruthless power. Each lovely scene, each sound and sight Wherein, with her, I found delight, Has lost the charm so sweet of yore, And glads my widowed heart no more. On lotus buds I seem to gaze,
- **Translation**: 

---

### Verse 2 (Ramayan 0.1162)
- **Original**: 1144 The Ramayana Or blooms that deck Palá[a532 sprays;533 But to my tortured memory rise The glories of my darling's eyes. Cool breezes through the forest stray Gathering odours on their way, Enriched with all the rifled scent Of lotus flower and filament. Their touch upon my temples falls And Sítá's fragrant breath recalls. Now look, dear brother, on the right Of Pampá towers a mountain height Where fairest Cassia trees unfold The treasures of their burnished gold. Proud mountain king! his woody side With myriad ores is decked and dyed, And as the wind-swept blossoms fall Their fragrant dust is stained with all. To yon high lands thy glances turn: With pendent fire they flash and burn, Where in their vernal glory blaze Palá[a flowers on leafless sprays. O Lakshma G, look! on Pampá's side What fair trees rise in blooming pride! 532 Butea Frondosa. A tree that bears a profusion of brilliant red flowers which appear before the leaves. 533 I omit five[lokaswhich contain nothing but a list of trees for which, with one or two exceptions, there are no equivalent names in English. The following is Gorresio's translation of the corresponding passage in the Bengal recension:— “Oh come risplendono in questa stagione di primavera i vitici, le galedupe, le bassie, le dalbergie, i diospyri… le tile, le michelie, le rottlerie, le pentaptere ed i pterospermi, i bombaci, le grislee, gli abri, gli amaranti e le dalbergie; i sirii, le galedupe, le barringtonie ed i palmizi, i xanthocymi, il pepebetel, le verbosine e le ticaie, le nauclee le erythrine, gli asochi, e le tapie fanno d'ogni intorno pompa de' lor fiori.”
- **Translation**: 

---

### Verse 3 (Ramayan 0.1163)
- **Original**: Canto I. Ráma's Lament. 1145 What climbing plants above them show Or hang their flowery garlands low! See how the amorous creeper rings The wind-rocked trees to which she clings, As though a dame by love impelled With clasping arms her lover held. Drunk with the varied scents that fill The balmy air, from hill to hill, From grove to grove, from tree to tree, The joyous wind is wandering free. These gay trees wave their branches bent By blooms, of honey redolent. There, slowly opening to the day, Buds with dark lustre deck the spray. The wild bee rests a moment where Each tempting flower is sweet and fair, Then, coloured by the pollen dyes, Deep in some odorous blossom lies. Soon from his couch away he springs: To other trees his course he wings, And tastes the honeyed blooms that grow Where Pampá's lucid waters flow. See, LakshmaG, see, how thickly spread With blossoms from the trees o'erhead, That grass the weary traveller woos With couches of a thousand hues, And beds on every height arrayed With red and yellow tints are laid, No longer winter chills the earth: A thousand flowerets spring to birth, And trees in rivalry assume Their vernal garb of bud and bloom. How fair they look, how bright and gay With tasselled flowers on every spray!
- **Translation**: 

---

### Verse 4 (Ramayan 0.1164)
- **Original**: 1146 The Ramayana While each to each proud challenge flings Borne in the song the wild bee sings. That mallard by the river edge Has bathed amid the reeds and sedge: Now with his mate he fondly plays And fires my bosom as I gaze. Mandákiní534 is far renowned: No lovelier flood on earth is found; But all her fairest charms combined In this sweet stream enchant the mind. O, if my love were here to look With me upon this lovely brook, Never for Ayodhyá would I pine, Or wish that Indra's lot were mine. If by my darling's side I strayed O'er the soft turf which decks the glade, Each craving thought were sweetly stilled, Each longing of my soul fulfilled. But, now my love is far away, Those trees which make the woods so gay, In all their varied beauty dressed, Wake thoughts of anguish in my breast. That lotus-covered stream behold Whose waters run so fresh and cold,[323] 534 A sacred stream often mentioned in the course of the poem. See Book II, Canto XCV.
- **Translation**: 

---

### Verse 5 (Ramayan 0.1165)
- **Original**: Canto I. Ráma's Lament. 1147 Sweet rill, the wildfowl's loved resort, Where curlew, swan, and diver sport; Where with his consort plays the drake, And tall deer love their thirst to slake, While from each woody bank is heard The wild note of each happy bird. The music of that joyous quire Fills all my soul with soft desire; And, as I hear, my sad thoughts fly To Sítá of the lotus eye, Whom, lovely with her moonbright cheek, In vain mine eager glances seek. Now turn, those chequered lawns survey Where hart and hind together stray. Ah, as they wander at their will My troubled breast with grief they fill, While torn by hopeless love I sigh For Sítá of the fawn-like eye. If in those glades where, touched by spring, Gay birds their amorous ditties sing, Mine own beloved I might see, Then, brother, it were well with me: If by my side she wandered still, And this cool breeze that stirs the rill Touched with its gentle breath the brows Of mine own dear Videhan spouse. For, LakshmaG, O how blest are those On whom the breath of Pampá blows, Dispelling all their care and gloom With sweets from where the lilies bloom! How can my gentle love remain Alive amid the woe and pain, Where prisoned far away she lies,— My darling of the lotus eyes?
- **Translation**: 

---

### Verse 6 (Ramayan 0.1166)
- **Original**: 1148 The Ramayana How shall I dare her sire to greet Whose lips have never known deceit? How stand before the childless king And meet his eager questioning? When banished by my sire's decree, In low estate, she followed me. So pure, so true to every vow, Where is my gentle darling now? How can I bear my widowed lot, And linger on where she is not, Who followed when from home I fled Distracted, disinherited? My spirit sinks in hopeless pain When my fond glances yearn in vain For that dear face with whose bright eye The worshipped lotus scarce can vie. Ah when, my brother, shall I hear That voice that rang so soft and clear, When, sweetly smiling as she spoke, From her dear lips gay laughter broke? When worn with toil and love I strayed With Sítá through the forest shade, No trace of grief was seen in her, My kind and thoughtful comforter. How shall my faltering tongue relate To Queen Kau[alyá Sítá's fate? How answer when in wild despair She questions, Where is Sítá, where? Haste, brother, haste: to Bharat hie, On whose fond love I still rely. My life can be no longer borne, Since Sítá from my side is torn.”
- **Translation**: 

---

### Verse 7 (Ramayan 0.1167)
- **Original**: Canto I. Ráma's Lament. 1149 Thus like a helpless mourner, bent By sorrow, Ráma made lament; And with wise counsel LakshmaG tried To soothe his care, and thus replied: “O best of men, thy grief oppose, Nor sink beneath thy weight of woes. Not thus despond the great and pure And brave like thee, but still endure. Reflect what anguish wrings the heart When loving souls are forced to part; And, mindful of the coming pain, Thy love within thy breast restrain. For earth, though cooled by wandering streams, Lies scorched beneath the midday beams. RávaG his steps to hell may bend, Or lower yet in flight descend; But be thou sure, O Raghu's son, Avenging death he shall not shun. Rise, Ráma, rise: the search begin, And track the giant foul with sin. Then shall the fiend, though far he fly, Resign his prey or surely die. Yea, though the trembling monster hide With Sítá close to Diti's535 side, E'en there, unless he yield the prize, Slain by this wrathful hand he dies. Thy heart with strength and courage stay, And cast this weakling mood away. Our fainting hopes in vain revive Unless with firm resolve we strive. The zeal that fires the toiler's breast 535 A daughter of Daksha who became one of the wives of Ka[yapa and mother of the Daityas. She is termed the general mother of Titans and malignant beings. See Book I Cantos XLV, XLVI.
- **Translation**: 

---

### Verse 8 (Ramayan 0.1168)
- **Original**: 1150 The Ramayana Mid earthly powers is first and best. Zeal every check and bar defies, And wins at length the loftiest prize, In woe and danger, toil and care, Zeal never yields to weak despair. With zealous heart thy task begin, And thou once more thy spouse shalt win. Cast fruitless sorrow from thy soul, Nor let this love thy heart control. Forget not all thy sacred lore, But be thy noble self once more.” He heard, his bosom rent by grief, The counsel of his brother chief; Crushed in his heart the maddening pain, And rose resolved and strong again. Then forth upon his journey went The hero on his task intent, Nor thought of Pampá's lovely brook,[324] Or trees which murmuring breezes shook, Though on dark woods his glances fell, On waterfall and cave and dell; And still by many a care distressed The son of Raghu onward pressed. As some wild elephant elate Moves through the woods in pride, So LakshmaG with majestic gait Strode by his brother's side. He, for his lofty spirit famed, Admonished and consoled; Showed Raghu's son what duty claimed, And bade his heart be bold. Then as the brothers strode apace To Rishyamúka's height,
- **Translation**: 

---

### Verse 9 (Ramayan 0.1169)
- **Original**: Canto II. Sugríva's Alarm. 1151 The sovereign of the Vánar race536 Was troubled at the sight. As on the lofty hill he strayed He saw the chiefs draw near: A while their glorious forms surveyed, And mused in restless fear. His slow majestic step he stayed And gazed upon the pair. And all his spirit sank dismayed By fear too great to bear. When in their glorious might the best Of royal chiefs came nigh, The Vánars in their wild unrest Prepared to turn and fly. They sought the hermit's sacred home537 For peace and bliss ordained, And there, where Vánars loved to roam, A sure asylum gained. Canto II. Sugríva's Alarm. Sugríva moved by wondering awe The high-souled sons of Raghu saw, In all their glorious arms arrayed; And grief upon his spirit weighed. 536 Sugríva, the ex-king of the Vánars, foresters, or monkeys, an exile from his home, wandering about the mountain Rishyamúka with his four faithful ex-ministers. 537 The hermitage of the Saint Matanga which his curse prevented Báli, the present king of the Vánars, from entering. The story is told at length in Canto XI of this Book.
- **Translation**: 

---

### Verse 10 (Ramayan 0.1170)
- **Original**: 1152 The Ramayana To every quarter of the sky He turned in fear his anxious eye, And roving still from spot to spot With troubled steps he rested not. He durst not, as he viewed the pair, Resolve to stand and meet them there; And drooping cheer and quailing breast The terror of the chief confessed. While the great fear his bosom shook, Brief counsel with his lords he took; Each gain and danger closely scanned, What hope in flight, what power to stand, While doubt and fear his bosom rent, On Raghu's sons his eyes he bent, And with a spirit ill at ease Addressed his lords in words like these: “Those chiefs with wandering steps invade The shelter of our pathless shade, And hither come in fair disguise Of hermit garb as Báli's spies.” Each lord beheld with troubled heart Those masters of the bowman's art, And left the mountain side to seek Sure refuge on a loftier peak. The Vánar chief in rapid flight Found shelter on a towering height, And all the band with one accord Were closely gathered round their lord. Their course the same, with desperate leap Each made his way from steep to steep, And speeding on in wild career Filled every height with sudden fear.
- **Translation**: 

---

### Verse 11 (Ramayan 0.1171)
- **Original**: Canto II. Sugríva's Alarm. 1153 Each heart was struck with mortal dread, As on their course the Vánars sped, While trees that crowned the steep were bent And crushed beneath them as they went. As in their eager flight they pressed For safety to each mountain crest, The wild confusion struck with fear Tiger and cat and wandering deer. The lords who watched Sugríva's will Were gathered on the royal hill, And all with reverent hands upraised Upon their king and leader gazed. Sugríva feared some evil planned, Some train prepared by Báli's hand. But, skilled in words that charm and teach, Thus Hanumán 538 began his speech: “Dismiss, dismiss thine idle fear, Nor dread the power of Báli here. For this is Malaya's glorious hill539 Where Báli's might can work no ill. I look around but nowhere see The hated foe who made thee flee, Fell Báli, fierce in form and face: Then fear not, lord of Vánar race. Alas, in thee I clearly find The weakness of the Vánar kind, [325] That loves from thought to thought to range, Fix no belief and welcome change. Mark well each hint and sign and scan, Discreet and wise, thine every plan. 538 Hanumán, Sugríva's chief general, was the son of the God of Wind. See Book I, Canto XVI. 539 A range of hills in Malabar; the Western Ghats in the Deccan.
- **Translation**: 

---

### Verse 12 (Ramayan 0.1172)
- **Original**: 1154 The Ramayana How may a king, with sense denied, The subjects of his sceptre guide?” Hanúmán, 540 wise in hour of need, Urged on the chief his prudent rede. His listening ear Sugríva bent, And spake in words more excellent: “Where is the dauntless heart that free From terror's chilling touch can see Two stranger warriors, strong as those, Equipped with swords and shafts and bows, With mighty arms and large full eyes, Like glorious children of the skies? Báli my foe, I ween, has sent These chiefs to aid his dark intent. Hence doubt and fear disturb me still, For thousands serve a monarch's will, In borrowed garb they come, and those Who walk disguised are counted foes. With secret thoughts they watch their time, And wound fond hearts that fear no crime. My foe in state affairs is wise, And prudent kings have searching eyes. By other hands they strike the foe: By meaner tools the truth they know. Now to those stranger warriors turn, And, less than king, their purpose learn. Mark well the trick and look of each; Observe his form and note his speech. With care their mood and temper sound, 540 Válmíki makes the second vowel in this name long or short to suit the exigencies of the verse. Other Indian poets have followed his example, and the same licence will be used in this translation.
- **Translation**: 

---

### Verse 13 (Ramayan 0.1173)
- **Original**: Canto III. Hanumán's Speech. 1155 And, if their minds be friendly found, With courteous looks and words begin Their confidence and love to win. Then as my friend and envoy speak, And question what the strangers seek. Ask why equipped with shaft and bow Through this wild maze of wood they go. If they, O chief, at first appear Pure of all guile, in heart sincere, Detect in speech and look the sin And treachery that lurk within.” He spoke: the Wind-God's son obeyed. With ready zeal he sought the shade, And reached with hasty steps the wood Where Raghu's son and LakshmaG stood.541 Canto III. Hanumán's Speech. The envoy in his faithful breast Pondered Sugríva's high behest. From Rishyamúka's peak he hied And placed him by the princes' side. The Wind-God's son with cautious art Had laid his Vánar form apart, And wore, to cheat the strangers eyes, 541 I omit a recapitulatory and interpolated verse in a different metre, which is as follows:— Reverencing with the words, So be it, the speech of the greatly terrified and unequalled monkey king, the magnanimous Hanumán then went where (stood) the very mighty Ráma with LakshmaG.
- **Translation**: 

---

### Verse 14 (Ramayan 0.1174)
- **Original**: 1156 The Ramayana A wandering mendicant's disguise.542 Before the heroes' feet he bent And did obeisance reverent, And spoke, the glorious pair to praise, His words of truth in courteous phrase, High honour duly paid, the best Of all the Vánar kind addressed, With free accord and gentle grace, Those glories of their warrior race: “O hermits, blest in vows, who shine Like royal saints or Gods divine, O best of young ascetics, say How to this spot you found your way, Scaring the troops of wandering deer And silvan things that harbour here Searching amid the trees that grow Where Pampá's gentle waters flow. And lending from your brows a gleam Of glory to the lovely stream. Who are you, say, so brave and fair, Clad in the bark which hermits wear? I see you heave the frequent sigh, I see the deer before you fly. While you, for strength and valour dread, The earth, like lordly lions, tread, Each bearing in his hand a bow, Like Indra's own, to slay the foe. With the grand paces of a bull, 542 The semi divine Hanumán possesses, like the Gods and demons, the power of wearing all shapes at will. He is one of theKámarúpís. Like Milton's good and bad angels“as they please They limb themselves, and colour, shape, or size Assume as likes them best, condense or rare.”
- **Translation**: 

---

### Verse 15 (Ramayan 0.1175)
- **Original**: Canto III. Hanumán's Speech. 1157 So bright and young and beautiful. The mighty arms you raise appear Like trunks which elephants uprear, And as you move this mountain-king543 Is glorious with the light you bring. How have you reached, like Gods in face, Best lords of earth, this lonely place, [326] With tresses coiled in hermit guise,544 And splendours of those lotus eyes? As Gods who leave their heavenly sphere, Alike your beauteous forms appear. The Lords of Day and Night545 might thus Stray from the skies to visit us. Heroic youth, so broad of chest, Fair with the beauty of the Blest, With lion shoulders, tall and strong, Like bulls who lead the lowing throng, Your arms, unmatched for grace and length, With massive clubs may vie in strength. Why do no gauds those limbs adorn Where priceless gems were meetly worn? Each noble youth is fit, I deem, To guard this earth, as lord supreme, With all her woods and seas, to reign From Meru's peak to Vindhya's chain. Your smooth bows decked with dyes and gold Are glorious in their masters' hold, And with the arms of Indra546 vie Which diamond splendours beautify. 543 Himálaya is of coursepar excellencethe Monarch of mountains, but the complimentary title is frequently given to other hills as here to Malaya. 544 Twisted up in a matted coil as was the custom of ascetics. 545 The sun and moon. 546 The rainbow.
- **Translation**: 

---

### Verse 16 (Ramayan 0.1176)
- **Original**: 1158 The Ramayana Your quivers glow with golden sheen, Well stored with arrows fleet and keen, Each gleaming like a fiery snake That joys the foeman's life to take. As serpents cast their sloughs away And all their new born sheen display, So flash your mighty swords inlaid With burning gold on hilt and blade. Why are you silent, heroes? Why My questions hear nor deign reply? Sugríva, lord of virtuous mind, The foremost of the Vánar kind, An exile from his royal state, Roams through the land disconsolate. I, Hanumán, of Vánar race, Sent by the king have sought this place, For he, the pious, just, and true, In friendly league would join with you. Know, godlike youths, that I am one Of his chief lords, the Wind-God's son. With course unchecked I roam at will, And now from Rishyamúka's hill, To please his heart, his hope to speed, I came disguised in beggar's weed.” Thus Hanúmán, well trained in lore Of language, spoke, and said no more. The son of Raghu joyed to hear The envoy's speech, and bright of cheer He turned to LakshmaG by his side, And thus in words of transport cried:
- **Translation**: 

---

### Verse 17 (Ramayan 0.1177)
- **Original**: Canto III. Hanumán's Speech. 1159 “The counselor we now behold Of King Sugríva righteous-souled. His face I long have yearned to see, And now his envoy comes to me With sweetest words in courteous phrase Answer this mighty lord who slays His foemen, by Sugríva sent, This Vánar chief most eloquent. For one whose words so sweetly flow The whole Rig-veda547 needs must know, And in his well-trained memory store The Yajush and the Sáman's lore. He must have bent his faithful ear All grammar's varied rules to hear. For his long speech how well he spoke! In all its length no rule he broke. In eye, on brow, in all his face The keenest look no guile could trace. No change of hue, no pose of limb Gave sign that aught was false in him. Concise, unfaltering, sweet and clear, Without a word to pain the ear. From chest to throat, nor high nor low, His accents came in measured flow. How well he spoke with perfect art That wondrous speech that charmed the heart, With finest skill and order graced In words that knew nor pause nor haste! That speech, with consonants that spring From the three seats of uttering,548 547 The Vedas are four in number, the Rich or Rig-veda, the Yajush or Yajur- veda; the Sáman or Sáma-veda, and the Atharvan or Atharva-veda. See p. 3. Note. 548 The chest, the throat, and the head.
- **Translation**: 

---

### Verse 18 (Ramayan 0.1178)
- **Original**: 1160 The Ramayana Would charm the spirit of a foe Whose sword is raised for mortal blow. How may a ruler's plan succeed Who lacks such envoy good at need? How fail, if one whose mind is stored With gifts so rare assist his lord? What plans can fail, with wisest speech Of envoy's lips to further each?” Thus Ráma spoke; and LakshmaG taught In all the art that utters thought, To King Sugríva's learned spy Thus made his eloquent reply: “Full well we know the gifts that grace Sugríva, lord of Vánar race, And hither turn our wandering feet That we that high-souled king may meet. So now our pleasant task shall be To do the words he speaks by thee.” His prudent speech the Vánar heard, And all his heart with joy was stirred. And hope that league with them would bring Redress and triumph to his king. [327] Canto IV. Lakshman's Reply.
- **Translation**: 

---

### Verse 19 (Ramayan 0.1179)
- **Original**: Canto IV. Lakshman's Reply. 1161 Cheered by the words that Ráma spoke, Joy in the Vánar's breast awoke, And, as his friendly mood he knew, His thoughts to King Sugríva flew: “Again,” he mused,“my high-souled lord Shall rule, to kingly state restored; Since one so mighty comes to save, And freely gives the help we crave.” Then joyous Hanumán, the best Of all the Vánar kind, addressed These words to Ráma, trained of yore In all the arts of speakers' lore:549 “Why do your feet this forest tread By silvan life inhabited, This awful maze of tree and thorn Which Pampá's flowering groves adorn?” 549 “In our own metrical romances, or wherever a poem is meant not for readers but for chanters and oral reciters, theseformulæ, to meet the same recurring case, exist by scores. Thus every woman in these metrical romances who happens to be young, is described as‘so bright of ble,’or complexion; always a man goes‘the mountenance of a mile’ before he overtakes or is overtaken. And so on through a vast bead-roll of cases. In the same spirit Homer has his eternalÄ¿½ ´'±Á'QÀ¿´Á± ¹´É½, orÄ¿½ ´'±À±¼µ¹²¿¼µ½¿Â ÀÁ¿ÃÆ·, &c. To a reader of sensibility, such recurrences wear an air of child-like sim- plicity, beautifully recalling the features of Homer's primitive age. But they would have appeared faults to all commonplace critics in literary ages.” D E Q UINCEY {FNS .Homer and the Homeridæ.
- **Translation**: 

---

### Verse 20 (Ramayan 0.1180)
- **Original**: 1162 The Ramayana He spoke: obedient to the eye Of Ráma, LakshmaG made reply, The name and fortune to unfold Of Raghu's son the lofty-souled: “True to the law, of fame unstained, The glorious Da[aratha reigned, And, steadfast in his duty, long Kept the four castes550 from scathe and wrong. Through his wide realm his will was done, And, loved by all, he hated none. Just to each creature great and small, Like the Good Sire he cared for all. The Ágnishmom,551 as priests advised, And various rites he solemnized, Where ample largess ever paid The Bráhmans for their holy aid. Here Ráma stands, his heir by birth, Whose name is glorious in the earth: Sure refuge he of all oppressed, Most faithful to his sire's behest. He, Da[aratha's eldest born Whom gifts above the rest adorn, Lord of each high imperial sign,552 The glory of his kingly line, Reft of his right, expelled from home, Came forth with me the woods to roam. And Sítá too, his faithful dame, Forth with her virtuous husband came, Like the sweet light when day is done 550 Bráhmans the sacerdotal caste. Kshatriyas the royal and military, Vai[yas the mercantile, andZúdras the servile. 551 A protracted sacrifice extending over several days. See Book I, p. 24 Note. 552 Possessed of all the auspicious personal marks that indicate capacity of universal sovereignty. See Book I. p. 2, and Note 3.
- **Translation**: 

---

