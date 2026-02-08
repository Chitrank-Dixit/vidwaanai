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

### Verse 1 (Ramayan 0.1741)
- **Original**: Canto CII. Lakshman Healed. 1723 Those worlds with thee? O speak, O speak! Rise up once more, my brother, rise, Look on me with thy loving eyes. Were not thy steps beside me still In gloomy wood, on breezy hill? Did not thy gentle care assuage Thy brother's grief and fitful rage? Didst thou not all his troubles share, His guide and comfort in despair?” As Ráma, vanquished, wept and sighed The Vánar chieftain thus replied: “Great Prince, unmanly thoughts dismiss, Nor yield thy soul to grief like this. In vain those burning tears are shed: Our glory LakshmaG is not dead. Death on his brow no mark has set, Where beauty's lustre lingers yet. Clear is the skin, and tender hues Of lotus flowers his palms suffuse. O Ráma, cheer thy trembling heart; Not thus do life and body part. Now, Hanumán, to thee I speak: Hie hence to tall Mahodaya's996 peak Where herbs of sovereign virtue grow Which life and health and strength bestow Bring thou the leaves to balm his pain, And Lakshma G shall be well again.” 996 Apparently a peak of the Himalaya chain.
- **Translation**: 

---

### Verse 2 (Ramayan 0.1742)
- **Original**: 1724 The Ramayana He ceased: the Wind-God's son obeyed Swift through the clouds his way he made. He reached the hill, nor stayed to find The wondrous herbs of healing kind, From its broad base the mount he tore With all the shrubs and trees it bore, Sped through the clouds again and showed To wise SusheG his woody load.997 SusheG in wonder viewed the hill, And culled the sovereign salve of ill. Soon as the healing herb he found, The fragrant leaves he crushed and ground. Then over LakshmaG's face he bent, Who, healed and strengthened by the scent Of that blest herb divinely sweet, Rose fresh and lusty on his feet. Canto CIII. Indra's Car. Then Raghu's son forgot his woe: Again he grasped his fallen bow And hurled at Lanká's lord amain The tempest of his arrowy rain.[489] 997 This exploit of Hanumán is related with inordinate prolixity in the Bengal recension (Gortesio's text). Among other adventures he narrowly escapes being shot by Bharat as he passes over Nandigrama near Ayodhyá. Hanumán stays Bharat in time, and gives him an account of what has befallen Ráma and Sítá in the forest and in Lanká.
- **Translation**: 

---

### Verse 3 (Ramayan 0.1743)
- **Original**: Canto CIII. Indra's Car. 1725 Drawn by the steeds his lords had brought, Again the giant turned and fought. And drove his glittering chariot nigh As springs the Day-God through the sky. Then, as his sounding bow he bent, Like thunderbolts his shafts were sent, As when dark clouds in rain time shed Fierce torrents on a mountain's head. High on his car the giant rode, On foot the son of Raghu strode. The Gods from their celestial height Indignant saw the unequal fight. Then he whom heavenly hosts revere, Lord Indra, called his charioteer: “Haste, Mátali,” he cried,“descend; To Raghu's son my chariot lend. With cheering words the chief address; And all the Gods thy deed will bless.” He bowed; he brought the glorious car Whose tinkling bells were heard afar; Fair as the sun of morning, bright With gold and pearl and lazulite. He yoked the steeds of tawny hue That swifter than the tempest flew. Then down the slope of heaven he hied And stayed the car by Ráma's side. “Ascend, O Chief,” he humbly cried, “The chariot which the Gods provide. The mighty bow of Indra see, Sent by the Gods who favour thee; Behold this coat of glittering mail, And spear and shafts which never fail.”
- **Translation**: 

---

### Verse 4 (Ramayan 0.1744)
- **Original**: 1726 The Ramayana Cheered by the grace the Immortals showed The chieftain on the chariot rode. Then as the car-borne warriors met The awful fight raged fiercer yet. Each shaft that RávaG shot became A serpent red with kindled flame, And round the limbs of Ráma hung With fiery jaws and quivering tongue. But every serpent fled dismayed When Raghu's valiant son displayed The weapon of the Feathered King,998 And loosed his arrows from the string. But RávaG armed his bow anew, And showers of shafts at Ráma flew, While the fierce king in swift career Smote with a dart the charioteer. An arrow shot by RávaG's hand Laid the proud banner on the sand, And Indra's steeds of heavenly strain Fell by the iron tempest slain. On Gods and spirits of the air Fell terror, trembling, and despair. The sea's white billows mounted high With froth and foam to drench the sky. The sun by lurid clouds was veiled, The friendly lights of heaven were paled; And, fiercely gleaming, fiery Mars Opposed the beams of gentler stars. 998 As Garu the king of birds is the mortal enemy of serpents the weapon sacred to him is of course best calculated to destroy the serpent arrows of RávaG.
- **Translation**: 

---

### Verse 5 (Ramayan 0.1745)
- **Original**: Canto CVI. Glory To The Sun. 1727 Then Ráma's eyes with fury blazed As Indra's heavenly spear he raised. Loud rang the bells: the glistering head Bright flashes through the region shed. Down came the spear in swift descent: The giant's lance was crushed and bent. Then RávaG's horses brave and fleet Fell dead beneath his arrowy sleet. Fierce on his foeman Ráma pressed, And gored with shafts his mighty breast. And spouting streams of crimson dyed The weary giant's limbs and side. [I omit Cantos CIV and CV in which the fight is renewed and RávaG severely reprimands his charioteer for timidity and want of confidence in his master's prowess, and orders him to charge straight at Ráma on the next occasion.] Canto CVI. Glory To The Sun. There faint and bleeding fast, apart Stood RávaG raging in his heart. Then, moved with ruth for Ráma's sake, Agastya999 came and gently spake: “Bend, Ráma, bend thy heart and ear The everlasting truth to hear Which all thy hopes through life will bless And crown thine arms with full success. The rising sun with golden rays, 999 The celebrated saint who has on former occasions assisted Ráma with his gifts and counsel.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1746)
- **Original**: 1728 The Ramayana Light of the worlds, adore and praise: The universal king, the lord By hosts of heaven and fiends adored. He tempers all with soft control, He is the Gods' diviner soul; And Gods above and fiends below And men to him their safety owe. He Brahmá, VishGu,Ziva, he Each person of the glorious Three, Is every God whose praise we tell, The King of Heaven,1000 the Lord of Hell:1001 Each God revered from times of old, The Lord of War,1002 the King of Gold:1003[490] Mahendra, Time and Death is he, The Moon, the Ruler of the Sea.1004 He hears our praise in every form,— The manes,1005 Gods who ride the storm,1006 The A[vins,1007 Manu,1008 they who stand Round Indra,1009 and the Sádhyas'1010 band He is the air, and life and fire, 1000 Indra. 1001 Yáma. 1002 Kártikeya. 1003 Kubera. 1004 VaruG. 1005 The Pitris, forefathers or spirits of the dead, are of two kinds, either the spirits of the father, grandfathers and great-grandfathers of an individual or the progenitors of mankind generally, to both of whom obsequial worship is paid and oblations of food are presented. 1006 The Maruts or Storm-Gods. 1007 The Heavenly Twins, the Castor and Pollux of the Hindus. 1008 The Man par excellence, the representative man and father of the human race regarded also as God. 1009 The Vasus, a class of deities originally personifications of natural phenom- ena. 1010 A class of celestial beings who dwell between the earth and the sun.
- **Translation**: 

---

### Verse 7 (Ramayan 0.1747)
- **Original**: Canto CVI. Glory To The Sun. 1729 The universal source and sire: He brings the seasons at his call, Creator, light, and nurse of all. His heavenly course he joys to run, Maker of Day, the golden sun. The steeds that whirl his car are seven,1011 The flaming steeds that flash through heaven. Lord of the sky, the conqueror parts The clouds of night with glistering darts. He, master of the Vedas' lore, Commands the clouds' collected store: He is the rivers' surest friend; He bids the rains, and they descend. Stars, planets, constellations own Their monarch of the golden throne. Lord of twelve forms,1012 to thee I bow, Most glorious King of heaven art thou. O Ráma, he who pays aright Due worship to the Lord of Light Shall never fall oppressed by ill, But find a stay and comfort still. Adore with all thy heart and mind This God of Gods, to him resigned; And thou his saving power shalt know Victorious o'er thy giant foe.” [This Canto does not appear in the Bengal recension. It comes in awkwardly and may I think be considered as an interpolation, but I paraphrase a portion of it as a relief after so much fighting and carnage, and as an interesting glimpse of the monotheistic ideas which underlie the Hindu religion. The hymn does not readily lend itself to metrical translation, and I have not attempted here 1011 The seven horses are supposed to symbolize the seven days of the week. 1012 One for each month in the year.
- **Translation**: 

---

### Verse 8 (Ramayan 0.1748)
- **Original**: 1730 The Ramayana to give a faithful rendering of the whole. A literal version of the text and the commentary given in the Calcutta edition will be found in the Additional Notes. A canto is here omitted. It contains fighting of the ordinary kind between Ráma and RávaG, and a description of sights and sounds of evil omen foreboding the destruction of the giant.] Canto CVIII. The Battle. He spoke, and vanished: Ráma raised His eyes with reverence meet, and praised The glorious Day-God full in view: Then armed him for the fight anew. Urged onward by his charioteer The giant's foaming steeds came near, And furious was the battle's din Where each resolved to die or win. The Rákshas host and Vánar bands Stood with their weapons in their hands, And watched in terror and dismay The fortune of the awful fray. The giant chief with rage inflamed His darts at Ráma's pennon aimed; But when they touched the chariot made By heavenly hands their force was stayed. Then Ráma's breast with fury swelled; He strained the mighty bow he held, And straight at RávaG's banner flew An arrow as the string he drew— A deadly arrow swift of flight, Like some huge snake ablaze with light,
- **Translation**: 

---

### Verse 9 (Ramayan 0.1749)
- **Original**: Canto CIX. The Battle. 1731 Whose fury none might e'er repel,— And, split in twain, the standard fell. At Ráma's steeds sharp arrows, hot With flames of fire, the giant shot. Unmoved the heavenly steeds sustained The furious shower the warrior rained, As though soft lotus tendrils smote Each haughty crest and glossy coat. Then volleyed swift by magic art, Tree, mountain peak and spear and dart, Trident and pike and club and mace Flew hurtling straight at Ráma's face. But Ráma with his steeds and car Escaped the storm which fell afar Where the strange missiles, as they rushed To earth, a thousand Vánars crushed. [491] Canto CIX. The Battle. With wondrous power and might and skill The giant fought with Ráma still. Each at his foe his chariot drove, And still for death or victory strove. The warriors' steeds together dashed, And pole with pole reëchoing clashed. Then Ráma launching dart on dart Made RávaG's coursers swerve and start. Nor was the lord of Lanká slow To rain his arrows on the foe,
- **Translation**: 

---

### Verse 10 (Ramayan 0.1750)
- **Original**: 1732 The Ramayana Who showed, by fiery points assailed, No trace of pain, nor shook nor quailed. Dense clouds of arrows Ráma shot With that strong arm which rested not, And spear and mace and club and brand Fell in dire rain from RávaG's hand. The storm of missiles fiercely cast Stirred up the oceans with its blast, And Serpent-Gods and fiends who dwell Below were troubled by the swell. The earth with hill and plain and brook And grove and garden reeled and shook: The very sun grew cold and pale, And horror stilled the rising gale. God and Gandharva, sage and saint Cried out, with grief and terror faint: “O may the prince of Raghu's line Give peace to Bráhmans and to kine, And, rescuing the worlds, o'erthrow The giant king our awful foe.” Then to his deadly string the pride Of Raghu's race a shaft applied. Sharp as a serpent's venomed fang Straight to its mark the arrow sprang, And from the giant's body shred With trenchant steel the monstrous head. There might the triple world behold That severed head adorned with gold. But when all eyes were bent to view, Swift in its stead another grew. Again the shaft was pointed well: Again the head divided fell; But still as each to earth was cast
- **Translation**: 

---

### Verse 11 (Ramayan 0.1751)
- **Original**: Canto CX. Rávan's Death. 1733 Another head succeeded fast. A hundred, bright with fiery flame, Fell low before the victor's aim, Yet RávaG by no sign betrayed That death was near or strength decayed. The doubtful fight he still maintained, And on the foe his missiles rained. In air, on earth, on plain, on hill, With awful might he battled still; And through the hours of night and day The conflict knew no pause or stay. Canto CX. Rávan's Death. Then Mátali to Ráma cried: “Let other arms the day decide. Why wilt thou strive with useless toil And see his might thy efforts foil? Launch at the foe thy dart whose fire Was kindled by the Almighty Sire.” He ceased: and Raghu's son obeyed: Upon his string the hero laid An arrow, like a snake that hissed. Whose fiery flight had never missed: The arrow Saint Agastya gave And blessed the chieftain's life to save That dart the Eternal Father made The Monarch of the Gods to aid; By Brahmá's self on him bestowed When forth to fight Lord Indra rode. 'Twas feathered with the rushing wind;
- **Translation**: 

---

### Verse 12 (Ramayan 0.1752)
- **Original**: 1734 The Ramayana The glowing sun and fire combined To the keen point their splendour lent; The shaft, ethereal element, By Meru's hill and Mandar, pride Of mountains, had its weight supplied. He laid it on the twisted cord, He turned the point at Lanká's lord, And swift the limb-dividing dart Pierced the huge chest and cleft the heart, And dead he fell upon the plain Like Vritra by the Thunderer slain. The Rákahas host when RávaG fell Sent forth a wild terrific yell, Then turned and fled, all hope resigned, Through Lanká's gates, nor looked behind. His voice each joyous Vánar raised, And Ráma, conquering Ráma, praised. Soft from celestial minstrels came The sound of music and acclaim. Soft, fresh, and cool, a rising breeze Brought odours from the heavenly trees, And ravishing the sight and smell A wondrous rain of blossoms fell: And voices breathed round Raghu's son: “Champion of Gods, well done, well done.” Canto CXI. Vibhishan's Lament.
- **Translation**: 

---

### Verse 13 (Ramayan 0.1753)
- **Original**: Canto CXI. Vibhishan's Lament. 1735 VibhishaG saw his brother slain, Nor could his heart its woe contain. O'er the dead king he sadly bent And mourned him with a loud lament: “O hero, bold and brave,” he cried, “Skilled in all arms, in battle tried. Spoiled of thy crown, with limbs outspread, [492] Why wilt thou press thy gory bed? Why slumber on the earth's cold breast, When sumptuous couches woo to rest? Ah me, my brother over bold, Thine is the fate my heart foretold: But love and pride forbade to hear The friend who blamed thy wild career. Fallen is the sun who gave us light, Our lordly moon is veiled in night. Our beacon fire is dead and cold A hundred waves have o'er it rolled. What could his light and fire avail Against Lord Ráma's arrowy hail? Woe for the giants' royal tree, Whose stately height was fair to see. His buds were deeds of kingly grace, His bloom the sons who decked his race. With rifled bloom and mangled bough The royal tree lies prostrate now.” “Nay, idly mourn not,” Ráma cried, “The warrior king has nobly died, Intrepid hero, firm through all, So fell he as the brave should fall; And ill beseems it chiefs like us To weep for those who perish thus. Be firm: thy causeless grief restrain, And pay the dues that yet remain.”
- **Translation**: 

---

### Verse 14 (Ramayan 0.1754)
- **Original**: 1736 The Ramayana Again VibhishaG sadly spoke: “His was the hero arm that broke Embattled Gods' and Indra's might, Unconquered ere to-day in fight. He rushed against thee, fought and fell, As Ocean, when his waters swell, Hurling his might against a rock, Falls spent and shattered by the shock. Woe for our king's untimely end, The generous lord the trusty friend: Our sure defence when fear arose, A dreaded scourge to stubborn foes. O, let the king thy hand has slain The honours of the dead obtain.” Then Ráma answered.“Hatred dies When low in dust the foeman lies. Now triumph bids the conflict cease, And knits us in the bonds of peace. Let funeral rites be duly paid. And be it mine thy toil to aid.” Canto CXII. The Rákshas Dames. High rose the universal wail That mourned the monarch's death, and, pale With crushing woe, her hair unbound, Her eyes in floods of sorrow drowned, Forth from the inner chambers came With trembling feet each royal dame, Heedless of those who bade them stay
- **Translation**: 

---

### Verse 15 (Ramayan 0.1755)
- **Original**: Canto CXIII. Mandodarí's Lament. 1737 They reached the field where RávaG lay; There falling by their husband's side, “Ah, King! ah dearest lord!” they cried. Like creepers shattered by the storm They threw them on his mangled form. One to his bleeding bosom crept And lifted up her voice and wept. About his feet one mourner clung, Around his neck another hung, One on the giant's severed head, Her pearly tears in torrents shed Fast as the drops the summer shower Pours down upon the lotus flower. “Ah, he whose arm in anger reared The King of Gods and Yáma feared, While panic struck their heavenly train, Lies prostrate in the battle slain. Thy haughty heart thou wouldst not bend, Nor listen to each wiser friend. Ah, had the dame, as they implored, Been yielded to her injured lord, We had not mourned this day thy fall, And happy had it been for all. Then Ráma and thy friends content In blissful peace their days had spent. Thine injured brother had not fled, Nor giant chiefs and Vánars bled. Yet for these woes we will not blame. Thy fancy for the Maithil dame, Fate, ruthless Fate, whom none may bend Has urged thee to thy hapless end.”
- **Translation**: 

---

### Verse 16 (Ramayan 0.1756)
- **Original**: 1738 The Ramayana Canto CXIII. Mandodarí's Lament. While thus they wept, supreme in place, The loveliest for form and face, Mandodarí drew near alone, Looked on her lord and made her moan: “Ah Monarch, Indra feared to stand In fight before thy conquering hand. From thy dread spear the Immortals ran; And art thou murdered by a man? Ah, 'twas no child of earth, I know, That smote thee with that mortal blow. 'Twas Death himself in Ráma's shape, That slew thee: Death whom none escape. Or was it he who rules the skies Who met thee, clothed in man's disguise? Ah no, my lord, not Indra: he In battle ne'er could look on thee. One only God thy match I deem: 'Twas VishGu's self, the Lord Supreme, Whose days through ceaseless time extend And ne'er began and ne'er shall end: He with the discus, shell, and mace, Brought ruin on the giant race. Girt by the Gods of heaven arrayed Like Vánar hosts his strength to aid, He Ráma's shape and arms assumed[493] And slew the king whom Fate had doomed. In Janasthán when Khara died With giant legions by his side, No mortal was the unconquered foe In Ráma's form who struck the blow. When Hanumán the Vanár came And burnt thy town with hostile flame,
- **Translation**: 

---

### Verse 17 (Ramayan 0.1757)
- **Original**: Canto CXIII. Mandodarí's Lament. 1739 I counselled peace in anxious fear: I counselled, but thou wouldst not hear. Thy fancy for the foreign dame Has brought thee death and endless shame. Why should thy foolish fancy roam? Hadst thou not wives as fair at home? In beauty, form and grace could she, Dear lord, surpass or rival me? Now will the days of Sítá glide In tranquil joy by Ráma's side: And I— ah me, around me raves A sea of woe with whelming waves. With thee in days of old I trod Each spot beloved by nymph and God; I stood with thee in proud delight On Mandar's side and Meru's height; With thee, my lord, enchanted strayed In Chaitraratha's1013 lovely shade, And viewed each fairest scene afar Transported in thy radiant car. But source of every joy wast thou, And all my bliss is ended now.” Then Ráma to VibhishaG cried: “Whate'er the ritual bids, provide. Obsequial honours duly pay, And these sad mourners' grief allay.” VibhishaG answered, wise and true, For duty's changeless law he knew: “Nay one who scorned all sacred vows And dared to touch another's spouse, Fell tyrant of the human race, With funeral rites I may not grace.” 1013 The garden of Kuvera, the God of Riches.
- **Translation**: 

---

### Verse 18 (Ramayan 0.1758)
- **Original**: 1740 The Ramayana Him Raghu's royal son, the best Of those who love the law, addressed: “False was the rover of the night, He loved the wrong and scorned the right. Yet for the fallen warrior plead The dauntless heart, the valorous deed. Let him who ne'er had brooked defeat, The chief whom Indra feared to meet, The ever-conquering lord, obtain The honours that should grace the slain.” VibhishaG bade his friends prepare The funeral rites with thoughtful care. Himself the royal palace sought Whence sacred fire was quickly brought, With sandal wood and precious scents And pearl and coral ornaments. Wise Bráhmans, while the tears that flowed Down their wan cheeks their sorrow sowed, Upon a golden litter laid The corpse in finest ropes arrayed. Thereon were flowers and pennons hung, And loud the monarch's praise was sung. Then was the golden litter raised, While holy fire in order blazed. And first in place VibhishaG led The slow procession of the dead, Behind, their cheeks with tears bedewed, Came sad the widowed multitude. Where, raised as Bráhmans ordered, stood Piled sandal logs, and scented wood, The body of the king was set High on a deerskin coverlet. Then duly to the monarch's shade The offerings for the dead they paid,
- **Translation**: 

---

### Verse 19 (Ramayan 0.1759)
- **Original**: Canto CXIV. Vibhishan Consecrated. 1741 And southward on the eastern side An altar formed and fire supplied. Then on the shoulder of the dead The oil and clotted milk were shed. All rites were done as rules ordain: The sacrificial goat was slain. Next on the corpse were perfumes thrown And many a flowery wreath was strown; And with VibhishaG's ready aid Rich vesture o'er the king was laid. Then while the tears their cheeks bedewed Parched grain upon the dead they strewed; Last, to the wood, as rules require, VibhishaG set the kindling fire. Then having bathed, as texts ordain, To Lanká went the mourning train. VibhishaG, when his task was done, Stood by the side of Raghu's son. And Ráma, freed from every foe, Unstrung at last his deadly bow, And laid the glittering shafts aside, And mail by Indra's love supplied. Canto CXIV. Vibhishan Consecrated.
- **Translation**: 

---

### Verse 20 (Ramayan 0.1760)
- **Original**: 1742 The Ramayana Joy reigned in heaven where every eye Had seen the Lord of Lanká die. In cars whose sheen surpassed the sun's Triumphant rode the radiant ones: And RávaG's death, by every tongue, And Ráma's glorious deeds were sung. They praised the Vánars true and brave, The counsel wise Sugríva gave. The deeds of Hanúmán they told, The valiant chief supremely bold, The strong ally, the faithful friend, And Sítá's truth which naught could bend. To Mátali, whom Indra sent, His head the son of Raghu bent: And he with fiery steeds who clove The clouds again to Swarga drove.[494] Round King Sugríva brave and true His arms in rapture Ráma threw, Looked on the host with joy and pride, And thus to noble LakshmaG cried: “Now let king-making drops be shed, Dear brother, on VibhishaG's head For truth and friendship nobly shown, And make him lord of RávaG's throne.” This longing of his heart he told: And Lakshma G took an urn of gold And bade the wind-fleet Vánars bring Sea water for the giants' king. The brimming urn was swiftly brought: Then on a throne superbly wrought VibhishaG sat, the giants' lord, And o'er his brows the drops were poured.
- **Translation**: 

---

