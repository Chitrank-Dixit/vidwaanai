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

### Verse 1 (Ramayana 0.1266)
- **Original**: 1248 The Ramayana Thus fades the light when Ráhu606 mars The glory of the Lord of Stars.607 All angry thoughts were stayed and stilled And kindly love his bosom filled. His brother's word the chief obeyed And took the chain as Báli prayed. On little Angad standing nigh The dying hero fixed his eye, And, ready from this world to part, Spoke the fond utterance of his heart: “Let time and place thy thoughts employ: In woe be strong, be meek in joy. Accept both pain and pleasure, still Obedient to Sugríva's will. Thou hast, my darling, from the first With tender care been softly nursed; But harder days, if thou wouldst win Sugríva's love, must now begin. To those who hate him ne'er incline, Nor count his foe a friend of thine. In all thy thoughts his welfare seek, Obedient, lowly, faithful, meek. Let no rash suit his bosom pain, Nor yet from due requests abstain.608 Each is a grievous fault, between The two is found the happy mean.” 606 A demon with the tail of a dragon, that causes eclipses by endeavouring to swallow the sun and moon. 607 The Lord of Stars is the Moon. 608 Or the passage may be interpreted:“Be neither too obsequious or affection- ate, nor wanting in due respect or love.”
- **Translation**: 

---

### Verse 2 (Ramayana 0.1267)
- **Original**: Canto XXII. Báli Dead. 1249 Then Báli ceased: his eyeballs rolled In stress of anguish uncontrolled His massive teeth were bared to view, And from the frame the spirit flew. Their lord and leader dead, the crowd Of noblest Vánars shrieked aloud: “Since thou, O King, hast sought the skies All desolate Kishkindhá lies. Her woods, where Vánars loved to rove, Are empty now, and hill and grove. From every eye the light is fled, Since thou, our mighty lord, art dead. Thine was the unwearied arm that bore The brunt of deadly fight of yore With Golabh the Gandharva, when, Lasting through five long years and ten, [352] The dreadful conflict knew no stay In gloom of night, in glare of day; And when the fifteenth year had past Thy dire opponent fell at last. If such a foeman fell beneath Our hero's arm and awful teeth Who freed us from our terror, how Is conquering Báli fallen now?” Then when they saw their leader slain Great anguish seized the Vánar train, Weeping their mighty chief, as when In pastures near a lion's den The cows by sudden fear are stirred, Slain the bold bull who led the herd. And hapless Tárá sank below The whelming waters of her woe, Looked upon Báli's face and fell
- **Translation**: 

---

### Verse 3 (Ramayana 0.1268)
- **Original**: 1250 The Ramayana Beside him whom she loved go well, Like a young creeper clinging round A tall tree prostrate on the ground. Canto XXIII. Tárá's Lament. She kissed her lifeless husband's face, She clasped him in a close embrace, Laid her soft lips upon his head; Then words like these the mourner said: “No words of mine wouldst thou regard, And now thy bed is cold and hard. Upon the rude rough ground o'erthrown, Beneath thee naught but sand and stone. To thee the earth is dearer far Than I and my caresses are, If thou upon her breast wilt lie, And to my words make no reply. Ah my beloved, good and brave, Bold to attack and strong to save, Fate is Sugríva's thrall, and we In him our lord and master see. Lo, by thy bed, a mournful band, Thy Vánar chiefs lamenting stand. O hear thy nobles' groans and cries, O mark thy Angad's weeping eyes, O list to my entreaties, break The chains of slumber and awake. Ah me, my lord, this lowly bed Where rest thy limbs and fallen head,
- **Translation**: 

---

### Verse 4 (Ramayana 0.1269)
- **Original**: Canto XXIII. Tárá's Lament. 1251 Is the cold couch where smitten lay Thy foemen in the bloody fray. O noble heart from blemish free, Lover of war, beloved by me. Why hast thou fled away and left Thy Tárá of all hope bereft? Unwise the father who allows His child to be a warrior's spouse, For, hero, see thy consort's fate, A widow now most desolate, For ever broken is my pride, My hope of lasting bliss has died, And sinking in the lowest deep Of sorrow's sea I pine and weep. Ah, surely not of earthly mould, This stony heart is stern and cold, Or, in a hundred pieces rent, It had not lingered to lament. Dead, dead! my husband, friend, and lord In whom my loving hopes were stored, First in the field, his foemen's dread, My own victorious Báli, dead! A woman when her lord has died, Though children flourish by her side, Though stores of gold her coffers fill, Is called a lonely widow still. Alas, thy bleeding gashes make Around thy limbs a purple lake: Thus slumbering was thy wont to lie On cushions bright with crimson dye. Dark streams of welling blood besmear Thy limbs where dust and mire adhere, Nor have I strength, weighed down by woe, Mine arms about thy form to throw.
- **Translation**: 

---

### Verse 5 (Ramayana 0.1270)
- **Original**: 1252 The Ramayana The issue of this day has brought Sugríva all his wishes sought, For Ráma shot one shaft and he Is freed from fear and jeopardy. Alas, alas, I may not rest My head upon thy wounded breast, Obstructed by the massive dart Deep buried in thy bleeding heart.” Then Níla from his bosom drew The fatal shaft that pierced him through, Like some tremendous serpent deep In caverns of a hill asleep. As from the hero's wound it came, Shot from the shaft a gleam of flame, Like the last flashes of the sun Descending when his course is run. From the wide rent in crimson flood Rushed the full stream of Báli's blood, Like torrents down a mountain's side With golden ore and copper dyed. Then Tárá brushed with tender care The dust of battle from his hair, While her sad eyes poured down their rain Upon her lord untimely slain. Once more she looked upon the dead; Then to her bright-eyed child she said: “Turn hither, turn thy weeping eyes Where low in death thy father lies. By sinful deed and bitter hate Our lord has met his mournful fate. Bright as the sun at early morn To Yáma's halls is Báli borne. Then go, my child, salute the king,
- **Translation**: 

---

### Verse 6 (Ramayana 0.1271)
- **Original**: Canto XXIII. Tárá's Lament. 1253 From whom our bliss and honour spring.” Obedient to his mother's hest His father's feet he gently pressed [353] With twining arms and lingering hands: “Father,” he cried,“here Angad stands.” Then Tárá:“Art thou stern and mute, Regardless of thy child's salute? Hast thou no blessing for thy son, No word for little Angad, none? O, hero, at thy lifeless feet Here with my boy I take my seat, As some sad mother of the herd, By the fierce lion undeterred, Lies moaning by the grassy dell Wherein her lord and leader fell. How, having wrought that awful rite, The sacrifice of deadly fight, Wherein the shaft by Ráma sped Supplied the place of water shed, How hast thou bathed thee at the end Without thy wife her aid to lend?609 Why do mine eyes no more behold Thy bright beloved chain of gold, Which, pleased with thee, the Immortals' King About thy neck vouchsafed to fling? Still lingering on thy lifeless face I see the pride of royal race: Thus when the sun has set, his glow Still rests upon the Lord of Snow. 609 Sacrifices and all religious rites begin and end with ablution, and the wife of the officiating Bráhman takes an important part in the performance of the holy ceremonies.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1272)
- **Original**: 1254 The Ramayana Alas my hero! undeterred Thou wouldst not listen to my word. With tears and prayers I sued in vain: Thou wouldst not listen, and art slain. Gone is my bliss, my glory: I And Angad now with thee will die.” Canto XXIV. Sugríva's Lament. But when Sugríva saw her weep O'erwhelmed in sorrow's rushing deep, Swift through his bosom pierced the sting Of anguish for the fallen king. At the sad sight his eyes beheld A flood of bitter tears outwelled, And, with his bosom racked and rent, To Ráma with his train he went. He came with faltering steps and slow Where Ráma held his mighty bow And arrow like a venomed snake, And to the son of Raghu spake: “Well hast thou kept, O King, thy vow: The promised fruit is gathered now. But life is marred, my soul to-day Turns sickening from all joy away. For, while this queen laments and sighs Amid a mourning people's cries, And Angad weeps his father slain, How can my heart delight to reign? For outrage, fury, senseless pride, My brother, doomed of yore, has died.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1273)
- **Original**: Canto XXIV. Sugríva's Lament. 1255 Yet, Raghu's son, in bitter woe I mourn his fated overthrow. Ah, better far in pain and ill To dwell on Rishyamúka still Than gain the heaven of Gods and all Its pleasures by my brother's fall. Did not he cry,— great-hearted foe,— “Go, for I will not slay thee, Go”? With his brave soul those words agree: My speech, my deeds, are worthy me. How can a brother counterweigh His grievous loss with joys of sway, And see with dull unpitying eye So brave and good a brother die? His lofty soul was nobly blind: My death alas, he ne'er designed; But I, urged blindly on by hate, Sought with his life my rage to sate. He smote me with a splintered tree: I groaned aloud and turned to flee, From stern reproaches he forbore, And gently bade me sin no more. Serene and dutiful and good He kept the laws of brotherhood: I, fierce and greedy, vengeful, base, Showed all the vices of our race. Ah me, dear friend, my brother's fate Lays on my soul a crushing weight: A sin no heart should e'er conceive, But at the thought each soul should grieve: Sin such as Indra's when his blow Laid heavenly Vi[varúpa610 low. 610 Vi[varúpa, a son of Twashmri or Vi[vakarmá the heavenly architect, was a three-headed monster slain by Indra.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1274)
- **Original**: 1256 The Ramayana Yet earth, the waters of the seas, The race of women and the trees Were fain upon themselves to take The weight of sin for Indra's sake. But who a Vánar's soul will free, Or ease the load that crushes me? Wretch that I am, I may not claim The reverence due to royal name. How shall I reign supreme, or dare Affect the power I should not share? Ah me, I sorrow for my sin, The ruin of my race and kin, Polluted by a hideous crime World-hated till the end of time. Alas, the floods of sorrow roll With whelming force upon my soul: So gathers the descending rain In the deep hollow of the plain.” [354] Canto XXV. Ráma's Speech. Then Raghu's son, whose feeling breast Shared the great woe that moved the rest, Strove with wise charm their grief to ease And gently spoke in words like these:
- **Translation**: 

---

### Verse 10 (Ramayana 0.1275)
- **Original**: Canto XXV. Ráma's Speech. 1257 “You ne'er can raise the dead to bliss By agony of grief like this. Cease your lament, nor leave undone The funeral task you may not shun. As nature orders o'er the dead. Your tributary tears are shed, But Fate, directing each event, Is still the lord preëminent. Yes, all obey the changeless laws Of Fate the universal cause. By Fate, the lives of all proceed, That governs every word and deed, None acts, none sees his hest obeyed, But each and all by Fate are swayed. The world its ordered course maintains, And o'er that course Fate ever reigns. Fate ne'er exceeds the rule of Fate: Is ne'er too swift, is ne'er too late, And making nature its ally Forgets no life, nor passes by. No kith and kin, no power and force Can check or stay its settled course, No friend or client, grace or charm, That victor of the world disarm. So all who see with prudent eyes The hand of Fate must recognize, For virtue rules, or love, or gain, As Fate's unchanged decrees ordain. Báli has died and won the meed That waits in heaven on noble deed, Throned in the seats the brave may reach By liberal hand and gentle speech, True to a warrior's duty, bold In fight, the hero lofty-souled
- **Translation**: 

---

### Verse 11 (Ramayana 0.1276)
- **Original**: 1258 The Ramayana Deigned not to guard his life: he died, And now in heaven is glorified. Then cease these tears and wild despair: Turn to the task that claims your care, For Báli's is the glorious fate Which warriors count most fortunate.” When Ráma's speech had found a close, Brave LakshmaG, terror of his foes, With wise and soothing words addressed Sugríva still with woe oppressed: “Arise Sugríva,” thus he said, “Perform the service of the dead. Prepare with Tárá and her son That Báli's rites be duly done. A store of funeral wood provide Which wind and sun and time have dried And richest sandal fit to grace The pyre of one of royal race. With words of comfort soft and kind Console poor Angad's troubled mind, Nor let thy heart be thus cast down, For thine is now the Vánars' town. Let Angad's care a wreath supply, And raiment rich with varied dye, And oil and perfumes for the fire, And all the solemn rites require. Go, hasten to the town, O King, And Tárá's little quickly bring. A virtue is despatch: and speed Is best of all in hour of need. Go, let a chosen band prepare The litter of the dead to bear. For stout and tall and strong of limb
- **Translation**: 

---

### Verse 12 (Ramayana 0.1277)
- **Original**: Canto XXV. Ráma's Speech. 1259 Must be the chiefs who carry him.” He spoke,— his friends' delight and pride,— Then stood again by Ráma's side. When Tára611 heard the words he said Within the town he quickly sped, And brought, on stalwart shoulders laid, The litter for the rites arrayed, Framed like a car for Gods, complete With painted sides and royal seat, With latticed windows deftly made, And golden birds and trees inlaid: Well joined and wrought in every part, A marvel of ingenious art. Where pleasure mounds in carven wood And many a graven figure stood. The best of jewels o'er it hung, And wreaths of flowers around it clung, And over all was raised on high A canopy of saffron dye, While like the sun of morning shone The brilliant blooms that lay thereon. That glorious litter Ráma eyed. And spake to LakshmaG by his side: “Let Báli on the bier be placed And with all funeral service graced.” Sugríva then with many a tear Drew Báli's body to the bier Whereon, with weeping Angad's aid, The relics of the chief were laid Neath many a vesture's varied fold, And wreaths and ornaments and gold. Then King Sugríva bade them speed 611 The Vánar chief, not to be confounded with Tárá.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1278)
- **Original**: 1260 The Ramayana The obsequies by law decreed: “Let Vánars lead the way and throw Rich gems around them as they go, And be the chosen bearers near Behind them laden with the bier. No costly rite may you deny, Used when the proudest monarchs die: As for a king of widest sway. Perform his obsequies to-day.”[355] Sugríva gave his high behest; Then Princely Tára and the rest, With little Angad weeping, led The long procession of the dead. Behind the funeral litter came, With Tárá first, each widowed dame, In tears and shrieks her loss deplored, Add cried aloud, My lord! My lord! While wood and hill and valley sent In echoes back the shrill lament. Then on a low and sandy isle Was reared the hero's funeral pile By crowds of toiling Vánars, where The mountain stream ran fresh and fair, The Vánar chiefs, a noble band, Had laid the litter on the sand, And stood a little space apart, Each mourning in his inmost heart. But Tárá, when her weeping eye Saw Báli, on the litter lie, Laid his dear head upon her lap, And wailed aloud her dire mishap; “O mighty Vánar, lord and king, To whose fond breast I loved to cling, Of goodly arms, wise, brave, and bold,
- **Translation**: 

---

### Verse 14 (Ramayana 0.1279)
- **Original**: Canto XXV. Ráma's Speech. 1261 Rise, look upon me as of old. Rise up, my sovereign, dost thou see A crowd of subjects weep for thee? Still o'er thy face, though breath has fled, The joyous light of life is spread: Thus around the sun, although he set, A crimson glory lingers yet. Death clad in Ráma's form to-day Hast dragged thee from the world away. One shaft from his tremendous bow Dooms us to widowhood and woe. Hast thou, O Vánar King, no eyes Thy weeping wives to recognize, Who for the length of way unmeet Have followed thee with weary feet? Yet every moon-faced beauty here By thee, O King was counted dear. Lord of the Vánar race, hast thou No eyes to see Sugríva now? About thee stands in mournful mood A sore-afflicted multitude, And Tára and thy lords of state Around their monarch weep and wait. Arise my lord, with gentle speech, As was thy wont, dismissing each, Then in the forest will we play And love shall make our spirits gay.” The Vánar dames raised Tárá, drowned In floods of sorrow, from the ground; And Angad with Sugríva's aid, O'erwhelmed with anguish and dismayed, Weeping for his departed sire, Placed Báli's body on the pyre:
- **Translation**: 

---

### Verse 15 (Ramayana 0.1280)
- **Original**: 1262 The Ramayana Then lit the flame, and round the dead Passed slowly with a mourner's tread. Thus with full rites the funeral train Performed the service for the slain, Then sought the flowing stream and made Libations to the parted shade. There, setting Angad first in place, The chieftains of the Vánar race, With Tárá and Sugríva, shed The water that delights the dead. Canto XXVI. The Coronation. Each Vánar councillor and peer In crowded numbers gathered near Sugríva, mournful king, while yet His vesture from the wave was wet, Before the chief of Raghu's seed Unwearied in each arduous deed, They stood and raised the reverent hand As saints before Lord Brahmá stand. Then Hanumán of massive mould, Like some tall hill of glistering gold, Son of the God whose wild blasts shake The forest, thus to Ráma spake: “By thy kind favour, O my lord, Sugríva, to his home restored Triumphant, has regained to-day His rank and power and royal sway. He now will call each faithful friend, Enter the city, and attend
- **Translation**: 

---

### Verse 16 (Ramayana 0.1281)
- **Original**: Canto XXVI. The Coronation. 1263 With sage advice and prudent care To every task that waits him there. Then balm and unguent shall anoint Our monarch, as the laws appoint, And gems and precious wreaths shall be His grateful offering, King, to thee. Do thou, O Ráma, with thy friend Thy steps within the city bend; Our ruler on his throne install, And with thy presence cheer us all.” Then, skilled in lore and arts that guide The speaker, Raghu's son replied: “For fourteen years I might not break The mandate that my father spake; Nor can I, till that time be fled, The street of town or village tread. Let King Sugríva seek the town Most worthy of her high renown, There let him be without delay Anointed, and begin his sway.” This answered, to Sugríva then Thus spake anew the king of men: “Do thou who knowest right ordain Prince Angad consort of thy reign; For he is noble, true, and bold, And trained a righteous course to hold Gifts like his sire's that youth adorn Born eldest to the eldest born. [356]
- **Translation**: 

---

### Verse 17 (Ramayana 0.1282)
- **Original**: 1264 The Ramayana This is the month ofZrávaG,612 first Of those that see the rain-clouds burst. Four months, thou knowest well, extends The season when the rain descends. No time for deeds of war is this: Seek thou thy fair metropolis, And I with LakshmaG, O my friend, The time upon this hill will spend. An ample cavern opens there Made lovely by the mountain air, And lotuses and lilies fill The pleasant lake and murmuring rill. When Kártik's613 month shall clear the skies, Then tempt the mighty enterprise. Now, chieftain to thy home repair, And be anointed sovereign there.” Sugríva heard: he bowed his head: Within the lovely town he sped Which Báli's royal will had swayed, Where thousand Vánar chiefs arrayed Gathered in order round their king, And led him on with welcoming. Low on the earth the lesser crowd Fell in prostration as they bowed. Sugríva looked with grateful eyes, Spake to them all and bade them rise. Then through the royal bowers he strode Wherein the monarch's wives abode. 612 ZrávaG: July-August. But the rains begin a month earlier, and what follows must not be taken literally. The text haspúrvo' yam várshiko másahZrávaGah salilágamdh. The Bengal recension has the same, and Gorresio translates: “Equesto ilmese Srâvana (luglio-agosto) primo della stagione piovosa, in cui dilagano le acque.” 613 Kártik: October-November.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1283)
- **Original**: Canto XXVI. The Coronation. 1265 Soon from the inner chambers came The Vánar of exalted fame; And joyful friends drew near and shed King-making balm upon his head, Like Gods anointing in the skies Their sovereign of the thousand eyes.614 Then brought they, o'er their king to hold The white umbrella decked with gold, And chouries with their waving hair In golden handles wondrous fair; And fragrant herbs and seed and spice, And sparkling gems exceeding price, And every bloom from woods and leas, And gum distilled from milky trees; And precious ointment white as milk, And spotless robes of cloth and silk, Wreaths of sweet flowers whose glories gleam In grassy grove, on lake or stream. And fragrant sandal and each scent That makes the soft breeze redolent; Grain, honey, odorous seed, and store Of oil and curd and golden ore; A noble tiger's skin, a pair Of sandals wrought with costliest care, Eight pairs of damsels drawing nigh Brought unguents stained with varied dye. Then gems and cates and robes displayed Before the twice-born priests were laid, That they would deign in order due 614 “Indras, as the nocturnal sun, hides himself, transformed, in the starry heavens: the stars are his eyes. The hundred-eyed or all-seeing (panoptês) Argos placed as a spy over the actions of the cow beloved by Zeus, in the Hellenic equivalent of this form of Indras.” D E G UBERNATIS {FNS ,Zoological Mythology, Vol. I, p. 418.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1284)
- **Original**: 1266 The Ramayana To consecrate the king anew. The sacred grass was duly spread And sacrificial flame was fed, Which Scripture-learned priests supplied With oil which texts had sanctified. Then, with all rites ordained of old, High on the terrace bright with gold, Whereon a glorious carpet lay, And fresh-culled garlands sweet and gay, Placed on his throne, Sugríva bent His looks toward the Orient. In horns from forehead of the bull, In pitchers bright and beautiful, In urns of gold the Vánara took Pure water brought from stream and brook, From every consecrated strand And every sea that beats the land. Then, as prescribed by sacred lore And many a mighty sage of yore,615 The leaders of the Vánars poured The sacred water on their lord.616 From every Vánar at the close Of that imperial rite arose Shouts of glad triumph, loud and long Repeated by the high-souled throng. Sugríva, when the rite was done, Obeyed the hest of Raghu's son, Prince Angad to his breast he strained, And partner of his sway ordained. 615 Baudháyana and others. 616 Sugríva appears to have been consecrated with all the ceremonies that attended theAbhishekaor coronation of an Indian prince of the Aryan race. Compare the preparations made for Ráma's consecration, Book II, Canto III. Thus Homer frequently introduces into Troy the rites of Hellenic worship.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1285)
- **Original**: Canto XXVII. Ráma On The Hill. 1267 Once more from all the host rang out The loud huzza and jovful shout. “Well done! well done!” each Vánar cried, And good Sugríva glorified. [357] Then with glad voices loudly raised Were Ráma and his brother praised; And bright Kishkindhá shone that day With happy throngs and banners gay. Canto XXVII. Ráma On The Hill. But when the solemn rite was o'er, And bold Sugríva reigned once more, The sons of Raghu sought the hill, Pra[ravaG of the rushing rill, Where roamed the tiger and the deer, And lions raised their voice of fear; Thick set with trees of every kind, With trailing shrubs and plants entwined; Home of the ape and monkey, lair Of mountain cat and pard and bear. In cloudy gloom against the sky The sanctifying hills rose high. Pierced in their crest, a spacious cave To Raghu's sons a shelter gave. Then Ráma, pure from every crime, In words well suited to the time To LakshmaG spake, whose faithful zeal Watched humbly for his brother's weal: “I love this spacious cavern where There breathes a fresh and pleasant air.
- **Translation**: 

---

