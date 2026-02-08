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

### Verse 1 (Ramayana 0.1086)
- **Original**: 1068 The Ramayana 'Tis vain behind yon bush to steal: Thy shimmering silks thy path reveal. Fly not, mine eyes pursue thy way; For pity's sake, dear Sítá, stay. Ah me, ah me, my words are vain; My gentle love is lost or slain. How could her tender bosom spurn Her husband on his home-return? Ah no, my love is surely dead, Fierce giants on her flesh have fed, Rending the soft limbs of their prey When I her lord was far away. That moon-bright face, that polished brow, Red lips, bright teeth— what are they now? Alas, my darling's shapely neck She loved with chains of gold to deck,— That neck that mocked the sandal scent, The ruthless fiends have grasped and rent. Alas, 'twas vain those arms to raise Soft as the young tree's tender sprays. Ah, dainty meal for giants' lips Were arms and quivering finger tips. Ah, she who counted many a friend Was left for fiends to seize and rend, Was left by me without defence From ravening giants' violence. O Lakshma G of the arm of might, Say, is my darling love in sight? O dearest Sítá. where art thou? Where is my darling consort now?” Thus as he cried in wild lament From grove to grove the mourner went, Here for a moment sank to rest,
- **Translation**: 

---

### Verse 2 (Ramayana 0.1087)
- **Original**: Canto LXII. Ráma's Lament. 1069 Then started up and onward pressed. Thus roaming on like one distraught Still for his vanished love he sought, He searched in wood and hill and glade, By rock and brook and wild cascade. Through groves with restless step he sped And left no spot unvisited. Through lawns and woods of vast extent Still searching for his love he went With eager steps and fast. For many a weary hour he toiled, Still in his fond endeavour foiled, Yet hoping to the last. Canto LXII. Ráma's Lament. When all the toil and search was vain He sought his leafy home again. 'Twas empty still: all scattered lay The seats of grass in disarray. He raised his shapely arms on high And spoke aloud with bitter cry: “Where is the Maithil dame?” he said, “O, whither has my darling fled? Who can have borne away my dame, Or feasted on her tender frame? If, Sítá hidden by some tree, Thou joyest still to mock at me, Cease, cease thy cruel sport, and take Compassion, or my heart will break. Bethink thee, love, the gentle fawns
- **Translation**: 

---

### Verse 3 (Ramayana 0.1088)
- **Original**: 1070 The Ramayana With whom thou playest on the lawns, Impatient for thy coming wait With streaming eyes disconsolate. Reft of my love, I needs must go Hence to the shades weighed down by woe. The king our sire will see me there, And cry,“O perjured Ráma, where, Where is thy faith, that thou canst speed From exile ere the time decreed?” Ah Sítá, whither hast thou fled And left me here disquieted, A hapless mourner, reft of hope, Too feeble with my woe to cope? E'en thus indignant Glory flies The wretch who stains his soul with lies. If thou, my love, art lost to view, I in my woe must perish too.” Thus Ráma by his grief distraught Wept for the wife he vainly sought, And Lakshma G whose fraternal breast Longed for his weal, the chief addressed[302] Whose soul gave way beneath the pain When all his eager search was vain, Like some great elephant who stands Sinking upon the treacherous sands: “Not yet, O wisest chief, despair; Renew thy toil with utmost care. This noble hill where trees are green Has many a cave and dark ravine. The Maithil lady day by day Delighted in the woods to stray, Deep in the grove she wanders still,
- **Translation**: 

---

### Verse 4 (Ramayana 0.1089)
- **Original**: Canto LXII. Ráma's Lament. 1071 Or walks by blossom-covered rill, Or fish-loved river stealing through Tall clusters of the dark bamboo. Or else the dame with arch design To prove thy mood, O Prince, and mine, Far in some sheltering thicket lies To frighten ere she meet our eyes. Then come, renew thy labour, trace The lady to her lurking-place, And search the wood from side to side To know where Sítá loves to bide. Collect thy thoughts, O royal chief, Nor yield to unavailing grief.” Thus LakshmaG, by attention stirred, To fresh attempts his brother spurred, And Ráma, as he ceased, began With LakshmaG's aid each spot to scan. In eager search their way they took Through wood, o'er hill, by pool and brook, They roamed each mount, nor spared to seek On ridge and crag and towering peak. They sought the dame in every spot; But all in vain; they found her not. Above, below, on every side They ranged the hill, and Ráma cried, “O Lakshma G, O my brother still No trace of Sítá on the hill!” Then LakshmaG as he roamed the wood Beside his glorious brother stood, And while fierce grief his bosom burned This answer to the chief returned: “Thou, Ráma, after toil and pain Wilt meet the Maithil dame again,
- **Translation**: 

---

### Verse 5 (Ramayana 0.1090)
- **Original**: 1072 The Ramayana As VishGu, Bali's might subdued, His empire of the earth renewed.”508 Then Ráma cried in mournful tone, His spirit by his woe o'erthrown; “The wood is searched from side to side, No distant spot remains untried, No lilied pool, no streamlet where The lotus buds are fresh and fair. Our eyes have searched the hill with all His caves and every waterfall,— But ah, not yet I find my wife, More precious than the breath of life.” As thus he mourned his vanished dame A mighty trembling seized his frame, And by o'erpowering grief assailed, His troubled senses reeled and failed. Too great to bear his misery grew, And many a long hot sigh he drew, Then as he wept and sobbed and sighed, “O Sítá, O my love!” he cried. Then LakshmaG, joining palm to palm, Tried every art his woe to calm. But Ráma in his anguish heard Or heeded not one soothing word, Still for his spouse he mourned, and shrill Rang out his lamentation still. 508 See Book I Canto XXXI.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1091)
- **Original**: Canto LXIII. Ráma's Lament. 1073 Canto LXIII. Ráma's Lament. Thus for his wife in vain he sought: Then, his sad soul with pain distraught, The hero of the lotus eyes Filled all the air with frantic cries. O'erpowered by love's strong influence, he His absent wife still seemed to see, And thus with accents weak and faint Renewed with tears his wild complaint: “Thou, fairer than their bloom, my spouse, Art hidden by A[oka boughs. Those blooms have power to banish care, But now they drive me to despair. Thine arms are like the plantain's stem: Why let the plantain cover them? Thou art not hidden, love; thy feet Betray thee in thy dark retreat. Thou runnest in thy girlish sport To flowery trees, thy dear resort. But cease, O cease, my love, I pray, To vex me with thy cruel play. Such mockery in a holy spot Where hermits dwell beseems thee not. Ah, now I see thy fickle mind To scornful mood too much inclined, Come, large-eyed beauty, I implore; Lone is the cot so dear before.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1092)
- **Original**: 1074 The Ramayana No, she is slain by giants; they Have stolen or devoured their prey, Or surely at my mournful cry My darling to her lord would fly. O Lakshma G, see those troops of deer: In each sad eye there gleams a tear. Those looks of woe too clearly say My consort is the giants' prey. O noblest, fairest of the fair, Where art thou, best of women, where? This day will dark Kaikeyí find Fresh triumph for her evil mind, When I, who with my Sítá came Return alone, without my dame. But ne'er can I return to see Those chambers where my queen should be And hear the scornful people speak[303] Of Ráma as a coward weak. For mine will be the coward's shame Who let the foeman steal his dame. How can I seek my home, or brook Upon Videha's king to look? How listen, when he bids me tell, My wanderings o'er, that all is well? He, when I meet his eager view, Will mark that Sítá comes not too, And when he hears the mournful tale His wildered sense will reel and fail. “O Da [aratha” will he cry, “Blest in thy mansion in the sky!” Ne'er to that town my steps shall bend, That town which Bharat's arms defend, For e'en the blessed homes above Would seem a waste without my love.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1093)
- **Original**: Canto LXIV. Ráma's Lament. 1075 Leave me, my brother, here, I pray; To fair Ayodhyá bend thy way. Without my love I cannot bear To live one hour in blank despair. Round Bharat's neck thy fond arms twine, And greet him with these words of mine: “Dear brother, still the power retain, And o'er the land as monarch reign.” With salutation next incline Before thy mother, his, and mine. Still, brother, to my words attend, And with all care each dame befriend. To my dear mother's ear relate My mournful tale and Sítá's fate.” Thus Ráma gave his sorrow vent, And from a heart which anguish rent, Mourned for his wife in loud lament,— Her of the glorious hair, From LakshmaG's cheek the colour fled, And o'er his heart came sudden dread, Sick, faint, and sore disquieted By woe too great to bear. Canto LXIV. Ráma's Lament. Reft of his love, the royal chief, Weighed down beneath his whelming grief, Desponding made his brother share His grievous burden of despair. Over his sinking bosom rolled The flood of sorrow uncontrolled.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1094)
- **Original**: 1076 The Ramayana And as he wept and sighed, In mournful accents faint and slow With words congenial to his woe, To LakshmaG thus he cried: “Brother, I ween, beneath the sun, Of all mankind there lives not one So full of sin, whose hand has done Such cursed deeds as mine. For my sad heart with misery bleeds, As, guerdon of those evil deeds, Still greater woe to woe succeeds In never-ending line. A life of sin I freely chose, And from my past transgression flows A ceaseless flood of bitter woes My folly to repay. The fruit of sin has ripened fast, Through many a sorrow have I passed, And now the crowning grief at last Falls on my head to-day. From all my faithful friends I fled, My sire is numbered with the dead, My royal rank is forfeited, My mother far away. These woes on which I sadly think Fill, till it raves above the brink, The stream of grief in which I sink,— The flood which naught can stay. Ne'er, brother, ne'er have I complained; Though long by toil and trouble pained, Without a murmur I sustained The woes of woodland life. But fiercer than the flames that rise
- **Translation**: 

---

### Verse 10 (Ramayana 0.1095)
- **Original**: Canto LXIV. Ráma's Lament. 1077 When crackling wood the food supplies,— Flashing a glow through evening skies,— This sorrow for my wife. Some cruel fiend has seized the prey And torn my trembling love away, While, as he bore her through the skies, She shrieked aloud with frantic cries, In tones of fear which, wild and shrill, Retained their native sweetness still. Ah me, that breast so soft and sweet, For sandal's precious perfume meet, Now all detained with dust and gore, Shall meet my fond caress no more. That face, whose lips with tones so clear Made pleasant music, sweet to hear,— With soft locks plaited o'er the brow,— Some giant's hand is on it now. It smiles not, as the dear light fails When Ráhu's jaw the moon assails. Ah, my true love! that shapely neck She loved with fairest chains to deck, The cruel demons rend, and drain The lifeblood from each mangled vein. Ah, when the savage monsters came And dragged away the helpless dame, The lady of the long soft eye Called like a lamb with piteous cry. Beneath this rock, O LakshmaG, see, My peerless consort sat with me, And gently talked to thee the while, Her sweet lips opening with a smile. Here is that fairest stream which she Loved ever, bright Godávarí. Ne'er can the dame have passed this way:
- **Translation**: 

---

### Verse 11 (Ramayana 0.1096)
- **Original**: 1078 The Ramayana So far alone she would not stray, Nor has my darling, lotus-eyed, Sought lilies by the river's side, For without me she ne'er would go[304] To streamlets where the wild flowers grow, Tell me not, brother, she has strayed To the dark forest's distant shade Where blooming boughs are gay and sweet, And bright birds love the cool retreat. Alone my love would never dare,— My timid love,— to wander there. O Lord of Day whose eye sees all We act and plan, on thee I call: For naught is hidden from thy sight,— Great witness thou of wrong and right. Where is she, lost or torn away? Dispel my torturing doubt and say. And O thou Wind who blowest free, The worlds have naught concealed from thee. List to my prayer, reveal one trace Of her, the glory of her race. Say, is she stolen hence, or dead, Or do her feet the forest tread?” Thus with disordered senses, faint With woe he poured his sad complaint, And then, a better way to teach, Wise LakshmaG spoke in seemly speech: “Up, brother dear, thy grief subdue, With heart and soul thy search renew. When woes oppress and dangers threat Brave effort ne'er was fruitless yet.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.1097)
- **Original**: Canto LXV. Ráma's Wrath. 1079 He spoke, but Ráma gave no heed To valiant LakshmaG's prudent rede. With double force the flood of pain Rushed o'er his yielding soul again. Canto LXV. Ráma's Wrath. With piteous voice, by woe subdued, Thus Raghu's son his speech renewed: “Thy steps, my brother, quickly turn To bright Godávarí and learn If Sítá to the stream have hied To cull the lilies on its side.” Obedient to the words he said, His brother to the river sped. The shelving banks he searched in vain, And then to Ráma turned again. “I searched, but found her not,” he cried; “I called aloud, but none replied. Where can the Maithil lady stray, Whose sight would chase our cares away? I know not where, her steps untraced, Roams Sítá of the dainty waist.”
- **Translation**: 

---

### Verse 13 (Ramayana 0.1098)
- **Original**: 1080 The Ramayana When Ráma heard the words he spoke Again he sank beneath the stroke, And with a bosom anguish-fraught Himself the lovely river sought. There standing on the shelving side, “O Sítá, where art thou?” he cried. No spirit voice an answer gave, No murmur from the trembling wave Of sweet Godávarí declared The outrage which the fiend had dared. “O speak!” the pitying spirits cried, But yet the stream their prayer denied, Nor dared she, coldly mute, relate To the sad chief his darling's fate Of RávaG's awful form she thought, And the dire deed his arm had wrought, And still withheld by fear dismayed, The tale for which the mourner prayed. When hope was none, his heart to cheer, That the bright stream his cry would hear While sorrow for his darling tore His longing soul he spake once more: “Though I have sought with tears and sighs Godárvarí no word replies, O say, what answer can I frame To Janak, father of my dame? Or how before her mother stand Leading no Sítá by the hand? Where is my loyal love who went Forth with her lord to banishment? Her faith to me she nobly held Though from my realm and home expelled,— A hermit, nursed on woodland fare,— She followed still and soothed my care.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1099)
- **Original**: Canto LXV. Ráma's Wrath. 1081 Of all my friends am I bereft, Nor is my faithful consort left. How slowly will the long nights creep While comfortless I wake and weep! O, if my wife may yet be found, With humble love I'll wander round This Janasthán, Pra[ravaG's hill, Mandákiní's delightful rill. See how the deer with gentle eyes Look on my face and sympathize. I mark their soft expression: each Would soothe me, if it could, with speech.” A while the anxious throng he eyed. And “Where is Sítá, where?” he cried. Thus while hot tears his utterance broke The mourning son of Raghu spoke. The deer in pity for his woes Obeyed the summons and arose. Upon his right thy stood, and raised Their sad eyes up to heaven and gazed Each to that quarter bent her look Which RávaG with his captive took. Then Raghu's son again they viewed, And toward that point their way pursued. Then LakshmaG watched their looks intent As moaning on their way they went, And marked each sign which struck his sense With mute expressive influence, Then as again his sorrow woke Thus to his brother chief he spoke: “Those deer thy eager question heard [305]
- **Translation**: 

---

### Verse 15 (Ramayana 0.1100)
- **Original**: 1082 The Ramayana And rose at once by pity stirred: See, in thy search their aid they lend, See, to the south their looks they bend. Arise, dear brother, let us go The way their eager glances show, If haply sign or trace descried Our footsteps in the search may guide.” The son of Raghu gave assent, And quickly to the south they went; With eager eyes the earth he scanned, And Lakshma G followed close at hand. As each to other spake his thought, And round with anxious glances sought, Scattered before them in the way, Blooms of a fallen garland lay. When Ráma saw that flowery rain He spoke once more with bitterest pain: “O Lakshma G every flower that lies Here on the ground I recognize. I culled them in the grove, and there My darling twined them in her hair. The sun, the earth, the genial breeze Have spared these flowers my soul to please.” Then to that woody hill he prayed, Whence flashed afar each wild cascade: “O best of mountains, hast thou seen A dame of perfect form and mien In some sweet spot with trees o'ergrown,— My darling whom I left alone?” Then as a lion threats a deer He thundered with a voice of fear: “Reveal her, mountain, to my view
- **Translation**: 

---

### Verse 16 (Ramayana 0.1101)
- **Original**: Canto LXV. Ráma's Wrath. 1083 With golden limbs and golden hue. Where is my darling Sítá? speak Before I rend thee peak from peak.” The mountain seemed her track to show, But told not all he sought to know. Then Da[aratha's son renewed His summons as the mount he viewed: “Soon as my flaming arrows fly, Consumed to ashes shall thou lie Without a herb or bud or tree, And birds no more shall dwell in thee. And if this stream my prayer deny, My wrath this day her flood shall dry, Because she lends no aid to trace My darling of the lotus face.” Thus Ráma spake as though his ire Would scorch them with his glance of fire; Then searching farther on the ground The footprint of a fiend he found, And small light traces here and there, Where Sítá in her great despair, Shrieking for Ráma's help, had fled Before the giant's mighty tread. His careful eye each trace surveyed Which Sítá and the fiend had made,— The quivers and the broken bow And ruined chariot of the foe,— And told, distraught by fear and grief, His tidings to his brother chief: “O Lakshma G, here,” he cried“behold My Sítá's earrings dropped with gold. Here lie her garlands torn and rent,
- **Translation**: 

---

### Verse 17 (Ramayana 0.1102)
- **Original**: 1084 The Ramayana Here lies each glittering ornament. O look, the ground on every side With blood-like drops of gold is dyed. The fiends who wear each strange disguise Have seized, I ween, the helpless prize. My lady, by their hands o'erpowered, Is slaughtered, mangled, and devoured. Methinks two fearful giants came And waged fierce battle for the dame. Whose, LakshmaG, was this mighty bow With pearls and gems in glittering row? Cast to the ground the fragments lie, And still their glory charms the eye. A bow so mighty sure was planned For heavenly God or giant's hand. Whose was this coat of golden mail Which, though its lustre now is pale, Shone like the sun of morning, bright With studs of glittering lazulite? Whose, LakshmaG, was this bloom-wreathed shade With all its hundred ribs displayed? This screen, most meet for royal brow, With broken staff lies useless now. And these tall asses, goblin-faced, With plates of golden harness graced, Whose hideous forms are stained with gore Who is the lord whose yoke they bore? Whose was this pierced and broken car That shoots a flame-like blaze afar? Whose these spent shafts at random spread, Each fearful with its iron head,— With golden mountings fair to see, Long as a chariot's axle-tree? These quivers see, which, rent in twain,
- **Translation**: 

---

### Verse 18 (Ramayana 0.1103)
- **Original**: Canto LXV. Ráma's Wrath. 1085 Their sheaves of arrows still contain. Whose was this driver? Dead and cold, His hands the whip and reins still hold. See, LakshmaG, here the foot I trace Of man, nay, one of giant race. The hatred that I nursed of old Grows mightier now a hundred fold Against these giants, fierce of heart, Who change their forms by magic art. Slain, eaten by the giant press, Or stolen is the votaress, Nor could her virtue bring defence To Sítá seized and hurried hence. O, if my love be slain or lost All hope of bliss for me is crossed. The power of all the worlds were vain To bring one joy to soothe my pain. The spirits with their blinded eyes Would look in wonder, and despise The Lord who made the worlds, the great Creator when compassionate. And so, I ween, the Immortals turn Cold eyes upon me now, and spurn [306] The weakling prompt at pity's call, Devoted to the good of all. But from this day behold me changed, From every gentle grace estranged. Now be it mine all life to slay, And sweep these cursed fiends away. As the great sun leaps up the sky, And the cold moonbeams fade and die, So vengeance rises in my breast, One passion conquering all the rest. Gandharvas in their radiant place,
- **Translation**: 

---

### Verse 19 (Ramayana 0.1104)
- **Original**: 1086 The Ramayana The Yakshas, and the giant race, Kinnars and men shall look in vain For joy they ne'er shall see again. The anguish of my great despair, O Lakshma G, fills the heaven and air; And I in wrath all life will slay Within the triple world to-day. Unless the Gods in heaven who dwell Restore my Sítá safe and well, I armed with all the fires of Fate, The triple world will devastate. The troubled stars from heaven shall fall, The moon be wrapped in gloomy pall, The fire be quenched, the wind be stilled, The radiant sun grow dark and chilled; Crushed every mountain's towering pride, And every lake and river dried, Dead every creeper, plant, and tree, And lost for aye the mighty sea. Thou shalt the world this day behold In wild disorder uncontrolled, With dying life which naught defends From the fierce storm my bowstring sends. My shafts this day, for Sítá's sake, The life of every fiend shall take. The Gods this day shall see the force That wings my arrows on their course, And mark how far that course is held, By my unsparing wrath impelled. No God, not one of Daitya strain, Goblin or Rákshas shall remain. My wrath shall end the worlds, and all Demons and Gods therewith shall fall. Each world which Gods, the Dánav race,
- **Translation**: 

---

### Verse 20 (Ramayana 0.1105)
- **Original**: Canto LXV. Ráma's Wrath. 1087 And giants make their dwelling place, Shall fall beneath my arrows sent In fury when my bow is bent. The arrows loosened from my string Confusion on the worlds shall bring. For she is lost or breathes no more, Nor will the Gods my love restore. Hence all on earth with life and breath This day I dedicate to death. All, till my darling they reveal, The fury of my shafts shall feel.” Thus as he spake by rage impelled, Red grew his eyes, his fierce lips swelled. His bark coat round his form he drew And coiled his hermit braids anew, Like Rudra when he yearned to slay The demon Tripur509 in the fray. So looked the hero brave and wise, The fury flashing from his eyes. Then Ráma, conqueror of the foe, From LakshmaG's hand received his bow, Strained the great string, and laid thereon A deadly dart that flashed and shone, And spake these words as fierce in ire As He who ends the worlds with fire: 509 An Asur or demon, king of Tripura, the modern Tipperah.
- **Translation**: 

---

