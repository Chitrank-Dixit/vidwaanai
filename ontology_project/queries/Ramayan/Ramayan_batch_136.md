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

### Verse 1 (Ramayana 0.746)
- **Original**: 728 The Ramayana No power or treasure would I win By fall of friend or kith or kin. Brother, believe the words I speak: For your dear sakes alone I seek Duty and pleasure, wealth and gain: A holy life, a happy reign. If royal sway my heart desires, My brothers' weal the wish inspires: Their bliss and safety is my care, By this uplifted bow I swear. 'Twere not so hard for me to gain This broad land girdled by the main, But even Indra's royal might Should ne'er be mine in duty's spite. If any bliss my soul can see Deprived of dearZatrughna, thee, And Bharat, may the flame destroy With ashy gloom the selfish joy. Far dearer than this life of mine, Knowing the custom of our line, His heart with fond affection fraught, Bharat Ayodhyá's town resought And hearing when he came that I, With thee and Sítá, forced to fly With matted hair and hermit dress Am wandering in the wilderness. While grief his troubled senses storms, And tender love his bosom warms, From every thought of evil clear, Is come to meet his brother here. Some grievous words perchance he spoke Kaikeyí's anger to provoke, Then won the king, and comes to lay Before my feet the royal sway.
- **Translation**: 

---

### Verse 2 (Ramayana 0.747)
- **Original**: Canto XCVIII. Lakshman Calmed. 729 Hither, methinks, in season due Comes Bharat for an interview, Nor in his secret heart has he One evil thought 'gainst thee or me. What has he done ere now, reflect! How failed in love or due respect [208] To make thee doubt his faith and lay This evil to his charge to-day? Thou shouldst not join with Bharat's name So harsh a speech and idle blame. The blows thy tongue at Bharat deals, My sympathizing bosom feels. How, urged by stress of any ill, Should sons their father's life-blood spill, Or brother slay in impious strife A brother dearer than his life? If thou these cruel words hast said By strong desire of empire led, My brother Bharat will I pray To give to thee the kingly sway. “Give him the realm,” my speech shall be, And Bharat will, methinks, agree.” Thus spoke the prince whose chief delight Was duty, and to aid the right: And Lakshma G keenly felt the blame, And shrank within himself for shame: And then his answer thus returned, With downcast eye and cheek that burned: “Brother, I ween, to see thy face Our sire himself has sought this place.” Thus LakshmaG spoke and stood ashamed, And Ráma saw and thus exclaimed: “It is the strong-armed monarch: he
- **Translation**: 

---

### Verse 3 (Ramayana 0.748)
- **Original**: 730 The Ramayana Is come, methinks, his sons to see, To bid us both the forest quit For joys for which he deems us fit: He thinks on all our care and pain, And now would lead us home again. My glorious father hence will bear Sítá who claims all tender care. I see two coursers fleet as storms, Of noble breed and lovely forms. I see the beast of mountain size Who bears the king our father wise, The aged Victor, march this way In front of all the armed array. But doubt and fear within me rise, For when I look with eager eyes I see no white umbrella spread, World-famous, o'er the royal head. Now, LakshmaG, from the tree descend, And to my words attention lend.” Thus spoke the pious prince: and he Descended from the lofty tree, And reverent hand to hand applied, Stood humbly by his brother's side. The host, compelled by Bharat's care, The wood from trampling feet to spare, Dense crowding half a league each way Encamped around the mountain lay. Below the tall hill's shelving side Gleamed the bright army far and wide Spread o'er the ample space, By Bharat led who firmly true In duty from his bosom threw
- **Translation**: 

---

### Verse 4 (Ramayana 0.749)
- **Original**: Canto XCIX. Bharat's Approach. 731 All pride, and near his brother drew To win the hero's grace. Canto XCIX. Bharat's Approach. Soon as the warriors took their rest Obeying Bharat's high behest, Thus Bharat toZatrughna spake: “A band of soldiers with thee take, And with these hunters o'er and o'er The thickets of the wood explore. With bow, sword, arrows in their hands Let Guha with his kindred bands Within this grove remaining trace The children of Kakutstha's race. And I meanwhile on foot will through This neighbouring wood my way pursue, With elders and the twice-born men, And every lord and citizen. There is, I feel, no rest for me Till Ráma's face again I see, Lakshma G, in arms and glory great, And Sítá born to happy fate: No rest, until his cheek as bright As the fair moon rejoice my sight, No rest until I see the eye With which the lotus petals vie; Till on my head those dear feet rest With signs of royal rank impressed; None, till my kingly brother gain His old hereditary reign,
- **Translation**: 

---

### Verse 5 (Ramayana 0.750)
- **Original**: 732 The Ramayana Till o'er his limbs and noble head The consecrating drops be shed. How blest is Janak's daughter, true To every wifely duty, who Cleaves faithful to her husband's side Whose realm is girt by Ocean's tide! This mountain too above the rest E'en as the King of Hills is blest,— Whose shades Kakutstha's scion hold As Nandan charms the Lord of Gold. Yea, happy is this tangled grove Where savage beasts unnumbered rove, Where, glory of the Warrior race, King Ráma finds a dwelling-place.” Thus Bharat, strong-armed hero spake, And walked within the pathless brake. O'er plains where gay trees bloomed he went, Through boughs in tangled net-work bent, And then from Ráma's cot appeared The banner which the flame upreared. And Bharat joyed with every friend To mark those smoky wreaths ascend: “Here Ráma dwells,” he thought;“at last The ocean of our toil is passed.” Then sure that Ráma's hermit cot Was on the mountain's side He stayed his army on the spot, And on with Guha hied. [209]
- **Translation**: 

---

### Verse 6 (Ramayana 0.751)
- **Original**: Canto C. The Meeting. 733 Canto C. The Meeting. Then Bharat toZatrughna showed The spot, and eager onward strode, First bidding Saint Va[ishmha bring The widowed consorts of the king. As by fraternal love impelled His onward course the hero held, Sumantra followed close behind Zatrughna with an anxious mind: Not Bharat's self more fain could be To look on Ráma's face than he. As, speeding on, the spot he neared, Amid the hermits' homes appeared His brother's cot with leaves o'erspread, And by its side a lowly shed. Before the shed great heaps were left Of gathered flowers and billets cleft, And on the trees hung grass and bark Ráma and LakshmaG's path to mark: And heaps of fuel to provide Against the cold stood ready dried. The long-armed chief, as on he went In glory's light preëminent, With joyous words like these addressed The braveZatrughna and the rest: “This is the place, I little doubt, Which Bharadvája pointed out, Not far from where we stand must be The woodland stream, Mandákiní. Here on the mountain's woody side Roam elephants in tusked pride, And ever with a roar and cry Each other, as they meet, defy.
- **Translation**: 

---

### Verse 7 (Ramayana 0.752)
- **Original**: 734 The Ramayana And see those smoke-wreaths thick and dark: The presence of the flame they mark, Which hermits in the forest strive By every art to keep alive. O happy me! my task is done, And I shall look on Raghu's son, Like some great saint, who loves to treat His elders with all reverence meet.” Thus Bharat reached that forest rill, Thus roamed on Chitrakúma's hill; Then pity in his breast awoke, And to his friends the hero spoke: “Woe, woe upon my life and birth! The prince of men, the lord of earth Has sought the lonely wood to dwell Sequestered in a hermit's cell. Through me, through me these sorrows fall On him the splendid lord of all: Through me resigning earthly bliss He hides him in a home like this. Now will I, by the world abhorred, Fall at the dear feet of my lord, And at fair Sítá's too, to win His pardon for my heinous sin.” As thus he sadly mourned and sighed, The son of Da[aratha spied A bower of leafy branches made, Sacred and lovely in the shade, Of fair proportions large and tall, Well roofed with boughs of palm, and Sál, Arranged in order due o'erhead Like grass upon an altar spread.
- **Translation**: 

---

### Verse 8 (Ramayana 0.753)
- **Original**: Canto C. The Meeting. 735 Two glorious bows were gleaming there, Like Indra's377 in the rainy air, Terror of foemen, backed with gold, Meet for the mightiest hand to hold: And quivered arrows cast a blaze Bright gleaming like the Day-God's rays: Thus serpents with their eyes aglow Adorn their capital below.378 Great swords adorned the cottage, laid Each in a case of gold brocade; There hung the trusty shields, whereon With purest gold the bosses shone. The brace to bind the bowman's arm, The glove to shield his hand from harm, A lustre to the cottage lent From many a golden ornament: Safe was the cot from fear of men As from wild beasts the lion's den. The fire upon the altar burned, That to the north and east was turned. Bharat his eager glances bent And gazed within the cot intent; In deerskin dress, with matted hair, Ráma his chief was sitting there: With lion-shoulders broad and strong, With lotus eyes, arms thick and long. The righteous sovereign, who should be Lord paramount from sea to sea, High-minded, born to lofty fate, Like Brahmá's self supremely great; With LakshmaG by his side, and her, Fair Sítá, for his minister. 377 The rainbow is called the bow of Indra. 378 Bhogavatí, the abode of the Nágas or Serpent race.
- **Translation**: 

---

### Verse 9 (Ramayana 0.754)
- **Original**: 736 The Ramayana And Bharat gazing, overcome By sorrow for a while was dumb, Then, yielding to his woe, he ran To Ráma and with sobs began: “He who a royal seat should fill With subjects round to do his will, My elder brother,— see him here, With silvan creatures waiting near. The high-souled hero, wont to wear The costliest robes exceeding fair, Now banished, in a deerskin dress, Here keeps the path of righteousness. How brooks the son of Raghu now The matted locks which load his brow, Around whose princely head were twined Sweet blossoms of the rarest kind? The prince whose merits grew, acquired[210] By rites performed as he desired, Would now a store of merit gain Bought by his body's toil and pain. Those limbs to which pure sandal lent The freshness of its fragrant scent, Exposed to sun, and dust, and rain, Are now defiled with many a stain. And I the wretched cause why this Falls on the prince whose right is bliss! Ah me, that ever I was born To be the people's hate and scorn!” Thus Bharat cried: of anguish sprung, Great drops upon his forehead hung. He fell o'erpowered— his grief was such— Ere he his brother's feet could touch. As on the glorious prince he gazed
- **Translation**: 

---

### Verse 10 (Ramayana 0.755)
- **Original**: Canto CI. Bharata Questioned. 737 In vain his broken voice he raised: “Dear lord”— through tears and sobbing came, The only words his lips could frame. And braveZatrughna wept aloud, As low at Ráma's feet he bowed. Then Ráma, while his tears ran fast, His arms around his brothers cast. Guha, Sumantra came to meet The princes in their wild retreat. Vrihaspati andZukra bright Their greeting thus rejoice to pay To the dear Lord who brings the night, And the great God who rules the day. Then wept the dwellers of the shade, Whose eyes the princes, meet to ride On mighty elephants, surveyed; And cast all thought of joy aside. Canto CI. Bharata Questioned. Then Ráma gazed, and scarcely knew Bharat so worn and changed in hue. He raised him, kissed him on the head, Embraced him, and thus kindly said: “Where was thy father, brother dear, That thou art come to seek me here? Unmeet, if he be living yet, Thy feet within the wood to set. I pray thee now the cause declare Why thou hast left the kingdom there, With matted locks and deerskin dress To roam the distant wilderness.”
- **Translation**: 

---

### Verse 11 (Ramayana 0.756)
- **Original**: 738 The Ramayana Thus questioned by the prince, at length Kaikeyí's son regained his strength, And hand to hand in reverence laid, To Ráma thus his answer made: “The great-armed monarch, O my lord, Has dared to do a thing abhorred, Left us, and grieving for his son, A home among the Gods has won. My mother Queen Kaikeyí gave The order to the king her slave, And at the bidding of the dame He wrought the sin which mars his fame. Athirst for sway, her hopes are crossed, She mourns her son, her husband lost, And through her impious crime will go For punishment to hell below. Now O my lord, forgive me all; Be gracious to thy lowly thrall: Anointed king, accept to-day Like Indra's self, the royal sway. Be gracious, Prince, to lord and peer, And widowed queens who seek thee here Accept the kingdom thine by right, And so thy faithful friends delight. Let the broad land no longer be All widowed and forlorn of thee: Let the full moon of autumn reign Triumphant o'er the night again. These lords and I before thee bend: O Ráma, to our prayer attend. O do not thou this grace deny: Thy brother, pupil, slave am I. Look on this venerable ring, Advisers of our sire the king,
- **Translation**: 

---

### Verse 12 (Ramayana 0.757)
- **Original**: Canto CI. Bharata Questioned. 739 From age to age so honoured: thou Shouldst grant their supplication now.” As weeping thus the hero prayed, His head at Ráma's feet he laid. Like a mad elephant he sighed: And Ráma gazed and thus replied: “How, brother, can a man of worth, True to his vows, of noble birth— A man like me, commit a sin The lordship of the land to win? No slightest shade of fault I see, O tamer of thy foes, in thee. But ne'er shouldst thou in childish thought The queen thy mother blame in aught. O brother wise and sinless, know The sacred laws would have it so, That from good wife and son require Obedience to their lord and sire. And we are all the king's, for thus The virtuous ever reckon us: Yea brother, be it known to thee, His wives, and sons, and pupils we. His is the right, if he deem fit, To bid me, throned as monarch, sit, Or in a coat of bark expel, And deerskin, in the wood to dwell. And O remember, best of all Who act as claims of duty call, As to a virtuous sire is due, Such honour claims a mother too. So they whose lives have ever been By duty led, the king and queen, Said,“Ráma, seek the forest shade:”
- **Translation**: 

---

### Verse 13 (Ramayana 0.758)
- **Original**: 740 The Ramayana And I (what could I else?) obeyed. Thou must the royal power retain,[211] And o'er the famed Ayodhyá reign: I dressed in bark my days will spend Where DaG ak's forest wilds extend. So Da[aratha spoke, our king, His share to each apportioning Before his honoured servants' eyes: Then, heir of bliss, he sought the skies. The righteous monarch's honoured will, Whom all revered, must guide thee still, And thou must still enjoy the share Assigned thee by our father's care. So I till twice seven years are spent Will roam this wood in banishment, Contented with the lot which he, My high-souled sire, has given me. The charge the monarch gave, endeared To all mankind, by all revered, Peer of the Lord Supreme, Far better, richer far in gain Of every blessing than to reign O'er all the worlds I deem.” Canto CII. Bharat's Tidings. He spoke: and Bharat thus replied: “If, false to every claim beside, I ne'er in kingly duties fail, What will my royal life avail? Still should the custom be observed,
- **Translation**: 

---

### Verse 14 (Ramayana 0.759)
- **Original**: Canto CIII. The Funeral Libation. 741 From which our line has never swerved, Which to the younger son ne'er gives The kingdom while the elder lives. Now to Ayodhyá rich and fair With me, O Raghu's son, repair, And to protect and gladden all Our house, thyself as king install. A king the world's opinion deems A man: to me a God he seems, Whose life in virtuous thoughts and deeds The lives of other men exceeds. When I in distant Kekaya stayed, And thou hadst sought the forest shade, Our father died, the saints' delight, So constant in each holy rite. Scarce with thy wife and LakshmaG thou Hadst journeyed forth to keep the vow, When mourning for his son, forspent, To heavenly rest the monarch went. Then up, O lord of men, away! His funeral rites of water pay: I andZatrughna, ere we came, Neglected not the sacred claim. But in the spirit-world, they say, That gift alone is fresh for aye Which best beloved hands have poured; And thou his dearest art, my lord. For thee he longed, for thee he grieved, His every thought on thee was bent, And crushed by woe, of thee bereaved, He thought of thee as hence he went.”
- **Translation**: 

---

### Verse 15 (Ramayana 0.760)
- **Original**: 742 The Ramayana Canto CIII. The Funeral Libation. When Ráma heard from Bharat each Dark sorrow of his mournful speech, And tidings of his father dead, His spirits fell, his senses fled. For the sad words his brother spoke Struck on him like a thunder stroke, Fierce as the bolt which Indra throws, The victor of his Daitya foes. Raising his arms in anguish, he, As when the woodman hews a tree With its fair flowery branches crowned, Fainted and fell upon the ground. Lord of the earth to earth he sank, Helpless, as when a towering bank With sudden ruin buries deep An elephant who lay asleep. Then swift his wife and brothers flew, And water, weeping, o'er him threw. As slowly sense and strength he gained, Fast from his eyes the tears he rained, And then in accents sad and weak Kakutstha's son began to speak, And mourning for the monarch dead, With righteous words to Bharat said: “What calls me home, when he, alas, Has gone the way which all must pass? Of him, the best of kings bereft What guardian has Ayodhyá left? How may I please his spirit? how Delight the high-souled monarch now, Who wept for me and went above By me ungraced with mourning love?
- **Translation**: 

---

### Verse 16 (Ramayana 0.761)
- **Original**: Canto CIII. The Funeral Libation. 743 Ah, happy brothers! you have paid Due offerings to his parting shade. E'en when my banishment is o'er, Back to my home I go no more, To look upon the widowed state Reft of her king, disconsolate. E'en then, O tamer of the foe, If to Ayodhyá's town I go, Who will direct me as of old, Now other worlds our father hold? From whom, my brother, shall I hear Those words which ever charmed mine ear And filled my bosom with delight Whene'er he saw me act aright?” Thus Ráma spoke: then nearer came And looking on his moonbright dame, “Sítá, the king is gone,” he said: “And Lakshma G, know thy sire is dead, [212] And with the Gods on high enrolled: This mournful news has Bharat told.” He spoke: the noble youths with sighs Rained down the torrents from their eyes. And then the brothers of the chief With words of comfort soothed his grief: “Now to the king our sire who swayed The earth be due libations paid.” Soon as the monarch's fate she knew, Sharp pangs of grief smote Sítá through: Nor could she look upon her lord With eyes from which the torrents poured. And Ráma strove with tender care To soothe the weeping dame's despair, And then, with piercing woe distressed,
- **Translation**: 

---

### Verse 17 (Ramayana 0.762)
- **Original**: 744 The Ramayana The mournful LakshmaG thus addressed: “Brother, I pray thee bring for me The pressed fruit of the Ingudí, And a bark mantle fresh and new, That I may pay this offering due. First of the three shall Sítá go, Next thou, and I the last: for so Moves the funereal pomp of woe.”379 Sumantra of the noble mind, Gentle and modest, meek and kind, Who, follower of each princely youth, To Ráma clung with constant truth, Now with the royal brothers' aid The grief of Ráma soothed and stayed, And lent his arm his lord to guide Down to the river's holy side. That lovely stream the heroes found, With woods that ever blossomed crowned, And there in bitter sorrow bent Their footsteps down the fair descent. Then where the stream that swiftly flowed A pure pellucid shallow showed, The funeral drops they duly shed, And “Father, this be thine,” they said. But he, the lord who ruled the land, Filled from the stream his hollowed hand, And turning to the southern side Stretched out his arm and weeping cried: “This sacred water clear and pure, 379 “The order of the procession on these occasions is that the children pre- cede according to age, then the women and after that the men according to age, the youngest first and the eldest last: when they descend into the water this is reversed and resumed when they come out of it.” C AREY AND M ARSHMAN .{FNS
- **Translation**: 

---

### Verse 18 (Ramayana 0.763)
- **Original**: Canto CIII. The Funeral Libation. 745 An offering which shall aye endure To thee, O lord of kings, I give: Accept it where the spirits live!” Then, when the solemn rite was o'er, Came Ráma to the river shore, And offered, with his brothers' aid, Fresh tribute to his father's shade. With jujube fruit he mixed the seed Of Ingudís from moisture freed, And placed it on a spot o'erspread With sacred grass, and weeping said: “Enjoy, great King, the cake which we Thy children eat and offer thee! For ne'er do blessed Gods refuse To share the food which mortals use.” Then Ráma turned him to retrace The path that brought him to the place, And up the mountain's pleasant side Where lovely lawns lay fair, he hied. Soon as his cottage door he gained His brothers to his breast he strained. From them and Sítá in their woes So loud the cry of weeping rose, That like the roar of lions round The mountain rolled the echoing sound. And Bharat's army shook with fear The weeping of the chiefs to hear. “Bharat,” the soldiers cried,“'tis plain, His brother Ráma meets again, And with these cries that round us ring They sorrow for their sire the king.” Then leaving car and wain behind,
- **Translation**: 

---

### Verse 19 (Ramayana 0.764)
- **Original**: 746 The Ramayana One eager thought in every mind, Swift toward the weeping, every man, As each could find a passage, ran. Some thither bent their eager course With car, and elephant, and horse, And youthful captains on their feet With longing sped their lord to meet, As though the new-come prince had been An exile for long years unseen. Earth beaten in their frantic zeal By clattering hoof and rumbling wheel, Sent forth a deafening noise as loud As heaven when black with many a cloud. Then, with their consorts gathered near, Wild elephants in sudden fear Rushed to a distant wood, and shed An odour round them as they fled. And every silvan thing that dwelt Within those shades the terror felt, Deer, lion, tiger, boar and roe, Bison, wild-cow, and buffalo. And when the tumult wild they heard, With trembling pinions flew each bird, From tree, from thicket, and from lake, Swan, koïl, curlew, crane, and drake. With men the ground was overspread, With startled birds the sky o'erhead. Then on his sacrificial ground The sinless, glorious chief was found. Loading with curses deep and loud The hump-back and the queen, the crowd Whose cheeks were wet, whose eyes were dim, In fond affection ran to him. While the big tears their eyes bedewed,
- **Translation**: 

---

### Verse 20 (Ramayana 0.765)
- **Original**: Canto CIV. The Meeting With The Queens. 747 He looked upon the multitude, [213] And then as sire and mother do, His arms about his loved ones threw. Some to his feet with reverence pressed, Some in his arms he strained: Each friend, with kindly words addressed, Due share of honour gained. Then, by their mighty woe o'ercome, The weeping heroes' cry Filled, like the roar of many a drum, Hill, cavern, earth, and sky. Canto CIV. The Meeting With The Queens. Va [ishmha with his soul athirst To look again on Ráma, first In line the royal widows placed, And then the way behind them traced. The ladies moving, faint and slow, Saw the fair stream before them flow, And by the bank their steps were led Which the two brothers visited. Kau [alyá with her faded cheek And weeping eyes began to speak, And thus in mournful tones addressed The queen Sumitrá and the rest: “See in the wood the bank's descent, Which the two orphan youths frequent, Whose noble spirits never fall, Though woes surround them, reft of all. Thy son with love that never tires
- **Translation**: 

---

