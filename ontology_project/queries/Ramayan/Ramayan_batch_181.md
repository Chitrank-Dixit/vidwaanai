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

### Verse 1 (Ramayana 0.1646)
- **Original**: 1628 The Ramayana Sugríva trembled as he viewed Each fallen prince with blood bedewed, And in his eyes which overflowed With tears the flame of anger glowed. “Calm,” cried VibhishaG,“calm thy fears, And stay the torrent of thy tears. Still must the chance of battle change, And victory still delight to range. Our cause again will she befriend And bring us triumph in the end. This is not death: each prince will break The spell that holds him, and awake; Nor long shall numbing magic bind The mighty arm, the lofty mind.” He ceased: his finger bathed in dew Across Sugríva's eyes he drew; From dulling mist his vision freed, And spoke these words to suit the need: “No time is this for fear: away With fainting heart and weak delay. Now, e'en the tear which sorrow wrings From loving eyes destruction brings. Up, on to battle at the head Of those brave troops which Ráma led. Or guardian by his side remain Till sense and strength the prince regain. Soon shall the trance-bound pair revive, And from our hearts all sorrow drive. Though prostrate on the earth he lie,[462] Deem not that Ráma's death is nigh; Deem not that Lakshmí will forget Or leave her darling champion yet. Rest here and be thy heart consoled;
- **Translation**: 

---

### Verse 2 (Ramayana 0.1647)
- **Original**: Canto XLVII. Sítá. 1629 Ponder my words, be firm and bold. I, foremost in the battlefield, Will rally all who faint or yield. Their staring eyes betray their fear; They whisper each in other's ear. They, when they hear my cheering cry And see the friend of Ráma nigh, Will cast their gloom and fears away Like faded wreaths of yesterday.” Thus calmed he King Sugríva's dread; Then gave new heart to those who fled. Fierce Indrajít, his soul on fire With pride of conquest, sought his sire, Raised reverent hands, and told him all, The battle and the princes' fall. Rejoicing at his foes' defeat Upsprang the monarch from his seat, Girt by his giant courtiers: round His warrior son his arms he wound, Close kisses on his head applied, And heard again how Ráma died. Canto XLVII. Sítá.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1648)
- **Original**: 1630 The Ramayana Still on the ground where Ráma slept Their faithful watch the Vánars kept. There Angad stood o'erwhelmed with grief And many a lord and warrior chief; And, ranged in densest mass around, Their tree-armed legions held the ground. Far ranged each Vánar's eager eye, Now swept the land, now sought the sky, All fearing, if a leaf was stirred, A Rákshas in the sound they heard. The lord of Lanká in his hall, Rejoicing at his foeman's fall, Commanded and the warders came Who ever watched the Maithil dame. “Go,” cried the Rákshas king,“relate To Janak's child her husband's fate. Low on the earth her Ráma lies, And dark in death are LakshmaG's eyes. Bring forth my car and let her ride To view the chieftains side by side. The lord to whom her fancy turned For whose dear sake my love she spurned, Lies smitten, as he fiercely led The battle, with his brother dead. Lead forth the royal lady: go Her husband's lifeless body show. Then from all doubt and terror free Her softening heart will turn to me.” They heard his speech: the car was brought; That shady grove the warders sought Where, mourning Ráma night and day, The melancholy lady lay. They placed her in the car and through
- **Translation**: 

---

### Verse 4 (Ramayana 0.1649)
- **Original**: Canto XLVIII. Sítá's Lament. 1631 The yielding air they swiftly flew. The lady looked upon the plain, Looked on the heaps of Vánar slain, Saw where, triumphant in the fight, Thronged the fierce rovers of the night, And Vánar chieftains, mournful-eyed, Watched by the fallen brothers' side. There stretched upon his gory bed Each brother lay as lie the dead, With shattered mail and splintered bow Pierced by the arrows of the foe. When on the pair her eyes she bent, Burst from her lips a wild lament Her eyes o'erflowed, she groaned and sighed And thus in trembling accents cried: Canto XLVIII. Sítá's Lament. “False are they all, proved false to-day, The prophets of my fortune, they Who in the tranquil time of old A blessed life for me foretold, Predicting I should never know A childless dame's, a widow's woe, False are they all, their words are vain, For thou, my lord and life, art slain. False was the priest and vain his lore Who blessed me in those days of yore By Ráma's side in bliss to reign: For thou, my lord and life, art slain. They hailed me happy from my birth,
- **Translation**: 

---

### Verse 5 (Ramayana 0.1650)
- **Original**: 1632 The Ramayana Proud empress of the lord of earth. They blessed me— but the thought is pain— For thou, my lord and life, art slain. Ah, fruitless hope! each glorious sign That stamps the future queen is mine, With no ill-omened mark to show A widow's crushing hour of woe. They say my hair is black and fine, They praise my brows' continuous line; My even teeth divided well, My bosom for its graceful swell. They praise my feet and fingers oft; They say my skin is smooth and soft, And call me happy to possess The twelve fair marks that bring success.955 But ah, what profit shall I gain? Thou, O my lord and life, art slain. The flattering seer in former days My gentle girlish smile would praise,[463] And swear that holy water shed By Bráhman hands upon my head Should make me queen, a monarch's bride: How is the promise verified? Matchless in might the brothers slew In Janasthán the giant crew. And forced the indomitable sea To let them pass to rescue me. Theirs was the fiery weapon hurled By him who rules the watery world;956 Theirs the dire shaft by Indra sped; Theirs was the mystic Brahmá's Head.957 955 On each foot, and at the root of each finger. 956 VaruG. 957 The name of one of the mystical weapons the command over which was
- **Translation**: 

---

### Verse 6 (Ramayana 0.1651)
- **Original**: Canto XLVIII. Sítá's Lament. 1633 In vain they fought, the bold and brave: A coward's hand their death-wounds gave. By secret shafts and magic spell The brothers, peers of Indra, fell. That foe, if seen by Ráma's eye One moment, had not lived to fly. Though swift as thought, his utmost speed Had failed him in the hour of need. No might, no tear, no prayer may stay Fate's dark inevitable day. Nor could their matchless valour shield These heroes on the battle field. I sorrow for the noble dead, I mourn my hopes for ever fled; But chief my weeping eyes o'erflow For Queen Kau[alyá's hopeless woe. The widowed queen is counting now Each hour prescribed by Ráma's vow, And lives because she longs to see Once more her princely sons and me.” Then Trijamá,958 of gentler mould Though Rákshas born, her grief consoled: “Dear Queen, thy causeless woe dispel: Thy husband lives, and all is well. Look round: in every Vánar face The light of joyful hope I trace. Not thus, believe me, shine the eyes Of warriors when their leader dies. An Army, when the chief is dead, Flies from the field dispirited. Here, undisturbed in firm array, given by Vi[vámitra to Ráma, as related in Book I. 958 One of Sítá's guard, and her comforter on a former occasion also.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1652)
- **Original**: 1634 The Ramayana The Vánars by the brothers stay. Love prompts my speech; no longer grieve; Ponder my counsel, and believe. These lips of mine from earliest youth Have spoken, and shall speak, the truth. Deep in my heart thy gentle grace And patient virtues hold their place. Turn, lady, turn once more thine eye: Though pierced with shafts the heroes lie, On brows and cheeks with blood-drops wet The light of beauty lingers yet. Such beauty ne'er is found in death, But vanishes with parting breath. O, trust the hope these tokens give: The heroes are not dead, but live.” Then Sítá joined her hands, and sighed, “O, may thy words be verified!” The car was turned, which fleet as thought The mourning queen to Lanká brought. They led her to the garden, where Again she yielded to despair, Lamenting for the chiefs who bled On earth's cold bosom with the dead. Canto XLIX. Ráma's Lament.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1653)
- **Original**: Canto XLIX. Ráma's Lament. 1635 Ranged round the spot where Ráma fell Each Vánar chief stood sentinel. At length the mighty hero broke The trance that held him, and awoke. He saw his senseless brother, dyed With blood from head to foot, and cried: “What have I now to do with life Or rescue of my prisoned wife, When thus before my weeping eyes, Slain in the fight, my brother lies? A queen like Sítá I may find Among the best of womankind, But never such a brother, tried In war, my guardian, friend, and guide. If he be dead, the brave and true, I will not live but perish too. How, reft of LakshmaG, shall I meet My mother, and Kaikeyí greet? My brother's eager question brook, And fond Sumitrá's longing look? What shall I say, o'erwhelmed with shame To cheer the miserable dame? How, when she hears her son is dead, Will her sad heart be comforted? Ah me, for longer life unfit This mortal body will I quit; For LakshmaG slaughtered for my sake, From sleep of death will never wake. Ah when I sank oppressed with care, Thy gentle voice could soothe despair. And art thou, O my brother, killed? Is that dear voice for ever stilled? Cold are those lips, my brother, whence Came never word to breed offence?
- **Translation**: 

---

### Verse 9 (Ramayana 0.1654)
- **Original**: 1636 The Ramayana Ah stretched upon the gory plain My brother lies untimely slain: Numbed is the mighty arm that slew The leaders of the giant crew. Transfixed with shafts, with blood-streams red, Thou liest on thy lowly bed:[464] So sinks to rest, his journey done, Mid arrowy rays the crimson sun. Thou, when from home and sire I fled, The wood's wild ways with me wouldst tread: Now close to thine my steps shall be, For I in death will follow thee. VibhishaG now will curse my name, And Ráma as a braggart blame, Who promised— but his word is vain— That he in Lanká's isle should reign. Return, Sugríva: reft of me Lead back thy Vánars o'er the sea, Nor hope to battle face to face With him who rules the giant race. Well have ye done and nobly fought, And death in desperate combat sought. All that heroic might can do, Brave Vánars, has been done by you. My faithful friends I now dismiss: Return: my last farewell is this.” Bedewed with tears was every cheek As thus the Vánars heard him speak. VibhishaG on the field had stayed The Vánar hosts who fled dismayed. Now lifting up his mace on high With martial step the chief drew nigh. The hosts who watched by Ráma's side
- **Translation**: 

---

### Verse 10 (Ramayana 0.1655)
- **Original**: Canto L. The Broken Spell. 1637 Beheld his shape and giant stride. 'Tis he, 'tis RávaG's son, they thought: And all in flight their safety sought. Canto L. The Broken Spell. Sugríva viewed the flying crowd, And thus to Angad cried aloud: “Why run the trembling hosts, as flee Storm-scattered barks across the sea?” “Dost thou not mark,” the chief replied, “Transfixed with shafts, with bloodstreams dyed, With arrowy toils about them wound, The sons of Raghu on the ground?” That moment brought VibhishaG near. Sugríva knew the cause of fear, And ordered Jámbaván, who led The bears, to check the hosts that fled. The king of bears his hest obeyed: The Vánars' headlong flight was stayed. A little while VibhishaG eyed The brothers fallen side by side. His giant fingers wet with dew Across the heroes' eyes he drew, Still on the pair his sad look bent, And spoke these word in wild lament: “Ah for the mighty chiefs brought low By coward hand and stealthy blow! Brave pair who loved the open fight, Slain by that rover of the night.
- **Translation**: 

---

### Verse 11 (Ramayana 0.1656)
- **Original**: 1638 The Ramayana Dishonest is the victory won By Indrajít my brother's son. I on their might for aid relied, And in my cause they fought and died. Lost is the hope that soothed each pain: I live, but live no more to reign, While Lanká's lord, untouched by ill, Exults in safe defiance still.” “Not thus,” Sugríva said,“repine, For Lanká's isle shall still be thine. Nor let the tyrant and his son Exult before the fight be done. These royal chiefs, though now dismayed, Freed from the spell by Garu 's aid, Triumphant yet the foe shall meet And lay the robber at their feet.” His hope the Vánar monarch told, And thus VibhishaG's grief consoled. Then to SusheG who at his side Expectant stood, Sugríva cried: “When these regain their strength and sense, Fly, bear them to Kishkindhá hence. Here with my legions will I stay, The tyrant and his kinsmen slay, And, rescued from the giant king, The Maithil lady will I bring, Like Glory lost of old, restored By Zakra, heaven's almighty lord.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.1657)
- **Original**: Canto L. The Broken Spell. 1639 SusheG made answer:“Hear me yet: When Gods and fiends in battle met, So fiercely fought the demon crew, So wild a storm of arrows flew, That heavenly warriors faint with pain, Sank smitten by the ceaseless rain. V [ihaspati,959 with herb and spell, Cured the sore wounds of those who fell. And, skilled in arts that heal and save, New life and sense and vigour gave. Far, on the Milky Ocean's shore, Still grow those herbs in boundless store; Let swiftest Vánars thither speed And bring them for our utmost need. Those herbs that on the mountain spring Let Panas and Sampáti bring, For well the wondrous leaves they know, That heal each wound and life bestow. Beside that sea which, churned of yore, The amrit on its surface bore, Where the white billows lash the land, Chandra's fair height and DroGa stand. Planted by Gods each glittering steep Looks down upon the milky deep. Let fleet Hanúmán bring us thence Those herbs of wondrous influence.” Meanwhile the rushing wind grew loud, Red lightnings flashed from banks of cloud. The mountains shook, the wild waves rose, And smitten with resistless blows [465] 959 The preceptor of the Gods.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1658)
- **Original**: 1640 The Ramayana Unrooted fell each stately tree That fringed the margin of the sea. All life within the waters feared Then, as the Vánars gazed, appeared King Garu 's self, a wondrous sight, Disclosed in flames of fiery light. From his fierce eye in sudden dread All serpents in a moment fled. And those transformed to shaft that bound The princes vanished in the ground. On Raghu's sons his eyes he bent, And hailed the lords armipotent. Then o'er them stooped the feathered king, And touched their faces with his wing. His healing touch their pangs allayed, And closed each rent the shafts had made. Again their eyes were bright and bold, Again the smooth skin shone like gold. Again within their shell enshrined Came memory and each power of mind: And, from those numbing bonds released, Their spirit, zeal, and strength increased. Firm on their feet they stood, and then Thus Ráma spake, the lord of men: “By thy dear grace in sorest need From deadly bonds we both are freed. To these glad eyes as welcome now As Aja960 or my sire art thou. Who art thou, mighty being? say, Thus glorious in thy bright array.” He ceased: the king of birds replied, While flashed his eye with joy and pride: 960 Ráma's grandfather.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1659)
- **Original**: Canto LI. Dhúmráksha's Sally. 1641 “In me, O Raghu's son, behold One who has loved thee from of old: Garu , the lord of all that fly, Thy guardian and thy friend am I. Not all the Gods in heaven could loose These numbing bonds, this serpent noose, Wherewith fierce RávaG's son, renowned For magic arts, your limbs had bound. Those arrows fixed in every limb Were mighty snakes, transformed by him. Blood thirsty race, they live beneath The earth, and slay with venomed teeth. On, smite the lord of Lanká's isle, But guard you from the giants' guile Who each dishonest art employ And by deceit brave foes destroy. So shall the tyrant RávaG bleed, And Sítá from his power be freed.” Thus Garu spake: then, swift as thought, The region of the sky he sought, Where in the distance like a blaze Of fire he vanished from the gaze. Then the glad Vánars' joy rang out In many a wild tumultuous shout, And the loud roar of drum and shell Startled each distant sentinel. Canto LI. Dhúmráksha's Sally.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1660)
- **Original**: 1642 The Ramayana King RávaG, where he sat within, Heard from his hall the deafening din, And with a spirit ill at ease Addressed his lords in words like these: “That warlike shout, those joyous cries, Loud as the thunder of the skies, Upsent from every Vánar throat, Some new-born confidence denote. Hark, how the sea and trembling shore Re-echo with the Vánars' roar. Though arrowy chains, securely twined Both Ráma and his brother bind, Still must the fierce triumphant shout Disturb my soul with rising doubt. Swift envoys to the army send, And learn what change these cries portend.” Obedient, at their master's call, Fleet giants clomb the circling wall. They saw the Vánars formed and led: They saw Sugríva at their head, The brothers from their bonds released: And hope grew faint and fear increased. Their faces pale with doubt and dread, Back to the giant king they sped, And to his startled ear revealed The tidings of the battle field. The flush of rage a while gave place To chilling fear that changed his face:
- **Translation**: 

---

### Verse 16 (Ramayana 0.1661)
- **Original**: Canto LII. Dhúmráksha's Death. 1643 “What?” cried the tyrant,“are my foes Freed from the binding snakes that close With venomed clasp round head and limb, Bright as the sun and fierce like him: The spell a God bestowed of yore, The spell that never failed before? If arts like these be useless, how Shall giant strength avail us now? Go forth, Dhúmráksha, good at need, The bravest of my warriors lead: Force through the foe thy conquering way, And Ráma and the Vánars slay.” Before his king with reverence due Dhúmráksha bowed him, and withdrew. Around him at his summons came Fierce legions led by chiefs of fame. Well armed with sword and spear and mace, They hurried to the gathering place, And rushed to battle, borne at speed By elephant and car and steed. Canto LII. Dhúmráksha's Death. The Vánars saw the giant foe Pour from the gate in gallant show, [466]
- **Translation**: 

---

### Verse 17 (Ramayana 0.1662)
- **Original**: 1644 The Ramayana Rejoiced with warriors' fierce delight And shouted, longing for the fight. Near came the hosts and nearer yet: Dire was the tumult as they met, As, serried line to line opposed, The Vánars and the giants closed. Fierce on the foe the Vánars rushed, And, wielding trees, the foremost crushed; But, feathered from the heron's wing, With eager flight from sounding string, Against them shot with surest aim A ceaseless storm of arrows came: And, pierced in head and chest and side, Full many a Vánar fell and died. They perished slain in fierce attacks With sword and pike and battle-axe; But myriads following undismayed Their valour in the fight displayed. Unnumbered Vánars rent and torn With shaft and spear to earth were borne. But crushed by branchy trees and blocks Of jagged stone and shivered rocks Which the wild Vánars wielded well The bravest of the giants fell. Their trampled banners strewed the fields, And broken swords and spears and shields; And, crushed by blows which none might stay, Cars, elephants, and riders lay. Dhúmráksha turned his furious eye And saw his routed legions fly. Still dauntless, with terrific blows, He struck and slew his foremost foes. At every blow, at every thrust, He laid a Vánar in the dust.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1663)
- **Original**: Canto LII. Dhúmráksha's Death. 1645 So fell they neath the sword and lance In battle's wild Gandharva961 dance, Where clang of bow and clash of sword Did duty for the silvery chord, And hoofs that rang and steeds that neighed Loud concert for the dancers made. So fiercely from Dhúmráksha's bow His arrows rained in ceaseless flow, The Vánar legions turned and fled To all the winds discomfited. Hanúmán saw the Vánars fly; He heaved a mighty rock on high. His keen eyes flashed with wrathful fire, And, rapid as the Wind his sire, Strong as the rushing tempests are, He hurled it at the advancing car. Swift through the air the missile sang: The giant from the chariot sprang, Ere crushed by that terrific blow Lay pole and wheel and flag and bow. Hanúmán's eyes with fury blazed: A mountain's rocky peak he raised, Poised it on high in act to throw, And rushed upon his giant foe. Dhúmráksha saw: he raised his mace And smote Hanúmán on the face, Who maddened by the wound's keen pang Again upon his foeman sprang; And on the giant's head the rock Descended with resistless shock. Crushed was each limb: a shapeless mass He lay upon the blood-stained grass. 961 The Gandharvas are warriors and Minstrels of Indra's heaven.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1664)
- **Original**: 1646 The Ramayana Canto LIII. Vajradanshtra's Sally. When Ráva G in his palace heard The mournful news, his wrath was stirred; And, gasping like a furious snake, To Vajradanshmra thus he spake: “Go forth, my fiercest captain, lead The bravest of the giants' breed. Go forth, the sons of Raghu slay And by their side Sugríva lay.” He ceased: the chieftain bowed his head And forth with gathered troops he sped. Cars, camels, steeds were well arrayed, And coloured banners o'er them played. Rings decked his arms: about his waist The life-protecting mail was braced, And on the chieftain's forehead set Glittered his cap and coronet. Borne on a bannered car that glowed With golden sheen the warrior rode, And footmen marched with spear and sword And bow and mace behind their lord. In pomp and pride of warlike state They sallied from the southern gate, But saw, as on their way they sped, Dread signs around and overhead. For there were meteors falling fast, Though not a cloud its shadow cast; And each ill-omened bird and beast, Forboding death, the fear increased, While many a giant slipped and reeled, Falling before he reached the field.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1665)
- **Original**: Canto LIV. Vajradanshtra's Death. 1647 They met in mortal strife engaged, And long and fierce the battle raged. Spears, swords uplifted, gleamed and flashed, And many a chief to earth was dashed. A ceaseless storm of arrows rained, And limbs were pierced and blood-distained. Terrific was the sound that filled The air, and every heart was chilled, As hurtling o'er the giants flew The rocks and trees which Vánars threw. Fierce as a hungry lion when Unwary deer approach his den, [467] Angad, his eyes with fury red, Waving a tree above his head, Rushed with wild charge which none could stay Where stood the giants' dense array. Like tall trees levelled by the blast Before him fell the giants fast, And earth that streamed with blood was strown With warriors, steeds, and cars o'erthrown. Canto LIV. Vajradanshtra's Death. The giant leader fiercely rained His arrows and the fight maintained. Each time the clanging cord he drew His certain shaft a Vánar slew. Then, as the creatures he has made Fly to the Lord of Life for aid, To Angad for protection fled The Vánar hosts dispirited.
- **Translation**: 

---

