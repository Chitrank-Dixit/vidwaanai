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

### Verse 1 (Ramayana 0.406)
- **Original**: 388 The Ramayana Such were the words and pleasant speech That Ráma heard, unmoved, from each Of the dear friends around him spread, As onward through the street he sped, For none could turn his eye or thought From the dear form his glances sought, With fruitless ardour forward cast Even when Raghu's son had past. And he who saw not Ráma nigh, Nor caught a look from Ráma's eye, A mark for scorn and general blame, Reproached himself in bitter shame. For to each class his equal mind With sympathy and love inclined Most fully of the princely four, So greatest love to him they bore. His circling course the hero bent Round shrine and altar, reverent, Round homes of Gods, where cross-roads met, Where many a sacred tree was set. Near to his father's house he drew Like Indra's beautiful to view, And with the light his glory gave Within the royal palace drave. Through three broad courts, where bowmen kept Their watch and ward, his coursers swept, Then through the two remaining went On foot the prince preëminent. Through all the courts the hero passed, And gained the ladies' bower at last; Then through the door alone withdrew, And left without his retinue. When thus the monarch's noble boy
- **Translation**: 

---

### Verse 2 (Ramayana 0.407)
- **Original**: Canto XVIII. The Sentence. 389 Had gone his sire to meet, The multitude, elate with joy, Stood watching in the street, And his return with eager eyes Expected at the gates, As for his darling moon to rise The King of Rivers285 waits. Canto XVIII. The Sentence. With hopeless eye and pallid mien There sat the monarch with the queen. His father's feet with reverence due He clasped, and touched Kaikeyí's too. The king, with eyes still brimming o'er, Cried Ráma! and could do no more. His voice was choked, his eye was dim, He could not speak or look on him. Then sudden fear made Ráma shake As though his foot had roused a snake, Soon as his eyes had seen the change So mournful, terrible, and strange. For there his reason well-nigh fled, Sighing, with soul disquieted, To torturing pangs a prey, Dismayed, despairing, and distraught, In a fierce whirl of wildering thought The hapless monarch lay, Like Ocean wave-engarlanded 285 The Sea.
- **Translation**: 

---

### Verse 3 (Ramayana 0.408)
- **Original**: 390 The Ramayana Storm-driven from his tranquil bed, The Sun-God in eclipse, Or like a holy seer, heart-stirred With anguish, when a lying word Has passed his heedless lips. The sight of his dear father, pained With woe and misery unexplained Filled Ráma with unrest, As Ocean's pulses rise and swell When the great moon he loves so well Shines full upon his breast. So grieving for his father's sake, To his own heart the hero spake: “Why will the king my sire to-day No kindly word of greeting say? At other times, though wroth he be, His eyes grow calm that look on me. Then why does anguish wring his brow To see his well-beloved now?” Sick and perplexed, distraught with woe, To Queen Kaikeyí bowing low, While pallor o'er his bright cheek spread, With humble reverence he said: “What have I done, unknown, amiss To make my father wroth like this? Declare it, O dear Queen, and win His pardon for my heedless sin. Why is the sire I ever find Filled with all love to-day unkind? With eyes cast down and pallid cheek This day alone he will not speak. Or lies he prostrate neath the blow Of fierce disease or sudden woe? For all our bliss is dashed with pain,
- **Translation**: 

---

### Verse 4 (Ramayana 0.409)
- **Original**: Canto XVIII. The Sentence. 391 And joy unmixt is hard to gain. Does stroke of evil fortune smite Dear Bharat, charming to the sight, Or on the braveZatrughna fall, Or consorts, for he loves them all? Against his words when I rebel, Or fail to please the monarch well, When deeds of mine his soul offend, That hour I pray my life may end. How should a man to him who gave His being and his life behave? The sire to whom he owes his birth Should be his deity on earth. Hast thou, by pride and folly moved, [114] With bitter taunt the king reproved? Has scorn of thine or cruel jest To passion stirred his gentle breast? Speak truly, Queen, that I may know What cause has changed the monarch so.” Thus by the high-souled prince addressed, Of Raghu's sons the chief and best, She cast all ruth and shame aside, And bold with greedy words replied: “Not wrath, O Ráma, stirs the king, Nor misery stabs with sudden sting; One thought that fills his soul has he, But dares not speak for fear of thee. Thou art so dear, his lips refrain From words that might his darling pain. But thou, as duty bids, must still The promise of thy sire fulfil. He who to me in days gone by Vouchsafed a boon with honours high,
- **Translation**: 

---

### Verse 5 (Ramayana 0.410)
- **Original**: 392 The Ramayana Dares now, a king, his word regret, And caitiff-like disowns the debt. The lord of men his promise gave To grant the boon that I might crave, And now a bridge would idly throw When the dried stream has ceased to flow. His faith the monarch must not break In wrath, or e'en for thy dear sake. From faith, as well the righteous know, Our virtue and our merits flow. Now, be they good or be they ill, Do thou thy father's words fulfil: Swear that his promise shall not fail, And I will tell thee all the tale. Yes, Ráma, when I hear that thou Hast bound thee by thy father's vow, Then, not till then, my lips shall speak, Nor will he tell what boon I seek.” He heard, and with a troubled breast This answer to the queen addressed: “Ah me, dear lady, canst thou deem That words like these thy lips beseem? I, at the bidding of my sire, Would cast my body to the fire, A deadly draught of poison drink, Or in the waves of ocean sink: If he command, it shall be done,— My father and my king in one. Then speak and let me know the thing So longed for by my lord the king. It shall be done: let this suffice; Ráma ne'er makes a promise twice.”
- **Translation**: 

---

### Verse 6 (Ramayana 0.411)
- **Original**: Canto XVIII. The Sentence. 393 He ended. To the princely youth Who loved the right and spoke the truth, Cruel, abominable came The answer of the ruthless dame: “When Gods and Titans fought of yore, Transfixed with darts and bathed in gore Two boons to me thy father gave For the dear life 'twas mine to save. Of him I claim the ancient debt, That Bharat on the throne be set, And thou, O Ráma, go this day To DaG ak forest far away. Now, Ráma, if thou wilt maintain Thy father's faith without a stain, And thine own truth and honour clear, Then, best of men, my bidding hear. Do thou thy father's word obey, Nor from the pledge he gave me stray. Thy life in DaG ak forest spend Till nine long years and five shall end. Upon my Bharat's princely head Let consecrating drops be shed, With all the royal pomp for thee Made ready by the king's decree. Seek DaG ak forest and resign Rites that would make the empire thine, For twice seven years of exile wear The coat of bark and matted hair. Then in thy stead let Bharat reign Lord of his royal sire's domain, Rich in the fairest gems that shine, Cars, elephants, and steeds, and kine. The monarch mourns thy altered fate And vails his brow compassionate:
- **Translation**: 

---

### Verse 7 (Ramayana 0.412)
- **Original**: 394 The Ramayana Bowed down by bitter grief he lies And dares not lift to thine his eyes. Obey his word: be firm and brave, And with great truth the monarch save.” While thus with cruel words she spoke, No grief the noble youth betrayed; But forth the father's anguish broke, At his dear Ráma's lot dismayed. Canto XIX. Ráma's Promise. Calm and unmoved by threatened woe The noble conqueror of the foe Answered the cruel words she spoke, Nor quailed beneath the murderous stroke: “Yea, for my father's promise sake I to the wood my way will take, And dwell a lonely exile there In hermit dress with matted hair. One thing alone I fain would learn, Why is the king this day so stern? Why is the scourge of foes so cold, Nor gives me greeting as of old? Now let not anger flush thy cheek: Before thy face the truth I speak, In hermit's coat with matted hair To the wild wood will I repair. How can I fail his will to do, Friend, master, grateful sovereign too? One only pang consumes my breast:
- **Translation**: 

---

### Verse 8 (Ramayana 0.413)
- **Original**: Canto XIX. Ráma's Promise. 395 That his own lips have not expressed His will, nor made his longing known That Bharat should ascend the throne. [115] To Bharat I would yield my wife, My realm and wealth, mine own dear life, Unasked I fain would yield them all: More gladly at my father's call, More gladly when the gift may free His honour and bring joy to thee. Thus, lady, his sad heart release From the sore shame, and give him peace. But tell me, O, I pray thee, why The lord of men, with downcast eye, Lies prostrate thus, and one by one Down his pale cheek the tear-drops run. Let couriers to thy father speed On horses of the swiftest breed, And, by the mandate of the king, Thy Bharat to his presence bring. My father's words I will not stay To question, but this very day To DaG ak's pathless wild will fare, For twice seven years an exile there.” When Ráma thus had made reply Kaikeyí's heart with joy beat high. She, trusting to the pledge she held, The youth's departure thus impelled: “'Tis well. Be messengers despatched On coursers ne'er for fleetness matched, To seek my father's home and lead My Bharat back with all their speed. And, Ráma, as I ween that thou Wilt scarce endure to linger now,
- **Translation**: 

---

### Verse 9 (Ramayana 0.414)
- **Original**: 396 The Ramayana So surely it were wise and good This hour to journey to the wood. And if, with shame cast down and weak, No word to thee the king can speak, Forgive, and from thy mind dismiss A trifle in an hour like this. But till thy feet in rapid haste Have left the city for the waste, And to the distant forest fled, He will not bathe nor call for bread.” “Woe! woe!” from the sad monarch burst, In surging floods of grief immersed; Then swooning, with his wits astray, Upon the gold-wrought couch he lay, And Ráma raised the aged king: But the stern queen, unpitying, Checked not her needless words, nor spared The hero for all speed prepared, But urged him with her bitter tongue, Like a good horse with lashes stung, She spoke her shameful speech. Serene He heard the fury of the queen, And to her words so vile and dread Gently, unmoved in mind, he said: “I would not in this world remain A grovelling thrall to paltry gain, But duty's path would fain pursue, True as the saints themselves are true. From death itself I would not fly My father's wish to gratify, What deed soe'er his loving son May do to please him, think it done. Amid all duties, Queen, I count
- **Translation**: 

---

### Verse 10 (Ramayana 0.415)
- **Original**: Canto XIX. Ráma's Promise. 397 This duty first and paramount, That sons, obedient, aye fulfil Their honoured fathers' word and will. Without his word, if thou decree, Forth to the forest will I flee, And there shall fourteen years be spent Mid lonely wilds in banishment. Methinks thou couldst not hope to find One spark of virtue in my mind, If thou, whose wish is still my lord, Hast for this grace the king implored. This day I go, but, ere we part, Must cheer my Sítá's tender heart, To my dear mother bid farewell; Then to the woods, a while to dwell. With thee, O Queen, the care must rest That Bharat hear his sire's behest, And guard the land with righteous sway, For such the law that lives for aye.” In speechless woe the father heard, Wept with loud cries, but spoke no word. Then Ráma touched his senseless feet, And hers, for honour most unmeet; Round both his circling steps he bent, Then from the bower the hero went. Soon as he reached the gate he found His dear companions gathered round. Behind him came Sumitrá's child With weeping eyes so sad and wild. Then saw he all that rich array Of vases for the glorious day. Round them with reverent stops he paced, Nor vailed his eye, nor moved in haste.
- **Translation**: 

---

### Verse 11 (Ramayana 0.416)
- **Original**: 398 The Ramayana The loss of empire could not dim The glory that encompassed him. So will the Lord of Cooling Rays286 On whom the world delights to gaze, Through the great love of all retain Sweet splendour in the time of wane. Now to the exile's lot resigned He left the rule of earth behind: As though all worldly cares he spurned No trouble was in him discerned. The chouries that for kings are used, And white umbrella, he refused, Dismissed his chariot and his men, And every friend and citizen. He ruled his senses, nor betrayed The grief that on his bosom weighed, And thus his mother's mansion sought To tell the mournful news he brought. Nor could the gay-clad people there Who flocked round Ráma true and fair, One sign of altered fortune trace Upon the splendid hero's face. Nor had the chieftain, mighty-armed, Lost the bright look all hearts that charmed,[116] As e'en from autumn moons is thrown A splendour which is all their own. With his sweet voice the hero spoke Saluting all the gathered folk, Then righteous-souled and great in fame Close to his mother's house he came. Lakshma G the brave, his brother's peer In princely virtues, followed near, 286 The Moon.
- **Translation**: 

---

### Verse 12 (Ramayana 0.417)
- **Original**: Canto XX. Kausalyá's Lament. 399 Sore troubled, but resolved to show No token of his secret woe. Thus to the palace Ráma went Where all were gay with hope and joy; But well he knew the dire event That hope would mar, that bliss destroy. So to his grief he would not yield Lest the sad change their hearts might rend, And, the dread tiding unrevealed, Spared from the blow each faithful friend. Canto XX. Kausalyá's Lament. But in the monarch's palace, when Sped from the bower that lord of men, Up from the weeping women went A mighty wail and wild lament: “Ah, he who ever freely did His duty ere his sire could bid, Our refuge and our sure defence, This day will go an exile hence, He on Kau[alyá loves to wait Most tender and affectionate, And as he treats his mother, thus From childhood has he treated us. On themes that sting he will not speak, And when reviled is calm and meek. He soothes the angry, heals offence: He goes to-day an exile hence. Our lord the king is most unwise, And looks on life with doting eyes,
- **Translation**: 

---

### Verse 13 (Ramayana 0.418)
- **Original**: 400 The Ramayana Who in his folly casts away The world's protection, hope, and stay.” Thus in their woe, like kine bereaved Of their young calves,287 the ladies grieved, And ever as they wept and wailed With keen reproach the king assailed. Their lamentation, mixed with tears, Smote with new grief the monarch's ears, Who, burnt with woe too great to bear, Fell on his couch and fainted there. Then Ráma, smitten with the pain His heaving heart could scarce restrain, Groaned like an elephant and strode With LakshmaG to the queen's abode. A warder there, whose hoary eld In honour high by all was held, Guarding the mansion, sat before The portal, girt with many more. Swift to their feet the warders sprang, And loud the acclamation rang, Hail, Ráma! as to him they bent, Of victor chiefs preëminent. One court he passed, and in the next Saw, masters of each Veda text, A crowd of Bráhmans, good and sage, 287 The comparison may to a European reader seem a homely one. But Spenser likens an infuriate woman to a cow“That is berobbed of her youngling dere.” Shakspeare also makes King Henry VI compare himself to the calf's mother that“Runs lowing up and down, Looking the way her harmless young one went.” “Cows,” says De Quincey,“are amongst the gentlest of breathing crea- tures; none show more passionate tenderness to their young, when deprived of them, and, in short, I am not ashamed to profess a deep love for these gentle creatures.”
- **Translation**: 

---

### Verse 14 (Ramayana 0.419)
- **Original**: Canto XX. Kausalyá's Lament. 401 Dear to the king for lore and age. To these he bowed his reverent head, Thence to the court beyond he sped. Old dames and tender girls, their care To keep the doors, were stationed there. And all, when Ráma came in view, Delighted to the chamber flew, To bear to Queen Kau[alyá's ear The tidings that she loved to hear. The queen, on rites and prayer intent, In careful watch the night had spent, And at the dawn, her son to aid, To VishGu holy offerings made. Firm in her vows, serenely glad, In robes of spotless linen clad, As texts prescribe, with grace implored, Her offerings in the fire she poured. Within her splendid bower he came, And saw her feed the sacred flame. There oil, and grain, and vases stood, With wreaths, and curds, and cates, and wood, And milk, and sesamum, and rice, The elements of sacrifice. She, worn and pale with many a fast And midnight hours in vigil past, In robes of purest white arrayed, To Lakshmí Queen drink-offerings paid. So long away, she flew to meet The darling of her soul: So runs a mare with eager feet To welcome back her foal. He with his firm support upheld The queen, as near she drew, And, by maternal love impelled,
- **Translation**: 

---

### Verse 15 (Ramayana 0.420)
- **Original**: 402 The Ramayana Her arms around him threw. Her hero son, her matchless boy She kissed upon the head: She blessed him in her pride and joy With tender words, and said:[117] “Be like thy royal sires of old, The nobly good, the lofty-souled! Their lengthened days and fame be thine, And virtue, as beseems thy line! The pious king, thy father, see True to his promise made to thee: That truth thy sire this day will show, And regent's power on thee bestow.” She spoke. He took the proffered seat, And as she pressed her son to eat, Raised reverent bands, and, touched with shame, Made answer to the royal dame: “Dear lady, thou hast yet to know That danger threats, and heavy woe: A grief that will with sore distress On Sítá, thee, and LakshmaG press. What need of seats have such as I? This day to DaG ak wood I fly. The hour is come, a time, unmeet For silken couch and gilded seat. I must to lonely wilds repair, Abstain from flesh, and living there On roots, fruit, honey, hermit's food, Pass twice seven years in solitude. To Bharat's hand the king will yield The regent power I thought to wield, And me, a hermit, will he send My days in DaG ak wood to spend.”
- **Translation**: 

---

### Verse 16 (Ramayana 0.421)
- **Original**: Canto XX. Kausalyá's Lament. 403 As when the woodman's axe has lopped A Zal branch in the grove, she dropped: So from the skies a Goddess falls Ejected from her radiant halls. When Ráma saw her lying low, Prostrate by too severe a blow, Around her form his arms he wound And raised her fainting from the ground. His hand upheld her like a mare Who feels her load too sore to bear, And sinks upon the way o'ertoiled, And all her limbs with dust are soiled. He soothed her in her wild distress With loving touch and soft caress. She, meet for highest fortune, eyed The hero watching by her side, And thus, while LakshmaG bent to hear, Addressed her son with many a tear! “If, Ráma, thou had ne'er been born My child to make thy mother mourn, Though reft of joy, a childless queen, Such woe as this I ne'er had seen. Though to the childless wife there clings One sorrow armed with keenest stings, “No child have I: no child have I,” No second misery prompts the sigh. When long I sought, alas, in vain, My husband's love and bliss to gain, In Ráma all my hopes I set And dreamed I might be happy yet. I, of the consorts first and best, Must bear my rivals' taunt and jest, And brook, though better far than they,
- **Translation**: 

---

### Verse 17 (Ramayana 0.422)
- **Original**: 404 The Ramayana The soul distressing words they say. What woman can be doomed to pine In misery more sore than mine, Whose hopeless days must still be spent In grief that ends not and lament? They scorned me when my son was nigh; When he is banished I must die. Me, whom my husband never prized, Kaikeyí's retinue despised With boundless insolence, though she Tops not in rank nor equals me. And they who do me service yet, Nor old allegiance quite forget, Whene'er they see Kaikeyí's son, With silent lips my glances shun. How, O my darling, shall I brook Each menace of Kaikeyí's look, And listen, in my low estate, To taunts of one so passionate? For seventeen years since thou wast born I sat and watched, ah me, forlorn! Hoping some blessed day to see Deliverance from my woes by thee. Now comes this endless grief and wrong, So dire I cannot bear it long, Sinking, with age and sorrow worn, Beneath my rivals' taunts and scorn. How shall I pass in dark distress My long lone days of wretchedness Without my Ráma's face, as bright As the full moon to cheer my sight? Alas, my cares thy steps to train, And fasts, and vows, and prayers are vain. Hard, hard, I ween, must be this heart
- **Translation**: 

---

### Verse 18 (Ramayana 0.423)
- **Original**: Canto XXI. Kausalyá Calmed. 405 To hear this blow nor burst apart, As some great river bank, when first The floods of Rain-time on it burst. No, Fate that speeds not will not slay, Nor Yama's halls vouchsafe me room, Or, like a lion's weeping prey, Death now had borne me to my doom. Hard is my heart and wrought of steel That breaks not with the crushing blow, Or in the pangs this day I feel My lifeless frame had sunk below. Death waits his hour, nor takes me now: But this sad thought augments my pain, That prayer and largess, fast and vow, And Heavenward service are in vain. Ah me, ah me! with fruitless toil Of rites austere a child I sought: Thus seed cast forth on barren soil Still lifeless lies and comes to naught. If ever wretch by anguish grieved Before his hour to death had fled, I mourning, like a cow bereaved, Had been this day among the dead.” [118] Canto XXI. Kausalyá Calmed.
- **Translation**: 

---

### Verse 19 (Ramayana 0.424)
- **Original**: 406 The Ramayana While thus Kau[alyá wept and sighed, With timely words sad LakshmaG cried: “O honoured Queen I like it ill That, subject to a woman's will, Ráma his royal state should quit And to an exile's doom submit. The aged king, fond, changed, and weak, Will as the queen compels him speak. But why should Ráma thus be sent To the wild woods in banishment? No least offence I find in him, I see no fault his fame to dim. Not one in all the world I know, Not outcast wretch, not secret foe, Whose whispering lips would dare assail His spotless life with slanderous tale. Godlike and bounteous, just, sincere, E'en to his very foemen dear: Who would without a cause neglect The right, and such a son reject? And if a king such order gave, In second childhood, passion's slave, What son within his heart would lay The senseless order, and obey? Come, Ráma, ere this plot be known Stand by me and secure the throne. Stand like the King who rules below, Stand aided by thy brother's bow: How can the might of meaner men Resist thy royal purpose then? My shafts, if rebels court their fate, Shall lay Ayodhyá desolate. Then shall her streets with blood be dyed Of those who stand on Bharat's side:
- **Translation**: 

---

### Verse 20 (Ramayana 0.425)
- **Original**: Canto XXI. Kausalyá Calmed. 407 None shall my slaughtering hand exempt, For gentle patience earns contempt. If, by Kaikeyí's counsel changed, Our father's heart be thus estranged, No mercy must our arm restrain, But let the foe be slain, be slain. For should the guide, respected long, No more discerning right and wrong, Turn in forbidden paths to stray, 'Tis meet that force his steps should stay. What power sufficient can he see, What motive for the wish has he, That to Kaikeyí would resign The empire which is justly thine? Can he, O conqueror of thy foes, Thy strength and mine in war oppose? Can he entrust, in our despite, To Bharat's hand thy royal right? I love this brother with the whole Affection of my faithful soul. Yea Queen, by bow and truth I swear, By sacrifice, and gift, and prayer, If Ráma to the forest goes, Or where the burning furnace glows, First shall my feet the forest tread, The flames shall first surround my head. My might shall chase thy grief and tears, As darkness flies when morn appears. Do thou, dear Queen, and Ráma too Behold what power like mine can do. My aged father I will kill, The vassal of Kaikeyí's will, Old, yet a child, the woman's thrall, Infirm, and base, the scorn of all.”
- **Translation**: 

---

