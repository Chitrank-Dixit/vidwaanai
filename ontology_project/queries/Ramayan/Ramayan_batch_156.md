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

### Verse 1 (Ramayana 0.1146)
- **Original**: 1128 The Ramayana See here the western altar stands Where daily with their trembling hands The aged saints, so long obeyed By me, their gifts of blossoms laid. The holy power, O Raghu's son, By their ascetic virtue won, Still keeps their well-loved altar bright, Filling the air with beams of light. And those seven neighbouring lakes behold Which, when the saints infirm and old, Worn out by fasts, no longer sought, Moved hither drawn by power of thought. Look, Ráma, where the devotees Hung their bark mantles on the trees, Fresh from the bath: those garments wet Through many a day are dripping yet. See, through those aged hermits' power The tender spray, this bright-hued flower With which the saints their worship paid, Fresh to this hour nor change nor fade. Here thou hast seen each lawn and dell, And heard the tale I had to tell: Permit thy servant, lord, I pray, To cast this mortal shell away, For I would dwell, this life resigned, With those great saints of lofty mind, Whom I within this holy shade With reverential care obeyed.” When Ráma and his brother heard The pious prayer the dame preferred, Filled full of transport and amazed They marvelled as her words they praised. Then Ráma to the votaress said
- **Translation**: 

---

### Verse 2 (Ramayana 0.1147)
- **Original**: Canto LXXVI. Pampá. 1129 Whose holy vows were perfected: “Go, lady, where thou fain wouldst be, O thou who well hast honoured me.” Her locks in hermit fashion tied, Clad in bark coat and black deer-hide, When Ráma gave consent, the dame Resigned her body to the flame. Then like the fire that burns and glows, To heaven the sainted lady rose, In all her heavenly garments dressed, Immortal wreaths on neck and breast, Bright with celestial gems she shone Most beautiful to look upon, And like the flame of lightning sent A glory through the firmament. That holy sphere the dame attained, By depth of contemplation gained, Where roam high saints with spirits pure In bliss that shall for aye endure. Canto LXXVI. Pampá. When Zavarí had sought the skies And gained her splendid virtue's prize, Ráma with LakshmaG stayed to brood O'er the strange scenes their eyes had viewed. His mind upon those saints was bent, For power and might preëminent And he to musing LakshmaG spoke The thoughts that in his bosom woke: [318]
- **Translation**: 

---

### Verse 3 (Ramayana 0.1148)
- **Original**: 1130 The Ramayana “Mine eyes this wondrous home have viewed Of those great saints with souls subdued, Where peaceful tigers dwell and birds, And deer abound in heedless herds. Our feet upon the banks have stood Of those seven lakes within the wood, Where we have duly dipped, and paid Libations to each royal shade. Forgotten now are thoughts of ill And joyful hopes my bosom fill. Again my heart is light and gay And grief and care have passed away. Come, brother, let us hasten where Bright Pampá's flood is fresh and fair, And towering in their beauty near Mount Rishyamúka's heights appear, Which, offspring of the Lord of Light, Still fearing Báli's conquering might, With four brave chiefs of Vánar race Sugríva makes his dwelling-place. I long with eager heart to find That leader of the Vánar kind, For on that chief my hopes depend That this our quest have prosperous end.” Thus Ráma spoke, in battle tried, And thus Sumitrá's son replied: “Come, brother, come, and speed away: My spirit brooks no more delay.” Thus spake Sumitrá's son, and then Forth from the grove the king of men With his dear brother by his side To Pampá's lucid waters hied. He gazed upon the woods where grew
- **Translation**: 

---

### Verse 4 (Ramayana 0.1149)
- **Original**: Canto LXXVI. Pampá. 1131 Trees rich in flowers of every hue. From brake and dell on every side The curlew and the peacock cried, And flocks of screaming parrots made Shrill music in the bloomy shade. His eager eyes, as on he went, On many a pool and tree were bent. Inflamed with love he journeyed on Till a fair flood before him shone. He stood upon the water's side Which streams from distant hills supplied: Matanga's name that water bore: There bathed he from the shelving shore. Then, each on earnest thoughts intent, Still farther on their way they went. But Ráma's heart once more gave way Beneath his grief and wild dismay. Before him lay the noble flood Adorned with many a lotus bud. On its fair banks A[oka glowed, And all bright trees their blossoms showed. Green banks that silver waves confined With lovely groves were fringed and lined. The crystal waters in their flow Showed level sands that gleamed below. There glittering fish and tortoise played, And bending trees gave pleasant shade. There creepers on the branches hung With lover-like embraces clung. There gay Gandharvas loved to meet, And Kinnars sought the calm retreat. There wandering Yakshas found delight, Snake-gods and rovers of the night. Cool were the pleasant waters, gay
- **Translation**: 

---

### Verse 5 (Ramayana 0.1150)
- **Original**: 1132 The Ramayana Each tree with creeper, flower, and spray. There flushed the lotus darkly red, Here their white glory lilies spread, Here sweet buds showed their tints of blue: So carpets gleam with many a hue. A grove of Mangoes blossomed nigh, Echoing with the peacock's cry. When Ráma by his brother's side The lovely flood of Pampá eyed, Decked like a beauty, fair to see With every charm of flower and tree, His mighty heart with woe was rent And thus he spoke in wild lament “Here, LakshmaG, on this beauteous shore, Stands, dyed with tints of many an ore, The mountain Rishyamúka bright With flowery trees that crown each height. Sprung from the chief who, famed of yore, The name of Riksharajas bore, Sugríva, chieftain strong and dread, Dwells on that mountain's towering head. Go to him, best of men, and seek That prince of Vánars on the peak, I cannot longer brook my pain, Or, Sítá lost, my life retain.” Thus by the pangs of love distressed, His thoughts on Sítá bent, His faithful brother he addressed, And cried in wild lament. He reached the lovely ground that lay On Pampá's wooded side, And told in anguish and dismay, The grief he could not hide.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1151)
- **Original**: Canto LXXVI. Pampá. 1133 With listless footsteps faint and slow His way the chief pursued, Till Pampá with her glorious show Of flowering woods he viewed. Through shades where every bird was found The prince with LakshmaG passed, And Pampá with her groves around Burst on his eyes at last. [319]
- **Translation**: 

---

### Verse 7 (Ramayana 0.1152)
- **Original**: BOOK IV. Canto I. Ráma's Lament. The princes stood by Pampá's side522 Which blooming lilies glorified. With troubled heart and sense o'erthrown There Ráma made his piteous moan. As the fair flood before him lay The reason of the chief gave way; And tender thoughts within him woke, As to Sumitrá's son he spoke: 522 Pampá is said by the commentator to be the name both of a lake and a brook which flows into it. The brook is said to rise in the hill Rishyamúka.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1153)
- **Original**: Canto I. Ráma's Lament. 1135 “How lovely Pampá's waters show, Where streams of lucid crystal flow! What glorious trees o'erhang the flood Which blooms of opening lotus stud! Look on the banks of Pampá where Thick groves extend divinely fair; And piles of trees, like hills in size, Lift their proud summits to the skies. But thought of Bharat's523 pain and toil, And my dear spouse the giant's spoil, Afflict my tortured heart and press My spirit down with heaviness. Still fair to me though sunk in woe Bright Pampá and her forest show. Where cool fresh waters charm the sight, And flowers of every hue are bright. The lotuses in close array Their passing loveliness display, And pard and tiger, deer and snake Haunt every glade and dell and brake. Those grassy spots display the hue Of topazes and sapphires' blue, And, gay with flowers of every dye, With richly broidered housings vie. What loads of bloom the high trees crown, Or weigh the bending branches down! And creepers tipped with bud and flower Each spray and loaded limb o'erpower. Now cool delicious breezes blow, And kindle love's voluptuous glow, When balmy sweetness fills the air, And fruit and flowers and trees are fair. 523 Who was acting as Regent for Ráma and leading an ascetic life while he mourned for his absent brother.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1154)
- **Original**: 1136 The Ramayana Those waving woods, that shine with bloom, Each varied tint in turn assume. Like labouring clouds they pour their showers In rain or ever-changing flowers. Behold, those forest trees, that stand High upon rock and table-land, As the cool gales their branches bend, Their floating blossoms downward send. See, LakshmaG, how the breezes play With every floweret on the spray. And sport in merry guise with all The fallen blooms and those that fall. See, brother, where the merry breeze Shakes the gay boughs of flowery trees, Disturbed amid their toil a throng Of bees pursue him, loud in song. The Koïls,524 mad with sweet delight, The bending trees to dance invite; And in its joy the wild wind sings As from the mountain cave he springs. On speed the gales in rapid course, And bend the woods beneath their force, Till every branch and spray they bind In many a tangled knot entwined. What balmy sweets those gales dispense With cool and sacred influence! Fatigue and trouble vanish: such The magic of their gentle touch. Hark, when the gale the boughs has bent In woods of honey redolent, Through all their quivering sprays the trees Are vocal with the murmuring bees. 524 The Indian Cuckoo.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1155)
- **Original**: Canto I. Ráma's Lament. 1137 The hills with towering summits rise, And with their beauty charm the eyes, Gay with the giant trees which bright With blossom spring from every height: And as the soft wind gently sways The clustering blooms that load the sprays, The very trees break forth and sing With startled wild bees' murmuring. Thine eyes to yonder Cassias525 turn Whose glorious clusters glow and burn. [320] Those trees in yellow robes behold, Like giants decked with burnished gold. Ah me, Sumitrá's son, the spring Dear to sweet birds who love and sing, Wakes in my lonely breast the flame Of sorrow as I mourn my dame. Love strikes me through with darts of fire, And wakes in vain the sweet desire. Hark, the loud Koïl swells his throat, And mocks me with his joyful note. I hear the happy wild-cock call Beside the shady waterfall. His cry of joy afflicts my breast By love's absorbing might possessed. My darling from our cottage heard One morn in spring this shrill-toned bird, And called me in her joy to hear The happy cry that charmed her ear. 525 The Cassia Fistula or Amaltás is a splendid tree like a giant laburnum covered with a profusion of chains and tassels of gold. Dr. Roxburgh well describes it as“uncommonly beautiful when in flower, few trees surpassing it in the elegance of its numerous long pendulous racemes of large bright-yellow flowers intermixed with the young lively green foliage.” It is remarkable also for its curious cylindrical black seed-pods about two feet long, which are called monkeys' walking-sticks.
- **Translation**: 

---

### Verse 11 (Ramayana 0.1156)
- **Original**: 1138 The Ramayana See, birds of every varied voice Around us in the woods rejoice, On creeper, shrub, and plant alight, Or wing from tree to tree their flight. Each bird his kindly mate has found, And loud their notes of triumph sound, Blending in sweetest music like The distant warblings of the shrike. See how the river banks are lined With birds of every hue and kind. Here in his joy the Koïl sings, There the glad wild-cock flaps his wings. The blooms of bright A[okas526 where The song of wild bees fills the air, And the soft whisper of the boughs Increase my longing for my spouse. The vernal flush of flower and spray Will burn my very soul away. What use, what care have I for life If I no more may see my wife Soft speaker with the glorious hair, And eyes with silken lashes fair? Now is the time when all day long 526 “The Jonesia Asoca is a tree of considerable size, native of southern India. It blossoms in February and March with large erect compact clusters of flowers, varying in colour from pale-orange to scarlet, almost to be mistaken, on a hasty glance, for immense trusses of bloom of an Ixora. Mr. Fortune considered this tree, when in full bloom, superior in beauty even to the Amherstia. The first time I saw the Asoc in flower was on the hill where the famous rock-cut temple of Kárlí is situated, and a large concourse of natives had assembled for the celebration of some Hindoo festival. Before proceeding to the temple the Mahratta women gathered from two trees, which were flowering somewhat below, each a fine truss of blossom, and inserted it in the hair at the back of her head.… As they moved about in groups it is impossible to imagine a more delightful effect than the rich scarlet bunches of flowers presented on their fine glossy jet-black hair.” FIRMINGER {FNS ,Gardening for India.
- **Translation**: 

---

### Verse 12 (Ramayana 0.1157)
- **Original**: Canto I. Ráma's Lament. 1139 The Koïls fill the woods with song. And gardens bloom at spring's sweet touch Which my beloved loved so much. Ah me, Sumitrá's son, the fire Of sorrow, sprung from soft desire, Fanned by the charms the spring time shows, Will burn my heart and end my woes, Whose sad eyes look on each fair tree, But my sweet love no more may see. Ah me, Ah me, from hour to hour Love in my soul will wax in power, And spring, upon whose charms I gaze, Whose breath the heat of toil allays, With thoughts of her for whom I strain My hopeless eyes, increase my pain. As fire in summer rages through The forests thick with dry bamboo, So will my fawn eyed love consume My soul o'erwhelmed with thoughts of gloom. Behold, beneath each spreading tree The peacocks dance527 in frantic glee, And, stirred by all the gales that blow, Their tails with jewelled windows glow, Each bird, in happy love elate, Rejoices with his darling mate. But sights like these of joy and peace My pangs of hopeless love increase. See on the mountain slope above The peahen languishing with love. Behold her now in amorous dance Close to her consort's side advance. 527 No other word can express the movements of peafowl under the influence of pleasing excitement, especially when after the long drought they hear the welcome roar of the thunder and feel that the rain is near.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1158)
- **Original**: 1140 The Ramayana He with a laugh of joy and pride Displays his glittering pinions wide; And follows through the tangled dell The partner whom he loves so well. Ah happy bird! no giant's hate Has robbed him of his tender mate; And still beside his loved one he Dances beneath the shade in glee. Ah, in this month when flowers are fair My widowed woe is hard to bear. See, gentle love a home may find In creatures of inferior kind. See how the peahen turns to meet Her consort now with love-drawn feet.[321] So, LakshmaG, if my large-eyed dear, The child of Janak still were here, She, by love's thrilling influence led, Upon my breast would lay her head. These blooms I gathered from the bough Without my love are useless now. A thousand blossoms fair to see With passing glory clothe each tree That hangs its cluster-burthened head Now that the dewy months528 are fled, But, followed by the bees that ply Their fragrant task, they fall and die. A thousand birds in wild delight Their rapture-breathing notes unite; Bird calls to bird in joyous strain, And turns my love to frenzied pain. O, if beneath those alien skies, There be a spring where Sítá lies, 528 The Dewy Season is one of the six ancient seasons of the Indian year, lasting from the middle of January to the middle of March.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1159)
- **Original**: Canto I. Ráma's Lament. 1141 I know my prisoned love must be Touched with like grief, and mourn with me. But ah, methinks that dreary clime Knows not the touch of spring's sweet time. How could my black eyed love sustain, Without her lord, so dire a pain? Or if the sweet spring come to her In distant lands a prisoner, How may his advent and her met On every side with taunt and threat? Ah, if the springtide's languor came With soft enchantment o'er my dame, My darling of the lotus eye, My gently speaking love, would die; For well my spirit knows that she Can never live bereft of me With love that never wavered yet My Sítá's heart, on me is set, Who, with a soul that ne'er can stray, With equal love her love repay. In vain, in vain the soft wind brings Sweet blossoms on his balmy wings; Delicious from his native snow, To me like fire he seems to glow. O, how I loved a breeze like this When darling Sítá shared the bliss! But now in vain for me it blows To fan the fury of my woes. That dark-winged bird that sought the skies Foretelling grief with warning cries, Sits on the tree where buds are gay, And pours glad music from the spray. That rover of the fields of air Will aid my love with friendly care,
- **Translation**: 

---

### Verse 15 (Ramayana 0.1160)
- **Original**: 1142 The Ramayana And me with gracious pity guide To my large-eyed Videhan's side.529 Hark, LakshmaG, how the woods around With love-inspiring chants resound, Where birds in every bloom-crowned tree Pour forth their amorous minstrelsy. As though an eager gallant wooed A gentle maid by love subdued, Enamoured of her flowers the bee Darts at the wind-rocked Tila tree.530 A [oka, brightest tree that grows, That lends a pang to lovers' woes, Hangs out his gorgeous bloom in scorn And mocks me as I weep forlorn. O Lakshma G, turn thine eye and see Each blossom-laden Mango tree, Like a young lover gaily dressed Whom fond desire forbids to rest. Look, son of Queen Sumitrá through The forest glades of varied hue, Where blooms are bright and grass is green The Kinnars531 with their loves are seen. See, brother, see where sweet and bright Those crimson lilies charm the sight, And o'er the flood a radiance throw Fair as the morning's roseate glow. See, Pampá, most divinely sweet, 529 Ráma appears to mean that on a former occasion a crow flying high over- head was an omen that indicated his approaching separation from Sítá; and that now the same bird's perching on a tree near him may be regarded as a happy augury that she will soon be restored to her husband. 530 A tree with beautiful and fragrant blossoms. 531 A race of semi-divine musicians attached to the service of Kuvera, repre- sented as centaurs reversed with human figures and horses' heads.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1161)
- **Original**: Canto I. Ráma's Lament. 1143 The swan's and mallard's loved retreat, Shows her glad waters bright and clear, Where lotuses their heads uprear From the pure wave, and charm the view With mingled tints of red and blue. Each like the morning's early beams Reflected in the crystal gleams; And bees on their sweet toil intent Weigh down each tender filament. There with gay lawns the wood recedes; There wildfowl sport amid the reeds, There roedeer stand upon the brink, And elephants descend to drink. The rippling waves which winds make fleet Against the bending lilies beat, And opening bud and flower and stem Gleam with the drops that hang on them. Life has no pleasure left for me While my dear queen I may not see, [322] Who loved so well those blooms that vie With the full splendour of her eye. O tyrant Love, who will not let My bosom for one hour forget The lost one whom I yearn to meet, Whose words were ever kind and sweet. Ah, haply might my heart endure This hopeless love that knows not cure, If spring with all his trees in flower Assailed me not with ruthless power. Each lovely scene, each sound and sight Wherein, with her, I found delight, Has lost the charm so sweet of yore, And glads my widowed heart no more. On lotus buds I seem to gaze,
- **Translation**: 

---

### Verse 17 (Ramayana 0.1162)
- **Original**: 1144 The Ramayana Or blooms that deck Palá[a532 sprays;533 But to my tortured memory rise The glories of my darling's eyes. Cool breezes through the forest stray Gathering odours on their way, Enriched with all the rifled scent Of lotus flower and filament. Their touch upon my temples falls And Sítá's fragrant breath recalls. Now look, dear brother, on the right Of Pampá towers a mountain height Where fairest Cassia trees unfold The treasures of their burnished gold. Proud mountain king! his woody side With myriad ores is decked and dyed, And as the wind-swept blossoms fall Their fragrant dust is stained with all. To yon high lands thy glances turn: With pendent fire they flash and burn, Where in their vernal glory blaze Palá[a flowers on leafless sprays. O Lakshma G, look! on Pampá's side What fair trees rise in blooming pride! 532 Butea Frondosa. A tree that bears a profusion of brilliant red flowers which appear before the leaves. 533 I omit five[lokaswhich contain nothing but a list of trees for which, with one or two exceptions, there are no equivalent names in English. The following is Gorresio's translation of the corresponding passage in the Bengal recension:— “Oh come risplendono in questa stagione di primavera i vitici, le galedupe, le bassie, le dalbergie, i diospyri… le tile, le michelie, le rottlerie, le pentaptere ed i pterospermi, i bombaci, le grislee, gli abri, gli amaranti e le dalbergie; i sirii, le galedupe, le barringtonie ed i palmizi, i xanthocymi, il pepebetel, le verbosine e le ticaie, le nauclee le erythrine, gli asochi, e le tapie fanno d'ogni intorno pompa de' lor fiori.”
- **Translation**: 

---

### Verse 18 (Ramayana 0.1163)
- **Original**: Canto I. Ráma's Lament. 1145 What climbing plants above them show Or hang their flowery garlands low! See how the amorous creeper rings The wind-rocked trees to which she clings, As though a dame by love impelled With clasping arms her lover held. Drunk with the varied scents that fill The balmy air, from hill to hill, From grove to grove, from tree to tree, The joyous wind is wandering free. These gay trees wave their branches bent By blooms, of honey redolent. There, slowly opening to the day, Buds with dark lustre deck the spray. The wild bee rests a moment where Each tempting flower is sweet and fair, Then, coloured by the pollen dyes, Deep in some odorous blossom lies. Soon from his couch away he springs: To other trees his course he wings, And tastes the honeyed blooms that grow Where Pampá's lucid waters flow. See, LakshmaG, see, how thickly spread With blossoms from the trees o'erhead, That grass the weary traveller woos With couches of a thousand hues, And beds on every height arrayed With red and yellow tints are laid, No longer winter chills the earth: A thousand flowerets spring to birth, And trees in rivalry assume Their vernal garb of bud and bloom. How fair they look, how bright and gay With tasselled flowers on every spray!
- **Translation**: 

---

### Verse 19 (Ramayana 0.1164)
- **Original**: 1146 The Ramayana While each to each proud challenge flings Borne in the song the wild bee sings. That mallard by the river edge Has bathed amid the reeds and sedge: Now with his mate he fondly plays And fires my bosom as I gaze. Mandákiní534 is far renowned: No lovelier flood on earth is found; But all her fairest charms combined In this sweet stream enchant the mind. O, if my love were here to look With me upon this lovely brook, Never for Ayodhyá would I pine, Or wish that Indra's lot were mine. If by my darling's side I strayed O'er the soft turf which decks the glade, Each craving thought were sweetly stilled, Each longing of my soul fulfilled. But, now my love is far away, Those trees which make the woods so gay, In all their varied beauty dressed, Wake thoughts of anguish in my breast. That lotus-covered stream behold Whose waters run so fresh and cold,[323] 534 A sacred stream often mentioned in the course of the poem. See Book II, Canto XCV.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1165)
- **Original**: Canto I. Ráma's Lament. 1147 Sweet rill, the wildfowl's loved resort, Where curlew, swan, and diver sport; Where with his consort plays the drake, And tall deer love their thirst to slake, While from each woody bank is heard The wild note of each happy bird. The music of that joyous quire Fills all my soul with soft desire; And, as I hear, my sad thoughts fly To Sítá of the lotus eye, Whom, lovely with her moonbright cheek, In vain mine eager glances seek. Now turn, those chequered lawns survey Where hart and hind together stray. Ah, as they wander at their will My troubled breast with grief they fill, While torn by hopeless love I sigh For Sítá of the fawn-like eye. If in those glades where, touched by spring, Gay birds their amorous ditties sing, Mine own beloved I might see, Then, brother, it were well with me: If by my side she wandered still, And this cool breeze that stirs the rill Touched with its gentle breath the brows Of mine own dear Videhan spouse. For, LakshmaG, O how blest are those On whom the breath of Pampá blows, Dispelling all their care and gloom With sweets from where the lilies bloom! How can my gentle love remain Alive amid the woe and pain, Where prisoned far away she lies,— My darling of the lotus eyes?
- **Translation**: 

---

