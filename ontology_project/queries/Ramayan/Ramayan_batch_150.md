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

### Verse 1 (Ramayana 0.1026)
- **Original**: 1008 The Ramayana Meanwhile, O stranger, grant my prayer: Thy name, thy race, thy birth declare, And why with no companion thou Roamest in DaG ak forest now.” Thus questioned Sítá, Ráma's dame. Then fierce the stranger's answer came: “Lord of the giant legions, he From whom celestial armies flee,— The dread of hell and earth and sky, RávaG the Rákshas king am I. Now when thy gold-like form I view Arrayed in silks of amber hue, My love, O thou of perfect mould, For all my dames is dead and cold. A thousand fairest women, torn From many a land my home adorn. But come, loveliest lady, be The queen of every dame and me. My city Lanká, glorious town, Looks from a mountain's forehead down[285] Where ocean with his flash and foam Beats madly on mine island home. With me, O Sítá, shalt thou rove Delighted through each shady grove, Nor shall thy happy breast retain Fond memory of this life of pain. In gay attire, a glittering band, Five thousand maids shall round thee stand, And serve thee at thy beck and sign, If thou, fair Sítá, wilt be mine.”
- **Translation**: 

---

### Verse 2 (Ramayana 0.1027)
- **Original**: Canto XLVII. Rávan's Wooing. 1009 Then forth her noble passion broke As thus in turn the lady spoke: “Me, me the wife of Ráma, him The lion lord with lion's limb, Strong as the sea, firm as the rock, Like Indra in the battle shock. The lord of each auspicious sign, The glory of his princely line, Like some fair Bodh tree strong and tall, The noblest and the best of all, Ráma, the heir of happy fate Who keeps his word inviolate, Lord of the lion gait, possessed Of mighty arm and ample chest, Ráma the lion-warrior, him Whose moon bright face no fear can dim, Ráma, his bridled passions' lord, The darling whom his sire adored,— Me, me the true and loving dame Of Ráma, prince of deathless fame— Me wouldst thou vainly woo and press? A jackal woo a lioness! Steal from the sun his glory! such Thy hope Lord Ráma's wife to touch. Ha! Thou hast seen the trees of gold, The sign which dying eyes behold, Thus seeking, weary of thy life, To win the love of Ráma's wife. Fool! wilt thou dare to rend away The famished lion's bleeding prey, Or from the threatening jaws to take The fang of some envenomed snake? What, wouldst thou shake with puny hand
- **Translation**: 

---

### Verse 3 (Ramayana 0.1028)
- **Original**: 1010 The Ramayana Mount Mandar,501 towering o'er the land, Put poison to thy lips and think The deadly cup a harmless drink? With pointed needle touch thine eye, A razor to thy tongue apply, Who wouldst pollute with impious touch The wife whom Ráma loves so much? Be round thy neck a millstone tied, And swim the sea from side to side; Or raising both thy hands on high Pluck sun and moon from yonder sky; Or let the kindled flame be pressed, Wrapt in thy garment, to thy breast; More wild the thought that seeks to win Ráma's dear wife who knows not sin. The fool who thinks with idle aim To gain the love of Ráma's dame, With dark and desperate footing makes His way o'er points of iron stakes. As Ocean to a bubbling spring, The lion to a fox, the king Of all the birds that ply the wing To an ignoble crow As gold to lead of little price, As to the drainings of the rice The drink they quaff in Paradise, The Amrit's heavenly flow, As sandal dust with perfume sweet Is to the mire that soils our feet, A tiger to a cat, As the white swan is to the owl, The peacock to the waterfowl, 501 The mountain which was used by the Gods as a churning stick at the Churning of the Ocean.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1029)
- **Original**: Canto XLVIII. Rávan's Speech. 1011 An eagle to a bat, Such is my lord compared with thee; And when with bow and arrows he, Mighty as Indra's self shall see His foeman, armed to slay, Thou, death-doomed like the fly that sips The oil that on the altar drips, Shalt cast the morsel from thy lips And lose thy half-won prey.” Thus in high scorn the lady flung The biting arrows of her tongue In bitter words that pierced and stung The rover of the night. She ceased. Her gentle cheek grew pale, Her loosened limbs began to fail, And like a plantain in the gale She trembled with affright. He terrible as Death stood nigh, And watched with fierce exulting eye The fear that shook her frame. To terrify the lady more, He counted all his triumphs o'er, Proclaimed the titles that he bore, His pedigree and name. Canto XLVIII. Rávan's Speech. With knitted brow and furious eye The stranger made his fierce reply: “In me O fairest dame, behold The brother of the King of Gold.
- **Translation**: 

---

### Verse 5 (Ramayana 0.1030)
- **Original**: 1012 The Ramayana The Lord of Ten Necks my title, named RávaG, for might and valour famed. Gods and Gandharva hosts I scare; Snakes, spirits, birds that roam the air Fly from my coming, wild with fear, Trembling like men when Death is near. Vai[ravaG once, my brother, wrought To ire, encountered me and fought,[286] But yielding to superior might Fled from his home in sore affright. Lord of the man-drawn chariot, still He dwells on famed Kailása's hill. I made the vanquished king resign The glorious car which now is mine,— Pushpak, the far-renowned, that flies Will-guided through the buxom skies. Celestial hosts by Indra led Flee from my face disquieted, And where my dreaded feet appear The wind is hushed or breathless is fear. Where'er I stand, where'er I go The troubled waters cease to flow, Each spell-bound wave is mute and still And the fierce sun himself is chill. Beyond the sea my Lanká stands Filled with fierce forms and giant bands, A glorious city fair to see As Indra's Amarávatí. A towering height of solid wall, Flashing afar, surrounds it all, Its golden courts enchant the sight, And gates aglow with lazulite. Steeds, elephants, and cars are there, And drums' loud music fills the air,
- **Translation**: 

---

### Verse 6 (Ramayana 0.1031)
- **Original**: Canto XLVIII. Rávan's Speech. 1013 Fair trees in lovely gardens grow Whose boughs with varied fruitage glow. Thou, beauteous Queen, with me shalt dwell In halls that suit a princess well, Thy former fellows shall forget Nor think of women with regret, No earthly joy thy soul shall miss, And take its fill of heavenly bliss. Of mortal Ráma think no more, Whose terms of days will soon be o'er. King Da[aratha looked in scorn On Ráma though the eldest born, Sent to the woods the weakling fool, And set his darling son to rule. What, O thou large-eyed dame, hast thou To do with fallen Ráma now, From home and kingdom forced to fly, A wretched hermit soon to die? Accept thy lover, nor refuse The giant king who fondly woos. O listen, nor reject in scorn A heart by Káma's arrows torn. If thou refuse to hear my prayer, Of grief and coming woe beware; For the sad fate will fall on thee Which came on hapless Urva[í, When with her foot she chanced to touch Purúravas, and sorrowed much.502. My little finger raised in fight Were more than match for Ráma's might. O fairest, blithe and happy be With him whom fortune sends to thee.” 502 The story will be found in GARRETT 'S{FNS Classical Dictionary. See A DDITIONAL N OTES {FNS
- **Translation**: 

---

### Verse 7 (Ramayana 0.1032)
- **Original**: 1014 The Ramayana Such were the words the giant said, And Sítá's angry eyes were red. She answered in that lonely place The monarch of the giant race: “Art thou the brother of the Lord Of Gold by all the world adored, And sprung of that illustrious seed Wouldst now attempt this evil deed? I tell thee, impious Monarch, all The giants by thy sin will fall, Whose reckless lord and king thou art, With foolish mind and lawless heart. Yea, one may hope to steal the wife Of Indra and escape with life. But he who Ráma's dame would tear From his loved side must needs despair. Yea, one may steal fairZachí, dame Of Him who shoots the thunder flame, May live successful in his aim And length of day may see; But hope, O giant King, in vain, Though cups of Amrit thou may drain, To shun the penalty and pain Of wronging one like me.” Canto XLIX. The Rape Of Sítá.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1033)
- **Original**: Canto XLIX. The Rape Of Sítá. 1015 The Rákshas monarch, thus addressed, His hands a while together pressed, And straight before her startled eyes Stood monstrous in his giant size. Then to the lady, with the lore Of eloquence, he spoke once more: “Thou scarce,” he cried,“hast heard aright The glories of my power and might. I borne sublime in air can stand And with these arms upheave the land, Drink the deep flood of Ocean dry And Death with conquering force defy, Pierce the great sun with furious dart And to her depths cleave earth apart. See, thou whom love and beauty blind, I wear each form as wills my mind.” As thus he spake in burning ire His glowing eyes were red with fire. His gentle garb aside was thrown And all his native shape was shown. Terrific, monstrous, wild, and dread As the dark God who rules the dead, His fiery eyes in fury rolled, His limbs were decked with glittering gold. Like some dark cloud the monster showed, And his fierce breast with fury glowed. The ten-faced rover of the night, With twenty arms exposed to sight, His saintly guise aside had laid And all his giant height displayed. [287] Attired in robes of crimson dye He stood and watched with angry eye The lady in her bright array
- **Translation**: 

---

### Verse 9 (Ramayana 0.1034)
- **Original**: 1016 The Ramayana Resplendent as the dawn of day When from the east the sunbeams break, And to the dark-haired lady spake: “If thou would call that lord thine own Whose fame in every world is known, Look kindly on my love, and be Bride of a consort meet for thee. With me let blissful years be spent, For ne'er thy choice shalt thou repent. No deed of mine shall e'er displease My darling as she lives at ease. Thy love for mortal man resign, And to a worthier lord incline. Ah foolish lady, seeming wise In thine own weak and partial eyes, By what fair graces art thou held To Ráma from his realm expelled? Misfortunes all his life attend, And his brief days are near their end. Unworthy prince, infirm of mind! A woman spoke and he resigned His home and kingdom and withdrew From troops of friends and retinue. And sought this forest dark and dread By savage beasts inhabited.” Thus RávaG urged the lady meet For love, whose words were soft and sweet. Near and more near the giant pressed As love's hot fire inflamed his breast. The leader of the giant crew His arm around the lady threw: Thus Budha503 with ill-omened might 503 Mercury: to be carefully distinguished from Buddha.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1035)
- **Original**: Canto XLIX. The Rape Of Sítá. 1017 Steals RohiGí's delicious light. One hand her glorious tresses grasped, One with its ruthless pressure clasped The body of his lovely prize, The Maithil dame with lotus eyes. The silvan Gods in wild alarm Marked his huge teeth and ponderous arm, And from that Death-like presence fled, Of mountain size and towering head. Then seen was RávaG's magic car Aglow with gold which blazed afar,— The mighty car which asses drew Thundering as it onward flew. He spared not harsh rebuke to chide The lady as she moaned and cried, Then with his arm about her waist His captive in the car he placed. In vain he threatened: long and shrill Rang out her lamentation still, O Ráma! which no fear could stay: But her dear lord was far away. Then rose the fiend, and toward the skies Bore his poor helpless struggling prize: Hurrying through the air above The dame who loathed his proffered love. So might a soaring eagle bear A serpent's consort through the air. As on he bore her through the sky She shrieked aloud her bitter cry. As when some wretch's lips complain In agony of maddening pain; “O Lakshma G, thou whose joy is still To do thine elder brother's will, This fiend, who all disguises wears,
- **Translation**: 

---

### Verse 11 (Ramayana 0.1036)
- **Original**: 1018 The Ramayana From Ráma's side his darling tears. Thou who couldst leave bliss, fortune, all, Yea life itself at duty's call, Dost thou not see this outrage done To hapless me, O Raghu's son? 'Tis thine, O victor of the foe, To bring the haughtiest spirit low, How canst thou such an outrage see And let the guilty fiend go free? Ah, seldom in a moment's time Comes bitter fruit of sin and crime, But in the day of harvest pain Comes like the ripening of the grain. So thou whom fate and folly lead To ruin for this guilty deed, Shalt die by Ráma's arm ere long A dreadful death for hideous wrong. Ah, too successful in their ends Are Queen Kaikeyí and her friends, When virtuous Ráma, dear to fame, Is mourning for his ravished dame. Ah me, ah me! a long farewell To lawn and glade and forest dell In Janasthán's wild region, where The Cassia trees are bright and fair With all your tongues to Ráma say That RávaG bears his wife away. Farewell, a long farewell to thee, O pleasant stream Godávarí, Whose rippling waves are ever stirred By many a glad wild water-bird! All ye to Ráma's ear relate The giant's deed and Sítá's fate. O all ye Gods who love this ground
- **Translation**: 

---

### Verse 12 (Ramayana 0.1037)
- **Original**: Canto XLIX. The Rape Of Sítá. 1019 Where trees of every leaf abound, Tell Ráma I am stolen hence, I pray you all with reverence. On all the living things beside That these dark boughs and coverts hide, Ye flocks of birds, ye troops of deer, I call on you my prayer to hear. All ye to Ráma's ear proclaim That RávaG tears away his dame With forceful arms,— his darling wife, Dearer to Ráma than his life. O, if he knew I dwelt in hell, My mighty lord, I know full well, Would bring me, conqueror, back to-day, Though Yáma's self reclaimed his prey.” Thus from the air the lady sent [288] With piteous voice her last lament, And as she wept she chanced to see The vulture on a lofty tree. As RávaG bore her swiftly by, On the dear bird she bent her eye, And with a voice which woe made faint Renewed to him her wild complaint: “O see, the king who rules the race Of giants, cruel, fierce and base, RávaG the spoiler bears me hence The helpless prey of violence. This fiend who roves in midnight shade By thee, dear bird, can ne'er be stayed, For he is armed and fierce and strong Triumphant in the power to wrong. For thee remains one only task,
- **Translation**: 

---

### Verse 13 (Ramayana 0.1038)
- **Original**: 1020 The Ramayana To do, kind friend, the thing I ask. To Ráma's ear by thee be borne How Sítá from her home is torn, And to the valiant LakshmaG tell The giant's deed and what befell.” Canto L. Jatáyus. The vulture from his slumber woke And heard the words which Sítá spoke He raised his eye and looked on her, Looked on her giant ravisher. That noblest bird with pointed beak, Majestic as a mountain peak, High on the tree addressed the king Of giants, wisely counselling: “O Ten-necked lord, I firmly hold To faith and laws ordained of old, And thou, my brother, shouldst refrain From guilty deeds that shame and stain. The vulture king supreme in air, Jamáyus is the name I bear. Thy captive, known by Sítá's name, Is the dear consort and the dame Of Ráma, Da[aratha's heir Who makes the good of all his care. Lord of the world in might he vies With the great Gods of seas and skies. The law he boasts to keep allows No king to touch another's spouse, And, more than all, a prince's dame
- **Translation**: 

---

### Verse 14 (Ramayana 0.1039)
- **Original**: Canto L. Jatáyus. 1021 High honour and respect may claim. Back to the earth thy way incline, Nor think of one who is not thine. Heroic souls should hold it shame To stoop to deeds which others blame, And all respect by them is shown To dames of others as their own. Not every case of bliss and gain The Scripture's holy texts explain, And subjects, when that light is dim, Look to their prince and follow him. The king is bliss and profit, he Is store of treasures fair to see, And all the people's fortunes spring, Their joy and misery, from the king. If, lord of giant race, thy mind Be fickle, false, to sin inclined, How wilt thou kingly place retain? High thrones in heaven no sinners gain. The soul which gentle passions sway Ne'er throws its nobler part away, Nor will the mansion of the base Long be the good man's dwelling-place. Prince Ráma, chief of high renown, Has wronged thee not in field or town. Ne'er has he sinned against thee: how Canst thou resolve to harm him now? If moved byZúrpaGakhá's prayer The giant Khara sought him there, And fighting fell with baffled aim, His and not Ráma's is the blame. Say, mighty lord of giants, say What fault on Ráma canst thou lay? What has the world's great master done
- **Translation**: 

---

### Verse 15 (Ramayana 0.1040)
- **Original**: 1022 The Ramayana That thou should steal his precious one? Quick, quick the Maithil dame release; Let Ráma's consort go in peace, Lest scorched by his terrific eye Beneath his wrath thou fall and die Like Vritra when Lord Indra threw The lightning flame that smote and slew. Ah fool, with blinded eyes to take Home to thy heart a venomed snake! Ah foolish eyes, too blind to see That Death's dire coils entangle thee! The prudent man his strength will spare, Nor lift a load too great to bear. Content is he with wholesome food Which gives him life and strength renewed, But who would dare the guilty deed That brings no fame or glorious meed, Where merit there is none to win And vengeance soon o'ertakes the sin? My course of life, Pulastya's son, For sixty thousand years has run. Lord of my kind I still maintain Mine old hereditary reign. I, worn by years, am older far Than thou, young lord of bow and car, In coat of glittering mail encased And armed with arrows at thy waist, But not unchallenged shalt thou go, Or steal the dame without a blow. Thou canst not, King, before mine eyes Bear off unchecked thy lovely prize, Safe as the truth of Scripture bent By no close logic's argument. Stay if thy courage let thee, stay
- **Translation**: 

---

### Verse 16 (Ramayana 0.1041)
- **Original**: Canto LI. The Combat. 1023 And meet me in the battle fray, And thou shalt stain the earth with gore Falling as Khara fell before. Soon Ráma, clothed in bark, shall smite [289] Thee, his proud foe, in deadly fight,— Ráma, from whom have oft times fled The Daitya hosts discomfited. No power have I to kill or slay: The princely youths are far away, But soon shalt thou with fearful eye Struck down beneath their arrows lie. But while I yet have life and sense, Thou shalt not, tyrant, carry hence Fair Sítá, Ramá's honoured queen, With lotus eyes and lovely mien. Whate'er the pain, whate'er the cost, Though in the struggle life be lost, The will of Raghu's noblest son And Da [aratha must be done. Stay for a while, O RávaG, stay, One hour thy flying car delay, And from that glorious chariot thou Shalt fall like fruit from shaken bough, For I to thee, while yet I live, The welcome of a foe will give.” Canto LI. The Combat.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1042)
- **Original**: 1024 The Ramayana RávaG's red eyes in fury rolled: Bright with his armlets' flashing gold, In high disdain, by passion stirred He rushed against the sovereign bird. With clash and din and furious blows Of murderous battle met the foes: Thus urged by winds two clouds on high Meet warring in the stormy sky. Then fierce the dreadful combat raged As fiend and bird in war engaged, As if two winged mountains sped To dire encounter overhead. Keen pointed arrows thick and fast, In never ceasing fury cast, Rained hurtling on the vulture king And smote him on the breast and wing. But still that noblest bird sustained The cloud of shafts which RávaG rained, And with strong beak and talons bent The body of his foeman rent. Then wild with rage the ten-necked king Laid ten swift arrows on his string,— Dread as the staff of Death were they, So terrible and keen to slay. Straight to his ear the string he drew, Straight to the mark the arrows flew, And pierced by every iron head The vulture's mangled body bled. One glance upon the car he bent Where Sítá wept with shrill lament, Then heedless of his wounds and pain Rushed at the giant king again. Then the brave vulture with the stroke Of his resistless talons broke
- **Translation**: 

---

### Verse 18 (Ramayana 0.1043)
- **Original**: Canto LI. The Combat. 1025 The giant's shafts and bow whereon The fairest pearls and jewels shone. The monster paused, by rage unmanned: A second bow soon armed his hand, Whence pointed arrows swift and true In hundreds, yea in thousands, flew. The monarch of the vultures, plied With ceaseless darts on every side, Showed like a bird that turns to rest Close covered by the branch-built nest. He shook his pinions to repel The storm of arrows as it fell; Then with his talons snapped in two The mighty bow which RávaG drew. Next with terrific wing he smote So fiercely on the giant's coat, The harness, glittering with the glow Of fire, gave way beneath the blow. With storm of murderous strokes he beat The harnessed asses strong and fleet,— Each with a goblin's monstrous face And plates of gold his neck to grace. Then on the car he turned his ire,— The will-moved car that shone like fire, And broke the glorious chariot, broke The golden steps and pole and yoke. The chouris and the silken shade Like the full moon to view displayed, Together with the guards who held Those emblems, to the ground he felled. The royal vulture hovered o'er The driver's head, and pierced and tore With his strong beak and dreaded claws His mangled brow and cheek and jaws.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1044)
- **Original**: 1026 The Ramayana With broken car and sundered bow, His charioteer and team laid low, One arm about the lady wound, Sprang the fierce giant to the ground. Spectators of the combat, all The spirits viewed the monster's fall: Lauding the vulture every one Cried with glad voice, Well done! well done! But weak with length of days, at last The vulture's strength was failing fast. The fiend again assayed to bear The lady through the fields of air. But when the vulture saw him rise Triumphant with his trembling prize, Bearing the sword that still was left When other arms were lost or cleft, Once more, impatient of repose, Swift from the earth her champion rose, Hung in the way the fiend would take, And thus addressing RávaG spake: “Thou, King of giants, rash and blind, Wilt be the ruin of thy kind, Stealing the wife of Ráma, him With lightning scars on chest and limb. A mighty host obeys his will And troops of slaves his palace fill;[290] His lords of state are wise and true, Kinsmen has he and retinue. As thirsty travellers drain the cup, Thou drinkest deadly poison up. The rash and careless fool who heeds No coming fruit of guilty deeds, A few short years of life shall see, And perish doomed to death like thee.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1045)
- **Original**: Canto LI. The Combat. 1027 Say whither wilt thou fly to loose Thy neck from Death's entangling noose, Caught like the fish that finds too late The hook beneath the treacherous bait? Never, O King— of this be sure— Will Raghu's fiery sons endure, Terrific in their vengeful rage, This insult to their hermitage. Thy guilty hands this day have done A deed which all reprove and shun, Unworthly of a noble chief, The pillage loved by coward thief. Stay, if thy heart allow thee, stay And meet me in the deadly fray. Soon shall thou stain the earth with gore, And fall as Khara fell before. The fruits of former deeds o'erpower The sinner in his dying hour: And such a fate on thee, O King, Thy tyranny and madness bring. Not e'en the Self-existent Lord, Who reigns by all the worlds adored, Would dare attempt a guilty deed Which the dire fruits of crime succeed.” Thus brave Jamáyus, best of birds, Addressed the fiend with moving words, Then ready for the swift attack Swooped down upon the giant's back. Down to the bone the talons went; With many a wound the flesh was rent: Such blows infuriate drivers deal Their elephants with pointed steel. Fixed in his back the strong beak lay,
- **Translation**: 

---

