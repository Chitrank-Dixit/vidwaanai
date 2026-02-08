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

### Verse 1 (Ramayana 0.326)
- **Original**: 308 The Ramayana And at thy side his place appoint Our gallant prince, so brave and strong, Riding in royal state along, Our eyes with joyful pride will see Screened by the shade that shelters thee.” Then spake the king again, as though Their hearts' true wish he sought to know: “These prayers for Ráma's rule suggest One question to my doubting breast. This thing, I pray, with truth explain: Why would ye, while I justly reign, That he, mine eldest son, should bear His part with me as ruling heir?” Then all the people made reply, Peasant and townsman, low and high: “Each noblest gift of form and mind,[091] O Monarch, in thy son we find. Do thou the godlike virtues hear Which Ráma to our hearts endear. So richly blest with graces, none In all the earth excels thy son: Nay, who to match with him may claim In truth, in justice, and in fame? True to his promise, gentle, kind, Unenvious, of grateful mind, Versed in the law and firm of soul, He keeps each sense with strict control. With duteous care he loves to sit By Bráhmans skilled in Holy Writ. Hence brightest glory, ne'er to end, And matchless fame his youth attend. Skilled in the use of spear and shield, And arms which heavenly warriors wield, Supreme in war, unconquered yet
- **Translation**: 

---

### Verse 2 (Ramayana 0.327)
- **Original**: Canto II. The People's Speech. 309 By man, fiend, God in battle met, Whene'er in pomp of war he goes 'Gainst town or city of the foes, He ever comes with LakshmaG back Victorious from the fierce attack. Returning homeward from afar Borne on his elephant or car, He ever to the townsmen bends And greets them as beloved friends, Asks how each son, each servant thrives, How fare our pupils, offerings, wives; And like a father bids us tell, Each for himself, that all is well. If pain or grief the city tries His heart is swift to sympathize. When festive scenes our thoughts employ He like a father shares the joy. High is the fate, O King, that gave Thy Ráma born to bless and save, With filial virtues fair and mild Like Ka[yap old Maríchi's child. Hence to the kingdom's distant ends One general prayer for him ascends. Each man in town and country prays For Ráma's strength, health, length of days. With hearts sincere, their wish the same, The tender girl, the aged dame, Subject and stranger, peasant, hind, One thought impressed on every mind, At evening and at dawning day To all the Gods for Ráma pray. Do thou, O King, of grace comply, And hear the people's longing cry, And let us on the throne by thee
- **Translation**: 

---

### Verse 3 (Ramayana 0.328)
- **Original**: 310 The Ramayana The lotus-tinted Ráma see. O thou who givest boons, attend; A gracious ear, O Monarch, lend And for our weal install, Consenting to our earnest prayer, Thy godlike Ráma Regent Heir, Who seeks the good of all.” Canto III. Dasaratha's Precepts. The monarch with the prayer complied Of suppliant hands, on every side Uplifted like a lotus-bed: And then these gracious words he said: “Great joy and mighty fame are mine Because your loving hearts incline, In full assembly clearly shown To place my Ráma on the throne.” Then to Va[ishmha, standing near, And Vámadeva loud and clear The monarch spoke that all might hear: “'Tis pure and lovely Chaitra now When flowers are sweet on every bough; All needful things with haste prepare That Ráma be appointed heir.”
- **Translation**: 

---

### Verse 4 (Ramayana 0.329)
- **Original**: Canto III. Dasaratha's Precepts. 311 Then burst the people's rapture out In loud acclaim and joyful shout; And when the tumult slowly ceased The king addressed the holy priest: “Give order, Saint, with watchful heed For what the coming rite will need. This day let all things ready wait Mine eldest son to consecrate.” Best of all men of second birth Va [ishmha heard the lord of earth, And gave commandment to the bands Of servitors with lifted hands Who waited on their master's eye: “Now by to-morrow's dawn supply Rich gold and herbs and gems of price And offerings for the sacrifice, Wreaths of white flowers and roasted rice, And oil and honey, separate; New garments and a car of state, An elephant with lucky signs, A fourfold host in ordered lines, The white umbrella, and a pair Of chowries,261 and a banner fair; A hundred vases, row on row, To shine like fire in splendid glow, A tiger's mighty skin, a bull With gilded horns most beautiful. All these, at dawn of coming day, Around the royal shrine array, Where burns the fire's undying ray. Each palace door, each city gate With wreaths of sandal decorate. 261 Whisks, usually made of the long tails of the Yak.
- **Translation**: 

---

### Verse 5 (Ramayana 0.330)
- **Original**: 312 The Ramayana And with the garlands' fragrant scent Let clouds of incense-smoke be blent. Let food of noble kind and taste Be for a hundred thousand placed; Fresh curds with streams of milk bedewed To feed the Bráhman multitude.[092] With care be all their wants supplied. And mid the twice-born chiefs divide Rich largess, with the early morn, And oil and curds and roasted corn. Soon as the sun has shown his light Pronounce the prayer to bless the rite, And then be all the Bráhmans called And in their ordered seats installed. Let all musicians skilled to play, And dancing-girls in bright array Stand ready in the second ring Within the palace of the king. Each honoured tree, each holy shrine With leaves and flowery wreaths entwine, And here and there beneath the shade Be food prepared and presents laid. Then brightly clad, in warlike guise, With long swords girt upon their thighs, Let soldiers of the nobler sort March to the monarch's splendid court.” Thus gave command the twice-born pair To active servants stationed there. Then hastened to the king and said That all their task was duly sped, The king to wise Sumantra spake: “Now quick, my lord, thy chariot take, And hither with thy swiftest speed
- **Translation**: 

---

### Verse 6 (Ramayana 0.331)
- **Original**: Canto III. Dasaratha's Precepts. 313 My son, my noble Ráma lead.” Sumantra, ere the word was given, His chariot from the court had driven, And Ráma, best of all who ride In cars, came sitting by his side. The lords of men had hastened forth From east and west and south and north, Áryan and stranger, those who dwell In the wild wood and on the fell, And as the Gods to Indra, they Showed honour to the king that day. Like Vásav, when his glorious form Is circled by the Gods of storm, Girt in his hall by kings he saw His car-borne Ráma near him draw, Like him who rules the minstrel band Of heaven;262 whose valour filled the land, Of mighty arm and stately pride Like a wild elephant in stride, As fair in face as that fair stone Dear to the moon, of moonbeams grown,263 With noble gifts and grace that took The hearts of all, and chained each look, World-cheering as the Lord of Rain When floods relieve the parching plain. The father, as the son came nigh, Gazed with an ever-thirstier eye. Sumantra helped the prince alight From the good chariot passing bright, 262 Chitraratha, King of the Gandharvas. 263 The Chandrakánta or Moonstone, a sort of crystal supposed to be composed of congealed moonbeams.
- **Translation**: 

---

### Verse 7 (Ramayana 0.332)
- **Original**: 314 The Ramayana And as to meet his sire he went Followed behind him reverent. Then Ráma clomb, the king to seek That terrace like Kailása's peak, And reached the presence of the king, Sumantra closely following. Before his father's face he came, Raised suppliant hands and named his name,264 And bowing lowly as is meet Paid reverence to the monarch's feet. But soon as Da[aratha viewed The prince in humble attitude, He raised him by the hand in haste And his beloved son embraced, Then signed him to a glorious throne, Gem-decked and golden, near his own. Then Ráma, best of Raghu's line, Made the fair seat with lustre shine As when the orient sun upsprings And his pure beam on Meru flings. The glory flashed on roof and wall, And with strange sheen suffused the hall, As when the moon's pure rays are sent Through autumn's star-lit firmament. Then swelled his breast with joy and pride As his dear son the father eyed, E'en as himself more fair arrayed In some clear mirror's face displayed. The aged monarch gazed awhile, Then thus addressed him with a smile, As Ka[yap, whom the worlds revere, Speaks for the Lord of Gods to hear: 264 A customary mark of respect to a superior.
- **Translation**: 

---

### Verse 8 (Ramayana 0.333)
- **Original**: Canto III. Dasaratha's Precepts. 315 “O thou of all my sons most dear, In virtue best, thy father's peer, Child of my consort first in place, Mine equal in her pride of race, Because the people's hearts are bound To thee by graces in thee found, Be thou in Pushya's favouring hour Made partner of my royal power. I know that thou by nature's bent Both modest art and excellent, But though thy gifts no counsel need My love suggests the friendly rede. Mine own dear son, be modest still, And rule each sense with earnest will. Keep thou the evils far away That spring from love and anger's sway. Thy noble course alike pursue In secret as in open view, And every nerve, the love to gain Of ministers and subjects, strain. The happy prince who sees with pride His thriving people satisfied; Whose arsenals with arms are stored, And treasury with golden hoard,— [093] His friends rejoice as joyed the Blest When Amrit crowned their eager quest. So well, my child, thy course maintain, And from all ill thy soul refrain.” The friends of Ráma, gathered nigh, Longing their lord to gratify, Ran to Kau[alyá's bower to tell The tidings that would please her well. She, host of dames, with many a gem,
- **Translation**: 

---

### Verse 9 (Ramayana 0.334)
- **Original**: 316 The Ramayana And gold, and kine rewarded them. Then Ráma paid the reverence due, Mounted the chariot, and withdrew, And to his splendid dwelling drove While crowds to show him honour strove. The people, when the monarch's speech Their willing ears had heard, Were wild with joy as though on each Great gifts had been conferred. With meek and low salute each man Turned to his home away, And there with happy heart began To all the Gods to pray. Canto IV. Ráma Summoned. The crowd dismissed, to high debate The monarch called his peers of state, And, counsel from their lips obtained, Firm in his will his will explained: “To-morrow with auspicious ray The moon in Pushya's sign will stay; Be that the time with happy fate Mine eldest son to consecrate, And let my Ráma, lotus-eyed, As Regent o'er the state preside.”
- **Translation**: 

---

### Verse 10 (Ramayana 0.335)
- **Original**: Canto IV. Ráma Summoned. 317 He sought, within, his charioteer, And cried“Again bring Ráma here.” To Ráma's home Sumantra hied Again to be the prince's guide. His coming, told to Ráma's ear, Suggested anxious doubt and fear. He bade the messenger be led That instant in, and thus he said: “Tell me the cause, omitting naught, Why thou again my house hast sought.” The envoy answered:“Prince, thy sire Has sent thy presence to require. My sender known, 'tis thine to say If thou wilt go or answer nay.” Then Ráma, when he heard his speech, Made haste the royal court to reach. Soon as the monarch was aware His dearest son was waiting there, Eager the parley to begin He bade them lead the prince within, Soon as he passed the chamber door The hero bent him to the floor, And at a distance from his seat Raised his joined hands his sire to greet. The monarch raised him from the ground, And loving arms about him wound, Then pointed to a seat that shone With gold for him to rest upon. “Aged am I,” he said,“and worn; In life's best joys my share have borne; Rites to the Gods, in hundreds, paid, With gifts of corn and largess made. I yearned for sons: my life is blest
- **Translation**: 

---

### Verse 11 (Ramayana 0.336)
- **Original**: 318 The Ramayana With them and thee of sons the best. No debt to saints or Bráhmans, no, Nor spirits, Gods, or self I owe. One duty now remains alone, To set thee on thy father's throne. Now therefore, Ráma, hear my rede, And mark my words with duteous heed: This day the peoples' general voice, Elects thee king of love and choice, And I, consenting to the prayer, Will make thee, darling, Regent Heir. Dread visions, each returning night, With evil omens scare my sight. Red meteors with a fearful sound Shoot wildly downward to the ground, While tempests lash the troubled air; And they who read the stars declare That, leagued against my natal sign, Ráhu,265 the Sun,266 and Mars combine. When portents dire as these appear, A monarch's death or woe is near. Then while my senses yet are spared, And thought and will are unimpaired, Be thou, my son, anointed king: Men's fancy is a fickle thing. To-day the moon, in order due, Entered the sign Punarvasu,267 To-morrow, as the wise foretell, 265 Ráhu, the ascending node, is in mythology a demon with the tail of a dragon whose head was severed from his body by VishGu, but being immortal, the head and tail retained their separate existence and being transferred to the stellar sphere became the authors of eclipses; the first especially by endeavouring to swallow the sun and moon. 266 In eclipse. 267 The seventh of the lunar asterisms.
- **Translation**: 

---

### Verse 12 (Ramayana 0.337)
- **Original**: Canto IV. Ráma Summoned. 319 In Pushya's favouring stars will dwell: Then on the throne shalt thou be placed. My soul, prophetic, counsels haste: Thee, O my son, to-morrow I As Regent Heir will sanctify. So till the coming night be passed Do thou and Sítá strictly fast: From worldly thoughts thy soul refrain, And couched on holy grass remain. [094] And let thy trusted lords attend In careful watch upon their friend, For, unexpected, check and bar Our weightiest counsels often mar. While Bharat too is far away Making with royal kin his stay, I deem the fittest time of all Thee, chosen Regent, to install. It may be Bharat still has stood True to the counsels of the good, Faithful to thee with tender trust, With governed senses, pure and just. But human minds, too well I know, Will sudden changes undergo, And by their constant deeds alone The virtue of the good is shown. Now, Ráma, go. My son, good night! Fixt is to-morrow for the rite.” Then Ráma paid the reverence due, And quickly to his home withdrew. He passed within, nor lingered there, But sought his mother's mansion, where The dame in linen robes arrayed Devoutly in the chapel prayed
- **Translation**: 

---

### Verse 13 (Ramayana 0.338)
- **Original**: 320 The Ramayana To Fortune's Queen, with utterance checked, That she her Ráma would protect. There was Sumitrá too, and there Was Lakshma G led by loving care: And when the royal choice they knew Sítá in haste was summoned too. Absorbed, with half-shut eyes, the queen Attended by the three was seen. She knew that Pushya's lucky hour Would raise her son to royal power, So fixed with bated breath each thought On God supreme, by all men sought. To her, as thus she knelt and prayed, Ráma drew near, due reverence paid, And then to swell his mother's joy, Thus spoke her own beloved boy; “O mother dear, my sire's decree Entrusts the people's weal to me. To-morrow I, for so his will, Anointed king, the throne shall fill. The few last hours till night shall end Sítá with me must fasting spend, For so my father has decreed, And holy priests with him agreed. What vows soever thou mayst deem My consecration's eve beseem, Do thou, sweet mother, for my sake And for beloved Sítá's make.” When the glad news Kau[alyá heard, So long desired, so long deferred, While tears of joy her utterance broke, In answer to her son she spoke: “Long be thy life, my darling: now
- **Translation**: 

---

### Verse 14 (Ramayana 0.339)
- **Original**: Canto IV. Ráma Summoned. 321 Thy prostrate foes before thee bow. Live long and with thy bright success My friends and dear Sumitrá's bless. Surely the stars were wondrous fair When thee, sweet son, thy mother bare, That thy good gifts such love inspire And win the favour of thy sire. With thee I travailed not in vain; Those lotus eyes reward my pain, And all the glory of the line Of old Ikshváku will be thine.” He smiled, and on his brother gazed Who sate with reverent hands upraised, And said:“My brother, thou must be Joint-ruler of this land with me. My second self thou, LakshmaG, art, And in my fortune bearest part. Be thine, Sumitrá's son, to know The joys from regal power that flow. My life itself, the monarch's seat, For thy dear sake to me are sweet.” Thus Ráma to his brother said, To both his mothers268 bowed his head, And then with Sítá by his side To his own house the hero hied. 268 Kau [alyá and Sumitrá.
- **Translation**: 

---

### Verse 15 (Ramayana 0.340)
- **Original**: 322 The Ramayana Canto V. Ráma's Fast. Then Saint Va[ishmha to the king Came ready at his summoning. “Now go,” exclaimed the monarch,“thou Enriched by fervent rite and vow, For Ráma and his wife ordain The fast, that joy may bless his reign.” The best of those who Scripture know Said to the king,“My lord, I go.” To Ráma's house Va[ishmha hied, The hero's fast by rule to guide, And skilled in sacred texts to tell Each step to him instructed well. Straight to Prince Ráma's high abode, That like a cloud pale-tinted showed, Borne in his priestly car he rode. Two courts he passed, and in the third He stayed his car. Then Ráma heard The holy sage was come, and flew To honour him with honour due. He hastened to the car and lent His hand to aid the priest's descent. Then spoke Va[ishmha words like these, Pleased with his reverent courtesies, With pleasant things his heart to cheer Who best deserved glad news to hear: “Prince, thou hast won thy father's grace, And thine will be the Regent's place: Now with thy Sítá, as is right, In strictest fasting spend the night,[095]
- **Translation**: 

---

### Verse 16 (Ramayana 0.341)
- **Original**: Canto V. Ráma's Fast. 323 For when the morrow's dawn is fair The king will consecrate his heir: So Nahush,269 as the wise relate, Yayáti joyed to consecrate.” Thus having said, Va[ishmha next Ordained the fast by rule and text, For Ráma faithful to his vows And the Videhan dame his spouse. Then from the prince's house he hied With courteous honours gratified. Round Ráma gathered every friend In pleasant talk a while to spend. He bade good night to all at last, And to his inner chamber passed. Then Ráma's house shone bright and gay With men and maids in glad array, As in the morning some fair lake When all her lotuses awake, And every bird that loves the flood Flits joyous round each opening bud. Forth from the house Va[ishmha drove, That with the king's in splendour strove, And all the royal street he viewed Filled with a mighty multitude The eager concourse blocked each square, Each road and lane and thoroughfare, And joyous shouts on every side Rose like the roar of Ocean's tide, As streams of men together came With loud huzza and glad acclaim. The ways were watered, swept and clean, 269 A king of the Lunar race, and father of Yayáti.
- **Translation**: 

---

### Verse 17 (Ramayana 0.342)
- **Original**: 324 The Ramayana And decked with flowers and garlands green And all Ayodhyá shone arrayed With banners on the roofs that played. Men, women, boys with eager eyes, Expecting when the sun should rise, Stood longing for the herald ray Of Ráma's consecration day, To see, a source of joy to all, The people-honoured festival. The priest advancing slowly through The mighty crowd he cleft in two, Near to the monarch's palace drew. He sought the terrace, by the stair, Like a white cloud-peak high in air, The reverend king of men to meet Who sate upon his splendid seat: Thus will V[ihaspati arise To meet the monarch of the skies. But when the king his coming knew, He left his throne and near him drew Questioned by him Va[ishmha said That all his task was duly sped. Then all who sate there, honouring Va [ishmha, rose as rose the king. Va [ishmha bade his lord adieu, And all the peers, dismissed, withdrew. Then as a royal lion seeks His cave beneath the rocky peaks, So to the chambers where abode His consorts Da[aratha strode. Full-thronged were those delightful bowers With women richly dressed, And splendid as the radiant towers
- **Translation**: 

---

### Verse 18 (Ramayana 0.343)
- **Original**: Canto VI. The City Decorated. 325 Where Indra loves to rest. Then brighter flashed a thousand eyes With the light his presence lent, As, when the moon begins to rise The star thronged firmament. Canto VI. The City Decorated. Then Ráma bathed in order due, His mind from worldly thoughts withdrew, And with his large-eyed wife besought NáráyaG, as a votary ought. Upon his head the brimming cup Of holy oil he lifted up, Then placed within the kindled fire The offering to that heavenly Sire, And as he sipped the remnant prayed To Him for blessing and for aid. Then with still lips and tranquil mind With his Videhan he reclined, In VishGu's chapel, on a bed Where holy grass was duly spread, While still the prince's every thought The God supreme, NáráyaG, sought. One watch remained the night to close When Ráma from his couch arose, And bade the men and maids adorn His palace for the solemn morn. He heard the bards and heralds raise Auspicious strains of joy and praise; And breathed devout, with voice restrained,
- **Translation**: 

---

### Verse 19 (Ramayana 0.344)
- **Original**: 326 The Ramayana The hymn for morning rites ordained; Then, with his head in reverence bowed, Praised Madhu's conquering foe aloud, And, in pure linen robes arrayed, The priests to raise their voices prayed. Obedient to the summons they Proclaimed to all the festal day. The Bráhmans' voices, deep and sweet, Resounded through the crowded street, And echoed through Ayodhyá went By many a loud-toned instrument. Then all the people joyed to hear That Ráma with his consort dear Had fasted till the morning light In preparation for the rite. Swiftly the joyful tidings through Ayodhyá's crowded city flew, And soon as dawn appeared, each man To decorate the town began.[096] In all the temples bright and fair As white clouds towering in the air, In streets, and where the cross-ways met, Where holy fig-trees had been set, In open square, in sacred shade, Where merchants' shops their wealth displayed, On all the mansions of the great, And householders of wealth and state, Where'er the people loved to meet, Where'er a tree adorned the street, Gay banners floated to the wind, And ribands round the staves were twined. Then clear the singers' voices rang, As, charming mind and ear, they sang. Here players shone in bright attire,
- **Translation**: 

---

### Verse 20 (Ramayana 0.345)
- **Original**: Canto VI. The City Decorated. 327 There dancing women swelled the quire. Each with his friend had much to say Of Ráma's consecration-day: Yea, even children, as they played At cottage doors beneath the shade. The royal street with flowers was strown Which loving hands in heaps had thrown, And here and there rich incense lent Its fragrance to the garland's scent; And all was fresh and fair and bright In honour of the coming rite. With careful foresight to illume With borrowed blaze the midnight gloom, The crowds erected here and there Trees in each street gay lamps to bear. The city thus from side to side In festal guise was beautified. The people of the town who longed To view the rite together thronged, And filling every court and square Praised the good king in converse there: “Our high-souled king! He throws a grace On old Ikshváku's royal race. He feels his years' increasing weight, And makes his son associate. Great joy to us the choice will bring Of Ráma for our lord and king. The good and bad to him are known, And long will he protect his own. No pride his prudent breast may swell, Most just, he loves his brothers well, And to us all that love extends, Cherished as brothers and as friends. Long may our lord in life remain,
- **Translation**: 

---

