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

### Verse 1 (Ramayan 0.461)
- **Original**: Canto XXIX. Sítá's Appeal. 443 The snakes that by the rives hide In sinuous course like rivers glide, And line the path with deadly foes: The wood, my love, is full of woes. Scorpions, and grasshoppers, and flies Disturb the wanderer as he lies, And wake him from his troubled doze: The wood, my love, is full of woes. Trees, thorny bushes, intertwined, Their branched ends together bind, And dense with grass the thicket grows: The wood, my dear, is full of woes, With many ills the flesh is tried, When these and countless fears beside Vex those who in the wood remain: The wilds are naught but grief and pain. Hope, anger must be cast aside, To penance every thought applied: No fear must be of things to fear: Hence is the wood for ever drear. Enough, my love: thy purpose quit: For forest life thou art not fit. As thus I think on all, I see The wild wood is no place for thee.” Canto XXIX. Sítá's Appeal. Thus Ráma spake. Her lord's address The lady heard with deep distress, And, as the tear bedimmed her eye, In soft low accents made reply:
- **Translation**: 

---

### Verse 2 (Ramayan 0.462)
- **Original**: 444 The Ramayana “The perils of the wood, and all The woes thou countest to appal, Led by my love I deem not pain; Each woe a charm, each loss a gain. Tiger, and elephant, and deer, Bull, lion, buffalo, in fear, Soon as thy matchless form they see, With every silvan beast will flee. With thee, O Ráma, I must go: My sire's command ordains it so. Bereft of thee, my lonely heart Must break, and life and I must part. While thou, O mighty lord, art nigh, Not even He who rules the sky, Though He is strongest of the strong, With all his might can do me wrong. Nor can a lonely woman left By her dear husband live bereft. In my great love, my lord, I ween, The truth of this thou mayst have seen. In my sire's palace long ago I heard the chief of those who know, The truth-declaring Bráhmans, tell My fortune, in the wood to dwell. I heard their promise who divine The future by each mark and sign, And from that hour have longed to lead The forest life their lips decreed. Now, mighty Ráma, I must share Thy father's doom which sends thee there; In this I will not be denied, But follow, love, where thou shalt guide. O husband, I will go with thee, Obedient to that high decree.
- **Translation**: 

---

### Verse 3 (Ramayan 0.463)
- **Original**: Canto XXIX. Sítá's Appeal. 445 Now let the Bráhmans' words be true, For this the time they had in view. I know full well the wood has woes; But they disturb the lives of those Who in the forest dwell, nor hold Their rebel senses well controlled. [129] In my sire's halls, ere I was wed, I heard a dame who begged her bread Before my mother's face relate What griefs a forest life await. And many a time in sport I prayed To seek with thee the greenwood shade, For O, my heart on this is set, To follow thee, dear anchoret. May blessings on thy life attend: I long with thee my steps to bend, For with such hero as thou art This pilgrimage enchants my heart. Still close, my lord, to thy dear side My spirit will be purified: Love from all sin my soul will free: My husband is a God to me. So, love, with thee shall I have bliss And share the life that follows this. I heard a Bráhman, dear to fame, This ancient Scripture text proclaim: “The woman whom on earth below Her parents on a man bestow, And lawfully their hands unite With water and each holy rite, She in this world shall be his wife, His also in the after life.” Then tell me, O beloved, why Thou wilt this earnest prayer deny,
- **Translation**: 

---

### Verse 4 (Ramayan 0.464)
- **Original**: 446 The Ramayana Nor take me with thee to the wood, Thine own dear wife so true and good. But if thou wilt not take me there Thus grieving in my wild despair, To fire or water I will fly, Or to the poisoned draught, and die.” So thus to share his exile, she Besought him with each earnest plea, Nor could she yet her lord persuade To take her to the lonely shade. The answer of the strong-armed chief Smote the Videhan's soul with grief, And from her eyes the torrents came bathing the bosom of the dame. Canto XXX. The Triumph Of Love. The daughter of Videha's king, While Ráma strove to soothe the sting Of her deep anguish, thus began Once more in furtherance of her plan: And with her spirit sorely tried By fear and anger, love and pride, With keenly taunting words addressed Her hero of the stately breast: “Why did the king my sire, who reigns O'er fair Videha's wide domains, Hail Ráma son with joy unwise, A woman in a man's disguise? Now falsely would the people say,
- **Translation**: 

---

### Verse 5 (Ramayan 0.465)
- **Original**: Canto XXX. The Triumph Of Love. 447 By idle fancies led astray, That Ráma's own are power and might, As glorious as the Lord of Light. Why sinkest thou in such dismay? What fears upon thy spirit weigh, That thou, O Ráma, fain wouldst flee From her who thinks of naught but thee? To thy dear will am I resigned In heart and body, soul and mind, As Sávitrí gave all to one, Satyaván, Dyumatsena's son.304 Not e'en in fancy can I brook To any guard save thee to look: Let meaner wives their houses shame, To go with thee is all my claim. Like some low actor, deemst thou fit Thy wife to others to commit— Thine own, espoused in maiden youth, Thy wife so long, unblamed for truth? Do thou, my lord, his will obey For whom thou losest royal sway, To whom thou wouldst thy wife confide— Not me, but thee, his wish may guide. Thou must not here thy wife forsake, And to the wood thy journey make, Whether stern penance, grief, and care, Or rule or heaven await thee there. Nor shall fatigue my limbs distress When wandering in the wilderness: Each path which near to thee I tread Shall seem a soft luxurious bed. 304 The story of Sávitrí, told in the Mahábhárat, has been admirably translated by Rückert, and elegantly epitomized by Mrs. Manning inIndia, Ancient and Mediæval. There is a free rendering of the story inIdylls from the Sanskrit.
- **Translation**: 

---

### Verse 6 (Ramayan 0.466)
- **Original**: 448 The Ramayana The reeds, the bushes where I pass, The thorny trees, the tangled grass Shall feel, if only thou be near, Soft to my touch as skins of deer. When the rude wind in fury blows, And scattered dust upon me throws, That dust, beloved lord, to me Shall as the precious sandal be. And what shall be more blest than I, When gazing on the wood I lie In some green glade upon a bed With sacred grass beneath us spread? The root, the leaf, the fruit which thou Shalt give me from the earth or bough, Scanty or plentiful, to eat, Shall taste to me as Amrit sweet. As there I live on flowers and roots And every season's kindly fruits, I will not for my mother grieve, My sire, my home, or all I leave. My presence, love, shall never add One pain to make the heart more sad;[130] I will not cause thee grief or care, Nor be a burden hard to bear. With thee is heaven, where'er the spot; Each place is hell where thou art not. Then go with me, O Ráma; this Is all my hope and all my bliss. If thou wilt leave thy wife who still Entreats thee with undaunted will, This very day shall poison close The life that spurns the rule of foes. How, after, can my soul sustain The bitter life of endless pain,
- **Translation**: 

---

### Verse 7 (Ramayan 0.467)
- **Original**: Canto XXX. The Triumph Of Love. 449 When thy dear face, my lord, I miss? No, death is better far than this. Not for an hour could I endure The deadly grief that knows not cure, Far less a woe I could not shun For ten long years, and three, and one.” While fires of woe consumed her, such Her sad appeal, lamenting much; Then with a wild cry, anguish-wrung, About her husband's neck she clung. Like some she-elephant who bleeds Struck by the hunter's venomed reeds, So in her quivering heart she felt The many wounds his speeches dealt. Then, as the spark from wood is gained,305 Down rolled the tear so long restrained: The crystal moisture, sprung from woe, From her sweet eyes began to flow, As runs the water from a pair Of lotuses divinely fair. And Sítá's face with long dark eyes, Pure as the moon of autumn skies, Faded with weeping, as the buds Of lotuses when sink the floods. Around his wife his arms he strained, Who senseless from her woe remained, And with sweet words, that bade her wake To life again, the hero spake: “I would not with thy woe, my Queen, Buy heaven and all its blissful sheen. Void of all fear am I as He, 305 Fire for sacrificial purposes is produced by the attrition of two pieces of wood.
- **Translation**: 

---

### Verse 8 (Ramayan 0.468)
- **Original**: 450 The Ramayana The self-existent God, can be. I knew not all thy heart till now, Dear lady of the lovely brow, So wished not thee in woods to dwell; Yet there mine arm can guard thee well. Now surely thou, dear love, wast made To dwell with me in green wood shade. And, as a high saint's tender mind Clings to its love for all mankind, So I to thee will ever cling, Sweet daughter of Videha's king. The good, of old, O soft of frame, Honoured this duty's sovereign claim, And I its guidance will not shun, True as light's Queen is to the Sun. I cannot, pride of Janak's line, This journey to the wood decline: My sire's behest, the oath he sware, The claims of truth, all lead me there. One duty, dear the same for aye, Is sire and mother to obey: Should I their orders once transgress My very life were weariness. If glad obedience be denied To father, mother, holy guide, What rites, what service can be done That stern Fate's favour may be won? These three the triple world comprise, O darling of the lovely eyes. Earth has no holy thing like these Whom with all love men seek to please. Not truth, or gift, or bended knee, Not honour, worship, lordly fee, Storms heaven and wins a blessing thence
- **Translation**: 

---

### Verse 9 (Ramayan 0.469)
- **Original**: Canto XXX. The Triumph Of Love. 451 Like sonly love and reverence. Heaven, riches, grain, and varied lore, With sons and many a blessing more, All these are made their own with ease By those their elders' souls who please. The mighty-souled, who ne'er forget, Devoted sons, their filial debt, Win worlds where Gods and minstrels are, And Brahmá's sphere more glorious far. Now as the orders of my sire, Who keeps the way of truth, require, So will I do, for such the way Of duty that endures for aye: To take thee, love, to DaG ak's wild My heart at length is reconciled, For thee such earnest thoughts impel To follow, and with me to dwell. O faultless form from feet to brows, Come with me, as my will allows, And duty there with me pursue, Trembler, whose bright eyes thrill me through. In all thy days, come good come ill, Preserve unchanged such noble will, And thou, dear love, wilt ever be The glory of thy house and me. Now, beauteous-armed, begin the tasks The woodland life of hermits asks. For me the joys of heaven above Have charms no more without thee, love. And now, dear Sítá, be not slow: Food on good mendicants bestow, And for the holy Bráhmans bring Thy treasures and each precious thing. Thy best attire and gems collect,
- **Translation**: 

---

### Verse 10 (Ramayan 0.470)
- **Original**: 452 The Ramayana The jewels which thy beauty decked, And every ornament and toy Prepared for hours of sport and joy: The beds, the cars wherein I ride, Among our followers, next, divide.” She conscious that her lord approved Her going, with great rapture moved,[131] Hastened within, without delay, Prepared to give their wealth away. Canto XXXI. Lakshman's Prayer. When Lakshma G, who had joined them there, Had heard the converse of the pair, His mien was changed, his eyes o'erflowed, His breast no more could bear its load. The son of Raghu, sore distressed, His brother's feet with fervour pressed, While thus to Sítá he complained, And him by lofty vows enchained: “If thou wilt make the woods thy home, Where elephant and roebuck roam, I too this day will take my bow And in the path before thee go. Our way will lie through forest ground Where countless birds and beasts are found, I heed not homes of Gods on high, I heed not life that cannot die, Nor would I wish, with thee away, O'er the three worlds to stretch my sway.”
- **Translation**: 

---

### Verse 11 (Ramayan 0.471)
- **Original**: Canto XXXI. Lakshman's Prayer. 453 Thus LakshmaG spake, with earnest prayer His brother's woodland life to share. As Ráma still his prayer denied With soothing words, again he cried: “When leave at first thou didst accord, Why dost thou stay me now, my lord? Thou art my refuge: O, be kind, Leave me not, dear my lord, behind. Thou canst not, brother, if thou choose That I still live, my wish refuse.” The glorious chief his speech renewed To faithful LakshmaG as he sued, And on the eyes of Ráma gazed Longing to lead, with hands upraised: “Thou art a hero just and dear, Whose steps to virtue's path adhere, Loved as my life till life shall end, My faithful brother and my friend. If to the woods thou take thy way With Sítá and with me to-day, Who for Kau[alyá will provide, And guard the good Sumitrá's side? The lord of earth, of mighty power, Who sends good things in plenteous shower, As Indra pours the grateful rain, A captive lies in passion's chain. The power imperial for her son Has A[vapati's daughter306 won, And she, proud queen, will little heed Her miserable rivals' need. So Bharat, ruler of the land, By Queen Kaikeyí's side will stand, 306 Kaikeyí.
- **Translation**: 

---

### Verse 12 (Ramayan 0.472)
- **Original**: 454 The Ramayana Nor of those two will ever think, While grieving in despair they sink. Now, LakshmaG, as thy love decrees, Or else the monarch's heart to please, Follow this counsel and protect My honoured mother from neglect. So thou, while not to me alone Thy great affection will be shown, To highest duty wilt adhere By serving those thou shouldst revere. Now, son of Raghu, for my sake Obey this one request I make, Or, of her darling son bereft, Kau [alyá has no comfort left.” The faithful LakshmaG, thus addressed In gentle words which love expressed, To him in lore of language learned, His answer, eloquent, returned: “Nay, through thy might each queen will share Attentive Bharat's love and care, Should Bharat, raised as king to sway This noblest realm, his trust betray, Nor for their safety well provide, Seduced by ill-suggesting pride, Doubt not my vengeful hand shall kill The cruel wretch who counsels ill— Kill him and all who lend him aid, And the three worlds in league arrayed. And good Kau[alyá well can fee A thousand champions like to me. A thousand hamlets rich in grain The station of that queen maintain.
- **Translation**: 

---

### Verse 13 (Ramayan 0.473)
- **Original**: Canto XXXI. Lakshman's Prayer. 455 She may, and my dear mother too, Live on the ample revenue. Then let me follow thee: herein: Is naught that may resemble sin. So shall I in my wish succeed, And aid, perhaps, my brother's need. My bow and quiver well supplied With arrows hanging at my side, My hands shall spade and basket bear, And for thy feet the way prepare. I'll bring thee roots and berries sweet. And woodland fare which hermits eat. Thou shall with thy Videhan spouse Recline upon the mountain's brows; Be mine the toil, be mine to keep Watch o'er thee waking or asleep.” Filled by his speech with joy and pride, Ráma to LakshmaG thus replied: “Go then, my brother, bid adieu To all thy friends and retinue. And those two bows of fearful might, Celestial, which, at that famed rite, Lord VaruG gave to Janak, king Of fair Vedeha with thee bring, With heavenly coats of sword-proof mail, Quivers, whose arrows never fail, [132] And golden-hilted swords so keen, The rivals of the sun in sheen. Tended with care these arms are all Preserved in my preceptor's hall. With speed, O LakshmaG, go, produce, And bring them hither for our use.” So on a woodland life intent,
- **Translation**: 

---

### Verse 14 (Ramayan 0.474)
- **Original**: 456 The Ramayana To see his faithful friends he went, And brought the heavenly arms which lay By Ráma's teacher stored away. And Raghu's son to Ráma showed Those wondrous arms which gleamed and glowed, Well kept, adorned with many a wreath Of flowers on case, and hilt, and sheath. The prudent Ráma at the sight Addressed his brother with delight: “Well art thou come, my brother dear, For much I longed to see thee here. For with thine aid, before I go, I would my gold and wealth bestow Upon the Bráhmans sage, who school Their lives by stern devotion's rule. And for all those who ever dwell Within my house and serve me well, Devoted servants, true and good, Will I provide a livelihood. Quick, go and summon to this place The good Va[ishmha's son, Suyajùa, of the Bráhman race The first and holiest one. To all the Bráhmans wise and good Will I due reverence pay, Then to the solitary wood With thee will take my way.” Canto XXXII. The Gift Of The Treasures.
- **Translation**: 

---

### Verse 15 (Ramayan 0.475)
- **Original**: Canto XXXII. The Gift Of The Treasures. 457 That speech so noble which conveyed His friendly wish, the chief obeyed, With steps made swift by anxious thought The wise Suyajùa's home he sought. Him in the hall of Fire307 he found, And bent before him to the ground: “O friend, to Ráma's house return, Who now performs a task most stern.” He, when his noonday rites were done, Went forth with fair Sumitrá's son, And came to Ráma's bright abode Rich in the love which Lakshmí showed. The son of Raghu, with his dame, With joined hands met him as he came, Showing to him who Scripture knew The worship that is Agni's due. With armlets, bracelets, collars, rings, With costly pearls on golden strings, With many a gem for neck and limb The son of Raghu honoured him. Then Ráma, at his wife's request, The wise Suyajùa thus addressed: “Accept a necklace too to deck With golden strings thy spouse's neck. And Sítá here, my friend, were glad A girdle to her gift to add. And many a bracelet wrought with care, And many an armlet rich and rare, My wife to thine is fain to give, Departing in the wood to live. A bed by skilful workmen made, With gold and various gems inlaid— 307 The chapel where the sacred fire used in worship is kept.
- **Translation**: 

---

### Verse 16 (Ramayan 0.476)
- **Original**: 458 The Ramayana This too, before she goes, would she Present, O saintly friend, to thee. Thine be my elephant, so famed, My uncle's present, Victor named; And let a thousand coins of gold, Great Bráhman, with the gift be told.” Thus Ráma spoke: nor he declined The noble gifts for him designed. On Ráma, LakshmaG, Sítá he Invoked all high felicity. In pleasant words then Ráma gave His best to LakshmaG prompt and brave, As Brahmá speaks for Him to hear Who rules the Gods' celestial sphere: “To the two best of Bráhmans run; Agastya bring, and Ku[ik's son, And precious gifts upon them rain, Like fostering floods upon the grain. O long-armed Prince of Raghu's line, Delight them with a thousand kine, And many a fair and costly gem, With gold and silver, give to them. To him, so deep in Scripture, who, To Queen Kau[alyá, ever true, Serves her with blessing and respect, Chief of the Taittiríya sect308— To him, with women-slaves, present A chariot rich with ornament, And costly robes of silk beside, Until the sage be satisfied. On Chitraratha, true and dear, My tuneful bard and charioteer, 308 The students and teachers of the Taittiríya portion of the Yajur Veda.
- **Translation**: 

---

### Verse 17 (Ramayan 0.477)
- **Original**: Canto XXXII. The Gift Of The Treasures. 459 Gems, robes, and plenteous wealth confer— Mine ancient friend and minister. And these who go with staff in hand, Grammarians trained, a numerous band, Who their deep study only prize, Nor think of other exercise, Who toil not, loving dainty fare, Whose praises e'en the good declare— On these be eighty cars bestowed, And each with precious treasures load. [133] A thousand bulls for them suffice, Two hundred elephants of price, And let a thousand kine beside The dainties of each meal provide. The throng who sacred girdles wear, And on Kau[alyá wait with care— A thousand golden coins shall please, Son of Sumitrá, each of these. Let all, dear LakshmaG of the train These special gifts of honour gain: My mother will rejoice to know Her Bráhmans have been cherished so.” Then Raghu's son addressed the crowd Who round him stood and wept aloud, When he to all who thronged the court Had dealt his wealth for their support: “In LakshmaG's house and mine remain, And guard them till I come again.” To all his people sad with grief, In loving words thus spoke their chief, Then bade his treasure-keeper bring Gold, silver, and each precious thing. Then straight the servants went and bore
- **Translation**: 

---

### Verse 18 (Ramayan 0.478)
- **Original**: 460 The Ramayana Back to their chief the wealth in store. Before the people's eyes it shone, A glorious pile to look upon. The prince of men with LakshmaG's aid Parted the treasures there displayed, Gave to the poor, the young, the old, And twice-born men, the gems and gold. A Bráhman, long in evil case, Named Trijam, born of Garga's race, Earned ever toiling in a wood With spade and plough his livelihood. The youthful wife, his babes who bore, Their indigence felt more and more. Thus to the aged man she spake: “Hear this my word: my counsel take. Come, throw thy spade and plough away; To virtuous Ráma go to-day, And somewhat of his kindness pray.” He heard the words she spoke: around His limbs his ragged cloth he wound, And took his journey by the road That led to Ráma's fair abode. To the fifth court he made his way; Nor met the Bráhman check or stay. Brighu, Angiras309 could not be Brighter with saintly light than he. To Ráma's presence on he pressed, And thus the noble chief addressed: “O Ráma, poor and weak am I, And many children round me cry. 309 Two of the divine personages calledPrajápatisand Brahmádikaswho were first created by Brahmá.
- **Translation**: 

---

### Verse 19 (Ramayan 0.479)
- **Original**: Canto XXXII. The Gift Of The Treasures. 461 Scant living in the woods I earn: On me thine eye of pity turn.” And Ráma, bent on sport and jest, The suppliant Bráhman thus addressed: “O aged man, one thousand kine, Yet undistributed, are mine. The cows on thee will I bestow As far as thou thy staff canst throw.” The Bráhman heard. In eager haste He bound his cloth around his waist. Then round his head his staff he whirled, And forth with mightiest effort hurled. Cast from his hand it flew, and sank To earth on Sarjú's farther bank, Where herds of kine in thousands fed Near to the well-stocked bullock shed. And all the cows that wandered o'er The meadow, far as Sarjú's shore, At Ráma's word the herdsmen drove To Trijam's cottage in the grove. He drew the Bráhman to his breast, And thus with calming words addressed: “Now be not angry, Sire. I pray: This jest of mine was meant in play. These thousand kine, but not alone. Their herdsmen too, are all thine own. And wealth beside I give thee: speak, Thine shall be all thy heart can seek.” Thus Ráma spake. And Trijam prayed For means his sacrifice to aid. And Ráma gave much wealth, required To speed his offering as desired.
- **Translation**: 

---

### Verse 20 (Ramayan 0.480)
- **Original**: 462 The Ramayana Canto XXXIII. The People's Lament. Thus Sítá and the princes brave Much wealth to all the Bráhmans gave. Then to the monarch's house the three Went forth the aged king to see. The princes from two servants took Those heavenly arms of glorious look, Adorned with garland and with band By Sítá's beautifying hand. On each high house a mournful throng Had gathered ere they passed along, Who gazed in pure unselfish woe From turret, roof, and portico. So dense the crowd that blocked the ways, The rest, unable there to gaze, Were fain each terrace to ascend, And thence their eyes on Ráma bend. Then as the gathered multitude On foot their well-loved Ráma viewed, No royal shade to screen his head, Such words, disturbed in grief, they said: “O look, our hero, wont to ride Leading a host in perfect pride— Now Lakshma G, sole of all his friends, With Sítá on his steps attends. Though he has known the sweets of power, And poured his gifts in liberal shower, From duty's path he will not swerve,[134] But, still his father's truth preserve. And she whose form so soft and fair Was veiled from spirits of the air, Now walks unsheltered from the day, Seen by the crowds who throng the way.
- **Translation**: 

---

