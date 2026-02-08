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

### Verse 1 (Ramayana 0.1786)
- **Original**: 1768 The Ramayana Godávarí the best of streams, Whose lucid waters sweetly glide By lilies that adorn her side. There dwelt Agastya, holy sage, In plantain-sheltered hermitage. See Zarabhanga's humble shed[501] Which sovereign Indra visited. See where the gentle hermits dwell Neath Atri's rule who loved us well; Where once thine eyes were blest to see His sainted dame who talked with thee. Now rest thine eyes with new delight On Chitrakúma's woody height, See Jumna flashing in the sun Through groves of brilliant foliage run. Screened by the shade of spreading boughs. There Bharadvája keeps his vows, There Gangá, river of the skies, Rolls the sweet wave that purifies, ThereZringavera's towers ascend Where Guha reigns, mine ancient friend. I see, I see thy glittering spires, Ayodhyá, city of my sires. Bow down, bow down thy head, my sweet, Our home, our long-lost home to greet.” Canto CXXVI. Bharat Consoled.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1787)
- **Original**: Canto CXXVI. Bharat Consoled. 1769 But Ráma bade the chariot stay, And halting in his airy way, In Bharadvája's holy shade His homage to the hermit paid. “O saint,” he cried,“I yearn to know My dear Ayodhyá's weal and woe. O tell me that the people thrive, And that the queens are yet alive.” Joy gleamed in Bhardvája's eye, Who gently smiled and made reply: “Thy brother, studious of thy will, Is faithful and obedient still. In tangled twine he coils his hair: Thy safe return is all his care. Before thy shoes he humbly bends, And to thy house and realm attends. When first these dreary years began, When first I saw the banished man, With Sítá, in his hermit coat, At this sad heart compassion smote. My breast with tender pity swelled: I saw thee from thy home expelled, Reft of all princely state, forlorn, A hapless wanderer travel-worn, Firm in thy purpose to fulfil Thy duty and thy father's will. But boundless is my rapture now: Triumphant, girt with friends, art thou. Where'er thy wandering steps have been, Thy joy and woe mine eyes have seen. Thy glorious deeds to me art known, The Bráhmans saved, the foes o'erthrown. Such power have countless seasons spent
- **Translation**: 

---

### Verse 3 (Ramayana 0.1788)
- **Original**: 1770 The Ramayana In penance and devotion lent. Thy virtues, best of chiefs, I know, And now a boon would fain bestow. This hospitable gift1024 receive: Then with the dawn my dwelling leave.” The bended head of Ráma showed His reverence for the grace bestowed; Then for each brave companion's sake He sought a further boon and spake: “O let that mighty power of thine The road to fair Ayodhyá line With trees where fruit of every hue The Vánars' eye and taste may woo, And flowers of every season, sweet With stores of honeyed juice, may meet.” The hero ceased: the hermit bent His reverend head in glad assent; And swift, as Bharadvája willed, The prayer of Ráma was fulfilled. For many a league the lengthening road Trees thick with fruit and blossom showed With luscious beauty to entice The taste like trees of Paradise. The Vánars passed beneath the shade Of that delightful colonnade, Still tasting with unbounded glee The treasures of each wondrous tree. 1024 The arghya, a respectful offering to Gods and venerable men consisting of rice, dúivá grass, flowers etc., with water.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1789)
- **Original**: Canto CXXVII. Ráma's Message. 1771 Canto CXXVII. Ráma's Message. But Ráma, when he first looked down And saw afar Ayodhyá's town, Had called Hanumán to his side, The chief on whom his heart relied, And said:“Brave Vánar, good at need, Haste onward, to Ayodhyá speed, And learn, I pray, if all be well With those who in the palace dwell. But as thou speedest on thy way Awhile atZringavera stay. Tell Guha the Nishádas' lord, That victor, with my queen restored, In health and strength with many a friend Homeward again my steps I bend. Thence by the road that he will show On to Ayodhyá swiftly go. There with my love my brother greet, And all our wondrous tale repeat. Say that victorious in the strife I come with LakshmaG and my wife, Then mark with keenest eye each trace Of joy or grief on Bharat's face. Be all his gestures closely viewed, [502] Each change of look and attitude. Where breathes the man who will not cling To all that glorifies a king? Where beats the heart that can resign An ancient kingdom, nor repine To lose a land renowned for breeds Of elephants and warrior steeds? If, won by custom day by day, My brother Bharat thirsts for sway,
- **Translation**: 

---

### Verse 5 (Ramayana 0.1790)
- **Original**: 1772 The Ramayana Still let him rule the nations, still The throne of old Ikshváku fill. Go, mark him well: his feelings learn, And, ere we yet be near return.” He ceased: and, garbed in human form, Forth sped Hanúmán swift as storm. Sublime in air he rose, and through The region of his father flew. He saw far far beneath his feet Where Gangá's flood and Jumna meet. Descending from the upper air He enteredZringavera, where King Guha's heart was well content To hear the message Ráma sent. Then, with his mighty strength renewed, The Vánar chief his way pursued, Válúkiní was far behind, And Gomatí with forests lined, And golden fields and pastures gay With flocks and herds beneath him lay. Then Nandigráma charmed his eye Where flowers were bright with every dye, And trees of lovely foliage made With meeting boughs delightful shade, Where women watched in trim array Their little sons' and grandsons' play. His eager eye on Bharat fell Who sat before his lonely cell. In hermit weed, with tangled hair, Pale, weak, and worn with ceaseless care. His royal pomp and state resigned For Ráma still he watched and pined, Still to his dreary vows adhered,
- **Translation**: 

---

### Verse 6 (Ramayana 0.1791)
- **Original**: Canto CXXVII. Ráma's Message. 1773 And royal Ráma's shoes revered. Yet still the terror of his arm Preserved the land from fear and harm. The Wind-God's son, in form a man, Raised reverent hands and thus began: “Fond greeting, Prince, I bring to thee, And Ráma's self has sent it: he For whom thy spirit sorrows yet As for a hapless anchoret In DaG ak wood, in dire distress, With matted hair and hermit dress. This sorrow from thy bosom fling, And hear the tale of joy I bring. This day thy brother shalt thou meet Exulting in his foe's defeat, Freed from his toil and lengthened vow, The light of victory on his brow, With Sítá, LakshmaG and his friends Homeward at last his steps he bends.” Then joy, too mighty for control, Rushed in full flood o'er Bharat's soul; His reeling sense and strength gave way, And fainting on the earth he lay, At length upspringing from the ground, His arms about Hanúmán wound, With tender tears of rapture sprung, He dewed the neck to which he clung: “Art thou a God or man,” he cried, “Whom love and pity hither guide? For this a hundred thousand kine, A hundred villages be thine. A score of maids of spotless lives
- **Translation**: 

---

### Verse 7 (Ramayana 0.1792)
- **Original**: 1774 The Ramayana To thee I give to be thy wives, Of golden hue and bright of face, Each lovely for her tender grace.” He ceased a while by joy subdued, And then his eager speech renewed. Canto CXXVIII. Hanumán's Story. “In doubt and fear long years have passed And glorious tidings come at last. True, true is now the ancient verse Which men in time of bliss rehearse: “Once only in a hundred years Great joy to mortal men appears.” But now his woes and triumph tell, And loss and gain as each befell.” He ceased: Hanúmán mighty-souled The tale of Ráma's wanderings told From that first day on which he stood In the drear shade of DaG ak wood. He told how fierce Virádha fell; He told ofZarabhanga's cell Where Ráma saw with wondering eyes Indra descended from the skies. He told howZúrpaGakhí came, Her soul aglow with amorous flame, And fled repulsed, with rage and tears, Reft of her nose and severed ears. He told how Ráma's might subdued The giants' furious multitude;
- **Translation**: 

---

### Verse 8 (Ramayana 0.1793)
- **Original**: Canto CXXIX. The Meeting With Bharat. 1775 How Khara with the troops he led And Tri[irás and DúshaG bled: How Ráma, tempted from his cot, The golden deer pursued and shot, And RávaG came and stole away The Maithil queen his hapless prey, When, as he fought, the dame to save, His noble life Jatáyus gave: How Ráma still the the search renewed, The robber to his hold pursued, Bridging the sea from shore to shore, And found his queen to part no more.1025 [503] Canto CXXIX. The Meeting With Bharat. O'erwhelmed with rapture Bharat heard The tale that all his being stirred, And, heralding the glad event, This order toZatrughna sent: “Let every shrine with flowers be gay Let incense burn and music play. Go forth, go forth to meet your king, Let tabours sound and minstrels sing, Let bards swell high the note of praise Skilled in the lore of ancient days, Call forth the royal matrons: call Each noble from the council hall. 1025 I have abridged Hanumán's outline of Ráma's adventures, with the details of which we are already sufficiently acquainted.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1794)
- **Original**: 1776 The Ramayana Send all we love and honour most, Send Bráhmans and the warrior host, A glorious company to bring In triumph home our lord the king.” Great rapture filledZatrughna's breast, Obedient to his brother's hest. “Send forth ten thousand men” he cried, “Let brawny arms be stoutly plied, And, smoothing all with skilful care, The road for Ko[al's king prepare. Then o'er the earth let thousands throw Fresh showers of water cool as snow, And others strew with garlands gay With loveliest blooms our monarch's way. On tower and temple porch and gate Let banners wave in royal state, And be each roof and terrace lined With blossoms loose and chaplets twined.” The nobles hasting forth fulfilled His order asZatrughna willed. Sublime on elephants they rode Whose gilded girths with jewels glowed. Attended close by thousands more Gay with the gear and flags they bore. A thousand chiefs their steeds bestrode, Their glittering cars a thousand showed. And countless hosts in rich array Pursued on foot their eager way. Veiled from the air with silken screens In litters rode the widowed queens. Kausalyá first, acknowledged head And sovereign of the household, led:
- **Translation**: 

---

### Verse 10 (Ramayana 0.1795)
- **Original**: Canto CXXIX. The Meeting With Bharat. 1777 Sumitrá next, and after, dames Of lower rank and humbler names. Then compassed by a white-robed throng Of Bráhmans, heralded with song, With shouts of joy from countless throats, And shells' and tambours' mingled notes, And drums resounding long and loud, Exulting Bharat joined the crowd. Still on his head, well-trained in lore Of duty, Ráma's shoes he bore. The moon-white canopy was spread With flowery twine engarlanded, And jewelled cheuries, meet to hold O'er Ráma's brow, shone bright with gold, Though Nandigráma's town they neared, Of Ráma yet no sign appeared. Then Bharat called the Vánar chief And questioned thus in doubt and grief: “Hast thou uncertain, like thy kind, A sweet delusive guile designed? Where, where is royal Ráma? show The hero, victor of the foe. I gaze, but see no Vánars still Who wear each varied shape at will.” In eager love thus Bharat cried, And thus the Wind-God's son replied: “Look, Bharat, on those laden trees That murmur with the song of bees; For Ráma's sake the saint has made Untimely fruits, unwonted shade. Such power in ages long ago Could Indra's gracious boon bestow. O, hear the Vánars' voices, hear
- **Translation**: 

---

### Verse 11 (Ramayana 0.1796)
- **Original**: 1778 The Ramayana The shouting which proclaims them near. E'en now about to cross they seem Sweet Gomatí's delightful stream. I see, I see the car designed By Brahmá's own creative mind, The car which, radiant as the moon, Moves at the will by Brahmá's boon; The car which once was Rávan's pride, The victor's spoil when Rávan died. Look, there are Raghu's sons: between The brothers stands the rescued queen. There is VibhishaG full in view, Sugríva and his retinue.” He ceased: then rapture loosed each tongue: From men and dames, from old and young, One long, one universal cry, 'Tis he, 'tis Ráma, smote the sky. All lighted down with eager speed From elephant and car and steed, And every joyful eye intent On Ráma's moonbright face was bent. Entranced a moment Bharat gazed: Then reverential hands he raised, And on his brother humbly pressed The honours due to welcome guest. Then Bharat clomb the car to greet His king and bowed him at his feet, Till Ráma raised him face to face And held him in a close embrace. Then LakshmaG and the Maithil dame He greeted as he spoke his name1026 1026 In these respectful salutations the person who salutes his superior mentions his own name even when it is well known to the person whom he salutes.
- **Translation**: 

---

### Verse 12 (Ramayana 0.1797)
- **Original**: Canto CXXIX. The Meeting With Bharat. 1779 He greeted next, supreme in place, The sovereign of the Vánar race, And Jámbaván and Báli's son, [504] And lords and chiefs, omitting none.1027 Sugríva to his heart he pressed And thus with grateful words addressed: “Four brothers, Vánar king, were we, And now we boast a fifth in thee. By kindly acts a friend we know: Offence and wrong proclaim the foe.” To King VibhishaG then he spake: “Well hast thou fought for Ráma's sake.” Nor was the braveZatrughna slow His reverential love to show To both his brothers, as was meet, And venerate the lady's feet. Then Ráma to his mother came, Saw her pale cheek and wasted frame, With gentle words her heart consoled, And clasped her feet with loving hold. Then at Sumitrá's feet he bent, And fair Kaikeyí's, reverent, Greeted each dame from chief to least, And bowed him to the household priest. Up rose a shout from all the throng: “O welcome, Ráma, mourned so long. Welcome, Kausalyá's joy and pride,” Ten hundred thousand voices cried. Then Bharat placed, in duty taught, On Ráma's feet the shoes he brought: “My King,” he cried,“receive again 1027 I have omitted the chieftains' names as they could not be introduced without padding. They are Mainda, Dwivid, Níla, Rishabh, SusheG, Nala, Gaváksha, Gandhamádan, Zarabh, and Panas.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1798)
- **Original**: 1780 The Ramayana The pledge preserved through years of pain, The rule and lordship of the land Entrusted to my weaker hand. No more I sigh o'er sorrows past, My birth and life are blest at last In the glad sight this day has shown, When Ráma comes to rule his own.” He ceased: the faithful love that moved The prince's soul each heart approved; Nor could the Vánar chiefs refrain From tender tears that fell like rain. Then Ráma, stirred with joy anew, His arms about his brother threw, And to the grove his course he bent Where Bharat's hermit days were spent. Alighting in that pure retreat He pressed the earth with eager feet. Then, at his hest, the car rose high And sailing through the northern sky Sped homeward to the Lord of Gold Who owned the wondrous prize of old.1028 Canto CXXX. The Consecration. 1028 The following addition is found in the Bengal recension: But Vai[ravaG (Kuvera) when he beheld his chariot said unto it:“Go, and carry Ráma, and come unto me when my thought shall call thee, And the chariot returned unto Ráma;” and he honoured it when he had heard what had passed.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1799)
- **Original**: Canto CXXX. The Consecration. 1781 Then, reverent hand to hand applied, Thus Bharat to his brother cried: “Thy realm, O King, is now restored, Uninjured to the rightful lord. This feeble arm with toil and pain, The weighty charge could scarce sustain. And the great burthen wellnigh broke The neck untrained to bear the yoke. The royal swan outspeeds the crow: The steed is swift, the mule is slow, Nor can my feeble feet be led O'er the rough ways where thine should tread. Now grant what all thy subjects ask: Begin, O King, thy royal task. Now let our longing eyes behold The glorious rite ordained of old, And on the new-found monarch's head Let consecrating drops be shed.” He ceased; victorious Ráma bent His head in token of assent. He sat, and tonsors trimmed with care His tangles of neglected hair Then, duly bathed, the hero shone With all his splendid raiment on. And Sítá with the matrons' aid Her limbs in shining robes arrayed, Sumantra then, the charioteer, Drew, ordered byZatrughna near, And stayed within the hermit grove The chariot and the steeds he drove. Therein Sugríva's consorts, graced With gems, and Ráma's queen were placed, All fain Ayodhyá to behold:
- **Translation**: 

---

### Verse 15 (Ramayana 0.1800)
- **Original**: 1782 The Ramayana And swift away the chariot rolled. Like Indra Lord of Thousand Eyes, Drawn by fleet lions through the skies. Thus radiant in his glory showed King Ráma as he homeward rode, In power and might unparalleled. The reins the hand of Bharat held. Above the peerless victor's head The snow-white shadeZatrughna spread, And Lakshma G's ever-ready hand His forehead with a chourie fanned. VibhishaG close to LakshmaG's side Sharing his task a chourie plied. Sugríva onZatrunjay came, An elephant of hugest frame: Nine thousand others bore, behind, The chieftains of the Vánar kind All gay, in forms of human mould, With rich attire and gems and gold.[505] Thus borne along in royal state King Ráma reached Ayodbyá's gate With merry noise of shells and drums And joyful shouts, He comes, he comes, A Bráhman host with solemn tread, And kine the long procession led, And happy maids in ordered bands Threw grain and gold with liberal hands. Neath gorgeous flags that waved in rows On towers and roofs and porticoes. Mid merry crowds who sang and cheered The palace of the king they neared. Then Raghu's son to Bharat, best Of duty's slaves, these words addressed: “Pass onward to the monarch's hall.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1801)
- **Original**: Canto CXXX. The Consecration. 1783 The high-souled Vánars with thee call, And let the chieftains, as is meet, The widows of our father greet. And to the Vánar king assign Those chambers, best of all, which shine With lazulite and pearl inlaid, And pleasant grounds with flowers and shade.” He ceased: and Bharat bent his head; Sugríva by the hand he led And passed within the palace where Stood couches whichZatrughna's care, With robes and hangings richly dyed, And burning lamps, had seen supplied. Then Bharat spake:“I pray thee, friend, Thy speedy messengers to send, Each sacred requisite to bring That we may consecrate our king.” Sugríva raised four urns of gold, The water for the rite to hold, And bade four swiftest Vánars flee And fill them from each distant sea. Then east and west and south and north The Vánar envoys hastened forth. Each in swift flight an ocean sought And back through air his treasure brought, And full five hundred floods beside Pure water for the king supplied. Then girt by many a Bráhman sage, Va [ishmha, chief for reverend age, High on a throne with jewels graced King Ráma and his Sítá placed. There by Jábáli, far revered, Vijay and Ka[yap's son appeared;
- **Translation**: 

---

### Verse 17 (Ramayana 0.1802)
- **Original**: 1784 The Ramayana By Gautam's side Kátváyan stood, And Vámadeva wise and good, Whose holy hands in order shed The pure sweet drops on Ráma's head. Then priests and maids and warriors, all Approaching at Va[ishmha's call, With sacred drops bedewed their king, The centre of a joyous ring, The guardians of the worlds, on high, And all the children of the sky From herbs wherewith their hands were filled Rare juices on his brow distilled. His brows were bound with glistering gold Which Manu's self had worn of old, Bright with the flash of many a gem His sire's ancestral diadem. Zatrughna lent his willing aid And o'er him held the regal shade: The monarchs whom his arm had saved The chouries round his forehead waved. A golden chain, that flashed and glowed With gems the God of Wind bestowed: Mahendra gave a glorious string Of fairest pearls to deck the king, The skies with acclamation rang, The gay nymphs danced, the minstrels sang. On that blest day the joyful plain Was clothed anew with golden grain. The trees the witching influence knew, And bent with fruits of loveliest hue, And Ráma's consecration lent New sweetness to each flowret's scent. The monarch, joy of Raghu's line, Gave largess to the Bráhmans, kine
- **Translation**: 

---

### Verse 18 (Ramayana 0.1803)
- **Original**: Canto CXXX. The Consecration. 1785 And steeds unnumbered, wealth untold Of robes and pearls and gems and gold. A jewelled chain, whose lustre passed The glory of the sun, he cast About his friend Sugríva's neck; And, Angad Báli's son to deck, He gave a pair of armlets bright With diamond and lazulite. A string of pearls of matchless hue Which gleams like tender moonlight threw Adorned with gems of brightest sheen, He gave to grace his darling queen. The offering from his hand received A moment on her bosom heaved; Then from her neck the chain she drew, A glance on all the Vánars threw, And wistful eyes on Ráma bent As still she held the ornament. Her wish he knew, and made reply To that mute question of her eye: “Yea, love; the chain on him bestow Whose wisdom truth and might we know, The firm ally, the faithful friend Through toil and peril to the end.” Then on Hanúmán's bosom hung The chain which Sítá's hand had flung: So may a cloud, when winds are still With moon-lit silver gird a hill.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1804)
- **Original**: 1786 The Ramayana To every Vánar Ráma gave Rich treasures from the mine and wave. And with their honours well content Homeward their steps the chieftains bent. Ten thousand years Ayodhyá, blest With Ráma's rule, had peace and rest, No widow mourned her murdered mate, No house was ever desolate. The happy land no murrain knew, The flocks and herds increased and grew.[506] The earth her kindly fruits supplied, No harvest failed, no children died. Unknown were want, disease, and crime: So calm, so happy was the time.1029 [507] 1029 Here follows in the original an enumeration of the chief blessings which will attend the man or woman who reads or hears read this tale of Ráma. These blessings are briefly mentioned at the end of the first Canto of the first book, and it appears unnecessary to repeat them here in their amplified form. The Bengal recension (Gorresio's edition) gives them more concisely as follows: “This is the great first poem blessed and glorious, which gives long life to men and victory to kings, the poem which Válmíki made. He who listens to this wondrous tale of Ráma unwearied in action shall be absolved from all his sins. By listening to the deeds of Ráma he who wishes for sons shall obtain his heart's desire, and to him who longs for riches shall riches be given. The virgin who asks for a husband shall obtain a husband suited to her mind, and shall meet again her dear kinsfolk who are far away. They who hear this poem which Válmíki made shall obtain all their desires and all their prayers shall be fulfilled.”
- **Translation**: 

---

### Verse 20 (Ramayana 0.1805)
- **Original**: APPENDIX. Section XIII. Rávan Doomed. Afterwards Rishya[ring said again to the King“I will perform another sacrificial act to secure thee a son.” Then the son of VibháGdak, of subdued passions, seeking the happiness of the king, proceeded to perform the sacrifice for the accomplishment of his wishes. Hither were previously collected the gods, with the Gandharvas, the Siddhas and the sages, for the sake of receiving their respective shares, Brahmá too, the sovereign of the gods, with StháGu, and NáráyaGa, chief of beings and the four support- ers of the universe, and the divine mothers of all the celestials, met together there. To the A[vamedha, the great sacrifice of the magnanimous monarch, came also Indra the glorious one, surrounded by the Maruts. Rishya[ring then supplicated the gods assembled for their share of the sacrifice (saying),“This devout king Da[aratha, who, through the desire of offspring, confiding in you, has performed sacred austerities, and who has offered to you the sacrifice called A[vamedha, is about to perform another sacrifice for the sake of obtaining sons: To him thus desirous of offspring be pleased to grant the blessing: I supplicate you all with joined hands. May he have four sons, renowned through the universe.” The gods replied to the sage's son supplicating with joined hands,“Be it so: thou, O Bráhman, art ever to be regarded by us, as the king is in a peculiar manner. The lord of men by this sacrifice shall obtain the great object of his desires.” Having thus said, the gods preceded by Indra, disappeared.
- **Translation**: 

---

