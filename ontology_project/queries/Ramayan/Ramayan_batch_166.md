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

### Verse 1 (Ramayana 0.1346)
- **Original**: 1328 The Ramayana The PáG yas'703 gates of pearl and gold. Then, with your task maturely planned, On ocean's shore your feet will stand. Where, by Agastya's high decree, Mahendra,704 planted in the sea, With tinted peaks against the tide Rises in solitary pride, And glorious in his golden glow Spurns back the waves that beat below. Fair mountain, bright with creepers' bloom And every tint that trees assume, Where Yaksha, God, and heavenly maid Meet wandering in the lovely shade, At changing moon and solemn tide By Indra's presence glorified. One hundred leagues in fair extent An island705 fronts the continent: No man may tread its glittering shore, With utmost heed that isle explore, For the fair country owns the sway Of RávaG whom we burn to slay. A mighty monster stands to keep The passage of the southern deep. Lifting her awful arms on high She grasps e'en shadows as they fly. Speed through that isle, and onward still Where in mid sea the Flowery Hill706 Raises on high his bloomy head 703 The PáG yas are a people of the Deccan. 704 Mahendra is the chain of hills that extends from Orissa and the northern Sircars to Gondwána, part of which near Ganjam is still called Mahendra Malay or hills of Mahendra. 705 Lanká, Sinhaladvípa, Sarandib, or Ceylon. 706 The Flowery Hill of course is mythical.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1347)
- **Original**: Canto XLI. The Army Of The South. 1329 By saints and angels visited. There, with a hundred gleaming peaks Bright as the sun, the sky he seeks, One glorious peak the Lord of Day Gilds ever with his loving ray; Thereon ne'er yet the glances fell Of thankless wretch or infidel. Bow to that hill in reverence due, And then once more your search pursue. Beyond that glorious mountain hie, And Súryaván,707 proud hill is nigh. Your rapid course yet farther bend Where Vaidyut's708 airy peaks ascend. There trees of noblest sort, profuse Of wealth, their kindly gifts produce. Their precious fruits, O Vánars, taste, The honey sip, and onward haste. Next will ye see Mount Kunjar rise, Who cheers with beauty hearts and eyes. There is Agastya's709 mansion, decked By heaven's all moulding architect. Near Bhogavatí710 stands, the place Where dwell the hosts of serpent race: A broad-wayed city, walled and barred, Which watchful legions keep and guard, The fiercest of the serpent youth, Each awful for his venomed tooth: 707 The whole of the geography south of Lanká is of course mythical. Súryaván means Sunny. 708 Vaidyut means connected with lightning. 709 Agastya is here placed far to the south of Lanká. Earlier in this Canto he was said to dwell on Malaya. 710 Bhogavatí has been frequently mentioned: it is the capital of the serpent Gods or demons, and usually represented as being in the regions under the earth.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1348)
- **Original**: 1330 The Ramayana And throned in his imperial hall Is Vásuki711 who rules them all. Explore the serpent city well, Search town and tower and citadel, And scan each field and wood that lies Around it, with your watchful eyes. Beyond that spot your way pursue: A noble mountain shall ye view, Named Rishabh, like a mighty bull, With gems made bright and beautiful.[376] All trees of sandal flourish there Of heavenly fragrance, rich and rare. But, though they tempt your longing eyes, Avoid to touch them, and be wise. For Rohitas, a guardian band Of fierce Gandharvas, round them stand, Who five bright sovereign lords712 obey, In glory like the God of Day. Here by good deeds a home is won With shapes like fire, the moon, the sun. Here they who merit heaven by worth Dwell on the confines of the earth. There stay: beyond it, dark and drear, Lies the departed spirits' sphere, And, girt with darkness, far from bliss, Is Yáma's sad metropolis.713 So far, my lords, o'er land and sea Your destined course is plain and free. Beyond your steps you may not set, 711 Vásuki is according to some accounts the king of the Nágas or serpent Gods. 712 Zailúsha, GramiGi, Siksha, Suka, Babhru. 713 The distant south beyond the confines of the earth is the home of departed spirits and the city of Yáma the God of Death.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1349)
- **Original**: Canto XLII. The Army Of The West. 1331 Where living thing ne'er journeyed yet. With utmost care these realms survey, And all you meet upon the way. And, when the lady's course is traced, Back to your king, O Vánars, haste. And he who tells me he has seen. After long search, the Maithil queen, Shall gain a noble guerdon: he In power and bliss shall equal me. Dear as my very life, above His fellows in his master's love; I call him, yea though stained with crime. My kinsman from that happy time.” Canto XLII. The Army Of The West. Then to SusheG Sugríva bent, And thus addressed him reverent: “Two hundred thousand of our best With thee, my lord, shall seek the west. Explore Suráshmra's714] distant plain, Explore Váhlíka's715 wild domain, And all the pleasant brooks that flee Through mountains to the western sea. Search clustering groves on mountain heights, And woods the home of anchorites. Search where the breezy hills are high, Search where the desert regions lie. 714 Suráshmra, the“good country,” is the modern Sura 715 A country north-west of Afghanistan, Baíkh.
- **Translation**: 

---

### Verse 5 (Ramayana 0.1350)
- **Original**: 1332 The Ramayana Search all the western land beset With woody mountains like a net. The country`s farthest limit reach, And stand upon the ocean beach. There wander through the groves of palm Where the soft air is full of balm. Through grassy dell and dark ravine Seek RávaG and the Maithil queen. Go visit Somagiri's716 steep Where Sindhu717 mingles with the deep. There lions, borne on swift wings, roam The levels of their mountain home, And elephants and monsters bear, Caught from the ocean, to their lair. You Vánars, changing forms at will, With rapid search must scour the hill, And his sky-kissing peak of gold Where loveliest trees their blooms unfold. There golden-peaked, ablaze with light, Uprises Páriyátra's718 height Where wild Gandharvas, fierce and fell, In bands of countless myriads dwell. Pluck ye no fruit within the wood; Beware the impious neighbourhood, Where, very mighty, strong, and hard To overcome, the fruit they guard. Yet search for Janak's daughter still, For Vánars there need fear no ill. Near, bright as turkis, Vajra719 named, 716 The Moon-mountain here is mythical. 717 Sindhu is the Indus. 718 Páriyátra, or as more usually written Páripátra, is the central or western portion of the Vindhya chain which skirts the province of Malwa. 719 Vajra means both diamond and thunderbolt, the two substances being
- **Translation**: 

---

### Verse 6 (Ramayana 0.1351)
- **Original**: Canto XLII. The Army Of The West. 1333 There stands a hill of diamond framed. Soaring a hundred leagues in pride, With trees and creepers glorified. Search there each cave and dark abyss By waterfall and precipice. Far in that sea the wild waves beat On Chakraván's720 firm-rooted feet. Where the great discus,721 thousand rayed, By Vísvakarmá's722 art was made. When Panchajan723 the fiend was slain. And Hayagríva,724 fierce in vain, [377] Thence taking shell and discus went Lord VishGu, God preëminent. On! sixty thousand hills of gold With wondering eyes shall ye behold, Where in his glory every one Is brilliant as the morning sun. Full in the midst King Meru,725 best Of mountains, lifts his lofty crest, supposed to be identical. 720 Chakraván means the discus-bearer. 721 The discus is the favourite weapon of VishGu. 722 The Indian Hephaistos or Vulcan. 723 Panchajan was a demon who lived in the sea in the form of a conch shell. W ILSON 'S{FNS VishGu PuráGa, V. 21. 724 Hayagríva, Horse-necked, is the name of a Daitya who at the dissolution of the universe caused by Brahmá's sleep, seized and carried off the Vedas. VishGu slew him and recovered the sacred treasures. 725 Meru stands in the centre of Jambudwípa and consequently of the earth. “The sun travels round the world, keeping Meru always on his right. To the spectator who fronts him, therefore, as he rises Meru must be always on the north; and as the sun's rays do not penetrate beyond the centre of the mountain, the regions beyond, or to the north of it must be in darkness, whilst those on the south of it must be in light: north and south being relative, not absolute, terms, depending on the position of the spectator with regard to the Sun and Meru.” W ILSON 'S{FNS VishGu PuráGa, Vol. II. p. 243. Note.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1352)
- **Original**: 1334 The Ramayana On whom of yore, as all have heard, The sun well-pleased this boon conferred: “On thee, O King, on thee and thine Light, day and night, shall ever shine. Gandharvas, Gods who love thee well And on thy sacred summits dwell, Undimmed in lustre, bright and fair, The golden sheen shall ever share.” The Vi[vas,726 Vasus,727 they who ride The tempest,728 every God beside, Draw nigh to Meru's lofty crest When evening darkens in the west, And to the parting Lord of Day The homage of their worship pay, Ere yet a while, unseen of all, Behind Mount Asta's729 peaks he fall. Wrought by the heavenly artist's care A glorious palace glitters there, And round about it sweet birds sing Where the gay trees are blossoming: The home of VaruG730 high-souled lord, Wrist-girded with his deadly cord.731 With ten tall stems, a palm between 726 The Vi[vadevas are a class of deities to whom sacrifices should be daily offered, as part of the ordinary worship of the householder. According to the Váyu PuráGa, this is a privilege conferred on them by Brahmá and the Pitris as a reward for religious austerities practised by them upon Himálaya. 727 The eight Vasus were originally personifications like other Vedic deities, of natural phenomena, such as Fire, Wind, &c. Their appellations are variously given by different authorities. 728 The Maruts or Storm-Gods, frequently addressed and worshipped as the attendants and allies of Indra. 729 The mountain behind which the sun sets. 730 One of the oldest and mightiest of the Vedic deities; in later mythology regarded as the God of the sea. 731 The knotted noose with which he seizes and punishes transgressors.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1353)
- **Original**: Canto XLII. The Army Of The West. 1335 Meru and Asta's hill is seen: Pure silver from the base it springs, And far and wide its lustre flings. Seek RávaG and the dame by brook, In pathless glen, in leafy nook On Meru's crest a hermit lives Bright with the light that penance gives: SávarGi732 is he named, renowned As Brahmá's peer, with glory crowned. There bowing down in reverence speak And ask him of the dame you seek. Thus far the splendid Lord of Day Pursues through heaven his ceaseless way, Shedding on every spot his light; Then sinks behind Mount Asta's height, Thus far advance: the sunless sea Beyond is all unknown to me. SusheG of mighty arm, long tried In peril, shall your legions guide. Receive his words with high respect, And ne'er his lightest wish neglect. He is my consort's sire, and hence Deserves the utmost reverence.” 732 SávarGi is a Manu, offspring of the Sun by Chháyá.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1354)
- **Original**: 1336 The Ramayana Canto XLIII. The Army Of The North. Forth went the legions of the west: And wise Sugríva addressed Zatabal, summoned from the crowd. To whom the sovereign cried aloud: “Go forth, O Vánar chief, go forth, Explore the regions of the north. Thy host a hundred thousand be, And Yáma's sons733 attend on thee. With dauntless courage, strength, and skill Search every river, wood, and hill. Through every land in order go Right onward to the Hills of Snow. Search mid the peaks that shine afar, In woods of Lodh and Deodár.734 Search if with Janak's daughter, screened By sheltering rocks, there lie the fiend.[378] The holy grounds of Soma tread By Gods and minstrels visited. Reach Kála's mount, and flats that lie Among the peaks that tower on high. Then leave that hill that gleams with ore, And fair Sudar[an's heights explore. Then on to Devasakhá735 hie, Loved by the children of the sky. A dreary land you then will see Without a hill or brook or tree, A hundred leagues, bare, wild, and dread 733 The poet has not said who the sons of Yáma are. 734 The Lodhra or Lodh (Symplocos Racemosa) and the Devadáru or Deodar are well known trees. 735 The hills mentioned are not identifiable. Soma means the Moon. Kála, black; Sudara[an, fair to see; and Devasakhá friend of the Gods.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1355)
- **Original**: Canto XLIII. The Army Of The North. 1337 In lifeless desolation, spread. Pursue your onward way, and haste Through the dire horrors of the waste Until triumphant with delight You reach Kailása's glittering height. There stands a palace decked with gold, For King Kuvera736 wrought of old, A home the heavenly artist planned And fashioned with his cunning hand. There lotuses adorn the flood With full-blown flower and opening bud Where swans and mallards float, and gay Apsarases737 come down to play. There King Vai[ravaG's738 self, the lord By all the universe adored, Who golden gifts to mortals sends, Lives with the Guhyakas739 his friends. Search every cavern in the steep, And green glens where the moonbeams sleep, If haply in that distant ground The robber and the dame be found. Then on to Krauncha's hill,740 and through His fearful pass your way pursue: Though dark and terrible the vale Your wonted courage must not fail. There through abyss and cavern seek, On lofty ridge, and mountain peak, 736 The God of Wealth. 737 The nymphs of Paradise. 738 Kuvera the son of Vi[ravas. 739 A class of demigods who, like the Yakshas, are the attendants of Kuvera, and the guardians of his treasures. 740 Situated in the eastern part of the Himálaya chain, on the north of Assam. The mountain was torn asunder and the pass formed by the War-God Kártikeya and Para[uráma.
- **Translation**: 

---

### Verse 11 (Ramayana 0.1356)
- **Original**: 1338 The Ramayana On, on! pursue your journey still By valley, lake, and towering hill. Reach the North Kurus' land, where rest The holy spirits of the blest: Where golden buds of lilies gleam Resplendent on the silver stream, And leaves of azure turkis throw Soft splendour on the waves below. Bright as the sun at early morn Fair pools that happy clime adorn, Where shine the loveliest flowers on stems Of crystal and all valued gems. Blue lotuses through all the land The glories of their blooms expand, And the resplendent earth is strown With peerless pearl and precious stone. There stately trees can scarce uphold The burthen of their fruits of gold, And ever flaunt their gay attire Of flower and leaf like flames of fire. All there sweet lives untroubled spend In bliss and joy that know not end, While pearl-decked maidens laugh, or sing To music of the silvery string.741. Still on your forward journey keep, And rest you by the northern deep, Where springing from the billows high 741 “The Uttara Kurus, it should be remarked, may have been a real people, as they are mentioned in the Aitareya BráhmaGa, VIII. 14.… Wherefore the several nations who dwell in this northern quarter, beyond the Himavat, the Uttara Kurus and the Uttara Madras are consecrated to glorious dominion, and people term them the glorious. In another passage of the same work, howev- er, the Uttara Kurus are treated as belonging to the domain of mythology.” M UIR 'S{FNS Sanskrit Texts. Vol. I. p. 494. See ADDITIONAL N OTES {FNS
- **Translation**: 

---

### Verse 12 (Ramayana 0.1357)
- **Original**: Canto XLIV. The Ring. 1339 Mount Somagiri742 seeks the sky, And lightens with perpetual glow The sunless realm that lies below. There, present through all life's extent, Dwells Brahmá Lord preëminent, And round the great God, manifest In Rudra743 forms high sages rest. Then turn, O Vánars: search no more, Nor tempt the sunless, boundless shore.” Canto XLIV. The Ring. But special counselling he gave To Hanumán the wise and brave: [379] To him on whom his soul relied, With friendly words the monarch cried: “O best of Vánars, naught can stay By land or sea thy rapid way, Who through the air thy flight canst bend, And to the Immortals' home ascend. All realms, I ween, are known to thee With every mountain, lake, and sea. In strength and speed which naught can tire Thou, worthy rival of thy sire The mighty monarch of the wind, Where'er thou wilt a way canst find. 742 The Moon-mountain. 743 The Rudras are the same as the storm winds, more usually called Maruts, and are often associated with Indra. In the later mythology the Rudras are regarded as inferior manifestations ofZiva, and most of their names are also names ofZiva.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1358)
- **Original**: 1340 The Ramayana Exert thy power, O swift and strong, Bring back the lady lost so long, For time and place, O thou most wise, Lie open to thy searching eyes.” When Ráma heard that special hest To Hanumán above the rest, He from the monarch's favour drew Hope of success and trust anew That he on whom his lord relied, In toil and peril trained and tried, Would to a happy issue bring The task commanded by the king. He gave the ring that bore his name, A token for the captive dame, That the sad lady in her woe The missive of her lord might know. “This ring,” he said,“my wife will see, Nor fear an envoy sent by me. Thy valour and thy skill combined, Thy resolute and vigorous mind, And King Sugríva's high behest, With joyful hopes inspire my breast.” Canto XLV. The Departure.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1359)
- **Original**: Canto XLV. The Departure. 1341 Away, away the Vánars sped Like locusts o'er the land outspread. To northern realms where rising high The King of Mountains cleaves the sky, FierceZatabal with vast array Of Vánar warriors led the way. Far southward, as his lord decreed, Wise Hanumán, the Wind-God's seed, With Angad his swift way pursued, And Tára's warlike multitude, Strong Vinata with all his band Betook him to the eastern land, And brave SusheG in eager quest Sped swiftly to the gloomy west. Each Vánar chieftain sought with speed The quarter by his king decreed, While from his legions rose on high The shout and boast and battle cry: “We will restore the dame and beat The robber down beneath our feet. My arm alone shall win the day From RávaG met in single fray, Shall rob the robber of his life, And rescue Ráma's captive wife All trembling in her fear and woe. Here, comrades, rest: no farther go: For I will vanquish hell, and she Shall by this arm again be free. The rooted mountains will I rend, The mightiest trees will break and bend, Earth to her deep foundations cleave, And make the calm sea throb and heave. A hundred leagues from steep to steep In desperate bound my feet shall leap.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1360)
- **Original**: 1342 The Ramayana My steps shall tread unchecked and free, Through woods, o'er land and hill and sea, Range as they list from flood to fell, And wander through the depths of hell.” Canto XLVI. Sugríva's Tale. “How, King,” cried Ráma,“didst thou gain Thy lore of sea and hill and plain?” “I told thee how,” Sugríva said, “From Báli's arm Máyáví fled744 To Malaya's hill, and strove to save His life by hiding in the cave. I told how Báli sought, to kill His foe, the hollow of the hill; Nor need I, King, again unfold The wondrous tale already told. Then, wandering forth, my way I took By many a town and wood and brook. I roamed the earth from place to place, Till, like a mirror's polished face, The whole broad disk, that lies between Its farthest bounds, mine eyes had seen. I wandered first to eastern skies Where fairest trees rejoiced mine eyes, And many a cave and wooded hill Where lilies robed the lake and rill. There metal dyes that hill745 adorn 744 Canto IX. 745 Udayagiri or the hill from which the sun rises.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1361)
- **Original**: Canto XLVI. Sugríva's Tale. 1343 Whence springs the sun to light the morn. There, too, I viewed the Milky sea, Where nymphs of heaven delight to be. Then to the south I made my way From regions of the rising day, And roamed o'er Vindhya, where the breeze Is odorous of sandal trees. Still in my fear I found no rest: I sought the regions of the west, And gazed on Asta,746 where the sun [380] Sinks when his daily course is run. Then from that noblest hill I fled And to the northern country sped, Saw Himaván,747 and Meru's steep, And stood beside the northern deep. But when, by Báli's might oppressed, E'en in those wilds I could not rest, Came Hanumán the wise and brave, And thus his prudent counsel gave: “'I told thee how Matanga748 cursed Thy tyrant, that his head should burst In pieces, should he dare invade The precincts of that tranquil shade. There may we dwell in peace and be From thy oppressor's malice free.” We went to Rishyamúka's hill, And spent our days secure from ill Where, with that curse upon his head, The cruel Báli durst not tread.” 746 Asta is the mountain behind which the sun sets. 747 Himálaya, the Hills of Snow. 748 Canto XI.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1362)
- **Original**: 1344 The Ramayana Canto XLVII. The Return. Thus forth in quest of Sítá went The legions King Sugríva sent. To many a distant town they hied By many a lake and river's side. As their great sovereign's order taught, Through valleys, plains, and groves they sought. They toiled unresting through the day: At night upon the ground they lay Where the tall trees, whose branches swayed Beneath their fruit, gave pleasant shade. Then, when a weary month was spent, Back to Pra[ravaG's hill they went, And stood with faces of despair Before their king Sugríva there. Thus, having wandered through the east, Great Vinata his labours ceased, And weary of the fruitless pain Returned to meet the king again, Brave Zatabali to the north Had led his Vánar legions forth. Now to Sugríva he sped With all his host dispirited. SusheG the western realms had sought, And homeward now his legions brought. All to Sugríva came, where still He sat with Ráma on the hill. Before their sovereign humbly bent And thus addressed him reverent: “On every hill our steps have been, By wood and cave and deep ravine; And all the wandering brooks we know Throughout the land that seaward flow,
- **Translation**: 

---

### Verse 18 (Ramayana 0.1363)
- **Original**: Canto XLVIII. The Asur's Death. 1345 Our feet by thy command have traced The tangled thicket and the waste, And dens and dingles hard to pass for creeping plants and matted grass. Well have we searched with toil and pain, And monstrous creatures have we slain But Hanumán of noblest mind The Maithil lady yet will find; For to his quarter of the sky749 The robber fiend was seen to fly.” Canto XLVIII. The Asur's Death. But Hanumán still onward pressed With Tára, Angad, and the rest, Through Vindhya's pathless glens he sped And left no spot unvisited. He gazed from every mountain height, He sought each cavern dark as night, And wandered through the bloomy shade By pool and river and cascade, But, though they sought in every place, Of Sítá yet they found no trace. On fruit and woodland berries fed Through many a lonely wild they sped, And reached at last, untouched by fear, A desert terrible and drear: A fruitless waste, a land of gloom 749 Hanumán was the leader of the army of the south which was under the nominal command of Angad the heir apparent.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1364)
- **Original**: 1346 The Ramayana Where trees were bare of leaf and bloom, Where every scanty stream was dried, And niggard earth her roots denied. No elephants through all the ground, No buffaloes or deer are found. There roams no tiger, pard, or bear, No creature of the wood is there. No bird displays his glittering wings, No tree, no shrub, no creeper springs. There rise no lilies from the flood, Resplendent with their flower and bud, Where the delighted bees may throng About the fragrance with their song. There lived a hermit KaGdu named, For truth and wealth of penance famed. Whom fervent zeal and holy rite Had dowered with all-surpassing might. His little son, a ten year child— So chanced it— perished in the wild. His death with fury stirred the sage, Who cursed the forest in his rage, Doomed from that hour to shelter none, A waste for bird and beast to shun.[381] They searched by every forest edge, They searched each cave and mountain ledge, And thickets whence the water fell Wandering through the tangled dell. Striving to do Sugríva's will They roamed along each leafy rill. But vain were all endeavours, vain The careful search, the toil and pain. Through one dark grove they scarce could wind, So thick were creepers intertwined. There as they struggled through the wood
- **Translation**: 

---

### Verse 20 (Ramayana 0.1365)
- **Original**: Canto XLIX. Angad's Speech. 1347 Before their eyes an Asur750 stood. High as a towering hill, his pride The very Gods in heaven defied. When on the fiend their glances fell Each braced him for the combat well. The demon raised his arm on high, And rushed upon them with a cry. Him Angad smote,— for, sure, he thought This was the fiend they long had sought. From his huge mouth by Angad felled, The blood in rushing torrents welled, As, like a mountain from his base Uptorn, he dropped upon his face. Thus fell the mighty fiend: and they Through the thick wood pursued their way; Then, weary with the toil, reclined Where leafy boughs to shade them twined. Canto XLIX. Angad's Speech. Then Angad spake:“We Vánars well Have searched each valley, cave, and dell, And hill, and brook, and dark recess, And tangled wood, and wilderness. But all in vain: no eye has seen The robber or the Maithil queen. A dreary time has passed away, And stern is he we all obey. 750 The Bengal recension— Gorresio's edition— calls this Asur or demon the son of Márícha.
- **Translation**: 

---

