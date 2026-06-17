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

### Verse 1 (Ramayan 0.521)
- **Original**: Canto XLII. Dasaratha's Lament. 503 Where'er he looked naught met his gaze But empty houses, courts, and ways. Closed were the temples: countless feet No longer trod the royal street, And thinking of his son he viewed Men weak and worn and woe-subdued. As sinks the sun into a cloud, So passed he on, and wept aloud, Within that house no more to be The dwelling of the banished three, Brave Ráma, his Vedehan bride, And Lakshma G by his brother's side: Like broad still waters, when the king Of all the birds that ply the wing Has swooped from heaven and borne away The glittering snakes that made them gay. With choking sobs and voice half spent The king renewed his sad lament: With broken utterance faint and low Scarce could he speak these words of woe: “My steps to Ráma's mother guide, And place me by Kau[alyá's side: There, only there my heart may know Some little respite from my woe.” The warders of the palace led The monarch, when his words were said, To Queen Kau[alyá's bower, and there Laid him with reverential care. But while he rested on the bed Still was his soul disquieted. In grief he tossed his arms on high Lamenting with a piteous cry: “O Ráma, Ráma,” thus said he,
- **Translation**: 

---

### Verse 2 (Ramayan 0.522)
- **Original**: 504 The Ramayana “My son, thou hast forsaken me. High bliss awaits those favoured men Left living in Ayodhyá then, Whose eyes shall see my son once more Returning when the time is o'er.” Then came the night, whose hated gloom Fell on him like the night of doom. At midnight Da[aratha cried To Queen Kau[alyá by his side: “I see thee not, Kau[alyá; lay Thy gentle hand in mine, I pray. When Ráma left his home my sight Went with him, nor returns to-night.” Canto XLIII. Kausalyá's Lament. Kau [alyá saw the monarch lie With drooping frame and failing eye, And for her banished son distressed With these sad words her lord addressed: “Kaikeyí, cruel, false, and vile Has cast the venom of her guile On Ráma lord of men, and she Will ravage like a snake set free; And more and more my soul alarm, Like a dire serpent bent on harm, For triumph crowns each dark intent, And Ráma to the wild is sent. Ah, were he doomed but here to stray Begging his food from day to day, Or do, enslaved, Kaikeyí's will,
- **Translation**: 

---

### Verse 3 (Ramayan 0.523)
- **Original**: Canto XLIII. Kausalyá's Lament. 505 This were a boon, a comfort still. But she, as chose her cruel hate, Has hurled him from his high estate, As Bráhmans when the moon is new Cast to the ground the demons' due.318 The long-armed hero, like the lord Of Nágas, with his bow and sword Begins, I ween, his forest life With LakshmaG and his faithful wife. Ah, how will fare the exiles now, Whom, moved by Queen Kaikeyí, thou Hast sent in forests to abide, Bred in delights, by woe untried? Far banished when their lives are young, With the fair fruit before them hung, Deprived of all their rank that suits, How will they live on grain and roots? O, that my years of woe were passed, And the glad hour were come at last When I shall see my children dear, Ráma, his wife, and LakshmaG here! When shall Ayodhyá, wild with glee, Again those mighty heroes see, And decked with wreaths her banners wave To welcome home the true and brave? When will the beautiful city view With happy eyes the lordly two Returning, joyful as the main When the dear moon is full again? When, like some mighty bull who leads The cow exulting through the meads, Will Ráma through the city ride, 318 The husks and chaff of the rice offered to the Gods.
- **Translation**: 

---

### Verse 4 (Ramayan 0.524)
- **Original**: 506 The Ramayana Strong-armed, with Sítá at his side? When will ten thousand thousand meet And crowd Ayodhyá's royal street, And grain in joyous welcome throw Upon my sons who tame the foe? When with delight shall youthful bands Of Bráhman maidens in their hands[146] Bear fruit and flowers in goodly show, And circling round Ayodhyá go? With ripened judgment of a sage, And godlike in his blooming age, When shall my virtuous son appear, Like kindly rain, our hearts to cheer? Ah, in a former life, I ween, This hand of mine, most base and mean, Has dried the udders of the kine And left the thirsty calves to pine. Hence, as the lion robs the cow, Kaikeyí makes me childless now, Exulting from her feebler foe To rend the son she cherished so. I had but him, in Scripture skilled, With every grace his soul was filled. Now not a joy has life to give, And robbed of him I would not live: Yea, all my days are dark and drear If he, my darling, be not near, And Lakshma G brave, my heart to cheer. As for my son I mourn and yearn, The quenchless flames of anguish burn And kill me with the pain, As in the summer's noontide blaze The glorious Day-God with his rays Consumes the parching plain.”
- **Translation**: 

---

### Verse 5 (Ramayan 0.525)
- **Original**: Canto XLIV. Sumitrá's Speech. 507 Canto XLIV. Sumitrá's Speech. Kau [alyá ceased her sad lament, Of beauteous dames most excellent. Sumitrá who to duty clave, In righteous words this answer gave: “Dear Queen, all noble virtues grace Thy son, of men the first in place. Why dost thou shed these tears of woe With bitter grief lamenting so? If Ráma, leaving royal sway Has hastened to the woods away, 'Tis for his high-souled father's sake That he his premise may not break. He to the path of duty clings Which lordly fruit hereafter brings— The path to which the righteous cleave— For him, dear Queen, thou shouldst not grieve. And Lakshma G too, the blameless-souled, The same high course with him will hold, And mighty bliss on him shall wait, So tenderly compassionate. And Sítá, bred with tender care, Well knows what toils await her there, But in her love she will not part From Ráma of the virtuous heart. Now has thy son through all the world The banner of his fame unfurled; True, modest, careful of his vow, What has he left to aim at now? The sun will mark his mighty soul, His wisdom, sweetness, self-control, Will spare from pain his face and limb, And with soft radiance shine for him.
- **Translation**: 

---

### Verse 6 (Ramayan 0.526)
- **Original**: 508 The Ramayana For him through forest glades shall spring A soft auspicious breeze, and bring Its tempered heat and cold to play Around him ever night and day. The pure cold moonbeams shall delight The hero as he sleeps at night, And soothe him with the soft caress Of a fond parent's tenderness. To him, the bravest of the brave, His heavenly arms the Bráhman gave, When fierce Suváhu dyed the plain With his life-blood by Ráma slain. Still trusting to his own right arm Thy hero son will fear no harm: As in his father's palace, he In the wild woods will dauntless be. Whene'er he lets his arrows fly His stricken foemen fall and die: And is that prince of peerless worth Too weak to keep and sway the earth? His sweet pure soul, his beauty's charm, His hero heart, his warlike arm, Will soon redeem his rightful reign When from the woods he comes again. The Bráhmans on the prince's head King-making drops shall quickly shed, And Sítá, Earth, and Fortune share The glories which await the heir. For him, when forth his chariot swept, The crowd that thronged Ayodhyá wept, With agonizing woe distressed. With him in hermít's mantle dressed In guise of Sítá Lakshmí went, And none his glory may prevent.
- **Translation**: 

---

### Verse 7 (Ramayan 0.527)
- **Original**: Canto XLIV. Sumitrá's Speech. 509 Yea, naught to him is high or hard, Before whose steps, to be his guard, Lakshma G, the best who draws the bow, With spear, shaft, sword rejoiced to go. His wanderings in the forest o'er, Thine eyes shall see thy son once more, Quit thy faint heart, thy grief dispel, For this, O Queen, is truth I tell. Thy son returning, moonlike, thence, Shall at thy feet do reverence, And, blest and blameless lady, thou Shalt see his head to touch them bow, Yea, thou shalt see thy son made king When he returns with triumphing, And how thy happy eyes will brim With tears of joy to look on him! Thou, blameless lady, shouldst the whole Of the sad people here console: Why in thy tender heart allow This bitter grief to harbour now? As the long banks of cloud distil Their water when they see the hill, [147] So shall the drops of rapture run From thy glad eyes to see thy son Returning, as he lowly bends To greet thee, girt by all his friends.” Thus soothing, kindly eloquent, With every hopeful argument Kau [alyá's heart by sorrow rent, Fair Queen Sumitrá ceased. Kau [alyá heard each pleasant plea, And grief began to leave her free, As the light clouds of autumn flee,
- **Translation**: 

---

### Verse 8 (Ramayan 0.528)
- **Original**: 510 The Ramayana Their watery stores decreased. Canto XLV. The Tamasá. Their tender love the people drew To follow Ráma brave and true, The high-souled hero, as he went Forth from his home to banishment. The king himself his friends obeyed, And turned him homeward as they prayed. But yet the people turned not back, Still close on Ráma's chariot track. For they who in Ayodhyá dwelt For him such fond affection felt, Decked with all grace and glories high, The dear full moon of every eye. Though much his people prayed and wept, Kakutstha's son his purpose kept, And still his journey would pursue To keep the king his father true. Deep in the hero's bosom sank Their love, whose signs his glad eye drank. He spoke to cheer them, as his own Dear children, in a loving tone: “If ye would grant my fond desire, Give Bharat now that love entire And reverence shown to me by all Who dwell within Ayodhyá's wall. For he, Kaikeyí's darling son, His virtuous career will run, And ever bound by duty's chain
- **Translation**: 

---

### Verse 9 (Ramayan 0.529)
- **Original**: Canto XLV. The Tamasá. 511 Consult your weal and bliss and gain. In judgment old, in years a child, With hero virtues meek and mild, A fitting lord is he to cheer His people and remove their fear. In him all kingly gifts abound, More noble than in me are found: Imperial prince, well proved and tried— Obey him as your lord and guide. And grant, I pray, the boon I ask: To please the king be still your task, That his fond heart, while I remain Far in the wood, may feel no pain.” The more he showed his will to tread The path where filial duty led, The more the people, round him thronged, For their dear Ráma's empire longed. Still more attached his followers grew, As Ráma, with his brother, drew The people with his virtues' ties, Lamenting all with tear-dimmed eyes. The saintly twice-born, triply old In glory, knowledge, seasons told, With hoary heads that shook and bowed, Their voices raised and spake aloud: “O steeds, who best and noblest are, Who whirl so swiftly Ráma's car, Go not, return: we call on you: Be to your master kind and true. For speechless things are swift to hear, And naught can match a horse's ear, O generous steeds, return, when thus You hear the cry of all of us.
- **Translation**: 

---

### Verse 10 (Ramayan 0.530)
- **Original**: 512 The Ramayana Each vow he keeps most firm and sure, And duty makes his spirit pure. Back with our chief! not wood-ward hence; Back to his royal residence!” Soon as he saw the aged band. Exclaiming in their misery, stand, And their sad cries around him rang, Swift from his chariot Ráma sprang. Then, still upon his journey bent, With Sítá and with LakshmaG went The hero by the old men's side Suiting to theirs his shortened stride. He could not pass the twice-born throng As weariedly they walked along: With pitying heart, with tender eye, He could not in his chariot fly. When the steps of Ráma viewed That still his onward course pursued, Woe shook the troubled heart of each, And burnt with grief they spoke this speech— “With thee, O Ráma, to the wood All Bráhmans go and Bráhmanhood: Borne on our aged shoulders, see, Our fires of worship go with thee. Bright canopies that lend their shade In Vájapeya319 rites displayed, In plenteous store are borne behind Like cloudlets in the autumn wind. No shelter from the sun hast thou, And, lest his fury burn thy brow, These sacrificial shades we bear 319 An important sacrifice at which seventeen victims were immolated.
- **Translation**: 

---

### Verse 11 (Ramayan 0.531)
- **Original**: Canto XLV. The Tamasá. 513 Shall aid thee in the noontide glare. Our hearts, who ever loved to pore On sacred text and Vedic lore, Now all to thee, beloved, turn, And for a life in forests yearn. Deep in our aged bosoms lies The Vedas' lore, the wealth we prize, There still, like wives at home, shall dwell, Whose love and truth protect them well. [148] To follow thee our hearts are bent; We need not plan or argument. All else in duty's law we slight, For following thee is following right. O noble Prince, retrace thy way: O, hear us, Ráma, as we lay, With many tears and many prayers, Our aged heads and swan-white hairs Low in the dust before thy feet; O, hear us, Ráma, we entreat. Full many of these who with thee run, Their sacred rites had just begun. Unfinished yet those rites remain; But finished if thou turn again. All rooted life and things that move To thee their deep affection prove. To them, when warmed by love, they glow And sue to thee, some favour show, Each lowly bush, each towering tree Would follow too for love of thee. Bound by its root it must remain; But— all it can— its boughs complain, As when the wild wind rushes by It tells its woe in groan and sigh. No more through air the gay birds flit,
- **Translation**: 

---

### Verse 12 (Ramayan 0.532)
- **Original**: 514 The Ramayana But, foodless, melancholy sit Together on the branch and call To thee whose kind heart feels for all.” As wailed the aged Bráhmans, bent To turn him back, with wild lament, Seemed Tamasá herself to aid, Checking his progress, as they prayed. Sumantra from the chariot freed With ready hand each weary steed; He groomed them with the utmost heed, Their limbs he bathed and dried, Then led them forth to drink and feed At pleasure in the grassy mead That fringed the river side. Canto XLVI. The Halt. When Ráma, chief of Raghu's race, Arrived at that delightful place, He looked on Sítá first, and then To LakshmaG spake the lord of men: “Now first the shades of night descend Since to the wilds our steps we bend. Joy to thee, brother! do not grieve For our dear home and all we leave. The woods unpeopled seem to weep Around us, as their tenants creep Or fly to lair and den and nest, Both bird and beast, to seek their rest.
- **Translation**: 

---

### Verse 13 (Ramayan 0.533)
- **Original**: Canto XLVI. The Halt. 515 Methinks Ayodhyá's royal town Where dwells my sire of high renown, With all her men and dames to-night Will mourn us vanished from their sight. For, by his virtues won, they cling In fond affection to their king, And thee and me, O brave and true, And Bharat andZatrughna too. I for my sire and mother feel Deep sorrow o'er my bosom steal, Lest mourning us, oppressed with fears, They blind their eyes with endless tears. Yet Bharat's duteous love will show Sweet comfort in their hours of woe, And with kind words their hearts sustain, Suggesting duty, bliss, and gain. I mourn my parents now no more: I count dear Bharat's virtues o'er, And his kind love and care dispel The doubts I had, and all is well. And thou thy duty wouldst not shun, And, following me, hast nobly done; Else, bravest, I should need a band Around my wife as guard to stand. On this first night, my thirst to slake, Some water only will I take: Thus, brother, thus my will decides, Though varied store the wood provides.” Thus having said to LakshmaG, he Addressed in turn Sumantra:“Be Most diligent to-night, my friend, And with due care thy horses tend.” The sun had set: Sumantra tied
- **Translation**: 

---

### Verse 14 (Ramayan 0.534)
- **Original**: 516 The Ramayana His noble horses side by side, Gave store of grass with liberal hand, And rested near them on the strand. Each paid the holy evening rite, And when around them fell the night, The charioteer, with LakshmaG's aid, A lowly bed for Ráma laid. To LakshmaG Ráma bade adieu, And then by Sítá's side he threw His limbs upon the leafy bed Their care upon the bank had spread. When Lakshma G saw the couple slept, Still on the strand his watch he kept, Still with Sumantra there conversed, And Ráma's varied gifts rehearsed. All night he watched, nor sought repose, Till on the earth the sun arose: With him Sumantra stayed awake, And still of Ráma's virtues spake. Thus, near the river's grassy shore Which herds unnumbered wandered o'er, Repose, untroubled, Ráma found, And all the people lay around. The glorious hero left his bed, Looked on the sleeping crowd, and said To LakshmaG, whom each lucky line Marked out for bliss with surest sign: “O brother LakshmaG, look on these Reclining at the roots of trees; All care of house and home resigned, Caring for us with heart and mind, These people of the city yearn[149]
- **Translation**: 

---

### Verse 15 (Ramayan 0.535)
- **Original**: Canto XLVI. The Halt. 517 To see us to our home return: To quit their lives will they consent, But never leave their firm intent. Come, while they all unconscious sleep, Let us upon the chariot leap, And swiftly on our journey speed Where naught our progress may impede, That these fond citizens who roam Far from Ikshváku's ancient home, No more may sleep 'neath bush and tree, Following still for love of me. A prince with tender care should heal The self-brought woes his people feel, And never let his subjects share The burthen he is forced to bear.” Then LakshmaG to the chief replied, Who stood like Justice by his side: “Thy rede, O sage, I well commend: Without delay the car ascend.” Then Ráma to Sumantra spoke: “Thy rapid steeds, I pray thee, yoke. Hence to the forest will I go: Away, my lord, and be not slow.” Sumantra, urged to utmost speed, Yoked to the car each generous steed, And then, with hand to hand applied, He came before the chief and cried: “Hail, Prince, whom mighty arms adorn, Hail, bravest of the chariot-borne! With Sítá and thy brother thou Mayst mount: the car is ready now.”
- **Translation**: 

---

### Verse 16 (Ramayan 0.536)
- **Original**: 518 The Ramayana The hero clomb the car with haste: His bow and gear within were placed, And quick the eddying flood he passed Of Tamasá whose waves run fast. Soon as he touched the farther side, That strong-armed hero, glorified, He found a road both wide and clear, Where e'en the timid naught could fear. Then, that the crowd might be misled, Thus Ráma to Sumantra said: “Speed north a while, then hasten back, Returning in thy former track, That so the people may not learn The course I follow: drive and turn.” Sumantra, at the chief's behest, Quick to the task himself addressed; Then near to Ráma came, and showed The chariot ready for the road. With Sítá, then, the princely two, Who o'er the line of Raghu threw A glory ever bright and new, Upon the chariot stood. Sumantra fast and faster drove His horses, who in fleetness strove Still onward to the distant grove, The hermit-haunted wood. Canto XLVII. The Citizens' Return.
- **Translation**: 

---

### Verse 17 (Ramayan 0.537)
- **Original**: Canto XLVII. The Citizens' Return. 519 The people, when the morn shone fair, Arose to find no Ráma there. Then fear and numbing grief subdued The senses of the multitude. The woe-born tears were running fast As all around their eyes they cast, And sadly looked, but found no trace Of Ráma, searching every place. Bereft of Ráma good and wise, With drooping cheer and weeping eyes, Each woe-distracted sage gave vent To sorrow in his wild lament: “Woe worth the sleep that stole our sense With its beguiling influence, That now we look in vain for him Of the broad chest and stalwart limb! How could the strong-armed hero, thus Deceiving all, abandon us? His people so devoted see, Yet to the woods, a hermit, flee? How can he, wont our hearts to cheer, As a fond sire his children dear,— How can the pride of Raghu's race Fly from us to some desert place! Here let us all for death prepare, Or on the last great journey fare;320 Of Ráma our dear lord bereft, What profit in our lives is left? Huge trunks of trees around us lie, With roots and branches sere and dry, Come let us set these logs on fire And throw our bodies on the pyre. 320 The great pilgrimage to the Himálayas, in order to die there.
- **Translation**: 

---

### Verse 18 (Ramayan 0.538)
- **Original**: 520 The Ramayana What shall we speak? How can we say We followed Ráma on his way, The mighty chief whose arm is strong, Who sweetly speaks, who thinks no wrong? Ayodhyá's town with sorrow dumb, Without our lord will see us come, And hopeless misery will strike Elder, and child, and dame alike. Forth with that peerless chief we came, Whose mighty heart is aye the same: How, reft of him we love, shall we Returning dare that town to see?” Complaining thus with varied cry They tossed their aged arms on high, And their sad hearts with grief were wrung, Like cows who sorrow for their young. A while they followed on the road Which traces of his chariot showed, But when at length those traces failed, A deep despair their hearts assailed.[150] The chariot marks no more discerned, The hopeless sages backward turned: “Ah, what is this? What can we more? Fate stops the way, and all is o'er.” With wearied hearts, in grief and shame They took the road by which they came, And reached Ayodhyá's city, where From side to side was naught but care. With troubled spirits quite cast down They looked upon the royal town, And from their eyes, oppressed with woe, Their tears again began to flow. Of Ráma reft, the city wore
- **Translation**: 

---

### Verse 19 (Ramayan 0.539)
- **Original**: Canto XLVIII. The Women's Lament. 521 No look of beauty as before, Like a dull river or a lake By Garu robbed of every snake. Dark, dismal as the moonless sky, Or as a sea whose bed is dry, So sad, to every pleasure dead, They saw the town, disquieted. On to their houses, high and vast, Where stores of precious wealth were massed, The melancholy Bráhmans passed, Their hearts with anguish cleft: Aloof from all, they came not near To stranger or to kinsman dear, Showing in faces blank and drear That not one joy was left. Canto XLVIII. The Women's Lament. When those who forth with Ráma went Back to the town their steps had bent, It seemed that death had touched and chilled Those hearts which piercing sorrow filled. Each to his several mansion came, And girt by children and his dame, From his sad eyes the water shed That o'er his cheek in torrents spread. All joy was fled: oppressed with cares No bustling trader showed his wares. Each shop had lost its brilliant look, Each householder forbore to cook. No hand with joy its earnings told,
- **Translation**: 

---

### Verse 20 (Ramayan 0.540)
- **Original**: 522 The Ramayana None cared to win a wealth of gold, And scarce the youthful mother smiled To see her first, her new-born child. In every house a woman wailed, And her returning lord assailed With keen taunt piercing like the steel That bids the tusked monster kneel: “What now to them is wedded dame, What house and home and dearest aim, Or son, or bliss, or gathered store, Whose eyes on Ráma look no more! There is but one in all the earth, One man alone of real worth, Lakshma G, who follows, true and good, Ráma, with Sítá, through the wood. Made holy for all time we deem Each pool and fountain, lake and stream, If great Kakutstha's son shall choose Their water for his bath to use. Each forest, dark with lovely trees, Shall yearn Kakutstha's son to please; Each mountain peak and woody hill, Each mighty flood and mazy rill, Each rocky height, each shady grove Where the blest feet of Ráma rove, Shall gladly welcome with the best Of all they have their honoured guest. The trees that clustering blossoms bear, And bright-hued buds to gem their hair, The heart of Ráma shall delight, And cheer him on the breezy height. For him the upland slopes will show The fairest roots and fruit that grow, And all their wealth before him fling
- **Translation**: 

---

