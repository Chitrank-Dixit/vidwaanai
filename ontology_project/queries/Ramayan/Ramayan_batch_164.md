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

### Verse 1 (Ramayana 0.1306)
- **Original**: 1288 The Ramayana And in his own all-conquering might The venom of its deadly bite. Prince Angad marked his angry look, And every hope his heart forsook. Then, his large eyes with fury red, To Angad LakshmaG turned and said: “Go tell the king that LakshmaG waits For audience at the city gates, Whose heart, O tamer of thy foes, Is heavy with his brother's woes. Bid him to Ráma's word attend, And ask if he will aid his friend. Go, let the king my message learn: Then hither with all speed return.” Prince Angad heard and wild with grief Cried as he looked upon the chief: “'Tis LakshmaG's self: impelled by ire He seeks the city of my sire.” At the fierce words and furious look Of Raghu's son he quailed and shook. Back through the city gates he sped, And, laden with the tale of dread, Sought King Sugríva, filled his ears And Rumá's with his doubts and fears. To Rumá and the king he bent, And clasped their feet most reverent, Clasped the dear feet of Tárá, too, And told the startling tale anew.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1307)
- **Original**: Canto XXXI. The Envoy. 1289 But King Sugríva's ear was dulled, By love and wine and languor lulled, Nor did the words that Angad spake The slumberer from his trance awake. But soon as Raghu's son came nigh The startled Vánars raised a cry, And strove to win his grace, while dread Each anxious heart disquieted. They saw, and, as they gathered round, Rose from the mighty throng a sound Like torrents when they downward dash, Or thunder with the lightning's flash. The shouting of the Vánars broke Sugríva's slumber, and he woke: Still with the wine his eyes were red, His neck with flowers was garlanded. Roused at the voice of Angad came Two Vánar lords of rank and fame; One Yaksha, one Prabháva hight,— Wise counsellors of gain and right. They came and raised their voices high, And told that Raghu's son was nigh: “Two brothers steadfast in their truth, Each glorious in the bloom of youth, Worthy of rule, have left the skies, And clothed their forms in men's disguise. One at thy gates, in warlike hands Holding his mighty weapon, stands. His message is the charioteer That brings the eager envoy near, Urged onward by his bold intent, And by the hest of Ráma sent.” The gathered Vánars saw and fled, And raised aloud their cry of dread.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1308)
- **Original**: 1290 The Ramayana Son of Queen Tárá, Angad ran To parley with the godlike man. Still fiery-eyed with rage and hate Stands LakshmaG at the city gate, And trembling Vánars scarce can fly Scathed by the lightning of his eye. “Go with thy son, thy kith and kin, The favour of the prince to win, And bow thy reverent head that so His fiery wrath may cease to glow. What righteous Ráma bids thee, do, And to thy plighted word be true.” Canto XXXII. Hanumán's Counsel. Sugríva heard, and, trained and tried In counsel, to his lords replied: “No deed of mine, no hasty word The anger of the prince has stirred. But haply some who hate me still And watch their time to work me ill, Have slandered me to Raghu's son, Accused of deeds I ne'er have done. Now, O my lords— for you are wise— Speak truly what your hearts advise, And, pondering each event, inquire The reason of the prince's ire. No fear have I of LakshmaG: none: No dread of Raghu's mightier son. But wrath, that fires a friendly breast Without due cause, disturbs my rest.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1309)
- **Original**: Canto XXXII. Hanumán's Counsel. 1291 With labour light is friendship gained, But with severest toil maintained. And doubt is strong, and faith is weak, [364] And friendship dies when traitors speak. Hence is my troubled bosom cold With fear of Ráma lofty-souled; For heavy on my spirit weigh His favours I can ne'er repay.” He ceased: and Hanumán of all The Vánars in the council hall In wisdom first, and rank, expressed The thoughts that filled his prudent breast: “No marvel thou rememberest yet The service thou shouldst ne'er forget, How the brave prince of Raghu's seed Thy days from fear and peril freed; And Báli for thy sake o'erthrew, Whom Indra's self might scarce subdue. I doubt not Ráma's anger burns For the scant love thy heart returns. For this he sends his brother, him Whose glory never waxes dim. Sunk in repose thy careless eye Marks not the seasons as they fly, Nor sees that autumn has begun With dark blooms opening to the sun. Clear is the sky: no cloudlet mars The splendour of the shining stars. The balmy air is soft and still, And clear and bright are lake and rill. Thou heedest not with blinded eyes The hour for warlike enterprise. Hence LakshmaG hither comes to break
- **Translation**: 

---

### Verse 5 (Ramayana 0.1310)
- **Original**: 1292 The Ramayana Thy slothful trance and bid thee wake. Then, Monarch, with a patient ear The high-souled Ráma's message hear, Which, reft of wife and realm and friends, Thus by another's mouth he sends. Thou, Vánar King, hast done amiss: And now I see no way but this: Before his envoy humbly stand And sue for peace with suppliant hand. High duty bids a courtier seek His master's weal, and freely speak. So by no thought of fear controlled My speech, O King, is free and bold, For Ráma, if his anger glow, Can, with the terrors of his bow This earth with all the Gods subdue, Gandharvas,635 and the demon crew. Unwise to stir his wrathful mood Whose favour must again be wooed. And, most of all, unwise for one Grateful like thee for service done. Go with thy son and kinsmen: bend Thy humble head and greet thy friend. And, like a fond obedient spouse, Be faithful to thy plighted vows.” Canto XXXIII. Lakshman's Entry. 635 Indra's associates in arms, and musicians of his heaven.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1311)
- **Original**: Canto XXXIII. Lakshman's Entry. 1293 Through the fair city LakshmaG came, Invited in Sugríva's name. Within the gates the guardian bands, Of Vánars raised their suppliant hands, And in their ordered ranks, amazed, Upon the princely hero gazed, They marked each burning breath he drew, The fury of his soul they knew. Their hearts were chilled with sudden fear: They gazed, but dared not venture near, Before his eyes the city, gay With gems and flowery gardens, lay, Where fane and palace rose on high, And things of beauty charmed the eye. Where trees of every blossom grew Yielding their fruit in season due To Vánars of celestial seed Who wore each varied form at need, Fair-faced and glorious with the shine Of heavenly robes and wreaths divine. There sandal, aloe, lotus bloomed, And there delicious breath perfumed The city's broad street, redolent Of sugary mead636 and honey scent. There many a lofty palace rose Like Vindhya or the Lord of Snows, And with sweet murmur sparkling rills Leapt lightly down the sheltering hills. On many a glorious palace, raised For prince and noble,637 Lakshma G gazed: 636 Maireya, a spirituous liquor from the blossoms of the Lythrum fruticosum, with sugar, &c. 637 Their names are as follows: Angad, Maínda, Dwida, Gavaya, Gaváksha, Gaja,Zarabha, Vidyunmáli, Sampáti, Súryáksa, Hanumán, Vírabáhu, Subáhu,
- **Translation**: 

---

### Verse 7 (Ramayana 0.1312)
- **Original**: 1294 The Ramayana Like clouds of paly hue they shone With fragrant wreaths that hung thereon: There wealth of jewels was enshrined, And fairer gems of womankind. There gleamed, of noble height and size, Like Indra's mansion in the skies, Protected by a crystal fence Of rock, the royal residence, With roof and turret high and bright Like Mount Kailása's loftiest height. There blooming trees, Mahendra's gift, High o'er the walls were seen to lift Their golden fruited boughs, that made With leaf and flower delicious shade. He saw a band of Vánars wait,[365] Wielding their weapons, at the gate Where golden portals flashed between Celestial garlands red and green. Within Sugríva's fair abode Unchecked the mighty hero strode, As when the sun of autumn shrouds His glory in a pile of clouds. Through seven wide courts he quickly passed, And reached the royal tower at last, Where seats were set with couch and bed Of gold and silver richly spread. While the young chieftain's feet drew near The sound of music reached his ear, As the soft breathings of the flute Came blending with the voice and lute. Then beauty showed her youth and grace And varied charm of form and face: Nala, Kúmuda, SusheGa, Tára, Jámbuvatu, Dadhivakra, Níla, Supátala, and Sunetra.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1313)
- **Original**: Canto XXXIII. Lakshman's Entry. 1295 Soft bright-eyed creatures, fair and young,— Gay garlands round their necks were hung, And greater charms to each were lent By richest dress and ornament. He saw the calm attendants wait About their lord in careless state, Heard women's girdles chime in sweet Accordance with their tinkling feet. He heard the anklet's silvery sound, He saw the calm that reigned around, And o'er him, as he listened, came A rush of rage, a flood of shame. He drew his bowstring: with the clang From ease to west the welkin rang: Then in his modest mood withdrew A little from the ladies' view. And sternly silent stood apart, While wrath for Ráma filled his heart. Sugríva knew the sounding string, And at the call the Vánar king Sprang swiftly from his golden seat, And feared the coming prince to meet. Then with cold lips that terror dried To beauteous Tárá thus he cried: “What cause of anger, O my spouse Fair with the charm of lovely brows, Sets LakshmaG's gentle breast on fire, And brings him in unwonted ire? Say, canst thou see, O faultless dame, A cause to fill his soul with flame? For there must be a reason when Such fury stirs the king of men. Reveal the sin, if sin of mine Anger the lord of Raghu's line.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1314)
- **Original**: 1296 The Ramayana Or go thyself, his rage subdue, And with soft words his favour woo. Soon as on thee his eyes are set His heart this anger will forget, For men like him of lofty mind Are never stern with womankind. First let thy gentle speech disarm His fury, and his spirit charm, And I, from fear of peril free, The conqueror of his foes will see.” She heard: with faltering steps and slow, With eyes that shone with trembling glow, With gold-girt body gently bent To meet the stranger prince she went. When Lakshma G saw the Vánar queen With tranquil eyes and modest mien, Before the dame he bent his head, And anger, at her presence, fled. Made bold by draughts of wine, and cheered By LakshmaG's look no more she feared, And in the trust his favour lent She thus addressed him eloquent: “Whence springs thy burning fury? say: Who dares thy will to disobey? Who checks the maddened flames that seize On forests full of withered trees?” Then LakshmaG spoke, her mind to ease, His kind reply in words like these:
- **Translation**: 

---

### Verse 10 (Ramayana 0.1315)
- **Original**: Canto XXXIII. Lakshman's Entry. 1297 “Thy lord his days in pleasure spends, Heedless of duty and of friends, Nor dost thou mark, though fondly true, The evil path his steps pursue. He cares not for affairs of state, Nor us forlorn and desolate, But sits a mere spectator still, A sensual slave to pleasure's will. Four months were fixed, the time agreed When he should help us in our need: But, bound in toils of pleasure fast, He sees not that the months are past. Where beats the heart which draughts of wine To virtue or to gain incline? Hast thou not heard those draughts destroy Virtue and gain and love and joy? For those who, helped at need, refuse Their aid in turn, their virtue lose: And they who scorn a friend disdain A treasure naught may buy again. Thy lord has cast his friend away, Nor feared from virtue's path to stray, If this be true, declare, O dame Who knowest duty's every claim, What further work remains for us Deceived and disappointed thus.” She listened, for his words were kind, Where virtue showed with gain combined, And thus in turn the prince addressed, As hope was rising in his breast: “No time, no cause of wrath I see With those who live and honour thee: And thou shouldst bear without offence
- **Translation**: 

---

### Verse 11 (Ramayana 0.1316)
- **Original**: 1298 The Ramayana Thy servant's fitful negligence. I know the seasons glide away, While Ráma maddens at delay I know what deed our thanks has earned, I know that grace should be returned. But still I know, whate'er befall, That conquering love is lord of all;[366] Know where Sugríva's thoughts, possessed By one absorbing passion, rest. But he whom sensual joys debase Heeds not the claim of time and place, And sees not with his blinded sight His duty or his gain aright. O pardon him who loves me! spare The Vánar caught in pleasure's snare, And once again let Ráma grace With favour him who rules our race. E'en royal saints, whose chief delight Was penance and austerest rite, At love's commandment have unbent, Beguiled by sweetest blandishment. And know, Sugríva, roused at last, The order to his lords has passed, And, long by love and bliss delayed, Wakes all on fire your hopes to aid. A countless host his city fills, New-gathered from a thousand hills: Impetuous chiefs, who wear at need Each varied form, his legions lead. Come then, O hero, kept aloof By modest awe, nor fear reproof: A faithful friend untouched by blame May look upon another's dame.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.1317)
- **Original**: Canto XXXIV. Lakshman's Speech. 1299 He passed within, by Tárá pressed, And by his own impatient breast, Refulgent there in sunlike sheen Sugríva on his throne was seen. Gay garlands round his neck were twined, And Rumá by her lord recline. Canto XXXIV. Lakshman's Speech. Sugríva started from his rest With doubt and terror in his breast. He heard the prince's furious tread He saw his eyes glow fiercely red. Swift sprang the monarch to his feet Upstarting from his golden seat. Rose Rumá and her fellows, too, And closely round Sugríva drew, As round the moon's full glory stand Attendant stars in glittering band. Sugríva glanced with reddened eyes, Raised his joined hands in suppliant guise Flew to the door, and rooted there Stood like the tree that grants each prayer.638 And Lakshma G saw, and, fiercely moved, With angry speech the king reproved: 638 The Kalpadruma or Wishing-tree is one of the trees of Svarga or Indra's Paradise: it has the power of granting all desires.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1318)
- **Original**: 1300 The Ramayana “Famed is the prince who loves the truth, Whose soul is touched with tender ruth, Who, liberal, keeps each sense subdued, And pays the debt of gratitude. But all unmeet a king to be, The meanest of the mean is he Who basely breaks the promise made To trusting friends who lent him aid. He sins who for a steed has lied, As if a hundred steeds had died: Or if he lie, a cow to win, Tenfold as heavy is the sin. But if the lie a man betray, Both he and his shall all decay.639 O Vánar King, the thankless man Is worthy of the general ban, Who takes assistance of his friends, And in his turn no service lends. This verse of old by Brahmá sung Is echoed now by every tongue. Hear what He cried in angry mood Bewailing man's ingratitude: “For draughts of wine, for slaughtered cows, For treacherous theft, for broken vows A pardon is ordained: but none For thankless scorn of service done.” Ungrateful, Vánar King, art thou, And faithless to thy plighted vow. For Ráma brought thee help, and yet Thou shunnest to repay the debt: Or, grateful, thou hadst surely pressed To aid the hero in his quest. 639 The meaning is that if a man promises to give a horse and then breaks his word he commits a sin as great as if he had killed a hundred horses.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1319)
- **Original**: Canto XXXV. Tárá's Speech. 1301 Thou art, in vulgar pleasures drowned, False to thy bond in honour bound. Nor yet has Ráma's guileless heart Discerned thee for the thing thou art— A snake who holds the frogs that cries And lures fresh victims as it dies. Brave Ráma, born for glorious fate, Has set thee in thy high estate, And to the Vánars' throne restored, Great-souled himself, their mean-souled lord. Now if thy pride disown what he, High thoughted prince, has done for thee, Struck by his arrows shalt thou fall, And Báli meet in Yáma's hall. Still open, to the gloomy God, Lies the sad path thy brother trod. Then to thy plighted word be true, Nor let thy steps that path pursue. Methinks the shafts of Ráma, shot Like thunderbolts, thou heedest not, Who canst, absorbed in sensual bliss, Thy promise from thy mind dismiss.” [367] Canto XXXV. Tárá's Speech.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1320)
- **Original**: 1302 The Ramayana He ceased: and Tárá starry-eyed Thus to the angry prince replied: “Not to my lord shouldst thou address A speech so fraught with bitterness: Not thus reproached my lord should be, And least of all, O Prince, by thee. He is no thankless coward— no— With spirit dead to valour's glow. From paths of truth he never strays, Nor wanders in forbidden ways. Ne'er will Sugríva's heart forget, By Ráma saved, the lasting debt. Still in his grateful breast will live The succour none but he could give. Restored to fame by Ráma's grace, To empire o'er the Vánar race, From ceaseless dread and toil set free, Restored to Rumá and to me: By grief and care and exile tried, New to the bliss so long denied, Like Vi[vámitra once, alas, He marks not how the seasons pass. That saint ten thousand years remained, By sweet Ghritáchí's640 love enchained, And deemed those years, that flew away So lightly, but a single day. O, if those years unheeded flew By him who times and seasons knew, Unequalled for his lofty mind, What marvel meaner eyes are blind? Then be not angry, Raghu's son, And let thy brother feel for one 640 The story is told in Book I, Canto LXIII, but the charmer there is called Menaká.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1321)
- **Original**: Canto XXXV. Tárá's Speech. 1303 Who many a weary year has spent Stranger to love and blandishment. Let not this wrath thy soul inflame, Like some mean wretch unknown to fame: For high and noble hearts like thine Love mercy and to ruth incline, Calm and deliberate, and slow With anger's raging fire to glow. At length, O righteous prince, relent, Nor let my words in vain be spent, This sudden blaze of fury slake, I pray thee for Sugríva's sake. He would renounce at Ráma's call Rumá and Angad, me and all Who call him lord: his gold and grain, The favour of his friend to gain. His arm shall slay the fiend more base In soul than all his impious race, And happy Ráma reunite To Sítá, rival in delight Of the triumphant Moon when he Rejoins his darling RohiGí.641 Ten million million demons guard The gates of Lanká firmly barred. All hope until that host be slain, To smite the robber king is vain. Nor with Sugríva's aid alone May king and host be overthrown. Thus ere he died— for well he knew— Spake Báli, and his words are true. I know not what his proofs might be, 641 RohiGí is the name of the ninth Nakshatra or lunar asterism personified as a daughter of Daksha, and the favourite wife of the Moon. Aldebaran is the principal star in the constellation.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1322)
- **Original**: 1304 The Ramayana But speak the words he spake to me. Hence far and wide our lords are sent To raise the mightiest armament, For their return Sugríva waits Ere he can sally from his gates. Still is the oath Sugríva swore Kept firmly even as before: And the great host this day will be Assembled by the king's decree, Ten thousand thousand troops, who wear The form of monkey and of bear, Prepared for thee the war to wage: Then let thy wrath no longer rage. The matrons of the Vánar race See marks of fury in thy face; They see thine eyes like blood are red, And will not yet be comforted.” Canto XXXVI. Sugríva's Speech. She ceased: and LakshmaG gave assent, Won by her gentle argument. So Tárá's pleading, just and mild, His softening heart had reconciled. His altered mood Sugríva saw, And cast aside the fear and awe Like raiment heavy with the rain Which on his troubled soul had lain. Then quickly to the ground he threw His flowery garland, bright of hue, Which round his royal neck he wore,
- **Translation**: 

---

### Verse 18 (Ramayana 0.1323)
- **Original**: Canto XXXVI. Sugríva's Speech. 1305 And, sobered, was himself once more. Then turning to the princely man In soothing words the king began: “My glory, wealth, and royal sway To other hands had passed away: But Ráma to my rescue came, And gave me back my power and fame. O Lakshma G, say, whose grateful heart [368] Could nurse the hope to pay in part, By service of a life, the deed Of Ráma sprung of heavenly seed? His foeman RávaG shall be slain, And Sítá shall be his again. The hero's side I will not leave, But he the conquest shall achieve. What need of help has he who drew His bow, and one great arrow flew Through seven tall trees, a mountain rent, And cleft the earth with force unspent? What aid needs he who shook his bow, And at the sound the earth below With hill and wood and rooted rock Quaked feverous with the thunder shock? Yet all my legions will I bring, And follow close the warrior king Marching on his impetuous way Fierce RávaG and his hosts to slay. If I be guilty of offence, Careless through love or negligence, Let him his loyal slave forgive; For error cleaves to all who live.” Thus king Sugríva, good and brave, In humble words his answer gave,
- **Translation**: 

---

### Verse 19 (Ramayana 0.1324)
- **Original**: 1306 The Ramayana Softened was LakshmaG's angry mood Who thus his friendly speech renewed: “My brother, Vánar King, will see A champion and a friend in thee. So strong art thou, so brave and bold, So pure in thought, so humble-souled, That thou deservest well to reign And all a monarch's bliss to gain. Lend thou my brother aid, and all His foes beneath his arm will fall. Full well the words thou speakest suit A chieftain wise and resolute. With grateful heart that loves the right, And foot that never yields in fight. O come, and my sad brother cheer Who mourns the wife he holds so dear. O pardon, friend, my harsh address, And Ráma's frantic bitterness.” Canto XXXVII. The Gathering. He ceased: and King Sugríva cried To sage Hanúmán642 by his side: “Summon the Vánar legions, those Who dwell about the Lord of Snows: Those who in Vindhyan groves delight, Kailása's, or Mahendra's height, Dwell on the Five bright Peaks, or where 642 Válmíki and succeeding poets make the second vowel in this name long or short at their pleasure.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1325)
- **Original**: Canto XXXVII. The Gathering. 1307 Mandar's white summit cleaves the air: Wherever they are wandring free In highlands by the western sea, On that east hill whence springs the sun, Or where he sinks when day is done. Call the great chiefs whose legions fill The forests of the Lotus Hill,643 Where every one in strength and size With the stupendous Anjan644 vies. Call those, with tints of burnished gold Whom Mahá [aila's caverns hold: Those who on Dhúmra roam, or hide In the wild woods on Meru's side. Call those who, brilliant as the sun, On high MaháruG leap and run, Quaffing sweet juices that distil From odorous trees upon the hill, Call those whom tranquil haunts delight, Where dwell the sage and anchorite In groves that through their wide extent Exhale a thousand blossoms' scent. Send out, send out: from coast to coast Assemble all the Vánar host: With force, with words, with gifts of price Compel, admonish and entice. Already envoys have been sent 643 Some of the mountains here mentioned are fabulous and others it is im- possible to identify. Sugríva means to include all the mountains of India from Kailás the residence of the God Kuvera, regarded as one of the loftiest peaks of the Himálayas, to Mahendra in the extreme south, from the mountain in the east where the sun is said to rise to Astáchal or the western mountain where he sets. The commentators give little assistance: that Mahá[aila, &c. are certain mountains is about all the information they give. 644 One of the celestial elephants of the Gods who protect the four quarters and intermediate points of the compass.
- **Translation**: 

---

