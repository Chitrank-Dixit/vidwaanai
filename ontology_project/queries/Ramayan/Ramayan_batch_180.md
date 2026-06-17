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

### Verse 1 (Ramayana 0.1626)
- **Original**: 1608 The Ramayana The gate that fronts the north shall be Assailed by LakshmaG and by me, For I myself have sworn to kill The tyrant who delights in ill. Armed with the boon which Brahmá gave, The Gods of heaven he loves to brave, And through the trembling worlds he flies, Oppressor of the just and wise. Thou, Jámbaván, and thou, O King Of Vánars, all your bravest bring, And with your hosts in dense array Straight to the centre force your way. But let no Vánar in the storm Disguise him in a human form, Ye chiefs who change your shapes at will, Retain your Vánar semblance still. Thus, when we battle with the foe, Both men and Vánars will ye know, In human form will seven appear; Myself, my brother LakshmaG here; VibhishaG, and the four he led From Lanká's city when he fled.” Thus Raghu's son the chiefs addressed: Then, gazing on Suvela's crest, Transported by the lovely sight, He longed to climb the mountain height. Canto XXXVIII. The Ascent Of Suvela.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1627)
- **Original**: Canto XXXVIII. The Ascent Of Suvela. 1609 “Come let us scale,” the hero cried, “This hill with various metals dyed. This night upon the breezy crest Sugríva, LakshmaG, I, will rest, With sage VibhishaG, faithful friend, His counsel and his lore to lend. From those tall peaks each eager eye The foeman's city shall espy, Who from the wood my darling stole And brought long anguish on my soul.” Thus spake the lord of men, and bent His footsteps to the steep ascent, And Lakshma G, true in weal and woe, Next followed with his shafts and bow. VibhishaG followed, next in place, The sovereign of the Vánar race, And hundreds of the forest kind Thronged with impetuous feet, behind. The chiefs in woods and mountains bred Fast followed to Suvela's head, And gazed on Lanká bright and fair As some gay city in the air. On glittering gates, on ramparts raised By giant hands, the chieftains gazed. They saw the mighty hosts that, skilled In arts of war, the city filled, And ramparts with new ramparts lined, The swarthy hosts that stood behind. With spirits burning for the fight They saw the giants from the height, And from a hundred throats rang out Defiance and the battle shout. Then sank the sun with dying flame,
- **Translation**: 

---

### Verse 3 (Ramayana 0.1628)
- **Original**: 1610 The Ramayana And soft the shades of twilight came, And the full moon's delicious light Was shed upon the tranquil night. Canto XXXIX. Lanká. They slept secure: the sun arose And called the chieftains from repose. Before the wondering Vánars, gay With grove and garden, Lanká lay, Where golden buds the Champak showed, And bright with bloom A[oka glowed, And palm and Sál and many a tree With leaf and flower were fair to see. They looked on wood and lawn and glade, On emerald grass and dusky shade, Where creepers filled the air with scent, And luscious fruit the branches bent, Where bees inebriate loved to throng, And each sweet bird was loud in song. The wondering Vánars passed the bound That circled that enchanting ground, And as they came a sweet breeze through The odorous alleys softly blew. Some Vánars, at their king's behest, Onward to bannered Lanká pressed, While, startled by the strangers' tread, The birds and deer before them fled. Earth trembled at each step they took, And Lanká at their shouting shook. Bright rose before their wondering eyes
- **Translation**: 

---

### Verse 4 (Ramayana 0.1629)
- **Original**: Canto XL. Rávan Attacked. 1611 Trikúma's peak that kissed the skies, And, clothed with flowers of every hue, Afar its golden radiance threw. Most fair to see the mountain's head [457] A hundred leagues in length was spread. There RávaG's town, securely placed, The summit of Trikúma graced. O'er leagues of land she stretched in pride, A hundred long and twenty wide. They saw a lofty wall enfold The city, built of blocks of gold, They saw the beams of morning fall On dome and fane within the wall, Bright with the shine that mansion gives Where VishGu in his glory lives. White-crested like the Lord of Snows Before them RávaG's palace rose. High on a thousand pillars raised With gold and precious stone it blazed, Guarded by giant warders, crown And ornament of Lanká's town. Canto XL. Rávan Attacked. Still stood the son of Raghu where Suvela's peak rose high in air, And with Sugríva turned his eye To scan each quarter of the sky. There on Trikúma, nobly planned And built by Vi[vakarmá's hand, He saw the lovely Lanká, dressed
- **Translation**: 

---

### Verse 5 (Ramayana 0.1630)
- **Original**: 1612 The Ramayana In all her varied beauty, rest. High on a tower above the gate The tyrant stood in kingly state. The royal canopy displayed Above him lent its grateful shade, And servants, from the giant band, His cheek with jewelled chowries fanned. Red sandal o'er his breast was spread, His ornaments and robe were red: Thus shows a cloud of darksome hue With golden sunbeams flashing through. While Ráma and the chiefs intent Upon the king their glances bent, Up sprang Sugríva from the ground And reached the turret at a bound. Unterrified the Vánar stood, And wroth, with wondrous hardihood, The king in bitter words addressed, And thus his scorn and hate expressed: “King of the giant race, in me The friend and slave of Ráma see. Lord of the world, he gives me power To smite thee in thy fenced tower.” While through the air his challenge rang, At RávaG's face the Vánar sprang. Snatched from his head the kingly crown And dashed it in his fury down. Straight at his foe the giant flew, His mighty arms about him threw. With strength resistless swung him round And dashed him panting to the ground. Unharmed amid the storm of blows Swift to his feet Sugríva rose.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1631)
- **Original**: Canto XL. Rávan Attacked. 1613 Again in furious fight they met: With streams of blood their limbs were wet, Each grasping his opponent's waist. Thus with their branches interlaced, Which, crimson with the flowers of spring, From side to side the breezes swing, In furious wrestle you may see The Kin[uk and the Seemal tree.948 They fought with fists and hands, alike Prepared to parry and to strike. Long time the doubtful combat, waged With matchless strength and fury, raged. Each fiercely struck, each guarded well, Till, closing, from the tower they fell, And, grasping each the other's throat, Lay for an instant in the moat. They rose, and each in fiercer mood The sanguinary strife renewed. Well matched in size and strength and skill They fought the dubious battle still. While sweat and blood their limbs bedewed They met, retreated, and pursued: Each stratagem and art they tried, Stood front to front and swerved aside. His hand a while the giant stayed And called his magic to his aid. But brave Sugríva, swift to know The guileful purpose of the foe, Gained with light leap the upper air, And breath and strength and spirit there; Then, joyous as for victory won, 948 The Kin[uk, also called Palá[a, is Butea Frondosa, a tree that bears beautiful red crescent shaped blossoms and is deservedly a favorite with poets. The Seemal orZálmalí is the silk cotton tree which also bears red blossoms.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1632)
- **Original**: 1614 The Ramayana Returned to Raghu's royal son. Canto XLI. Ráma's Envoy. When Ráma saw each bloody trace On King Sugríva's limbs and face, He cried, while, sorrowing at the view, His arms about his friend he threw: “Too venturous chieftain, kings like us Bring not their lives in peril thus; Nor, save when counsel shows the need, Attempt so bold, so rash a deed. Remember, I, VibhishaG all Have sorrowed fearing for thy fall. O do not— for us all I speak— These desperate adventures seek.” “I could not,” cried Sugríva,“brook Upon the giant king to look,[458] Nor challenge to the deadly strife The fiend who robbed thee of thy wife.” “Now Lakshma G, marshal,” Ráma cried, “Our legions where the woods are wide, And stand we ready to oppose The fury of our giant foes. This day our armies shall ascend The walls which RávaG's powers defend, And floods of Rákshas blood shall stain The streets encumbered with the slain.” Down from the peak he came, and viewed The Vánars' ordered multitude. Each captain there for battle burned,
- **Translation**: 

---

### Verse 8 (Ramayana 0.1633)
- **Original**: Canto XLI. Ráma's Envoy. 1615 Each fiery eye to Lanká turned. On, where the royal brothers led To Lanká's walls the legions sped. The northern gate, where giant foes Swarmed round their monarch, Ráma chose Where he in person might direct The battle, and his troops protect. What arm but his the post might keep Where, strong as he who sways the deep,949 Mid thousands armed with bow and mace, Stood RávaG mightiest of his race? The eastern gate was Níla's post, Where marshalled stood his Vánar host, And Mainda with his troops arrayed, And Dwivid stood to lend him aid. The southern gate was Angad's care, Who ranged his bold battalions there. Hanúmán by the port that faced The setting sun his legions placed, And King Sugríva held the wood East of the gate where RávaG stood. On every side the myriads met, And Lanká's walls of close beset That scarce the roving gale could win A passage to the hosts within. Loud as the angry ocean's roar When wild waves lash the rocky shore, Ten thousand thousand throats upsent A shout that tore the firmament, And Lanká with each grove and brook And tower and wall and rampart shook. The giants heard, and were appalled: 949 VaruGa.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1634)
- **Original**: 1616 The Ramayana Then Raghu's son to Angad called, And, led by kingly duty,950 gave This order merciful as brave: “Go, Angad, RávaG's presence seek, And thus my words of warning speak: “How art thou changed and fallen now, O Monarch of the giants, thou Whose impious fury would not spare Saint, nymph, or spirit of the air; Whose foot in haughty triumph trod On Yaksha, king, and Serpent God: How art thou fallen from thy pride Which Brahmá's favour fortified! With myriads at thy Lanká's gate I stand my righteous ire to sate, And punish thee with sword and flame, The tyrant fiend who stole my dame. Now show the might, employ the guile, O Monarch of the giants' isle, Which stole a helpless dame away: Call up thy power and strength to-day. Once more I warn thee, Rákshas King, This hour the Maithil lady bring, And, yielding while there yet is time, Seek, suppliant, pardon for the crime, Or I will leave beneath the sun No living Rákshas, no, not one. In vain from battle wilt thou fly, Or borne on pinions seek the sky; The hand of Ráma shall not spare; His fiery shaft shall smite thee there.’ ” 950 The duty of a king to save the lives of his people and avoid bloodshed until milder methods have been tried in vain.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1635)
- **Original**: Canto XLI. Ráma's Envoy. 1617 He ceased: and Angad bowed his head; Thence like embodied flame he sped, And lighted from his airy road Within the Rákshas king's abode. There sate, the centre of a ring Of counsellors, the giant king. Swift through the circle Angad pressed, And spoke with fury in his breast: “Sent by the lord of Ko[al's land, His envoy here, O King, I stand, Angad the son of Báli: fame Has haply taught thine ears my name. Thus in the words of Ráma I Am come to warn thee or defy: Come forth, and fighting in the van Display the spirit of a man. This arm shall slay thee, tyrant: all Thy nobles, kith and kin shall fall: And earth and heaven, from terror freed, Shall joy to see the oppressor bleed. VibhishaG, when his foe is slain, Anointed king in peace shall reign. Once more I counsel thee: repent, Avoid the mortal punishment, With honour due the dame restore, And pardon for thy sin implore.” Loud rose the king's infuriate cry: “Seize, seize the Vánar, let him die.” Four of his band their lord obeyed, And eager hands on Angad laid. He purposing his strength to show Gave no resistance to the foe, But swiftly round his captors cast
- **Translation**: 

---

### Verse 11 (Ramayana 0.1636)
- **Original**: 1618 The Ramayana His mighty arms and held them fast. Fierce shout and cry around him rang: Light to the palace roof he sprang, There his detaining arms unwound, And hurled the giants to the ground. Then, smiting with a fearful stroke, A turret from the roof he broke,— As when the fiery levin sent[459] By Indra from the clouds has rent The proud peak of the Lord of Snow,— And flung the stony mass below. Again with loud terrific cry He sprang exulting to the sky, And, joyous for his errand done, Stood by the side of Raghu's son. Canto XLII. The Sally. Still was the cry,“The Vánar foes Around the leaguered city close.” King RávaG from the terrace gazed And saw, with eyes where fury blazed, The Vánar host in serried ranks Press to the moat and line the banks, And, first in splendour and in place, The lion lord of Raghu's race. And Ráma looked on Lanká where Gay flags were streaming to the air, And, while keen sorrow pierced him through, His loving thoughts to Sítá flew: “There, there in deep affliction lies
- **Translation**: 

---

### Verse 12 (Ramayana 0.1637)
- **Original**: Canto XLII. The Sally. 1619 My darling with the fawn-like eyes. There on the cold bare ground she keeps Sad vigil and for Ráma weeps.” Mad with the thought,“Charge, charge,” he cried. “Let earth with Rákshas blood be dyed.” Responsive to his call rang out A loud, a universal shout, As myriads filled the moat with stone, Trees, rocks, and mountains overthrown, And charging at their leader's call Pressed forward furious to the wall. Some in their headlong ardour scaled The rampart's height, the guard assailed, And many a ponderous fragment rent From portal, tower, and battlement. Huge gates adorned with burnished gold Were loosed and lifted from their hold; And post and pillar, with a sound Like thunder, fell upon the ground. At every portal, east and west And north and south, the chieftains pressed Each in his post appointed led His myriads in the forest bred. “Charge, let the gates be opened wide: Charge, charge, my giants,” RávaG cried. They heard his voice, and loud and long Rang the wild clamour of the throng, And shell and drum their notes upsent, And every martial instrument. Forth, at the bidding of their lord From every gate the giants poured, As, when the waters rise and swell,
- **Translation**: 

---

### Verse 13 (Ramayana 0.1638)
- **Original**: 1620 The Ramayana Huge waves preceding waves impel. Again from every Vánar throat A scream of fierce defiance smote The welkin: earth and sea and sky Reëchoed with the awful cry. The roar of elephants, the neigh Of horses eager for the fray. The frequent clash of warriors' steel, The rattling of the chariot wheel. Fierce was the deadly fight: opposed In terrible array they closed, As when the Gods of heaven enraged With rebel fiends wild battle waged. Axe, spear, and mace were wielded well: At every blow a Vánar fell. But shivered rock and brandished tree Brought many a giant on his knee, To perish in his turn beneath The deadly wounds of nails and teeth. Canto XLIII. The Single Combats. Brave chiefs of each opposing side Their strength in single combat tried. Fierce Indrajít the fight began With Angad in the battle's van. Sampáti, strongest of his race, Stood with Prajangha face to face. Hanúmán, Jambumáli met In mortal opposition set. VibhishaG, brother of the lord
- **Translation**: 

---

### Verse 14 (Ramayana 0.1639)
- **Original**: Canto XLIII. The Single Combats. 1621 Of Lanká, raised his threatening sword And singled out, with eyes aglow With wrath,Zatrughna for his foe. The mighty Gaja Tapan sought, And Níla with Nikumbha fought. Sugríva, Vánar king, defied Fierce Praghas long in battle tried, And Lakshma G fearless in the fight Encountered Vírúpáksha's might. To meet the royal Ráma came Wild Agniketu fierce as flame; Mitraghana, he who loved to strike His foeman and his friend alike: With Ra[miketu, known and feared Where'er his ponderous flag was reared; And Yajnakopa whose delight Was ruin of the sacred rite. These met and fought, with thousands more, And trampled earth was red with gore. Swift as the bolt which Indra sends When fire from heaven the mountain rends Smote Indrajít with furious blows On Angad queller of his foes. But Angad from his foeman tore The murderous mace the warrior bore, [460] And low in dust his coursers rolled, His driver, and his car of gold. Struck by the shafts Prajangha sped, The Vánar chief Sampáti bled, But, heedless of his gashes he Crushed down the giant with a tree. Then car-borne Jambumáli smote Hanumán on the chest and throat; But at the car the Vánar rushed,
- **Translation**: 

---

### Verse 15 (Ramayana 0.1640)
- **Original**: 1622 The Ramayana And chariot, steeds, and rider crushed. Sugríva whirled a huge tree round, And struck fierce Praghas to the ground. One arrow shot from LakshmaG's bow Laid mighty Vírúpáksha low. His giant foes round Ráma pressed And shot their shafts at head and breast; But, when the iron shower was spent, Four arrows from his bow he sent, And every missile, deftly sped; Cleft from the trunk a giant head.951 Canto XLIV. The Night. The lord of Light had sunk and set: Night came; the foeman struggled yet; And fiercer for the gloom of night Grew the wild fury of the fight. Scarce could each warrior's eager eye The foeman from the friend descry. “Rákshas or Vánar? say;” cried each, And foe knew foeman by his speech. “Why wilt thou fly? O warrior, stay: Turn on the foe, and rend and slay:” Such were the cries, such words of fear Smote through the gloom each listening ear. Each swarthy rover of the night Whose golden armour flashed with light, 951 I have omitted several of these single combats, as there is little variety in the details and each duel results in the victory of the Vánar or his ally.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1641)
- **Original**: Canto XLIV. The Night. 1623 Showed like a towering hill embraced By burning woods about his waist. The giants at the Vánars flew, And ravening ate the foes they slew: With mortal bite like serpent's fang, The Vánars at the giants sprang, And car and steeds and they who bore The pennons fell bedewed with gore. No serried band, no firm array The fury of their charge could stay. Down went the horse and rider, down Went giant lords of high renown. Though midnight's shade was dense and dark, With skill that swerved not from the mark Their bows the sons of Raghu drew, And each keen shaft a chieftain slew. Uprose the blinding dust from meads Ploughed by the cars and trampling steeds, And where the warriors fell the flood Was dark and terrible with blood. Six giants952 singled Ráma out, And charged him with a furious shout Loud as the roaring of the sea When every wind is raging free. Six times he shot: six heads were cleft; Six giants dead on earth were left. Nor ceased he yet: his bow he strained, And from the sounding weapon rained A storm of shafts whose fiery glare Filled all the region of the air; And chieftains dropped before his aim Like moths that perish in the flame. 952 Yajna[atru, Mahápár[va, Mahodar, Vajradanshmra,Zuka, and SáraG.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1642)
- **Original**: 1624 The Ramayana Earth glistened where the arrows fell, As shines in autumn nights a dell Which fireflies, flashing through the gloom, With momentary light illume. But Indrajít, when Báli's son953 The victory o'er the foe had won, Saw with a fury-kindled eye His mangled steeds and driver die; Then, lost in air, he fled the fight, And vanished from the victor's sight. The Gods and saints glad voices raised, And Angad for his virtue praised; And Raghu's sons bestowed the meed Of honour due to valorous deed. Compelled his shattered car to quit, Rage filled the soul of Indrajít, Who brooked not, strong by Brahmá's grace Defeat from one of Vánar race. In magic mist concealed from view His bow the treacherous warrior drew, And Raghu's sons were first to feel The tempest of his winged steel. Then when his arrows failed to kill The princes who defied him still, He bound them with the serpent noose,954 The magic bond which none might loose. 953 Angad. 954 A mysterious weapon consisting of serpents transformed to arrows which deprived the wounded object of all sense and power of motion.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1643)
- **Original**: Canto XLV. Indrajít's Victory. 1625 Canto XLV. Indrajít's Victory. Brave Ráma, burning still to know The station of his artful foe, [461] Gave to ten chieftains, mid the best Of all the host, his high behest. Swift rose in air the Vánar band: Each region of the sky they scanned: But RávaG's son by magic skill Checked them with arrows swifter still, When streams of blood from chest and side The dauntless Vánars' limbs had dyed, The giant in his misty shroud Showed like the sun obscured by cloud. Like serpents hissing through the air, His arrows smote the princely pair; And from their limbs at every rent A stream of rushing blood was sent. Like Kin[uk trees they stood, that show In spring their blossoms' crimson glow. Then Indrajít with fury eyed Ikshváku's royal sons, and cried: “Not mighty Indra can assail Or see me when I choose to veil My form in battle: and can ye, Children of earth, contend with me? The arrowy noose this hand has shot Has bound you with a hopeless knot; And, slaughtered by my shafts and bow, To Yáma's hall this hour ye go.”
- **Translation**: 

---

### Verse 19 (Ramayana 0.1644)
- **Original**: 1626 The Ramayana He spoke, and shouted. Then anew The arrows from his bowstring flew, And pierced, well aimed with perfect art, Each limb and joint and vital part. Transfixed with shafts in every limb, Their strength relaxed, their eyes grew dim. As two tall standards side by side, With each sustaining rope untied, Fall levelled by the howling blast, So earth's majestic lords at last Beneath the arrowy tempest reeled, And prostrate pressed the battle field. Canto XLVI. Indrajít's Triumph. The Vánar chiefs whose piercing eyes Scanned eagerly the earth and skies, Saw the brave brothers wounded sore Transfixed with darts and stained with gore. The monarch of the Vánar race, With wise VibhishaG, reached the place; Angad and Níla came behind, And others of the forest kind, And standing with Hanúmán there Lamented for the fallen pair. Their melancholy eyes they raised; In fruitless search a while they gazed. But magic arts VibhishaG knew; Not hidden from his keener view, Though veiled by magic from the rest, The son of RávaG stood confessed.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1645)
- **Original**: Canto XLVI. Indrajít's Triumph. 1627 Fierce Indrajít with savage pride The fallen sons of Raghu eyed, And every giant heart was proud As thus the warrior cried aloud: “Slain by mine arrows Ráma lies, And closed in death are LakshmaG's eyes. Dead are the mighty princes who DúshaG and Khara smote and slew. The Gods and fiends may toil in vain To free them from the binding chain. The haughty chief, my father's dread, Who drove him sleepless from his bed, While Lanká, troubled like a brook In rain time, heard his name and shook: He whose fierce hate our lives pursued Lies helpless by my shafts subdued. Now fruitless is each wondrous deed Wrought by the race the forests breed, And fruitless every toil at last Like cloudlets when the rains are past.” Then rose the shout of giants loud As thunder from a bursting cloud, When, deeming Ráma, dead, they raised Their voices and the conqueror praised. Still motionless, as lie the slain, The brothers pressed the bloody plain, No sigh they drew, no breath they heaved, And lay as though of life bereaved. Proud of the deed his art had done, To Lanká's town went RávaG's son, Where, as he passed, all fear was stilled, And every heart with triumph filled.
- **Translation**: 

---

