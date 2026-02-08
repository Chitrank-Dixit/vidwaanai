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

### Verse 1 (Ramayan 0.1701)
- **Original**: Canto LXVII. Kumbhakarna's Death. 1683 By slow degrees the Vánars' lord Felt life and sense and strength restored. He heard the giants' joyful boast: He thought upon his Vánar host. His teeth and feet he fiercely plied, And bit and rent the giant's side, Who, mad with pain and smeared with gore, Hurled to the ground the load he bore. Regardless of a storm of blows Swift to the sky the Vánar rose, Then lightly like a flying ball High overleapt the city wall, And joyous for deliverance won Regained the side of Raghu's son. And Kumbhakar Ga, mad with hate And fury, sallied from the gate, The carnage of the foe renewed And filled his maw with gory food. Slaying, with headlong frenzy blind, Both Vánar foes and giant kind. Nor would Sumitrá's valiant son982 The might of KumbhakarGa shun, Who through his harness felt the sting Of keen shafts loosened from the string. His heart confessed the warrior's power, And, bleeding from the ceaseless shower That smote him on the chest and side, With words like these the giant cried: “Well fought, well fought, Sumitrá's son; Eternal glory hast thou won, on the heads of kings and conquerors when they go forth to battle and return is frequently mentioned by Indian poets. 982 Lakshma G.
- **Translation**: 

---

### Verse 2 (Ramayan 0.1702)
- **Original**: 1684 The Ramayana For thou in desperate fight hast met The victor never conquered yet, Whom, borne on huge Airávat's back, E'en Indra trembles to attack. Go, son of Queen Sumitrá, go: Thy valour and thy strength I know. Now all my hope and earnest will Is Ráma in the fight to kill. Let him beneath my weapons fall, And I will meet and conquer all.” The chieftain, of Sumitrá born, Made answer as he laughed in scorn: “Yea, thou hast won a victor's fame From trembling Gods and Indra's shame. There waits thee now a mightier foe Whose prowess thou hast yet to know. There, famous in a hundred lands, Ráma the son of Raghu stands.” Straight at the king the giant sped, And earth was shaken at his tread. His bow the hero grasped and strained, And deadly shafts in torrents rained. As KumbhakarGa felt each stroke From his huge mouth burst fire and smoke; His hands were loosed in mortal pain And dropped his weapons on the plain. Though reft of spear and sword and mace No terror changed his haughty face. With heavy hands he rained his blows And smote to death a thousand foes. Where'er the furious monster strode While down his limbs the red blood flowed
- **Translation**: 

---

### Verse 3 (Ramayan 0.1703)
- **Original**: Canto LXVII. Kumbhakarna's Death. 1685 Like torrents down a mountain's side, Vánars and bears and giants died. High o'er his head a rock he swung, And the huge mass at Ráma flung. But Ráma's arrows bright as flame Shattered the mountain as it came. Then Raghu's son, his eyes aglow With burning anger, charged the foe, And as his bow he strained and tried With fearful clang the cord replied. Wroth at the bowstring's threatening clang To meet his foe the giant sprang. High towering with enormous frame Huge as a wood-crowned hill he came. But Ráma firm and self-possessed In words like these the foe addressed: “Draw near, O Rákshas lord, draw near, Nor turn thee from the fight in fear. Thou meetest Ráma face to face, Destroyer of the giant race. Come, fight, and thou shalt feel this hour, Laid low in death, thy conqueror's power.” He ceased: and mad with wrath and pride The giant champion thus replied: “Come thou to me and thou shalt find A foeman of a different kind. No Khara, no Virádha,— thou Hast met a mightier warrior now. The strength of KumbhakarGa fear, And dread the iron mace I rear This mace in days of yore subdued The Gods and Dánav multitude. Prove, lion of Ikshváku's line,
- **Translation**: 

---

### Verse 4 (Ramayan 0.1704)
- **Original**: 1686 The Ramayana Thy power upon these limbs of mine. Then, after trial, shalt thou bleed, And with thy flesh my hunger feed.” He ceased: and Ráma, undismayed, Upon his cord those arrows laid[478] Which pierced the stately Sál trees through, And Báli king of Vánars slew. They flew, they smote, but smote in vain Those mighty limbs that felt no pain. Then Ráma sent with surest aim The dart that bore the Wind-God's name. The missile from the giant tore His huge arm and the mace it bore, Which crushed the Vánars where it fell: And dire was KumbhakarGa's yell. The giant seized a tree, and then Rushed madly at the lord of men. Another dart, Lord Indra's own, To meet his furious onset thrown, His left arm from the shoulder lopped, And like a mountain peak it dropped. Then from the bow of Ráma sped Two arrows, each with crescent head; And, winged with might which naught could stay, They cut the giant's legs away. They fell, and awful was the sound As those vast columns shook the ground; And sky and sea and hill and cave In echoing roars their answer gave. Then from his side the hero drew A dart that like the tempest flew— No deadlier shaft has ever flown Than that which Indra called his own—
- **Translation**: 

---

### Verse 5 (Ramayan 0.1705)
- **Original**: Canto LXVIII. Rávan's Lament. 1687 Nor could the giant's mail-armed neck The fury of the missile check. Through skin and flesh and bone it smote And rent asunder head and throat. Down with the sound of thunder rolled The head adorned with rings of gold, And crushed to pieces in its fall A gate, a tower, a massive wall. Hurled to the sea the body fell: Terrific was the ocean's swell, Nor could swift fin and nimble leap Save the crushed creatures of the deep. Thus he who plagued in impious pride The Gods and Bráhmans fought and died. Glad were the hosts of heaven, and long The air re-echoed with their song.983 Canto LXVIII. Rávan's Lament. 983 I have abridged this long Canto by omitting some vain repetitions, common- place epithets and similes and other unimportant matter. There are many verses in this Canto which European scholars would rigidly exclude as unmistakeably the work of later rhapsodists. Even the reverent Commentator whom I follow ventures to remark once or twice:Ayam [loka prak shipta iti bahavah,“This [lokaor verse is in the opinion of many interpolated.”
- **Translation**: 

---

### Verse 6 (Ramayan 0.1706)
- **Original**: 1688 The Ramayana They ran to RávaG in his hall And told him of his brother's fall: “Fierce as the God who rules the dead, Upon the routed foe he fed; And, victor for a while, at length Fell slain by Ráma's matchless strength. Now like a mighty hill in size His mangled trunk extended lies, And where he fell, a bleeding mass, Blocks Lanká's gate that none may pass.” The monarch heard: his strength gave way; And fainting on the ground he lay. Grieved at the giants' mournful tale, Long, shrill was Atikáya's wail; And Tri[irás in sorrow bowed His triple head, and wept aloud. Mahodar, Mahápár[va shed Hot tears and mourned their brother dead. At length, his wandering sense restored, In loud lament cried Lanká's lord: “Ah chief, for might and valour famed, Whose arm the haughty foeman tamed, Forsaking me, thy friends and all, Why hast thou fled to Yáma's hall? Why hast thou fled to taste no more The slaughtered foeman's flesh and gore? Ah me, my life is done to-day: My better arm is lopped away. Whereon in danger I relied, And, fearless, Gods and fiends defied. How could a shaft from Ráma's bow The matchless giant overthrow, Whose iron frame so strong of yore The crushing bolt of Indra bore?
- **Translation**: 

---

### Verse 7 (Ramayan 0.1707)
- **Original**: Canto LXIX. Narántak's Death. 1689 This day the Gods and sages meet And triumph at their foe's defeat. This day the Vánar chiefs will boast And, with new ardour fired, their host In fiercer onset will assail Our city, and the ramparts scale. What care I for a monarch's name, For empire, or the Maithil dame? What joy can power and riches give, Or life that I should care to live, Unless this arm in mortal fray The slayer of my brother slay? For me, of KumbhakarGa reft, Death is the only solace left; And I will seek, o'erwhelmed with woes, The realm to which my brother goes. Ah me ill-minded, not to take His counsel when VibhishaG spake When he this evil day foretold My foolish heart was overbold: I drove my sage adviser hence, And reap the fruits of mine offence.” [479] Canto LXIX. Narántak's Death.
- **Translation**: 

---

### Verse 8 (Ramayan 0.1708)
- **Original**: 1690 The Ramayana Pierced to the soul by sorrow's sting Thus wailed the evil-hearted king. Then Tri[irás stood forth and cried: “Yea, father, he has fought and died, Our bravest: and the loss is sore: But rouse thee, and lament no more. Hast thou not still thy coat of mail, Thy bow and shafts which never fail? A thousand asses draw thy car Which roars like thunder heard afar. Thy valour and thy warrior skill, Thy God-given strength, are left thee still. Unarmed, thy matchless might subdued The Gods and Dánav multitude. Armed with thy glorious weapons, how Shall Raghu's son oppose thee now? Or, sire, within thy palace stay; And I myself will sweep away Thy foes, like Garu when he makes A banquet of the writhing snakes. Soon Raghu's son shall press the plain, As Narak984 fell by VishGu slain, Or Zambar985 in rebellious pride Who met the King of Gods986 and died.” The monarch heard: his courage grew, And life and spirit came anew. Devántak and Narántak heard, And their fierce souls with joy were stirred; 984 Narak was a demon, son of Bhúmi or Earth, who haunted the city Prágjy- otisha. 985 Zambar was a demon of drought. 986 Indra.
- **Translation**: 

---

### Verse 9 (Ramayan 0.1709)
- **Original**: Canto LXIX. Narántak's Death. 1691 And Atikáya987 burned to fight, And heard the summons with delight; While from the rest loud rang the cry, “I too will fight,” “and I,” “and I.” The joyous king his sons embraced, With gold and chains and jewels graced, And sent them forth with stirring speech Of benison and praise to each. Forth from the gate the princes sped And ranged for war the troops they led. The Vánar legions charged anew, And trees and rocks for missiles flew. They saw Narántak's mighty form Borne on a steed that mocked the storm. To check his charge in vain they strove: Straight through their host his way he clove, As springs a dolphin through the tide: And countless Vánars fell and died, And mangled limbs and corpses lay To mark the chief's ensanguined way, Sugríva saw them fall or fly When fierce Narántak's steed was nigh, And marked the giant where he sped O'er heaps of dying or of dead. He bade the royal Angad face That bravest chief of giant race. As springs the sun from clouds dispersed, So Angad from the Vánars burst. No weapon for the fight he bore Save nails and teeth, and sought no more. “Leave, giant chieftain,” thus he spoke, 987 Devántak (Slayer of Gods) Narántak (Slayer of Men) Atikáya (Huge of Frame) and Tri[irás (Three Headed) were all sons of RávaG.
- **Translation**: 

---

### Verse 10 (Ramayan 0.1710)
- **Original**: 1692 The Ramayana “Leave foes unworthy of thy stroke, And bend against a nobler heart The terrors of thy deadly dart.” Narántak heard the words he spake: Fast breathing, like an angry snake, With bloody teeth his lips he pressed And hurled his dart at Angad's breast. True was the aim and fierce the stroke, Yet on his breast the missile broke. Then Angad at the giant flew, And with a blow his courser slew: The fierce hand crushed through flesh and bone, And steed and rider fell o'erthrown. Narántak's eyes with fury blazed: His heavy hand on high he raised And struck in savage wrath the head Of Báli's son, who reeled and bled, Fainted a moment and no more: Then stronger, fiercer than before Smote with that fist which naught could stay, And crushed to death the giant lay. Canto LXX. The Death Of Trisirás.
- **Translation**: 

---

### Verse 11 (Ramayan 0.1711)
- **Original**: Canto LXX. The Death Of Trisirás. 1693 Then raged the Rákshas chiefs, and all Burned to avenge Narántak's fall. Devántak raised his club on high And rushed at Angad with a cry. Behind came Tri[irás, and near Mahodar charged with levelled spear. There Angad stood to fight with three: High o'er his head he waved a tree, And at Devántak, swift and true As Indra's flaming bolt, it flew. But, cut by giant shafts in twain, With minished force it flew in vain. A shower of trees and blocks of stone From Angad's hand was fiercely thrown; But well his club Devántak plied And turned each rock and tree aside. Nor yet, by three such foes assailed, [480] The heart of Angad sank or quailed. He slew the mighty beast that bore Mahodar: from his head he tore A bleeding tusk, and blow on blow Fell fiercely on his Rákshas foe. The giant reeled, but strength regained, And furious strokes on Angad rained, Who, wounded by the storm of blows, Sank on his knees, but swiftly rose. Then Tri[irás, as up he sprang, Drew his great bow with awful clang, And fixed three arrows from his sheaf Full in the forehead of the chief. Hanúmán saw, nor long delayed To speed with Níla to his aid, Who at the three-faced giant sent A peak from Lanká's mountain rent.
- **Translation**: 

---

### Verse 12 (Ramayan 0.1712)
- **Original**: 1694 The Ramayana But Tri[irás with certain aim Shot rapid arrows as it came: And shivered by their force it broke And fell to earth with flash and smoke. Then as the Wind-God's son came nigh, Devántak reared his mace on high. Hanúmán smote him on the head And stretched the monstrous giant dead. Fierce Tri[irás with fury strained His bow, and showers of arrows rained That smote on Níla's side and chest: He sank a moment, sore distressed; But quickly gathered strength to seize A mountain with its crown of trees. Crushed by the hill, distained with gore, Mahodar fell to rise no more. Then Tri[irás raised high his spear Which chilled the trembling foe with fear And, like a flashing meteor through The air at Hanúmán it flew. The Vánar shunned the threatened stroke, And with strong hands the weapon broke. The giant drew his glittering blade: Dire was the wound the weapon made Deep in the Vánar's ample chest, Who, for a moment sore oppressed, Raised his broad hand, regaining might, And struck the rover of the night. Fierce was the blow: with one wild yell Low on the earth the monster fell. Hanúmán seized his fallen sword Which served no more its senseless lord, And from the monster triple-necked
- **Translation**: 

---

### Verse 13 (Ramayan 0.1713)
- **Original**: Canto LXXI. Atikáya's Death. 1695 Smote his huge heads with crowns bedecked. Then Mahápár[va burned with ire; Fierce flashed his eyes with vengeful fire. A moment on the dead he gazed, Then his black mace aloft was raised, And down the mass of iron came That struck and shook the Vánar's frame. Hanúmán's chest was wellnigh crushed, And from his mouth red torrents gushed: Yet served one instant to restore His spirit: from the foe he tore His awful mace, and smote, and laid The giant in the dust dismayed. Crushed were his jaws and teeth and eyes: Breathless and still he lay as lies A summit from a mountain rent By him who rules the firmament. Canto LXXI. Atikáya's Death. But Atikáya's wrath grew high To see his noblest kinsmen die. He, fiercest of the giant race, Presuming still on Brahmá's grace; Proud tamer of the Immortals' pride, Whose power and might with Indra's vied, For blood and vengeful carnage burned, And on the foe his fury turned. High on a car that flashed and glowed Bright as a thousand suns he rode. Around his princely brows was set
- **Translation**: 

---

### Verse 14 (Ramayan 0.1714)
- **Original**: 1696 The Ramayana A rich bejewelled coronet. Gold pendants in his ears he wore; He strained and tried the bow he bore, And ever, as a shaft he aimed, His name and royal race proclaimed. Scarce might the Vánars brook to hear His clanging bow and voice of fear: To Raghu's elder son they fled, Their sure defence in woe and dread. Then Ráma bent his eyes afar And saw the giant in his car Fast following the flying crowd And roaring like a rainy cloud. He, with the lust of battle fired, Turned to VibhishaG and inquired: “Say, who is this, of mountain size, This archer with the lion eyes? His car, which strikes our host with awe, A thousand eager coursers draw. Surrounded by the flashing spears Which line his car, the chief appears Like some huge cloud when lightnings play About it on a stormy day; And the great bow he joys to hold Whose bended back is bright with gold, As Indra's bow makes glad the skies, That best of chariots glorifies. O see the sunlike splendour flung From the great flag above him hung, Where, blazoned with refulgent lines, Ráhu988 the dreadful Dragon shines. Full thirty quivers near his side, 988 The demon of eclipse who seizes the Sun and Moon.
- **Translation**: 

---

### Verse 15 (Ramayan 0.1715)
- **Original**: Canto LXXI. Atikáya's Death. 1697 His car with shafts is well supplied: [481] And flashing like the light of stars Gleam his two mighty scimitars. Say, best of giants, who is he Before whose face the Vánars flee?” Thus Ráma spake. VibhishaG eyed The giants' chief, and thus replied: “This Ráma, this is RávaG's son: High fame his youthful might has won. He, best of warriors, bows his ear The wisdom of the wise to hear. Supreme is he mid those who know The mastery of sword and bow. Unrivalled in the bold attack On elephant's or courser's back, He knows, beside, each subtler art, To win the foe, to bribe, or part. On him the giant hosts rely, And fear no ill when he is nigh. This peerless chieftain bears the name Of Atikáya huge of frame, Whom Dhanyamáliní of yore To RávaG lord of Lanká bore.” Roused by his bow-string's awful clang, To meet their foes the Vánars sprang. Armed with tall trees from Lanká's wood, And rocks and mountain peaks, they stood. The giant's arrows, gold-bedecked, The storm of hurtling missiles checked; And ever on his foemen poured Fierce tempest from his clanging cord; Nor could the Vánar chiefs sustain
- **Translation**: 

---

### Verse 16 (Ramayan 0.1716)
- **Original**: 1698 The Ramayana His shafts' intolerable rain. They fled: the victor gained the place Where stood the lord of Raghu's race, And cried with voice of thunder:“Lo, Borne on my car, with shaft and bow, I, champion of the giants, scorn To fight with weaklings humbly born. Come forth your bravest, if he dare, And fight with one who will not spare.” Forth sprang Sumitrá's noble child,989 And strained his ready bow, and smiled; And giants trembled as the clang Through heaven and earth reëchoing rang. The giant to his string applied A pointed shaft, and proudly cried; “Turn, turn, Sumitrá's son and fly, For terrible as Death am I. Fly, nor that youthful form oppose, Untrained in war, to warriors' blows. What! wilt thou waste thy childish breath And wake the dormant fire of death? Cast down, rash boy, that useless bow: Preserve thy life, uninjured go.” He ceased: and stirred by wrath & pride Sumitrá's noble son replied: “By warlike deed, not words alone, The valour of the brave is shown. Cease with vain boasts my scorn to move, And with thine arm thy prowess prove. Borne on thy car, with sword and bow, With all thine arms, thy valour show. 989 Lakshma G.
- **Translation**: 

---

### Verse 17 (Ramayan 0.1717)
- **Original**: Canto LXXI. Atikáya's Death. 1699 Fight, and my deadly shafts this day Low in the dust thy head shall lay, And, rushing fast in ceaseless flood, Shall rend thy flesh and drink thy blood.” His giant foe no answer made, But on his string an arrow laid. He raised his arm, the cord he drew, At LakshmaG's breast the arrow flew. Sumitrá's son, his foemen's dread, Shot a fleet shaft with crescent head, Which cleft that arrow pointed well, And harmless to the earth it fell. A shower of shafts from LakshmaG's bow Fell fast and furious on the foe Who quailed not as the missiles smote With idle force his iron coat. Then came the friendly Wind-God near, And whispered thus in LakshmaG's ear: “Such shafts as these in vain assail Thy foe's impenetrable mail. A more tremendous missile try, Or never may the giant die. Employ the mighty spell, and aim The weapon known by Brahmá's name.” He ceased; Sumitrá's son obeyed: On his great bow the shaft was laid, And with a roar like thunder, true As Indra's flashing bolt, it flew. The giant poured his shafts like rain To check its course, but all in vain. With spear and mace and sword he tried To turn the fiery dart aside. Winged with a force which naught could check,
- **Translation**: 

---

### Verse 18 (Ramayan 0.1718)
- **Original**: 1700 The Ramayana It smote the monster in the neck, And, sundered from his shoulders, rolled To earth his head and helm of gold. Canto LXXII. Rávan's Speech. The giants bent, in rage and grief, Their eyes upon the fallen chief: Then flying wild with fear and pale To RávaG bore the mournful tale. He heard how Atikáya died, Then turned him to his lords, and cried: “Where are they now— my bravest— where, Wise to consult and prompt to dare? Where is Dhúmráksha, skilled to wield All weapons in the battle field? Akampan, and Prahasta's might, And Kumbhakar Ga bold in fight? These, these and many a Rákshas more, Each master of the arms he bore,[482] Who every foe in fight o'erthrew, The victors none could e'er subdue, Have perished by the might of one, The vengeful arm of Raghu's son. In vain I cast mine eyes around, No match for Ráma here is found, No chief to stand before that bow Whose deadly shafts have caused our woe. Now, warriors, to your stations hence; Provide ye for the wall's defence, And be the A[oka garden, where
- **Translation**: 

---

### Verse 19 (Ramayan 0.1719)
- **Original**: Canto LXXIII. Indrajít's Victory. 1701 The lady lies, your special care. Be every lane and passage barred, Set at each gate a chosen guard. And with your troops, where danger calls, Be ready to defend the walls. Each movement of the Vánars mark; Observe them when the skies grow dark; Be ready in the dead of night, And ere the morning bring the light. Taught by our loss we may not scorn These legions of the forest-born.” He ceased: the Rákshas lords obeyed; Each at his post his troops arrayed: And, torn with pangs that pierced him through The monarch from the hall withdrew. Canto LXXIII. Indrajít's Victory. But Indrajít the fierce and bold With words like these his sire consoled: “Dismiss, O King, thy grief and dread, And be not thus disquieted. Against this numbing sorrow strive, For Indrajít is yet alive; And none in battle may withstand The fury of his strong right hand. This day, O sire, thine eyes shall see The sons of Raghu slain by me.”
- **Translation**: 

---

### Verse 20 (Ramayan 0.1720)
- **Original**: 1702 The Ramayana He ceased: he bade the king farewell: Clear, mid the roar of drum and shell, The clash of sword and harness rang As to his car the warrior sprang. Close followed by his Rákshas train Through Lanká's gate he reached the plain. Then down he leapt, and bade a band Of giants by the chariot stand: Then with due rites, as rules require, Did worship to the Lord of Fire. The sacred oil, as texts ordain, With wreaths of scented flowers and grain, Within the flame in order due, That mightiest of the giants threw. There on the ground were spear and blade, And arrowy leaves and fuel laid; An iron ladle deep and wide, And robes with sanguine colours dyed. Beside him stood a sable goat: The giant seized it by the throat, And straight from the consuming flame Auspicious signs of victory came. For swiftly, curling to the right, The fire leapt up with willing light Undimmed by smoky cloud, and, red Like gold, upon the offering fed. They brought him, while the flame yet glowed, The dart by Brahmá's grace bestowed, And all the arms he wielded well Were charmed with text and holy spell. Then fiercer for the fight he burned, And at the foe his chariot turned, While all his followers lifting high
- **Translation**: 

---

