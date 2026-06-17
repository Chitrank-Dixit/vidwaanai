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

### Verse 1 (Ramayana 0.226)
- **Original**: 208 The Ramayana Serve her great guest with woodland store, Whom all should honour evermore? Didst thou the tale to Ráma tell Of what in ancient days befell, The sin, the misery, and the shame Of guilty God and faithless dame? And, O thou best of hermits, say, Did Ráma's healing presence stay Her trial? was the wife restored Again to him, my sire and lord? Say, Hermit, did that sire of mine Receive her with a soul benign, When long austerities in time Had cleansed her from the taint of crime?[063] And, son of Ku[ik, let me know, Did my great-minded father show Honour to Ráma, and regard, Before he journeyed hitherward?” The hermit with attentive ear Marked all the questions of the seer: To him for eloquence far-famed, His eloquent reply he framed: “Yea, 'twas my care no task to shun, And all I had to do was done; As ReGuká and Bhrigu's child, The saint and dame were reconciled.” When the great sage had thus replied, To Ráma Zatánanda cried: “A welcome visit, Prince, is thine, Thou scion of King Raghu's line. With him to guide thy way aright, This sage invincible in might, This Bráhman sage, most glorious-bright,
- **Translation**: 

---

### Verse 2 (Ramayana 0.227)
- **Original**: Canto LI. Visvámitra. 209 By long austerities has wrought A wondrous deed, exceeding thought: Thou knowest well, O strong of arm, This sure defence from scathe and harm. None, Ráma, none is living now In all the earth more blest than thou, That thou hast won a saint so tried In fervid rites thy life to guide. Now listen, Prince, while I relate His lofty deeds and wondrous fate. He was a monarch pious-souled. His foemen in the dust he rolled; Most learned, prompt at duty's claim, His people's good his joy and aim. Of old the Lord of Life gave birth To mighty Ku[a, king of earth. His son was Ku[anábha, strong, Friend of the right, the foe of wrong. Gádhi, whose fame no time shall dim, Heir of his throne was born to him, And Vi[vámitra, Gádhi's heir, Governed the land with kingly care. While years unnumbered rolled away The monarch reigned with equal sway. At length, assembling many a band, He led his warriors round the land— Complete in tale, a mighty force, Cars, elephants, and foot, and horse. Through cities, groves, and floods he passed, O'er lofty hills, through regions vast. He reached Va[ishmha's pure abode, Where trees, and flowers, and creepers glowed, Where troops of sylvan creatures fed;
- **Translation**: 

---

### Verse 3 (Ramayana 0.228)
- **Original**: 210 The Ramayana Which saints and angels visited. Gods, fauns, and bards of heavenly race, And spirits, glorified the place; The deer their timid ways forgot, And holy Bráhmans thronged the spot. Bright in their souls, like fire, were these, Made pure by long austerities, Bound by the rule of vows severe, And each in glory Brahmá's peer. Some fed on water, some on air, Some on the leaves that withered there. Roots and wild fruit were others' food; All rage was checked, each sense subdued, There Bálakhilyas220 went and came, Now breathed the prayer, now fed the flame: These, and ascetic bands beside, The sweet retirement beautified. Such was Va[ishmha's blest retreat, Like Brahmá's own celestial seat, Which gladdened Vi[vámitra's eyes, Peerless for warlike enterprise. Canto LII. Vasishtha's Feast. 220 Divine personages of minute size produced from the hair of Brahmá, and probably the origin of “That small infantry Warred on by cranes.”
- **Translation**: 

---

### Verse 4 (Ramayana 0.229)
- **Original**: Canto LII. Vasishtha's Feast. 211 Right glad was Vi[vámitra when He saw the prince of saintly men. Low at his feet the hero bent, And did obeisance, reverent. The king was welcomed in, and shown A seat beside the hermit's own, Who offered him, when resting there, Fruit in due course, and woodland fare. And Vi[vámitra, noblest king, Received Va[ishmha's welcoming, Turned to his host, and prayed him tell That he and all with him were well. Va [ishmha to the king replied That all was well on every side, That fire, and vows, and pupils throve, And all the trees within the grove. And then the son of Brahmá, best Of all who pray with voice suppressed, Questioned with pleasant words like these The mighty king who sate at ease: “And is it well with thee? I pray; And dost thou win by virtuous sway Thy people's love, discharging all The duties on a king that fall? Are all thy servants fostered well? Do all obey, and none rebel? Hast thou, destroyer of the foe, No enemies to overthrow? Does fortune, conqueror! still attend Thy treasure, host, and every friend? Is it all well? Does happy fate On sons and children's children wait?”
- **Translation**: 

---

### Verse 5 (Ramayana 0.230)
- **Original**: 212 The Ramayana He spoke. The modest king replied That all was prosperous far and wide. [064] Thus for awhile the two conversed, As each to each his tale rehearsed, And as the happy moments flew, Their joy and friendship stronger grew. When such discourse had reached an end, Thus spoke the saint most reverend To royal Vi[vámitra, while His features brightened with a smile: “O mighty lord of men. I fain Would banquet thee and all thy train In mode that suits thy station high: And do not thou my prayer deny. Let my good lord with favour take The offering that I fain would make, And let me honour, ere we part, My royal guest with loving heart.” Him Vi[vámitra thus addressed: “Why make, O Saint, this new request? Thy welcome and each gracious word Sufficient honour have conferred. Thou gavest roots and fruit to eat, The treasures of this pure retreat, And water for my mouth and feet; And — boon I prize above the rest— Thy presence has mine eyesight blest. Honoured by thee in every way, To whom all honour all should pay, I now will go. My lord, Good-bye! Regard me with a friendly eye.”
- **Translation**: 

---

### Verse 6 (Ramayana 0.231)
- **Original**: Canto LIII. Visvámitra's Request. 213 Him speaking thus Va[ishmha stayed, And still to share his banquet prayed. The will of Gádhi's son he bent, And won the monarch to consent, Who spoke in answer.“Let it be, Great Hermit, as it pleases thee.” When, best of those who breathe the prayer, He heard the king his will declare, He called the cow of spotted skin, All spot without, all pure within. “Come, Dapple-skin,” he cried,“with speed; Hear thou my words and help at need. My heart is set to entertain This monarch and his mighty train With sumptuous meal and worthy fare; Be thine the banquet to prepare. Each dainty cate, each goodly dish, Of six-fold taste221 as each may wish— All these, O cow of heavenly power, Rain down for me in copious shower: Viands and drink for tooth and lip, To eat, to suck, to quaff, to sip— Of these sufficient, and to spare, O plenty-giving cow, prepare.” Canto LIII. Visvámitra's Request. 221 Sweet, salt, pungent, bitter, acid, and astringent.
- **Translation**: 

---

### Verse 7 (Ramayana 0.232)
- **Original**: 214 The Ramayana Thus charged, O slayer of thy foes, The cow from whom all plenty flows, Obedient to her saintly lord, Viands to suit each taste, outpoured. Honey she gave, and roasted grain, Mead sweet with flowers, and sugar-cane. Each beverage of flavour rare, An food of every sort, were there: Hills of hot rice, and sweetened cakes, And curdled milk and soup in lakes. Vast beakers foaming to the brim With sugared drink prepared for him, And dainty sweetmeats, deftly made, Before the hermit's guests were laid. So well regaled, so nobly fed, The mighty army banqueted, And all the train, from chief to least, Delighted in Va[ishmha's feast. Then Vi[vámitra, royal sage, Surrounded by his vassalage, Prince, peer, and counsellor, and all From highest lord to lowest thrall, Thus feasted, to Va[ishmha cried With joy, supremely gratified: “Rich honour I, thus entertained, Most honourable lord, have gained: Now hear, before I journey hence, My words, O skilled in eloquence. Bought for a hundred thousand kine, Let Dapple-skin, O Saint, be mine. A wondrous jewel is thy cow, And gems are for the monarch's brow.222 222 “Of old hoards and minerals in the earth, the king is entitled to half by reason of his general protection, and because he is the lord paramount of the
- **Translation**: 

---

### Verse 8 (Ramayana 0.233)
- **Original**: Canto LIII. Visvámitra's Request. 215 To me her rightful lord resign This Dapple-skin thou callest thine.” The great Va[ishmha, thus addressed, Arch-hermit of the holy breast, To Vi[vámitra answer made, The king whom all the land obeyed: “Not for a hundred thousand,— nay, Not if ten million thou wouldst pay, With silver heaps the price to swell,— Will I my cow, O Monarch, sell. Unmeet for her is such a fate. That I my friend should alienate. As glory with the virtuous, she For ever makes her home with me. On her mine offerings which ascend To Gods and spirits all depend: My very life is due to her, My guardian, friend, and minister. [065] The feeding of the sacred flame,223 The dole which living creatures claim.224. The mighty sacrifice by fire, Each formula the rites require,225 And various saving lore beside, Are by her aid, in sooth, supplied. The banquet which thy host has shared, soil.” M ANU {FNS , Book VIII. 39. 223 Ghí or clarified butter,“holy oil,” being one of the essentials of sacrifice. 224 “A Bráhman had five principal duties to discharge every day: study and teaching the Veda, oblations to the manes or spirits of the departed, sacrifice to the Gods, hospitable offerings to men, anda gift of food to all creatures. The last consisted of rice or other grain which the Bráhman was to offer every day outside his house in the open air. MANU {FNS , Book III. 70.” G ORRESIO {FNS 225 These were certain sacred words of invocation such asváhá,vasham, etc., pronounced at the time of sacrifice.
- **Translation**: 

---

### Verse 9 (Ramayana 0.234)
- **Original**: 216 The Ramayana Believe it, was by her prepared, In her mine only treasures lie, She cheers mine heart and charms mine eye. And reasons more could I assign Why Dapple-skin can ne'er be thine.” The royal sage, his suit denied, With eloquence more earnest cried: “Tusked elephants, a goodly train, Each with a golden girth and chain, Whose goads with gold well fashioned shine— Of these be twice seven thousand thine. And four-horse cars with gold made bright, With steeds most beautifully white, Whose bells make music as they go, Eight hundred, Saint, will I bestow. Eleven thousand mettled steeds From famous lands, of noble breeds— These will I gladly give, O thou Devoted to each holy vow. Ten million heifers, fair to view, Whose sides are marked with every hue— These in exchange will I assign; But let thy Dapple-skin be mine. Ask what thou wilt, and piles untold Of priceless gems and gleaming gold, O best of Bráhmans, shall be thine; But let thy Dapple-skin be mine.”
- **Translation**: 

---

### Verse 10 (Ramayana 0.235)
- **Original**: Canto LIV. The Battle. 217 The great Va[ishmha, thus addressed, Made answer to the king's request: “Ne'er will I give my cow away, My gem, my wealth, my life and stay. My worship at the moon's first show, And at the full, to her I owe; And sacrifices small and great, Which largess due and gifts await. From her alone, their root, O King, My rites and holy service spring. What boots it further words to say? I will not give my cow away Who yields me what I ask each day.” Canto LIV. The Battle. As Saint Va[ishmha answered so, Nor let the cow of plenty go, The monarch, as a last resource, Began to drag her off by force. While the king's servants tore away Their moaning, miserable prey, Sad, sick at heart, and sore distressed, She pondered thus within her breast: “Why am I thus forsaken? why Betrayed by him of soul most high. Va [ishmha, ravished by the hands Of soldiers of the monarch's bands? Ah me! what evil have I done Against the lofty-minded one, That he, so pious, can expose
- **Translation**: 

---

### Verse 11 (Ramayana 0.236)
- **Original**: 218 The Ramayana The innocent whose love he knows?” In her sad breast as thus she thought, And heaved deep sighs with anguish fraught, With wondrous speed away she fled, And back to Saint Va[ishmha sped. She hurled by hundreds to the ground The menial crew that hemmed her round, And flying swifter than the blast Before the saint herself she cast. There Dapple-skin before the saint Stood moaning forth her sad complaint, And wept and lowed: such tones as come From wandering cloud or distant drum. “O son of Brahmá,” thus cried she, “Why hast thou thus forsaken me, That the king's men, before thy face, Bear off thy servant from her place?” Then thus the Bráhman saint replied To her whose heart with woe was tried, And grieving for his favourite's sake, As to a suffering sister spake: “I leave thee not: dismiss the thought; Nor, duteous, hast thou failed in aught. This king, o'erweening in the pride Of power, has reft thee from my side. Little, I ween, my strength could do 'Gainst him, a mighty warrior too. Strong, as a soldier born and bred,— Great, as a king whom regions dread. See! what a host the conqueror leads, With elephants, and cars, and steeds. O'er countless bands his pennons fly; So is he mightier far than I.”[066]
- **Translation**: 

---

### Verse 12 (Ramayana 0.237)
- **Original**: Canto LIV. The Battle. 219 He spoke. Then she, in lowly mood, To that high saint her speech renewed: “So judge not they who wisest are: The Bráhman's might is mightier far. For Bráhmans strength from Heaven derive, And warriors bow when Bráhmans strive. A boundless power 'tis thine to wield: To such a king thou shouldst not yield, Who, very mighty though he be,— So fierce thy strength,— must bow to thee. Command me, Saint. Thy power divine Has brought me here and made me thine; And I, howe'er the tyrant boast, Will tame his pride and slay his host.” Then cried the glorious sage:“Create A mighty force the foe to mate.” She lowed, and quickened into life, Pahlavas,226 burning for the strife, King Vi[vámitra's army slew Before the very leader's view. The monarch in excessive ire, His eyes with fury darting fire, Rained every missile on the foe Till all the Pahlavas were low. 226 “It is well known that the Persians were called Pahlavas by the Indians. The Zakasare nomad tribes inhabiting Central Asia, the Scythes of the Greeks, whom the Persians also, as Herodotus tells us, called Sakæ just as the Indians did. Lib. VII 64A¹ ³pÁ sÁÃ±¹ Àq½Ä±Â Ä¿zÂ £{¸±Â.º±»s¿ÅÃ¹ £qº±Â. The name Yavans seems to be used rather indefinitely for nations situated beyond Persia to the west.… After the time of Alexander the Great the Indians as well as the Persians called the Greeks also Yavans.” SCHLEGEL {FNS . Lassen thinks that the Pahlavas were the same people as the qºÄÅµÂ of Herodotus, and that this non-Indian people dwelt on the north-west confines of India.
- **Translation**: 

---

### Verse 13 (Ramayana 0.238)
- **Original**: 220 The Ramayana She, seeing all her champions slain, Lying by thousands on the plain. Created, by her mere desire, Yavans andZakas, fierce and dire. And all the ground was overspread With Yavans and withZakas dread: A host of warriors bright and strong, And numberless in closest throng: The threads within the lotus stem, So densely packed, might equal them. In gold-hued mail 'against war's attacks, Each bore a sword and battle-axe, The royal host, where'er these came, Fell as if burnt with ravening flame. The monarch, famous through the world Again his fearful weapons hurled, That made Kámbojas,227 Barbars,228 all, With Yavans, troubled, flee and fall. Canto LV. The Hermitage Burnt. So o'er the field that host lay strown, By Vi[vámitra's darts o'erthrown. Then thus Va[ishmha charged the cow: “Create with all thy vigour now.” 227 See page 13, note 6. 228 Barbarians, non-Sanskrit-speaking tribes.
- **Translation**: 

---

### Verse 14 (Ramayana 0.239)
- **Original**: Canto LV. The Hermitage Burnt. 221 Forth sprang Kámbojas, as she lowed; Bright as the sun their faces glowed, Forth from her udder Barbars poured,— Soldiers who brandished spear and sword,— And Yavans with their shafts and darts, And Zakas from her hinder parts. And every pore upon her fell, And every hair-producing cell, With Mlechchhas229 and Kirátas230 teemed, And forth with them Hárítas streamed. And Vi[vámitra's mighty force, Car, elephant, and foot, and horse, Fell in a moment's time, subdued By that tremendous multitude. The monarch's hundred sons, whose eyes Beheld the rout in wild surprise, Armed with all weapons, mad with rage, Rushed fiercely on the holy sage. One cry he raised, one glance he shot, And all fell scorched upon the spot: Burnt by the sage to ashes, they With horse, and foot, and chariot, lay. The monarch mourned, with shame and pain, His army lost, his children slain, Like Ocean when his roar is hushed, Or some great snake whose fangs are crushed: [067] 229 A comprehensive term for foreign or outcast races of different faith and language from the Hindus. 230 The Kirátas and Hárítas are savage aborigines of India who occupy hills and jungles and are altogether different in race and character from the Hindus. Dr. Muir remarks in his Sanskrit Texts, Vol. I. p. 488 (second edition) that it does not appear that it is the object of this legend to represent this miraculous creation as the origin of these tribes, and that nothing more may have been intended than that the cow called into existence large armies, of the same stock with particular tribes previously existing.
- **Translation**: 

---

### Verse 15 (Ramayana 0.240)
- **Original**: 222 The Ramayana Or as in swift eclipse the Sun Dark with the doom he cannot shun: Or a poor bird with mangled wing— So, reft of sons and host, the king No longer, by ambition fired, The pride of war his breast inspired. He gave his empire to his son— Of all he had, the only one: And bade him rule as kings are taught Then straight a hermit-grove he sought. Far to Himálaya's side he fled, Which bards and Nágas visited, And, Mahádeva's231 grace to earn, He gave his life to penance stern. A lengthened season thus passed by, When Ziva's self, the Lord most High, Whose banner shows the pictured bull,232 Appeared, the God most bountiful: “Why fervent thus in toil and pain? What brings thee here? what boon to gain? Thy heart's desire, O Monarch, speak: I grant the boons which mortals seek.” The king, his adoration paid, To Mahádeva answer made: “If thou hast deemed me fit to win Thy favour, O thou void of sin, On me, O mighty God, bestow The wondrous science of the bow, All mine, complete in every part, With secret spell and mystic art. To me be all the arms revealed 231 The Great God,Ziva. 232 Nandi, the snow-white bull, the attendant and favourite vehicle ofZiva.
- **Translation**: 

---

### Verse 16 (Ramayana 0.241)
- **Original**: Canto LV. The Hermitage Burnt. 223 That Gods, and saints, and Titans wield, And every dart that arms the hands Of spirits, fiends and minstrel bands, Be mine, O Lord supreme in place, This token of thy boundless grace.” The Lord of Gods then gave consent, And to his heavenly mansion went. Triumphant in the arms he held, The monarch's breast with glory swelled. So swells the ocean, when upon His breast the full moon's beams have shone. Already in his mind he viewed Va [ishmha at his feet subdued. He sought that hermit's grove, and there Launched his dire weapons through the air, Till scorched by might that none could stay The hermitage in ashes lay. Where'er the inmates saw, aghast, The dart that Vi[vámitra cast, To every side they turned and fled In hundreds forth disquieted. Va [ishmha's pupils caught the fear, And every bird and every deer, And fled in wild confusion forth Eastward and westward, south and north, And so Va[ishmha's holy shade A solitary wild was made, Silent awhile, for not a sound Disturbed the hush that was around.
- **Translation**: 

---

### Verse 17 (Ramayana 0.242)
- **Original**: 224 The Ramayana Va [ishmha then, with eager cry, Called,“Fear not, friends, nor seek to fly. This son of Gádhi dies to-day, Like hoar-frost in the morning's ray.” Thus having said, the glorious sage Spoke to the king in words of rage: “Because thou hast destroyed this grove Which long in holy quiet throve, By folly urged to senseless crime, Now shalt thou die before thy time.” Canto LVI. Visvámitra's Vow. But Vi[vámitra, at the threat Of that illustrious anchoret, Cried, as he launched with ready hand A fiery weapon,“Stand, O Stand!” Va [ishmha, wild with rage and hate, Raising, as 'twere the Rod of Fate, His mighty Bráhman wand on high, To Vi[vámitra made reply: “Nay, stand, O Warrior thou, and show What soldier can, 'gainst Bráhman foe. O Gádhi's son, thy days are told; Thy pride is tamed, thy dart is cold. How shall a warrior's puissance dare With Bráhman's awful strength compare? To-day, base Warrior, shall thou feel That God-sent might is more than steel.” He raised his Bráhman staff, nor missed The fiery dart that near him hissed:
- **Translation**: 

---

### Verse 18 (Ramayana 0.243)
- **Original**: Canto LVI. Visvámitra's Vow. 225 And quenched the fearful weapon fell, As flame beneath the billow's swell. Then Gádhi's son in fury threw Lord VaruG's arm and Rudra's too: Indra's fierce bolt that all destroys; That which the Lord of Herds employs: The Human, that which minstrels keep, The deadly Lure, the endless Sleep: The Yawner, and the dart which charms; Lament and Torture, fearful arms: The Terrible, the dart which dries, The Thunderbolt which quenchless flies, And Fate's dread net, and Brahmá's noose, And that which waits for VaruG's use: The dart he loves who wields the bow Pináka, and twin bolts that glow With fury as they flash and fly, The quenchless Liquid and the Dry: The dart of Vengeance, swift to kill: The Goblins' dart, the Curlew's Bill: [068] The discus both of Fate and Right, And VishGu's, of unerring flight: The Wind-God's dart, the Troubler dread, The weapon named the Horse's Head. From his fierce hand two spears were thrown, And the great mace that smashes bone; The dart of spirits of the air, And that which Fate exults to bear: The Trident dart which slaughters foes, And that which hanging skulls compose:233 233 “The names of many of these weapons which are mythical and partly alle- gorical have occurred in Canto XXIX. The general signification of the story is clear enough. It is a contest for supremacy between the regal or military order
- **Translation**: 

---

### Verse 19 (Ramayana 0.244)
- **Original**: 226 The Ramayana These fearful darts in fiery rain He hurled upon the saint amain, An awful miracle to view. But as the ceaseless tempest flew, The sage with wand of God-sent power Still swallowed up that fiery shower. Then Gádhi's son, when these had failed, With Brahmá's dart his foe assailed. The Gods, with Indra at their head, And Nágas, quailed disquieted, And saints and minstrels, when they saw The king that awful weapon draw; And the three worlds were filled with dread, And trembled as the missile sped. The saint, with Bráhman wand, empowered By lore divine that dart devoured. Nor could the triple world withdraw Rapt gazes from that sight of awe; For as he swallowed down the dart Of Brahmá, sparks from every part, From finest pore and hair-cell, broke Enveloped in a veil of smoke. The staff he waved was all aglow Like Yáma's sceptre, King below, Or like the lurid fire of Fate Whose rage the worlds will desolate. and Bráhmanical or priestly authority, like one of those struggles which our own Europe saw in the middle ages when without employing warlike weapons the priesthood frequently gained the victory.” SCHLEGEL {FNS . For a full account of the early contests between the Bráhmans and the Kshattriyas, see Muir's Original Sanskrit Texts (Second edition) Vol. I. Ch. IV.
- **Translation**: 

---

### Verse 20 (Ramayana 0.245)
- **Original**: Canto LVII. Trisanku. 227 The hermits, whom that sight had awed, Extolled the saint, with hymn and laud: “Thy power, O Sage, is ne'er in vain: Now with thy might thy might restrain. Be gracious, Master, and allow The worlds to rest from trouble now; For Vi[vámitra, strong and dread, By thee has been discomfited.” Then, thus addressed, the saint, well pleased, The fury of his wrath appeased. The king, o'erpowered and ashamed, With many a deep-drawn sigh exclaimed: “Ah! Warriors' strength is poor and slight; A Bráhman's power is truly might. This Bráhman staff the hermit held The fury of my darts has quelled. This truth within my heart impressed, With senses ruled and tranquil breast My task austere will I begin, And Bráhmanhood will strive to win.” Canto LVII. Trisanku. Then with his heart consumed with woe, Still brooding on his overthrow By the great saint he had defied, At every breath the monarch sighed. Forth from his home his queen he led, And to a land far southward fled. There, fruit and roots his only food,
- **Translation**: 

---

