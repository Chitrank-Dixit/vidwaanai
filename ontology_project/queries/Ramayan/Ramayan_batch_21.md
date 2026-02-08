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

### Verse 1 (Ramayan 0.401)
- **Original**: Canto XVI. Ráma Summoned. 383 The Mother of a son like thee. Now rise, O Ráma, speed away. Go to thy sire without delay: For he and Queen Kaikeyí seek An interview with thee to speak.” The lion-lord of men, the best Of splendid heroes, thus addressed, To Sítá spake with joyful cheer: “The king and queen, my lady dear, Touching the throning, for my sake Some salutary counsel take. The lady of the full black eye Would fain her husband gratify, And, all his purpose understood, Counsels the monarch to my good. A happy fate is mine, I ween, When he, consulting with his queen, Sumantra on this charge, intent Upon my gain and good, has sent. An envoy of so noble sort Well suits the splendour of the court. The consecration rite this day Will join me in imperial sway. To meet the lord of earth, for so His order bids me, I will go. Thou, lady, here in comfort stay, And with thy maidens rest or play.”
- **Translation**: 

---

### Verse 2 (Ramayan 0.402)
- **Original**: 384 The Ramayana Thus Ráma spake. For meet reply The lady of the large black eye Attended to the door her lord, And blessings on his head implored: “The majesty and royal state Which holy Bráhmans venerate, The consecration and the rite Which sanctifies the ruler's might, And all imperial powers should be Thine by thy father's high decree, As He, the worlds who formed and planned, The kingship gave to Indra's hand.[112] Then shall mine eyes my king adore When lustral rites and fast are o'er, And black deer's skin and roebuck's horn Thy lordly limbs and hand adorn. May He whose hands the thunder wield Be in the east thy guard and shield; May Yáma's care the south befriend, And VaruG's arm the west defend; And let Kuvera, Lord of Gold, The north with firm protection hold.” Then Ráma spoke a kind farewell, And hailed the blessings as they fell From Sítá's gentle lips; and then, As a young lion from his den Descends the mountain's stony side, So from the hall the hero hied. First LakshmaG at the door he viewed Who stood in reverent attitude, Then to the central court he pressed Where watched the friends who loved him best. To all his dear companions there
- **Translation**: 

---

### Verse 3 (Ramayan 0.403)
- **Original**: Canto XVI. Ráma Summoned. 385 He gave kind looks and greeting fair. On to the lofty car that glowed Like fire the royal tiger strode. Bright as himself its silver shone: A tiger's skin was laid thereon. With cloudlike thunder, as it rolled, It flashed with gems and burnished gold, And, like the sun's meridian blaze, Blinded the eye that none could gaze. Like youthful elephants, tall and strong, Fleet coursers whirled the car along: In such a car the Thousand-eyed Borne by swift horses loves to ride. So like Parjanya,282 when he flies Thundering through the autumn skies, The hero from the palace sped, As leaves the moon some cloud o'erhead. Still close to Ráma LakshmaG kept, Behind him to the car he leapt, And, watching with fraternal care, Waved the long chouri's silver hair, As from the palace gate he came Up rose the tumult of acclaim. While loud huzza and jubilant shout Pealed from the gathered myriads out. Then elephants, like mountains vast, And steeds who all their kind surpassed, Followed their lord by hundreds, nay By thousands, led in long array. First marched a band of warriors trained, With sandal dust and aloe stained; Well armed was each with sword and bow, 282 The Rain-God.
- **Translation**: 

---

### Verse 4 (Ramayan 0.404)
- **Original**: 386 The Ramayana And every breast with hope aglow, And ever, as they onward went, Shouts from the warrior train, And every sweet-toned instrument Prolonged the minstrel strain. On passed the tamer of his foes, While well clad dames, in crowded rows, Each chamber lattice thronged to view, And chaplets on the hero threw. Then all, of peerless face and limb, Sang Ráma's praise for love of him, And blent their voices, soft and sweet, From palace high and crowded street: “Now, sure, Kau[alyá's heart must swell To see the son she loves so well, Thee Ráma, thee, her joy and pride, Triumphant o'er the realm preside.” Then— for they knew his bride most fair Of all who part the soft dark hair, His love, his life, possessed the whole Of her young hero's heart and soul:— “Be sure the lady's fate repays Some mighty vow of ancient days,283 For blest with Ráma's love is she As, with the Moon's, sweet Rohiní.”284 Such were the witching words that came From lips of many a peerless dame Crowding the palace roofs to greet The hero as he gained the street. 283 In a former life. 284 One of the lunar asterisms, represented as the favourite wife of the Moon. See p. 4, note.
- **Translation**: 

---

### Verse 5 (Ramayan 0.405)
- **Original**: Canto XVII. Ráma's Approach. 387 Canto XVII. Ráma's Approach. As Ráma, rendering blithe and gay His loving friends, pursued his way, He saw on either hand a press Of mingled people numberless. The royal street he traversed, where Incense of aloe filled the air, Where rose high palaces, that vied With paly clouds, on either side; With flowers of myriad colours graced. And food for every varied taste, Bright as the glowing path o'erhead Which feet of Gods celestial tread, Loud benedictions, sweet to hear, From countless voices soothed his ear. While he to each gave due salute His place and dignity to suit: “Be thou,” the joyful people cried, “Be thou our guardian, lord and guide. Throned and anointed king to-day, Thy feet set forth upon the way Wherein, each honoured as a God, Thy fathers and forefathers trod. Thy sire and his have graced the throne, And loving care to us have shown: Thus blest shall we and ours remain, Yea still more blest in Ráma's reign. [113] No more of dainty fare we need, And but one cherished object heed, That we may see our prince today Invested with imperial sway.”
- **Translation**: 

---

### Verse 6 (Ramayan 0.406)
- **Original**: 388 The Ramayana Such were the words and pleasant speech That Ráma heard, unmoved, from each Of the dear friends around him spread, As onward through the street he sped, For none could turn his eye or thought From the dear form his glances sought, With fruitless ardour forward cast Even when Raghu's son had past. And he who saw not Ráma nigh, Nor caught a look from Ráma's eye, A mark for scorn and general blame, Reproached himself in bitter shame. For to each class his equal mind With sympathy and love inclined Most fully of the princely four, So greatest love to him they bore. His circling course the hero bent Round shrine and altar, reverent, Round homes of Gods, where cross-roads met, Where many a sacred tree was set. Near to his father's house he drew Like Indra's beautiful to view, And with the light his glory gave Within the royal palace drave. Through three broad courts, where bowmen kept Their watch and ward, his coursers swept, Then through the two remaining went On foot the prince preëminent. Through all the courts the hero passed, And gained the ladies' bower at last; Then through the door alone withdrew, And left without his retinue. When thus the monarch's noble boy
- **Translation**: 

---

### Verse 7 (Ramayan 0.407)
- **Original**: Canto XVIII. The Sentence. 389 Had gone his sire to meet, The multitude, elate with joy, Stood watching in the street, And his return with eager eyes Expected at the gates, As for his darling moon to rise The King of Rivers285 waits. Canto XVIII. The Sentence. With hopeless eye and pallid mien There sat the monarch with the queen. His father's feet with reverence due He clasped, and touched Kaikeyí's too. The king, with eyes still brimming o'er, Cried Ráma! and could do no more. His voice was choked, his eye was dim, He could not speak or look on him. Then sudden fear made Ráma shake As though his foot had roused a snake, Soon as his eyes had seen the change So mournful, terrible, and strange. For there his reason well-nigh fled, Sighing, with soul disquieted, To torturing pangs a prey, Dismayed, despairing, and distraught, In a fierce whirl of wildering thought The hapless monarch lay, Like Ocean wave-engarlanded 285 The Sea.
- **Translation**: 

---

### Verse 8 (Ramayan 0.408)
- **Original**: 390 The Ramayana Storm-driven from his tranquil bed, The Sun-God in eclipse, Or like a holy seer, heart-stirred With anguish, when a lying word Has passed his heedless lips. The sight of his dear father, pained With woe and misery unexplained Filled Ráma with unrest, As Ocean's pulses rise and swell When the great moon he loves so well Shines full upon his breast. So grieving for his father's sake, To his own heart the hero spake: “Why will the king my sire to-day No kindly word of greeting say? At other times, though wroth he be, His eyes grow calm that look on me. Then why does anguish wring his brow To see his well-beloved now?” Sick and perplexed, distraught with woe, To Queen Kaikeyí bowing low, While pallor o'er his bright cheek spread, With humble reverence he said: “What have I done, unknown, amiss To make my father wroth like this? Declare it, O dear Queen, and win His pardon for my heedless sin. Why is the sire I ever find Filled with all love to-day unkind? With eyes cast down and pallid cheek This day alone he will not speak. Or lies he prostrate neath the blow Of fierce disease or sudden woe? For all our bliss is dashed with pain,
- **Translation**: 

---

### Verse 9 (Ramayan 0.409)
- **Original**: Canto XVIII. The Sentence. 391 And joy unmixt is hard to gain. Does stroke of evil fortune smite Dear Bharat, charming to the sight, Or on the braveZatrughna fall, Or consorts, for he loves them all? Against his words when I rebel, Or fail to please the monarch well, When deeds of mine his soul offend, That hour I pray my life may end. How should a man to him who gave His being and his life behave? The sire to whom he owes his birth Should be his deity on earth. Hast thou, by pride and folly moved, [114] With bitter taunt the king reproved? Has scorn of thine or cruel jest To passion stirred his gentle breast? Speak truly, Queen, that I may know What cause has changed the monarch so.” Thus by the high-souled prince addressed, Of Raghu's sons the chief and best, She cast all ruth and shame aside, And bold with greedy words replied: “Not wrath, O Ráma, stirs the king, Nor misery stabs with sudden sting; One thought that fills his soul has he, But dares not speak for fear of thee. Thou art so dear, his lips refrain From words that might his darling pain. But thou, as duty bids, must still The promise of thy sire fulfil. He who to me in days gone by Vouchsafed a boon with honours high,
- **Translation**: 

---

### Verse 10 (Ramayan 0.410)
- **Original**: 392 The Ramayana Dares now, a king, his word regret, And caitiff-like disowns the debt. The lord of men his promise gave To grant the boon that I might crave, And now a bridge would idly throw When the dried stream has ceased to flow. His faith the monarch must not break In wrath, or e'en for thy dear sake. From faith, as well the righteous know, Our virtue and our merits flow. Now, be they good or be they ill, Do thou thy father's words fulfil: Swear that his promise shall not fail, And I will tell thee all the tale. Yes, Ráma, when I hear that thou Hast bound thee by thy father's vow, Then, not till then, my lips shall speak, Nor will he tell what boon I seek.” He heard, and with a troubled breast This answer to the queen addressed: “Ah me, dear lady, canst thou deem That words like these thy lips beseem? I, at the bidding of my sire, Would cast my body to the fire, A deadly draught of poison drink, Or in the waves of ocean sink: If he command, it shall be done,— My father and my king in one. Then speak and let me know the thing So longed for by my lord the king. It shall be done: let this suffice; Ráma ne'er makes a promise twice.”
- **Translation**: 

---

### Verse 11 (Ramayan 0.411)
- **Original**: Canto XVIII. The Sentence. 393 He ended. To the princely youth Who loved the right and spoke the truth, Cruel, abominable came The answer of the ruthless dame: “When Gods and Titans fought of yore, Transfixed with darts and bathed in gore Two boons to me thy father gave For the dear life 'twas mine to save. Of him I claim the ancient debt, That Bharat on the throne be set, And thou, O Ráma, go this day To DaG ak forest far away. Now, Ráma, if thou wilt maintain Thy father's faith without a stain, And thine own truth and honour clear, Then, best of men, my bidding hear. Do thou thy father's word obey, Nor from the pledge he gave me stray. Thy life in DaG ak forest spend Till nine long years and five shall end. Upon my Bharat's princely head Let consecrating drops be shed, With all the royal pomp for thee Made ready by the king's decree. Seek DaG ak forest and resign Rites that would make the empire thine, For twice seven years of exile wear The coat of bark and matted hair. Then in thy stead let Bharat reign Lord of his royal sire's domain, Rich in the fairest gems that shine, Cars, elephants, and steeds, and kine. The monarch mourns thy altered fate And vails his brow compassionate:
- **Translation**: 

---

### Verse 12 (Ramayan 0.412)
- **Original**: 394 The Ramayana Bowed down by bitter grief he lies And dares not lift to thine his eyes. Obey his word: be firm and brave, And with great truth the monarch save.” While thus with cruel words she spoke, No grief the noble youth betrayed; But forth the father's anguish broke, At his dear Ráma's lot dismayed. Canto XIX. Ráma's Promise. Calm and unmoved by threatened woe The noble conqueror of the foe Answered the cruel words she spoke, Nor quailed beneath the murderous stroke: “Yea, for my father's promise sake I to the wood my way will take, And dwell a lonely exile there In hermit dress with matted hair. One thing alone I fain would learn, Why is the king this day so stern? Why is the scourge of foes so cold, Nor gives me greeting as of old? Now let not anger flush thy cheek: Before thy face the truth I speak, In hermit's coat with matted hair To the wild wood will I repair. How can I fail his will to do, Friend, master, grateful sovereign too? One only pang consumes my breast:
- **Translation**: 

---

### Verse 13 (Ramayan 0.413)
- **Original**: Canto XIX. Ráma's Promise. 395 That his own lips have not expressed His will, nor made his longing known That Bharat should ascend the throne. [115] To Bharat I would yield my wife, My realm and wealth, mine own dear life, Unasked I fain would yield them all: More gladly at my father's call, More gladly when the gift may free His honour and bring joy to thee. Thus, lady, his sad heart release From the sore shame, and give him peace. But tell me, O, I pray thee, why The lord of men, with downcast eye, Lies prostrate thus, and one by one Down his pale cheek the tear-drops run. Let couriers to thy father speed On horses of the swiftest breed, And, by the mandate of the king, Thy Bharat to his presence bring. My father's words I will not stay To question, but this very day To DaG ak's pathless wild will fare, For twice seven years an exile there.” When Ráma thus had made reply Kaikeyí's heart with joy beat high. She, trusting to the pledge she held, The youth's departure thus impelled: “'Tis well. Be messengers despatched On coursers ne'er for fleetness matched, To seek my father's home and lead My Bharat back with all their speed. And, Ráma, as I ween that thou Wilt scarce endure to linger now,
- **Translation**: 

---

### Verse 14 (Ramayan 0.414)
- **Original**: 396 The Ramayana So surely it were wise and good This hour to journey to the wood. And if, with shame cast down and weak, No word to thee the king can speak, Forgive, and from thy mind dismiss A trifle in an hour like this. But till thy feet in rapid haste Have left the city for the waste, And to the distant forest fled, He will not bathe nor call for bread.” “Woe! woe!” from the sad monarch burst, In surging floods of grief immersed; Then swooning, with his wits astray, Upon the gold-wrought couch he lay, And Ráma raised the aged king: But the stern queen, unpitying, Checked not her needless words, nor spared The hero for all speed prepared, But urged him with her bitter tongue, Like a good horse with lashes stung, She spoke her shameful speech. Serene He heard the fury of the queen, And to her words so vile and dread Gently, unmoved in mind, he said: “I would not in this world remain A grovelling thrall to paltry gain, But duty's path would fain pursue, True as the saints themselves are true. From death itself I would not fly My father's wish to gratify, What deed soe'er his loving son May do to please him, think it done. Amid all duties, Queen, I count
- **Translation**: 

---

### Verse 15 (Ramayan 0.415)
- **Original**: Canto XIX. Ráma's Promise. 397 This duty first and paramount, That sons, obedient, aye fulfil Their honoured fathers' word and will. Without his word, if thou decree, Forth to the forest will I flee, And there shall fourteen years be spent Mid lonely wilds in banishment. Methinks thou couldst not hope to find One spark of virtue in my mind, If thou, whose wish is still my lord, Hast for this grace the king implored. This day I go, but, ere we part, Must cheer my Sítá's tender heart, To my dear mother bid farewell; Then to the woods, a while to dwell. With thee, O Queen, the care must rest That Bharat hear his sire's behest, And guard the land with righteous sway, For such the law that lives for aye.” In speechless woe the father heard, Wept with loud cries, but spoke no word. Then Ráma touched his senseless feet, And hers, for honour most unmeet; Round both his circling steps he bent, Then from the bower the hero went. Soon as he reached the gate he found His dear companions gathered round. Behind him came Sumitrá's child With weeping eyes so sad and wild. Then saw he all that rich array Of vases for the glorious day. Round them with reverent stops he paced, Nor vailed his eye, nor moved in haste.
- **Translation**: 

---

### Verse 16 (Ramayan 0.416)
- **Original**: 398 The Ramayana The loss of empire could not dim The glory that encompassed him. So will the Lord of Cooling Rays286 On whom the world delights to gaze, Through the great love of all retain Sweet splendour in the time of wane. Now to the exile's lot resigned He left the rule of earth behind: As though all worldly cares he spurned No trouble was in him discerned. The chouries that for kings are used, And white umbrella, he refused, Dismissed his chariot and his men, And every friend and citizen. He ruled his senses, nor betrayed The grief that on his bosom weighed, And thus his mother's mansion sought To tell the mournful news he brought. Nor could the gay-clad people there Who flocked round Ráma true and fair, One sign of altered fortune trace Upon the splendid hero's face. Nor had the chieftain, mighty-armed, Lost the bright look all hearts that charmed,[116] As e'en from autumn moons is thrown A splendour which is all their own. With his sweet voice the hero spoke Saluting all the gathered folk, Then righteous-souled and great in fame Close to his mother's house he came. Lakshma G the brave, his brother's peer In princely virtues, followed near, 286 The Moon.
- **Translation**: 

---

### Verse 17 (Ramayan 0.417)
- **Original**: Canto XX. Kausalyá's Lament. 399 Sore troubled, but resolved to show No token of his secret woe. Thus to the palace Ráma went Where all were gay with hope and joy; But well he knew the dire event That hope would mar, that bliss destroy. So to his grief he would not yield Lest the sad change their hearts might rend, And, the dread tiding unrevealed, Spared from the blow each faithful friend. Canto XX. Kausalyá's Lament. But in the monarch's palace, when Sped from the bower that lord of men, Up from the weeping women went A mighty wail and wild lament: “Ah, he who ever freely did His duty ere his sire could bid, Our refuge and our sure defence, This day will go an exile hence, He on Kau[alyá loves to wait Most tender and affectionate, And as he treats his mother, thus From childhood has he treated us. On themes that sting he will not speak, And when reviled is calm and meek. He soothes the angry, heals offence: He goes to-day an exile hence. Our lord the king is most unwise, And looks on life with doting eyes,
- **Translation**: 

---

### Verse 18 (Ramayan 0.418)
- **Original**: 400 The Ramayana Who in his folly casts away The world's protection, hope, and stay.” Thus in their woe, like kine bereaved Of their young calves,287 the ladies grieved, And ever as they wept and wailed With keen reproach the king assailed. Their lamentation, mixed with tears, Smote with new grief the monarch's ears, Who, burnt with woe too great to bear, Fell on his couch and fainted there. Then Ráma, smitten with the pain His heaving heart could scarce restrain, Groaned like an elephant and strode With LakshmaG to the queen's abode. A warder there, whose hoary eld In honour high by all was held, Guarding the mansion, sat before The portal, girt with many more. Swift to their feet the warders sprang, And loud the acclamation rang, Hail, Ráma! as to him they bent, Of victor chiefs preëminent. One court he passed, and in the next Saw, masters of each Veda text, A crowd of Bráhmans, good and sage, 287 The comparison may to a European reader seem a homely one. But Spenser likens an infuriate woman to a cow“That is berobbed of her youngling dere.” Shakspeare also makes King Henry VI compare himself to the calf's mother that“Runs lowing up and down, Looking the way her harmless young one went.” “Cows,” says De Quincey,“are amongst the gentlest of breathing crea- tures; none show more passionate tenderness to their young, when deprived of them, and, in short, I am not ashamed to profess a deep love for these gentle creatures.”
- **Translation**: 

---

### Verse 19 (Ramayan 0.419)
- **Original**: Canto XX. Kausalyá's Lament. 401 Dear to the king for lore and age. To these he bowed his reverent head, Thence to the court beyond he sped. Old dames and tender girls, their care To keep the doors, were stationed there. And all, when Ráma came in view, Delighted to the chamber flew, To bear to Queen Kau[alyá's ear The tidings that she loved to hear. The queen, on rites and prayer intent, In careful watch the night had spent, And at the dawn, her son to aid, To VishGu holy offerings made. Firm in her vows, serenely glad, In robes of spotless linen clad, As texts prescribe, with grace implored, Her offerings in the fire she poured. Within her splendid bower he came, And saw her feed the sacred flame. There oil, and grain, and vases stood, With wreaths, and curds, and cates, and wood, And milk, and sesamum, and rice, The elements of sacrifice. She, worn and pale with many a fast And midnight hours in vigil past, In robes of purest white arrayed, To Lakshmí Queen drink-offerings paid. So long away, she flew to meet The darling of her soul: So runs a mare with eager feet To welcome back her foal. He with his firm support upheld The queen, as near she drew, And, by maternal love impelled,
- **Translation**: 

---

### Verse 20 (Ramayan 0.420)
- **Original**: 402 The Ramayana Her arms around him threw. Her hero son, her matchless boy She kissed upon the head: She blessed him in her pride and joy With tender words, and said:[117] “Be like thy royal sires of old, The nobly good, the lofty-souled! Their lengthened days and fame be thine, And virtue, as beseems thy line! The pious king, thy father, see True to his promise made to thee: That truth thy sire this day will show, And regent's power on thee bestow.” She spoke. He took the proffered seat, And as she pressed her son to eat, Raised reverent bands, and, touched with shame, Made answer to the royal dame: “Dear lady, thou hast yet to know That danger threats, and heavy woe: A grief that will with sore distress On Sítá, thee, and LakshmaG press. What need of seats have such as I? This day to DaG ak wood I fly. The hour is come, a time, unmeet For silken couch and gilded seat. I must to lonely wilds repair, Abstain from flesh, and living there On roots, fruit, honey, hermit's food, Pass twice seven years in solitude. To Bharat's hand the king will yield The regent power I thought to wield, And me, a hermit, will he send My days in DaG ak wood to spend.”
- **Translation**: 

---

