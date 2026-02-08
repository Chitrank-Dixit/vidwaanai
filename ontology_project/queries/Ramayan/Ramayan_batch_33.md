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

### Verse 1 (Ramayan 0.641)
- **Original**: Canto LXXI. Bharat's Return. 623 And passed the doors, to him unclosed, Where check nor bar his way oppossd. There Bharat stayed to bid adieu To grandsire and to uncle too, Then, withZatrughna by his side, Mounting his car, away he hied. The strong-wheeled cars were yoked, and they More than a hundred, rolled away: Servants, with horses, asses, kine, Followed their lord in endless line. So, guarded by his own right hand, Forth high-souled Bharat hied, Surrounded by a lordly band On whom the king relied. Beside him satZatrughna dear, The scourge of trembling foes: Thus from the light of Indra's sphere A saint made perfect goes. Canto LXXI. Bharat's Return. Then Bharat's face was eastward bent As from the royal town he went. He reached Sudámá's farther side, And glorious, gazed upon the tide; Passed Hládiní, and saw her toss Her westering billows hard to cross. Then old Ikshváku's famous son O'erZatadrú348 his passage won, 348 “The Zatadrú,‘the hundred-channeled’— the Zaradrus of Ptolemy, Hesydrus of Pliny— is the Sutlej.” W ILSON 'S{FNS VishGu PuráGa, Vol. II. p. 130.
- **Translation**: 

---

### Verse 2 (Ramayan 0.642)
- **Original**: 624 The Ramayana Near Ailadhána on the strand, And came to Aparparyat's land. O'erZilá's flood he hurried fast, Akurvatí's fair stream he passed, Crossed o'er Ágneya's rapid rill, And Zalyakartan onward still. Zilávahá's swift stream he eyed, True to his vows and purified, Then crossed the lofty hills, and stood In Chaitraratha's mighty wood. He reached the confluence where meet Sarasvatí349 and Gangá fleet, And through BháruG a forest, spread Northward of Viramatsya, sped. He sought Kálinda's child, who fills[179] The soul with joy, begirt by hills, Reached Yamuná, and passing o'er, Rested his army on the shore: He gave his horses food and rest, Bathed reeking limb and drooping crest. They drank their fill and bathed them there, And water for their journey bare. Thence through a mighty wood he sped All wild and uninhabited, As in fair chariot through the skies, Most fair in shape a Storm-God flies. At An[udhána Gangá, hard To cross, his onward journey barred, So turning quickly thence he came To Prágvam's city dear to fame. There having gained the farther side To Kumikoshmiká he hied: 349 The Sarasvatí or Sursooty is a tributary of the Caggar or Guggur in Sirhind.
- **Translation**: 

---

### Verse 3 (Ramayan 0.643)
- **Original**: Canto LXXI. Bharat's Return. 625 The stream he crossed, and onward then To Dharmavardhan brought his men. Thence, leaving ToraG on the north, To Jambuprastha journeyed forth. Then onward to a pleasant grove By fair Varútha's town he drove, And when a while he there had stayed, Went eastward from the friendly shade. Eastward of Ujjiháná where The Priyak trees are tall and fair, He passed, and rested there each steed Exhausted with the journey's speed. There orders to his men addressed, With quickened pace he onward pressed, A while at Sarvatírtha spent, Then o'er Uttániká he went. O'er many a stream beside he sped With coursers on the mountains bred, And passing Hastiprishmhak, took The road o'er Kumiká's fair brook. Then, at Lohitya's village, he Crossed o'er the swift Kapívatí, Then passed, where Eka[ála stands, The StháGumatí's flood and sands, And Gomatí of fair renown By Vinata's delightful town. When to Kalinga near he drew, A wood of Sal trees charmed the view; That passed, the sun began to rise, And Bharat saw with happy eyes, Ayodhyá's city, built and planned By ancient Manu's royal hand. Seven nights upon the road had passed, And when he saw the town at last
- **Translation**: 

---

### Verse 4 (Ramayan 0.644)
- **Original**: 626 The Ramayana Before him in her beauty spread, Thus Bharat to the driver said: “This glorious city from afar, Wherein pure groves and gardens are, Seems to my eager eyes to-day A lifeless pile of yellow clay. Through all her streets where erst a throng Of men and women streamed along, Uprose the multitudinous roar: To-day I hear that sound no more. No longer do mine eyes behold The leading people, as of old, On elephants, cars, horses, go Abroad and homeward, to and fro. The brilliant gardens, where we heard The wild note of each rapturous bird, Where men and women loved to meet, In pleasant shades, for pastime sweet,— These to my eyes this day appear Joyless, and desolate, and drear: Each tree that graced the garden grieves, And every path is spread with leaves. The merry cry of bird and beast, That spake aloud their joy, has ceased: Still is the long melodious note That charmed us from each warbling throat. Why blows the blessed air no more, The incense-breathing air that bore Its sweet incomparable scent Of sandal and of aloe blent? Why are the drum and tabour mute? Why is the music of the lute That woke responsive to the quill, Loved by the happy, hushed and still?
- **Translation**: 

---

### Verse 5 (Ramayan 0.645)
- **Original**: Canto LXXI. Bharat's Return. 627 My boding spirit gathers hence Dire sins of awful consequence, And omens, crowding on my sight, Weigh down my soul with wild affright. Scarce shall I find my friends who dwell Here in Ayodhyá safe and well: For surely not without a cause This crushing dread my soul o'erawes.” Heart sick, dejected, every sense Confused by terror's influence, On to the town he quickly swept Which King Ikshváku's children kept. He passed through Vaijayanta's gate, With weary steeds, disconsolate, And all who near their station held, His escort, crying Victory, swelled, With heart distracted still he bowed Farewell to all the following crowd, Turned to the driver and began To question thus the weary man: “Why was I brought, O free from blame, So fast, unknown for what I came? Yet fear of ill my heart appals, And all my wonted courage falls. For I have heard in days gone by The changes seen when monarchs die; And all those signs, O charioteer, I see to-day surround me here: Each kinsman's house looks dark and grim, No hand delights to keep it trim: The beauty vanished, and the pride, The doors, unkept, stand open wide. No morning rites are offered there,
- **Translation**: 

---

### Verse 6 (Ramayan 0.646)
- **Original**: 628 The Ramayana No grateful incense loads the air, And all therein, with brows o'ercast, Sit joyless on the ground and fast. Their lovely chaplets dry and dead,[180] Their courts unswept, with dust o'erspread, The temples of the Gods to-day No more look beautiful and gay. Neglected stands each holy shrine, Each image of a Lord divine. No shop where flowery wreaths are sold Is bright and busy as of old. The women and the men I mark Absorbed in fancies dull and dark, Their gloomy eyes with tears bedewed, A poor afflicted multitude.” His mind oppressed with woe and dread, Thus Bharat to his driver said, Viewed the dire signs Ayodhyá showed, And onward to the palace rode. Canto LXXII. Bharat's Inquiry. He entered in, he looked around, Nor in the house his father found; Then to his mother's dwelling, bent To see her face, he quickly went. She saw her son, so long away, Returning after many a day, And from her golden seat in joy Sprung forward to her darling boy.
- **Translation**: 

---

### Verse 7 (Ramayan 0.647)
- **Original**: Canto LXXII. Bharat's Inquiry. 629 Within the bower, no longer bright, Came Bharat lover of the right, And bending with observance sweet Clasped his dear mother's lovely feet. Long kisses on his brow she pressed, And held her hero to her breast, Then fondly drew him to her knees, And questioned him in words like these: “How many nights have fled, since thou Leftest thy grandsire's home, till now? By flying steeds so swiftly borne, Art thou not weak and travel-worn? How fares the king my father, tell: Is Yudhájit thine uncle well? And now, my son, at length declare The pleasure of the visit there.” Thus to the offspring of the king She spake with tender questioning, And to his mother made reply Young Bharat of the lotus eye: “The seventh night has come and fled Since from my grandsire's home I sped: My mother's sire is well, and he, Yudhájit, from all trouble free. The gold and every precious thing Presented by the conqueror king, The slower guards behind convey: I left them weary on the way. Urged by the men my father sent, My hasty course I hither bent: Now, I implore, an answer deign, And all I wish to know, explain. Unoccupied I now behold
- **Translation**: 

---

### Verse 8 (Ramayan 0.648)
- **Original**: 630 The Ramayana This couch of thine adorned with gold, And each of King Ikshváku's race Appears with dark and gloomy face. The king is aye, my mother dear, Most constant in his visits here. To meet my sire I sought this spot: How is it that I find him not? I long to clasp my father's feet: Say where he lingers, I entreat. Perchance the monarch may be seen Where dwells Kau[alyá, eldest queen.” His father's fate, from him concealed, Kaikeyí to her son revealed: Told as glad news the story sad, For lust of sway had made her mad: “Thy father, O my darling, know, Has gone the way all life must go: Devout and famed, of lofty thought, In whom the good their refuge sought.” When Bharat pious, pure, and true, Heard the sad words which pierced him through, Grieved for the sire he loved so well Prostrate upon the ground he fell: Down fell the strong-armed hero, high Tossing his arms, and a sad cry, “Ah, woe is me, unhappy, slain!” Burst from his lips again, again, Afflicted for his father's fate By grief's intolerable weight, With every sense amazed and cowed The splendid hero wailed aloud: “Ah me, my royal father's bed
- **Translation**: 

---

### Verse 9 (Ramayan 0.649)
- **Original**: Canto LXXII. Bharat's Inquiry. 631 Of old a gentle radiance shed, Like the pure sky when clouds are past, And the moon's light is o'er it cast: Ah, of its wisest lord bereft, It shows to-day faint radiance left, As when the moon has left the sky. Or mighty Ocean's depths are dry.” With choking sobs, with many a tear, Pierced to the heart with grief sincere, The best of conquerors poured his sighs, And with his robe veiled face and eyes. Kaikeyí saw him fallen there, Godlike, afflicted, in despair, Used every art to move him thence, And tried him thus with eloquence: “Arise, arise, my dearest; why Wilt thou, famed Prince, so lowly lie? Not by such grief as this are moved Good men like thee, by all approved. The earth thy father nobly swayed, And rites to Heaven he duly paid. At length his race of life was run: Thou shouldst not mourn for him, my son.” Long on the ground he wept, and rolled From side to side, still unconsoled, And then, with bitter grief oppressed, His mother with these words addressed: [181]
- **Translation**: 

---

### Verse 10 (Ramayan 0.650)
- **Original**: 632 The Ramayana “This joyful hope my bosom fed When from my grandsire's halls I sped— “The king will throne his eldest son, And sacrifice, as should be done.” But all is changed, my hope was vain, And this sad heart is rent in twain, For my dear father's face I miss, Who ever sought his loved ones' bliss. But in my absence, mother, say, What sickness took my sire away? Ah, happy Ráma, happy they Allowed his funeral rites to pay! The glorious monarch has not learned That I his darling have returned, Or quickly had he hither sped, And pressed his kisses on my head. Where is that hand whose gentle touch, Most soft and kind I loved so much, The hand that loved to brush away The dust that on his darling lay? Quick, bear the news to Ráma's ear; Tell the great chief that I am here: Brother, and sire, and friend, and all Is he, and I his trusty thrall. For noble hearts, to virtue true, Their sires in elder brothers view. To clasp his feet I fain would bow: He is my hope and refuge now. What said my glorious sire, who knew Virtue and vice, so brave and true? Firm in his vows, dear lady, say, What said he ere he passed away? What was his rede to me? I crave To hear the last advice he gave.”
- **Translation**: 

---

### Verse 11 (Ramayan 0.651)
- **Original**: Canto LXXII. Bharat's Inquiry. 633 Thus closely questioned by the youth, Kaikeyí spoke the mournful truth: “The high-souled monarch wept and sighed, For Ráma, Sítá, LakshmaG, cried, Then, best of all who go to bliss, Passed to the world which follows this. “Ah, blessed are the people who Shall Ráma and his Sítá view, And Lakshma G of the mighty arm, Returning free from scathe and harm.” Such were the words, the last of all, Thy father, ere he died, let fall, By Fate and Death's dread coils enwound, As some great elephant is bound.” He heard, yet deeper in despair, Her lips this double woe declare, And with sad brow that showed his pain Questioned his mother thus again: “But where is he, of virtue tried, Who fills Kau[alyá's heart with pride, Where is the noble Ráma? where Is LakshmaG brave, and Sítá fair?” Thus pressed, the queen began to tell The story as each thing befell, And gave her son in words like these, The mournful news she meant to please: “The prince is gone in hermit dress To DaG ak's mighty wilderness, And Lakshma G brave and Sítá share The wanderings of the exile there.”
- **Translation**: 

---

### Verse 12 (Ramayan 0.652)
- **Original**: 634 The Ramayana Then Bharat's soul with fear was stirred Lest Ráma from the right had erred, And jealous for ancestral fame, He put this question to the dame: “Has Ráma grasped with lawless hold A Bráhman's house, or land, or gold? Has Ráma harmed with ill intent Some poor or wealthy innocent? Was Ráma, faithless to his vows, Enamoured of anothers spouse? Why was he sent to DaG ak's wild, Like one who kills an unborn child?” He questioned thus: and she began To tell her deeds and crafty plan. Deceitful-hearted, fond, and blind As is the way of womankind: “No Bráhman's wealth has Ráma seized, No dame his wandering fancy pleased; His very eyes he ne'er allows To gaze upon a neighbour's spouse. But when I heard the monarch planned To give the realm to Ráma's hand, I prayed that Ráma hence might flee, And claimed the throne, my son, for thee. The king maintained the name he bare, And did according to my prayer, And Ráma, with his brother, sent, And Sítá, forth to banishment. When his dear son was seen no more, The lord of earth was troubled sore: Too feeble with his grief to strive, He joined the elemental Five. Up then, most dutiful! maintain
- **Translation**: 

---

### Verse 13 (Ramayan 0.653)
- **Original**: Canto LXXIII. Kaikeyí Reproached. 635 The royal state, arise, and reign. For thee, my darling son, for thee All this was planned and wrought by me. Come, cast thy grief and pain aside, With manly courage fortified. This town and realm are all thine own, And fear and grief are here unknown. Come, with Va[ishmha's guiding aid, And priests in ritual skilled Let the king's funeral dues be paid, And every claim fulfilled. Perform his obsequies with all That suits his rank and worth, Then give the mandate to install Thyself as lord of earth.” Canto LXXIII. Kaikeyí Reproached. But when he heard the queen relate His brothers' doom, his father's fate, Thus Bharat to his mother said With burning grief disquieted: [182] “Alas, what boots it now to reign, Struck down by grief and well-nigh slain? Ah, both are gone, my sire, and he Who was a second sire to me. Grief upon grief thy hand has made, And salt upon gashes laid: For my dear sire has died through thee, And Ráma roams a devotee. Thou camest like the night of Fate
- **Translation**: 

---

### Verse 14 (Ramayan 0.654)
- **Original**: 636 The Ramayana This royal house to devastate. Unwitting ill, my hapless sire Placed in his bosom coals of fire, And through thy crimes his death he met, O thou whose heart on sin is set. Shame of thy house! thy senseless deed Has reft all joy from Raghu's seed. The truthful monarch, dear to fame, Received thee as his wedded dame, And by thy act to misery doomed Has died by flames of grief consumed. Kau [alyá and Sumitrá too The coming of my mother rue, And if they live oppressed by woe, For their dear sons their sad tears flow. Was he not ever good and kind,— That hero of the duteous mind? Skilled in all filial duties, he As a dear mother treated thee. Kau [alyá too, the eldest queen, Who far foresees with insight keen, Did she not ever show thee all A sister's love at duty's call? And hast thou from the kingdom chased Her son, with bark around his waist, To the wild wood, to dwell therein, And dost not sorrow for thy sin? The love I bare to Raghu's son Thou knewest not, ambitious one, If thou hast wrought this impious deed For royal sway, in lawless greed. With him and LakshmaG far away, What power have I the realm to sway? What hope will fire my bosom when
- **Translation**: 

---

### Verse 15 (Ramayan 0.655)
- **Original**: Canto LXXIII. Kaikeyí Reproached. 637 I see no more these lords of men? The holy king, who loved the right Relied on Ráma's power and might, His guardian and his glory, so Joys Meru in his woods below. How can I bear, a steer untrained, The load his mightier strength sustained? What power have I to brook alone This weight on feeble shoulders thrown? But if the needful power were bought By strength of mind and brooding thought, No triumph shall attend the dame Who dooms her son to lasting shame. Now should no doubt that son prevent From quitting thee on evil bent. But Ráma's love o'erpowers my will, Who holds thee as his mother still. Whence did the thought, O thou whose eyes Are turned to sinful deeds, arise— A plan our ancient sires would hate, O fallen from thy virtuous state? For in the line from which we spring The eldest is anointed king: No monarchs from the rule decline, And, least of all, Ikshváku's line. Our holy sires, to virtue true, Upon our race a lustre threw, But with subversive frenzy thou Hast marred our lineal honour now, Of lofty birth, a noble line Of previous kings is also thine: Then whence this hated folly? whence This sudden change that steals thy sense? Thou shalt not gain thine impious will,
- **Translation**: 

---

### Verse 16 (Ramayan 0.656)
- **Original**: 638 The Ramayana O thou whose thoughts are bent on ill, Thou from whose guilty hand descend These sinful blows my life to end. Now to the forest will I go, Thy cherished plans to overthrow, And bring my brother, free from stain, His people's darling, home again. And Ráma, when again he turns, Whose glory like a beacon burns, In me a faithful slave shall find To serve him with contented mind.” Canto LXXIV. Bharat's Lament. When Bharat's anger-sharpened tongue Reproaches on the queen had flung, Again, with mighty rage possessed, The guilty dame he thus addressed: “Flee, cruel, wicked sinner, flee, Let not this kingdom harbour thee. Thou who hast thrown all right aside, Weep thou for me when I have died. Canst thou one charge against the king, Or the most duteous Ráma bring? The one thy sin to death has sent, The other chased to banishment. Our line's destroyer, sin defiled Like one who kills an unborn child, Ne'er with thy lord in heaven to dwell, Thy portion shall be down in hell Because thy hand, that stayed for naught,
- **Translation**: 

---

### Verse 17 (Ramayan 0.657)
- **Original**: Canto LXXIV. Bharat's Lament. 639 This awful wickedness has wrought, And ruined him whom all held dear, My bosom too is stirred with fear. My father by thy sin is dead, And Ráma to the wood is fled; And of thy deed I bear the stain, And fameless in the world remain. Ambitious, evil-souled, in show My mother, yet my direst foe. My throning ne'er thine eyes shall bless, Thy husband's wicked murderess. [183] Thou art not A[vapati's child, That righteous king most sage and mild, But thou wast born a fiend, a foe My father's house to overthrow. Thou who hast made Kau[alyá, pure, Gentle, affectionate, endure The loss of him who was her bliss,— What worlds await thee, Queen, for this? Was it not patent to thy sense That Ráma was his friends' defence, Kau [alyá's own true child most dear, The eldest and his father's peer? Men in the son not only trace The father's figure, form, and face, But in his heart they also find The offspring of the father's mind; And hence, though dear their kinsmen are, To mothers sons are dearer far. There goes an ancient legend how Good Surabhí, the God-loved cow, Saw two of her dear children strain, Drawing a plough and faint with pain. She saw them on the earth outworn,
- **Translation**: 

---

### Verse 18 (Ramayan 0.658)
- **Original**: 640 The Ramayana Toiling till noon from early morn, And as she viewed her children's woe, A flood of tears began to flow. As through the air beneath her swept The Lord of Gods, the drops she wept, Fine, laden with delicious smell, Upon his heavenly body fell. And Indra lifted up his eyes And saw her standing in the skies, Afflicted with her sorrow's weight, Sad, weeping, all disconsolate. The Lord of Gods in anxious mood Thus spoke in suppliant attitude: “No fear disturbs our rest, and how Come this great dread upon thee now? Whence can this woe upon thee fall, Say, gentle one who lovest all?” Thus spake the God who rules the skies, Indra, the Lord supremely wise; And gentle Surabhí, well learned In eloquence, this speech returned: “Not thine the fault, great God, not thine And guiltless are the Lords divine: I mourn two children faint with toil, Labouring hard in stubborn soil. Wasted and sad I see them now, While the sun beats on neck and brow, Still goaded by the cruel hind,— No pity in his savage mind. O Indra, from this body sprang These children, worn with many a pang. For this sad sight I mourn, for none Is to the mother like her son.”
- **Translation**: 

---

### Verse 19 (Ramayan 0.659)
- **Original**: Canto LXXIV. Bharat's Lament. 641 He saw her weep whose offspring feed In thousands over hill and mead, And knew that in a mother's eye Naught with a son, for love, can vie. He deemed her, when the tears that came From her sad eyes bedewed his frame, Laden with their celestial scent, Of living things most excellent. If she these tears of sorrow shed Who many a thousand children bred, Think what a life of woe is left Kau [alyá, of her Ráma reft. An only son was hers and she Is rendered childless now by thee. Here and hereafter, for thy crime, Woe is thy lot through endless time. And now, O Queen, without delay, With all due honour will I pay Both to my brother and my sire The rites their several fates require. Back to Ayodhyá will I bring The long-armed chief, her lord and king, And to the wood myself betake Where hermit saints their dwelling make. For, sinner both in deed and thought! This hideous crime which thou hast wrought I cannot bear, or live to see The people's sad eyes bent on me. Begone, to DaG ak wood retire, Or cast thy body to the fire, Or bind around thy neck the rope: No other refuge mayst thou hope. When Ráma, lord of valour true, Has gained the earth, his right and due,
- **Translation**: 

---

### Verse 20 (Ramayan 0.660)
- **Original**: 642 The Ramayana Then, free from duty's binding debt, My vanished sin shall I forget.” Thus like an elephant forced to brook The goading of the driver's hook, Quick panting like a serpent maimed, He fell to earth with rage inflamed. Canto LXXV. The Abjuration. A while he lay: he rose at length, And slowly gathering sense and strength, With angry eyes which tears bedewed, The miserable queen he viewed, And spake with keen reproach to her Before each lord and minister: “No lust have I for kingly sway, My mother I no more obey: Naught of this consecration knew Which Da[aratha kept in view. I withZatrughna all the time Was dwelling in a distant clime: I knew of Ráma's exile naught, That hero of the noble thought: I knew not how fair Sítá went, And Lakshma G, forth to banishment.”
- **Translation**: 

---

