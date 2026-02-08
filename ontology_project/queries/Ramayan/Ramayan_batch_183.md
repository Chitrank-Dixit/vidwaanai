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

### Verse 1 (Ramayana 0.1686)
- **Original**: 1668 The Ramayana The chains of slumber and awake.” He ceased: and Brahmá made reply; “Six months in slumber shall he lie And then arising for a day Shall cast the numbing bonds away.” Now Ráva G in his doubt and dread Has roused the monster from his bed, Who comes in this the hour of need On slaughtered Vánars flesh to feed. Each Vánar, when his awe-struck eyes Behold the monstrous chieftain, flies. With hopeful words their minds deceive, And let our trembling hosts believe They see no giant, but, displayed, A lifeless engine deftly made.” Then Ráma called to Níla:“Haste, Let troops near every gate be placed, And, armed with fragments of the rock And trees, each lane and alley block.”[473] Thus Ráma spoke: the chief obeyed, And swift the Vánars stood arrayed, As when the black clouds their battle form, The summit of a hill to storm. Canto LXII. Rávan's Request.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1687)
- **Original**: Canto LXII. Rávan's Request. 1669 Along bright Lanká's royal road The giant, roused from slumber, strode, While from the houses on his head A rain of fragrant flowers was shed. He reached the monarch's gate whereon Rich gems and golden fretwork shone. Through court and corridor that shook Beneath his tread his way he took, And stood within the chamber where His brother sat in dark despair. But sudden, at the grateful sight The monarch's eye again grew bright. He started up, forgot his fear, And drew his giant brother near. The younger pressed the elder's feet And paid the King observance meet, Then cried:“O Monarch, speak thy will, And let my care thy word fulfil. What sudden terror and dismay Have burst the bonds in which I lay?” Fierce flashed the flame from RávaG's eye, As thus in wrath he made reply: “Fair time, I ween, for sleep is this, To lull thy soul in tranquil bliss, Unheeding, in oblivion drowned, The dangers that our lives surround. Brave Ráma, Da[aratha's son, A passage o'er the sea has won, And, with the Vánar monarch's aid, Round Lanká's walls his hosts arrayed. Though never in the deadly field My Rákshas troops were known to yield, The bravest of the giant train
- **Translation**: 

---

### Verse 3 (Ramayana 0.1688)
- **Original**: 1670 The Ramayana Have fallen by the Vánars slain. Hence comes my fear. O fierce and brave, Go forth, our threatened Lanká save. Go forth, a dreadful vengeance take: For this, O chief, I bade thee wake. The Gods and trembling fiends have felt The furious blows thine arm has dealt. Earth has no warrior, heaven has none To match thy might, Paulastya's son.” Canto LXIII. Kumbhakarna's Boast. Then KumbhakarGa laughed aloud And cried;“O Monarch, once so proud, We warned thee, but thou wouldst not hear; And now the fruits of sin appear. We warned thee, I, thy nobles, all Who loved thee, in thy council hall. Those sovereigns who with blinded eyes Neglect the foe their hearts despise, Soon, falling from their high estate Bring on themselves the stroke of fate. Accept at length, thy life to save, The counsel sage VibhishaG gave, The prudent counsel spurned before, And Sítá to her lord restore.”972 972 I omit a tedious sermon on the danger of rashness and the advantages of prudence, sufficient to irritate a less passionate hearer than RávaG.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1689)
- **Original**: Canto LXIII. Kumbhakarna's Boast. 1671 The monarch frowned, by passion moved And thus in angry words reproved: “Wilt thou thine elder brother school, Forgetful of the ancient rule That bids thee treat him as the sage Who guides thee with the lore of age? Think on the dangers of the day, Nor idly throw thy words away: If, led astray, by passion stirred, I in the pride of power have erred; If deeds of old were done amiss, No time for vain reproach is this. Up, brother; let thy loving care The errors of thy king repair.” To calm his wrath, his soul to ease, The younger spake in words like these: “Yea, from our bosoms let us cast All idle sorrow for the past. Let grief and anger be repressed: Again be firm and self-possessed. This day, O Monarch, shalt thou see The Vánar legions turn and flee, And Ráma and his brother slain With their hearts' blood shall dye the plain. Yea, if the God who rules the dead, And VaruG their battalions led; If Indra with the Storm-Gods came Against me, and the Lord of Flame, Still would I fight with all and slay Thy banded foes, my King, to-day. If Raghu's son this day withstand The blow of mine uplifted hand, Deep in his breast my darts shall sink,
- **Translation**: 

---

### Verse 5 (Ramayana 0.1690)
- **Original**: 1672 The Ramayana And torrents of his life-blood drink. O fear not, in my promise trust: This arm shall lay him in the dust, Shall leave the fierce Sugríva dyed With gore, and LakshmaG by his side, And strike the great Hanúmán down, The spoiler of our glorious town.”973 [474] Canto LXIV. Mahodar's Speech. He ceased: and when his lips were closed Mahodar thus his rede opposed: “Why wilt thou shame thy noble birth And speak like one of little worth? Why boast thee thus in youthful pride Rejecting wisdom for thy guide? How will thy single arm oppose The victor of a thousand foes, Who proved in Janasthán his might And slew the rovers of the night? The remnant of those legions, they Who saw his power that fatal day, Now in this leaguered city dread The mighty chief from whom they fled. And wouldst thou meet the lord of men, Beard the great lion in his den, 973 The Bengal recension assigns a very different speech to KumbhakarGa and makes him say that Nárad the messenger of the Gods had formerly told him that VishGu himself incarnate as Da[aratha's son should come to destroy RávaG.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1691)
- **Original**: Canto LXIV. Mahodar's Speech. 1673 And, when thine eyes are open, break The slumber of a deadly snake? Who may an equal battle wage With him, so awful in his rage, Fierce as the God of Death whom none May vanquish, Da[aratha's son? But, RávaG, shall the lady still Refuse compliance with thy will? No, listen, King, to this design Which soon shall make the captive thine. This day through Lanká's streets proclaim That four of us974 of highest fame With KumbhakarGa at our head Will strike the son of Raghu dead. Forth to the battle will we go And prove our prowess on the foe. Then, if our bold attempt succeed, No further plans thy hopes will need. But if in vain our warriors strive, And Raghu's son be left alive, We will return, and, wounded sore, Our armour stained with gouts of gore, Will show the shafts that rent each frame, Keen arrows marked with Ráma's name, And say we giants have devoured The princes whom our might o'erpowered. Then let the joyful tidings spread That Raghu's royal sons are dead. To all around thy pleasure show, Gold, pearls, and precious robes, bestow. Gay garlands round the portals twine, Enjoy the banquet and the wine. 974 Mahodar, Dwijihva, Sanhráda, and Vitardan.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1692)
- **Original**: 1674 The Ramayana Then go, the scornful lady seek, And woo her when her heart is weak. Rich robes and gold and gems display, And gently wile her grief away. Then will she feel her hopeless state, Widowed, forlorn, and desolate; Know that on thee her bliss depends, Far from her country and her friends; Then, her proud spirit overthrown, The lady will be all thine own.” Canto LXV. Kumbhakarna's Speech. But haughty KumbhakarGa spurned His counsel, and to RávaG turned: “Thy life from peril will I free And slay the foe who threatens thee. A hero never vaunts in vain, Like bellowing clouds devoid of rain, Nor, Monarch, be thine ear inclined To counsellors of slavish kind, Who with mean arts their king mislead And mar each gallant plan and deed. O, let not words like his beguile The glorious king of Lanká's isle.”
- **Translation**: 

---

### Verse 8 (Ramayana 0.1693)
- **Original**: Canto LXV. Kumbhakarna's Speech. 1675 Thus scornful KumbhakarGa cried, And RávaG with a laugh replied: “Mahodar fears and fain would shun The battle with Ikshváku's son. Of all my giant warriors, who Is strong as thou, and brave and true? Ride, conqueror, to the battle ride, And tame the foeman's senseless pride. Go forth like Yáma to the field, And let thine arm thy trident wield. Scared by the lightning of thine eye The Vánar hosts will turn and fly; And Ráma, when he sees thee near, With trembling heart will own his fear.” The champion heard, and, well content, Forth from the hall his footsteps bent. He grasped his spear, the foeman's dread, Black iron all, both shaft and head, Which, dyed in many a battle, bore Great spots of slaughtered victims' gore. The king upon his neck had thrown The jewelled chain which graced his own. And garlands of delicious scent About his limbs for ornament. Around his arms gay bracelets clung, And pendants in his ears were hung. Adorned with gold, about his waist His coat of mail was firmly braced, And like NáráyaG975 or the God Who rules the sky he proudly trod. Behind him went a mighty throng Of giant warriors tall and strong, [475] 975 A name of VishGu.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1694)
- **Original**: 1676 The Ramayana On elephants of noblest breeds. With cars, with camels, and with steeds: And, armed with spear and axe and sword Were fain to battle for their lord.976 Canto LXVI. Kumbhakarna's Sally. In pomp and pride of warlike state The giant passed the city gate. He raised his voice: the hills, the shore Of Lanká's sea returned the roar. The Vánars saw the chief draw nigh Whom not the ruler of the sky, Nor Yáma, monarch of the dead, Might vanquish, and affrighted fled. When royal Angad, Báli's son, Saw the scared Vánars turn and run, Undaunted still he kept his ground, And shouted as he gazed around: “O Nala, Níla, stay nor let Your souls your generous worth forget, O Kumud and Gaváksha, why Like base-born Vánars will ye fly? Turn, turn, nor shame your order thus: This giant is no match for us” 976 There is so much commonplace repetition in these Sallies of the Rákshas chieftains that omissions are frequently necessary. The usual ill omens attend the sally of KumbhakarGa, and the Canto ends with a description of the terrified Vánars' flight which is briefly repeated in different words at the beginning of the next Canto.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1695)
- **Original**: Canto LXVI. Kumbhakarna's Sally. 1677 They heard his voice: the flight was stayed; Again for war they stood arrayed, And hurled upon the foe a shower Of mountain peaks and trees in flower. Still on his limbs their missiles rained: Unmoved, their blows he still sustained, And seemed unconscious of the stroke When rocks against his body broke. Fierce as the flame when woods are dry He charged with fury in his eye. Like trees consumed with fervent heat They fell beneath the giant's feet. Some o'er the ground, dyed red with gore, Fled wild with terror to the shore, And, deeming that all hope was lost, Ran to the bridge they erst had crossed. Some clomb the trees their lives to save, Some sought the mountain and the cave; Some hid them in the bosky dell, And there in deathlike slumber fell. When Angad saw the chieftains fly He called them with a mighty cry: “Once more, O Vánars, charge once more, On to the battle as before. In all her compass earth has not, To hide you safe, one secret spot. What! leave your arms? each nobler dame Will scorn her consort for the shame. This blot upon your names efface, And keep your valour from disgrace. Stay, chieftains; wherefore will ye run, A band of warriors scared by one?”
- **Translation**: 

---

### Verse 11 (Ramayana 0.1696)
- **Original**: 1678 The Ramayana Scarce would they hear: they would not stay, And basely spoke in wild dismay: “Have we not fought, and fought in vain Have we not seen our mightiest slain? The giant's matchless force we fear, And fly because our lives are dear.” But Báli's son with gentle art Dispelled their dread and cheered each heart. They turned and formed and waited still Obedient to the prince's will. Canto LXVII. Kumbhakarna's Death. Thus from their flight the Vánars turned, And every heart for battle burned, Determined on the spot to die Or gain a warrior's meed on high. Again the Vánars stooped to seize Their weapons, rocks and fallen trees; Again the deadly fight began, And fiercely at the giant ran. Unmoved the monster kept his place: He raised on high his awful mace, Whirled the huge weapon round his head And laid the foremost Vánars dead. Eight thousand fell bedewed with gore, Then sank and died seven hundred more. Then thirty, twenty, ten, or eight At each fierce onset met their fate, And fast the fallen were devoured Like snakes by Garu 's beak o'erpowered.
- **Translation**: 

---

### Verse 12 (Ramayana 0.1697)
- **Original**: Canto LXVII. Kumbhakarna's Death. 1679 Then Dwivid from the Vánar van, Armed with an uptorn mountain, ran, Like a huge cloud when fierce winds blow, And charged amain the mountain foe. With wondrous force the hill he threw: O'er KumbhakarGa's head it flew, And falling on his host afar Crushed many a giant, steed, and car. Rocks, trees, by fierce Hanúmán sped, Rained fast on KumbhakarGa's head. Whose spear each deadlier missile stopped, And harmless on the plain it dropped. [476] Then with his furious eyes aglow The giant rushed upon the foe, Where, with a woody hill upheaved, Hanúmán's might his charge received. Through his vast frame the giant felt The angry blow Hanúmán dealt. He reeled a moment, sore distressed, Then smote the Vánar on the breast, As when the War-God's furious stroke Through Krauncha's hill a passage broke.977 Fierce was the blow, and deep and wide The rent: with crimson torrents dyed, Hanúmán, maddened by the pain, Roared like a cloud that brings the rain, And from each Rákshas throat rang out Loud clamour and exultant shout. Then Níla hurled with mustered might The fragment of a mountain height; 977 Kártikeya the God of War, and the hero and incarnation Para[uráma are said to have cut a passage through the mountain Krauncha, a part of the Himálayan range, in the same way as the immense gorge that splits the Pyrenees under the towers of Marboré was cloven at one blow of Roland's sword Durandal.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1698)
- **Original**: 1680 The Ramayana Nor would the rock the foe have missed, But KumbhakarGa raised his fist And smote so fiercely that the mass Fell crushed to powder on the grass. Five chieftains of the Vánar race978 Charged KumbhakarGa face to face, And his huge frame they wildly beat With rocks and trees and hands and feet. Round Rishabh first the giant wound His arms and hurled him to the ground, Where speechless, senseless, wounded sore, He lay his face besmeared with gore. Then Níla with his fist he slew, And Zarabh with his knee o'erthrew, Nor could Gaváksha's strength withstand The force of his terrific hand. At Gandhamádan's eager call Rushed thousands to avenge their fall, Nor ceased those Vánars to assail With knee and fist and tooth and nail. Around his foes the giant threw His mighty arms, and nearer drew The captives subject to his will: Then snatched them up and ate his fill. There was no respite then, no pause: Fast gaped and closed his hell-like jaws: Yet, prisoned in that gloomy cave, Some Vánars still their lives could save: Some through his nostrils found a way, Some through his ears resought the day. Like Indra with his thunder, like The God of Death in act to strike, 978 Rishabh,Zarabh, Níla, Gaváksha, and Gandhamádan.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1699)
- **Original**: Canto LXVII. Kumbhakarna's Death. 1681 The giant seized his ponderous spear, And charged the foe in swift career. Before his might the Vánars fell, Nor could their hosts his charge repel. Then trembling, nor ashamed to run, They turned and fled to Raghu's son. When Báli's warrior son979 beheld Their flight, his heart with fury swelled. He rushed, with his terrific shout, To meet the foe and stay the rout. He came, he hurled a mountain peak, And smote the giant on the cheek. His ponderous spear the giant threw: Fierce was the cast, the aim was true; But Angad, trained in war and tried, Saw ere it came, and leapt aside. Then with his open hand he smote The giant on the chest and throat. That blow the giant scarce sustained; But sense and strength were soon regained. With force which nothing might resist He caught the Vánar by the wrist, Whirled him, as if in pastime, round, And dashed him senseless on the ground. There low on earth his foe lay crushed: At King Sugríva next he rushed, Who, waiting for the charge, stood still, And heaved on high a shattered hill, He looked on KumbhakarGa dyed With streams of blood, and fiercely cried: “Great glory has thine arm achieved, 979 Angad. The text calls him the son of the son of him who holds the thunderbolt,i.e.the grandson of Indra.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1700)
- **Original**: 1682 The Ramayana And thousands of their lives bereaved. Now leave a while thy meaner foes, And brook the hill Sugríva throws.” He spoke, and hurled the mass he held: The giant's chest the stroke repelled, Then on the Vánars fell despair, And Rákshas clamour filled the air. The giant raised his arm, and fast Came the tremendous980 spear he cast. Hanúmán caught it as it flew, And knapped it on his knee in two. The giant saw the broken spear: His clouded eye confessed his fear; Yet at Sugríva's head he sent A peak from Lanká's mountain rent.[477] The rushing mass no might could stay: Sugríva fell and senseless lay. The giant stooped his foe to seize, And bore him thence, as bears the breeze A cloud in autumn through the sky. He heard the sad Immortals sigh, And shouts of triumph long and loud Went up from all the Rákshas crowd. Through Lanká's gate the giant passed Holding his struggling captive fast, While from each terrace, house, and tower Fell on his haughty head a shower Of fragrant scent and flowery rain, Blossoms and leaves and scattered grain.981 980 Literally, weighing a thousandbháras. The bhára is a weight equal to 2000 palas, thepalais equal to fourkar[as, and thekar[a to 11375 French grammes or about 176 grains troy. The spear seems very light for a warrior of Kumbhakar Ga's strength and stature and the work performed with it. 981 The custom of throwing parched or roasted grain, with wreaths and flowers,
- **Translation**: 

---

### Verse 16 (Ramayana 0.1701)
- **Original**: Canto LXVII. Kumbhakarna's Death. 1683 By slow degrees the Vánars' lord Felt life and sense and strength restored. He heard the giants' joyful boast: He thought upon his Vánar host. His teeth and feet he fiercely plied, And bit and rent the giant's side, Who, mad with pain and smeared with gore, Hurled to the ground the load he bore. Regardless of a storm of blows Swift to the sky the Vánar rose, Then lightly like a flying ball High overleapt the city wall, And joyous for deliverance won Regained the side of Raghu's son. And Kumbhakar Ga, mad with hate And fury, sallied from the gate, The carnage of the foe renewed And filled his maw with gory food. Slaying, with headlong frenzy blind, Both Vánar foes and giant kind. Nor would Sumitrá's valiant son982 The might of KumbhakarGa shun, Who through his harness felt the sting Of keen shafts loosened from the string. His heart confessed the warrior's power, And, bleeding from the ceaseless shower That smote him on the chest and side, With words like these the giant cried: “Well fought, well fought, Sumitrá's son; Eternal glory hast thou won, on the heads of kings and conquerors when they go forth to battle and return is frequently mentioned by Indian poets. 982 Lakshma G.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1702)
- **Original**: 1684 The Ramayana For thou in desperate fight hast met The victor never conquered yet, Whom, borne on huge Airávat's back, E'en Indra trembles to attack. Go, son of Queen Sumitrá, go: Thy valour and thy strength I know. Now all my hope and earnest will Is Ráma in the fight to kill. Let him beneath my weapons fall, And I will meet and conquer all.” The chieftain, of Sumitrá born, Made answer as he laughed in scorn: “Yea, thou hast won a victor's fame From trembling Gods and Indra's shame. There waits thee now a mightier foe Whose prowess thou hast yet to know. There, famous in a hundred lands, Ráma the son of Raghu stands.” Straight at the king the giant sped, And earth was shaken at his tread. His bow the hero grasped and strained, And deadly shafts in torrents rained. As KumbhakarGa felt each stroke From his huge mouth burst fire and smoke; His hands were loosed in mortal pain And dropped his weapons on the plain. Though reft of spear and sword and mace No terror changed his haughty face. With heavy hands he rained his blows And smote to death a thousand foes. Where'er the furious monster strode While down his limbs the red blood flowed
- **Translation**: 

---

### Verse 18 (Ramayana 0.1703)
- **Original**: Canto LXVII. Kumbhakarna's Death. 1685 Like torrents down a mountain's side, Vánars and bears and giants died. High o'er his head a rock he swung, And the huge mass at Ráma flung. But Ráma's arrows bright as flame Shattered the mountain as it came. Then Raghu's son, his eyes aglow With burning anger, charged the foe, And as his bow he strained and tried With fearful clang the cord replied. Wroth at the bowstring's threatening clang To meet his foe the giant sprang. High towering with enormous frame Huge as a wood-crowned hill he came. But Ráma firm and self-possessed In words like these the foe addressed: “Draw near, O Rákshas lord, draw near, Nor turn thee from the fight in fear. Thou meetest Ráma face to face, Destroyer of the giant race. Come, fight, and thou shalt feel this hour, Laid low in death, thy conqueror's power.” He ceased: and mad with wrath and pride The giant champion thus replied: “Come thou to me and thou shalt find A foeman of a different kind. No Khara, no Virádha,— thou Hast met a mightier warrior now. The strength of KumbhakarGa fear, And dread the iron mace I rear This mace in days of yore subdued The Gods and Dánav multitude. Prove, lion of Ikshváku's line,
- **Translation**: 

---

### Verse 19 (Ramayana 0.1704)
- **Original**: 1686 The Ramayana Thy power upon these limbs of mine. Then, after trial, shalt thou bleed, And with thy flesh my hunger feed.” He ceased: and Ráma, undismayed, Upon his cord those arrows laid[478] Which pierced the stately Sál trees through, And Báli king of Vánars slew. They flew, they smote, but smote in vain Those mighty limbs that felt no pain. Then Ráma sent with surest aim The dart that bore the Wind-God's name. The missile from the giant tore His huge arm and the mace it bore, Which crushed the Vánars where it fell: And dire was KumbhakarGa's yell. The giant seized a tree, and then Rushed madly at the lord of men. Another dart, Lord Indra's own, To meet his furious onset thrown, His left arm from the shoulder lopped, And like a mountain peak it dropped. Then from the bow of Ráma sped Two arrows, each with crescent head; And, winged with might which naught could stay, They cut the giant's legs away. They fell, and awful was the sound As those vast columns shook the ground; And sky and sea and hill and cave In echoing roars their answer gave. Then from his side the hero drew A dart that like the tempest flew— No deadlier shaft has ever flown Than that which Indra called his own—
- **Translation**: 

---

### Verse 20 (Ramayana 0.1705)
- **Original**: Canto LXVIII. Rávan's Lament. 1687 Nor could the giant's mail-armed neck The fury of the missile check. Through skin and flesh and bone it smote And rent asunder head and throat. Down with the sound of thunder rolled The head adorned with rings of gold, And crushed to pieces in its fall A gate, a tower, a massive wall. Hurled to the sea the body fell: Terrific was the ocean's swell, Nor could swift fin and nimble leap Save the crushed creatures of the deep. Thus he who plagued in impious pride The Gods and Bráhmans fought and died. Glad were the hosts of heaven, and long The air re-echoed with their song.983 Canto LXVIII. Rávan's Lament. 983 I have abridged this long Canto by omitting some vain repetitions, common- place epithets and similes and other unimportant matter. There are many verses in this Canto which European scholars would rigidly exclude as unmistakeably the work of later rhapsodists. Even the reverent Commentator whom I follow ventures to remark once or twice:Ayam [loka prak shipta iti bahavah,“This [lokaor verse is in the opinion of many interpolated.”
- **Translation**: 

---

