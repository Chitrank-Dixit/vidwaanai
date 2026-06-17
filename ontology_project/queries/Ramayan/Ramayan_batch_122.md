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

### Verse 1 (Ramayana 0.466)
- **Original**: 448 The Ramayana The reeds, the bushes where I pass, The thorny trees, the tangled grass Shall feel, if only thou be near, Soft to my touch as skins of deer. When the rude wind in fury blows, And scattered dust upon me throws, That dust, beloved lord, to me Shall as the precious sandal be. And what shall be more blest than I, When gazing on the wood I lie In some green glade upon a bed With sacred grass beneath us spread? The root, the leaf, the fruit which thou Shalt give me from the earth or bough, Scanty or plentiful, to eat, Shall taste to me as Amrit sweet. As there I live on flowers and roots And every season's kindly fruits, I will not for my mother grieve, My sire, my home, or all I leave. My presence, love, shall never add One pain to make the heart more sad;[130] I will not cause thee grief or care, Nor be a burden hard to bear. With thee is heaven, where'er the spot; Each place is hell where thou art not. Then go with me, O Ráma; this Is all my hope and all my bliss. If thou wilt leave thy wife who still Entreats thee with undaunted will, This very day shall poison close The life that spurns the rule of foes. How, after, can my soul sustain The bitter life of endless pain,
- **Translation**: 

---

### Verse 2 (Ramayana 0.467)
- **Original**: Canto XXX. The Triumph Of Love. 449 When thy dear face, my lord, I miss? No, death is better far than this. Not for an hour could I endure The deadly grief that knows not cure, Far less a woe I could not shun For ten long years, and three, and one.” While fires of woe consumed her, such Her sad appeal, lamenting much; Then with a wild cry, anguish-wrung, About her husband's neck she clung. Like some she-elephant who bleeds Struck by the hunter's venomed reeds, So in her quivering heart she felt The many wounds his speeches dealt. Then, as the spark from wood is gained,305 Down rolled the tear so long restrained: The crystal moisture, sprung from woe, From her sweet eyes began to flow, As runs the water from a pair Of lotuses divinely fair. And Sítá's face with long dark eyes, Pure as the moon of autumn skies, Faded with weeping, as the buds Of lotuses when sink the floods. Around his wife his arms he strained, Who senseless from her woe remained, And with sweet words, that bade her wake To life again, the hero spake: “I would not with thy woe, my Queen, Buy heaven and all its blissful sheen. Void of all fear am I as He, 305 Fire for sacrificial purposes is produced by the attrition of two pieces of wood.
- **Translation**: 

---

### Verse 3 (Ramayana 0.468)
- **Original**: 450 The Ramayana The self-existent God, can be. I knew not all thy heart till now, Dear lady of the lovely brow, So wished not thee in woods to dwell; Yet there mine arm can guard thee well. Now surely thou, dear love, wast made To dwell with me in green wood shade. And, as a high saint's tender mind Clings to its love for all mankind, So I to thee will ever cling, Sweet daughter of Videha's king. The good, of old, O soft of frame, Honoured this duty's sovereign claim, And I its guidance will not shun, True as light's Queen is to the Sun. I cannot, pride of Janak's line, This journey to the wood decline: My sire's behest, the oath he sware, The claims of truth, all lead me there. One duty, dear the same for aye, Is sire and mother to obey: Should I their orders once transgress My very life were weariness. If glad obedience be denied To father, mother, holy guide, What rites, what service can be done That stern Fate's favour may be won? These three the triple world comprise, O darling of the lovely eyes. Earth has no holy thing like these Whom with all love men seek to please. Not truth, or gift, or bended knee, Not honour, worship, lordly fee, Storms heaven and wins a blessing thence
- **Translation**: 

---

### Verse 4 (Ramayana 0.469)
- **Original**: Canto XXX. The Triumph Of Love. 451 Like sonly love and reverence. Heaven, riches, grain, and varied lore, With sons and many a blessing more, All these are made their own with ease By those their elders' souls who please. The mighty-souled, who ne'er forget, Devoted sons, their filial debt, Win worlds where Gods and minstrels are, And Brahmá's sphere more glorious far. Now as the orders of my sire, Who keeps the way of truth, require, So will I do, for such the way Of duty that endures for aye: To take thee, love, to DaG ak's wild My heart at length is reconciled, For thee such earnest thoughts impel To follow, and with me to dwell. O faultless form from feet to brows, Come with me, as my will allows, And duty there with me pursue, Trembler, whose bright eyes thrill me through. In all thy days, come good come ill, Preserve unchanged such noble will, And thou, dear love, wilt ever be The glory of thy house and me. Now, beauteous-armed, begin the tasks The woodland life of hermits asks. For me the joys of heaven above Have charms no more without thee, love. And now, dear Sítá, be not slow: Food on good mendicants bestow, And for the holy Bráhmans bring Thy treasures and each precious thing. Thy best attire and gems collect,
- **Translation**: 

---

### Verse 5 (Ramayana 0.470)
- **Original**: 452 The Ramayana The jewels which thy beauty decked, And every ornament and toy Prepared for hours of sport and joy: The beds, the cars wherein I ride, Among our followers, next, divide.” She conscious that her lord approved Her going, with great rapture moved,[131] Hastened within, without delay, Prepared to give their wealth away. Canto XXXI. Lakshman's Prayer. When Lakshma G, who had joined them there, Had heard the converse of the pair, His mien was changed, his eyes o'erflowed, His breast no more could bear its load. The son of Raghu, sore distressed, His brother's feet with fervour pressed, While thus to Sítá he complained, And him by lofty vows enchained: “If thou wilt make the woods thy home, Where elephant and roebuck roam, I too this day will take my bow And in the path before thee go. Our way will lie through forest ground Where countless birds and beasts are found, I heed not homes of Gods on high, I heed not life that cannot die, Nor would I wish, with thee away, O'er the three worlds to stretch my sway.”
- **Translation**: 

---

### Verse 6 (Ramayana 0.471)
- **Original**: Canto XXXI. Lakshman's Prayer. 453 Thus LakshmaG spake, with earnest prayer His brother's woodland life to share. As Ráma still his prayer denied With soothing words, again he cried: “When leave at first thou didst accord, Why dost thou stay me now, my lord? Thou art my refuge: O, be kind, Leave me not, dear my lord, behind. Thou canst not, brother, if thou choose That I still live, my wish refuse.” The glorious chief his speech renewed To faithful LakshmaG as he sued, And on the eyes of Ráma gazed Longing to lead, with hands upraised: “Thou art a hero just and dear, Whose steps to virtue's path adhere, Loved as my life till life shall end, My faithful brother and my friend. If to the woods thou take thy way With Sítá and with me to-day, Who for Kau[alyá will provide, And guard the good Sumitrá's side? The lord of earth, of mighty power, Who sends good things in plenteous shower, As Indra pours the grateful rain, A captive lies in passion's chain. The power imperial for her son Has A[vapati's daughter306 won, And she, proud queen, will little heed Her miserable rivals' need. So Bharat, ruler of the land, By Queen Kaikeyí's side will stand, 306 Kaikeyí.
- **Translation**: 

---

### Verse 7 (Ramayana 0.472)
- **Original**: 454 The Ramayana Nor of those two will ever think, While grieving in despair they sink. Now, LakshmaG, as thy love decrees, Or else the monarch's heart to please, Follow this counsel and protect My honoured mother from neglect. So thou, while not to me alone Thy great affection will be shown, To highest duty wilt adhere By serving those thou shouldst revere. Now, son of Raghu, for my sake Obey this one request I make, Or, of her darling son bereft, Kau [alyá has no comfort left.” The faithful LakshmaG, thus addressed In gentle words which love expressed, To him in lore of language learned, His answer, eloquent, returned: “Nay, through thy might each queen will share Attentive Bharat's love and care, Should Bharat, raised as king to sway This noblest realm, his trust betray, Nor for their safety well provide, Seduced by ill-suggesting pride, Doubt not my vengeful hand shall kill The cruel wretch who counsels ill— Kill him and all who lend him aid, And the three worlds in league arrayed. And good Kau[alyá well can fee A thousand champions like to me. A thousand hamlets rich in grain The station of that queen maintain.
- **Translation**: 

---

### Verse 8 (Ramayana 0.473)
- **Original**: Canto XXXI. Lakshman's Prayer. 455 She may, and my dear mother too, Live on the ample revenue. Then let me follow thee: herein: Is naught that may resemble sin. So shall I in my wish succeed, And aid, perhaps, my brother's need. My bow and quiver well supplied With arrows hanging at my side, My hands shall spade and basket bear, And for thy feet the way prepare. I'll bring thee roots and berries sweet. And woodland fare which hermits eat. Thou shall with thy Videhan spouse Recline upon the mountain's brows; Be mine the toil, be mine to keep Watch o'er thee waking or asleep.” Filled by his speech with joy and pride, Ráma to LakshmaG thus replied: “Go then, my brother, bid adieu To all thy friends and retinue. And those two bows of fearful might, Celestial, which, at that famed rite, Lord VaruG gave to Janak, king Of fair Vedeha with thee bring, With heavenly coats of sword-proof mail, Quivers, whose arrows never fail, [132] And golden-hilted swords so keen, The rivals of the sun in sheen. Tended with care these arms are all Preserved in my preceptor's hall. With speed, O LakshmaG, go, produce, And bring them hither for our use.” So on a woodland life intent,
- **Translation**: 

---

### Verse 9 (Ramayana 0.474)
- **Original**: 456 The Ramayana To see his faithful friends he went, And brought the heavenly arms which lay By Ráma's teacher stored away. And Raghu's son to Ráma showed Those wondrous arms which gleamed and glowed, Well kept, adorned with many a wreath Of flowers on case, and hilt, and sheath. The prudent Ráma at the sight Addressed his brother with delight: “Well art thou come, my brother dear, For much I longed to see thee here. For with thine aid, before I go, I would my gold and wealth bestow Upon the Bráhmans sage, who school Their lives by stern devotion's rule. And for all those who ever dwell Within my house and serve me well, Devoted servants, true and good, Will I provide a livelihood. Quick, go and summon to this place The good Va[ishmha's son, Suyajùa, of the Bráhman race The first and holiest one. To all the Bráhmans wise and good Will I due reverence pay, Then to the solitary wood With thee will take my way.” Canto XXXII. The Gift Of The Treasures.
- **Translation**: 

---

### Verse 10 (Ramayana 0.475)
- **Original**: Canto XXXII. The Gift Of The Treasures. 457 That speech so noble which conveyed His friendly wish, the chief obeyed, With steps made swift by anxious thought The wise Suyajùa's home he sought. Him in the hall of Fire307 he found, And bent before him to the ground: “O friend, to Ráma's house return, Who now performs a task most stern.” He, when his noonday rites were done, Went forth with fair Sumitrá's son, And came to Ráma's bright abode Rich in the love which Lakshmí showed. The son of Raghu, with his dame, With joined hands met him as he came, Showing to him who Scripture knew The worship that is Agni's due. With armlets, bracelets, collars, rings, With costly pearls on golden strings, With many a gem for neck and limb The son of Raghu honoured him. Then Ráma, at his wife's request, The wise Suyajùa thus addressed: “Accept a necklace too to deck With golden strings thy spouse's neck. And Sítá here, my friend, were glad A girdle to her gift to add. And many a bracelet wrought with care, And many an armlet rich and rare, My wife to thine is fain to give, Departing in the wood to live. A bed by skilful workmen made, With gold and various gems inlaid— 307 The chapel where the sacred fire used in worship is kept.
- **Translation**: 

---

### Verse 11 (Ramayana 0.476)
- **Original**: 458 The Ramayana This too, before she goes, would she Present, O saintly friend, to thee. Thine be my elephant, so famed, My uncle's present, Victor named; And let a thousand coins of gold, Great Bráhman, with the gift be told.” Thus Ráma spoke: nor he declined The noble gifts for him designed. On Ráma, LakshmaG, Sítá he Invoked all high felicity. In pleasant words then Ráma gave His best to LakshmaG prompt and brave, As Brahmá speaks for Him to hear Who rules the Gods' celestial sphere: “To the two best of Bráhmans run; Agastya bring, and Ku[ik's son, And precious gifts upon them rain, Like fostering floods upon the grain. O long-armed Prince of Raghu's line, Delight them with a thousand kine, And many a fair and costly gem, With gold and silver, give to them. To him, so deep in Scripture, who, To Queen Kau[alyá, ever true, Serves her with blessing and respect, Chief of the Taittiríya sect308— To him, with women-slaves, present A chariot rich with ornament, And costly robes of silk beside, Until the sage be satisfied. On Chitraratha, true and dear, My tuneful bard and charioteer, 308 The students and teachers of the Taittiríya portion of the Yajur Veda.
- **Translation**: 

---

### Verse 12 (Ramayana 0.477)
- **Original**: Canto XXXII. The Gift Of The Treasures. 459 Gems, robes, and plenteous wealth confer— Mine ancient friend and minister. And these who go with staff in hand, Grammarians trained, a numerous band, Who their deep study only prize, Nor think of other exercise, Who toil not, loving dainty fare, Whose praises e'en the good declare— On these be eighty cars bestowed, And each with precious treasures load. [133] A thousand bulls for them suffice, Two hundred elephants of price, And let a thousand kine beside The dainties of each meal provide. The throng who sacred girdles wear, And on Kau[alyá wait with care— A thousand golden coins shall please, Son of Sumitrá, each of these. Let all, dear LakshmaG of the train These special gifts of honour gain: My mother will rejoice to know Her Bráhmans have been cherished so.” Then Raghu's son addressed the crowd Who round him stood and wept aloud, When he to all who thronged the court Had dealt his wealth for their support: “In LakshmaG's house and mine remain, And guard them till I come again.” To all his people sad with grief, In loving words thus spoke their chief, Then bade his treasure-keeper bring Gold, silver, and each precious thing. Then straight the servants went and bore
- **Translation**: 

---

### Verse 13 (Ramayana 0.478)
- **Original**: 460 The Ramayana Back to their chief the wealth in store. Before the people's eyes it shone, A glorious pile to look upon. The prince of men with LakshmaG's aid Parted the treasures there displayed, Gave to the poor, the young, the old, And twice-born men, the gems and gold. A Bráhman, long in evil case, Named Trijam, born of Garga's race, Earned ever toiling in a wood With spade and plough his livelihood. The youthful wife, his babes who bore, Their indigence felt more and more. Thus to the aged man she spake: “Hear this my word: my counsel take. Come, throw thy spade and plough away; To virtuous Ráma go to-day, And somewhat of his kindness pray.” He heard the words she spoke: around His limbs his ragged cloth he wound, And took his journey by the road That led to Ráma's fair abode. To the fifth court he made his way; Nor met the Bráhman check or stay. Brighu, Angiras309 could not be Brighter with saintly light than he. To Ráma's presence on he pressed, And thus the noble chief addressed: “O Ráma, poor and weak am I, And many children round me cry. 309 Two of the divine personages calledPrajápatisand Brahmádikaswho were first created by Brahmá.
- **Translation**: 

---

### Verse 14 (Ramayana 0.479)
- **Original**: Canto XXXII. The Gift Of The Treasures. 461 Scant living in the woods I earn: On me thine eye of pity turn.” And Ráma, bent on sport and jest, The suppliant Bráhman thus addressed: “O aged man, one thousand kine, Yet undistributed, are mine. The cows on thee will I bestow As far as thou thy staff canst throw.” The Bráhman heard. In eager haste He bound his cloth around his waist. Then round his head his staff he whirled, And forth with mightiest effort hurled. Cast from his hand it flew, and sank To earth on Sarjú's farther bank, Where herds of kine in thousands fed Near to the well-stocked bullock shed. And all the cows that wandered o'er The meadow, far as Sarjú's shore, At Ráma's word the herdsmen drove To Trijam's cottage in the grove. He drew the Bráhman to his breast, And thus with calming words addressed: “Now be not angry, Sire. I pray: This jest of mine was meant in play. These thousand kine, but not alone. Their herdsmen too, are all thine own. And wealth beside I give thee: speak, Thine shall be all thy heart can seek.” Thus Ráma spake. And Trijam prayed For means his sacrifice to aid. And Ráma gave much wealth, required To speed his offering as desired.
- **Translation**: 

---

### Verse 15 (Ramayana 0.480)
- **Original**: 462 The Ramayana Canto XXXIII. The People's Lament. Thus Sítá and the princes brave Much wealth to all the Bráhmans gave. Then to the monarch's house the three Went forth the aged king to see. The princes from two servants took Those heavenly arms of glorious look, Adorned with garland and with band By Sítá's beautifying hand. On each high house a mournful throng Had gathered ere they passed along, Who gazed in pure unselfish woe From turret, roof, and portico. So dense the crowd that blocked the ways, The rest, unable there to gaze, Were fain each terrace to ascend, And thence their eyes on Ráma bend. Then as the gathered multitude On foot their well-loved Ráma viewed, No royal shade to screen his head, Such words, disturbed in grief, they said: “O look, our hero, wont to ride Leading a host in perfect pride— Now Lakshma G, sole of all his friends, With Sítá on his steps attends. Though he has known the sweets of power, And poured his gifts in liberal shower, From duty's path he will not swerve,[134] But, still his father's truth preserve. And she whose form so soft and fair Was veiled from spirits of the air, Now walks unsheltered from the day, Seen by the crowds who throng the way.
- **Translation**: 

---

### Verse 16 (Ramayana 0.481)
- **Original**: Canto XXXIII. The People's Lament. 463 Ah, for that gently-nurtured form! How will it fade with sun and storm! How will the rain, the cold, the heat Mar fragrant breast and tinted feet! Surely some demon has possessed His sire, and speaks within his breast, Or how could one that is a king Thus send his dear son wandering? It were a deed unkindly done To banish e'en a worthless son: But what, when his pure life has gained The hearts of all, by love enchained? Six sovereign virtues join to grace Ráma the foremost of his race: Tender and kind and pure is he, Docile, religious, passion-free. Hence misery strikes not him alone: In bitterest grief the people moan, Like creatures of the stream, when dry In the great heat the channels lie. The world is mournful with the grief That falls on its beloved chief, As, when the root is hewn away, Tree, fruit, and flower, and bud decay. The soul of duty, bright to see, He is the root of you and me; And all of us, who share his grief, His branches, blossom, fruit, and leaf. Now like the faithful LakshmaG, we Will follow and be true as he; Our wives and kinsmen call with speed, And hasten where our lord shall lead. Yes, we will leave each well-loved spot, The field, the garden, and the cot,
- **Translation**: 

---

### Verse 17 (Ramayana 0.482)
- **Original**: 464 The Ramayana And, sharers of his weal and woe, Behind the pious Ráma go. Our houses, empty of their stores, With ruined courts and broken doors, With all their treasures borne away. And gear that made them bright and gay: O'errun by rats, with dust o'erspread, Shrines, whence the deities have fled, Where not a hand the water pours, Or sweeps the long-neglected floors, No incense loads the evening air, No Bráhmans chant the text and prayer, No fire of sacrifice is bright, No gift is known, no sacred rite; With floors which broken vessels strew, As if our woes had crushed them too— Of these be stern Kaikeyí queen, And rule o'er homes where we have been. The wood where Ráma's feet may roam Shall be our city and our home, And this fair city we forsake, Our flight a wilderness shall make. Each serpent from his hole shall hie, The birds and beasts from mountain fly, Lions and elephants in fear Shall quit the woods when we come near, Yield the broad wilds for us to range, And take our city in exchange. With Ráma will we hence, content If, where he is, our days be spent.” Such were the varied words the crowd Of all conditions spoke aloud. And Ráma heard their speeches, yet
- **Translation**: 

---

### Verse 18 (Ramayana 0.483)
- **Original**: Canto XXXIV. Ráma In The Palace. 465 Changed not his purpose firmly set. His father's palace soon he neared, That like Kailása's hill appeared. Like a wild elephant he strode Right onward to the bright abode. Within the palace court he stepped, Where ordered bands their station kept, And saw Sumantra standing near With down-cast eye and gloomy cheer. Canto XXXIV. Ráma In The Palace. The dark incomparable chief Whose eye was like a lotus leaf, Cried to the mournful charioteer, “Go tell my sire that I am here.” Sumantra, sad and all dismayed, The chieftain's order swift obeyed. Within the palace doors he hied And saw the king, who wept and sighed. Like the great sun when wrapped in shade Like fire by ashes overlaid, Or like a pool with waters dried, So lay the world's great lord and pride, A while the wise Sumantra gazed On him whose senses woe has dazed, Grieving for Ráma. Near he drew With hands upraised in reverence due. With blessing first his king he hailed; Then with a voice that well-nigh failed,
- **Translation**: 

---

### Verse 19 (Ramayana 0.484)
- **Original**: 466 The Ramayana In trembling accents soft and low Addressed the monarch in his woe: “The prince of men, thy Ráma, waits Before thee at the palace gates. His wealth to Bráhmans he has dealt, And all who in his home have dwelt. Admit thy son. His friends have heard His kind farewell and parting word, He longs to see thee first, and then Will seek the wilds, O King of men. He, with each princely virtue's blaze, Shines as the sun engirt by rays.” The truthful King who loved to keep The law profound as Ocean's deep, And stainless as the dark blue sky, Thus to Sumantra made reply:[135] “Go then, Sumantra, go and call My wives and ladies one and all. Drawn round me shall they fill the place When I behold my Ráma's face.” Quick to the inner rooms he sped, And thus to all the women said, “Come, at the summons of the king: Come all, and make no tarrying.”
- **Translation**: 

---

### Verse 20 (Ramayana 0.485)
- **Original**: Canto XXXIV. Ráma In The Palace. 467 Their husband's word, by him conveyed, Soon as they heard, the dames obeyed, And following his guidance all Came thronging to the regal hall. In number half seven hundred, they, All lovely dames, in long array, With their bright eyes for weeping red, To stand round Queen Kau[alyá, sped. They gathered, and the monarch viewed One moment all the multitude, Then to Sumantra spoke and said: “Now let my son be hither led.” Sumantra went. Then Ráma came, And Lakshma G, and the Maithil dame, And, as he led them on, their guide Straight to the monarch's presence hied. When yet far off the father saw His son with raised palms toward him draw, Girt by his ladies, sick with woes, Swift from his royal seat he rose. With all his strength the aged man To meet his darling Ráma ran, But trembling, wild with dark despair, Fell on the ground and fainted there. And Lakshma G, wont in cars to ride, And Ráma, threw them by the side Of the poor miserable king, Half lifeless with his sorrow's sting. Throughout the spacious hall up went A thousand women's wild lament: “Ah Ráma! ” thus they wailed and wept, And anklets tinkled as they stepped Around his body, weeping, threw
- **Translation**: 

---

