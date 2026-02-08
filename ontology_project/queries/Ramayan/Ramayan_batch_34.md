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

### Verse 1 (Ramayan 0.661)
- **Original**: Canto LXXV. The Abjuration. 643 Thus high-souled Bharat, mid the crowd, Lifted his voice and cried aloud.[184] Kau [alyá heard, she raised her head, And quickly to Sumitrá said: “Bharat, Kaikeyí's son is here,— Hers whose fell deeds I loathe and fear: That youth of foresight keen I fain Would meet and see his face again.” Thus to Sumitrá spake the dame, And straight to Bharat's presence came With altered mien, neglected dress, Trembling and faint with sore distress. Bharat,Zatrughna by his side, To meet her, toward her palace hied. And when the royal dame they viewed Distressed with dire solicitude, Sad, fallen senseless on the ground, About her neck their arms they wound. The noble matron prostrate there, Embraced, with tears, the weeping pair, And with her load of grief oppressed, To Bharat then these words addressed: “Now all is thine, without a foe, This realm for which thou longest so. Ah, soon Kaikeyí's ruthless hand Has won the empire of the land, And made my guiltless Ráma flee Dressed like some lonely devotee. Herein what profit has the queen, Whose eye delights in havoc, seen? Me also, me 'twere surely good To banish to the distant wood, To dwell amid the shades that hold My famous son with limbs like gold.
- **Translation**: 

---

### Verse 2 (Ramayan 0.662)
- **Original**: 644 The Ramayana Nay, with the sacred fire to guide, Will I, Sumitrá by my side, Myself to the drear wood repair And seek the son of Raghu there. This land which rice and golden corn And wealth of every kind adorn, Car, elephant, and steed, and gem,— She makes thee lord of it and them.” With taunts like these her bitter tongue The heart of blameless Bharat wrung And direr pangs his bosom tore Than when the lancet probes a sore. With troubled senses all astray Prone at her feet he fell and lay. With loud lament a while he plained, And slowly strength and sense regained. With suppliant hand to hand applied He turned to her who wept and sighed, And thus bespake the queen, whose breast With sundry woes was sore distressed: “Why these reproaches, noble dame? I, knowing naught, am free from blame. Thou knowest well what love was mine For Ráma, chief of Raghu's line. O, never be his darkened mind To Scripture's guiding lore inclined, By whose consent the prince who led The good, the truthful hero, fled. May he obey the vilest lord, Offend the sun with act abhorred,350 And strike a sleeping cow, who lent 350 Súryamcha pratimehatu, adversus solem mingat. An offence expressly forbidden by the Laws of Manu.
- **Translation**: 

---

### Verse 3 (Ramayan 0.663)
- **Original**: Canto LXXV. The Abjuration. 645 His voice to Ráma's banishment. May the good king who all befriends, And, like his sons, the people tends, Be wronged by him who gave consent To noble Ráma's banishment. On him that king's injustice fall, Who takes, as lord, a sixth of all, Nor guards, neglectful of his trust, His people, as a ruler must. The crime of those who swear to fee, At holy rites, some devotee, And then the promised gift deny, Be his who willed the prince should fly. When weapons clash and heroes bleed, With elephant and harnessed steed, Ne'er, like the good, be his to fight Whose heart allowed the prince's flight. Though taught with care by one expert May he the Veda's text pervert, With impious mind on evil bent, Whose voice approved the banishment. May he with traitor lips reveal Whate'er he promised to conceal, And bruit abroad his friend's offence, Betrayed by generous confidence. No wife of equal lineage born The wretch's joyless home adorn: Ne'er may he do one virtuous deed, And dying see no child succeed. When in the battle's awful day Fierce warriors stand in dread array, Let the base coward turn and fly, And smitten by the foeman, die. Long may he wander, rags his wear,
- **Translation**: 

---

### Verse 4 (Ramayan 0.664)
- **Original**: 646 The Ramayana Doomed in his hand a skull to bear, And like an idiot beg his bread, Who gave consent when Ráma fled. His sin who holy rites forgets, Asleep when shows the sun and sets, A load upon his soul shall lie Whose will allowed the prince to fly. His sin who loves his Master's dame, His, kindler of destructive flame, His who betrays his trusting friend Shall, mingled all, on him descend. By him no reverence due be paid To blessed God or parted shade: May sire and mother's sacred name In vain from him obedience claim. Ne'er may he go where dwell the good, Nor win their fame and neighbourhood, But lose all hopes of bliss to-day, Who willed the prince should flee away. May he deceive the poor and weak Who look to him and comfort seek,[185] Betray the suppliants who complain, And make the hopeful hope in vain. Long may his wife his kiss expect, And pine away in cold neglect. May he his lawful love despise, And turn on other dames his eyes, Fool, on forbidden joys intent, Whose will allowed the banishment. His sin who deadly poison throws To spoil the water as it flows, Lay on the wretch its burden dread Who gave consent when Ráma fled.”351 351 Bharat does not intend these curses for any particular person: he merely
- **Translation**: 

---

### Verse 5 (Ramayan 0.665)
- **Original**: Canto LXXV. The Abjuration. 647 Thus with his words he undeceived Kau [alyá's troubled heart, who grieved For son and husband reft away; Then prostrate on the ground he lay. Him as he lay half-senseless there, Freed by the mighty oaths he sware, Kau [alyá, by her woe distressed, With melancholy words addressed: “Anew, my son, this sorrow springs To rend my heart with keener stings: These awful oaths which thou hast sworn My breast with double grief have torn. Thy soul, and faithful LakshmaG's too, Are still, thank Heaven! to virtue true. True to thy promise, thou shalt gain The mansions which the good obtain.” Then to her breast that youth she drew, Whose sweet fraternal love she knew, And there in strict embraces held The hero, as her tears outwelled. And Bharat's heart grew sick and faint With grief and oft-renewed complaint, And all his senses were distraught By the great woe that in him wrought. Thus he lay and still bewailed With sighs and loud lament Till all his strength and reason failed, The hours of night were spent. wishes to prove his own innocence by invoking them on his own head if he had any share in banishing Ráma.
- **Translation**: 

---

### Verse 6 (Ramayan 0.666)
- **Original**: 648 The Ramayana Canto LXXVI. The Funeral. The saint Va[ishmha, best of all Whose words with moving wisdom fall, Bharat, Kaikeyí's son, addressed, Whom burning fires of grief distressed: “O Prince, whose fame is widely spread, Enough of grief: be comforted. The time is come: arise, and lay Upon the pyre the monarch's clay.” He heard the words Va[ishmha spoke, And slumbering resolution woke. Then skilled in all the laws declare, He bade his friends the rites prepare. They raised the body from the oil, And placed it, dripping, on the soil; Then laid it on a bed, whereon Wrought gold and precious jewels shone. There, pallor o'er his features spread, The monarch, as in sleep, lay dead. Then Bharat sought his father's side, And lifted up his voice and cried: “O King, and has thy heart designed To part and leave thy son behind? Make Ráma flee, who loves the right, And Lakshma G of the arm of might? Whither, great Monarch, wilt thou go And leave this people in their woe, Mourning their hero, wild with grief, Of Ráma reft, their lion chief? Ah, who will guard the people well Who in Ayodhyá's city dwell, When thou, my sire, hast sought the sky,
- **Translation**: 

---

### Verse 7 (Ramayan 0.667)
- **Original**: Canto LXXVI. The Funeral. 649 And Ráma has been forced to fly? In widowed woe, bereft of thee, The land no more is fair to see: The city, to my aching sight, Is gloomy as a moonless night.” Thus, with o'erwhelming sorrow pained, Sad Bharat by the bed complained: And thus Va[ishmha, holy sage, Spoke his deep anguish to assuage: “O Lord of men, no longer stay; The last remaining duties pay: Haste, mighty-armed, as I advise, The funeral rites to solemnize.” And Bharat heard Va[ishmha's rede With due attention and agreed. He summoned straight from every side Chaplain, and priest, and holy guide. The sacred fires he bade them bring Forth from the chapel of the king, Wherein the priests in order due, And ministers, the offerings threw. Distraught in mind, with sob and tear, They laid the body on a bier, And servants, while their eyes brimmed o'er The monarch from the palace bore. Another band of mourners led The long procession of the dead: Rich garments in the way they cast, And gold and silver, as they passed. Then other hands the corse bedewed With fragrant juices that exude From sandal, cedar, aloe, pine,
- **Translation**: 

---

### Verse 8 (Ramayan 0.668)
- **Original**: 650 The Ramayana And every perfume rare and fine. Then priestly hands the mighty dead Upon the pyre deposited. The sacred fires they tended next, And muttered low each funeral text; And priestly singers who rehearse[186] The Zaman 352 sang their holy verse. Forth from the town in litters came, Or chariots, many a royal dame, And honoured so the funeral ground, With aged followers ringed around. With steps in inverse order bent,353 The priests in sad procession went Around the monarch's burning pyre Who well had nursed each sacred fire: With Queen Kau[alyá and the rest, Their tender hearts with woe distressed. The voice of women, shrill and clear As screaming curlews, smote the ear, As from a thousand voices rose The shriek that tells of woman's woes. Then weeping, faint, with loud lament, Down Sarjú's shelving bank they went. There standing on the river side With Bharat, priest, and peer, Their lips the women purified With water fresh and clear. Returning to the royal town, Their eyes with tear-drops filled, Ten days on earth they laid them down, And wept till grief was stilled. 352 The Sáma-veda, the hymns of which are chanted aloud. 353 Walking from right to left.
- **Translation**: 

---

### Verse 9 (Ramayan 0.669)
- **Original**: Canto LXXVII. The Gathering Of The Ashes. 651 Canto LXXVII. The Gathering Of The Ashes. The tenth day passed: the prince again Was free from every legal stain. He bade them on the twelfth the great Remaining honour celebrate. Much gold he gave, and gems, and food, To all the Bráhman multitude, And goats whose hair was white and fine, And many a thousand head of kine: Slaves, men and damsels, he bestowed, And many a car and fair abode: Such gifts he gave the Bráhman race His father's obsequies to grace. Then when the morning's earliest ray Appeared upon the thirteenth day, Again the hero wept and sighed Distraught and sorrow-stupefied; Drew, sobbing in his anguish, near, The last remaining debt to clear, And at the bottom of the pyre, He thus bespake his royal sire: “O father, hast thou left me so, Deserted in my friendless woe, When he to whom the charge was given To keep me, to the wood is driven? Her only son is forced away Who was his helpless mother's stay: Ah, whither, father, art thou fled; Leaving the queen uncomforted?”
- **Translation**: 

---

### Verse 10 (Ramayan 0.670)
- **Original**: 652 The Ramayana He looked upon the pile where lay The bones half-burnt and ashes grey, And uttering a piteous moan, Gave way, by anguish overthrown. Then as his tears began to well, Prostrate to earth the hero fell; So from its seat the staff they drag, And cast to earth some glorious flag. The ministers approached again The prince whom rites had freed from stain; So when Yayáti fell, each seer, In pity for his fate, drew near. Zatrughna saw him lying low O'erwhelmed beneath the crush of woe, And as upon the king he thought, He fell upon the earth distraught. When to his loving memory came Those noble gifts, that kingly frame, He sorrowed, by his woe distressed, As one by frenzied rage possessed: “Ah me, this surging sea of woe Has drowned us with its overflow: The source is Manthará, dire and dark, Kaikeyí is the ravening shark: And the great boons the monarch gave Lend conquering might to every wave. Ah, whither wilt thou go, and leave Thy Bharat in his woe to grieve, Whom ever 'twas thy greatest joy To fondle as a tender boy? Didst thou not give with thoughtful care Our food, our drink, our robes to wear? Whose love will now for us provide, When thou, our king and sire, hast died?
- **Translation**: 

---

### Verse 11 (Ramayan 0.671)
- **Original**: Canto LXXVII. The Gathering Of The Ashes. 653 At such a time bereft, forlorn, Why is not earth in sunder torn, Missing her monarch's firm control, His love of right, his lofty soul? Ah me, for Ráma roams afar, My sire is where the Blessed are; How can I live deserted? I Will pass into the fire and die. Abandoned thus, I will not brook Upon Ayodhyá's town to look, Once guarded by Ikshváku's race: The wood shall be my dwelling place.” Then when the princes' mournful train Heard the sad brothers thus complain, And saw their misery, at the view Their grief burst wilder out anew. Faint with lamenting, sad and worn, Each like a bull with broken horn, The brothers in their wild despair Lay rolling, mad with misery, there. Then old Va[ishmha good and true, Their father's priest, all lore who knew, Raised weeping Bharat on his feet, And thus bespake with counsel meet: “Twelve days, my lord, have past away [187] Since flames consumed thy father's clay: Delay no more: as rules ordain, Gather what bones may yet remain. Three constant pairs are ever found To hem all mortal creatures round:354 Then mourn not thus, O Prince, for none Their close companionship may shun.” 354 Birth and death, pleasure and pain, loss and gain.
- **Translation**: 

---

### Verse 12 (Ramayan 0.672)
- **Original**: 654 The Ramayana Sumantra badeZatrughna rise, And soothed his soul with counsel wise, And skilled in truth, his hearer taught How all things are and come to naught. When rose each hero from the ground, A lion lord of men, renowned, He showed like Indra's flag,355 whereon Fierce rains have dashed and suns have shone. They wiped their red and weeping eyes, And gently made their sad replies: Then, urged to haste, the royal pair Performed the rites that claimed their care. Canto LXXVIII. Manthará Punished. Zatrughna thus to Bharat spake Who longed the forest road to take: “He who in woe was wont to give Strength to himself and all that live— Dear Ráma, true and pure in heart, Is banished by a woman's art. Yet here was LakshmaG, brave and strong, Could not his might prevent the wrong? Could not his arm the king restrain, Or make the banished free again? One loving right and fearing crime Had checked the monarch's sin in time, When, vassal of a woman's will, His feet approached the path of ill.” 355 Erected upon a tree or high staff in honour of Indra.
- **Translation**: 

---

### Verse 13 (Ramayan 0.673)
- **Original**: Canto LXXVIII. Manthará Punished. 655 While LakshmaG's younger brother, dread Zatrughna, thus to Bharat said, Came to the fronting door, arrayed In glittering robes, the hump-back maid. There she, with sandal-oil besmeared, In garments meet for queens appeared: And lustre to her form was lent By many a gem and ornament. She girdled with her broidered zone, And many a chain about her thrown, Showed like a female monkey round Whose body many a string is bound. When on that cause of evil fell The quick eye of the sentinel, He grasped her in his ruthless hold, And hastening in,Zatrughna told: “Here is the wicked pest,” he cried, “Through whom the king thy father died, And Ráma wanders in the wood: Do with her as thou deemest good.” The warder spoke: and every word Zatrughna's breast to fury stirred: He called the servants, all and each. And spake in wrath his hasty speech: “This is the wretch my sire who slew, And misery on my brothers drew: Let her this day obtain the meed, Vile sinner, of her cruel deed.” He spake; and moved by fury laid His mighty hand upon the maid, Who as her fellows ringed her round, Made with her cries the hall resound. Soon as the gathered women viewed Zatrughna in his angry mood,
- **Translation**: 

---

### Verse 14 (Ramayan 0.674)
- **Original**: 656 The Ramayana Their hearts disturbed by sudden dread, They turned and from his presence fled. “His rage,” they cried,“on us will fall, And ruthless, he will slay us all. Come, to Kau[alyá let us flee: Our hope, our sure defence is she, Approved by all, of virtuous mind, Compassionate, and good, and kind.” His eyes with burning wrath aglow, Zatrughna, shatterer of the foe, Dragged on the ground the hump-back maid Who shrieked aloud and screamed for aid. This way and that with no remorse He dragged her with resistless force, And chains and glittering trinkets burst Lay here and there with gems dispersed, Till like the sky of Autumn shone The palace floor they sparkled on. The lord of men, supremely strong, Haled in his rage the wretch along: Where Queen Kaikeyí dwelt he came, And sternly then addressed the dame. Deep in her heart Kaikeyí felt The stabs his keen reproaches dealt, And ofZatrughna's ire afraid, To Bharat flew and cried for aid. He looked and saw the prince inflamed With burning rage, and thus exclaimed: “Forgive! thine angry arm restrain: A woman never may be slain. My hand Kaikeyí's blood would spill, The sinner ever bent on ill, But Ráma, long in duty tried,
- **Translation**: 

---

### Verse 15 (Ramayan 0.675)
- **Original**: Canto LXXIX. Bharat's Commands. 657 Would hate the impious matricide: And if he knew thy vengeful blade Had slaughtered e'en this hump-back maid, Never again, be sure, would he Speak friendly word to thee or me.” When Bharat's speechZatrughna heard He calmed the rage his breast that stirred, [188] Releasing from her dire constraint The trembling wretch with terror faint. Then to Kaikeyí's feet she crept, And prostrate in her misery wept. Kaikeyí on the hump-back gazed, And saw her weep and gasp. Still quivering, with her senses dazed, From fierceZatrughna's grasp. With gentle words of pity she Assuaged her wild despair, E'en as a tender hand might free A curlew from the snare. Canto LXXIX. Bharat's Commands. Now when the sun's returning ray Had ushered in the fourteenth day, The gathered peers of state addressed To Bharat's ear their new request: “Our lord to heaven has parted hence, Long served with deepest reverence; Ráma, the eldest, far from home, And Lakshma G, in the forest roam.
- **Translation**: 

---

### Verse 16 (Ramayan 0.676)
- **Original**: 658 The Ramayana O Prince, of mighty fame, be thou Our guardian and our monarch now, Lest secret plot or foeman's hate Assail our unprotected state. With longing eyes, O Lord of men, To thee look friend and citizen, And ready is each sacred thing To consecrate our chosen king. Come, Bharat, and accept thine own Ancient hereditary throne. Thee let the priests this day install As monarch to preserve us all.” Around the sacred gear he bent His circling footsteps reverent, And, firm to vows he would not break, Thus to the gathered people spake: “The eldest son is ever king: So rules the house from which we spring: Nor should ye, Lords, like men unwise, With words like these to wrong advise. Ráma is eldest born, and he The ruler of the land shall be. Now to the woods will I repair, Five years and nine to lodge me there. Assemble straight a mighty force, Cars, elephants, and foot and horse, For I will follow on his track And bring my eldest brother back. Whate'er the rites of throning need Placed on a car the way shall lead: The sacred vessels I will take To the wild wood for Ráma's sake. I o'er the lion prince's head
- **Translation**: 

---

### Verse 17 (Ramayan 0.677)
- **Original**: Canto LXXX. The Way Prepared. 659 The sanctifying balm will shed, And bring him, as the fire they bring Forth from the shrine, with triumphing. Nor will I let my mother's greed In this her cherished aim succeed: In pathless wilds will I remain, And Ráma here as king shall reign. To make the rough ways smooth and clear Send workman out and pioneer: Let skilful men attend beside Our way through pathless spots to guide.” As thus the royal Bharat spake, Ordaining all for Ráma's sake, The audience gave with one accord Auspicious answer to their lord: “Be royal Fortune aye benign To thee for this good speech of thine, Who wishest still thine elder's hand To rule with kingly sway the land.” Their glorious speech, their favouring cries Made his proud bosom swell: And from the prince's noble eyes The tears of rapture fell.356 Canto LXXX. The Way Prepared. 356 I follow in this stanza the Bombay edition in preference to Schlegel's which gives the tears of joy to the courtiers.
- **Translation**: 

---

### Verse 18 (Ramayan 0.678)
- **Original**: 660 The Ramayana All they who knew the joiner's art, Or distant ground in every part; Each busied in his several trade, To work machines or ply the spade; Deft workmen skilled to frame the wheel, Or with the ponderous engine deal; Guides of the way, and craftsmen skilled, To sink the well, make bricks, and build; And those whose hands the tree could hew, And work with slips of cut bamboo, Went forward, and to guide them, they Whose eyes before had seen the way. Then onward in triumphant mood Went all the mighty multitude. Like the great sea whose waves leap high When the full moon is in the sky. Then, in his proper duty skilled, Each joined him to his several guild, And onward in advance they went With every tool and implement. Where bush and tangled creeper lay With trenchant steel they made the way; They felled each stump, removed each stone, And many a tree was overthrown. In other spots, on desert lands, Tall trees were reared by busy hands. Where'er the line of road they took, They plied the hatchet, axe, and hook.[189] Others, with all their strength applied, Cast vigorous plants and shrubs aside, In shelving valleys rooted deep, And levelled every dale and steep. Each pit and hole that stopped the way They filled with stones, and mud, and clay,
- **Translation**: 

---

### Verse 19 (Ramayan 0.679)
- **Original**: Canto LXXX. The Way Prepared. 661 And all the ground that rose and fell With busy care was levelled well. They bridged ravines with ceaseless toil, And pounded fine the flinty soil. Now here, now there, to right and left, A passage through the ground they cleft, And soon the rushing flood was led Abundant through the new-cut bed, Which by the running stream supplied With ocean's boundless waters vied. In dry and thirsty spots they sank Full many a well and ample tank, And altars round about them placed To deck the station in the waste. With well-wrought plaster smoothly spread, With bloomy trees that rose o'erhead, With banners waving in the air, And wild birds singing here and there, With fragrant sandal-water wet, With many a flower beside it set, Like the Gods' heavenly pathway showed That mighty host's imperial road. Deft workmen, chosen for their skill To do the high-souled Bharat's will, In every pleasant spot where grew Trees of sweet fruit and fair to view, As he commanded, toiled to grace With all delights his camping-place. And they who read the stars, and well Each lucky sign and hour could tell, Raised carefully the tented shade Wherein high-minded Bharat stayed. With ample space of level ground, With broad deep moat encompassed round;
- **Translation**: 

---

### Verse 20 (Ramayan 0.680)
- **Original**: 662 The Ramayana Like Mandar in his towering pride, With streets that ran from side to side; Enwreathed with many a palace tall Surrounded by its noble wall; With roads by skilful workmen made, Where many a glorious banner played; With stately mansions, where the dove Sat nestling in her cote above. Rising aloft supremely fair Like heavenly cars that float in air, Each camp in beauty and in bliss Matched Indra's own metropolis. As shines the heaven on some fair night, With moon and constellations filled, The prince's royal road was bright, Adorned by art of workmen skilled. Canto LXXXI. The Assembly. Ere yet the dawn had ushered in The day should see the march begin, Herald and bard who rightly knew Each nice degree of honour due, Their loud auspicious voices raised, And royal Bharat blessed and praised. With sticks of gold the drum they smote, Which thundered out its deafening note, Blew loud the sounding shell, and blent Each high and low-toned instrument. The mingled sound of drum and horn Through all the air was quickly borne,
- **Translation**: 

---

