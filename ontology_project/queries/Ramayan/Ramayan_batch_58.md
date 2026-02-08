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

### Verse 1 (Ramayan 0.1141)
- **Original**: Canto LXXIV. Kabandha's Death. 1123 Deep in the woods will meet thine eyes. No wandering elephants invade The stillness of that holy shade, But checked by saint Matanga's power They spare each consecrated bower. Through many an age those trees have stood World-famous as Matanga's wood Still, Raghu's son, pursue thy way: Through shades where birds are vocal stray, Fair as the blessed wood where rove Immortal Gods, or Nandan's grove. Near Pampá eastward, full in sight, Stands Rishyamúka's wood-crowned height. 'Tis hard to climb that towering steep Where serpents unmolested sleep. The free and bounteous, formed of old By Brahmá of superior mould, Who sink when day is done to rest Reclining on that mountain crest,— What wealth or joy in dreams they view, Awaking find the vision true. But if a villain stained with crime That holy hill presume to climb, The giants in their fury sweep From the hill top the wretch asleep. There loud and long is heard the roar Of elephants on Pampá's shore, Who near Matanga's dwelling stray And in those waters bathe and play. A while they revel by the flood, Their temples stained with streams like blood, Then wander far away dispersed, Dark as huge clouds before they burst. But ere they part they drink their fill
- **Translation**: 

---

### Verse 2 (Ramayan 0.1142)
- **Original**: 1124 The Ramayana Of bright pure water from the rill, Delightful to the touch, where meet Scents of all flowers divinely sweet, Then speeding from the river side Deep in the sheltering thicket hide. Then bears and tigers shalt thou view Whose soft skins show the sapphire's hue, And silvan deer that wander nigh Shall harmless from thy presence fly. High in that mountain's wooded side Is a fair cavern deep and wide, Yet hard to enter: piles of rock The portals of the cavern block.521 Fast by the eastern door a pool Gleams with broad waters fresh and cool, Where stores of roots and fruit abound, And thick trees shade the grassy ground. This mountain cave the virtuous-souled Sugríva, and his Vánars hold, And oft the mighty chieftain seeks The summits of those towering peaks.” Thus spake Kabandha high in air His counsel to the royal pair. Still on his neck that wreath he bore, And radiance like the sun's he wore. Their eyes the princely brothers raised And on that blissful being gazed: “Behold, we go: no more delay; Begin,” they cried,“thy heavenward way.” “Depart,” Kabandha's voice replied, “Pursue your search, and bliss betide.” 521 Or as the commentator Tírtha says,Zilápidháná, rock-covered, may be the name of the cavern.
- **Translation**: 

---

### Verse 3 (Ramayan 0.1143)
- **Original**: Canto LXXV. Savarí. 1125 Thus to the happy chiefs he said, Then on his heavenward journey sped. Thus once again Kabandha won A shape that glittered like the sun Without a spot or stain. Thus bade he Ráma from the air To great Sugríva's side repair His friendly love to gain. Canto LXXV. Savarí. Thus counselled by their friendly guide On through the wood the princes hied, Pursuing still the eastern road To Pampá which Kabandha showed, Where trees that on the mountains grew With fruit like honey charmed the view. They rested weary for the night Upon a mountain's wooded height, Then onward with the dawn they hied And stood on Pampá's western side, Where Zavarí's fair home they viewed Deep in that shady solitude. The princes reached the holy ground Where noble trees stood thick around, And joying in the lovely view Near to the aged votaress drew. To meet the sons of Raghu came, With hands upraised, the pious dame, And bending low with reverence meet Welcomed them both and pressed their feet.
- **Translation**: 

---

### Verse 4 (Ramayan 0.1144)
- **Original**: 1126 The Ramayana Then water, as beseems, she gave, Their lips to cool, their feet to lave. To that pure saint who never broke One law of duty Ráma spoke: “I trust no cares invade thy peace, While holy works and zeal increase; That thou content with scanty food All touch of ire hast long subdued; That all thy vows are well maintained[317] While peace of mind is surely gained, That reverence of the saints who taught Thy faithful heart due fruit has brought.” The aged votaress pure of taint, Revered by every perfect saint, Rose to her feet by Ráma's side And thus in gentle tones replied: “My penance meed this day I see Complete, my lord, in meeting thee. This day the fruit of birth I gain, Nor have I served the saints in vain. I reap rich fruits of toil and vow, And heaven itself awaits me now, When I, O chief of men, have done Honour to thee the godlike one. I feel, great lord, thy gentle eye My earthly spirit purify, And I, brave tamer of thy foes, Shall through thy grace in bliss repose. Thy feet by Chitrakúma strayed When those great saints whom I obeyed, In dazzling chariots bright of hue, Hence to their heavenly mansions flew.
- **Translation**: 

---

### Verse 5 (Ramayan 0.1145)
- **Original**: Canto LXXV. Savarí. 1127 As the high saints were borne away I heard their holy voices say: “In this pure grove, O devotee, Prince Ráma soon will visit thee. When he and LakshmaG seek this shade, Be to thy guests all honour paid. Him shalt thou see, and pass away To those blest worlds which ne'er decay.” To me, O mighty chief, the best Of lofty saints these words addressed. Laid up within my dwelling lie Fruits of each sort which woods supply,— Food culled for thee in endless store From every tree on Pampá's shore.” Thus to her virtuous guest she sued And he, with heavenly lore endued, Words such as these in turn addressed To her with equal knowledge blest: “Danu himself the power has told Of thy great masters lofty-souled. Now if thou will, mine eyes would fain Assurance of their glories gain.” She heard the prince his wish declare: Then rose she, and the royal pair Of brothers through the wood she led That round her holy dwelling spread. “Behold Matanga's wood” she cried, “A grove made famous far and wide. Dark as thick clouds and filled with herds Of wandering deer, and joyous birds. In this pure spot each reverend sire With offerings fed the holy fire.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1146)
- **Original**: 1128 The Ramayana See here the western altar stands Where daily with their trembling hands The aged saints, so long obeyed By me, their gifts of blossoms laid. The holy power, O Raghu's son, By their ascetic virtue won, Still keeps their well-loved altar bright, Filling the air with beams of light. And those seven neighbouring lakes behold Which, when the saints infirm and old, Worn out by fasts, no longer sought, Moved hither drawn by power of thought. Look, Ráma, where the devotees Hung their bark mantles on the trees, Fresh from the bath: those garments wet Through many a day are dripping yet. See, through those aged hermits' power The tender spray, this bright-hued flower With which the saints their worship paid, Fresh to this hour nor change nor fade. Here thou hast seen each lawn and dell, And heard the tale I had to tell: Permit thy servant, lord, I pray, To cast this mortal shell away, For I would dwell, this life resigned, With those great saints of lofty mind, Whom I within this holy shade With reverential care obeyed.” When Ráma and his brother heard The pious prayer the dame preferred, Filled full of transport and amazed They marvelled as her words they praised. Then Ráma to the votaress said
- **Translation**: 

---

### Verse 7 (Ramayan 0.1147)
- **Original**: Canto LXXVI. Pampá. 1129 Whose holy vows were perfected: “Go, lady, where thou fain wouldst be, O thou who well hast honoured me.” Her locks in hermit fashion tied, Clad in bark coat and black deer-hide, When Ráma gave consent, the dame Resigned her body to the flame. Then like the fire that burns and glows, To heaven the sainted lady rose, In all her heavenly garments dressed, Immortal wreaths on neck and breast, Bright with celestial gems she shone Most beautiful to look upon, And like the flame of lightning sent A glory through the firmament. That holy sphere the dame attained, By depth of contemplation gained, Where roam high saints with spirits pure In bliss that shall for aye endure. Canto LXXVI. Pampá. When Zavarí had sought the skies And gained her splendid virtue's prize, Ráma with LakshmaG stayed to brood O'er the strange scenes their eyes had viewed. His mind upon those saints was bent, For power and might preëminent And he to musing LakshmaG spoke The thoughts that in his bosom woke: [318]
- **Translation**: 

---

### Verse 8 (Ramayan 0.1148)
- **Original**: 1130 The Ramayana “Mine eyes this wondrous home have viewed Of those great saints with souls subdued, Where peaceful tigers dwell and birds, And deer abound in heedless herds. Our feet upon the banks have stood Of those seven lakes within the wood, Where we have duly dipped, and paid Libations to each royal shade. Forgotten now are thoughts of ill And joyful hopes my bosom fill. Again my heart is light and gay And grief and care have passed away. Come, brother, let us hasten where Bright Pampá's flood is fresh and fair, And towering in their beauty near Mount Rishyamúka's heights appear, Which, offspring of the Lord of Light, Still fearing Báli's conquering might, With four brave chiefs of Vánar race Sugríva makes his dwelling-place. I long with eager heart to find That leader of the Vánar kind, For on that chief my hopes depend That this our quest have prosperous end.” Thus Ráma spoke, in battle tried, And thus Sumitrá's son replied: “Come, brother, come, and speed away: My spirit brooks no more delay.” Thus spake Sumitrá's son, and then Forth from the grove the king of men With his dear brother by his side To Pampá's lucid waters hied. He gazed upon the woods where grew
- **Translation**: 

---

### Verse 9 (Ramayan 0.1149)
- **Original**: Canto LXXVI. Pampá. 1131 Trees rich in flowers of every hue. From brake and dell on every side The curlew and the peacock cried, And flocks of screaming parrots made Shrill music in the bloomy shade. His eager eyes, as on he went, On many a pool and tree were bent. Inflamed with love he journeyed on Till a fair flood before him shone. He stood upon the water's side Which streams from distant hills supplied: Matanga's name that water bore: There bathed he from the shelving shore. Then, each on earnest thoughts intent, Still farther on their way they went. But Ráma's heart once more gave way Beneath his grief and wild dismay. Before him lay the noble flood Adorned with many a lotus bud. On its fair banks A[oka glowed, And all bright trees their blossoms showed. Green banks that silver waves confined With lovely groves were fringed and lined. The crystal waters in their flow Showed level sands that gleamed below. There glittering fish and tortoise played, And bending trees gave pleasant shade. There creepers on the branches hung With lover-like embraces clung. There gay Gandharvas loved to meet, And Kinnars sought the calm retreat. There wandering Yakshas found delight, Snake-gods and rovers of the night. Cool were the pleasant waters, gay
- **Translation**: 

---

### Verse 10 (Ramayan 0.1150)
- **Original**: 1132 The Ramayana Each tree with creeper, flower, and spray. There flushed the lotus darkly red, Here their white glory lilies spread, Here sweet buds showed their tints of blue: So carpets gleam with many a hue. A grove of Mangoes blossomed nigh, Echoing with the peacock's cry. When Ráma by his brother's side The lovely flood of Pampá eyed, Decked like a beauty, fair to see With every charm of flower and tree, His mighty heart with woe was rent And thus he spoke in wild lament “Here, LakshmaG, on this beauteous shore, Stands, dyed with tints of many an ore, The mountain Rishyamúka bright With flowery trees that crown each height. Sprung from the chief who, famed of yore, The name of Riksharajas bore, Sugríva, chieftain strong and dread, Dwells on that mountain's towering head. Go to him, best of men, and seek That prince of Vánars on the peak, I cannot longer brook my pain, Or, Sítá lost, my life retain.” Thus by the pangs of love distressed, His thoughts on Sítá bent, His faithful brother he addressed, And cried in wild lament. He reached the lovely ground that lay On Pampá's wooded side, And told in anguish and dismay, The grief he could not hide.
- **Translation**: 

---

### Verse 11 (Ramayan 0.1151)
- **Original**: Canto LXXVI. Pampá. 1133 With listless footsteps faint and slow His way the chief pursued, Till Pampá with her glorious show Of flowering woods he viewed. Through shades where every bird was found The prince with LakshmaG passed, And Pampá with her groves around Burst on his eyes at last. [319]
- **Translation**: 

---

### Verse 12 (Ramayan 0.1152)
- **Original**: BOOK IV. Canto I. Ráma's Lament. The princes stood by Pampá's side522 Which blooming lilies glorified. With troubled heart and sense o'erthrown There Ráma made his piteous moan. As the fair flood before him lay The reason of the chief gave way; And tender thoughts within him woke, As to Sumitrá's son he spoke: 522 Pampá is said by the commentator to be the name both of a lake and a brook which flows into it. The brook is said to rise in the hill Rishyamúka.
- **Translation**: 

---

### Verse 13 (Ramayan 0.1153)
- **Original**: Canto I. Ráma's Lament. 1135 “How lovely Pampá's waters show, Where streams of lucid crystal flow! What glorious trees o'erhang the flood Which blooms of opening lotus stud! Look on the banks of Pampá where Thick groves extend divinely fair; And piles of trees, like hills in size, Lift their proud summits to the skies. But thought of Bharat's523 pain and toil, And my dear spouse the giant's spoil, Afflict my tortured heart and press My spirit down with heaviness. Still fair to me though sunk in woe Bright Pampá and her forest show. Where cool fresh waters charm the sight, And flowers of every hue are bright. The lotuses in close array Their passing loveliness display, And pard and tiger, deer and snake Haunt every glade and dell and brake. Those grassy spots display the hue Of topazes and sapphires' blue, And, gay with flowers of every dye, With richly broidered housings vie. What loads of bloom the high trees crown, Or weigh the bending branches down! And creepers tipped with bud and flower Each spray and loaded limb o'erpower. Now cool delicious breezes blow, And kindle love's voluptuous glow, When balmy sweetness fills the air, And fruit and flowers and trees are fair. 523 Who was acting as Regent for Ráma and leading an ascetic life while he mourned for his absent brother.
- **Translation**: 

---

### Verse 14 (Ramayan 0.1154)
- **Original**: 1136 The Ramayana Those waving woods, that shine with bloom, Each varied tint in turn assume. Like labouring clouds they pour their showers In rain or ever-changing flowers. Behold, those forest trees, that stand High upon rock and table-land, As the cool gales their branches bend, Their floating blossoms downward send. See, LakshmaG, how the breezes play With every floweret on the spray. And sport in merry guise with all The fallen blooms and those that fall. See, brother, where the merry breeze Shakes the gay boughs of flowery trees, Disturbed amid their toil a throng Of bees pursue him, loud in song. The Koïls,524 mad with sweet delight, The bending trees to dance invite; And in its joy the wild wind sings As from the mountain cave he springs. On speed the gales in rapid course, And bend the woods beneath their force, Till every branch and spray they bind In many a tangled knot entwined. What balmy sweets those gales dispense With cool and sacred influence! Fatigue and trouble vanish: such The magic of their gentle touch. Hark, when the gale the boughs has bent In woods of honey redolent, Through all their quivering sprays the trees Are vocal with the murmuring bees. 524 The Indian Cuckoo.
- **Translation**: 

---

### Verse 15 (Ramayan 0.1155)
- **Original**: Canto I. Ráma's Lament. 1137 The hills with towering summits rise, And with their beauty charm the eyes, Gay with the giant trees which bright With blossom spring from every height: And as the soft wind gently sways The clustering blooms that load the sprays, The very trees break forth and sing With startled wild bees' murmuring. Thine eyes to yonder Cassias525 turn Whose glorious clusters glow and burn. [320] Those trees in yellow robes behold, Like giants decked with burnished gold. Ah me, Sumitrá's son, the spring Dear to sweet birds who love and sing, Wakes in my lonely breast the flame Of sorrow as I mourn my dame. Love strikes me through with darts of fire, And wakes in vain the sweet desire. Hark, the loud Koïl swells his throat, And mocks me with his joyful note. I hear the happy wild-cock call Beside the shady waterfall. His cry of joy afflicts my breast By love's absorbing might possessed. My darling from our cottage heard One morn in spring this shrill-toned bird, And called me in her joy to hear The happy cry that charmed her ear. 525 The Cassia Fistula or Amaltás is a splendid tree like a giant laburnum covered with a profusion of chains and tassels of gold. Dr. Roxburgh well describes it as“uncommonly beautiful when in flower, few trees surpassing it in the elegance of its numerous long pendulous racemes of large bright-yellow flowers intermixed with the young lively green foliage.” It is remarkable also for its curious cylindrical black seed-pods about two feet long, which are called monkeys' walking-sticks.
- **Translation**: 

---

### Verse 16 (Ramayan 0.1156)
- **Original**: 1138 The Ramayana See, birds of every varied voice Around us in the woods rejoice, On creeper, shrub, and plant alight, Or wing from tree to tree their flight. Each bird his kindly mate has found, And loud their notes of triumph sound, Blending in sweetest music like The distant warblings of the shrike. See how the river banks are lined With birds of every hue and kind. Here in his joy the Koïl sings, There the glad wild-cock flaps his wings. The blooms of bright A[okas526 where The song of wild bees fills the air, And the soft whisper of the boughs Increase my longing for my spouse. The vernal flush of flower and spray Will burn my very soul away. What use, what care have I for life If I no more may see my wife Soft speaker with the glorious hair, And eyes with silken lashes fair? Now is the time when all day long 526 “The Jonesia Asoca is a tree of considerable size, native of southern India. It blossoms in February and March with large erect compact clusters of flowers, varying in colour from pale-orange to scarlet, almost to be mistaken, on a hasty glance, for immense trusses of bloom of an Ixora. Mr. Fortune considered this tree, when in full bloom, superior in beauty even to the Amherstia. The first time I saw the Asoc in flower was on the hill where the famous rock-cut temple of Kárlí is situated, and a large concourse of natives had assembled for the celebration of some Hindoo festival. Before proceeding to the temple the Mahratta women gathered from two trees, which were flowering somewhat below, each a fine truss of blossom, and inserted it in the hair at the back of her head.… As they moved about in groups it is impossible to imagine a more delightful effect than the rich scarlet bunches of flowers presented on their fine glossy jet-black hair.” FIRMINGER {FNS ,Gardening for India.
- **Translation**: 

---

### Verse 17 (Ramayan 0.1157)
- **Original**: Canto I. Ráma's Lament. 1139 The Koïls fill the woods with song. And gardens bloom at spring's sweet touch Which my beloved loved so much. Ah me, Sumitrá's son, the fire Of sorrow, sprung from soft desire, Fanned by the charms the spring time shows, Will burn my heart and end my woes, Whose sad eyes look on each fair tree, But my sweet love no more may see. Ah me, Ah me, from hour to hour Love in my soul will wax in power, And spring, upon whose charms I gaze, Whose breath the heat of toil allays, With thoughts of her for whom I strain My hopeless eyes, increase my pain. As fire in summer rages through The forests thick with dry bamboo, So will my fawn eyed love consume My soul o'erwhelmed with thoughts of gloom. Behold, beneath each spreading tree The peacocks dance527 in frantic glee, And, stirred by all the gales that blow, Their tails with jewelled windows glow, Each bird, in happy love elate, Rejoices with his darling mate. But sights like these of joy and peace My pangs of hopeless love increase. See on the mountain slope above The peahen languishing with love. Behold her now in amorous dance Close to her consort's side advance. 527 No other word can express the movements of peafowl under the influence of pleasing excitement, especially when after the long drought they hear the welcome roar of the thunder and feel that the rain is near.
- **Translation**: 

---

### Verse 18 (Ramayan 0.1158)
- **Original**: 1140 The Ramayana He with a laugh of joy and pride Displays his glittering pinions wide; And follows through the tangled dell The partner whom he loves so well. Ah happy bird! no giant's hate Has robbed him of his tender mate; And still beside his loved one he Dances beneath the shade in glee. Ah, in this month when flowers are fair My widowed woe is hard to bear. See, gentle love a home may find In creatures of inferior kind. See how the peahen turns to meet Her consort now with love-drawn feet.[321] So, LakshmaG, if my large-eyed dear, The child of Janak still were here, She, by love's thrilling influence led, Upon my breast would lay her head. These blooms I gathered from the bough Without my love are useless now. A thousand blossoms fair to see With passing glory clothe each tree That hangs its cluster-burthened head Now that the dewy months528 are fled, But, followed by the bees that ply Their fragrant task, they fall and die. A thousand birds in wild delight Their rapture-breathing notes unite; Bird calls to bird in joyous strain, And turns my love to frenzied pain. O, if beneath those alien skies, There be a spring where Sítá lies, 528 The Dewy Season is one of the six ancient seasons of the Indian year, lasting from the middle of January to the middle of March.
- **Translation**: 

---

### Verse 19 (Ramayan 0.1159)
- **Original**: Canto I. Ráma's Lament. 1141 I know my prisoned love must be Touched with like grief, and mourn with me. But ah, methinks that dreary clime Knows not the touch of spring's sweet time. How could my black eyed love sustain, Without her lord, so dire a pain? Or if the sweet spring come to her In distant lands a prisoner, How may his advent and her met On every side with taunt and threat? Ah, if the springtide's languor came With soft enchantment o'er my dame, My darling of the lotus eye, My gently speaking love, would die; For well my spirit knows that she Can never live bereft of me With love that never wavered yet My Sítá's heart, on me is set, Who, with a soul that ne'er can stray, With equal love her love repay. In vain, in vain the soft wind brings Sweet blossoms on his balmy wings; Delicious from his native snow, To me like fire he seems to glow. O, how I loved a breeze like this When darling Sítá shared the bliss! But now in vain for me it blows To fan the fury of my woes. That dark-winged bird that sought the skies Foretelling grief with warning cries, Sits on the tree where buds are gay, And pours glad music from the spray. That rover of the fields of air Will aid my love with friendly care,
- **Translation**: 

---

### Verse 20 (Ramayan 0.1160)
- **Original**: 1142 The Ramayana And me with gracious pity guide To my large-eyed Videhan's side.529 Hark, LakshmaG, how the woods around With love-inspiring chants resound, Where birds in every bloom-crowned tree Pour forth their amorous minstrelsy. As though an eager gallant wooed A gentle maid by love subdued, Enamoured of her flowers the bee Darts at the wind-rocked Tila tree.530 A [oka, brightest tree that grows, That lends a pang to lovers' woes, Hangs out his gorgeous bloom in scorn And mocks me as I weep forlorn. O Lakshma G, turn thine eye and see Each blossom-laden Mango tree, Like a young lover gaily dressed Whom fond desire forbids to rest. Look, son of Queen Sumitrá through The forest glades of varied hue, Where blooms are bright and grass is green The Kinnars531 with their loves are seen. See, brother, see where sweet and bright Those crimson lilies charm the sight, And o'er the flood a radiance throw Fair as the morning's roseate glow. See, Pampá, most divinely sweet, 529 Ráma appears to mean that on a former occasion a crow flying high over- head was an omen that indicated his approaching separation from Sítá; and that now the same bird's perching on a tree near him may be regarded as a happy augury that she will soon be restored to her husband. 530 A tree with beautiful and fragrant blossoms. 531 A race of semi-divine musicians attached to the service of Kuvera, repre- sented as centaurs reversed with human figures and horses' heads.
- **Translation**: 

---

