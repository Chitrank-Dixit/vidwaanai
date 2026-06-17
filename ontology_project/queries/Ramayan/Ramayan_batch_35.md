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

### Verse 1 (Ramayan 0.681)
- **Original**: Canto LXXXI. The Assembly. 663 And as in Bharat's ear it rang, Gave the sad prince another pang. Then Bharat, starting from repose, Stilled the glad sounds that round him rose, “I am not king; no more mistake:” Then toZatrughna thus he spake: “O see what general wrongs succeed Sprung from Kaikeyí's evil deed! The king my sire has died and thrown Fresh miseries on me alone. The royal bliss, on duty based, Which our just high-souled father graced, Wanders in doubt and sore distress Like a tossed vessel rudderless. And he who was our lordly stay Roams in the forest far away, Expelled by this my mother, who To duty's law is most untrue.” As royal Bharat thus gave vent To bitter grief in wild lament, Gazing upon his face the crowd Of pitying women wept aloud. His lamentation scarce was o'er, When Saint Va[ishmha, skilled in lore Of royal duty, dear to fame, To join the great assembly came. Girt by disciples ever true Still nearer to that hall he drew, Resplendent, heavenly to behold, Adorned with wealth of gems and gold: E'en so a man in duty tried Draws near to meet his virtuous bride.
- **Translation**: 

---

### Verse 2 (Ramayan 0.682)
- **Original**: 664 The Ramayana He reached his golden seat o'erlaid With coverlet of rich brocade, There sat, in all the Vedas read, And called the messengers, and said: “Go forth, let Bráhman, Warrior, peer, And every captain gather here: Let all attentive hither throng: Go, hasten: we delay too long. Zatrughna, glorious Bharat bring, The noble children of the king,357[190] Yudhájit358 and Sumantra, all The truthful and the virtuous call.” He ended: soon a mighty sound Of thickening tumult rose around, As to the hall they bent their course With car, and elephant, and horse, The people all with glad acclaim Welcomed Prince Bharat as he came: E'en as they loved their king to greet, Or as the Gods Lord Indra359 meet. The vast assembly shone as fair With Bharat's kingly face As Da[aratha's self were there To glorify the place. It gleamed like some unruffled lake Where monsters huge of mould With many a snake their pastime take O'er shells, sand, gems, and gold. 357 The commentator says“Zatrughna accompanied by the other sons of the king.” 358 Not Bharat's uncle, but some councillor. 359 Zatakratu, Lord of a hundred sacrifices, the performance of a hundred A[vamedhas or sacrifices of a horse entitling the sacrificer to this exalted dignity.
- **Translation**: 

---

### Verse 3 (Ramayan 0.683)
- **Original**: Canto LXXXII. The Departure. 665 Canto LXXXII. The Departure. The prudent prince the assembly viewed Thronged with its noble multitude, Resplendent as a cloudless night When the full moon is in his height; While robes of every varied hue A glory o'er the synod threw. The priest in lore of duty skilled Looked on the crowd the hall that filled, And then in accents soft and grave To Bharat thus his counsel gave: “The king, dear son, so good and wise, Has gone from earth and gained the skies, Leaving to thee, her rightful lord, This rich wide land with foison stored. And still has faithful Ráma stood Firm to the duty of the good, And kept his father's hest aright, As the moon keeps its own dear light. Thus sire and brother yield to thee This realm from all annoyance free: Rejoice thy lords: enjoy thine own: Anointed king, ascend the throne. Let vassal Princes hasten forth From distant lands, west, south, and north, From Kerala,360 from every sea, And bring ten million gems to thee.” As thus the sage Va[ishmha spoke, A storm of grief o'er Bharat broke. And longing to be just and true, His thoughts to duteous Ráma flew. 360 The modern Malabar.
- **Translation**: 

---

### Verse 4 (Ramayan 0.684)
- **Original**: 666 The Ramayana With sobs and sighs and broken tones, E'en as a wounded mallard moans, He mourned with deepest sorrow moved, And thus the holy priest reproved: “O, how can such as Bharat dare The power and sway from him to tear, Wise, and devout, and true, and chaste, With Scripture lore and virtue graced? Can one of Da[aratha's seed Be guilty of so vile a deed? The realm and I are Ráma's: thou, Shouldst speak the words of justice now. For he, to claims of virtue true, Is eldest born and noblest too: Nahush, Dilípa could not be More famous in their lives than he. As Da[aratha ruled of right, So Ráma's is the power and right. If I should do this sinful deed And forfeit hope of heavenly meed, My guilty act would dim the shine Of old Ikshváku's glorious line. Nay, as the sin my mother wrought Is grievous to my inmost thought, I here, my hands together laid, Will greet him in the pathless shade. To Ráma shall my steps be bent, My King, of men most excellent, Raghu's illustrious son, whose sway Might hell, and earth, and heaven obey.” That righteous speech, whose every word Bore virtue's stamp, the audience heard; On Ráma every thought was set,
- **Translation**: 

---

### Verse 5 (Ramayan 0.685)
- **Original**: Canto LXXXII. The Departure. 667 And with glad tears each eye was wet. “Then, if the power I still should lack To bring my noble brother back, I in the wood will dwell, and share His banishment with LakshmaG there. By every art persuasive I To bring him from the wood will try, And show him to your loving eyes, O Bráhmans noble, good, and wise. E'en now, the road to make and clear, Each labourer pressed, and pioneer Have I sent forward to precede The army I resolve to lead.” Thus, by fraternal love possessed, His firm resolve the prince expressed, Then to Sumantra, deeply read In holy texts, he turned and said: “Sumantra, rise without delay, And as I bid my words obey. Give orders for the march with speed, And all the army hither lead.” The wise Sumantra, thus addressed, Obeyed the high-souled chief's behest. He hurried forth with joy inspired And gave the orders he desired. Delight each soldier's bosom filled, And through each chief and captain thrilled, [191]
- **Translation**: 

---

### Verse 6 (Ramayan 0.686)
- **Original**: 668 The Ramayana To hear that march proclaimed, to bring Dear Ráma back from wandering. From house to house the tidings flew: Each soldier's wife the order knew, And as she listened blithe and gay Her husband urged to speed away. Captain and soldier soon declared The host equipped and all prepared With chariots matching thought for speed, And wagons drawn by ox and steed. When Bharat by Va[ishmha's side, His ready host of warriors eyed, Thus in Sumantra's ear he spoke: “My car and horses quickly yoke.” Sumantra hastened to fulfil With ready joy his master's will, And quickly with the chariot sped Drawn by fleet horses nobly bred. Then glorious Bharat, true, devout, Whose genuine valour none could doubt, Gave in fit words his order out; For he would seek the shade Of the great distant wood, and there Win his dear brother with his prayer: “Sumantra, haste! my will declare The host be all arrayed. I to the wood my way will take, To Ráma supplication make, And for the world's advantage sake, Will lead him home again.” Then, ordered thus, the charioteer Who listened with delighted ear, Went forth and gave his orders clear To captains of the train.
- **Translation**: 

---

### Verse 7 (Ramayan 0.687)
- **Original**: Canto LXXXIII. The Journey Begun. 669 He gave the popular chiefs the word, And with the news his friends he stirred, And not a single man deferred Preparing for the road. Then Bráhman, Warrior, Merchant, thrall, Obedient to Sumantra's call, Each in his house arose, and all Yoked elephant or camel tall, Or ass or noble steed in stall, And full appointed showed. Canto LXXXIII. The Journey Begun. Then Bharat rose at early morn, And in his noble chariot borne Drove forward at a rapid pace Eager to look on Ráma's face. The priests and lords, a fair array, In sun-bright chariots led the way. Behind, a well appointed throng, Nine thousand elephants streamed along. Then sixty thousand cars, and then, With various arms, came fighting men. A hundred thousand archers showed In lengthened line the steeds they rode— A mighty host, the march to grace Of Bharat, pride of Raghu's race. Kaikeyí and Sumitrá came, And good Kau[alyá, dear to fame: By hopes of Ráma's coming cheered They in a radiant car appeared.
- **Translation**: 

---

### Verse 8 (Ramayan 0.688)
- **Original**: 670 The Ramayana On fared the noble host to see Ráma and LakshmaG, wild with glee, And still each other's ear to please, Of Ráma spoke in words like these: “When shall our happy eyes behold Our hero true, and pure, and bold, So lustrous dark, so strong of arm, Who keeps the world from woe and harm? The tears that now our eyeballs dim Will vanish at the sight of him, As the whole world's black shadows fly When the bright sun ascends the sky.” Conversing thus their way pursued The city's joyous multitude, And each in mutual rapture pressed A friend or neighbour to his breast. Thus every man of high renown, And every merchant of the town, And leading subjects, joyous went Toward Ráma in his banishment. And those who worked the potter's wheel, And artists skilled in gems to deal; And masters of the weaver's art, And those who shaped the sword and dart; And they who golden trinkets made, And those who plied the fuller's trade; And servants trained the bath to heat, And they who dealt in incense sweet; Physicians in their business skilled, And those who wine and mead distilled; And workmen deft in glass who wrought, And those whose snares the peacock caught; With them who bored the ear for rings,
- **Translation**: 

---

### Verse 9 (Ramayan 0.689)
- **Original**: Canto LXXXIII. The Journey Begun. 671 Or sawed, or fashioned ivory things; And those who knew to mix cement, Or lived by sale of precious scent; And men who washed, and men who sewed, And thralls who mid the herds abode; And fishers of the flood, and they Who played and sang, and women gay; And virtuous Bráhmans, Scripture-wise, Of life approved in all men's eyes; These swelled the prince's lengthened train, Borne each in car or bullock wain. Fair were the robes they wore upon Their limbs where red-hued unguents shone. These all in various modes conveyed Their journey after Bharat made; The soldiers' hearts with rapture glowed, Following Bharat on his road, Their chief whose tender love would fain Bring his dear brother home again. With elephant, and horse, and car, The vast procession travelled far, [192] And came where Gangá's waves below The town ofZringavera361 flow. There, with his friends and kinsmen nigh, Dwelt Guha, Ráma's dear ally, Heroic guardian of the land With dauntless heart and ready hand. There for a while the mighty force That followed Bharat stayed its course, Gazing on Gangá's bosom stirred By many a graceful water-bird. When Bharat viewed his followers there, 361 Now Sungroor, in the Allahabad district.
- **Translation**: 

---

### Verse 10 (Ramayan 0.690)
- **Original**: 672 The Ramayana And Gangá's water, blest and fair, The prince, who lore of words possessed, His councillors and lords addressed: “The captains of the army call: Proclaim this day a halt for all, That so to-morrow, rested, we May cross this flood that seeks the sea. Meanwhile, descending to the shore, The funeral stream I fain would pour From Gangá's fair auspicious tide To him, my father glorified.” Thus Bharat spoke: each peer and lord Approved his words with one accord, And bade the weary troops repose In separate spots where'er they chose. There by the mighty stream that day, Most glorious in its vast array The prince's wearied army lay In various groups reclined. There Bharat's hours of night were spent, While every eager thought he bent On bringing home from banishment His brother, great of mind. Canto LXXXIV. Guha's Anger.
- **Translation**: 

---

### Verse 11 (Ramayan 0.691)
- **Original**: Canto LXXXIV. Guha's Anger. 673 King Guha saw the host spread o'er The wide expanse of Gangá's shore, With waving flag and pennon graced, And to his followers spoke in haste: “A mighty army meets my eyes, That rivals Ocean's self in size: Where'er I look my very mind No limit to the host can find. Sure Bharat with some evil thought His army to our land has brought. See, huge of form, his flag he rears, That like an Ebony-tree appears. He comes with bonds to take and chain, Or triumph o'er our people slain: And after, Ráma will he slay,— Him whom his father drove away: The power complete he longs to gain, And — task too hard— usurp the reign. So Bharat comes with wicked will His brother Ráma's blood to spill. But Ráma's slave and friend am I; He is my lord and dear ally. Keep here your watch in arms arrayed Near Gangá's flood to lend him aid, And let my gathered servants stand And line with troops the river strand. Here let the river keepers meet, Who flesh and roots and berries eat; A hundred fishers man each boat Of the five hundred here afloat, And let the youthful and the strong Assemble in defensive throng. But yet, if, free from guilty thought 'Gainst Ráma, he this land have sought,
- **Translation**: 

---

### Verse 12 (Ramayan 0.692)
- **Original**: 674 The Ramayana The prince's happy host to-day Across the flood shall make its way.” He spoke: then bearing in a dish A gift of honey, meat, and fish, The king of the Nishádas drew Toward Bharat for an interview. When Bharat's noble charioteer Observed the monarch hastening near, He duly, skilled in courteous lore, The tidings to his master bore: “This aged prince who hither bends His footsteps with a thousand friends, Knows, firm ally of Ráma, all That may in DaG ak wood befall: Therefore, Kakutstha's son, admit The monarch, as is right and fit: For doubtless he can clearly tell Where Ráma now and LakshmaG dwell.” When Bharat heard Sumantra's rede, To his fair words the prince agreed: “Go quickly forth,” he cried,“and bring Before my face the aged king.” King Guha, with his kinsmen near, Rejoiced the summoning to hear: He nearer drew, bowed low his head, And thus to royal Bharat said: “No mansions can our country boast, And unexpected comes thy host: But what we have I give thee all: Rest in the lodging of thy thrall. See, the Nishádas here have brought The fruit and roots their hands have sought:
- **Translation**: 

---

### Verse 13 (Ramayan 0.693)
- **Original**: Canto LXXXV. Guha And Bharat. 675 And we have woodland fare beside, And store of meat both fresh and dried. To rest their weary limbs, I pray This night at least thy host may stay: Then cheered with all we can bestow To-morrow thou with it mayst go.” Canto LXXXV. Guha And Bharat. Thus the Nishádas' king besought: The prince with spirit wisdom-fraught [193] Replied in seemly words that blent Deep matter with the argument: “Thou, friend of him whom I revere, With honours high hast met me here, For thou alone wouldst entertain And feed to-day so vast a train.” In such fair words the prince replied, Then, pointing to the path he cried: “Which way aright will lead my feet To Bharadvája's calm retreat; For all this land near Gangá's streams Pathless and hard to traverse seems?”
- **Translation**: 

---

### Verse 14 (Ramayan 0.694)
- **Original**: 676 The Ramayana Thus spoke the prince: King Guha heard Delighted every prudent word, And gazing on that forest wide, Raised suppliant hands, and thus replied: “My servants, all the ground who know, O glorious Prince, with thee shall go With constant care thy way to guide, And I will journey by thy side. But this thy host so wide dispread Wakes in my heart one doubt and dread, Lest, threatening Ráma good and great, Ill thoughts thy journey stimulate.” But when King Guha, ill at ease, Declared his fear in words like these, As pure as is the cloudless sky With soft voice Bharat made reply: “Suspect me not: ne'er come the time For me to plot so foul a crime! He is my eldest brother, he Is like a father dear to me. I go to lead my brother thence Who makes the wood his residence. No thought but this thy heart should frame: This simple truth my lips proclaim.” Then with glad cheer King Guha cried, With Bharat's answer gratified: “Blessed art thou: on earth I see None who may vie, O Prince, with thee, Who canst of thy free will resign The kingdom which unsought is thine. For this, a name that ne'er shall die, Thy glory through the worlds shall fly,
- **Translation**: 

---

### Verse 15 (Ramayan 0.695)
- **Original**: Canto LXXXV. Guha And Bharat. 677 Who fain wouldst balm thy brother's pain And lead the exile home again.” As Guha thus, and Bharat, each To other spoke in friendly speech, The Day-God sank with glory dead, And night o'er all the sky was spread. Soon as King Guha's thoughtful care Had quartered all the army there, Well honoured, Bharat laid his head BesideZatrughna on a bed. But grief for Ráma yet oppressed High-minded Bharat's faithful breast— Such torment little was deserved By him who ne'er from duty swerved. The fever raged through every vein And burnt him with its inward pain: So when in woods the flames leap free The fire within consumes the tree. From heat of burning anguish sprung The sweat upon his body hung, As when the sun with fervid glow On high Himálaya melts the snow. As, banished from the herd, a bull Wanders alone and sorrowful. Thus sighing and distressed, In misery and bitter grief, With fevered heart that mocked relief, Distracted in his mind, the chief Still mourned and found no rest.
- **Translation**: 

---

### Verse 16 (Ramayan 0.696)
- **Original**: 678 The Ramayana Canto LXXXVI. Guha's Speech. Guha the king, acquainted well With all that in the wood befell, To Bharat the unequalled told The tale of LakshmaG mighty-souled: “With many an earnest word I spake To LakshmaG as he stayed awake, And with his bow and shaft in hand To guard his brother kept his stand: “Now sleep a little, LakshmaG, see This pleasant bed is strewn for thee: Hereon thy weary body lay, And strengthen thee with rest, I pray, Inured to toil are men like these, But thou hast aye been nursed in ease. Rest, duteous-minded! I will keep My watch while Ráma lies asleep: For in the whole wide world is none Dearer to me than Raghu's son. Harbour no doubt or jealous fear: I speak the truth with heart sincere: For from the grace which he has shown Will glory on my name be thrown: Great store of merit shall I gain, And duteous, form no wish in vain. Let me enforced by many a row Of followers, armed with shaft and bow For well-loved Ráma's weal provide Who lies asleep by Sítá's side. For through this wood I often go, And all its shades conceal I know: And we with conquering arms can meet A four-fold host arrayed complete.”
- **Translation**: 

---

### Verse 17 (Ramayan 0.697)
- **Original**: Canto LXXXVI. Guha's Speech. 679 “With words like these I spoke, designed To move the high-souled Bharat's mind, But he upon his duty bent, Plied his persuasive argument: “O, how can slumber close mine eyes When lowly couched with Sítá lies The royal Ráma? can I give My heart to joy, or even live? He whom no mighty demon, no, Nor heavenly God can overthrow, See, Guha, how he lies, alas, [194] With Sítá couched on gathered grass. By varied labours, long, severe, By many a prayer and rite austere, He, Da[aratha's cherished son, By Fortune stamped, from Heaven was won. Now as his son is forced to fly, The king ere long will surely die: Reft of his guardian hand, forlorn In widowed grief this land will mourn. E'en now perhaps, with toil o'erspent, The women cease their loud lament, And cries of woe no longer ring Throughout the palace of the king. But ah for sad Kau[alyá! how Fare she and mine own mother now? How fares the king? this night, I think, Some of the three in death will sink. With hopes uponZatrughna set My mother may survive as yet, But the sad queen will die who bore The hero, for her grief is sore. His cherished wish that would have made Dear Ráma king, so long delayed,
- **Translation**: 

---

### Verse 18 (Ramayan 0.698)
- **Original**: 680 The Ramayana “Too late! too late!” the king will cry, And conquered by his misery die. When Fate has brought the mournful day Which sees my father pass away, How happy in their lives are they Allowed his funeral rites to pay. Our exile o'er, with him who ne'er Turns from the oath his lips may swear, May we returning safe and well gain in fair Ayodhyá dwell.” Thus Bharat stood with many a sigh Lamenting, and the night went by. Soon as the morning light shone fair In votive coils both bound their hair. And then I sent them safely o'er And left them on the farther shore. With Sítá then they onward passed, Their coats of bark about them cast, Their locks like hermits' bound, The mighty tamers of the foe, Each with his arrows and his bow, Went over the rugged ground, Proud in their strength and undeterred Like elephants that lead the herd, And gazing oft around.” Canto LXXXVII. Guha's Story.
- **Translation**: 

---

### Verse 19 (Ramayan 0.699)
- **Original**: Canto LXXXVII. Guha's Story. 681 That speech of Guha Bharat heard With grief and tender pity stirred, And as his ears the story drank, Deep in his thoughtful heart it sank. His large full eyes in anguish rolled, His trembling limbs grew stiff and cold; Then fell he, like a tree uptorn, In woe too grievous to be borne. When Guha saw the long-armed chief Whose eye was like a lotus leaf, With lion shoulders strong and fair, High-mettled, prostrate in despair,— Pale, bitterly afflicted, he Reeled as in earthquake reels a tree. But whenZatrughna standing nigh Saw his dear brother helpless lie, Distraught with woe his head he bowed, Embraced him oft and wept aloud. Then Bharat's mothers came, forlorn Of their dear king, with fasting worn, And stood with weeping eyes around The hero prostrate on the ground. Kau [alyá, by her woe oppressed, The senseless Bharat's limbs caressed, As a fond cow in love and fear Caresses oft her youngling dear: Then yielding to her woe she said, Weeping and sore disquieted: “What torments, O my son, are these Of sudden pain or swift disease? The lives of us and all the line Depend, dear child, on only thine. Ráma and LakshmaG forced to flee, I live by naught but seeing thee:
- **Translation**: 

---

### Verse 20 (Ramayan 0.700)
- **Original**: 682 The Ramayana For as the king has past away Thou art my only help to-day. Hast thou, perchance, heard evil news Of LakshmaG, which thy soul subdues, Or Ráma dwelling with his spouse— My all is he— neath forest boughs?” Then slowly gathering sense and strength The weeping hero rose at length, And words like these to Guha spake, That bade Kau[alyá comfort take: “Where lodged the prince that night? and where Lakshma G the brave, and Sítá fair? Show me the couch whereon he lay, Tell me the food he ate, I pray.” Then Guha the Nishádas' king Replied to Bharat's questioning: “Of all I had I brought the best To serve my good and honoured guest Food of each varied kind I chose, And every fairest fruit that grows. Ráma the hero truly brave Declined the gift I humbly gave: His Warrior part he ne'er forgot, And what I brought accepted not: “No gifts, my friend, may we accept: Our law is, Give, and must be kept.” The high-souled chief, O Monarch, thus With gracious words persuaded us. Then calm and still, absorbed in thought, He drank the water LakshmaG brought, And then, obedient to his vows, He fasted with his gentle spouse. So LakshmaG too from food abstained,[195]
- **Translation**: 

---

