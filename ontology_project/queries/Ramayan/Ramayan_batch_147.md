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

### Verse 1 (Ramayana 0.966)
- **Original**: 948 The Ramayana “Wilt thou absorbed in pleasure, still Pursue unchecked thy selfish will: Nor turn thy heedless eyes to see The coming fate which threatens thee? The king who days and hours employs In base pursuit of vulgar joys Must in his people's sight be vile As fire that smokes on funeral pile. He who when duty calls him spares No time for thought of royal cares, Must with his realm and people all Involved in fatal ruin fall. As elephants in terror shrink From the false river's miry brink, Thus subjects from a monarch flee Whose face their eyes may seldom see, Who spends the hours for toil ordained In evil courses unrestrained. He who neglects to guard and hold His kingdom by himself controlled, Sinks nameless like a hill whose head Is buried in the ocean's bed. Thy foes are calm and strong and wise, Fiends, Gods, and warriors of the skies,— How, heedless, wicked, weak, and vain, Wilt thou thy kingly state maintain? Thou, lord of giants, void of sense, Slave of each changing influence, Heedless of all that makes a king, Destruction on thy head wilt bring. O conquering chief, the prince, who boasts, Of treasury and rule and hosts, By others led, though lord of all, Is meaner than the lowest thrall.
- **Translation**: 

---

### Verse 2 (Ramayana 0.967)
- **Original**: Canto XXXIII. Súrpanakhá's Speech. 949 For this are monarchs said to be Long-sighted, having power to see Things far away by faithful eyes Of messengers and loyal spies. But aid from such thou wilt not seek: Thy counsellors are blind and weak, Or thou from these hadst surely known Thy legions and thy realm o'erthrown. Know, twice seven thousand, fierce in might, Are slain by Ráma in the fight, And they, the giant host who led, Khara and DúshaG, both are dead. Know, Ráma with his conquering arm Has freed the saints from dread of harm, Has smitten Janasthán and made Asylum safe in DaG ak's shade. Enslaved and dull, of blinded sight, Intoxicate with vain delight, Thou closest still thy heedless eyes To dangers in thy realm that rise. A king besotted, mean, unkind, Of niggard hand and slavish mind. Will find no faithful followers heed Their master in his hour of need. The friend on whom he most relies, In danger, from a monarch flies, Imperious in his high estate, Conceited, proud, and passionate; Who ne'er to state affairs attends With wholesome fear when woe impends Most weak and worthless as the grass, Soon from his sway the realm will pass. For rotting wood a use is found, For clods and dust that strew the ground,
- **Translation**: 

---

### Verse 3 (Ramayana 0.968)
- **Original**: 950 The Ramayana But when a king has lost his sway, Useless he falls, and sinks for aye. As raiment by another worn, As faded garland crushed and torn, So is, unthroned, the proudest king, Though mighty once, a useless thing. But he who every sense subdues And each event observant views, Rewards the good and keeps from wrong, Shall reign secure and flourish long. Though lulled in sleep his senses lie He watches with a ruler's eye, Untouched by favour, ire, and hate, And him the people celebrate. O weak of mind, without a trace[269] Of virtues that a king should grace, Who hast not learnt from watchful spy That low in death the giants lie. Scorner of others, but enchained By every base desire, By thee each duty is disdained Which time and place require. Soon wilt thou, if thou canst not learn, Ere yet it be too late, The good from evil to discern, Fall from thy high estate.” As thus she ceased not to upbraid The king with cutting speech, And every fault to view displayed, Naming and marking each, The monarch of the sons of night, Of wealth and power possessed, And proud of his imperial might, Long pondered in his breast.
- **Translation**: 

---

### Verse 4 (Ramayana 0.969)
- **Original**: Canto XXXIV. Súrpanakhá's Speech. 951 Canto XXXIV. Súrpanakhá's Speech. Then forth the giant's fury broke As ZúrpaGakhá harshly spoke. Girt by his lords the demon king Looked on her, fiercely questioning: “Who is this Ráma, whence, and where? His form, his might, his deeds declare. His wandering steps what purpose led To DaG ak forest, hard to tread? What arms are his that he could smite In fray the rovers of the night, And Tri[irás and DúshaG lay Low on the earth, and Khara slay? Tell all, my sister, and declare Who maimed thee thus, of form most fair.” Thus by the giant king addressed, While burnt her fury unrepressed, The giantess declared at length The hero's form and deeds and strength:
- **Translation**: 

---

### Verse 5 (Ramayana 0.970)
- **Original**: 952 The Ramayana “Long are his arms and large his eyes: A black deer's skin his dress supplies. King Da[aratha's son is he, Fair as Kandarpa's self to see. Adorned with many a golden band, A bow, like Indra's, arms his hand, And shoots a flood of arrows fierce As venomed snakes to burn and pierce. I looked, I looked, but never saw His mighty hand the bowstring draw That sent the deadly arrows out, While rang through air his battle-shout. I looked, I looked, and saw too well How with that hail the giants fell, As falls to earth the golden grain, Struck by the blows of Indra's rain. He fought, and twice seven thousand, all Terrific giants, strong and tall, Fell by the pointed shafts o'erthrown Which Ráma shot on foot, alone. Three little hours had scarcely fled,— Khara and DúshaG both were dead, And he had freed the saints and made Asylum sure in DaG ak's shade. Me of his grace the victor spared, Or I the giants' fate had shared. The high-souled Ráma would not deign His hand with woman's blood to stain. The glorious LakshmaG, justly dear, In gifts and warrior might his peer, Serves his great brother with the whole Devotion of his faithful soul: Impetuous victor, bold and wise, First in each hardy enterprise,
- **Translation**: 

---

### Verse 6 (Ramayana 0.971)
- **Original**: Canto XXXIV. Súrpanakhá's Speech. 953 Still ready by his side to stand, A second self or better hand. And Ráma has a large-eyed spouse, Pure as the moon her cheek and brows, Dearer than life in Ráma's sight, Whose happiness is her delight. With beauteous hair and nose the dame From head to foot has naught to blame. She shines the wood's bright Goddess, Queen Of beauty with her noble mien. First in the ranks of women placed Is Sítá of the dainty waist. In all the earth mine eyes have ne'er Seen female form so sweetly fair. Goddess nor nymph can vie with her, Nor bride of heavenly chorister. He who might call this dame his own, Her eager arms about him thrown, Would live more blest in Sítá's love Than Indra in the world above. She, peerless in her form and face And rich in every gentle grace, Is worthy bride, O King, for thee, As thou art meet her lord to be. I even I, will bring the bride In triumph to her lover's side— This beauty fairer than the rest, With rounded limb and heaving breast. Each wound upon my face I owe To cruel LakshmaG's savage blow. But thou, O brother, shalt survey Her moonlike loveliness to-day, And Káma's piercing shafts shall smite Thine amorous bosom at the sight.
- **Translation**: 

---

### Verse 7 (Ramayana 0.972)
- **Original**: 954 The Ramayana If in thy breast the longing rise To make thine own the beauteous prize, Up, let thy better foot begin The journey and the treasure win. If, giant Lord, thy favouring eyes Regard the plan which I advise, Up, cast all fear and doubt away And execute the words I say Come, giant King, this treasure seek, For thou art strong and they are weak.[270] Let Sítá of the faultless frame Be borne away and be thy dame. Thy host in Janasthán who dwelt Forth to the battle hied. And by the shafts which Ráma dealt They perished in their pride. DúshaG and Khara breathe no more, Laid low upon the plain. Arise, and ere the day be o'er Take vengeance for the slain.” Canto XXXV. Rávan's Journey. When Ráva G, by her fury spurred, That terrible advice had heard, He bade his nobles quit his side, And to the work his thought applied. He turned his anxious mind to scan On every side the hardy plan: The gain against the risk he laid, Each hope and fear with care surveyed,
- **Translation**: 

---

### Verse 8 (Ramayana 0.973)
- **Original**: Canto XXXV. Rávan's Journey. 955 And in his heart at length decreed To try performance of the deed. Then steady in his dire intent The giant to the courtyard went. There to his charioteer he cried, “Bring forth the car whereon I ride.” Aye ready at his master's word The charioteer the order heard, And yoked with active zeal the best Of chariots at his lord's behest. Asses with heads of goblins drew That wondrous car where'er it flew. Obedient to the will it rolled Adorned with gems and glistering gold. Then mounting, with a roar as loud As thunder from a labouring cloud, The mighty monarch to the tide Of Ocean, lord of rivers, hied. White was the shade above him spread, White chouris waved around his head, And he with gold and jewels bright Shone like the glossy lazulite. Ten necks and twenty arms had he: His royal gear was good to see. The heavenly Gods' insatiate foe, Who made the blood of hermits flow, He like the Lord of Hills appeared With ten huge heads to heaven upreared. In the great car whereon he rode, Like some dark cloud the giant showed, When round it in their close array The cranes 'mid wreaths of lightning play. He looked, and saw, from realms of air, The rocky shore of ocean, where
- **Translation**: 

---

### Verse 9 (Ramayana 0.974)
- **Original**: 956 The Ramayana Unnumbered trees delightful grew With flower and fruit of every hue. He looked on many a lilied pool With silvery waters fresh and cool, And shores like spacious altars meet For holy hermits' lone retreat. The graceful palm adorned the scene, The plantain waved her glossy green. There grew the sál and betel, there On bending boughs the flowers were fair. There hermits dwelt who tamed each sense By strictest rule of abstinence: Gandharvas, Kinnars,488 thronged the place, Nágas and birds of heavenly race. Bright minstrels of the ethereal quire, And saints exempt from low desire, With Ájas, sons of Brahmá's line, Maríchipas of seed divine, Vaikhánasas and Máshas strayed, And Bálakhilyas489 in the shade. The lovely nymphs of heaven were there, Celestial wreaths confined their hair, And to each form new grace was lent By wealth of heavenly ornament. Well skilled was each in play and dance And gentle arts of dalliance. The glorious wife of many a God Those beautiful recesses trod, There Gods and Dánavs, all who eat The food of heaven, rejoiced to meet. The swan and Sáras thronged each bay 488 Beings with the body of a man and the head of a horse. 489 Ájas, Maríchipas, Vaikhánasas, Máshas, and Bálakhilyas are classes of supernatural beings who lead the lives of hermits.
- **Translation**: 

---

### Verse 10 (Ramayana 0.975)
- **Original**: Canto XXXV. Rávan's Journey. 957 With curlews, ducks, and divers gay, Where the sea spray rose soft and white O'er rocks of glossy lazulite. As his swift way the fiend pursued Pale chariots of the Gods he viewed, Bearing each lord whose rites austere Had raised him to the heavenly sphere. Thereon celestial garlands hung, There music played and songs were sung. Then bright Gandharvas met his view, And heavenly nymphs, as on he flew. He saw the sandal woods below, And precious trees of odorous flow, That to the air around them lent Their riches of delightful scent; Nor failed his roving eye to mark Tall aloe trees in grove and park. He looked on wood with cassias filled, And plants which balmy sweets distilled, Where her fair flowers the betel showed And the bright pods of pepper glowed. The pearls in many a silvery heap Lay on the margin of the deep. And grey rocks rose amid the red Of coral washed from ocean's bed. [271] High soared the mountain peaks that bore Treasures of gold and silver ore, And leaping down the rocky walls Came wild and glorious waterfalls. Fair towns which grain and treasure held, And dames who every gem excelled, He saw outspread beneath him far, With steed, and elephant, and car. That ocean shore he viewed that showed
- **Translation**: 

---

### Verse 11 (Ramayana 0.976)
- **Original**: 958 The Ramayana Fair as the blessed Gods' abode Where cool delightful breezes played O'er levels in the freshest shade. He saw a fig-tree like a cloud With mighty branches earthward bowed. It stretched a hundred leagues and made For hermit bands a welcome shade. Thither the feathered king of yore An elephant and tortoise bore, And lighted on a bough to eat The captives of his taloned feet. The bough unable to sustain The crushing weight and sudden strain, Loaded with sprays and leaves of spring Gave way beneath the feathered king. Under the shadow of the tree Dwelt many a saint and devotee, Ájas, the sons of Brahmá's line, Máshas, Maríchipas divine. Vaikhánasas, and all the race Of Bálakhilyas, loved the place. But pitying their sad estate The feathered monarch raised the weight Of the huge bough, and bore away The loosened load and captured prey. A hundred leagues away he sped, Then on his monstrous booty fed, And with the bough he smote the lands Where dwell the wild Nisháda bands. High joy was his because his deed From jeopardy the hermits freed. That pride for great deliverance wrought A double share of valour brought. His soul conceived the high emprise
- **Translation**: 

---

### Verse 12 (Ramayana 0.977)
- **Original**: Canto XXXV. Rávan's Journey. 959 To snatch the Amrit from the skies. He rent the nets of iron first, Then through the jewel chamber burst, And bore the drink of heaven away That watched in Indra's palace lay. Such was the hermit-sheltering tree Which RávaG turned his eye to see. Still marked where Garu sought to rest, The fig-tree bore the name of Blest. When Ráva G stayed his chariot o'er The ocean's heart-enchanting shore, He saw a hermitage that stood Sequestered in the holy wood. He saw the fiend Márícha there With deerskin garb, and matted hair Coiled up in hermit guise, who spent His days by rule most abstinent. As guest and host are wont to meet, They met within that lone retreat. Before the king Márícha placed Food never known to human taste. He entertained his guest with meat And gave him water for his feet, And then addressed the giant king With timely words of questioning: “Lord, is it well with thee, and well With those in Lanká's town who dwell? What sudden thought, what urgent need Has brought thee with impetuous speed?”
- **Translation**: 

---

### Verse 13 (Ramayana 0.978)
- **Original**: 960 The Ramayana The fiend Márícha thus addressed RávaG the king, his mighty guest, And he, well skilled in arts that guide The eloquent, in turn replied: Canto XXXVI. Rávan's Speech. “Hear me, Márícha, while I speak, And tell thee why thy home I seek. Sick and distressed am I, and see My surest hope and help in thee. Of Janasthán I need not tell, Where ZúrpaGakhá, Khara, dwell, And DúshaG with the arm of might, And Tri[irás, the fierce in fight, Who feeds on human flesh and gore, And many noble giants more, Who roam in dark of midnight through The forest, brave and strong and true. By my command they live at ease And slaughter saints and devotees. Those twice seven thousand giants, all Obedient to their captain's call, Joying in war and ruthless deeds Follow where mighty Khara leads. Those fearless warrior bands who roam Through Janasthán their forest home, In all their terrible array Met Ráma in the battle fray. Girt with all weapons forth they sped With Khara at the army's head.
- **Translation**: 

---

### Verse 14 (Ramayana 0.979)
- **Original**: Canto XXXVI. Rávan's Speech. 961 The front of battle Ráma held: With furious wrath his bosom swelled. Without a word his hate to show He launched the arrows from his bow. On the fierce hosts the missiles came, Each burning with destructive flame, The twice seven thousand fell o'erthrown By him, a man, on foot, alone. Khara the army's chief and pride, And DúshaG, fearless warrior, died, And Tri[irás the fierce was slain, And Da G ak wood was free again. He, banished by his angry sire, Roams with his wife in mean attire. This wretch, his Warrior tribe's disgrace Has slain the best of giant race. [272] Harsh, wicked, fierce and greedy-souled, A fool, with senses uncontrolled, No thought of duty stirs his breast: He joys to see the world distressed. He sought the wood with fair pretence Of truthful life and innocence, But his false hand my sister left Mangled, of nose and ears bereft. This Ráma's wife who bears the name Of Sítá, in her face and frame Fair as a daughter of the skies,— Her will I seize and bring the prize Triumphant from the forest shade: For this I seek thy willing aid. If thou, O mighty one, wilt lend Thy help and stand beside thy friend, I with my brothers may defy
- **Translation**: 

---

### Verse 15 (Ramayana 0.980)
- **Original**: 962 The Ramayana All Gods embattled in the sky. Come, aid me now, for thine the power To succour in the doubtful hour. Thou art in war and time of fear, For heart and hand, without a peer. For thou art skilled in art and wile, A warrior brave and trained in guile. With this one hope, this only aim, O Rover of the Night, I came. Now let me tell what aid I ask To back me in my purposed task. In semblance of a golden deer Adorned with silver spots appear. Go, seek his dwelling: in the way Of Ráma and his consort stray. Doubt not the lady, when she sees The wondrous deer amid the trees, Will bid her lord and LakshmaG take The creature for its beauty's sake. Then when the chiefs have parted thence, And left her lone, without defence, As Ráhu storms the moonlight, I Will seize the lovely dame and fly. Her lord will waste away and weep For her his valour could not keep. Then boldly will I strike the blow And wreak my vengeance on the foe.” When wise Márícha heard the tale His heart grew faint, his cheek was pale, He stared with open orbs, and tried To moisten lips which terror dried, And grief, like death, his bosom rent As on the king his look he bent.
- **Translation**: 

---

### Verse 16 (Ramayana 0.981)
- **Original**: Canto XXXVII. Márícha's Speech. 963 The monarch's will he strove to stay, Distracted with alarm, For well he knew the might that lay In Ráma's matchless arm. With suppliant hands Márícha stood And thus began to tell His counsel for the tyrant's good, And for his own as well: Canto XXXVII. Márícha's Speech. Márícha gave attentive ear The ruler of the fiends to hear: Then, trained in all the rules that teach The eloquent, began his speech: “'Tis easy task, O King, to find Smooth speakers who delight the mind. But they who urge and they who do Distasteful things and wise, are few. Thou hast not learnt, by proof untaught, And borne away by eager thought, That Ráma, formed for high emprise, With VaruG or with Indra vies. Still let thy people live in peace, Nor let their name and lineage cease, For Ráma with his vengeful hand Can sweep the giants from the land. O, let not Janak's daughter bring Destruction on the giant king. Let not the lady Sítá wake A tempest, on thy head to break.
- **Translation**: 

---

### Verse 17 (Ramayana 0.982)
- **Original**: 964 The Ramayana Still let the dame, by care untried, Be happy by her husband's side, Lest swift avenging ruin fall On glorious Lanká, thee, and all. Men such as thou with wills unchained, Advised by sin and unrestrained, Destroy themselves, the king, the state, And leave the people desolate. Ráma, in bonds of duty held, Was never by his sire expelled. He is no wretch of greedy mind, Dishonour of his Warrior kind. Free from all touch of rancorous spite, All creatures' good is his delight. He saw his sire of truthful heart Deceived by Queen Kaikeyí's art, And said, a true and duteous son, “What thou hast promised shall be done.” To gratify the lady's will, His father's promise to fulfil, He left his realm and all delight For DaG ak wood, an anchorite. No cruel wretch, no senseless fool Is Ráma, unrestrained by rule. This groundless charge has ne'er been heard, Nor shouldst thou speak the slanderous word. Ráma in truth and goodness bold Is Virtue's self in human mould, The sovereign of the world confessed As Indra rules among the Blest. And dost thou plot from him to rend The darling whom his arms defend? Less vain the hope to steal away The glory of the Lord of Day.[273]
- **Translation**: 

---

### Verse 18 (Ramayana 0.983)
- **Original**: Canto XXXVII. Márícha's Speech. 965 O RávaG, guard thee from the fire Of vengeful Ráma's kindled ire,— Each spark a shaft with deadly aim, While bow and falchion feed the flame. Cast not away in hopeless strife Thy realm, thy bliss, thine own dear life. O RávaG of his might beware, A God of Death who will not spare. That bow he knows so well to draw Is the destroyer's flaming jaw, And with his shafts which flash and glow He slays the armies of the foe. Thou ne'er canst win— the thought forego— From the safe guard of shaft and bow King Janak's child, the dear delight Of Ráma unapproached in might. The spouse of Raghu's son, confessed Lion of men with lion chest,— Dearer than life, through good and ill Devoted to her husband's will, The slender-waisted, still must be From thy polluting touches free. Far better grasp with venturous hand The flame to wildest fury fanned. What, King of giants, canst thou gain From this attempt so wild and vain? If in the fight his eye he bend Upon thee, Lord, thy days must end, So life and bliss and royal sway, Lost beyond hope, will pass away. Summon each lord of high estate, And chief, VibhishaG490 to debate. 490 “The younger brother of the giant RávaG; when he and his brother had practiced austerities for a long series of years, Brahmá appeared to offer
- **Translation**: 

---

### Verse 19 (Ramayana 0.984)
- **Original**: 966 The Ramayana With peers in lore of counsel tried Consider, reason, and decide Scan strength and weakness, count the cost, What may be gained and what be lost. Examine and compare aright Thy proper power and Ráma's might, Then if thy weal be still thy care, Thou wilt be prudent and forbear. O giant King, the contest shun, Thy force is all too weak The lord of Kosál's mighty son In deadly fray to seek. King of the hosts that rove at night, O hear what I advise: My prudent counsel do not slight; Be patient and be wise.” Canto XXXVIII. Márícha's Speech. them boons: VibhishaGa asked that he might never meditate any unrighteous- ness.… On the death of RávaG VibhishaGa was installed as Rája of Lanká.” G ARRETT 'S{FNS Classical Dictionary of India.
- **Translation**: 

---

### Verse 20 (Ramayana 0.985)
- **Original**: Canto XXXVIII. Márícha's Speech. 967 “Once in my strength and vigour's pride I roamed this earth from side to side, And towering like a mountain's crest, A thousand Nágas'491 might possessed. Like some vast sable cloud I showed: My golden armlets flashed and glowed. A crown I wore, an axe I swayed, And all I met were sore afraid. I roved where DaG ak wood is spread; On flesh of slaughtered saints I fed. Then Vi[vámitra, sage revered, Holy of heart, my fury feared. To Da[aratha's court he sped And went before the king and said:492 “With me, my lord, thy Ráma send On holy days his aid to lend. Márícha fills my soul with dread And keeps me sore disquieted.” The monarch heard the saint's request And thus the glorious sage addressed: “My boy as yet in arms untrained The age of twelve has scarce attained. But I myself a host will lead To guard thee in the hour of need. My host with fourfold troops complete, The rover of the night shall meet, And I, O best of saints, will kill Thy foeman and thy prayer fulfil.” The king vouchsafed his willing aid: The saint again this answer made: 491 Serpent-gods. 492 See p. 33.
- **Translation**: 

---

