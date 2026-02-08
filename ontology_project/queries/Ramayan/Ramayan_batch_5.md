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

### Verse 1 (Ramayan 0.81)
- **Original**: Canto XI. The Sacrifice Decreed. 63 Obedient to his lord's behest Away Sumantra sped, And brought Va[ishmha and the rest, In Scripture deeply read. Suyajùa, Vámadeva came, Jávali, Ka[yap's son, And old Va[ishmha, dear to fame, Obedient every one. King Da[aratha met them there And duly honoured each, And spoke in pleasant words his fair And salutary speech: “In childless longing doomed to pine, No happiness, O lords, is mine. So have I for this cause decreed To slay the sacrificial steed. Fain would I pay that offering high Wherein the horse is doomed to die, With Rishya[ring his aid to lend, And with your glory to befriend.” With loud applause each holy man Received his speech, approved the plan, And, by the wise Va[ishmha led, Gave praises to the king, and said: “The sons thou cravest shalt thou see, Of fairest glory, born to thee, Whose holy feelings bid thee take This righteous course for offspring's sake.” Cheered by the ready praise of those Whose aid he sought, his spirits rose, And thus the king his speech renewed With looks of joy and gratitude: “Let what the coming rites require Be ready as the priests desire,
- **Translation**: 

---

### Verse 2 (Ramayan 0.82)
- **Original**: 64 The Ramayana And let the horse, ordained to bleed, With fitting guard and priest, be freed,86 Yonder on Sarjú's northern side The sacrificial ground provide; And let the saving rites, that naught Ill-omened may occur, be wrought. The offering I announce to-day Each lord of earth may claim to pay, Provided that his care can guard The holy rite by flaws unmarred. For wandering fiends, whose watchful spite Waits eagerly to spoil each rite, Hunting with keenest eye detect The slightest slip, the least neglect; And when the sacred work is crossed The workman is that moment lost. Let preparation due be made: Your powers the charge can meet: That so the noble rite be paid In every point complete.” And all the Bráhmans answered, Yea, His mandate honouring, And gladly promised to obey The order of the king. They cried with voices raised aloud: “Success attend thine aim!” Then bade farewell, and lowly bowed, And hastened whence they came. King Da[aratha went within, His well loved wives to see: And said:“Your lustral rites begin, 86 It was essential that the horse should wander free for a year before immo- lation, as a sign that his master's paramount sovereignty was acknowledged by all neighbouring princes.
- **Translation**: 

---

### Verse 3 (Ramayan 0.83)
- **Original**: Canto XII. The Sacrifice Begun. 65 For these shall prosper me. A glorious offering I prepare That precious fruit of sons may bear.” Their lily faces brightened fast Those pleasant words to hear, As lilies, when the winter's past, In lovelier hues appear. Canto XII. The Sacrifice Begun. Again the spring with genial heat Returning made the year complete. To win him sons, without delay His vow the king resolved to pay: And to Va[ishmha, saintly man, In modest words this speech began: “Prepare the rite with all things fit As is ordained in Holy Writ, And keep with utmost care afar Whate'er its sacred forms might mar. Thou art, my lord, my trustiest guide, Kind-hearted, and my friend beside; So is it meet thou undertake This heavy task for duty's sake.” Then he, of twice-born men the best, His glad assent at once expressed: “Fain will I do whate'er may be Desired, O honoured King, by thee.” To ancient priests he spoke, who, trained In holy rites, deep skill had gained: “Here guards be stationed, good and sage
- **Translation**: 

---

### Verse 4 (Ramayan 0.84)
- **Original**: 66 The Ramayana Religious men of trusted age. And various workmen send and call, Who frame the door and build the wall: With men of every art and trade, Who read the stars and ply the spade,[021] And mimes and minstrels hither bring, And damsels trained to dance and sing.” Then to the learned men he said, In many a page of Scripture read: “Be yours each rite performed to see According to the king's decree. And stranger Bráhmans quickly call To this great rite that welcomes all. Pavilions for the princes, decked With art and ornament, erect, And handsome booths by thousands made The Bráhman visitors to shade, Arranged in order side by side, With meat and drink and all supplied. And ample stables we shall need For many an elephant and steed: And chambers where the men may lie, And vast apartments, broad and high, Fit to receive the countless bands Of warriors come from distant lands. For our own people too provide Sufficient tents, extended wide, And stores of meat and drink prepare, And all that can be needed there. And food in plenty must be found For guests from all the country round. Of various viands presents make, For honour, not for pity's sake, That fit regard and worship be
- **Translation**: 

---

### Verse 5 (Ramayan 0.85)
- **Original**: Canto XII. The Sacrifice Begun. 67 Paid to each caste in due degree. And let not wish or wrath excite Your hearts the meanest guest to slight; But still observe with special grace Those who obtain the foremost place, Whether for happier skill in art Or bearing in the rite their part. Do you, I pray, with friendly mind Perform the task to you assigned, And work the rite, as bids the law, Without omission, slip, or flaw” They answered:“As thou seest fit So will we do and naught omit.” The sage Va[icmha then addressed Sumantra called at his behest: “The princes of the earth invite, And famous lords who guard the rite, Priest, Warrior, Merchant, lowly thrall, In countless thousands summon all. Where'er their home be, far or near, Gather the good with honour here, And Janak, whose imperial sway The men of Míthilá87 obey. The firm of vow, the dread of foes, Who all the lore of Scripture knows, Invite him here with honour high, King Da[aratha's old ally. And Ká [i's88 lord of gentle speech, Who finds a pleasant word for each, 87 Called also Vidcha, later Tirabhukti, corrupted into the modern Tirhut, a province bounded on the west and east by the Gaudakí and Kau[ikí rivers, on the south by the Ganges, and on the north by the skirts of the Himálayas. 88 The celebrated city of Benares. See Dr. Hall's learned and exhaustive Monograph in theSacred City of the Hindus, by the Rev. M. A. Sherring.
- **Translation**: 

---

### Verse 6 (Ramayan 0.86)
- **Original**: 68 The Ramayana In length of days our monarch's peer, Illustrious king, invite him here. The father of our ruler's bride, Known for his virtues far and wide, The king whom Kekaya's89 realms obey, Him with his son invite, I pray. And Lomapád the Angas' king, True to his vows and godlike, bring. For be thine invitations sent To west and south and orient. Call those who rule Suráshmra's90 land, Suvíra's91 realm and Sindhu's strand, And all the kings of earth beside In friendship's bonds with us allied: Invite them all to hasten in With retinue and kith and kin.” Va [ishmha's speech without delay Sumantra bent him to obey. And sent his trusty envoys forth Eastward and westward, south and north. Obedient to the saint's request Himself he hurried forth, and pressed Each nobler chief and lord and king To hasten to the gathering. Before the saint Va[ishmha stood All those who wrought with stone and wood, And showed the work which every one In furtherance of the rite had done, Rejoiced their ready zeal to see, Thus to the craftsmen all said he: 89 Kekaya is supposed to have been in the Panjáb. The name of the king was A [vapati (Lord of Horses), father of Da[aratha's wife Kaikeyí. 90 Surat. 91 Apparently in the west of India not far from the Indus.
- **Translation**: 

---

### Verse 7 (Ramayan 0.87)
- **Original**: Canto XIII. The Sacrifice Finished. 69 “I charge ye, masters, see to this, That there be nothing done amiss, And this, I pray, in mind be borne, That not one gift ye give in scorn: Whenever scorn a gift attends Great sin is his who thus offends.” And now some days and nights had past, And kings began to gather fast, And precious gems in liberal store As gifts to Da[aratha bore. Then joy thrilled through Va[ishmha's breast As thus the monarch he addressed: “Obedient to thy high decree The kings, my lord, are come to thee. [022] And it has been my care to greet And honour all with reverence meet. Thy servants' task is ended quite, And all is ready for the rite. Come forth then to the sacred ground Where all in order will be found.” Then Rishya[ring confirmed the tale: Nor did their words to move him fail. The stars propitious influence lent When forth the world's great ruler went. Then by the sage Va[ishmha led The priest begun to speed Those glorious rites wherein is shed The lifeblood of the steed. Canto XIII. The Sacrifice Finished.
- **Translation**: 

---

### Verse 8 (Ramayan 0.88)
- **Original**: 70 The Ramayana The circling year had filled its course, And back was brought the wandering horse: Then upon Sarjú's northern strand Began the rite the king had planned. With Rishya[ring the forms to guide, The Bráhmans to their task applied, At that great offering of the steed Their lofty-minded king decreed. The priests, who all the Scripture knew, Performed their part in order due, And circled round in solemn train As precepts of the law ordain. Pravargya rites92 were duly sped: For Upasads93 the flames were fed. Then from the plant94 the juice was squeezed, And those high saints with minds well pleased Performed the mystic rites begun With bathing ere the rise of sun They gave the portion Indra's claim, And hymned the King whom none can blame. The mid-day bathing followed next, Observed as bids the holy text. Then the good priests with utmost care, In form that Scripture's rules declare, 92 “The Pravargya ceremony lasts for three days, and is always performed twice a day, in the forenoon and afternoon. It precedes the animal and Soma sacrifices. For without having undergone it, no one is allowed to take part in the solemn Soma feast prepared for the gods.” Haug'sAitareya BráhmaGam . Vol. II. p. 41. noteq.v. 93 Upasads.“The Gods said, Let us perform the burnt offerings called Upasads (i.e.besieging). For by means of anUpasad, i.e.besieging, they conquer a large (fortified) town.”— Ibid.p. 32. 94 The Soma plant, or Asclepias Acida. Its fermented juice was drunk in sacrifice by the priests and offered to the Gods who enjoyed the intoxicating draught.
- **Translation**: 

---

### Verse 9 (Ramayan 0.89)
- **Original**: Canto XIII. The Sacrifice Finished. 71 For the third time pure water shed On high souled Da[aratha's head. Then Rishya[ring and all the rest To Indra and the Gods addressed Their sweet-toned hymn of praise and prayer, And called them in the rite to share. With sweetest song and hymn entoned They gave the Gods in heaven enthroned, As duty bids, the gifts they claim, The holy oil that feeds the flame. And many an offering there was paid, And not one slip in all was made. For with most careful heed they saw That all was done by Veda law. None, all those days, was seen oppressed By hunger or by toil distressed. Why speak of human kind? No beast Was there that lacked an ample feast. For there was store for all who came, For orphan child and lonely dame; The old and young were well supplied, The poor and hungry satisfied. Throughout the day ascetics fed, And those who roam to beg their bread: While all around the cry was still, “Give forth, give forth,” and “Eat your fill.” “Give forth with liberal hand the meal, And various robes in largess deal.” Urged by these cries on every side Unweariedly their task they plied: And heaps of food like hills in size In boundless plenty met the eyes: And lakes of sauce, each day renewed, Refreshed the weary multitude.
- **Translation**: 

---

### Verse 10 (Ramayan 0.90)
- **Original**: 72 The Ramayana And strangers there from distant lands, And women folk in crowded bands The best of food and drink obtained At the great rite the king ordained. Apart from all, the Bráhmans there, Thousands on thousands, took their share Of various dainties sweet to taste, On plates of gold and silver placed, All ready set, as, when they willed, The twice-born men their places filled. And servants in fair garments dressed Waited upon each Bráhman guest. Of cheerful mind and mien were they, With gold and jewelled earrings gay. The best of Bráhmans praised the fare Of countless sorts, of flavour rare: And thus to Raghu's son they cried: “We bless thee, and are satisfied.” Between the rites some Bráhmans spent The time in learned argument,[023] With ready flow of speech, sedate, And keen to vanquish in debate.95 There day by day the holy train Performed all rites as rules ordain. No priest in all that host was found 95 “Tum in cærimoniarum intervallis Brachmanæ facundi, sollertes, crebros sermones de rerum causis instituebant, alter alterum vincendi cupidi. This public disputation in the assembly of Bráhmans on the nature of things, and the almost fraternal connexion between theology and philosophy deserves some notice; whereas the priests of some religions are generally but little inclined to show favour to philosophers, nay, sometimes persecute them with the most rancorous hatred, as we are taught both by history and experience.… This [loka is found in the MSS. of different recensions of the Rámáyan, and we have, therefore, the most trustworthy testimony to the antiquity of philosophy among the Indians.” SCHLEGEL {FNS .
- **Translation**: 

---

### Verse 11 (Ramayan 0.91)
- **Original**: Canto XIII. The Sacrifice Finished. 73 But kept the vows that held him bound: None, but the holy Vedas knew, And all their six-fold science96 too. No Bráhman there was found unfit To speak with eloquence and wit. And now the appointed time came near The sacrificial posts to rear. They brought them, and prepared to fix Of Bel97 and Khádir98 six and six; Six, made of the Palá[a99 tree, Of Fig-wood one, apart to be: Of Sleshmát100 and of Devadár101 One column each, the mightiest far: So thick the two, the arms of man Their ample girth would fail to span. All these with utmost care were wrought By hand of priests in Scripture taught, And all with gold were gilded bright To add new splendour to the rite: Twenty-and-one those stakes in all, Each one-and-twenty cubits tall: And one-and-twenty ribbons there Hung on the pillars, bright and fair. 96 The Angas or appendices of the Vedas, pronunciation, prosody, grammar, ritual, astronomy, and explanation of obscurities. 97 In Sanskritvilva, theÆgle Marmelos. “He who desires food and wishes to grow fat, ought to make his Yúpa (sacrificial post) of Bilva wood.” Haug's Aítareya Bráhmanam. Vol. II.p. 73. 98 The Mimosa Catechu.“He who desires heaven ought to make his Yúpa of Khádira wood.”— Ibid. 99 The Butea Frondosa.“He who desires beauty and sacred knowledge ought to make his Yúpa of Palá[a wood.”— Ibid. 100 The Cardia Latifolia. 101 A kind of pine. The word means literally the tree of the Gods. Compare the Hebrew “trees of the Lord.”
- **Translation**: 

---

### Verse 12 (Ramayan 0.92)
- **Original**: 74 The Ramayana Firm in the earth they stood at last, Where cunning craftsmen fixed them fast; And there unshaken each remained, Octagonal and smoothly planed. Then ribbons over all were hung, And flowers and scent around them flung. Thus decked they cast a glory forth Like the great saints who star the north.102 The sacrificial altar then Was raised by skilful twice-born men, In shape and figure to behold An eagle with his wings of gold, With twice nine pits and formed three-fold Each for some special God, beside The pillars were the victims tied; The birds that roam the wood, the air, The water, and the land were there, And snakes and things of reptile birth, And healing herbs that spring from earth: As texts prescribe, in Scripture found, Three hundred victims there were bound. The steed devoted to the host Of Gods, the gem they honour most, Was duly sprinkled. Then the Queen Kau [alyá, with delighted mien, With reverent steps around him paced, And with sweet wreaths the victim graced; Then with three swords in order due She smote the steed with joy, and slew. That night the queen, a son to gain, With calm and steady heart was fain By the dead charger's side to stay 102 The Hindus call the constellation of Ursa Major the Seven Rishis or Saints.
- **Translation**: 

---

### Verse 13 (Ramayan 0.93)
- **Original**: Canto XIII. The Sacrifice Finished. 75 From evening till the break of day. Then came three priests, their care to lead The other queens to touch the steed, Upon Kau [alyá to attend, Their company and aid to lend. As by the horse she still reclined, With happy mien and cheerful mind, With Rishya[ring the twice-born came And praised and blessed the royal dame. The priest who well his duty knew, And every sense could well subdue, From out the bony chambers freed And boiled the marrow of the steed. Above the steam the monarch bent, And, as he smelt the fragrant scent, In time and order drove afar All error that his hopes could mar. Then sixteen priests together came And cast into the sacred flame The severed members of the horse, Made ready all in ordered course. On piles of holy Fig-tree raised [024] The meaner victims' bodies blazed: The steed, of all the creatures slain, Alone required a pile of cane. Three days, as is by law decreed, Lasted that Offering of the Steed. The Chatushmom began the rite, And when the sun renewed his light, The Ukthya followed: after came The Atirátra's holy flame. These were the rites, and many more Arranged by light of holy lore, The Aptoryám of mighty power,
- **Translation**: 

---

### Verse 14 (Ramayan 0.94)
- **Original**: 76 The Ramayana And, each performed in proper hour, The Abhijit and Vi[vajit With every form and service fit; And with the sacrifice at night The Jyotishmom and Áyus rite.103 The Atirátra, literally lasting through the night, is a division of the service of the Jyotishmoma. The Abhijit,the everywhere victorious, is the name of a sub-division of the great sacrifice of the Gavámanaya. The Vi[vajit, orthe all-conquering, is a similar sub-division. Áyus is the name of a service forming a division of the Abhiplava sacrifice. The Aptoryám, is the seventh or last part of the Jyotishmoma, for the performance of which it is not essentially necessary, but a voluntary sacrifice instituted for the attainment of a specific desire. The literal meaning of the word would be in conformity with thePrau hamanoramá ,“a sacrifice which procures the attainment of the desired object.” G OLDSTÜCKER 'S D ICTIONARY {FNS . 103 A minute account of these ancient ceremonies would be out of place here. “Ágnishmoma is the name of a sacrifice, or rather a series of offerings to fire for five days. It is the first and principal part of the Jyotishmoma, one of the great sacrifices in which especially the juice of the Soma plant is offered for the pur- pose of obtaining Swarga or heaven.” G OLDSTÜCKER 'S D ICTIONARY {FNS . “The Ágnishmoma is Agni. It is called so because they (the gods) praised him with this Stoma. They called it so to hide the proper meaning of the word: for the gods like to hide the proper meaning of words.” “On account of four classes of gods having praised Agni with four Stomas, the whole was calledChatushmoma (containing four Stomas).” “It (the Ágnishmoma) is calledJyotishmoma , for they praised Agni when he had risen up (to the sky) in the shape of a light (jyotis).” “This (Ágnishmoma) is a sacrificial performance which has no beginning and no end.” H AUG 'S{FNS Aitareya BráhmaGam .
- **Translation**: 

---

### Verse 15 (Ramayan 0.95)
- **Original**: Canto XIII. The Sacrifice Finished. 77 “The Ukthya is a slight modification of the Ágnishmoma sac- rifice. The noun to be supplied to it iskratu. It is a Soma sacrifice also, and one of the seven SaGsthas or component parts of the Jyotishmoma. Its name indicates its nature. ForUkthya means ‘what refers to the Uktha,’which is an older name for Shástra,i.e.recitation of one of the Hotri priests at the time of the Soma libations. Thus this sacrifice is only a kind of supplement to the Ágnishmoma.” H AUG {FNS .Ai. B. The task was done, as laws prescribe: The monarch, glory of his tribe, Bestowed the land in liberal grants Upon the sacred ministrants. He gave the region of the east, His conquest, to the Hotri priest. The west, the celebrant obtained: The south, the priest presiding gained: The northern region was the share Of him who chanted forth the prayer,104 Thus did each priest obtain his meed At the great Slaughter of the Steed, Ordained, the best of all to be, 104 “Four classes of priests were required in India at the most solemn sacrifices. 1. The officiating priests, manual labourers, and acolytes, who had chiefly to prepare the sacrificial ground, to dress the altar, slay the victims, and pour out the libations. 2. The choristers, who chant the sacred hymns. 3. The reciters or readers, who repeat certain hymns. 4. The overseers or bishops, who watch and superintend the proceedings of the other priests, and ought to be familiar with all the Vedas. The formulas and verses to be muttered by the first class are contained in the Yajur-veda-sanhitá. The hymns to be sung by the second class are in the Sama-veda-sanhitá. The Atharva-veda is said to be intended for the Brahman or overseer, who is to watch the proceedings of the sacrifice, and to remedy any mistake that may occur. The hymns to be recited by the third class are contained in the Rigveda,” Chips from a German Workshop.
- **Translation**: 

---

### Verse 16 (Ramayan 0.96)
- **Original**: 78 The Ramayana By self-existent deity. Ikshváku's son with joyful mind This noble fee to each assigned, But all the priests with one accord Addressed that unpolluted lord: “Tis thine alone to keep the whole Of this broad earth in firm control.[025] No gift of lands from thee we seek: To guard these realms our hands were weak. On sacred lore our days are spent: Let other gifts our wants content.” The chief of old Ikshváku's line Gave them ten hundred thousand kine, A hundred millions of fine gold, The same in silver four times told. But every priest in presence there With one accord resigned his share. To Saint Va[ishmha, high of soul, And Rishya[ring they gave the whole. That largess pleased those Bráhmans well, Who bade the prince his wishes tell. Then Da[aratha, mighty king, Made answer thus to Rishya[ring: “O holy Hermit, of thy grace, Vouchsafe the increase of my race.” He spoke; nor was his prayer denied: The best of Bráhmans thus replied: “Four sons, O Monarch, shall be thine, Upholders of thy royal line.”
- **Translation**: 

---

### Verse 17 (Ramayan 0.97)
- **Original**: Canto XIV. Rávan Doomed. 79 Canto XIV. Rávan Doomed. The saint, well read in holy lore, Pondered awhile his answer o'er, And thus again addressed the king, His wandering thoughts regathering: “Another rite will I begin Which shall the sons thou cravest win, Where all things shall be duly sped And first Atharva texts be read.” Then by VibháGdak's gentle son Was that high sacrifice begun, The king's advantage seeking still And zealous to perform his will. Now all the Gods had gathered there, Each one for his allotted share: Brahmá, the ruler of the sky, StháGu, NáráyaG, Lord most high, And holy Indra men might view With Maruts105 for his retinue; The heavenly chorister, and saint, And spirit pure from earthly taint, With one accord had sought the place The high-souled monarch's rite to grace. Then to the Gods who came to take Their proper share the hermit spake: “For you has Da[aratha slain The votive steed, a son to gain; Stern penance-rites the king has tried, And in firm faith on you relied, 105 The Maruts are the winds, deified in the religion of the Veda like other mighty powers and phenomena of nature.
- **Translation**: 

---

### Verse 18 (Ramayan 0.98)
- **Original**: 80 The Ramayana And now with undiminished care A second rite would fain prepare. But, O ye Gods, consent to grant The longing of your supplicant. For him beseeching hands I lift, And pray you all to grant the gift, That four fair sons of high renown The offerings of the king may crown.” They to the hermit's son replied: “His longing shall be gratified. For, Bráhman, in most high degree We love the king and honour thee.” These words the Gods in answer said, And vanished thence by Indra led. Thus to the Lord, the worlds who made, The Immortals all assembled prayed: “O Brahmá, mighty by thy grace, RávaG, who rules the giant race, Torments us in his senseless pride, And penance-loving saints beside. For thou well pleased in days of old Gavest the boon that makes him bold, That God nor demon e'er should kill His charmed life, for so thy will. We, honouring that high behest, Bear all his rage though sore distressed. That lord of giants fierce and fell Scourges the earth and heaven and hell. Mad with thy boon, his impious rage Smites saint and bard and God and sage. The sun himself withholds his glow, The wind in fear forbears to blow; The fire restrains his wonted heat
- **Translation**: 

---

### Verse 19 (Ramayan 0.99)
- **Original**: Canto XIV. Rávan Doomed. 81 Where stand the dreaded RávaG's feet, And, necklaced with the wandering wave, The sea before him fears to rave. Kuvera's self in sad defeat Is driven from his blissful seat. We see, we feel the giant's might, And woe comes o'er us and affright. To thee, O Lord, thy suppliants pray To find some cure this plague to stay.” Thus by the gathered Gods addressed He pondered in his secret breast, And said:“One only way I find To slay this fiend of evil mind. He prayed me once his life to guard From demon, God, and heavenly bard, And spirits of the earth and air, And I consenting heard his prayer. But the proud giant in his scorn Recked not of man of woman born. None else may take his life away, But only man the fiend may slay.” The Gods, with Indra at their head, Rejoiced to hear the words he said. Then crowned with glory like a flame, Lord VishGu to the council came; His hands shell, mace, and discus bore, And saffron were the robes he wore. [026] Riding his eagle through the crowd, As the sun rides upon a cloud, With bracelets of fine gold, he came Loud welcomed by the Gods' acclaim. His praise they sang with one consent, And cried, in lowly reverence bent:
- **Translation**: 

---

### Verse 20 (Ramayan 0.100)
- **Original**: 82 The Ramayana “O Lord whose hand fierce Madhu106 slew, Be thou our refuge, firm and true; Friend of the suffering worlds art thou, We pray thee help thy suppliants now.” Then VishGu spake:“Ye Gods, declare, What may I do to grant your prayer?” “King Da[aratha,” thus cried they, “Fervent in penance many a day, The sacrificial steed has slain, Longing for sons, but all in vain. Now, at the cry of us forlorn, Incarnate as his seed be born. Three queens has he: each lovely dame Like Beauty, Modesty, or Fame. Divide thyself in four, and be His offspring by these noble three. Man's nature take, and slay in fight RávaG who laughs at heavenly might: This common scourge, this rankling thorn Whom the three worlds too long have borne For RávaG in the senseless pride Of might unequalled has defied The host of heaven, and plagues with woe Angel and bard and saint below, Crushing each spirit and each maid Who plays in Nandan's107 heavenly shade. O conquering Lord, to thee we bow; Our surest hope and trust art thou. Regard the world of men below, And slay the Gods' tremendous foe.” 106 A Titan or fiend whose destruction has given VishGu one of his well-known titles, Mádhava. 107 The garden of Indra.
- **Translation**: 

---

