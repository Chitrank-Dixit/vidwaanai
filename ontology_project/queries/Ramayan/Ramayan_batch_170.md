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

### Verse 1 (Ramayana 0.1426)
- **Original**: 1408 The Ramayana Mid crowds with hair in matted twine Clothed in the skins of deer and kine,— Whose only arms, which none might blame, Were blades of grass and holy flame806 There savage warriors roamed in bands With clubs and maces in their hands, Some dwarfish forms, some huge of size, With single ears and single eyes. Some shone in glittering mail arrayed With bow and mace and flashing blade; Fiends of all shapes and every hue, Some fierce and foul, some fair to view.[399] He saw the grisly legions wait In strictest watch at RávaG's gate, Whose palace on the mountain crest Rose proudly towering o'er the rest, Fenced with high ramparts from the foe, And lotus-covered moats below. But Hanumán, unhindered, found Quick passage through the guarded bound, Mid elephants of noblest breed, And gilded car and neighing steed. [I omit Canto V. which corresponds to chapter XI. in Gorresio's edition. That scholar justly observes:“The eleventh chapter, Description of Evening, is certainly the work of the Rhapsodists and an interpolation of later date. The chapter might be omitted without any injury to the action of the poem, and besides the me- tre, style, conceits and images differ from the general tenour of the poem; and that continual repetition of the same sounds at the end of each hemistich which is not exactly rime, but assonance, 806 Priests who fought only with the weapons of religion, the sacred grass used like the verbena of the Romans at sacred rites and the consecrated fire to consume the offering of ghee.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1427)
- **Original**: Canto VI. The Court. 1409 reveals the artificial labour of a more recent age.” The following sample will probably be enough. Fair shone the moon, as if to lend His cheering light to guide a friend, And, circled by the starry host, Looked down upon the wild sea-coast. The Vánar cheiftain raised his eyes, And saw him sailing through the skies Like a bright swan who joys to take His pastime on a silver lake; Fair moon that calms the mourner's pain. Heaves up the waters of the main, And o'er the life beneath him throws A tender light of soft repose, The charm that clings to Mandar's hill, Gleams in the sea when winds are still, And decks the lilly's opening flower, Showed in that moon her sweetest power. I am unable to show the difference of style in a translation.] Canto VI. The Court. The palace gates were guarded well By many a Rákshas sentinel, And far within, concealed from view, Were dames and female retinue For charm of form and face renowned; Whose tinkling armlets made a sound, Clashed by the wearers in their glee, Like music of a distant sea.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1428)
- **Original**: 1410 The Ramayana The hall beyond the palace gate, Rich with each badge of royal state, Where lines of noble courtiers stood, Showed like a lion-guarded wood. There the wild music rose and fell Of drum and tabor and of shell, Through chambers at each holy tide By solemn worship sanctified. Through grove and garden, undismayed, From house to house the Vánar strayed, And still his wondering glances bent On terrace, dome, and battlement: Then with a light and rapid tread Prahasta's807 home he visited, And Kumbhakar Ga's808 courtyard where A cloudy pile rose high in air; And, wandering o'er the hill, explored The garden of each Rákshas lord. Each court and grove he wandered through, Then nigh to RávaG's palace drew. She-demons watched it foul of face, Each armed with sword and spear and mace, And warrior fiends of every hue, A strange and fearful retinue. There elephants in many a row, The terror of the stricken foe. Huge Airávat,809 deftly trained In battle-fields, stood ready chained. Fair litters on the ground were set Adorned with gems and golden net. Gay bloomy creepers clothed the walls; 807 One of the Rákshas lords. 808 The brother RávaG. 809 Indra's elephant.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1429)
- **Original**: Canto VII. Rávan's Palace. 1411 Green bowers were there and picture halls, And chambers made for soft delight. Broad banners waved on every height. And from the roof like Mandar's hill The peacock's cry came loud and shrill.810 Canto VII. Rávan's Palace. He passed within the walls and gazed On gems and gold that round him blazed, And many a latticed window bright With turkis and with lazulite. [400] Through porch and ante-rooms he passed Each richer, fairer than the last; And spacious halls where lances lay, And bows and shells, in fair array: A glorious house that matched in show All Paradise displayed below. Upon the polished floor were spread Fresh buds and blossoms white and red, And women shone, a lovely crowd, As lightning flashes through a cloud: A palace splendid as the sky Which moon and planets glorify: Like earth whose towering hills unfold Their zones and streaks of glittering gold; 810 RávaG's palace appears to have occupied the whole extent of ground, and to have contained within its outer walls the mansions of all the great Rákshas chiefs. RávaG's own dwelling seems to have been situated within the enchanted chariot Pushpak: but the description is involved and confused, and it is difficult to say whether the chariot was inside the palace or the palace inside the chariot.
- **Translation**: 

---

### Verse 5 (Ramayana 0.1430)
- **Original**: 1412 The Ramayana Where waving on the mountain brows The tall trees bend their laden boughs, And every bough and tender spray With a bright load of bloom is gay, And every flower the breeze has bent Fills all the region with its scent. Near the tall palace pale of hue Shone lovely lakes where lilies blew, And lotuses with flower and bud Gleamed on the bosom of the flood. There shone with gems that flashed afar The marvel of the Flower-named811 car, Mid wondrous dwellings still confessed Supreme and nobler than the rest. Thereon with wondrous art designed Were turkis birds of varied kind. And many a sculptured serpent rolled His twisted coil in burnished gold. And steeds were there of noblest form With flying feet as fleet as storm: And elephants with deftest skill Stood sculptured by a silver rill, Each bearing on his trunk a wreath Of lilies from the flood beneath. There Lakshmí,812 beauty's heavenly queen, Wrought by the artist's skill, was seen Beside a flower-clad pool to stand Holding a lotus in her hand. 811 Pushpak from pushpa a flower. The car has been mentioned before in RávaG's expedition to carry off Sítá, Book III, Canto XXXV. 812 Lakshmí is the wife of VishGu and the Goddess of Beauty and Felicity. She rose, like Aphrodite, from the foam of the sea. For an account of her birth and beauty, see Book I, Canto XLV.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1431)
- **Original**: Canto VIII. The Enchanted Car. 1413 Canto VIII. The Enchanted Car. There gleamed the car with wealth untold Of precious gems and burnished gold; Nor could the Wind-God's son withdraw His rapt gaze from the sight he saw, By Vi[vakarmá's813 self proclaimed The noblest work his hand had framed. Uplifted in the air it glowed Bright as the sun's diurnal road. The eye might scan the wondrous frame And vainly seek one spot to blame, So fine was every part and fair With gems inlaid with lavish care. No precious stones so rich adorn The cars wherein the Gods are borne, Prize of the all-resistless might That sprang from pain and penance rite,814 Obedient to the master's will It moved o'er wood and towering hill, A glorious marvel well designed By Vi[vakarmá's artist mind, Adorned with every fair device That decks the cars of Paradise. Swift moving as the master chose It flew through air or sank or rose,815 And in its fleetness left behind The fury of the rushing wind: 813 Vi[vakarmá is the architect of the Gods, the Hephaestos or Mulciber of the Indian heaven. 814 RávaG in the resistless power which his long austerities had endowed him with, had conquered his brother Kuvera the God of Gold and taken from him his greatest treasure this enchanted car. 815 Like Milton's heavenly car,“Itself instinct with spirit.”
- **Translation**: 

---

### Verse 7 (Ramayana 0.1432)
- **Original**: 1414 The Ramayana Meet mansion for the good and great, The holy, wise, and fortunate. Throughout the chariot's vast extent Were chambers wide and excellent, All pure and lovely to the eyes As moonlight shed from cloudless skies. Fierce goblins, rovers of the night Who cleft the clouds with swiftest flight In countless hosts that chariot drew, With earrings clashing as they flew. Canto IX. The Ladies' Bower. Where stately mansions rose around, A palace fairer still he found, Whose royal height and splendour showed Where RávaG's self, the king, abode. A chosen band with bow and sword Guarded the palace of their lord, Where Ráksha's dames of noble race And many a princess fair of face Whom Ráva G's arm had torn away From vanquished kings in slumber lay.[401] There jewelled arches high o'erhead An ever-changing lustre shed From ruby, pearl, and every gem On golden pillars under them. Delicious came the tempered air That breathed a heavenly summer there, Stealing through bloomy trees that bore Each pleasant fruit in endless store.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1433)
- **Original**: Canto IX. The Ladies' Bower. 1415 No check was there from jealous guard, No door was fast, no portal barred; Only a sweet air breathed to meet The stranger, as a host should greet A wanderer of his kith and kin And woo his weary steps within. He stood within a spacious hall With fretted roof and painted wall, The giant RávaG's boast and pride, Loved even as a lovely bride. 'Twere long to tell each marvel there, The crystal floor, the jewelled stair, The gold, the silver, and the shine Of chrysolite and almandine. There breathed the fairest blooms of spring; There flashed the proud swan's silver wing, The splendour of whose feathers broke Through fragrant wreaths of aloe smoke. “'Tis Indra's heaven,” the Vánar cried, Gazing in joy from side to side; “The home of all the Gods is this, The mansion of eternal bliss.” There were the softest carpets spread, Delightful to the sight and tread, Where many a lovely woman lay O'ercome by sleep, fatigued with play. The wine no longer cheered the feast, The sound of revelry had ceased. The tinkling feet no longer stirred, No chiming of a zone was heard. So when each bird has sought her nest, And swans are mute and wild bees rest, Sleep the fair lilies on the lake Till the sun's kiss shall bid them wake.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1434)
- **Original**: 1416 The Ramayana Like the calm field of winter's sky Which stars unnumbered glorify, So shone and glowed the sumptuous room With living stars that chased the gloom. “These are the stars,” the chieftain cried, “In autumn nights that earth-ward glide, In brighter forms to reappear And shine in matchless lustre here.” With wondering eyes a while he viewed Each graceful form and attitude. One lady's head was backward thrown, Bare was her arm and loose her zone. The garland that her brow had graced Hung closely round another's waist. Here gleamed two little feet all bare Of anklets that had sparkled there, Here lay a queenly dame at rest In all her glorious garments dressed. There slept another whose small hand Had loosened every tie and band, In careless grace another lay With gems and jewels cast away, Like a young creeper when the tread Of the wild elephant has spread Confusion and destruction round, And cast it flowerless to the ground. Here lay a slumberer still as death, Save only that her balmy breath Raised ever and anon the lace That floated o'er her sleeping face. There, sunk in sleep, an amorous maid Her sweet head on a mirror laid, Like a fair lily bending till Her petals rest upon the rill.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1435)
- **Original**: Canto X. Rávan Asleep. 1417 Another black-eyed damsel pressed Her lute upon her heaving breast, As though her loving arms were twined Round him for whom her bosom pined. Another pretty sleeper round A silver vase her arms had wound, That seemed, so fresh and fair and young A wreath of flowers that o'er it hung. In sweet disorder lay a throng Weary of dance and play and song, Where heedless girls had sunk to rest One pillowed on another's breast, Her tender cheek half seen beneath Bed roses of the falling wreath, The while her long soft hair concealed The beauties that her friend revealed. With limbs at random interlaced Round arm and leg and throat and waist, That wreath of women lay asleep Like blossoms in a careless heap. Canto X. Rávan Asleep. Apart a dais of crystal rose With couches spread for soft repose, Adorned with gold and gems of price Meet for the halls of Paradise. A canopy was o'er them spread Pale as the light the moon beams shed,
- **Translation**: 

---

### Verse 11 (Ramayana 0.1436)
- **Original**: 1418 The Ramayana And female figures,816 deftly planned, The faces of the sleepers fanned, There on a splendid couch, asleep On softest skins of deer and sheep. Dark as a cloud that dims the day The monarch of the giants lay, Perfumed with sandal's precious scent And gay with golden ornament.[402] His fiery eyes in slumber closed, In glittering robes the king reposed Like Mandar's mighty hill asleep With flowery trees that clothe his steep. Near and more near the Vánar The monarch of the fiends to view, And saw the giant stretched supine Fatigued with play and drunk with wine. While, shaking all the monstrous frame, His breath like hissing serpents' came. With gold and glittering bracelets gay His mighty arms extended lay Huge as the towering shafts that bear The flag of Indra high in air. Scars by Airávat's tusk impressed Showed red upon his shaggy breast. And on his shoulders were displayed The dints the thunder-bolt had made.817 The spouses of the giant king Around their lord were slumbering, And, gay with sparkling earrings, shone 816 Women, says Válmíki. But the Commentator says that automatic figures only are meant. Women would have seen Hanumán and given the alarm. 817 RávaG had fought against Indra and the Gods, and his body was still scarred by the wounds inflicted by the tusks of Indra's elephant and by the fiery bolts of the Thunderer.
- **Translation**: 

---

### Verse 12 (Ramayana 0.1437)
- **Original**: Canto XI. The Banquet Hall. 1419 Fair as the moon to look upon. There by her husband's side was seen Mandodarí the favourite queen, The beauty of whose youthful face Beamed a soft glory through the place. The Vánar marked the dame more fair Than all the royal ladies there, And thought,“These rarest beauties speak The matchless dame I come to seek. Peerless in grace and splendour, she The Maithil queen must surely be.” Canto XI. The Banquet Hall. But soon the baseless thought was spurned And longing hope again returned: “No: Ráma's wife is none of these, No careless dame that lives at ease. Her widowed heart has ceased to care For dress and sleep and dainty fare. She near a lover ne'er would lie Though Indra wooed her from the sky. Her own, her only lord, whom none Can match in heaven, is Raghu's son.”
- **Translation**: 

---

### Verse 13 (Ramayana 0.1438)
- **Original**: 1420 The Ramayana Then to the banquet hall intent On strictest search his steps he bent. He passed within the door, and found Fair women sleeping on the ground, Where wearied with the song, perchance, The merry game, the wanton dance, Each girl with wine and sleep oppressed Had sunk her drooping head to rest. That spacious hall from side to side With noblest fare was well supplied, There quarters of the boar, and here Roast of the buffalo and deer, There on gold plate, untouched as yet The peacock and the hen were set. There deftly mixed with salt and curd Was meat of many a beast and bird, Of kid and porcupine and hare, And dainties of the sea and air. There wrought of gold, ablaze with shine Of precious stones, were cups of wine. Through court and bower and banquet hall The Vánar passed and viewed them all; From end to end, in every spot, For Sítá searched, but found her not. Canto XII. The Search Renewed. Again the Vánar chief began Each chamber, bower, and hall to scan. In vain: he found not her he sought, And pondered thus in bitter thought:
- **Translation**: 

---

### Verse 14 (Ramayana 0.1439)
- **Original**: Canto XII. The Search Renewed. 1421 “Ah me the Maithil queen is slain: She, ever true and free from stain, The fiend's entreaty has denied, And by his cruel hand has died. Or has she sunk, by terror killed, When first she saw the palace filled With female monsters evil miened Who wait upon the robber fiend? No battle fought, no might displayed, In vain this anxious search is made; Nor shall my steps, made slow by shame, Because I failed to find the dame, Back to our lord the king be bent, For he is swift to punishment. In every bower my feet have been, The dames of RávaG have I seen; But Ráma's spouse I seek in vain, And all my toil is fruitless pain. How shall I meet the Vánar band I left upon the ocean strand? How, when they bid me speak, proclaim These tidings of defeat and shame? How shall I look on Angad's eye? What words will Jámbaván reply? Yet dauntless hearts will never fail To win success though foes assail, And I this sorrow will subdue And search the palace through and through, Exploring with my cautious tread Each spot as yet unvisited.” Again he turned him to explore Each chamber, hall, and corridor, And arbour bright with scented bloom,
- **Translation**: 

---

### Verse 15 (Ramayana 0.1440)
- **Original**: 1422 The Ramayana And lodge and cell and picture-room.[403] With eager eye and noiseless feet He passed through many a cool retreat Where women lay in slumber drowned; But Sítá still was nowhere found. Canto XIII. Despair And Hope. Then rapid as the lightning's flame From RávaG's halls the Vánar came. Each lingering hope was cold and dead, And thus within his heart he said: “Alas, my fruitless search is done: Long have I toiled for Raghu's son; And yet with all my care have seen No traces of the ravished queen. It may be, while the giant through The lone air with his captive flew, The Maithil lady, tender-souled, Slipped struggling from the robber's hold, And the wild sea is rolling now O'er Sítá of the beauteous brow. Or did she perish of alarm When circled by the monster's arm? Or crushed, unable to withstand The pressure of that monstrous hand? Or when she spurned his suit with scorn, Her tender limbs were rent and torn. And she, her virtue unsubdued, Was slaughtered for the giant's food. Shall I to Raghu's son relate
- **Translation**: 

---

### Verse 16 (Ramayana 0.1441)
- **Original**: Canto XIII. Despair And Hope. 1423 His well-beloved consort's fate, My crime the same if I reveal The mournful story or conceal? If with no happier tale to tell I seek our mountain citadel, How shall I face our lord the king, And meet his angry questioning? How shall I greet my friends, and brook The muttered taunt, the scornful look? How to the son of Raghu go And kill him with my tale of woe? For sure the mournful tale I bear Will strike him dead with wild despair. And Lakshma G ever fond and true, Will, undivided, perish too. Bharat will learn his brother's fate, And die of grief disconsolate, And sadZatrughna with a cry Of anguish on his corpse will die. Our king Sugríva, ever found True to each bond in honour bound, Will mourn the pledge he vainly gave, And die with him he could not save. Then Rumá his devoted wife For her dead lord will leave her life, And Tárá, widowed and forlorn, Will die in anguish, sorrow-worn. On Angad too the blow will fall Killing the hope and joy of all. The ruin of their prince and king The Vánars' souls with woe will wring. And each, overwhelmed with dark despair, Will beat his head and rend his hair. Each, graced and honoured long, will miss
- **Translation**: 

---

### Verse 17 (Ramayana 0.1442)
- **Original**: 1424 The Ramayana His careless life of easy bliss, In happy troops will play no more On breezy rock and shady shore, But with his darling wife and child Will seek the mountain top, and wild With hopeless desolation, throw Himself, his wife, and babe, below. Ah no: unless the dame I find I ne'er will meet my Vánar kind. Here rather in some distant dell A lonely hermit will I dwell, Where roots and berries will supply My humble wants until I die; Or on the shore will raise a pyre And perish in the kindled fire. Or I will strictly fast until With slow decay my life I kill, And ravening dogs and birds of air The limbs of Hanumán shall tear. Here will I die, but never bring Destruction on my race and king. But still unsearched one grove I see With many a bright A[oka tree. There will I enter in, and through The tangled shade my search renew. Be glory to the host on high, The Sun and Moon who light the sky, The Vasus818 and the Maruts'819 train, 818 The Vasus are a class of eight deities, originally personifications of natural phenomena. 819 The Maruts are the winds or Storm-Gods.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1443)
- **Original**: Canto XIV. The Asoka Grove. 1425 Ádityas820 and the A[vins821 twain. So may I win success, and bring The lady back with triumphing.” Canto XIV. The Asoka Grove. He cleared the barrier at a bound; He stood within the pleasant ground, [404] And with delighted eyes surveyed The climbing plants and varied shade, He saw unnumbered trees unfold The treasures of their pendent gold, As, searching for the Maithil queen, He strayed through alleys soft and green; And when a spray he bent or broke Some little bird that slept awoke. Whene'er the breeze of morning blew, Where'er a startled peacock flew, The gaily coloured branches shed Their flowery rain upon his head That clung around the Vánar till He seemed a blossom-covered hill,822 The earth, on whose fair bosom lay The flowers that fell from every spray, Was glorious as a lovely maid In all her brightest robes arrayed, 820 The Ádityas originally seven deities of the heavenly sphere of whom VaruGa is the chief. The name Áditya was afterwards given to any God, specially to Súrya the Sun. 821 The A[vins are the Heavenly Twins, the Castor and Pollux of the Hindus. 822 The poet forgets that Hanumán has reduced himself to the size of a cat.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1444)
- **Original**: 1426 The Ramayana He saw the breath of morning shake The lilies on the rippling lake Whose waves a pleasant lapping made On crystal steps with gems inlaid. Then roaming through the enchanted ground, A pleasant hill the Vánar found, And grottoes in the living stone With grass and flowery trees o'ergrown. Through rocks and boughs a brawling rill Leapt from the bosom of the hill, Like a proud beauty when she flies From her love's arms with angry eyes. He clomb a tree that near him grew And leafy shade around him threw. “Hence,” thought the Vánar,“shall I see The Maithil dame, if here she be, These lovely trees, this cool retreat Will surely tempt her wandering feet. Here the sad queen will roam apart. And dream of Ráma in her heart.” Canto XV. Sítá. Fair as Kailása white with snow He saw a palace flash and glow, A crystal pavement gem-inlaid, And coral steps and colonnade, And glittering towers that kissed the skies, Whose dazzling splendour charmed his eyes. There pallid, with neglected dress,
- **Translation**: 

---

### Verse 20 (Ramayana 0.1445)
- **Original**: Canto XVI. Hanumán's Lament. 1427 Watched close by fiend and giantess, Her sweet face thin with constant flow Of tears, with fasting and with woe; Pale as the young moon's crescent when The first faint light returns to men: Dim as the flame when clouds of smoke The latent glory hide and choke; Like RohiGí the queen of stars Oppressed by the red planet Mars; From her dear friends and husband torn, Amid the cruel fiends, forlorn, Who fierce-eyed watch around her kept, A tender woman sat and wept. Her sobs, her sighs, her mournful mien, Her glorious eyes, proclaimed the queen. “This, this is she,” the Vánar cried, “Fair as the moon and lotus-eyed, I saw the giant Rávan bear A captive through the fields of air. Such was the beauty of the dame; Her form, her lips, her eyes the same. This peerless queen whom I behold Is Ráma's wife with limbs of gold. Best of the sons of men is he, And worthy of her lord is she.” Canto XVI. Hanumán's Lament.
- **Translation**: 

---

