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

### Verse 1 (Ramayana 0.1606)
- **Original**: 1588 The Ramayana Canto XXX. Sárdúla's Speech. They told their lord that Ráma still Lay waiting by Suvela's hill. The tyrant, flushed with angry glow, Heard of the coming of the foe, And thus with close inquiry pressed Zárdúla spokesman for the rest: “Why art thou sad, night-rover? speak: Has grief or terror changed thy cheek? Have the wild Vánars' hostile bands Assailed thee with their mighty hands?” Zárdúla heard, but scarce might speak; His trembling tones were faint and weak: “O Giant King, in vain we try The purpose of the foe to spy. Their strength and number none may tell, And Ráma guards his legions well. He leaves no hope to prying eyes, And parley with the chiefs denies: Each road and path a Vánar guard, Of mountain size, has closed and barred. Soon as my feet an entrance found By giants was I seized and bound, And wounded sore I fell beneath Their fists and knees and hands and teeth. Then trembling, bleeding, wellnigh dead To Ráma's presence was I led. He in his mercy stooped to save, And freedom to the captive gave. With rocks and shattered mountains he Has bridged his way athwart the sea, And he and all his legions wait
- **Translation**: 

---

### Verse 2 (Ramayana 0.1607)
- **Original**: Canto XXXI. The Magic Head. 1589 Embattled close to Lanká's gate. Soon will the host thy wall assail, And, swarming on, the rampart scale. Now, O my King, his consort yield, Or arm thee with the sword and shield. This choice is left thee: choose between Thy safety and the Maithil queen.”943 Canto XXXI. The Magic Head. The tyrant's troubled eye confessed The secret fear that filled his breast. With dread of coming woe dismayed He called his counsellors to aid; Then sternly silent, deep in thought, His chamber in the palace sought. Then, as the surest hope of all, The monarch bade his servants call [451] Vidyujjihva, whom magic skill Made master of the means of ill. Then spake the lord of Lanká's isle: “Come, Sítá with thine arts beguile. With magic skill and deftest care A head like Ráma's own prepare. This head, long shafts and mighty bow, To Janak's daughter will we show.” 943 I omit the rest of this canto, which is mere repetition. RávaG gives in the same words his former answer that the Gods, Gandharvas and fiends combined shall not force him to give up Sítá. He then ordersZárdúla to tell him the names of the Vánar chieftains whom he has seen in Ráma's army. These have already been mentioned byZuka and SáraG.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1608)
- **Original**: 1590 The Ramayana He ceased: Vidyujjihva obeyed, And wondrous magic skill displayed; And RávaG for the art he showed An ornament of price bestowed. Then to the grove where Sítá lay The lord of Lanká took his way. Pale, wasted, weeping, on the ground The melancholy queen he found, Whose thoughts in utmost stress of ill Were fixed upon her husband still. The giant king approached the dame, Declared in tones of joy his name; Then heeding naught her wild distress Bespake her, stern and pitiless: “The prince to whom thy fancies cling Though loved and wooed by Lanká's king, Who slew the noble Khara,— he Is slain by warriors sent by me. Thy living root is hewn away, Thy scornful pride is tamed to-day. Thy lord in battle's front has died, And Sítá shall be RávaG's bride. Hence, idle thoughts: thy hope is fled; What wilt thou, Sítá, with the dead? Rise, child of Janak, rise and be The queen of all my queens and me. Incline thine ear, and I will tell, Dear lady, how thy husband fell. He bridged his way across the sea With countless troops to fight with me. The setting sun had flushed the west When on the shore they took their rest. Weary with toil no watch they kept, Securely on the sands they slept.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1609)
- **Original**: Canto XXXI. The Magic Head. 1591 Prahasta's troops assailed our foes, And smote them in their deep repose. Scarce could their bravest prove their might: They perished in the dark of night. Axe, spear, and sword, directed well, Upon the sleeping myriads fell. First in the fight Prahasta's sword Reft of his head thy slumbering lord. Roused at the din VibhishaG rose, The captive of surrounding foes, And Lakshma G through the woods that spread Around him with his Vánars fled. Hanúmán fell: one deadly stroke The neck of King Sugríva broke, And Mainda sank, and Dwivid lay Gasping in blood his life away. The Vánars died, or fled dispersed Like cloudlets when the storm has burst. Some rose aloft in air, and more Ran to the sea and filled the shore. On shore, in woods, on hill and plain Our conquering giants left the slain. Thus my victorious host o'erthrew The Vánars, and thy husband slew: See, rudely stained with dust, and red With dropping blood, the severed head.” Then, turning to a Rákshas slave, The ruthless king his mandate gave, And straight Vidyujjihva who bore The head still wet with dripping gore, The arrows and the mighty bow, Bent down before his master low. “Vidyujjihva,” cried RávaG,“place
- **Translation**: 

---

### Verse 5 (Ramayana 0.1610)
- **Original**: 1592 The Ramayana The head before the lady's face, And let her see with weeping eyes That low in death her husband lies.” Before the queen the giant laid The beauteous head his art had made. And RávaG cried:“Thine eyes will know These arrows and the mighty bow. With fame of this by Ráma strung The earth and heaven and hell have rung. Prahasta brought it hither when His hand had slain thy prince of men. Now, widowed Queen, thy hopes resign: Forget thy husband and be mine.” Canto XXXII. Sítá's Lament. Again her eyes with tears o'erflowed: She gazed upon the head he showed, Gazed on the bow so famed of yore, The glorious bow which Ráma bore. She gazed upon his cheek and brows, The eyes of her beloved spouse; His lips, the lustre of his hair, The priceless gem that glittered there. The features of her lord she knew, And, pierced with anguish at the view, She lifted up her voice and cried: “Kaikeyí, art thou satisfied? Now all thy longings are fulfilled; The joy of Raghu's race is killed,
- **Translation**: 

---

### Verse 6 (Ramayana 0.1611)
- **Original**: Canto XXXII. Sítá's Lament. 1593 And ruined is the ancient line, Destroyer, by that fraud of thine. Ah, what offence, O cruel dame, What fault in Ráma couldst thou blame, To drive him clad in hermit dress With Sítá to the wilderness?” Great trembling seized her frame, and she Fell like a stricken plantain tree. As lie the dead she lay; at length Slowly regaining sense and strength, On the dear head she fixed her eye [452] And cried with very bitter cry: “Ah, when thy cold dead cheek I view, My hero, I am murdered too. Then first a faithful woman's eyes See sorrow, when her husband dies. When thou, my lord, wast nigh to save, Some stealthy hand thy death wound gave. Thou art not dead: rise, hero, rise; Long life was thine, as spake the wise Whose words, I ween, are ever true, For faith lies open to their view. Ah lord, and shall thy head recline On earth's cold breast, forsaking mine, Counting her chill lap dearer far Than I and my caresses are? Ah, is it thus these eyes behold Thy famous bow adorned with gold, Whereon of yore I loved to bind Sweet garlands that my hands had twined? And hast thou sought in heaven a place Amid the founders of thy race, Where in the home deserved so well
- **Translation**: 

---

### Verse 7 (Ramayana 0.1612)
- **Original**: 1594 The Ramayana Thy sires and Da[aratha dwell? Or dost thou shine a brighter star In skies where blest immortals are, Forsaking in thy lofty scorn The race wherein thy sires were born? Turn to my gaze, O turn thine eye: Why are thy cold lips silent, why? When first we met as youth and maid, When in thy hand my hand was laid, Thy promise was thy steps should be Through life in duty's path with me. Remember, faithful still, thy vow, And take me with thee even now. Is that broad bosom where I hung, That neck to which I fondly clung, Where flowery garlands breathed their scent By hungry dogs and vultures rent? Shall no funereal honours grace The parted lord of Raghu's race, Whose bounty liberal fees bestowed, For whom the fires of worship glowed? Kau [alyá wild with grief will see One sole survivor of the three Who in their hermit garments went To the dark woods in banishment. Then at her cry shall LakshmaG tell How, slain by night, the Vánars fell; How to thy side the giants crept, And slew the hero as he slept. Thy fate and mine the queen will know, And broken-hearted die of woe. For my unworthy sake, for mine, Ráma, the glory of his line, Who bridged his way across the main,
- **Translation**: 

---

### Verse 8 (Ramayana 0.1613)
- **Original**: Canto XXXII. Sítá's Lament. 1595 Is basely in a puddle slain; And I, the graceless wife he wed, Have brought this ruin on his head. Me, too, on him, O RávaG, slay: The wife beside her husband lay. By his dear body let me rest, Cheek close to cheek and breast to breast, My happy eyes I then will close, And follow whither Ráma goes.” Thus cried the miserable dame; When to the king a warder came, Before the giant monarch bowed And said that, followed by a crowd Of counsellors and lords of state, Prahasta stood before the gate, And, sent by some engrossing care, Craved audience of his master there. The anxious tyrant left his seat And hastened forth the chief to meet: Then summoning his nobles all, Took counsel in his regal hall. When Lanká's lord had left the queen, The head and bow no more were seen. The giant king his nobles eyed, And, terrible as Yáma, cried: “O faithful lords, the time is come: Gather our hosts with beat of drum. Nigh to the town our foeman draws: Be prudent, nor reveal the cause.”
- **Translation**: 

---

### Verse 9 (Ramayana 0.1614)
- **Original**: 1596 The Ramayana The nobles listened and obeyed: Swift were the gathered troops arrayed, And countless rovers of the night Stood burning for the hour of fight. Canto XXXIII. Saramá. But Saramá, of gentler mood, With pitying eyes the mourner viewed, Stole to her side and softly told Glad tidings that her heart consoled, Revealing with sweet voice and smile The secret of the giant's guile. She, one of those who night and day Watching in turns by Sítá lay, Though Rákshas born felt pity's touch, And loved the hapless lady much. “I heard,” she said,“thy bitter cry, Heard RávaG's speech and thy reply, For, hiding in the thicket near, No word or tone escaped mine ear. When Ráva G hastened forth I bent My steps to follow as he went, And learnt the secret cause that drove The monarch from the A[oka grove. Believe me, Queen, thou needst not weep For Ráma slaughtered in his sleep. Thy lion lord of men defies By day attack, by night surprise. Can even giants slay with ease
- **Translation**: 

---

### Verse 10 (Ramayana 0.1615)
- **Original**: Canto XXXIII. Saramá. 1597 Vast hosts who fight with brandished trees, For whom, with eye that never sleeps, His constant watch thy Ráma keeps? [453] Lord of the mighty arm and chest, Of earthly warriors first and best, Whose fame through all the regions rings, Proud scion of a hundred kings; Who guards his life and loves to lend His saving succour to a friend: Whose bow no hand but his can strain,— Thy lord, thy Ráma is not slain. Obedient to his master's will, A great magician, trained in ill, With deftest art surpassing thought That marvellous illusion wrought. Let rising hope thy grief dispel: Look up and smile, for all is well, And gentle Lakshmí, Fortune's Queen, Regards thee with a favouring mien. Thy Ráma with his Vánar train Has thrown a bridge athwart the main, Has led his countless legions o'er, And ranged them on this southern shore. These eyes have seen the hero stand Girt by his hosts on Lanká's strand, And breathless spies each moment bring Fresh tidings to the giant king; And every peer and lord of state Is called to counsel and debate.” She ceased: the sound, long loud and clear, Of gathering armies smote her ear, Where call of drum and shell rang out, The tambour and the battle shout;
- **Translation**: 

---

### Verse 11 (Ramayana 0.1616)
- **Original**: 1598 The Ramayana And, while the din the echoes woke, Again to Janak's child she spoke: “Hear, lady, hear the loud alarms That call the Rákshas troops to arms, From stable and from stall they lead The elephant and neighing steed, Brace harness on with deftest care, And chariots for the fight prepare. Swift o'er the trembling ground career Mailed horsemen armed with axe and spear, And here and there in road and street The terrible battalions meet. I hear the gathering near and far, The snorting steed, the rattling car. Bold chieftains, leaders of the brave, Press densely on, like wave on wave, And bright the evening sunbeams glance On helm and shield, on sword and lance. Hark, lady, to the ringing steel, Hark to the rolling chariot wheel: Hark to the mettled courser's neigh And drums' loud thunder far away. The Queen of Fortune holds thee dear, For Lanká's troops are struck with fear, And Ráma with the lotus eyes, Like Indra monarch of the skies, With conquering arm will slay his foe And free his lady from her woe. Soon will his breast support thy head, And tears of joy thine eyes will shed. Soon by his mighty arm embraced The long-lost rapture wilt thou taste, And Ráma, meet for highest bliss, Will gain his guerdon in thy kiss.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.1617)
- **Original**: Canto XXXIV. Saramá's Tidings. 1599 Canto XXXIV. Saramá's Tidings. Thus Saramá her story told: And Sítá's spirit was consoled, As when the first fresh rain is shed The parching earth is comforted. Then, filled with zeal for Sítá's sake, Again in gentle tones she spake, And, skilled in arts that soothe and please, Addressed the queen in words like these: “Thy husband, lady, will I seek, Say the fond words thy lips would speak, And then, unseen of any eye, Back to thy side will swiftly fly. My airy flights are speedier far Than Garu a's and the tempest are.” Then Sítá spake: her former woe Still left her accents faint and low: “I know thy steps, which naught can stay, Can urge through heaven and hell their way. Then if thy love and changeless will Would serve the helpless captive still, Go forth and learn each plot and guile Planned by the lord of Lanká's isle. With magic art like maddening wine He cheats these weeping eyes of mine, Torments me with his suit, nor spares Reproof or flattery, threats or prayers. These guards surround me night and day; My heart is sad, my senses stray; And helpless in my woe I fear The tyrant RávaG even here.”
- **Translation**: 

---

### Verse 13 (Ramayana 0.1618)
- **Original**: 1600 The Ramayana Then Saramá replied:“I go To learn the purpose of thy foe, Soon by thy side again to stand And tell thee what the king has planned.” She sped, she heard with eager ears The tyrant speak his hopes and fears, Where, gathered at their master's call, The nobles filled the council hall; Then swiftly, to her promise true, Back to the A[oka grove she flew. The lady on the grassy ground, Longing for her return, she found; Who with a gentle smile, to greet The envoy, led her to a seat. Through her worn frame a shiver ran As Saramá her tale began: “There stood the royal mother: she Besought her son to set thee free,[454] And to her counsel, tears and prayers, The elder nobles added theirs: “O be the Maithil queen restored With honour to her angry lord, Let Janasthán's unhappy fight Be witness of the hero's might. Hanúmán o'er the waters came And looked upon the guarded dame. Let Lanká's chiefs who fought and fell The prowess of the leader tell.” In vain they sued, in vain she wept, His purpose still unchanged he kept, As clings the miser to his gold, He would not loose thee from his hold. No, never till in death he lies, Will Lanká's lord release his prize.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1619)
- **Original**: Canto XXXV. Malyaván's Speech. 1601 Soon slain by Ráma's arrows all The giants with their king will fall, And Ráma to his home will lead His black-eyed queen from bondage freed.” An awful sound that moment rose From Lanká's fast-approaching foes, Where drum and shell in mingled peal Made earth in terror rock and reel. The hosts within the walls arrayed Stood trembling, in their hearts dismayed; Thought of the tempest soon to burst, And Lanká's lord, their ruin, cursed. Canto XXXV. Malyaván's Speech. The fearful notes of drum and shell Upon the ear of RávaG fell. One moment quailed his haughty look, One moment in his fear he shook, But soon recalling wonted pride, His counsellors he sternly eyed, And with a voice that thundered through The council hall began anew: “Lords, I have heard— your tongues have told— How Raghu's son is fierce and bold. To Lanká's shore has bridged his way And hither leads his wild array. I know your might, in battle tried, Fighting and conquering by my side. Why now, when such a foe is near, Looks eye to eye in silent fear?”
- **Translation**: 

---

### Verse 15 (Ramayana 0.1620)
- **Original**: 1602 The Ramayana He ceased, his mother's sire well known For wisdom in the council shown, Malyaván, sage and faithful guide. Thus to the monarch's speech replied: “Long reigns the king in safe repose, Unmoved by fear of vanquished foes, Whose feet by saving knowledge led In justice path delight to tread: Who knows to sheath the sword or wield, To order peace, to strike or yield: Prefers, when foes are stronger, peace, And bids a doubtful conflict cease. Now, King, the choice before thee lies, Make peace with Ráma, and be wise. This day the captive queen restore Who brings the foe to Lanká's shore. The Sire by whom the worlds are swayed Of yore the Gods and demons made. With these Injustice sided; those Fair Justice for her champions chose. Still Justice dwells with Gods above; Injustice, fiends and giants love. Thou, through the worlds that fear thee, long Hast scorned the right and loved the wrong, And Justice, with thy foes allied, Gives might resistless to their side. Thou, guided by thy wicked will, Hast found delight in deeds of ill, And sages in their holy rest Have trembled, by thy power oppressed. But they, who check each vain desire, Are clothed with might which burns like fire. In them the power and glory live Which zeal and saintly fervour give.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1621)
- **Original**: Canto XXXV. Malyaván's Speech. 1603 Their constant task, their sole delight Is worship and each holy rite, To chant aloud the Veda hymn, Nor let the sacred fires grow dim. Now through the air like thunder ring The echoes of the chants they sing. The vapours of their incense rise And veil with cloudy pall the skies, And Rákshas might grows weak and faint Killed by the power of sage and saint. By Brahmá's boon thy life was screened From God, Gandharva, Yaksha, fiend; But Vánars, men, and bears, arrayed Against thee now, thy shores invade. Red meteors, heralds of despair Flash frequent through the lurid air, Foretelling to my troubled mind The ruin of the Rákshas kind. With awful thundering overhead Clouds black as night are densely spread, And oozing from the gloomy pall Great drops of blood on Lanká fall. Dogs roam through house and shrine to steal The sacred oil and curd and meal, Cats pair with tigers, hounds with swine, And asses' foals are born of kine. In these and countless signs I trace The ruin of the giant race. 'Tis VishGu's self who comes to storm Thy city, clothed in Ráma's form; For, well I ween, no mortal hand The ocean with a bridge has spanned. O giant King, the dame release, And sue to Raghu's son for peace”
- **Translation**: 

---

### Verse 17 (Ramayana 0.1622)
- **Original**: 1604 The Ramayana [455] Canto XXXVI. Rávan's Reply. But RávaG's breast with fury swelled, And thus he spake by Death impelled, While, under brows in anger bent, Fierce glances from his eyes were sent: “The bitter words which thou, misled By friendly thought, hast fondly said, Which praise the foe and counsel fear, Unheeded fall upon mine ear. How canst thou deem a mighty foe This Ráma who, in stress of woe, Seeks, banished as his sire decreed, Assistance from the Vánar breed? Am I so feeble in thine eyes, Though feared by dwellers of the skies,— Whose might in many a battle shown The glorious race of giants own? Shall I for fear of him restore The lady whom I hither bore, Exceeding fair like Beauty's Queen944 Without her well-loved lotus seen? Around the chief let LakshmaG stand, Sugríva, and each Vánar band, Soon, Malyaván, thine eyes will see This boasted Ráma slain by me. I in the brunt of war defy 944 Lakshmí is the Goddess both of beauty and fortune, and is represented with a lotus in her hand.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1623)
- **Original**: Canto XXXVI. Rávan's Reply. 1605 The mightiest warriors of the sky; And if I stoop to combat men, Shall I be weak and tremble then? This mangled trunk the foe may rend, But RávaG ne'er can yield or bend, And be it vice or virtue, I This nature never will belie. What marvel if he bridged the sea? Why should this deed disquiet thee? This, only this, I surely know, Back with his life he shall not go.” Thus in loud tones the king exclaimed, And mute stood Malyaván ashamed, His reverend head he humbly bent, And slowly to his mansion went. But RávaG stayed, and deep in care Held counsel with his nobles there, All entrance to secure and close, And guard the city from their foes. He bade the chief Prahasta wait, Commander at the eastern gate, To fierce Mahodar, strong and brave, To keep the southern gate, he gave, Where Mahápár[va's might should aid The chieftain with his hosts arrayed. To guard the west— no chief more fit— He placed the warrior Indrajít, His son, the giant's joy and boast, Surrounded by a Rákshas host: And mighty SáraG hastened forth With Zuka to protect the north.945 945 The poet appears to have forgotten thatZuka and SáraG were dismissed with ignominy in Canto XXIX, and have not been reinstated.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1624)
- **Original**: 1606 The Ramayana “I will myself,” the monarch cried, “Be present on the northern side.” These orders for the walls' defence The tyrant gave, then parted thence, And, by the hope of victory fired, To chambers far within, retired. Canto XXXVII. Preparations. Lords of the legions of the wood, The chieftains with VibhishaG stood, And, strangers in the foeman's land, Their hopes and fears in council scanned: “See, see where Lanká's towers ascend, Which RávaG's power and might defend, Which Gods, Gandharvas, fiends would fail To conquer, if they durst assail. How shall our legions pass within, The city of the foe to win, With massive walls and portals barred Which RávaG keeps with surest guard?” With anxious looks the walls they eyed: And sage VibhishaG thus replied: “These lords of mine946 can answer: they Within the walls have found their way, The foeman's plan and order learned, And hither to my side returned. Now, Ráma, let my tongue declare 946 The four who fled with him. Their names are Anala, Panasa, Sampáti, and Pramati.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1625)
- **Original**: Canto XXXVII. Preparations. 1607 How Ráva G's hosts are stationed there. Prahasta heads, in warlike state, His legions at the eastern gate. To guard the southern portal stands Mahodar, girt by Rákshas bands, Where mighty Mahápár[va, sent By RávaG's hest, his aid has lent. Guard of the gate that fronts the west Is valiant Indrajít, the best Of warriors, RávaG's joy and pride; And by the youthful chieftain's side Are giants, armed for fierce attacks With sword and mace and battle-axe. North, where approach is dreaded most, The king, encompassed with a host Of giants trained in war, whose hands Wield maces, swords and lances, stands. [456] All these are chiefs whom RávaG chose As mightiest to resist his foes; And each a countless army947 leads With elephants and cars and steeds.” Then Ráma, while his spirit burned For battle, words like these returned: “The eastern gate be Níla's care, Opponent of Prahasta there. The southern gate, with troops arrayed Let Angad, Báli's son, invade. The gate that fronts the falling sun Shall be by brave Hanúmán won; Soon through its portals shall he lead His myriads of Vánar breed. 947 The numbers here are comparatively moderate: ten thousand elephants, ten thousand chariots, twenty thousand horses and ten million giants.
- **Translation**: 

---

