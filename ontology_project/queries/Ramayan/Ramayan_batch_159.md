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

### Verse 1 (Ramayana 0.1206)
- **Original**: 1188 The Ramayana Beheld me come with one to aid: Then shrinking from unequal fight, He turned his back in swiftest flight. From vengeful foes his life to save He sought the refuge of a cave. Then when I saw the fiend had fled Within that cavern dark and dread, Thus to my brother cruel-eyed, Impatient in my wrath, I cried: “I seek no more my royal town Till I have struck the demon down. Here by the cavern's mouth remain Until my hand the foe have slain.” Upon his faith my heart relied, And swift within the depths I hied. A year went by: in every spot I sought the fiend, but found him not. At length my foe I saw and slew, Whom long I feared when lost to view; And all his kinsmen by his side Beneath my vengeful fury died. The monster, as he reeled and fell, Poured forth his blood with roar and yell; And, filling all the cavern, dyed The portal with the crimson tide. Upon my foeman slain at last One look, one pitying look, I cast. I sought again the light of day: The cave was closed and left no way. To the barred mouth I sadly came, And called aloud Sugríva's name. But all was still: no voice replied,[335] And hope within my bosom died. With furious efforts, vain at first,
- **Translation**: 

---

### Verse 2 (Ramayana 0.1207)
- **Original**: Canto X. Sugríva's Story. 1189 Through bars of rock my way I burst. Then, free once more, the path that brought My feet in safety home I sought. 'Twas thus Sugríva dared despise The claim of brothers' friendly ties. With crags of rock he barred me in, And for himself the realm would win.” Thus Báli spoke in words severe; And then, unmoved by ruth or fear, Left me a single robe and sent His brother forth in banishment. He cast me out with scathe and scorn, And from my side my wife was torn. Now in great fear and ill at ease I roam this land with woods and seas, Or dwell on Rishyamúka's hill, And sorrow for my consort still. Thou hast the tale how first arose This bitter hate of brother foes. Such are the griefs neath which I pine, And all without a fault of mine. O swift to save in hour of fear, My prayer who dread this Báli, hear With gracious love assistance deign, And mine oppressor's arm restrain.” Then Raghu's son, the good and brave, With a gay laugh his answer gave: “These shafts of mine which ne'er can fail, Before whose sheen the sun grows pale, Winged by my fury, fleet and fierce, The wicked Báli's heart shall pierce. Yea, mark the words I speak, so long
- **Translation**: 

---

### Verse 3 (Ramayana 0.1208)
- **Original**: 1190 The Ramayana Shall live that wretch who joys in wrong, Until these angered eyes have seen The robber of thy darling queen. I, taught by equal suffering, know What waves of grief above thee flow. This hand thy captive wife shall free, And give thy kingdom back to thee.” Sugríva joyed as Ráma spoke, And valour in his breast awoke. His eye grew bright, his heart grew bold, And thus his wondrous tale he told: Canto XI. Dundubhi. “I doubt not, Prince, thy peerless might, Armed with these shafts so keen and bright, Like all-destroying fires of fate, The worlds could burn and devastate. But lend thou first thy mind and ear Of Báli's power and might to hear. How bold, how firm, in battle tried, Is Báli's heart; and then decide. From east to west, from south to north On restless errand hurrying forth, From farthest sea to sea he flies Before the sun has lit the skies. A mountain top he oft will seek, Tear from its root a towering peak, Hurl it aloft, as 'twere a ball, And catch it ere to earth it fall.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1209)
- **Original**: Canto XI. Dundubhi. 1191 And many a tree that long has stood In health and vigour in the wood, His single arm to earth will throw, The marvels of his might to show. Shaped like a bull, a monster bore The name of Dundubhi of yore: He matched in size a mountain height, A thousand elephants in might. By pride of wondrous gifts impelled, And strength he deemed unparalleled, To Ocean, lord of stream and brook, Athirst for war, his way he took. He reached the king of rolling waves Whose gems are piled in sunless caves, And threw his challenge to the sea; “Come forth, O King, and fight with me.” He spoke, and from his ocean bed The righteous567 monarch heaved his head, And gave, sedate, his calm reply To him whom fate impelled to die: “Not mine, not mine the power,” he cried, “To cope with thee in battle tried; But listen to my voice, and seek The worthier foe of whom I speak. The Lord of Hills, where hermits live And love the home his forests give, Whose child isZankar's darling queen,568 The King of Snows is he I mean. Deep caves has he, and dark boughs shade 567 Righteous because he never transgresses his bounds, and “over his great tides Fidelity presides.” 568 Himálaya, the Lord of Snow, is the father of Umá the wife ofZiva orZankar.
- **Translation**: 

---

### Verse 5 (Ramayana 0.1210)
- **Original**: 1192 The Ramayana The torrent and the wild cascade. From him expect the fierce delight Which heroes feel in equal fight.” He deemed that fear checked ocean's king, And, like an arrow from the string, To the wild woods that clothe the side Of Lord Himálaya's hills he hied. Then Dundubhi, with hideous roar, Huge fragments from the summit tore Vast as Airávat,569 white with snow, And hurled them to the plains below. Then like a white cloud soft, serene, The Lord of Mountains' form was seen. It sat upon a lofty crest, And thus the furious fiend addressed: “Beseems thee not, O virtue's friend, My mountain tops to rive and rend;[336] For I, the hermit's calm retreat, For deeds of war am all unmeet.” The demon's eye with rage grew red, And thus in furious tone he said: “If thou from fear or sloth decline To match thy strength in war with mine, Where shall I find a champion, say, To meet me burning for the fray?” He spoke: Himálaya, skilled in lore Of eloquence, replied once more, And, angered in his righteous mind, Addressed the chief of demon kind: “The Vánar Báli, brave and wise, 569 Indra's celestial elephant.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1211)
- **Original**: Canto XI. Dundubhi. 1193 Son of the God who rules the skies,570 Sways, glorious in his high renown, Kishkindhá his imperial town. Well may that valiant lord who knows Each art of war his might oppose To thine, in equal battle set, As Namuehi571 and Indra met. Go, if thy soul desire the fray; To Báli's city speed away, And that unconquered hero meet Whose fame is high for warlike feat.” He listened to the Lord of Snow, And, his proud heart with rage aglow, Sped swift away and lighted down By vast Kishkindhá, Báli's town. With pointed horns to strike and gore The semblance of a bull he bore, Huge as a cloud that downward bends Ere the full flood of rain descends. Impelled by pride and rage and hate, He thundered at Kishkindhá's gate; And with his bellowing, like the sound Of pealing drums, he shook the ground, He rent the earth and prostrate threw The trees that near the portal grew. King Báli from the bowers within Indignant heard the roar and din. Then, moonlike mid the stars, with all His dames he hurried to the wall; And to the fiend this speech, expressed In clear and measured words, addressed: 570 Báli was the son of Indra. See p. 28. 571 An Asur slain by Indra. See p. 261 Note. He is, like Vritra, a form of the demon of drought destroyed by the beneficent God of the firmament.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1212)
- **Original**: 1194 The Ramayana “Know me for monarch. Báli styled, Of Vánar tribes that roam the wild. Say why dost thou this gate molest, And bellowing thus disturb our rest? I know thee, mighty fiend: beware And guard thy life with wiser care.” He spoke: and thus the fiend returned, While red with rage his eyeballs burned: “What! speak when all thy dames are nigh And hero-like thy foe defy? Come, meet me in the fight this day, And learn my strength by bold assay. Or shall I spare thee, and relent Until the coming night be spent? Take then the respite of a night And yield thee to each soft delight. Then, monarch of the Vánar race With loving arms thy friends embrace. Gifts on thy faithful lords bestow, Bid each and all farewell, and go. Show in the streets once more thy face, Install thy son to fill thy place. Dally a while with each dear dame; And then my strength thy pride shall tame For, should I smite thee drunk with wine Enamoured of those dames of thine, Beneath diseases bowed and bent, Or weak, unarmed, or negligent, My deed would merit hate and scorn As his who slays the child unborn.” Then Báli's soul with rage was fired, Queen Tára and the dames retired; And slowly, with a laugh of pride, The king of Vánars thus replied:
- **Translation**: 

---

### Verse 8 (Ramayana 0.1213)
- **Original**: Canto XI. Dundubhi. 1195 “Me, fiend, thou deemest drunk with wine: Unless thy fear the fight decline, Come, meet me in the fray, and test The spirit of my valiant breast.” He spoke in wrath and high disdain; And, laying down his golden chain, Gift of his sire Mahendra, dared The demon, for the fray prepared; Seized by the horns the monster, vast As a huge hill, and held him fast, Then fiercely dragged him round and round, And, shouting, hurled him to the ground. Blood streaming from his ears, he rose, And wild with fury strove the foes. Then Báli, match for Indra's might, With every arm renewed the fight. He fought with fists, and feet, and knees, With fragments of the rock, and trees. At last the monster's strength, assailed By Zakra's572 conquering offspring, failed. Him Báli raised with mighty strain And dashed upon the ground again; Where, bruised and shattered, in a tide Of rushing blood, the demon died. King Báli saw the lifeless corse, And bending, with tremendous force Raised the huge bulk from where it lay, And hurled it full a league away. As through the air the body flew, Some blood-drops, caught by gales that blew, Welled from his shattered jaw and fell By Saint Matanga's hermit cell: 572 Another name of Indra or Mahendra.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1214)
- **Original**: 1196 The Ramayana Matanga saw, illustrious sage, Those drops defile his hermitage,[337] And, as he marvelled whence they came, Fierce anger filled his soul with flame: “Who is the villain, evil-souled, With childish thoughts unwise and bold, Who is the impious wretch,” he cried, “By whom my grove with blood is dyed?” Thus spoke Matanga in his rage, And hastened from the hermitage, When lo, before his wondering eyes Lay the dead bull of mountain size. His hermit soul was nothing slow The doer of the deed to know, And thus the Vánar in a burst Of wild tempestuous wrath he cursed: “Ne'er let that Vánar wander here, For, if he come, his death is near, Whose impious hand with blood has dyed The holy place where I abide, Who threw this demon corse and made A ruin of the pleasant shade. If e'er he plant his wicked feet Within one league of my retreat; Yea, if the villain come so nigh That very hour he needs must die. And let the Vánar lords who dwell In the dark woods that skirt my cell Obey my words, and speeding hence Find them some meeter residence. Here if they dare to stay, on all The terrors of my curse shall fall. They spoil the tender saplings, dear
- **Translation**: 

---

### Verse 10 (Ramayana 0.1215)
- **Original**: Canto XI. Dundubhi. 1197 As children which I cherish here, Mar root and branch and leaf and spray, And steal the ripening fruit away. One day I grant, no further hour, To-morrow shall my curse have power, And then each Vánar I may see A stone through countless years shall be.” The Vánars heard the curse and hied From sheltering wood and mountain side. King Báli marked their haste and dread, And to the flying leaders said: “Speak, Vánar chiefs, and tell me why From Saint Matanga's grove ye fly To gather round me: is it well With all who in those woodlands dwell?” He spoke: the Vánar leaders told King Báli with his chain of gold What curse the saint had on them laid, Which drove them from their ancient shade. Then royal Báli sought the sage, With reverent hands to soothe his rage. The holy man his suppliant spurned, And to his cell in anger turned. That curse on Báli sorely pressed, And long his conscious soul distressed. Him still the curse and terror keep Afar from Rishyamúka's steep. He dares not to the grove draw nigh, Nay scarce will hither turn his eye. We know what terrors warm him hence, And roam these woods in confidence. Look, Prince, before thee white and dry The demon's bones uncovered lie, Who, like a hill in bulk and length,
- **Translation**: 

---

### Verse 11 (Ramayana 0.1216)
- **Original**: 1198 The Ramayana Fell ruind for his pride of strength. See those high Sál trees seven in row That droop their mighty branches low, These at one grasp would Báli seize, And leafless shake the trembling trees. These tales I tell, O Prince, to show The matchless power that arms the foe. How canst thou hope to slay him? how Meet Báli in the battle now?” Sugríva spoke and sadly sighed: And Lakshma G with a laugh replied: “What show of power, what proof and test May still the doubts that fill thy breast?” He spoke. Sugríva thus replied: “See yonder Sál trees side by side. King Báli here would take his stand Grasping his bow with vigorous hand, And every arrow, keen and true, Would strike its tree and pierce it through. If Ráma now his bow will bend, And through one trunk an arrow send; Or if his arm can raise and throw Two hundred measures of his bow, Grasped by a foot and hurled through air, The demon bull that moulders there, My heart will own his might and fain Believe my foe already slain.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.1217)
- **Original**: Canto XI. Dundubhi. 1199 Sugríva spoke inflamed with ire, Scanned Ráma with a glance of fire, Pondered a while in silent mood. And thus again his speech renewed: “All lands with Báli's glories ring, A valiant, strong, and mighty king; In conscious power unused to yield, A hero first in every field. His wondrous deeds his might declare, Deeds Gods might scarcely do or dare; And on this power reflecting still I roam on Rishyamúka's hill. Awed by my brother's might I rove, In doubt and fear, from grove to grove, While Hanumán, my chosen friend, And faithful lords my steps attend; And now, O true to friendship's tie, I hail in thee my best ally. My surest refuge from my foes, And steadfast as the Lord of Snows. Still, when I muse how strong and bold Is cruel Báli, evil-souled, But ne'er, O chief of Raghu's line, Have seen what strength in war is thine, Though in my heart I may not dare Doubt thy great might, despise, compare, Thoughts of his fearful deeds will rise And fill my soul with sad surmise. Speech, form, and trust which naught may move [338] Thy secret strength and glory prove, As smouldering ashes dimly show The dormant fires that live below.”
- **Translation**: 

---

### Verse 13 (Ramayana 0.1218)
- **Original**: 1200 The Ramayana He ceased: and Ráma answered, while Played o'er his lips a gracious smile: “Not yet convinced? This clear assay Shall drive each lingering doubt away.” Thus Ráma spoke his heart to cheer, To Dundubhi's vast frame drew near: He touched it with his foot in play And sent it twenty leagues away. Sugríva marked what easy force Hurled through the air that demon's corse Whose mighty bones were white and dried, And to the son of Raghu cried: “My brother Báli, when his might Was drunk and weary from the fight, Hurled forth the monster body, fresh With skin and sinews, blood and flesh. Now flesh and blood are dried away, The crumbling bones are light as hay, Which thou, O Raghu's son, hast sent Flying through air in merriment. This test alone is weak to show If thou be stronger or the foe. By thee a heap of mouldering bone, By him the recent corse was thrown. Thy strength, O Prince, is yet untried: Come, pierce one tree: let this decide. Prepare thy ponderous bow and bring Close to thine ear the straining string. On yonder Sál tree fix thine eye, And let the mighty arrow fly, I doubt not, chief, that I shall see Thy pointed shaft transfix the tree. Then come, assay the easy task, And do for love the thing I ask.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1219)
- **Original**: Canto XII. The Palm Trees. 1201 Best of all lights, the Day-God fills With glory earth and sky: Himálaya is the lord of hills That heave their heads on high. The royal lion is the best Of beasts that tread the earth; And thou, O hero, art confessed First in heroic worth.” Canto XII. The Palm Trees. Then Ráma, that his friend might know His strength unrivalled, grasped his bow, That mighty bow the foe's dismay,— And on the string an arrow lay. Next on the tree his eye he bent, And forth the hurtling weapon went. Loosed from the matchless hero's hold, That arrow, decked with burning gold, Cleft the seven palms in line, and through The hill that rose behind them flew: Six subterranean realms it passed, And reached the lowest depth at last, Whence speeding back through earth and air It sought the quiver, and rested there.573 Upon the cloven trees amazed, The sovereign of the Vánars gazed. With all his chains and gold outspread Prostrate on earth he laid his head. 573 The Bengal recension makes it return in the form of a swan.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1220)
- **Original**: 1202 The Ramayana Then, rising, palm to palm he laid In reverent act, obeisance made, And joyously to Ráma, best Of war-trained chiefs, these words addressed: “What champion, Raghu's son, may hope With thee in deadly fight to cope, Whose arrow, leaping from the bow, Cleaves tree and hill and earth below? Scarce might the Gods, arrayed for strife By Indra's self, escape, with life Assailed by thy victorious hand: And how may Báli hope to stand? All grief and care are past away, And joyous thoughts my bosom sway, Who have in thee a friend, renowned, As VaruG574 or as Indra, found. Then on! subdue,— 'tis friendship's claim,— My foe who bears a brother's name. Strike Báli down beneath thy feet: With suppliant hands I thus entreat.” Sugríva ceased, and Ráma pressed The grateful Vánar to his breast; And thoughts of kindred feeling woke In LakshmaG's bosom, as he spoke: “On to Kishkindhá, on with speed! Thou, Vánar King, our way shalt lead, Then challenge Báli forth to fight. 574 VaruGa is one of the oldest of the Vedic Gods, corresponding in name and partly in character to thePÁ±½yÂ of the Greeks and is often regarded as the supreme deity. He upholds heaven and earth, possesses extraordinary power and wisdom, sends his messengers through both worlds, numbers the very winkings of men's eyes, punishes transgressors whom he seizes with his deadly noose, and pardons the sins of those who are penitent. In later mythology he has become the God of the sea.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1221)
- **Original**: Canto XII. The Palm Trees. 1203 Thy foe who scorns a brother's right.” They sought Kishkindhá's gate and stood Concealed by trees in densest wood, Sugríva, to the fight addressed, More closely drew his cinctured vest, And raised a wild sky-piercing shout [339] To call the foeman Báli out. Forth came impetuous Báli, stirred To fury by the shout he heard. So the great sun, ere night has ceased, Springs up impatient to the east. Then fierce and wild the conflict raged As hand to hand the foes engaged, As though in battle mid the stars Fought Mercury and fiery Mars.575 To highest pitch of frenzy wrought With fists like thunderbolts they fought, While near them Ráma took his stand, And viewed the battle, bow in hand. Alike they stood in form and might, Like heavenly A[vins576 paired in fight, Nor might the son of Raghu know Where fought the friend and where the foe; 575 Budha, not to be confounded with the great reformer Buddha, is the son of Soma or the Moon, and regent of the planet Mercury. Angára is the regent of Mars who is called the red or the fiery planet. The encounter between Michael and Satan is similarly said to have been as if “Two planets rushing from aspect malign Of fiercest opposition in midsky Should combat, and their jarring spheres compound.” Paradise Lost.Book VI. 576 The A[vins or Heavenly Twins, the Dioskuri or Castor and Pollux of the Hindus, have frequently been mentioned. See p. 36, Note.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1222)
- **Original**: 1204 The Ramayana So, while his bow was ready bent, No life-destroying shaft he sent. Crushed down by Báli's mightier stroke Sugríva's force now sank and broke, Who, hoping naught from Ráma's aid, To Rishyamúka fled dismayed, Weary, and faint, and wounded sore, His body bruised and dyed with gore, From Báli's blows, in rage and dread, Afar to sheltering woods he fled. Nor Báli farther dared pursue, The curbing curse too well he knew. “Fled from thy death!” the victor cried, And home the mighty warrior hied. Hanúmán, LakshmaG, Raghu's son Beheld the conquered Vánar run, And followed to the sheltering shade Where yet Sugríva stood dismayed. Near and more near the chieftains came, Then, for intolerable shame, Not daring yet to lift his eyes, Sugríva spoke with burning sighs: “Thy matchless strength I first beheld, And dared my foe, by thee impelled. Why hast thou tried me with deceit And urged me to a sure defeat? Thou shouldst have said,“I will not slay Thy foeman in the coming fray.” For had I then thy purpose known I had not waged the fight alone.”
- **Translation**: 

---

### Verse 18 (Ramayana 0.1223)
- **Original**: Canto XII. The Palm Trees. 1205 The Vánar sovereign, lofty-souled, In plaintive voice his sorrows told. Then Ráma spake:“Sugríva, list, All anger from thy heart dismissed, And I will tell the cause that stayed Mine arrow, and withheld the aid. In dress, adornment, port, and height, In splendour, battle-shout, and might, No shade of difference could I see Between thy foe, O King, and thee. So like was each, I stood at gaze, My senses lost in wildering maze, Nor loosened from my straining bow A deadly arrow at the foe, Lest in my doubt the shaft should send To sudden death our surest friend. O, if this hand in heedless guilt And rash resolve thy blood had spilt, Through every land, O Vánar King, My wild and foolish act would ring. Sore weight of sin on him must lie By whom a friend is made to die; And Lakshma G, I, and Sítá, best Of dames, on thy protection rest. On, warrior! for the fight prepare; Nor fear again thy foe to dare. Within one hour thine eye shall view My arrow strike thy foeman through; Shall see the stricken Báli lie Low on the earth, and gasp and die. But come, a badge about thee bind, O monarch of the Vánar kind, That in the battle shock mine eyes The friend and foe may recognize.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1224)
- **Original**: 1206 The Ramayana Come, LakshmaG, let that creeper deck With brightest bloom Sugríva's neck, And be a happy token, twined Around the chief of lofty mind.” Upon the mountain slope there grew A threading creeper fair to view, And Lakshma G plucked the bloom and round Sugríva's neck a garland wound. Graced with the flowery wreath he wore, The Vánar chief the semblance bore Of a dark cloud at close of day Engarlanded with cranes at play, In glorious light the Vánar glowed As by his comrade's side he strode, And, still on Ráma's word intent, His steps to great Kishkindhá bent. [340] Canto XIII. The Return To Kishkindhá. Thus with Sugríva, from the side Of Rishyamúka, Ráma hied, And stood before Kishkindhá's gate Where Báli kept his regal state. The hero in his warrior hold Raised his great bow adorned with gold, And drew his pointed arrow bright As sunbeams, finisher of fight. Strong-necked Sugríva led the way With LakshmaG mighty in the fray.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1225)
- **Original**: Canto XIII. The Return To Kishkindhá. 1207 Nala and Níla came behind With Hanumán of lofty mind, And valiant Tára, last in place, A leader of the Vánar race. They gazed on many a tree that showed The glory of its pendent load, And brook and limpid rill that made Sweet murmurs as they seaward strayed. They looked on caverns dark and deep, On bower and glen and mountain steep, And saw the opening lotus stud With roseate cup the crystal flood, While crane and swan and coot and drake Made pleasant music on the lake, And from the reedy bank was heard The note of many a happy bird. In open lawns, in tangled ways, They saw the tall deer stand at gaze, Or marked them free and fearless roam, Fed with sweet grass, their woodland home. At times two flashing tusks between The wavings of the wood were seen, And some mad elephant, alone, Like a huge moving hill, was shown. And scarcely less in size appeared Great monkeys all with dust besmeared. And various birds that roam the skies, And silvan creatures, met their eyes, As through the wood the chieftains sped, And followed where Sugríva led. Then Ráma, as their way they made, Saw near at hand a lovely shade, And, as he gazed upon the trees,
- **Translation**: 

---

