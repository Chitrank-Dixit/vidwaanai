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

### Verse 1 (Ramayana 0.1226)
- **Original**: 1208 The Ramayana Spake to Sugríva words like these; “Those stately trees in beauty rise, Fair as a cloud in autumn skies. I fain, my friend, would learn from thee What pleasant grove is that I see.” Thus Ráma spake, the mighty souled; And thus his tale Sugríva told: “That, Ráma, is a wide retreat That brings repose to weary feet. Bright streams and fruit and roots are there, And shady gardens passing fair. There, neath the roof of hanging boughs, The sacred Seven maintained their vows. Their heads in dust were lowly laid, In streams their nightly beds were made. Each seventh night they broke their fast, But air was still their sole repast, And when seven hundred years were spent To homes in heaven the hermits went. Their glory keeps the garden yet, With walls of stately trees beset. Scarce would the Gods and demons dare, By Indra led, to enter there. No beast that roams the wood is found, No bird of air, within the bound; Or, thither if they idly stray, They find no more their homeward way. You hear at times mid dulcet tones The chime of anklets, rings, and zones. You hear the song and music sound, And heavenly fragrance breathes around,
- **Translation**: 

---

### Verse 2 (Ramayana 0.1227)
- **Original**: Canto XIII. The Return To Kishkindhá. 1209 There duly burn the triple fires577 Where mounts the smoke in curling spires, And, in a dun wreath, hangs above The tall trees, like a brooding dove. Round branch and crest the vapours close Till every tree enveloped shows A hill of lazulite when clouds Hang round it with their misty shrouds. With LakshmaG, lord of Raghu's line, In reverent guise thine head incline, And with fixt heart and suppliant hand Give honour to the sainted band. They who with faithful hearts revere The holy Seven who harboured here, Shall never, son of Raghu, know In all their lives an hour of woe.” Then Ráma and his brother bent, And did obeisance reverent With suppliant hand and lowly head, Then with Sugríva onward sped. Beyond the sainted Seven's abode Far on their way the chieftains strode, And great Kishkindhá's portal gained, The royal town where Báli reigned. Then by the gate they took their stand All ready armed a noble band, And burning every one To slay in battle, hand to hand, Their foeman, Indra's son. 577 Called respectively Gárhapatya, Áhavaniya, and DakshiGa, household, sacrificial, and southern.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1228)
- **Original**: 1210 The Ramayana Canto XIV. The Challenge. They stood where trees of densest green Wove round their forms a veiling screen. O'er all the garden's pleasant shade The eyes of King Sugríva strayed,[341] And, as on grass and tree he gazed, The fires of wrath within him blazed. Then like a mighty cloud on high, When roars the tempest through the sky, Girt by his friends he thundered out His dread sky-rending battle-shout Like some proud lion in his gait, Or as the sun begins his state, Sugríva let his quick glance rest On Ráma whom he thus addressed: “There is the seat of Báli's sway, Where flags on wall and turret play, Which mighty bands of Vánars hold, Rich in all arms and store of gold. Thy promise to thy mind recall That Báli by thy hand shall fall. As kindly fruits adorn the bough. So give my hopes their harvest now.” In suppliant tone the Vánar prayed, And Raghu's son his answer made: “By LakshmaG's hand this flowery twine Was wound about thee for a sign. The wreath of giant creeper throws About thy form its brillant glows, As though about the sun were set The bright stars for a coronet. One shaft of mine this day, dear friend,
- **Translation**: 

---

### Verse 4 (Ramayana 0.1229)
- **Original**: Canto XIV. The Challenge. 1211 Thy sorrow and thy fear shall end. And, from the bowstring freed, shall be Giver of freedom, King, to thee. Then come, Sugríva, quickly show, Where'er he lie, thy bitter foe; And let my glance the wretch descry Whose deeds, a brother's name belie. Yea, soon in dust and blood o'erthrown Shall Báli fall and gasp and groan. Once let this eye the foeman see, Then, if he live to turn and flee, Despise my puny strength, and shame With foul opprobrium Ráma's name. Hast thou not seen his hand, O King, Through seven tall trees one arrow wing? Still in that strength securely trust, And deem thy foeman in the dust. In all my days, though surely tried By grief and woe, I ne'er have lied; And still by duty's law restrained Will ne'er with falsehood's charge be stained. Cast doubt away: the oath I sware Its kindly fruit shall quickly bear, As smiles the land with golden grain By mercy of the Lord of rain. Oh, warrior to the gate I defy Thy foe with shout and battle-cry, Till Báli with his chain of gold Come speeding from his royal hold. Proud hearts, with warlike fire aglow, Brook not the challenge of a foe: Each on his power and might relies, And most before his ladies eyes. King Báli loves the fray too well
- **Translation**: 

---

### Verse 5 (Ramayana 0.1230)
- **Original**: 1212 The Ramayana To linger in his citadel, And, when he hears thy battle-shout, All wild for war will hasten out.” He spoke. Sugríva raised a cry That shook and rent the echoing sky, A shout so fierce and loud and dread That stately bulls in terror fled, Like dames who fly from threatened stain In some ignoble monarch's reign. The deer in wild confusion ran Like horses turned in battle's van. Down fell the birds, like Gods who fall When merits fail,578 at that dread call. So fiercely, boldened for the fray, The offspring of the Lord of Day Sent forth his furious shout as loud As thunder from a labouring cloud, Or, where the gale blows fresh and free, The roaring of the troubled sea. Canto XV. Tárá. 578 The store of merit accumulated by a holy or austere life secures only a temporary seat in the mansion of bliss. When by the lapse of time this store is exhausted, return to earth is unavoidable.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1231)
- **Original**: Canto XV. Tárá. 1213 That shout, which shook the land with fear, In thunder smote on Báli's ear, Where in the chamber barred and closed The sovereign with his dame reposed. Each amorous thought was rudely stilled, And pride and rage his bosom filled. His angry eyes flashed darkly red, And all his native brightness fled, As when, by swift eclipse assailed, The glory of the sun has failed. While in his fury uncontrolled He ground his teeth, his eyeballs rolled, He seemed a lake wherein no gem Of blossom decks the lotus stem. He heard, and with indignant pride Forth from the bower the Vánar hied. And the earth trembled at the beat And fury of his hastening feet. But Tárá to her consort flew, Her loving arms around him threw, And trembling and bewildered, gave Wise counsel that might heal and save: “O dear my lord, this rage control That like a torrent floods thy soul, And cast these idle thoughts away Like faded wreath of yesterday, O tarry till the morning light, Then, if thou wilt, go forth and fight. [342] Think not I doubt thy valour, no; Or deem thee weaker than thy foe, Yet for a while would have thee stay Nor see thee tempt the fight to-day. Now list, my loving lord, and learn The reason why I bid thee turn.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1232)
- **Original**: 1214 The Ramayana Thy foeman came in wrath and pride, And thee to deadly fight defied. Thou wentest out: he fought, and fled Sore wounded and discomfited. But yet, untaught by late defeat, He comes his conquering foe to meet, And calls thee forth with cry and shout: Hence spring, my lord, this fear and doubt. A heart so bold that will not yield, But yearns to tempt the desperate field, Such loud defiance, fiercely pressed, On no uncertain hope can rest. So lately by thine arm o'erthrown, He comes not back, I ween, alone. Some mightier comrade guards his side, And spurs him to this burst of pride. For nature made the Vánar wise: On arms of might his hope relies; And never will Sugríva seek A friend whose power to save is weak. Now listen while my lips unfold The wondrous tale my Angad told. Our child the distant forest sought, And, learnt from spies, the tidings brought. Two sons of Da[aratha, sprung From old Ikshváku, brave and young, Renowned in arms, in war untamed— Ráma and LakshmaG are they named— Have with thy foe Sugríva made A league of love and friendly aid. Now Ráma, famed for exploit high, Is bound thy brother's firm ally,
- **Translation**: 

---

### Verse 8 (Ramayana 0.1233)
- **Original**: Canto XV. Tárá. 1215 Like fires of doom579 that ruin all He makes each foe before him fall. He is the suppliant's sure defence, The tree that shelters innocence. The poor and wretched seek his feet: In him the noblest glories meet. With skill and knowledge vast and deep His sire's commands he loved to keep; With princely gifts and graces stored As metals deck the Mountains' Lord.580 Thou canst not, O my hero, stand Before the might of Ráma's hand; For none may match his powers or dare With him in deeds of war compare. Hear, I entreat, the words I say, Nor lightly turn my rede away. O let fraternal discord cease, And link you in the bonds of peace. Let consecrating rites ordain Sugríva partner of thy reign. Let war and thoughts of conflict end, And be thou his and Ráma's friend, Each soft approach of love begin, And to thy soul thy brother win; For whether here or there he be, Thy brother still, dear lord, is he. Though far and wide these eyes I strain A friend like him I seek in vain. Let gentle words his heart incline, And gifts and honours make him thine, Till, foes no more, in love allied, You stand as brothers side by side. 579 The conflagration which destroys the world at the end of a Yuga or age. 580 Himálaya.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1234)
- **Original**: 1216 The Ramayana Thou in high rank wast wont to hold Sugríva, formed in massive mould; Then come, thy brother's love regain, For other aids are weak and vain. If thou would please my soul, and still Preserve me from all fear and ill, I pray thee by thy love be wise And do the thing which I advise. Assuage thy fruitless wrath, and shun The mightier arms of Raghu's son; For Indra's peer in might is he, A foe too strong, my lord, for thee.” Canto XVI. The Fall Of Báli. Thus Tárá with the starry eyes581 Her counsel gave with burning sighs. But Báli, by her prayers unmoved, Spurned her advice, and thus reproved: “How may this insult, scathe, and scorn By me, dear love, be tamely born? My brother, yea my foe, comes nigh And dares me forth with shout and cry. Learn, trembler! that the valiant, they Who yield no step in battle fray, Will die a thousand deaths but ne'er An unavenged dishonour bear. Nor, O my love, be thou dismayed 581 Tárá means“star.” The poet plays upon the name by comparing her beauty to that of the Lord of stars, the Moon.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1235)
- **Original**: Canto XVI. The Fall Of Báli. 1217 Though Ráma lend Sugríva aid, For one so pure and duteous, one Who loves the right, all sin will shun, Release me from thy soft embrace, And with thy dames thy steps retrace: Enough already, O mine own, Of love and sweet devotion shown. Drive all thy fear and doubt away; I seek Sugríva in the fray His boisterous rage and pride to still, And tame the foe I would not kill. My fury, armed with brandished trees, Shall strike Sugríva to his knees: [343] Nor shall the humbled foe withstand The blows of my avenging hand, When, nerved by rage and pride, I beat The traitor down beneath my feet. Thou, love, hast lent thine own sweet aid, And all thy tender care displayed; Now by my life, by these who yearn To serve thee well, I pray thee turn. But for a while, dear dame, I go To come triumphant o'er the foe.” Thus Báli spake in gentlest tone: Soft arms about his neck were thrown; Then round her lord the lady went With sad steps slow and reverent. She stood in solemn guise to bless With prayers for safety and success, Then with her train her chamber sought By grief and racking fear distraught.
- **Translation**: 

---

### Verse 11 (Ramayana 0.1236)
- **Original**: 1218 The Ramayana With serpent's pantings fierce and fast King Báli from the city passed. His glance, as each quick breath he drew, Around to find the foe he threw, And saw where fierce Sugríva showed His form with golden hues that glowed, And, as a fire resplendent, stayed To meet his foe in arms arrayed. When Báli, long-armed chieftain, found Sugríva stationed on the ground, Impelled by warlike rage he braced His warrior garb about his waist, And with his mighty arm raised high Rushed at Sugríva with a cry. But when Sugríva, fierce and bold, Saw Báli with his chain of gold, His arm he heaved, his hand he closed, And face to face his foe opposed. To him whose eyes with fury shone, In charge impetuous rushing on, Skilled in each warlike art and plan, Báli with hasty words began: “My ponderous hand, to fight addressed With fingers clenched and arm compressed Shall on thy death doomed brow descend And, crashing down, thy life shall end.” He spoke; and wild with rage and pride, The fierce Sugríva thus replied: “Thus let my arm begin the strife And from thy body crush the life.” Then Báli, wounded and enraged, With furious blows the battle waged. Sugríva seemed, with blood-streams dyed,
- **Translation**: 

---

### Verse 12 (Ramayana 0.1237)
- **Original**: Canto XVI. The Fall Of Báli. 1219 A hill with fountains in his side. But with his native force unspent A Sál tree from the earth he rent, And like the bolt of Indra smote On Báli's head and chest and throat. Bruised by the blows he could not shield, Half vanquished Báli sank and reeled, As sinks a vessel with her freight Borne down by overwhelming weight. Swift as SuparGa's582 swiftest flight In awful strength they rushed to fight: So might the sun and moon on high Encountering battle in the sky. Fierce and more fierce, as fought the foes, The furious rage of combat rose. They warred with feet and arms and knees, With nails and stones and boughs and trees, And blows descending fast as rain Dyed each dark form with crimson stain, While like two thunder-clouds they met With battle-cry and shout and threat. Then Ráma saw Sugríva quail, Marked his worn strength grow weak and fail. Saw how he turned his wistful eye To every quarter of the sky. His friend's defeat he could not brook, Bent on his shaft an eager look, Then burned to slay the conquering foe, And laid his arrow on the bow. As to an orb the bow he drew Forth from the string the arrow flew Like Fate's tremendous discus hurled 582 SuparGa, the Well-winged, is another name of Garu a the King of Birds. See p. 28, Note.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1238)
- **Original**: 1220 The Ramayana By Yáma 583 forth to end the world. So loud the din that every bird The bow-string's clans with terror heard, And wildly fled the affrighted deer As though the day of doom were near. So, deadly as the serpent's fang, Forth from the string the arrow sprang. Like the red lightning's flash and flame It flew unerring to its aim, And, hissing murder through the air, Pierced Báli's breast, and quivered there. Struck by the shaft that flew so well The mighty Vánar reeled and fell, As earthward Indra's flag they pull When A [víní's fair moon is full.584 Canto XVII. Báli's Speech. Like some proud tree before the blast Brave Báli to the ground was cast, Where prostrate in the dust he rolled Clad in the sheen of glistening gold,[344] 583 The God of Death. 584 The flag-staff erected in honour of the God Indra is lowered when the festival is over. A[víní in astronomy is the head of Aries or the first of the twenty-eight lunar mansions or asterisms.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1239)
- **Original**: Canto XVII. Báli's Speech. 1221 As when uptorn the standard lies Of the great God who rules the skies. When low upon the earth was laid The lord whom Vánar tribes obeyed, Dark as a moonless sky no more His land her joyous aspect wore. Though low in dust and mire was rolled The form of Báli lofty-souled, Still life and valour, might and grace Clung to their well-loved dwelling-place. That golden chain with rich gems set, The choicest gift of Sákra,585 yet Preserved his life nor let decay Steal strength and beauty's light away. Still from that chain divinely wrought His dusky form a glory caught, As a dark cloud, when day is done, Made splendid by the dying sun. As fell the hero, crushed in fight, There beamed afar a triple light From limbs, from chain, from shaft that drank His life-blood as the warrior sank. The never-failing shaft, impelled By the great bow which Ráma held, Brought bliss supreme, and lit the way To Brahmá's worlds which ne'er decay.586 Ráma and LakshmaG nearer drew The mighty fallen foe to view, Mahendra's son, the brave and bold, 585 Indra the father of Báli. 586 It is believed that every creature killed by Ráma obtained in consequence immediate beatitude. “And blessed the hand that gave so dear a death.”
- **Translation**: 

---

### Verse 15 (Ramayana 0.1240)
- **Original**: 1222 The Ramayana The monarch with his chain of gold, With lustrous face and tawny eyes, Broad chest, and arms of wondrous size, Like Lord Mahendra fierce in fight, Or VishGu's never-conquered might, Now fallen like Yayáti587 sent From heaven, his store of merit spent, Like the bright flame that pales and dies, Like the great sun who fires the skies, Doomed in the general doom to fall When time shall end and ruin all. The wounded Báli, when he saw Ráma and LakshmaG nearer draw, Keen words to Raghu's son, impressed With justice' holy stamp, addressed: “What fame, from one thou hast not slain In front of battle, canst thou gain, Whose secret hand has laid me low When madly fighting with my foe? From every tongue thy glory rings, A scion of a line of kings, True to thy vows, of noblest race, With every gentle gift and grace: Whose tender heart for woe can feel, And joy in every creature's weal: Whose breast with high ambition swells, Knows duty's claim and ne'er rebels. They praise thy valour, patience, ruth, 587 “Yayáti was invited to heaven by Indra, and conveyed on the way thither by Mátali, Indra's charioteer. He afterwards returned to earth where, by his virtuous administration he rendered all his subjects exempt from passion and decay.” G ARRETT 'S C. D.OF INDIA {FNS .
- **Translation**: 

---

### Verse 16 (Ramayana 0.1241)
- **Original**: Canto XVII. Báli's Speech. 1223 Thy firmness, self-restraint, and truth: Thy hand prepared for sin's control, All virtues of a princely soul. I thought of all these gifts of thine, And glories of an ancient line, I set my Tárá's tears at naught, I met Sugríva and we fought. O Ráma, till this fatal morn I held that thou wouldst surely scorn To strike me as I fought my foe And thought not of a stranger's blow, But now thine evil heart is shown, A yawning well with grass o'ergrown. Thou wearest virtue's badge,588 but guile And meanest sin thy soul defile. I took thee not for treacherous fire, A sinner clad in saint's attire; Nor deemed thou idly wouldst profess The show and garb of righteousness. In fenced town, in open land, Ne'er hast thou suffered at this hand, Nor canst of proud contempt complain: Then wherefore is the guiltless slain? My harmless life in woods I lead, On forest fruits and roots I feed. My foeman in the field I sought, And ne'er with thee, O Ráma, fought. Upon thy limbs, O King, I see The raiment of a devotee; And how can one like thee, who springs From a proud line of ancient kings, Beneath fair virtue's mask, disgrace 588 The ascetic's dress which he wore during his exile.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1242)
- **Original**: 1224 The Ramayana His lineage by a deed so base? From Raghu is thy long descent, For duteous deeds prëeminent: Why, sinner clad in saintly dress, Roamest thou through the wilderness? Truth, valour, justice free from spot, The hand that gives and grudges not, The might that strikes the sinner down, These bring a prince his best renown. Here in the woods, O King, we live On roots and fruit which branches give.589[345] Thus nature framed our harmless race: Thou art a man supreme in place. Silver and gold and land provoke The fierce attack, the robber's stroke, Canst thou desire this wild retreat, The berries and the fruit we eat? 'Tis not for mighty kings to tread The flowery path, by pleasure led. Theirs be the arm that crushes sin, Theirs the soft grace to woo and win: The steadfast will that guides the state, Wise favour to the good and great; And for all time are kings renowned Who blend these arts and ne'er confound. But thou art weak and swift to ire, Unstable, slave of each desire. Thou tramplest duty in the dust, And in thy bow is all thy trust. 589 There is much inconsistency in the passages of the poem in which the Vánars are spoken of, which seems to point to two widely different legends. The Vánars are generally represented as semi-divine beings with preternatural powers, living in houses and eating and drinking like men sometimes as here, as monkeys pure and simple, living is woods and eating fruit and roots.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1243)
- **Original**: Canto XVII. Báli's Speech. 1225 Thou carest naught for noble gain, And treatest virtue with disdain, While every sense its captive draws To follow pleasure's changing laws. I wronged thee not in word or deed, But by thy deadly dart I bleed. What wilt thou, mid the virtuous, say To purge thy lasting stain away? All these, O King, must sink to hell, The regicide, the infidel, He who in blood and slaughter joys, A Bráhman or a cow destroys, Untimely weds in law's despite Scorning an elder brother's right,590 Who dares his Teacher's bed ascend, The miser, spy, and treacherous friend. These impious wretches, one and all, Must to the hell of sinners fall. My skin the holy may not wear, Useless to thee my bones and hair; Nor may my slaughtered body be The food of devotees like thee. These five-toed things a man may slay And feed upon the fallen prey; The mailed rhinoceros may die, And, with the hare his food supply. Iguanas he may kill and eat, 590 For a younger brother to marry before the elder is a gross violation of Indian law and duty. The same law applied to daughters with the Hebrews:“It must not be so done in our country to give the younger before the first-born.” G ENESIS {FNS xix. 26.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1244)
- **Original**: 1226 The Ramayana With porcupine and tortoise meat.591 But all the wise account it sin To touch my bones and hair and skin. My flesh they may not eat; and I A useless prey, O Ráma, die. In vain my Tárá reasoned well, On dull deaf ears her counsel fell. I scorned her words though sooth and sweet, And hither rushed my fate to meet. Ah for the land thou rulest! she Finds no protection, lord, from thee, Neglected like some noble dame By a vile husband dead to shame. Mean-hearted coward, false and vile, Whose cruel soul delights in guile, Could Da[aratha, noblest king, Beget so mean and base a thing? Alas! an elephant, in form Of Ráma, in a maddening storm Of passion casting to the ground The girth of law592 that clipped him round, Too wildly passionate to feel The prick of duty's guiding steel,593 Has charged me unawares, and dead I fall beneath his murderous tread. How, stained with this my base defeat, 591 “The hedgehog and porcupine, the lizard, the rhinoceros, the tortoise, and the rabbit or hare, wise legislators declare lawful food among five-toed animals.” M ANU {FNS , v. 18. 592 “He can not buckle his distempered cause Within the belt of rule.” M ACBETH {FNS . 593 The Anku[ or iron hook with which an elephant is driven and guided.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1245)
- **Original**: Canto XVII. Báli's Speech. 1227 How wilt thou dare, where good men meet, To speak, when every tongue will blame With keen reproach this deed of shame? Such hero strength and valour, shown Upon the innocent alone, Thou hast not proved in manly strife On him who robbed thee of thy wife. Hadst thou but fought in open field And met me boldly unconcealed, This day had been thy fate to fall, Slain by this hand, to Yáma's hall. In vain I strove, and struck by thee Fell by a hand I could not see. Thus bites a snake, for sins of yore, A sleeping man who wakes no more. Sugríva's foeman thou hast killed, And thus his heart's desire fulfilled; But, Ráma, hadst thou sought me first, And told the hope thy soul has nursed, That very day had I restored The Maithil lady to her lord; And, binding RávaG with a chain, Had laid him at thy feet unslain. [346] Yea, were she sunk in deepest hell, Or whelmed beneath the ocean's swell, I would have followed on her track And brought the rescued lady back, As Hayagríva594 once set free 594 Hayagríva, Horse-necked, is a form of VishGu.
- **Translation**: 

---

