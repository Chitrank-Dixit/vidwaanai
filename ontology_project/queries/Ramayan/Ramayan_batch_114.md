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

### Verse 1 (Ramayana 0.306)
- **Original**: 288 The Ramayana As he and Da[aratha spoke A tempest from the welkin broke, That shook the spacious earth amain And hurled high trees upon the plain. The sun grew dark with murky cloud, And o'er the skies was cast a shroud, While o'er the army, faint with dread, A veil of dust and ashes spread. King, princes, saints their sense retained, Fear-stupefied the rest remained. At length, their wits returning, all Beneath the gloom and ashy pall Saw Jamadagni's son with dread, His long hair twisted round his head, Who, sprung from Bhrigu, loved to beat The proudest kings beneath his feet. Firm as Kailása's hill he showed, Fierce as the fire of doom he glowed. His axe upon his shoulder lay, His bow was ready for the fray, With thirsty arrows wont to fly Like Lightnings from the angry sky. A long keen arrow forth he drew, Invincible like those which flew From Ziva's ever-conquering bow And Tripura in death laid low. When his wild form, that struck with awe, Fearful as ravening flame, they saw, Va [ishmha and the saints whose care Was sacrifice and muttered prayer, Drew close together, each to each, And questioned thus with bated speech: “Indignant at his father's fate
- **Translation**: 

---

### Verse 2 (Ramayana 0.307)
- **Original**: Canto LXXV. The Parle. 289 Will he on warriors vent his hate, The slayers of his father slay, And sweep the loathed race away? But when of old his fury raged Seas of their blood his wrath assuaged: [086] So doubtless now he has not planned To slay all warriors in the land.” Then with a gift the saints drew near To Bhrigu's son whose look was fear, And Ráma! Ráma! soft they cried. The gift he took, no word replied. Then Bhrigu's son his silence broke And thus to Ráma Ráma spoke: Canto LXXV. The Parle. “Heroic Ráma, men proclaim The marvels of thy matchless fame, And I from loud-voiced rumour know The exploit of the broken bow, Yea, bent and broken, mighty Chief, A feat most wondrous, past belief. Stirred by thy fame thy face I sought: A peerless bow I too have brought. This mighty weapon, strong and dire, Great Jamadagni owned, my sire. Draw with its shaft my father's bow, And thus thy might, O Ráma, show. This proof of prowess let me see— The weapon bent and drawn by thee;
- **Translation**: 

---

### Verse 3 (Ramayana 0.308)
- **Original**: 290 The Ramayana Then single fight our strength shall try, And this shall raise thy glory high.” King Da[aratha heard with dread The boastful speech, and thus he said; Raising his hands in suppliant guise, With pallid cheek and timid eyes: “Forgetful of the bloody feud Ascetic toils hast thou pursued; Then, Bráhman, let thy children be Untroubled and from danger free. Sprung of the race of Bhrigu, who Read holy lore, to vows most true, Thou swarest to the Thousand-eyed And thy fierce axe was cast aside. Thou turnedst to thy rites away Leaving the earth to Ka[yap's sway, And wentest far a grove to seek Beneath Mahendra's255 mountain peak. Now, mighty Hermit, art thou here To slay us all with doom severe? For if alone my Ráma fall, We share his fate and perish all.” 255 “The author of theRaghuvaE[a places the mountain Mahendra in the territo- ry of the king of the Kalingans, whose palace commanded a view of the ocean. It is well known that the country along the coast to the south of the mouths of the Ganges was the seat of this people. Hence it may be suspected that this Mahendra is what Pliny calls‘promontorium Calingon.’ The modern name, Cape Palmyras, from the palmyras Borassus flabelliformis, which abound there agrees remarkably with the description of the poet who speaks of the groves of these trees.RaghuvaE[a, VI. 51.” SCHLEGEL {FNS .
- **Translation**: 

---

### Verse 4 (Ramayana 0.309)
- **Original**: Canto LXXV. The Parle. 291 As thus the aged sire complained The mighty chief no answer deigned. To Ráma only thus he cried: “Two bows, the Heavenly Artist's pride, Celestial, peerless, vast, and strong, By all the worlds were honoured long. One to the Three-eyed God256 was given, By glory to the conflict driven, Thus armed fierce Tripura he slew: And then by thee 'twas burst in two. The second bow, which few may brave, The highest Gods to VishGu gave. This bow I hold; before it fall The foeman's fenced tower and wall. Then prayed the Gods the Sire Most High By some unerring proof to try Were praise for might Lord VishGu's due, Or his whose Neck is stained with Blue.257 The mighty Sire their wishes knew, And he whose lips are ever true Caused the two Gods to meet as foes. Then fierce the rage of battle rose: Bristled in dread each starting hair As Ziva strove with VishGu there. But VishGu raised his voice amain. And Ziva's bowstring twanged in vain; Its master of the Three bright Eyes Stood fixt in fury and surprise. Then all the dwellers in the sky, Minstrel, and saint, and God drew nigh, And prayed them that the strife might cease, And the great rivals met in peace. 256 Ziva. 257 Siva. God of the Azure Neck.
- **Translation**: 

---

### Verse 5 (Ramayana 0.310)
- **Original**: 292 The Ramayana 'Twas seen howZiva's bow has failed Unnerved, when VishGu's might assailed, And Gods and heavenly sages thence To Vishnu gave preëminence. Then gloriousZiva in his rage Gave it to Devarát the sage Who ruled Videha's fertile land, To pass it down from hand to hand. But this my bow, whose shafts smite down The foeman's fenced tower and town, To great Richíka VishGu lent To be a pledge and ornament, Then Jamadagni, Bráhman dread, My sire, the bow inherited. But Arjun stooped to treachery vile And slew my noble sire by guile, Whose penance awful strength had gained, Whose hand the God-given bow retained.[087] I heard indignant how he fell By mournful fate, too sad to tell. My vengeful fury since that time Scourges all Warriors for the crime. As generations spring to life I war them down in endless strife. All earth I brought beneath my sway, And gave it for his meed and pay To holy Ka[yap, when of yore The rites performed by him were o'er. Then to Mahendra's hill I turned Strong in the strength that penance earned, And toiled upon his lofty head By Gods immortal visited. The breaking of the bow I knew From startled Gods conversing, through
- **Translation**: 

---

### Verse 6 (Ramayana 0.311)
- **Original**: Canto LXXVI. Debarred From Heaven. 293 The airy regions, of thy deed, And hither came with swiftest speed. Now, for thy Warrior's honour sake, This best of bows, O Ráma, take: This, owned by VishGu's self of old, My sire and grandsire loved to hold. Drawn to its head upon the string, One town-destroying arrow bring; If this thou can, O hero, I In single fight thy strength will try.” Canto LXXVI. Debarred From Heaven. The haughty challenge, undeterred The son of Da[aratha heard, And cried, while reverence for his sire Checked the full torrent of his ire: “Before this day have I been told The deed that stained thy hands of old. But pity bids my soul forget: Thy father, murdered, claimed the debt. My strength, O Chief, thou deemest slight, Too feeble for a Warrior's might. Now will I show thy wondering eyes The prowess which they dare despise.”
- **Translation**: 

---

### Verse 7 (Ramayana 0.312)
- **Original**: 294 The Ramayana He hastened then with graceful ease That mighty bow and shaft to seize. His hand the weapon strung and swayed: The arrow on the string was laid. Then Jamadagni's son he eyed, And thus in words of fury cried: “Thou art a Bráhman, still to be Most highly honoured, Chief, by me. For Vi[vámitra's sake beside Shall reverence due be ne'er denied. Though mine the power, I would not send A dart at thee thy life to end. But thy great power to wander free, Which penance-rites have won for thee, Or glorious worlds from thee to wrest, Is the firm purpose of my breast, And VishGu's dart which now I strain Can ne'er be shot to fall in vain: It strikes the mighty, and it stuns The madness of the haughty ones.” Then Gods, and saints and heavenly choir Preceded by the General Sire, Met in the air and gazed below On Ráma with that wondrous bow. Nymph, minstrel, angel, all were there, Snake-God, and spirit of the air, Giant, and bard, and gryphon, met, Their eyes upon the marvel set. In senseless hush the world was chained While Ráma's hand the bow retained, And Jamadagni's son amazed And powerless on the hero gazed. Then when his swelling heart had shrunk,
- **Translation**: 

---

### Verse 8 (Ramayana 0.313)
- **Original**: Canto LXXVI. Debarred From Heaven. 295 And his proud strength in torpor sunk, Scarce his voice ventured, low and weak, To Ráma lotus-eyed, to speak: “When long ago I gave away The whole broad land to Ka[yap's sway He charged me never to remain Within the limits of his reign. Obedient to my guide's behest On earth by night I never rest. My choice is made, I will not dim Mine honour and be false to him. So, son of Raghu, leave me still The power to wander where I will, And swifter than the thought my flight Shall place me on Mahendra's height. My mansions of eternal joy, By penance won, thou mayst destroy, My path to these thy shaft may stay. Now to the work! No more delay! I know thee Lord of Gods; I know Thy changeless might laid Madhu low. All other hands would surely fail To bend this bow. All hail! all hail! See! all the Gods have left the skies To bend on thee their eager eyes, With whose achievements none compete, Whose arm in war no God can meet. No shame is mine, I ween, for thou, Lord of the Worlds, hast dimmed my brow. Now, pious Ráma, 'tis thy part To shoot afar that glorious dart: I, when the fatal shaft is shot, Will seek that hill and tarry not.”
- **Translation**: 

---

### Verse 9 (Ramayana 0.314)
- **Original**: 296 The Ramayana He ceased. The wondrous arrow flew, And Jamadagni's offspring knew Those glorious worlds to him were barred, Once gained by penance long and hard. Then straight the airy quarters cleared, And the mid regions bright appeared, While Gods and saints unnumbered praised Ráma, the mighty bow who raised. And Jamadagni's son, o'erawed. Extolled his name with highest laud,[088] With reverent steps around him strode, Then hastened on his airy road. Far from the sight of all he fled, And rested on Mahendra's head. Canto LXXVII. Bharat's Departure. Then Ráma with a cheerful mind The bow to VaruG's hand resigned. Due reverence to the saints he paid, And thus addressed his sire dismayed: “As Bhrigu's son is far from view, Now let the host its march pursue, And to Ayodhyá's town proceed In four-fold bands, with thee to lead.”
- **Translation**: 

---

### Verse 10 (Ramayana 0.315)
- **Original**: Canto LXXVII. Bharat's Departure. 297 King Da[aratha thus addressed His lips to Ráma's forehead pressed, And held him to his aged breast. Rejoiced in sooth was he to know That Bhrigu's son had parted so, And hailed a second life begun For him and his victorious son. He urged the host to speed renewed, And soon Ayodhyá's gates he viewed. High o'er the roofs gay pennons played; Tabour and drum loud music made; Fresh water cooled the royal road, And flowers in bright profusion glowed. Glad crowds with garlands thronged the ways Rejoicing on their king to gaze And all the town was bright and gay Exalting in the festive day. People and Bráhmans flocked to meet Their monarch ere he gained the street. The glorious king amid the throng Rode with his glorious sons along, And passed within his dear abode That like Himálaya's mountain showed. And there Kau[alyá, noble queen, Sumitrá with her lovely mien, Kaikeyí of the dainty waist, And other dames his bowers who graced, Stood in the palace side by side And welcomed home each youthful bride: Fair Sítá, lofty-fated dame, Urmilá of the glorious fame, And Ku [adhwaj's children fair, With joyous greeting and with prayer, As all in linen robes arrayed
- **Translation**: 

---

### Verse 11 (Ramayana 0.316)
- **Original**: 298 The Ramayana With offerings at the altars prayed. Due reverence paid to God above, Each princess gave her soul to love, And hidden in her inmost bower Passed with her lord each blissful hour. The royal youths, of spirit high, With whom in valor none could vie, Lived each within his palace bounds Bright as Kuvera's pleasure-grounds, With riches, troops of faithful friends, And bliss that wedded life attends: Brave princes trained in warlike skill, And duteous to their father's will. At length the monarch called one morn Prince Bharat, of Kaikeyí born, And cried:“My son, within our gates Lord Yudhájit thine uncle waits. The son of Kekaya's king is he, And came, my child, to summon thee.” Then Bharat for the road prepared, And withZatrughna forth he fared. First to his sire he bade adieu, Brave Ráma, and his mothers too. Lord Yudhájit with joyful pride Went forth, the brothers by his side, And reached the city where he dwelt: And mighty joy his father felt.
- **Translation**: 

---

### Verse 12 (Ramayana 0.317)
- **Original**: Canto LXXVII. Bharat's Departure. 299 Ráma and LakshmaG honoured still Their godlike sire with duteous will. Two constant guides for Ráma stood, His father's wish, the people's good. Attentive to the general weal He thought and wrought to please and heal. His mothers too he strove to please With love and sonly courtesies. At every time, in every spot, His holy guides he ne'er forgot. So for his virtues kind and true Dearer and dearer Ráma grew To Da[aratha, Bráhmans, all In town and country, great and small. And Ráma by his darling's side Saw many a blissful season glide, Lodged in her soul, each thought on her, Lover, and friend, and worshipper. He loved her for his father's voice Had given her and approved the choice: He loved her for each charm she wore And her sweet virtues more and more. So he her lord and second life Dwelt in the bosom of his wife, In double form, that, e'en apart, Each heart could commune free with heart. Still grew that child of Janak's race, More goddess-fair in form and face, The loveliest wife that e'er was seen, In mortal mould sweet Beauty's Queen. Then shone the son Kau[alyá bore, With this bright dame allied, Like VishGu whom the Gods adore,
- **Translation**: 

---

### Verse 13 (Ramayana 0.318)
- **Original**: 300 The Ramayana With Lakshmi by his side. [089]
- **Translation**: 

---

### Verse 14 (Ramayana 0.319)
- **Original**: BOOK II. Canto I. The Heir Apparent. So Bharat to his grandsire went Obedient to the message sent, And for his fond companion chose Zatrughna slayer of his foes.258 There Bharat for a time remained With love and honour entertained, King A[vapati's constant care, Beloved as a son and heir. Yet ever, as they lived at ease, While all around combined to please, The aged sire they left behind Was present to each hero's mind. Nor could the king's fond memory stray From his brave children far away, Dear Bharat andZatrughna dear, Each VaruG's match or Indra's peer. 258 Zatrughna means slayer of foes, and the word is repeated as an intensive epithet.
- **Translation**: 

---

### Verse 15 (Ramayana 0.320)
- **Original**: 302 The Ramayana To all the princes, young and brave, His soul with fond affection clave; Around his loving heart they clung Like arms from his own body sprung.259 But best and noblest of the four, Good as the God whom all adore, Lord of all virtues, undefiled, His darling was his eldest child. For he was beautiful and strong, From envy free, the foe of wrong, With all his father's virtues blest, And peerless in the world confessed. With placid soul he softly spoke: No harsh reply could taunts provoke. He ever loved the good and sage Revered for virtue and for age, And when his martial tasks were o'er Sate listening to their peaceful lore. Wise, modest, pure, he honoured eld, His lips from lying tales withheld; Due reverence to the Bráhmans gave, And ruled each passion like a slave. Most tender, prompt at duty's call, Loved by all men he loved them all. Proud of the duties of his race, With spirit meet for Warrior's place. He strove to win by glorious deed, Throned with the Gods, a priceless meed. With him in speech and quick reply Vrihaspati might hardly vie, But never would his accents flow For evil or for empty show. 259 Alluding to the images of VishGu, which have four arms, the four princes being portions of the substance of that God.
- **Translation**: 

---

### Verse 16 (Ramayana 0.321)
- **Original**: Canto I. The Heir Apparent. 303 In art and science duly trained, His student vow he well maintained; He learnt the lore for princes fit, The Vedas and their Holy Writ, And with his well-drawn bow at last His mighty father's fame surpassed. Of birth exalted, truthful, just, With vigorous hand, with noble trust, Well taught by aged twice-born men Who gain and right could clearly ken, Full well the claims and bounds he knew Of duty, gain, and pleasure too: Of memory keen, of ready tact, In civil business prompt to act. Reserved, his features ne'er disclosed What counsel in his heart reposed. All idle rage and mirth controlled, He knew the times to give and hold, Firm in his faith, of steadfast will, He sought no wrong, he spoke no ill: Not rashly swift, not idly slow, His faults and others' keen to know. Each merit, by his subtle sense; He matched with proper recompense. He knew the means that wealth provide, And with keen eye expense could guide. Wild elephants could he reclaim, And mettled steeds could mount and tame. No arm like his the bow could wield, Or drive the chariot to the field. Skilled to attack, to deal the blow, Or lead a host against the foe: Yea, e'en infuriate Gods would fear To meet his arm in full career.
- **Translation**: 

---

### Verse 17 (Ramayana 0.322)
- **Original**: 304 The Ramayana As the great sun in noontide blaze Is glorious with his world of rays, So Ráma with these virtues shone Which all men loved to gaze upon. The aged monarch fain would rest, And said within his weary breast, “Oh that I might, while living yet, My Ráma o'er the kingdom set. And see, before my course be run, The hallowed drops anoint my son; See all this spacious land obey, From side to side, my first-born's sway, And then, my life and joy complete, Obtain in heaven a blissful seat!” In him the monarch saw combined The fairest form, the noblest mind, And counselled how his son might share, The throne with him as Regent Heir. For fearful signs in earth and sky, And weakness warned him death was nigh: But Ráma to the world endeared By every grace his bosom cheered,[090] The moon of every eye, whose ray Drove all his grief and fear away. So duty urged that hour to seize, Himself, his realm, to bless and please. From town and country, far and near, He summoned people, prince, and peer. To each he gave a meet abode, And honoured all and gifts bestowed. Then, splendid in his king's attire, He viewed them, as the general Sire,
- **Translation**: 

---

### Verse 18 (Ramayana 0.323)
- **Original**: Canto II. The People's Speech. 305 In glory of a God arrayed, Looks on the creatures he has made. But Kekaya's king he called not then For haste, nor Janak, lord of men; For after to each royal friend The joyful tidings he would send. Mid crowds from distant countries met The king upon his throne was set; Then honoured by the people, all The rulers thronged into the hall. On thrones assigned, each king in place Looked silent on the monarch's face. Then girt by lords of high renown And throngs from hamlet and from town He showed in regal pride, As, honoured by the radiant band Of blessed Gods that round him stand, Lord Indra, Thousand-eyed. Canto II. The People's Speech. Then to the full assembly bowed The monarch, and addressed the crowd With gracious speech, in accents loud As heavenly drum or thunder-cloud:
- **Translation**: 

---

### Verse 19 (Ramayana 0.324)
- **Original**: 306 The Ramayana “Needs not to you who know declare How ever with paternal care My fathers of Ikshváku's line Have ruled the realm which now is mine. I too have taught my feet to tread The pathway of the mighty dead, And with fond care that never slept Have, as I could, my people kept. So toiling still, and ne'er remiss For all my people's weal and bliss, Beneath the white umbrella's260 shade. Old age is come and strength decayed. Thousands of years have o'er me flown, And generations round me grown And passed away. I crave at length Repose and ease for broken strength. Feeble and worn I scarce can bear The ruler's toil, the judge's care, With royal dignity, a weight That tries the young and temperate. I long to rest, my labour done, And in my place to set my son, If to the twice-born gathered here My counsel wise and good appear. For greater gifts than mine adorn Ráma my son, my eldest-born. Like Indra brave, before him fall The foeman's cities, tower and wall. Him prince of men for power and might, The best maintainer of the right, Fair as the moon when nothing bars His glory close to Pushya's stars, 260 Chief of the insignia of imperial dignity.
- **Translation**: 

---

### Verse 20 (Ramayana 0.325)
- **Original**: Canto II. The People's Speech. 307 Him with to-morrow's light I fain Would throne the consort of my reign. A worthy lord for you, I ween, Marked as her own by Fortune's Queen. The triple world itself would be Well ruled by such a king as he. To such high bliss and happy fate Will I the country dedicate, And my sad heart will cease to grieve If he the precious charge receive. Thus is my careful plan matured, Thus for myself is rest secured; Lieges, approve the words I say, Or point ye out some wiser way. Devise your prudent plan. My mind Is fondly to this thought inclined, But men by keen debating move Some middle course which all approve.” The monarch ceased. In answer came The joyous princes' glad acclaim. So peacocks in the rain rejoice And hail the cloud with lifted voice. Murmurs of joy from thousands round Shook the high palace with the sound. Then when the gathered throng had learned His will who right and gain discerned, Peasant and townsman, priest and chief, All met in consultation brief, And soon agreed with one accord Gave answer to their sovereign lord: “King of the land, we know thee old: Thousands of years have o'er thee rolled, Ráma thy son, we pray, anoint,
- **Translation**: 

---

