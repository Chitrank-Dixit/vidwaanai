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

### Verse 1 (Ramayan 0.1781)
- **Original**: Canto CXXIII. The Magic Car. 1763 I long to see my fatherland. Far is Ayodhyá: long, alas, The dreary road and hard to pass.” “One day,” VibhishaG cried,“one day Shall bear thee o'er that length of way. Is not the wondrous chariot mine, Named Pushpak, wrought by hands divine. The prize which RávaG seized of old Victorious o'er the God of Gold? This chariot, kept with utmost care, Will waft thee through the fields of air, And thou shalt light unwearied down In fair Ayodhyá's royal town. But yet if aught that I have done Has pleased thee well, O Raghu's son; If still thou carest for thy friend, Some little time in Lanká spend; There after toil of battle rest Within my halls an honoured guest.” Again the son of Raghu spake: “Thy life was perilled for my sake. Thy counsel gave me priceless aid: All honours have been richly paid. Scarce can my love refuse, O best Of giant kind, thy last request. But still I yearn once more to see My home and all most dear to me; Nor can I brook one hour's delay: Forgive me, speed me on my way.” He ceased: the magic car was brought. Of yore by Vi[vakarmá wrought. In sunlike sheen it flashed and blazed; And Raghu's sons in wonder gazed.
- **Translation**: 

---

### Verse 2 (Ramayan 0.1782)
- **Original**: 1764 The Ramayana Canto CXXIV. The Departure. The giant lord the chariot viewed, And humbly thus his speech renewed: “Behold, O King, the car prepared: Now be thy further will declared.” He ceased: and Ráma spake once more: “These hosts who thronged to Lanká's shore Their faith and might have nobly shown, And set thee on the giants' throne. Let pearls and gems and gold repay The feats of many a desperate day, That all may go triumphant hence Proud of their noble recompense.” VibhishaG, ready at his call, With gold and gems enriched them all. Then Ráma clomb the glorious car That shone like day's resplendent star. There in his lap he held his dame Vailing her eyes in modest shame. Beside him LakshmaG took his stand, Whose mighty bow still armed his hand, “O King VibhishaG,” Ráma cried, “O Vánar chiefs, so long allied,[500] My comrades till the foemen fell, List, for I speak a long farewell. The task, in doubt and fear begun, With your good aid is nobly done. Leave Lanká's shore, your steps retrace, Brave warriors of the Vánar race. Thou, King Sugríva, true, through all, To friendship's bond and duty's call, Seek far Kishkindhá with thy train And o'er thy realm in glory reign.
- **Translation**: 

---

### Verse 3 (Ramayan 0.1783)
- **Original**: Canto CXXIV. The Departure. 1765 Farewell, VibhishaG, Lanká's throne Won by our arms is now thine own, Thou, mighty lord, hast nought to dread From heavenly Gods by Indra led. My last farewell, 0 King, receive, For Lanká's isle this hour I leave.” Loud rose their cry in answer:“We, O Raghu's son, would go with thee. With thee delighted would we stray Where sweet Ayodhyá's groves are gay, Then in the joyous synod view King-making balm thy brows bedew; Our homage to Kau[alyá pay, And hasten on our homeward way.” Their prayer the son of Raghu heard, And spoke, his heart with rapture stirred: “Sugríva, O my faithful friend, VibhishaG and ye chiefs, ascend. A joy beyond all joys the best Will fill my overflowing breast, If girt by you, O noble band, I seek again my native land.” With Vánar lords in danger tried Sugríva sprang to Ráma's side, And girt by chiefs of giant kind Vibhíshan's step was close behind. Swift through the air, as Ráma chose, The wondrous car from earth arose. And decked with swans and silver wings Bore through the clouds its freight of kings.
- **Translation**: 

---

### Verse 4 (Ramayan 0.1784)
- **Original**: 1766 The Ramayana Canto CXXV. The Return. Then Ráma, speeding through the skies, Bent on the earth his eager eyes: “Look, Sítá, see, divinely planned And built by Vi[vakarmá's hand, Lanká the lovely city rest Enthroned on Mount Trikúma's crest Behold those fields, ensanguined yet, Where Vánar hosts and giants met. There, vainly screened by charm and spell, The robber Rávan fought and fell. There knelt Mandodarí1021 and shed Her tears in floods for Rávan dead. And every dame who loved him sent From her sad heart her wild lament. There gleams the margin of the deep, Where, worn with toil, we sank to sleep. Look, love, the unconquered sea behold, King VaruG's home ordained of old, Whose boundless waters roar and swell Rich with their store of pearl and shell. O see, the morning sun is bright On fair HiraGyanábha's1022 height, Who rose from Ocean's sheltering breast That Hanumán might stay and rest. There stretches, famed for evermore, The wondrous bridge from shore to shore. The worlds, to life's remotest day, Due reverence to the work shall pay, Which holier for the lapse of time 1021 RávaG's queen. 1022 Or Maináka.
- **Translation**: 

---

### Verse 5 (Ramayan 0.1785)
- **Original**: Canto CXXV. The Return. 1767 Shall give release from sin and crime. Now thither bend, dear love, thine eyes Where green with groves Kishkindhá lies, The seat of King Sugríva's reign, Where Báli by this hand was slain.1023 There Ríshyamúka's hill behold Bright gleaming with embedded gold. There too my wandering foot I set, There King Sugríva first I met. And, where yon trees their branches wave, My promise of assistance gave. There, flushed with lilies, Pampá shines With banks which greenest foliage lines, Where melancholy steps I bent And mourned thee with a mad lament. There fierce Kabandha, spreading wide His giant arms, in battle died. Turn, Sítá, turn thine eyes and see In Janasthán that glorious tree: There RávaG, lord of giants slew Our friend Jamáyus brave and true, Thy champion in the hopeless strife, Who gave for thee his noble life. Now mark that glade amid the trees Where once we lived as devotees. See, see our leafy cot between Those waving boughs of densest green, Where RávaG seized his prize and stole My love the darling of my soul. O, look again: beneath thee gleams 1023 Here, in the North-west recension, Sítá expresses a wish that Tárá and the wives of the Vánar chiefs should be invited to accompany her to Ayodhyá. The car decends, and the Vánar matrons are added to the party. The Bengal recension ignores this palpable interruption.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1786)
- **Original**: 1768 The Ramayana Godávarí the best of streams, Whose lucid waters sweetly glide By lilies that adorn her side. There dwelt Agastya, holy sage, In plantain-sheltered hermitage. See Zarabhanga's humble shed[501] Which sovereign Indra visited. See where the gentle hermits dwell Neath Atri's rule who loved us well; Where once thine eyes were blest to see His sainted dame who talked with thee. Now rest thine eyes with new delight On Chitrakúma's woody height, See Jumna flashing in the sun Through groves of brilliant foliage run. Screened by the shade of spreading boughs. There Bharadvája keeps his vows, There Gangá, river of the skies, Rolls the sweet wave that purifies, ThereZringavera's towers ascend Where Guha reigns, mine ancient friend. I see, I see thy glittering spires, Ayodhyá, city of my sires. Bow down, bow down thy head, my sweet, Our home, our long-lost home to greet.” Canto CXXVI. Bharat Consoled.
- **Translation**: 

---

### Verse 7 (Ramayan 0.1787)
- **Original**: Canto CXXVI. Bharat Consoled. 1769 But Ráma bade the chariot stay, And halting in his airy way, In Bharadvája's holy shade His homage to the hermit paid. “O saint,” he cried,“I yearn to know My dear Ayodhyá's weal and woe. O tell me that the people thrive, And that the queens are yet alive.” Joy gleamed in Bhardvája's eye, Who gently smiled and made reply: “Thy brother, studious of thy will, Is faithful and obedient still. In tangled twine he coils his hair: Thy safe return is all his care. Before thy shoes he humbly bends, And to thy house and realm attends. When first these dreary years began, When first I saw the banished man, With Sítá, in his hermit coat, At this sad heart compassion smote. My breast with tender pity swelled: I saw thee from thy home expelled, Reft of all princely state, forlorn, A hapless wanderer travel-worn, Firm in thy purpose to fulfil Thy duty and thy father's will. But boundless is my rapture now: Triumphant, girt with friends, art thou. Where'er thy wandering steps have been, Thy joy and woe mine eyes have seen. Thy glorious deeds to me art known, The Bráhmans saved, the foes o'erthrown. Such power have countless seasons spent
- **Translation**: 

---

### Verse 8 (Ramayan 0.1788)
- **Original**: 1770 The Ramayana In penance and devotion lent. Thy virtues, best of chiefs, I know, And now a boon would fain bestow. This hospitable gift1024 receive: Then with the dawn my dwelling leave.” The bended head of Ráma showed His reverence for the grace bestowed; Then for each brave companion's sake He sought a further boon and spake: “O let that mighty power of thine The road to fair Ayodhyá line With trees where fruit of every hue The Vánars' eye and taste may woo, And flowers of every season, sweet With stores of honeyed juice, may meet.” The hero ceased: the hermit bent His reverend head in glad assent; And swift, as Bharadvája willed, The prayer of Ráma was fulfilled. For many a league the lengthening road Trees thick with fruit and blossom showed With luscious beauty to entice The taste like trees of Paradise. The Vánars passed beneath the shade Of that delightful colonnade, Still tasting with unbounded glee The treasures of each wondrous tree. 1024 The arghya, a respectful offering to Gods and venerable men consisting of rice, dúivá grass, flowers etc., with water.
- **Translation**: 

---

### Verse 9 (Ramayan 0.1789)
- **Original**: Canto CXXVII. Ráma's Message. 1771 Canto CXXVII. Ráma's Message. But Ráma, when he first looked down And saw afar Ayodhyá's town, Had called Hanumán to his side, The chief on whom his heart relied, And said:“Brave Vánar, good at need, Haste onward, to Ayodhyá speed, And learn, I pray, if all be well With those who in the palace dwell. But as thou speedest on thy way Awhile atZringavera stay. Tell Guha the Nishádas' lord, That victor, with my queen restored, In health and strength with many a friend Homeward again my steps I bend. Thence by the road that he will show On to Ayodhyá swiftly go. There with my love my brother greet, And all our wondrous tale repeat. Say that victorious in the strife I come with LakshmaG and my wife, Then mark with keenest eye each trace Of joy or grief on Bharat's face. Be all his gestures closely viewed, [502] Each change of look and attitude. Where breathes the man who will not cling To all that glorifies a king? Where beats the heart that can resign An ancient kingdom, nor repine To lose a land renowned for breeds Of elephants and warrior steeds? If, won by custom day by day, My brother Bharat thirsts for sway,
- **Translation**: 

---

### Verse 10 (Ramayan 0.1790)
- **Original**: 1772 The Ramayana Still let him rule the nations, still The throne of old Ikshváku fill. Go, mark him well: his feelings learn, And, ere we yet be near return.” He ceased: and, garbed in human form, Forth sped Hanúmán swift as storm. Sublime in air he rose, and through The region of his father flew. He saw far far beneath his feet Where Gangá's flood and Jumna meet. Descending from the upper air He enteredZringavera, where King Guha's heart was well content To hear the message Ráma sent. Then, with his mighty strength renewed, The Vánar chief his way pursued, Válúkiní was far behind, And Gomatí with forests lined, And golden fields and pastures gay With flocks and herds beneath him lay. Then Nandigráma charmed his eye Where flowers were bright with every dye, And trees of lovely foliage made With meeting boughs delightful shade, Where women watched in trim array Their little sons' and grandsons' play. His eager eye on Bharat fell Who sat before his lonely cell. In hermit weed, with tangled hair, Pale, weak, and worn with ceaseless care. His royal pomp and state resigned For Ráma still he watched and pined, Still to his dreary vows adhered,
- **Translation**: 

---

### Verse 11 (Ramayan 0.1791)
- **Original**: Canto CXXVII. Ráma's Message. 1773 And royal Ráma's shoes revered. Yet still the terror of his arm Preserved the land from fear and harm. The Wind-God's son, in form a man, Raised reverent hands and thus began: “Fond greeting, Prince, I bring to thee, And Ráma's self has sent it: he For whom thy spirit sorrows yet As for a hapless anchoret In DaG ak wood, in dire distress, With matted hair and hermit dress. This sorrow from thy bosom fling, And hear the tale of joy I bring. This day thy brother shalt thou meet Exulting in his foe's defeat, Freed from his toil and lengthened vow, The light of victory on his brow, With Sítá, LakshmaG and his friends Homeward at last his steps he bends.” Then joy, too mighty for control, Rushed in full flood o'er Bharat's soul; His reeling sense and strength gave way, And fainting on the earth he lay, At length upspringing from the ground, His arms about Hanúmán wound, With tender tears of rapture sprung, He dewed the neck to which he clung: “Art thou a God or man,” he cried, “Whom love and pity hither guide? For this a hundred thousand kine, A hundred villages be thine. A score of maids of spotless lives
- **Translation**: 

---

### Verse 12 (Ramayan 0.1792)
- **Original**: 1774 The Ramayana To thee I give to be thy wives, Of golden hue and bright of face, Each lovely for her tender grace.” He ceased a while by joy subdued, And then his eager speech renewed. Canto CXXVIII. Hanumán's Story. “In doubt and fear long years have passed And glorious tidings come at last. True, true is now the ancient verse Which men in time of bliss rehearse: “Once only in a hundred years Great joy to mortal men appears.” But now his woes and triumph tell, And loss and gain as each befell.” He ceased: Hanúmán mighty-souled The tale of Ráma's wanderings told From that first day on which he stood In the drear shade of DaG ak wood. He told how fierce Virádha fell; He told ofZarabhanga's cell Where Ráma saw with wondering eyes Indra descended from the skies. He told howZúrpaGakhí came, Her soul aglow with amorous flame, And fled repulsed, with rage and tears, Reft of her nose and severed ears. He told how Ráma's might subdued The giants' furious multitude;
- **Translation**: 

---

### Verse 13 (Ramayan 0.1793)
- **Original**: Canto CXXIX. The Meeting With Bharat. 1775 How Khara with the troops he led And Tri[irás and DúshaG bled: How Ráma, tempted from his cot, The golden deer pursued and shot, And RávaG came and stole away The Maithil queen his hapless prey, When, as he fought, the dame to save, His noble life Jatáyus gave: How Ráma still the the search renewed, The robber to his hold pursued, Bridging the sea from shore to shore, And found his queen to part no more.1025 [503] Canto CXXIX. The Meeting With Bharat. O'erwhelmed with rapture Bharat heard The tale that all his being stirred, And, heralding the glad event, This order toZatrughna sent: “Let every shrine with flowers be gay Let incense burn and music play. Go forth, go forth to meet your king, Let tabours sound and minstrels sing, Let bards swell high the note of praise Skilled in the lore of ancient days, Call forth the royal matrons: call Each noble from the council hall. 1025 I have abridged Hanumán's outline of Ráma's adventures, with the details of which we are already sufficiently acquainted.
- **Translation**: 

---

### Verse 14 (Ramayan 0.1794)
- **Original**: 1776 The Ramayana Send all we love and honour most, Send Bráhmans and the warrior host, A glorious company to bring In triumph home our lord the king.” Great rapture filledZatrughna's breast, Obedient to his brother's hest. “Send forth ten thousand men” he cried, “Let brawny arms be stoutly plied, And, smoothing all with skilful care, The road for Ko[al's king prepare. Then o'er the earth let thousands throw Fresh showers of water cool as snow, And others strew with garlands gay With loveliest blooms our monarch's way. On tower and temple porch and gate Let banners wave in royal state, And be each roof and terrace lined With blossoms loose and chaplets twined.” The nobles hasting forth fulfilled His order asZatrughna willed. Sublime on elephants they rode Whose gilded girths with jewels glowed. Attended close by thousands more Gay with the gear and flags they bore. A thousand chiefs their steeds bestrode, Their glittering cars a thousand showed. And countless hosts in rich array Pursued on foot their eager way. Veiled from the air with silken screens In litters rode the widowed queens. Kausalyá first, acknowledged head And sovereign of the household, led:
- **Translation**: 

---

### Verse 15 (Ramayan 0.1795)
- **Original**: Canto CXXIX. The Meeting With Bharat. 1777 Sumitrá next, and after, dames Of lower rank and humbler names. Then compassed by a white-robed throng Of Bráhmans, heralded with song, With shouts of joy from countless throats, And shells' and tambours' mingled notes, And drums resounding long and loud, Exulting Bharat joined the crowd. Still on his head, well-trained in lore Of duty, Ráma's shoes he bore. The moon-white canopy was spread With flowery twine engarlanded, And jewelled cheuries, meet to hold O'er Ráma's brow, shone bright with gold, Though Nandigráma's town they neared, Of Ráma yet no sign appeared. Then Bharat called the Vánar chief And questioned thus in doubt and grief: “Hast thou uncertain, like thy kind, A sweet delusive guile designed? Where, where is royal Ráma? show The hero, victor of the foe. I gaze, but see no Vánars still Who wear each varied shape at will.” In eager love thus Bharat cried, And thus the Wind-God's son replied: “Look, Bharat, on those laden trees That murmur with the song of bees; For Ráma's sake the saint has made Untimely fruits, unwonted shade. Such power in ages long ago Could Indra's gracious boon bestow. O, hear the Vánars' voices, hear
- **Translation**: 

---

### Verse 16 (Ramayan 0.1796)
- **Original**: 1778 The Ramayana The shouting which proclaims them near. E'en now about to cross they seem Sweet Gomatí's delightful stream. I see, I see the car designed By Brahmá's own creative mind, The car which, radiant as the moon, Moves at the will by Brahmá's boon; The car which once was Rávan's pride, The victor's spoil when Rávan died. Look, there are Raghu's sons: between The brothers stands the rescued queen. There is VibhishaG full in view, Sugríva and his retinue.” He ceased: then rapture loosed each tongue: From men and dames, from old and young, One long, one universal cry, 'Tis he, 'tis Ráma, smote the sky. All lighted down with eager speed From elephant and car and steed, And every joyful eye intent On Ráma's moonbright face was bent. Entranced a moment Bharat gazed: Then reverential hands he raised, And on his brother humbly pressed The honours due to welcome guest. Then Bharat clomb the car to greet His king and bowed him at his feet, Till Ráma raised him face to face And held him in a close embrace. Then LakshmaG and the Maithil dame He greeted as he spoke his name1026 1026 In these respectful salutations the person who salutes his superior mentions his own name even when it is well known to the person whom he salutes.
- **Translation**: 

---

### Verse 17 (Ramayan 0.1797)
- **Original**: Canto CXXIX. The Meeting With Bharat. 1779 He greeted next, supreme in place, The sovereign of the Vánar race, And Jámbaván and Báli's son, [504] And lords and chiefs, omitting none.1027 Sugríva to his heart he pressed And thus with grateful words addressed: “Four brothers, Vánar king, were we, And now we boast a fifth in thee. By kindly acts a friend we know: Offence and wrong proclaim the foe.” To King VibhishaG then he spake: “Well hast thou fought for Ráma's sake.” Nor was the braveZatrughna slow His reverential love to show To both his brothers, as was meet, And venerate the lady's feet. Then Ráma to his mother came, Saw her pale cheek and wasted frame, With gentle words her heart consoled, And clasped her feet with loving hold. Then at Sumitrá's feet he bent, And fair Kaikeyí's, reverent, Greeted each dame from chief to least, And bowed him to the household priest. Up rose a shout from all the throng: “O welcome, Ráma, mourned so long. Welcome, Kausalyá's joy and pride,” Ten hundred thousand voices cried. Then Bharat placed, in duty taught, On Ráma's feet the shoes he brought: “My King,” he cried,“receive again 1027 I have omitted the chieftains' names as they could not be introduced without padding. They are Mainda, Dwivid, Níla, Rishabh, SusheG, Nala, Gaváksha, Gandhamádan, Zarabh, and Panas.
- **Translation**: 

---

### Verse 18 (Ramayan 0.1798)
- **Original**: 1780 The Ramayana The pledge preserved through years of pain, The rule and lordship of the land Entrusted to my weaker hand. No more I sigh o'er sorrows past, My birth and life are blest at last In the glad sight this day has shown, When Ráma comes to rule his own.” He ceased: the faithful love that moved The prince's soul each heart approved; Nor could the Vánar chiefs refrain From tender tears that fell like rain. Then Ráma, stirred with joy anew, His arms about his brother threw, And to the grove his course he bent Where Bharat's hermit days were spent. Alighting in that pure retreat He pressed the earth with eager feet. Then, at his hest, the car rose high And sailing through the northern sky Sped homeward to the Lord of Gold Who owned the wondrous prize of old.1028 Canto CXXX. The Consecration. 1028 The following addition is found in the Bengal recension: But Vai[ravaG (Kuvera) when he beheld his chariot said unto it:“Go, and carry Ráma, and come unto me when my thought shall call thee, And the chariot returned unto Ráma;” and he honoured it when he had heard what had passed.
- **Translation**: 

---

### Verse 19 (Ramayan 0.1799)
- **Original**: Canto CXXX. The Consecration. 1781 Then, reverent hand to hand applied, Thus Bharat to his brother cried: “Thy realm, O King, is now restored, Uninjured to the rightful lord. This feeble arm with toil and pain, The weighty charge could scarce sustain. And the great burthen wellnigh broke The neck untrained to bear the yoke. The royal swan outspeeds the crow: The steed is swift, the mule is slow, Nor can my feeble feet be led O'er the rough ways where thine should tread. Now grant what all thy subjects ask: Begin, O King, thy royal task. Now let our longing eyes behold The glorious rite ordained of old, And on the new-found monarch's head Let consecrating drops be shed.” He ceased; victorious Ráma bent His head in token of assent. He sat, and tonsors trimmed with care His tangles of neglected hair Then, duly bathed, the hero shone With all his splendid raiment on. And Sítá with the matrons' aid Her limbs in shining robes arrayed, Sumantra then, the charioteer, Drew, ordered byZatrughna near, And stayed within the hermit grove The chariot and the steeds he drove. Therein Sugríva's consorts, graced With gems, and Ráma's queen were placed, All fain Ayodhyá to behold:
- **Translation**: 

---

### Verse 20 (Ramayan 0.1800)
- **Original**: 1782 The Ramayana And swift away the chariot rolled. Like Indra Lord of Thousand Eyes, Drawn by fleet lions through the skies. Thus radiant in his glory showed King Ráma as he homeward rode, In power and might unparalleled. The reins the hand of Bharat held. Above the peerless victor's head The snow-white shadeZatrughna spread, And Lakshma G's ever-ready hand His forehead with a chourie fanned. VibhishaG close to LakshmaG's side Sharing his task a chourie plied. Sugríva onZatrunjay came, An elephant of hugest frame: Nine thousand others bore, behind, The chieftains of the Vánar kind All gay, in forms of human mould, With rich attire and gems and gold.[505] Thus borne along in royal state King Ráma reached Ayodbyá's gate With merry noise of shells and drums And joyful shouts, He comes, he comes, A Bráhman host with solemn tread, And kine the long procession led, And happy maids in ordered bands Threw grain and gold with liberal hands. Neath gorgeous flags that waved in rows On towers and roofs and porticoes. Mid merry crowds who sang and cheered The palace of the king they neared. Then Raghu's son to Bharat, best Of duty's slaves, these words addressed: “Pass onward to the monarch's hall.
- **Translation**: 

---

