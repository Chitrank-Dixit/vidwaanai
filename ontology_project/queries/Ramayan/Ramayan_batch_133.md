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

### Verse 1 (Ramayana 0.686)
- **Original**: 668 The Ramayana To hear that march proclaimed, to bring Dear Ráma back from wandering. From house to house the tidings flew: Each soldier's wife the order knew, And as she listened blithe and gay Her husband urged to speed away. Captain and soldier soon declared The host equipped and all prepared With chariots matching thought for speed, And wagons drawn by ox and steed. When Bharat by Va[ishmha's side, His ready host of warriors eyed, Thus in Sumantra's ear he spoke: “My car and horses quickly yoke.” Sumantra hastened to fulfil With ready joy his master's will, And quickly with the chariot sped Drawn by fleet horses nobly bred. Then glorious Bharat, true, devout, Whose genuine valour none could doubt, Gave in fit words his order out; For he would seek the shade Of the great distant wood, and there Win his dear brother with his prayer: “Sumantra, haste! my will declare The host be all arrayed. I to the wood my way will take, To Ráma supplication make, And for the world's advantage sake, Will lead him home again.” Then, ordered thus, the charioteer Who listened with delighted ear, Went forth and gave his orders clear To captains of the train.
- **Translation**: 

---

### Verse 2 (Ramayana 0.687)
- **Original**: Canto LXXXIII. The Journey Begun. 669 He gave the popular chiefs the word, And with the news his friends he stirred, And not a single man deferred Preparing for the road. Then Bráhman, Warrior, Merchant, thrall, Obedient to Sumantra's call, Each in his house arose, and all Yoked elephant or camel tall, Or ass or noble steed in stall, And full appointed showed. Canto LXXXIII. The Journey Begun. Then Bharat rose at early morn, And in his noble chariot borne Drove forward at a rapid pace Eager to look on Ráma's face. The priests and lords, a fair array, In sun-bright chariots led the way. Behind, a well appointed throng, Nine thousand elephants streamed along. Then sixty thousand cars, and then, With various arms, came fighting men. A hundred thousand archers showed In lengthened line the steeds they rode— A mighty host, the march to grace Of Bharat, pride of Raghu's race. Kaikeyí and Sumitrá came, And good Kau[alyá, dear to fame: By hopes of Ráma's coming cheered They in a radiant car appeared.
- **Translation**: 

---

### Verse 3 (Ramayana 0.688)
- **Original**: 670 The Ramayana On fared the noble host to see Ráma and LakshmaG, wild with glee, And still each other's ear to please, Of Ráma spoke in words like these: “When shall our happy eyes behold Our hero true, and pure, and bold, So lustrous dark, so strong of arm, Who keeps the world from woe and harm? The tears that now our eyeballs dim Will vanish at the sight of him, As the whole world's black shadows fly When the bright sun ascends the sky.” Conversing thus their way pursued The city's joyous multitude, And each in mutual rapture pressed A friend or neighbour to his breast. Thus every man of high renown, And every merchant of the town, And leading subjects, joyous went Toward Ráma in his banishment. And those who worked the potter's wheel, And artists skilled in gems to deal; And masters of the weaver's art, And those who shaped the sword and dart; And they who golden trinkets made, And those who plied the fuller's trade; And servants trained the bath to heat, And they who dealt in incense sweet; Physicians in their business skilled, And those who wine and mead distilled; And workmen deft in glass who wrought, And those whose snares the peacock caught; With them who bored the ear for rings,
- **Translation**: 

---

### Verse 4 (Ramayana 0.689)
- **Original**: Canto LXXXIII. The Journey Begun. 671 Or sawed, or fashioned ivory things; And those who knew to mix cement, Or lived by sale of precious scent; And men who washed, and men who sewed, And thralls who mid the herds abode; And fishers of the flood, and they Who played and sang, and women gay; And virtuous Bráhmans, Scripture-wise, Of life approved in all men's eyes; These swelled the prince's lengthened train, Borne each in car or bullock wain. Fair were the robes they wore upon Their limbs where red-hued unguents shone. These all in various modes conveyed Their journey after Bharat made; The soldiers' hearts with rapture glowed, Following Bharat on his road, Their chief whose tender love would fain Bring his dear brother home again. With elephant, and horse, and car, The vast procession travelled far, [192] And came where Gangá's waves below The town ofZringavera361 flow. There, with his friends and kinsmen nigh, Dwelt Guha, Ráma's dear ally, Heroic guardian of the land With dauntless heart and ready hand. There for a while the mighty force That followed Bharat stayed its course, Gazing on Gangá's bosom stirred By many a graceful water-bird. When Bharat viewed his followers there, 361 Now Sungroor, in the Allahabad district.
- **Translation**: 

---

### Verse 5 (Ramayana 0.690)
- **Original**: 672 The Ramayana And Gangá's water, blest and fair, The prince, who lore of words possessed, His councillors and lords addressed: “The captains of the army call: Proclaim this day a halt for all, That so to-morrow, rested, we May cross this flood that seeks the sea. Meanwhile, descending to the shore, The funeral stream I fain would pour From Gangá's fair auspicious tide To him, my father glorified.” Thus Bharat spoke: each peer and lord Approved his words with one accord, And bade the weary troops repose In separate spots where'er they chose. There by the mighty stream that day, Most glorious in its vast array The prince's wearied army lay In various groups reclined. There Bharat's hours of night were spent, While every eager thought he bent On bringing home from banishment His brother, great of mind. Canto LXXXIV. Guha's Anger.
- **Translation**: 

---

### Verse 6 (Ramayana 0.691)
- **Original**: Canto LXXXIV. Guha's Anger. 673 King Guha saw the host spread o'er The wide expanse of Gangá's shore, With waving flag and pennon graced, And to his followers spoke in haste: “A mighty army meets my eyes, That rivals Ocean's self in size: Where'er I look my very mind No limit to the host can find. Sure Bharat with some evil thought His army to our land has brought. See, huge of form, his flag he rears, That like an Ebony-tree appears. He comes with bonds to take and chain, Or triumph o'er our people slain: And after, Ráma will he slay,— Him whom his father drove away: The power complete he longs to gain, And — task too hard— usurp the reign. So Bharat comes with wicked will His brother Ráma's blood to spill. But Ráma's slave and friend am I; He is my lord and dear ally. Keep here your watch in arms arrayed Near Gangá's flood to lend him aid, And let my gathered servants stand And line with troops the river strand. Here let the river keepers meet, Who flesh and roots and berries eat; A hundred fishers man each boat Of the five hundred here afloat, And let the youthful and the strong Assemble in defensive throng. But yet, if, free from guilty thought 'Gainst Ráma, he this land have sought,
- **Translation**: 

---

### Verse 7 (Ramayana 0.692)
- **Original**: 674 The Ramayana The prince's happy host to-day Across the flood shall make its way.” He spoke: then bearing in a dish A gift of honey, meat, and fish, The king of the Nishádas drew Toward Bharat for an interview. When Bharat's noble charioteer Observed the monarch hastening near, He duly, skilled in courteous lore, The tidings to his master bore: “This aged prince who hither bends His footsteps with a thousand friends, Knows, firm ally of Ráma, all That may in DaG ak wood befall: Therefore, Kakutstha's son, admit The monarch, as is right and fit: For doubtless he can clearly tell Where Ráma now and LakshmaG dwell.” When Bharat heard Sumantra's rede, To his fair words the prince agreed: “Go quickly forth,” he cried,“and bring Before my face the aged king.” King Guha, with his kinsmen near, Rejoiced the summoning to hear: He nearer drew, bowed low his head, And thus to royal Bharat said: “No mansions can our country boast, And unexpected comes thy host: But what we have I give thee all: Rest in the lodging of thy thrall. See, the Nishádas here have brought The fruit and roots their hands have sought:
- **Translation**: 

---

### Verse 8 (Ramayana 0.693)
- **Original**: Canto LXXXV. Guha And Bharat. 675 And we have woodland fare beside, And store of meat both fresh and dried. To rest their weary limbs, I pray This night at least thy host may stay: Then cheered with all we can bestow To-morrow thou with it mayst go.” Canto LXXXV. Guha And Bharat. Thus the Nishádas' king besought: The prince with spirit wisdom-fraught [193] Replied in seemly words that blent Deep matter with the argument: “Thou, friend of him whom I revere, With honours high hast met me here, For thou alone wouldst entertain And feed to-day so vast a train.” In such fair words the prince replied, Then, pointing to the path he cried: “Which way aright will lead my feet To Bharadvája's calm retreat; For all this land near Gangá's streams Pathless and hard to traverse seems?”
- **Translation**: 

---

### Verse 9 (Ramayana 0.694)
- **Original**: 676 The Ramayana Thus spoke the prince: King Guha heard Delighted every prudent word, And gazing on that forest wide, Raised suppliant hands, and thus replied: “My servants, all the ground who know, O glorious Prince, with thee shall go With constant care thy way to guide, And I will journey by thy side. But this thy host so wide dispread Wakes in my heart one doubt and dread, Lest, threatening Ráma good and great, Ill thoughts thy journey stimulate.” But when King Guha, ill at ease, Declared his fear in words like these, As pure as is the cloudless sky With soft voice Bharat made reply: “Suspect me not: ne'er come the time For me to plot so foul a crime! He is my eldest brother, he Is like a father dear to me. I go to lead my brother thence Who makes the wood his residence. No thought but this thy heart should frame: This simple truth my lips proclaim.” Then with glad cheer King Guha cried, With Bharat's answer gratified: “Blessed art thou: on earth I see None who may vie, O Prince, with thee, Who canst of thy free will resign The kingdom which unsought is thine. For this, a name that ne'er shall die, Thy glory through the worlds shall fly,
- **Translation**: 

---

### Verse 10 (Ramayana 0.695)
- **Original**: Canto LXXXV. Guha And Bharat. 677 Who fain wouldst balm thy brother's pain And lead the exile home again.” As Guha thus, and Bharat, each To other spoke in friendly speech, The Day-God sank with glory dead, And night o'er all the sky was spread. Soon as King Guha's thoughtful care Had quartered all the army there, Well honoured, Bharat laid his head BesideZatrughna on a bed. But grief for Ráma yet oppressed High-minded Bharat's faithful breast— Such torment little was deserved By him who ne'er from duty swerved. The fever raged through every vein And burnt him with its inward pain: So when in woods the flames leap free The fire within consumes the tree. From heat of burning anguish sprung The sweat upon his body hung, As when the sun with fervid glow On high Himálaya melts the snow. As, banished from the herd, a bull Wanders alone and sorrowful. Thus sighing and distressed, In misery and bitter grief, With fevered heart that mocked relief, Distracted in his mind, the chief Still mourned and found no rest.
- **Translation**: 

---

### Verse 11 (Ramayana 0.696)
- **Original**: 678 The Ramayana Canto LXXXVI. Guha's Speech. Guha the king, acquainted well With all that in the wood befell, To Bharat the unequalled told The tale of LakshmaG mighty-souled: “With many an earnest word I spake To LakshmaG as he stayed awake, And with his bow and shaft in hand To guard his brother kept his stand: “Now sleep a little, LakshmaG, see This pleasant bed is strewn for thee: Hereon thy weary body lay, And strengthen thee with rest, I pray, Inured to toil are men like these, But thou hast aye been nursed in ease. Rest, duteous-minded! I will keep My watch while Ráma lies asleep: For in the whole wide world is none Dearer to me than Raghu's son. Harbour no doubt or jealous fear: I speak the truth with heart sincere: For from the grace which he has shown Will glory on my name be thrown: Great store of merit shall I gain, And duteous, form no wish in vain. Let me enforced by many a row Of followers, armed with shaft and bow For well-loved Ráma's weal provide Who lies asleep by Sítá's side. For through this wood I often go, And all its shades conceal I know: And we with conquering arms can meet A four-fold host arrayed complete.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.697)
- **Original**: Canto LXXXVI. Guha's Speech. 679 “With words like these I spoke, designed To move the high-souled Bharat's mind, But he upon his duty bent, Plied his persuasive argument: “O, how can slumber close mine eyes When lowly couched with Sítá lies The royal Ráma? can I give My heart to joy, or even live? He whom no mighty demon, no, Nor heavenly God can overthrow, See, Guha, how he lies, alas, [194] With Sítá couched on gathered grass. By varied labours, long, severe, By many a prayer and rite austere, He, Da[aratha's cherished son, By Fortune stamped, from Heaven was won. Now as his son is forced to fly, The king ere long will surely die: Reft of his guardian hand, forlorn In widowed grief this land will mourn. E'en now perhaps, with toil o'erspent, The women cease their loud lament, And cries of woe no longer ring Throughout the palace of the king. But ah for sad Kau[alyá! how Fare she and mine own mother now? How fares the king? this night, I think, Some of the three in death will sink. With hopes uponZatrughna set My mother may survive as yet, But the sad queen will die who bore The hero, for her grief is sore. His cherished wish that would have made Dear Ráma king, so long delayed,
- **Translation**: 

---

### Verse 13 (Ramayana 0.698)
- **Original**: 680 The Ramayana “Too late! too late!” the king will cry, And conquered by his misery die. When Fate has brought the mournful day Which sees my father pass away, How happy in their lives are they Allowed his funeral rites to pay. Our exile o'er, with him who ne'er Turns from the oath his lips may swear, May we returning safe and well gain in fair Ayodhyá dwell.” Thus Bharat stood with many a sigh Lamenting, and the night went by. Soon as the morning light shone fair In votive coils both bound their hair. And then I sent them safely o'er And left them on the farther shore. With Sítá then they onward passed, Their coats of bark about them cast, Their locks like hermits' bound, The mighty tamers of the foe, Each with his arrows and his bow, Went over the rugged ground, Proud in their strength and undeterred Like elephants that lead the herd, And gazing oft around.” Canto LXXXVII. Guha's Story.
- **Translation**: 

---

### Verse 14 (Ramayana 0.699)
- **Original**: Canto LXXXVII. Guha's Story. 681 That speech of Guha Bharat heard With grief and tender pity stirred, And as his ears the story drank, Deep in his thoughtful heart it sank. His large full eyes in anguish rolled, His trembling limbs grew stiff and cold; Then fell he, like a tree uptorn, In woe too grievous to be borne. When Guha saw the long-armed chief Whose eye was like a lotus leaf, With lion shoulders strong and fair, High-mettled, prostrate in despair,— Pale, bitterly afflicted, he Reeled as in earthquake reels a tree. But whenZatrughna standing nigh Saw his dear brother helpless lie, Distraught with woe his head he bowed, Embraced him oft and wept aloud. Then Bharat's mothers came, forlorn Of their dear king, with fasting worn, And stood with weeping eyes around The hero prostrate on the ground. Kau [alyá, by her woe oppressed, The senseless Bharat's limbs caressed, As a fond cow in love and fear Caresses oft her youngling dear: Then yielding to her woe she said, Weeping and sore disquieted: “What torments, O my son, are these Of sudden pain or swift disease? The lives of us and all the line Depend, dear child, on only thine. Ráma and LakshmaG forced to flee, I live by naught but seeing thee:
- **Translation**: 

---

### Verse 15 (Ramayana 0.700)
- **Original**: 682 The Ramayana For as the king has past away Thou art my only help to-day. Hast thou, perchance, heard evil news Of LakshmaG, which thy soul subdues, Or Ráma dwelling with his spouse— My all is he— neath forest boughs?” Then slowly gathering sense and strength The weeping hero rose at length, And words like these to Guha spake, That bade Kau[alyá comfort take: “Where lodged the prince that night? and where Lakshma G the brave, and Sítá fair? Show me the couch whereon he lay, Tell me the food he ate, I pray.” Then Guha the Nishádas' king Replied to Bharat's questioning: “Of all I had I brought the best To serve my good and honoured guest Food of each varied kind I chose, And every fairest fruit that grows. Ráma the hero truly brave Declined the gift I humbly gave: His Warrior part he ne'er forgot, And what I brought accepted not: “No gifts, my friend, may we accept: Our law is, Give, and must be kept.” The high-souled chief, O Monarch, thus With gracious words persuaded us. Then calm and still, absorbed in thought, He drank the water LakshmaG brought, And then, obedient to his vows, He fasted with his gentle spouse. So LakshmaG too from food abstained,[195]
- **Translation**: 

---

### Verse 16 (Ramayana 0.701)
- **Original**: Canto LXXXVIII. The Ingudí Tree. 683 And sipped the water that remained: Then with ruled lips, devoutly staid, The three362 their evening worship paid. Then LakshmaG with unwearied care Brought heaps of sacred grass, and there With his own hands he quickly spread, For Ráma's rest, a pleasant bed, And faithful Sítá's too, where they Reclining each by other lay. Then LakshmaG bathed their feet, and drew A little distance from the two. Here stands the tree which lent them shade, Here is the grass beneath it laid, Where Ráma and his consort spent The night together ere they went. Lakshma G, whose arms the foeman quell, Watched all the night as sentinel, And kept his great bow strung: His hand was gloved, his arm was braced, Two well-filled quivers at his waist, With deadly arrows, hung. I took my shafts and trusty bow, And with that tamer of the foe Stood ever wakeful near, And with my followers, bow in hand, Behind me ranged, a ready band, Kept watch o'er Indra's peer.” Canto LXXXVIII. The Ingudí Tree. 362 Ráma, LakshmaG, and Sumantra.
- **Translation**: 

---

### Verse 17 (Ramayana 0.702)
- **Original**: 684 The Ramayana When Bharat with each friend and peer Had heard that tale so full and clear, They went together to the tree The bed which Ráma pressed to see. Then Bharat to his mothers said: “Behold the high-souled hero's bed: These tumbled heaps of grass betray Where he that night with Sítá lay: Unmeet, the heir of fortune high Thus on the cold bare earth should lie, The monarch's son, in counsel sage, Of old imperial lineage. That lion-lord whose noble bed With finest skins of deer was spread,— How can he now endure to press The bare earth, cold and comfortless! This sudden fall from bliss to grief Appears untrue, beyond belief: My senses are distraught: I seem To view the fancies of a dream. There is no deity so great, No power in heaven can master Fate, If Ráma, Da[aratha's heir, Lay on the ground and slumbered there; And lovely Sítá, she who springs From fair Videha's ancient kings, Ráma's dear wife, by all adored, Lay on the earth beside her lord. Here was his couch, upon this heap He tossed and turned in restless sleep: On the hard soil each manly limb Has stamped the grass with signs of him. That night, it seems, fair Sítá spent Arrayed in every ornament,
- **Translation**: 

---

### Verse 18 (Ramayana 0.703)
- **Original**: Canto LXXXVIII. The Ingudí Tree. 685 For here and there my eyes behold Small particles of glistering gold. She laid her outer garment here, For still some silken threads appear, How dear in her devoted eyes Must be the bed where Ráma lies, Where she so tender could repose And by his side forget her woes. Alas, unhappy, guilty me! For whom the prince was forced to flee, And chief of Raghu's sons and best, A bed like this with Sítá pressed. Son of a royal sire whose hand Ruled paramount o'er every land, Could he who every joy bestows, Whose body like the lotus shows, The friend of all, who charms the sight, Whose flashing eyes are darkly bright, Leave the dear kingdom, his by right, Unmeet for woe, the heir of bliss, And lie upon a bed like this? Great joy and happy fate are thine, O Lakshma G, marked with each fair sign, Whose faithful footsteps follow still Thy brother in his hour of ill. And blest is Sítá, nobly good, Who dwells with Ráma in the wood. Ours is, alas, a doubtful fate Of Ráma reft and desolate. My royal sire has gained the skies, In woods the high-souled hero lies; The state is wrecked and tempest-tossed, A vessel with her rudder lost. Yet none in secret thought has planned
- **Translation**: 

---

### Verse 19 (Ramayana 0.704)
- **Original**: 686 The Ramayana With hostile might to seize the land: Though forced in distant wilds to dwell, The hero's arm protects it well. Unguarded, with deserted wall, No elephant or steed in stall, My father's royal city shows Her portals open to her foes, Of bold protectors reft and bare, Defenceless in her dark despair: But still her foes the wish restrain, As men from poisoned cates refrain. I from this hour my nights will pass Couched on the earth or gathered grass, Eat only fruit and roots, and wear A coat of bark, and matted hair. I in the woods will pass, content, For him the term of banishment; So shall I still unbroken save The promise which the hero gave.[196] While I remain for Ráma there, Zatrughna will my exile share, And Ráma in his home again, With LakshmaG, o'er Ayodhyá reign, for him, to rule and guard the state, The twice-born men shall consecrate. O, may the Gods I serve incline To grant this earnest wish of mine! If when I bow before his feet And with all moving arts entreat, He still deny my prayer, Then with my brother will I live: He must, he must permission give, Roaming in forests there.”
- **Translation**: 

---

### Verse 20 (Ramayana 0.705)
- **Original**: Canto LXXXIX. The Passage Of Gangá. 687 Canto LXXXIX. The Passage Of Gangá. That night the son of Raghu lay On Gangá's bank till break of day: Then with the earliest light he woke And thus to braveZatrughna spoke. “Rise up,Zatrughna, from thy bed: Why sleepest thou the night is fled. See how the sun who chases night Wakes every lotus with his light. Arise, arise, and first of all The lord ofZringavera call, For he his friendly aid will lend Our army o'er the flood to send.” Thus urged,Zatrughna answered:“I, Remembering Ráma, sleepless lie.” As thus the brothers, each to each, The lion-mettled, ended speech, Came Guha, the Nishádas' king, And spoke with kindly questioning: “Hast thou in comfort passed,” he cried, “The night upon the river side? With thee how fares it? and are these, Thy soldiers, healthy and at ease?” Thus the Nishádas' lord inquired In gentle words which love inspired, And Bharat, Ráma's faithful slave, Thus to the king his answer gave: “The night has sweetly passed, and we Are highly honoured, King, by thee. Now let thy servants boats prepare, Our army o'er the stream to bear.”
- **Translation**: 

---

