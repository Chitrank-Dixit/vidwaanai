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

### Verse 1 (Ramayana 0.666)
- **Original**: 648 The Ramayana Canto LXXVI. The Funeral. The saint Va[ishmha, best of all Whose words with moving wisdom fall, Bharat, Kaikeyí's son, addressed, Whom burning fires of grief distressed: “O Prince, whose fame is widely spread, Enough of grief: be comforted. The time is come: arise, and lay Upon the pyre the monarch's clay.” He heard the words Va[ishmha spoke, And slumbering resolution woke. Then skilled in all the laws declare, He bade his friends the rites prepare. They raised the body from the oil, And placed it, dripping, on the soil; Then laid it on a bed, whereon Wrought gold and precious jewels shone. There, pallor o'er his features spread, The monarch, as in sleep, lay dead. Then Bharat sought his father's side, And lifted up his voice and cried: “O King, and has thy heart designed To part and leave thy son behind? Make Ráma flee, who loves the right, And Lakshma G of the arm of might? Whither, great Monarch, wilt thou go And leave this people in their woe, Mourning their hero, wild with grief, Of Ráma reft, their lion chief? Ah, who will guard the people well Who in Ayodhyá's city dwell, When thou, my sire, hast sought the sky,
- **Translation**: 

---

### Verse 2 (Ramayana 0.667)
- **Original**: Canto LXXVI. The Funeral. 649 And Ráma has been forced to fly? In widowed woe, bereft of thee, The land no more is fair to see: The city, to my aching sight, Is gloomy as a moonless night.” Thus, with o'erwhelming sorrow pained, Sad Bharat by the bed complained: And thus Va[ishmha, holy sage, Spoke his deep anguish to assuage: “O Lord of men, no longer stay; The last remaining duties pay: Haste, mighty-armed, as I advise, The funeral rites to solemnize.” And Bharat heard Va[ishmha's rede With due attention and agreed. He summoned straight from every side Chaplain, and priest, and holy guide. The sacred fires he bade them bring Forth from the chapel of the king, Wherein the priests in order due, And ministers, the offerings threw. Distraught in mind, with sob and tear, They laid the body on a bier, And servants, while their eyes brimmed o'er The monarch from the palace bore. Another band of mourners led The long procession of the dead: Rich garments in the way they cast, And gold and silver, as they passed. Then other hands the corse bedewed With fragrant juices that exude From sandal, cedar, aloe, pine,
- **Translation**: 

---

### Verse 3 (Ramayana 0.668)
- **Original**: 650 The Ramayana And every perfume rare and fine. Then priestly hands the mighty dead Upon the pyre deposited. The sacred fires they tended next, And muttered low each funeral text; And priestly singers who rehearse[186] The Zaman 352 sang their holy verse. Forth from the town in litters came, Or chariots, many a royal dame, And honoured so the funeral ground, With aged followers ringed around. With steps in inverse order bent,353 The priests in sad procession went Around the monarch's burning pyre Who well had nursed each sacred fire: With Queen Kau[alyá and the rest, Their tender hearts with woe distressed. The voice of women, shrill and clear As screaming curlews, smote the ear, As from a thousand voices rose The shriek that tells of woman's woes. Then weeping, faint, with loud lament, Down Sarjú's shelving bank they went. There standing on the river side With Bharat, priest, and peer, Their lips the women purified With water fresh and clear. Returning to the royal town, Their eyes with tear-drops filled, Ten days on earth they laid them down, And wept till grief was stilled. 352 The Sáma-veda, the hymns of which are chanted aloud. 353 Walking from right to left.
- **Translation**: 

---

### Verse 4 (Ramayana 0.669)
- **Original**: Canto LXXVII. The Gathering Of The Ashes. 651 Canto LXXVII. The Gathering Of The Ashes. The tenth day passed: the prince again Was free from every legal stain. He bade them on the twelfth the great Remaining honour celebrate. Much gold he gave, and gems, and food, To all the Bráhman multitude, And goats whose hair was white and fine, And many a thousand head of kine: Slaves, men and damsels, he bestowed, And many a car and fair abode: Such gifts he gave the Bráhman race His father's obsequies to grace. Then when the morning's earliest ray Appeared upon the thirteenth day, Again the hero wept and sighed Distraught and sorrow-stupefied; Drew, sobbing in his anguish, near, The last remaining debt to clear, And at the bottom of the pyre, He thus bespake his royal sire: “O father, hast thou left me so, Deserted in my friendless woe, When he to whom the charge was given To keep me, to the wood is driven? Her only son is forced away Who was his helpless mother's stay: Ah, whither, father, art thou fled; Leaving the queen uncomforted?”
- **Translation**: 

---

### Verse 5 (Ramayana 0.670)
- **Original**: 652 The Ramayana He looked upon the pile where lay The bones half-burnt and ashes grey, And uttering a piteous moan, Gave way, by anguish overthrown. Then as his tears began to well, Prostrate to earth the hero fell; So from its seat the staff they drag, And cast to earth some glorious flag. The ministers approached again The prince whom rites had freed from stain; So when Yayáti fell, each seer, In pity for his fate, drew near. Zatrughna saw him lying low O'erwhelmed beneath the crush of woe, And as upon the king he thought, He fell upon the earth distraught. When to his loving memory came Those noble gifts, that kingly frame, He sorrowed, by his woe distressed, As one by frenzied rage possessed: “Ah me, this surging sea of woe Has drowned us with its overflow: The source is Manthará, dire and dark, Kaikeyí is the ravening shark: And the great boons the monarch gave Lend conquering might to every wave. Ah, whither wilt thou go, and leave Thy Bharat in his woe to grieve, Whom ever 'twas thy greatest joy To fondle as a tender boy? Didst thou not give with thoughtful care Our food, our drink, our robes to wear? Whose love will now for us provide, When thou, our king and sire, hast died?
- **Translation**: 

---

### Verse 6 (Ramayana 0.671)
- **Original**: Canto LXXVII. The Gathering Of The Ashes. 653 At such a time bereft, forlorn, Why is not earth in sunder torn, Missing her monarch's firm control, His love of right, his lofty soul? Ah me, for Ráma roams afar, My sire is where the Blessed are; How can I live deserted? I Will pass into the fire and die. Abandoned thus, I will not brook Upon Ayodhyá's town to look, Once guarded by Ikshváku's race: The wood shall be my dwelling place.” Then when the princes' mournful train Heard the sad brothers thus complain, And saw their misery, at the view Their grief burst wilder out anew. Faint with lamenting, sad and worn, Each like a bull with broken horn, The brothers in their wild despair Lay rolling, mad with misery, there. Then old Va[ishmha good and true, Their father's priest, all lore who knew, Raised weeping Bharat on his feet, And thus bespake with counsel meet: “Twelve days, my lord, have past away [187] Since flames consumed thy father's clay: Delay no more: as rules ordain, Gather what bones may yet remain. Three constant pairs are ever found To hem all mortal creatures round:354 Then mourn not thus, O Prince, for none Their close companionship may shun.” 354 Birth and death, pleasure and pain, loss and gain.
- **Translation**: 

---

### Verse 7 (Ramayana 0.672)
- **Original**: 654 The Ramayana Sumantra badeZatrughna rise, And soothed his soul with counsel wise, And skilled in truth, his hearer taught How all things are and come to naught. When rose each hero from the ground, A lion lord of men, renowned, He showed like Indra's flag,355 whereon Fierce rains have dashed and suns have shone. They wiped their red and weeping eyes, And gently made their sad replies: Then, urged to haste, the royal pair Performed the rites that claimed their care. Canto LXXVIII. Manthará Punished. Zatrughna thus to Bharat spake Who longed the forest road to take: “He who in woe was wont to give Strength to himself and all that live— Dear Ráma, true and pure in heart, Is banished by a woman's art. Yet here was LakshmaG, brave and strong, Could not his might prevent the wrong? Could not his arm the king restrain, Or make the banished free again? One loving right and fearing crime Had checked the monarch's sin in time, When, vassal of a woman's will, His feet approached the path of ill.” 355 Erected upon a tree or high staff in honour of Indra.
- **Translation**: 

---

### Verse 8 (Ramayana 0.673)
- **Original**: Canto LXXVIII. Manthará Punished. 655 While LakshmaG's younger brother, dread Zatrughna, thus to Bharat said, Came to the fronting door, arrayed In glittering robes, the hump-back maid. There she, with sandal-oil besmeared, In garments meet for queens appeared: And lustre to her form was lent By many a gem and ornament. She girdled with her broidered zone, And many a chain about her thrown, Showed like a female monkey round Whose body many a string is bound. When on that cause of evil fell The quick eye of the sentinel, He grasped her in his ruthless hold, And hastening in,Zatrughna told: “Here is the wicked pest,” he cried, “Through whom the king thy father died, And Ráma wanders in the wood: Do with her as thou deemest good.” The warder spoke: and every word Zatrughna's breast to fury stirred: He called the servants, all and each. And spake in wrath his hasty speech: “This is the wretch my sire who slew, And misery on my brothers drew: Let her this day obtain the meed, Vile sinner, of her cruel deed.” He spake; and moved by fury laid His mighty hand upon the maid, Who as her fellows ringed her round, Made with her cries the hall resound. Soon as the gathered women viewed Zatrughna in his angry mood,
- **Translation**: 

---

### Verse 9 (Ramayana 0.674)
- **Original**: 656 The Ramayana Their hearts disturbed by sudden dread, They turned and from his presence fled. “His rage,” they cried,“on us will fall, And ruthless, he will slay us all. Come, to Kau[alyá let us flee: Our hope, our sure defence is she, Approved by all, of virtuous mind, Compassionate, and good, and kind.” His eyes with burning wrath aglow, Zatrughna, shatterer of the foe, Dragged on the ground the hump-back maid Who shrieked aloud and screamed for aid. This way and that with no remorse He dragged her with resistless force, And chains and glittering trinkets burst Lay here and there with gems dispersed, Till like the sky of Autumn shone The palace floor they sparkled on. The lord of men, supremely strong, Haled in his rage the wretch along: Where Queen Kaikeyí dwelt he came, And sternly then addressed the dame. Deep in her heart Kaikeyí felt The stabs his keen reproaches dealt, And ofZatrughna's ire afraid, To Bharat flew and cried for aid. He looked and saw the prince inflamed With burning rage, and thus exclaimed: “Forgive! thine angry arm restrain: A woman never may be slain. My hand Kaikeyí's blood would spill, The sinner ever bent on ill, But Ráma, long in duty tried,
- **Translation**: 

---

### Verse 10 (Ramayana 0.675)
- **Original**: Canto LXXIX. Bharat's Commands. 657 Would hate the impious matricide: And if he knew thy vengeful blade Had slaughtered e'en this hump-back maid, Never again, be sure, would he Speak friendly word to thee or me.” When Bharat's speechZatrughna heard He calmed the rage his breast that stirred, [188] Releasing from her dire constraint The trembling wretch with terror faint. Then to Kaikeyí's feet she crept, And prostrate in her misery wept. Kaikeyí on the hump-back gazed, And saw her weep and gasp. Still quivering, with her senses dazed, From fierceZatrughna's grasp. With gentle words of pity she Assuaged her wild despair, E'en as a tender hand might free A curlew from the snare. Canto LXXIX. Bharat's Commands. Now when the sun's returning ray Had ushered in the fourteenth day, The gathered peers of state addressed To Bharat's ear their new request: “Our lord to heaven has parted hence, Long served with deepest reverence; Ráma, the eldest, far from home, And Lakshma G, in the forest roam.
- **Translation**: 

---

### Verse 11 (Ramayana 0.676)
- **Original**: 658 The Ramayana O Prince, of mighty fame, be thou Our guardian and our monarch now, Lest secret plot or foeman's hate Assail our unprotected state. With longing eyes, O Lord of men, To thee look friend and citizen, And ready is each sacred thing To consecrate our chosen king. Come, Bharat, and accept thine own Ancient hereditary throne. Thee let the priests this day install As monarch to preserve us all.” Around the sacred gear he bent His circling footsteps reverent, And, firm to vows he would not break, Thus to the gathered people spake: “The eldest son is ever king: So rules the house from which we spring: Nor should ye, Lords, like men unwise, With words like these to wrong advise. Ráma is eldest born, and he The ruler of the land shall be. Now to the woods will I repair, Five years and nine to lodge me there. Assemble straight a mighty force, Cars, elephants, and foot and horse, For I will follow on his track And bring my eldest brother back. Whate'er the rites of throning need Placed on a car the way shall lead: The sacred vessels I will take To the wild wood for Ráma's sake. I o'er the lion prince's head
- **Translation**: 

---

### Verse 12 (Ramayana 0.677)
- **Original**: Canto LXXX. The Way Prepared. 659 The sanctifying balm will shed, And bring him, as the fire they bring Forth from the shrine, with triumphing. Nor will I let my mother's greed In this her cherished aim succeed: In pathless wilds will I remain, And Ráma here as king shall reign. To make the rough ways smooth and clear Send workman out and pioneer: Let skilful men attend beside Our way through pathless spots to guide.” As thus the royal Bharat spake, Ordaining all for Ráma's sake, The audience gave with one accord Auspicious answer to their lord: “Be royal Fortune aye benign To thee for this good speech of thine, Who wishest still thine elder's hand To rule with kingly sway the land.” Their glorious speech, their favouring cries Made his proud bosom swell: And from the prince's noble eyes The tears of rapture fell.356 Canto LXXX. The Way Prepared. 356 I follow in this stanza the Bombay edition in preference to Schlegel's which gives the tears of joy to the courtiers.
- **Translation**: 

---

### Verse 13 (Ramayana 0.678)
- **Original**: 660 The Ramayana All they who knew the joiner's art, Or distant ground in every part; Each busied in his several trade, To work machines or ply the spade; Deft workmen skilled to frame the wheel, Or with the ponderous engine deal; Guides of the way, and craftsmen skilled, To sink the well, make bricks, and build; And those whose hands the tree could hew, And work with slips of cut bamboo, Went forward, and to guide them, they Whose eyes before had seen the way. Then onward in triumphant mood Went all the mighty multitude. Like the great sea whose waves leap high When the full moon is in the sky. Then, in his proper duty skilled, Each joined him to his several guild, And onward in advance they went With every tool and implement. Where bush and tangled creeper lay With trenchant steel they made the way; They felled each stump, removed each stone, And many a tree was overthrown. In other spots, on desert lands, Tall trees were reared by busy hands. Where'er the line of road they took, They plied the hatchet, axe, and hook.[189] Others, with all their strength applied, Cast vigorous plants and shrubs aside, In shelving valleys rooted deep, And levelled every dale and steep. Each pit and hole that stopped the way They filled with stones, and mud, and clay,
- **Translation**: 

---

### Verse 14 (Ramayana 0.679)
- **Original**: Canto LXXX. The Way Prepared. 661 And all the ground that rose and fell With busy care was levelled well. They bridged ravines with ceaseless toil, And pounded fine the flinty soil. Now here, now there, to right and left, A passage through the ground they cleft, And soon the rushing flood was led Abundant through the new-cut bed, Which by the running stream supplied With ocean's boundless waters vied. In dry and thirsty spots they sank Full many a well and ample tank, And altars round about them placed To deck the station in the waste. With well-wrought plaster smoothly spread, With bloomy trees that rose o'erhead, With banners waving in the air, And wild birds singing here and there, With fragrant sandal-water wet, With many a flower beside it set, Like the Gods' heavenly pathway showed That mighty host's imperial road. Deft workmen, chosen for their skill To do the high-souled Bharat's will, In every pleasant spot where grew Trees of sweet fruit and fair to view, As he commanded, toiled to grace With all delights his camping-place. And they who read the stars, and well Each lucky sign and hour could tell, Raised carefully the tented shade Wherein high-minded Bharat stayed. With ample space of level ground, With broad deep moat encompassed round;
- **Translation**: 

---

### Verse 15 (Ramayana 0.680)
- **Original**: 662 The Ramayana Like Mandar in his towering pride, With streets that ran from side to side; Enwreathed with many a palace tall Surrounded by its noble wall; With roads by skilful workmen made, Where many a glorious banner played; With stately mansions, where the dove Sat nestling in her cote above. Rising aloft supremely fair Like heavenly cars that float in air, Each camp in beauty and in bliss Matched Indra's own metropolis. As shines the heaven on some fair night, With moon and constellations filled, The prince's royal road was bright, Adorned by art of workmen skilled. Canto LXXXI. The Assembly. Ere yet the dawn had ushered in The day should see the march begin, Herald and bard who rightly knew Each nice degree of honour due, Their loud auspicious voices raised, And royal Bharat blessed and praised. With sticks of gold the drum they smote, Which thundered out its deafening note, Blew loud the sounding shell, and blent Each high and low-toned instrument. The mingled sound of drum and horn Through all the air was quickly borne,
- **Translation**: 

---

### Verse 16 (Ramayana 0.681)
- **Original**: Canto LXXXI. The Assembly. 663 And as in Bharat's ear it rang, Gave the sad prince another pang. Then Bharat, starting from repose, Stilled the glad sounds that round him rose, “I am not king; no more mistake:” Then toZatrughna thus he spake: “O see what general wrongs succeed Sprung from Kaikeyí's evil deed! The king my sire has died and thrown Fresh miseries on me alone. The royal bliss, on duty based, Which our just high-souled father graced, Wanders in doubt and sore distress Like a tossed vessel rudderless. And he who was our lordly stay Roams in the forest far away, Expelled by this my mother, who To duty's law is most untrue.” As royal Bharat thus gave vent To bitter grief in wild lament, Gazing upon his face the crowd Of pitying women wept aloud. His lamentation scarce was o'er, When Saint Va[ishmha, skilled in lore Of royal duty, dear to fame, To join the great assembly came. Girt by disciples ever true Still nearer to that hall he drew, Resplendent, heavenly to behold, Adorned with wealth of gems and gold: E'en so a man in duty tried Draws near to meet his virtuous bride.
- **Translation**: 

---

### Verse 17 (Ramayana 0.682)
- **Original**: 664 The Ramayana He reached his golden seat o'erlaid With coverlet of rich brocade, There sat, in all the Vedas read, And called the messengers, and said: “Go forth, let Bráhman, Warrior, peer, And every captain gather here: Let all attentive hither throng: Go, hasten: we delay too long. Zatrughna, glorious Bharat bring, The noble children of the king,357[190] Yudhájit358 and Sumantra, all The truthful and the virtuous call.” He ended: soon a mighty sound Of thickening tumult rose around, As to the hall they bent their course With car, and elephant, and horse, The people all with glad acclaim Welcomed Prince Bharat as he came: E'en as they loved their king to greet, Or as the Gods Lord Indra359 meet. The vast assembly shone as fair With Bharat's kingly face As Da[aratha's self were there To glorify the place. It gleamed like some unruffled lake Where monsters huge of mould With many a snake their pastime take O'er shells, sand, gems, and gold. 357 The commentator says“Zatrughna accompanied by the other sons of the king.” 358 Not Bharat's uncle, but some councillor. 359 Zatakratu, Lord of a hundred sacrifices, the performance of a hundred A[vamedhas or sacrifices of a horse entitling the sacrificer to this exalted dignity.
- **Translation**: 

---

### Verse 18 (Ramayana 0.683)
- **Original**: Canto LXXXII. The Departure. 665 Canto LXXXII. The Departure. The prudent prince the assembly viewed Thronged with its noble multitude, Resplendent as a cloudless night When the full moon is in his height; While robes of every varied hue A glory o'er the synod threw. The priest in lore of duty skilled Looked on the crowd the hall that filled, And then in accents soft and grave To Bharat thus his counsel gave: “The king, dear son, so good and wise, Has gone from earth and gained the skies, Leaving to thee, her rightful lord, This rich wide land with foison stored. And still has faithful Ráma stood Firm to the duty of the good, And kept his father's hest aright, As the moon keeps its own dear light. Thus sire and brother yield to thee This realm from all annoyance free: Rejoice thy lords: enjoy thine own: Anointed king, ascend the throne. Let vassal Princes hasten forth From distant lands, west, south, and north, From Kerala,360 from every sea, And bring ten million gems to thee.” As thus the sage Va[ishmha spoke, A storm of grief o'er Bharat broke. And longing to be just and true, His thoughts to duteous Ráma flew. 360 The modern Malabar.
- **Translation**: 

---

### Verse 19 (Ramayana 0.684)
- **Original**: 666 The Ramayana With sobs and sighs and broken tones, E'en as a wounded mallard moans, He mourned with deepest sorrow moved, And thus the holy priest reproved: “O, how can such as Bharat dare The power and sway from him to tear, Wise, and devout, and true, and chaste, With Scripture lore and virtue graced? Can one of Da[aratha's seed Be guilty of so vile a deed? The realm and I are Ráma's: thou, Shouldst speak the words of justice now. For he, to claims of virtue true, Is eldest born and noblest too: Nahush, Dilípa could not be More famous in their lives than he. As Da[aratha ruled of right, So Ráma's is the power and right. If I should do this sinful deed And forfeit hope of heavenly meed, My guilty act would dim the shine Of old Ikshváku's glorious line. Nay, as the sin my mother wrought Is grievous to my inmost thought, I here, my hands together laid, Will greet him in the pathless shade. To Ráma shall my steps be bent, My King, of men most excellent, Raghu's illustrious son, whose sway Might hell, and earth, and heaven obey.” That righteous speech, whose every word Bore virtue's stamp, the audience heard; On Ráma every thought was set,
- **Translation**: 

---

### Verse 20 (Ramayana 0.685)
- **Original**: Canto LXXXII. The Departure. 667 And with glad tears each eye was wet. “Then, if the power I still should lack To bring my noble brother back, I in the wood will dwell, and share His banishment with LakshmaG there. By every art persuasive I To bring him from the wood will try, And show him to your loving eyes, O Bráhmans noble, good, and wise. E'en now, the road to make and clear, Each labourer pressed, and pioneer Have I sent forward to precede The army I resolve to lead.” Thus, by fraternal love possessed, His firm resolve the prince expressed, Then to Sumantra, deeply read In holy texts, he turned and said: “Sumantra, rise without delay, And as I bid my words obey. Give orders for the march with speed, And all the army hither lead.” The wise Sumantra, thus addressed, Obeyed the high-souled chief's behest. He hurried forth with joy inspired And gave the orders he desired. Delight each soldier's bosom filled, And through each chief and captain thrilled, [191]
- **Translation**: 

---

