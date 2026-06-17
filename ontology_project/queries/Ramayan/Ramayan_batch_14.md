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

### Verse 1 (Ramayan 0.261)
- **Original**: Canto LXI. Sunahsepha. 243 The glory of Ikshváku's line Made offer of a thousand kine, And sought to buy at lordly price A victim for the sacrifice. To many a distant land he drove, To many a people, town, and grove, And holy shades where hermits rest, Pursuing still his eager quest. At length on Bhrigu's sacred height The saint Richíka met his sight Sitting beneath the holy boughs. His children near him, and his spouse. The mighty lord drew near, assayed To win his grace, and reverence paid; And then the sainted king addressed The Bráhman saint with this request: “Bought with a hundred thousand kine, Give me, O Sage, a son of thine To be a victim in the rite, And thanks the favour shall requite. For I have roamed all countries round, Nor sacrificial victim found. Then, gentle Hermit, deign to spare One child amid the number there.” Then to the monarch's speech replied The hermit, penance-glorified: “For countless kine, for hills of gold, Mine eldest son shall ne'er be sold.” But, when she heard the saint's reply, The children's mother, standing nigh, Words such as these in answer said To Ambarísha, monarch dread:
- **Translation**: 

---

### Verse 2 (Ramayan 0.262)
- **Original**: 244 The Ramayana “My lord, the saint, has spoken well: His eldest child he will not sell. And know, great Monarch, that above The rest my youngest born I love. 'Tis ever thus: the father's joy Is centred in his eldest boy. The mother loves her darling best Whom last she rocked upon her breast: My youngest I will ne'er forsake.” As thus the sire and mother spake, Young Zunah[epha, of the three The midmost, cried unurged and free: “My sire withholds his eldest son, My mother keeps her youngest one: Then take me with thee, King: I ween The son is sold who comes between.” The king with joy his home resought, And took the prize his kine had bought. He bade the youth his car ascend, And hastened back the rites to end.242 So the ram caught in the thicket took the place of Isaac, or, as the Musalmáns say, of Ishmael. 242 “Ambarísha is the twenty-ninth in descent from Ikshváku, and is there- fore separated by an immense space of time from Tri[anku in whose story Vi[vámitra had played so important a part. Yet Richíka, who is represented as having young sons while Ambarísha was yet reigning being himself the son of Bhrigu and to be numbered with the most ancient sages, is said to have married the younger sister of Vi[vámitra. But I need not again remark that there is a perpetual anachronism in Indian mythology.” SCHLEGEL .{FNS . “In the mythical story related in this and the following Canto we may discover, I think, some indication of the epoch at which the immolation of lower animals was substituted for human sacrifice.… So when Iphigenia was about to be sacrificed at Aulis, one legend tells us that a hind was substituted for the virgin.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 3 (Ramayan 0.263)
- **Original**: Canto LXII. Ambarísha's Sacrifice. 245 Canto LXII. Ambarísha's Sacrifice. As thus the king that youth conveyed, His weary steeds at length he stayed At height of noon their rest to take Upon the bank of Pushkar's lake. There while the king enjoyed repose The captiveZunah[epha rose, And hasting to the water's side His uncle Vi[vámitra spied, With many a hermit 'neath the trees Engaged in stern austerities. Distracted with the toil and thirst, With woeful mien, away he burst, Swift to the hermit's breast he flew, And weeping thus began to sue: “No sire have I, no mother dear, No kith or kin my heart to cheer: As justice bids, O Hermit, deign To save me from the threatened pain. O thou to whom the wretched flee, And find a saviour, Saint, in thee, Now let the king obtain his will, And me my length of days fulfil, That rites austere I too may share, May rise to heaven and rest me there. With tender soul and gentle brow Be guardian of the orphan thou, And as a father pities, so Preserve me from my fear and woe.”
- **Translation**: 

---

### Verse 4 (Ramayan 0.264)
- **Original**: 246 The Ramayana When Vi [vámitra, glorious saint, Had heard the boy's heart-rending plaint. He soothed his grief, his tears he dried, [074] Then called his sons to him, and cried: “The time is come for you to show The duty and the aid bestow For which, regarding future life, A man gives children to his wife. This hermit's son, whom here you see A suppliant, refuge seeks with me. O sons, the friendless youth befriend, And, pleasing me, his life defend. For holy works you all have wrought, True to the virtuous life I taught. Go, and as victims doomed to bleed, Die, and Lord Agni's hunger feed. So shall the rite completed end, This orphan gain a saving friend, Due offerings to the Gods be paid, And your own father's voice obeyed.” Then Madhushyand and all the rest Answered their sire with scorn and jest: “What! aid to others' sons afford, And leave thine own to die, my lord! To us it seems a horrid deed, As 'twere on one's own flesh to feed.” The hermit heard his sons' reply, And burning rage inflamed his eye. Then forth his words of fury burst: “Audacious speech, by virtue cursed! It lifts on end each shuddering hair— My charge to scorn! my wrath to dare!
- **Translation**: 

---

### Verse 5 (Ramayan 0.265)
- **Original**: Canto LXII. Ambarísha's Sacrifice. 247 You, like Va[ishmha's evil brood, Shall make the flesh of dogs your food A thousand years in many a birth, And punished thus shall dwell on earth.” Thus on his sons his curse he laid. Then calmed again that youth dismayed, And blessed him with his saving aid: “When in the sacred fetters bound, And with a purple garland crowned, At VishGu's post thou standest tied, With lauds be Agni glorified. And these two hymns of holy praise Forget not, Hermit's son, to raise In the king's rite, and thou shalt be Lord of thy wish, preserved, and free.” He learnt the hymns with mind intent, And from the hermit's presence went. To Ambarísha thus he spake: “Let us our onward journey take. Haste to thy home, O King, nor stay The lustral rites with slow delay.” The boy's address the monarch cheered, And soon the sacred ground he neared. The convocation's high decree Declared the youth from blemish free; Clothed in red raiment he was tied A victim at the pillar's side. There bound, the Fire-God's hymn he raised, And Indra and Upendra praised. Thousand-eyed VishGu, pleased to hear The mystic laud, inclined his ear, And won by worship, swift to save,
- **Translation**: 

---

### Verse 6 (Ramayan 0.266)
- **Original**: 248 The Ramayana Long life toZunah[epha gave. The king in bounteous measure gained The fruit of sacrifice ordained, By grace of Him who rules the skies, Lord Indra of the thousand eyes. And Vi[vámitra evermore. Pursued his task on Pushkar's shore Until a thousand years had past In fierce austerity and fast. Canto LXIII. Menaká. A thousand years had thus flown by When all the Gods within the sky, Eager that he the fruit might gain Of fervent rite and holy pain, Approached the great ascetic, now Bathed after toil and ended vow. Then Brahmá speaking for the rest With sweetest words the sage addressed: “Hail, Saint! This high and holy name Thy rites have won, thy merits claim.”
- **Translation**: 

---

### Verse 7 (Ramayan 0.267)
- **Original**: Canto LXIII. Menaká. 249 Thus spoke the Lord whom Gods revere, And sought again his heavenly sphere. But Vi[vámitra, more intent, His mind to sterner penance bent. So many a season rolled away, When Menaká, fair nymph, one day Came down from Paradise to lave Her perfect limbs in Pushkar's wave, The glorious son of Ku[ik saw That peerless shape without a flaw Flash through the flood's translucent shroud Like lightning gleaming through a cloud. He saw her in that lone retreat, Most beautiful from head to feet, And by Kandarpa's243 might subdued He thus addressed her as he viewed: “Welcome, sweet nymph! O deign, I pray, In these calm shades awhile to stay. To me some gracious favour show, For love has set my breast aglow.” He spoke. The fairest of the fair Made for awhile her dwelling there, While day by day the wild delight Stayed vow austere and fervent rite There as the winsome charmer wove Her spells around him in the grove, And bound him in a golden chain, Five sweet years fled, and five again. Then Vi[vámitra woke to shame, And, fraught with anguish, memory came For quick he knew, with anger fired, That all the Immortals had conspired [075] 243 The Indian Cupid.
- **Translation**: 

---

### Verse 8 (Ramayan 0.268)
- **Original**: 250 The Ramayana To lap his careless soul in ease, And mar his long austerities. “Ten years have past, each day and night Unheeded in delusive flight. So long my fervent rites were stayed, While thus I lay by love betrayed.” As thus long sighs the hermit heaved, And, touched with deep repentance, grieved, He saw the fair one standing nigh With suppliant hands and trembling eye. With gentle words he bade her go, Then sought the northern hills of snow. With firm resolve he vowed to beat The might of love beneath his feet. Still northward to the distant side Of Kau[ikí244, the hermit hide, And gave his life to penance there With rites austere most hard to bear. A thousand years went by, and still He laboured on the northern hill With pains so terrible and drear That all the Gods were chilled with fear, 244 “The same as she whose praises Vi[vámitra has already sung in Canto XXXV, and whom the poet brings yet alive upon the scene in Canto LXI. Her proper name wasSatyavatí(Truthful); the patronymic, Kau[ikí was preserved by the river into which she is said to have been changed, and is still recognized in the corrupted forms Ku[a and Ku[í. The river flows from the heights of the Himálaya towards the Ganges, bounding on the east the country of Videha (Behar). The name is no doubt half hidden in theCosoagus of Pliny and the Kossounos of Arrian. But each author has fallen into the same error in his enumeration of these rivers (Condochatem, Erannoboam, Cosoagum, Sonum). The Erannoboas, (HiraGyaváha) and the Sone are not different streams, but well-known names of the same river. Moreover the order is disturbed, in which on the right and left they fall into the Ganges. To be consistent with geogra- phy it should be written: Erannoboam sive Sonum, Condochatem (Gandakí), Cosoagum.” SCHLEGEL {FNS .
- **Translation**: 

---

### Verse 9 (Ramayan 0.269)
- **Original**: Canto LXIII. Menaká. 251 And Gods and saints, for swift advice, Met in the halls of Paradise. “Let Ku[ik's son,” they counselled,“be A Mighty saint by just decree.” His ear to hear their counsel lent The Sire of worlds, omnipotent. To him enriched by rites severe He spoke in accents sweet to hear: “Hail, Mighty Saint! dear son, all hail! Thy fervour wins, thy toils prevail. Won by thy vows and zeal intense I give this high preëminence.” He to the General Sire replied, Not sad, nor wholly satisfied: “When thou, O Brahmá, shalt declare The title, great beyond compare, Of Bráhman saint my worthy meed, Hard earned by many a holy deed, Then may I deem in sooth I hold Each sense of body well controlled.” Then Brahmá cried,“Not yet, not yet: Toil on awhile O Anchoret!”
- **Translation**: 

---

### Verse 10 (Ramayan 0.270)
- **Original**: 252 The Ramayana Thus having said to heaven he went, The saint, upon his task intent, Began his labours to renew, Which sterner yet and fiercer grew. His arms upraised, without a rest, With but one foot the earth he pressed; The air his food, the hermit stood Still as a pillar hewn from wood. Around him in the summer days Five mighty fires combined to blaze. In floods of rain no veil was spread Save clouds, to canopy his head. In the dank dews both night and day Couched in the stream the hermit lay. Thus, till a thousand years had fled, He plied his task of penance dread. Then VishGu and the Gods with awe The labours of the hermit saw, And Zakra, in his troubled breast, Lord of the skies, his fear confessed. And brooded on a plan to spoil The merits of the hermit's toil. Encompassed by his Gods of Storm He summoned Rambhá, fair of form, And spoke a speech for woe and weal, The saint to mar, the God to heal. Canto LXIV. Rambhá.
- **Translation**: 

---

### Verse 11 (Ramayan 0.271)
- **Original**: Canto LXIV. Rambhá. 253 “A great emprise, O lovely maid, To save the Gods, awaits thine aid: To bind the son of Ku[ik sure, And take his soul with love's sweet lure.” Thus order'd by the Thousand-eyed The suppliant nymph in fear replied: “O Lord of Gods, this mighty sage Is very fierce and swift to rage. I doubt not, he so dread and stern On me his scorching wrath will turn. Of this, my lord, am I afraid: Have mercy on a timid maid.” Her suppliant hands began to shake, When thus again Lord Indra spake: “O Rambhá, drive thy fears away, And as I bid do thou obey. In Koïl's form, who takes the heart When trees in spring to blossom start, I, with Kandarpa for my friend, Close to thy side mine aid will lend. [076] Do thou thy beauteous splendour arm With every grace and winsome charm, And from his awful rites seduce This Ku[ik's son, the stern recluse.” Lord Indra ceased. The nymph obeyed: In all her loveliest charms arrayed, With winning ways and witching smile She sought the hermit to beguile. The sweet note of that tuneful bird The saint with ravished bosom heard, And on his heart a rapture passed As on the nymph a look he cast. But when he heard the bird prolong
- **Translation**: 

---

### Verse 12 (Ramayan 0.272)
- **Original**: 254 The Ramayana His sweet incomparable song, And saw the nymph with winning smile, The hermit's heart perceived the wile. And straight he knew the Thousand-eyed A plot against his peace had tried. Then Ku[ik's son indignant laid His curse upon the heavenly maid: “Because thou wouldst my soul engage Who fight to conquer love and rage, Stand, till ten thousand years have flown, Ill-fated maid, transformed to stone. A Bráhman then, in glory strong, Mighty through penance stern and long, Shall free thee from thine altered shape; Thou from my curse shalt then escape.” But when the saint had cursed her so, His breast was burnt with fires of woe, Grieved that long effort to restrain His mighty wrath was all in vain. Cursed by the angry sage's power, She stood in stone that selfsame hour. Kandarpa heard the words he said, And quickly from his presence fled. His fall beneath his passion's sway Had reft the hermit's meed away. Unconquered yet his secret foes, The humbled saint refused repose: “No more shall rage my bosom till, Sealed be my lips, my tongue be still. My very breath henceforth I hold Until a thousand years are told: Victorious o'er each erring sense, I'll dry my frame with abstinence, Until by penance duly done
- **Translation**: 

---

### Verse 13 (Ramayan 0.273)
- **Original**: Canto LXV. Visvámitra's Triumph 255 A Bráhman's rank be bought and won. For countless years, as still as death, I taste no food, I draw no breath, And as I toil my frame shall stand Unharmed by time's destroying hand.” Canto LXV. Visvámitra's Triumph Then from Himálaya's heights of snow, The glorious saint prepared to go, And dwelling in the distant east His penance and his toil increased. A thousand years his lips he held Closed by a vow unparalleled, And other marvels passing thought, Unrivalled in the world, he wrought. In all the thousand years his frame Dry as a log of wood became. By many a cross and check beset, Rage had not stormed his bosom yet. With iron will that naught could bend He plied his labour till the end. So when the weary years were o'er, Freed from his vow so stern and sore, The hermit, all his penance sped, Sate down to eat his meal of bread. Then Indra, clad in Bráhman guise, Asked him for food with hungry eyes. The mighty saint, with steadfast soul, To the false Bráhman gave the whole, And when no scrap for him remained,
- **Translation**: 

---

### Verse 14 (Ramayan 0.274)
- **Original**: 256 The Ramayana Fasting and faint, from speech refrained. His silent vow he would not break: No breath he heaved, no word he spake, Then as he checked his breath, behold! Around his brow thick smoke-clouds rolled And the three worlds, as if o'erspread With ravening flames, were filled with dread. Then God and saint and bard, convened, And Nága lord, and snake, and fiend, Thus to the General Father cried, Distracted, sad, and terrified: “Against the hermit, sore assailed, Lure, scathe, and scorn have naught availed, Proof against rage and treacherous art He keeps his vow with constant heart. Now if his toils assist him naught To gain the boon his soul has sought, He through the worlds will ruin send That fixt and moving things shall end, The regions now are dark with doom, No friendly ray relieves the gloom. Each ocean foams with maddened tide, The shrinking hills in fear subside. Trembles the earth with feverous throe The wind in fitful tempest blows. No cure we see with troubled eyes: And atheist brood on earth may rise. The triple world is wild with care, Or spiritless in dull despair. Before that saint the sun is dim, His blessed light eclipsed by him. Now ere the saint resolve to bring Destruction on each living thing, Let us appease, while yet we may,
- **Translation**: 

---

### Verse 15 (Ramayan 0.275)
- **Original**: Canto LXV. Visvámitra's Triumph 257 Him bright as fire, like fire to slay. Yea, as the fiery flood of Fate Lays all creation desolate, He o'er the conquered Gods may reign: O, grant him what he longs to gain.” [077] Then all the Blest, by Brahmá led, Approached the saint and sweetly said: “Hail, Bráhman Saint! for such thy place: Thy vows austere have won our grace. A Bráhman's rank thy penance stern And ceaseless labour richly earn. I with the Gods of Storm decree Long life, O Bráhman Saint, to thee. May peace and joy thy soul possess: Go where thou wilt in happiness.” Thus by the General Sire addressed, Joy and high triumph filled his breast. His head in adoration bowed, Thus spoke he to the Immortal crowd: “If I, ye Gods, have gained at last Both length of days and Bráhman caste, Grant that the high mysterious name, And holy Vedas, own my claim, And that the formula to bless The sacrifice, its lord confess. And let Va[ishmha, who excels In Warriors' art and mystic spells, In love of God without a peer, Confirm the boon you promise here.”
- **Translation**: 

---

### Verse 16 (Ramayan 0.276)
- **Original**: 258 The Ramayana With Brahmá's son Va[ishmha, best Of those who pray with voice repressed, The Gods by earnest prayer prevailed, And thus his new-made friend he hailed: “Thy title now is sure and good To rights of saintly Bráhmanhood.” Thus spake the sage. The Gods, content, Back to their heavenly mansions went. And Vi[vámitra, pious-souled, Among the Bráhman saints enrolled, On reverend Va[ishmha pressed The honours due to holy guest. Successful in his high pursuit, The sage, in penance resolute, Walked in his pilgrim wanderings o'er The whole broad land from shore to shore. 'Twas thus the saint, O Raghu's son, His rank among the Bráhmans won. Best of all hermits, Prince, is he; In him incarnate Penance see. Friend of the right, who shrinks from ill, Heroic powers attend him still.” The Bráhman, versed in ancient lore, Thus closed his tale, and said no more, To Zatánanda Ku[ik's son Cried in delight, Well done! well done! Then Janak, at the tale amazed, Spoke thus with suppliant hands upraised: “High fate is mine, O Sage, I deem, And thanks I owe for bliss supreme, That thou and Raghu's children too Have come my sacrifice to view. To look on thee with blessed eyes
- **Translation**: 

---

### Verse 17 (Ramayan 0.277)
- **Original**: Canto LXVI. Janak's Speech. 259 Exalts my soul and purifies. Yea, thus to see thee face to face Enriches me with store of grace. Thy holy labours wrought of old, And mighty penance, fully told, Ráma and I with great delight Have heard, O glorious Anchorite. Unrivalled thine ascetic deeds: Thy might, O Saint, all might exceeds. No thought may scan, no limit bound The virtues that in thee are found. The story of thy wondrous fate My thirsty ears can never sate. The hour of evening rites is near: The sun declines in swift career. At early dawn, O Hermit, deign To let me see thy face again. Best of ascetics, part in bliss: Do thou thy servant now dismiss.” The saint approved, and glad and kind Dismissed the king with joyful mind Around the sage King Janak went With priests and kinsmen reverent. Then Vi[vámitra, honoured so, By those high-minded, rose to go, And with the princes took his way To seek the lodging where they lay. Canto LXVI. Janak's Speech.
- **Translation**: 

---

### Verse 18 (Ramayan 0.278)
- **Original**: 260 The Ramayana With cloudless lustre rose the sun; The king, his morning worship done, Ordered his heralds to invite The princes and the anchorite. With honour, as the laws decree, The monarch entertained the three. Then to the youths and saintly man Videha's lord this speech began: “O blameless Saint, most welcome thou! If I may please thee tell me how. Speak, mighty lord, whom all revere, 'Tis thine to order, mine to hear.” Thus he on mighty thoughts intent; Then thus the sage most eloquent: “King Da[aratha's sons, this pair Of warriors famous everywhere, Are come that best of bows to see That lies a treasure stored by thee. This, mighty Janak, deign to show, That they may look upon the bow, And then, contented, homeward go.” Then royal Janak spoke in turn: “O best of Saints, the story learn Why this famed bow, a noble prize, A treasure in my palace lies. A monarch, Devarát by name, Who sixth from ancient Nimi came, Held it as ruler of the land, A pledge in his successive hand. This bow the mighty Rudra bore[078] At Daksha's245 sacrifice of yore, 245 “Daksha was one of the ancient Progenitors or Prajápatis created by Brah- má. The sacrifice which is here spoken of and in whichZankar orZiva (called
- **Translation**: 

---

### Verse 19 (Ramayan 0.279)
- **Original**: Canto LXVI. Janak's Speech. 261 When carnage of the Immortals stained The rite that Daksha had ordained. Then as the Gods sore wounded fled, Victorious Rudra, mocking, said: “Because, O Gods, ye gave me naught When I my rightful portion sought, Your dearest parts I will not spare, But with my bow your frames will tear.” The Sons of Heaven, in wild alarm, Soft flatteries tried his rage to charm. Then Bhava, Lord whom Gods adore, Grew kind and friendly as before, And every torn and mangled limb Was safe and sound restored by him. Thenceforth this bow, the gem of bows, That freed the God of Gods from foes, Stored by our great forefathers lay A treasure and a pride for aye. Once, as it chanced, I ploughed the ground, When sudden, 'neath the share was found An infant springing from the earth, Named Sítá from her secret birth.246 In strength and grace the maiden grew, My cherished daughter, fair to view. also here Rudra and Bhava) smote the Gods because he had not been invited to share the sacred oblations with them, seems to refer to the origin of the worship ofZiva, to its increase and to the struggle it maintained with other older forms of worship.” G ORRESIO {FNS . 246 Sítá means a furrow. “Great Erectheus swayed, That owed his nurture to the blue-eyed maid, But from the teeming furrow took his birth, The mighty offspring of the foodful earth.” Iliad, Book II.
- **Translation**: 

---

### Verse 20 (Ramayan 0.280)
- **Original**: 262 The Ramayana I vowed her, of no mortal birth, Meet prize for noblest hero's worth. In strength and grace the maiden grew, And many a monarch came to woo. To all the princely suitors I Gave, mighty Saint, the same reply: “I give not thus my daughter, she Prize of heroic worth shall be.247 To Míthilá the suitors pressed Their power and might to manifest. To all who came with hearts aglow I offeredZiva's wondrous bow. Not one of all the royal band Could raise or take the bow in hand. The suitors' puny might I spurned, And back the feeble princes turned. Enraged thereat, the warriors met, With force combined my town beset. Stung to the heart with scorn and shame, With war and threats they madly came, Besieged my peaceful walls, and long To Míthilá did grievous wrong. There, wasting all, a year they lay, And brought my treasures to decay, Filling my soul, O Hermit chief, With bitter woe and hopeless grief. At last by long-wrought penance I Won favour with the Gods on high, Who with my labours well content A four-fold host to aid me sent. Then swift the baffled heroes fled To all the winds discomfited— 247 “The whole story of Sítá, as will be seen in the course of the poem has a great analogy with the ancient myth of Proserpine.” G ORRESIO {FNS .
- **Translation**: 

---

