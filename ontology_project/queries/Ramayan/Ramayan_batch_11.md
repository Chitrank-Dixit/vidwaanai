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

### Verse 1 (Ramayan 0.201)
- **Original**: Canto XLIV. The Descent Of Gangá. 183 Then every spirit, sage, and bard, Condemned to earth by sentence hard, Pressed eagerly around the tide ThatZiva's touch had sanctified. Then they whom heavenly doom had hurled, Accursed, to this lower world, Touched the pure wave, and freed from sin Resought the skies and entered in. And all the world was glad, whereon The glorious water flowed and shone, For sin and stain were banished thence By the sweet river's influence. First, in a car of heavenly frame, The royal saint of deathless name, Bhagírath, very glorious rode, And after him fair Gangá flowed. God, sage, and bard, the chief in place Of spirits and the Nága race, Nymph, giant, fiend, in long array Sped where Bhagírath led the way; And all the hosts the flood that swim Followed the stream that followed him. Where'er the great Bhagírath led, There ever glorious Gangá fled, The best of floods, the rivers' queen, Whose waters wash the wicked clean. It chanced that Jahnu, great and good, Engaged with holy offerings stood; The river spread her waves around Flooding his sacrificial ground. The saint in anger marked her pride, And at one draught her stream he dried. Then God, and sage, and bard, afraid,
- **Translation**: 

---

### Verse 2 (Ramayan 0.202)
- **Original**: 184 The Ramayana To noble high-souled Jahnu prayed, And begged that he would kindly deem His own dear child that holy stream. Moved by their suit, he soothed their fears And loosed her waters from his ears. Hence Gangá through the world is styled Both Jáhnavi and Jahnu's child. Then onward still she followed fast, And reached the great sea bank at last. Thence deep below her way she made To end those rites so long delayed. The monarch reached the Ocean's side, And still behind him Gangá hied. He sought the depths which open lay Where Sagar's sons had dug their way. So leading through earth's nether caves The river's purifying waves,[056] Over his kinsmen's dust the lord His funeral libation poured. Soon as the flood their dust bedewed, Their spirits gained beatitude, And all in heavenly bodies dressed Rose to the skies' eternal rest. Then thus to King Bhagírath said Brahmá, when, coming at the head Of all his bright celestial train, He saw those spirits freed from stain: “Well done! great Prince of men, well done! Thy kinsmen bliss and heaven have won. The sons of Sagar mighty-souled, Are with the Blest, as Gods, enrolled, Long as the Ocean's flood shall stand Upon the border of the land,
- **Translation**: 

---

### Verse 3 (Ramayan 0.203)
- **Original**: Canto XLIV. The Descent Of Gangá. 185 So long shall Sagar's sons remain, And, godlike, rank in heaven retain. Gangá thine eldest child shall be, Called from thy name Bhágirathí; Named also— for her waters fell From heaven and flow through earth and hell— Tripathagá, stream of the skies, Because three paths she glorifies. And, mighty King, 'tis given thee now To free thee and perform thy vow. No longer, happy Prince, delay Drink-offerings to thy kin to pay. For this the holiest Sagar sighed, But mourned the boon he sought denied. Then An[umán, dear Prince! although No brighter name the world could show, Strove long the heavenly flood to gain To visit earth, but strove in vain. Nor was she by the sages' peer, Blest with all virtues, most austere, Thy sire Dilípa, hither brought, Though with fierce prayers the boon he sought. But thou, O King, earned success, And won high fame which God will bless. Through thee, O victor of thy foes, On earth this heavenly Gangá flows, And thou hast gained the meed divine That waits on virtue such as thine. Now in her ever holy wave Thyself, O best of heroes, lave: So shalt thou, pure from every sin, The blessed fruit of merit win. Now for thy kin who died of yore The meet libations duly pour.
- **Translation**: 

---

### Verse 4 (Ramayan 0.204)
- **Original**: 186 The Ramayana Above the heavens I now ascend: Depart, and bliss thy steps attend.” Thus to the mighty king who broke His foemens' might, Lord Brahmá spoke, And with his Gods around him rose To his own heaven of blest repose. The royal sage no more delayed, But, the libation duly paid, Home to his regal city hied With water cleansed and purified. There ruled he his ancestral state, Best of all men, most fortunate. And all the people joyed again In good Bhagírath's gentle reign. Rich, prosperous, and blest were they, And grief and sickness fled away. Thus, Ráma, I at length have told How Gangá came from heaven of old. Now, for the evening passes swift, I wish thee each auspicious gift. This story of the flood's descent Will give— for 'tis most excellent— Wealth, purity, fame, length of days, And to the skies its hearers raise” Canto XLV. The Quest Of The Amrit.
- **Translation**: 

---

### Verse 5 (Ramayan 0.205)
- **Original**: Canto XLV. The Quest Of The Amrit. 187 High and more high their wonder rose As the strange story reached its close, And thus, with LakshmaG, Ráma, best Of Raghu's sons, the saint addressed: “Most wondrous is the tale which thou Hast told of heavenly Gangá, how From realms above descending she Flowed through the land and filled the sea. In thinking o'er what thou hast said The night has like a moment fled, Whose hours in musing have been spent Upon thy words most excellent: So much, O holy Sage, thy lore Has charmed us with this tale of yore.” Day dawned. The morning rites were done And the victorious Raghu's son Addressed the sage in words like these, Rich in his long austerities: “The night is past: the morn is clear; Told is the tale so good to hear: Now o'er that river let us go, Three-pathed, the best of all that flow. This boat stands ready on the shore To bear the holy hermits o'er, Who of thy coming warned, in haste, The barge upon the bank have placed.” And Ku [ik's son approved his speech, And moving to the sandy beach, Placed in the boat the hermit band, And reached the river's further strand. On the north bank their feet they set, And greeted all the saints they met.
- **Translation**: 

---

### Verse 6 (Ramayan 0.206)
- **Original**: 188 The Ramayana On Gangá's shore they lighted down, And saw Vi[álá's lovely town. Thither, the princes by his side, The best of holy hermits hied. It was a town exceeding fair[057] That might with heaven itself compare. Then, suppliant palm to palm applied, Famed Ráma asked his holy guide: “O best of hermits, say what race Of monarchs rules this lovely place. Dear master, let my prayer prevail, For much I long to hear the tale.” Moved by his words, the saintly man Vi[álá's ancient tale began: “List, Ráma, list, with closest heed The tale of Indra's wondrous deed, And mark me as I truly tell What here in ancient days befell. Ere Krita's famous Age200 had fled, Strong were the sons of Diti201 bred; And Aditi's brave children too Were very mighty, good, and true. The rival brothers fierce and bold Were sons of Ka[yap lofty-souled. Of sister mothers born, they vied, Brood against brood, in jealous pride. Once, as they say, band met with band, And, joined in awful council, planned To live, unharmed by age and time, Immortal in their youthful prime. Then this was, after due debate, 200 The First or Golden Age. 201 Diti and Aditi were wives of Ka[yap, and mothers respectively of Titans and Gods.
- **Translation**: 

---

### Verse 7 (Ramayan 0.207)
- **Original**: Canto XLV. The Quest Of The Amrit. 189 The counsel of the wise and great, To churn with might the milky sea202 The life-bestowing drink to free. This planned, they seized the Serpent King, Vásuki, for their churning-string, And Mandar's mountain for their pole, And churned with all their heart and soul. As thus, a thousand seasons through, This way and that the snake they drew, Biting the rocks, each tortured head, A very deadly venom shed. Thence, bursting like a mighty flame, A pestilential poison came, Consuming, as it onward ran, The home of God, and fiend, and man. Then all the suppliant Gods in fear To Zankar,203 mighty lord, drew near. To Rudra, King of Herds, dismayed, “Save us, O save us, Lord!” they prayed. Then VishGu, bearing shell, and mace, And discus, showed his radiant face, And thus addressed in smiling glee The Trident wielding deity: “What treasure first the Gods upturn From troubled Ocean, as they churn, Should— for thou art the eldest— be Conferred, O best of Gods, on thee. Then come, and for thy birthright's sake, This venom as thy first fruits take.” He spoke, and vanished from their sight, When Ziva saw their wild affright, And heard his speech by whom is borne 202 One of the seven seas surrounding as many worlds in concentric rings. 203 Zankar and Rudra are names ofZiva.
- **Translation**: 

---

### Verse 8 (Ramayan 0.208)
- **Original**: 190 The Ramayana The mighty bow of bending horn,204 The poisoned flood at once he quaffed As 'twere the Amrit's heavenly draught. Then from the Gods departing went Ziva, the Lord pre-eminent. The host of Gods and Asurs still Kept churning with one heart and will. But Mandar's mountain, whirling round, Pierced to the depths below the ground. Then Gods and bards in terror flew To him who mighty Madhu slew. “Help of all beings! more than all, The Gods on thee for aid may call. Ward off, O mighty-armed! our fate, And bear up Mandar's threatening weight.” Then VishGu, as their need was sore, The semblance of a tortoise wore, And in the bed of Ocean lay The mountain on his back to stay. Then he, the soul pervading all, Whose locks in radiant tresses fall, One mighty arm extended still, And grasped the summit of the hill. So ranged among the Immortals, he Joined in the churning of the sea. 204 “ZárEgin, literallycarrying a bow of horn, is a constantly recurring name of VishGu. The Indians also, therefore, knew the art of making bows out of the hons of antelopes or wild goats, which Homer ascribes to the Trojans of the heroic age.” SCHLEGEL {FNS .
- **Translation**: 

---

### Verse 9 (Ramayan 0.209)
- **Original**: Canto XLV. The Quest Of The Amrit. 191 A thousand years had reached their close, When calmly from the ocean rose The gentle sage205 with staff and can, Lord of the art of healing man. Then as the waters foamed and boiled, As churning still the Immortals toiled, Of winning face and lovely frame, Forth sixty million fair ones came. Born of the foam and water, these Were aptly named Apsarases.206 [058] Each had her maids. The tongue would fail— So vast the throng— to count the tale. But when no God or Titan wooed A wife from all that multitude, Refused by all, they gave their love In common to the Gods above. Then from the sea still vext and wild Rose Surá,207 VaruG's maiden child. A fitting match she sought to find: But Diti's sons her love declined, 205 Dhanvantari, the physician of the Gods. 206 The poet plays upon the word and fancifully derives it fromapsu, the locative case plural ofap, water, andrasa, taste.… The word is probably derived fromap, water, andsri, to go, and seems to signifyinhabitants of the water, nymphs of the stream; or, as Goldstücker thinks (Dict. s.v.) these divinities were originally personifications of the vapours which are attracted by the sun and form into mist or clouds. 207 “Surá, in the feminine comprehends all sorts of intoxicating liquors, many kinds of which the Indians from the earliest times distilled and prepared from rice, sugar-cane, the palm tree, and various flowers and plants. Nothing is considered more disgraceful among orthodox Hindus than drunkenness, and the use of wine is forbidden not only to Bráhmans but the two other orders as well.… So it clearly appears derogatory to the dignity of the Gods to have received a nymph so pernicious, who ought rather to have been made over to the Titans. However the etymological fancy has prevailed. The wordSura, a God, is derived from the indeclinableSwar heaven.” SCHLEGEL {FNS .
- **Translation**: 

---

### Verse 10 (Ramayan 0.210)
- **Original**: 192 The Ramayana Their kinsmen of the rival brood To the pure maid in honour sued. Hence those who loved that nymph so fair The hallowed name of Suras bear. And Asurs are the Titan crowd Her gentle claims who disallowed. Then from the foamy sea was freed Uchchaih[ravas,208 the generous steed, And Kaustubha, of gems the gem,209 And Soma, Moon God, after them. At length when many a year had fled, Up floated, on her lotus bed, A maiden fair and tender-eyed, In the young flush of beauty's pride. She shone with pearl and golden sheen, And seals of glory stamped her queen, On each round arm glowed many a gem, On her smooth brows, a diadem. Rolling in waves beneath her crown The glory of her hair flowed down, Pearls on her neck of price untold, The lady shone like burnisht gold. Queen of the Gods, she leapt to land, A lotus in her perfect hand, And fondly, of the lotus-sprung, To lotus-bearing VishGu clung. 208 Literally, high-eared, the horse of Indra. Compare the production of the horse from the sea by Neptune. 209 “And Kaustubha the best Of gems that burns with living light Upon Lord VishGu's breast.” Churning of the Ocean.
- **Translation**: 

---

### Verse 11 (Ramayan 0.211)
- **Original**: Canto XLV. The Quest Of The Amrit. 193 Her Gods above and men below As Beauty's Queen and Fortune know.210 Gods, Titans, and the minstrel train Still churned and wrought the troubled main. At length the prize so madly sought, The Amrit, to their sight was brought. For the rich spoil, 'twixt these and those A fratricidal war arose, And, host 'gainst host in battle, set, Aditi's sons and Diti's met. United, with the giants' aid, Their fierce attack the Titans made, And wildly raged for many a day That universe-astounding fray. When wearied arms were faint to strike, And ruin threatened all alike, VishGu, with art's illusive aid, The Amrit from their sight conveyed. That Best of Beings smote his foes Who dared his deathless arm oppose: Yea, VishGu, all-pervading God, Beneath his feet the Titans trod Aditi's race, the sons of light, slew Diti's brood in cruel fight. 210 “That this story of the birth of Lakshmí is of considerable antiquity is evident from one of her namesKshírábdhi-tanayá, daughter of the Milky Sea, which is found inAmarasinha the most ancient of Indian lexicographers. The similarity to the Greek myth of Venus being born from the foam of the sea is remarkable.” “In this description of Lakshmí one thing only offends me, that she is said to have four arms. Each of VishGu's arms, single, as far as the elbow, there branches into two; but Lakshmí in all the brass seals that I possess or remember to have seen has two arms only. Nor does this deformity of redundant limbs suit the pattern of perfect beauty.” SCHLEGEL {FNS . I have omitted the offensive epithet.
- **Translation**: 

---

### Verse 12 (Ramayan 0.212)
- **Original**: 194 The Ramayana Then town-destroying211 Indra gained His empire, and in glory reigned O'er the three worlds with bard and sage Rejoicing in his heritage. Canto XLVI. Diti's Hope. But Diti, when her sons were slain, Wild with a childless mother's pain, To Ka[yap spake, Marícha's son, Her husband:“O thou glorious one![059] Dead are the children, mine no more, The mighty sons to thee I bore. Long fervour's meed, I crave a boy Whose arm may Indra's life destroy. The toil and pain my care shall be: To bless my hope depends on thee. Give me a mighty son to slay Fierce Indra, gracious lord! I pray.” 211 Purandhar, a common title of Indra.
- **Translation**: 

---

### Verse 13 (Ramayan 0.213)
- **Original**: Canto XLVI. Diti's Hope. 195 Then glorious Ka[yap thus replied To Diti, as she wept and sighed: “Thy prayer is heard, dear saint! Remain Pure from all spot, and thou shalt gain A son whose arm shall take the life Of Indra in the battle strife. For full a thousand years endure Free from all stain, supremely pure; Then shall thy son and mine appear, Whom the three worlds shall serve with fear.” These words the glorious Ka[yap said, Then gently stroked his consort's head, Blessed her, and bade a kind adieu, And turned him to his rites anew. Soon as her lord had left her side, Her bosom swelled with joy and pride. She sought the shade of holy boughs, And there began her awful vows. While yet she wrought her rites austere, Indra, unbidden, hastened near, With sweet observance tending her, A reverential minister. Wood, water, fire, and grass he brought, Sweet roots and woodland fruit he sought, And all her wants, the Thousand-eyed, With never-failing care, supplied, With tender love and soft caress Removing pain and weariness. When, of the thousand years ordained, Ten only unfulfilled remained, Thus to her son, the Thousand-eyed, The Goddess in her triumph cried: “Best of the mighty! there remain
- **Translation**: 

---

### Verse 14 (Ramayan 0.214)
- **Original**: 196 The Ramayana But ten short years of toil and pain; These years of penance soon will flee, And a new brother thou shalt see. Him for thy sake I'll nobly breed, And lust of war his soul shall feed; Then free from care and sorrow thou Shalt see the worlds before him bow.”212 Canto XLVII. Sumati. Thus to Lord Indra, Thousand-eyed, Softly beseeching Diti sighed. When but a blighted bud was left, Which Indra's hand in seven had cleft:213 “No fault, O Lord of Gods, is thine; The blame herein is only mine. But for one grace I fain would pray, As thou hast reft this hope away. This bud, O Indra, which a blight Has withered ere it saw the light— From this may seven fair spirits rise To rule the regions of the skies. Be theirs through heaven's unbounded space 212 A few verses are here left untranslated on account of the subject and language being offensive to modern taste. 213 “In this myth of Indra destroying the unborn fruit of Diti with his thun- derbolt, from which afterwards came the Maruts or Gods of Wind and Storm, geological phenomena are, it seems, represented under mythical images. In the great Mother of the Gods is, perhaps, figured the dry earth: Indra the God of thunder rends it open, and there issue from its rent bosom the Maruts or exhalations of the earth. But such ancient myths are difficult to interpret with absolute certainty.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 15 (Ramayan 0.215)
- **Original**: Canto XLVII. Sumati. 197 On shoulders of the winds to race, My children, drest in heavenly forms, Far-famed as Maruts, Gods of storms. One God to Brahmá's sphere assign, Let one, O Indra, watch o'er thine; And ranging through the lower air, The third the name of Váyu214 bear. Gods let the four remaining be, And roam through space, obeying thee.” The Town-destroyer, Thousand-eyed, Who smote fierce Bali till he died, Joined suppliant hands, and thus replied: “Thy children heavenly forms shall wear; The names devised by thee shall bear, And, Maruts called by my decree, Shall Amrit drink and wait on me. From fear and age and sickness freed, Through the three worlds their wings shall speed.” Thus in the hermits' holy shade Mother and son their compact made, And then, as fame relates, content, Home to the happy skies they went. This is the spot— so men have told— Where Lord Mahendra215 dwelt of old, This is the blessed region where His votaress mother claimed his care. Here gentle Alambúshá bare To old Ikshváku, king and sage, Vi[ála, glory of his age, By whom, a monarch void of guilt, Was this fair town Vi[álá built. [060] 214 Wind. 215 Indra, withmahá , great, prefixed.
- **Translation**: 

---

### Verse 16 (Ramayan 0.216)
- **Original**: 198 The Ramayana His son was Hemachandra, still Renowned for might and warlike skill. From him the great Suchandra came; His son, Dhúmrá[va, dear to fame. Next followed royal Srinjay; then Famed Sahadeva, lord of men. Next came Ku[á[va, good and mild, Whose son was Somadatta styled, And Sumati, his heir, the peer Of Gods above, now governs here. And ever through Ikshváku's grace, Vi[álá's kings, his noble race, Are lofty-souled, and blest with length Of days, with virtue, and with strength. This night, O prince, we here will sleep; And when the day begins to peep, Our onward way will take with thee, The king of Míthilá to see.” Then Sumati, the king, aware Of Vi[vámitra's advent there, Came quickly forth with honour meet The lofty-minded sage to greet. Girt with his priest and lords the king Did low obeisance, worshipping, With suppliant hands, with head inclined, Thus spoke he after question kind; “Since thou hast deigned to bless my sight, And grace awhile thy servant's seat, High fate is mine, great Anchorite, And none may with my bliss compete.”
- **Translation**: 

---

### Verse 17 (Ramayan 0.217)
- **Original**: Canto XLVIII. Indra And Ahalyá 199 Canto XLVIII. Indra And Ahalyá When mutual courtesies had past, Vi[álá's ruler spoke at last: “These princely youths, O Sage, who vie In might with children of the sky, Heroic, born for happy fate, With elephants' or lions' gait, Bold as the tiger or the bull, With lotus eyes so large and full, Armed with the quiver, sword, and bow, Whose figures like the A[vins216 show, Like children of the deathless Powers, Come freely to these shades of ours,217— How have they reached on foot this place? What do they seek, and what their race? As sun and moon adorn the sky, This spot the heroes glorify. Alike in stature, port, and mien, The same fair form in each is seen,” He spoke; and at the monarch's call The best of hermits told him all, How in the grove with him they dwelt, And slaughter to the demons dealt. Then wonder filled the monarch's breast, Who tended well each royal guest. Thus entertained, the princely pair Remained that night and rested there, And with the morn's returning ray To Mithilá pursued their way. 216 The Heavenly Twins. 217 Not banished from heaven as the inferior Gods and demigods sometimes were.
- **Translation**: 

---

### Verse 18 (Ramayan 0.218)
- **Original**: 200 The Ramayana When Janak's lovely city first Upon their sight, yet distant, burst, The hermits all with joyful cries Hailed the fair town that met their eyes. Then Ráma saw a holy wood, Close, in the city's neighbourhood, O'ergrown, deserted, marked by age, And thus addressed the mighty sage: “O reverend lord. I long to know What hermit dwelt here long ago.” Then to the prince his holy guide, Most eloquent of men, replied: “O Ráma, listen while I tell Whose was this grove, and what befell When in the fury of his rage The high saint cursed the hermitage. This was the grove— most lovely then— Of Gautam, O thou best of men, Like heaven itself, most honoured by The Gods who dwell above the sky. Here with Ahalyá at his side His fervid task the ascetic plied. Years fled in thousands. On a day It chanced the saint had gone away, When Town-destroying Indra came, And saw the beauty of the dame. The sage's form the God endued, And thus the fair Ahalyá wooed: “Love, sweet! should brook no dull delay But snatch the moments when he may.” She knew him in the saint's disguise, Lord Indra of the Thousand Eyes, But touched by love's unholy fire, She yielded to the God's desire.
- **Translation**: 

---

### Verse 19 (Ramayan 0.219)
- **Original**: Canto XLVIII. Indra And Ahalyá 201 “Now, Lord of Gods!” she whispered,“flee, From Gautam save thyself and me.” Trembling with doubt and wild with dread Lord Indra from the cottage fled; But fleeing in the grove he met The home-returning anchoret, Whose wrath the Gods and fiends would shun, Such power his fervent rites had won. Fresh from the lustral flood he came, In splendour like the burning flame, With fuel for his sacred rites, And grass, the best of eremites. The Lord of Gods was sad of cheer To see the mighty saint so near, And when the holy hermit spied In hermit's garb the Thousand-eyed, [061] He knew the whole, his fury broke Forth on the sinner as he spoke: “Because my form thou hast assumed, And wrought this folly, thou art doomed, For this my curse to thee shall cling, Henceforth a sad and sexless thing.” No empty threat that sentence came, It chilled his soul and marred his frame, His might and godlike vigour fled, And every nerve was cold and dead. Then on his wife his fury burst, And thus the guilty dame he cursed: “For countless years, disloyal spouse, Devoted to severest vows, Thy bed the ashes, air thy food, Here shalt thou live in solitude.
- **Translation**: 

---

### Verse 20 (Ramayan 0.220)
- **Original**: 202 The Ramayana This lonely grove thy home shall be, And not an eye thy form shall see. When Ráma, Da [aratha's child, Shall seek these shades then drear and wild, His coming shall remove thy stain, And make the sinner pure again. Due honour paid to him, thy guest, Shall cleanse thy fond and erring breast, Thee to my side in bliss restore, And give thy proper shape once more.”218 Thus to his guilty wife he said, Then far the holy Gautam fled, And on Himálaya's lovely heights Spent the long years in sternest rites.” Canto XLIX. Ahalyá Freed. Then Ráma, following still his guide, Within the grove, with LakshmaG, hied, Her vows a wondrous light had lent To that illustrious penitent. He saw the glorious lady, screened From eye of man, and God, and fiend, Like some bright portent which the care 218 Kumárila says:“In the same manner, if it is said that Indra was the seducer of Ahalyá this does not imply that the God Indra committed such a crime, but Indra means the sun, and Ahalyá (from ahan and lí) the night; and as the night is seduced and ruined by the sun of the morning, therefore is Indra called the paramour of Ahalyá.” M AX M ULLER {FNS , History of Ancient Sanskrit Literature, p. 530.
- **Translation**: 

---

