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

### Verse 1 (Ramayana 0.86)
- **Original**: 68 The Ramayana In length of days our monarch's peer, Illustrious king, invite him here. The father of our ruler's bride, Known for his virtues far and wide, The king whom Kekaya's89 realms obey, Him with his son invite, I pray. And Lomapád the Angas' king, True to his vows and godlike, bring. For be thine invitations sent To west and south and orient. Call those who rule Suráshmra's90 land, Suvíra's91 realm and Sindhu's strand, And all the kings of earth beside In friendship's bonds with us allied: Invite them all to hasten in With retinue and kith and kin.” Va [ishmha's speech without delay Sumantra bent him to obey. And sent his trusty envoys forth Eastward and westward, south and north. Obedient to the saint's request Himself he hurried forth, and pressed Each nobler chief and lord and king To hasten to the gathering. Before the saint Va[ishmha stood All those who wrought with stone and wood, And showed the work which every one In furtherance of the rite had done, Rejoiced their ready zeal to see, Thus to the craftsmen all said he: 89 Kekaya is supposed to have been in the Panjáb. The name of the king was A [vapati (Lord of Horses), father of Da[aratha's wife Kaikeyí. 90 Surat. 91 Apparently in the west of India not far from the Indus.
- **Translation**: 

---

### Verse 2 (Ramayana 0.87)
- **Original**: Canto XIII. The Sacrifice Finished. 69 “I charge ye, masters, see to this, That there be nothing done amiss, And this, I pray, in mind be borne, That not one gift ye give in scorn: Whenever scorn a gift attends Great sin is his who thus offends.” And now some days and nights had past, And kings began to gather fast, And precious gems in liberal store As gifts to Da[aratha bore. Then joy thrilled through Va[ishmha's breast As thus the monarch he addressed: “Obedient to thy high decree The kings, my lord, are come to thee. [022] And it has been my care to greet And honour all with reverence meet. Thy servants' task is ended quite, And all is ready for the rite. Come forth then to the sacred ground Where all in order will be found.” Then Rishya[ring confirmed the tale: Nor did their words to move him fail. The stars propitious influence lent When forth the world's great ruler went. Then by the sage Va[ishmha led The priest begun to speed Those glorious rites wherein is shed The lifeblood of the steed. Canto XIII. The Sacrifice Finished.
- **Translation**: 

---

### Verse 3 (Ramayana 0.88)
- **Original**: 70 The Ramayana The circling year had filled its course, And back was brought the wandering horse: Then upon Sarjú's northern strand Began the rite the king had planned. With Rishya[ring the forms to guide, The Bráhmans to their task applied, At that great offering of the steed Their lofty-minded king decreed. The priests, who all the Scripture knew, Performed their part in order due, And circled round in solemn train As precepts of the law ordain. Pravargya rites92 were duly sped: For Upasads93 the flames were fed. Then from the plant94 the juice was squeezed, And those high saints with minds well pleased Performed the mystic rites begun With bathing ere the rise of sun They gave the portion Indra's claim, And hymned the King whom none can blame. The mid-day bathing followed next, Observed as bids the holy text. Then the good priests with utmost care, In form that Scripture's rules declare, 92 “The Pravargya ceremony lasts for three days, and is always performed twice a day, in the forenoon and afternoon. It precedes the animal and Soma sacrifices. For without having undergone it, no one is allowed to take part in the solemn Soma feast prepared for the gods.” Haug'sAitareya BráhmaGam . Vol. II. p. 41. noteq.v. 93 Upasads.“The Gods said, Let us perform the burnt offerings called Upasads (i.e.besieging). For by means of anUpasad, i.e.besieging, they conquer a large (fortified) town.”— Ibid.p. 32. 94 The Soma plant, or Asclepias Acida. Its fermented juice was drunk in sacrifice by the priests and offered to the Gods who enjoyed the intoxicating draught.
- **Translation**: 

---

### Verse 4 (Ramayana 0.89)
- **Original**: Canto XIII. The Sacrifice Finished. 71 For the third time pure water shed On high souled Da[aratha's head. Then Rishya[ring and all the rest To Indra and the Gods addressed Their sweet-toned hymn of praise and prayer, And called them in the rite to share. With sweetest song and hymn entoned They gave the Gods in heaven enthroned, As duty bids, the gifts they claim, The holy oil that feeds the flame. And many an offering there was paid, And not one slip in all was made. For with most careful heed they saw That all was done by Veda law. None, all those days, was seen oppressed By hunger or by toil distressed. Why speak of human kind? No beast Was there that lacked an ample feast. For there was store for all who came, For orphan child and lonely dame; The old and young were well supplied, The poor and hungry satisfied. Throughout the day ascetics fed, And those who roam to beg their bread: While all around the cry was still, “Give forth, give forth,” and “Eat your fill.” “Give forth with liberal hand the meal, And various robes in largess deal.” Urged by these cries on every side Unweariedly their task they plied: And heaps of food like hills in size In boundless plenty met the eyes: And lakes of sauce, each day renewed, Refreshed the weary multitude.
- **Translation**: 

---

### Verse 5 (Ramayana 0.90)
- **Original**: 72 The Ramayana And strangers there from distant lands, And women folk in crowded bands The best of food and drink obtained At the great rite the king ordained. Apart from all, the Bráhmans there, Thousands on thousands, took their share Of various dainties sweet to taste, On plates of gold and silver placed, All ready set, as, when they willed, The twice-born men their places filled. And servants in fair garments dressed Waited upon each Bráhman guest. Of cheerful mind and mien were they, With gold and jewelled earrings gay. The best of Bráhmans praised the fare Of countless sorts, of flavour rare: And thus to Raghu's son they cried: “We bless thee, and are satisfied.” Between the rites some Bráhmans spent The time in learned argument,[023] With ready flow of speech, sedate, And keen to vanquish in debate.95 There day by day the holy train Performed all rites as rules ordain. No priest in all that host was found 95 “Tum in cærimoniarum intervallis Brachmanæ facundi, sollertes, crebros sermones de rerum causis instituebant, alter alterum vincendi cupidi. This public disputation in the assembly of Bráhmans on the nature of things, and the almost fraternal connexion between theology and philosophy deserves some notice; whereas the priests of some religions are generally but little inclined to show favour to philosophers, nay, sometimes persecute them with the most rancorous hatred, as we are taught both by history and experience.… This [loka is found in the MSS. of different recensions of the Rámáyan, and we have, therefore, the most trustworthy testimony to the antiquity of philosophy among the Indians.” SCHLEGEL {FNS .
- **Translation**: 

---

### Verse 6 (Ramayana 0.91)
- **Original**: Canto XIII. The Sacrifice Finished. 73 But kept the vows that held him bound: None, but the holy Vedas knew, And all their six-fold science96 too. No Bráhman there was found unfit To speak with eloquence and wit. And now the appointed time came near The sacrificial posts to rear. They brought them, and prepared to fix Of Bel97 and Khádir98 six and six; Six, made of the Palá[a99 tree, Of Fig-wood one, apart to be: Of Sleshmát100 and of Devadár101 One column each, the mightiest far: So thick the two, the arms of man Their ample girth would fail to span. All these with utmost care were wrought By hand of priests in Scripture taught, And all with gold were gilded bright To add new splendour to the rite: Twenty-and-one those stakes in all, Each one-and-twenty cubits tall: And one-and-twenty ribbons there Hung on the pillars, bright and fair. 96 The Angas or appendices of the Vedas, pronunciation, prosody, grammar, ritual, astronomy, and explanation of obscurities. 97 In Sanskritvilva, theÆgle Marmelos. “He who desires food and wishes to grow fat, ought to make his Yúpa (sacrificial post) of Bilva wood.” Haug's Aítareya Bráhmanam. Vol. II.p. 73. 98 The Mimosa Catechu.“He who desires heaven ought to make his Yúpa of Khádira wood.”— Ibid. 99 The Butea Frondosa.“He who desires beauty and sacred knowledge ought to make his Yúpa of Palá[a wood.”— Ibid. 100 The Cardia Latifolia. 101 A kind of pine. The word means literally the tree of the Gods. Compare the Hebrew “trees of the Lord.”
- **Translation**: 

---

### Verse 7 (Ramayana 0.92)
- **Original**: 74 The Ramayana Firm in the earth they stood at last, Where cunning craftsmen fixed them fast; And there unshaken each remained, Octagonal and smoothly planed. Then ribbons over all were hung, And flowers and scent around them flung. Thus decked they cast a glory forth Like the great saints who star the north.102 The sacrificial altar then Was raised by skilful twice-born men, In shape and figure to behold An eagle with his wings of gold, With twice nine pits and formed three-fold Each for some special God, beside The pillars were the victims tied; The birds that roam the wood, the air, The water, and the land were there, And snakes and things of reptile birth, And healing herbs that spring from earth: As texts prescribe, in Scripture found, Three hundred victims there were bound. The steed devoted to the host Of Gods, the gem they honour most, Was duly sprinkled. Then the Queen Kau [alyá, with delighted mien, With reverent steps around him paced, And with sweet wreaths the victim graced; Then with three swords in order due She smote the steed with joy, and slew. That night the queen, a son to gain, With calm and steady heart was fain By the dead charger's side to stay 102 The Hindus call the constellation of Ursa Major the Seven Rishis or Saints.
- **Translation**: 

---

### Verse 8 (Ramayana 0.93)
- **Original**: Canto XIII. The Sacrifice Finished. 75 From evening till the break of day. Then came three priests, their care to lead The other queens to touch the steed, Upon Kau [alyá to attend, Their company and aid to lend. As by the horse she still reclined, With happy mien and cheerful mind, With Rishya[ring the twice-born came And praised and blessed the royal dame. The priest who well his duty knew, And every sense could well subdue, From out the bony chambers freed And boiled the marrow of the steed. Above the steam the monarch bent, And, as he smelt the fragrant scent, In time and order drove afar All error that his hopes could mar. Then sixteen priests together came And cast into the sacred flame The severed members of the horse, Made ready all in ordered course. On piles of holy Fig-tree raised [024] The meaner victims' bodies blazed: The steed, of all the creatures slain, Alone required a pile of cane. Three days, as is by law decreed, Lasted that Offering of the Steed. The Chatushmom began the rite, And when the sun renewed his light, The Ukthya followed: after came The Atirátra's holy flame. These were the rites, and many more Arranged by light of holy lore, The Aptoryám of mighty power,
- **Translation**: 

---

### Verse 9 (Ramayana 0.94)
- **Original**: 76 The Ramayana And, each performed in proper hour, The Abhijit and Vi[vajit With every form and service fit; And with the sacrifice at night The Jyotishmom and Áyus rite.103 The Atirátra, literally lasting through the night, is a division of the service of the Jyotishmoma. The Abhijit,the everywhere victorious, is the name of a sub-division of the great sacrifice of the Gavámanaya. The Vi[vajit, orthe all-conquering, is a similar sub-division. Áyus is the name of a service forming a division of the Abhiplava sacrifice. The Aptoryám, is the seventh or last part of the Jyotishmoma, for the performance of which it is not essentially necessary, but a voluntary sacrifice instituted for the attainment of a specific desire. The literal meaning of the word would be in conformity with thePrau hamanoramá ,“a sacrifice which procures the attainment of the desired object.” G OLDSTÜCKER 'S D ICTIONARY {FNS . 103 A minute account of these ancient ceremonies would be out of place here. “Ágnishmoma is the name of a sacrifice, or rather a series of offerings to fire for five days. It is the first and principal part of the Jyotishmoma, one of the great sacrifices in which especially the juice of the Soma plant is offered for the pur- pose of obtaining Swarga or heaven.” G OLDSTÜCKER 'S D ICTIONARY {FNS . “The Ágnishmoma is Agni. It is called so because they (the gods) praised him with this Stoma. They called it so to hide the proper meaning of the word: for the gods like to hide the proper meaning of words.” “On account of four classes of gods having praised Agni with four Stomas, the whole was calledChatushmoma (containing four Stomas).” “It (the Ágnishmoma) is calledJyotishmoma , for they praised Agni when he had risen up (to the sky) in the shape of a light (jyotis).” “This (Ágnishmoma) is a sacrificial performance which has no beginning and no end.” H AUG 'S{FNS Aitareya BráhmaGam .
- **Translation**: 

---

### Verse 10 (Ramayana 0.95)
- **Original**: Canto XIII. The Sacrifice Finished. 77 “The Ukthya is a slight modification of the Ágnishmoma sac- rifice. The noun to be supplied to it iskratu. It is a Soma sacrifice also, and one of the seven SaGsthas or component parts of the Jyotishmoma. Its name indicates its nature. ForUkthya means ‘what refers to the Uktha,’which is an older name for Shástra,i.e.recitation of one of the Hotri priests at the time of the Soma libations. Thus this sacrifice is only a kind of supplement to the Ágnishmoma.” H AUG {FNS .Ai. B. The task was done, as laws prescribe: The monarch, glory of his tribe, Bestowed the land in liberal grants Upon the sacred ministrants. He gave the region of the east, His conquest, to the Hotri priest. The west, the celebrant obtained: The south, the priest presiding gained: The northern region was the share Of him who chanted forth the prayer,104 Thus did each priest obtain his meed At the great Slaughter of the Steed, Ordained, the best of all to be, 104 “Four classes of priests were required in India at the most solemn sacrifices. 1. The officiating priests, manual labourers, and acolytes, who had chiefly to prepare the sacrificial ground, to dress the altar, slay the victims, and pour out the libations. 2. The choristers, who chant the sacred hymns. 3. The reciters or readers, who repeat certain hymns. 4. The overseers or bishops, who watch and superintend the proceedings of the other priests, and ought to be familiar with all the Vedas. The formulas and verses to be muttered by the first class are contained in the Yajur-veda-sanhitá. The hymns to be sung by the second class are in the Sama-veda-sanhitá. The Atharva-veda is said to be intended for the Brahman or overseer, who is to watch the proceedings of the sacrifice, and to remedy any mistake that may occur. The hymns to be recited by the third class are contained in the Rigveda,” Chips from a German Workshop.
- **Translation**: 

---

### Verse 11 (Ramayana 0.96)
- **Original**: 78 The Ramayana By self-existent deity. Ikshváku's son with joyful mind This noble fee to each assigned, But all the priests with one accord Addressed that unpolluted lord: “Tis thine alone to keep the whole Of this broad earth in firm control.[025] No gift of lands from thee we seek: To guard these realms our hands were weak. On sacred lore our days are spent: Let other gifts our wants content.” The chief of old Ikshváku's line Gave them ten hundred thousand kine, A hundred millions of fine gold, The same in silver four times told. But every priest in presence there With one accord resigned his share. To Saint Va[ishmha, high of soul, And Rishya[ring they gave the whole. That largess pleased those Bráhmans well, Who bade the prince his wishes tell. Then Da[aratha, mighty king, Made answer thus to Rishya[ring: “O holy Hermit, of thy grace, Vouchsafe the increase of my race.” He spoke; nor was his prayer denied: The best of Bráhmans thus replied: “Four sons, O Monarch, shall be thine, Upholders of thy royal line.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.97)
- **Original**: Canto XIV. Rávan Doomed. 79 Canto XIV. Rávan Doomed. The saint, well read in holy lore, Pondered awhile his answer o'er, And thus again addressed the king, His wandering thoughts regathering: “Another rite will I begin Which shall the sons thou cravest win, Where all things shall be duly sped And first Atharva texts be read.” Then by VibháGdak's gentle son Was that high sacrifice begun, The king's advantage seeking still And zealous to perform his will. Now all the Gods had gathered there, Each one for his allotted share: Brahmá, the ruler of the sky, StháGu, NáráyaG, Lord most high, And holy Indra men might view With Maruts105 for his retinue; The heavenly chorister, and saint, And spirit pure from earthly taint, With one accord had sought the place The high-souled monarch's rite to grace. Then to the Gods who came to take Their proper share the hermit spake: “For you has Da[aratha slain The votive steed, a son to gain; Stern penance-rites the king has tried, And in firm faith on you relied, 105 The Maruts are the winds, deified in the religion of the Veda like other mighty powers and phenomena of nature.
- **Translation**: 

---

### Verse 13 (Ramayana 0.98)
- **Original**: 80 The Ramayana And now with undiminished care A second rite would fain prepare. But, O ye Gods, consent to grant The longing of your supplicant. For him beseeching hands I lift, And pray you all to grant the gift, That four fair sons of high renown The offerings of the king may crown.” They to the hermit's son replied: “His longing shall be gratified. For, Bráhman, in most high degree We love the king and honour thee.” These words the Gods in answer said, And vanished thence by Indra led. Thus to the Lord, the worlds who made, The Immortals all assembled prayed: “O Brahmá, mighty by thy grace, RávaG, who rules the giant race, Torments us in his senseless pride, And penance-loving saints beside. For thou well pleased in days of old Gavest the boon that makes him bold, That God nor demon e'er should kill His charmed life, for so thy will. We, honouring that high behest, Bear all his rage though sore distressed. That lord of giants fierce and fell Scourges the earth and heaven and hell. Mad with thy boon, his impious rage Smites saint and bard and God and sage. The sun himself withholds his glow, The wind in fear forbears to blow; The fire restrains his wonted heat
- **Translation**: 

---

### Verse 14 (Ramayana 0.99)
- **Original**: Canto XIV. Rávan Doomed. 81 Where stand the dreaded RávaG's feet, And, necklaced with the wandering wave, The sea before him fears to rave. Kuvera's self in sad defeat Is driven from his blissful seat. We see, we feel the giant's might, And woe comes o'er us and affright. To thee, O Lord, thy suppliants pray To find some cure this plague to stay.” Thus by the gathered Gods addressed He pondered in his secret breast, And said:“One only way I find To slay this fiend of evil mind. He prayed me once his life to guard From demon, God, and heavenly bard, And spirits of the earth and air, And I consenting heard his prayer. But the proud giant in his scorn Recked not of man of woman born. None else may take his life away, But only man the fiend may slay.” The Gods, with Indra at their head, Rejoiced to hear the words he said. Then crowned with glory like a flame, Lord VishGu to the council came; His hands shell, mace, and discus bore, And saffron were the robes he wore. [026] Riding his eagle through the crowd, As the sun rides upon a cloud, With bracelets of fine gold, he came Loud welcomed by the Gods' acclaim. His praise they sang with one consent, And cried, in lowly reverence bent:
- **Translation**: 

---

### Verse 15 (Ramayana 0.100)
- **Original**: 82 The Ramayana “O Lord whose hand fierce Madhu106 slew, Be thou our refuge, firm and true; Friend of the suffering worlds art thou, We pray thee help thy suppliants now.” Then VishGu spake:“Ye Gods, declare, What may I do to grant your prayer?” “King Da[aratha,” thus cried they, “Fervent in penance many a day, The sacrificial steed has slain, Longing for sons, but all in vain. Now, at the cry of us forlorn, Incarnate as his seed be born. Three queens has he: each lovely dame Like Beauty, Modesty, or Fame. Divide thyself in four, and be His offspring by these noble three. Man's nature take, and slay in fight RávaG who laughs at heavenly might: This common scourge, this rankling thorn Whom the three worlds too long have borne For RávaG in the senseless pride Of might unequalled has defied The host of heaven, and plagues with woe Angel and bard and saint below, Crushing each spirit and each maid Who plays in Nandan's107 heavenly shade. O conquering Lord, to thee we bow; Our surest hope and trust art thou. Regard the world of men below, And slay the Gods' tremendous foe.” 106 A Titan or fiend whose destruction has given VishGu one of his well-known titles, Mádhava. 107 The garden of Indra.
- **Translation**: 

---

### Verse 16 (Ramayana 0.101)
- **Original**: Canto XIV. Rávan Doomed. 83 When thus the suppliant Gods had prayed, His wise reply NáráyaG108 made: “What task demands my presence there, And whence this dread, ye Gods declare.” The Gods replied:“We fear, O Lord, Fierce RávaG, ravener abhorred. Be thine the glorious task, we pray, In human form this fiend to slay. By thee of all the Blest alone This sinner may be overthrown. He gained by penance long and dire The favour of the mighty Sire. Then He who every gift bestows Guarded the fiend from heavenly foes, And gave a pledge his life that kept From all things living, man except. On him thus armed no other foe Than man may deal the deadly blow. Assume, O King, a mortal birth, And strike the demon to the earth.” Then VishGu, God of Gods, the Lord Supreme by all the worlds adored, To Brahmá and the suppliants spake: “Dismiss your fear: for your dear sake In battle will I smite him dead, The cruel fiend, the Immortal's dread. And lords and ministers and all His kith and kin with him shall fall. Then, in the world of mortal men, 108 One of the most ancient and popular of the numerous names of VishGu. The word has been derived in several ways, and may meanhe who moved on the (primordial) waters, orhe who pervades or influences men or their thoughts.
- **Translation**: 

---

### Verse 17 (Ramayana 0.102)
- **Original**: 84 The Ramayana Ten thousand years and hundreds ten I as a human king will reign, And guard the earth as my domain.” God, saint, and nymph, and minstrel throng With heavenly voices raised their song In hymns of triumph to the God Whose conquering feet on Madhu trod: “Champion of Gods, as man appear, This cruel RávaG slay, The thorn that saints and hermits fear, The plague that none can stay. In savage fury uncontrolled His pride for ever grows: He dares the Lord of Gods to hold Among his deadly foes.” Canto XV. The Nectar. When wisest VishGu thus had given His promise to the Gods of heaven, He pondered in his secret mind A suited place of birth to find, Then he decreed, the lotus-eyed, In four his being to divide, And Da [aratha, gracious king, He chose as sire from whom to spring. That childless prince of high renown, Who smote in war his foemen down, At that same time with utmost care
- **Translation**: 

---

### Verse 18 (Ramayana 0.103)
- **Original**: Canto XV. The Nectar. 85 Prepared the rite that wins an heir.109 Then VishGu, fain on earth to dwell, Bade the Almighty Sire farewell, And vanished while a reverent crowd Of Gods and saints in worship bowed. The monarch watched the sacred rite, When a vast form of awful might, Of matchless splendour, strength, and size Was manifest before his eyes. [027] From forth the sacrificial flame, Dark, robed in red, the being came. His voice was drumlike, loud and low, His face suffused with rosy glow. Like a huge lion's mane appeared The long locks of his hair and beard. He shone with many a lucky sign, And many an ornament divine; A towering mountain in his height, A tiger in his gait and might. No precious mine more rich could be, No burning flame more bright than he. His arms embraced in loving hold, Like a dear wife, a vase of gold Whose silver lining held a draught Of nectar as in heaven is quaffed: A vase so vast, so bright to view, They scarce could count the vision true. Upon the king his eyes he bent, And said:“The Lord of life has sent His servant down, O Prince, to be A messenger from heaven to thee.” The king with all his nobles by 109 The Horse-Sacrifice, just described.
- **Translation**: 

---

### Verse 19 (Ramayana 0.104)
- **Original**: 86 The Ramayana Raised reverent hands and made reply: “Welcome, O glorious being! Say How can my care thy grace repay.” Envoy of Him whom all adore Thus to the king he spake once more: “The Gods accept thy worship: they Give thee the blessed fruit to-day. Approach and take, O glorious King, This heavenly nectar which I bring, For it shall give thee sons and wealth, And bless thee with a store of health. Give it to those fair queens of thine, And bid them quaff the drink divine: And they the princely sons shall bear Long sought by sacrifice and prayer.” “Yea, O my lord,” the monarch said, And took the vase upon his head, The gift of Gods, of fine gold wrought, With store of heavenly liquor fraught. He honoured, filled with transport new, That wondrous being, fair to view, As round the envoy of the God With reverential steps he trod.110 His errand done, that form of light 110 To walk round an object keeping the right side towards it is a mark of great respect. The Sanskrit word for the observance ispradakshiGá, from pra pro, anddaksha right, Greek´µ¾w¿Â, Latin dexter, Gaelic deas-il. A similar ceremony is observed by the Gaels. “In the meantime she traced around him, with wavering steps, the propitia- tion, which some have thought has been derived from the Druidical mythology. It consists, as is well known, in the person who makes thedeasilwalking three times round the person who is the object of the ceremony, taking care to move according to the course of the sun.” SCOTT {FNS .The Two Drovers.
- **Translation**: 

---

### Verse 20 (Ramayana 0.105)
- **Original**: Canto XV. The Nectar. 87 Arose and vanished from the sight. High rapture filled the monarch's soul, Possessed of that celestial bowl, As when a man by want distressed With unexpected wealth is blest. And rays of transport seemed to fall Illuminating bower and hall, As when the autumn moon rides high, And floods with lovely light the sky. Quick to the ladies' bower he sped, And thus to Queen Kau[alyá said: “This genial nectar take and quaff,” He spoke, and gave the lady half. Part of the nectar that remained Sumitrá from his hand obtained. He gave, to make her fruitful too, Kaikeyí half the residue. A portion yet remaining there, He paused awhile to think. Then gave Sumitrá, with her share. The remnant of the drink. Thus on each queen of those fair three A part the king bestowed, And with sweet hope a child to see Their yearning bosoms glowed. The heavenly bowl the king supplied Their longing souls relieved, And soon, with rapture and with pride, Each royal dame conceived. He gazed upon each lady's face, And triumphed as he gazed, As Indra in his royal place By Gods and spirits praised.
- **Translation**: 

---

