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

### Verse 1 (Ramayan 0.1641)
- **Original**: Canto XLIV. The Night. 1623 Showed like a towering hill embraced By burning woods about his waist. The giants at the Vánars flew, And ravening ate the foes they slew: With mortal bite like serpent's fang, The Vánars at the giants sprang, And car and steeds and they who bore The pennons fell bedewed with gore. No serried band, no firm array The fury of their charge could stay. Down went the horse and rider, down Went giant lords of high renown. Though midnight's shade was dense and dark, With skill that swerved not from the mark Their bows the sons of Raghu drew, And each keen shaft a chieftain slew. Uprose the blinding dust from meads Ploughed by the cars and trampling steeds, And where the warriors fell the flood Was dark and terrible with blood. Six giants952 singled Ráma out, And charged him with a furious shout Loud as the roaring of the sea When every wind is raging free. Six times he shot: six heads were cleft; Six giants dead on earth were left. Nor ceased he yet: his bow he strained, And from the sounding weapon rained A storm of shafts whose fiery glare Filled all the region of the air; And chieftains dropped before his aim Like moths that perish in the flame. 952 Yajna[atru, Mahápár[va, Mahodar, Vajradanshmra,Zuka, and SáraG.
- **Translation**: 

---

### Verse 2 (Ramayan 0.1642)
- **Original**: 1624 The Ramayana Earth glistened where the arrows fell, As shines in autumn nights a dell Which fireflies, flashing through the gloom, With momentary light illume. But Indrajít, when Báli's son953 The victory o'er the foe had won, Saw with a fury-kindled eye His mangled steeds and driver die; Then, lost in air, he fled the fight, And vanished from the victor's sight. The Gods and saints glad voices raised, And Angad for his virtue praised; And Raghu's sons bestowed the meed Of honour due to valorous deed. Compelled his shattered car to quit, Rage filled the soul of Indrajít, Who brooked not, strong by Brahmá's grace Defeat from one of Vánar race. In magic mist concealed from view His bow the treacherous warrior drew, And Raghu's sons were first to feel The tempest of his winged steel. Then when his arrows failed to kill The princes who defied him still, He bound them with the serpent noose,954 The magic bond which none might loose. 953 Angad. 954 A mysterious weapon consisting of serpents transformed to arrows which deprived the wounded object of all sense and power of motion.
- **Translation**: 

---

### Verse 3 (Ramayan 0.1643)
- **Original**: Canto XLV. Indrajít's Victory. 1625 Canto XLV. Indrajít's Victory. Brave Ráma, burning still to know The station of his artful foe, [461] Gave to ten chieftains, mid the best Of all the host, his high behest. Swift rose in air the Vánar band: Each region of the sky they scanned: But RávaG's son by magic skill Checked them with arrows swifter still, When streams of blood from chest and side The dauntless Vánars' limbs had dyed, The giant in his misty shroud Showed like the sun obscured by cloud. Like serpents hissing through the air, His arrows smote the princely pair; And from their limbs at every rent A stream of rushing blood was sent. Like Kin[uk trees they stood, that show In spring their blossoms' crimson glow. Then Indrajít with fury eyed Ikshváku's royal sons, and cried: “Not mighty Indra can assail Or see me when I choose to veil My form in battle: and can ye, Children of earth, contend with me? The arrowy noose this hand has shot Has bound you with a hopeless knot; And, slaughtered by my shafts and bow, To Yáma's hall this hour ye go.”
- **Translation**: 

---

### Verse 4 (Ramayan 0.1644)
- **Original**: 1626 The Ramayana He spoke, and shouted. Then anew The arrows from his bowstring flew, And pierced, well aimed with perfect art, Each limb and joint and vital part. Transfixed with shafts in every limb, Their strength relaxed, their eyes grew dim. As two tall standards side by side, With each sustaining rope untied, Fall levelled by the howling blast, So earth's majestic lords at last Beneath the arrowy tempest reeled, And prostrate pressed the battle field. Canto XLVI. Indrajít's Triumph. The Vánar chiefs whose piercing eyes Scanned eagerly the earth and skies, Saw the brave brothers wounded sore Transfixed with darts and stained with gore. The monarch of the Vánar race, With wise VibhishaG, reached the place; Angad and Níla came behind, And others of the forest kind, And standing with Hanúmán there Lamented for the fallen pair. Their melancholy eyes they raised; In fruitless search a while they gazed. But magic arts VibhishaG knew; Not hidden from his keener view, Though veiled by magic from the rest, The son of RávaG stood confessed.
- **Translation**: 

---

### Verse 5 (Ramayan 0.1645)
- **Original**: Canto XLVI. Indrajít's Triumph. 1627 Fierce Indrajít with savage pride The fallen sons of Raghu eyed, And every giant heart was proud As thus the warrior cried aloud: “Slain by mine arrows Ráma lies, And closed in death are LakshmaG's eyes. Dead are the mighty princes who DúshaG and Khara smote and slew. The Gods and fiends may toil in vain To free them from the binding chain. The haughty chief, my father's dread, Who drove him sleepless from his bed, While Lanká, troubled like a brook In rain time, heard his name and shook: He whose fierce hate our lives pursued Lies helpless by my shafts subdued. Now fruitless is each wondrous deed Wrought by the race the forests breed, And fruitless every toil at last Like cloudlets when the rains are past.” Then rose the shout of giants loud As thunder from a bursting cloud, When, deeming Ráma, dead, they raised Their voices and the conqueror praised. Still motionless, as lie the slain, The brothers pressed the bloody plain, No sigh they drew, no breath they heaved, And lay as though of life bereaved. Proud of the deed his art had done, To Lanká's town went RávaG's son, Where, as he passed, all fear was stilled, And every heart with triumph filled.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1646)
- **Original**: 1628 The Ramayana Sugríva trembled as he viewed Each fallen prince with blood bedewed, And in his eyes which overflowed With tears the flame of anger glowed. “Calm,” cried VibhishaG,“calm thy fears, And stay the torrent of thy tears. Still must the chance of battle change, And victory still delight to range. Our cause again will she befriend And bring us triumph in the end. This is not death: each prince will break The spell that holds him, and awake; Nor long shall numbing magic bind The mighty arm, the lofty mind.” He ceased: his finger bathed in dew Across Sugríva's eyes he drew; From dulling mist his vision freed, And spoke these words to suit the need: “No time is this for fear: away With fainting heart and weak delay. Now, e'en the tear which sorrow wrings From loving eyes destruction brings. Up, on to battle at the head Of those brave troops which Ráma led. Or guardian by his side remain Till sense and strength the prince regain. Soon shall the trance-bound pair revive, And from our hearts all sorrow drive. Though prostrate on the earth he lie,[462] Deem not that Ráma's death is nigh; Deem not that Lakshmí will forget Or leave her darling champion yet. Rest here and be thy heart consoled;
- **Translation**: 

---

### Verse 7 (Ramayan 0.1647)
- **Original**: Canto XLVII. Sítá. 1629 Ponder my words, be firm and bold. I, foremost in the battlefield, Will rally all who faint or yield. Their staring eyes betray their fear; They whisper each in other's ear. They, when they hear my cheering cry And see the friend of Ráma nigh, Will cast their gloom and fears away Like faded wreaths of yesterday.” Thus calmed he King Sugríva's dread; Then gave new heart to those who fled. Fierce Indrajít, his soul on fire With pride of conquest, sought his sire, Raised reverent hands, and told him all, The battle and the princes' fall. Rejoicing at his foes' defeat Upsprang the monarch from his seat, Girt by his giant courtiers: round His warrior son his arms he wound, Close kisses on his head applied, And heard again how Ráma died. Canto XLVII. Sítá.
- **Translation**: 

---

### Verse 8 (Ramayan 0.1648)
- **Original**: 1630 The Ramayana Still on the ground where Ráma slept Their faithful watch the Vánars kept. There Angad stood o'erwhelmed with grief And many a lord and warrior chief; And, ranged in densest mass around, Their tree-armed legions held the ground. Far ranged each Vánar's eager eye, Now swept the land, now sought the sky, All fearing, if a leaf was stirred, A Rákshas in the sound they heard. The lord of Lanká in his hall, Rejoicing at his foeman's fall, Commanded and the warders came Who ever watched the Maithil dame. “Go,” cried the Rákshas king,“relate To Janak's child her husband's fate. Low on the earth her Ráma lies, And dark in death are LakshmaG's eyes. Bring forth my car and let her ride To view the chieftains side by side. The lord to whom her fancy turned For whose dear sake my love she spurned, Lies smitten, as he fiercely led The battle, with his brother dead. Lead forth the royal lady: go Her husband's lifeless body show. Then from all doubt and terror free Her softening heart will turn to me.” They heard his speech: the car was brought; That shady grove the warders sought Where, mourning Ráma night and day, The melancholy lady lay. They placed her in the car and through
- **Translation**: 

---

### Verse 9 (Ramayan 0.1649)
- **Original**: Canto XLVIII. Sítá's Lament. 1631 The yielding air they swiftly flew. The lady looked upon the plain, Looked on the heaps of Vánar slain, Saw where, triumphant in the fight, Thronged the fierce rovers of the night, And Vánar chieftains, mournful-eyed, Watched by the fallen brothers' side. There stretched upon his gory bed Each brother lay as lie the dead, With shattered mail and splintered bow Pierced by the arrows of the foe. When on the pair her eyes she bent, Burst from her lips a wild lament Her eyes o'erflowed, she groaned and sighed And thus in trembling accents cried: Canto XLVIII. Sítá's Lament. “False are they all, proved false to-day, The prophets of my fortune, they Who in the tranquil time of old A blessed life for me foretold, Predicting I should never know A childless dame's, a widow's woe, False are they all, their words are vain, For thou, my lord and life, art slain. False was the priest and vain his lore Who blessed me in those days of yore By Ráma's side in bliss to reign: For thou, my lord and life, art slain. They hailed me happy from my birth,
- **Translation**: 

---

### Verse 10 (Ramayan 0.1650)
- **Original**: 1632 The Ramayana Proud empress of the lord of earth. They blessed me— but the thought is pain— For thou, my lord and life, art slain. Ah, fruitless hope! each glorious sign That stamps the future queen is mine, With no ill-omened mark to show A widow's crushing hour of woe. They say my hair is black and fine, They praise my brows' continuous line; My even teeth divided well, My bosom for its graceful swell. They praise my feet and fingers oft; They say my skin is smooth and soft, And call me happy to possess The twelve fair marks that bring success.955 But ah, what profit shall I gain? Thou, O my lord and life, art slain. The flattering seer in former days My gentle girlish smile would praise,[463] And swear that holy water shed By Bráhman hands upon my head Should make me queen, a monarch's bride: How is the promise verified? Matchless in might the brothers slew In Janasthán the giant crew. And forced the indomitable sea To let them pass to rescue me. Theirs was the fiery weapon hurled By him who rules the watery world;956 Theirs the dire shaft by Indra sped; Theirs was the mystic Brahmá's Head.957 955 On each foot, and at the root of each finger. 956 VaruG. 957 The name of one of the mystical weapons the command over which was
- **Translation**: 

---

### Verse 11 (Ramayan 0.1651)
- **Original**: Canto XLVIII. Sítá's Lament. 1633 In vain they fought, the bold and brave: A coward's hand their death-wounds gave. By secret shafts and magic spell The brothers, peers of Indra, fell. That foe, if seen by Ráma's eye One moment, had not lived to fly. Though swift as thought, his utmost speed Had failed him in the hour of need. No might, no tear, no prayer may stay Fate's dark inevitable day. Nor could their matchless valour shield These heroes on the battle field. I sorrow for the noble dead, I mourn my hopes for ever fled; But chief my weeping eyes o'erflow For Queen Kau[alyá's hopeless woe. The widowed queen is counting now Each hour prescribed by Ráma's vow, And lives because she longs to see Once more her princely sons and me.” Then Trijamá,958 of gentler mould Though Rákshas born, her grief consoled: “Dear Queen, thy causeless woe dispel: Thy husband lives, and all is well. Look round: in every Vánar face The light of joyful hope I trace. Not thus, believe me, shine the eyes Of warriors when their leader dies. An Army, when the chief is dead, Flies from the field dispirited. Here, undisturbed in firm array, given by Vi[vámitra to Ráma, as related in Book I. 958 One of Sítá's guard, and her comforter on a former occasion also.
- **Translation**: 

---

### Verse 12 (Ramayan 0.1652)
- **Original**: 1634 The Ramayana The Vánars by the brothers stay. Love prompts my speech; no longer grieve; Ponder my counsel, and believe. These lips of mine from earliest youth Have spoken, and shall speak, the truth. Deep in my heart thy gentle grace And patient virtues hold their place. Turn, lady, turn once more thine eye: Though pierced with shafts the heroes lie, On brows and cheeks with blood-drops wet The light of beauty lingers yet. Such beauty ne'er is found in death, But vanishes with parting breath. O, trust the hope these tokens give: The heroes are not dead, but live.” Then Sítá joined her hands, and sighed, “O, may thy words be verified!” The car was turned, which fleet as thought The mourning queen to Lanká brought. They led her to the garden, where Again she yielded to despair, Lamenting for the chiefs who bled On earth's cold bosom with the dead. Canto XLIX. Ráma's Lament.
- **Translation**: 

---

### Verse 13 (Ramayan 0.1653)
- **Original**: Canto XLIX. Ráma's Lament. 1635 Ranged round the spot where Ráma fell Each Vánar chief stood sentinel. At length the mighty hero broke The trance that held him, and awoke. He saw his senseless brother, dyed With blood from head to foot, and cried: “What have I now to do with life Or rescue of my prisoned wife, When thus before my weeping eyes, Slain in the fight, my brother lies? A queen like Sítá I may find Among the best of womankind, But never such a brother, tried In war, my guardian, friend, and guide. If he be dead, the brave and true, I will not live but perish too. How, reft of LakshmaG, shall I meet My mother, and Kaikeyí greet? My brother's eager question brook, And fond Sumitrá's longing look? What shall I say, o'erwhelmed with shame To cheer the miserable dame? How, when she hears her son is dead, Will her sad heart be comforted? Ah me, for longer life unfit This mortal body will I quit; For LakshmaG slaughtered for my sake, From sleep of death will never wake. Ah when I sank oppressed with care, Thy gentle voice could soothe despair. And art thou, O my brother, killed? Is that dear voice for ever stilled? Cold are those lips, my brother, whence Came never word to breed offence?
- **Translation**: 

---

### Verse 14 (Ramayan 0.1654)
- **Original**: 1636 The Ramayana Ah stretched upon the gory plain My brother lies untimely slain: Numbed is the mighty arm that slew The leaders of the giant crew. Transfixed with shafts, with blood-streams red, Thou liest on thy lowly bed:[464] So sinks to rest, his journey done, Mid arrowy rays the crimson sun. Thou, when from home and sire I fled, The wood's wild ways with me wouldst tread: Now close to thine my steps shall be, For I in death will follow thee. VibhishaG now will curse my name, And Ráma as a braggart blame, Who promised— but his word is vain— That he in Lanká's isle should reign. Return, Sugríva: reft of me Lead back thy Vánars o'er the sea, Nor hope to battle face to face With him who rules the giant race. Well have ye done and nobly fought, And death in desperate combat sought. All that heroic might can do, Brave Vánars, has been done by you. My faithful friends I now dismiss: Return: my last farewell is this.” Bedewed with tears was every cheek As thus the Vánars heard him speak. VibhishaG on the field had stayed The Vánar hosts who fled dismayed. Now lifting up his mace on high With martial step the chief drew nigh. The hosts who watched by Ráma's side
- **Translation**: 

---

### Verse 15 (Ramayan 0.1655)
- **Original**: Canto L. The Broken Spell. 1637 Beheld his shape and giant stride. 'Tis he, 'tis RávaG's son, they thought: And all in flight their safety sought. Canto L. The Broken Spell. Sugríva viewed the flying crowd, And thus to Angad cried aloud: “Why run the trembling hosts, as flee Storm-scattered barks across the sea?” “Dost thou not mark,” the chief replied, “Transfixed with shafts, with bloodstreams dyed, With arrowy toils about them wound, The sons of Raghu on the ground?” That moment brought VibhishaG near. Sugríva knew the cause of fear, And ordered Jámbaván, who led The bears, to check the hosts that fled. The king of bears his hest obeyed: The Vánars' headlong flight was stayed. A little while VibhishaG eyed The brothers fallen side by side. His giant fingers wet with dew Across the heroes' eyes he drew, Still on the pair his sad look bent, And spoke these word in wild lament: “Ah for the mighty chiefs brought low By coward hand and stealthy blow! Brave pair who loved the open fight, Slain by that rover of the night.
- **Translation**: 

---

### Verse 16 (Ramayan 0.1656)
- **Original**: 1638 The Ramayana Dishonest is the victory won By Indrajít my brother's son. I on their might for aid relied, And in my cause they fought and died. Lost is the hope that soothed each pain: I live, but live no more to reign, While Lanká's lord, untouched by ill, Exults in safe defiance still.” “Not thus,” Sugríva said,“repine, For Lanká's isle shall still be thine. Nor let the tyrant and his son Exult before the fight be done. These royal chiefs, though now dismayed, Freed from the spell by Garu 's aid, Triumphant yet the foe shall meet And lay the robber at their feet.” His hope the Vánar monarch told, And thus VibhishaG's grief consoled. Then to SusheG who at his side Expectant stood, Sugríva cried: “When these regain their strength and sense, Fly, bear them to Kishkindhá hence. Here with my legions will I stay, The tyrant and his kinsmen slay, And, rescued from the giant king, The Maithil lady will I bring, Like Glory lost of old, restored By Zakra, heaven's almighty lord.”
- **Translation**: 

---

### Verse 17 (Ramayan 0.1657)
- **Original**: Canto L. The Broken Spell. 1639 SusheG made answer:“Hear me yet: When Gods and fiends in battle met, So fiercely fought the demon crew, So wild a storm of arrows flew, That heavenly warriors faint with pain, Sank smitten by the ceaseless rain. V [ihaspati,959 with herb and spell, Cured the sore wounds of those who fell. And, skilled in arts that heal and save, New life and sense and vigour gave. Far, on the Milky Ocean's shore, Still grow those herbs in boundless store; Let swiftest Vánars thither speed And bring them for our utmost need. Those herbs that on the mountain spring Let Panas and Sampáti bring, For well the wondrous leaves they know, That heal each wound and life bestow. Beside that sea which, churned of yore, The amrit on its surface bore, Where the white billows lash the land, Chandra's fair height and DroGa stand. Planted by Gods each glittering steep Looks down upon the milky deep. Let fleet Hanúmán bring us thence Those herbs of wondrous influence.” Meanwhile the rushing wind grew loud, Red lightnings flashed from banks of cloud. The mountains shook, the wild waves rose, And smitten with resistless blows [465] 959 The preceptor of the Gods.
- **Translation**: 

---

### Verse 18 (Ramayan 0.1658)
- **Original**: 1640 The Ramayana Unrooted fell each stately tree That fringed the margin of the sea. All life within the waters feared Then, as the Vánars gazed, appeared King Garu 's self, a wondrous sight, Disclosed in flames of fiery light. From his fierce eye in sudden dread All serpents in a moment fled. And those transformed to shaft that bound The princes vanished in the ground. On Raghu's sons his eyes he bent, And hailed the lords armipotent. Then o'er them stooped the feathered king, And touched their faces with his wing. His healing touch their pangs allayed, And closed each rent the shafts had made. Again their eyes were bright and bold, Again the smooth skin shone like gold. Again within their shell enshrined Came memory and each power of mind: And, from those numbing bonds released, Their spirit, zeal, and strength increased. Firm on their feet they stood, and then Thus Ráma spake, the lord of men: “By thy dear grace in sorest need From deadly bonds we both are freed. To these glad eyes as welcome now As Aja960 or my sire art thou. Who art thou, mighty being? say, Thus glorious in thy bright array.” He ceased: the king of birds replied, While flashed his eye with joy and pride: 960 Ráma's grandfather.
- **Translation**: 

---

### Verse 19 (Ramayan 0.1659)
- **Original**: Canto LI. Dhúmráksha's Sally. 1641 “In me, O Raghu's son, behold One who has loved thee from of old: Garu , the lord of all that fly, Thy guardian and thy friend am I. Not all the Gods in heaven could loose These numbing bonds, this serpent noose, Wherewith fierce RávaG's son, renowned For magic arts, your limbs had bound. Those arrows fixed in every limb Were mighty snakes, transformed by him. Blood thirsty race, they live beneath The earth, and slay with venomed teeth. On, smite the lord of Lanká's isle, But guard you from the giants' guile Who each dishonest art employ And by deceit brave foes destroy. So shall the tyrant RávaG bleed, And Sítá from his power be freed.” Thus Garu spake: then, swift as thought, The region of the sky he sought, Where in the distance like a blaze Of fire he vanished from the gaze. Then the glad Vánars' joy rang out In many a wild tumultuous shout, And the loud roar of drum and shell Startled each distant sentinel. Canto LI. Dhúmráksha's Sally.
- **Translation**: 

---

### Verse 20 (Ramayan 0.1660)
- **Original**: 1642 The Ramayana King RávaG, where he sat within, Heard from his hall the deafening din, And with a spirit ill at ease Addressed his lords in words like these: “That warlike shout, those joyous cries, Loud as the thunder of the skies, Upsent from every Vánar throat, Some new-born confidence denote. Hark, how the sea and trembling shore Re-echo with the Vánars' roar. Though arrowy chains, securely twined Both Ráma and his brother bind, Still must the fierce triumphant shout Disturb my soul with rising doubt. Swift envoys to the army send, And learn what change these cries portend.” Obedient, at their master's call, Fleet giants clomb the circling wall. They saw the Vánars formed and led: They saw Sugríva at their head, The brothers from their bonds released: And hope grew faint and fear increased. Their faces pale with doubt and dread, Back to the giant king they sped, And to his startled ear revealed The tidings of the battle field. The flush of rage a while gave place To chilling fear that changed his face:
- **Translation**: 

---

