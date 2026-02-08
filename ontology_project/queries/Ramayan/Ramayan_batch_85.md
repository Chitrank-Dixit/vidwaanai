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

### Verse 1 (Ramayan 0.1681)
- **Original**: Canto LX. Kumbhakarna Roused. 1663 They reached the dwelling where he lay, A cave that reached a league each way, Sweet with fair blooms of lovely scent And bright with golden ornament. His breathings came so fierce and fast, Scarce could the giants brook the blast. They found him on a golden bed With his huge limbs at length outspread. They piled their heaps of venison near, Fat buffaloes and boars and deer. With wreaths of flowers they fanned his face, And incense sweetened all the place. Each raised his mighty voice as loud As thunders of an angry cloud, And conchs their stirring summons gave That echoed through the giant's cave. Then on his breast they rained their blows, And high the wild commotion rose When cymbal vied with drum and horn. And war cries on the gale upborne. Through all the air loud discord spread, And, struck with fear, the birds fell dead. But still he slept and took his rest. Then dashed they on his shaggy chest Clubs, maces, fragments of the rock: He moved not once, nor felt the shock. The giants made one effort more With shell and drum and shout and roar. Club, mallet, mace, in fury plied, Rained blows upon his breast and side. And elephants were urged to aid, And camels groaned and horses neighed. They drenched him with a hundred pails, They tore his ears with teeth and nails.
- **Translation**: 

---

### Verse 2 (Ramayan 0.1682)
- **Original**: 1664 The Ramayana They bound together many a mace And beat him on the head and face; And elephants with ponderous tread Stamped on his limbs and chest and head. The unusual weight his slumber broke: He started, shook his sides, and woke; And, heedless of the wounds and blows, Yawning with thirst and hunger rose, His jaws like hell gaped fierce and wide, Dire as the flame neath ocean's tide. Red as the sun on Meru's crest The giant's face his wrath expressed, And every burning breath he drew Was like the blast that rushes through The mountain cedars. Up he raised His awful head with eyes that blazed Like comets, dire as Death in form Who threats the worlds with fire and storm. The giants pointed to their stores Of buffaloes and deer and boars, And straight he gorged him with a flood Of wine, with marrow, flesh, and blood. He ceased: the giants ventured near And bent their lowly heads in fear. Then Kumbhakar[n.]a glared with eyes Still heavy in their first surprise, Still drowsy from his troubled rest, And thus the giant band addressed. “How have ye dared my sleep to break? No trifling cause should bid me wake. Say, is all well? or tell the need That drives you with unruly speed To wake me. Mark the words I say, The king shall tremble in dismay,[472]
- **Translation**: 

---

### Verse 3 (Ramayan 0.1683)
- **Original**: Canto LX. Kumbhakarna Roused. 1665 The fire be quenched and Indra slain Ere ye shall break my rest in vain.” Yúpáksha answered:“Chieftain, hear; No God or fiend excites our fear. But men in arms our walls assail: We tremble lest their might prevail. For vengeful Ráma vows to slay The foe who stole his queen away, And, matchless for his warlike deeds, A host of mighty Vánars leads. Ere now a monstrous Vánar came, Laid Lanká waste with ruthless flame, And Aksha, RávaG's offspring, slew With all his warrior retinue. Our king who never trembled yet For heavenly hosts in battle met, At length the general dread has shared, O'erthrown by Ráma's arm and spared.” He ceased: and KumbhakarGa spake: “I will go forth and vengeance take; Will tread their hosts beneath my feet, Then triumph-flushed our king will meet. Our giant bands shall eat their fill Of Vánars whom this arm shall kill. The princes' blood shall be my draught, The chieftains' shall by you be quaffed.” He spake, and, with an eager stride That shook the earth, to RávaG hied.
- **Translation**: 

---

### Verse 4 (Ramayan 0.1684)
- **Original**: 1666 The Ramayana Canto LXI. The Vánars' Alarm. The son of Raghu near the wall Saw, proudly towering over all, The mighty giant stride along Attended by the warrior throng; Heard KumbhakarGa's heavy feet Awake the echoes of the street; And, with the lust of battle fired, Turned to VibhishaG and inquired: “VibhishaG, tell that chieftain's name Who rears so high his mountain frame; With glittering helm and lion eyes, Preëminent in might and size Above the rest of giant birth, He towers the standard of the earth; And all the Vánars when they see The mighty warrior turn and flee.” “In him,” VibhishaG answered,“know Vi[ravas' son, the Immortals' foe, Fierce KumbhakarGa, mightier far Than Gods and fiends and giants are. He conquered Yáma in the fight, And Indra trembling owned his might. His arm the Gods and fiends subdued, Gandharvas and the serpent brood. The rest of his gigantic race Are wondrous strong by God-giving grace; But nature at his birth to him Gave matchless power and strength of limb. Scarce was he born, fierce monster, when He killed and ate a thousand men. The trembling race of men, appalled,
- **Translation**: 

---

### Verse 5 (Ramayan 0.1685)
- **Original**: Canto LXI. The Vánars' Alarm. 1667 On Indra for protection called; And he, to save the suffering world, His bolt at KumbhakarGa hurled. So awful was the monster's yell That fear on all the nations fell, He, rushing on with furious roar, A tusk from huge Airávat tore, And dealt the God so dire a blow That Indra reeling left his foe, And with the Gods and mortals fled To Brahmá's throne dispirited. “O Brahmá,” thus the suppliants cried, “Some refuge for this woe provide. If thus his maw the giant sate Soon will the world be desolate.” The Self-existent calmed their woe, And spake in anger to their foe: “As thou wast born, Pulastya's son, That worlds might weep by thee undone, Thou like the dead henceforth shalt be: Such is the curse I lay on thee.” Senseless he lay, nor spoke nor stirred; Such was the power of Brahmá's word. But RávaG, troubled for his sake, Thus to the Self-existent spake: “Who lops the tree his care has reared When golden fruit has first appeared? Not thus, O Brahmá, deal with one Descended from thine own dear son.971 Still thou, O Lord, thy word must keep, He may not die, but let him sleep. Yet fix a time for him to break 971 Pulastya was the son of Brahmá and father of Vi[ravas or Paulastya the father of RávaG and KumbhakarGa.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1686)
- **Original**: 1668 The Ramayana The chains of slumber and awake.” He ceased: and Brahmá made reply; “Six months in slumber shall he lie And then arising for a day Shall cast the numbing bonds away.” Now Ráva G in his doubt and dread Has roused the monster from his bed, Who comes in this the hour of need On slaughtered Vánars flesh to feed. Each Vánar, when his awe-struck eyes Behold the monstrous chieftain, flies. With hopeful words their minds deceive, And let our trembling hosts believe They see no giant, but, displayed, A lifeless engine deftly made.” Then Ráma called to Níla:“Haste, Let troops near every gate be placed, And, armed with fragments of the rock And trees, each lane and alley block.”[473] Thus Ráma spoke: the chief obeyed, And swift the Vánars stood arrayed, As when the black clouds their battle form, The summit of a hill to storm. Canto LXII. Rávan's Request.
- **Translation**: 

---

### Verse 7 (Ramayan 0.1687)
- **Original**: Canto LXII. Rávan's Request. 1669 Along bright Lanká's royal road The giant, roused from slumber, strode, While from the houses on his head A rain of fragrant flowers was shed. He reached the monarch's gate whereon Rich gems and golden fretwork shone. Through court and corridor that shook Beneath his tread his way he took, And stood within the chamber where His brother sat in dark despair. But sudden, at the grateful sight The monarch's eye again grew bright. He started up, forgot his fear, And drew his giant brother near. The younger pressed the elder's feet And paid the King observance meet, Then cried:“O Monarch, speak thy will, And let my care thy word fulfil. What sudden terror and dismay Have burst the bonds in which I lay?” Fierce flashed the flame from RávaG's eye, As thus in wrath he made reply: “Fair time, I ween, for sleep is this, To lull thy soul in tranquil bliss, Unheeding, in oblivion drowned, The dangers that our lives surround. Brave Ráma, Da[aratha's son, A passage o'er the sea has won, And, with the Vánar monarch's aid, Round Lanká's walls his hosts arrayed. Though never in the deadly field My Rákshas troops were known to yield, The bravest of the giant train
- **Translation**: 

---

### Verse 8 (Ramayan 0.1688)
- **Original**: 1670 The Ramayana Have fallen by the Vánars slain. Hence comes my fear. O fierce and brave, Go forth, our threatened Lanká save. Go forth, a dreadful vengeance take: For this, O chief, I bade thee wake. The Gods and trembling fiends have felt The furious blows thine arm has dealt. Earth has no warrior, heaven has none To match thy might, Paulastya's son.” Canto LXIII. Kumbhakarna's Boast. Then KumbhakarGa laughed aloud And cried;“O Monarch, once so proud, We warned thee, but thou wouldst not hear; And now the fruits of sin appear. We warned thee, I, thy nobles, all Who loved thee, in thy council hall. Those sovereigns who with blinded eyes Neglect the foe their hearts despise, Soon, falling from their high estate Bring on themselves the stroke of fate. Accept at length, thy life to save, The counsel sage VibhishaG gave, The prudent counsel spurned before, And Sítá to her lord restore.”972 972 I omit a tedious sermon on the danger of rashness and the advantages of prudence, sufficient to irritate a less passionate hearer than RávaG.
- **Translation**: 

---

### Verse 9 (Ramayan 0.1689)
- **Original**: Canto LXIII. Kumbhakarna's Boast. 1671 The monarch frowned, by passion moved And thus in angry words reproved: “Wilt thou thine elder brother school, Forgetful of the ancient rule That bids thee treat him as the sage Who guides thee with the lore of age? Think on the dangers of the day, Nor idly throw thy words away: If, led astray, by passion stirred, I in the pride of power have erred; If deeds of old were done amiss, No time for vain reproach is this. Up, brother; let thy loving care The errors of thy king repair.” To calm his wrath, his soul to ease, The younger spake in words like these: “Yea, from our bosoms let us cast All idle sorrow for the past. Let grief and anger be repressed: Again be firm and self-possessed. This day, O Monarch, shalt thou see The Vánar legions turn and flee, And Ráma and his brother slain With their hearts' blood shall dye the plain. Yea, if the God who rules the dead, And VaruG their battalions led; If Indra with the Storm-Gods came Against me, and the Lord of Flame, Still would I fight with all and slay Thy banded foes, my King, to-day. If Raghu's son this day withstand The blow of mine uplifted hand, Deep in his breast my darts shall sink,
- **Translation**: 

---

### Verse 10 (Ramayan 0.1690)
- **Original**: 1672 The Ramayana And torrents of his life-blood drink. O fear not, in my promise trust: This arm shall lay him in the dust, Shall leave the fierce Sugríva dyed With gore, and LakshmaG by his side, And strike the great Hanúmán down, The spoiler of our glorious town.”973 [474] Canto LXIV. Mahodar's Speech. He ceased: and when his lips were closed Mahodar thus his rede opposed: “Why wilt thou shame thy noble birth And speak like one of little worth? Why boast thee thus in youthful pride Rejecting wisdom for thy guide? How will thy single arm oppose The victor of a thousand foes, Who proved in Janasthán his might And slew the rovers of the night? The remnant of those legions, they Who saw his power that fatal day, Now in this leaguered city dread The mighty chief from whom they fled. And wouldst thou meet the lord of men, Beard the great lion in his den, 973 The Bengal recension assigns a very different speech to KumbhakarGa and makes him say that Nárad the messenger of the Gods had formerly told him that VishGu himself incarnate as Da[aratha's son should come to destroy RávaG.
- **Translation**: 

---

### Verse 11 (Ramayan 0.1691)
- **Original**: Canto LXIV. Mahodar's Speech. 1673 And, when thine eyes are open, break The slumber of a deadly snake? Who may an equal battle wage With him, so awful in his rage, Fierce as the God of Death whom none May vanquish, Da[aratha's son? But, RávaG, shall the lady still Refuse compliance with thy will? No, listen, King, to this design Which soon shall make the captive thine. This day through Lanká's streets proclaim That four of us974 of highest fame With KumbhakarGa at our head Will strike the son of Raghu dead. Forth to the battle will we go And prove our prowess on the foe. Then, if our bold attempt succeed, No further plans thy hopes will need. But if in vain our warriors strive, And Raghu's son be left alive, We will return, and, wounded sore, Our armour stained with gouts of gore, Will show the shafts that rent each frame, Keen arrows marked with Ráma's name, And say we giants have devoured The princes whom our might o'erpowered. Then let the joyful tidings spread That Raghu's royal sons are dead. To all around thy pleasure show, Gold, pearls, and precious robes, bestow. Gay garlands round the portals twine, Enjoy the banquet and the wine. 974 Mahodar, Dwijihva, Sanhráda, and Vitardan.
- **Translation**: 

---

### Verse 12 (Ramayan 0.1692)
- **Original**: 1674 The Ramayana Then go, the scornful lady seek, And woo her when her heart is weak. Rich robes and gold and gems display, And gently wile her grief away. Then will she feel her hopeless state, Widowed, forlorn, and desolate; Know that on thee her bliss depends, Far from her country and her friends; Then, her proud spirit overthrown, The lady will be all thine own.” Canto LXV. Kumbhakarna's Speech. But haughty KumbhakarGa spurned His counsel, and to RávaG turned: “Thy life from peril will I free And slay the foe who threatens thee. A hero never vaunts in vain, Like bellowing clouds devoid of rain, Nor, Monarch, be thine ear inclined To counsellors of slavish kind, Who with mean arts their king mislead And mar each gallant plan and deed. O, let not words like his beguile The glorious king of Lanká's isle.”
- **Translation**: 

---

### Verse 13 (Ramayan 0.1693)
- **Original**: Canto LXV. Kumbhakarna's Speech. 1675 Thus scornful KumbhakarGa cried, And RávaG with a laugh replied: “Mahodar fears and fain would shun The battle with Ikshváku's son. Of all my giant warriors, who Is strong as thou, and brave and true? Ride, conqueror, to the battle ride, And tame the foeman's senseless pride. Go forth like Yáma to the field, And let thine arm thy trident wield. Scared by the lightning of thine eye The Vánar hosts will turn and fly; And Ráma, when he sees thee near, With trembling heart will own his fear.” The champion heard, and, well content, Forth from the hall his footsteps bent. He grasped his spear, the foeman's dread, Black iron all, both shaft and head, Which, dyed in many a battle, bore Great spots of slaughtered victims' gore. The king upon his neck had thrown The jewelled chain which graced his own. And garlands of delicious scent About his limbs for ornament. Around his arms gay bracelets clung, And pendants in his ears were hung. Adorned with gold, about his waist His coat of mail was firmly braced, And like NáráyaG975 or the God Who rules the sky he proudly trod. Behind him went a mighty throng Of giant warriors tall and strong, [475] 975 A name of VishGu.
- **Translation**: 

---

### Verse 14 (Ramayan 0.1694)
- **Original**: 1676 The Ramayana On elephants of noblest breeds. With cars, with camels, and with steeds: And, armed with spear and axe and sword Were fain to battle for their lord.976 Canto LXVI. Kumbhakarna's Sally. In pomp and pride of warlike state The giant passed the city gate. He raised his voice: the hills, the shore Of Lanká's sea returned the roar. The Vánars saw the chief draw nigh Whom not the ruler of the sky, Nor Yáma, monarch of the dead, Might vanquish, and affrighted fled. When royal Angad, Báli's son, Saw the scared Vánars turn and run, Undaunted still he kept his ground, And shouted as he gazed around: “O Nala, Níla, stay nor let Your souls your generous worth forget, O Kumud and Gaváksha, why Like base-born Vánars will ye fly? Turn, turn, nor shame your order thus: This giant is no match for us” 976 There is so much commonplace repetition in these Sallies of the Rákshas chieftains that omissions are frequently necessary. The usual ill omens attend the sally of KumbhakarGa, and the Canto ends with a description of the terrified Vánars' flight which is briefly repeated in different words at the beginning of the next Canto.
- **Translation**: 

---

### Verse 15 (Ramayan 0.1695)
- **Original**: Canto LXVI. Kumbhakarna's Sally. 1677 They heard his voice: the flight was stayed; Again for war they stood arrayed, And hurled upon the foe a shower Of mountain peaks and trees in flower. Still on his limbs their missiles rained: Unmoved, their blows he still sustained, And seemed unconscious of the stroke When rocks against his body broke. Fierce as the flame when woods are dry He charged with fury in his eye. Like trees consumed with fervent heat They fell beneath the giant's feet. Some o'er the ground, dyed red with gore, Fled wild with terror to the shore, And, deeming that all hope was lost, Ran to the bridge they erst had crossed. Some clomb the trees their lives to save, Some sought the mountain and the cave; Some hid them in the bosky dell, And there in deathlike slumber fell. When Angad saw the chieftains fly He called them with a mighty cry: “Once more, O Vánars, charge once more, On to the battle as before. In all her compass earth has not, To hide you safe, one secret spot. What! leave your arms? each nobler dame Will scorn her consort for the shame. This blot upon your names efface, And keep your valour from disgrace. Stay, chieftains; wherefore will ye run, A band of warriors scared by one?”
- **Translation**: 

---

### Verse 16 (Ramayan 0.1696)
- **Original**: 1678 The Ramayana Scarce would they hear: they would not stay, And basely spoke in wild dismay: “Have we not fought, and fought in vain Have we not seen our mightiest slain? The giant's matchless force we fear, And fly because our lives are dear.” But Báli's son with gentle art Dispelled their dread and cheered each heart. They turned and formed and waited still Obedient to the prince's will. Canto LXVII. Kumbhakarna's Death. Thus from their flight the Vánars turned, And every heart for battle burned, Determined on the spot to die Or gain a warrior's meed on high. Again the Vánars stooped to seize Their weapons, rocks and fallen trees; Again the deadly fight began, And fiercely at the giant ran. Unmoved the monster kept his place: He raised on high his awful mace, Whirled the huge weapon round his head And laid the foremost Vánars dead. Eight thousand fell bedewed with gore, Then sank and died seven hundred more. Then thirty, twenty, ten, or eight At each fierce onset met their fate, And fast the fallen were devoured Like snakes by Garu 's beak o'erpowered.
- **Translation**: 

---

### Verse 17 (Ramayan 0.1697)
- **Original**: Canto LXVII. Kumbhakarna's Death. 1679 Then Dwivid from the Vánar van, Armed with an uptorn mountain, ran, Like a huge cloud when fierce winds blow, And charged amain the mountain foe. With wondrous force the hill he threw: O'er KumbhakarGa's head it flew, And falling on his host afar Crushed many a giant, steed, and car. Rocks, trees, by fierce Hanúmán sped, Rained fast on KumbhakarGa's head. Whose spear each deadlier missile stopped, And harmless on the plain it dropped. [476] Then with his furious eyes aglow The giant rushed upon the foe, Where, with a woody hill upheaved, Hanúmán's might his charge received. Through his vast frame the giant felt The angry blow Hanúmán dealt. He reeled a moment, sore distressed, Then smote the Vánar on the breast, As when the War-God's furious stroke Through Krauncha's hill a passage broke.977 Fierce was the blow, and deep and wide The rent: with crimson torrents dyed, Hanúmán, maddened by the pain, Roared like a cloud that brings the rain, And from each Rákshas throat rang out Loud clamour and exultant shout. Then Níla hurled with mustered might The fragment of a mountain height; 977 Kártikeya the God of War, and the hero and incarnation Para[uráma are said to have cut a passage through the mountain Krauncha, a part of the Himálayan range, in the same way as the immense gorge that splits the Pyrenees under the towers of Marboré was cloven at one blow of Roland's sword Durandal.
- **Translation**: 

---

### Verse 18 (Ramayan 0.1698)
- **Original**: 1680 The Ramayana Nor would the rock the foe have missed, But KumbhakarGa raised his fist And smote so fiercely that the mass Fell crushed to powder on the grass. Five chieftains of the Vánar race978 Charged KumbhakarGa face to face, And his huge frame they wildly beat With rocks and trees and hands and feet. Round Rishabh first the giant wound His arms and hurled him to the ground, Where speechless, senseless, wounded sore, He lay his face besmeared with gore. Then Níla with his fist he slew, And Zarabh with his knee o'erthrew, Nor could Gaváksha's strength withstand The force of his terrific hand. At Gandhamádan's eager call Rushed thousands to avenge their fall, Nor ceased those Vánars to assail With knee and fist and tooth and nail. Around his foes the giant threw His mighty arms, and nearer drew The captives subject to his will: Then snatched them up and ate his fill. There was no respite then, no pause: Fast gaped and closed his hell-like jaws: Yet, prisoned in that gloomy cave, Some Vánars still their lives could save: Some through his nostrils found a way, Some through his ears resought the day. Like Indra with his thunder, like The God of Death in act to strike, 978 Rishabh,Zarabh, Níla, Gaváksha, and Gandhamádan.
- **Translation**: 

---

### Verse 19 (Ramayan 0.1699)
- **Original**: Canto LXVII. Kumbhakarna's Death. 1681 The giant seized his ponderous spear, And charged the foe in swift career. Before his might the Vánars fell, Nor could their hosts his charge repel. Then trembling, nor ashamed to run, They turned and fled to Raghu's son. When Báli's warrior son979 beheld Their flight, his heart with fury swelled. He rushed, with his terrific shout, To meet the foe and stay the rout. He came, he hurled a mountain peak, And smote the giant on the cheek. His ponderous spear the giant threw: Fierce was the cast, the aim was true; But Angad, trained in war and tried, Saw ere it came, and leapt aside. Then with his open hand he smote The giant on the chest and throat. That blow the giant scarce sustained; But sense and strength were soon regained. With force which nothing might resist He caught the Vánar by the wrist, Whirled him, as if in pastime, round, And dashed him senseless on the ground. There low on earth his foe lay crushed: At King Sugríva next he rushed, Who, waiting for the charge, stood still, And heaved on high a shattered hill, He looked on KumbhakarGa dyed With streams of blood, and fiercely cried: “Great glory has thine arm achieved, 979 Angad. The text calls him the son of the son of him who holds the thunderbolt,i.e.the grandson of Indra.
- **Translation**: 

---

### Verse 20 (Ramayan 0.1700)
- **Original**: 1682 The Ramayana And thousands of their lives bereaved. Now leave a while thy meaner foes, And brook the hill Sugríva throws.” He spoke, and hurled the mass he held: The giant's chest the stroke repelled, Then on the Vánars fell despair, And Rákshas clamour filled the air. The giant raised his arm, and fast Came the tremendous980 spear he cast. Hanúmán caught it as it flew, And knapped it on his knee in two. The giant saw the broken spear: His clouded eye confessed his fear; Yet at Sugríva's head he sent A peak from Lanká's mountain rent.[477] The rushing mass no might could stay: Sugríva fell and senseless lay. The giant stooped his foe to seize, And bore him thence, as bears the breeze A cloud in autumn through the sky. He heard the sad Immortals sigh, And shouts of triumph long and loud Went up from all the Rákshas crowd. Through Lanká's gate the giant passed Holding his struggling captive fast, While from each terrace, house, and tower Fell on his haughty head a shower Of fragrant scent and flowery rain, Blossoms and leaves and scattered grain.981 980 Literally, weighing a thousandbháras. The bhára is a weight equal to 2000 palas, thepalais equal to fourkar[as, and thekar[a to 11375 French grammes or about 176 grains troy. The spear seems very light for a warrior of Kumbhakar Ga's strength and stature and the work performed with it. 981 The custom of throwing parched or roasted grain, with wreaths and flowers,
- **Translation**: 

---

