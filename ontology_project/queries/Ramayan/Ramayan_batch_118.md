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

### Verse 1 (Ramayana 0.386)
- **Original**: 368 The Ramayana Gave to the bird his flesh and bone, And by his truth made heaven his own.277 Alarka, when a Bráhman famed For Scripture lore his promise claimed, Tore from his head his bleeding eyes And unreluctant gave the prize. His narrow bounds prescribed restrain The Rivers' Lord, the mighty main, Who, though his waters boil and rave, Keeps faithful to the word he gave. Truth all religion comprehends, Through all the world its might extends: In truth alone is justice placed, On truth the words of God are based: A life in truth unchanging past Will bring the highest bliss at last. If thou the right would still pursue, Be constant to thy word and true: Let me thy promise fruitful see, For boons, O King, proceed from thee. Now to preserve thy righteous fame, And yielding to my earnest claim— Thrice I repeat it— send thy child, Thy Ráma, to the forest wild. But if the boon thou still deny, Before thy face, forlorn, I die.” 277 See Additional Notes, THE SUPPLIANT D OVE {FNS .
- **Translation**: 

---

### Verse 2 (Ramayana 0.387)
- **Original**: Canto XIV. Ráma Summoned. 369 Thus was the helpless monarch stung By Queen Kaikeyí's fearless tongue, As Bali strove in vain to loose His limbs from Indra's fatal noose. Dismayed in soul and pale with fear, The monarch, like a trembling steer Between the chariot's wheel and yoke, Again to Queen Kaikeyí spoke, With sad eyes fixt in vacant stare, Gathering courage from despair: “That hand I took, thou sinful dame, With texts, before the sacred flame, Thee and thy son, I scorn and hate, And all at once repudiate. [108] The night is fled: the dawn is near: Soon will the holy priests be here To bid me for the rite prepare That with my son the throne will share, The preparation made to grace My Ráma in his royal place— With this, e'en this, my darling for My death the funeral flood shall pour. Thou and thy son at least forbear In offerings to my shade to share, For by the plot thy guile has laid His consecration will be stayed. This very day how shall I brook To meet each subject's altered look? To mark each gloomy joyless brow That was so bright and glad but now?” While thus the high-souled monarch spoke To the stern queen, the Morning broke, And holy night had slowly fled,
- **Translation**: 

---

### Verse 3 (Ramayana 0.388)
- **Original**: 370 The Ramayana With moon and stars engarlanded. Yet once again the cruel queen Spoke words in answer fierce and keen, Still on her evil purpose bent, Wild with her rage and eloquent: “What speech is this? Such words as these Seem sprung from poison-sown disease. Quick to thy noble Ráma send And bid him on his sire attend. When to my son the rule is given; When Ráma to the woods is driven; When not a rival copes with me, From chains of duty thou art free.” Thus goaded, like a generous steed Urged by sharp spurs to double speed, “My senses are astray,” he cried, “And duty's bonds my hands have tied. I long to see mine eldest son, My virtuous, my beloved one.” And now the night had past away; Out shone the Maker of the Day, Bringing the planetary hour And moment of auspicious power. Va [ishmha, virtuous, far renowned, Whose young disciples girt him round, With sacred things without delay Through the fair city took his way. He traversed, where the people thronged, And all for Ráma's coming longed, The town as fair in festive show As his who lays proud cities low.278 278 Indra, called also Purandara, Town-destroyer.
- **Translation**: 

---

### Verse 4 (Ramayana 0.389)
- **Original**: Canto XIV. Ráma Summoned. 371 He reached the palace where he heard The mingled notes of many a bird, Where crowded thick high-honoured bands Of guards with truncheons in their hands. Begirt by many a sage, elate, Va [ishmha reached the royal gate, And standing by the door he found Sumantra, for his form renowned, The king's illustrious charioteer And noble counsellor and peer. To him well skilled in every part Of his hereditary art Va [ishmha said:“O charioteer, Inform the king that I am here, Here ready by my side behold These sacred vessels made of gold, Which water for the rite contain From Gangá and each distant main. Here for installing I have brought The seat prescribed of fig-wood wrought, All kinds of seed and precious scent And many a gem and ornament; Grain, sacred grass, the garden's spoil, Honey and curds and milk and oil; Eight radiant maids, the best of all War elephants that feed in stall; A four-horse car, a bow and sword. A litter, men to bear their lord; A white umbrella bright and fair That with the moon may well compare; Two chouries of the whitest hair; A golden beaker rich and rare; A bull high-humped and fair to view, Girt with gold bands and white of hue;
- **Translation**: 

---

### Verse 5 (Ramayana 0.390)
- **Original**: 372 The Ramayana A four-toothed steed with flowing mane, A throne which lions carved sustain; A tiger's skin, the sacred fire, Fresh kindled, which the rites require; The best musicians skilled to play, And dancing-girls in raiment gay; Kine, Bráhmans, teachers fill the court, And bird and beast of purest sort. From town and village, far and near, The noblest men are gathered here; Here merchants with their followers crowd, And men in joyful converse loud, And kings from many a distant land To view the consecration stand. The dawn is come, the lucky day; Go bid the monarch haste away, That now Prince Ráma may obtain The empire, and begin his reign.” Soon as he heard the high behest The driver of the chariot pressed Within the chambers of the king, His lord with praises honouring. And none of all the warders checked His entrance for their great respect Of him well known, in place so high, Still fain their king to gratify. He stood beside the royal chief, Unwitting of his deadly grief, And with sweet words began to sing The praises of his lord and king: “As, when the sun begins to rise, The sparkling sea delights our eyes, Wake, calm with gentle soul, and thus[109]
- **Translation**: 

---

### Verse 6 (Ramayana 0.391)
- **Original**: Canto XIV. Ráma Summoned. 373 Give rapture, mighty King, to us. As Mátali279 this selfsame hour Sang lauds of old to Indra's power, When he the Titan hosts o'erthrew, So hymn I thee with praises due. The Vedas, with their kindred lore, Brahmá their soul-born Lord adore, With all the doctrines of the wise, And bid him, as I bid thee, rise. As, with the moon, the Lord of Day Wakes with the splendour of his ray Prolific Earth, who neath him lies, So, mighty King, I bid thee rise. With blissful words, O Lord of men, Rise, radiant in thy form, as when The sun ascending darts his light From Meru's everlasting height. May Ziva, Agni, Sun, and Moon Bestow on thee each choicest boon, Kuvera, VaruGa, Indra bless Kakutstha's son with all success. Awake, the holy night is fled, The happy light abroad is spread; Awake, O best of kings, and share The glorious task that claims thy care. The holy sage Va[ishmha waits, With all his Bráhmans, at the gate. Give thy decree, without delay, To consecrate thy son today. As armies, by no captain led, As flocks that feed unshepherded, Such is the fortune of a state 279 Indra's charioteer.
- **Translation**: 

---

### Verse 7 (Ramayana 0.392)
- **Original**: 374 The Ramayana Without a king and desolate.” Such were the words the bard addressed, With weight of sage advice impressed; And, as he heard, the hapless king Felt deeper yet his sorrow's sting. At length, all joy and comfort fled, He raised his eyes with weeping red, And, mournful for his Ráma's sake, The good and glorious monarch spake: “Why seek with idle praise to greet The wretch for whom no praise is meet? Thy words mine aching bosom tear, And plunge me deeper in despair.” Sumantra heard the sad reply, And saw his master's tearful eye. With reverent palm to palm applied He drew a little space aside. Then, as the king, with misery weak, With vain endeavour strove to speak, Kaikeyí, skilled in plot and plan, To sage Sumantra thus began: “The king, absorbed in joyful thought For his dear son, no rest has sought: Sleepless to him the night has past, And now o'erwatched he sinks at last. Then go, Sumantra, and with speed The glorious Ráma hither lead: Go, as I pray, nor longer wait; No time is this to hesitate.” “How can I go, O Lady fair, Unless my lord his will declare?” “Fain would I see him,” cried the king,
- **Translation**: 

---

### Verse 8 (Ramayana 0.393)
- **Original**: Canto XV. The Preparations. 375 “Quick, quick, my beauteous Ráma bring.” Then rose the happy thought to cheer The bosom of the charioteer, “The king, I ween, of pious mind, The consecration has designed.” Sumantra for his wisdom famed, Delighted with the thought he framed, From the calm chamber, like a bay Of crowded ocean, took his way. He turned his face to neither side, But forth he hurried straight; Only a little while he eyed The guards who kept the gate. He saw in front a gathered crowd Of men of every class, Who, parting as he came, allowed The charioteer to pass. Canto XV. The Preparations. There slept the Bráhmans, deeply read In Scripture, till the night had fled; Then, with the royal chaplains, they Took each his place in long array. There gathered fast the chiefs of trade, Nor peer nor captain long delayed, Assembling all in order due The consecrating rite to view.
- **Translation**: 

---

### Verse 9 (Ramayana 0.394)
- **Original**: 376 The Ramayana The morning dawned with cloudless ray On Pushya's high auspicious day, And Cancer with benignant power Looked down on Ráma's natal hour. The twice-born chiefs, with zealous heed, Made ready what the rite would need. The well-wrought throne of holy wood And golden urns in order stood. There was the royal car whereon A tiger's skin resplendent shone; There water, brought for sprinkling thence Where, in their sacred confluence, Blend Jumná's waves with Gangá's tide, From many a holy flood beside, From brook and fountain far and near, From pool and river, sea and mere. And there were honey, curd, and oil, Parched rice and grass, the garden's spoil, Fresh milk, eight girls in bright attire, An elephant with eyes of fire; And urns of gold and silver made, With milky branches overlaid, All brimming from each sacred flood, And decked with many a lotus bud.[110] And dancing-women fair and free, Gay with their gems, were there to see, Who stood in bright apparel by With lovely brow and witching eye. White flashed the jewelled chouri there, And shone like moonbeams through the air; The white umbrella overhead A pale and moonlike lustre shed, Wont in pure splendour to precede, And in such rites the pomp to lead.
- **Translation**: 

---

### Verse 10 (Ramayana 0.395)
- **Original**: Canto XV. The Preparations. 377 There stood the charger by the side Of the great bull of snow-white hide; There was all music soft and loud, And bards and minstrels swelled the crowd. For now the monarch bade combine Each custom of his ancient line With every rite Ayodhyá's state Observed, her kings to consecrate. Then, summoned by the king's behest, The multitudes together pressed, And, missing still the royal sire, Began, impatient, to inquire: “Who to our lord will tidings bear That all his people throng the square? Where is the king? the sun is bright, And all is ready for the rite.” As thus they spoke, Sumantra, tried In counsel, to the chiefs replied, Gathered from lands on every side: “To Ráma's house I swiftly drave, For so the king his mandate gave. Our aged lord and Ráma too In honour high hold all of you: I in your words (be long your days!) Will ask him why he thus delays.”
- **Translation**: 

---

### Verse 11 (Ramayana 0.396)
- **Original**: 378 The Ramayana Thus spoke the peer in Scripture read, And to the ladies' bower he sped. Quick through the gates Sumantra hied, Which access ne'er to him denied. Behind the curtained screen he drew, Which veiled the chamber from the view. In benediction loud he raised His voice, and thus the monarch praised: “Sun, Moon, Kuvera,Ziva bless Kakutstha's son with high success! The Lords of air, flood, fire decree The victory, my King, to thee! The holy night has past away, Auspicious shines the morning's ray. Rise, Lord of men, thy part to take In the great rite. Awake! awake! Bráhmans and captains, chiefs of trade, All wait in festive garb arrayed; For thee they look with eager eyes: O Raghu's son, awake! arise.” To him in holy Scripture read, Who hailed him thus, the monarch said, Upraising from his sleep his head: “Go, Ráma, hither lead as thou Wast ordered by the queen but now. Come, tell me why my mandate laid Upon thee thus is disobeyed. Away! and Ráma hither bring; I sleep not: make no tarrying.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.397)
- **Original**: Canto XV. The Preparations. 379 Thus gave the king command anew: Sumantra from his lord withdrew; With head in lowly reverence bent, And filled with thoughts of joy, he went. The royal street he traversed, where Waved flag and pennon to the air, And, as with joy the car he drove, He let his eyes delighted rove. On every side, where'er he came, He heard glad words, their theme the same, As in their joy the gathered folk Of Ráma and the throning spoke. Then saw he Ráma's palace bright And vast as Mount Kailása's height, That glorious in its beauty showed As Indra's own supreme abode: With folding doors both high and wide; With hundred porches beautified: Where golden statues towering rose O'er gemmed and coralled porticoes. Bright like a cave in Meru's side, Or clouds through Autumn's sky that ride: Festooned with length of bloomy twine, Flashing with pearls and jewels' shine, While sandal-wood and aloe lent The mingled riches of their scent; With all the odorous sweets that fill The breezy heights of Dardar's hill. There by the gate the Sáras screamed, And shrill-toned peacocks' plumage gleamed. Its floors with deftest art inlaid, Its sculptured wolves in gold arrayed, With its bright sheen the palace took The mind of man and chained the look,
- **Translation**: 

---

### Verse 13 (Ramayana 0.398)
- **Original**: 380 The Ramayana For like the sun and moon it glowed, And mocked Kuvera's loved abode. Circling the walls a crowd he viewed Who stood in reverent attitude, With throngs of countrymen who sought Acceptance of the gifts they brought. The elephant was stationed there, Appointed Ráma's self to bear; Adorned with pearls, his brow and cheek Were sandal-dyed in many a streak, While he, in stature, bulk, and pride, With Indra's own Airávat280 vied. Sumantra, borne by coursers fleet, Flashing a radiance o'er the street, To Ráma's palace flew, And all who lined the royal road, Or thronged the prince's rich abode, Rejoiced as near he drew. And with delight his bosom swelled As onward still his course he held[111] Through many a sumptuous court Like Indra's palace nobly made, Where peacocks revelled in the shade, And beasts of silvan sort. Through many a hall and chamber wide, That with Kailása's splendour vied. Or mansions of the Blest, While Ráma's friends, beloved and tried, Before his coming stepped aside, Still on Sumantra pressed. He reached the chamber door, where stood Around his followers young and good, 280 The elephant of Indra.
- **Translation**: 

---

### Verse 14 (Ramayana 0.399)
- **Original**: Canto XVI. Ráma Summoned. 381 Bard, minstrel, charioteer, Well skilled the tuneful chords to sweep, With soothing strain to lull to sleep, Or laud their master dear. Then, like a dolphin darting through Unfathomed depths of ocean's blue With store of jewels decked, Through crowded halls that rock-like rose, Or as proud hills where clouds repose, Sumantra sped unchecked— Halls like the glittering domes on high Reared for the dwellers of the sky By heavenly architect. Canto XVI. Ráma Summoned. So through the crowded inner door Sumantra, skilled in ancient lore, On to the private chambers pressed Which stood apart from all the rest. There youthful warriors, true and bold, Whose ears were ringed with polished gold, All armed with trusty bows and darts, Watched with devoted eyes and hearts. And hoary men, a faithful train, Whose aged hands held staves of cane, The ladies' guard, apparelled fair In red attire, were stationed there. Soon as they saw Sumantra nigh, Each longed his lord to gratify, And from his seat beside the door
- **Translation**: 

---

### Verse 15 (Ramayana 0.400)
- **Original**: 382 The Ramayana Up sprang each ancient servitor. Then to the warders quickly cried The skilled Sumantra, void of pride: “Tell Ráma that the charioteer Sumantra waits for audience here.” The ancient men with one accord Seeking the pleasure of their lord, Passing with speed the chamber door To Ráma's ear the message bore. Forthwith the prince with duteous heed Called in the messenger with speed, For 'twas his sire's command, he knew, That sent him for the interview. Like Lord Kuvera, well arrayed, He pressed a couch of gold, Wherefrom a covering of brocade Hung down in many a fold. Oil and the sandal's fragrant dust Had tinged his body o'er Dark as the stream the spearman's thrust Drains from the wounded boar. Him Sítá watched with tender care, A chouri in her hand, As Chitrá,281 ever fond in fair, Beside the Moon will stand. Him glorious with unborrowed light, A liberal lord, of sunlike might, Sumantra hailed in words like these, Well skilled in gentle courtesies, As, with joined hands in reverence raised, Upon the beauteous prince he gazed: “Happy Kau[alyá! Blest is she, 281 A star in the spike of Virgo: hence the name of the mouth Chaitra or Chait.
- **Translation**: 

---

### Verse 16 (Ramayana 0.401)
- **Original**: Canto XVI. Ráma Summoned. 383 The Mother of a son like thee. Now rise, O Ráma, speed away. Go to thy sire without delay: For he and Queen Kaikeyí seek An interview with thee to speak.” The lion-lord of men, the best Of splendid heroes, thus addressed, To Sítá spake with joyful cheer: “The king and queen, my lady dear, Touching the throning, for my sake Some salutary counsel take. The lady of the full black eye Would fain her husband gratify, And, all his purpose understood, Counsels the monarch to my good. A happy fate is mine, I ween, When he, consulting with his queen, Sumantra on this charge, intent Upon my gain and good, has sent. An envoy of so noble sort Well suits the splendour of the court. The consecration rite this day Will join me in imperial sway. To meet the lord of earth, for so His order bids me, I will go. Thou, lady, here in comfort stay, And with thy maidens rest or play.”
- **Translation**: 

---

### Verse 17 (Ramayana 0.402)
- **Original**: 384 The Ramayana Thus Ráma spake. For meet reply The lady of the large black eye Attended to the door her lord, And blessings on his head implored: “The majesty and royal state Which holy Bráhmans venerate, The consecration and the rite Which sanctifies the ruler's might, And all imperial powers should be Thine by thy father's high decree, As He, the worlds who formed and planned, The kingship gave to Indra's hand.[112] Then shall mine eyes my king adore When lustral rites and fast are o'er, And black deer's skin and roebuck's horn Thy lordly limbs and hand adorn. May He whose hands the thunder wield Be in the east thy guard and shield; May Yáma's care the south befriend, And VaruG's arm the west defend; And let Kuvera, Lord of Gold, The north with firm protection hold.” Then Ráma spoke a kind farewell, And hailed the blessings as they fell From Sítá's gentle lips; and then, As a young lion from his den Descends the mountain's stony side, So from the hall the hero hied. First LakshmaG at the door he viewed Who stood in reverent attitude, Then to the central court he pressed Where watched the friends who loved him best. To all his dear companions there
- **Translation**: 

---

### Verse 18 (Ramayana 0.403)
- **Original**: Canto XVI. Ráma Summoned. 385 He gave kind looks and greeting fair. On to the lofty car that glowed Like fire the royal tiger strode. Bright as himself its silver shone: A tiger's skin was laid thereon. With cloudlike thunder, as it rolled, It flashed with gems and burnished gold, And, like the sun's meridian blaze, Blinded the eye that none could gaze. Like youthful elephants, tall and strong, Fleet coursers whirled the car along: In such a car the Thousand-eyed Borne by swift horses loves to ride. So like Parjanya,282 when he flies Thundering through the autumn skies, The hero from the palace sped, As leaves the moon some cloud o'erhead. Still close to Ráma LakshmaG kept, Behind him to the car he leapt, And, watching with fraternal care, Waved the long chouri's silver hair, As from the palace gate he came Up rose the tumult of acclaim. While loud huzza and jubilant shout Pealed from the gathered myriads out. Then elephants, like mountains vast, And steeds who all their kind surpassed, Followed their lord by hundreds, nay By thousands, led in long array. First marched a band of warriors trained, With sandal dust and aloe stained; Well armed was each with sword and bow, 282 The Rain-God.
- **Translation**: 

---

### Verse 19 (Ramayana 0.404)
- **Original**: 386 The Ramayana And every breast with hope aglow, And ever, as they onward went, Shouts from the warrior train, And every sweet-toned instrument Prolonged the minstrel strain. On passed the tamer of his foes, While well clad dames, in crowded rows, Each chamber lattice thronged to view, And chaplets on the hero threw. Then all, of peerless face and limb, Sang Ráma's praise for love of him, And blent their voices, soft and sweet, From palace high and crowded street: “Now, sure, Kau[alyá's heart must swell To see the son she loves so well, Thee Ráma, thee, her joy and pride, Triumphant o'er the realm preside.” Then— for they knew his bride most fair Of all who part the soft dark hair, His love, his life, possessed the whole Of her young hero's heart and soul:— “Be sure the lady's fate repays Some mighty vow of ancient days,283 For blest with Ráma's love is she As, with the Moon's, sweet Rohiní.”284 Such were the witching words that came From lips of many a peerless dame Crowding the palace roofs to greet The hero as he gained the street. 283 In a former life. 284 One of the lunar asterisms, represented as the favourite wife of the Moon. See p. 4, note.
- **Translation**: 

---

### Verse 20 (Ramayana 0.405)
- **Original**: Canto XVII. Ráma's Approach. 387 Canto XVII. Ráma's Approach. As Ráma, rendering blithe and gay His loving friends, pursued his way, He saw on either hand a press Of mingled people numberless. The royal street he traversed, where Incense of aloe filled the air, Where rose high palaces, that vied With paly clouds, on either side; With flowers of myriad colours graced. And food for every varied taste, Bright as the glowing path o'erhead Which feet of Gods celestial tread, Loud benedictions, sweet to hear, From countless voices soothed his ear. While he to each gave due salute His place and dignity to suit: “Be thou,” the joyful people cried, “Be thou our guardian, lord and guide. Throned and anointed king to-day, Thy feet set forth upon the way Wherein, each honoured as a God, Thy fathers and forefathers trod. Thy sire and his have graced the throne, And loving care to us have shown: Thus blest shall we and ours remain, Yea still more blest in Ráma's reign. [113] No more of dainty fare we need, And but one cherished object heed, That we may see our prince today Invested with imperial sway.”
- **Translation**: 

---

