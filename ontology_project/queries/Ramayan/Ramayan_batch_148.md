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

### Verse 1 (Ramayana 0.986)
- **Original**: 968 The Ramayana “By Ráma's might, and his alone, Can this great fiend be overthrown. I know in days of yore the Blest Thy saving help in fight confessed. Still of thy famous deeds they tell In heaven above, in earth, and hell, A mighty host obeys thy hest: Here let it still, I pray thee, rest. Thy glorious son, though yet a boy, Will in the fight that fiend destroy. Ráma alone with me shall go: Be happy, victor of the foe.” He spoke: the monarch gave assent, And Ráma to the hermit lent. So to his woodland home in joy Went Vi[vámitra with the boy. With ready bow the champion stood To guard the rites in DaG ak wood. With glorious eyes, most bright to view, Beardless as yet and dark of hue; A single robe his only wear, His temples veiled with waving hair,[274] Around his neck a chain of gold, He grasped the bow he loved to hold; And the young hero's presence made A glory in the forest shade. Thus Ráma with his beauteous mien, Like the young rising moon was seen, I, like a cloud which tempest brings, My arms adorned with golden rings, Proud of the boon which lent me might, Approached where dwelt the anchorite. But Ráma saw me venturing nigh,
- **Translation**: 

---

### Verse 2 (Ramayana 0.987)
- **Original**: Canto XXXVIII. Márícha's Speech. 969 Raising my murderous axe on high; He saw, and fearless of the foe, Strung with calm hand his trusty bow. By pride of conscious strength beguiled, I scorned him as a feeble child, And rushed with an impetuous bound On Vi[vámitra's holy ground. A keen swift shaft he pointed well, The foeman's rage to check and quell, And hurled a hundred leagues away Deep in the ocean waves I lay. He would not kill, but, nobly brave, My forfeit life he chose to save. So there I lay with wandering sense Dazed by that arrow's violence. Long in the sea I lay: at length Slowly returned my sense and strength, And rising from my watery bed To Lanká's town again I sped. Thus was I spared, but all my band Fell slain by Ráma's conquering hand,— A boy, untrained in warrior's skill, Of iron arm and dauntless will. If thou with Ráma still, in spite Of warning and of prayer, wilt fight, I see terrific woes impend, And dire defeat thy days will end. Thy giants all will feel the blow And share the fatal overthrow, Who love the taste of joy and play, The banquet and the festal day. Thine eyes will see destruction take Thy Lanká, lost for Sítá's sake, And stately pile and palace fall
- **Translation**: 

---

### Verse 3 (Ramayana 0.988)
- **Original**: 970 The Ramayana With terrace, dome, and jewelled wall. The good will die: the crime of kings Destruction on the people brings: The sinless die, as in the lake The fish must perish with the snake. The prostrate giants thou wilt see Slain for this folly wrought by thee, Their bodies bright with precious scent And sheen of heavenly ornament; Or see the remnant of thy train Seek refuge far, when help is vain And with their wives, or widowed, fly To every quarter of the sky; Thy mournful eyes, where'er they turn, Will see thy stately city burn, When royal homes with fire are red, And arrowy nets around are spread. A sin that tops all sins in shame Is outrage to another's dame, A thousand wives thy palace fill, And countless beauties wait thy will. O rest contented with thine own, Nor let thy race be overthrown. If thou, O King, hast still delight In rank and wealth and power and might, In noble wives, in troops of friends, In all that royal state attends, I warn thee, cast not all away, Nor challenge Ráma to the fray. If deaf to every friendly prayer, Thou still wilt seek the strife, And from the side of Ráma tear His lovely Maithil wife, Soon will thy life and empire end
- **Translation**: 

---

### Verse 4 (Ramayana 0.989)
- **Original**: Canto XXXIX. Márícha's Speech. 971 Destroyed by Ráma's bow, And thou, with kith and kin and friend, To Yáma's realm must go.” Canto XXXIX. Márícha's Speech. “I told thee of that dreadful day When Ráma smote and spared to slay. Now hear me, RávaG, while I tell What in the after time befell. At length, restored to strength and pride, I and two mighty fiends beside Assumed the forms of deer and strayed Through DaG ak wood in lawn and glade, I reared terrific horns: beneath Were flaming tongue and pointed teeth. I roamed where'er my fancy led, And on the flesh of hermits fed, In sacred haunt, by hallowed tree, Where'er the ritual fires might be. A fearful shape, I wandered through The wood, and many a hermit slew. With ruthless rage the saints I killed Who in the grove their tasks fulfilled. When smitten to the earth they sank, Their flesh I ate, their blood I drank, And with my cruel deeds dismayed All dwellers in the forest shade, Spoiling their rites in bitter hate, With human blood inebriate. Once in the wood I chanced to see
- **Translation**: 

---

### Verse 5 (Ramayana 0.990)
- **Original**: 972 The Ramayana Ráma again, a devotee, A hermit, fed on scanty fare, Who made the good of all his care. His noble wife was by his side, And Lakshma G in the battle tried. In senseless pride I scorned the might Of that illustrious anchorite, And heedless of a hermit foe, Recalled my earlier overthrow.[275] I charged him in my rage and scorn To slay him with my pointed horn, In heedless haste, to fury wrought As on my former wounds I thought. Then from the mighty bow he drew Three foe-destroying arrows flew, Keen-pointed, leaping from the string, Swift as the wind or feathered king. Dire shafts, on flesh of foemen fed, Like rushing thunderbolts they sped, With knots well smoothed and barbs well bent, Shot e'en as one, the arrows went. But I who Ráma's might had felt, And knew the blows the hero dealt, Escaped by rapid flight. The two Who lingered on the spot, he slew. I fled from mortal danger, freed From the dire shaft by timely speed. Now to deep thought my days I give, And as a humble hermit live. In every shrub, in every tree I view that noblest devotee. In every knotted trunk I mark His deerskin and his coat of bark, And see the bow-armed Ráma stand
- **Translation**: 

---

### Verse 6 (Ramayana 0.991)
- **Original**: Canto XXXIX. Márícha's Speech. 973 Like Yáma with his noose in hand. I tell thee RávaG, in my fright A thousand Rámas mock my sight, This wood with every bush and bough Seems all one fearful Ráma now. Throughout the grove there is no spot So lonely where I see him not. He haunts me in my dreams by night, And wakes me with the wild affright. The letter that begins his name Sends terror through my startled frame. The rapid cars whereon we ride, The rich rare jewels, once my pride, Have names493 that strike upon mine ear With hated sound that counsels fear. His mighty strength too well I know, Nor art thou match for such a foe. Too strong were Raghus's son in fight For Namuchi or Bali's might. Then Ráma to the battle dare, Or else be patient and forbear; But, wouldst thou see me live in peace, Let mention of the hero cease. The good whose holy lives were spent In deepest thought, most innocent, With all their people many a time Have perished through another's crime. So in the common ruin, I Must for another's folly die, Do all thy strength and courage can, But ne'er will I approve the plan. For he, in might supremely great, 493 The Sanskrit words for car and jewels begin withra.
- **Translation**: 

---

### Verse 7 (Ramayana 0.992)
- **Original**: 974 The Ramayana The giant world could extirpate, Since, when impetuous Khara sought The grove of Janasthán and fought For ZúrpaGakhá's sake, he died By Ráma's hand in battle tried. How has he wronged thee? Soothly swear, And Ráma's fault and sin declare. I warn thee, and my words are wise, I seek thy people's weal: But if this rede thou wilt despise, Nor hear my last appeal, Thou with thy kin and all thy friends In fight this day wilt die, When his great bow the hero bends, And shafts unerring fly.” Canto XL. Rávan's Speech. But RávaG scorned the rede he gave In timely words to warn and save, E'en as the wretch who hates to live Rejects the herb the leeches give. By fate to sin and ruin spurred, That sage advice the giant heard, Then in reproaches hard and stern Thus to Márícha spoke in turn:
- **Translation**: 

---

### Verse 8 (Ramayana 0.993)
- **Original**: Canto XL. Rávan's Speech. 975 “Is this thy counsel, weak and base, Unworthy of thy giant race? Thy speech is fruitless, vain, thy toil Like casting seed on barren soil. No words of thine shall drive me back From Ráma and the swift attack. A fool is he, inured to sin, And more, of human origin. The craven, at a woman's call To leave his sire, his mother, all The friends he loved, the power and sway, And hasten to the woods away! But now his anger will I rouse, Stealing away his darling spouse. I in thy sight will ravish her From Khara's cruel murderer. Upon this plan my soul is bent, And naught shall move my firm intent, Not if the way through demons led And Gods with Indra at their head. 'Tis thine, when questioned, to explain The hope and fear, the loss and gain, And, when thy king thy thoughts would know, The triumph or the danger show. A prudent counsellor should wait, And speak when ordered in debate, With hands uplifted, calm and meek, If honour and reward he seek. Or, when some prudent course he sees Which, spoken, may his king displease [276] He should by hints of dexterous art His counsel to his lord impart. But prudent words are said in vain When the blunt speech brings grief and pain.
- **Translation**: 

---

### Verse 9 (Ramayana 0.994)
- **Original**: 976 The Ramayana A high-souled king will scarcely thank The man who shames his royal rank. Five are the shapes that kings assume, Of majesty, of grace, and gloom: Like Indra now, or Agni, now Like the dear Moon, with placid brow: Like mighty VaruG now they show, Now fierce as He who rules below. O giant, monarchs lofty-souled Are kind and gentle, stern and bold, With gracious love their gifts dispense And swiftly punish each offence. Thus subjects should their rulers view With all respect and honour due. But folly leads thy heart to slight Thy monarch and neglect his right. Thou hast in lawless pride addressed With bitter words thy royal guest. I asked thee not my strength to scan, Or loss and profit in the plan. I only spoke to tell the deed O mighty one, by me decreed, And bid thee in the peril lend Thy succour to support thy friend. Hear me again, and I will tell How thou canst aid my venture well. In semblance of a golden deer Adorned with silver drops, appear: And near the cottage in the way Of Ráma and his consort stray. Draw nigh, and wandering through the brake With thy strange form her fancy take. The Maithil dame with wondering eyes Will took upon thy fair disguise,
- **Translation**: 

---

### Verse 10 (Ramayana 0.995)
- **Original**: Canto XL. Rávan's Speech. 977 And quickly bid her husband go And bring the deer that charms her so, When Raghu's son has left the place, Still pressing onward in the chase, Cry out,“O Lakshma G! Ah, mine own!” With voice resembling Ráma's tone. When Lakshma G hears his brother's cry, Impelled by Sítá he will fly, Restless with eager love, to aid The hunter in the distant shade. When both her guards have left her side, Even as Indra, thousand-eyed, ClaspsZachí, will I bear away The Maithil dame an easy prey. When thou, my friend, this aid hast lent, Go where thou wilt and live content. True servant, faithful to thy vow, With half my realm I thee endow. Go forth, may luck thy way attend That leads thee to the happy end. I in my car will quickly be In DaG ak wood, and follow thee. So will I cheat this Ráma's eyes And win without a blow the prize; And safe return to Lanká's town With thee, my friend, this day shall crown. But if thou wilt not aid my will, My hand this day thy blood shall spill. Yea, thou must share the destined task, For force will take the help I ask. No bliss that rebel's life attends Whose stubborn will his lord offends. Thy life, if thou the task assay, In jeopardy may stand;
- **Translation**: 

---

### Verse 11 (Ramayana 0.996)
- **Original**: 978 The Ramayana Oppose me, and this very day Thou diest by this hand. Now ponder all that thou hast heard Within thy prudent breast: Reflect with care on every word, And do what seems the best.” Canto XLI. Márícha's Reply. Against his judgment sorely pressed By his imperious lord's behest, Márícha threats of death defied And thus with bitter words replied: “Ah, who, my King, with sinful thought This wild and wicked counsel taught, By which destruction soon will fall On thee, thy sons, thy realm and all? Who is the guilty wretch who sees With envious eye thy blissful ease, And by this plan, so falsely shown, Death's gate for thee has open thrown? With souls impelled by mean desire Thy foes against thy life conspire. They urge thee to destruction's brink, And gladly would they see thee sink. Who with base thought to work thee woe This fatal road has dared to show, And, triumph in his wicked eye, Would see thee enter in and die? To all thy counsellors, untrue, The punishment of death is due,
- **Translation**: 

---

### Verse 12 (Ramayana 0.997)
- **Original**: Canto XLI. Márícha's Reply. 979 Who see thee tempt the dangerous way, Nor strain each nerve thy foot to stay. Wise lords, whose king, by passion led, The path of sin begins to tread, Restrain him while there yet is time: But thine,— they see nor heed the crime. These by their master's will obtain Merit and fame and joy and gain. 'Tis only by their master's grace That servants hold their lofty place. But when the monarch stoops to sin They lose each joy they strive to win, And all the people people high and low Fall in the common overthrow. [277] Merit and fame and honour spring, Best of the mighty, from the king. So all should strive with heart and will To keep the king from every ill. Pride, violence, and sullen hate Will ne'er maintain a monarch's state, And those who cruel deeds advise Must perish when their master dies, Like drivers with their cars o'erthrown In places rough with root and stone. The good whose holy lives were spent On duty's highest laws intent, With wives and children many a time Have perished for another's crime. Hapless are they whose sovereign lord, Opposed to all, by all abhorred, Is cruel-hearted, harsh, severe: Thus might a jackal tend the deer. Now all the giant race await, Destroyed by thee, a speedy fate,
- **Translation**: 

---

### Verse 13 (Ramayana 0.998)
- **Original**: 980 The Ramayana Ruled by a king so cruel-souled, Foolish in heart and uncontrolled. Think not I fear the sudden blow That threatens now to lay me low: I mourn the ruin that I see Impending o'er thy host and thee. Me first perchance will Ráma kill, But soon his hand thy blood will spill. I die, and if by Ráma slain And not by thee, I count it gain. Soon as the hero's face I see His angry eyes will murder me, And if on her thy hands thou lay Thy friends and thou are dead this day. If with my help thou still must dare The lady from her lord to tear, Farewell to all our days are o'er, Lanká and giants are no more. In vain, in vain, an earnest friend, I warn thee, King, and pray. Thou wilt not to my prayers attend, Or heed the words I say So men, when life is fleeting fast And death's sad hour is nigh, Heedless and blinded to the last Reject advice and die.” Canto XLII. Márícha Transformed.
- **Translation**: 

---

### Verse 14 (Ramayana 0.999)
- **Original**: Canto XLII. Márícha Transformed. 981 Márícha thus in wild unrest With bitter words the king addressed. Then to his giant lord in dread, “Arise, and let us go,” he said. “Ah, I have met that mighty lord Armed with his shafts and bow and sword, And if again that bow he bend Our lives that very hour will end. For none that warrior can provoke And think to fly his deadly stroke. Like Yáma with his staff is he, And his dread hand will slaughter thee. What can I more? My words can find No passage to thy stubborn mind. I go, great King, thy task to share, And may success attend thee there.” With that reply and bold consent The giant king was well content. He strained Márícha to his breast And thus with joyful words addressed: “There spoke a hero dauntless still, Obedient to his master's will, Márícha's proper self once more: Some other took thy shape before. Come, mount my jewelled car that flies. Will-governed, through the yielding skies. These asses, goblin-faced, shall bear Us quickly through the fields of air. Attract the lady with thy shape, Then through the wood, at will, escape. And I, when she has no defence, Will seize the dame and bear her thence.”
- **Translation**: 

---

### Verse 15 (Ramayana 0.1000)
- **Original**: 982 The Ramayana Again Márícha made reply, Consent and will to signify. With rapid speed the giants two From the calm hermit dwelling flew, Borne in that wondrous chariot, meet For some great God's celestial seat. They from their airy path looked down On many a wood and many a town, On lake and river, brook and rill, City and realm and towering hill. Soon he whom giant hosts obeyed, Márícha by his side, surveyed The dark expanse of DaG ak wood Where Ráma's hermit cottage stood. They left the flying car, whereon The wealth of gold and jewels shone, And thus the giant king addressed Márícha as his hand he pressed: “Márícha, look! before our eyes Round Ráma's home the plantains rise. His hermitage is now in view: Quick to the work we came to do!” Thus RávaG spoke, Márícha heard Obedient to his master's word, Threw off his giant shape and near The cottage strayed a beauteous deer. With magic power, by rapid change, His borrowed form was fair and strange. A sapphire tipped each horn with light; His face was black relieved with white. The turkis and the ruby shed A glory from his ears and head.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1001)
- **Original**: Canto XLII. Márícha Transformed. 983 His arching neck was proudly raised, And lazulites beneath it blazed. With roseate bloom his flanks were dyed, And lotus tints adorned his hide. His shape was fair, compact, and slight; [278] His hoofs were carven lazulite. His tail with every changing glow Displayed the hues of Indra's bow. With glossy skin so strangely flecked, With tints of every gem bedecked. A light o'er Ráma's home he sent, And through the wood, where'er he went. The giant clad in that strange dress That took the soul with loveliness, To charm the fair Videhan's eyes With mingled wealth of mineral dyes, Moved onward, cropping in his way, The grass and grain and tender spray. His coat with drops of silver bright, A form to gaze on with delight, He raised his fair neck as he went To browse on bud and filament. Now in the Cassia grove he strayed, Now by the cot in plantains' shade. Slowly and slowly on he came To catch the glances of the dame, And the tall deer of splendid hue Shone full at length in Sítá's view. He roamed where'er his fancy chose Where Ráma's leafy cottage rose. Now near, now far, in careless ease, He came and went among the trees. Now with light feet he turned to fly, Now, reassured, again drew nigh:
- **Translation**: 

---

### Verse 17 (Ramayana 0.1002)
- **Original**: 984 The Ramayana Now gambolled close with leap and bound, Now lay upon the grassy ground: Now sought the door, devoid of fear, And mingled with the troop of deer; Led them a little way, and thence Again returned with confidence. Now flying far, now turning back Emboldened on his former track, Seeking to win the lady's glance He wandered through the green expanse. Then thronging round, the woodland deer Gazed on his form with wondering fear; A while they followed where he led, Then snuffed the tainted gale and fled. The giant, though he longed to slay The startled quarry, spared the prey, And mindful of the shape he wore To veil his nature, still forbore. Then Sítá of the glorious eye, Returning from her task drew nigh; For she had sought the wood to bring Each loveliest flower of early spring. Now would the bright-eyed lady choose Some gorgeous bud with blending hues, Now plucked the mango's spray, and now The bloom from an A[oka bough. She with her beauteous form, unmeet For woodland life and lone retreat, That wondrous dappled deer beheld Gemmed with rich pearls, unparalleled, His silver hair the lady saw, His radiant teeth and lips and jaw, And gazed with rapture as her eyes Expanded in their glad surprise.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1003)
- **Original**: Canto XLIII. The Wondrous Deer. 985 And when the false deer's glances fell On her whom Ráma loved so well, He wandered here and there, and cast A luminous beauty as he passed; And Janak's child with strange delight Kept gazing on the unwonted sight. Canto XLIII. The Wondrous Deer. She stooped, her hands with flowers to fill, But gazed upon the marvel still: Gazed on its back and sparkling side Where silver hues with golden vied. Joyous was she of faultless mould, With glossy skin like polished gold. And loudly to her husband cried And bow-armed LakshmaG by his side: Again, again she called in glee: “O come this glorious creature see; Quick, quick, my lord, this deer to view. And bring thy brother LakshmaG too.” As through the wood her clear tones rang, Swift to her side the brothers sprang. With eager eyes the grove they scanned, And saw the deer before them stand. But doubt was strong in LakshmaG's breast, Who thus his thought and fear expressed:
- **Translation**: 

---

### Verse 19 (Ramayana 0.1004)
- **Original**: 986 The Ramayana “Stay, for the wondrous deer we see The fiend Márícha's self may be. Ere now have kings who sought this place To take their pastime in the chase, Met from his wicked art defeat, And fallen slain by like deceit. He wears, well trained in magic guile, The figure of a deer a while, Bright as the very sun, or place Where dwell the gay Gandharva race. No deer, O Ráma, e'er was seen Thus decked with gold and jewels' sheen. 'Tis magic, for the world has ne'er, Lord of the world, shown aught so fair.” But Sítá of the lovely smile, A captive to the giant's wile, Turned LakshmaG's prudent speech aside And thus with eager words replied: “My honoured lord, this deer I see With beauty rare enraptures me. Go, chief of mighty arm, and bring For my delight this precious thing. Fair creatures of the woodland roam Untroubled near our hermit home. The forest cow and stag are there, The fawn, the monkey, and the bear, Where spotted deer delight to play,[279] And strong and beauteous Kinnars494 stray. But never, as they wandered by, Has such a beauty charmed mine eye As this with limbs so fair and slight, 494 A race of beings of human shape but with the heads of horses, like centaurs reversed.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1005)
- **Original**: Canto XLIII. The Wondrous Deer. 987 So gentle, beautiful and bright. O see, how fair it is to view With jewels of each varied hue: Bright as the rising moon it glows, Lighting the wood where'er it goes. Ah me, what form and grace are there! Its limbs how fine, its hues how fair! Transcending all that words express, It takes my soul with loveliness. O, if thou would, to please me, strive To take the beauteous thing alive, How thou wouldst gaze with wondering eyes Delighted on the lovely prize! And when our woodland life is o'er, And we enjoy our realm once more, The wondrous animal will grace The chambers of my dwelling-place, And a dear treasure will it be To Bharat and the queens and me, And all with rapture and amaze Upon its heavenly form will gaze. But if the beauteous deer, pursued, Thine arts to take it still elude, Strike it, O chieftain, and the skin Will be a treasure, laid within. O, how I long my time to pass Sitting upon the tender grass, With that soft fell beneath me spread Bright with its hair of golden thread! This strong desire, this eager will, Befits a gentle lady ill: But when I first beheld, its look My breast with fascination took. See, golden hair its flank adorns,
- **Translation**: 

---

