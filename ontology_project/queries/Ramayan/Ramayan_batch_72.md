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

### Verse 1 (Ramayan 0.1421)
- **Original**: Canto II. Lanká. 1403 A thousand trees mid flowers that glowed Hung down their fruit's delicious load,803 And in their crests that rocked and swayed Sweet birds delightful music made. And there were pleasant pools whereon The glories of the lotus shone; And gleams of sparkling fountains, stirred By many a joyous water-bird. Around, in lovely gardens grew Blooms sweet of scent and bright of hue, And Lanká, seat of RávaG's sway, Before the wondering Vánar lay: With stately domes and turrets tall, Encircled by a golden wall, And moats whose waters were aglow With lily blossoms bright below: For Sítá's sake defended well With bolt and bar and sentinel, And Rákshases who roamed in bands With ready bows in eager hands. He saw the stately mansions rise Like pale-hued clouds in autumn skies; Where noble streets were broad and bright, And banners waved on every height. Her gates were glorious to behold Rich with the shine of burnished gold: A lovely city planned and decked By heaven's creative architect,804 Fairest of earthly cities meet To be the Gods' celestial seat. The Vánar by the northern gate 803 Through the power that RávaG's stern mortifications had won for him his trees bore flowers and fruit simultaneously. 804 Vi[vakarmá is the architect of the Gods.
- **Translation**: 

---

### Verse 2 (Ramayan 0.1422)
- **Original**: 1404 The Ramayana Thus in his heart began debate “Our mightiest host would strive in vain To take this city on the main: A city that may well defy The chosen warriors of the sky; A city never to be won E'en by the arm of Raghu's son. Here is no hope by guile to win The hostile hearts of those within. 'Twere vain to war, or bribe, or sow Dissension mid the Vánar foe. But now my search must I pursue Until the Maithil queen I view: And, when I find the captive dame, Make victory mine only aim. But, if I wear my present shape, How shall I enter and escape The Rákshas troops, their guards and spies, And sleepless watch of cruel eyes? The fiends of giant race who hold This mighty town are strong and bold; And I must labour to elude The fiercely watchful multitude. I in a shape to mock their sight Must steal within the town by night, Blind with my art the demons' eyes, And thus achieve my enterprise. How may I see, myself unseen Of the fierce king, the captive queen, And meet her in some lonely place, With none beside her, face to face?” When the bright sun had left the skies The Vánar dwarfed his mighty size,[398]
- **Translation**: 

---

### Verse 3 (Ramayan 0.1423)
- **Original**: Canto III. The Guardian Goddess. 1405 And, in the straitest bounds restrained, The bigness of a cat retained.805 Then, when the moon's soft light was spread, Within the city's walls he sped. Canto III. The Guardian Goddess. There from the circling rampart's height He gazed upon the wondrous sight; Broad gates with burnished gold displayed, And courts with turkises inlaid; With gleaming silver, gems, and rows Of crystal stairs and porticoes. In semblance of a Rákshas dame The city's guardian Goddess came,— For she with glances sure and keen The entrance of a foe had seen,— And thus with fury in her eye Addressed him with an angry cry: “Who art thou? what has led thee, say, Within these walls to find thy way? Thou mayst not enter here in spite Of RávaG and his warriors' might.” “And who art thou?” the Vánar cried, By form and frown unterrified, “Why hast thou met me by the gate, And chid me thus infuriate?” 805 So in Paradise Lost Satan when he has stealthily entered the garden of Eden assumes the form of a cormorant.
- **Translation**: 

---

### Verse 4 (Ramayan 0.1424)
- **Original**: 1406 The Ramayana He ceased: and Lanká made reply: “The guardian of the town am I, Who watch for ever to fulfil My lord the Rákshas monarch's will. But thou shalt fall this hour, and deep Shall be thy never-ending sleep.” Again he spake:“In spite of thee This golden city will I see. Her gates and towers, and all the pride Of street and square from side to side, And freely wander where I please Amid her groves of flowering trees; On all her beauties sate mine eye. Then, as I came, will homeward hie.” Swift with an angry roar she smote With her huge hand the Vánar's throat. The smitten Vánar, rage-impelled, With fist upraised the monster felled: But quick repented, stirred with shame And pity for a vanquished dame, When with her senses troubled, weak With terror, thus she strove to speak: “O spare me thou whose arm is strong: O spare me, and forgive the wrong. The brave that law will ne'er transgress That spares a woman's helplessness. Hear, best of Vánars, brave and bold, What Brahmá's self of yore foretold; “Beware,” he said,“the fatal hour When thou shalt own a Vánar's power. Then is the giants' day of fear, For terror and defeat are near.”
- **Translation**: 

---

### Verse 5 (Ramayan 0.1425)
- **Original**: Canto IV. Within The City. 1407 Now, Vánar chief, o'ercome by thee, I own the truth of heaven's decree. For Sítá's sake will ruin fall On RávaG, and his town, and all.” Canto IV. Within The City. The guardian goddess thus subdued, The Vánar chief his way pursued, And reached the broad imperial street Where fresh-blown flowers were bright and sweet. The city seemed a fairer sky Where cloud-like houses rose on high, Whence the soft sound of tabors came Through many a latticed window frame, And ever and anon rang out The merry laugh and joyous shout. From house to house the Vánar went And marked each varied ornament, Where leaves and blossoms deftly strung About the crystal columns hung. Then soft and full and sweet and clear The song of women charmed his ear, And, blending with their dulcet tones, Their anklets' chime and tinkling zones. He heard the Rákshas minstrel sing The praises of their matchless king; And softly through the evening air Came murmurings of text and prayer. Here moved a priest with tonsured head, And there an eager envoy sped,
- **Translation**: 

---

### Verse 6 (Ramayan 0.1426)
- **Original**: 1408 The Ramayana Mid crowds with hair in matted twine Clothed in the skins of deer and kine,— Whose only arms, which none might blame, Were blades of grass and holy flame806 There savage warriors roamed in bands With clubs and maces in their hands, Some dwarfish forms, some huge of size, With single ears and single eyes. Some shone in glittering mail arrayed With bow and mace and flashing blade; Fiends of all shapes and every hue, Some fierce and foul, some fair to view.[399] He saw the grisly legions wait In strictest watch at RávaG's gate, Whose palace on the mountain crest Rose proudly towering o'er the rest, Fenced with high ramparts from the foe, And lotus-covered moats below. But Hanumán, unhindered, found Quick passage through the guarded bound, Mid elephants of noblest breed, And gilded car and neighing steed. [I omit Canto V. which corresponds to chapter XI. in Gorresio's edition. That scholar justly observes:“The eleventh chapter, Description of Evening, is certainly the work of the Rhapsodists and an interpolation of later date. The chapter might be omitted without any injury to the action of the poem, and besides the me- tre, style, conceits and images differ from the general tenour of the poem; and that continual repetition of the same sounds at the end of each hemistich which is not exactly rime, but assonance, 806 Priests who fought only with the weapons of religion, the sacred grass used like the verbena of the Romans at sacred rites and the consecrated fire to consume the offering of ghee.
- **Translation**: 

---

### Verse 7 (Ramayan 0.1427)
- **Original**: Canto VI. The Court. 1409 reveals the artificial labour of a more recent age.” The following sample will probably be enough. Fair shone the moon, as if to lend His cheering light to guide a friend, And, circled by the starry host, Looked down upon the wild sea-coast. The Vánar cheiftain raised his eyes, And saw him sailing through the skies Like a bright swan who joys to take His pastime on a silver lake; Fair moon that calms the mourner's pain. Heaves up the waters of the main, And o'er the life beneath him throws A tender light of soft repose, The charm that clings to Mandar's hill, Gleams in the sea when winds are still, And decks the lilly's opening flower, Showed in that moon her sweetest power. I am unable to show the difference of style in a translation.] Canto VI. The Court. The palace gates were guarded well By many a Rákshas sentinel, And far within, concealed from view, Were dames and female retinue For charm of form and face renowned; Whose tinkling armlets made a sound, Clashed by the wearers in their glee, Like music of a distant sea.
- **Translation**: 

---

### Verse 8 (Ramayan 0.1428)
- **Original**: 1410 The Ramayana The hall beyond the palace gate, Rich with each badge of royal state, Where lines of noble courtiers stood, Showed like a lion-guarded wood. There the wild music rose and fell Of drum and tabor and of shell, Through chambers at each holy tide By solemn worship sanctified. Through grove and garden, undismayed, From house to house the Vánar strayed, And still his wondering glances bent On terrace, dome, and battlement: Then with a light and rapid tread Prahasta's807 home he visited, And Kumbhakar Ga's808 courtyard where A cloudy pile rose high in air; And, wandering o'er the hill, explored The garden of each Rákshas lord. Each court and grove he wandered through, Then nigh to RávaG's palace drew. She-demons watched it foul of face, Each armed with sword and spear and mace, And warrior fiends of every hue, A strange and fearful retinue. There elephants in many a row, The terror of the stricken foe. Huge Airávat,809 deftly trained In battle-fields, stood ready chained. Fair litters on the ground were set Adorned with gems and golden net. Gay bloomy creepers clothed the walls; 807 One of the Rákshas lords. 808 The brother RávaG. 809 Indra's elephant.
- **Translation**: 

---

### Verse 9 (Ramayan 0.1429)
- **Original**: Canto VII. Rávan's Palace. 1411 Green bowers were there and picture halls, And chambers made for soft delight. Broad banners waved on every height. And from the roof like Mandar's hill The peacock's cry came loud and shrill.810 Canto VII. Rávan's Palace. He passed within the walls and gazed On gems and gold that round him blazed, And many a latticed window bright With turkis and with lazulite. [400] Through porch and ante-rooms he passed Each richer, fairer than the last; And spacious halls where lances lay, And bows and shells, in fair array: A glorious house that matched in show All Paradise displayed below. Upon the polished floor were spread Fresh buds and blossoms white and red, And women shone, a lovely crowd, As lightning flashes through a cloud: A palace splendid as the sky Which moon and planets glorify: Like earth whose towering hills unfold Their zones and streaks of glittering gold; 810 RávaG's palace appears to have occupied the whole extent of ground, and to have contained within its outer walls the mansions of all the great Rákshas chiefs. RávaG's own dwelling seems to have been situated within the enchanted chariot Pushpak: but the description is involved and confused, and it is difficult to say whether the chariot was inside the palace or the palace inside the chariot.
- **Translation**: 

---

### Verse 10 (Ramayan 0.1430)
- **Original**: 1412 The Ramayana Where waving on the mountain brows The tall trees bend their laden boughs, And every bough and tender spray With a bright load of bloom is gay, And every flower the breeze has bent Fills all the region with its scent. Near the tall palace pale of hue Shone lovely lakes where lilies blew, And lotuses with flower and bud Gleamed on the bosom of the flood. There shone with gems that flashed afar The marvel of the Flower-named811 car, Mid wondrous dwellings still confessed Supreme and nobler than the rest. Thereon with wondrous art designed Were turkis birds of varied kind. And many a sculptured serpent rolled His twisted coil in burnished gold. And steeds were there of noblest form With flying feet as fleet as storm: And elephants with deftest skill Stood sculptured by a silver rill, Each bearing on his trunk a wreath Of lilies from the flood beneath. There Lakshmí,812 beauty's heavenly queen, Wrought by the artist's skill, was seen Beside a flower-clad pool to stand Holding a lotus in her hand. 811 Pushpak from pushpa a flower. The car has been mentioned before in RávaG's expedition to carry off Sítá, Book III, Canto XXXV. 812 Lakshmí is the wife of VishGu and the Goddess of Beauty and Felicity. She rose, like Aphrodite, from the foam of the sea. For an account of her birth and beauty, see Book I, Canto XLV.
- **Translation**: 

---

### Verse 11 (Ramayan 0.1431)
- **Original**: Canto VIII. The Enchanted Car. 1413 Canto VIII. The Enchanted Car. There gleamed the car with wealth untold Of precious gems and burnished gold; Nor could the Wind-God's son withdraw His rapt gaze from the sight he saw, By Vi[vakarmá's813 self proclaimed The noblest work his hand had framed. Uplifted in the air it glowed Bright as the sun's diurnal road. The eye might scan the wondrous frame And vainly seek one spot to blame, So fine was every part and fair With gems inlaid with lavish care. No precious stones so rich adorn The cars wherein the Gods are borne, Prize of the all-resistless might That sprang from pain and penance rite,814 Obedient to the master's will It moved o'er wood and towering hill, A glorious marvel well designed By Vi[vakarmá's artist mind, Adorned with every fair device That decks the cars of Paradise. Swift moving as the master chose It flew through air or sank or rose,815 And in its fleetness left behind The fury of the rushing wind: 813 Vi[vakarmá is the architect of the Gods, the Hephaestos or Mulciber of the Indian heaven. 814 RávaG in the resistless power which his long austerities had endowed him with, had conquered his brother Kuvera the God of Gold and taken from him his greatest treasure this enchanted car. 815 Like Milton's heavenly car,“Itself instinct with spirit.”
- **Translation**: 

---

### Verse 12 (Ramayan 0.1432)
- **Original**: 1414 The Ramayana Meet mansion for the good and great, The holy, wise, and fortunate. Throughout the chariot's vast extent Were chambers wide and excellent, All pure and lovely to the eyes As moonlight shed from cloudless skies. Fierce goblins, rovers of the night Who cleft the clouds with swiftest flight In countless hosts that chariot drew, With earrings clashing as they flew. Canto IX. The Ladies' Bower. Where stately mansions rose around, A palace fairer still he found, Whose royal height and splendour showed Where RávaG's self, the king, abode. A chosen band with bow and sword Guarded the palace of their lord, Where Ráksha's dames of noble race And many a princess fair of face Whom Ráva G's arm had torn away From vanquished kings in slumber lay.[401] There jewelled arches high o'erhead An ever-changing lustre shed From ruby, pearl, and every gem On golden pillars under them. Delicious came the tempered air That breathed a heavenly summer there, Stealing through bloomy trees that bore Each pleasant fruit in endless store.
- **Translation**: 

---

### Verse 13 (Ramayan 0.1433)
- **Original**: Canto IX. The Ladies' Bower. 1415 No check was there from jealous guard, No door was fast, no portal barred; Only a sweet air breathed to meet The stranger, as a host should greet A wanderer of his kith and kin And woo his weary steps within. He stood within a spacious hall With fretted roof and painted wall, The giant RávaG's boast and pride, Loved even as a lovely bride. 'Twere long to tell each marvel there, The crystal floor, the jewelled stair, The gold, the silver, and the shine Of chrysolite and almandine. There breathed the fairest blooms of spring; There flashed the proud swan's silver wing, The splendour of whose feathers broke Through fragrant wreaths of aloe smoke. “'Tis Indra's heaven,” the Vánar cried, Gazing in joy from side to side; “The home of all the Gods is this, The mansion of eternal bliss.” There were the softest carpets spread, Delightful to the sight and tread, Where many a lovely woman lay O'ercome by sleep, fatigued with play. The wine no longer cheered the feast, The sound of revelry had ceased. The tinkling feet no longer stirred, No chiming of a zone was heard. So when each bird has sought her nest, And swans are mute and wild bees rest, Sleep the fair lilies on the lake Till the sun's kiss shall bid them wake.
- **Translation**: 

---

### Verse 14 (Ramayan 0.1434)
- **Original**: 1416 The Ramayana Like the calm field of winter's sky Which stars unnumbered glorify, So shone and glowed the sumptuous room With living stars that chased the gloom. “These are the stars,” the chieftain cried, “In autumn nights that earth-ward glide, In brighter forms to reappear And shine in matchless lustre here.” With wondering eyes a while he viewed Each graceful form and attitude. One lady's head was backward thrown, Bare was her arm and loose her zone. The garland that her brow had graced Hung closely round another's waist. Here gleamed two little feet all bare Of anklets that had sparkled there, Here lay a queenly dame at rest In all her glorious garments dressed. There slept another whose small hand Had loosened every tie and band, In careless grace another lay With gems and jewels cast away, Like a young creeper when the tread Of the wild elephant has spread Confusion and destruction round, And cast it flowerless to the ground. Here lay a slumberer still as death, Save only that her balmy breath Raised ever and anon the lace That floated o'er her sleeping face. There, sunk in sleep, an amorous maid Her sweet head on a mirror laid, Like a fair lily bending till Her petals rest upon the rill.
- **Translation**: 

---

### Verse 15 (Ramayan 0.1435)
- **Original**: Canto X. Rávan Asleep. 1417 Another black-eyed damsel pressed Her lute upon her heaving breast, As though her loving arms were twined Round him for whom her bosom pined. Another pretty sleeper round A silver vase her arms had wound, That seemed, so fresh and fair and young A wreath of flowers that o'er it hung. In sweet disorder lay a throng Weary of dance and play and song, Where heedless girls had sunk to rest One pillowed on another's breast, Her tender cheek half seen beneath Bed roses of the falling wreath, The while her long soft hair concealed The beauties that her friend revealed. With limbs at random interlaced Round arm and leg and throat and waist, That wreath of women lay asleep Like blossoms in a careless heap. Canto X. Rávan Asleep. Apart a dais of crystal rose With couches spread for soft repose, Adorned with gold and gems of price Meet for the halls of Paradise. A canopy was o'er them spread Pale as the light the moon beams shed,
- **Translation**: 

---

### Verse 16 (Ramayan 0.1436)
- **Original**: 1418 The Ramayana And female figures,816 deftly planned, The faces of the sleepers fanned, There on a splendid couch, asleep On softest skins of deer and sheep. Dark as a cloud that dims the day The monarch of the giants lay, Perfumed with sandal's precious scent And gay with golden ornament.[402] His fiery eyes in slumber closed, In glittering robes the king reposed Like Mandar's mighty hill asleep With flowery trees that clothe his steep. Near and more near the Vánar The monarch of the fiends to view, And saw the giant stretched supine Fatigued with play and drunk with wine. While, shaking all the monstrous frame, His breath like hissing serpents' came. With gold and glittering bracelets gay His mighty arms extended lay Huge as the towering shafts that bear The flag of Indra high in air. Scars by Airávat's tusk impressed Showed red upon his shaggy breast. And on his shoulders were displayed The dints the thunder-bolt had made.817 The spouses of the giant king Around their lord were slumbering, And, gay with sparkling earrings, shone 816 Women, says Válmíki. But the Commentator says that automatic figures only are meant. Women would have seen Hanumán and given the alarm. 817 RávaG had fought against Indra and the Gods, and his body was still scarred by the wounds inflicted by the tusks of Indra's elephant and by the fiery bolts of the Thunderer.
- **Translation**: 

---

### Verse 17 (Ramayan 0.1437)
- **Original**: Canto XI. The Banquet Hall. 1419 Fair as the moon to look upon. There by her husband's side was seen Mandodarí the favourite queen, The beauty of whose youthful face Beamed a soft glory through the place. The Vánar marked the dame more fair Than all the royal ladies there, And thought,“These rarest beauties speak The matchless dame I come to seek. Peerless in grace and splendour, she The Maithil queen must surely be.” Canto XI. The Banquet Hall. But soon the baseless thought was spurned And longing hope again returned: “No: Ráma's wife is none of these, No careless dame that lives at ease. Her widowed heart has ceased to care For dress and sleep and dainty fare. She near a lover ne'er would lie Though Indra wooed her from the sky. Her own, her only lord, whom none Can match in heaven, is Raghu's son.”
- **Translation**: 

---

### Verse 18 (Ramayan 0.1438)
- **Original**: 1420 The Ramayana Then to the banquet hall intent On strictest search his steps he bent. He passed within the door, and found Fair women sleeping on the ground, Where wearied with the song, perchance, The merry game, the wanton dance, Each girl with wine and sleep oppressed Had sunk her drooping head to rest. That spacious hall from side to side With noblest fare was well supplied, There quarters of the boar, and here Roast of the buffalo and deer, There on gold plate, untouched as yet The peacock and the hen were set. There deftly mixed with salt and curd Was meat of many a beast and bird, Of kid and porcupine and hare, And dainties of the sea and air. There wrought of gold, ablaze with shine Of precious stones, were cups of wine. Through court and bower and banquet hall The Vánar passed and viewed them all; From end to end, in every spot, For Sítá searched, but found her not. Canto XII. The Search Renewed. Again the Vánar chief began Each chamber, bower, and hall to scan. In vain: he found not her he sought, And pondered thus in bitter thought:
- **Translation**: 

---

### Verse 19 (Ramayan 0.1439)
- **Original**: Canto XII. The Search Renewed. 1421 “Ah me the Maithil queen is slain: She, ever true and free from stain, The fiend's entreaty has denied, And by his cruel hand has died. Or has she sunk, by terror killed, When first she saw the palace filled With female monsters evil miened Who wait upon the robber fiend? No battle fought, no might displayed, In vain this anxious search is made; Nor shall my steps, made slow by shame, Because I failed to find the dame, Back to our lord the king be bent, For he is swift to punishment. In every bower my feet have been, The dames of RávaG have I seen; But Ráma's spouse I seek in vain, And all my toil is fruitless pain. How shall I meet the Vánar band I left upon the ocean strand? How, when they bid me speak, proclaim These tidings of defeat and shame? How shall I look on Angad's eye? What words will Jámbaván reply? Yet dauntless hearts will never fail To win success though foes assail, And I this sorrow will subdue And search the palace through and through, Exploring with my cautious tread Each spot as yet unvisited.” Again he turned him to explore Each chamber, hall, and corridor, And arbour bright with scented bloom,
- **Translation**: 

---

### Verse 20 (Ramayan 0.1440)
- **Original**: 1422 The Ramayana And lodge and cell and picture-room.[403] With eager eye and noiseless feet He passed through many a cool retreat Where women lay in slumber drowned; But Sítá still was nowhere found. Canto XIII. Despair And Hope. Then rapid as the lightning's flame From RávaG's halls the Vánar came. Each lingering hope was cold and dead, And thus within his heart he said: “Alas, my fruitless search is done: Long have I toiled for Raghu's son; And yet with all my care have seen No traces of the ravished queen. It may be, while the giant through The lone air with his captive flew, The Maithil lady, tender-souled, Slipped struggling from the robber's hold, And the wild sea is rolling now O'er Sítá of the beauteous brow. Or did she perish of alarm When circled by the monster's arm? Or crushed, unable to withstand The pressure of that monstrous hand? Or when she spurned his suit with scorn, Her tender limbs were rent and torn. And she, her virtue unsubdued, Was slaughtered for the giant's food. Shall I to Raghu's son relate
- **Translation**: 

---

