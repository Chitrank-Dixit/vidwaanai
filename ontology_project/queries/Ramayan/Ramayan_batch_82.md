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

### Verse 1 (Ramayan 0.1621)
- **Original**: Canto XXXV. Malyaván's Speech. 1603 Their constant task, their sole delight Is worship and each holy rite, To chant aloud the Veda hymn, Nor let the sacred fires grow dim. Now through the air like thunder ring The echoes of the chants they sing. The vapours of their incense rise And veil with cloudy pall the skies, And Rákshas might grows weak and faint Killed by the power of sage and saint. By Brahmá's boon thy life was screened From God, Gandharva, Yaksha, fiend; But Vánars, men, and bears, arrayed Against thee now, thy shores invade. Red meteors, heralds of despair Flash frequent through the lurid air, Foretelling to my troubled mind The ruin of the Rákshas kind. With awful thundering overhead Clouds black as night are densely spread, And oozing from the gloomy pall Great drops of blood on Lanká fall. Dogs roam through house and shrine to steal The sacred oil and curd and meal, Cats pair with tigers, hounds with swine, And asses' foals are born of kine. In these and countless signs I trace The ruin of the giant race. 'Tis VishGu's self who comes to storm Thy city, clothed in Ráma's form; For, well I ween, no mortal hand The ocean with a bridge has spanned. O giant King, the dame release, And sue to Raghu's son for peace”
- **Translation**: 

---

### Verse 2 (Ramayan 0.1622)
- **Original**: 1604 The Ramayana [455] Canto XXXVI. Rávan's Reply. But RávaG's breast with fury swelled, And thus he spake by Death impelled, While, under brows in anger bent, Fierce glances from his eyes were sent: “The bitter words which thou, misled By friendly thought, hast fondly said, Which praise the foe and counsel fear, Unheeded fall upon mine ear. How canst thou deem a mighty foe This Ráma who, in stress of woe, Seeks, banished as his sire decreed, Assistance from the Vánar breed? Am I so feeble in thine eyes, Though feared by dwellers of the skies,— Whose might in many a battle shown The glorious race of giants own? Shall I for fear of him restore The lady whom I hither bore, Exceeding fair like Beauty's Queen944 Without her well-loved lotus seen? Around the chief let LakshmaG stand, Sugríva, and each Vánar band, Soon, Malyaván, thine eyes will see This boasted Ráma slain by me. I in the brunt of war defy 944 Lakshmí is the Goddess both of beauty and fortune, and is represented with a lotus in her hand.
- **Translation**: 

---

### Verse 3 (Ramayan 0.1623)
- **Original**: Canto XXXVI. Rávan's Reply. 1605 The mightiest warriors of the sky; And if I stoop to combat men, Shall I be weak and tremble then? This mangled trunk the foe may rend, But RávaG ne'er can yield or bend, And be it vice or virtue, I This nature never will belie. What marvel if he bridged the sea? Why should this deed disquiet thee? This, only this, I surely know, Back with his life he shall not go.” Thus in loud tones the king exclaimed, And mute stood Malyaván ashamed, His reverend head he humbly bent, And slowly to his mansion went. But RávaG stayed, and deep in care Held counsel with his nobles there, All entrance to secure and close, And guard the city from their foes. He bade the chief Prahasta wait, Commander at the eastern gate, To fierce Mahodar, strong and brave, To keep the southern gate, he gave, Where Mahápár[va's might should aid The chieftain with his hosts arrayed. To guard the west— no chief more fit— He placed the warrior Indrajít, His son, the giant's joy and boast, Surrounded by a Rákshas host: And mighty SáraG hastened forth With Zuka to protect the north.945 945 The poet appears to have forgotten thatZuka and SáraG were dismissed with ignominy in Canto XXIX, and have not been reinstated.
- **Translation**: 

---

### Verse 4 (Ramayan 0.1624)
- **Original**: 1606 The Ramayana “I will myself,” the monarch cried, “Be present on the northern side.” These orders for the walls' defence The tyrant gave, then parted thence, And, by the hope of victory fired, To chambers far within, retired. Canto XXXVII. Preparations. Lords of the legions of the wood, The chieftains with VibhishaG stood, And, strangers in the foeman's land, Their hopes and fears in council scanned: “See, see where Lanká's towers ascend, Which RávaG's power and might defend, Which Gods, Gandharvas, fiends would fail To conquer, if they durst assail. How shall our legions pass within, The city of the foe to win, With massive walls and portals barred Which RávaG keeps with surest guard?” With anxious looks the walls they eyed: And sage VibhishaG thus replied: “These lords of mine946 can answer: they Within the walls have found their way, The foeman's plan and order learned, And hither to my side returned. Now, Ráma, let my tongue declare 946 The four who fled with him. Their names are Anala, Panasa, Sampáti, and Pramati.
- **Translation**: 

---

### Verse 5 (Ramayan 0.1625)
- **Original**: Canto XXXVII. Preparations. 1607 How Ráva G's hosts are stationed there. Prahasta heads, in warlike state, His legions at the eastern gate. To guard the southern portal stands Mahodar, girt by Rákshas bands, Where mighty Mahápár[va, sent By RávaG's hest, his aid has lent. Guard of the gate that fronts the west Is valiant Indrajít, the best Of warriors, RávaG's joy and pride; And by the youthful chieftain's side Are giants, armed for fierce attacks With sword and mace and battle-axe. North, where approach is dreaded most, The king, encompassed with a host Of giants trained in war, whose hands Wield maces, swords and lances, stands. [456] All these are chiefs whom RávaG chose As mightiest to resist his foes; And each a countless army947 leads With elephants and cars and steeds.” Then Ráma, while his spirit burned For battle, words like these returned: “The eastern gate be Níla's care, Opponent of Prahasta there. The southern gate, with troops arrayed Let Angad, Báli's son, invade. The gate that fronts the falling sun Shall be by brave Hanúmán won; Soon through its portals shall he lead His myriads of Vánar breed. 947 The numbers here are comparatively moderate: ten thousand elephants, ten thousand chariots, twenty thousand horses and ten million giants.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1626)
- **Original**: 1608 The Ramayana The gate that fronts the north shall be Assailed by LakshmaG and by me, For I myself have sworn to kill The tyrant who delights in ill. Armed with the boon which Brahmá gave, The Gods of heaven he loves to brave, And through the trembling worlds he flies, Oppressor of the just and wise. Thou, Jámbaván, and thou, O King Of Vánars, all your bravest bring, And with your hosts in dense array Straight to the centre force your way. But let no Vánar in the storm Disguise him in a human form, Ye chiefs who change your shapes at will, Retain your Vánar semblance still. Thus, when we battle with the foe, Both men and Vánars will ye know, In human form will seven appear; Myself, my brother LakshmaG here; VibhishaG, and the four he led From Lanká's city when he fled.” Thus Raghu's son the chiefs addressed: Then, gazing on Suvela's crest, Transported by the lovely sight, He longed to climb the mountain height. Canto XXXVIII. The Ascent Of Suvela.
- **Translation**: 

---

### Verse 7 (Ramayan 0.1627)
- **Original**: Canto XXXVIII. The Ascent Of Suvela. 1609 “Come let us scale,” the hero cried, “This hill with various metals dyed. This night upon the breezy crest Sugríva, LakshmaG, I, will rest, With sage VibhishaG, faithful friend, His counsel and his lore to lend. From those tall peaks each eager eye The foeman's city shall espy, Who from the wood my darling stole And brought long anguish on my soul.” Thus spake the lord of men, and bent His footsteps to the steep ascent, And Lakshma G, true in weal and woe, Next followed with his shafts and bow. VibhishaG followed, next in place, The sovereign of the Vánar race, And hundreds of the forest kind Thronged with impetuous feet, behind. The chiefs in woods and mountains bred Fast followed to Suvela's head, And gazed on Lanká bright and fair As some gay city in the air. On glittering gates, on ramparts raised By giant hands, the chieftains gazed. They saw the mighty hosts that, skilled In arts of war, the city filled, And ramparts with new ramparts lined, The swarthy hosts that stood behind. With spirits burning for the fight They saw the giants from the height, And from a hundred throats rang out Defiance and the battle shout. Then sank the sun with dying flame,
- **Translation**: 

---

### Verse 8 (Ramayan 0.1628)
- **Original**: 1610 The Ramayana And soft the shades of twilight came, And the full moon's delicious light Was shed upon the tranquil night. Canto XXXIX. Lanká. They slept secure: the sun arose And called the chieftains from repose. Before the wondering Vánars, gay With grove and garden, Lanká lay, Where golden buds the Champak showed, And bright with bloom A[oka glowed, And palm and Sál and many a tree With leaf and flower were fair to see. They looked on wood and lawn and glade, On emerald grass and dusky shade, Where creepers filled the air with scent, And luscious fruit the branches bent, Where bees inebriate loved to throng, And each sweet bird was loud in song. The wondering Vánars passed the bound That circled that enchanting ground, And as they came a sweet breeze through The odorous alleys softly blew. Some Vánars, at their king's behest, Onward to bannered Lanká pressed, While, startled by the strangers' tread, The birds and deer before them fled. Earth trembled at each step they took, And Lanká at their shouting shook. Bright rose before their wondering eyes
- **Translation**: 

---

### Verse 9 (Ramayan 0.1629)
- **Original**: Canto XL. Rávan Attacked. 1611 Trikúma's peak that kissed the skies, And, clothed with flowers of every hue, Afar its golden radiance threw. Most fair to see the mountain's head [457] A hundred leagues in length was spread. There RávaG's town, securely placed, The summit of Trikúma graced. O'er leagues of land she stretched in pride, A hundred long and twenty wide. They saw a lofty wall enfold The city, built of blocks of gold, They saw the beams of morning fall On dome and fane within the wall, Bright with the shine that mansion gives Where VishGu in his glory lives. White-crested like the Lord of Snows Before them RávaG's palace rose. High on a thousand pillars raised With gold and precious stone it blazed, Guarded by giant warders, crown And ornament of Lanká's town. Canto XL. Rávan Attacked. Still stood the son of Raghu where Suvela's peak rose high in air, And with Sugríva turned his eye To scan each quarter of the sky. There on Trikúma, nobly planned And built by Vi[vakarmá's hand, He saw the lovely Lanká, dressed
- **Translation**: 

---

### Verse 10 (Ramayan 0.1630)
- **Original**: 1612 The Ramayana In all her varied beauty, rest. High on a tower above the gate The tyrant stood in kingly state. The royal canopy displayed Above him lent its grateful shade, And servants, from the giant band, His cheek with jewelled chowries fanned. Red sandal o'er his breast was spread, His ornaments and robe were red: Thus shows a cloud of darksome hue With golden sunbeams flashing through. While Ráma and the chiefs intent Upon the king their glances bent, Up sprang Sugríva from the ground And reached the turret at a bound. Unterrified the Vánar stood, And wroth, with wondrous hardihood, The king in bitter words addressed, And thus his scorn and hate expressed: “King of the giant race, in me The friend and slave of Ráma see. Lord of the world, he gives me power To smite thee in thy fenced tower.” While through the air his challenge rang, At RávaG's face the Vánar sprang. Snatched from his head the kingly crown And dashed it in his fury down. Straight at his foe the giant flew, His mighty arms about him threw. With strength resistless swung him round And dashed him panting to the ground. Unharmed amid the storm of blows Swift to his feet Sugríva rose.
- **Translation**: 

---

### Verse 11 (Ramayan 0.1631)
- **Original**: Canto XL. Rávan Attacked. 1613 Again in furious fight they met: With streams of blood their limbs were wet, Each grasping his opponent's waist. Thus with their branches interlaced, Which, crimson with the flowers of spring, From side to side the breezes swing, In furious wrestle you may see The Kin[uk and the Seemal tree.948 They fought with fists and hands, alike Prepared to parry and to strike. Long time the doubtful combat, waged With matchless strength and fury, raged. Each fiercely struck, each guarded well, Till, closing, from the tower they fell, And, grasping each the other's throat, Lay for an instant in the moat. They rose, and each in fiercer mood The sanguinary strife renewed. Well matched in size and strength and skill They fought the dubious battle still. While sweat and blood their limbs bedewed They met, retreated, and pursued: Each stratagem and art they tried, Stood front to front and swerved aside. His hand a while the giant stayed And called his magic to his aid. But brave Sugríva, swift to know The guileful purpose of the foe, Gained with light leap the upper air, And breath and strength and spirit there; Then, joyous as for victory won, 948 The Kin[uk, also called Palá[a, is Butea Frondosa, a tree that bears beautiful red crescent shaped blossoms and is deservedly a favorite with poets. The Seemal orZálmalí is the silk cotton tree which also bears red blossoms.
- **Translation**: 

---

### Verse 12 (Ramayan 0.1632)
- **Original**: 1614 The Ramayana Returned to Raghu's royal son. Canto XLI. Ráma's Envoy. When Ráma saw each bloody trace On King Sugríva's limbs and face, He cried, while, sorrowing at the view, His arms about his friend he threw: “Too venturous chieftain, kings like us Bring not their lives in peril thus; Nor, save when counsel shows the need, Attempt so bold, so rash a deed. Remember, I, VibhishaG all Have sorrowed fearing for thy fall. O do not— for us all I speak— These desperate adventures seek.” “I could not,” cried Sugríva,“brook Upon the giant king to look,[458] Nor challenge to the deadly strife The fiend who robbed thee of thy wife.” “Now Lakshma G, marshal,” Ráma cried, “Our legions where the woods are wide, And stand we ready to oppose The fury of our giant foes. This day our armies shall ascend The walls which RávaG's powers defend, And floods of Rákshas blood shall stain The streets encumbered with the slain.” Down from the peak he came, and viewed The Vánars' ordered multitude. Each captain there for battle burned,
- **Translation**: 

---

### Verse 13 (Ramayan 0.1633)
- **Original**: Canto XLI. Ráma's Envoy. 1615 Each fiery eye to Lanká turned. On, where the royal brothers led To Lanká's walls the legions sped. The northern gate, where giant foes Swarmed round their monarch, Ráma chose Where he in person might direct The battle, and his troops protect. What arm but his the post might keep Where, strong as he who sways the deep,949 Mid thousands armed with bow and mace, Stood RávaG mightiest of his race? The eastern gate was Níla's post, Where marshalled stood his Vánar host, And Mainda with his troops arrayed, And Dwivid stood to lend him aid. The southern gate was Angad's care, Who ranged his bold battalions there. Hanúmán by the port that faced The setting sun his legions placed, And King Sugríva held the wood East of the gate where RávaG stood. On every side the myriads met, And Lanká's walls of close beset That scarce the roving gale could win A passage to the hosts within. Loud as the angry ocean's roar When wild waves lash the rocky shore, Ten thousand thousand throats upsent A shout that tore the firmament, And Lanká with each grove and brook And tower and wall and rampart shook. The giants heard, and were appalled: 949 VaruGa.
- **Translation**: 

---

### Verse 14 (Ramayan 0.1634)
- **Original**: 1616 The Ramayana Then Raghu's son to Angad called, And, led by kingly duty,950 gave This order merciful as brave: “Go, Angad, RávaG's presence seek, And thus my words of warning speak: “How art thou changed and fallen now, O Monarch of the giants, thou Whose impious fury would not spare Saint, nymph, or spirit of the air; Whose foot in haughty triumph trod On Yaksha, king, and Serpent God: How art thou fallen from thy pride Which Brahmá's favour fortified! With myriads at thy Lanká's gate I stand my righteous ire to sate, And punish thee with sword and flame, The tyrant fiend who stole my dame. Now show the might, employ the guile, O Monarch of the giants' isle, Which stole a helpless dame away: Call up thy power and strength to-day. Once more I warn thee, Rákshas King, This hour the Maithil lady bring, And, yielding while there yet is time, Seek, suppliant, pardon for the crime, Or I will leave beneath the sun No living Rákshas, no, not one. In vain from battle wilt thou fly, Or borne on pinions seek the sky; The hand of Ráma shall not spare; His fiery shaft shall smite thee there.’ ” 950 The duty of a king to save the lives of his people and avoid bloodshed until milder methods have been tried in vain.
- **Translation**: 

---

### Verse 15 (Ramayan 0.1635)
- **Original**: Canto XLI. Ráma's Envoy. 1617 He ceased: and Angad bowed his head; Thence like embodied flame he sped, And lighted from his airy road Within the Rákshas king's abode. There sate, the centre of a ring Of counsellors, the giant king. Swift through the circle Angad pressed, And spoke with fury in his breast: “Sent by the lord of Ko[al's land, His envoy here, O King, I stand, Angad the son of Báli: fame Has haply taught thine ears my name. Thus in the words of Ráma I Am come to warn thee or defy: Come forth, and fighting in the van Display the spirit of a man. This arm shall slay thee, tyrant: all Thy nobles, kith and kin shall fall: And earth and heaven, from terror freed, Shall joy to see the oppressor bleed. VibhishaG, when his foe is slain, Anointed king in peace shall reign. Once more I counsel thee: repent, Avoid the mortal punishment, With honour due the dame restore, And pardon for thy sin implore.” Loud rose the king's infuriate cry: “Seize, seize the Vánar, let him die.” Four of his band their lord obeyed, And eager hands on Angad laid. He purposing his strength to show Gave no resistance to the foe, But swiftly round his captors cast
- **Translation**: 

---

### Verse 16 (Ramayan 0.1636)
- **Original**: 1618 The Ramayana His mighty arms and held them fast. Fierce shout and cry around him rang: Light to the palace roof he sprang, There his detaining arms unwound, And hurled the giants to the ground. Then, smiting with a fearful stroke, A turret from the roof he broke,— As when the fiery levin sent[459] By Indra from the clouds has rent The proud peak of the Lord of Snow,— And flung the stony mass below. Again with loud terrific cry He sprang exulting to the sky, And, joyous for his errand done, Stood by the side of Raghu's son. Canto XLII. The Sally. Still was the cry,“The Vánar foes Around the leaguered city close.” King RávaG from the terrace gazed And saw, with eyes where fury blazed, The Vánar host in serried ranks Press to the moat and line the banks, And, first in splendour and in place, The lion lord of Raghu's race. And Ráma looked on Lanká where Gay flags were streaming to the air, And, while keen sorrow pierced him through, His loving thoughts to Sítá flew: “There, there in deep affliction lies
- **Translation**: 

---

### Verse 17 (Ramayan 0.1637)
- **Original**: Canto XLII. The Sally. 1619 My darling with the fawn-like eyes. There on the cold bare ground she keeps Sad vigil and for Ráma weeps.” Mad with the thought,“Charge, charge,” he cried. “Let earth with Rákshas blood be dyed.” Responsive to his call rang out A loud, a universal shout, As myriads filled the moat with stone, Trees, rocks, and mountains overthrown, And charging at their leader's call Pressed forward furious to the wall. Some in their headlong ardour scaled The rampart's height, the guard assailed, And many a ponderous fragment rent From portal, tower, and battlement. Huge gates adorned with burnished gold Were loosed and lifted from their hold; And post and pillar, with a sound Like thunder, fell upon the ground. At every portal, east and west And north and south, the chieftains pressed Each in his post appointed led His myriads in the forest bred. “Charge, let the gates be opened wide: Charge, charge, my giants,” RávaG cried. They heard his voice, and loud and long Rang the wild clamour of the throng, And shell and drum their notes upsent, And every martial instrument. Forth, at the bidding of their lord From every gate the giants poured, As, when the waters rise and swell,
- **Translation**: 

---

### Verse 18 (Ramayan 0.1638)
- **Original**: 1620 The Ramayana Huge waves preceding waves impel. Again from every Vánar throat A scream of fierce defiance smote The welkin: earth and sea and sky Reëchoed with the awful cry. The roar of elephants, the neigh Of horses eager for the fray. The frequent clash of warriors' steel, The rattling of the chariot wheel. Fierce was the deadly fight: opposed In terrible array they closed, As when the Gods of heaven enraged With rebel fiends wild battle waged. Axe, spear, and mace were wielded well: At every blow a Vánar fell. But shivered rock and brandished tree Brought many a giant on his knee, To perish in his turn beneath The deadly wounds of nails and teeth. Canto XLIII. The Single Combats. Brave chiefs of each opposing side Their strength in single combat tried. Fierce Indrajít the fight began With Angad in the battle's van. Sampáti, strongest of his race, Stood with Prajangha face to face. Hanúmán, Jambumáli met In mortal opposition set. VibhishaG, brother of the lord
- **Translation**: 

---

### Verse 19 (Ramayan 0.1639)
- **Original**: Canto XLIII. The Single Combats. 1621 Of Lanká, raised his threatening sword And singled out, with eyes aglow With wrath,Zatrughna for his foe. The mighty Gaja Tapan sought, And Níla with Nikumbha fought. Sugríva, Vánar king, defied Fierce Praghas long in battle tried, And Lakshma G fearless in the fight Encountered Vírúpáksha's might. To meet the royal Ráma came Wild Agniketu fierce as flame; Mitraghana, he who loved to strike His foeman and his friend alike: With Ra[miketu, known and feared Where'er his ponderous flag was reared; And Yajnakopa whose delight Was ruin of the sacred rite. These met and fought, with thousands more, And trampled earth was red with gore. Swift as the bolt which Indra sends When fire from heaven the mountain rends Smote Indrajít with furious blows On Angad queller of his foes. But Angad from his foeman tore The murderous mace the warrior bore, [460] And low in dust his coursers rolled, His driver, and his car of gold. Struck by the shafts Prajangha sped, The Vánar chief Sampáti bled, But, heedless of his gashes he Crushed down the giant with a tree. Then car-borne Jambumáli smote Hanumán on the chest and throat; But at the car the Vánar rushed,
- **Translation**: 

---

### Verse 20 (Ramayan 0.1640)
- **Original**: 1622 The Ramayana And chariot, steeds, and rider crushed. Sugríva whirled a huge tree round, And struck fierce Praghas to the ground. One arrow shot from LakshmaG's bow Laid mighty Vírúpáksha low. His giant foes round Ráma pressed And shot their shafts at head and breast; But, when the iron shower was spent, Four arrows from his bow he sent, And every missile, deftly sped; Cleft from the trunk a giant head.951 Canto XLIV. The Night. The lord of Light had sunk and set: Night came; the foeman struggled yet; And fiercer for the gloom of night Grew the wild fury of the fight. Scarce could each warrior's eager eye The foeman from the friend descry. “Rákshas or Vánar? say;” cried each, And foe knew foeman by his speech. “Why wilt thou fly? O warrior, stay: Turn on the foe, and rend and slay:” Such were the cries, such words of fear Smote through the gloom each listening ear. Each swarthy rover of the night Whose golden armour flashed with light, 951 I have omitted several of these single combats, as there is little variety in the details and each duel results in the victory of the Vánar or his ally.
- **Translation**: 

---

