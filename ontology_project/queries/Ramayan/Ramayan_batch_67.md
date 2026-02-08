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

### Verse 1 (Ramayan 0.1321)
- **Original**: Canto XXXV. Tárá's Speech. 1303 Who many a weary year has spent Stranger to love and blandishment. Let not this wrath thy soul inflame, Like some mean wretch unknown to fame: For high and noble hearts like thine Love mercy and to ruth incline, Calm and deliberate, and slow With anger's raging fire to glow. At length, O righteous prince, relent, Nor let my words in vain be spent, This sudden blaze of fury slake, I pray thee for Sugríva's sake. He would renounce at Ráma's call Rumá and Angad, me and all Who call him lord: his gold and grain, The favour of his friend to gain. His arm shall slay the fiend more base In soul than all his impious race, And happy Ráma reunite To Sítá, rival in delight Of the triumphant Moon when he Rejoins his darling RohiGí.641 Ten million million demons guard The gates of Lanká firmly barred. All hope until that host be slain, To smite the robber king is vain. Nor with Sugríva's aid alone May king and host be overthrown. Thus ere he died— for well he knew— Spake Báli, and his words are true. I know not what his proofs might be, 641 RohiGí is the name of the ninth Nakshatra or lunar asterism personified as a daughter of Daksha, and the favourite wife of the Moon. Aldebaran is the principal star in the constellation.
- **Translation**: 

---

### Verse 2 (Ramayan 0.1322)
- **Original**: 1304 The Ramayana But speak the words he spake to me. Hence far and wide our lords are sent To raise the mightiest armament, For their return Sugríva waits Ere he can sally from his gates. Still is the oath Sugríva swore Kept firmly even as before: And the great host this day will be Assembled by the king's decree, Ten thousand thousand troops, who wear The form of monkey and of bear, Prepared for thee the war to wage: Then let thy wrath no longer rage. The matrons of the Vánar race See marks of fury in thy face; They see thine eyes like blood are red, And will not yet be comforted.” Canto XXXVI. Sugríva's Speech. She ceased: and LakshmaG gave assent, Won by her gentle argument. So Tárá's pleading, just and mild, His softening heart had reconciled. His altered mood Sugríva saw, And cast aside the fear and awe Like raiment heavy with the rain Which on his troubled soul had lain. Then quickly to the ground he threw His flowery garland, bright of hue, Which round his royal neck he wore,
- **Translation**: 

---

### Verse 3 (Ramayan 0.1323)
- **Original**: Canto XXXVI. Sugríva's Speech. 1305 And, sobered, was himself once more. Then turning to the princely man In soothing words the king began: “My glory, wealth, and royal sway To other hands had passed away: But Ráma to my rescue came, And gave me back my power and fame. O Lakshma G, say, whose grateful heart [368] Could nurse the hope to pay in part, By service of a life, the deed Of Ráma sprung of heavenly seed? His foeman RávaG shall be slain, And Sítá shall be his again. The hero's side I will not leave, But he the conquest shall achieve. What need of help has he who drew His bow, and one great arrow flew Through seven tall trees, a mountain rent, And cleft the earth with force unspent? What aid needs he who shook his bow, And at the sound the earth below With hill and wood and rooted rock Quaked feverous with the thunder shock? Yet all my legions will I bring, And follow close the warrior king Marching on his impetuous way Fierce RávaG and his hosts to slay. If I be guilty of offence, Careless through love or negligence, Let him his loyal slave forgive; For error cleaves to all who live.” Thus king Sugríva, good and brave, In humble words his answer gave,
- **Translation**: 

---

### Verse 4 (Ramayan 0.1324)
- **Original**: 1306 The Ramayana Softened was LakshmaG's angry mood Who thus his friendly speech renewed: “My brother, Vánar King, will see A champion and a friend in thee. So strong art thou, so brave and bold, So pure in thought, so humble-souled, That thou deservest well to reign And all a monarch's bliss to gain. Lend thou my brother aid, and all His foes beneath his arm will fall. Full well the words thou speakest suit A chieftain wise and resolute. With grateful heart that loves the right, And foot that never yields in fight. O come, and my sad brother cheer Who mourns the wife he holds so dear. O pardon, friend, my harsh address, And Ráma's frantic bitterness.” Canto XXXVII. The Gathering. He ceased: and King Sugríva cried To sage Hanúmán642 by his side: “Summon the Vánar legions, those Who dwell about the Lord of Snows: Those who in Vindhyan groves delight, Kailása's, or Mahendra's height, Dwell on the Five bright Peaks, or where 642 Válmíki and succeeding poets make the second vowel in this name long or short at their pleasure.
- **Translation**: 

---

### Verse 5 (Ramayan 0.1325)
- **Original**: Canto XXXVII. The Gathering. 1307 Mandar's white summit cleaves the air: Wherever they are wandring free In highlands by the western sea, On that east hill whence springs the sun, Or where he sinks when day is done. Call the great chiefs whose legions fill The forests of the Lotus Hill,643 Where every one in strength and size With the stupendous Anjan644 vies. Call those, with tints of burnished gold Whom Mahá [aila's caverns hold: Those who on Dhúmra roam, or hide In the wild woods on Meru's side. Call those who, brilliant as the sun, On high MaháruG leap and run, Quaffing sweet juices that distil From odorous trees upon the hill, Call those whom tranquil haunts delight, Where dwell the sage and anchorite In groves that through their wide extent Exhale a thousand blossoms' scent. Send out, send out: from coast to coast Assemble all the Vánar host: With force, with words, with gifts of price Compel, admonish and entice. Already envoys have been sent 643 Some of the mountains here mentioned are fabulous and others it is im- possible to identify. Sugríva means to include all the mountains of India from Kailás the residence of the God Kuvera, regarded as one of the loftiest peaks of the Himálayas, to Mahendra in the extreme south, from the mountain in the east where the sun is said to rise to Astáchal or the western mountain where he sets. The commentators give little assistance: that Mahá[aila, &c. are certain mountains is about all the information they give. 644 One of the celestial elephants of the Gods who protect the four quarters and intermediate points of the compass.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1326)
- **Original**: 1308 The Ramayana To warn them of their lord's intent. Let others urged by thee repeat My mandate that their steps be fleet. Those lords who yielding to the sway Of love's delight would fain delay, Urge hither with the utmost speed, Or with thee to my presence lead: And those who linger to the last Until ten days be come and passed, And dare their sovereign to defy, For their offence shall surely die. Thousands, yea millions, shall there be, Obedient to their king's decree, The lions of the Vánar race, Assembled from each distant place, Forth shall they haste like hills in size, Or mighty clouds that veil the skies, And swiftly speeding on their way Bring all our legions in array.”[369] He ceased: the son of Váyu645 heard, Submissive to his sovereign's word; And sent his rapid envoys forth To east and west and south and north. They bent their airy course afar Along the paths of bird and star, And sped through ether farther yet Where VishGu's splendid sphere is set.646 By sea, on hill, by wood and lake They called to arms for Ráma's sake, As each with terror in his breast Obeyed his awful king's behest. 645 Váyu or the Wind was the father of Hanumán. 646 The path or station of VishGu is the space between the seven Rishis or Ursa Major, and Dhruva or the polar star.
- **Translation**: 

---

### Verse 7 (Ramayan 0.1327)
- **Original**: Canto XXXVII. The Gathering. 1309 Three million Vánars, fierce and strong As Anjan's self, a wondrous throng Sped from the spot where Ráma still Gazed restless from the woody hill. Ten million others, brave and bold, With coats that shone like burning gold, Came flying from the mountain crest Where sinks the weary sun to rest. Impetuous from the northern skies, Where Mount Kailása's summits rise, Ten hundred millions hasted, hued Like manes of lions, ne'er subdued: The dwellers on Himálaya's side, Whose food his roots and fruit supplied, With rangers of the Vindhyan chain And neighbours of the Milky Main.647 Some from the palm groves where they fed, Some from the woods of betel sped: In countless numbers, fierce and brave, They came from mountain, lake, and cave. As on their way the Vánars went To rouse each distant armament, They chanced that wondrous tree to view That on Himálaya's summit grew. Of old upon that sacred height Was wrought Mahe[var's648 glorious rite, Which every God in heaven beheld, And his glad heart with triumph swelled. There from pure seed at random sown Bright plants with luscious fruit had grown, 647 One of the seven seas which surround the earth in concentric circles. 648 The title of Mahe[var or Mighty Lord is sometimes given to Indra, but more generally toZiva whom it here denotes.
- **Translation**: 

---

### Verse 8 (Ramayan 0.1328)
- **Original**: 1310 The Ramayana And, sweet as Amrit to the taste, The summit of the mountain graced. Who once should eat the virtuous fruit That sprang from so divine a root, One whole revolving moon should be From every pang of hunger free. The Vánars culled the fruit they found Ripe on the sacrificial ground With rare celestial odours sweet, To lay them at Sugríva's feet. Those noble envoys scoured the land To summon every Vánar band Then swiftly homeward at the head Of countless armaments they sped. They gathered by Kishkindhá's wall. They thronged Sugríva's palace hall, And, richly laden, bare within That fruit of heavenly origin. Their gifts before their king they spread, And thus in tones of triumph said: “Through every land our way we took To visit hill and wood and brook, And all thy hosts from east to west Flock hither at their lord's behest.” Sugríva with delighted look The present of his envoys took, Then bade them go, with gracious speech Rewarding and dismissing each.
- **Translation**: 

---

### Verse 9 (Ramayan 0.1329)
- **Original**: Canto XXXVIII. Sugríva's Departure. 1311 Canto XXXVIII. Sugríva's Departure. Thus all the princely Vánars, true To their appointed tasks, withdrew. Sugríva deemed already done The work he planned for Raghu's son. Then LakshmaG gently spoke and cheered Sugríva for his valour feared: “Now, chieftain, if thy will be so, Forth from Kishkindhá let us go.” Sugríva's heart swelled high with pride As to the prince he thus replied: “Come, speed we forth without delay: 'Tis mine thy mandate to obey.” Sugríva bade the dames adieu, And Tárá and the rest withdrew. Then at their chieftain's summons came The Vánars first in rank and fame, A trusty brave and reverent band, Meet e'en before a queen to stand. They at his call made haste to bring The litter of the glorious king. “Mount, O my friend.” Sugríva cried, And straight Sumitrá's son complied. Then took by LakshmaG's side his place The sovereign of the woodland race, Upraised by Vánars, fleet and strong, Who bore the glittering load along. On high above his royal head A paly canopy was spread, And chouries white in many a hand The forehead of the monarch fanned, And shell and drum and song and shout Pealed round him as the king passed out. [370]
- **Translation**: 

---

### Verse 10 (Ramayan 0.1330)
- **Original**: 1312 The Ramayana About the monarch went a throng Of Vánar warriors brave and strong, As onward to the mountain shade Where Ráma dwelt his way he made. Soon as the lovely spot he viewed Where Ráma lived in solitude, The Vánar monarch, far-renowed, With LakshmaG, lightly stepped to ground, And to the son of Raghu went Joining his raised hands reverent. As their great leader raised his hands, So suppliant stood the Vánar bands. Well pleased the son of Raghu saw Those legions, hushed in reverent awe, Stand silent like the tranquil floods That raise their hands of lotus buds. But Ráma, when the king, to greet His friend, had bowed him at his feet, Raised him who ruled the Vánar race, And held him in a close embrace: Then, when his arms he had unknit, Besought him by his side to sit, And thus with gentle words the best Of men the Vánar king addressed: “The prince who well his days divides, And knows aright the times and tides To follow duty, joy, or gain, He, only he, deserves to reign. But he who wealth and virtue leaves, And every hour to pleasure cleaves, Falls from his bliss like him who wakes From slumber on a branch that breaks. True king is he who smites his foes,
- **Translation**: 

---

### Verse 11 (Ramayan 0.1331)
- **Original**: Canto XXXVIII. Sugríva's Departure. 1313 And favour to his servants shows, And of that fruit makes timely use Which virtue, wealth, and joy produce. The hour is come that bids thee rise To aid me in my enterprise. Then call thy nobles to debate, And with their help deliberate.” “Lost was my power,” the king replied, “All strength had fled, all hope had died. The Vánars owned another lord, But by thy grace was all restored. All this, O conqueror of the foe, To thee and LakshmaG's aid I owe. And his should be the villain's shame Who durst deny the sacred claim. These Vánar chiefs of noblest birth Have at my bidding roamed the earth, And brought from distant regions all Our legions at their monarch's call: Fierce bears with monkey troops combined, And apes of every varied kind, Terrific in their forms, who dwell In grove and wood and bosky dell: The bright Gandharvas' brood, the seed Of Gods,649 they change their shapes at need. Each with his legions in array, Hither, O Prince, they make their way. They come: and tens of millions swell To numbers that no tongue may tell.650 For thee their armies will unite 649 See Book I, Canto XVI. 650 The numbers are unmanageable in English verse. The poet speaks of hundreds ofarbudas; and anarbuda is a hundred millions.
- **Translation**: 

---

### Verse 12 (Ramayan 0.1332)
- **Original**: 1314 The Ramayana With chiefs, Mahendra's peers in might. From Meru and from Vindhya's chain They come like clouds that bring the rain. These round thee to the war will go, To smite to earth thy demon foe; Will slay the Rákshas and restore Thy consort when the fight is o'er.” Canto XXXIX. The Vánar Host. Then Ráma, best of all who guide Their steps by duty, thus replied: “What marvel if Lord Indra send The kindly rain, O faithful friend? If, thousand-rayed, the God of Day Drive every darksome cloud away? Or, rising high, the Lord of Night Flood the broad heaven with silver light? What marvel, King, that one like thee The glory of his friends should be? No marvel, O my lord, that thou Hast shown thy noble nature now. Thy heart, Sugríva, well I know: Naught from thy lips but truth may flow, With thee for friend and champion all My foes beneath my arm will fall. The Rákshas, when my queen he stole, Brought sure destruction on his soul,
- **Translation**: 

---

### Verse 13 (Ramayan 0.1333)
- **Original**: Canto XXXIX. The Vánar Host. 1315 Like Anuhláda651 who beguiled Queen Zachí called Puloma's child. Yes, near, Sugríva, is the day When I my demon foe shall slay, As conquering Indra in his ire Slew Queen Paulomí's haughty sire.”652 [371] He ceased: thick clouds of dust rose high To every quarter of the sky: The very sun grew faint and pale Behind the darkly-gathering veil. The mighty clouds that hung o'erhead From east to west thick darkness spread, And earth to her foundations shook With hill and forest, lake and brook. Then hidden was the ground beneath Fierce warriors armed with fearful teeth, Hosts numberless, each lord in size A match for him who rules the skies: From many a sea and distant hill, From rock and river, lake and rill. Some like the morning sun were bright, Some, like the moon, were silver white: These green as lotus fibres, those White-coated from their native snows.653 651 Anuhláda or Anuhráda is one of the four sons of the mighty HiraGyaka[ipu, an Asur or a Daitya son of Ka[yapa and Diti and killed by VishGu in his incarnation of the Man-LionNarasinha. According to the Bhágavata PuráGa the Daitya or Asur HiraGyaka[ipu and HiraGyáksha his brother, both killed by VishGu, were born again as RávaG and KumbhakarGa his brother. 652 Puloma, a demon, was the father-in-law of Indra who destroyed him in order to avert an imprecation. Paulomí is a patronymic denotingZachí the daughter of Puloma. 653 “Observe the variety of colours which the poem attributes to all these inhabitants of the different mountainous regions, some white, others yellow, &c. Such different colours were perhaps peculiar and distinctive characteristics of those various races.” G ORRESSIO {FNS .
- **Translation**: 

---

### Verse 14 (Ramayan 0.1334)
- **Original**: 1316 The Ramayana Then Zatabali came in view Girt by a countless retinue. Like some gold mountain high in air Tárá's illustrious sire654 was there. There Rumá`s father,655 far-renowned, With tens of thousands ranged around. There, tinted like the tender green Of lotus filaments, was seen, Compassed by countless legions, one Whose face was as the morning sun, Hanúmán's father good and great, Kesarí,656 wisest in debate. There the proud king Gaváksha, feared For his strong warrior arm, appeared. There Dhúmra, mighty lord, the dread Of foes, his ursine legions led. There Panas, first for warlike fame, With twenty million warriors came. There glorious Níla, dark of hue, Arrayed his countless troops in view. There moved lord Gavaya brave and bold, Resplendent like a hill of gold, And near him Darímukha stood With millions from the hill and wood And Dwivid famed for strength and speed, And Mamda, both of A[vin seed. There Gaja, strong and glorious, led The countless troops around him spread, 654 SusheG. 655 Tára. 656 Kesarí was the husband of Hanúmán's mother, and is here called his father.
- **Translation**: 

---

### Verse 15 (Ramayan 0.1335)
- **Original**: Canto XXXIX. The Vánar Host. 1317 And Jámbaván657 the king whose sway The bears delighted to obey, With swarming myriads onward pressed True to his lord Sugríva's hest; And princely Ruman, dear to fame, Led millions whom no hosts could tame, All these and many a chief beside658 Came onward fierce in warlike pride. They covered all the plain, and still Pressed forward over wood and hill. In rows for many a league around They rested on the grassy ground; Or to Sugríva made their way, Like clouds about the Lord of Day, And to the king their proud heads bent In power and might preeminent. Sugríva then to Ráma sped, And raised his reverent hands, and said That every chief from coast to coast Was present with his warrior host. 657 “I here unite under one heading two animals of very diverse nature and race, but which from some gross resemblances, probably helped by an equivoque in the language, are closely affiliated in the Hindoo myth… a reddish colour of the skin, want of symmetry and ungainliness of form, strength in hugging with the fore paws or arms, the faculty of climbing, shortness of tail(?), sen- suality, capacity of instruction in dancing and in music, are all characteristics which more or less distinguish and meet in bears as well as in monkeys. In theRámáya Gam , the wise Jámnavant, the Odysseus of the expedition of Lanká, is called now king of the bears (rikshaparthivah), now great monkey (Mahákapih).” D E G UBERNATIS {FNS :Zoological Mythology, Vol. II. p. 97. 658 Gandhamádana, Angad, Tára, Indrajánu, Rambha, Durmukha, Hanumán, Nala, Da mukha,Zarabha, Kumuda, Vahni.
- **Translation**: 

---

### Verse 16 (Ramayan 0.1336)
- **Original**: 1318 The Ramayana Canto XL. The Army Of The East. With practised eye the king reviewed The Vánars' countless multitude, And, joying that his hest was done, Thus spake to Raghu's mighty son: “See, all the Vánar hosts who fear My sovereign might are gathered here. Chiefs strong as Indra's self, who speed Wher'er they list, these armies lead. Fierce and terrific to the view As Daityas or the Dánav659 crew,[372] Famed in all lands for souls afire With lofty thoughts, they never tire, O'er hill and vale they wander free, And islets of the distant sea. And these gathered myriads, all Will serve thee, Ráma, at thy call. Whate'er thy heart advises, say: Thy mandates will the host obey.” Then answered Ráma, as he pressed The Vánar monarch to his breast: “O search for my lost Sítá, strive To find her if she still survive: And in thy wondrous wisdom trace Fierce RávaG to his dwelling-place. And when by toil and search we know Where Sítá lies and where the foe, With thee, dear friend, will I devise Fit means to end the enterprise. 659 Daityas and Dánavas are fiends and enemies of the Gods, like the Titans of Greek mythology.
- **Translation**: 

---

### Verse 17 (Ramayan 0.1337)
- **Original**: Canto XL. The Army Of The East. 1319 Not mine, not LakshmaG's is the power To guide us in the doubtful hour. Thou, sovereign of the Vánars, thou Must be our hope and leader now.” He ceased: at King Sugríva's call Near came a Vánar strong and tall. Huge as a towering mountain, loud As some tremendous thunder cloud, A prince who warlike legions led: To him his sovereign turned and said: “Go, take ten thousand660 of our race Well trained in lore of time and place, And search the eastern region; through Groves, woods, and hills thy way pursue. There seek for Sítá, trace the spot Where RávaG hides, and weary not. Search for the captive in the caves Of mountains, and by woods and waves. To Sarjú,661 Kau [ikí,662 repair, Bhagírath's daughter663 fresh and fair. Search mighty Yamun's664 peak, explore Swift Yamuná's665 delightful shore, 660 I reduce the unwieldy numbers of the original to more modest figures. 661 Sarayú now Sarjú is the river on which Ayodhyá was built. 662 Kau [ikí is a river which flows through Behar, commonly called Kosi. 663 Bhagírath's daughter is Gangá or the Ganges. The legend is told at length in Book I Canto XLIV.The Descent of Gangá. 664 A mountain not identified. 665 The Jumna. The river is personified as the twin sister of Yáma, and hence regarded as the daughter of the Sun.
- **Translation**: 

---

### Verse 18 (Ramayan 0.1338)
- **Original**: 1320 The Ramayana Sarasvati666 and Sindhu's667 tide, And rapidZona's668 pebbly side. Then roam afar by Mahí's669 bed Where Kálamahí's groves are spread. Go where the silken tissue shines, Go to the land of silver mines.670 Visit each isle and mountain steep And city circled by the deep, And distant villages that high About the peaks of Mandar lie. Speed over Yavadwipa's land,671 And see MountZi[ir672 proudly stand Uplifting to the skies his head By Gods and Dánavs visited. Search each ravine and mountain pass, Each tangled thicket deep in grass. Search every cave with utmost care If haply Ráma's queen be there. Then pass beyond the sounding sea Where heavenly beings wander free, 666 The Sarasvatí (corruptly called Sursooty, is supposed to join the Ganges and Jumna at Prayág or Allahabad. It rises in the mountains bounding the north-east part of the province of Delhi, and running in a south-westerly direction becomes lost in the sands of the great desert. 667 The Sindhu is the Indus, the Sanskrits becoming h in Persian and being in this instance dropped by the Greeks. 668 The Sone which rises in the district of Nagpore and falls into the Ganges above Patna. 669 Mahí is a river rising in Malwa and falling into the gulf of Cambay after a westerly course of 280 miles. 670 There is nothing to show what parts of the country the poet intended to denote as silk-producing and silver-producing. 671 Yavadwipa means the island of Yava, wherever that may be. 672 Zi[ir is said to be a mountain ridge projecting from the base of Meru on the south. Wilson'sVishnu PuráGa, ed. Hall, Vol. II. p. 117.
- **Translation**: 

---

### Verse 19 (Ramayan 0.1339)
- **Original**: Canto XL. The Army Of The East. 1321 And Zona's673 waters swift and strong With ruddy billows foam along. Search where his shelving banks descend, Search where the hanging woods extend. Try if the pathless thickets screen The robber and the captive queen. Search where the torrent floods that rend The mountain to the plains descend: Search dark abysses where they rave, Search mountain slope and wood and cave Then on with rapid feet and gain The inlands of the fearful main Where, tortured by the tempest's lash, Against rude rocks the billows dash: An ocean like a sable cloud, Whose margent monstrous serpents crowd: [373] An ocean rising with a roar To beat upon an iron shore. On, onward still! your feet shall tread Shores of the sea whose waves are red, Where spreading wide your eyes shall see The guilt-tormenting cotton tree674 And the wild spot where Garu 675 dwells Which gems adorn and ocean shells, High as Kailása, nobly decked, Wrought by the heavenly architect.676 673 This appears to be some mythical stream and not the well-knownZone. The name means red-coloured. 674 A fabulous thorny rod of the cotton tree used for torturing the wicked in hell. The tree gives its name,Zálmalí, to one of the seven Dwípas, or great divisions of the known continent: and also to a hell where the wicked are tormented with the pickles of the tree. 675 The king of the feathered creation. 676 Vi[vakarmá, the Mulciber of the Indian heaven.
- **Translation**: 

---

### Verse 20 (Ramayan 0.1340)
- **Original**: 1322 The Ramayana Huge giants named Mandehas677 there In each foul shape they love to wear, Numbing the soul with terror's chill, Hang from the summit of the hill. When darts the sun his earliest beam They plunge them in the ocean stream, New vigour from his rays obtain, And hang upon the rocks again. Speed onward still: your steps shall be At length beside the Milky Sea Whose every ripple as it curls Gleams glorious with its wealth of pearls. Amid that sea like pale clouds spread The white Mount Rishabh678 rears his head. About the mountain's glorious waist Woods redolent of bloom are braced. A lake where lotuses unfold Their silver buds with threads of gold, Sudar[an ever bright and fair Where white swans sport, lies gleaming there, The wandering Kinnar's679 dear resort, Where heavenly nymphs and Yakshas680 sport. On! leave the Milky Sea behind: Another flood your search shall find, A waste of waters, wild and drear, That chills each living heart with fear. There see the horse's awful head, 677 “The terrific fiends named Mandehas attempt to devour the sun: for Brahmá denounced this curse upon them, that without the power to perish they should die every day (and revive by night) and therefore a fierce contest occurs (daily) between them and the sun.” W ILSON 'S{FNS VishGu PuráGa. Vol. II. p. 250. 678 Said in theVishGu PuráGa to be a ridge projecting from the base of Meru to the north. 679 Kinnars are centaurs reversed, beings with equine head and human bodies. 680 Yakshas are demi-gods attendant on Kuvera the God of wealth.
- **Translation**: 

---

