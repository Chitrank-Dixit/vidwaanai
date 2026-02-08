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

### Verse 1 (Ramayan 0.741)
- **Original**: Canto XCVII. Lakshman's Anger. 723 The suppliant I must still protect. But ne'er in vain this dart may flee; Yield for thy life a part of thee, What portion of thy body, say, Shall this mine arrow rend away? Thus far, O bird, thus far alone On thee my pity may be shown. Forfeit a part thy life to buy: 'Tis better so to live than die.” Thus Ráma spoke: the bird of air Pondered his speech with anxious care, And wisely deemed it good to give One of his eyes that he might live. To Raghu's son he made reply: “O Ráma, I will yield an eye. So let me in thy grace confide And live hereafter single-eyed.” Then Ráma charged the shaft, and lo, Full in the eye it smote the crow. And the Videhan lady gazed Upon the ruined eye amazed. The crow to Ráma humbly bent, Then where his fancy led he went. Ráma with LakshmaG by his side With needful work was occupied. Canto XCVII. Lakshman's Anger.
- **Translation**: 

---

### Verse 2 (Ramayan 0.742)
- **Original**: 724 The Ramayana Thus Ráma showed his love the rill Whose waters ran beneath the hill, Then resting on his mountain seat Refreshed her with the choicest meat. So there reposed the happy two: Then Bharat's army nearer drew: Rose to the skies a dusty cloud, The sound of trampling feet was loud. The swelling roar of marching men Drove the roused tiger from his den, And scared amain the serpent race Flying to hole and hiding-place. The herds of deer in terror fled, The air was filled with birds o'erhead, The bear began to leave his tree, The monkey to the cave to flee. Wild elephants were all amazed As though the wood around them blazed. The lion oped his ponderous jaw, The buffalo looked round in awe. The prince, who heard the deafening sound, And saw the silvan creatures round Fly wildly startled from their rest, The glorious LakshmaG thus addressed: “Sumitrá's noble son most dear, Hark, LakshmaG, what a roar I hear, The tumult of a coming crowd, Appalling, deafening, deep, and loud! The din that yet more fearful grows Scares elephants and buffaloes, Or frightened by the lions, deer Are flying through the wood in fear. I fain would know who seeks this place Comes prince or monarch for the chase?
- **Translation**: 

---

### Verse 3 (Ramayan 0.743)
- **Original**: Canto XCVII. Lakshman's Anger. 725 Or does some mighty beast of prey Frighten the silvan herds away? 'Tis hard to reach this mountain height, Yea, e'en for birds in airy flight. Then fain, O LakshmaG, would I know What cause disturbs the forest so.” Lakshma G in haste, the wood to view, Climbed a high Sál that near him grew, The forest all around he eyed, First gazing on the eastern side. Then northward when his eyes he bent He saw a mighty armament Of elephants, and cars, and horse, And men on foot, a mingled force, And banners waving in the breeze, And spoke to Ráma words like these: “Quick, quick, my lord, put out the fire, Let Sítá to the cave retire. [207] Thy coat of mail around thee throw, Prepare thine arrows and thy bow.” In eager haste thus LakshmaG cried, And Ráma, lion lord, replied: “Still closer be the army scanned, And say who leads the warlike band.” Lakshma G his answer thus returned, As furious rage within him burned, Exciting him like kindled fire To scorch the army in his ire: “'Tis Bharat: he has made the throne By consecrating rites his own: To gain the whole dominion thus He comes in arms to slaughter us.
- **Translation**: 

---

### Verse 4 (Ramayan 0.744)
- **Original**: 726 The Ramayana I mark tree-high upon his car His flagstaff of the Kovidár,376 I see his glittering banner glance, I see his chivalry advance: I see his eager warriors shine On elephants in lengthened line. Now grasp we each the shafts and bow, And higher up the mountain go. Or in this place, O hero, stand With weapons in each ready hand. Perhaps beneath our might may fall This leader of the standard tall, And Bharat I this day may see Who brought this mighty woe on thee, Sítá, and me, who drove away My brother from the royal sway. Bharat our foe at length is nigh, And by this hand shall surely die: Brother, I see no sin at all If Bharat by my weapon fall. No fault is his who slays the foe Whose hand was first to strike the blow: With Bharat now the crime begins Who against thee and duty sins. The queen athirst for royal sway Will see her darling son to-day Fall by this hand, like some fair tree Struck by an elephant, slain by me. Kaikeyí's self shall perish too With kith and kin and retinue, And earth by my avenging deed Shall from this mass of sin be freed. 376 Bauhinea variegata, a species of ebony.
- **Translation**: 

---

### Verse 5 (Ramayan 0.745)
- **Original**: Canto XCVIII. Lakshman Calmed. 727 This day my wrath, too long restrained, Shall fall upon the foe, unchained, Mad as the kindled flame that speeds Destroying through the grass and reeds. This day mine arrows keen and fierce The bodies of the foe shall pierce: The woods on Chitrakúma's side Shall run with torrents crimson-dyed. The wandering beasts of prey shall feed On heart-cleft elephant and steed, And drag to mountain caves away The bodies that my arrows slay. Doubt not that Bharat and his train Shall in this mighty wood be slain: So shall I pay the debt my bow And these my deadly arrows owe.” Canto XCVIII. Lakshman Calmed. Then Ráma nobly calm allayed The wrath that LakshmaG's bosom swayed: “What need have we the sword to wield, To bend the bow or lift the shield, If Bharat brave, and wise, and good, Himself has sought this sheltering wood? I sware my father's will to do, And if I now my brother slew What gain in kingship should I find, Despised and scorned by all mankind? Believe me, e'en as I would shrink From poisoned meat or deadly drink,
- **Translation**: 

---

### Verse 6 (Ramayan 0.746)
- **Original**: 728 The Ramayana No power or treasure would I win By fall of friend or kith or kin. Brother, believe the words I speak: For your dear sakes alone I seek Duty and pleasure, wealth and gain: A holy life, a happy reign. If royal sway my heart desires, My brothers' weal the wish inspires: Their bliss and safety is my care, By this uplifted bow I swear. 'Twere not so hard for me to gain This broad land girdled by the main, But even Indra's royal might Should ne'er be mine in duty's spite. If any bliss my soul can see Deprived of dearZatrughna, thee, And Bharat, may the flame destroy With ashy gloom the selfish joy. Far dearer than this life of mine, Knowing the custom of our line, His heart with fond affection fraught, Bharat Ayodhyá's town resought And hearing when he came that I, With thee and Sítá, forced to fly With matted hair and hermit dress Am wandering in the wilderness. While grief his troubled senses storms, And tender love his bosom warms, From every thought of evil clear, Is come to meet his brother here. Some grievous words perchance he spoke Kaikeyí's anger to provoke, Then won the king, and comes to lay Before my feet the royal sway.
- **Translation**: 

---

### Verse 7 (Ramayan 0.747)
- **Original**: Canto XCVIII. Lakshman Calmed. 729 Hither, methinks, in season due Comes Bharat for an interview, Nor in his secret heart has he One evil thought 'gainst thee or me. What has he done ere now, reflect! How failed in love or due respect [208] To make thee doubt his faith and lay This evil to his charge to-day? Thou shouldst not join with Bharat's name So harsh a speech and idle blame. The blows thy tongue at Bharat deals, My sympathizing bosom feels. How, urged by stress of any ill, Should sons their father's life-blood spill, Or brother slay in impious strife A brother dearer than his life? If thou these cruel words hast said By strong desire of empire led, My brother Bharat will I pray To give to thee the kingly sway. “Give him the realm,” my speech shall be, And Bharat will, methinks, agree.” Thus spoke the prince whose chief delight Was duty, and to aid the right: And Lakshma G keenly felt the blame, And shrank within himself for shame: And then his answer thus returned, With downcast eye and cheek that burned: “Brother, I ween, to see thy face Our sire himself has sought this place.” Thus LakshmaG spoke and stood ashamed, And Ráma saw and thus exclaimed: “It is the strong-armed monarch: he
- **Translation**: 

---

### Verse 8 (Ramayan 0.748)
- **Original**: 730 The Ramayana Is come, methinks, his sons to see, To bid us both the forest quit For joys for which he deems us fit: He thinks on all our care and pain, And now would lead us home again. My glorious father hence will bear Sítá who claims all tender care. I see two coursers fleet as storms, Of noble breed and lovely forms. I see the beast of mountain size Who bears the king our father wise, The aged Victor, march this way In front of all the armed array. But doubt and fear within me rise, For when I look with eager eyes I see no white umbrella spread, World-famous, o'er the royal head. Now, LakshmaG, from the tree descend, And to my words attention lend.” Thus spoke the pious prince: and he Descended from the lofty tree, And reverent hand to hand applied, Stood humbly by his brother's side. The host, compelled by Bharat's care, The wood from trampling feet to spare, Dense crowding half a league each way Encamped around the mountain lay. Below the tall hill's shelving side Gleamed the bright army far and wide Spread o'er the ample space, By Bharat led who firmly true In duty from his bosom threw
- **Translation**: 

---

### Verse 9 (Ramayan 0.749)
- **Original**: Canto XCIX. Bharat's Approach. 731 All pride, and near his brother drew To win the hero's grace. Canto XCIX. Bharat's Approach. Soon as the warriors took their rest Obeying Bharat's high behest, Thus Bharat toZatrughna spake: “A band of soldiers with thee take, And with these hunters o'er and o'er The thickets of the wood explore. With bow, sword, arrows in their hands Let Guha with his kindred bands Within this grove remaining trace The children of Kakutstha's race. And I meanwhile on foot will through This neighbouring wood my way pursue, With elders and the twice-born men, And every lord and citizen. There is, I feel, no rest for me Till Ráma's face again I see, Lakshma G, in arms and glory great, And Sítá born to happy fate: No rest, until his cheek as bright As the fair moon rejoice my sight, No rest until I see the eye With which the lotus petals vie; Till on my head those dear feet rest With signs of royal rank impressed; None, till my kingly brother gain His old hereditary reign,
- **Translation**: 

---

### Verse 10 (Ramayan 0.750)
- **Original**: 732 The Ramayana Till o'er his limbs and noble head The consecrating drops be shed. How blest is Janak's daughter, true To every wifely duty, who Cleaves faithful to her husband's side Whose realm is girt by Ocean's tide! This mountain too above the rest E'en as the King of Hills is blest,— Whose shades Kakutstha's scion hold As Nandan charms the Lord of Gold. Yea, happy is this tangled grove Where savage beasts unnumbered rove, Where, glory of the Warrior race, King Ráma finds a dwelling-place.” Thus Bharat, strong-armed hero spake, And walked within the pathless brake. O'er plains where gay trees bloomed he went, Through boughs in tangled net-work bent, And then from Ráma's cot appeared The banner which the flame upreared. And Bharat joyed with every friend To mark those smoky wreaths ascend: “Here Ráma dwells,” he thought;“at last The ocean of our toil is passed.” Then sure that Ráma's hermit cot Was on the mountain's side He stayed his army on the spot, And on with Guha hied. [209]
- **Translation**: 

---

### Verse 11 (Ramayan 0.751)
- **Original**: Canto C. The Meeting. 733 Canto C. The Meeting. Then Bharat toZatrughna showed The spot, and eager onward strode, First bidding Saint Va[ishmha bring The widowed consorts of the king. As by fraternal love impelled His onward course the hero held, Sumantra followed close behind Zatrughna with an anxious mind: Not Bharat's self more fain could be To look on Ráma's face than he. As, speeding on, the spot he neared, Amid the hermits' homes appeared His brother's cot with leaves o'erspread, And by its side a lowly shed. Before the shed great heaps were left Of gathered flowers and billets cleft, And on the trees hung grass and bark Ráma and LakshmaG's path to mark: And heaps of fuel to provide Against the cold stood ready dried. The long-armed chief, as on he went In glory's light preëminent, With joyous words like these addressed The braveZatrughna and the rest: “This is the place, I little doubt, Which Bharadvája pointed out, Not far from where we stand must be The woodland stream, Mandákiní. Here on the mountain's woody side Roam elephants in tusked pride, And ever with a roar and cry Each other, as they meet, defy.
- **Translation**: 

---

### Verse 12 (Ramayan 0.752)
- **Original**: 734 The Ramayana And see those smoke-wreaths thick and dark: The presence of the flame they mark, Which hermits in the forest strive By every art to keep alive. O happy me! my task is done, And I shall look on Raghu's son, Like some great saint, who loves to treat His elders with all reverence meet.” Thus Bharat reached that forest rill, Thus roamed on Chitrakúma's hill; Then pity in his breast awoke, And to his friends the hero spoke: “Woe, woe upon my life and birth! The prince of men, the lord of earth Has sought the lonely wood to dwell Sequestered in a hermit's cell. Through me, through me these sorrows fall On him the splendid lord of all: Through me resigning earthly bliss He hides him in a home like this. Now will I, by the world abhorred, Fall at the dear feet of my lord, And at fair Sítá's too, to win His pardon for my heinous sin.” As thus he sadly mourned and sighed, The son of Da[aratha spied A bower of leafy branches made, Sacred and lovely in the shade, Of fair proportions large and tall, Well roofed with boughs of palm, and Sál, Arranged in order due o'erhead Like grass upon an altar spread.
- **Translation**: 

---

### Verse 13 (Ramayan 0.753)
- **Original**: Canto C. The Meeting. 735 Two glorious bows were gleaming there, Like Indra's377 in the rainy air, Terror of foemen, backed with gold, Meet for the mightiest hand to hold: And quivered arrows cast a blaze Bright gleaming like the Day-God's rays: Thus serpents with their eyes aglow Adorn their capital below.378 Great swords adorned the cottage, laid Each in a case of gold brocade; There hung the trusty shields, whereon With purest gold the bosses shone. The brace to bind the bowman's arm, The glove to shield his hand from harm, A lustre to the cottage lent From many a golden ornament: Safe was the cot from fear of men As from wild beasts the lion's den. The fire upon the altar burned, That to the north and east was turned. Bharat his eager glances bent And gazed within the cot intent; In deerskin dress, with matted hair, Ráma his chief was sitting there: With lion-shoulders broad and strong, With lotus eyes, arms thick and long. The righteous sovereign, who should be Lord paramount from sea to sea, High-minded, born to lofty fate, Like Brahmá's self supremely great; With LakshmaG by his side, and her, Fair Sítá, for his minister. 377 The rainbow is called the bow of Indra. 378 Bhogavatí, the abode of the Nágas or Serpent race.
- **Translation**: 

---

### Verse 14 (Ramayan 0.754)
- **Original**: 736 The Ramayana And Bharat gazing, overcome By sorrow for a while was dumb, Then, yielding to his woe, he ran To Ráma and with sobs began: “He who a royal seat should fill With subjects round to do his will, My elder brother,— see him here, With silvan creatures waiting near. The high-souled hero, wont to wear The costliest robes exceeding fair, Now banished, in a deerskin dress, Here keeps the path of righteousness. How brooks the son of Raghu now The matted locks which load his brow, Around whose princely head were twined Sweet blossoms of the rarest kind? The prince whose merits grew, acquired[210] By rites performed as he desired, Would now a store of merit gain Bought by his body's toil and pain. Those limbs to which pure sandal lent The freshness of its fragrant scent, Exposed to sun, and dust, and rain, Are now defiled with many a stain. And I the wretched cause why this Falls on the prince whose right is bliss! Ah me, that ever I was born To be the people's hate and scorn!” Thus Bharat cried: of anguish sprung, Great drops upon his forehead hung. He fell o'erpowered— his grief was such— Ere he his brother's feet could touch. As on the glorious prince he gazed
- **Translation**: 

---

### Verse 15 (Ramayan 0.755)
- **Original**: Canto CI. Bharata Questioned. 737 In vain his broken voice he raised: “Dear lord”— through tears and sobbing came, The only words his lips could frame. And braveZatrughna wept aloud, As low at Ráma's feet he bowed. Then Ráma, while his tears ran fast, His arms around his brothers cast. Guha, Sumantra came to meet The princes in their wild retreat. Vrihaspati andZukra bright Their greeting thus rejoice to pay To the dear Lord who brings the night, And the great God who rules the day. Then wept the dwellers of the shade, Whose eyes the princes, meet to ride On mighty elephants, surveyed; And cast all thought of joy aside. Canto CI. Bharata Questioned. Then Ráma gazed, and scarcely knew Bharat so worn and changed in hue. He raised him, kissed him on the head, Embraced him, and thus kindly said: “Where was thy father, brother dear, That thou art come to seek me here? Unmeet, if he be living yet, Thy feet within the wood to set. I pray thee now the cause declare Why thou hast left the kingdom there, With matted locks and deerskin dress To roam the distant wilderness.”
- **Translation**: 

---

### Verse 16 (Ramayan 0.756)
- **Original**: 738 The Ramayana Thus questioned by the prince, at length Kaikeyí's son regained his strength, And hand to hand in reverence laid, To Ráma thus his answer made: “The great-armed monarch, O my lord, Has dared to do a thing abhorred, Left us, and grieving for his son, A home among the Gods has won. My mother Queen Kaikeyí gave The order to the king her slave, And at the bidding of the dame He wrought the sin which mars his fame. Athirst for sway, her hopes are crossed, She mourns her son, her husband lost, And through her impious crime will go For punishment to hell below. Now O my lord, forgive me all; Be gracious to thy lowly thrall: Anointed king, accept to-day Like Indra's self, the royal sway. Be gracious, Prince, to lord and peer, And widowed queens who seek thee here Accept the kingdom thine by right, And so thy faithful friends delight. Let the broad land no longer be All widowed and forlorn of thee: Let the full moon of autumn reign Triumphant o'er the night again. These lords and I before thee bend: O Ráma, to our prayer attend. O do not thou this grace deny: Thy brother, pupil, slave am I. Look on this venerable ring, Advisers of our sire the king,
- **Translation**: 

---

### Verse 17 (Ramayan 0.757)
- **Original**: Canto CI. Bharata Questioned. 739 From age to age so honoured: thou Shouldst grant their supplication now.” As weeping thus the hero prayed, His head at Ráma's feet he laid. Like a mad elephant he sighed: And Ráma gazed and thus replied: “How, brother, can a man of worth, True to his vows, of noble birth— A man like me, commit a sin The lordship of the land to win? No slightest shade of fault I see, O tamer of thy foes, in thee. But ne'er shouldst thou in childish thought The queen thy mother blame in aught. O brother wise and sinless, know The sacred laws would have it so, That from good wife and son require Obedience to their lord and sire. And we are all the king's, for thus The virtuous ever reckon us: Yea brother, be it known to thee, His wives, and sons, and pupils we. His is the right, if he deem fit, To bid me, throned as monarch, sit, Or in a coat of bark expel, And deerskin, in the wood to dwell. And O remember, best of all Who act as claims of duty call, As to a virtuous sire is due, Such honour claims a mother too. So they whose lives have ever been By duty led, the king and queen, Said,“Ráma, seek the forest shade:”
- **Translation**: 

---

### Verse 18 (Ramayan 0.758)
- **Original**: 740 The Ramayana And I (what could I else?) obeyed. Thou must the royal power retain,[211] And o'er the famed Ayodhyá reign: I dressed in bark my days will spend Where DaG ak's forest wilds extend. So Da[aratha spoke, our king, His share to each apportioning Before his honoured servants' eyes: Then, heir of bliss, he sought the skies. The righteous monarch's honoured will, Whom all revered, must guide thee still, And thou must still enjoy the share Assigned thee by our father's care. So I till twice seven years are spent Will roam this wood in banishment, Contented with the lot which he, My high-souled sire, has given me. The charge the monarch gave, endeared To all mankind, by all revered, Peer of the Lord Supreme, Far better, richer far in gain Of every blessing than to reign O'er all the worlds I deem.” Canto CII. Bharat's Tidings. He spoke: and Bharat thus replied: “If, false to every claim beside, I ne'er in kingly duties fail, What will my royal life avail? Still should the custom be observed,
- **Translation**: 

---

### Verse 19 (Ramayan 0.759)
- **Original**: Canto CIII. The Funeral Libation. 741 From which our line has never swerved, Which to the younger son ne'er gives The kingdom while the elder lives. Now to Ayodhyá rich and fair With me, O Raghu's son, repair, And to protect and gladden all Our house, thyself as king install. A king the world's opinion deems A man: to me a God he seems, Whose life in virtuous thoughts and deeds The lives of other men exceeds. When I in distant Kekaya stayed, And thou hadst sought the forest shade, Our father died, the saints' delight, So constant in each holy rite. Scarce with thy wife and LakshmaG thou Hadst journeyed forth to keep the vow, When mourning for his son, forspent, To heavenly rest the monarch went. Then up, O lord of men, away! His funeral rites of water pay: I andZatrughna, ere we came, Neglected not the sacred claim. But in the spirit-world, they say, That gift alone is fresh for aye Which best beloved hands have poured; And thou his dearest art, my lord. For thee he longed, for thee he grieved, His every thought on thee was bent, And crushed by woe, of thee bereaved, He thought of thee as hence he went.”
- **Translation**: 

---

### Verse 20 (Ramayan 0.760)
- **Original**: 742 The Ramayana Canto CIII. The Funeral Libation. When Ráma heard from Bharat each Dark sorrow of his mournful speech, And tidings of his father dead, His spirits fell, his senses fled. For the sad words his brother spoke Struck on him like a thunder stroke, Fierce as the bolt which Indra throws, The victor of his Daitya foes. Raising his arms in anguish, he, As when the woodman hews a tree With its fair flowery branches crowned, Fainted and fell upon the ground. Lord of the earth to earth he sank, Helpless, as when a towering bank With sudden ruin buries deep An elephant who lay asleep. Then swift his wife and brothers flew, And water, weeping, o'er him threw. As slowly sense and strength he gained, Fast from his eyes the tears he rained, And then in accents sad and weak Kakutstha's son began to speak, And mourning for the monarch dead, With righteous words to Bharat said: “What calls me home, when he, alas, Has gone the way which all must pass? Of him, the best of kings bereft What guardian has Ayodhyá left? How may I please his spirit? how Delight the high-souled monarch now, Who wept for me and went above By me ungraced with mourning love?
- **Translation**: 

---

