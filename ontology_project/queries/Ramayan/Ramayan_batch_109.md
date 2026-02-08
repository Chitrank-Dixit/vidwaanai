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

### Verse 1 (Ramayana 0.206)
- **Original**: 188 The Ramayana On Gangá's shore they lighted down, And saw Vi[álá's lovely town. Thither, the princes by his side, The best of holy hermits hied. It was a town exceeding fair[057] That might with heaven itself compare. Then, suppliant palm to palm applied, Famed Ráma asked his holy guide: “O best of hermits, say what race Of monarchs rules this lovely place. Dear master, let my prayer prevail, For much I long to hear the tale.” Moved by his words, the saintly man Vi[álá's ancient tale began: “List, Ráma, list, with closest heed The tale of Indra's wondrous deed, And mark me as I truly tell What here in ancient days befell. Ere Krita's famous Age200 had fled, Strong were the sons of Diti201 bred; And Aditi's brave children too Were very mighty, good, and true. The rival brothers fierce and bold Were sons of Ka[yap lofty-souled. Of sister mothers born, they vied, Brood against brood, in jealous pride. Once, as they say, band met with band, And, joined in awful council, planned To live, unharmed by age and time, Immortal in their youthful prime. Then this was, after due debate, 200 The First or Golden Age. 201 Diti and Aditi were wives of Ka[yap, and mothers respectively of Titans and Gods.
- **Translation**: 

---

### Verse 2 (Ramayana 0.207)
- **Original**: Canto XLV. The Quest Of The Amrit. 189 The counsel of the wise and great, To churn with might the milky sea202 The life-bestowing drink to free. This planned, they seized the Serpent King, Vásuki, for their churning-string, And Mandar's mountain for their pole, And churned with all their heart and soul. As thus, a thousand seasons through, This way and that the snake they drew, Biting the rocks, each tortured head, A very deadly venom shed. Thence, bursting like a mighty flame, A pestilential poison came, Consuming, as it onward ran, The home of God, and fiend, and man. Then all the suppliant Gods in fear To Zankar,203 mighty lord, drew near. To Rudra, King of Herds, dismayed, “Save us, O save us, Lord!” they prayed. Then VishGu, bearing shell, and mace, And discus, showed his radiant face, And thus addressed in smiling glee The Trident wielding deity: “What treasure first the Gods upturn From troubled Ocean, as they churn, Should— for thou art the eldest— be Conferred, O best of Gods, on thee. Then come, and for thy birthright's sake, This venom as thy first fruits take.” He spoke, and vanished from their sight, When Ziva saw their wild affright, And heard his speech by whom is borne 202 One of the seven seas surrounding as many worlds in concentric rings. 203 Zankar and Rudra are names ofZiva.
- **Translation**: 

---

### Verse 3 (Ramayana 0.208)
- **Original**: 190 The Ramayana The mighty bow of bending horn,204 The poisoned flood at once he quaffed As 'twere the Amrit's heavenly draught. Then from the Gods departing went Ziva, the Lord pre-eminent. The host of Gods and Asurs still Kept churning with one heart and will. But Mandar's mountain, whirling round, Pierced to the depths below the ground. Then Gods and bards in terror flew To him who mighty Madhu slew. “Help of all beings! more than all, The Gods on thee for aid may call. Ward off, O mighty-armed! our fate, And bear up Mandar's threatening weight.” Then VishGu, as their need was sore, The semblance of a tortoise wore, And in the bed of Ocean lay The mountain on his back to stay. Then he, the soul pervading all, Whose locks in radiant tresses fall, One mighty arm extended still, And grasped the summit of the hill. So ranged among the Immortals, he Joined in the churning of the sea. 204 “ZárEgin, literallycarrying a bow of horn, is a constantly recurring name of VishGu. The Indians also, therefore, knew the art of making bows out of the hons of antelopes or wild goats, which Homer ascribes to the Trojans of the heroic age.” SCHLEGEL {FNS .
- **Translation**: 

---

### Verse 4 (Ramayana 0.209)
- **Original**: Canto XLV. The Quest Of The Amrit. 191 A thousand years had reached their close, When calmly from the ocean rose The gentle sage205 with staff and can, Lord of the art of healing man. Then as the waters foamed and boiled, As churning still the Immortals toiled, Of winning face and lovely frame, Forth sixty million fair ones came. Born of the foam and water, these Were aptly named Apsarases.206 [058] Each had her maids. The tongue would fail— So vast the throng— to count the tale. But when no God or Titan wooed A wife from all that multitude, Refused by all, they gave their love In common to the Gods above. Then from the sea still vext and wild Rose Surá,207 VaruG's maiden child. A fitting match she sought to find: But Diti's sons her love declined, 205 Dhanvantari, the physician of the Gods. 206 The poet plays upon the word and fancifully derives it fromapsu, the locative case plural ofap, water, andrasa, taste.… The word is probably derived fromap, water, andsri, to go, and seems to signifyinhabitants of the water, nymphs of the stream; or, as Goldstücker thinks (Dict. s.v.) these divinities were originally personifications of the vapours which are attracted by the sun and form into mist or clouds. 207 “Surá, in the feminine comprehends all sorts of intoxicating liquors, many kinds of which the Indians from the earliest times distilled and prepared from rice, sugar-cane, the palm tree, and various flowers and plants. Nothing is considered more disgraceful among orthodox Hindus than drunkenness, and the use of wine is forbidden not only to Bráhmans but the two other orders as well.… So it clearly appears derogatory to the dignity of the Gods to have received a nymph so pernicious, who ought rather to have been made over to the Titans. However the etymological fancy has prevailed. The wordSura, a God, is derived from the indeclinableSwar heaven.” SCHLEGEL {FNS .
- **Translation**: 

---

### Verse 5 (Ramayana 0.210)
- **Original**: 192 The Ramayana Their kinsmen of the rival brood To the pure maid in honour sued. Hence those who loved that nymph so fair The hallowed name of Suras bear. And Asurs are the Titan crowd Her gentle claims who disallowed. Then from the foamy sea was freed Uchchaih[ravas,208 the generous steed, And Kaustubha, of gems the gem,209 And Soma, Moon God, after them. At length when many a year had fled, Up floated, on her lotus bed, A maiden fair and tender-eyed, In the young flush of beauty's pride. She shone with pearl and golden sheen, And seals of glory stamped her queen, On each round arm glowed many a gem, On her smooth brows, a diadem. Rolling in waves beneath her crown The glory of her hair flowed down, Pearls on her neck of price untold, The lady shone like burnisht gold. Queen of the Gods, she leapt to land, A lotus in her perfect hand, And fondly, of the lotus-sprung, To lotus-bearing VishGu clung. 208 Literally, high-eared, the horse of Indra. Compare the production of the horse from the sea by Neptune. 209 “And Kaustubha the best Of gems that burns with living light Upon Lord VishGu's breast.” Churning of the Ocean.
- **Translation**: 

---

### Verse 6 (Ramayana 0.211)
- **Original**: Canto XLV. The Quest Of The Amrit. 193 Her Gods above and men below As Beauty's Queen and Fortune know.210 Gods, Titans, and the minstrel train Still churned and wrought the troubled main. At length the prize so madly sought, The Amrit, to their sight was brought. For the rich spoil, 'twixt these and those A fratricidal war arose, And, host 'gainst host in battle, set, Aditi's sons and Diti's met. United, with the giants' aid, Their fierce attack the Titans made, And wildly raged for many a day That universe-astounding fray. When wearied arms were faint to strike, And ruin threatened all alike, VishGu, with art's illusive aid, The Amrit from their sight conveyed. That Best of Beings smote his foes Who dared his deathless arm oppose: Yea, VishGu, all-pervading God, Beneath his feet the Titans trod Aditi's race, the sons of light, slew Diti's brood in cruel fight. 210 “That this story of the birth of Lakshmí is of considerable antiquity is evident from one of her namesKshírábdhi-tanayá, daughter of the Milky Sea, which is found inAmarasinha the most ancient of Indian lexicographers. The similarity to the Greek myth of Venus being born from the foam of the sea is remarkable.” “In this description of Lakshmí one thing only offends me, that she is said to have four arms. Each of VishGu's arms, single, as far as the elbow, there branches into two; but Lakshmí in all the brass seals that I possess or remember to have seen has two arms only. Nor does this deformity of redundant limbs suit the pattern of perfect beauty.” SCHLEGEL {FNS . I have omitted the offensive epithet.
- **Translation**: 

---

### Verse 7 (Ramayana 0.212)
- **Original**: 194 The Ramayana Then town-destroying211 Indra gained His empire, and in glory reigned O'er the three worlds with bard and sage Rejoicing in his heritage. Canto XLVI. Diti's Hope. But Diti, when her sons were slain, Wild with a childless mother's pain, To Ka[yap spake, Marícha's son, Her husband:“O thou glorious one![059] Dead are the children, mine no more, The mighty sons to thee I bore. Long fervour's meed, I crave a boy Whose arm may Indra's life destroy. The toil and pain my care shall be: To bless my hope depends on thee. Give me a mighty son to slay Fierce Indra, gracious lord! I pray.” 211 Purandhar, a common title of Indra.
- **Translation**: 

---

### Verse 8 (Ramayana 0.213)
- **Original**: Canto XLVI. Diti's Hope. 195 Then glorious Ka[yap thus replied To Diti, as she wept and sighed: “Thy prayer is heard, dear saint! Remain Pure from all spot, and thou shalt gain A son whose arm shall take the life Of Indra in the battle strife. For full a thousand years endure Free from all stain, supremely pure; Then shall thy son and mine appear, Whom the three worlds shall serve with fear.” These words the glorious Ka[yap said, Then gently stroked his consort's head, Blessed her, and bade a kind adieu, And turned him to his rites anew. Soon as her lord had left her side, Her bosom swelled with joy and pride. She sought the shade of holy boughs, And there began her awful vows. While yet she wrought her rites austere, Indra, unbidden, hastened near, With sweet observance tending her, A reverential minister. Wood, water, fire, and grass he brought, Sweet roots and woodland fruit he sought, And all her wants, the Thousand-eyed, With never-failing care, supplied, With tender love and soft caress Removing pain and weariness. When, of the thousand years ordained, Ten only unfulfilled remained, Thus to her son, the Thousand-eyed, The Goddess in her triumph cried: “Best of the mighty! there remain
- **Translation**: 

---

### Verse 9 (Ramayana 0.214)
- **Original**: 196 The Ramayana But ten short years of toil and pain; These years of penance soon will flee, And a new brother thou shalt see. Him for thy sake I'll nobly breed, And lust of war his soul shall feed; Then free from care and sorrow thou Shalt see the worlds before him bow.”212 Canto XLVII. Sumati. Thus to Lord Indra, Thousand-eyed, Softly beseeching Diti sighed. When but a blighted bud was left, Which Indra's hand in seven had cleft:213 “No fault, O Lord of Gods, is thine; The blame herein is only mine. But for one grace I fain would pray, As thou hast reft this hope away. This bud, O Indra, which a blight Has withered ere it saw the light— From this may seven fair spirits rise To rule the regions of the skies. Be theirs through heaven's unbounded space 212 A few verses are here left untranslated on account of the subject and language being offensive to modern taste. 213 “In this myth of Indra destroying the unborn fruit of Diti with his thun- derbolt, from which afterwards came the Maruts or Gods of Wind and Storm, geological phenomena are, it seems, represented under mythical images. In the great Mother of the Gods is, perhaps, figured the dry earth: Indra the God of thunder rends it open, and there issue from its rent bosom the Maruts or exhalations of the earth. But such ancient myths are difficult to interpret with absolute certainty.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 10 (Ramayana 0.215)
- **Original**: Canto XLVII. Sumati. 197 On shoulders of the winds to race, My children, drest in heavenly forms, Far-famed as Maruts, Gods of storms. One God to Brahmá's sphere assign, Let one, O Indra, watch o'er thine; And ranging through the lower air, The third the name of Váyu214 bear. Gods let the four remaining be, And roam through space, obeying thee.” The Town-destroyer, Thousand-eyed, Who smote fierce Bali till he died, Joined suppliant hands, and thus replied: “Thy children heavenly forms shall wear; The names devised by thee shall bear, And, Maruts called by my decree, Shall Amrit drink and wait on me. From fear and age and sickness freed, Through the three worlds their wings shall speed.” Thus in the hermits' holy shade Mother and son their compact made, And then, as fame relates, content, Home to the happy skies they went. This is the spot— so men have told— Where Lord Mahendra215 dwelt of old, This is the blessed region where His votaress mother claimed his care. Here gentle Alambúshá bare To old Ikshváku, king and sage, Vi[ála, glory of his age, By whom, a monarch void of guilt, Was this fair town Vi[álá built. [060] 214 Wind. 215 Indra, withmahá , great, prefixed.
- **Translation**: 

---

### Verse 11 (Ramayana 0.216)
- **Original**: 198 The Ramayana His son was Hemachandra, still Renowned for might and warlike skill. From him the great Suchandra came; His son, Dhúmrá[va, dear to fame. Next followed royal Srinjay; then Famed Sahadeva, lord of men. Next came Ku[á[va, good and mild, Whose son was Somadatta styled, And Sumati, his heir, the peer Of Gods above, now governs here. And ever through Ikshváku's grace, Vi[álá's kings, his noble race, Are lofty-souled, and blest with length Of days, with virtue, and with strength. This night, O prince, we here will sleep; And when the day begins to peep, Our onward way will take with thee, The king of Míthilá to see.” Then Sumati, the king, aware Of Vi[vámitra's advent there, Came quickly forth with honour meet The lofty-minded sage to greet. Girt with his priest and lords the king Did low obeisance, worshipping, With suppliant hands, with head inclined, Thus spoke he after question kind; “Since thou hast deigned to bless my sight, And grace awhile thy servant's seat, High fate is mine, great Anchorite, And none may with my bliss compete.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.217)
- **Original**: Canto XLVIII. Indra And Ahalyá 199 Canto XLVIII. Indra And Ahalyá When mutual courtesies had past, Vi[álá's ruler spoke at last: “These princely youths, O Sage, who vie In might with children of the sky, Heroic, born for happy fate, With elephants' or lions' gait, Bold as the tiger or the bull, With lotus eyes so large and full, Armed with the quiver, sword, and bow, Whose figures like the A[vins216 show, Like children of the deathless Powers, Come freely to these shades of ours,217— How have they reached on foot this place? What do they seek, and what their race? As sun and moon adorn the sky, This spot the heroes glorify. Alike in stature, port, and mien, The same fair form in each is seen,” He spoke; and at the monarch's call The best of hermits told him all, How in the grove with him they dwelt, And slaughter to the demons dealt. Then wonder filled the monarch's breast, Who tended well each royal guest. Thus entertained, the princely pair Remained that night and rested there, And with the morn's returning ray To Mithilá pursued their way. 216 The Heavenly Twins. 217 Not banished from heaven as the inferior Gods and demigods sometimes were.
- **Translation**: 

---

### Verse 13 (Ramayana 0.218)
- **Original**: 200 The Ramayana When Janak's lovely city first Upon their sight, yet distant, burst, The hermits all with joyful cries Hailed the fair town that met their eyes. Then Ráma saw a holy wood, Close, in the city's neighbourhood, O'ergrown, deserted, marked by age, And thus addressed the mighty sage: “O reverend lord. I long to know What hermit dwelt here long ago.” Then to the prince his holy guide, Most eloquent of men, replied: “O Ráma, listen while I tell Whose was this grove, and what befell When in the fury of his rage The high saint cursed the hermitage. This was the grove— most lovely then— Of Gautam, O thou best of men, Like heaven itself, most honoured by The Gods who dwell above the sky. Here with Ahalyá at his side His fervid task the ascetic plied. Years fled in thousands. On a day It chanced the saint had gone away, When Town-destroying Indra came, And saw the beauty of the dame. The sage's form the God endued, And thus the fair Ahalyá wooed: “Love, sweet! should brook no dull delay But snatch the moments when he may.” She knew him in the saint's disguise, Lord Indra of the Thousand Eyes, But touched by love's unholy fire, She yielded to the God's desire.
- **Translation**: 

---

### Verse 14 (Ramayana 0.219)
- **Original**: Canto XLVIII. Indra And Ahalyá 201 “Now, Lord of Gods!” she whispered,“flee, From Gautam save thyself and me.” Trembling with doubt and wild with dread Lord Indra from the cottage fled; But fleeing in the grove he met The home-returning anchoret, Whose wrath the Gods and fiends would shun, Such power his fervent rites had won. Fresh from the lustral flood he came, In splendour like the burning flame, With fuel for his sacred rites, And grass, the best of eremites. The Lord of Gods was sad of cheer To see the mighty saint so near, And when the holy hermit spied In hermit's garb the Thousand-eyed, [061] He knew the whole, his fury broke Forth on the sinner as he spoke: “Because my form thou hast assumed, And wrought this folly, thou art doomed, For this my curse to thee shall cling, Henceforth a sad and sexless thing.” No empty threat that sentence came, It chilled his soul and marred his frame, His might and godlike vigour fled, And every nerve was cold and dead. Then on his wife his fury burst, And thus the guilty dame he cursed: “For countless years, disloyal spouse, Devoted to severest vows, Thy bed the ashes, air thy food, Here shalt thou live in solitude.
- **Translation**: 

---

### Verse 15 (Ramayana 0.220)
- **Original**: 202 The Ramayana This lonely grove thy home shall be, And not an eye thy form shall see. When Ráma, Da [aratha's child, Shall seek these shades then drear and wild, His coming shall remove thy stain, And make the sinner pure again. Due honour paid to him, thy guest, Shall cleanse thy fond and erring breast, Thee to my side in bliss restore, And give thy proper shape once more.”218 Thus to his guilty wife he said, Then far the holy Gautam fled, And on Himálaya's lovely heights Spent the long years in sternest rites.” Canto XLIX. Ahalyá Freed. Then Ráma, following still his guide, Within the grove, with LakshmaG, hied, Her vows a wondrous light had lent To that illustrious penitent. He saw the glorious lady, screened From eye of man, and God, and fiend, Like some bright portent which the care 218 Kumárila says:“In the same manner, if it is said that Indra was the seducer of Ahalyá this does not imply that the God Indra committed such a crime, but Indra means the sun, and Ahalyá (from ahan and lí) the night; and as the night is seduced and ruined by the sun of the morning, therefore is Indra called the paramour of Ahalyá.” M AX M ULLER {FNS , History of Ancient Sanskrit Literature, p. 530.
- **Translation**: 

---

### Verse 16 (Ramayana 0.221)
- **Original**: Canto XLIX. Ahalyá Freed. 203 Of Brahmá launches through the air, Designed by his illusive art To flash a moment and depart: Or like the flame that leaps on high To sink involved in smoke and die: Or like the full moon shining through The wintry mist, then lost to view: Or like the sun's reflection, cast Upon the flood, too bright to last: So was the glorious dame till then Removed from Gods' and mortals' ken, Till— such was Gautam's high decree— Prince Ráma came to set her free. Then, with great joy that dame to meet, The sons of Raghu clapped her feet; And she, remembering Gautam's oath, With gentle grace received them both; Then water for their feet she gave, Guest-gift, and all that strangers crave. The prince, of courteous rule aware, Received, as meet, the lady's care. Then flowers came down in copious rain, And moving to the heavenly strain Of music in the skies that rang, The nymphs and minstrels danced and sang: And all the Gods with one glad voice Praised the great dame, and cried,“Rejoice! Through fervid rites no more defiled, But with thy husband reconciled.” Gautam, the holy hermit knew— For naught escaped his godlike view— That Ráma lodged beneath that shade,
- **Translation**: 

---

### Verse 17 (Ramayana 0.222)
- **Original**: 204 The Ramayana And hasting there his homage paid. He took Ahalyá to his side, From sin and folly purified, And let his new-found consort bear In his austerities a share. Then Ráma, pride of Raghu's race, Welcomed by Gautam, face to face, Who every highest honour showed, To Mithilá pursued his road. Canto L. Janak. The sons of Raghu journeyed forth, Bending their steps 'twixt east and north. Soon, guided by the sage, they found, Enclosed, a sacrificial ground. Then to the best of saints, his guide, In admiration Ráma cried: “The high-souled king no toil has spared, But nobly for his rite prepared, How many thousand Bráhmans here, From every region, far and near, Well read in holy lore, appear! How many tents, that sages screen, With wains in hundreds, here are seen! Great Bráhman, let us find a place Where we may stay and rest a space.” The hermit did as Ráma prayed, And in a spot his lodging made,[062] Far from the crowd, sequestered, clear, With copious water flowing near.
- **Translation**: 

---

### Verse 18 (Ramayana 0.223)
- **Original**: Canto L. Janak. 205 Then Janak, best of kings, aware Of Vi[vámitra lodging there, With Zatánanda for his guide— The priest on whom he most relied, His chaplain void of guile and stain— And others of his priestly train, Bearing the gift that greets the guest, To meet him with all honour pressed. The saint received with gladsome mind Each honour and observance kind: Then of his health he asked the king, And how his rites were prospering, Janak, with chaplain and with priest, Addressed the hermits, chief and least, Accosting all, in due degree, With proper words of courtesy. Then, with his palms together laid, The king his supplication made: “Deign, reverend lord, to sit thee down With these good saints of high renown.” Then sate the chief of hermits there, Obedient to the monarch's prayer. Chaplain and priest, and king and peer, Sate in their order, far or near. Then thus the king began to say: “The Gods have blest my rite to-day, And with the sight of thee repaid The preparations I have made. Grateful am I, so highly blest, That thou, of saints the holiest, Hast come, O Bráhman, here with all These hermits to the festival. Twelve days, O Bráhman Sage, remain— For so the learned priests ordain—
- **Translation**: 

---

### Verse 19 (Ramayana 0.224)
- **Original**: 206 The Ramayana And then, O heir of Ku[ik's name, The Gods will come their dues to claim.” With looks that testified delight Thus spake he to the anchorite, Then with his suppliant hands upraised, He asked, as earnestly he gazed: “These princely youths, O Sage, who vie In might with children of the sky, Heroic, born for happy fate, With elephants' or lions' gait, Bold as the tiger and the bull, With lotus eyes so large and full, Armed with the quiver, sword and bow, Whose figures like the A[vins show, Like children of the heavenly Powers, Come freely to these shades of ours,— How have they reached on foot this place? What do they seek, and what their race? As sun and moon adorn the sky, This spot the heroes glorify: Alike in stature, port, and mien, The same fair form in each is seen.”219 Thus spoke the monarch, lofty-souled, The saint, of heart unfathomed, told How, sons of Da[aratha, they Accompanied his homeward way, How in the hermitage they dwelt, And slaughter to the demons dealt: Their journey till the spot they neared 219 “The preceding sixteen lines have occurred before in Canto XLVIII. This Homeric custom of repeating a passage of several lines is strange to our poet. This is the only instance I remember. The repetition of single lines is common enough.” SCHLEGEL {FNS .
- **Translation**: 

---

### Verse 20 (Ramayana 0.225)
- **Original**: Canto LI. Visvámitra. 207 Whence fair Vi[álá's towers appeared: Ahalyá seen and freed from taint; Their meeting with her lord the saint; And how they thither came, to know The virtue of the famous bow. Thus Vi[vámitra spoke the whole To royal Janak, great of soul, And when this wondrous tale was o'er, The glorious hermit said no more. Canto LI. Visvámitra. Wise Vi[vámitra's tale was done: Then sainted Gautam's eldest son, GreatZatánanda, far-renowned, Whom long austerities had crowned With glory— as the news he heard The down upon his body stirred,— Filled full of wonder at the sight Of Ráma, felt supreme delight. When Zatánanda saw the pair Of youthful princes seated there, He turned him to the holy man Who sate at ease, and thus began: “And didst thou, mighty Sage, in truth Show clearly to this royal youth My mother, glorious far and wide, Whom penance-rites have sanctified? And did my glorious mother— she, Heiress of noble destiny—
- **Translation**: 

---

