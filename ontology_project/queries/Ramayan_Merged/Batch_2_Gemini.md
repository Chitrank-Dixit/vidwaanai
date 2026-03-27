# Merged Batch 2 (Files 17-32)
# Assigned Agent: Gemini



--- Start of Ramayan_batch_17.md ---

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

### Verse 1 (Ramayan 0.321)
- **Original**: Canto I. The Heir Apparent. 303 In art and science duly trained, His student vow he well maintained; He learnt the lore for princes fit, The Vedas and their Holy Writ, And with his well-drawn bow at last His mighty father's fame surpassed. Of birth exalted, truthful, just, With vigorous hand, with noble trust, Well taught by aged twice-born men Who gain and right could clearly ken, Full well the claims and bounds he knew Of duty, gain, and pleasure too: Of memory keen, of ready tact, In civil business prompt to act. Reserved, his features ne'er disclosed What counsel in his heart reposed. All idle rage and mirth controlled, He knew the times to give and hold, Firm in his faith, of steadfast will, He sought no wrong, he spoke no ill: Not rashly swift, not idly slow, His faults and others' keen to know. Each merit, by his subtle sense; He matched with proper recompense. He knew the means that wealth provide, And with keen eye expense could guide. Wild elephants could he reclaim, And mettled steeds could mount and tame. No arm like his the bow could wield, Or drive the chariot to the field. Skilled to attack, to deal the blow, Or lead a host against the foe: Yea, e'en infuriate Gods would fear To meet his arm in full career.
- **Translation**: 

---

### Verse 2 (Ramayan 0.322)
- **Original**: 304 The Ramayana As the great sun in noontide blaze Is glorious with his world of rays, So Ráma with these virtues shone Which all men loved to gaze upon. The aged monarch fain would rest, And said within his weary breast, “Oh that I might, while living yet, My Ráma o'er the kingdom set. And see, before my course be run, The hallowed drops anoint my son; See all this spacious land obey, From side to side, my first-born's sway, And then, my life and joy complete, Obtain in heaven a blissful seat!” In him the monarch saw combined The fairest form, the noblest mind, And counselled how his son might share, The throne with him as Regent Heir. For fearful signs in earth and sky, And weakness warned him death was nigh: But Ráma to the world endeared By every grace his bosom cheered,[090] The moon of every eye, whose ray Drove all his grief and fear away. So duty urged that hour to seize, Himself, his realm, to bless and please. From town and country, far and near, He summoned people, prince, and peer. To each he gave a meet abode, And honoured all and gifts bestowed. Then, splendid in his king's attire, He viewed them, as the general Sire,
- **Translation**: 

---

### Verse 3 (Ramayan 0.323)
- **Original**: Canto II. The People's Speech. 305 In glory of a God arrayed, Looks on the creatures he has made. But Kekaya's king he called not then For haste, nor Janak, lord of men; For after to each royal friend The joyful tidings he would send. Mid crowds from distant countries met The king upon his throne was set; Then honoured by the people, all The rulers thronged into the hall. On thrones assigned, each king in place Looked silent on the monarch's face. Then girt by lords of high renown And throngs from hamlet and from town He showed in regal pride, As, honoured by the radiant band Of blessed Gods that round him stand, Lord Indra, Thousand-eyed. Canto II. The People's Speech. Then to the full assembly bowed The monarch, and addressed the crowd With gracious speech, in accents loud As heavenly drum or thunder-cloud:
- **Translation**: 

---

### Verse 4 (Ramayan 0.324)
- **Original**: 306 The Ramayana “Needs not to you who know declare How ever with paternal care My fathers of Ikshváku's line Have ruled the realm which now is mine. I too have taught my feet to tread The pathway of the mighty dead, And with fond care that never slept Have, as I could, my people kept. So toiling still, and ne'er remiss For all my people's weal and bliss, Beneath the white umbrella's260 shade. Old age is come and strength decayed. Thousands of years have o'er me flown, And generations round me grown And passed away. I crave at length Repose and ease for broken strength. Feeble and worn I scarce can bear The ruler's toil, the judge's care, With royal dignity, a weight That tries the young and temperate. I long to rest, my labour done, And in my place to set my son, If to the twice-born gathered here My counsel wise and good appear. For greater gifts than mine adorn Ráma my son, my eldest-born. Like Indra brave, before him fall The foeman's cities, tower and wall. Him prince of men for power and might, The best maintainer of the right, Fair as the moon when nothing bars His glory close to Pushya's stars, 260 Chief of the insignia of imperial dignity.
- **Translation**: 

---

### Verse 5 (Ramayan 0.325)
- **Original**: Canto II. The People's Speech. 307 Him with to-morrow's light I fain Would throne the consort of my reign. A worthy lord for you, I ween, Marked as her own by Fortune's Queen. The triple world itself would be Well ruled by such a king as he. To such high bliss and happy fate Will I the country dedicate, And my sad heart will cease to grieve If he the precious charge receive. Thus is my careful plan matured, Thus for myself is rest secured; Lieges, approve the words I say, Or point ye out some wiser way. Devise your prudent plan. My mind Is fondly to this thought inclined, But men by keen debating move Some middle course which all approve.” The monarch ceased. In answer came The joyous princes' glad acclaim. So peacocks in the rain rejoice And hail the cloud with lifted voice. Murmurs of joy from thousands round Shook the high palace with the sound. Then when the gathered throng had learned His will who right and gain discerned, Peasant and townsman, priest and chief, All met in consultation brief, And soon agreed with one accord Gave answer to their sovereign lord: “King of the land, we know thee old: Thousands of years have o'er thee rolled, Ráma thy son, we pray, anoint,
- **Translation**: 

---

### Verse 6 (Ramayan 0.326)
- **Original**: 308 The Ramayana And at thy side his place appoint Our gallant prince, so brave and strong, Riding in royal state along, Our eyes with joyful pride will see Screened by the shade that shelters thee.” Then spake the king again, as though Their hearts' true wish he sought to know: “These prayers for Ráma's rule suggest One question to my doubting breast. This thing, I pray, with truth explain: Why would ye, while I justly reign, That he, mine eldest son, should bear His part with me as ruling heir?” Then all the people made reply, Peasant and townsman, low and high: “Each noblest gift of form and mind,[091] O Monarch, in thy son we find. Do thou the godlike virtues hear Which Ráma to our hearts endear. So richly blest with graces, none In all the earth excels thy son: Nay, who to match with him may claim In truth, in justice, and in fame? True to his promise, gentle, kind, Unenvious, of grateful mind, Versed in the law and firm of soul, He keeps each sense with strict control. With duteous care he loves to sit By Bráhmans skilled in Holy Writ. Hence brightest glory, ne'er to end, And matchless fame his youth attend. Skilled in the use of spear and shield, And arms which heavenly warriors wield, Supreme in war, unconquered yet
- **Translation**: 

---

### Verse 7 (Ramayan 0.327)
- **Original**: Canto II. The People's Speech. 309 By man, fiend, God in battle met, Whene'er in pomp of war he goes 'Gainst town or city of the foes, He ever comes with LakshmaG back Victorious from the fierce attack. Returning homeward from afar Borne on his elephant or car, He ever to the townsmen bends And greets them as beloved friends, Asks how each son, each servant thrives, How fare our pupils, offerings, wives; And like a father bids us tell, Each for himself, that all is well. If pain or grief the city tries His heart is swift to sympathize. When festive scenes our thoughts employ He like a father shares the joy. High is the fate, O King, that gave Thy Ráma born to bless and save, With filial virtues fair and mild Like Ka[yap old Maríchi's child. Hence to the kingdom's distant ends One general prayer for him ascends. Each man in town and country prays For Ráma's strength, health, length of days. With hearts sincere, their wish the same, The tender girl, the aged dame, Subject and stranger, peasant, hind, One thought impressed on every mind, At evening and at dawning day To all the Gods for Ráma pray. Do thou, O King, of grace comply, And hear the people's longing cry, And let us on the throne by thee
- **Translation**: 

---

### Verse 8 (Ramayan 0.328)
- **Original**: 310 The Ramayana The lotus-tinted Ráma see. O thou who givest boons, attend; A gracious ear, O Monarch, lend And for our weal install, Consenting to our earnest prayer, Thy godlike Ráma Regent Heir, Who seeks the good of all.” Canto III. Dasaratha's Precepts. The monarch with the prayer complied Of suppliant hands, on every side Uplifted like a lotus-bed: And then these gracious words he said: “Great joy and mighty fame are mine Because your loving hearts incline, In full assembly clearly shown To place my Ráma on the throne.” Then to Va[ishmha, standing near, And Vámadeva loud and clear The monarch spoke that all might hear: “'Tis pure and lovely Chaitra now When flowers are sweet on every bough; All needful things with haste prepare That Ráma be appointed heir.”
- **Translation**: 

---

### Verse 9 (Ramayan 0.329)
- **Original**: Canto III. Dasaratha's Precepts. 311 Then burst the people's rapture out In loud acclaim and joyful shout; And when the tumult slowly ceased The king addressed the holy priest: “Give order, Saint, with watchful heed For what the coming rite will need. This day let all things ready wait Mine eldest son to consecrate.” Best of all men of second birth Va [ishmha heard the lord of earth, And gave commandment to the bands Of servitors with lifted hands Who waited on their master's eye: “Now by to-morrow's dawn supply Rich gold and herbs and gems of price And offerings for the sacrifice, Wreaths of white flowers and roasted rice, And oil and honey, separate; New garments and a car of state, An elephant with lucky signs, A fourfold host in ordered lines, The white umbrella, and a pair Of chowries,261 and a banner fair; A hundred vases, row on row, To shine like fire in splendid glow, A tiger's mighty skin, a bull With gilded horns most beautiful. All these, at dawn of coming day, Around the royal shrine array, Where burns the fire's undying ray. Each palace door, each city gate With wreaths of sandal decorate. 261 Whisks, usually made of the long tails of the Yak.
- **Translation**: 

---

### Verse 10 (Ramayan 0.330)
- **Original**: 312 The Ramayana And with the garlands' fragrant scent Let clouds of incense-smoke be blent. Let food of noble kind and taste Be for a hundred thousand placed; Fresh curds with streams of milk bedewed To feed the Bráhman multitude.[092] With care be all their wants supplied. And mid the twice-born chiefs divide Rich largess, with the early morn, And oil and curds and roasted corn. Soon as the sun has shown his light Pronounce the prayer to bless the rite, And then be all the Bráhmans called And in their ordered seats installed. Let all musicians skilled to play, And dancing-girls in bright array Stand ready in the second ring Within the palace of the king. Each honoured tree, each holy shrine With leaves and flowery wreaths entwine, And here and there beneath the shade Be food prepared and presents laid. Then brightly clad, in warlike guise, With long swords girt upon their thighs, Let soldiers of the nobler sort March to the monarch's splendid court.” Thus gave command the twice-born pair To active servants stationed there. Then hastened to the king and said That all their task was duly sped, The king to wise Sumantra spake: “Now quick, my lord, thy chariot take, And hither with thy swiftest speed
- **Translation**: 

---

### Verse 11 (Ramayan 0.331)
- **Original**: Canto III. Dasaratha's Precepts. 313 My son, my noble Ráma lead.” Sumantra, ere the word was given, His chariot from the court had driven, And Ráma, best of all who ride In cars, came sitting by his side. The lords of men had hastened forth From east and west and south and north, Áryan and stranger, those who dwell In the wild wood and on the fell, And as the Gods to Indra, they Showed honour to the king that day. Like Vásav, when his glorious form Is circled by the Gods of storm, Girt in his hall by kings he saw His car-borne Ráma near him draw, Like him who rules the minstrel band Of heaven;262 whose valour filled the land, Of mighty arm and stately pride Like a wild elephant in stride, As fair in face as that fair stone Dear to the moon, of moonbeams grown,263 With noble gifts and grace that took The hearts of all, and chained each look, World-cheering as the Lord of Rain When floods relieve the parching plain. The father, as the son came nigh, Gazed with an ever-thirstier eye. Sumantra helped the prince alight From the good chariot passing bright, 262 Chitraratha, King of the Gandharvas. 263 The Chandrakánta or Moonstone, a sort of crystal supposed to be composed of congealed moonbeams.
- **Translation**: 

---

### Verse 12 (Ramayan 0.332)
- **Original**: 314 The Ramayana And as to meet his sire he went Followed behind him reverent. Then Ráma clomb, the king to seek That terrace like Kailása's peak, And reached the presence of the king, Sumantra closely following. Before his father's face he came, Raised suppliant hands and named his name,264 And bowing lowly as is meet Paid reverence to the monarch's feet. But soon as Da[aratha viewed The prince in humble attitude, He raised him by the hand in haste And his beloved son embraced, Then signed him to a glorious throne, Gem-decked and golden, near his own. Then Ráma, best of Raghu's line, Made the fair seat with lustre shine As when the orient sun upsprings And his pure beam on Meru flings. The glory flashed on roof and wall, And with strange sheen suffused the hall, As when the moon's pure rays are sent Through autumn's star-lit firmament. Then swelled his breast with joy and pride As his dear son the father eyed, E'en as himself more fair arrayed In some clear mirror's face displayed. The aged monarch gazed awhile, Then thus addressed him with a smile, As Ka[yap, whom the worlds revere, Speaks for the Lord of Gods to hear: 264 A customary mark of respect to a superior.
- **Translation**: 

---

### Verse 13 (Ramayan 0.333)
- **Original**: Canto III. Dasaratha's Precepts. 315 “O thou of all my sons most dear, In virtue best, thy father's peer, Child of my consort first in place, Mine equal in her pride of race, Because the people's hearts are bound To thee by graces in thee found, Be thou in Pushya's favouring hour Made partner of my royal power. I know that thou by nature's bent Both modest art and excellent, But though thy gifts no counsel need My love suggests the friendly rede. Mine own dear son, be modest still, And rule each sense with earnest will. Keep thou the evils far away That spring from love and anger's sway. Thy noble course alike pursue In secret as in open view, And every nerve, the love to gain Of ministers and subjects, strain. The happy prince who sees with pride His thriving people satisfied; Whose arsenals with arms are stored, And treasury with golden hoard,— [093] His friends rejoice as joyed the Blest When Amrit crowned their eager quest. So well, my child, thy course maintain, And from all ill thy soul refrain.” The friends of Ráma, gathered nigh, Longing their lord to gratify, Ran to Kau[alyá's bower to tell The tidings that would please her well. She, host of dames, with many a gem,
- **Translation**: 

---

### Verse 14 (Ramayan 0.334)
- **Original**: 316 The Ramayana And gold, and kine rewarded them. Then Ráma paid the reverence due, Mounted the chariot, and withdrew, And to his splendid dwelling drove While crowds to show him honour strove. The people, when the monarch's speech Their willing ears had heard, Were wild with joy as though on each Great gifts had been conferred. With meek and low salute each man Turned to his home away, And there with happy heart began To all the Gods to pray. Canto IV. Ráma Summoned. The crowd dismissed, to high debate The monarch called his peers of state, And, counsel from their lips obtained, Firm in his will his will explained: “To-morrow with auspicious ray The moon in Pushya's sign will stay; Be that the time with happy fate Mine eldest son to consecrate, And let my Ráma, lotus-eyed, As Regent o'er the state preside.”
- **Translation**: 

---

### Verse 15 (Ramayan 0.335)
- **Original**: Canto IV. Ráma Summoned. 317 He sought, within, his charioteer, And cried“Again bring Ráma here.” To Ráma's home Sumantra hied Again to be the prince's guide. His coming, told to Ráma's ear, Suggested anxious doubt and fear. He bade the messenger be led That instant in, and thus he said: “Tell me the cause, omitting naught, Why thou again my house hast sought.” The envoy answered:“Prince, thy sire Has sent thy presence to require. My sender known, 'tis thine to say If thou wilt go or answer nay.” Then Ráma, when he heard his speech, Made haste the royal court to reach. Soon as the monarch was aware His dearest son was waiting there, Eager the parley to begin He bade them lead the prince within, Soon as he passed the chamber door The hero bent him to the floor, And at a distance from his seat Raised his joined hands his sire to greet. The monarch raised him from the ground, And loving arms about him wound, Then pointed to a seat that shone With gold for him to rest upon. “Aged am I,” he said,“and worn; In life's best joys my share have borne; Rites to the Gods, in hundreds, paid, With gifts of corn and largess made. I yearned for sons: my life is blest
- **Translation**: 

---

### Verse 16 (Ramayan 0.336)
- **Original**: 318 The Ramayana With them and thee of sons the best. No debt to saints or Bráhmans, no, Nor spirits, Gods, or self I owe. One duty now remains alone, To set thee on thy father's throne. Now therefore, Ráma, hear my rede, And mark my words with duteous heed: This day the peoples' general voice, Elects thee king of love and choice, And I, consenting to the prayer, Will make thee, darling, Regent Heir. Dread visions, each returning night, With evil omens scare my sight. Red meteors with a fearful sound Shoot wildly downward to the ground, While tempests lash the troubled air; And they who read the stars declare That, leagued against my natal sign, Ráhu,265 the Sun,266 and Mars combine. When portents dire as these appear, A monarch's death or woe is near. Then while my senses yet are spared, And thought and will are unimpaired, Be thou, my son, anointed king: Men's fancy is a fickle thing. To-day the moon, in order due, Entered the sign Punarvasu,267 To-morrow, as the wise foretell, 265 Ráhu, the ascending node, is in mythology a demon with the tail of a dragon whose head was severed from his body by VishGu, but being immortal, the head and tail retained their separate existence and being transferred to the stellar sphere became the authors of eclipses; the first especially by endeavouring to swallow the sun and moon. 266 In eclipse. 267 The seventh of the lunar asterisms.
- **Translation**: 

---

### Verse 17 (Ramayan 0.337)
- **Original**: Canto IV. Ráma Summoned. 319 In Pushya's favouring stars will dwell: Then on the throne shalt thou be placed. My soul, prophetic, counsels haste: Thee, O my son, to-morrow I As Regent Heir will sanctify. So till the coming night be passed Do thou and Sítá strictly fast: From worldly thoughts thy soul refrain, And couched on holy grass remain. [094] And let thy trusted lords attend In careful watch upon their friend, For, unexpected, check and bar Our weightiest counsels often mar. While Bharat too is far away Making with royal kin his stay, I deem the fittest time of all Thee, chosen Regent, to install. It may be Bharat still has stood True to the counsels of the good, Faithful to thee with tender trust, With governed senses, pure and just. But human minds, too well I know, Will sudden changes undergo, And by their constant deeds alone The virtue of the good is shown. Now, Ráma, go. My son, good night! Fixt is to-morrow for the rite.” Then Ráma paid the reverence due, And quickly to his home withdrew. He passed within, nor lingered there, But sought his mother's mansion, where The dame in linen robes arrayed Devoutly in the chapel prayed
- **Translation**: 

---

### Verse 18 (Ramayan 0.338)
- **Original**: 320 The Ramayana To Fortune's Queen, with utterance checked, That she her Ráma would protect. There was Sumitrá too, and there Was Lakshma G led by loving care: And when the royal choice they knew Sítá in haste was summoned too. Absorbed, with half-shut eyes, the queen Attended by the three was seen. She knew that Pushya's lucky hour Would raise her son to royal power, So fixed with bated breath each thought On God supreme, by all men sought. To her, as thus she knelt and prayed, Ráma drew near, due reverence paid, And then to swell his mother's joy, Thus spoke her own beloved boy; “O mother dear, my sire's decree Entrusts the people's weal to me. To-morrow I, for so his will, Anointed king, the throne shall fill. The few last hours till night shall end Sítá with me must fasting spend, For so my father has decreed, And holy priests with him agreed. What vows soever thou mayst deem My consecration's eve beseem, Do thou, sweet mother, for my sake And for beloved Sítá's make.” When the glad news Kau[alyá heard, So long desired, so long deferred, While tears of joy her utterance broke, In answer to her son she spoke: “Long be thy life, my darling: now
- **Translation**: 

---

### Verse 19 (Ramayan 0.339)
- **Original**: Canto IV. Ráma Summoned. 321 Thy prostrate foes before thee bow. Live long and with thy bright success My friends and dear Sumitrá's bless. Surely the stars were wondrous fair When thee, sweet son, thy mother bare, That thy good gifts such love inspire And win the favour of thy sire. With thee I travailed not in vain; Those lotus eyes reward my pain, And all the glory of the line Of old Ikshváku will be thine.” He smiled, and on his brother gazed Who sate with reverent hands upraised, And said:“My brother, thou must be Joint-ruler of this land with me. My second self thou, LakshmaG, art, And in my fortune bearest part. Be thine, Sumitrá's son, to know The joys from regal power that flow. My life itself, the monarch's seat, For thy dear sake to me are sweet.” Thus Ráma to his brother said, To both his mothers268 bowed his head, And then with Sítá by his side To his own house the hero hied. 268 Kau [alyá and Sumitrá.
- **Translation**: 

---

### Verse 20 (Ramayan 0.340)
- **Original**: 322 The Ramayana Canto V. Ráma's Fast. Then Saint Va[ishmha to the king Came ready at his summoning. “Now go,” exclaimed the monarch,“thou Enriched by fervent rite and vow, For Ráma and his wife ordain The fast, that joy may bless his reign.” The best of those who Scripture know Said to the king,“My lord, I go.” To Ráma's house Va[ishmha hied, The hero's fast by rule to guide, And skilled in sacred texts to tell Each step to him instructed well. Straight to Prince Ráma's high abode, That like a cloud pale-tinted showed, Borne in his priestly car he rode. Two courts he passed, and in the third He stayed his car. Then Ráma heard The holy sage was come, and flew To honour him with honour due. He hastened to the car and lent His hand to aid the priest's descent. Then spoke Va[ishmha words like these, Pleased with his reverent courtesies, With pleasant things his heart to cheer Who best deserved glad news to hear: “Prince, thou hast won thy father's grace, And thine will be the Regent's place: Now with thy Sítá, as is right, In strictest fasting spend the night,[095]
- **Translation**: 

---



--- End of Ramayan_batch_17.md ---


--- Start of Ramayan_batch_18.md ---

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

### Verse 1 (Ramayan 0.341)
- **Original**: Canto V. Ráma's Fast. 323 For when the morrow's dawn is fair The king will consecrate his heir: So Nahush,269 as the wise relate, Yayáti joyed to consecrate.” Thus having said, Va[ishmha next Ordained the fast by rule and text, For Ráma faithful to his vows And the Videhan dame his spouse. Then from the prince's house he hied With courteous honours gratified. Round Ráma gathered every friend In pleasant talk a while to spend. He bade good night to all at last, And to his inner chamber passed. Then Ráma's house shone bright and gay With men and maids in glad array, As in the morning some fair lake When all her lotuses awake, And every bird that loves the flood Flits joyous round each opening bud. Forth from the house Va[ishmha drove, That with the king's in splendour strove, And all the royal street he viewed Filled with a mighty multitude The eager concourse blocked each square, Each road and lane and thoroughfare, And joyous shouts on every side Rose like the roar of Ocean's tide, As streams of men together came With loud huzza and glad acclaim. The ways were watered, swept and clean, 269 A king of the Lunar race, and father of Yayáti.
- **Translation**: 

---

### Verse 2 (Ramayan 0.342)
- **Original**: 324 The Ramayana And decked with flowers and garlands green And all Ayodhyá shone arrayed With banners on the roofs that played. Men, women, boys with eager eyes, Expecting when the sun should rise, Stood longing for the herald ray Of Ráma's consecration day, To see, a source of joy to all, The people-honoured festival. The priest advancing slowly through The mighty crowd he cleft in two, Near to the monarch's palace drew. He sought the terrace, by the stair, Like a white cloud-peak high in air, The reverend king of men to meet Who sate upon his splendid seat: Thus will V[ihaspati arise To meet the monarch of the skies. But when the king his coming knew, He left his throne and near him drew Questioned by him Va[ishmha said That all his task was duly sped. Then all who sate there, honouring Va [ishmha, rose as rose the king. Va [ishmha bade his lord adieu, And all the peers, dismissed, withdrew. Then as a royal lion seeks His cave beneath the rocky peaks, So to the chambers where abode His consorts Da[aratha strode. Full-thronged were those delightful bowers With women richly dressed, And splendid as the radiant towers
- **Translation**: 

---

### Verse 3 (Ramayan 0.343)
- **Original**: Canto VI. The City Decorated. 325 Where Indra loves to rest. Then brighter flashed a thousand eyes With the light his presence lent, As, when the moon begins to rise The star thronged firmament. Canto VI. The City Decorated. Then Ráma bathed in order due, His mind from worldly thoughts withdrew, And with his large-eyed wife besought NáráyaG, as a votary ought. Upon his head the brimming cup Of holy oil he lifted up, Then placed within the kindled fire The offering to that heavenly Sire, And as he sipped the remnant prayed To Him for blessing and for aid. Then with still lips and tranquil mind With his Videhan he reclined, In VishGu's chapel, on a bed Where holy grass was duly spread, While still the prince's every thought The God supreme, NáráyaG, sought. One watch remained the night to close When Ráma from his couch arose, And bade the men and maids adorn His palace for the solemn morn. He heard the bards and heralds raise Auspicious strains of joy and praise; And breathed devout, with voice restrained,
- **Translation**: 

---

### Verse 4 (Ramayan 0.344)
- **Original**: 326 The Ramayana The hymn for morning rites ordained; Then, with his head in reverence bowed, Praised Madhu's conquering foe aloud, And, in pure linen robes arrayed, The priests to raise their voices prayed. Obedient to the summons they Proclaimed to all the festal day. The Bráhmans' voices, deep and sweet, Resounded through the crowded street, And echoed through Ayodhyá went By many a loud-toned instrument. Then all the people joyed to hear That Ráma with his consort dear Had fasted till the morning light In preparation for the rite. Swiftly the joyful tidings through Ayodhyá's crowded city flew, And soon as dawn appeared, each man To decorate the town began.[096] In all the temples bright and fair As white clouds towering in the air, In streets, and where the cross-ways met, Where holy fig-trees had been set, In open square, in sacred shade, Where merchants' shops their wealth displayed, On all the mansions of the great, And householders of wealth and state, Where'er the people loved to meet, Where'er a tree adorned the street, Gay banners floated to the wind, And ribands round the staves were twined. Then clear the singers' voices rang, As, charming mind and ear, they sang. Here players shone in bright attire,
- **Translation**: 

---

### Verse 5 (Ramayan 0.345)
- **Original**: Canto VI. The City Decorated. 327 There dancing women swelled the quire. Each with his friend had much to say Of Ráma's consecration-day: Yea, even children, as they played At cottage doors beneath the shade. The royal street with flowers was strown Which loving hands in heaps had thrown, And here and there rich incense lent Its fragrance to the garland's scent; And all was fresh and fair and bright In honour of the coming rite. With careful foresight to illume With borrowed blaze the midnight gloom, The crowds erected here and there Trees in each street gay lamps to bear. The city thus from side to side In festal guise was beautified. The people of the town who longed To view the rite together thronged, And filling every court and square Praised the good king in converse there: “Our high-souled king! He throws a grace On old Ikshváku's royal race. He feels his years' increasing weight, And makes his son associate. Great joy to us the choice will bring Of Ráma for our lord and king. The good and bad to him are known, And long will he protect his own. No pride his prudent breast may swell, Most just, he loves his brothers well, And to us all that love extends, Cherished as brothers and as friends. Long may our lord in life remain,
- **Translation**: 

---

### Verse 6 (Ramayan 0.346)
- **Original**: 328 The Ramayana Good Da [aratha, free from stain, By whose most gracious favour we Ráma anointed king shall see.” Such were the words the townsmen spoke Heard by the gathering countryfolk, Who from the south, north, east, and west, Stirred by the joyful tidings, pressed. For by their eager longing led To Ráma's consecration sped The villagers from every side, And filled Ayodhyá's city wide. This way and that way strayed the crowd, While rose a murmur long and loud, As when the full moon floods the skies And Ocean's waves with thunder rise. That town, like Indra's city fair, While peasants thronged her ways, Tumultuous roared like Ocean, where Each flood-born monster plays. Canto VII. Manthará's Lament. It chanced a slave-born handmaid, bred With Queen Kaikeyí, fancy-led, Mounted the stair and stood upon The terrace like the moon that shone. Thence Manthará at ease surveyed Ayodhyá to her eyes displayed, Where water cooled the royal street, Where heaps of flowers were fresh and sweet,
- **Translation**: 

---

### Verse 7 (Ramayan 0.347)
- **Original**: Canto VII. Manthará's Lament. 329 And costly flags and pennons hung On roof and tower their shadow flung; With covered ways prepared in haste, And many an awning newly placed; With sandal-scented streams bedewed, Thronged by a new bathed multitude: Whose streets were full of Bráhman bands With wreaths and sweetmeats in their hands. Loud instruments their music raised, And through the town, where'er she gazed, The doors of temples glittered white, And the maid marvelled at the sight. Of Ráma's nurse who, standing by, Gazed with a joy-expanded eye, In robes of purest white attired, The wondering damsel thus inquired: “Does Ráma's mother give away Rich largess to the crowds to-day, On some dear object fondly bent, Or blest with measureless content? What mean these signs of rare delight On every side that meet my sight? Say, will the king with joy elate Some happy triumph celebrate?”
- **Translation**: 

---

### Verse 8 (Ramayan 0.348)
- **Original**: 330 The Ramayana The nurse, with transport uncontrolled, Her glad tale to the hump-back told: “Our lord the king to-morrow morn Will consecrate his eldest-born, And raise, in Pushya's favouring hour, Prince Ráma to the royal power.” As thus the nurse her tidings spoke, Rage in the hump-back's breast awoke. Down from the terrace, like the head Of high Kailása's hill, she sped. Sin in her thoughts, her soul aflame, Where Queen Kaikeyí slept, she came:[097] “Why sleepest thou?” she cried,“arise, Peril is near, unclose thine eyes. Ah, heedless Queen, too blind to know What floods of sin above thee flow! Thy boasts of love and grace are o'er: Thine is the show and nothing more. His favour is an empty cheat, A torrent dried by summer's heat.” Thus by the artful maid addressed In cruel words from raging breast, The queen, sore troubled, spoke in turn; “What evil news have I to learn? That mournful eye, that altered cheek Of sudden woe or danger speak.” Such were the words Kaikeyí said: Then Manthará, her eyeballs red With fury, skilled with treacherous art To grieve yet more her lady's heart, From Ráma, in her wicked hate, Kaikeyí's love to alienate,
- **Translation**: 

---

### Verse 9 (Ramayan 0.349)
- **Original**: Canto VII. Manthará's Lament. 331 Upon her evil purpose bent Began again most eloquent: “Peril awaits thee swift and sure, And utter woe defying cure; King Da[aratha will create Prince Ráma Heir Associate. Plunged in the depths of wild despair, My soul a prey to pain and care, As though the flames consumed me, zeal Has brought me for my lady's weal, Thy grief, my Queen, is grief to me: Thy gain my greatest gain would be. Proud daughter of a princely line, The rights of consort queen are thine. How art thou, born of royal race, Blind to the crimes that kings debase? Thy lord is gracious, to deceive, And flatters, but thy soul to grieve, While thy pure heart that thinks no sin Knows not the snares that hem thee in. Thy husband's lips on thee bestow Soft soothing word, an empty show: The wealth, the substance, and the power This day will be Kau[alyá's dower. With crafty soul thy child he sends To dwell among thy distant friends, And, every rival far from sight, To Ráma gives the power and might. Ah me! for thou, unhappy dame, Deluded by a husband's name, With more than mother's love hast pressed A serpent to thy heedless breast, And cherished him who works thee woe, No husband but a deadly foe.
- **Translation**: 

---

### Verse 10 (Ramayan 0.350)
- **Original**: 332 The Ramayana For like a snake, unconscious Queen, Or enemy who stabs unseen, King Da[aratha all untrue Has dealt with thee and Bharat too. Ah, simple lady, long beguiled By his soft words who falsely smiled! Poor victim of the guileless breast, A happier fate thou meritest. For thee and thine destruction waits When he Prince Ráma consecrates. Up, lady, while there yet is time; Preserve thyself, prevent the crime. Up, from thy careless ease, and free Thyself, O Queen, thy son, and me!” Delighted at the words she said, Kaikeyí lifted from the bed, Like autumn's moon, her radiant head, And joyous at the tidings gave A jewel to the hump-back slave; And as she gave the precious toy She cried in her exceeding joy: “Take this, dear maiden, for thy news Most grateful to mine ear, and choose What grace beside most fitly may The welcome messenger repay. I joy that Ráma gains the throne: Kau [alyá's son is as mine own.” Canto VIII. Manthará's Speech.
- **Translation**: 

---

### Verse 11 (Ramayan 0.351)
- **Original**: Canto VIII. Manthará's Speech. 333 The damsel's breast with fury burned: She answered, as the gift she spurned: “What time, O simple Queen, is this For idle dreams of fancied bliss? Hast thou not sense thy state to know, Engulfed in seas of whelming woe; Sick as I am with grief and pain My lips can scarce a laugh restrain To see thee hail with ill-timed joy A peril mighty to destroy. I mourn for one so fondly blind: What woman of a prudent mind Would welcome, e'en as thou hast done, The lordship of a rival's son, Rejoiced to find her secret foe Empowered, like death, to launch the blow; I see that Ráma still must fear Thy Bharat, to his throne too near. Hence is my heart disquieted, For those who fear are those we dread. Lakshma G, the mighty bow who draws, With all his soul serves Ráma's cause; And chains as strong to Bharat bind Zatrughna, with his heart and mind, Now next to Ráma, lady fair, Thy Bharat is the lawful heir: And far remote, I ween, the chance That might the younger two advance. Yes, Queen, 'tis Ráma that I dread, Wise, prompt, in warlike science bred; And oh, I tremble when I think Of thy dear child on ruin's brink. [098] Blest with a lofty fate is she, Kau [alyá; for her son will be
- **Translation**: 

---

### Verse 12 (Ramayan 0.352)
- **Original**: 334 The Ramayana Placed, when the moon and Pushya meet, By Bráhmans on the royal seat, Thou as a slave in suppliant guise Must wait upon Kau[alyá's eyes, With all her wealth and bliss secured And glorious from her foes assured. Her slave with us who serve thee, thou Wilt see thy son to Ráma bow, And Sítá's friends exult o'er all, While Bharat's wife shares Bharat's fall.” As thus the maid in wrath complained, Kaikeyí saw her heart was pained, And answered eager in defence Of Ráma's worth and excellence: “Nay, Ráma, born the monarch's heir, By holy fathers trained with care, Virtuous, grateful, pure, and true, Claims royal sway as rightly due. He, like a sire, will long defend Each brother, minister, and friend. Then why, O hump-back, art thou pained To hear that he the throne has gained? Be sure when Ráma's empire ends, The kingdom to my son descends, Who, when a hundred years are flown, Shall sit upon his fathers' throne. Why is thine heart thus sad to see The joy that is and long shall be, This fortune by possession sure And hopes which we may count secure? Dear as the darling son I bore Is Ráma, yea, or even more. Most duteous to Kau[alyá, he
- **Translation**: 

---

### Verse 13 (Ramayan 0.353)
- **Original**: Canto VIII. Manthará's Speech. 335 Is yet more dutiful to me. What though he rule, we need not fear: His brethren to his soul are dear. And if the throne Prince Ráma fill Bharat will share the empire still.” She ceased. The troubled damsel sighed Sighs long and hot, and thus replied: “What madness has possessed thy mind, To warnings deaf, to dangers blind? Canst thou not see the floods of woe That threaten o'er thine head to flow: First Ráma will the throne acquire, Then Ráma's son succeed his sire, While Bharat will neglected pine Excluded from the royal line. Not all his sons, O lady fair, The kingdom of a monarch share: All ruling when a sovereign dies Wild tumult in the state would rise. The eldest, be he good or ill, Is ruler by the father's will. Know, tender mother, that thy son Without a friend and all undone, Far from the joyous ease of home An alien from his race will roam. I sped to thee for whom I feel, But thy fond heart mistakes my zeal, Thy hand a present would bestow Because thy rival triumphs so. When Ráma once begins his sway Without a foe his will to stay, Thy darling Bharat he will drive To distant lands if left alive.
- **Translation**: 

---

### Verse 14 (Ramayan 0.354)
- **Original**: 336 The Ramayana By thee the child was sent away Beneath his grandsire's roof to stay. Even in stocks and stones perforce Will friendship spring from intercourse. The youngZatrughna too would go With Bharat, for he loved him so. As LakshmaG still to Ráma cleaves, He his dear Bharat never leaves. There is an ancient tale they tell: A tree the foresters would fell Was saved by reeds that round it stood, For love that sprang of neighbourhood. So LakshmaG Ráma will defend, And each on each for aid depend. Such fame on earth their friendship wins As that which binds the Heavenly Twins. And Ráma ne'er will purpose wrong To LakshmaG, for their love is strong. But Bharat, Oh, of this be sure, Must evil at his hands endure. Come, Ráma from his home expel An exile in the woods to dwell. The plan, O Queen, which I advise Secures thy weal if thou be wise. So we and all thy kith and kin Advantage from thy gain shall win. Shall Bharat, meet for happier fate, Born to endure his rival's hate, With all his fortune ruined cower And dread his brother's mightier power! Up, Queen, to save thy son, arise; Prostrate at Ráma's feet he lies. So the proud elephant who leads His trooping consorts through the reeds
- **Translation**: 

---

### Verse 15 (Ramayan 0.355)
- **Original**: Canto IX. The Plot. 337 Falls in the forest shade beneath The lion's spring and murderous teeth. Scorned by thee in thy bliss and pride Kau [alyá was of old defied, And will she now forbear to show The vengeful rancour of a foe? O Queen, thy darling is undone When Ráma's hand has once begun Ayodhyá's realm to sway, Come, win the kingdom for thy child And drive the alien to the wild In banishment to-day.” Canto IX. The Plot. As fury lit Kaikeyí's eyes She spoke with long and burning sighs: [099] “This day my son enthroned shall see, And Ráma to the woods shall flee. But tell me, damsel, if thou can, A certain way, a skilful plan That Bharat may the empire gain, And Ráma's hopes be nursed in vain.” The lady ceased. The wicked maid The mandate of her queen obeyed, And darkly plotting Ráma's fall Responded to Kaikeyí's call.
- **Translation**: 

---

### Verse 16 (Ramayan 0.356)
- **Original**: 338 The Ramayana “I will declare, do thou attend, How Bharat may his throne ascend. Dost thou forget what things befell? Or dost thou feign, remembering well? Or wouldst thou hear my tongue repeat A story for thy need so meet? Gay lady, if thy will be so, Now hear the tale of long ago, And when my tongue has done its part Ponder the story in thine heart. When Gods and demons fought of old, Thy lord, with royal saints enrolled, Sped to the war with thee to bring His might to aid the Immortals' King. Far to the southern land he sped Where DaG ak's mighty wilds are spread, To Vaijayanta's city swayed By Zambara, whose flag displayd The hugest monster of the sea. Lord of a hundred wiles was be; With might which Gods could never blame Against the King of Heaven he came. Then raged the battle wild and dread, And mortal warriors fought and bled; The fiends by night with strength renewed Charged, slew the sleeping multitude. Thy lord, King Da[aratha, long Stood fighting with the demon throng, But long of arm, unmatched in strength, Fell wounded by their darts at length. Thy husband, senseless, by thine aid Was from the battle field conveyed, And wounded nigh to death thy lord Was by thy care to health restored.
- **Translation**: 

---

### Verse 17 (Ramayan 0.357)
- **Original**: Canto IX. The Plot. 339 Well pleased the grateful monarch sware To grant thy first and second prayer. Thou for no favour then wouldst sue, The gifts reserved for season due; And he, thy high-souled lord, agreed To give the boons when thou shouldst need. Myself I knew not what befell, But oft the tale have heard thee tell, And close to thee in friendship knit Deep in my heart have treasured it. Remind thy husband of his oath, Recall the boons and claim them both, That Bharat on the throne be placed With rites of consecration graced, And Ráma to the woods be sent For twice seven years of banishment. Go, Queen, the mourner's chamber270 seek, With angry eye and burning cheek; And with disordered robes and hair On the cold earth lie prostrate there. When the king comes still mournful lie, Speak not a word nor meet his eye, But let thy tears in torrent flow, And lie enamoured of thy woe. Well do I know thou long hast been, And ever art, his darling queen. For thy dear sake, O well-loved dame, The mighty king would brave the flame, But ne'er would anger thee, or brook To meet his favourite's wrathful look. Thy loving lord would even die 270 Literallythe chamber of wrath,a “growlery,” a small, dark, unfurnished room to which it seems, the wives and ladies of the king betook themselves when offended and sulky.
- **Translation**: 

---

### Verse 18 (Ramayan 0.358)
- **Original**: 340 The Ramayana Thy fancy, Queen, to gratify, And never could he arm his breast To answer nay to thy request. Listen and learn, O dull of sense, Thine all-resistless influence. Gems he will offer, pearls and gold: Refuse his gifts, be stern and cold. Those proffered boons at length recall, And claim them till he grants thee all. And O my lady, high in bliss, With heedful thought forget not this. When from the ground his queen he lifts And grants again the promised gifts, Bind him with oaths he cannot break And thy demands unflnching, make. That Ráma travel to the wild Five years and nine from home exiled, And Bharat, best of all who reign, The empire of the land obtain. For when this term of years has fled Over the banished Ráma's head, Thy royal son to vigour grown And rooted firm will stand alone. The king, I know, is well inclined, And this the hour to move his mind. Be bold: the threatened rite prevent, And force the king from his intent.” She ceased. So counselled to her bane Disguised beneath a show of gain, Kaikeyí in her joy and pride To Manthará again replied: “Thy sense I envy, prudent maid; With sagest lore thy lids persuade.
- **Translation**: 

---

### Verse 19 (Ramayan 0.359)
- **Original**: Canto IX. The Plot. 341 No hump-back maid in all the earth, For wise resolve, can match thy worth. Thou art alone with constant zeal Devoted to thy lady's weal. Dear girl, without thy faithful aid I had not marked the plot he laid. [100] Full of all guile and sin and spite Misshapen hump-backs shock the sight: But thou art fair and formed to please, Bent like a lily by the breeze. I look thee o'er with watchful eye, And in thy frame no fault can spy; The chest so deep, the waist so trim, So round the lines of breast and limb.271 Thy cheeks with moonlike beauty shine, And the warm wealth of youth is thine. Thy legs, my girl, are long and neat, And somewhat long thy dainty feet, While stepping out before my face Thou seemest like a crane to pace. The thousand wiles are in thy breast Which Zambara the fiend possessed, And countless others all thine own, O damsel sage, to thee are known. Thy very hump becomes thee too, O thou whose face is fair to view, For there reside in endless store Plots, wizard wiles, and warrior lore. A golden chain I'll round it fling When Ráma's flight makes Bharat king: Yea, polished links of finest gold, When once the wished for prize I hold 271 In these four lines I do not translate faithfully, and I do not venture to follow Kaikeyí farther in her eulogy of the hump-back's charms.
- **Translation**: 

---

### Verse 20 (Ramayan 0.360)
- **Original**: 342 The Ramayana With naught to fear and none to hate, Thy hump, dear maid, shall decorate. A golden frontlet wrought with care, And precious jewels shalt thou wear: Two lovely robes around thee fold, And walk a Goddess to behold, Bidding the moon himself compare His beauty with a face so fair. With scent of precious sandal sweet Down to the nails upon thy feet, First of the household thou shalt go And pay with scorn each battled foe.” Kaikeyí's praise the damsel heard, And thus again her lady stirred, Who lay upon her beauteous bed Like fire upon the altar fed: “Dear Queen, they build the bridge in vain When swollen streams are dry again. Arise, thy glorious task complete, And draw the king to thy retreat.” The large-eyed lady left her bower Exulting in her pride of power, And with the hump-back sought the gloom And silence of the mourner's room. The string of priceless pearls that hung Around her neck to earth she flung, With all the wealth and lustre lent By precious gem and ornament. Then, listening to her slave's advice, Lay, like a nymph from Paradise. As on the ground her limbs she laid Once more she cried unto the maid:
- **Translation**: 

---



--- End of Ramayan_batch_18.md ---


--- Start of Ramayan_batch_19.md ---

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

### Verse 1 (Ramayan 0.361)
- **Original**: Canto IX. The Plot. 343 “Soon must thou to the monarch say Kaikeyí's soul has past away, Or, Ráma banished as we planned, My son made king shall rule the land. No more for gold and gems I care, For brave attire or dainty fare. If Ráma should the throne ascend, That very hour my life will end.” The royal lady wounded through The bosom with the darts that flew Launched from the hump-back's tongue Pressed both her hands upon her side, And o'er and o'er again she cried With wildering fury stung: “Yes, it shall be thy task to tell That I have hurried hence to dwell In Yáma's realms of woe, Or happy Bharat shall be king, And doomed to years of wandering Kau [alyá's son shall go. I heed not dainty viands now Fair wreaths of flowers to twine my brow, Soft balm or precious scent: My very life I count as naught, Nothing on earth can claim my thought But Ráma's banishment.” She spoke these words of cruel ire; Then stripping off her gay attire, The cold bare floor she pressed. So, falling from her home on high, Some lovely daughter of the sky Upon the ground might rest. With darkened brow and furious mien,
- **Translation**: 

---

### Verse 2 (Ramayan 0.362)
- **Original**: 344 The Ramayana Stripped of her gems and wreath, the queen In spotless beauty lay, Like heaven obscured with gathering cloud, When shades of midnight darkness shroud Each star's expiring ray. Canto X. Dasaratha's Speech. As Queen Kaikeyí thus obeyed The sinful counsel of her maid She sank upon the chamber floor, As sinks in anguish, wounded sore, An elephant beneath the smart Of the wild hunter's venomed dart. The lovely lady in her mind Revolved the plot her maid designed, And prompt the gain and risk to scan She step by step approved the plan. Misguided by the hump-back's guile She pondered her resolve awhile, As the fair path that bliss secured The miserable lady lured,[101] Devoted to her queen, and swayed By hopes of gain and bliss, the maid Rejoiced, her lady's purpose known, And deemed the prize she sought her own. Then bent upon her purpose dire, Kaikeyí with her soul on fire, Upon the floor lay, languid, down, Her brows contracted in a frown. The bright-hued wreath that bound her hair,
- **Translation**: 

---

### Verse 3 (Ramayan 0.363)
- **Original**: Canto X. Dasaratha's Speech. 345 Chains, necklets, jewels rich and rare, Stripped off by her own fingers lay Spread on the ground in disarray, And to the floor a lustre lent As stars light up the firmament. Thus prostrate in the mourner's cell, In garb of woe the lady fell, Her long hair in a single braid, Like some fair nymph of heaven dismayed.272 The monarch, Ráma to install, With thoughtful care had ordered all, And now within his home withdrew, Dismissing first his retinue. Now all the town has heard, thought he, What joyful rite the morn will see. So turned he to her bower to cheer With the glad news his darling's ear. Majestic, as the Lord of Night, When threatened by the Dragon's might, Bursts radiant on the evening sky Pale with the clouds that wander by, So Da[aratha, great in fame, To Queen Kaikeyí's palace came. There parrots flew from tree to tree, And gorgeous peacocks wandered free, While ever and anon was heard The note of some glad water-bird. Here loitered dwarf and hump-backed maid, There lute and lyre sweet music played. 272 These verses are evidently an interpolation. They contain nothing that has not been already related: the words only are altered. As the whole poem could not be recited at once, the rhapsodists at the beginning of a fresh recitation would naturally remind their hearers of the events immediately preceding.
- **Translation**: 

---

### Verse 4 (Ramayan 0.364)
- **Original**: 346 The Ramayana Here, rich in blossom, creepers twined O'er grots with wondrous art designed, There Champac and A[oka flowers Hung glorious o'er the summer bowers, And mid the waving verdure rose Gold, silver, ivory porticoes. Through all the months in ceaseless store The trees both fruit and blossom bore. With many a lake the grounds were graced; Seats gold and silver, here were placed; Here every viand wooed the taste, It was a garden meet to vie E'en with the home of Gods on high. Within the mansion rich and vast The mighty Da[aratha passed: Not there was his beloved queen On her fair couch reclining seen. With love his eager pulses beat For the dear wife he came to meet, And in his blissful hopes deceived, He sought his absent love and grieved. For never had she missed the hour Of meeting in her sumptuous bower, And never had the king of men Entered the empty room till then. Still urged by love and anxious thought News of his favourite queen he sought, For never had his loving eyes Found her or selfish or unwise. Then spoke at length the warder maid, With hands upraised and sore afraid: “My Lord and King, the queen has sought The mourner's cell with rage distraught.”
- **Translation**: 

---

### Verse 5 (Ramayan 0.365)
- **Original**: Canto X. Dasaratha's Speech. 347 The words the warder maiden said He heard with soul disquieted, And thus as fiercer grief assailed, His troubled senses wellnigh failed. Consumed by torturing fires of grief The king, the world's imperial chief, His lady lying on the ground In most unqueenly posture, found. The aged king, all pure within, Saw the young queen resolved on sin, Low on the ground, his own sweet wife, To him far dearer than his life, Like some fair creeping plant uptorn, Or like a maid of heaven forlorn, A nymph of air or Goddess sent From Swarga down in banishment. As some wild elephant who tries To soothe his consort as she lies Struck by the hunter's venomed dart, So the great king disturbed in heart, Strove with soft hand and fond caress To soothe his darling queen's distress, And in his love addressed with sighs The lady of the lotus eyes: “I know not, Queen, why thou shouldst be Thus angered to the heart with me. Say, who has slighted thee, or whence Has come the cause of such offence That in the dust thou liest low, And rendest my fond heart with woe, As if some goblin of the night Had struck thee with a deadly blight, And cast foul influence on her
- **Translation**: 

---

### Verse 6 (Ramayan 0.366)
- **Original**: 348 The Ramayana Whose spells my loving bosom stir? I have Physicians famed for skill, Each trained to cure some special ill: My sweetest lady, tell thy pain, And they shall make thee well again. Whom, darling, wouldst thou punished see? Or whom enriched with lordly fee?[102] Weep not, my lovely Queen, and stay This grief that wears thy frame away; Speak, and the guilty shall be freed. The guiltless be condemned to bleed, The poor enriched, the rich abased, The low set high, the proud disgraced. My lords and I thy will obey, All slaves who own thy sovereign sway; And I can ne'er my heart incline To check in aught one wish of thine. Now by my life I pray thee tell The thoughts that in thy bosom dwell. The power and might thou knowest well, Should from thy breast all doubt expel. I swear by all my merit won, Speak, and thy pleasure shall be done. Far as the world's wide bounds extend My glorious empire knows no end. Mine are the tribes in eastern lands, And those who dwell on Sindhu's sands: Mine is Suráshmra, far away, Suvíra's realm admits my sway. My best the southern nations fear, The Angas and the Vangas hear. And as lord paramount I reign O'er Magadh and the Matsyas' plain,
- **Translation**: 

---

### Verse 7 (Ramayan 0.367)
- **Original**: Canto XI. The Queen's Demand. 349 Ko [al, and Ká[i's wide domain:273 All rich in treasures of the mine, In golden corn, sheep, goats, and kine. Choose what thou wilt. Kaikeyí, thence: But tell me, O my darling, whence Arose thy grief, and it shall fly Like hoar-frost when the sun is high.” She, by his loving words consoled, Longed her dire purpose to unfold, And sought with sharper pangs to wring The bosom of her lord the king. Canto XI. The Queen's Demand. To him enthralled by love, and blind, Pierced by his darts who shakes the mind,274 Kaikeyí with remorseless breast Her grand purpose thus expressed: “O King, no insult or neglect Have I endured, or disrespect. One wish I have, and faith would see That longing granted, lord, by thee. Now pledge thy word if thou incline To listen to this prayer of mine, Then I with confidence will speak, And thou shalt hear the boon I seek.” 273 The [lokaor distich which I have been forced to expand into these nine lines is evidently spurious, but is found in all the commented MSS. which Schlegel consulted. 274 Manmatha, Mind-disturber, a name of Káma or Love.
- **Translation**: 

---

### Verse 8 (Ramayan 0.368)
- **Original**: 350 The Ramayana Ere she had ceased, the monarch fell, A victim to the lady's spell, And to the deadly snare she set Sprang, like a roebuck to the net. Her lover raised her drooping head, Smiled, playing with her hair, and said: “Hast thou not learnt, wild dame, till now That there is none so dear as thou To me thy loving husband, save My Ráma bravest of the brave? By him my race's high-souled heir, By him whom none can match, I swear, Now speak the wish that on thee weighs: By him whose right is length of days, Whom if my fond paternal eye Saw not one hour I needs must die,— I swear by Ráma my dear son, Speak, and thy bidding shall be done. Speak, darling; if thou choose, request To have the heart from out my breast; Regard my words, sweet love, and name The wish thy mind thinks fit to frame. Nor let thy soul give way to doubt: My power should drive suspicion out. Yea, by my merits won I swear, Speak, darling, I will grant thy prayer.” The queen, ambitious, overjoyed To see him by her plot decoyed, More eager still her aims to reach, Spoke her abominable speech: “A boon thou grantest, nothing loth, And swearest with repeated oath. Now let the thirty Gods and three
- **Translation**: 

---

### Verse 9 (Ramayan 0.369)
- **Original**: Canto XI. The Queen's Demand. 351 My witnesses, with Indra, be. Let sun and moon and planets hear, Heaven, quarters, day and night, give ear. The mighty world, the earth outspread, With bards of heaven and demons dread; The ghosts that walk in midnight shade, And household Gods, our present aid, A every being great and small To hear and mark the oath I call.” When thus the archer king was bound, With treacherous arts and oaths enwound, She to her bounteous lord subdued By blinding love, her speech renewed: “Remember, King, that long-past day Of Gods' and demons' battle fray. And how thy foe in doubtful strife Had nigh bereft thee of thy life. Remember, it was only I Preserved thee when about to die, And thou for watchful love and care Wouldst grant my first and second prayer. Those offered boons, pledged with thee then, I now demand, O King of men, [103] Of thee, O Monarch, good and just, Whose righteous soul observes each trust. If thou refuse thy promise sworn, I die, despised, before the morn. These rites in Ráma's name begun— Transfer them, and enthrone my son. The time is come to claim at last The double boon of days long-past, When Gods and demons met in fight, And thou wouldst fain my care requite.
- **Translation**: 

---

### Verse 10 (Ramayan 0.370)
- **Original**: 352 The Ramayana Now forth to DaG ak's forest drive Thy Ráma for nine years and five, And let him dwell a hermit there With deerskin coat and matted hair. Without a rival let my boy The empire of the land enjoy, And let mine eyes ere morning see Thy Ráma to the forest flee.” Canto XII. Dasaratha's Lament. The monarch, as Kaikeyí pressed With cruel words her dire request, Stood for a time absorbed in thought While anguish in his bosom wrought. “Does some wild dream my heart assail? Or do my troubled senses fail? Does some dire portent scare my view? Or frenzy's stroke my soul subdue?” Thus as he thought, his troubled mind In doubt and dread no rest could find, Distressed and trembling like a deer Who sees the dreaded tigress near. On the bare ground his limbs he threw, And many a long deep sigh he drew, Like a wild snake, with fury blind, By charms within a ring confined. Once as the monarch's fury woke, “Shame on thee!” from his bosom broke, And then in sense-bewildering pain He fainted on the ground again.
- **Translation**: 

---

### Verse 11 (Ramayan 0.371)
- **Original**: Canto XII. Dasaratha's Lament. 353 At length, when slowly strength returned, He answered as his eyeballs burned With the wild fury of his ire Consuming her, as 'twere, with fire: “Fell traitress, thou whose thoughts design The utter ruin of my line, What wrong have I or Ráma done? Speak murderess, speak thou wicked one, Seeks he not evermore to please Thee with all sonlike courtesies? By what persuasion art thou led To bring this ruin on his head? Ah me, that fondly unaware I brought thee home my life to share, Called daughter of a king, in truth A serpent with a venomed tooth! What fault can I pretend to find In Ráma praised by all mankind, That I my darling should forsake? No, take my life, my glory take: Let either queen be from me torn, But not my well-loved eldest-born. Him but to see is highest bliss, And death itself his face to miss. The world may sunless stand, the grain May thrive without the genial rain, But if my Ráma be not nigh My spirit from its frame will fly. Enough, thine impious plan forgo, O thou who plottest sin and woe. My head before thy feet, I kneel, And pray thee some compassion feel. O wicked dame, what can have led Thy heart to dare a plot so dread?
- **Translation**: 

---

### Verse 12 (Ramayan 0.372)
- **Original**: 354 The Ramayana Perchance thy purpose is to sound The grace thy son with me has found; Perchance the words that, all these days, Thou still hast said in Ráma's praise, Were only feigned, designed to cheer With flatteries a father's ear. Soon as thy grief, my Queen, I knew, My bosom felt the anguish too. In empty halls art thou possessed, And subject to anothers' hest? Now on Ikshváku's ancient race Falls foul disorder and disgrace, If thou, O Queen, whose heart so long Has loved the good should choose the wrong. Not once, O large-eyed dame, hast thou Been guilty of offence till now, Nor said a word to make me grieve, Now will I now thy sin believe. With thee my Ráma used to hold Like place with Bharat lofty-souled. As thou so often, when the pair Were children yet, wouldst fain declare. And can thy righteous soul endure That Ráma glorious, pious, pure, Should to the distant wilds be sent For fourteen years of banishment? Yea, Ráma Bharat's self exceeds In love to thee and sonlike deeds, And, for deserving love of thee, As Bharat, even so is he. Who better than that chieftain may Obedience, love, and honour pay, Thy dignity with care protect, Thy slightest word and wish respect?
- **Translation**: 

---

### Verse 13 (Ramayan 0.373)
- **Original**: Canto XII. Dasaratha's Lament. 355 Of all his countless followers none Can breathe a word against my son; Of many thousands not a dame Can hint reproach or whisper blame. All creatures feel the sweet control Of Ráma's pure and gentle soul. The pride of Manu's race he binds To him the people's grateful minds. He wins the subjects with his truth, [104] The poor with gifts and gentle ruth, His teachers with his docile will, The foemen with his archer skill. Truth, purity, religious zeal, The hand to give, the heart to feel, The love that ne'er betrays a friend, The rectitude that naught can bend, Knowledge, and meek obedience grace My Ráma pride of Raghu's race. Canst thou thine impious plot design 'Gainst him in whom these virtues shine, Whose glory with the sages vies, Peer of the Gods who rule the skies! From him no harsh or bitter word To pain one creature have I heard, And how can I my son address, For thee, with words of bitterness? Have mercy, Queen: some pity show To see my tears of anguish flow, And listen to my mournful cry, A poor old man who soon must die. Whate'er this sea-girt land can boast Of rich and rare from coast to coast, To thee, my Queen, I give it all: But O, thy deadly words recall:
- **Translation**: 

---

### Verse 14 (Ramayan 0.374)
- **Original**: 356 The Ramayana O see, my suppliant hands entreat, Again my lips are on thy feet: Save Ráma, save my darling child, Nor kill me with this sin defiled.” He grovelled on the ground, and lay To burning grief a senseless prey, And ever and anon, assailed By floods of woe he wept and wailed, Striving with eager speed to gain The margent of his sea of pain. With fiercer words she fiercer yet The hapless father's pleading met: “O Monarch, if thy soul repent The promise and thy free consent, How wilt thou in the world maintain Thy fame for truth unsmirched with stain? When gathered kings with thee converse, And bid thee all the tale rehearse, What wilt thou say, O truthful King, In answer to their questioning? “She to whose love my life I owe, Who saved me smitten by the foe, Kaikeyí, for her tender care, Was cheated of the oath I sware.” Thus wilt thou answer, and forsworn Wilt draw on thee the princes' scorn. Learn from that tale, the Hawk and Dove,275 How strong for truth was Saivya's love. Pledged by his word the monarch gave His flesh the suppliant bird to save. So King Alarka gave his eyes, 275 This story is told in the Mahábhárat. A free version of it may be found in Scenes from the Rámáyan, etc.
- **Translation**: 

---

### Verse 15 (Ramayan 0.375)
- **Original**: Canto XII. Dasaratha's Lament. 357 And gained a mansion in the skies. The Sea himself his promise keeps, And ne'er beyond his limit sweeps. My deeds of old again recall, Nor let thy bond dishonoured fall. The rights of truth thou wouldst forget, Thy Ráma on the throne to set, And let thy days in pleasure glide, Fond King, Kau[alyá by thy side. Now call it by what name thou wilt, Justice, injustice, virtue, guilt, Thy word and oath remain the same, And thou must yield what thus I claim. If Ráma be anointed, I This very day will surely die, Before thy face will poison drink, And lifeless at thy feet will sink. Yea, better far to die than stay Alive to see one single day The crowds before Kau[alyá stand And hail her queen with reverent hand. Now by my son, myself, I swear, No gift, no promise whatsoe'er My steadfast soul shall now content, But only Ráma's banishment.” So far she spake by rage impelled, And then the queen deep silence held. He heard her speech full fraught with ill, But spoke no word bewildered still, Gazed on his love once held so dear Who spoke unlovely rede to hear; Then as he slowly pondered o'er The queen's resolve and oath she swore.
- **Translation**: 

---

### Verse 16 (Ramayan 0.376)
- **Original**: 358 The Ramayana Once sighing forth, Ah Ráma! he Fell prone as falls a smitten tree. His senses lost like one insane, Faint as a sick man weak with pain, Or like a wounded snake dismayed, So lay the king whom earth obeyed. Long burning sighs he slowly heaved, As, conquered by his woe, he grieved, And thus with tears and sobs between His sad faint words addressed the queen: “By whom, Kaikeyí, wast thou taught This flattering hope with ruin fraught? Have goblins seized thy soul, O dame, Who thus canst speak and feel no shame? Thy mind with sin is sicklied o'er, From thy first youth ne'er seen before. A good and loving wife wast thou, But all, alas! is altered now. What terror can have seized thy breast To make thee frame this dire request, That Bharat o'er the land may reign, And Ráma in the woods remain? Turn from thine evil ways, O turn, And thy perfidious counsel spurn, If thou would fain a favour do To people, lord, and Bharat too. O wicked traitress, fierce and vile, Who lovest deeds of sin and guile,[105] What crime or grievance dost thou see, What fault in Ráma or in me? Thy son will ne'er the throne accept If Ráma from his rights be kept, For Bharat's heart more firmly yet
- **Translation**: 

---

### Verse 17 (Ramayan 0.377)
- **Original**: Canto XII. Dasaratha's Lament. 359 Than Ráma's is on justice set. How shall I say, Go forth, and brook Upon my Ráma's face to look, See his pale cheek and ashy lips Dimmed like the moon in sad eclipse? How see the plan so well prepared When prudent friends my counsels shared, All ruined, like a host laid low Beneath some foeman's murderous blow. What will these gathered princes say, From regions near and far away? “O'erlong endures the monarch's reign, or now he is a child again.” When many a good and holy sage In Scripture versed, revered for age, Shall ask for Ráma, what shall I Unhappy, what shall I reply? “By Queen Kaikeyí long distressed I drove him forth and dispossessed.” Although herein the truth I speak, They all will hold me false and weak. What will Kau[alyá say when she Demands her son exiled by me? Alas! what answer shall I frame, Or how console the injured dame? She like a slave on me attends, And with a sister's care she blends A mother's love, a wife's, a friend's. In spite of all her tender care, Her noble son, her face most fair, Another queen I could prefer And for thy sake neglected her, But now, O Queen, my heart is grieved For love and care by thee received,
- **Translation**: 

---

### Verse 18 (Ramayan 0.378)
- **Original**: 360 The Ramayana E'en as the sickening wretch repents His dainty meal and condiments. And how will Queen Sumitrá trust The husband whom she finds unjust, Seeing my Ráma driven hence Dishonoured, and for no offence? Ah! the Videhan bride will hear A double woe, a double fear, Two whelming sorrows at one breath, Her lord's disgrace, his father's death. Mine aged bosom she will wring And kill me with her sorrowing, Sad as a fair nymph left to weep Deserted on Himálaya's steep. For short will be my days, I ween, When I with mournful eyes have seen My Ráma wandering forth alone And heard dear Sítá sob and moan. Ah me! my fond belief I rue. Vile traitress, loved as good and true, As one who in his thirst has quaffed, Deceived by looks, a deadly draught. Ah! thou hast slain me, murderess, while Soothing my soul with words of guile, As the wild hunter kills the deer Lured from the brake his song to hear. Soon every honest tongue will fling Reproach on the dishonest king; The people's scorn in every street The seller of his child will meet, And such dishonour will be mine As whelms a Bráhman drunk with wine. Ah me, for my unhappy fate, Compelled thy words to tolerate!
- **Translation**: 

---

### Verse 19 (Ramayan 0.379)
- **Original**: Canto XII. Dasaratha's Lament. 361 Such woe is sent to scourge a crime Committed in some distant time. For many a day with sinful care I cherished thee, thou sin and snare, Kept thee, unwitting, like a cord Destined to bind its hapless lord. Mine hours of ease I spent with thee, Nor deemed my love my death would be, While like a heedless child I played, On a black snake my hand I laid. A cry from every mouth will burst And all the world will hold me curst, Because I saw my high-souled son Unkinged, unfathered, and undone; “The king by power of love beguiled Is weaker than a foolish child, His own beloved son to make An exile for a woman's sake. By chaste and holy vows restrained, By reverend teachers duly trained. When he his virtue's fruit should taste He falls by sin and woe disgraced.” Two words will all his answer be When I pronounce the stern decree, “Hence, Ráma, to the woods away,” All he will say is, I obey. O, if he would my will withstand When banished from his home and land, This were a comfort in my woe; But he will ne'er do this, I know. My Ráma to the forest fled, And curses thick upon my head, Grim Death will bear me hence away, His world-abominated prey.
- **Translation**: 

---

### Verse 20 (Ramayan 0.380)
- **Original**: 362 The Ramayana When I am gone and Ráma too. How wilt thou those I love pursue? What vengeful sin will be designed Against the queens I leave behind? When thou hast slain her son and me Kau [alyá soon will follow: she Will sink beneath her sorrows' weight, And die like me disconsolate. Exist, Kaikeyí, in thy pride, And let thy heart be gratified, When thou my queens and me hast hurled, And children, to the under world. Soon wilt thou rule as empress o'er My noble house unvext before. But then to wild confusion left,[106] Of Ráma and of me bereft. If Bharat to thy plan consent And long for Ráma's banishment, Ne'er let his hands presume to pay The funeral honours to my clay. Vile foe, thou cause of all mine ill, Obtain at last thy cursed will. A widow soon shalt thou enjoy The sweets of empire with thy boy. O Princess, sure some evil fate First brought thee here to devastate, In whom the night of ruin lies Veiled in a consort's fair disguise. The scorn of all and deepest shame Will long pursue my hated name, And dire disgrace on me will press, Misled by thee to wickedness. How shall my Ráma, whom, before, His elephant or chariot bore,
- **Translation**: 

---



--- End of Ramayan_batch_19.md ---


--- Start of Ramayan_batch_20.md ---

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

### Verse 1 (Ramayan 0.381)
- **Original**: Canto XII. Dasaratha's Lament. 363 Now with his feet, a wanderer, tread The forest wilds around him spread? How shall my son, to please whose taste, The deftest cooks, with earrings graced, With rivalry and jealous care The dainty meal and cates prepare— How shall he now his life sustain With acid fruit and woodland grain? He spends his time unvext by cares, And robes of precious texture wears: How shall he, with one garment round His limbs recline upon the ground? Whose was this plan, this cruel thought Unheard till now, with ruin fraught, To make thy son Ayodhyá's king, And send my Ráma wandering? Shame, shame on women! Vile, untrue, Their selfish ends they still pursue. Not all of womankind I mean. But more than all this wicked queen. O worthless, cruel, selfish dame, I brought thee home, my plague and woe. What fault in me hast thou to blame, Or in my son who loves thee so? Fond wives may from their husbands flee, And fathers may their sons desert, But all the world would rave to see My Ráma touched with deadly hurt. I joy his very step to hear, As though his godlike form I viewed; And when I see my Ráma near I feel my youth again renewed. There might be life without the sun, Yea, e'en if Indra sent no rain,
- **Translation**: 

---

### Verse 2 (Ramayan 0.382)
- **Original**: 364 The Ramayana But, were my Ráma banished, none Would, so I think, alive remain. A foe that longs my life to take, I brought thee here my death to be, Caressed thee long, a venomed snake, And through my folly die. Ah me! Ráma and me and LakshmaG slay, And then with Bharat rule the state; So bring the kingdom to decay, And fawn on those thy lord who hate, Plotter of woe, for evil bred, For such a speech why do not all Thy teeth from out thy wicked head Split in a thousand pieces fall? My Ráma's words are ever kind, He knows not how to speak in ire: Then how canst thou presume to find A fault in him whom all admire? Yield to despair, go mad, or die, Or sink within the rifted earth; Thy fell request will I deny, Thou shamer of thy royal birth. Thy longer life I scarce can bear, Thou ruin of my home and race, Who wouldst my heart and heartstrings tear, Keen as a razor, false and base. My life is gone, why speak of joy? For what, without my son, were sweet? Spare, lady, him thou canst destroy; I pray thee as I touch thy feet.” He fell and wept with wild complaint, Heart-struck by her presumptuous speech, But could not touch, so weak and faint, The cruel feet he strove to reach.
- **Translation**: 

---

### Verse 3 (Ramayan 0.383)
- **Original**: Canto XIII. Dasaratha's Distress. 365 Canto XIII. Dasaratha's Distress. Unworthy of his mournful fate, The mighty king, unfortunate, Lay prostrate in unseemly guise, As, banished from the blissful skies, Yayáti, in his evil day. His merit all exhausted, lay.276 The queen, triumphant in the power Won by her beauty's fatal dower, Still terrible and unsubdued, Her dire demand again renewed: “Great Monarch, 'twas thy boast till now To love the truth and keep the vow; Then wherefore would thy lips refuse The promised boon 'tis mine to choose?” King Da[aratha, thus addressed, With anger raging in his breast, Sank for a while beneath the pain, Then to Kaikeyí spoke again: [107] “Childless so long, at length I won, With mighty toil, from Heaven a son, Ráma, the mighty-armed; and how Shall I desert my darling now? A scholar wise, a hero bold, Of patient mood, with wrath controlled, How can I bid my Ráma fly, My darling of the lotus eye? 276 Only the highest merit obtains a home in heaven for ever. Minor degrees of merit procure only leases of heavenly mansions terminable after periods proportioned to the fund which buys them. King Yayáti went to heaven and when his term expired was unceremoniously ejected, and thrown down to earth.
- **Translation**: 

---

### Verse 4 (Ramayan 0.384)
- **Original**: 366 The Ramayana In heaven itself I scarce could bear, When asking of my Ráma there, To hear the Gods his griefs declare, And O, that death would take me hence Before I wrong his innocence!” As thus the monarch wept and wailed, And maddening grief his heart assailed, The sun had sought his resting-place, And night was closing round apace. But yet the moon-crowned night could bring No comfort to the wretched king. As still he mourned with burning sighs And fixed his gaze upon the skies: “O Night whom starry fires adorn, I long not for the coming morn. Be kind and show some mercy: see, My suppliant hands are raised to thee. Nay, rather fly with swifter pace; No longer would I see the face Of Queen Kaikeyí, cruel, dread, Who brings this woe upon mine head.” Again with suppliant hands he tried To move the queen, and wept and sighed: “To me, unhappy me, inclined To good, sweet dame, thou shouldst be kind; Whose life is well-nigh fled, who cling To thee for succour, me thy king. This, only this, is all my claim: Have mercy, O my lovely dame. None else have I to take my part, Have mercy: thou art good at heart. Hear, lady of the soft black eye, And win a name that ne'er shall die:
- **Translation**: 

---

### Verse 5 (Ramayan 0.385)
- **Original**: Canto XIV. Ráma Summoned. 367 Let Ráma rule this glorious land, The gift of thine imperial hand. O lady of the dainty waist, With eyes and lips of beauty graced, Please Ráma, me, each saintly priest, Bharat, and all from chief to least.” She heard his wild and mournful cry, She saw the tears his speech that broke, Saw her good husband's reddened eye, But, cruel still, no word she spoke. His eyes upon her face he bent, And sought for mercy, but in vain: She claimed his darling's banishment, He swooned upon the ground again. Canto XIV. Ráma Summoned. The wicked queen her speech renewed, When rolling on the earth she viewed Ikshváku's son, Ayodhyá's king, For his dear Ráma sorrowing: “Why, by a simple promise bound, Liest thou prostrate on the ground, As though a grievous sin dismayed Thy spirit! Why so sore afraid? Keep still thy word. The righteous deem That truth, mid duties, is supreme: And now in truth and honour's name I bid thee own the binding claim. Zaivya, a king whom earth obeyed, Once to a hawk a promise made,
- **Translation**: 

---

### Verse 6 (Ramayan 0.386)
- **Original**: 368 The Ramayana Gave to the bird his flesh and bone, And by his truth made heaven his own.277 Alarka, when a Bráhman famed For Scripture lore his promise claimed, Tore from his head his bleeding eyes And unreluctant gave the prize. His narrow bounds prescribed restrain The Rivers' Lord, the mighty main, Who, though his waters boil and rave, Keeps faithful to the word he gave. Truth all religion comprehends, Through all the world its might extends: In truth alone is justice placed, On truth the words of God are based: A life in truth unchanging past Will bring the highest bliss at last. If thou the right would still pursue, Be constant to thy word and true: Let me thy promise fruitful see, For boons, O King, proceed from thee. Now to preserve thy righteous fame, And yielding to my earnest claim— Thrice I repeat it— send thy child, Thy Ráma, to the forest wild. But if the boon thou still deny, Before thy face, forlorn, I die.” 277 See Additional Notes, THE SUPPLIANT D OVE {FNS .
- **Translation**: 

---

### Verse 7 (Ramayan 0.387)
- **Original**: Canto XIV. Ráma Summoned. 369 Thus was the helpless monarch stung By Queen Kaikeyí's fearless tongue, As Bali strove in vain to loose His limbs from Indra's fatal noose. Dismayed in soul and pale with fear, The monarch, like a trembling steer Between the chariot's wheel and yoke, Again to Queen Kaikeyí spoke, With sad eyes fixt in vacant stare, Gathering courage from despair: “That hand I took, thou sinful dame, With texts, before the sacred flame, Thee and thy son, I scorn and hate, And all at once repudiate. [108] The night is fled: the dawn is near: Soon will the holy priests be here To bid me for the rite prepare That with my son the throne will share, The preparation made to grace My Ráma in his royal place— With this, e'en this, my darling for My death the funeral flood shall pour. Thou and thy son at least forbear In offerings to my shade to share, For by the plot thy guile has laid His consecration will be stayed. This very day how shall I brook To meet each subject's altered look? To mark each gloomy joyless brow That was so bright and glad but now?” While thus the high-souled monarch spoke To the stern queen, the Morning broke, And holy night had slowly fled,
- **Translation**: 

---

### Verse 8 (Ramayan 0.388)
- **Original**: 370 The Ramayana With moon and stars engarlanded. Yet once again the cruel queen Spoke words in answer fierce and keen, Still on her evil purpose bent, Wild with her rage and eloquent: “What speech is this? Such words as these Seem sprung from poison-sown disease. Quick to thy noble Ráma send And bid him on his sire attend. When to my son the rule is given; When Ráma to the woods is driven; When not a rival copes with me, From chains of duty thou art free.” Thus goaded, like a generous steed Urged by sharp spurs to double speed, “My senses are astray,” he cried, “And duty's bonds my hands have tied. I long to see mine eldest son, My virtuous, my beloved one.” And now the night had past away; Out shone the Maker of the Day, Bringing the planetary hour And moment of auspicious power. Va [ishmha, virtuous, far renowned, Whose young disciples girt him round, With sacred things without delay Through the fair city took his way. He traversed, where the people thronged, And all for Ráma's coming longed, The town as fair in festive show As his who lays proud cities low.278 278 Indra, called also Purandara, Town-destroyer.
- **Translation**: 

---

### Verse 9 (Ramayan 0.389)
- **Original**: Canto XIV. Ráma Summoned. 371 He reached the palace where he heard The mingled notes of many a bird, Where crowded thick high-honoured bands Of guards with truncheons in their hands. Begirt by many a sage, elate, Va [ishmha reached the royal gate, And standing by the door he found Sumantra, for his form renowned, The king's illustrious charioteer And noble counsellor and peer. To him well skilled in every part Of his hereditary art Va [ishmha said:“O charioteer, Inform the king that I am here, Here ready by my side behold These sacred vessels made of gold, Which water for the rite contain From Gangá and each distant main. Here for installing I have brought The seat prescribed of fig-wood wrought, All kinds of seed and precious scent And many a gem and ornament; Grain, sacred grass, the garden's spoil, Honey and curds and milk and oil; Eight radiant maids, the best of all War elephants that feed in stall; A four-horse car, a bow and sword. A litter, men to bear their lord; A white umbrella bright and fair That with the moon may well compare; Two chouries of the whitest hair; A golden beaker rich and rare; A bull high-humped and fair to view, Girt with gold bands and white of hue;
- **Translation**: 

---

### Verse 10 (Ramayan 0.390)
- **Original**: 372 The Ramayana A four-toothed steed with flowing mane, A throne which lions carved sustain; A tiger's skin, the sacred fire, Fresh kindled, which the rites require; The best musicians skilled to play, And dancing-girls in raiment gay; Kine, Bráhmans, teachers fill the court, And bird and beast of purest sort. From town and village, far and near, The noblest men are gathered here; Here merchants with their followers crowd, And men in joyful converse loud, And kings from many a distant land To view the consecration stand. The dawn is come, the lucky day; Go bid the monarch haste away, That now Prince Ráma may obtain The empire, and begin his reign.” Soon as he heard the high behest The driver of the chariot pressed Within the chambers of the king, His lord with praises honouring. And none of all the warders checked His entrance for their great respect Of him well known, in place so high, Still fain their king to gratify. He stood beside the royal chief, Unwitting of his deadly grief, And with sweet words began to sing The praises of his lord and king: “As, when the sun begins to rise, The sparkling sea delights our eyes, Wake, calm with gentle soul, and thus[109]
- **Translation**: 

---

### Verse 11 (Ramayan 0.391)
- **Original**: Canto XIV. Ráma Summoned. 373 Give rapture, mighty King, to us. As Mátali279 this selfsame hour Sang lauds of old to Indra's power, When he the Titan hosts o'erthrew, So hymn I thee with praises due. The Vedas, with their kindred lore, Brahmá their soul-born Lord adore, With all the doctrines of the wise, And bid him, as I bid thee, rise. As, with the moon, the Lord of Day Wakes with the splendour of his ray Prolific Earth, who neath him lies, So, mighty King, I bid thee rise. With blissful words, O Lord of men, Rise, radiant in thy form, as when The sun ascending darts his light From Meru's everlasting height. May Ziva, Agni, Sun, and Moon Bestow on thee each choicest boon, Kuvera, VaruGa, Indra bless Kakutstha's son with all success. Awake, the holy night is fled, The happy light abroad is spread; Awake, O best of kings, and share The glorious task that claims thy care. The holy sage Va[ishmha waits, With all his Bráhmans, at the gate. Give thy decree, without delay, To consecrate thy son today. As armies, by no captain led, As flocks that feed unshepherded, Such is the fortune of a state 279 Indra's charioteer.
- **Translation**: 

---

### Verse 12 (Ramayan 0.392)
- **Original**: 374 The Ramayana Without a king and desolate.” Such were the words the bard addressed, With weight of sage advice impressed; And, as he heard, the hapless king Felt deeper yet his sorrow's sting. At length, all joy and comfort fled, He raised his eyes with weeping red, And, mournful for his Ráma's sake, The good and glorious monarch spake: “Why seek with idle praise to greet The wretch for whom no praise is meet? Thy words mine aching bosom tear, And plunge me deeper in despair.” Sumantra heard the sad reply, And saw his master's tearful eye. With reverent palm to palm applied He drew a little space aside. Then, as the king, with misery weak, With vain endeavour strove to speak, Kaikeyí, skilled in plot and plan, To sage Sumantra thus began: “The king, absorbed in joyful thought For his dear son, no rest has sought: Sleepless to him the night has past, And now o'erwatched he sinks at last. Then go, Sumantra, and with speed The glorious Ráma hither lead: Go, as I pray, nor longer wait; No time is this to hesitate.” “How can I go, O Lady fair, Unless my lord his will declare?” “Fain would I see him,” cried the king,
- **Translation**: 

---

### Verse 13 (Ramayan 0.393)
- **Original**: Canto XV. The Preparations. 375 “Quick, quick, my beauteous Ráma bring.” Then rose the happy thought to cheer The bosom of the charioteer, “The king, I ween, of pious mind, The consecration has designed.” Sumantra for his wisdom famed, Delighted with the thought he framed, From the calm chamber, like a bay Of crowded ocean, took his way. He turned his face to neither side, But forth he hurried straight; Only a little while he eyed The guards who kept the gate. He saw in front a gathered crowd Of men of every class, Who, parting as he came, allowed The charioteer to pass. Canto XV. The Preparations. There slept the Bráhmans, deeply read In Scripture, till the night had fled; Then, with the royal chaplains, they Took each his place in long array. There gathered fast the chiefs of trade, Nor peer nor captain long delayed, Assembling all in order due The consecrating rite to view.
- **Translation**: 

---

### Verse 14 (Ramayan 0.394)
- **Original**: 376 The Ramayana The morning dawned with cloudless ray On Pushya's high auspicious day, And Cancer with benignant power Looked down on Ráma's natal hour. The twice-born chiefs, with zealous heed, Made ready what the rite would need. The well-wrought throne of holy wood And golden urns in order stood. There was the royal car whereon A tiger's skin resplendent shone; There water, brought for sprinkling thence Where, in their sacred confluence, Blend Jumná's waves with Gangá's tide, From many a holy flood beside, From brook and fountain far and near, From pool and river, sea and mere. And there were honey, curd, and oil, Parched rice and grass, the garden's spoil, Fresh milk, eight girls in bright attire, An elephant with eyes of fire; And urns of gold and silver made, With milky branches overlaid, All brimming from each sacred flood, And decked with many a lotus bud.[110] And dancing-women fair and free, Gay with their gems, were there to see, Who stood in bright apparel by With lovely brow and witching eye. White flashed the jewelled chouri there, And shone like moonbeams through the air; The white umbrella overhead A pale and moonlike lustre shed, Wont in pure splendour to precede, And in such rites the pomp to lead.
- **Translation**: 

---

### Verse 15 (Ramayan 0.395)
- **Original**: Canto XV. The Preparations. 377 There stood the charger by the side Of the great bull of snow-white hide; There was all music soft and loud, And bards and minstrels swelled the crowd. For now the monarch bade combine Each custom of his ancient line With every rite Ayodhyá's state Observed, her kings to consecrate. Then, summoned by the king's behest, The multitudes together pressed, And, missing still the royal sire, Began, impatient, to inquire: “Who to our lord will tidings bear That all his people throng the square? Where is the king? the sun is bright, And all is ready for the rite.” As thus they spoke, Sumantra, tried In counsel, to the chiefs replied, Gathered from lands on every side: “To Ráma's house I swiftly drave, For so the king his mandate gave. Our aged lord and Ráma too In honour high hold all of you: I in your words (be long your days!) Will ask him why he thus delays.”
- **Translation**: 

---

### Verse 16 (Ramayan 0.396)
- **Original**: 378 The Ramayana Thus spoke the peer in Scripture read, And to the ladies' bower he sped. Quick through the gates Sumantra hied, Which access ne'er to him denied. Behind the curtained screen he drew, Which veiled the chamber from the view. In benediction loud he raised His voice, and thus the monarch praised: “Sun, Moon, Kuvera,Ziva bless Kakutstha's son with high success! The Lords of air, flood, fire decree The victory, my King, to thee! The holy night has past away, Auspicious shines the morning's ray. Rise, Lord of men, thy part to take In the great rite. Awake! awake! Bráhmans and captains, chiefs of trade, All wait in festive garb arrayed; For thee they look with eager eyes: O Raghu's son, awake! arise.” To him in holy Scripture read, Who hailed him thus, the monarch said, Upraising from his sleep his head: “Go, Ráma, hither lead as thou Wast ordered by the queen but now. Come, tell me why my mandate laid Upon thee thus is disobeyed. Away! and Ráma hither bring; I sleep not: make no tarrying.”
- **Translation**: 

---

### Verse 17 (Ramayan 0.397)
- **Original**: Canto XV. The Preparations. 379 Thus gave the king command anew: Sumantra from his lord withdrew; With head in lowly reverence bent, And filled with thoughts of joy, he went. The royal street he traversed, where Waved flag and pennon to the air, And, as with joy the car he drove, He let his eyes delighted rove. On every side, where'er he came, He heard glad words, their theme the same, As in their joy the gathered folk Of Ráma and the throning spoke. Then saw he Ráma's palace bright And vast as Mount Kailása's height, That glorious in its beauty showed As Indra's own supreme abode: With folding doors both high and wide; With hundred porches beautified: Where golden statues towering rose O'er gemmed and coralled porticoes. Bright like a cave in Meru's side, Or clouds through Autumn's sky that ride: Festooned with length of bloomy twine, Flashing with pearls and jewels' shine, While sandal-wood and aloe lent The mingled riches of their scent; With all the odorous sweets that fill The breezy heights of Dardar's hill. There by the gate the Sáras screamed, And shrill-toned peacocks' plumage gleamed. Its floors with deftest art inlaid, Its sculptured wolves in gold arrayed, With its bright sheen the palace took The mind of man and chained the look,
- **Translation**: 

---

### Verse 18 (Ramayan 0.398)
- **Original**: 380 The Ramayana For like the sun and moon it glowed, And mocked Kuvera's loved abode. Circling the walls a crowd he viewed Who stood in reverent attitude, With throngs of countrymen who sought Acceptance of the gifts they brought. The elephant was stationed there, Appointed Ráma's self to bear; Adorned with pearls, his brow and cheek Were sandal-dyed in many a streak, While he, in stature, bulk, and pride, With Indra's own Airávat280 vied. Sumantra, borne by coursers fleet, Flashing a radiance o'er the street, To Ráma's palace flew, And all who lined the royal road, Or thronged the prince's rich abode, Rejoiced as near he drew. And with delight his bosom swelled As onward still his course he held[111] Through many a sumptuous court Like Indra's palace nobly made, Where peacocks revelled in the shade, And beasts of silvan sort. Through many a hall and chamber wide, That with Kailása's splendour vied. Or mansions of the Blest, While Ráma's friends, beloved and tried, Before his coming stepped aside, Still on Sumantra pressed. He reached the chamber door, where stood Around his followers young and good, 280 The elephant of Indra.
- **Translation**: 

---

### Verse 19 (Ramayan 0.399)
- **Original**: Canto XVI. Ráma Summoned. 381 Bard, minstrel, charioteer, Well skilled the tuneful chords to sweep, With soothing strain to lull to sleep, Or laud their master dear. Then, like a dolphin darting through Unfathomed depths of ocean's blue With store of jewels decked, Through crowded halls that rock-like rose, Or as proud hills where clouds repose, Sumantra sped unchecked— Halls like the glittering domes on high Reared for the dwellers of the sky By heavenly architect. Canto XVI. Ráma Summoned. So through the crowded inner door Sumantra, skilled in ancient lore, On to the private chambers pressed Which stood apart from all the rest. There youthful warriors, true and bold, Whose ears were ringed with polished gold, All armed with trusty bows and darts, Watched with devoted eyes and hearts. And hoary men, a faithful train, Whose aged hands held staves of cane, The ladies' guard, apparelled fair In red attire, were stationed there. Soon as they saw Sumantra nigh, Each longed his lord to gratify, And from his seat beside the door
- **Translation**: 

---

### Verse 20 (Ramayan 0.400)
- **Original**: 382 The Ramayana Up sprang each ancient servitor. Then to the warders quickly cried The skilled Sumantra, void of pride: “Tell Ráma that the charioteer Sumantra waits for audience here.” The ancient men with one accord Seeking the pleasure of their lord, Passing with speed the chamber door To Ráma's ear the message bore. Forthwith the prince with duteous heed Called in the messenger with speed, For 'twas his sire's command, he knew, That sent him for the interview. Like Lord Kuvera, well arrayed, He pressed a couch of gold, Wherefrom a covering of brocade Hung down in many a fold. Oil and the sandal's fragrant dust Had tinged his body o'er Dark as the stream the spearman's thrust Drains from the wounded boar. Him Sítá watched with tender care, A chouri in her hand, As Chitrá,281 ever fond in fair, Beside the Moon will stand. Him glorious with unborrowed light, A liberal lord, of sunlike might, Sumantra hailed in words like these, Well skilled in gentle courtesies, As, with joined hands in reverence raised, Upon the beauteous prince he gazed: “Happy Kau[alyá! Blest is she, 281 A star in the spike of Virgo: hence the name of the mouth Chaitra or Chait.
- **Translation**: 

---



--- End of Ramayan_batch_20.md ---


--- Start of Ramayan_batch_21.md ---

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

### Verse 1 (Ramayan 0.401)
- **Original**: Canto XVI. Ráma Summoned. 383 The Mother of a son like thee. Now rise, O Ráma, speed away. Go to thy sire without delay: For he and Queen Kaikeyí seek An interview with thee to speak.” The lion-lord of men, the best Of splendid heroes, thus addressed, To Sítá spake with joyful cheer: “The king and queen, my lady dear, Touching the throning, for my sake Some salutary counsel take. The lady of the full black eye Would fain her husband gratify, And, all his purpose understood, Counsels the monarch to my good. A happy fate is mine, I ween, When he, consulting with his queen, Sumantra on this charge, intent Upon my gain and good, has sent. An envoy of so noble sort Well suits the splendour of the court. The consecration rite this day Will join me in imperial sway. To meet the lord of earth, for so His order bids me, I will go. Thou, lady, here in comfort stay, And with thy maidens rest or play.”
- **Translation**: 

---

### Verse 2 (Ramayan 0.402)
- **Original**: 384 The Ramayana Thus Ráma spake. For meet reply The lady of the large black eye Attended to the door her lord, And blessings on his head implored: “The majesty and royal state Which holy Bráhmans venerate, The consecration and the rite Which sanctifies the ruler's might, And all imperial powers should be Thine by thy father's high decree, As He, the worlds who formed and planned, The kingship gave to Indra's hand.[112] Then shall mine eyes my king adore When lustral rites and fast are o'er, And black deer's skin and roebuck's horn Thy lordly limbs and hand adorn. May He whose hands the thunder wield Be in the east thy guard and shield; May Yáma's care the south befriend, And VaruG's arm the west defend; And let Kuvera, Lord of Gold, The north with firm protection hold.” Then Ráma spoke a kind farewell, And hailed the blessings as they fell From Sítá's gentle lips; and then, As a young lion from his den Descends the mountain's stony side, So from the hall the hero hied. First LakshmaG at the door he viewed Who stood in reverent attitude, Then to the central court he pressed Where watched the friends who loved him best. To all his dear companions there
- **Translation**: 

---

### Verse 3 (Ramayan 0.403)
- **Original**: Canto XVI. Ráma Summoned. 385 He gave kind looks and greeting fair. On to the lofty car that glowed Like fire the royal tiger strode. Bright as himself its silver shone: A tiger's skin was laid thereon. With cloudlike thunder, as it rolled, It flashed with gems and burnished gold, And, like the sun's meridian blaze, Blinded the eye that none could gaze. Like youthful elephants, tall and strong, Fleet coursers whirled the car along: In such a car the Thousand-eyed Borne by swift horses loves to ride. So like Parjanya,282 when he flies Thundering through the autumn skies, The hero from the palace sped, As leaves the moon some cloud o'erhead. Still close to Ráma LakshmaG kept, Behind him to the car he leapt, And, watching with fraternal care, Waved the long chouri's silver hair, As from the palace gate he came Up rose the tumult of acclaim. While loud huzza and jubilant shout Pealed from the gathered myriads out. Then elephants, like mountains vast, And steeds who all their kind surpassed, Followed their lord by hundreds, nay By thousands, led in long array. First marched a band of warriors trained, With sandal dust and aloe stained; Well armed was each with sword and bow, 282 The Rain-God.
- **Translation**: 

---

### Verse 4 (Ramayan 0.404)
- **Original**: 386 The Ramayana And every breast with hope aglow, And ever, as they onward went, Shouts from the warrior train, And every sweet-toned instrument Prolonged the minstrel strain. On passed the tamer of his foes, While well clad dames, in crowded rows, Each chamber lattice thronged to view, And chaplets on the hero threw. Then all, of peerless face and limb, Sang Ráma's praise for love of him, And blent their voices, soft and sweet, From palace high and crowded street: “Now, sure, Kau[alyá's heart must swell To see the son she loves so well, Thee Ráma, thee, her joy and pride, Triumphant o'er the realm preside.” Then— for they knew his bride most fair Of all who part the soft dark hair, His love, his life, possessed the whole Of her young hero's heart and soul:— “Be sure the lady's fate repays Some mighty vow of ancient days,283 For blest with Ráma's love is she As, with the Moon's, sweet Rohiní.”284 Such were the witching words that came From lips of many a peerless dame Crowding the palace roofs to greet The hero as he gained the street. 283 In a former life. 284 One of the lunar asterisms, represented as the favourite wife of the Moon. See p. 4, note.
- **Translation**: 

---

### Verse 5 (Ramayan 0.405)
- **Original**: Canto XVII. Ráma's Approach. 387 Canto XVII. Ráma's Approach. As Ráma, rendering blithe and gay His loving friends, pursued his way, He saw on either hand a press Of mingled people numberless. The royal street he traversed, where Incense of aloe filled the air, Where rose high palaces, that vied With paly clouds, on either side; With flowers of myriad colours graced. And food for every varied taste, Bright as the glowing path o'erhead Which feet of Gods celestial tread, Loud benedictions, sweet to hear, From countless voices soothed his ear. While he to each gave due salute His place and dignity to suit: “Be thou,” the joyful people cried, “Be thou our guardian, lord and guide. Throned and anointed king to-day, Thy feet set forth upon the way Wherein, each honoured as a God, Thy fathers and forefathers trod. Thy sire and his have graced the throne, And loving care to us have shown: Thus blest shall we and ours remain, Yea still more blest in Ráma's reign. [113] No more of dainty fare we need, And but one cherished object heed, That we may see our prince today Invested with imperial sway.”
- **Translation**: 

---

### Verse 6 (Ramayan 0.406)
- **Original**: 388 The Ramayana Such were the words and pleasant speech That Ráma heard, unmoved, from each Of the dear friends around him spread, As onward through the street he sped, For none could turn his eye or thought From the dear form his glances sought, With fruitless ardour forward cast Even when Raghu's son had past. And he who saw not Ráma nigh, Nor caught a look from Ráma's eye, A mark for scorn and general blame, Reproached himself in bitter shame. For to each class his equal mind With sympathy and love inclined Most fully of the princely four, So greatest love to him they bore. His circling course the hero bent Round shrine and altar, reverent, Round homes of Gods, where cross-roads met, Where many a sacred tree was set. Near to his father's house he drew Like Indra's beautiful to view, And with the light his glory gave Within the royal palace drave. Through three broad courts, where bowmen kept Their watch and ward, his coursers swept, Then through the two remaining went On foot the prince preëminent. Through all the courts the hero passed, And gained the ladies' bower at last; Then through the door alone withdrew, And left without his retinue. When thus the monarch's noble boy
- **Translation**: 

---

### Verse 7 (Ramayan 0.407)
- **Original**: Canto XVIII. The Sentence. 389 Had gone his sire to meet, The multitude, elate with joy, Stood watching in the street, And his return with eager eyes Expected at the gates, As for his darling moon to rise The King of Rivers285 waits. Canto XVIII. The Sentence. With hopeless eye and pallid mien There sat the monarch with the queen. His father's feet with reverence due He clasped, and touched Kaikeyí's too. The king, with eyes still brimming o'er, Cried Ráma! and could do no more. His voice was choked, his eye was dim, He could not speak or look on him. Then sudden fear made Ráma shake As though his foot had roused a snake, Soon as his eyes had seen the change So mournful, terrible, and strange. For there his reason well-nigh fled, Sighing, with soul disquieted, To torturing pangs a prey, Dismayed, despairing, and distraught, In a fierce whirl of wildering thought The hapless monarch lay, Like Ocean wave-engarlanded 285 The Sea.
- **Translation**: 

---

### Verse 8 (Ramayan 0.408)
- **Original**: 390 The Ramayana Storm-driven from his tranquil bed, The Sun-God in eclipse, Or like a holy seer, heart-stirred With anguish, when a lying word Has passed his heedless lips. The sight of his dear father, pained With woe and misery unexplained Filled Ráma with unrest, As Ocean's pulses rise and swell When the great moon he loves so well Shines full upon his breast. So grieving for his father's sake, To his own heart the hero spake: “Why will the king my sire to-day No kindly word of greeting say? At other times, though wroth he be, His eyes grow calm that look on me. Then why does anguish wring his brow To see his well-beloved now?” Sick and perplexed, distraught with woe, To Queen Kaikeyí bowing low, While pallor o'er his bright cheek spread, With humble reverence he said: “What have I done, unknown, amiss To make my father wroth like this? Declare it, O dear Queen, and win His pardon for my heedless sin. Why is the sire I ever find Filled with all love to-day unkind? With eyes cast down and pallid cheek This day alone he will not speak. Or lies he prostrate neath the blow Of fierce disease or sudden woe? For all our bliss is dashed with pain,
- **Translation**: 

---

### Verse 9 (Ramayan 0.409)
- **Original**: Canto XVIII. The Sentence. 391 And joy unmixt is hard to gain. Does stroke of evil fortune smite Dear Bharat, charming to the sight, Or on the braveZatrughna fall, Or consorts, for he loves them all? Against his words when I rebel, Or fail to please the monarch well, When deeds of mine his soul offend, That hour I pray my life may end. How should a man to him who gave His being and his life behave? The sire to whom he owes his birth Should be his deity on earth. Hast thou, by pride and folly moved, [114] With bitter taunt the king reproved? Has scorn of thine or cruel jest To passion stirred his gentle breast? Speak truly, Queen, that I may know What cause has changed the monarch so.” Thus by the high-souled prince addressed, Of Raghu's sons the chief and best, She cast all ruth and shame aside, And bold with greedy words replied: “Not wrath, O Ráma, stirs the king, Nor misery stabs with sudden sting; One thought that fills his soul has he, But dares not speak for fear of thee. Thou art so dear, his lips refrain From words that might his darling pain. But thou, as duty bids, must still The promise of thy sire fulfil. He who to me in days gone by Vouchsafed a boon with honours high,
- **Translation**: 

---

### Verse 10 (Ramayan 0.410)
- **Original**: 392 The Ramayana Dares now, a king, his word regret, And caitiff-like disowns the debt. The lord of men his promise gave To grant the boon that I might crave, And now a bridge would idly throw When the dried stream has ceased to flow. His faith the monarch must not break In wrath, or e'en for thy dear sake. From faith, as well the righteous know, Our virtue and our merits flow. Now, be they good or be they ill, Do thou thy father's words fulfil: Swear that his promise shall not fail, And I will tell thee all the tale. Yes, Ráma, when I hear that thou Hast bound thee by thy father's vow, Then, not till then, my lips shall speak, Nor will he tell what boon I seek.” He heard, and with a troubled breast This answer to the queen addressed: “Ah me, dear lady, canst thou deem That words like these thy lips beseem? I, at the bidding of my sire, Would cast my body to the fire, A deadly draught of poison drink, Or in the waves of ocean sink: If he command, it shall be done,— My father and my king in one. Then speak and let me know the thing So longed for by my lord the king. It shall be done: let this suffice; Ráma ne'er makes a promise twice.”
- **Translation**: 

---

### Verse 11 (Ramayan 0.411)
- **Original**: Canto XVIII. The Sentence. 393 He ended. To the princely youth Who loved the right and spoke the truth, Cruel, abominable came The answer of the ruthless dame: “When Gods and Titans fought of yore, Transfixed with darts and bathed in gore Two boons to me thy father gave For the dear life 'twas mine to save. Of him I claim the ancient debt, That Bharat on the throne be set, And thou, O Ráma, go this day To DaG ak forest far away. Now, Ráma, if thou wilt maintain Thy father's faith without a stain, And thine own truth and honour clear, Then, best of men, my bidding hear. Do thou thy father's word obey, Nor from the pledge he gave me stray. Thy life in DaG ak forest spend Till nine long years and five shall end. Upon my Bharat's princely head Let consecrating drops be shed, With all the royal pomp for thee Made ready by the king's decree. Seek DaG ak forest and resign Rites that would make the empire thine, For twice seven years of exile wear The coat of bark and matted hair. Then in thy stead let Bharat reign Lord of his royal sire's domain, Rich in the fairest gems that shine, Cars, elephants, and steeds, and kine. The monarch mourns thy altered fate And vails his brow compassionate:
- **Translation**: 

---

### Verse 12 (Ramayan 0.412)
- **Original**: 394 The Ramayana Bowed down by bitter grief he lies And dares not lift to thine his eyes. Obey his word: be firm and brave, And with great truth the monarch save.” While thus with cruel words she spoke, No grief the noble youth betrayed; But forth the father's anguish broke, At his dear Ráma's lot dismayed. Canto XIX. Ráma's Promise. Calm and unmoved by threatened woe The noble conqueror of the foe Answered the cruel words she spoke, Nor quailed beneath the murderous stroke: “Yea, for my father's promise sake I to the wood my way will take, And dwell a lonely exile there In hermit dress with matted hair. One thing alone I fain would learn, Why is the king this day so stern? Why is the scourge of foes so cold, Nor gives me greeting as of old? Now let not anger flush thy cheek: Before thy face the truth I speak, In hermit's coat with matted hair To the wild wood will I repair. How can I fail his will to do, Friend, master, grateful sovereign too? One only pang consumes my breast:
- **Translation**: 

---

### Verse 13 (Ramayan 0.413)
- **Original**: Canto XIX. Ráma's Promise. 395 That his own lips have not expressed His will, nor made his longing known That Bharat should ascend the throne. [115] To Bharat I would yield my wife, My realm and wealth, mine own dear life, Unasked I fain would yield them all: More gladly at my father's call, More gladly when the gift may free His honour and bring joy to thee. Thus, lady, his sad heart release From the sore shame, and give him peace. But tell me, O, I pray thee, why The lord of men, with downcast eye, Lies prostrate thus, and one by one Down his pale cheek the tear-drops run. Let couriers to thy father speed On horses of the swiftest breed, And, by the mandate of the king, Thy Bharat to his presence bring. My father's words I will not stay To question, but this very day To DaG ak's pathless wild will fare, For twice seven years an exile there.” When Ráma thus had made reply Kaikeyí's heart with joy beat high. She, trusting to the pledge she held, The youth's departure thus impelled: “'Tis well. Be messengers despatched On coursers ne'er for fleetness matched, To seek my father's home and lead My Bharat back with all their speed. And, Ráma, as I ween that thou Wilt scarce endure to linger now,
- **Translation**: 

---

### Verse 14 (Ramayan 0.414)
- **Original**: 396 The Ramayana So surely it were wise and good This hour to journey to the wood. And if, with shame cast down and weak, No word to thee the king can speak, Forgive, and from thy mind dismiss A trifle in an hour like this. But till thy feet in rapid haste Have left the city for the waste, And to the distant forest fled, He will not bathe nor call for bread.” “Woe! woe!” from the sad monarch burst, In surging floods of grief immersed; Then swooning, with his wits astray, Upon the gold-wrought couch he lay, And Ráma raised the aged king: But the stern queen, unpitying, Checked not her needless words, nor spared The hero for all speed prepared, But urged him with her bitter tongue, Like a good horse with lashes stung, She spoke her shameful speech. Serene He heard the fury of the queen, And to her words so vile and dread Gently, unmoved in mind, he said: “I would not in this world remain A grovelling thrall to paltry gain, But duty's path would fain pursue, True as the saints themselves are true. From death itself I would not fly My father's wish to gratify, What deed soe'er his loving son May do to please him, think it done. Amid all duties, Queen, I count
- **Translation**: 

---

### Verse 15 (Ramayan 0.415)
- **Original**: Canto XIX. Ráma's Promise. 397 This duty first and paramount, That sons, obedient, aye fulfil Their honoured fathers' word and will. Without his word, if thou decree, Forth to the forest will I flee, And there shall fourteen years be spent Mid lonely wilds in banishment. Methinks thou couldst not hope to find One spark of virtue in my mind, If thou, whose wish is still my lord, Hast for this grace the king implored. This day I go, but, ere we part, Must cheer my Sítá's tender heart, To my dear mother bid farewell; Then to the woods, a while to dwell. With thee, O Queen, the care must rest That Bharat hear his sire's behest, And guard the land with righteous sway, For such the law that lives for aye.” In speechless woe the father heard, Wept with loud cries, but spoke no word. Then Ráma touched his senseless feet, And hers, for honour most unmeet; Round both his circling steps he bent, Then from the bower the hero went. Soon as he reached the gate he found His dear companions gathered round. Behind him came Sumitrá's child With weeping eyes so sad and wild. Then saw he all that rich array Of vases for the glorious day. Round them with reverent stops he paced, Nor vailed his eye, nor moved in haste.
- **Translation**: 

---

### Verse 16 (Ramayan 0.416)
- **Original**: 398 The Ramayana The loss of empire could not dim The glory that encompassed him. So will the Lord of Cooling Rays286 On whom the world delights to gaze, Through the great love of all retain Sweet splendour in the time of wane. Now to the exile's lot resigned He left the rule of earth behind: As though all worldly cares he spurned No trouble was in him discerned. The chouries that for kings are used, And white umbrella, he refused, Dismissed his chariot and his men, And every friend and citizen. He ruled his senses, nor betrayed The grief that on his bosom weighed, And thus his mother's mansion sought To tell the mournful news he brought. Nor could the gay-clad people there Who flocked round Ráma true and fair, One sign of altered fortune trace Upon the splendid hero's face. Nor had the chieftain, mighty-armed, Lost the bright look all hearts that charmed,[116] As e'en from autumn moons is thrown A splendour which is all their own. With his sweet voice the hero spoke Saluting all the gathered folk, Then righteous-souled and great in fame Close to his mother's house he came. Lakshma G the brave, his brother's peer In princely virtues, followed near, 286 The Moon.
- **Translation**: 

---

### Verse 17 (Ramayan 0.417)
- **Original**: Canto XX. Kausalyá's Lament. 399 Sore troubled, but resolved to show No token of his secret woe. Thus to the palace Ráma went Where all were gay with hope and joy; But well he knew the dire event That hope would mar, that bliss destroy. So to his grief he would not yield Lest the sad change their hearts might rend, And, the dread tiding unrevealed, Spared from the blow each faithful friend. Canto XX. Kausalyá's Lament. But in the monarch's palace, when Sped from the bower that lord of men, Up from the weeping women went A mighty wail and wild lament: “Ah, he who ever freely did His duty ere his sire could bid, Our refuge and our sure defence, This day will go an exile hence, He on Kau[alyá loves to wait Most tender and affectionate, And as he treats his mother, thus From childhood has he treated us. On themes that sting he will not speak, And when reviled is calm and meek. He soothes the angry, heals offence: He goes to-day an exile hence. Our lord the king is most unwise, And looks on life with doting eyes,
- **Translation**: 

---

### Verse 18 (Ramayan 0.418)
- **Original**: 400 The Ramayana Who in his folly casts away The world's protection, hope, and stay.” Thus in their woe, like kine bereaved Of their young calves,287 the ladies grieved, And ever as they wept and wailed With keen reproach the king assailed. Their lamentation, mixed with tears, Smote with new grief the monarch's ears, Who, burnt with woe too great to bear, Fell on his couch and fainted there. Then Ráma, smitten with the pain His heaving heart could scarce restrain, Groaned like an elephant and strode With LakshmaG to the queen's abode. A warder there, whose hoary eld In honour high by all was held, Guarding the mansion, sat before The portal, girt with many more. Swift to their feet the warders sprang, And loud the acclamation rang, Hail, Ráma! as to him they bent, Of victor chiefs preëminent. One court he passed, and in the next Saw, masters of each Veda text, A crowd of Bráhmans, good and sage, 287 The comparison may to a European reader seem a homely one. But Spenser likens an infuriate woman to a cow“That is berobbed of her youngling dere.” Shakspeare also makes King Henry VI compare himself to the calf's mother that“Runs lowing up and down, Looking the way her harmless young one went.” “Cows,” says De Quincey,“are amongst the gentlest of breathing crea- tures; none show more passionate tenderness to their young, when deprived of them, and, in short, I am not ashamed to profess a deep love for these gentle creatures.”
- **Translation**: 

---

### Verse 19 (Ramayan 0.419)
- **Original**: Canto XX. Kausalyá's Lament. 401 Dear to the king for lore and age. To these he bowed his reverent head, Thence to the court beyond he sped. Old dames and tender girls, their care To keep the doors, were stationed there. And all, when Ráma came in view, Delighted to the chamber flew, To bear to Queen Kau[alyá's ear The tidings that she loved to hear. The queen, on rites and prayer intent, In careful watch the night had spent, And at the dawn, her son to aid, To VishGu holy offerings made. Firm in her vows, serenely glad, In robes of spotless linen clad, As texts prescribe, with grace implored, Her offerings in the fire she poured. Within her splendid bower he came, And saw her feed the sacred flame. There oil, and grain, and vases stood, With wreaths, and curds, and cates, and wood, And milk, and sesamum, and rice, The elements of sacrifice. She, worn and pale with many a fast And midnight hours in vigil past, In robes of purest white arrayed, To Lakshmí Queen drink-offerings paid. So long away, she flew to meet The darling of her soul: So runs a mare with eager feet To welcome back her foal. He with his firm support upheld The queen, as near she drew, And, by maternal love impelled,
- **Translation**: 

---

### Verse 20 (Ramayan 0.420)
- **Original**: 402 The Ramayana Her arms around him threw. Her hero son, her matchless boy She kissed upon the head: She blessed him in her pride and joy With tender words, and said:[117] “Be like thy royal sires of old, The nobly good, the lofty-souled! Their lengthened days and fame be thine, And virtue, as beseems thy line! The pious king, thy father, see True to his promise made to thee: That truth thy sire this day will show, And regent's power on thee bestow.” She spoke. He took the proffered seat, And as she pressed her son to eat, Raised reverent bands, and, touched with shame, Made answer to the royal dame: “Dear lady, thou hast yet to know That danger threats, and heavy woe: A grief that will with sore distress On Sítá, thee, and LakshmaG press. What need of seats have such as I? This day to DaG ak wood I fly. The hour is come, a time, unmeet For silken couch and gilded seat. I must to lonely wilds repair, Abstain from flesh, and living there On roots, fruit, honey, hermit's food, Pass twice seven years in solitude. To Bharat's hand the king will yield The regent power I thought to wield, And me, a hermit, will he send My days in DaG ak wood to spend.”
- **Translation**: 

---



--- End of Ramayan_batch_21.md ---


--- Start of Ramayan_batch_22.md ---

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

### Verse 1 (Ramayan 0.421)
- **Original**: Canto XX. Kausalyá's Lament. 403 As when the woodman's axe has lopped A Zal branch in the grove, she dropped: So from the skies a Goddess falls Ejected from her radiant halls. When Ráma saw her lying low, Prostrate by too severe a blow, Around her form his arms he wound And raised her fainting from the ground. His hand upheld her like a mare Who feels her load too sore to bear, And sinks upon the way o'ertoiled, And all her limbs with dust are soiled. He soothed her in her wild distress With loving touch and soft caress. She, meet for highest fortune, eyed The hero watching by her side, And thus, while LakshmaG bent to hear, Addressed her son with many a tear! “If, Ráma, thou had ne'er been born My child to make thy mother mourn, Though reft of joy, a childless queen, Such woe as this I ne'er had seen. Though to the childless wife there clings One sorrow armed with keenest stings, “No child have I: no child have I,” No second misery prompts the sigh. When long I sought, alas, in vain, My husband's love and bliss to gain, In Ráma all my hopes I set And dreamed I might be happy yet. I, of the consorts first and best, Must bear my rivals' taunt and jest, And brook, though better far than they,
- **Translation**: 

---

### Verse 2 (Ramayan 0.422)
- **Original**: 404 The Ramayana The soul distressing words they say. What woman can be doomed to pine In misery more sore than mine, Whose hopeless days must still be spent In grief that ends not and lament? They scorned me when my son was nigh; When he is banished I must die. Me, whom my husband never prized, Kaikeyí's retinue despised With boundless insolence, though she Tops not in rank nor equals me. And they who do me service yet, Nor old allegiance quite forget, Whene'er they see Kaikeyí's son, With silent lips my glances shun. How, O my darling, shall I brook Each menace of Kaikeyí's look, And listen, in my low estate, To taunts of one so passionate? For seventeen years since thou wast born I sat and watched, ah me, forlorn! Hoping some blessed day to see Deliverance from my woes by thee. Now comes this endless grief and wrong, So dire I cannot bear it long, Sinking, with age and sorrow worn, Beneath my rivals' taunts and scorn. How shall I pass in dark distress My long lone days of wretchedness Without my Ráma's face, as bright As the full moon to cheer my sight? Alas, my cares thy steps to train, And fasts, and vows, and prayers are vain. Hard, hard, I ween, must be this heart
- **Translation**: 

---

### Verse 3 (Ramayan 0.423)
- **Original**: Canto XXI. Kausalyá Calmed. 405 To hear this blow nor burst apart, As some great river bank, when first The floods of Rain-time on it burst. No, Fate that speeds not will not slay, Nor Yama's halls vouchsafe me room, Or, like a lion's weeping prey, Death now had borne me to my doom. Hard is my heart and wrought of steel That breaks not with the crushing blow, Or in the pangs this day I feel My lifeless frame had sunk below. Death waits his hour, nor takes me now: But this sad thought augments my pain, That prayer and largess, fast and vow, And Heavenward service are in vain. Ah me, ah me! with fruitless toil Of rites austere a child I sought: Thus seed cast forth on barren soil Still lifeless lies and comes to naught. If ever wretch by anguish grieved Before his hour to death had fled, I mourning, like a cow bereaved, Had been this day among the dead.” [118] Canto XXI. Kausalyá Calmed.
- **Translation**: 

---

### Verse 4 (Ramayan 0.424)
- **Original**: 406 The Ramayana While thus Kau[alyá wept and sighed, With timely words sad LakshmaG cried: “O honoured Queen I like it ill That, subject to a woman's will, Ráma his royal state should quit And to an exile's doom submit. The aged king, fond, changed, and weak, Will as the queen compels him speak. But why should Ráma thus be sent To the wild woods in banishment? No least offence I find in him, I see no fault his fame to dim. Not one in all the world I know, Not outcast wretch, not secret foe, Whose whispering lips would dare assail His spotless life with slanderous tale. Godlike and bounteous, just, sincere, E'en to his very foemen dear: Who would without a cause neglect The right, and such a son reject? And if a king such order gave, In second childhood, passion's slave, What son within his heart would lay The senseless order, and obey? Come, Ráma, ere this plot be known Stand by me and secure the throne. Stand like the King who rules below, Stand aided by thy brother's bow: How can the might of meaner men Resist thy royal purpose then? My shafts, if rebels court their fate, Shall lay Ayodhyá desolate. Then shall her streets with blood be dyed Of those who stand on Bharat's side:
- **Translation**: 

---

### Verse 5 (Ramayan 0.425)
- **Original**: Canto XXI. Kausalyá Calmed. 407 None shall my slaughtering hand exempt, For gentle patience earns contempt. If, by Kaikeyí's counsel changed, Our father's heart be thus estranged, No mercy must our arm restrain, But let the foe be slain, be slain. For should the guide, respected long, No more discerning right and wrong, Turn in forbidden paths to stray, 'Tis meet that force his steps should stay. What power sufficient can he see, What motive for the wish has he, That to Kaikeyí would resign The empire which is justly thine? Can he, O conqueror of thy foes, Thy strength and mine in war oppose? Can he entrust, in our despite, To Bharat's hand thy royal right? I love this brother with the whole Affection of my faithful soul. Yea Queen, by bow and truth I swear, By sacrifice, and gift, and prayer, If Ráma to the forest goes, Or where the burning furnace glows, First shall my feet the forest tread, The flames shall first surround my head. My might shall chase thy grief and tears, As darkness flies when morn appears. Do thou, dear Queen, and Ráma too Behold what power like mine can do. My aged father I will kill, The vassal of Kaikeyí's will, Old, yet a child, the woman's thrall, Infirm, and base, the scorn of all.”
- **Translation**: 

---

### Verse 6 (Ramayan 0.426)
- **Original**: 408 The Ramayana Thus LakshmaG cried, the mighty-souled: Down her sad cheeks the torrents rolled, As to her son Kau[alyá spake: “Now thou hast heard thy brother, take His counsel if thou hold it wise, And do the thing his words advise, Do not, my son, with tears I pray, My rival's wicked word obey, Leave me not here consumed with woe, Nor to the wood, an exile, go. If thou, to virtue ever true, Thy duty's path would still pursue, The highest duty bids thee stay And thus thy mother's voice obey. Thus Ka[yap's great ascetic son A seat among the Immortals won: In his own home, subdued, he stayed, And honour to his mother paid. If reverence to thy sire be due, Thy mother claims like honour too, And thus I charge thee, O my child, Thou must not seek the forest wild. Ah, what to me were life and bliss, Condemned my darling son to miss? But with my Ráma near, to eat The very grass itself were sweet. But if thou still wilt go and leave Thy hapless mother here to grieve, I from that hour will food abjure, Nor life without my son endure. Then it will be thy fate to dwell In depth of world-detested hell. As Ocean in the olden time
- **Translation**: 

---

### Verse 7 (Ramayan 0.427)
- **Original**: Canto XXI. Kausalyá Calmed. 409 Was guilty of an impious crime That marked the lord of each fair flood As one who spills a Bráhman's blood.”288 Thus spake the queen, and wept, and sighed: Then righteous Ráma thus replied: “I have no power to slight or break Commandments which my father spake. I bend my head, dear lady, low, Forgive me, for I needs must go. Once KaGdu, mighty saint, who made His dwelling in the forest shade, [119] A cow — and duty's claims he knew— Obedient to his father, slew. And in the line from which we spring, When ordered by their sire the king, Through earth the sons of Sagar cleft, And countless things of life bereft.289 So Jamadagní's son290 obeyed His sire, when in the wood he laid His hand upon his axe, and smote Through Renuká his mother's throat. The deeds of these and more beside. Peers of the Gods, my steps shall guide, And resolute will I fulfil My father's word, my father's will. Nor I, O Queen, unsanctioned tread This righteous path, by duty led: The road my footsteps journey o'er Was traversed by the great of yore. 288 The commentators say that, in a former creation, Ocean grieved his mother and suffered in consequence the pains of hell. 289 As described in Book I Canto XL. 290 Parasúráma.
- **Translation**: 

---

### Verse 8 (Ramayan 0.428)
- **Original**: 410 The Ramayana This high command which all accept Shall faithfully by me be kept, For duty ne'er will him forsake Who fears his sire's command to break.” Thus to his mother wild with grief: Then thus to LakshmaG spake the chief Of those by whom the bow is bent, Mid all who speak, most eloquent: “I know what love for me thou hast, What firm devotion unsurpassed: Thy valour and thy worth I know, And glory that appals the foe. Blest youth, my mother's woe is great, It bends her 'neath its matchless weight: No claims will she, with blinded eyes, Of truth and patience recognize. For duty is supreme in place, And truth is duty's noblest base. Obedient to my sire's behest I serve the cause of duty best. For man should truly do whate'er To mother, Bráhman, sire, he sware: He must in duty's path remain, Nor let his word be pledged in vain. And, O my brother, how can I Obedience to this charge deny? Kaikeyí's tongue my purpose spurred, But 'twas my sire who gave the word. Cast these unholy thoughts aside Which smack of war and Warriors' pride; To duty's call, not wrath attend, And tread the path which I commend.”
- **Translation**: 

---

### Verse 9 (Ramayan 0.429)
- **Original**: Canto XXI. Kausalyá Calmed. 411 Ráma by fond affection moved His brother LakshmaG thus reproved; Then with joined hands and reverent head Again to Queen Kau[alyá said: “I needs must go— do thou consent— To the wild wood in banishment. O give me, by my life I pray, Thy blessing ere I go away. I, when the promised years are o'er, Shall see Ayodhyá's town once more. Then, mother dear, thy tears restrain, Nor let thy heart be wrung by pain: In time, my father's will obeyed, Shall I return from greenwood shade. My dear Videhan, thou, and I, Lakshma G, Sumitrá, feel this tie, And must my father's word obey, As duty bids that rules for aye. Thy preparations now forgo, And lock within thy breast thy woe, Nor be my pious wish withstood To go an exile to the wood.” Calm and unmoved the prince explained His duty's claim and purpose high, The mother life and sense regained, Looked on her son and made reply: “If reverence be thy father's due, The same by right and love is mine: Go not, my charge I thus renew, Nor leave me here in woe to pine, What were such lonely life to me, Rites to the shades, or deathless lot?
- **Translation**: 

---

### Verse 10 (Ramayan 0.430)
- **Original**: 412 The Ramayana More dear, my son, one hour with thee Than all the world where thou art not.” As bursts to view, when brands blaze high, Some elephant concealed by night, So, when he heard his mother's cry, Burnt Ráma's grief with fiercer might. Thus to the queen, half senseless still, And Lakshma G, burnt with heart-felt pain, True to the right, with steadfast will, His duteous speech he spoke again: “Brother, I know thy loving mind, Thy valour and thy truth I know, But now to claims of duty blind Thou and my mother swell my woe. The fruits of deeds in human life Make love, gain, duty, manifest, Dear when they meet as some fond wife With her sweet babes upon her breast. But man to duty first should turn Whene'er the three are not combined: For those who heed but gain we spurn, And those to pleasure all resigned. Shall then the virtuous disobey Hosts of an aged king and sire, Though feverous joy that father sway, Or senseless love or causeless ire? I have no power, commanded thus, To slight his promise and decree: The honoured sire of both of us, My mother's lord and life is he. Shall she, while yet the holy king Is living, on the right intent,— Shall she, like some poor widowed thing, Go forth with me to banishment?
- **Translation**: 

---

### Verse 11 (Ramayan 0.431)
- **Original**: Canto XXII. Lakshman Calmed. 413 Now, mother, speed thy parting son, And let thy blessing soothe my pain, [120] That I may turn, mine exile done, Like King Yayáti, home again. Fair glory and the fruit she gives, For lust of sway I ne'er will slight: What, for the span a mortal lives. Were rule of faith without the right?” He soothed her thus, firm to the last His counsel to his brother told: Then round the queen in reverence passed, And held her in his loving hold. Canto XXII. Lakshman Calmed. So Ráma kept unshaken still His noble heart with iron will. To his dear brother next he turned, Whose glaring eyes with fury burned, Indignant, panting like a snake, And thus again his counsel spake: “Thine anger and thy grief restrain, And firm in duty's path remain. Dear brother, lay thy scorn aside, And be the right thy joy and pride. Thy ready zeal and thoughtful care To aid what rites should grace the heir,— These 'tis another's now to ask; Come, gird thee for thy noble task, That Bharat's throning rites may he Graced with the things prepared for me.
- **Translation**: 

---

### Verse 12 (Ramayan 0.432)
- **Original**: 414 The Ramayana And with thy gentle care provide That her fond heart, now sorely tried With fear and longing for my sake, With doubt and dread may never ache. To know that thoughts of coming ill One hour that tender bosom fill With agony and dark despair Is grief too great for me to bear. I cannot, brother, call to mind One wilful fault or undesigned, When I have pained in anything My mothers or my sire the king. The right my father keeps in view, In promise, word, and action true; Let him then all his fear dismiss, Nor dread the loss of future bliss. He fears his truth herein will fail: Hence bitter thoughts his heart assail. He trembles lest the rites proceed, And at his pangs my heart should bleed. So now this earnest wish is mine, The consecration to resign, And from this city turn away To the wild wood with no delay. My banishment to-day will free Kaikeyí from her cares, that she, At last contented and elate, May Bharat's throning celebrate. Then will the lady's trouble cease, Then will her heart have joy and peace, When wandering in the wood I wear Deerskin, and bark, and matted hair. Nor shall by me his heart be grieved Whose choice approved, whose mind conceived
- **Translation**: 

---

### Verse 13 (Ramayan 0.433)
- **Original**: Canto XXII. Lakshman Calmed. 415 This counsel which I follow. No, Forth to the forest will I go. 'Tis Fate, Sumitrás son, confess, That sends me to the wilderness. 'Tis Fate alone that gives away To other hands the royal sway. How could Kaikeyí's purpose bring On me this pain and suffering, Were not her change of heart decreed By Fate whose will commands the deed? I know my filial love has been The same throughout for every queen, And with the same affection she Has treated both her son and me. Her shameful words of cruel spite To stay the consecrating rite, And drive me banished from the throne,— These I ascribe to Fate alone, How could she, born of royal race, Whom nature decks with fairest grace, Speak like a dame of low degree Before the king to torture me? But Fate, which none may comprehend, To which all life must bow and bend, In her and me its power has shown, And all my hopes are overthrown. What man, Sumitrá's darling, may Contend with Fate's resistless sway, Whose all-commanding power we find Our former deeds alone can bind? Our life and death, our joy and pain, Anger and fear, and loss and gain, Each thing that is, in every state, All is the work of none but Fate.
- **Translation**: 

---

### Verse 14 (Ramayan 0.434)
- **Original**: 416 The Ramayana E'en saints, inspired with rigid zeal, When once the stroke of Fate they feel, In sternest vows no more engage, And fall enslaved by love and rage. So now the sudden stroke whose weight Descends unlooked for, comes of Fate, And with unpitying might destroys The promise of commencing joys. Weigh this true counsel in thy soul: With thy firm heart thy heart control; Then, brother, thou wilt cease to grieve For hindered rites which now I leave. So cast thy needless grief away, And strictly my commands obey. Those preparations check with speed, Nor let my throning rites proceed. Those urns that stand prepared to shed King-making drops upon my head, Shall, with their pure lustrations now Inaugurate my hermit's vow.[121] Yet what have I to do with things That touch the state and pomp of kings? These hands of mine shall water take To sanctify the vow I make. Now Lakshma G, let thy heart no more My fortune changed and lost deplore. A forest life more joys may bring Than those that wait upon a king, Now though her arts successful mar My consecrating rite, Let not the youngest queen too far Thy jealous fear excite. Nor let one thought suggesting ill Upon our father fall,
- **Translation**: 

---

### Verse 15 (Ramayan 0.435)
- **Original**: Canto XXIII. Lakshman's Anger. 417 But let thy heart remember still That Fate is lord of all.” Canto XXIII. Lakshman's Anger. Thus Ráma to his brother said; And Lakshma G bent his drooping head. In turns by grief and pride impelled, A middle course of thought he held, Then in a frown of anger, bent His brows that chief most excellent, And like a serpent in his hole, Breathed fierce and fast in wrath of soul. His threatening brows so darkly frowned, His eyes so fiercely glanced around, They made his glare, which none might brook, Like some infuriate lion's look. Like some wild elephant, full oft He raised and shook his hand291 aloft. Now turned his neck to left and right Now bent, now raised its stately height. Now in his rage that sword he felt Which mangling wounds to foemen dealt, With sidelong glance his brother eyed, And thus in burning words replied: “Thy rash resolve, thy eager haste, Thy mighty fear, are all misplaced: No room is here for duty's claim, 291 The Sanskrit wordhastasignifies bothhand, and the trunk of“The beast that bears between his eyes a serpent for a head.”
- **Translation**: 

---

### Verse 16 (Ramayan 0.436)
- **Original**: 418 The Ramayana No cause to dread the people's blame. Can one as brave as thou consent To use a coward's argument? The glory of the Warrior race With craven speech his lips debase? Can one like thee so falsely speak, Exalting Fate, confessed so weak? Canst thou, undoubting still restrain? Suspicions of those sinful twain? Canst thou, most duteous, fail to know Their hearts are set on duty's show? They with deceit have set their trains, And now the fruit rewards their pains. Had they not long ago agreed, O Ráma, on this treacherous deed, That promised boon, so long retained, He erst had given and she had gained. I cannot, O my brother, bear To see another throned as heir With rites which all our people hate: Then, O, this passion tolerate. This vaunted duty which can guide Thy steps from wisdom's path aside, And change the counsel of thy breast, O lofty-hearted, I detest. Wilt thou, when power and might are thine, Submit to this abhorred design? Thy father's impious hest fulfil, That vassal of Kaikeyí's will? But if thou still wilt shut thine eyes, Nor see the guile herein that lies, My soul is sad, I deeply mourn, And duty seems a thing to scorn. Canst thou one moment think to please
- **Translation**: 

---

### Verse 17 (Ramayan 0.437)
- **Original**: Canto XXIII. Lakshman's Anger. 419 This pair who live for love and ease, And 'gainst thy peace, as foes, allied, With tenderest names their hatred hide? Now if thy judgment still refers To Fate this plot of his and hers, My mind herein can ne'er agree: And O, in this be ruled by me. Weak, void of manly pride are they Who bend to Fate's imputed sway: The choicest souls, the nobly great Disdain to bow their heads to Fate. And he who dares his Fate control With vigorous act and manly soul, Though threatening Fate his hopes assail, Unmoved through all need never quail. This day mankind shall learn aright The power of Fate and human might, So shall the gulf that lies between A man and Fate be clearly seen. The might of Fate subdued by me This hour the citizens shall see, Who saw its intervention stay Thy consecrating rites to-day. My power shall turn this Fate aside, That threatens, as, with furious stride, An elephant who scorns to feel, In rage unchecked, the driver's steel. Not the great Lords whose sleepless might Protects the worlds, shall stay the rite Though earth, hell, heaven combine their powers: And shall we fear this sire of ours? Then if their minds are idly bent To doom thee, King, to banishment, Through twice seven years of exile they [122]
- **Translation**: 

---

### Verse 18 (Ramayan 0.438)
- **Original**: 420 The Ramayana Shall in the lonely forest stay. I will consume the hopes that fire The queen Kaikeyí and our sire, That to her son this check will bring Advantage, making Bharat king. The power of Fate will ne'er withstand The might that arms my vigorous hand; If danger and distress assail, My fearless strength will still prevail. A thousand circling years shall flee: The forest then thy home shall be, And thy good sons, succeeding, hold The empire which their sire controlled. The royal saints, of old who reigned, For aged kings this rest ordained: These to their sons their realm commit That they, like sires, may cherish it. O pious soul, if thou decline The empire which is justly thine, Lest, while the king distracted lies, Disorder in the state should rise, I,— or no mansion may I find In worlds to hero souls assigned,— The guardian of thy realm will be, As the sea-bank protects the sea. Then cast thine idle fears aside: With prosperous rites be sanctified. The lords of earth may strive in vain: My power shall all their force restrain. My pair of arms, my warrior's bow Are not for pride or empty show: For no support these shafts were made; And binding up ill suits my blade: To pierce the foe with deadly breach—
- **Translation**: 

---

### Verse 19 (Ramayan 0.439)
- **Original**: Canto XXIII. Lakshman's Anger. 421 This is the work of all and each. But small, methinks the love I show For him I count my mortal foe. Soon as my trenchant steel is bare, Flashing its lightning through the air, I heed no foe, nor stand aghast Though Indra's self the levin cast. Then shall the ways be hard to pass, Where chariots lie in ruinous mass; When elephant and man and steed Crushed in the murderous onslaught bleed, And legs and heads fall, heap on heap, Beneath my sword's tremendous sweep. Struck by my keen brand's trenchant blade, Thine enemies shall fall dismayed, Like towering mountains rent in twain, Or lightning clouds that burst in rain. When armed with brace and glove I stand, And take my trusty bow in hand, Who then shall vaunt his might? who dare Count him a man to meet me there? Then will I loose my shafts, and strike Man, elephant, and steed alike: At one shall many an arrow fly, And many a foe with one shall die. This day the world my power shall see, That none in arms can rival me: My strength the monarch shall abase, And set thee, lord, in lordliest place. These arms which breathe the sandal's scent, Which golden bracelets ornament, These hands which precious gifts bestow, Which guard the friend and smite the foe, A nobler service shall assay,
- **Translation**: 

---

### Verse 20 (Ramayan 0.440)
- **Original**: 422 The Ramayana And fight in Ráma's cause to-day, The robbers of thy rights to stay. Speak, brother, tell thy foeman's name Whom I, in conquering strife, May strip of followers and fame, Of fortune, or of life. Say, how may all this sea-girt land Be brought to own thy sway: Thy faithful servant here I stand To listen and obey.” Then strove the bride of Raghu's race Sad LakshmaG's heart to cheer, While slowly down the hero's face, Unchecked, there rolled a tear. “The orders of my sire,” he cried, “My will shall ne'er oppose: I follow still, whate'er betide, The path which duty shows.” Canto XXIV. Kausalyá Calmed. But when Kau[alyásaw that he Resolved to keep his sire's decree, While tears and sobs her utterance broke, Her very righteous speech she spoke: “Can he, a stranger yet to pain, Whose pleasant words all hearts enchain, Son of the king and me the queen, Live on the grain his hands may glean; Can he, whose slaves and menials eat The finest cakes of sifted wheat—
- **Translation**: 

---



--- End of Ramayan_batch_22.md ---


--- Start of Ramayan_batch_23.md ---

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

### Verse 1 (Ramayan 0.441)
- **Original**: Canto XXIV. Kausalyá Calmed. 423 Can Ráma in the forest live On roots and fruit which woodlands give; Who will believe, who will not fear When the sad story smites his ear, That one so dear, so noble held, Is by the king his sire expelled? Now surely none may Fate resist, Which orders all as it may list, If, Ráma, in thy strength and grace, The woods become thy dwelling-place. A childless mother long I grieved, And many a sigh for offspring heaved, With wistful longing weak and worn Till thou at last, my son, wast born. Fanned by the storm of that desire Deep in my soul I felt the fire, Whose offerings flowed from weeping eyes, With fuel fed of groans and sighs, [123] While round the flame the smoke grew hot Of tears because thou camest not. Now reft of thee, too fiery fierce The flame of woe my heart will pierce, As, when the days of spring return, The sun's hot beams the forest burn. The mother cow still follows near The wanderings of her youngling dear. So close to thine my feet shall be, Where'er thou goest following thee.” Ráma, the noblest lord of men, Heard his fond mother's speech, and then In soothing words like these replied To the sad queen who wept and sighed: “Nay, by Kaikeyí's art beguiled,
- **Translation**: 

---

### Verse 2 (Ramayan 0.442)
- **Original**: 424 The Ramayana When I am banished to the wild, If thou, my mother, also fly, The aged king will surely die. When wedded dames their lords forsake, Long for the crime their souls shall ache. Thou must not e'en in thought within Thy bosom frame so dire a sin. Long as Kakutstha's son, who reigns Lord of the earth, in life remains, Thou must with love his will obey: This duty claims, supreme for aye. Yes, mother, thou and I must be Submissive to my sire's decree, King, husband, sire is he confessed, The lord of all, the worthiest. I in the wilds my days will spend Till twice seven years have reached an end, Then with great joy will come again, And faithful to thy hests remain.” Kau [alyá by her son addressed, With love and passion sore distressed, Afflicted, with her eyes bedewed, To Ráma thus her speech renewed: “Nay, Ráma, but my heart will break If with these queens my home I make. Lead me too with thee; let me go And wander like a woodland roe.” Then, while no tear the hero shed, Thus to the weeping queen he said: “Mother, while lives the husband, he Is woman's lord and deity. O dearest lady, thou and I Our lord and king must ne'er deny;
- **Translation**: 

---

### Verse 3 (Ramayan 0.443)
- **Original**: Canto XXIV. Kausalyá Calmed. 425 The lord of earth himself have we Our guardian wise and friend to be. And Bharat, true to duty's call, Whose sweet words take the hearts of all, Will serve thee well, and ne'er forget The virtuous path before him set. Be this, I pray, thine earnest care, That the old king my father ne'er, When I have parted hence, may know, Grieved for his son, a pang of woe. Let not this grief his soul distress, To kill him with the bitterness. With duteous care, in every thing, Love, comfort, cheer the aged king. Though, best of womankind, a spouse Keeps firmly all her fasts and vows, Nor yet her husband's will obeys, She treads in sin's forbidden ways. She to her husband's will who bends, Goes to high bliss that never ends, Yea, though the Gods have found in her No reverential worshipper. Bent on his weal, a woman still Must seek to do her husband's will: For Scripture, custom, law uphold This duty Heaven revealed of old. Honour true Bráhmans for my sake, And constant offerings duly make, With fire-oblations and with flowers, To all the host of heavenly powers. Look to the coming time, and yearn For the glad hour of my return. And still thy duteous course pursue, Abstemious, humble, kind, and true.
- **Translation**: 

---

### Verse 4 (Ramayan 0.444)
- **Original**: 426 The Ramayana The highest bliss shalt thou obtain When I from exile come again, If, best of those who keep the right, The king my sire still see the light.” The queen, by Ráma thus addressed, Still with a mother's grief oppressed, While her long eyes with tears were dim, Began once more and answered him: “Not by my pleading may be stayed The firm resolve thy soul has made. My hero, thou wilt go; and none The stern commands of Fate may shun. Go forth, dear child whom naught can bend, And may all bliss thy steps attend. Thou wilt return, and that dear day Will chase mine every grief away. Thou wilt return, thy duty done, Thy vows discharged, high glory won; From filial debt wilt thou be free, And sweetest joy will come on me. My son, the will of mighty Fate At every time must dominate, If now it drives thee hence to stray Heedless of me who bid thee stay. Go, strong of arm, go forth, my boy, Go forth, again to come with joy, And thine expectant mother cheer With those sweet tones she loves to hear. O that the blessed hour were nigh When thou shalt glad this anxious eye, With matted hair and hermit dress returning from the wilderness.” Kau [alyá's conscious soul approved,
- **Translation**: 

---

### Verse 5 (Ramayan 0.445)
- **Original**: Canto XXV. Kausalyá's Blessing. 427 As her proud glance she bent On Ráma constant and unmoved, Resolved on banishment. Such words, with happy omens fraught To her dear son she said, Invoking with each eager thought A blessing on his head. [124] Canto XXV. Kausalyá's Blessing. Her grief and woe she cast aside, Her lips with water purified, And thus her benison began That mother of the noblest man: “If thou wilt hear no words of mine, Go forth, thou pride of Raghu's line. Go, darling, and return with speed, Walking where noble spirits lead. May virtue on thy steps attend, And be her faithful lover's friend. May Those to whom thy vows are paid In temple and in holy shade, With all the mighty saints combine To keep that precious life of thine. The arms wise Vi[vámitra292 gave Thy virtuous soul from danger save. Long be thy life: thy sure defence Shall be thy truthful innocence, 292 See P. 41.
- **Translation**: 

---

### Verse 6 (Ramayan 0.446)
- **Original**: 428 The Ramayana And that obedience, naught can tire, To me thy mother and thy sire. May fanes where holy fires are fed, Altars with grass and fuel spread, Each sacrificial ground, each tree, Rock, lake, and mountain, prosper thee. Let old Viráj,293 and Him who made The universe, combine to aid; Let Indra and each guardian Lord Who keeps the worlds, their help afford, And be thy constant friend the Sun, Lord Púshá, Bhaga, Aryuman.294 Fortnights and seasons, nights and days, Years, months, and hours, protect thy ways, Vrihaspati shall still be nigh, The War-God, and the Moon on high, And Nárad295 and the sainted seven296 Shall watch thee from their starry heaven. The mountains, and the seas which ring The world, and VaruGa the King, Sky, ether, and the wind, whate'er Moves not or moves, for thee shall care. Each lunar mansion be benign, With happier light the planets shine; All gods, each light in heaven that glows, Protect my child where'er he goes. The twilight hours, the day and night, Keep in the wood thy steps aright. Watch, minute, instant, as they flee, Shall all bring happiness to thee. 293 The first progeny of Brahmá or Brahmá himself. 294 These are three names of the Sun. 295 See P. 1. 296 The saints who form the constellation of Ursa Major.
- **Translation**: 

---

### Verse 7 (Ramayan 0.447)
- **Original**: Canto XXV. Kausalyá's Blessing. 429 Celestials and the Titan brood Protect thee in thy solitude, And haunt the mighty wood to bless The wanderer in his hermit dress. Fear not, by mightier guardians screened, The giant or night-roving fiend; Nor let the cruel race who tear Man's flesh for food thy bosom scare. Far be the ape, the scorpion's sting, Fly, gnat, and worm, and creeping thing. Thee shall the hungry lion spare, The tiger, elephant, and bear: Safe, from their furious might repose, Safe from the horned buffaloes. Each savage thing the forests breed, That love on human flesh to feed, Shall for my child its rage abate, When thus its wrath I deprecate. Blest be thy ways: may sweet success The valour of my darling bless. To all that Fortune can bestow, Go forth, my child, my Ráma, go. Go forth, O happy in the love Of all the Gods below, above; And in those guardian powers confide Thy paths who keep, thy steps who guide. May Zukra,297 Yáma, Sun, and Moon, And He who gives each golden boon,298 Won by mine earnest prayers, be good To thee, my son, in DaG ak wood. Fire, wind, and smoke, each text and spell From mouths of holy seers that fell, 297 The regent of the planet Venus. 298 Kuvera.
- **Translation**: 

---

### Verse 8 (Ramayan 0.448)
- **Original**: 430 The Ramayana Guard Ráma when his limbs he dips, Or with the stream makes pure his lips! May the great saints and He, the Lord Who made the worlds, by worlds adored, And every God in heaven beside My banished Ráma keep and guide.” Thus with due praise the long-eyed dame, Ennobled by her spotless fame, With wreaths of flowers and precious scent Worshipped the Gods, most reverent. A high-souled Bráhman lit the fire, And offered, at the queen's desire, The holy oil ordained to burn For Ráma's weal and safe return. Kau [alyá best of dames, with care Set oil, wreaths, fuel, mustard, there. Then when the rites of fire had ceased, For Ráma's bliss and health, the priest, Standing without gave what remained In general offering,299 as ordained.[125] Dealing among the twice-horn train Honey, and curds, and oil, and grain, He bade each heart and voice unite To bless the youthful anchorite. Then Ráma's mother, glorious dame Bestowed, to meet the Bráhman's claim, A lordly fee for duty done: And thus again addressed her son: 299 Bali, or the presentation of food to all created beings, is one of the five great sacraments of the Hindu religion: it consists in throwing a small parcel of the offering,Ghee, or rice, or the like, into the open air at the back of the house.
- **Translation**: 

---

### Verse 9 (Ramayan 0.449)
- **Original**: Canto XXV. Kausalyá's Blessing. 431 “Such blessings as the Gods o'erjoyed Poured forth, when Vritra300 was destroyed, On Indra of the thousand eyes, Attend, my child, thine enterprise! Yea, such as Vinatá once gave To King SuparGa301 swift and brave, Who sought the drink that cheers the skies, Attend, my child, thine enterprise! Yea, such as, when the Amrit rose,302 And Indra slew his Daitya foes, The royal Aditi bestowed On Him whose hand with slaughter glowed Of that dire brood of monstrous size, Attend, my child, thine enterprise! E'en such as peerless VishGu graced, When with his triple step he paced, Outbursting from the dwarf's disguise,303 Attend, my child, thine enterprise! Floods, isles, and seasons as they fly, Worlds, Vedas, quarters of the sky, Combine, O mighty-armed, to bless Thee destined heir of happiness!” The long-eyed lady ceased: she shed Pure scent and grain upon his head. And that prized herb whose sovereign power Preserves from dark misfortune's hour, Upon the hero's arm she set, To be his faithful amulet. While holy texts she murmured low, 300 In mythology, a demon slain by Indra. 301 Called also Garu , the King of the birds, offspring of Vinatá. See p. 53. 302 See P. 56. 303 See P. 43.
- **Translation**: 

---

### Verse 10 (Ramayan 0.450)
- **Original**: 432 The Ramayana And spoke glad words though crushed by woe, Concealing with obedient tongue The pangs with which her heart was wrung. She bent, she kissed his brow, she pressed Her darling to her troubled breast: “Firm in thy purpose, go,” she cried, “Go Ráma, and may bliss betide. Attain returning safe and well, Triumphant in Ayodhyá, dwell. Then shall my happy eyes behold The empire by thy will controlled. Then grief and care shall leave no trace, Joy shall light up thy mother's face, And I shall see my darling reign, In moonlike glory come again. These eyes shall fondly gaze on thee So faithful to thy sire's decree, When thou the forest wild shalt quit On thine ancestral throne to sit. Yea, thou shalt turn from exile back, Nor choicest blessings ever lack, Then fill with rapture ever new My bosom and thy consort's too. To Ziva and the heavenly host My worship has been paid, To mighty saint, to godlike ghost, To every wandering shade. Forth to the forest thou wilt hie, Therein to dwell so long: Let all the quarters of the sky Protect my child from wrong.” Her blessings thus the queen bestowed; Then round him fondly paced, And often, while her eyes o'erflowed,
- **Translation**: 

---

### Verse 11 (Ramayan 0.451)
- **Original**: Canto XXVI. Alone With Sítá. 433 Her dearest son embraced. Kau [alyá's honoured feet he pressed, As round her steps she bent, And radiant with her prayers that blessed, To Sítá's home he went. Canto XXVI. Alone With Sítá. So Ráma, to his purpose true, To Queen Kau[alyá bade adieu, Received the benison she gave, And to the path of duty clave. As through the crowded street he passed, A radiance on the way he cast, And each fair grace, by all approved, The bosoms of the people moved. Now of the woeful change no word The fair Videhan bride had heard; The thought of that imperial rite Still filled her bosom with delight. With grateful heart and joyful thought The Gods in worship she had sought, And, well in royal duties learned, Sat longing till her lord returned, Not all unmarked by grief and shame Within his sumptuous home he came, And hurried through the happy crowd With eye dejected, gloomy-browed. Up Sítá sprang, and every limb Trembled with fear at sight of him.
- **Translation**: 

---

### Verse 12 (Ramayan 0.452)
- **Original**: 434 The Ramayana She marked that cheek where anguish fed, Those senses care-disquieted. For, when he looked on her, no more Could his heart hide the load it bore, Nor could the pious chief control The paleness o'er his cheek that stole. His altered cheer, his brow bedewed With clammy drops, his grief she viewed, And cried, consumed with fires of woe, “What, O my lord, has changed thee so?[126] Vrihaspati looks down benign, And the moon rests in Pushya's sign, As Bráhmans sage this day declare: Then whence, my lord, this grief and care? Why does no canopy, like foam For its white beauty, shade thee home, Its hundred ribs spread wide to throw Splendour on thy fair head below? Where are the royal fans, to grace The lotus beauty of thy face, Fair as the moon or wild-swan's wing, And waving round the new-made king? Why do no sweet-toned bards rejoice To hail thee with triumphant voice? No tuneful heralds love to raise Loud music in their monarch's praise? Why do no Bráhmans, Scripture-read, Pour curds and honey on thy head, Anointed, as the laws ordain, With holy rites, supreme to reign? Where are the chiefs of every guild? Where are the myriads should have filled The streets, and followed home their king With merry noise and triumphing?
- **Translation**: 

---

### Verse 13 (Ramayan 0.453)
- **Original**: Canto XXVI. Alone With Sítá. 435 Why does no gold-wrought chariot lead With four brave horses, best for speed? No elephant precede the crowd Like a huge hill or thunder cloud, Marked from his birth for happy fate, Whom signs auspicious decorate? Why does no henchman, young and fair, Precede thee, and delight to bear Entrusted to his reverent hold The burthen of thy throne of gold? Why, if the consecrating rite Be ready, why this mournful plight? Why do I see this sudden change, This altered mien so sad and strange?” To her, as thus she weeping cried, Raghu's illustrious son replied: “Sítá, my honoured sire's decree Commands me to the woods to flee. O high-born lady, nobly bred In the good paths thy footsteps tread, Hear, Janak's daughter, while I tell The story as it all befell. Of old my father true and brave Two boons to Queen Kaikeyí gave. Through these the preparations made For me to-day by her are stayed, For he is bound to disallow This promise by that earlier vow. In DaG ak forest wild and vast Must fourteen years by me be passed. My father's will makes Bharat heir, The kingdom and the throne to share. Now, ere the lonely wild I seek,
- **Translation**: 

---

### Verse 14 (Ramayan 0.454)
- **Original**: 436 The Ramayana I come once more with thee to speak. In Bharat's presence, O my dame, Ne'er speak with pride of Ráma's name: Another's eulogy to hear Is hateful to a monarch's ear. Thou must with love his rule obey To whom my father yields the sway. With love and sweet observance learn His grace, and more the king's, to earn. Now, that my father may not break The words of promise that he spake, To the drear wood my steps are bent: Be firm, good Sítá, and content. Through all that time, my blameless spouse, Keep well thy fasts and holy vows. Rise from thy bed at break of day, And to the Gods due worship pay. With meek and lowly love revere The lord of men, my father dear, And reverence to Kau[alyá show, My mother, worn with eld and woe: By duty's law, O best of dames, High worship from thy love she claims, Nor to the other queens refuse Observance, rendering each her dues: By love and fond attention shown They are my mothers like mine own. Let Bharat andZatrughna bear In thy sweet love a special share: Dear as my life, O let them be Like brother and like son to thee. In every word and deed refrain From aught that Bharat's soul may pain: He is Ayodhyá's king and mine,
- **Translation**: 

---

### Verse 15 (Ramayan 0.455)
- **Original**: Canto XXVII. Sítá's Speech. 437 The head and lord of all our line. For those who serve and love them much With weariless endeavour, touch And win the gracious hearts of kings. While wrath from disobedience springs. Great monarchs from their presence send Their lawful sons who still offend, And welcome to the vacant place Good children of an alien race. Then, best of women, rest thou here, And Bharat's will with love revere. Obedient to thy king remain, And still thy vows of truth maintain. To the wide wood my steps I bend: Make thou thy dwelling here; See that thy conduct ne'er offend, And keep my words, my dear.” Canto XXVII. Sítá's Speech. His sweetly-speaking bride, who best Deserved her lord, he thus addressed. Then tender love bade passion wake, And thus the fair Videhan spake: “What words are these that thou hast said? Contempt of me the thought has bred. O best of heroes, I dismiss With bitter scorn a speech like this: [127]
- **Translation**: 

---

### Verse 16 (Ramayan 0.456)
- **Original**: 438 The Ramayana Unworthy of a warrior's fame It taints a monarch's son with shame, Ne'er to be heard from those who know The science of the sword and bow. My lord, the mother, sire, and son Receive their lots by merit won; The brother and the daughter find The portions to their deeds assigned. The wife alone, whate'er await, Must share on earth her husband's fate. So now the king's command which sends Thee to the wild, to me extends. The wife can find no refuge, none, In father, mother, self, or son: Both here, and when they vanish hence, Her husband is her sole defence. If, Raghu's son, thy steps are led Where DaG ak's pathless wilds are spread, My foot before thine own shall pass Through tangled thorn and matted grass. Dismiss thine anger and thy doubt: Like refuse water cast them out, And lead me, O my hero, hence— I know not sin— with confidence. Whate'er his lot, 'tis far more sweet To follow still a husband's feet Than in rich palaces to lie, Or roam at pleasure through the sky. My mother and my sire have taught What duty bids, and trained each thought, Nor have I now mine ear to turn The duties of a wife to learn. I'll seek with thee the woodland dell And pathless wild where no men dwell,
- **Translation**: 

---

### Verse 17 (Ramayan 0.457)
- **Original**: Canto XXVII. Sítá's Speech. 439 Where tribes of silvan creatures roam, And many a tiger makes his home. My life shall pass as pleasant there As in my father's palace fair. The worlds shall wake no care in me; My only care be truth to thee. There while thy wish I still obey, True to my vows with thee I'll stray, And there shall blissful hours be spent In woods with honey redolent. In forest shades thy mighty arm Would keep a stranger's life from harm, And how shall Sítá think of fear When thou, O glorious lord, art near? Heir of high bliss, my choice is made, Nor can I from my will be stayed. Doubt not; the earth will yield me roots, These will I eat, and woodland fruits; And as with thee I wander there I will not bring thee grief or care. I long, when thou, wise lord, art nigh, All fearless, with delighted eye To gaze upon the rocky hill, The lake, the fountain, and the rill; To sport with thee, my limbs to cool, In some pure lily-covered pool, While the white swan's and mallard's wings Are plashing in the water-springs. So would a thousand seasons flee Like one sweet day, if spent with thee. Without my lord I would not prize A home with Gods above the skies: Without my lord, my life to bless, Where could be heaven or happiness?
- **Translation**: 

---

### Verse 18 (Ramayan 0.458)
- **Original**: 440 The Ramayana Forbid me not: with thee I go The tangled wood to tread. There will I live with thee, as though This roof were o'er my head. My will for thine shall be resigned; Thy feet my steps shall guide. Thou, only thou, art in my mind: I heed not all beside. Thy heart shall ne'er by me be grieved; Do not my prayer deny: Take me, dear lord; of thee bereaved Thy Sítá swears to die.” These words the duteous lady spake, Nor would he yet consent His faithful wife with him to take To share his banishment. He soothed her with his gentle speech; To change her will he strove; And much he said the woes to teach Of those in wilds who rove. Canto XXVIII. The Dangers Of The Wood. Thus Sítá spake, and he who knew His duty, to its orders true, Was still reluctant as the woes Of forest life before him rose. He sought to soothe her grief, to dry The torrent from each brimming eye, And then, her firm resolve to shake, These words the pious hero spake:
- **Translation**: 

---

### Verse 19 (Ramayan 0.459)
- **Original**: Canto XXVIII. The Dangers Of The Wood. 441 “O daughter of a noble line, Whose steps from virtue ne'er decline, Remain, thy duties here pursue, As my fond heart would have thee do. Now hear me, Sítá, fair and weak, And do the words that I shall speak. Attend and hear while I explain Each danger in the wood, each pain. Thy lips have spoken: I condemn The foolish words that fell from them. This senseless plan, this wish of thine To live a forest life, resign. The names of trouble and distress Suit well the tangled wilderness. In the wild wood no joy I know, A forest life is nought but woe. The lion in his mountain cave Answers the torrents as they rave, And forth his voice of terror throws: The wood, my love, is full of woes. [128] There mighty monsters fearless play, And in their maddened onset slay The hapless wretch who near them goes: The wood, my love, is full of woes. 'Tis hard to ford each treacherous flood, So thick with crocodiles and mud, Where the wild elephants repose: The wood, my love, is full of woes. Or far from streams the wanderer strays Through thorns and creeper-tangled ways, While round him many a wild-cock crows: The wood, my love, is full of woes. On the cold ground upon a heap Of gathered leaves condemned to sleep,
- **Translation**: 

---

### Verse 20 (Ramayan 0.460)
- **Original**: 442 The Ramayana Toil-wearied, will his eyelids close: The wood, my love, is full of woes. Long days and nights must he content His soul with scanty aliment, What fruit the wind from branches blows: The wood, my love, is full of woes. O Sítá, while his strength may last, The ascetic in the wood must fast, Coil on his head his matted hair, And bark must be his only wear. To Gods and spirits day by day The ordered worship he must pay, And honour with respectful care Each wandering guest who meets him there. The bathing rites he ne'er must shun At dawn, at noon, at set of sun, Obedient to the law he knows: The wood, my love, is full of woes. To grace the altar must be brought The gift of flowers his hands have sought— The debt each pious hermit owes: The wood, my love, is full of woes. The devotee must be content To live, severely abstinent, On what the chance of fortune shows: The wood, my love, is full of woes. Hunger afflicts him evermore: The nights are black, the wild winds roar; And there are dangers worse than those: The wood, my love, is full of woes. There creeping things in every form Infest the earth, the serpents swarm, And each proud eye with fury glows: The wood, my love, is full of woes.
- **Translation**: 

---



--- End of Ramayan_batch_23.md ---


--- Start of Ramayan_batch_24.md ---

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

### Verse 1 (Ramayan 0.461)
- **Original**: Canto XXIX. Sítá's Appeal. 443 The snakes that by the rives hide In sinuous course like rivers glide, And line the path with deadly foes: The wood, my love, is full of woes. Scorpions, and grasshoppers, and flies Disturb the wanderer as he lies, And wake him from his troubled doze: The wood, my love, is full of woes. Trees, thorny bushes, intertwined, Their branched ends together bind, And dense with grass the thicket grows: The wood, my dear, is full of woes, With many ills the flesh is tried, When these and countless fears beside Vex those who in the wood remain: The wilds are naught but grief and pain. Hope, anger must be cast aside, To penance every thought applied: No fear must be of things to fear: Hence is the wood for ever drear. Enough, my love: thy purpose quit: For forest life thou art not fit. As thus I think on all, I see The wild wood is no place for thee.” Canto XXIX. Sítá's Appeal. Thus Ráma spake. Her lord's address The lady heard with deep distress, And, as the tear bedimmed her eye, In soft low accents made reply:
- **Translation**: 

---

### Verse 2 (Ramayan 0.462)
- **Original**: 444 The Ramayana “The perils of the wood, and all The woes thou countest to appal, Led by my love I deem not pain; Each woe a charm, each loss a gain. Tiger, and elephant, and deer, Bull, lion, buffalo, in fear, Soon as thy matchless form they see, With every silvan beast will flee. With thee, O Ráma, I must go: My sire's command ordains it so. Bereft of thee, my lonely heart Must break, and life and I must part. While thou, O mighty lord, art nigh, Not even He who rules the sky, Though He is strongest of the strong, With all his might can do me wrong. Nor can a lonely woman left By her dear husband live bereft. In my great love, my lord, I ween, The truth of this thou mayst have seen. In my sire's palace long ago I heard the chief of those who know, The truth-declaring Bráhmans, tell My fortune, in the wood to dwell. I heard their promise who divine The future by each mark and sign, And from that hour have longed to lead The forest life their lips decreed. Now, mighty Ráma, I must share Thy father's doom which sends thee there; In this I will not be denied, But follow, love, where thou shalt guide. O husband, I will go with thee, Obedient to that high decree.
- **Translation**: 

---

### Verse 3 (Ramayan 0.463)
- **Original**: Canto XXIX. Sítá's Appeal. 445 Now let the Bráhmans' words be true, For this the time they had in view. I know full well the wood has woes; But they disturb the lives of those Who in the forest dwell, nor hold Their rebel senses well controlled. [129] In my sire's halls, ere I was wed, I heard a dame who begged her bread Before my mother's face relate What griefs a forest life await. And many a time in sport I prayed To seek with thee the greenwood shade, For O, my heart on this is set, To follow thee, dear anchoret. May blessings on thy life attend: I long with thee my steps to bend, For with such hero as thou art This pilgrimage enchants my heart. Still close, my lord, to thy dear side My spirit will be purified: Love from all sin my soul will free: My husband is a God to me. So, love, with thee shall I have bliss And share the life that follows this. I heard a Bráhman, dear to fame, This ancient Scripture text proclaim: “The woman whom on earth below Her parents on a man bestow, And lawfully their hands unite With water and each holy rite, She in this world shall be his wife, His also in the after life.” Then tell me, O beloved, why Thou wilt this earnest prayer deny,
- **Translation**: 

---

### Verse 4 (Ramayan 0.464)
- **Original**: 446 The Ramayana Nor take me with thee to the wood, Thine own dear wife so true and good. But if thou wilt not take me there Thus grieving in my wild despair, To fire or water I will fly, Or to the poisoned draught, and die.” So thus to share his exile, she Besought him with each earnest plea, Nor could she yet her lord persuade To take her to the lonely shade. The answer of the strong-armed chief Smote the Videhan's soul with grief, And from her eyes the torrents came bathing the bosom of the dame. Canto XXX. The Triumph Of Love. The daughter of Videha's king, While Ráma strove to soothe the sting Of her deep anguish, thus began Once more in furtherance of her plan: And with her spirit sorely tried By fear and anger, love and pride, With keenly taunting words addressed Her hero of the stately breast: “Why did the king my sire, who reigns O'er fair Videha's wide domains, Hail Ráma son with joy unwise, A woman in a man's disguise? Now falsely would the people say,
- **Translation**: 

---

### Verse 5 (Ramayan 0.465)
- **Original**: Canto XXX. The Triumph Of Love. 447 By idle fancies led astray, That Ráma's own are power and might, As glorious as the Lord of Light. Why sinkest thou in such dismay? What fears upon thy spirit weigh, That thou, O Ráma, fain wouldst flee From her who thinks of naught but thee? To thy dear will am I resigned In heart and body, soul and mind, As Sávitrí gave all to one, Satyaván, Dyumatsena's son.304 Not e'en in fancy can I brook To any guard save thee to look: Let meaner wives their houses shame, To go with thee is all my claim. Like some low actor, deemst thou fit Thy wife to others to commit— Thine own, espoused in maiden youth, Thy wife so long, unblamed for truth? Do thou, my lord, his will obey For whom thou losest royal sway, To whom thou wouldst thy wife confide— Not me, but thee, his wish may guide. Thou must not here thy wife forsake, And to the wood thy journey make, Whether stern penance, grief, and care, Or rule or heaven await thee there. Nor shall fatigue my limbs distress When wandering in the wilderness: Each path which near to thee I tread Shall seem a soft luxurious bed. 304 The story of Sávitrí, told in the Mahábhárat, has been admirably translated by Rückert, and elegantly epitomized by Mrs. Manning inIndia, Ancient and Mediæval. There is a free rendering of the story inIdylls from the Sanskrit.
- **Translation**: 

---

### Verse 6 (Ramayan 0.466)
- **Original**: 448 The Ramayana The reeds, the bushes where I pass, The thorny trees, the tangled grass Shall feel, if only thou be near, Soft to my touch as skins of deer. When the rude wind in fury blows, And scattered dust upon me throws, That dust, beloved lord, to me Shall as the precious sandal be. And what shall be more blest than I, When gazing on the wood I lie In some green glade upon a bed With sacred grass beneath us spread? The root, the leaf, the fruit which thou Shalt give me from the earth or bough, Scanty or plentiful, to eat, Shall taste to me as Amrit sweet. As there I live on flowers and roots And every season's kindly fruits, I will not for my mother grieve, My sire, my home, or all I leave. My presence, love, shall never add One pain to make the heart more sad;[130] I will not cause thee grief or care, Nor be a burden hard to bear. With thee is heaven, where'er the spot; Each place is hell where thou art not. Then go with me, O Ráma; this Is all my hope and all my bliss. If thou wilt leave thy wife who still Entreats thee with undaunted will, This very day shall poison close The life that spurns the rule of foes. How, after, can my soul sustain The bitter life of endless pain,
- **Translation**: 

---

### Verse 7 (Ramayan 0.467)
- **Original**: Canto XXX. The Triumph Of Love. 449 When thy dear face, my lord, I miss? No, death is better far than this. Not for an hour could I endure The deadly grief that knows not cure, Far less a woe I could not shun For ten long years, and three, and one.” While fires of woe consumed her, such Her sad appeal, lamenting much; Then with a wild cry, anguish-wrung, About her husband's neck she clung. Like some she-elephant who bleeds Struck by the hunter's venomed reeds, So in her quivering heart she felt The many wounds his speeches dealt. Then, as the spark from wood is gained,305 Down rolled the tear so long restrained: The crystal moisture, sprung from woe, From her sweet eyes began to flow, As runs the water from a pair Of lotuses divinely fair. And Sítá's face with long dark eyes, Pure as the moon of autumn skies, Faded with weeping, as the buds Of lotuses when sink the floods. Around his wife his arms he strained, Who senseless from her woe remained, And with sweet words, that bade her wake To life again, the hero spake: “I would not with thy woe, my Queen, Buy heaven and all its blissful sheen. Void of all fear am I as He, 305 Fire for sacrificial purposes is produced by the attrition of two pieces of wood.
- **Translation**: 

---

### Verse 8 (Ramayan 0.468)
- **Original**: 450 The Ramayana The self-existent God, can be. I knew not all thy heart till now, Dear lady of the lovely brow, So wished not thee in woods to dwell; Yet there mine arm can guard thee well. Now surely thou, dear love, wast made To dwell with me in green wood shade. And, as a high saint's tender mind Clings to its love for all mankind, So I to thee will ever cling, Sweet daughter of Videha's king. The good, of old, O soft of frame, Honoured this duty's sovereign claim, And I its guidance will not shun, True as light's Queen is to the Sun. I cannot, pride of Janak's line, This journey to the wood decline: My sire's behest, the oath he sware, The claims of truth, all lead me there. One duty, dear the same for aye, Is sire and mother to obey: Should I their orders once transgress My very life were weariness. If glad obedience be denied To father, mother, holy guide, What rites, what service can be done That stern Fate's favour may be won? These three the triple world comprise, O darling of the lovely eyes. Earth has no holy thing like these Whom with all love men seek to please. Not truth, or gift, or bended knee, Not honour, worship, lordly fee, Storms heaven and wins a blessing thence
- **Translation**: 

---

### Verse 9 (Ramayan 0.469)
- **Original**: Canto XXX. The Triumph Of Love. 451 Like sonly love and reverence. Heaven, riches, grain, and varied lore, With sons and many a blessing more, All these are made their own with ease By those their elders' souls who please. The mighty-souled, who ne'er forget, Devoted sons, their filial debt, Win worlds where Gods and minstrels are, And Brahmá's sphere more glorious far. Now as the orders of my sire, Who keeps the way of truth, require, So will I do, for such the way Of duty that endures for aye: To take thee, love, to DaG ak's wild My heart at length is reconciled, For thee such earnest thoughts impel To follow, and with me to dwell. O faultless form from feet to brows, Come with me, as my will allows, And duty there with me pursue, Trembler, whose bright eyes thrill me through. In all thy days, come good come ill, Preserve unchanged such noble will, And thou, dear love, wilt ever be The glory of thy house and me. Now, beauteous-armed, begin the tasks The woodland life of hermits asks. For me the joys of heaven above Have charms no more without thee, love. And now, dear Sítá, be not slow: Food on good mendicants bestow, And for the holy Bráhmans bring Thy treasures and each precious thing. Thy best attire and gems collect,
- **Translation**: 

---

### Verse 10 (Ramayan 0.470)
- **Original**: 452 The Ramayana The jewels which thy beauty decked, And every ornament and toy Prepared for hours of sport and joy: The beds, the cars wherein I ride, Among our followers, next, divide.” She conscious that her lord approved Her going, with great rapture moved,[131] Hastened within, without delay, Prepared to give their wealth away. Canto XXXI. Lakshman's Prayer. When Lakshma G, who had joined them there, Had heard the converse of the pair, His mien was changed, his eyes o'erflowed, His breast no more could bear its load. The son of Raghu, sore distressed, His brother's feet with fervour pressed, While thus to Sítá he complained, And him by lofty vows enchained: “If thou wilt make the woods thy home, Where elephant and roebuck roam, I too this day will take my bow And in the path before thee go. Our way will lie through forest ground Where countless birds and beasts are found, I heed not homes of Gods on high, I heed not life that cannot die, Nor would I wish, with thee away, O'er the three worlds to stretch my sway.”
- **Translation**: 

---

### Verse 11 (Ramayan 0.471)
- **Original**: Canto XXXI. Lakshman's Prayer. 453 Thus LakshmaG spake, with earnest prayer His brother's woodland life to share. As Ráma still his prayer denied With soothing words, again he cried: “When leave at first thou didst accord, Why dost thou stay me now, my lord? Thou art my refuge: O, be kind, Leave me not, dear my lord, behind. Thou canst not, brother, if thou choose That I still live, my wish refuse.” The glorious chief his speech renewed To faithful LakshmaG as he sued, And on the eyes of Ráma gazed Longing to lead, with hands upraised: “Thou art a hero just and dear, Whose steps to virtue's path adhere, Loved as my life till life shall end, My faithful brother and my friend. If to the woods thou take thy way With Sítá and with me to-day, Who for Kau[alyá will provide, And guard the good Sumitrá's side? The lord of earth, of mighty power, Who sends good things in plenteous shower, As Indra pours the grateful rain, A captive lies in passion's chain. The power imperial for her son Has A[vapati's daughter306 won, And she, proud queen, will little heed Her miserable rivals' need. So Bharat, ruler of the land, By Queen Kaikeyí's side will stand, 306 Kaikeyí.
- **Translation**: 

---

### Verse 12 (Ramayan 0.472)
- **Original**: 454 The Ramayana Nor of those two will ever think, While grieving in despair they sink. Now, LakshmaG, as thy love decrees, Or else the monarch's heart to please, Follow this counsel and protect My honoured mother from neglect. So thou, while not to me alone Thy great affection will be shown, To highest duty wilt adhere By serving those thou shouldst revere. Now, son of Raghu, for my sake Obey this one request I make, Or, of her darling son bereft, Kau [alyá has no comfort left.” The faithful LakshmaG, thus addressed In gentle words which love expressed, To him in lore of language learned, His answer, eloquent, returned: “Nay, through thy might each queen will share Attentive Bharat's love and care, Should Bharat, raised as king to sway This noblest realm, his trust betray, Nor for their safety well provide, Seduced by ill-suggesting pride, Doubt not my vengeful hand shall kill The cruel wretch who counsels ill— Kill him and all who lend him aid, And the three worlds in league arrayed. And good Kau[alyá well can fee A thousand champions like to me. A thousand hamlets rich in grain The station of that queen maintain.
- **Translation**: 

---

### Verse 13 (Ramayan 0.473)
- **Original**: Canto XXXI. Lakshman's Prayer. 455 She may, and my dear mother too, Live on the ample revenue. Then let me follow thee: herein: Is naught that may resemble sin. So shall I in my wish succeed, And aid, perhaps, my brother's need. My bow and quiver well supplied With arrows hanging at my side, My hands shall spade and basket bear, And for thy feet the way prepare. I'll bring thee roots and berries sweet. And woodland fare which hermits eat. Thou shall with thy Videhan spouse Recline upon the mountain's brows; Be mine the toil, be mine to keep Watch o'er thee waking or asleep.” Filled by his speech with joy and pride, Ráma to LakshmaG thus replied: “Go then, my brother, bid adieu To all thy friends and retinue. And those two bows of fearful might, Celestial, which, at that famed rite, Lord VaruG gave to Janak, king Of fair Vedeha with thee bring, With heavenly coats of sword-proof mail, Quivers, whose arrows never fail, [132] And golden-hilted swords so keen, The rivals of the sun in sheen. Tended with care these arms are all Preserved in my preceptor's hall. With speed, O LakshmaG, go, produce, And bring them hither for our use.” So on a woodland life intent,
- **Translation**: 

---

### Verse 14 (Ramayan 0.474)
- **Original**: 456 The Ramayana To see his faithful friends he went, And brought the heavenly arms which lay By Ráma's teacher stored away. And Raghu's son to Ráma showed Those wondrous arms which gleamed and glowed, Well kept, adorned with many a wreath Of flowers on case, and hilt, and sheath. The prudent Ráma at the sight Addressed his brother with delight: “Well art thou come, my brother dear, For much I longed to see thee here. For with thine aid, before I go, I would my gold and wealth bestow Upon the Bráhmans sage, who school Their lives by stern devotion's rule. And for all those who ever dwell Within my house and serve me well, Devoted servants, true and good, Will I provide a livelihood. Quick, go and summon to this place The good Va[ishmha's son, Suyajùa, of the Bráhman race The first and holiest one. To all the Bráhmans wise and good Will I due reverence pay, Then to the solitary wood With thee will take my way.” Canto XXXII. The Gift Of The Treasures.
- **Translation**: 

---

### Verse 15 (Ramayan 0.475)
- **Original**: Canto XXXII. The Gift Of The Treasures. 457 That speech so noble which conveyed His friendly wish, the chief obeyed, With steps made swift by anxious thought The wise Suyajùa's home he sought. Him in the hall of Fire307 he found, And bent before him to the ground: “O friend, to Ráma's house return, Who now performs a task most stern.” He, when his noonday rites were done, Went forth with fair Sumitrá's son, And came to Ráma's bright abode Rich in the love which Lakshmí showed. The son of Raghu, with his dame, With joined hands met him as he came, Showing to him who Scripture knew The worship that is Agni's due. With armlets, bracelets, collars, rings, With costly pearls on golden strings, With many a gem for neck and limb The son of Raghu honoured him. Then Ráma, at his wife's request, The wise Suyajùa thus addressed: “Accept a necklace too to deck With golden strings thy spouse's neck. And Sítá here, my friend, were glad A girdle to her gift to add. And many a bracelet wrought with care, And many an armlet rich and rare, My wife to thine is fain to give, Departing in the wood to live. A bed by skilful workmen made, With gold and various gems inlaid— 307 The chapel where the sacred fire used in worship is kept.
- **Translation**: 

---

### Verse 16 (Ramayan 0.476)
- **Original**: 458 The Ramayana This too, before she goes, would she Present, O saintly friend, to thee. Thine be my elephant, so famed, My uncle's present, Victor named; And let a thousand coins of gold, Great Bráhman, with the gift be told.” Thus Ráma spoke: nor he declined The noble gifts for him designed. On Ráma, LakshmaG, Sítá he Invoked all high felicity. In pleasant words then Ráma gave His best to LakshmaG prompt and brave, As Brahmá speaks for Him to hear Who rules the Gods' celestial sphere: “To the two best of Bráhmans run; Agastya bring, and Ku[ik's son, And precious gifts upon them rain, Like fostering floods upon the grain. O long-armed Prince of Raghu's line, Delight them with a thousand kine, And many a fair and costly gem, With gold and silver, give to them. To him, so deep in Scripture, who, To Queen Kau[alyá, ever true, Serves her with blessing and respect, Chief of the Taittiríya sect308— To him, with women-slaves, present A chariot rich with ornament, And costly robes of silk beside, Until the sage be satisfied. On Chitraratha, true and dear, My tuneful bard and charioteer, 308 The students and teachers of the Taittiríya portion of the Yajur Veda.
- **Translation**: 

---

### Verse 17 (Ramayan 0.477)
- **Original**: Canto XXXII. The Gift Of The Treasures. 459 Gems, robes, and plenteous wealth confer— Mine ancient friend and minister. And these who go with staff in hand, Grammarians trained, a numerous band, Who their deep study only prize, Nor think of other exercise, Who toil not, loving dainty fare, Whose praises e'en the good declare— On these be eighty cars bestowed, And each with precious treasures load. [133] A thousand bulls for them suffice, Two hundred elephants of price, And let a thousand kine beside The dainties of each meal provide. The throng who sacred girdles wear, And on Kau[alyá wait with care— A thousand golden coins shall please, Son of Sumitrá, each of these. Let all, dear LakshmaG of the train These special gifts of honour gain: My mother will rejoice to know Her Bráhmans have been cherished so.” Then Raghu's son addressed the crowd Who round him stood and wept aloud, When he to all who thronged the court Had dealt his wealth for their support: “In LakshmaG's house and mine remain, And guard them till I come again.” To all his people sad with grief, In loving words thus spoke their chief, Then bade his treasure-keeper bring Gold, silver, and each precious thing. Then straight the servants went and bore
- **Translation**: 

---

### Verse 18 (Ramayan 0.478)
- **Original**: 460 The Ramayana Back to their chief the wealth in store. Before the people's eyes it shone, A glorious pile to look upon. The prince of men with LakshmaG's aid Parted the treasures there displayed, Gave to the poor, the young, the old, And twice-born men, the gems and gold. A Bráhman, long in evil case, Named Trijam, born of Garga's race, Earned ever toiling in a wood With spade and plough his livelihood. The youthful wife, his babes who bore, Their indigence felt more and more. Thus to the aged man she spake: “Hear this my word: my counsel take. Come, throw thy spade and plough away; To virtuous Ráma go to-day, And somewhat of his kindness pray.” He heard the words she spoke: around His limbs his ragged cloth he wound, And took his journey by the road That led to Ráma's fair abode. To the fifth court he made his way; Nor met the Bráhman check or stay. Brighu, Angiras309 could not be Brighter with saintly light than he. To Ráma's presence on he pressed, And thus the noble chief addressed: “O Ráma, poor and weak am I, And many children round me cry. 309 Two of the divine personages calledPrajápatisand Brahmádikaswho were first created by Brahmá.
- **Translation**: 

---

### Verse 19 (Ramayan 0.479)
- **Original**: Canto XXXII. The Gift Of The Treasures. 461 Scant living in the woods I earn: On me thine eye of pity turn.” And Ráma, bent on sport and jest, The suppliant Bráhman thus addressed: “O aged man, one thousand kine, Yet undistributed, are mine. The cows on thee will I bestow As far as thou thy staff canst throw.” The Bráhman heard. In eager haste He bound his cloth around his waist. Then round his head his staff he whirled, And forth with mightiest effort hurled. Cast from his hand it flew, and sank To earth on Sarjú's farther bank, Where herds of kine in thousands fed Near to the well-stocked bullock shed. And all the cows that wandered o'er The meadow, far as Sarjú's shore, At Ráma's word the herdsmen drove To Trijam's cottage in the grove. He drew the Bráhman to his breast, And thus with calming words addressed: “Now be not angry, Sire. I pray: This jest of mine was meant in play. These thousand kine, but not alone. Their herdsmen too, are all thine own. And wealth beside I give thee: speak, Thine shall be all thy heart can seek.” Thus Ráma spake. And Trijam prayed For means his sacrifice to aid. And Ráma gave much wealth, required To speed his offering as desired.
- **Translation**: 

---

### Verse 20 (Ramayan 0.480)
- **Original**: 462 The Ramayana Canto XXXIII. The People's Lament. Thus Sítá and the princes brave Much wealth to all the Bráhmans gave. Then to the monarch's house the three Went forth the aged king to see. The princes from two servants took Those heavenly arms of glorious look, Adorned with garland and with band By Sítá's beautifying hand. On each high house a mournful throng Had gathered ere they passed along, Who gazed in pure unselfish woe From turret, roof, and portico. So dense the crowd that blocked the ways, The rest, unable there to gaze, Were fain each terrace to ascend, And thence their eyes on Ráma bend. Then as the gathered multitude On foot their well-loved Ráma viewed, No royal shade to screen his head, Such words, disturbed in grief, they said: “O look, our hero, wont to ride Leading a host in perfect pride— Now Lakshma G, sole of all his friends, With Sítá on his steps attends. Though he has known the sweets of power, And poured his gifts in liberal shower, From duty's path he will not swerve,[134] But, still his father's truth preserve. And she whose form so soft and fair Was veiled from spirits of the air, Now walks unsheltered from the day, Seen by the crowds who throng the way.
- **Translation**: 

---



--- End of Ramayan_batch_24.md ---


--- Start of Ramayan_batch_25.md ---

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

### Verse 1 (Ramayan 0.481)
- **Original**: Canto XXXIII. The People's Lament. 463 Ah, for that gently-nurtured form! How will it fade with sun and storm! How will the rain, the cold, the heat Mar fragrant breast and tinted feet! Surely some demon has possessed His sire, and speaks within his breast, Or how could one that is a king Thus send his dear son wandering? It were a deed unkindly done To banish e'en a worthless son: But what, when his pure life has gained The hearts of all, by love enchained? Six sovereign virtues join to grace Ráma the foremost of his race: Tender and kind and pure is he, Docile, religious, passion-free. Hence misery strikes not him alone: In bitterest grief the people moan, Like creatures of the stream, when dry In the great heat the channels lie. The world is mournful with the grief That falls on its beloved chief, As, when the root is hewn away, Tree, fruit, and flower, and bud decay. The soul of duty, bright to see, He is the root of you and me; And all of us, who share his grief, His branches, blossom, fruit, and leaf. Now like the faithful LakshmaG, we Will follow and be true as he; Our wives and kinsmen call with speed, And hasten where our lord shall lead. Yes, we will leave each well-loved spot, The field, the garden, and the cot,
- **Translation**: 

---

### Verse 2 (Ramayan 0.482)
- **Original**: 464 The Ramayana And, sharers of his weal and woe, Behind the pious Ráma go. Our houses, empty of their stores, With ruined courts and broken doors, With all their treasures borne away. And gear that made them bright and gay: O'errun by rats, with dust o'erspread, Shrines, whence the deities have fled, Where not a hand the water pours, Or sweeps the long-neglected floors, No incense loads the evening air, No Bráhmans chant the text and prayer, No fire of sacrifice is bright, No gift is known, no sacred rite; With floors which broken vessels strew, As if our woes had crushed them too— Of these be stern Kaikeyí queen, And rule o'er homes where we have been. The wood where Ráma's feet may roam Shall be our city and our home, And this fair city we forsake, Our flight a wilderness shall make. Each serpent from his hole shall hie, The birds and beasts from mountain fly, Lions and elephants in fear Shall quit the woods when we come near, Yield the broad wilds for us to range, And take our city in exchange. With Ráma will we hence, content If, where he is, our days be spent.” Such were the varied words the crowd Of all conditions spoke aloud. And Ráma heard their speeches, yet
- **Translation**: 

---

### Verse 3 (Ramayan 0.483)
- **Original**: Canto XXXIV. Ráma In The Palace. 465 Changed not his purpose firmly set. His father's palace soon he neared, That like Kailása's hill appeared. Like a wild elephant he strode Right onward to the bright abode. Within the palace court he stepped, Where ordered bands their station kept, And saw Sumantra standing near With down-cast eye and gloomy cheer. Canto XXXIV. Ráma In The Palace. The dark incomparable chief Whose eye was like a lotus leaf, Cried to the mournful charioteer, “Go tell my sire that I am here.” Sumantra, sad and all dismayed, The chieftain's order swift obeyed. Within the palace doors he hied And saw the king, who wept and sighed. Like the great sun when wrapped in shade Like fire by ashes overlaid, Or like a pool with waters dried, So lay the world's great lord and pride, A while the wise Sumantra gazed On him whose senses woe has dazed, Grieving for Ráma. Near he drew With hands upraised in reverence due. With blessing first his king he hailed; Then with a voice that well-nigh failed,
- **Translation**: 

---

### Verse 4 (Ramayan 0.484)
- **Original**: 466 The Ramayana In trembling accents soft and low Addressed the monarch in his woe: “The prince of men, thy Ráma, waits Before thee at the palace gates. His wealth to Bráhmans he has dealt, And all who in his home have dwelt. Admit thy son. His friends have heard His kind farewell and parting word, He longs to see thee first, and then Will seek the wilds, O King of men. He, with each princely virtue's blaze, Shines as the sun engirt by rays.” The truthful King who loved to keep The law profound as Ocean's deep, And stainless as the dark blue sky, Thus to Sumantra made reply:[135] “Go then, Sumantra, go and call My wives and ladies one and all. Drawn round me shall they fill the place When I behold my Ráma's face.” Quick to the inner rooms he sped, And thus to all the women said, “Come, at the summons of the king: Come all, and make no tarrying.”
- **Translation**: 

---

### Verse 5 (Ramayan 0.485)
- **Original**: Canto XXXIV. Ráma In The Palace. 467 Their husband's word, by him conveyed, Soon as they heard, the dames obeyed, And following his guidance all Came thronging to the regal hall. In number half seven hundred, they, All lovely dames, in long array, With their bright eyes for weeping red, To stand round Queen Kau[alyá, sped. They gathered, and the monarch viewed One moment all the multitude, Then to Sumantra spoke and said: “Now let my son be hither led.” Sumantra went. Then Ráma came, And Lakshma G, and the Maithil dame, And, as he led them on, their guide Straight to the monarch's presence hied. When yet far off the father saw His son with raised palms toward him draw, Girt by his ladies, sick with woes, Swift from his royal seat he rose. With all his strength the aged man To meet his darling Ráma ran, But trembling, wild with dark despair, Fell on the ground and fainted there. And Lakshma G, wont in cars to ride, And Ráma, threw them by the side Of the poor miserable king, Half lifeless with his sorrow's sting. Throughout the spacious hall up went A thousand women's wild lament: “Ah Ráma! ” thus they wailed and wept, And anklets tinkled as they stepped Around his body, weeping, threw
- **Translation**: 

---

### Verse 6 (Ramayan 0.486)
- **Original**: 468 The Ramayana Their loving arms the brothers two, And then, with Sítá's gentle aid, The king upon a couch was laid. At length to earth's imperial lord, When life and knowledge were restored, Though seas of woe went o'er his head, With suppliant hand, thus Ráma said: “Lord of us all, great King, thou art: Bid me farewell before we part, To DaG ak wood this day I go: One blessing and one look bestow. Let LakshmaG my companion be, And Sítá also follow me. With truthful pleas I sought to bend Their purpose; but no ear they lend. Now cast this sorrow from thy heart, And let us all, great King, depart. As Brahmá sends his children, so Let LakshmaG, me, and Sítá go.” He stood unmoved, and watched intent Until the king should grant consent. Upon his son his eyes he cast, And thus the monarch spake at last: “O Ráma, by her arts enslaved, I gave the boons Kaikeyí craved, Unfit to reign, by her misled: Be ruler in thy father's stead.”
- **Translation**: 

---

### Verse 7 (Ramayan 0.487)
- **Original**: Canto XXXIV. Ráma In The Palace. 469 Thus by the lord of men addressed, Ráma, of virtue's friends the best, In lore of language duly learned, His answer, reverent, thus returned: “A thousand years, O King, remain O'er this our city still to reign. I in the woods my life will lead: The lust of rule no more I heed. Nine years and five I there will spend, And when the portioned days shall end, Will come, my vows and exile o'er, And clasp thy feet, my King, once more.” A captive in the snare of truth, Weeping, distressed with woe and ruth, Thus spake the monarch, while the queen Kaikeyí urged him on unseen: “Go then, O Ráma, and begin Thy course unvext by fear and sin: Go, my beloved son, and earn Success, and joy, and safe return. So fast the bonds of duty bind. O Raghu's son, thy truthful mind, That naught can turn thee back, or guide Thy will so strongly fortified. But O, a little longer stay, Nor turn thy steps this night away, That I one little day-— alas! One only— -with my son may pass. Me and thy mother do not slight, But stay, my son, with me to-night; With every dainty please thy taste, And seek to-morrow morn the waste. Hard is thy task, O Raghu's son,
- **Translation**: 

---

### Verse 8 (Ramayan 0.488)
- **Original**: 470 The Ramayana Dire is the toil thou wilt not shun, Far to the lonely wood to flee, And leave thy friends for love of me. I swear it by my truth, believe, For thee, my son, I deeply grieve, Misguided by the traitress dame With hidden guile like smouldering flame. Now, by her wicked counsel stirred, Thou fain wouldst keep my plighted word. No marvel that my eldest born Would hold me true when I have sworn.” Then Ráma having calmly heard His wretched father speak each word, With LakshmaG standing by his side Thus, humbly, to the King replied: “If dainties now my taste regale, To-morrow must those dainties fail. This day departure I prefer To all that wealth can minister. O'er this fair land, no longer mine, Which I, with all her realms, resign,[136] Her multitudes of men, her grain, Her stores of wealth, let Bharat reign. And let the promised boon which thou Wast pleased to grant the queen ere now, Be hers in full. Be true, O King, Kind giver of each precious thing. Thy spoken word I still will heed, Obeying all thy lips decreed: And fourteen years in woods will dwell With those who live in glade and dell. No hopes of power my heart can touch, No selfish joys attract so much
- **Translation**: 

---

### Verse 9 (Ramayan 0.489)
- **Original**: Canto XXXIV. Ráma In The Palace. 471 As son of Raghu, to fulfil With heart and soul my father's will. Dismiss, dismiss thy needless woe, Nor let those drowning torrents flow: The Lord of Rivers in his pride Keeps to the banks that bar his tide. Here in thy presence I declare; By thy good deeds, thy truth, I swear; Nor lordship, joy, nor lands I prize; Life, heaven, all blessings I despise. I wish to see thee still remain Most true, O King, and free from stain. It must not, Sire, it must not be: I cannot rest one hour with thee. Then bring this sorrow to an end, For naught my settled will can bend. I gave a pledge that binds me too, And to that pledge I still am true. Kaikeyí bade me speed away: She prayed me, and I answered yea. Pine not for me, and weep no more; The wood for us has joy in store, Filled with the wild deer's peaceful herds And voices of a thousand birds. A father is the God of each, Yea, e'en of Gods, so Scriptures teach: And I will keep my sire's decree, For as a God I honour thee. O best of men, the time is nigh, The fourteen years will soon pass by And to thine eyes thy son restore: Be comforted, and weep no more. Thou with thy firmness shouldst support These weeping crowds who throng the court;
- **Translation**: 

---

### Verse 10 (Ramayan 0.490)
- **Original**: 472 The Ramayana Then why, O chief of high renown, So troubled, and thy soul cast down?” Canto XXXV. Kaikeyí Reproached. Wild with the rage he could not calm, Sumantra, grinding palm on palm, His head in quick impatience shook, And sighed with woe he could not brook. He gnashed his teeth, his eyes were red, From his changed face the colour fled. In rage and grief that knew no law, The temper of the king he saw. With his word-arrows swift and keen He shook the bosom of the queen. With scorn, as though its lightning stroke Would blast her body, thus he spoke: “Thou, who, of no dread sin afraid, Hast Da[aratha's self betrayed, Lord of the world, whose might sustains Each thing that moves or fixed remains, What direr crime is left thee now? Death to thy lord and house art thou, Whose cruel deeds the king distress, Mahendra's peer in mightiness, Firm as the mountain's rooted steep, Enduring as the Ocean's deep. Despise not Da[aratha, he Is a kind lord and friend to thee. A loving wife in worth outruns The mother of ten million sons.
- **Translation**: 

---

### Verse 11 (Ramayan 0.491)
- **Original**: Canto XXXV. Kaikeyí Reproached. 473 Kings, when their sires have passed away, Succeed by birthright to the sway. Ikshváku's son still rules the state, Yet thou this rule wouldst violate. Yea, let thy son, Kaikeyí, reign, Let Bharat rule his sire's domain. Thy will, O Queen, shall none oppose: We all will go where Ráma goes. No Bráhman, scorning thee, will rest Within the realm thou governest, But all will fly indignant hence: So great thy trespass and offence. I marvel, when thy crime I see, Earth yawns not quick to swallow thee; And that the Bráhman saints prepare No burning scourge thy soul to scare, With cries of shame to smite thee, bent Upon our Ráma's banishment. The Mango tree with axes fell, And tend instead the Neem tree well, Still watered with all care the tree Will never sweet and pleasant be. Thy mother's faults to thee descend, And with thy borrowed nature blend. True is the ancient saw: the Neem Can ne'er distil a honeyed stream. Taught by the tale of long ago Thy mother's hateful sin we know. A bounteous saint, as all have heard, A boon upon thy sire conferred, And all the eloquence revealed That fills the wood, the flood, the field. No creature walked, or swam, or flew, But he its varied language knew.
- **Translation**: 

---

### Verse 12 (Ramayan 0.492)
- **Original**: 474 The Ramayana One morn upon his couch he heard The chattering of a gorgeous bird. And as he marked its close intent He laughed aloud in merriment. Thy mother furious with her lord, And fain to perish by the cord, Said to her husband:“I would know, O Monarch, why thou laughest so.”[137] The king in answer spake again: “If I this laughter should explain, This very hour would be my last, For death, be sure would follow fast.” Again thy mother, flushed with ire, To Kekaya spake, thy royal sire: “Tell me the cause; then live or die: I will not brook thy laugh, not I.” Thus by his darling wife addressed, The king whose might all earth confessed, To that kind saint his story told Who gave the wondrous gift of old. He listened to the king's complaint, And thus in answer spoke the saint: “King, let her quit thy home or die, But never with her prayer comply.” The saint's reply his trouble stilled, And all his heart with pleasure filled. Thy mother from his home he sent, And days like Lord Kuvera's spent. So thou wouldst force the king, misled By thee, in evil paths to tread, And bent on evil wouldst begin, Through folly, this career of sin. Most true, methinks, in thee is shown The ancient saw so widely known:
- **Translation**: 

---

### Verse 13 (Ramayan 0.493)
- **Original**: Canto XXXV. Kaikeyí Reproached. 475 The sons their fathers' worth declare And girls their mothers' nature share. So be not thou. For pity's sake Accept the word the monarch spake. Thy husband's will, O Queen, obey, And be the people's hope and stay, O, do not, urged by folly, draw The king to tread on duty's law. The lord who all the world sustains, Bright as the God o'er Gods who reigns. Our glorious king, by sin unstained, Will never grant what fraud obtained; No shade of fault in him is seen: Let Ráma be anointed, Queen. Remember, Queen, undying shame Will through the world pursue thy name, If Ráma leave the king his sire, And, banished, to the wood retire. Come, from thy breast this fever fling: Of his own realm be Ráma king. None in this city e'er can dwell To tend and love thee half so well. When Ráma sits in royal place, True to the custom of his race Our monarch of the mighty bow A hermit to the woods will go.”310 310 It was the custom of the kings of the solar dynasty to resign in their extreme old age the kingdom to the heir, and spend the remainder of their days in holy meditation in the forest: “For such through ages in their life's decline Is the good custom of Ikshváku's line.” RaghuraE[a.
- **Translation**: 

---

### Verse 14 (Ramayan 0.494)
- **Original**: 476 The Ramayana Sumantra thus, palm joined to palm, Poured forth his words of bane and balm, With keen reproach, with pleading kind, Striving to move Kaikeyí's mind. In vain he prayed, in vain reproved, She heard unsoftened and unmoved. Nor could the eyes that watched her view One yielding look, one change of hue. Canto XXXVI. Siddhárth's Speech. Ikshváku's son with anguish torn For the great oath his lips had sworn, With tears and sighs of sharpest pain Thus to Sumantra spake again: “Prepare thou quick a perfect force, Cars, elephants, and foot, and horse, To follow Raghu's scion hence Equipped with all magnificence. Let traders with the wealth they sell, And those who charming stories tell, And dancing-women fair of face, The prince's ample chariots grace. On all the train who throng his courts, And those who share his manly sports, Great gifts of precious wealth bestow, And bid them with their master go. Let noble arms, and many a wain, And townsmen swell the prince's train; And hunters best for woodland skill Their places in the concourse fill.
- **Translation**: 

---

### Verse 15 (Ramayan 0.495)
- **Original**: Canto XXXVI. Siddhárth's Speech. 477 While elephants and deer he slays, Drinking wood honey as he strays, And looks on streams each fairer yet, His kingdom he may chance forget. Let all my gold and wealth of corn With Ráma to the wilds be borne; For it will soothe the exile's lot To sacrifice in each pure spot, Deal ample largess forth, and meet Each hermit in his calm retreat. The wealth shall Ráma with him bear, Ayodhyá shall be Bharat's share.” As thus Kakutstha's offspring spoke, Fear in Kaikeyí's breast awoke. The freshness of her face was dried, Her trembling tongue was terror-tied. Alarmed and sad, with bloodless cheek, She turned to him and scarce could speak: “Nay, Sire, but Bharat shall not gain An empty realm where none remain. My Bharat shall not rule a waste Reft of all sweets to charm the taste— The wine-cup's dregs, all dull and dead, Whence the light foam and life are fled.” Thus in her rage the long-eyed dame Spoke her dire speech untouched by shame. [138] Then, answering, Da[aratha spoke: “Why, having bowed me to the yoke, Dost thou, must cruel, spur and goad Me who am struggling with the load? Why didst thou not oppose at first This hope, vile Queen, so fondly nursed?”
- **Translation**: 

---

### Verse 16 (Ramayan 0.496)
- **Original**: 478 The Ramayana Scarce could the monarch's angry speech The ears of the fair lady reach, When thus, with double wrath inflamed, Kaikeyí to the king exclaimed: “Sagar, from whom thy line is traced, Drove forth his eldest son disgraced, Called Asamanj, whose fate we know: Thus should thy son to exile go.” “Fie on thee, dame!” the monarch said; Each of her people bent his head, And stood in shame and sorrow mute: She marked not, bold and resolute. Then great Siddhárth, inflamed with rage, The good old councillor and sage On whose wise rede the king relied, To Queen Kaikeyí thus replied: “But Asamanj the cruel laid His hands on infants as they played, Cast them to Sarjú's flood, and smiled For pleasure when he drowned a child.”311 The people saw, and, furious, sped Straight the the king his sire and said: “Choose us, O glory of the throne, Choose us, or Asamanj alone.” 311 See Book I, Canto XXXIX. An Indian prince in more modern times appears to have diverted himself in a similar way. It is still reported in Belgaum that Appay Deasy was wont to amuse himself “by making several young and beautiful women stand side by side on a narrow balcony, without a parapet, overhanging the deep reservoir at the new palace in Nipani. He used then to pass along the line of trembling creatures, and suddenly thrusting one of them headlong into the water below, he used to watch her drowning, and derive pleasure from her dying agonies.”— History of the Belgaum District. By H. J. Stokes, M. S. C.
- **Translation**: 

---

### Verse 17 (Ramayan 0.497)
- **Original**: Canto XXXVI. Siddhárth's Speech. 479 “Whence comes this dread?” the monarch cried; And all the people thus replied: “In folly, King, he loves to lay Fierce hands upon our babes at play, Casts them to Sarjú's flood and joys To murder our bewildered boys.” With heedful ear the king of men Heard each complaining citizen. To please their troubled minds he strove, And from the state his son he drove. With wife and gear upon a car He placed him quick, and sent him far. And thus he gave commandment,“He Shall all his days an exile be.” With basket and with plough he strayed O'er mountain heights, through pathless shade, Roaming all lands a weary time, An outcast wretch defiled with crime. Sagar, the righteous path who held, His wicked offspring thus expelled. But what has Ráma done to blame? Why should his sentence be the same? No sin his stainless name can dim; We see no fault at all in him. Pure as the moon, no darkening blot On his sweet life has left a spot. If thou canst see one fault, e'en one, To dim the fame of Raghu's son, That fault this hour, O lady, show, And Ráma to the wood shall go. To drive the guiltless to the wild, Truth's constant lover, undefiled, Would, by defiance of the right, The glory e'en of Indra blight.
- **Translation**: 

---

### Verse 18 (Ramayan 0.498)
- **Original**: 480 The Ramayana Then cease, O lady, and dismiss Thy hope to ruin Ráma's bliss, Or all thy gain, O fair of face, Will be men's hatred, and disgrace.” Canto XXXVII. The Coats Of Bark. Thus spake the virtuous sage: and then Ráma addressed the king of men. In laws of meek behaviour bred, Thus to his sire he meekly said: “King, I renounce all earthly care, And live in woods on woodland fare. What, dead to joys, have I to do With lordly train and retinue! Who gives his elephant and yet Upon the girths his heart will set? How can a cord attract his eyes Who gives away the nobler prize? Best of the good, with me be led No host, my King with banners spread. All wealth, all lordship I resign: The hermit's dress alone be mine. Before I go, have here conveyed A little basket and a spade. With these alone I go, content, For fourteen years of banishment.”
- **Translation**: 

---

### Verse 19 (Ramayan 0.499)
- **Original**: Canto XXXVII. The Coats Of Bark. 481 With her own hands Kaikeyí took The hermit coats of bark, and,“Look,” She cried with bold unblushing brow Before the concourse,“Dress thee now.” That lion leader of the brave Took from her hand the dress she gave, Cast his fine raiment on the ground, [139] And round his waist the vesture bound. Then quick the hero LakshmaG too His garment from his shoulders threw, And, in the presence of his sire, Indued the ascetic's rough attire. But Sítá, in her silks arrayed, Threw glances, trembling and afraid, On the bark coat she had to wear, Like a shy doe that eyes the snare. Ashamed and weeping for distress From the queen's hand she took the dress. The fair one, by her husband's side Who matched heaven's minstrel monarch,312 cried: “How bind they on their woodland dress, Those hermits of the wilderness?” There stood the pride of Janak's race Perplexed, with sad appealing face. One coat the lady's fingers grasped, One round her neck she feebly clasped, But failed again, again, confused By the wild garb she ne'er had used. Then quickly hastening Ráma, pride Of all who cherish virtue, tied The rough bark mantle on her, o'er The silken raiment that she wore. 312 Chitraratha, King of the celestial choristers.
- **Translation**: 

---

### Verse 20 (Ramayan 0.500)
- **Original**: 482 The Ramayana Then the sad women when they saw Ráma the choice bark round her draw, Rained water from each tender eye, And cried aloud with bitter cry: “O, not on her, beloved, not On Sítá falls thy mournful lot. If, faithful to thy father's will, Thou must go forth, leave Sítá still. Let Sítá still remaining here Our hearts with her loved presence cheer. With LakshmaG by thy side to aid Seek thou, dear son, the lonely shade. Unmeet, one good and fair as she Should dwell in woods a devotee. Let not our prayers be prayed in vain: Let beauteous Sítá yet remain; For by thy love of duty tied Thou wilt not here thyself abide.” Then the king's venerable guide Va [ishmha, when he saw each coat Enclose the lady's waist and throat, Her zeal with gentle words repressed, And Queen Kaikeyí thus addressed: “O evil-hearted sinner, shame Of royal Kekaya's race and name; Who matchless in thy sin couldst cheat Thy lord the king with vile deceit; Lost to all sense of duty, know Sítá to exile shall not go. Sítá shall guard, as 'twere her own, The precious trust of Ráma's throne. Those joined by wedlock's sweet control Have but one self and common soul.
- **Translation**: 

---



--- End of Ramayan_batch_25.md ---


--- Start of Ramayan_batch_26.md ---

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

### Verse 1 (Ramayan 0.501)
- **Original**: Canto XXXVII. The Coats Of Bark. 483 Thus Sítá shall our empress be, For Ráma's self and soul is she. Or if she still to Ráma cleave And for the woods the kingdom leave: If naught her loving heart deter, We and this town will follow her. The warders of the queen shall take Their wives and go for Ráma's sake, The nation with its stores of grain, The city's wealth shall swell his train. Bharat,Zatrughna both will wear Bark mantles, and his lodging share, Still with their elder brother dwell In the wild wood, and serve him well. Rest here alone, and rule thy state Unpeopled, barren, desolate; Be empress of the land and trees, Thou sinner whom our sorrows please. The land which Ráma reigns not o'er Shall bear the kingdom's name no more: The woods which Ráma wanders through Shall be our home and kingdom too. Bharat, be sure, will never deign O'er realms his father yields, to reign. Nay, if the king's true son he be, He will not, sonlike, dwell with thee. Nay, shouldst thou from the earth arise, And send thy message from the skies, To his forefathers' custom true No erring course would he pursue. So hast thou, by thy grievous fault, Offended him thou wouldst exalt. In all the world none draws his breath Who loves not Ráma, true to death.
- **Translation**: 

---

### Verse 2 (Ramayan 0.502)
- **Original**: 484 The Ramayana This day, O Queen, shalt thou behold Birds, deer, and beasts from lea and fold Turn to the woods in Ráma's train. And naught save longing trees remain.” Canto XXXVIII. Care For Kausalyá Then when the people wroth and sad Saw Sítá in bark vesture clad, Though wedded, like some widowed thing, They cried out,“Shame upon thee, King!” Grieved by their cry and angry look The lord of earth at once forsook All hope in life that still remained, In duty, self, and fame unstained. Ikshváku's son with burning sighs On Queen Kaikeyí bent his eyes, And said:“But Sítá must not flee In garments of a devotee. My holy guide has spoken truth: Unfit is she in tender youth,[140] So gently nurtured, soft and fair, The hardships of the wood to share. How has she sinned, devout and true, The noblest monarch's child, That she should garb of bark indue And journey to the wild? That she should spend her youthful days Amid a hermit band, Like some poor mendicant who strays Sore troubled, through the land?
- **Translation**: 

---

### Verse 3 (Ramayan 0.503)
- **Original**: Canto XXXVIII. Care For Kausalyá 485 Ah, let the child of Janak throw Her dress of bark aside, And let the royal lady go With royal wealth supplied. Not such the pledge I gave before, Unfit to linger here: The oath, which I the sinner swore Is kept, and leaves her clear. Won from her childlike love this too My instant death would be, As blossoms on the old bamboo Destroy the parent tree.313 If aught amiss by Ráma done Offend thee, O thou wicked one, What least transgression canst thou find In her, thou worst of womankind? What shade of fault in her appears, Whose full soft eye is like the deer's? What canst thou blame in Janak's child, So gentle, modest, true, and mild? Is not one crime complete, that sent My Ráma forth to banishment? And wilt thou other sins commit, Thou wicked one, to double it? This is the pledge and oath I swore, What thou besoughtest, and no more, Of Ráma — for I heard thee, dame— When he for consecration came. Now with this limit not content, In hell should be thy punishment, Who fain the Maithil bride wouldst press To clothe her limbs with hermit dress.” 313 It is said that the bamboo dies after flowering.
- **Translation**: 

---

### Verse 4 (Ramayan 0.504)
- **Original**: 486 The Ramayana Thus spake the father in his woe; And Ráma, still prepared to go, To him who sat with drooping head Spake in return these words and said: “Just King, here stands my mother dear, Kau [alyá, one whom all revere. Submissive, gentle, old is she, And keeps her lips from blame of thee, For her, kind lord, of me bereft A sea of whelming woe is left. O, show her in her new distress Still fonder love and tenderness. Well honoured by thine honoured hand Her grief for me let her withstand, Who wrapt in constant thought of me In me would live a devotee. Peer of Mahendra, O, to her be kind, And treat I pray, my gentle mother so, That, when I dwell afar, her life resigned, She may not pass to Yáma's realm for woe.” Canto XXXIX. Counsel To Sítá. Scarce had the sire, with each dear queen, Heard Ráma's pleading voice, and seen His darling in his hermit dress Ere failed his senses for distress. Convulsed with woe, his soul that shook, On Raghu's son he could not look; Or if he looked with failing eye
- **Translation**: 

---

### Verse 5 (Ramayan 0.505)
- **Original**: Canto XXXIX. Counsel To Sítá. 487 He could not to the chief reply. By pangs of bitter grief assailed, The long-armed monarch wept and wailed, Half dead a while and sore distraught, While Ráma filled his every thought. “This hand of mine in days ere now Has reft her young from many a cow, Or living things has idly slain: Hence comes, I ween, this hour of pain. Not till the hour is come to die Can from its shell the spirit fly. Death comes not, and Kaikeyí still Torments the wretch she cannot kill, Who sees his son before him quit The fine soft robes his rank that fit, And, glorious as the burning fire, In hermit garb his limbs attire. Now all the people grieve and groan Through Queen Kaikeyí's deed alone, Who, having dared this deed of sin, Strives for herself the gain to win.” He spoke. With tears his eyes grew dim, His senses all deserted him. He cried, O Ráma, once, then weak And fainting could no further speak. Unconscious there he lay: at length Regathering his sense and strength, While his full eyes their torrents shed, To wise Sumantra thus he said: “Yoke the light car, and hither lead Fleet coursers of the noblest breed, And drive this heir of lofty fate Beyond the limit of the state.
- **Translation**: 

---

### Verse 6 (Ramayan 0.506)
- **Original**: 488 The Ramayana This seems the fruit that virtues bear, The meed of worth which texts declare— The sending of the brave and good By sire and mother to the wood.'” He heard the monarch, and obeyed, With ready feet that ne'er delayed, And brought before the palace gate The horses and the car of state. Then to the monarch's son he sped, And raising hands of reverence said[141] That the light car which gold made fair, With best of steeds, was standing there. King Da[aratha called in haste The lord o'er all his treasures placed. And spoke, well skilled in place and time, His will to him devoid of crime: “Count all the years she has to live Afar in forest wilds, and give To Sítá robes and gems of price As for the time may well suffice.” Quick to the treasure-room he went, Charged by that king most excellent, Brought the rich stores, and gave them all To Sítá in the monarch's hall. The Maithil dame of high descent Received each robe and ornament, And tricked those limbs, whose lines foretold High destiny, with gems and gold. So well adorned, so fair to view, A glory through the hall she threw: So, when the Lord of Light upsprings, His radiance o'er the sky he flings. Then Queen Kau[alyá spake at last,
- **Translation**: 

---

### Verse 7 (Ramayan 0.507)
- **Original**: Canto XXXIX. Counsel To Sítá. 489 With loving arms about her cast, Pressed lingering kisses on her head, And to the high-souled lady said: “Ah, in this faithless world below When dark misfortune comes and woe, Wives, loved and cherished every day, Neglect their lords and disobey. Yes, woman's nature still is this:— After long days of calm and bliss When some light grief her spirit tries, She changes all her love, or flies. Young wives are thankless, false in soul, With roving hearts that spurn control. Brooding on sin and quickly changed, In one short hour their love estranged. Not glorious deed or lineage fair, Not knowledge, gift, or tender care In chains of lasting love can bind A woman's light inconstant mind. But those good dames who still maintain What right, truth, Scripture, rule ordain— No holy thing in their pure eyes With one beloved husband vies. Nor let thy lord my son, condemned To exile, be by thee contemned, For be he poor or wealthy, he Is as a God, dear child, to thee.” When Sítá heard Kau[alyá's speech Her duty and her gain to teach, She joined her palms with reverent grace And gave her answer face to face: “All will I do, forgetting naught, Which thou, O honoured Queen, hast taught.
- **Translation**: 

---

### Verse 8 (Ramayan 0.508)
- **Original**: 490 The Ramayana I know, have heard, and deep have stored The rules of duty to my lord. Not me, good Queen, shouldst thou include Among the faithless multitude. Its own sweet light the moon shall leave Ere I to duty cease to cleave. The stringless lute gives forth no strain, The wheelless car is urged in vain; No joy a lordless dame, although Blest with a hundred sons, can know. From father, brother, and from son A measured share of joy is won: Who would not honour, love, and bless Her lord, whose gifts are measureless? Thus trained to think, I hold in awe Scripture's command and duty's law. Him can I hold in slight esteem? Her lord is woman's God, I deem.” Kau [alyá heard the lady's speech, Nor failed those words her heart to reach. Then, pure in mind, she gave to flow The tear that sprang of joy and woe. Then duteous Ráma forward came And stood before the honoured dame, And joining reverent hands addressed The queen in rank above the rest: “O mother, from these tears refrain; Look on my sire and still thy pain. To thee my days afar shall fly As if sweet slumber closed thine eye, And fourteen years of exile seem To thee, dear mother, like a dream. On me returning safe and well, Girt by my friends, thine eyes shall dwell.”
- **Translation**: 

---

### Verse 9 (Ramayan 0.509)
- **Original**: Canto XL. Ráma's Departure. 491 Thus for their deep affection's sake The hero to his mother spake, Then to the half seven hundred too, Wives of his sire, paid reverence due. Thus Da[aratha's son addressed That crowd of matrons sore distressed: “If from these lips, while here I dwelt, One heedless taunt you e'er have felt, Forgive me, pray. And now adieu, I bid good-bye to all of you.” Then straight, like curlews' cries, upwent The voices of their wild lament, While, as he bade farewell, the crowd Of royal women wept aloud, And through the ample hall's extent. Where erst the sound of tabour, blent With drum and shrill-toned instrument, In joyous concert rose, Now rang the sound of wailing high, The lamentation and the cry, The shriek, the choking sob, the sigh That told the ladies' woes. Canto XL. Ráma's Departure. Then Ráma, Sítá, LakshmaG bent At the king's feet, and sadly went [142]
- **Translation**: 

---

### Verse 10 (Ramayan 0.510)
- **Original**: 492 The Ramayana Round him with slow steps reverent. When Ráma of the duteous heart Had gained his sire's consent to part, With Sítá by his side he paid Due reverence to the queen dismayed. And Lakshma G, with affection meet, Bowed down and clasped his mother's feet. Sumitrá viewed him as he pressed Her feet, and thus her son addressed: “Neglect not Ráma wandering there, But tend him with thy faithful care. In hours of wealth, in time of woe, Him, sinless son, thy refuge know. From this good law the just ne'er swerve, That younger sons the eldest serve, And to this righteous rule incline All children of thine ancient line— Freely to give, reward each rite, Nor spare their bodies in the fight. Let Ráma Da[aratha be, Look upon Sítá as on me, And let the cot wherein you dwell Be thine Ayodhyá. Fare thee well.” Her blessing thus Sumitrá gave To him whose soul to Ráma clave, Exclaiming, when her speech was done, “Go forth, O LakshmaG, go, my son. Go forth, my son to win success, High victory and happiness. Go forth thy foemen to destroy, And turn again at last with joy.” As Mátali his charioteer Speaks for the Lord of Gods to hear,
- **Translation**: 

---

### Verse 11 (Ramayan 0.511)
- **Original**: Canto XL. Ráma's Departure. 493 Sumantra, palm to palm applied, In reverence trained, to Ráma cried: “O famous Prince, my car ascend,— May blessings on thy course attend,— And swiftly shall my horses flee And place thee where thou biddest me. The fourteen years thou hast to stay Far in the wilds, begin to-day; For Oueen Kaikeyí cries, Away.” Then Sítá, best of womankind, Ascended, with a tranquil mind, Soon as her toilet task was done, That chariot brilliant as the sun. Ráma and LakshmaG true and bold Sprang on the car adorned with gold. The king those years had counted o'er, And given Sítá robes and store Of precious ornaments to wear When following her husband there. The brothers in the car found place For nets and weapons of the chase, There warlike arms and mail they laid, A leathern basket and a spade. Soon as Sumantra saw the three Were seated in the chariot, he Urged on each horse of noble breed, Who matched the rushing wind in speed. As thus the son of Raghu went Forth for his dreary banishment, Chill numbing grief the town assailed, All strength grew weak, all spirit failed, Ayodhyá through her wide extent Was filled with tumult and lament:
- **Translation**: 

---

### Verse 12 (Ramayan 0.512)
- **Original**: 494 The Ramayana Steeds neighed and shook the bells they bore, Each elephant returned a roar. Then all the city, young and old, Wild with their sorrow uncontrolled, Rushed to the car, as, from the sun The panting herds to water run. Before the car, behind, they clung, And there as eagerly they hung, With torrents streaming from their eyes, Called loudly with repeated cries: “Listen, Sumantra: draw thy rein; Drive gently, and thy steeds restrain. Once more on Ráma will we gaze, Now to be lost for many days. The queen his mother has, be sure, A heart of iron, to endure To see her godlike Ráma go, Nor feel it shattered by the blow. Sítá, well done! Videha's pride, Still like his shadow by his side; Rejoicing in thy duty still As sunlight cleaves to Meru's hill. Thou, LakshmaG, too, hast well deserved, Who from thy duty hast not swerved, Tending the peer of Gods above, Whose lips speak naught but words of love. Thy firm resolve is nobly great, And high success on thee shall wait. Yea, thou shalt win a priceless meed— Thy path with him to heaven shall lead.” As thus they spake, they could not hold The tears that down their faces rolled, While still they followed for a space Their darling of Ikshváku's race.
- **Translation**: 

---

### Verse 13 (Ramayan 0.513)
- **Original**: Canto XL. Ráma's Departure. 495 There stood surrounded by a ring Of mournful wives the mournful king; For,“I will see once more,” he cried, “Mine own dear son,” and forth he hied. As he came near, there rose the sound Of weeping, as the dames stood round. So the she-elephants complain When their great lord and guide is slain. Kakutstha's son, the king of men, The glorious sire, looked troubled then, As the full moon is when dismayed By dark eclipse's threatening shade. Then Da[aratha's son, designed For highest fate of lofty mind, Urged to more speed the charioteer, “Away, away! why linger here? Urge on thy horses,” Rama cried, And “Stay, O stay,” the people sighed. Sumantra, urged to speed away, The townsmen's call must disobey, Forth as the long-armed hero went, [143] The dust his chariot wheels up sent Was laid by streams that ever flowed From their sad eyes who filled the road. Then, sprung of woe, from eyes of all The women drops began to fall, As from each lotus on the lake The darting fish the water shake. When he, the king of high renown, Saw that one thought held all the town, Like some tall tree he fell and lay, Whose root the axe has hewn away. Then straight a mighty cry from those Who followed Ráma's car arose,
- **Translation**: 

---

### Verse 14 (Ramayan 0.514)
- **Original**: 496 The Ramayana Who saw their monarch fainting there Beneath that grief too great to bear. Then “Ráma, Ráma!” with the cry Of “Ah, his mother!” sounded high, As all the people wept aloud Around the ladies' sorrowing crowd. When Ráma backward turned his eye, And saw the king his father lie With troubled sense and failing limb, And the sad queen, who followed him, Like some young creature in the net, That will not, in its misery, let Its wild eyes on its mother rest, So, by the bonds of duty pressed, His mother's look he could not meet. He saw them with their weary feet, Who, used to bliss, in cars should ride, Who ne'er by sorrow should be tried, And, as one mournful look he cast, “Drive on,” he cried,“Sumantra, fast.” As when the driver's torturing hook Goads on an elephant, the look Of sire and mother in despair Was more than Ráma's heart could bear. As mother kine to stalls return Which hold the calves for whom they yearn, So to the car she tried to run As a cow seeks her little one. Once and again the hero's eyes Looked on his mother, as with cries Of woe she called and gestures wild, “O Sítá, LakshmaG, O my child!” “Stay,” cried the king,“thy chariot stay:” “On, on,” cried Ráma,“speed away.”
- **Translation**: 

---

### Verse 15 (Ramayan 0.515)
- **Original**: Canto XLI. The Citizens' Lament. 497 As one between two hosts, inclined To neither was Sumantra's mind. But Ráma spake these words again: “A lengthened woe is bitterest pain. On, on; and if his wrath grow hot, Thine answer be,‘I heard thee not.’ ” Sumantra, at the chief's behest, Dismissed the crowd that toward him pressed, And, as he bade, to swiftest speed Urged on his way each willing steed. The king's attendants parted thence, And paid him heart-felt reverence: In mind, and with the tears he wept, Each still his place near Ráma kept. As swift away the horses sped, His lords to Da[aratha said: “To follow him whom thou again Wouldst see returning home is vain.” With failing limb and drooping mien He heard their counsel wise: Still on their son the king and queen Kept fast their lingering eyes.314 Canto XLI. The Citizens' Lament. 314 “Thirty centuries have passed since he began this memorable journey. Every step of it is known and is annually traversed by thousands: hero worship is not extinct. What can Faith do! How strong are the ties of religion when entwined with the legends of a country! How many a cart creeps creaking and weary along the road from Ayodhyá to Chitrakúm. It is this that gives the Rámáyan a strange interest, the story still lives.” Calcutta Review: Vol. XXIII.
- **Translation**: 

---

### Verse 16 (Ramayan 0.516)
- **Original**: 498 The Ramayana The lion chief with hands upraised Was born from eyes that fondly gazed. But then the ladies' bower was rent With cries of weeping and lament: “Where goes he now, our lord, the sure Protector of the friendless poor, In whom the wretched and the weak Defence and aid were wont to seek? All words of wrath he turned aside, And ne'er, when cursed, in ire replied. He shared his people's woe, and stilled The troubled breast which rage had filled. Our chief, on lofty thoughts intent, In glorious fame preëminent: As on his own dear mother, thus He ever looked on each of us. Where goes he now? His sire's behest, By Queen Kaikeyí's guile distressed, Has banished to the forest hence Him who was all the world's defence. Ah, senseless King, to drive away The hope of men, their guard and stay, To banish to the distant wood Ráma the duteous, true, and good!” The royal dames, like cows bereaved Of their young calves, thus sadly grieved. The monarch heard them as they wailed, And by the fire of grief assailed For his dear son, he bowed his head, And all his sense and memory fled. Then were no fires of worship fed, Thick darkness o'er the sun was spread. The cows their thirsty calves denied,
- **Translation**: 

---

### Verse 17 (Ramayan 0.517)
- **Original**: Canto XLI. The Citizens' Lament. 499 And elephants flung their food aside. [144] Tri[anku,315 Jupiter looked dread, And Mercury and Mars the red, In direful opposition met, The glory of the moon beset. The lunar stars withheld their light, The planets were no longer bright, But meteors with their horrid glare, And dire Vi[ákhás316 lit the air. As troubled Ocean heaves and raves When Doom's wild tempest sweeps the waves, Thus all Ayodhyá reeled and bent When Ráma to the forest went. And chilling grief and dark despair Fell suddenly on all men there. Their wonted pastime all forgot, Nor thought of food, or touched it not. Crowds in the royal street were seen With weeping eye and troubled mien: No more a people gay and glad, Each head and heart was sick and sad. No more the cool wind softly blew, The moon no more was fair to view, No more the sun with genial glow Cherished the world now plunged in woe. Sons, brothers, husbands, wedded wives Forgot the ties that joined their lives; No thought for kith and kin was spared, But all for only Ráma cared. And Ráma's friends who loved him best, Their minds disordered and distressed. By the great burthen of their woes 315 See p. 72. 316 Four stars of the sixteenth lunar asterism.
- **Translation**: 

---

### Verse 18 (Ramayan 0.518)
- **Original**: 500 The Ramayana Turned not to slumber or repose. Like Earth with all her hills bereft Of Indra's guiding care. Ayodhyá in her sorrow left By him, the high souled heir, Was bowed by fear and sorrow's force, And shook with many a throe, While warrior, elephant, and horse Sent up the cry of woe. Canto XLII. Dasaratha's Lament. While yet the dust was seen afar That marked the course of Ráma's car, The glory of Ikshváku's race Turned not away his eager face. While yet his duteous son he saw He could not once his gaze withdraw, But rooted to the spot remained With eyes that after Ráma strained. But when that dust no more he viewed, Fainting he fell by grief subdued. To his right hand Kau[alyá went, And ready aid the lady lent, While Bharat's loving mother tried To raise him on the other side. The king, within whose ordered soul Justice and virtue held control, To Queen Kaikeyí turned and said, With every sense disquieted: “Touch me not, thou whose soul can plot
- **Translation**: 

---

### Verse 19 (Ramayan 0.519)
- **Original**: Canto XLII. Dasaratha's Lament. 501 All sin. Kaikeyí, touch me not. No loving wife, no friend to me, I ne'er again would look on thee; Ne'er from this day have aught to do With thee and all thy retinue; Thee whom no virtuous thoughts restrain, Whose selfish heart seeks only gain. The hand I laid in mine, O dame, The steps we took around the flame,317 And all that links thy life to mine Here and hereafter I resign. If Bharat too, thy darling son, Joy in the rule thy art has won, Ne'er may the funeral offerings paid By his false hand approach my shade.” Then while the dust upon him hung, The monarch to Kau[alyá clung, And she with mournful steps and slow Turned to the palace, worn with woe. As one whose hand has touched the fire, Or slain a Bráhman in his ire, He felt his heart with sorrow torn Still thinking of his son forlorn. Each step was torture, as the road The traces of the chariot showed, And as the shadowed sun grows dim So care and anguish darkened him. He raised a cry, by woe distraught, As of his son again he thought. And judging that the car had sped Beyond the city, thus he said: “I still behold the foot-prints made 317 In the marriage service.
- **Translation**: 

---

### Verse 20 (Ramayan 0.520)
- **Original**: 502 The Ramayana By the good horses that conveyed My son afar: these marks I see, But high-souled Ráma, where is he? Ah me, my son! my first and best, On pleasant couches wont to rest, With limbs perfumed with sandal, fanned By many a beauty's tender hand: Where will he lie with log or stone Beneath him for a pillow thrown, To leave at morn his earthy bed, Neglected, and with dust o'erspread, As from the flood with sigh and pant Comes forth the husband elephant? The men who make the woods their home Shall see the long-armed hero roam Roused from his bed, though lord of all, In semblance of a friendless thrall. Janak's dear child who ne'er has met[145] With aught save joy and comfort yet, Will reach to-day the forest, worn And wearied with the brakes of thorn. Ah, gentle girl, of woods unskilled, How will her heart with dread be filled At the wild beasts' deep roaring there, Whose voices lift the shuddering hair! Kaikeyí, glory in thy gain, And, widow queen, begin to reign: No will, no power to live have I When my brave son no more is nigh.” Thus pouring forth laments, the king Girt by the people's crowded ring, Entered the noble bower like one New-bathed when funeral rites are done.
- **Translation**: 

---



--- End of Ramayan_batch_26.md ---


--- Start of Ramayan_batch_27.md ---

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

### Verse 1 (Ramayan 0.521)
- **Original**: Canto XLII. Dasaratha's Lament. 503 Where'er he looked naught met his gaze But empty houses, courts, and ways. Closed were the temples: countless feet No longer trod the royal street, And thinking of his son he viewed Men weak and worn and woe-subdued. As sinks the sun into a cloud, So passed he on, and wept aloud, Within that house no more to be The dwelling of the banished three, Brave Ráma, his Vedehan bride, And Lakshma G by his brother's side: Like broad still waters, when the king Of all the birds that ply the wing Has swooped from heaven and borne away The glittering snakes that made them gay. With choking sobs and voice half spent The king renewed his sad lament: With broken utterance faint and low Scarce could he speak these words of woe: “My steps to Ráma's mother guide, And place me by Kau[alyá's side: There, only there my heart may know Some little respite from my woe.” The warders of the palace led The monarch, when his words were said, To Queen Kau[alyá's bower, and there Laid him with reverential care. But while he rested on the bed Still was his soul disquieted. In grief he tossed his arms on high Lamenting with a piteous cry: “O Ráma, Ráma,” thus said he,
- **Translation**: 

---

### Verse 2 (Ramayan 0.522)
- **Original**: 504 The Ramayana “My son, thou hast forsaken me. High bliss awaits those favoured men Left living in Ayodhyá then, Whose eyes shall see my son once more Returning when the time is o'er.” Then came the night, whose hated gloom Fell on him like the night of doom. At midnight Da[aratha cried To Queen Kau[alyá by his side: “I see thee not, Kau[alyá; lay Thy gentle hand in mine, I pray. When Ráma left his home my sight Went with him, nor returns to-night.” Canto XLIII. Kausalyá's Lament. Kau [alyá saw the monarch lie With drooping frame and failing eye, And for her banished son distressed With these sad words her lord addressed: “Kaikeyí, cruel, false, and vile Has cast the venom of her guile On Ráma lord of men, and she Will ravage like a snake set free; And more and more my soul alarm, Like a dire serpent bent on harm, For triumph crowns each dark intent, And Ráma to the wild is sent. Ah, were he doomed but here to stray Begging his food from day to day, Or do, enslaved, Kaikeyí's will,
- **Translation**: 

---

### Verse 3 (Ramayan 0.523)
- **Original**: Canto XLIII. Kausalyá's Lament. 505 This were a boon, a comfort still. But she, as chose her cruel hate, Has hurled him from his high estate, As Bráhmans when the moon is new Cast to the ground the demons' due.318 The long-armed hero, like the lord Of Nágas, with his bow and sword Begins, I ween, his forest life With LakshmaG and his faithful wife. Ah, how will fare the exiles now, Whom, moved by Queen Kaikeyí, thou Hast sent in forests to abide, Bred in delights, by woe untried? Far banished when their lives are young, With the fair fruit before them hung, Deprived of all their rank that suits, How will they live on grain and roots? O, that my years of woe were passed, And the glad hour were come at last When I shall see my children dear, Ráma, his wife, and LakshmaG here! When shall Ayodhyá, wild with glee, Again those mighty heroes see, And decked with wreaths her banners wave To welcome home the true and brave? When will the beautiful city view With happy eyes the lordly two Returning, joyful as the main When the dear moon is full again? When, like some mighty bull who leads The cow exulting through the meads, Will Ráma through the city ride, 318 The husks and chaff of the rice offered to the Gods.
- **Translation**: 

---

### Verse 4 (Ramayan 0.524)
- **Original**: 506 The Ramayana Strong-armed, with Sítá at his side? When will ten thousand thousand meet And crowd Ayodhyá's royal street, And grain in joyous welcome throw Upon my sons who tame the foe? When with delight shall youthful bands Of Bráhman maidens in their hands[146] Bear fruit and flowers in goodly show, And circling round Ayodhyá go? With ripened judgment of a sage, And godlike in his blooming age, When shall my virtuous son appear, Like kindly rain, our hearts to cheer? Ah, in a former life, I ween, This hand of mine, most base and mean, Has dried the udders of the kine And left the thirsty calves to pine. Hence, as the lion robs the cow, Kaikeyí makes me childless now, Exulting from her feebler foe To rend the son she cherished so. I had but him, in Scripture skilled, With every grace his soul was filled. Now not a joy has life to give, And robbed of him I would not live: Yea, all my days are dark and drear If he, my darling, be not near, And Lakshma G brave, my heart to cheer. As for my son I mourn and yearn, The quenchless flames of anguish burn And kill me with the pain, As in the summer's noontide blaze The glorious Day-God with his rays Consumes the parching plain.”
- **Translation**: 

---

### Verse 5 (Ramayan 0.525)
- **Original**: Canto XLIV. Sumitrá's Speech. 507 Canto XLIV. Sumitrá's Speech. Kau [alyá ceased her sad lament, Of beauteous dames most excellent. Sumitrá who to duty clave, In righteous words this answer gave: “Dear Queen, all noble virtues grace Thy son, of men the first in place. Why dost thou shed these tears of woe With bitter grief lamenting so? If Ráma, leaving royal sway Has hastened to the woods away, 'Tis for his high-souled father's sake That he his premise may not break. He to the path of duty clings Which lordly fruit hereafter brings— The path to which the righteous cleave— For him, dear Queen, thou shouldst not grieve. And Lakshma G too, the blameless-souled, The same high course with him will hold, And mighty bliss on him shall wait, So tenderly compassionate. And Sítá, bred with tender care, Well knows what toils await her there, But in her love she will not part From Ráma of the virtuous heart. Now has thy son through all the world The banner of his fame unfurled; True, modest, careful of his vow, What has he left to aim at now? The sun will mark his mighty soul, His wisdom, sweetness, self-control, Will spare from pain his face and limb, And with soft radiance shine for him.
- **Translation**: 

---

### Verse 6 (Ramayan 0.526)
- **Original**: 508 The Ramayana For him through forest glades shall spring A soft auspicious breeze, and bring Its tempered heat and cold to play Around him ever night and day. The pure cold moonbeams shall delight The hero as he sleeps at night, And soothe him with the soft caress Of a fond parent's tenderness. To him, the bravest of the brave, His heavenly arms the Bráhman gave, When fierce Suváhu dyed the plain With his life-blood by Ráma slain. Still trusting to his own right arm Thy hero son will fear no harm: As in his father's palace, he In the wild woods will dauntless be. Whene'er he lets his arrows fly His stricken foemen fall and die: And is that prince of peerless worth Too weak to keep and sway the earth? His sweet pure soul, his beauty's charm, His hero heart, his warlike arm, Will soon redeem his rightful reign When from the woods he comes again. The Bráhmans on the prince's head King-making drops shall quickly shed, And Sítá, Earth, and Fortune share The glories which await the heir. For him, when forth his chariot swept, The crowd that thronged Ayodhyá wept, With agonizing woe distressed. With him in hermít's mantle dressed In guise of Sítá Lakshmí went, And none his glory may prevent.
- **Translation**: 

---

### Verse 7 (Ramayan 0.527)
- **Original**: Canto XLIV. Sumitrá's Speech. 509 Yea, naught to him is high or hard, Before whose steps, to be his guard, Lakshma G, the best who draws the bow, With spear, shaft, sword rejoiced to go. His wanderings in the forest o'er, Thine eyes shall see thy son once more, Quit thy faint heart, thy grief dispel, For this, O Queen, is truth I tell. Thy son returning, moonlike, thence, Shall at thy feet do reverence, And, blest and blameless lady, thou Shalt see his head to touch them bow, Yea, thou shalt see thy son made king When he returns with triumphing, And how thy happy eyes will brim With tears of joy to look on him! Thou, blameless lady, shouldst the whole Of the sad people here console: Why in thy tender heart allow This bitter grief to harbour now? As the long banks of cloud distil Their water when they see the hill, [147] So shall the drops of rapture run From thy glad eyes to see thy son Returning, as he lowly bends To greet thee, girt by all his friends.” Thus soothing, kindly eloquent, With every hopeful argument Kau [alyá's heart by sorrow rent, Fair Queen Sumitrá ceased. Kau [alyá heard each pleasant plea, And grief began to leave her free, As the light clouds of autumn flee,
- **Translation**: 

---

### Verse 8 (Ramayan 0.528)
- **Original**: 510 The Ramayana Their watery stores decreased. Canto XLV. The Tamasá. Their tender love the people drew To follow Ráma brave and true, The high-souled hero, as he went Forth from his home to banishment. The king himself his friends obeyed, And turned him homeward as they prayed. But yet the people turned not back, Still close on Ráma's chariot track. For they who in Ayodhyá dwelt For him such fond affection felt, Decked with all grace and glories high, The dear full moon of every eye. Though much his people prayed and wept, Kakutstha's son his purpose kept, And still his journey would pursue To keep the king his father true. Deep in the hero's bosom sank Their love, whose signs his glad eye drank. He spoke to cheer them, as his own Dear children, in a loving tone: “If ye would grant my fond desire, Give Bharat now that love entire And reverence shown to me by all Who dwell within Ayodhyá's wall. For he, Kaikeyí's darling son, His virtuous career will run, And ever bound by duty's chain
- **Translation**: 

---

### Verse 9 (Ramayan 0.529)
- **Original**: Canto XLV. The Tamasá. 511 Consult your weal and bliss and gain. In judgment old, in years a child, With hero virtues meek and mild, A fitting lord is he to cheer His people and remove their fear. In him all kingly gifts abound, More noble than in me are found: Imperial prince, well proved and tried— Obey him as your lord and guide. And grant, I pray, the boon I ask: To please the king be still your task, That his fond heart, while I remain Far in the wood, may feel no pain.” The more he showed his will to tread The path where filial duty led, The more the people, round him thronged, For their dear Ráma's empire longed. Still more attached his followers grew, As Ráma, with his brother, drew The people with his virtues' ties, Lamenting all with tear-dimmed eyes. The saintly twice-born, triply old In glory, knowledge, seasons told, With hoary heads that shook and bowed, Their voices raised and spake aloud: “O steeds, who best and noblest are, Who whirl so swiftly Ráma's car, Go not, return: we call on you: Be to your master kind and true. For speechless things are swift to hear, And naught can match a horse's ear, O generous steeds, return, when thus You hear the cry of all of us.
- **Translation**: 

---

### Verse 10 (Ramayan 0.530)
- **Original**: 512 The Ramayana Each vow he keeps most firm and sure, And duty makes his spirit pure. Back with our chief! not wood-ward hence; Back to his royal residence!” Soon as he saw the aged band. Exclaiming in their misery, stand, And their sad cries around him rang, Swift from his chariot Ráma sprang. Then, still upon his journey bent, With Sítá and with LakshmaG went The hero by the old men's side Suiting to theirs his shortened stride. He could not pass the twice-born throng As weariedly they walked along: With pitying heart, with tender eye, He could not in his chariot fly. When the steps of Ráma viewed That still his onward course pursued, Woe shook the troubled heart of each, And burnt with grief they spoke this speech— “With thee, O Ráma, to the wood All Bráhmans go and Bráhmanhood: Borne on our aged shoulders, see, Our fires of worship go with thee. Bright canopies that lend their shade In Vájapeya319 rites displayed, In plenteous store are borne behind Like cloudlets in the autumn wind. No shelter from the sun hast thou, And, lest his fury burn thy brow, These sacrificial shades we bear 319 An important sacrifice at which seventeen victims were immolated.
- **Translation**: 

---

### Verse 11 (Ramayan 0.531)
- **Original**: Canto XLV. The Tamasá. 513 Shall aid thee in the noontide glare. Our hearts, who ever loved to pore On sacred text and Vedic lore, Now all to thee, beloved, turn, And for a life in forests yearn. Deep in our aged bosoms lies The Vedas' lore, the wealth we prize, There still, like wives at home, shall dwell, Whose love and truth protect them well. [148] To follow thee our hearts are bent; We need not plan or argument. All else in duty's law we slight, For following thee is following right. O noble Prince, retrace thy way: O, hear us, Ráma, as we lay, With many tears and many prayers, Our aged heads and swan-white hairs Low in the dust before thy feet; O, hear us, Ráma, we entreat. Full many of these who with thee run, Their sacred rites had just begun. Unfinished yet those rites remain; But finished if thou turn again. All rooted life and things that move To thee their deep affection prove. To them, when warmed by love, they glow And sue to thee, some favour show, Each lowly bush, each towering tree Would follow too for love of thee. Bound by its root it must remain; But— all it can— its boughs complain, As when the wild wind rushes by It tells its woe in groan and sigh. No more through air the gay birds flit,
- **Translation**: 

---

### Verse 12 (Ramayan 0.532)
- **Original**: 514 The Ramayana But, foodless, melancholy sit Together on the branch and call To thee whose kind heart feels for all.” As wailed the aged Bráhmans, bent To turn him back, with wild lament, Seemed Tamasá herself to aid, Checking his progress, as they prayed. Sumantra from the chariot freed With ready hand each weary steed; He groomed them with the utmost heed, Their limbs he bathed and dried, Then led them forth to drink and feed At pleasure in the grassy mead That fringed the river side. Canto XLVI. The Halt. When Ráma, chief of Raghu's race, Arrived at that delightful place, He looked on Sítá first, and then To LakshmaG spake the lord of men: “Now first the shades of night descend Since to the wilds our steps we bend. Joy to thee, brother! do not grieve For our dear home and all we leave. The woods unpeopled seem to weep Around us, as their tenants creep Or fly to lair and den and nest, Both bird and beast, to seek their rest.
- **Translation**: 

---

### Verse 13 (Ramayan 0.533)
- **Original**: Canto XLVI. The Halt. 515 Methinks Ayodhyá's royal town Where dwells my sire of high renown, With all her men and dames to-night Will mourn us vanished from their sight. For, by his virtues won, they cling In fond affection to their king, And thee and me, O brave and true, And Bharat andZatrughna too. I for my sire and mother feel Deep sorrow o'er my bosom steal, Lest mourning us, oppressed with fears, They blind their eyes with endless tears. Yet Bharat's duteous love will show Sweet comfort in their hours of woe, And with kind words their hearts sustain, Suggesting duty, bliss, and gain. I mourn my parents now no more: I count dear Bharat's virtues o'er, And his kind love and care dispel The doubts I had, and all is well. And thou thy duty wouldst not shun, And, following me, hast nobly done; Else, bravest, I should need a band Around my wife as guard to stand. On this first night, my thirst to slake, Some water only will I take: Thus, brother, thus my will decides, Though varied store the wood provides.” Thus having said to LakshmaG, he Addressed in turn Sumantra:“Be Most diligent to-night, my friend, And with due care thy horses tend.” The sun had set: Sumantra tied
- **Translation**: 

---

### Verse 14 (Ramayan 0.534)
- **Original**: 516 The Ramayana His noble horses side by side, Gave store of grass with liberal hand, And rested near them on the strand. Each paid the holy evening rite, And when around them fell the night, The charioteer, with LakshmaG's aid, A lowly bed for Ráma laid. To LakshmaG Ráma bade adieu, And then by Sítá's side he threw His limbs upon the leafy bed Their care upon the bank had spread. When Lakshma G saw the couple slept, Still on the strand his watch he kept, Still with Sumantra there conversed, And Ráma's varied gifts rehearsed. All night he watched, nor sought repose, Till on the earth the sun arose: With him Sumantra stayed awake, And still of Ráma's virtues spake. Thus, near the river's grassy shore Which herds unnumbered wandered o'er, Repose, untroubled, Ráma found, And all the people lay around. The glorious hero left his bed, Looked on the sleeping crowd, and said To LakshmaG, whom each lucky line Marked out for bliss with surest sign: “O brother LakshmaG, look on these Reclining at the roots of trees; All care of house and home resigned, Caring for us with heart and mind, These people of the city yearn[149]
- **Translation**: 

---

### Verse 15 (Ramayan 0.535)
- **Original**: Canto XLVI. The Halt. 517 To see us to our home return: To quit their lives will they consent, But never leave their firm intent. Come, while they all unconscious sleep, Let us upon the chariot leap, And swiftly on our journey speed Where naught our progress may impede, That these fond citizens who roam Far from Ikshváku's ancient home, No more may sleep 'neath bush and tree, Following still for love of me. A prince with tender care should heal The self-brought woes his people feel, And never let his subjects share The burthen he is forced to bear.” Then LakshmaG to the chief replied, Who stood like Justice by his side: “Thy rede, O sage, I well commend: Without delay the car ascend.” Then Ráma to Sumantra spoke: “Thy rapid steeds, I pray thee, yoke. Hence to the forest will I go: Away, my lord, and be not slow.” Sumantra, urged to utmost speed, Yoked to the car each generous steed, And then, with hand to hand applied, He came before the chief and cried: “Hail, Prince, whom mighty arms adorn, Hail, bravest of the chariot-borne! With Sítá and thy brother thou Mayst mount: the car is ready now.”
- **Translation**: 

---

### Verse 16 (Ramayan 0.536)
- **Original**: 518 The Ramayana The hero clomb the car with haste: His bow and gear within were placed, And quick the eddying flood he passed Of Tamasá whose waves run fast. Soon as he touched the farther side, That strong-armed hero, glorified, He found a road both wide and clear, Where e'en the timid naught could fear. Then, that the crowd might be misled, Thus Ráma to Sumantra said: “Speed north a while, then hasten back, Returning in thy former track, That so the people may not learn The course I follow: drive and turn.” Sumantra, at the chief's behest, Quick to the task himself addressed; Then near to Ráma came, and showed The chariot ready for the road. With Sítá, then, the princely two, Who o'er the line of Raghu threw A glory ever bright and new, Upon the chariot stood. Sumantra fast and faster drove His horses, who in fleetness strove Still onward to the distant grove, The hermit-haunted wood. Canto XLVII. The Citizens' Return.
- **Translation**: 

---

### Verse 17 (Ramayan 0.537)
- **Original**: Canto XLVII. The Citizens' Return. 519 The people, when the morn shone fair, Arose to find no Ráma there. Then fear and numbing grief subdued The senses of the multitude. The woe-born tears were running fast As all around their eyes they cast, And sadly looked, but found no trace Of Ráma, searching every place. Bereft of Ráma good and wise, With drooping cheer and weeping eyes, Each woe-distracted sage gave vent To sorrow in his wild lament: “Woe worth the sleep that stole our sense With its beguiling influence, That now we look in vain for him Of the broad chest and stalwart limb! How could the strong-armed hero, thus Deceiving all, abandon us? His people so devoted see, Yet to the woods, a hermit, flee? How can he, wont our hearts to cheer, As a fond sire his children dear,— How can the pride of Raghu's race Fly from us to some desert place! Here let us all for death prepare, Or on the last great journey fare;320 Of Ráma our dear lord bereft, What profit in our lives is left? Huge trunks of trees around us lie, With roots and branches sere and dry, Come let us set these logs on fire And throw our bodies on the pyre. 320 The great pilgrimage to the Himálayas, in order to die there.
- **Translation**: 

---

### Verse 18 (Ramayan 0.538)
- **Original**: 520 The Ramayana What shall we speak? How can we say We followed Ráma on his way, The mighty chief whose arm is strong, Who sweetly speaks, who thinks no wrong? Ayodhyá's town with sorrow dumb, Without our lord will see us come, And hopeless misery will strike Elder, and child, and dame alike. Forth with that peerless chief we came, Whose mighty heart is aye the same: How, reft of him we love, shall we Returning dare that town to see?” Complaining thus with varied cry They tossed their aged arms on high, And their sad hearts with grief were wrung, Like cows who sorrow for their young. A while they followed on the road Which traces of his chariot showed, But when at length those traces failed, A deep despair their hearts assailed.[150] The chariot marks no more discerned, The hopeless sages backward turned: “Ah, what is this? What can we more? Fate stops the way, and all is o'er.” With wearied hearts, in grief and shame They took the road by which they came, And reached Ayodhyá's city, where From side to side was naught but care. With troubled spirits quite cast down They looked upon the royal town, And from their eyes, oppressed with woe, Their tears again began to flow. Of Ráma reft, the city wore
- **Translation**: 

---

### Verse 19 (Ramayan 0.539)
- **Original**: Canto XLVIII. The Women's Lament. 521 No look of beauty as before, Like a dull river or a lake By Garu robbed of every snake. Dark, dismal as the moonless sky, Or as a sea whose bed is dry, So sad, to every pleasure dead, They saw the town, disquieted. On to their houses, high and vast, Where stores of precious wealth were massed, The melancholy Bráhmans passed, Their hearts with anguish cleft: Aloof from all, they came not near To stranger or to kinsman dear, Showing in faces blank and drear That not one joy was left. Canto XLVIII. The Women's Lament. When those who forth with Ráma went Back to the town their steps had bent, It seemed that death had touched and chilled Those hearts which piercing sorrow filled. Each to his several mansion came, And girt by children and his dame, From his sad eyes the water shed That o'er his cheek in torrents spread. All joy was fled: oppressed with cares No bustling trader showed his wares. Each shop had lost its brilliant look, Each householder forbore to cook. No hand with joy its earnings told,
- **Translation**: 

---

### Verse 20 (Ramayan 0.540)
- **Original**: 522 The Ramayana None cared to win a wealth of gold, And scarce the youthful mother smiled To see her first, her new-born child. In every house a woman wailed, And her returning lord assailed With keen taunt piercing like the steel That bids the tusked monster kneel: “What now to them is wedded dame, What house and home and dearest aim, Or son, or bliss, or gathered store, Whose eyes on Ráma look no more! There is but one in all the earth, One man alone of real worth, Lakshma G, who follows, true and good, Ráma, with Sítá, through the wood. Made holy for all time we deem Each pool and fountain, lake and stream, If great Kakutstha's son shall choose Their water for his bath to use. Each forest, dark with lovely trees, Shall yearn Kakutstha's son to please; Each mountain peak and woody hill, Each mighty flood and mazy rill, Each rocky height, each shady grove Where the blest feet of Ráma rove, Shall gladly welcome with the best Of all they have their honoured guest. The trees that clustering blossoms bear, And bright-hued buds to gem their hair, The heart of Ráma shall delight, And cheer him on the breezy height. For him the upland slopes will show The fairest roots and fruit that grow, And all their wealth before him fling
- **Translation**: 

---



--- End of Ramayan_batch_27.md ---


--- Start of Ramayan_batch_28.md ---

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

### Verse 1 (Ramayan 0.541)
- **Original**: Canto XLVIII. The Women's Lament. 523 Ere the due hour of ripening. For him each earth-upholding hill Its crystal water shall distil, And all its floods shall be displayed In many a thousand-hued cascade. Where Ráma stands is naught to fear, No danger comes if he be near; For all who live on him depend, The world's support, and lord, and friend. Ere in too distant wilds he stray, Let us to Ráma speed away, For rich reward on those will wait Who serve a prince of soul so great. We will attend on Sítá there; Be Raghu's son your special care.” The city dames, with grief distressed, Thus once again their lords addressed: “Ráma shall be your guard and guide, And Sítá will for us provide. For who would care to linger here, Where all is sad and dark and drear? Who, mid the mourners, hope for bliss In a poor soulless town like this? If Queen Kaikeyí's treacherous sin, Our lord expelled, the kingdom win, We heed not sons or golden store, Our life itself we prize no more. If she, seduced by lust of sway, Her lord and son could cast away, Whom would she leave unharmed, the base Defiler of her royal race? We swear it by our children dear, We will not dwell as servants here;
- **Translation**: 

---

### Verse 2 (Ramayan 0.542)
- **Original**: 524 The Ramayana If Queen Kaikeyí live to reign, We will not in her realm remain. Bowed down by her oppressive hand, The helpless, lordless, godless land, Cursed for Kaikeyí's guilt will fall, And swift destruction seize it all.[151] For, Ráma forced from home to fly, The king his sire will surely die, And when the king has breathed his last Ruin will doubtless follow fast. Sad, robbed of merits, drug the cup And drink the poisoned mixture up, Or share the exiled Ráma's lot, Or seek some land that knows her not. No reason, but a false pretence Drove Ráma, Sítá, LakshmaG hence, And we to Bharat have been given Like cattle to the shambles driven.” While in each house the women, pained At loss of Ráma, still complained, Sank to his rest the Lord of Day, And night through all the sky held sway. The fires of worship all were cold, No text was hummed, no tale was told, And shades of midnight gloom came down Enveloping the mournful town. Still, sick at heart, the women shed, As for a son or husband fled, For Ráma tears, disquieted: No child was loved as he. And all Ayodhyá, where the feast, Music, and song, and dance had ceased, And merriment and glee,
- **Translation**: 

---

### Verse 3 (Ramayan 0.543)
- **Original**: Canto XLIX. The Crossing Of The Rivers. 525 Where every merchant's store was closed That erst its glittering wares exposed, Was like a dried up sea. Canto XLIX. The Crossing Of The Rivers. Now Ráma, ere the night was fled, O'er many a league of road had sped, Till, as his course he onward held, The morn the shades of night dispelled. The rites of holy dawn he paid, And all the country round surveyed. He saw, as still he hurried through With steeds which swift as arrows flew, Hamlets and groves with blossoms fair, And fields which showed the tillers' care, While from the clustered dwellings near The words of peasants reached his ear: “Fie on our lord the king, whose soul Is yielded up to love's control! Fie on the vile Kaikeyí! Shame On that malicious sinful dame, Who, keenly bent on cruel deeds, No bounds of right and virtue heeds, But with her wicked art has sent So good a prince to banishment, Wise, tender-hearted, ruling well His senses, in the woods to dwell. Ah cruel king! his heart of steel For his own son no love could feel, Who with the sinless Ráma parts,
- **Translation**: 

---

### Verse 4 (Ramayan 0.544)
- **Original**: 526 The Ramayana The darling of the people's hearts.” These words he heard the peasants say, Who dwelt in hamlets by the way, And, lord of all the realm by right, Through Ko[ala pursued his flight. Through the auspicious flood, at last, Of Veda[rutí's stream he passed, And onward to the place he sped By Saint Agastya tenanted. Still on for many an hour he hied, And crossed the stream whose cooling tide Rolls onward till she meets the sea, The herd-frequented Gomatí.321 Borne by his rapid horses o'er, He reached that river's further shore. And Syandiká's, whose swan-loved stream Resounded with the peacock's scream. Then as he journeyed on his road To his Videhan bride he showed The populous land which Manu old To King Ikshváku gave to hold. The glorious prince, the lord of men Looked on the charioteer, and then Voiced like a wild swan, loud and clear, He spake these words and bade him hear: “When shall I, with returning feet My father and my mother meet? When shall I lead the hunt once more In bloomy woods on Sarjú's shore? Most eagerly I long to ride Urging the chase on Sarjú's side. For royal saints have seen no blame 321 Known to Europeans as the Goomtee.
- **Translation**: 

---

### Verse 5 (Ramayan 0.545)
- **Original**: Canto L. The Halt Under The Ingudí. 527 In this, the monarch's matchless game.” Thus speeding on,— no rest or stay,— Ikshváku's son pursued his way. Oft his sweet voice the silence broke, And thus on varied themes he spoke. Canto L. The Halt Under The Ingudí.322 So through the wide and fair extent Of Ko[ala the hero went. Then toward Ayodhyá back he gazed, And cried, with suppliant hands upraised: “Farewell, dear city, first in place, Protected by Kakutstha's race! And Gods, who in thy temples dwell, And keep thine ancient citadel! I from his debt my sire will free, Thy well-loved towers again will see, And, coming from my wild retreat, My mother and my father meet.” [152] Then burning grief inflamed his eye, As his right arm he raised on high, And, while hot tears his cheek bedewed, Addressed the mournful multitude: “By love and tender pity moved, Your love for me you well have proved; Now turn again with joy, and win Success in all your hands begin.” 322 A tree, commonly calledIngua.
- **Translation**: 

---

### Verse 6 (Ramayan 0.546)
- **Original**: 528 The Ramayana Before the high souled chief they bent, With circling steps around him went, And then with bitter wailing, they Departed each his several way. Like the great sun engulfed by night, The hero sped beyond their sight, While still the people mourned his fate And wept aloud disconsolate. The car-borne chieftain passed the bound Of Ko[ala's delightful ground, Where grain and riches bless the land, And people give with liberal hand: A lovely realm unvexed by fear, Where countless shrines and stakes323 appear: Where mango-groves and gardens grow, And streams of pleasant water flow: Where dwells content a well-fed race, And countless kine the meadows grace: Filled with the voice of praise and prayer: Each hamlet worth a monarch's care. Before him three-pathed Gangá rolled Her heavenly waters bright and cold; O'er her pure breast no weeds were spread, Her banks were hermit-visited. The car-borne hero saw the tide That ran with eddies multiplied, And thus the charioteer addressed: “Here on the bank to-day we rest. Not distant from the river, see! There grows a lofty Ingudí With blossoms thick on every spray: There rest we, charioteer, to-day. 323 Sacrificial posts to which the victims were tied.
- **Translation**: 

---

### Verse 7 (Ramayan 0.547)
- **Original**: Canto L. The Halt Under The Ingudí. 529 I on the queen of floods will gaze, Whose holy stream has highest praise, Where deer, and bird, and glittering snake, God, Daitya, bard their pastime take.” Sumantra, LakshmaG gave assent, And with the steeds they thither went. When Ráma reached the lovely tree, With Sítá and with LakshmaG, he Alighted from the car: with speed Sumantra loosed each weary steed. And, hand to hand in reverence laid, Stood near to Ráma in the shade. Ráma's dear friend, renowned by fame, Who of Nisháda lineage came, Guha, the mighty chief, adored Through all the land as sovereign lord, Soon as he heard that prince renowned Was resting on Nisháda ground, Begirt by counsellor and peer And many an honoured friend drew near. Soon as the monarch came in view, Ráma and LakshmaG toward him flew. Then Guha, at the sight distressed, His arms around the hero pressed, Laid both his hands upon his head Bowed to those lotus feet, and said: “O Ráma, make thy wishes known, And be this kingdom as thine own. Who, mighty-armed, will ever see A guest so dear as thou to me?”
- **Translation**: 

---

### Verse 8 (Ramayan 0.548)
- **Original**: 530 The Ramayana He placed before him dainty fare Of every flavour, rich and rare, Brought forth the gift for honoured guest, And thus again the chief addressed: “Welcome, dear Prince, whose arms are strong; These lands and all to thee belong. Thy servants we, our lord art thou; Begin, good king, thine empire now. See, various food before thee placed, And cups to drink and sweets to taste For thee soft beds are hither borne, And for thy horses grass and corn.” To Guha as he pressed and prayed, Thus Raghu's son his answer made: “'Twas aye thy care my heart to please With honour, love, and courtesies, And friendship brings thee now to greet Thy guest thus humbly on thy feet.” Again the hero spake, as round The king his shapely arms he wound: “Guha, I see that all is well With thee and those who with thee dwell; That health and bliss and wealth attend Thy realm, thyself, and every friend. But all these friendly gifts of thine, Bound to refuse, I must decline. Grass, bark, and hide my only wear, And woodland roots and fruit my fare, On duty all my heart is set; I seek the woods, an anchoret. A little grass and corn to feed The horses— this is all I need.
- **Translation**: 

---

### Verse 9 (Ramayan 0.549)
- **Original**: Canto L. The Halt Under The Ingudí. 531 So by this favour, King, alone Shall honour due to me be shown. For these good steeds who brought me here Are to my sire supremely dear; And kind attention paid to these Will honour me and highly please.” Then Guha quickly bade his train Give water to the steeds, and grain. And Ráma, ere the night grew dark, Paid evening rites in dress of bark, And tasted water, on the strand, Drawn from the stream by LakshmaG's hand. And Lakshma G with observance meet Bathed his beloved brother's feet, [153] Who rested with his Maithil spouse: Then sat him down 'neath distant boughs. And Guha with his bow sat near To LakshmaG and the charioteer, And with the prince conversing kept His faithful watch while Ráma slept. As Da[aratha's glorious heir, Of lofty soul and wisdom rare, Reclining with his Sítá there Beside the river lay— He who no troubles e'er had seen, Whose life a life of bliss had been— That night beneath the branches green Passed pleasantly away.
- **Translation**: 

---

### Verse 10 (Ramayan 0.550)
- **Original**: 532 The Ramayana Canto LI. Lakshman's Lament. As LakshmaG still his vigil held By unaffected love impelled, Guha, whose heart the sight distressed, With words like these the prince addressed: “Beloved youth, this pleasant bed Was brought for thee, for thee is spread; On this, my Prince, thine eyelids close, And heal fatigue with sweet repose. My men are all to labour trained, But hardship thou hast ne'er sustained. All we this night our watch will keep And guard Kakutstha's son asleep. In all the world there breathes not one More dear to me than Raghu's son. The words I speak, heroic youth, Are true: I swear it by my truth. Through his dear grace supreme renown Will, so I trust, my wishes crown. So shall my life rich store obtain Of merit, blest with joy and gain. While Raghu's son and Sítá lie Entranced in happy slumber, I Will, with my trusty bow in hand, Guard my dear friend with all my band. To me, who oft these forests range, Is naught therein or new or strange. We could with equal might oppose A four-fold army led by foes.”
- **Translation**: 

---

### Verse 11 (Ramayan 0.551)
- **Original**: Canto LI. Lakshman's Lament. 533 Then royal LakshmaG made reply: “With thee to stand as guardian nigh, Whose faithful soul regards the right, Fearless we well might rest to-night. But how, when Ráma lays his head With Sítá on his lowly bed,— How can I sleep? how can I care For life, or aught that's bright and fair? Behold the conquering chief, whose might Is match for Gods and fiends in fight; With Sítá now he rests his head Asleep on grass beneath him spread. Won by devotion, text, and prayer, And many a rite performed with care, Chief of our father's sons he shines Well marked, like him, with favouring signs. Brief, brief the monarch's life will be Now his dear son is forced to flee; And quickly will the widowed state Mourn for her lord disconsolate. Each mourner there has wept her fill; The cries of anguish now are still: In the king's hall each dame, o'ercome With weariness of woe is dumb. This first sad night of grief, I ween, Will do to death each sorrowing queen: Scarce is Kau[alyá left alive; My mother, too, can scarce survive. If when her heart is fain to break, She lingers forZatrughna's sake, Kau [alyá, mother of the chief, Must sink beneath the chilling grief. That town which countless thousands fill, Whose hearts with love of Ráma thrill,—
- **Translation**: 

---

### Verse 12 (Ramayan 0.552)
- **Original**: 534 The Ramayana The world's delight, so rich and fair,— Grieved for the king, his death will share. The hopes he fondly cherished, crossed Ayodhyá's throne to Ráma lost,— With mournful cries, Too late, too late! The king my sire will meet his fate. And when my sire has passed away, Most happy in their lot are they, Allowed, with every pious care, Part in his funeral rites to bear. And O, may we with joy at last,— These years of forest exile past,— Turn to Ayodhyá's town to dwell With him who keeps his promise well!” While thus the hero mighty-souled, In wild lament his sorrow told, Faint with the load that on him lay, The hours of darkness passed away. As thus the prince, impelled by zeal For his loved brother, prompt to feel Strong yearnings for the people's weal, His words of truth outspake, King Guha grieved to see his woe, Heart-stricken, gave his tears to flow, Tormented by the common blow, Sad, as a wounded snake. Canto LII. The Crossing Of Gangá.
- **Translation**: 

---

### Verse 13 (Ramayan 0.553)
- **Original**: Canto LII. The Crossing Of Gangá. 535 Soon as the shades of night had fled, Uprising from his lowly bed, Ráma the famous, broad of chest, His brother LakshmaG thus addressed: “Now swift upsprings the Lord of Light, And fled is venerable night. [154] That dark-winged bird the Koïl now Is calling from the topmost bough, And sounding from the thicket nigh Is heard the peacock's early cry. Come, cross the flood that seeks the sea, The swiftly flowing Jáhnaví.”324 King Guha heard his speech, agreed, And called his minister with speed: “A boat,” he cried,“swift, strong, and fair, With rudder, oars, and men, prepare, And place it ready by the shore To bear the pilgrims quickly o'er.” Thus Guha spake: his followers all Bestirred them at their master's call; Then told the king that ready manned A gay boat waited near the strand. Then Guha, hand to hand applied, With reverence thus to Ráma cried: “The boat is ready by the shore: How, tell me, can I aid thee more? O lord of men, it waits for thee To cross the flood that seeks the sea. O godlike keeper of thy vow, Embark: the boat is ready now.” 324 Daughter of Jahnu, a name of the Ganges. See p. 55.
- **Translation**: 

---

### Verse 14 (Ramayan 0.554)
- **Original**: 536 The Ramayana Then Ráma, lord of glory high, Thus to King Guha made reply: “Thanks for thy gracious care, my lord: Now let the gear be placed on board.” Each bow-armed chief, in mail encased, Bound sword and quiver to his waist, And then with Sítá near them hied Down the broad river's shelving side. Then with raised palms the charioteer, In lowly reverence drawing near, Cried thus to Ráma good and true: “Now what remains for me to do?” With his right hand, while answering The hero touched his friend: “Go back,” he said,“and on the king With watchful care attend. Thus far, Sumantra, thou wast guide; Now to Ayodhyá turn,” he cried: “Hence seek we leaving steeds and car, On foot the wood that stretches far.” Sumantra, when, with grieving heart, He heard the hero bid him part, Thus to the bravest of the brave, Ikshváku's son, his answer gave: “In all the world men tell of naught, To match thy deed, by heroes wrought— Thus with thy brother and thy wife Thrall-like to lead a forest life. No meet reward of fruit repays Thy holy lore, thy saintlike days, Thy tender soul, thy love of truth, If woe like this afflicts thy youth. Thou, roaming under forest boughs
- **Translation**: 

---

### Verse 15 (Ramayan 0.555)
- **Original**: Canto LII. The Crossing Of Gangá. 537 With thy dear brother and thy spouse Shalt richer meed of glory gain Than if three worlds confessed thy reign. Sad is our fate, O Ráma: we, Abandoned and repelled by thee, Must serve as thralls Kaikeyí's will, Imperious, wicked, born to ill.” Thus cried the faithful charioteer, As Raghu's son, in rede his peer, Was fast departing on his road,— And long his tears of anguish flowed. But Ráma, when those tears were dried His lips with water purified, And in soft accents, sweet and clear, Again addressed the charioteer: “I find no heart, my friend, like thine, So faithful to Ikshváku's line. Still first in view this object keep, That ne'er for me my sire may weep. For he, the world's far-ruling king, Is old, and wild with sorrow's sting; With love's great burthen worn and weak: Deem this the cause that thus I speak Whate'er the high-souled king decrees His loved Kaikeyí's heart to please, Yea, be his order what it may, Without demur thou must obey, For this alone great monarchs reign, That ne'er a wish be formed in vain. Then, O Sumantra, well provide That by no check the king be tried: Nor let his heart in sorrow pine: This care, my faithful friend, be thine.
- **Translation**: 

---

### Verse 16 (Ramayan 0.556)
- **Original**: 538 The Ramayana The honoured king my father greet, And thus for me my words repeat To him whose senses are controlled, Untired till now by grief, and old; “I, Sítá, LakshmaG sorrow not, O Monarch, for our altered lot: The same to us, if here we roam, Or if Ayodhyá be our home, The fourteen years will quickly fly, The happy hour will soon be nigh When thou, my lord, again shalt see Lakshma G, the Maithil dame, and me.” Thus having soothed, O charioteer, My father and my mother dear, Let all the queens my message learn, But to Kaikeyí chiefly turn. With loving blessings from the three, From LakshmaG, Sítá, and from me, My mother, Queen Kau[alyá, greet With reverence to her sacred feet. And add this prayer of mine:“O King; Send quickly forth and Bharat bring, And set him on the royal throne Which thy decree has made his own. When he upon the throne is placed, When thy fond arms are round him laced, Thine aged heart will cease to ache With bitter pangs for Ráma's sake.”[155] And say to Bharat:“See thou treat The queens with all observance meet: What care the king receives, the same Show thou alike to every dame. Obedience to thy father's will Who chooses thee the throne to fill,
- **Translation**: 

---

### Verse 17 (Ramayan 0.557)
- **Original**: Canto LII. The Crossing Of Gangá. 539 Will earn for thee a store of bliss Both in the world to come and this.’ ” Thus Ráma bade Sumantra go With thoughtful care instructed so. Sumantra all his message heard, And spake again, by passion stirred: “O, should deep feeling mar in aught The speech by fond devotion taught, Forgive whate'er I wildly speak: My love is strong, my tongue is weak. How shall I, if deprived of thee, Return that mournful town to see: Where sick at heart the people are Because their Ráma roams afar. Woe will be theirs too deep to brook When on the empty car they look, As when from hosts, whose chiefs are slain, One charioteer comes home again. This very day, I ween, is food Forsworn by all the multitude, Thinking that thou, with hosts to aid, Art dwelling in the wild wood's shade. The great despair, the shriek of woe They uttered when they saw thee go, Will, when I come with none beside, A hundred-fold be multiplied. How to Kau[alyá can I say: “O Queen, I took thy son away, And with thy brother left him well: Weep not for him; thy woe dispel?” So false a tale I cannot frame, Yet how speak truth and grieve the dame? How shall these horses, fleet and bold,
- **Translation**: 

---

### Verse 18 (Ramayan 0.558)
- **Original**: 540 The Ramayana Whom not a hand but mine can hold, Bear others, wont to whirl the car Wherein Ikshváku's children are! Without thee, Prince, I cannot, no, I cannot to Ayodhyá go. Then deign, O Ráma, to relent, And let me share thy banishment. But if no prayers can move thy heart, If thou wilt quit me and depart, The flames shall end my car and me, Deserted thus and reft of thee. In the wild wood when foes are near, When dangers check thy vows austere, Borne in my car will I attend, All danger and all care to end. For thy dear sake I love the skill That guides the steed and curbs his will: And soon a forest life will be As pleasant, for my love of thee. And if these horses near thee dwell, And serve thee in the forest well, They, for their service, will not miss The due reward of highest bliss. Thine orders, as with thee I stray, Will I with heart and head obey, Prepared, for thee, without a sigh, To lose Ayodhyá or the sky. As one defiled with hideous sin, I never more can pass within Ayodhyá, city of our king, Unless beside me thee I bring. One wish is mine, I ask no more, That, when thy banishment is o'er I in my car may bear my lord,
- **Translation**: 

---

### Verse 19 (Ramayan 0.559)
- **Original**: Canto LII. The Crossing Of Gangá. 541 Triumphant, to his home restored. The fourteen years, if spent with thee, Will swift as light-winged moments flee; But the same years, without thee told, Were magnified a hundred-fold. Do not, kind lord, thy servant leave, Who to his master's son would cleave, And the same path with him pursue, Devoted, tender, just and true.” Again, again Sumantra made His varied plaint, and wept and prayed. Him Raghu's son, whose tender breast Felt for his servants, thus addressed: “O faithful servant, well my heart Knows how attached and true thou art. Hear thou the words I speak, and know Why to the town I bid thee go. Soon as Kaikeyí, youngest queen, Thy coming to the town has seen, No doubt will then her mind oppress That Ráma roams the wilderness. And so the dame, her heart content With proof of Ráma's banishment, Will doubt the virtuous king no more As faithless to the oath he swore. Chief of my cares is this, that she, Youngest amid the queens, may see Bharat her son securely reign O'er rich Ayodhyá's wide domain. For mine and for the monarch's sake Do thou thy journey homeward take, And, as I bade, repeat each word That from my lips thou here hast heard.”
- **Translation**: 

---

### Verse 20 (Ramayan 0.560)
- **Original**: 542 The Ramayana Thus spake the prince, and strove to cheer The sad heart of the charioteer, And then to royal Guha said These words most wise and spirited: “Guha, dear friend, it is not meet That people throng my calm retreat: For I must live a strict recluse, And mould my life by hermits' use. I now the ancient rule accept By good ascetics gladly kept. I go: bring fig-tree juice that I In matted coils my hair may tie.” Quick Guha hastened to produce, For the king's son, that sacred juice. Then Ráma of his long locks made, And Lakshma G's too, the hermit braid.[156] And the two royal brothers there With coats of bark and matted hair, Transformed in lovely likeness stood To hermit saints who love the wood. So Ráma, with his brother bold, A pious anchorite enrolled, Obeyed the vow which hermits take, And to his friend, King Guha, spake: “May people, treasure, army share, And fenced forts, thy constant care: Attend to all: supremely hard The sovereign's task, to watch and guard.”
- **Translation**: 

---



--- End of Ramayan_batch_28.md ---


--- Start of Ramayan_batch_29.md ---

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

### Verse 1 (Ramayan 0.561)
- **Original**: Canto LII. The Crossing Of Gangá. 543 Ikshváku's son, the good and brave, This last farewell to Guha gave, And then, with LakshmaG and his bride, Determined, on his way he hied. Soon as he viewed, upon the shore, The bark prepared to waft them o'er Impetuous Gangá's rolling tide, To LakshmaG thus the chieftain cried: “Brother, embark; thy hand extend, Thy gentle aid to Sítá lend: With care her trembling footsteps guide, And place the lady by thy side.” When Lakshma G heard, prepared to aid, His brother's words he swift obeyed. Within the bark he placed the dame, Then to her side the hero came. Next LakshmaG's elder brother, lord Of brightest glory, when on board, Breathing a prayer for blessings, meet For priest or warrior to repeat, Then he and car-borne LakshmaG bent, Well-pleased, their heads, most reverent, Their hands, with Sítá, having dipped, As Scripture bids, and water sipped, Farewell to wise Sumantra said, And Guha, with the train he led. So Ráma took, on board, his stand, And urged the vessel from the land. Then swift by vigorous arms impelled Her onward course the vessel held, And guided by the helmsman through The dashing waves of Gangá flew. Half way across the flood they came, When Sítá, free from spot and blame,
- **Translation**: 

---

### Verse 2 (Ramayan 0.562)
- **Original**: 544 The Ramayana Her reverent hands together pressed, The Goddess of the stream addressed: “May the great chieftain here who springs From Da[aratha, best of kings, Protected by thy care, fulfil His prudent father's royal will. When in the forest he has spent His fourteen years of banishment, With his dear brother and with me His home again my lord shall see. Returning on that blissful day, I will to thee mine offerings pay, Dear Queen, whose waters gently flow, Who canst all blessed gifts bestow. For, three-pathed Queen, though wandering here, Thy waves descend from Brahmá's sphere, Spouse of the God o'er floods supreme, Though rolling here thy glorious stream. To thee, fair Queen, my head shall bend, To thee shall hymns of praise ascend, When my brave lord shall turn again, And, joyful, o'er his kingdom reign. To win thy grace, O Queen divine, A hundred thousand fairest kine, And precious robes and finest meal Among the Bráhmans will I deal. A hundred jars of wine shall flow, When to my home, O Queen, I go; With these, and flesh, and corn, and rice, Will I, delighted, sacrifice. Each hallowed spot, each holy shrine That stands on these fair shores of thine, Each fane and altar on thy banks Shall share my offerings and thanks.
- **Translation**: 

---

### Verse 3 (Ramayan 0.563)
- **Original**: Canto LII. The Crossing Of Gangá. 545 With me and LakshmaG, free from harm, May he the blameless, strong of arm, Reseek Ayodhyá from the wild, O blameless Lady undefiled!” As, praying for her husband's sake, The faultless dame to Gangá spake, To the right bank the vessel flew With her whose heart was right and true. Soon as the bark had crossed the wave, The lion leader of the brave, Leaving the vessel on the strand, With wife and brother leapt to land. Then Ráma thus the prince addressed Who filled with joy Sumitrá's breast: “Be thine alike to guard and aid In peopled spot, in lonely shade. Do thou, Sumitrá's son, precede: Let Sítá walk where thou shalt lead. Behind you both my place shall be, To guard the Maithil dame and thee. For she, to woe a stranger yet, No toil or grief till now has met; The fair Videhan will assay The pains of forest life to-day. To-day her tender feet must tread Rough rocky wilds around her spread: No tilth is there, no gardens grow, No crowding people come and go.”
- **Translation**: 

---

### Verse 4 (Ramayan 0.564)
- **Original**: 546 The Ramayana The hero ceased: and LakshmaG led Obedient to the words he said: And Sítá followed him, and then Came Raghu's pride, the lord of men. With Sítá walking o'er the sand They sought the forest, bow in hand, But still their lingering glances threw Where yet Sumantra stood in view. Sumantra, when his watchful eye The royal youths no more could spy, Turned from the spot whereon he stood Homeward with Guha from the wood.[157] Still on the brothers forced their way Where sweet birds sang on every spray, Though scarce the eye a path could find Mid flowering trees where creepers twined. Far on the princely brothers pressed, And stayed their feet at length to rest Beneath a fig tree's mighty shade With countless pendent shoots displayed. Reclining there a while at ease, They saw, not far, beneath fair trees A lake with many a lotus bright That bore the name of Lovely Sight. Ráma his wife's attention drew, And Lakshma G's, to the charming view: “Look, brother, look how fair the flood Glows with the lotus, flower and bud!” They drank the water fresh and clear, And with their shafts they slew a deer. A fire of boughs they made in haste, And in the flame the meat they placed. So Raghu's sons with Sítá shared
- **Translation**: 

---

### Verse 5 (Ramayan 0.565)
- **Original**: Canto LIII. Ráma's Lament. 547 The hunter's meal their hands prepared, Then counselled that the spreading tree Their shelter and their home should be. Canto LIII. Ráma's Lament. When evening rites were duly paid, Reclined beneath the leafy shade, To LakshmaG thus spake Ráma, best Of those who glad a people's breast: “Now the first night has closed the day That saw us from our country stray, And parted from the charioteer; Yet grieve not thou, my brother dear. Henceforth by night, when others sleep, Must we our careful vigil keep, Watching for Sítá's welfare thus, For her dear life depends on us. Bring me the leaves that lie around, And spread them here upon the ground, That we on lowly beds may lie, And let in talk the night go by.”
- **Translation**: 

---

### Verse 6 (Ramayan 0.566)
- **Original**: 548 The Ramayana So on the ground with leaves o'erspread, He who should press a royal bed, Ráma with LakshmaG thus conversed, And many a pleasant tale rehearsed: “This night the king,” he cried,“alas! In broken sleep will sadly pass. Kaikeyí now content should be, For mistress of her wish is she. So fiercely she for empire yearns, That when her Bharat home returns, She in her greed, may even bring Destruction on our lord the king. What can he do, in feeble eld, Reft of all aid and me expelled, His soul enslaved by love, a thrall Obedient to Kaikeyí's call? As thus I muse upon his woe And all his wisdoms overthrow, Love is, methinks, of greater might To stir the heart than gain and right. For who, in wisdom's lore untaught, Could by a beauty's prayer be bought To quit his own obedient son, Who loves him, as my sire has done! Bharat, Kaikeyí's child, alone Will, with his wife, enjoy the throne, And blissfully his rule maintain O'er happy Ko[ala's domain. To Bharat's single lot will fall The kingdom and the power and all, When fails the king from length of days, And Ráma in the forest strays. Whoe'er, neglecting right and gain, Lets conquering love his soul enchain,
- **Translation**: 

---

### Verse 7 (Ramayan 0.567)
- **Original**: Canto LIII. Ráma's Lament. 549 To him, like Da[aratha's lot, Comes woe with feet that tarry not. Methinks at last the royal dame, Dear LakshmaG, has secured her aim, To see at once her husband dead, Her son enthroned, and Ráma fled. Ah me! I fear, lest borne away By frenzy of success, she slay Kau [alyá, through her wicked hate Of me, bereft, disconsolate; Or her who aye for me has striven Sumitrá, to devotion given. Hence, LakshmaG, to Ayodhyá speed, Returning in the hour of need. With Sítá I my steps will bend Where DaG ak's mighty woods extend. No guardian has Kau[alyá now: O, be her friend and guardian thou. Strong hate may vile Kaikeyí lead To many a base unrighteous deed, Treading my mother 'neath her feet When Bharat holds the royal seat. Sure in some antenatal time Were children, by Kau[alyá's crime, Torn from their mothers' arms away, And hence she mourns this evil day. She for her child no toil would spare Tending me long with pain and care; Now in the hour of fruitage she Has lost that son, ah, woe is me. O Lakshma G, may no matron e'er A son so doomed to sorrow bear As I, my mother's heart who rend With anguish that can never end.
- **Translation**: 

---

### Verse 8 (Ramayan 0.568)
- **Original**: 550 The Ramayana The Sáriká,325 methinks, possessed More love than glows in Ráma's breast. Who, as the tale is told to us, Addressed the stricken parrot thus:[158] “Parrot, the capturer's talons tear, While yet alone thou flutterest there, Before his mouth has closed on me:” So cried the bird, herself to free. Reft of her son, in childless woe, My mother's tears for ever flow: Ill-fated, doomed with grief to strive, What aid can she from me derive? Pressed down by care, she cannot rise From sorrow's flood wherein she lies. In righteous wrath my single arm Could, with my bow, protect from harm Ayodhyá's town and all the earth: But what is hero prowess worth? Lest breaking duty's law I sin, And lose the heaven I strive to win, The forest life today I choose, And kingly state and power refuse.” Thus mourning in that lonely spot The troubled chief bewailed his lot, And filled with tears, his eyes ran o'er; Then silent sat, and spake no more. To him, when ceased his loud lament, Like fire whose brilliant might is spent, Or the great sea when sleeps the wave, Thus LakshmaG consolation gave: “Chief of the brave who bear the bow, E'en now Ayodhyá, sunk in woe, 325 The Mainá or Gracula religiosa, a favourite cage-bird, easily taught to talk.
- **Translation**: 

---

### Verse 9 (Ramayan 0.569)
- **Original**: Canto LIV. Bharadvája's Hermitage. 551 By thy departure reft of light Is gloomy as the moonless night. Unfit it seems that thou, O chief, Shouldst so afflict thy soul with grief, So with thou Sítá's heart consign To deep despair as well as mine. Not I, O Raghu's son, nor she Could live one hour deprived of thee: We were, without thine arm to save, Like fish deserted by the wave. Although my mother dear to meet, Zatrughna, and the king, were sweet, On them, or heaven, to feed mine eye Were nothing, if thou wert not by.” Sitting at ease, their glances fell Upon the beds, constructed well, And there the sons of virtue laid Their limbs beneath the fig tree's shade. Canto LIV. Bharadvája's Hermitage. So there that night the heroes spent Under the boughs that o'er them bent, And when the sun his glory spread, Upstarting, from the place they sped. On to that spot they made their way, Through the dense wood that round them lay, Where Yamuná's326 swift waters glide To blend with Gangá's holy tide. 326 The Jumna.
- **Translation**: 

---

### Verse 10 (Ramayan 0.570)
- **Original**: 552 The Ramayana Charmed with the prospect ever new The glorious heroes wandered through Full many a spot of pleasant ground, Rejoicing as they gazed around, With eager eye and heart at ease, On countless sorts of flowery trees. And now the day was half-way sped When thus to LakshmaG Ráma said: “There, there, dear brother, turn thine eyes; See near Prayág327 that smoke arise: The banner of our Lord of Flames The dwelling of some saint proclaims. Near to the place our steps we bend Where Yamuná and Gangá blend. I hear and mark the deafening roar When chafing floods together pour. See, near us on the ground are left Dry logs, by labouring woodmen cleft, And the tall trees, that blossom near Saint Bharadvája's home, appear.” The bow-armed princes onward passed, And as the sun was sinking fast They reached the hermit's dwelling, set Near where the rushing waters met. The presence of the warrior scared The deer and birds as on he fared, And struck them with unwonted awe: Then Bharadvája's cot they saw. The high-souled hermit soon they found Girt by his dear disciples round: Calm saint, whose vows had well been wrought, Whose fervent rites keen sight had bought. 327 The Hindu name of Allahabad.
- **Translation**: 

---

### Verse 11 (Ramayan 0.571)
- **Original**: Canto LIV. Bharadvája's Hermitage. 553 Duly had flames of worship blazed When Ráma on the hermit gazed: His suppliant hands the hero raised, Drew nearer to the holy man With his companions, and began, Declaring both his name and race And why they sought that distant place: “Saint, Da[aratha's children we, Ráma and LakshmaG, come to thee. This my good wife from Janak springs, The best of fair Videha's kings; Through lonely wilds, a faultless dame, To this pure grove with me she came. My younger brother follows still Me banished by my father's will: Sumitrá's son, bound by a vow,— He roams the wood beside me now. Sent by my father forth to rove, We seek, O Saint, some holy grove, Where lives of hermits we may lead, And upon fruits and berries feed.” When Bharadvája, prudent-souled, Had heard the prince his tale unfold, Water he bade them bring, a bull, And honour-gifts in dishes full, [159] And drink and food of varied taste, Berries and roots, before him placed, And then the great ascetic showed A cottage for the guests' abode. The saint these honours gladly paid To Ráma who had thither strayed, Then compassed sat by birds and deer And many a hermit resting near.
- **Translation**: 

---

### Verse 12 (Ramayan 0.572)
- **Original**: 554 The Ramayana The prince received the service kind, And sat him down rejoiced in mind. Then Bharadvája silence broke, And thus the words of duty spoke: “Kakutstha's royal son, that thou Hadst sought this grove I knew ere now. Mine ears have heard thy story, sent Without a sin to banishment. Behold, O Prince, this ample space Near where the mingling floods embrace, Holy, and beautiful, and clear: Dwell with us, and be happy here.” By Bharadvája thus addressed, Ráma whose kind and tender breast All living things would bless and save, In gracious words his answer gave: “My honoured lord, this tranquil spot, Fair home of hermits, suits me not: For all the neighbouring people here Will seek us when they know me near: With eager wish to look on me, And the Videhan dame to see, A crowd of rustics will intrude Upon the holy solitude. Provide, O gracious lord, I pray, Some quiet home that lies away, Where my Videhan spouse may dwell Tasting the bliss deserved so well.”
- **Translation**: 

---

### Verse 13 (Ramayan 0.573)
- **Original**: Canto LIV. Bharadvája's Hermitage. 555 The hermit heard the prayer he made: A while in earnest thought he stayed, And then in words like these expressed His answer to the chief's request: “Ten leagues away there stands a hill Where thou mayst live, if such thy will: A holy mount, exceeding fair; Great saints have made their dwelling there: There great Langúrs328 in thousands play, And bears amid the thickets stray; Wide-known by Chitrakúma's name, It rivals Gandhamádan's329 fame. Long as the man that hill who seeks Gazes upon its sacred peaks, To holy things his soul he gives And pure from thought of evil lives. There, while a hundred autumns fled, Has many a saint with hoary head Spent his pure life, and won the prize, By deep devotion, in the skies: Best home, I ween, if such retreat, Far from the ways of men, be sweet: Or let thy years of exile flee Here in this hermitage with me.” Thus Bharadvája spake, and trained In lore of duty, entertained The princes and the dame, and pressed His friendly gifts on every guest. 328 The Langúr is a large monkey. 329 A mountain said to lie to the east of Meru.
- **Translation**: 

---

### Verse 14 (Ramayan 0.574)
- **Original**: 556 The Ramayana Thus to Prayág the hero went, Thus saw the saint preëminent, And varied speeches heard and said: Then holy night o'er heaven was spread. And Ráma took, by toil oppressed, With Sítá and his brother, rest; And so the night, with sweet content, In Bharadvája's grove was spent. But when the dawn dispelled the night, Ráma approached the anchorite, And thus addressed the holy sire Whose glory shone like kindled fire: “Well have we spent, O truthful Sage, The night within thy hermitage: Now let my lord his guests permit For their new home his grove to quit.” Then, as he saw the morning break, In answer Bharadvája spake: “Go forth to Chitrakúma's hill, Where berries grow, and sweets distil: Full well, I deem, that home will suit Thee, Ráma, strong and resolute. Go forth, and Chitrakúma seek, Famed mountain of the Varied Peak. In the wild woods that gird him round All creatures of the chase are found: Thou in the glades shalt see appear Vast herds of elephants and deer. With Sítá there shalt thou delight To gaze upon the woody height; There with expanding heart to look On river, table-land, and brook, And see the foaming torrent rave
- **Translation**: 

---

### Verse 15 (Ramayan 0.575)
- **Original**: Canto LV. The Passage Of Yamuná. 557 Impetuous from the mountain cave. Auspicious hill! where all day long The lapwing's cry, the Koïl's song Make all who listen gay: Where all is fresh and fair to see, Where elephants and deer roam free, There, as a hermit, stay.” Canto LV. The Passage Of Yamuná. The princely tamers of their foes Thus passed the night in calm repose, Then to the hermit having bent With reverence, on their way they went. High favour Bharadvája showed, And blessed them ready for the road. [160] With such fond looks as fathers throw On their own sons, before they go. Then spake the saint with glory bright To Ráma peerless in his might: “First, lords of men, direct your feet Where Yamuná and Gangá meet; Then to the swift Kálindí330 go, Whose westward waves to Gangá flow. When thou shalt see her lovely shore Worn by their feet who hasten o'er, Then, Raghu's son, a raft prepare, And cross the Sun born river there. Upon her farther bank a tree, 330 Another name of the Jumna, daughter of the Sun.
- **Translation**: 

---

### Verse 16 (Ramayan 0.576)
- **Original**: 558 The Ramayana Near to the landing wilt thou see. The blessed source of varied gifts, There her green boughs that Fig-tree lifts: A tree where countless birds abide, By Zyáma's name known far and wide. Sítá, revere that holy shade: There be thy prayers for blessing prayed. Thence for a league your way pursue, And a dark wood shall meet your view, Where tall bamboos their foliage show, The Gum-tree and the Jujube grow. To Chitrakúma have I oft Trodden that path so smooth and soft, Where burning woods no traveller scare, But all is pleasant, green, and fair.” When thus the guests their road had learned, Back to his cot the hermit turned, And Ráma, LakshmaG, Sítá paid Their reverent thanks for courteous aid. Thus Ráma spake to LakshmaG, when The saint had left the lords of men: “Great store of bliss in sooth is ours On whom his love the hermit showers.” As each to other wisely talked, The lion lords together walked On to Kálindí's woody shore; And gentle Sítá went before. They reached that flood, whose waters flee With rapid current to the sea; Their minds a while to thought they gave And counselled how to cross the wave. At length, with logs together laid, A mighty raft the brothers made.
- **Translation**: 

---

### Verse 17 (Ramayan 0.577)
- **Original**: Canto LV. The Passage Of Yamuná. 559 Then dry bamboos across were tied, And grass was spread from side to side. And the great hero LakshmaG brought Cane and Rose-Apple boughs and wrought, Trimming the branches smooth and neat, For Sítá's use a pleasant seat. And Ráma placed thereon his dame Touched with a momentary shame, Resembling in her glorious mien All-thought-surpassing Fortune's Queen. Then Ráma hastened to dispose, Each in its place, the skins and bows, And by the fair Videhan laid The coats, the ornaments, and spade. When Sítá thus was set on board, And all their gear was duly stored, The heroes each with vigorous hand, Pushed off the raft and left the land. When half its way the raft had made, Thus Sítá to Kálindí prayed: “Goddess, whose flood I traverse now, Grant that my lord may keep his vow. For thee shall bleed a thousand kine, A hundred jars shall pour their wine, When Ráma sees that town again Where old Ikshváku's children reign.” Thus to Kálindí's stream she sued And prayed in suppliant attitude. Then to the river's bank the dame, Fervent in supplication, came. They left the raft that brought them o'er, And the thick wood that clothed the shore, And to the Fig-treeZyáma made
- **Translation**: 

---

### Verse 18 (Ramayan 0.578)
- **Original**: 560 The Ramayana Their way, so cool with verdant shade. Then Sítá viewed that best of trees, And reverent spake in words like these: “Hail, hail, O mighty tree! Allow My husband to complete his vow; Let us returning, I entreat, Kau [alyá and Sumitrá meet.” Then with her hands together placed Around the tree she duly paced. When Ráma saw his blameless spouse A suppliant under holy boughs, The gentle darling of his heart, He thus to LakshmaG spake apart: “Brother, by thee our way be led; Let Sítá close behind thee tread: I, best of men, will grasp my bow, And hindmost of the three will go. What fruits soe'er her fancy take, Or flowers half hidden in the brake, For Janak's child forget not thou To gather from the brake or bough.” Thus on they fared. The tender dame Asked Ráma, as they walked, the name Of every shrub that blossoms bore, Creeper, and tree unseen before: And Lakshma G fetched, at Sítá's prayer, Boughs of each tree with clusters fair. Then Janak's daughter joyed to see The sand-discoloured river flee, Where the glad cry of many a bird, The sáras and the swan, was heard. A league the brothers travelled through The forest noble game they slew:
- **Translation**: 

---

### Verse 19 (Ramayan 0.579)
- **Original**: Canto LVI. Chitrakúta 561 Beneath the trees their meal they dressed And sat them down to eat and rest. A while in that delightful shade Where elephants unnumbered strayed, Where peacocks screamed and monkeys played, [161] They wandered with delight. Then by the river's side they found A pleasant spot of level ground, Where all was smooth and fair around, Their lodging for the night. Canto LVI. Chitrakúta Then Ráma, when the morning rose, Called LakshmaG gently from repose: “Awake, the pleasant voices hear Of forest birds that warble near. Scourge of thy foes, no longer stay; The hour is come to speed away.”
- **Translation**: 

---

### Verse 20 (Ramayan 0.580)
- **Original**: 562 The Ramayana The slumbering prince unclosed his eyes When thus his brother bade him rise, Compelling, at the timely cry, Fatigue, and sleep, and rest to fly. The brothers rose and Sítá too; Pure water from the stream they drew, Paid morning rites, then followed still The road to Chitrakúma's hill. Then Ráma as he took the road With LakshmaG, while the morning, glowed, To the Videhan lady cried, Sítá the fair, the lotus-eyed: “Look round thee, dear; each flowery tree Touched with the fire of morning see: The Kin[uk, now the Frosts are fled,— How glorious with his wreaths of red! The Bel-trees see, so loved of men, Hanging their boughs in every glen. O'erburthened with their fruit and flowers: A plenteous store of food is ours. See, LakshmaG, in the leafy trees, Where'er they make their home. Down hangs, the work of labouring bees The ponderous honeycomb. In the fair wood before us spread The startled wild-cock cries: Hark, where the flowers are soft to tread, The peacock's voice replies. Where elephants are roaming free, And sweet birds' songs are loud, The glorious Chitrakúma see: His peaks are in the cloud. On fair smooth ground he stands displayed, Begirt by many a tree:
- **Translation**: 

---



--- End of Ramayan_batch_29.md ---


--- Start of Ramayan_batch_30.md ---

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

### Verse 1 (Ramayan 0.581)
- **Original**: Canto LVI. Chitrakúta 563 O brother, in that holy shade How happy shall we be!”331 Then Ráma, LakshmaG, Sítá, each Spoke raising suppliant hands this speech To him, in woodland dwelling met, Válmíki, ancient anchoret: “O Saint, this mountain takes the mind, With creepers, trees of every kind, With fruit and roots abounding thus, A pleasant life it offers us: Here for a while we fain would stay, And pass a season blithe and gay.” Then the great saint, in duty trained, With honour gladly entertained: He gave his guests a welcome fair, And bade them sit and rest them there, Ráma of mighty arm and chest His faithful LakshmaG then addressed: “Brother, bring hither from the wood Selected timber strong and good, And build therewith a little cot; My heart rejoices in the spot That lies beneath the mountain's side, Remote, with water well supplied.” 331 “We have often looked on that green hill: it is the holiest spot of that sect of the Hindu faith who devote themselves to this incarnation of VishGu. The whole neighbourhood is Ráma's country. Every headland has some legend, every cavern is connected with his name; some of the wild fruits are still calledSítáphal, being the reputed food of the exile. Thousands and thousands annually visit the spot, and round the hill is a raised foot-path, on which the devotee, with naked feet, treads full of pious awe.” Calcutta Review, Vol. XXIII.
- **Translation**: 

---

### Verse 2 (Ramayan 0.582)
- **Original**: 564 The Ramayana Sumitrá's son his words obeyed, Brought many a tree, and deftly made, With branches in the forest cut, As Ráma bade, a leafy hut. Then Ráma, when the cottage stood Fair, firmly built, and walled with wood, To LakshmaG spake, whose eager mind To do his brother's will inclined: “Now, LakshmaG as our cot is made, Must sacrifice be duly paid By us, for lengthened life who hope, With venison of the antelope. Away, O bright-eyed LakshmaG, speed: Struck by thy bow a deer must bleed: As Scripture bids, we must not slight The duty that commands the rite.” Lakshma G, the chief whose arrows laid His foemen low, his word obeyed; And Ráma thus again addressed The swift performer of his hest: “Prepare the venison thou hast shot, To sacrifice for this our cot. Haste, brother dear, for this the hour, And this the day of certain power.” Then glorious LakshmaG took the buck His arrow in the wood had struck; Bearing his mighty load he came, And laid it in the kindled flame.[162] Soon as he saw the meat was done, And that the juices ceased to run From the broiled carcass, LakshmaG then Spoke thus to Ráma best of men: “The carcass of the buck, entire,
- **Translation**: 

---

### Verse 3 (Ramayan 0.583)
- **Original**: Canto LVI. Chitrakúta 565 Is ready dressed upon the fire. Now be the sacred rites begun To please the God, thou godlike one.” Ráma the good, in ritual trained, Pure from the bath, with thoughts restrained, Hasted those verses to repeat Which make the sacrifice complete. The hosts celestial came in view, And Ráma to the cot withdrew, While a sweet sense of rapture stole Through the unequalled hero's soul. He paid the Vi[vedevas332 due. And Rudra's right, and VishGu's too, Nor wonted blessings, to protect Their new-built home, did he neglect. With voice repressed he breathed the prayer, Bathed duly in the river fair, And gave good offerings that remove The stain of sin, as texts approve. And many an altar there he made, And shrines, to suit the holy shade, All decked with woodland chaplets sweet, And fruit and roots and roasted meat, With muttered prayer, as texts require, Water, and grass and wood and fire. So Ráma, LakshmaG, Sítá paid Their offerings to each God and shade, And entered then their pleasant cot That bore fair signs of happy lot. They entered, the illustrious three, 332 Deities of a particular class in which five or ten are enumerated. They are worshipped particularly at the funeral obsequies in honour of deceased progenitors.
- **Translation**: 

---

### Verse 4 (Ramayan 0.584)
- **Original**: 566 The Ramayana The well-set cottage, fair to see, Roofed with the leaves of many a tree, And fenced from wind and rain: So, at their Father Brahmá's call, The Gods of heaven, assembling all, To their own glorious council hall Advance in shining train. So, resting on that lovely hill, Near the fair lily-covered rill, The happy prince forgot, Surrounded by the birds and deer, The woe, the longing, and the fear That gloom the exile's lot. Canto LVII. Sumantra's Return. When Ráma reached the southern bank, King Guha's heart with sorrow sank: He with Sumantra talked, and spent With his deep sorrow, homeward went. Sumantra, as the king decreed, Yoked to the car each noble steed, And to Ayodhyá's city sped With his sad heart disquieted. On lake and brook and scented grove His glances fell, as on he drove: City and village came in view As o'er the road his coursers flew. On the third day the charioteer, When now the hour of night was near, Came to Ayodhyá's gate, and found
- **Translation**: 

---

### Verse 5 (Ramayan 0.585)
- **Original**: Canto LVII. Sumantra's Return. 567 The city all in sorrow drowned. To him, in spirit quite cast down, Forsaken seemed the silent town, And by the rush of grief oppressed He pondered in his mournful breast: “Is all Ayodhyá burnt with grief, Steed, elephant, and man, and chief? Does her loved Ráma's exile so Afflict her with the fires of woe?” Thus as he mused, his steeds flew fast, And swiftly through the gate he passed. On drove the charioteer, and then In hundreds, yea in thousands, men Ran to the car from every side, And, “Ráma, where is Ráma?” cried. Sumantra said:“My chariot bore The duteous prince to Gangá's shore; I left him there at his behest, And homeward to Ayodhyá pressed.” Soon as the anxious people knew That he was o'er the flood they drew Deep sighs, and crying, Ráma! all Wailed, and big tears began to fall. He heard the mournful words prolonged, As here and there the people thronged: “Woe, woe for us, forlorn, undone, No more to look on Raghu's son! His like again we ne'er shall see, Of heart so true, of hand so free, In gifts, in gatherings for debate, When marriage pomps we celebrate, What should we do? What earthly thing Can rest, or hope, or pleasure bring?”
- **Translation**: 

---

### Verse 6 (Ramayan 0.586)
- **Original**: 568 The Ramayana Thus the sad town, which Ráma kept As a kind father, wailed and wept. Each mansion, as the car went by, Sent forth a loud and bitter cry, As to the window every dame, Mourning for banished Ráma, came. As his sad eyes with tears o'erflowed, He sped along the royal road To Da[aratha's high abode. There leaping down his car he stayed; Within the gates his way he made; Through seven broad courts he onward hied Where people thronged on every side. From each high terrace, wild with woe, The royal ladies flocked below:[163] He heard them talk in gentle tone, As each for Ráma made her moan: “What will the charioteer reply To Queen Kau[alyá's eager cry? With Ráma from the gates he went; Homeward alone, his steps are bent. Hard is a life with woe distressed, But difficult to win is rest, If, when her son is banished, still She lives beneath her load of ill.” Such was the speech Sumantra heard From them whom grief unfeigned had stirred. As fires of anguish burnt him through, Swift to the monarch's hall he drew, Past the eighth court; there met his sight, The sovereign in his palace bright, Still weeping for his son, forlorn, Pale, faint, and all with sorrow worn.
- **Translation**: 

---

### Verse 7 (Ramayan 0.587)
- **Original**: Canto LVII. Sumantra's Return. 569 As there he sat, Sumantra bent And did obeisance reverent, And to the king repeated o'er The message he from Ráma bore. The monarch heard, and well-nigh brake His heart, but yet no word he spake: Fainting to earth he fell, and dumb, By grief for Ráma overcome. Rang through the hall a startling cry, And women's arms were tossed on high, When, with his senses all astray, Upon the ground the monarch lay. Kau [alyá, with Sumitrá's aid, Raised from the ground her lord dismayed: “Sire, of high fate,” she cried,“O, why Dost thou no single word reply To Ráma's messenger who brings News of his painful wanderings? The great injustice done, art thou Shame-stricken for thy conduct now? Rise up, and do thy part: bestow Comfort and help in this our woe. Speak freely, King; dismiss thy fear, For Queen Kaikeyí stands not near, Afraid of whom thou wouldst not seek Tidings of Ráma: freely speak.” When the sad queen had ended so, She sank, insatiate in her woe, And prostrate lay upon the ground, While her faint voice by sobs was drowned. When all the ladies in despair Saw Queen Kau[alyá wailing there, And the poor king oppressed with pain,
- **Translation**: 

---

### Verse 8 (Ramayan 0.588)
- **Original**: 570 The Ramayana They flocked around and wept again. Canto LVIII. Ráma's Message. The king a while had senseless lain, When care brought memory back again. Then straight he called, the news to hear Of Ráma, for the charioteer, With reverent hand to hand applied He waited by the old man's side, Whose mind with anguish was distraught Like a great elephant newly caught. The king with bitter pain distressed The faithful charioteer addressed, Who, sad of mien, with flooded eye, And dust upon his limbs, stood by: “Where will be Ráma's dwelling now At some tree's foot, beneath the bough; Ah, what will be the exile's food, Bred up with kind solicitude? Can he, long lapped in pleasant rest, Unmeet for pain, by pain oppressed, Son of earth's king, his sad night spend Earth-couched, as one that has no friend? Behind him, when abroad he sped, Cars, elephant, and foot were led: Then how shall Ráma dwell afar In the wild woods where no men are? How, tell me, did the princes there, With Sítá good and soft and fair, Alighting from the chariot, tread
- **Translation**: 

---

### Verse 9 (Ramayan 0.589)
- **Original**: Canto LVIII. Ráma's Message. 571 The forest wilds around them spread? A happy lot is thine, I ween, Whose eyes my two dear sons have seen Seeking on foot the forest shade, Like the bright Twins to view displayed, The heavenly A[vins, when they seek The woods that hang 'neath Mandar's peak. What words, Sumantra, quickly tell, From Ráma, LakshmaG, Sítá fell? How in the wood did Ráma eat? What was his bed, and what his seat? Full answer to my questions give, For I on thy replies shall live, As with the saints Yayáti held Sweet converse, from the skies expelled.” Urged by the lord of men to speak, Whose sobbing voice came faint and weak, Thus he, while tears his utterance broke, In answer to the monarch spoke: “Hear then the words that Ráma said, Resolved in duty's path to tread. Joining his hands, his head he bent, And gave this message, reverent: “Sumantra, to my father go, Whose lofty mind all people know: Bow down before him, as is meet, And in my stead salute his feet. Then to the queen my mother bend, And give the greeting that I send: Ne'er may her steps from duty err, And may it still be well with her. And add this word:“O Queen, pursue Thy vows with faithful heart and true;
- **Translation**: 

---

### Verse 10 (Ramayan 0.590)
- **Original**: 572 The Ramayana And ever at due season turn Where holy fires of worship burn. And, lady, on our lord bestow[164] Such honour as to Gods we owe. Be kind to every queen: let pride And thought of self be cast aside. In the king's fond opinion raise Kaikeyí, by respect and praise. Let the young Bharat ever be Loved, honoured as the king by thee: Thy king-ward duty ne'er forget: High over all are monarchs set.” And Bharat, too, for me address: Pray that all health his life may bless. Let every royal lady share, As justice bids, his love and care. Say to the strong-armed chief who brings Joy to Iksváku's line of kings: “As ruling prince thy care be shown Of him, our sire, who holds the throne. Stricken in years he feels their weight; But leave him in his royal state. As regent heir content thee still, Submissive to thy father's will.’ ” Ráma again his charge renewed, As the hot flood his cheek bedewed: “Hold as thine own my mother dear Who drops for me the longing tear.” Then LakshmaG, with his soul on fire, Spake breathing fast these words of ire: “Say, for what sin, for what offence Was royal Ráma banished thence? He is the cause, the king: poor slave
- **Translation**: 

---

### Verse 11 (Ramayan 0.591)
- **Original**: Canto LVIII. Ráma's Message. 573 To the light charge Kaikeyí gave. Let right or wrong the motive be, The author of our woe is he. Whether the exile were decreed Through foolish faith or guilty greed, For promises or empire, still The king has wrought a grievous ill. Grant that the Lord of all saw fit To prompt the deed and sanction it, In Ráma's life no cause I see For which the king should bid him flee. His blinded eyes refused to scan The guilt and folly of the plan, And from the weakness of the king Here and hereafter woe shall spring. No more my sire: the ties that used To bind me to the king are loosed. My brother Ráma, Raghu's son, To me is lord, friend, sire in one. The love of men how can he win, Deserting, by the cruel sin, Their joy, whose heart is swift to feel A pleasure in the people's weal? Shall he whose mandate could expel The virtuous Ráma, loved so well, To whom his subjects' fond hearts cling— Shall he in spite of them be king?” But Janak's child, my lord, stood by, And oft the votaress heaved a sigh. She seemed with dull and wandering sense, Beneath a spirit's influence. The noble princess, pained with woe Which till that hour she ne'er could know,
- **Translation**: 

---

### Verse 12 (Ramayan 0.592)
- **Original**: 574 The Ramayana Tears in her heavy trouble shed, But not a word to me she said. She raised her face which grief had dried And tenderly her husband eyed, Gazed on him as he turned to go While tear chased tear in rapid flow.” Canto LIX. Dasaratha's Lament. As thus Sumantra, best of peers, Told his sad tale with many tears, The monarch cried,“I pray thee, tell At length again what there befell.” Sumantra, at the king's behest, Striving with sobs he scarce repressed, His trembling voice at last controlled, And thus his further tidings told: “Their locks in votive coils they wound, Their coats of bark upon them bound, To Gangá's farther shore they went, Thence to Prayág their steps were bent. I saw that LakshmaG walked ahead To guard the path the two should tread. So far I saw, no more could learn, Forced by the hero to return. Retracing slow my homeward course, Scarce could I move each stubborn horse: Shedding hot tears of grief he stood
- **Translation**: 

---

### Verse 13 (Ramayan 0.593)
- **Original**: Canto LIX. Dasaratha's Lament. 575 When Ráma turned him to the wood.333 As the two princes parted thence I raised my hands in reverence, Mounted my ready car, and bore The grief that stung me to the core. With Guha all that day I stayed, Still by the earnest hope delayed That Ráma, ere the time should end, Some message from the wood might send. Thy realms, great Monarch, mourn the blow, And sympathize with Ráma's woe. [165] Each withering tree hangs low his head, And shoot, and bud, and flower are dead. Dried are the floods that wont to fill The lake, the river, and the rill. Drear is each grove and garden now, Dry every blossom on the bough. Each beast is still, no serpents crawl: A lethargy of woe on all. The very wood is silent: crushed With grief for Ráma, all is hushed. Fair blossoms from the water born, Gay garlands that the earth adorn, And every fruit that gleams like gold, Have lost the scent that charmed of old. Empty is every grove I see, 333 “So in Homer the horses of Achilles lamented with many bitter tears the death of Patroclus slain by Hector:” “=ÀÀ¿¹ ´'0±ºw´±¿,¼qÇ·Â Àq½µÅ¸µ½ yÄµÂ, »¶¹¿½,Àµ¹´t ÀÁöÄ± ÀÅ¸sÃ¸·½ !½¹yÇ¿¹¿ ½ º¿½w½Ã¹ ÀµÃy½Ä¿Â QÆ' ºÄ¿Á¿Â ½´Á¿Æy½¿¹¿” ILIAD .{FNS XVII. 426. “Ancient poesy frequently associated nature with the joys and sorrows of man.” G ORRESIO .{FNS
- **Translation**: 

---

### Verse 14 (Ramayan 0.594)
- **Original**: 576 The Ramayana Or birds sit pensive on the tree. Where'er I look, its beauty o'er, The pleasance charms not as before. I drove through fair Ayodhyá's street: None flew with joy the car to meet. They saw that Ráma was not there, And turned them sighing in despair. The people in the royal way Wept tears of bitter grief, when they Beheld me coming, from afar, No Ráma with me in the car. From palace roof and turret high Each woman bent her eager eye; She looked for Ráma, but in vain; Gazed on the car and shrieked for pain. Their long clear eyes with sorrow drowned They, when this common grief was found, Looked each on other, friend and foe, In sympathy of levelling woe: No shade of difference between Foe, friend, or neutral, there was seen. Without a joy, her bosom rent With grief for Ráma's banishment, Ayodhyá like the queen appears Who mourns her son with many tears.”
- **Translation**: 

---

### Verse 15 (Ramayan 0.595)
- **Original**: Canto LIX. Dasaratha's Lament. 577 He ended: and the king, distressed. With sobbing voice that lord addressed: “Ah me, by false Kaikeyí led, Of evil race, to evil bred, I took no counsel of the sage, Nor sought advice from skill and age, I asked no lord his aid to lend, I called no citizen or friend. Rash was my deed, bereft of sense Slave to a woman's influence. Surely, my lord, a woe so great Falls on us by the will of Fate; It lays the house of Raghu low, For Destiny will have it so. I pray thee, if I e'er have done An act to please thee, yea, but one, Fly, fly, and Ráma homeward lead: My life, departing, counsels speed. Fly, ere the power to bid I lack, Fly to the wood: bring Ráma back. I cannot live for even one Short hour bereaved of my son. But ah, the prince, whose arms are strong, Has journeyed far: the way is long: Me, me upon the chariot place, And let me look on Ráma's face. Ah me, my son, mine eldest-born, Where roams he in the wood forlorn, The wielder of the mighty bow, Whose shoulders like the lion's show? O, ere the light of life be dim, Take me to Sítá and to him. O Ráma, LakshmaG, and O thou Dear Sítá, constant to thy vow,
- **Translation**: 

---

### Verse 16 (Ramayan 0.596)
- **Original**: 578 The Ramayana Beloved ones, you cannot know That I am dying of my woe.” The king to bitter grief a prey, That drove each wandering sense away, Sunk in affliction's sea, too wide To traverse, in his anguish cried: “Hard, hard to pass, my Queen, this sea Of sorrow raging over me: No Ráma near to soothe mine eye, Plunged in its lowest deeps I lie. Sorrow for Ráma swells the tide, And Sítá's absence makes it wide: My tears its foamy flood distain, Made billowy by my sighs of pain: My cries its roar, the arms I throw About me are the fish below, Kaikeyí is the fire that feeds Beneath: my hair the tangled weeds: Its source the tears for Ráma shed: The hump-back's words its monsters dread: The boon I gave the wretch its shore, Till Ráma's banishment be o'er.334 Ah me, that I should long to set My eager eyes to-day On Raghu's son, and he be yet With LakshmaG far away!” Thus he of lofty glory wailed, And sank upon the bed. Beneath the woe his spirit failed, And all his senses fled. 334 The lines containing this heap of forced metaphors are marked as spurious by Schlegel.
- **Translation**: 

---

### Verse 17 (Ramayan 0.597)
- **Original**: Canto LX. Kausalyá Consoled. 579 Canto LX. Kausalyá Consoled. As Queen Kau[alyá, trembling much, As blighted by a goblin's touch, Still lying prostrate, half awoke To consciousness, 'twas thus she spoke: “Bear me away, Sumantra, far, Where Ráma, Sítá, LakshmaG are. Bereft of them I have no power To linger on a single hour. [166] Again, I pray, thy steps retrace, And me in DaG ak forest place, For after them I needs must go, Or sink to Yama's realms below.” His utterance choked by tears that rolled Down from their fountains uncontrolled, With suppliant hands the charioteer Thus spake, the lady's heart to cheer: “Dismiss thy grief, despair, and dread That fills thy soul, of sorrow bred, For pain and anguish thrown aside, Will Ráma in the wood abide. And Lakshma G, with unfailing care Will guard the feet of Ráma there, Earning, with governed sense, the prize That waits on duty in the skies. And Sítá in the wild as well As in her own dear home will dwell; To Ráma all her heart she gives, And free from doubt and terror lives. No faintest sign of care or woe The features of the lady show: Methinks Videha's pride was made
- **Translation**: 

---

### Verse 18 (Ramayan 0.598)
- **Original**: 580 The Ramayana For exile in the forest shade. E'en as of old she used to rove Delighted in the city's grove, Thus, even thus she joys to tread The woodlands uninhabited. Like a young child, her face as fair As the young moon, she wanders there. What though in lonely woods she stray Still Ráma is her joy and stay: All his the heart no sorrow bends, Her very life on him depends. For, if her lord she might not see, Ayodhyá like the wood would be. She bids him, as she roams, declare The names of towns and hamlets there, Marks various trees that meet her eye, And many a brook that hurries by, And Janak's daughter seems to roam One little league away from home When Ráma or his brother speaks And gives the answer that she seeks. This, Lady, I remember well, Nor angry words have I to tell: Reproaches at Kaikeyí shot, Such, Queen, my mind remembers not.” The speech when Sítá's wrath was high, Sumantra passed in silence by, That so his pleasant words might cheer With sweet report Kau[alyá's ear. “Her moonlike beauty suffers not Though winds be rude and suns be hot: The way, the danger, and the toil Her gentle lustre may not soil. Like the red lily's leafy crown
- **Translation**: 

---

### Verse 19 (Ramayan 0.599)
- **Original**: Canto LX. Kausalyá Consoled. 581 Or as the fair full moon looks down, So the Videhan lady's face Still shines with undiminished grace. What if the borrowed colours throw O'er her fine feet no rosy glow, Still with their natural tints they spread A lotus glory where they tread. In sportive grace she walks the ground And sweet her chiming anklets sound. No jewels clasp the faultless limb: She leaves them all for love of him. If in the woods her gentle eye A lion sees, or tiger nigh, Or elephant, she fears no ill For Ráma's arm supports her still. No longer be their fate deplored, Nor thine, nor that of Ko[al's lord, For conduct such as theirs shall buy Wide glory that can never die. For casting grief and care away, Delighting in the forest, they With joyful spirits, blithe and gay, Set forward on the ancient way Where mighty saints have led: Their highest aim, their dearest care To keep their father's honour fair, Observing still the oath he sware, They roam, on wild fruit fed.” Thus with persuasive art he tried To turn her from her grief aside, By soothing fancies won. But still she gave her sorrow vent: “Ah Ráma,” was her shrill lament, “My love, my son, my son!”
- **Translation**: 

---

### Verse 20 (Ramayan 0.600)
- **Original**: 582 The Ramayana Canto LXI. Kausalyá's Lament. When, best of all who give delight, Her Ráma wandered far from sight, Kau [alyá weeping, sore distressed, The king her husband thus addressed: “Thy name, O Monarch, far and wide Through the three worlds is glorified: Yet Ráma's is the pitying mind, His speed is true, his heart is kind. How will thy sons, good lord, sustain With Sítá, all their care and pain? How in the wild endure distress, Nursed in the lap of tenderness? How will the dear Videhan bear The heat and cold when wandering there Bred in the bliss of princely state, So young and fair and delicate? The large-eyed lady, wont to eat The best of finely seasoned meat— How will she now her life sustain With woodland fare of self-sown grain? Will she, with joys encompassed long, Who loved the music and the song, In the wild wood endure to hear The ravening lion's voice of fear? Where sleeps my strong-armed hero, where,[167] Like Lord Mahendra's standard, fair? Where is, by LakshmaG's side, his bed, His club-like arm beneath his head? When shall I see his flower-like eyes, And face that with the lotus vies, Feel his sweet lily breath, and view His glorious hair and lotus hue?
- **Translation**: 

---



--- End of Ramayan_batch_30.md ---


--- Start of Ramayan_batch_31.md ---

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

### Verse 1 (Ramayan 0.601)
- **Original**: Canto LXI. Kausalyá's Lament. 583 The heart within my breast, I feel, Is adamant or hardest steel, Or, in a thousand fragments split, The loss of him had shattered it, When those I love, who should be blest, Are wandering in the wood distressed, Condemned their wretched lives to lead In exile, by thy ruthless deed. If, when the fourteen years are past, Ráma reseeks his home at last, I think not Bharat will consent To yield the wealth and government. At funeral feasts some mourners deal To kith and kin the solemn meal, And having duly fed them all Some Bráhmans to the banquet call. The best of Bráhmans, good and wise, The tardy summoning despise, And, equal to the Gods, disdain Cups, e'en of Amrit, thus to drain. Nay e'en when Bráhmans first have fed, They loathe the meal for others spread, And from the leavings turn with scorn, As bulls avoid a fractured horn. So Ráma, sovereign lord of men, Will spurn the sullied kingship then: He born the eldest and the best, His younger's leavings will detest, Turning from tasted food away, As tigers scorn another's prey. The sacred post is used not twice, Nor elements, in sacrifice. But once the sacred grass is spread, But once with oil the flame is fed:
- **Translation**: 

---

### Verse 2 (Ramayan 0.602)
- **Original**: 584 The Ramayana So Ráma's pride will ne'er receive The royal power which others leave, Like wine when tasteless dregs are left, Or rites of Soma juice bereft. Be sure the pride of Raghu's race Will never stoop to such disgrace: The lordly lion will not bear That man should beard him in his lair. Were all the worlds against him ranged His dauntless soul were still unchanged: He, dutiful, in duty strong, Would purge the impious world from wrong. Could not the hero, brave and bold, The archer, with his shafts of gold, Burn up the very seas, as doom Will in the end all life consume? Of lion's might, eyed like a bull, A prince so brave and beautiful, Thou hast with wicked hate pursued, Like sea-born tribes who eat their brood. If thou, O Monarch, hadst but known The duty all the Twice-born own, If the good laws had touched thy mind, Which sages in the Scriptures find, Thou ne'er hadst driven forth to pine This brave, this duteous son of thine. First on her lord the wife depends, Next on her son and last on friends: These three supports in life has she, And not a fourth for her may be. Thy heart, O King, I have not won; In wild woods roams my banished son; Far are my friends: ah, hapless me, Quite ruined and destroyed by thee.”
- **Translation**: 

---

### Verse 3 (Ramayan 0.603)
- **Original**: Canto LXII. Dasaratha Consoled. 585 Canto LXII. Dasaratha Consoled. The queen's stern speech the monarch heard, As rage and grief her bosom stirred, And by his anguish sore oppressed Reflected in his secret breast. Fainting and sad, with woe distraught, He wandered in a maze of thought; At length the queller of the foe Grew conscious, rallying from his woe. When consciousness returned anew Long burning sighs the monarch drew, Again immersed in thought he eyed Kau [alyá standing by his side. Back to his pondering soul was brought The direful deed his hand had wrought, When, guiltless of the wrong intent, His arrow at a sound was sent. Distracted by his memory's sting, And mourning for his son, the king To two consuming griefs a prey, A miserable victim lay. The double woe devoured him fast, As on the ground his eyes he cast, Joined suppliant hands, her heart to touch, And spake in the answer, trembling much: “Kau [alyá, for thy grace I sue, Joining these hands as suppliants do. Thou e'en to foes hast ever been A gentle, good, and loving queen. Her lord, with noble virtues graced, Her lord, by lack of all debased, Is still a God in woman's eyes, If duty's law she hold and prize.
- **Translation**: 

---

### Verse 4 (Ramayan 0.604)
- **Original**: 586 The Ramayana Thou, who the right hast aye pursued, Life's changes and its chances viewed, Shouldst never launch, though sorrow-stirred, At me distressed, one bitter word.” She listened, as with sorrow faint He murmured forth his sad complaint: Her brimming eyes with tears ran o'er, As spouts the new fallen water pour;[168] His suppliant hands, with fear dismayed She gently clasped in hers, and laid, Like a fair lotus, on her head, And faltering in her trouble said: “Forgive me; at thy feet I lie, With low bent head to thee I cry. By thee besought, thy guilty dame Pardon from thee can scarcely claim. She merits not the name of wife Who cherishes perpetual strife With her own husband good and wise, Her lord both here and in the skies. I know the claims of duty well, I know thy lips the truth must tell. All the wild words I rashly spoke, Forth from my heart, through anguish, broke; For sorrow bends the stoutest soul, And cancels Scripture's high control. Yea, sorrow's might all else o'erthrows The strongest and the worst of foes. 'Tis thus with all: we keenly feel, Yet bear the blows our foemen deal, But when a slender woe assails The manliest spirit bends and quails. The fifth long night has now begun
- **Translation**: 

---

### Verse 5 (Ramayan 0.605)
- **Original**: Canto LXIII. The Hermit's Son. 587 Since the wild woods have lodged my son: To me whose joy is drowned in tears, Each day a dreary year appears. While all my thoughts on him are set Grief at my heart swells wilder yet: With doubled might thus Ocean raves When rushing floods increase his waves.” As from Kau[alyá reasoning well The gentle words of wisdom fell, The sun went down with dying flame, And darkness o'er the landscape came. His lady's soothing words in part Relieved the monarch's aching heart, Who, wearied out by all his woes, Yielded to sleep and took repose. Canto LXIII. The Hermit's Son. But soon by rankling grief oppressed The king awoke from troubled rest, And his sad heart was tried again With anxious thought where all was pain. Ráma and LakshmaG's mournful fate On Da [aratha, good and great As Indra, pressed with crushing weight, As when the demon's might assails The Sun-God, and his glory pales. Ere yet the sixth long night was spent, Since Ráma to the woods was sent, The king at midnight sadly thought
- **Translation**: 

---

### Verse 6 (Ramayan 0.606)
- **Original**: 588 The Ramayana Of the old crime his hand had wrought, And thus to Queen Kau[alyá cried Who still for Ráma moaned and sighed: “If thou art waking, give, I pray, Attention to the words I say. Whate'er the conduct men pursue, Be good or ill the acts they do, Be sure, dear Queen, they find the meed Of wicked or of virtuous deed. A heedless child we call the man Whose feeble judgment fails to scan The weight of what his hands may do, Its lightness, fault, and merit too. One lays the Mango garden low, And bids the gay Palá[as grow: Longing for fruit their bloom he sees, But grieves when fruit should bend the trees. Cut by my hand, my fruit-trees fell, Palá[a trees I watered well. My hopes this foolish heart deceive, And for my banished son I grieve. Kau [alyá, in my youthful prime Armed with my bow I wrought the crime, Proud of my skill, my name renowned, An archer prince who shoots by sound. The deed this hand unwitting wrought This misery on my soul has brought, As children seize the deadly cup And blindly drink the poison up. As the unreasoning man may be Charmed with the gay Palá[a tree, I unaware have reaped the fruit Of joying at a sound to shoot. As regent prince I shared the throne,
- **Translation**: 

---

### Verse 7 (Ramayan 0.607)
- **Original**: Canto LXIII. The Hermit's Son. 589 Thou wast a maid to me unknown, The early Rain-time duly came, And strengthened love's delicious flame. The sun had drained the earth that lay All glowing 'neath the summer day, And to the gloomy clime had fled Where dwell the spirits of the dead.335 The fervent heat that moment ceased, The darkening clouds each hour increased And frogs and deer and peacocks all Rejoiced to see the torrents fall. Their bright wings heavy from the shower, The birds, new-bathed, had scarce the power To reach the branches of the trees Whose high tops swayed beneath the breeze. The fallen rain, and falling still, Hung like a sheet on every hill, Till, with glad deer, each flooded steep Showed glorious as the mighty deep. The torrents down its wooded side Poured, some unstained, while others dyed [169] Gold, ashy, silver, ochre, bore The tints of every mountain ore. In that sweet time, when all are pleased, My arrows and my bow I seized; Keen for the chase, in field or grove, Down Sarjú's bank my car I drove. I longed with all my lawless will Some elephant by night to kill, Some buffalo that came to drink, Or tiger, at the river's brink. When all around was dark and still, 335 The southern region is the abode of Yama the Indian Pluto, and of departed spirits.
- **Translation**: 

---

### Verse 8 (Ramayan 0.608)
- **Original**: 590 The Ramayana I heard a pitcher slowly fill, And thought, obscured in deepest shade, An elephant the sound had made. I drew a shaft that glittered bright, Fell as a serpent's venomed bite; I longed to lay the monster dead, And to the mark my arrow sped. Then in the calm of morning, clear A hermit's wailing smote my ear: “Ah me, ah me,” he cried, and sank, Pierced by my arrow, on the bank. E'en as the weapon smote his side, I heard a human voice that cried: “Why lights this shaft on one like me, A poor and harmless devotee? I came by night to fill my jar From this lone stream where no men are. Ah, who this deadly shaft has shot? Whom have I wronged, and knew it not? Why should a boy so harmless feel The vengeance of the winged steel? Or who should slay the guiltless son Of hermit sire who injures none, Who dwells retired in woods, and there Supports his life on woodland fare? Ah me, ah me, why am I slain, What booty will the murderer gain? In hermit coils I bind my hair, Coats made of skin and bark I wear. Ah, who the cruel deed can praise Whose idle toil no fruit repays, As impious as the wretch's crime Who dares his master's bed to climb? Nor does my parting spirit grieve
- **Translation**: 

---

### Verse 9 (Ramayan 0.609)
- **Original**: Canto LXIII. The Hermit's Son. 591 But for the life which thus I leave: Alas, my mother and my sire,— I mourn for them when I expire. Ah me, that aged, helpless pair, Long cherished by my watchful care, How will it be with them this day When to the Five336 I pass away? Pierced by the self-same dart we die, Mine aged mother, sire, and I. Whose mighty hand, whose lawless mind Has all the three to death consigned?” When I, by love of duty stirred, That touching lamentation heard, Pierced to the heart by sudden woe, I threw to earth my shafts and bow. My heart was full of grief and dread As swiftly to the place I sped, Where, by my arrow wounded sore, A hermit lay on Sarjú's shore. His matted hair was all unbound, His pitcher empty on the ground, And by the fatal arrow pained, He lay with dust and gore distained. I stood confounded and amazed: His dying eyes to mine he raised, And spoke this speech in accents stern, As though his light my soul would burn: “How have I wronged thee, King, that I Struck by thy mortal arrow die? The wood my home, this jar I brought, And water for my parents sought. This one keen shaft that strikes me through 336 The five elements of which the body consists, and to which it returns.
- **Translation**: 

---

### Verse 10 (Ramayan 0.610)
- **Original**: 592 The Ramayana Slays sire and aged mother too. Feeble and blind, in helpless pain, They wait for me and thirst in vain. They with parched lips their pangs must bear, And hope will end in blank despair. Ah me, there seems no fruit in store For holy zeal or Scripture lore, Or else ere now my sire would know That his dear son is lying low. Yet, if my mournful fate he knew, What could his arm so feeble do? The tree, firm-rooted, ne'er may be The guardian of a stricken tree. Haste to my father, and relate While time allows, my sudden fate, Lest he consume thee as the fire Burns up the forest, in his ire. This little path, O King, pursue: My father's cot thou soon wilt view. There sue for pardon to the sage, Lest he should curse thee in his rage. First from the wound extract the dart That kills me with its deadly smart, E'en as the flushed impetuous tide Eats through the river's yielding side.” I feared to draw the arrow out, And pondered thus in painful doubt: “Now tortured by the shaft he lies, But if I draw it forth he dies.” Helpless I stood, faint, sorely grieved: The hermit's son my thought perceived; As one o'ercome by direst pain He scarce had strength to speak again.
- **Translation**: 

---

### Verse 11 (Ramayan 0.611)
- **Original**: Canto LXIV. Dasaratha's Death. 593 With writhing limb and struggling breath, Nearer and ever nearer death “My senses undisturbed remain, And fortitude has conquered pain: Now from one tear thy soul be freed. Thy hand has made a Bráhman bleed. Let not this pang thy bosom wring: No twice-born youth am I, O King, [170] For of a Vai[ya sire I came, Who wedded with aZúdra dame.” These words the boy could scarcely say, As tortured by the shaft he lay, Twisting his helpless body round, Then trembling senseless on the ground. Then from his bleeding side I drew The rankling shaft that pierced him through. With death's last fear my face he eyed, And, rich in store of penance, died.” Canto LXIV. Dasaratha's Death. The son of Raghu to his queen Thus far described the unequalled scene, And, as the hermit's death he rued, The mournful story thus renewed: “The deed my heedless hand had wrought Perplexed me with remorseful thought, And all alone I pondered still How kindly deed might salve the ill. The pitcher from the ground I took,
- **Translation**: 

---

### Verse 12 (Ramayan 0.612)
- **Original**: 594 The Ramayana And filled it from that fairest brook, Then, by the path the hermit showed, I reached his sainted sire's abode. I came, I saw: the aged pair, Feeble and blind, were sitting there, Like birds with clipped wings, side by side, With none their helpless steps to guide. Their idle hours the twain beguiled With talk of their returning child, And still the cheering hope enjoyed, The hope, alas, by me destroyed. Then spoke the sage, as drawing near The sound of footsteps reached his ear: “Dear son, the water quickly bring; Why hast thou made this tarrying? Thy mother thirsts, and thou hast played, And bathing in the brook delayed. She weeps because thou camest not; Haste, O my son, within the cot. If she or I have ever done A thing to pain thee, dearest son, Dismiss the memory from thy mind: A hermit thou, be good and kind. On thee our lives, our all, depend: Thou art thy friendless parents' friend. The eyeless couple's eye art thou: Then why so cold and silent now?” With sobbing voice and bosom wrung I scarce could move my faltering tongue, And with my spirit filled with dread I looked upon the sage, and said, While mind, and sense, and nerve I strung To fortify my trembling tongue,
- **Translation**: 

---

### Verse 13 (Ramayan 0.613)
- **Original**: Canto LXIV. Dasaratha's Death. 595 And let the aged hermit know His son's sad fate, my fear and woe: “High-minded Saint, not I thy child, A warrior, Da[aratha styled. I bear a grievous sorrow's weight Born of a deed which good men hate. My lord, I came to Sarjú's shore, And in my hand my bow I bore For elephant or beast of chase That seeks by night his drinking place. There from the stream a sound I heard As if a jar the water stirred. An elephant, I thought, was nigh: I aimed, and let an arrow fly. Swift to the place I made my way, And there a wounded hermit lay Gasping for breath: the deadly dart Stood quivering in his youthful heart. I hastened near with pain oppressed; He faltered out his last behest. And quickly, as he bade me do, From his pierced side the shaft I drew. I drew the arrow from the rent, And up to heaven the hermit went, Lamenting, as from earth he passed, His aged parents to the last. Thus, unaware, the deed was done: My hand, unwitting, killed thy son. For what remains, O, let me win Thy pardon for my heedless sin.” As the sad tale of sin I told The hermit's grief was uncontrolled. With flooded eyes, and sorrow-faint,
- **Translation**: 

---

### Verse 14 (Ramayan 0.614)
- **Original**: 596 The Ramayana Thus spake the venerable saint: I stood with hand to hand applied, And listened as he spoke and sighed: “If thou, O King, hadst left unsaid By thine own tongue this tale of dread, Thy head for hideous guilt accursed Had in a thousand pieces burst. A hermit's blood by warrior spilt, In such a case, with purposed guilt, Down from his high estate would bring Even the thunder's mighty King. And he a dart who conscious sends Against the devotee who spends His pure life by the law of Heaven— That sinner's head will split in seven. Thou livest, for thy heedless hand Has wrought a deed thou hast not planned, Else thou and all of Raghu's line Had perished by this act of thine. Now guide us,” thus the hermit said, “Forth to the spot where he lies dead. Guide us, this day, O Monarch, we For the last time our son would see: The hermit dress of skin he wore Rent from his limbs distained with gore; His senseless body lying slain, His soul in Yama's dark domain.” Alone the mourning pair I led, Their souls with woe disquieted, And let the dame and hermit lay[171] Their hands upon the breathless clay. The father touched his son, and pressed The body to his aged breast;
- **Translation**: 

---

### Verse 15 (Ramayan 0.615)
- **Original**: Canto LXIV. Dasaratha's Death. 597 Then falling by the dead boy's side, He lifted up his voice, and cried: “Hast thou no word, my child, to say? No greeting for thy sire to-day? Why art thou angry, darling? why Wilt thou upon the cold earth lie? If thou, my son, art wroth with me, Here, duteous child, thy mother see. What! no embrace for me, my son? No word of tender love— not one? Whose gentle voice, so soft and clear, Soothing my spirit, shall I hear When evening comes, with accents sweet Scripture or ancient lore repeat? Who, having fed the sacred fire, And duly bathed, as texts require, Will cheer, when evening rites are done, The father mourning for his son? Who will the daily meal provide For the poor wretch who lacks a guide, Feeding the helpless with the best Berries and roots, like some dear guest? How can these hands subsistence find For thy poor mother, old and blind? The wretched votaress how sustain, Who mourns her child in ceaseless pain? Stay yet a while, my darling, stay, Nor fly to Yama's realm to-day. To-morrow I thy sire and she Who bare thee, child, will go with, thee.337 337 So dying York cries over the body of Suffolk: “Tarry, dear cousin Suffolk! My soul shall thine keep company to heaven:
- **Translation**: 

---

### Verse 16 (Ramayan 0.616)
- **Original**: 598 The Ramayana Then when I look on Yama, I To great Vivasvat's son will cry: “Hear, King of justice, and restore Our child to feed us, I implore. Lord of the world, of mighty fame, Faithful and just, admit my claim, And grant this single boon to free My soul from fear, to one like me.” Because, my son, untouched by stain, By sinful hands thou fallest slain, Win, through thy truth, the sphere where those Who die by hostile darts repose. Seek the blest home prepared for all The valiant who in battle fall, Who face the foe and scorn to yield, In glory dying on the field. Rise to the heaven where Dhundhumár And Nahush, mighty heroes, are, Where Janamejay and the blest Dilípa, Sagar, Saivya, rest: Home of all virtuous spirits, earned By fervent rites and Scripture learned: By those whose sacred fires have glowed, Whose liberal hands have fields bestowed: By givers of a thousand cows, By lovers of one faithful spouse: By those who serve their masters well, And cast away this earthly shell. None of my race can ever know The bitter pain of lasting woe. But doomed to that dire fate is he Tarry, sweet soul, for mine, then fly abreast.” King Henry V, Act IV, 6.
- **Translation**: 

---

### Verse 17 (Ramayan 0.617)
- **Original**: Canto LXIV. Dasaratha's Death. 599 Whose guilty hand has slaughtered thee.” Thus with wild tears the aged saint Made many a time his piteous plaint, Then with his wife began to shed The funeral water for the dead. But in a shape celestial clad, Won by the merits of the lad, The spirit from the body brake And to the mourning parents spake: “A glorious home in realms above Rewards my care and filial love. You, honoured parents, soon shall be Partakers of that home with me.” He spake, and swiftly mounting high, With Indra near him, to the sky On a bright car, with flame that glowed, Sublime the duteous hermit rode. The father, with his consort's aid, The funeral rites with water paid, And thus his speech to me renewed Who stood in suppliant attitude: “Slay me this day, O, slay me, King, For death no longer has a sting. Childless am I: thy dart has done To death my dear, my only son. Because the boy I loved so well Slain by thy heedless arrow fell, My curse upon thy soul shall press With bitter woe and heaviness. I mourn a slaughtered child, and thou Shalt feel the pangs that kill me now. Bereft and suffering e'en as I,
- **Translation**: 

---

### Verse 18 (Ramayan 0.618)
- **Original**: 600 The Ramayana So shalt thou mourn thy son, and die. Thy hand unwitting dealt the blow That laid a holy hermit low, And distant, therefore, is the time When thou shalt suffer for the crime. The hour shall come when, crushed by woes Like these I feel, thy life shall close: A debt to pay in after days Like his the priestly fee who pays.” This curse on me the hermit laid, Nor yet his tears and groans were stayed. Then on the pyre their bodies cast The pair; and straight to heaven they passed. As in sad thought I pondered long Back to my memory came the wrong Done in wild youth, O lady dear, When 'twas my boast to shoot by ear.[172] The deed has borne the fruit, which now Hangs ripe upon the bending bough: Thus dainty meats the palate please, And lure the weak to swift disease. Now on my soul return with dread The words that noble hermit said, That I for a dear son should grieve, And of the woe my life should leave.” Thus spake the king with many a tear; Then to his wife he cried in fear: “I cannot see thee, love; but lay Thy gentle hand in mine, I pray. Ah me, if Ráma touched me thus, If once, returning home to us, He bade me wealth and lordship give,
- **Translation**: 

---

### Verse 19 (Ramayan 0.619)
- **Original**: Canto LXIV. Dasaratha's Death. 601 Then, so I think, my soul would live. Unlike myself, unjust and mean Have been my ways with him, my Queen, But like himself is all that he, My noble son, has done to me. His son, though far from right he stray, What prudent sire would cast away? What banished son would check his ire, Nor speak reproaches of his sire? I see thee not: these eyes grow blind, And memory quits my troubled mind. Angels of Death are round me: they Summon my soul with speed away. What woe more grievous can there be, That, when from light and life I flee, I may not, ere I part, behold My virtuous Ráma, true and bold? Grief for my son, the brave and true, Whose joy it was my will to do, Dries up my breath, as summer dries The last drop in the pool that lies. Not men, but blessed Gods, are they Whose eyes shall see his face that day; See him, when fourteen years are past, With earrings decked return at last. My fainting mind forgets to think: Low and more low my spirits sink. Each from its seat, my senses steal: I cannot hear, or taste, or feel. This lethargy of soul o'ercomes Each organ, and its function numbs: So when the oil begins to fail, The torch's rays grow faint and pale. This flood of woe caused by this hand
- **Translation**: 

---

### Verse 20 (Ramayan 0.620)
- **Original**: 602 The Ramayana Destroys me helpless and unmanned, Resistless as the floods that bore A passage through the river shore. Ah Raghu's son, ah mighty-armed, By whom my cares were soothed and charmed, My son in whom I took delight, Now vanished from thy father's sight! Kau [alyá, ah, I cannot see; Sumitrá, gentle devotee! Alas, Kaikeyí, cruel dame, My bitter foe, thy father's shame!” Kau [alyá and Sumitrá kept Their watch beside him as he wept. And Da [aratha moaned and sighed, And grieving for his darling died. Canto LXV. The Women's Lament. And now the night had past away, And brightly dawned another day; The minstrels, trained to play and sing, Flocked to the chamber of the king: Bards, who their gayest raiment wore, And heralds famed for ancient lore: And singers, with their songs of praise, Made music in their several ways. There as they poured their blessings choice And hailed their king with hand and voice, Their praises with a swelling roar Echoed through court and corridor.
- **Translation**: 

---



--- End of Ramayan_batch_31.md ---


--- Start of Ramayan_batch_32.md ---

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

### Verse 1 (Ramayan 0.621)
- **Original**: Canto LXV. The Women's Lament. 603 Then as the bards his glory sang, From beaten palms loud answer rang, As glad applauders clapped their hands, And told his deeds in distant lands. The swelling concert woke a throng Of sleeping birds to life and song: Some in the branches of the trees, Some caged in halls and galleries. Nor was the soft string music mute; The gentle whisper of the lute, And blessings sung by singers skilled The palace of the monarch filled. Eunuchs and dames of life unstained, Each in the arts of waiting trained, Drew near attentive as before, And crowded to the chamber door: These skilful when and how to shed The lustral stream o'er limb and head, Others with golden ewers stood Of water stained with sandal wood. And many a maid, pure, young, and fair, Her load of early offerings bare, Cups of the flood which all revere, And sacred things, and toilet gear. Each several thing was duly brought As rule of old observance taught, And lucky signs on each impressed Stamped it the fairest and the best. There anxious, in their long array, All waited till the shine of day: But when the king nor rose nor spoke, Doubt and alarm within them woke. Forthwith the dames, by duty led, Attendants on the monarch's bed,
- **Translation**: 

---

### Verse 2 (Ramayan 0.622)
- **Original**: 604 The Ramayana Within the royal chamber pressed To wake their master from his rest. Skilled in the lore of dreaming, they First touched the bed on which he lay. But none replied; no sound was heard,[173] Nor hand, nor head, nor body stirred. They trembled, and their dread increased, Fearing his breath of life had ceased, And bending low their heads, they shook Like the tall reeds that fringe the brook. In doubt and terror down they knelt, Looked on his face, his cold hand felt, And then the gloomy truth appeared Of all their hearts had darkly feared. Kau [alyá and Sumitrá, worn With weeping for their sons, forlorn, Woke not, but lay in slumber deep And still as death's unending sleep. Bowed down by grief, her colour fled, Her wonted lustre dull and dead, Kau [alyá shone not, like a star Obscured behind a cloudy bar. Beside the king's her couch was spread, And next was Queen Sumitrá's bed, Who shone no more with beauty's glow, Her face bedewed with tears of woe. There lapped in sleep each wearied queen, There as in sleep, the king was seen; And swift the troubling thought came o'er Their spirits that he breathed no more. At once with wailing loud and high The matrons shrieked a bitter cry, As widowed elephants bewail Their dead lord in the woody vale.
- **Translation**: 

---

### Verse 3 (Ramayan 0.623)
- **Original**: Canto LXV. The Women's Lament. 605 At the loud shriek that round them rang, Kau [alyá and Sumitrá sprang Awakened from their beds, with eyes Wide open in their first surprise. Quick to the monarch's side they came, And saw and touched his lifeless frame; One cry, O husband! forth they sent, And prostrate to the ground they went. The king of Ko[al's daughter338 there Writhed, with the dust on limb and hair Lustreless, as a star might lie Hurled downward from the glorious sky. When the king's voice in death was stilled, The women who the chamber filled Saw, like a widow elephant slain, Kau [alyá prostrate in her pain. Then all the monarch's ladies led By Queen Kaikeyí at their head, Poured forth their tears, and weeping so, Sank on the ground, consumed by woe. The cry of grief so long and loud Went up from all the royal crowd, That, doubled by the matron train, It made the palace ring again. Filled with dark fear and eager eyes, Anxiety and wild surmise; Echoing with the cries of grief Of sorrowing friends who mourned their chief, Dejected, pale with deep distress, Hurled from their height of happiness: Such was the look the palace wore Where lay the king who breathed no more. 338 Kau [alyá, daughter of the king of another Ko[al.
- **Translation**: 

---

### Verse 4 (Ramayan 0.624)
- **Original**: 606 The Ramayana Canto LXVI. The Embalming. Kau [alyá's eyes with tears o'erflowed, Weighed down by varied sorrows' load; On her dead lord her gaze she bent, Who lay like fire whose might is spent, Like the great deep with waters dry, Or like the clouded sun on high. Then on her lap she laid his head. And on Kaikeyí looked and said: “Triumphant now enjoy thy reign Without a thorn thy side to pain. Thou hast pursued thy single aim, And killed the king, O wicked dame. Far from my sight my Ráma flies, My perished lord has sought the skies. No friend, no hope my life to cheer, I cannot tread the dark path here. Who would forsake her husband, who That God to whom her love is due, And wish to live one hour, but she Whose heart no duty owns, like thee? The ravenous sees no fault: his greed Will e'en on poison blindly feed. Kaikeyí, through a hump-back maid, This royal house in death has laid. King Janak, with his queen, will hear Heart rent like me the tidings drear Of Ráma banished by the king, Urged by her impious counselling. No son has he, his age is great, And sinking with the double weight, He for his darling child will pine, And pierced with woe his life resign.
- **Translation**: 

---

### Verse 5 (Ramayan 0.625)
- **Original**: Canto LXVI. The Embalming. 607 Sprung from Videha's monarch, she A sad and lovely devotee, Roaming the wood, unmeet for woe, Will toil and trouble undergo. She in the gloomy night with fear The cries of beast and bird will hear, And trembling in her wild alarm Will cling to Ráma's sheltering arm. Ah, little knows my duteous son That I am widowed and undone— My Ráma of the lotus eye, Gone hence, gone hence, alas, to die. Now, as a living wife and true, I, e'en this day, will perish too: Around his form these arms will throw And to the fire with him will go.” Clasping her husband's lifeless clay A while the weeping votaress lay, Till chamberlains removed her thence [174] O'ercome by sorrow's violence. Then in a cask of oil they laid Him who in life the world had swayed, And finished, as the lords desired, All rites for parted souls required. The lords, all-wise, refused to burn The monarch ere his son's return; So for a while the corpse they set Embalmed in oil, and waited yet. The women heard: no doubt remained, And wildly for the king they plained. With gushing tears that drowned each eye Wildly they waved their arms on high, And each her mangling nails impressed
- **Translation**: 

---

### Verse 6 (Ramayan 0.626)
- **Original**: 608 The Ramayana Deep in her head and knee and breast: “Of Ráma reft,— who ever spake The sweetest words the heart to take, Who firmly to the truth would cling,— Why dost thou leave us, mighty King? How can the consorts thou hast left Widowed, of Raghu's son bereft, Live with our foe Kaikeyí near, The wicked queen we hate and fear? She threw away the king, her spite Drove Ráma forth and LakshmaG's might, And gentle Sítá: how will she Spare any, whosoe'er it be?” Oppressed with sorrow, tear-distained, The royal women thus complained. Like night when not a star appears, Like a sad widow drowned in tears, Ayodhyá's city, dark and dim, Reft of her lord was sad for him. When thus for woe the king to heaven had fled, And still on earth his lovely wives remained. With dying light the sun to rest had sped, And night triumphant o'er the landscape reigned. Canto LXVII. The Praise Of Kings.
- **Translation**: 

---

### Verse 7 (Ramayan 0.627)
- **Original**: Canto LXVII. The Praise Of Kings. 609 That night of sorrow passed away, And rose again the God of Day. Then all the twice-born peers of state Together met for high debate. Jáválí, lord of mighty fame. And Gautam, and Kátyáyan came, And Márkandeya's reverend age, And Vámadeva, glorious sage: Sprung from Mudgalya's seed the one, The other ancient Ka[yap's son. With lesser lords these Bráhmans each Spoke in his turn his several speech, And turning to Va[ishmha, best Of household priests him thus addressed: “The night of bitter woe has past, Which seemed a hundred years to last, Our king, in sorrow for his son, Reunion with the Five has won. His soul is where the blessed are, While Ráma roams in woods afar, And Lakshma G, bright in glorious deeds, Goes where his well-loved brother leads. And Bharat andZatrughna, they Who smite their foes in battle fray, Far in the realm of Kekaya stay, Where their maternal grandsire's care Keeps Rájagriha's city fair. Let one of old Ikshváku's race Obtain this day the sovereign's place, Or havoc and destruction straight Our kingless land will devastate. In kingless lands no thunder's voice, No lightning wreaths the heart rejoice, Nor does Parjanya's heavenly rain
- **Translation**: 

---

### Verse 8 (Ramayan 0.628)
- **Original**: 610 The Ramayana Descend upon the burning plain. Where none is king, the sower's hand Casts not the seed upon the land; The son against the father strives. And husbands fail to rule their wives. In kingless realms no princes call Their friends to meet in crowded hall; No joyful citizens resort To garden trim or sacred court. In kingless realms no Twice-born care To sacrifice with text and prayer, Nor Bráhmans, who their vows maintain, The great solemnities ordain. The joys of happier days have ceased: No gathering, festival, or feast Together calls the merry throng Delighted with the play and song. In kingless lands it ne'er is well With sons of trade who buy and sell: No men who pleasant tales repeat Delight the crowd with stories sweet. In kingless realms we ne'er behold Young maidens decked with gems and gold, Flock to the gardens blithe and gay To spend their evening hours in play. No lover in the flying car Rides with his love to woods afar. In kingless lands no wealthy swain Who keeps the herd and reaps the grain, Lies sleeping, blest with ample store, Securely near his open door. Upon the royal roads we see No tusked elephant roaming free, Of three-score years, whose head and neck
- **Translation**: 

---

### Verse 9 (Ramayan 0.629)
- **Original**: Canto LXVII. The Praise Of Kings. 611 Sweet tinkling bells of silver deck. We hear no more the glad applause When his strong bow each rival draws, No clap of hands, no eager cries That cheer each martial exercise. In kingless realms no merchant bands Who travel forth to distant lands, With precious wares their wagons load, [175] And fear no danger on the road. No sage secure in self-control, Brooding on God with mind and soul, In lonely wanderings finds his home Where'er at eve his feet may roam. In kingless realms no man is sure He holds his life and wealth secure. In kingless lands no warriors smite The foeman's host in glorious fight. In kingless lands the wise no more, Well trained in Scripture's holy lore, In shady groves and gardens meet To argue in their calm retreat. No longer, in religious fear, Do they who pious vows revere, Bring dainty cates and wreaths of flowers As offerings to the heavenly powers. No longer, bright as trees in spring, Shine forth the children of the king Resplendent in the people's eyes With aloe wood and sandal dyes. A brook where water once has been, A grove where grass no more is green, Kine with no herdsman's guiding hand— So wretched is a kingless land. The car its waving banner rears,
- **Translation**: 

---

### Verse 10 (Ramayan 0.630)
- **Original**: 612 The Ramayana Banner of fire the smoke appears: Our king, the banner of our pride, A God with Gods is glorified. In kingless lands no law is known, And none may call his wealth his own, Each preys on each from hour to hour, As fish the weaker fish devour. Then fearless, atheists overleap The bounds of right the godly keep, And when no royal powers restrain, Preëminence and lordship gain. As in the frame of man the eye Keeps watch and ward, a careful spy, The monarch in his wide domains Protects the truth, the right maintains. He is the right, the truth is he, Their hopes in him the well-born see. On him his people's lives depend, Mother is he, and sire, and friend. The world were veiled in blinding night, And none could see or know aright, Ruled there no king in any state The good and ill to separate. We will obey thy word and will As if our king were living still: As keeps his bounds the faithful sea, So we observe thy high decree. O best of Bráhmans, first in place, Our kingless land lies desolate: Some scion of Ikshváku's race Do thou as monarch consecrate.”
- **Translation**: 

---

### Verse 11 (Ramayan 0.631)
- **Original**: Canto LXVIII. The Envoys. 613 Canto LXVIII. The Envoys. Va [ishmha heard their speech and prayer, And thus addressed the concourse there, Friends, Bráhmans, counsellors, and all Assembled in the palace hall: “Ye know that Bharat, free from care, Still lives in Rájagriha339 where The father of his mother reigns: Zatrughna by his side remains. Let active envoys, good at need, Thither on fleetest horses speed, To bring the hero youths away: Why waste the time in dull delay?” Quick came from all the glad reply: “Va [ishmha, let the envoys fly!” He heard their speech, and thus renewed His charge before the multitude: “Nandan, A[ok, Siddhárth, attend, Your ears, Jayanta, Vijay, lend: Be yours, what need requires, to do: I speak these words to all of you. With coursers of the fleetest breed To Rájagriha's city speed. Then rid your bosoms of distress, And Bharat thus from me address: “The household priest and peers by us Send health to thee and greet thee thus: Come to thy father's home with haste: Thine absent time no longer waste.” 339 Rájagriha, or Girivraja was the capital of A[vapati, Bharat's maternal grandfather.
- **Translation**: 

---

### Verse 12 (Ramayan 0.632)
- **Original**: 614 The Ramayana But speak no word of Ráma fled, Tell not the prince his sire is dead, Nor to the royal youth the fate That ruins Raghu's race relate. Go quickly hence, and with you bear Fine silken vestures rich and rare, And gems and many a precious thing As gifts to Bharat and the king.” With ample stores of food supplied, Each to his home the envoys hied, Prepared, with steeds of swiftest race, To Kekaya's land340 their way to trace. They made all due provision there, And every need arranged with care, Then ordered by Va[ishmha, they Went forth with speed upon their way. Then northward of Pralamba, west Of Apartála, on they pressed, Crossing the Máliní that flowed With gentle stream athwart the road. They traversed Gangá's holy waves[176] Where she Hástinapura341 laves, Thence to Panchála342 westward fast Through Kurujángal's land343 Note. 340 The Kekayas or Kaikayas in the Punjab appear amongst the chief nations in the war of the Mahábhárata; their king being a kinsman of KrishGa. 341 Hástinapura was the capital of the kingdom of Kuru, near the modern Delhi. 342 The Panchálas occupied the upper part of the Doab. 343 “Kurujángala and its inhabitants are frequently mentioned in the Mahábhárata, as in theÁdi-parv.3789, 4337,et al.” W ILSON 'S{FNS VishGu PuráGa,Vol. II. p. 176. DR . HALL 'S{FNS
- **Translation**: 

---

### Verse 13 (Ramayan 0.633)
- **Original**: Canto LXVIII. The Envoys. 615 they passed. On, on their course the envoys held By urgency of task impelled. Quick glancing at each lucid flood And sweet lake gay with flower and bud. Beyond, they passed unwearied o'er, Where glad birds fill the flood and shore Of ZaradaG á racing fleet With heavenly water clear and sweet, Thereby a tree celestial grows Which every boon on prayer bestows: To its blest shade they humbly bent, Then to Kulingá's town they went. Then, having passed the Warrior's Wood, In Abhikála next they stood, O'er sacred Ikshumatí344 Edition. The Ikshumatí was a river in Kurukshetra. came, Their ancient kings' ancestral claim. They saw the learned Bráhmans stand, Each drinking from his hollowed hand, And through Báhíka345 journeying still They reached at length Sudáman's hill: There VishGu's footstep turned to see, Vipá[á346 viewed, andZálmalí, And many a lake and river met, Tank, pool, and pond, and rivulet. 344 “The I¾{¼±Ä¹Â of Arrian. SeeAs. Res. Vol. XV. p. 420, 421, also Indische Alterthumskunde, Vol. I. p. 602, first footnote.” W ILSON 'S{FNS VishGu PuráGa, Vol. I. p. 421. DR . HALL 'S{FNS 345 “The Báhíkas are described in the Mahábhárata, KarGa Parvan, with some detail, and comprehend the different nations of the Punjab from the Sutlej to the Indus.” W ILSON 'S{FNS VishGu PuráGa, Vol. I. p. 167. 346 The Beas, Hyphasis, or Bibasis.
- **Translation**: 

---

### Verse 14 (Ramayan 0.634)
- **Original**: 616 The Ramayana And lions saw, and tigers near, And elephants and herds of deer, And still, by prompt obedience led, Along the ample road they sped. Then when their course so swift and long, Had worn their steeds though fleet and strong, To Girivraja's splendid town They came by night, and lighted down. To please their master, and to guard The royal race, the lineal right, The envoys, spent with riding hard, To that fair city came by night.347 347 It would be lost labour to attempt to verify all the towns and streams mentioned in Cantos LXVIII and LXXII. Professor Wilson observes (VishGu PuráGa, p. 139. Dr. Hall's Edition)“States, and tribes, and cities have disap- peared, even from recollection; and some of the natural features of the country, especially the rivers, have undergone a total alteration.… Notwithstanding these impediments, however, we should be able to identify at least mountains and rivers, to a much greater extent than is now practicable, if our maps were not so miserably defective in their nomenclature. None of our surveyors or geographers have been oriental scholars. It may be doubted if any of them have been conversant with the spoken language of the country. They have, consequently, put down names at random, according to their own inaccurate appreciation of sounds carelessly, vulgarly, and corruptly uttered; and their maps of India are crowded with appellations which bear no similitude whatever either to past or present denominations. We need not wonder that we cannot discover Sanskrit names in English maps, when, in the immediate vicinity of Calcutta, Barnagore represents Baráhanagar, Dakshine[war is metamorphosed into Duckinsore, Ulubaría into Willoughbury.… There is scarcely a name in our Indian maps that does not afford proof of extreme indifference to accuracy in nomenclature, and of an incorrectness in estimating sounds, which is, in some degree, perhaps, a national defect.” For further information regarding the road from Ayodhyá to Rájagriha, see
- **Translation**: 

---

### Verse 15 (Ramayan 0.635)
- **Original**: Canto LXIX. Bharat's Dream. 617 Canto LXIX. Bharat's Dream. The night those messengers of state Had past within the city's gate, In dreams the slumbering Bharat saw A sight that chilled his soul with awe. The dream that dire events foretold Left Bharat's heart with horror cold, [177] And with consuming woes distraught, Upon his aged sire he thought. His dear companions, swift to trace The signs of anguish on his face, Drew near, his sorrow to expel, And pleasant tales began to tell. Some woke sweet music's cheering sound, And others danced in lively round. With joke and jest they strove to raise His spirits, quoting ancient plays; But Bharat still, the lofty-souled, Deaf to sweet tales his fellows told, Unmoved by music, dance, and jest, Sat silent, by his woe oppressed. To him, begirt by comrades near, Thus spoke the friend he held most dear: “Why ringed around by friends, art thou So silent and so mournful now?” “Hear thou,” thus Bharat made reply, “What chills my heart and dims mine eye. I dreamt I saw the king my sire Sink headlong in a lake of mire Down from a mountain high in air, His body soiled, and loose his hair. Additional Notes.
- **Translation**: 

---

### Verse 16 (Ramayan 0.636)
- **Original**: 618 The Ramayana Upon the miry lake he seemed To lie and welter, as I dreamed; With hollowed hands full many a draught Of oil he took, and loudly laughed. With head cast down I saw him make A meal on sesamum and cake; The oil from every member dripped, And in its clammy flood he dipped. The ocean's bed was bare and dry, The moon had fallen from the sky, And all the world lay still and dead, With whelming darkness overspread. The earth was rent and opened wide, The leafy trees were scorched, and died; I saw the seated mountains split, And wreaths of rising smoke emit. The stately beast the monarch rode His long tusks rent and splintered showed; And flames that quenched and cold had lain Blazed forth with kindled light again. I looked, and many a handsome dame, Arrayed in brown and sable came And bore about the monarch, dressed, On iron stool, in sable vest. And then the king, of virtuous mind, A blood-red wreath around him twined, Forth on an ass-drawn chariot sped, As southward still he bent his head. Then, crimson-clad, a dame appeared Who at the monarch laughed and jeered; And a she-monster, dire to view, Her hand upon his body threw. Such is the dream I dreamt by night, Which chills me yet with wild affright:
- **Translation**: 

---

### Verse 17 (Ramayan 0.637)
- **Original**: Canto LXX. Bharat's Departure. 619 Either the king or Ráma, I Or LakshmaG now must surely die. For when an ass-drawn chariot seems To bear away a man in dreams, Be sure above his funeral pyre The smoke soon rears its cloudy spire. This makes my spirit low and weak, My tongue is slow and loth to speak: My lips and throat are dry for dread, And all my soul disquieted. My lips, relaxed, can hardly speak, And chilling dread has changed my cheek I blame myself in aimless fears, And still no cause of blame appears. I dwell upon this dream of ill Whose changing scenes I viewed, And on the startling horror still My troubled thoughts will brood. Still to my soul these terrors cling, Reluctant to depart, And the strange vision of the king Still weighs upon my heart.” Canto LXX. Bharat's Departure. While thus he spoke, the envoys borne On horses faint and travel-worn Had gained the city fenced around With a deep moat's protecting bound. An audience of the king they gained, And honours from the prince obtained;
- **Translation**: 

---

### Verse 18 (Ramayan 0.638)
- **Original**: 620 The Ramayana The monarch's feet they humbly pressed, To Bharat next these words addressed: “The household priest and peers by us Send health to thee and greet thee thus: “Come to thy father's house with haste: Thine absent time no longer waste.” Receive these vestures rich and rare, These costly gems and jewels fair, And to thy uncle here present Each precious robe and ornament. These for the king and him suffice— Two hundred millions is their price— These, worth a hundred millions, be Reserved, O large-eyed Prince, for thee.” Loving his friends with heart and soul, The joyful prince received the whole, Due honour to the envoys paid, And thus in turn his answer made: “Of Da[aratha tidings tell: Is the old king my father well? Is Ráma, and is LakshmaG, he Of the high-soul, from sickness free? And she who walks where duty leads, Kau [alyá, known for gracious deeds, Mother of Ráma, loving spouse, Bound to her lord by well kept vows? And Lakshma G's mother too, the dame Sumitrá skilled in duty's claim, Who brave Zatrughna also bare, Second in age,— her health declare.[178] And she, in self-conceit most sage, With selfish heart most prone to rage, My mother, fares she well? has she
- **Translation**: 

---

### Verse 19 (Ramayan 0.639)
- **Original**: Canto LXX. Bharat's Departure. 621 Sent message or command to me?” Thus Bharat spake, the mighty-souled, And they in brief their tidings told: “All they of whom thou askest dwell, O lion lord, secure and well: Thine all the smiles of fortune are: Make ready; let them yoke the car.” Thus by the royal envoys pressed, Bharat again the band addressed: “I go with you: no long delay, A single hour I bid you stay.” Thus Bharat, son of him who swayed Ayodhyás realm, his answer made, And then bespoke, his heart to please, His mother's sire in words like these: “I go to see my father, King, Urged by the envoys' summoning; And when thy soul desires to see Thy grandson, will return to thee.” The king his grandsire kissed his head, And in reply to Bharat said: “Go forth, dear child: how blest is she, The mother of a son like thee! Greet well thy sire, thy mother greet, O thou whose arms the foe defeat; The household priest, and all the rest Amid the Twice-born chief and best; And Ráma and brave LakshmaG, who Shoot the long shaft with aim so true.”
- **Translation**: 

---

### Verse 20 (Ramayan 0.640)
- **Original**: 622 The Ramayana To him the king high honour showed, And store of wealth and gifts bestowed, The choicest elephants to ride, And skins and blankets deftly dyed, A thousand strings of golden beads, And sixteen hundred mettled steeds: And boundless wealth before him piled Gave Kekaya to Kaikeyí's child. And men of counsel, good and tried, On whose firm truth he aye relied, King A[vapati gave with speed Prince Bharat on his way to lead. And noble elephants, strong and young, From sires of Indra[ira sprung, And others tall and fair to view Of great Airávat's lineage true: And well yoked asses fleet of limb The prince his uncle gave to him. And dogs within the palace bred, Of body vast and massive head, With mighty fangs for battle, brave, The tiger's match in strength, he gave. Yet Bharat's bosom hardly glowed To see the wealth the king bestowed; For he would speed that hour away, Such care upon his bosom lay: Those eager envoys urged him thence, And that sad vision's influence. He left his court-yard, crowded then With elephants and steeds and men, And, peerless in immortal fame, To the great royal street he came. He saw, as farther still he went, The inner rooms most excellent,
- **Translation**: 

---



--- End of Ramayan_batch_32.md ---
