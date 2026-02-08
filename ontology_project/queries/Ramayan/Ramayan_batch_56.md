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

### Verse 1 (Ramayan 0.1101)
- **Original**: Canto LXV. Ráma's Wrath. 1083 With golden limbs and golden hue. Where is my darling Sítá? speak Before I rend thee peak from peak.” The mountain seemed her track to show, But told not all he sought to know. Then Da[aratha's son renewed His summons as the mount he viewed: “Soon as my flaming arrows fly, Consumed to ashes shall thou lie Without a herb or bud or tree, And birds no more shall dwell in thee. And if this stream my prayer deny, My wrath this day her flood shall dry, Because she lends no aid to trace My darling of the lotus face.” Thus Ráma spake as though his ire Would scorch them with his glance of fire; Then searching farther on the ground The footprint of a fiend he found, And small light traces here and there, Where Sítá in her great despair, Shrieking for Ráma's help, had fled Before the giant's mighty tread. His careful eye each trace surveyed Which Sítá and the fiend had made,— The quivers and the broken bow And ruined chariot of the foe,— And told, distraught by fear and grief, His tidings to his brother chief: “O Lakshma G, here,” he cried“behold My Sítá's earrings dropped with gold. Here lie her garlands torn and rent,
- **Translation**: 

---

### Verse 2 (Ramayan 0.1102)
- **Original**: 1084 The Ramayana Here lies each glittering ornament. O look, the ground on every side With blood-like drops of gold is dyed. The fiends who wear each strange disguise Have seized, I ween, the helpless prize. My lady, by their hands o'erpowered, Is slaughtered, mangled, and devoured. Methinks two fearful giants came And waged fierce battle for the dame. Whose, LakshmaG, was this mighty bow With pearls and gems in glittering row? Cast to the ground the fragments lie, And still their glory charms the eye. A bow so mighty sure was planned For heavenly God or giant's hand. Whose was this coat of golden mail Which, though its lustre now is pale, Shone like the sun of morning, bright With studs of glittering lazulite? Whose, LakshmaG, was this bloom-wreathed shade With all its hundred ribs displayed? This screen, most meet for royal brow, With broken staff lies useless now. And these tall asses, goblin-faced, With plates of golden harness graced, Whose hideous forms are stained with gore Who is the lord whose yoke they bore? Whose was this pierced and broken car That shoots a flame-like blaze afar? Whose these spent shafts at random spread, Each fearful with its iron head,— With golden mountings fair to see, Long as a chariot's axle-tree? These quivers see, which, rent in twain,
- **Translation**: 

---

### Verse 3 (Ramayan 0.1103)
- **Original**: Canto LXV. Ráma's Wrath. 1085 Their sheaves of arrows still contain. Whose was this driver? Dead and cold, His hands the whip and reins still hold. See, LakshmaG, here the foot I trace Of man, nay, one of giant race. The hatred that I nursed of old Grows mightier now a hundred fold Against these giants, fierce of heart, Who change their forms by magic art. Slain, eaten by the giant press, Or stolen is the votaress, Nor could her virtue bring defence To Sítá seized and hurried hence. O, if my love be slain or lost All hope of bliss for me is crossed. The power of all the worlds were vain To bring one joy to soothe my pain. The spirits with their blinded eyes Would look in wonder, and despise The Lord who made the worlds, the great Creator when compassionate. And so, I ween, the Immortals turn Cold eyes upon me now, and spurn [306] The weakling prompt at pity's call, Devoted to the good of all. But from this day behold me changed, From every gentle grace estranged. Now be it mine all life to slay, And sweep these cursed fiends away. As the great sun leaps up the sky, And the cold moonbeams fade and die, So vengeance rises in my breast, One passion conquering all the rest. Gandharvas in their radiant place,
- **Translation**: 

---

### Verse 4 (Ramayan 0.1104)
- **Original**: 1086 The Ramayana The Yakshas, and the giant race, Kinnars and men shall look in vain For joy they ne'er shall see again. The anguish of my great despair, O Lakshma G, fills the heaven and air; And I in wrath all life will slay Within the triple world to-day. Unless the Gods in heaven who dwell Restore my Sítá safe and well, I armed with all the fires of Fate, The triple world will devastate. The troubled stars from heaven shall fall, The moon be wrapped in gloomy pall, The fire be quenched, the wind be stilled, The radiant sun grow dark and chilled; Crushed every mountain's towering pride, And every lake and river dried, Dead every creeper, plant, and tree, And lost for aye the mighty sea. Thou shalt the world this day behold In wild disorder uncontrolled, With dying life which naught defends From the fierce storm my bowstring sends. My shafts this day, for Sítá's sake, The life of every fiend shall take. The Gods this day shall see the force That wings my arrows on their course, And mark how far that course is held, By my unsparing wrath impelled. No God, not one of Daitya strain, Goblin or Rákshas shall remain. My wrath shall end the worlds, and all Demons and Gods therewith shall fall. Each world which Gods, the Dánav race,
- **Translation**: 

---

### Verse 5 (Ramayan 0.1105)
- **Original**: Canto LXV. Ráma's Wrath. 1087 And giants make their dwelling place, Shall fall beneath my arrows sent In fury when my bow is bent. The arrows loosened from my string Confusion on the worlds shall bring. For she is lost or breathes no more, Nor will the Gods my love restore. Hence all on earth with life and breath This day I dedicate to death. All, till my darling they reveal, The fury of my shafts shall feel.” Thus as he spake by rage impelled, Red grew his eyes, his fierce lips swelled. His bark coat round his form he drew And coiled his hermit braids anew, Like Rudra when he yearned to slay The demon Tripur509 in the fray. So looked the hero brave and wise, The fury flashing from his eyes. Then Ráma, conqueror of the foe, From LakshmaG's hand received his bow, Strained the great string, and laid thereon A deadly dart that flashed and shone, And spake these words as fierce in ire As He who ends the worlds with fire: 509 An Asur or demon, king of Tripura, the modern Tipperah.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1106)
- **Original**: 1088 The Ramayana “As age and time and death and fate All life with checkless power await, So LakshmaG in my wrath to-day My vengeful might shall brook no stay, Unless this day I see my dame In whose sweet form is naught to blame,— Yea, as before, my love behold Fair with bright teeth and perfect mould, This world shall feel a deadly blow Destroyed with ruthless overthrow, And serpent lords and Gods of air, Gandharvas, men, the doom shall share.” Canto LXVI. Lakshman's Speech. He stood incensed with eyes of flame, Still mourning for his ravished dame, Determined, like the fire of Fate, To leave the wide world desolate. His ready bow the hero eyed, And as again, again he sighed, The triple world would fain consume Like Hara510 in the day of doom. Then LakshmaG moved with sorrow viewed His brother in unwonted mood, And reverent palm to palm applied, Thus spoke with lips which terror dried “Thy heart was ever soft and kind, To every creature's good inclined. 510 Ziva.
- **Translation**: 

---

### Verse 7 (Ramayan 0.1107)
- **Original**: Canto LXVI. Lakshman's Speech. 1089 Cast not thy tender mood away, Nor yield to anger's mastering sway. The moon for gentle grace is known, The sun has splendour all his own, The restless wind is free and fast, And earth in patience unsurpassed. So glory with her noble fruit Is thine eternal attribute. O, let not, for the sin of one, The triple world be all undone. I know not whose this car that lies In fragments here before our eyes, Nor who the chiefs who met and fought, Nor what the prize the foemen sought; Who marked the ground with hoof and wheel, [307] Or whose the hand that plied the steel Which left this spot, the battle o'er, Thus sadly dyed with drops of gore. Searching with utmost care I view The signs of one and not of two. Where'er I turn mine eyes I trace No mighty host about the place. Then mete not out for one offence This all-involving recompense. For kings should use the sword they bear, But mild in time should learn to spare, Thou, ever moved by misery's call, Wast the great hope and stay of all. Throughout this world who would not blame This outrage on thy ravished dame? Gandharvas, Dánavs, Gods, the trees, The rocks, the rivers, and the seas, Can ne'er in aught thy soul offend, As one whom holiest rites befriend.
- **Translation**: 

---

### Verse 8 (Ramayan 0.1108)
- **Original**: 1090 The Ramayana But him who dared to steal the dame Pursue, O King, with ceaseless aim, With me, the hermits' holy band, And thy great bow to arm thy hand By every mighty flood we'll seek, Each wood, each hill from base to peak. To the fair homes of Gods we'll fly, And bright Gandharvas in the sky, Until we reach, where'er he be, The wretch who stole thy spouse from thee. Then if the Gods will not restore Thy Sítá when the search is o'er, Then, royal lord of Ko[al's land, No longer hold thy vengeful hand. If meekness, prayer, and right be weak To bring thee back the dame we seek, Up, brother, with a deadly shower Of gold-bright shafts thy foes o'erpower, Fierce as the flashing levin sent From King Mahendra's firmament. Canto LXVII. Ráma Appeased. As Ráma, pierced by sorrow's sting, Lamented like a helpless thing, And by his mighty woe distraught Was lost in maze of troubled thought, Sumitrá's son with loving care Consoled him in his wild despair, And while his feet he gently pressed With words like these the chief addressed:
- **Translation**: 

---

### Verse 9 (Ramayan 0.1109)
- **Original**: Canto LXVII. Ráma Appeased. 1091 “For sternest vow and noblest deed Was Da [aratha blessed with seed. Thee for his son the king obtained, Like Amrit by the Gods regained. Thy gentle graces won his heart, And all too weak to live apart The monarch died, as Bharat told, And lives on high mid Gods enrolled. If thou, O Ráma, wilt not bear This grief which fills thee with despair, How shall a weaker man e'er hope, Infirm and mean, with woe to cope? Take heart, I pray thee, noblest chief: What man who breathes is free from grief? Misfortunes come and burn like flame, Then fly as quickly as they came. Yayáti son of Nahush reigned With Indra on the throne he gained. But falling for a light offence He mourned a while the consequence. Va [ishmha, reverend saint and sage, Priest of our sire from youth to age, Begot a hundred sons, but they Were smitten in a single day.511 And she, the queen whom all revere, The mother whom we hold so dear, The earth herself not seldom feels Fierce fever when she shakes and reels. And those twin lights, the world's great eyes, On which the universe relies,— Does not eclipse at times assail Their brilliance till their fires grow pale? 511 See Book I, Canto LIX.
- **Translation**: 

---

### Verse 10 (Ramayan 0.1110)
- **Original**: 1092 The Ramayana The mighty Powers, the Immortal Blest Bend to a law which none contest. No God, no bodied life is free From conquering Fate's supreme decree. E'enZakra's self must reap the meed Of virtue and of sinful deed. And O great lord of men, wilt thou Helpless beneath thy misery bow? No, if thy dame be lost or dead, O hero, still be comforted, Nor yield for ever to thy woe O'ermastered like the mean and low. Thy peers, with keen far-reaching eyes, Spend not their hours in ceaseless sighs; In dire distress, in whelming ill Their manly looks are hopeful still. To this, great chief, thy reason bend, And earnestly the truth perpend. By reason's aid the wisest learn The good and evil to discern. With sin and goodness scarcely known Faint light by chequered lives is shown; Without some clear undoubted deed We mark not how the fruits succeed. In time of old, O thou most brave, To me thy lips such counsel gave. V [ihaspati512 can scarcely find New wisdom to instruct thy mind. For thine is wit and genius high Meet for the children of the sky. I rouse that heart benumbed by pain And call to vigorous life again. 512 The preceptor of the Gods.
- **Translation**: 

---

### Verse 11 (Ramayan 0.1111)
- **Original**: Canto LXVIII. Jatáyus. 1093 Be manly godlike vigour shown; Put forth that noblest strength, thine own. [308] Strive, best of old Ikshváku's strain, Strive till the conquered foe be slain. Where is the profit or the joy If thy fierce rage the worlds destroy? Search till thou find the guilty foe, Then let thy hand no mercy show.” Canto LXVIII. Jatáyus. Thus faithful LakshmaG strove to cheer The prince with counsel wise and clear. Who, prompt to seize the pith of all, Let not that wisdom idly fall. With vigorous effort he restrained The passion in his breast that reigned, And leaning on his bow for rest His brother LakshmaG thus addressed: “How shall we labour now, reflect; Whither again our search direct? Brother, what plan canst thou devise To bring her to these longing eyes?”
- **Translation**: 

---

### Verse 12 (Ramayan 0.1112)
- **Original**: 1094 The Ramayana To him by toil and sorrow tried The prudent LakshmaG thus replied: “Come, though our labour yet be vain, And search through Janasthán again,— A realm where giant foes abound, And trees and creepers hide the ground. For there are caverns deep and dread, By deer and wild birds tenanted, And hills with many a dark abyss, Grotto and rock and precipice. There bright Gandharvas love to dwell, And Kinnars in each bosky dell. With me thy eager search to aid Be every hill and cave surveyed. Great chiefs like thee, the best of men, Endowed with sense and piercing ken, Though tried by trouble never fail, Like rooted hills that mock the gale.” Then Ráma, pierced by anger's sting, Laid a keen arrow on his string, And by the faithful LakshmaG's side Roamed through the forest far and wide. Jamáyus there with blood-drops dyed, Lying upon the ground he spied, Huge as a mountain's shattered crest, Mid all the birds of air the best. In wrath the mighty bird he eyed, And thus the chief to LakshmaG cried:
- **Translation**: 

---

### Verse 13 (Ramayan 0.1113)
- **Original**: Canto LXVIII. Jatáyus. 1095 “Ah me, these signs the truth betray; My darling was the vulture's prey. Some demon in the bird's disguise Roams through the wood that round us lies. On large-eyed Sítá he has fed, And rests him now with wings outspread. But my keen shafts whose flight is true, Shall pierce the ravenous monster through.” An arrow on the string he laid, And rushing near the bird surveyed, While earth to ocean's distant side Trembled beneath his furious stride. With blood and froth on neck and beak The dying bird essayed to speak, And with a piteous voice, distressed, Thus Da[aratha's son addressed: “She whom like some sweet herb of grace Thou seekest in this lonely place, Fair lady, is fierce RávaG's prey, Who took, beside, my life away. Lakshma G and thou had parted hence And left the dame without defence. I saw her swiftly borne away By RávaG's might which none could stay. I hurried to the lady's aid, I crushed his car and royal shade, And putting forth my warlike might Hurled RávaG to the earth in fight. Here, Ráma, lies his broken bow, Here lie the arrows of the foe. There on the ground before thee are The fragments of his battle car.
- **Translation**: 

---

### Verse 14 (Ramayan 0.1114)
- **Original**: 1096 The Ramayana There bleeds the driver whom my wings Beat down with ceaseless buffetings. When toil my aged strength subdued, His sword my weary pinions hewed. Then lifting up the dame he bare His captive through the fields of air. Thy vengeful blows from me restrain, Already by the giant slain.” When Ráma heard the vulture tell The tale that proved his love so well, His bow upon the ground he placed, And tenderly the bird embraced: Then to the earth he fell o'erpowered, And burning tears both brothers showered, For double pain and anguish pressed Upon the patient hero's breast. The solitary bird he eyed Who in the lone wood gasped and sighed, And as again his anguish woke Thus Ráma to his brother spoke: “Expelled from power the woods I tread, My spouse is lost, the bird is dead. A fate so sad, I ween, would tame The vigour of the glorious flame. If I to cool my fever tried To cross the deep from side to side, The sea,— so hard my fate,— would dry His waters as my feet came nigh. In all this world there lives not one So cursed as I beneath the sun; So strong a net of misery cast Around me holds the captive fast,
- **Translation**: 

---

### Verse 15 (Ramayan 0.1115)
- **Original**: Canto LXIX. The Death Of Jatáyus. 1097 Best of all birds that play the wing, Loved, honoured by our sire the king, The vulture, in my fate enwound, Lies bleeding, dying on the ground.” Then Ráma and his brother stirred [309] By pity mourned the royal bird, And, as their hands his limbs caressed, Affection for a sire expressed. And Ráma to his bosom strained The bird with mangled wings distained, With crimson blood-drops dyed. He fell, and shedding many a tear, “Where is my spouse than life more dear? Where is my love?” he cried. Canto LXIX. The Death Of Jatáyus. As Ráma viewed with heart-felt pain The vulture whom the fiend had slain, In words with tender love impressed His brother chief he thus addressed:
- **Translation**: 

---

### Verse 16 (Ramayan 0.1116)
- **Original**: 1098 The Ramayana “This royal bird with faithful thought For my advantage strove and fought. Slain by the fiend in mortal strife For me he yields his noble life. See, LakshmaG, how his wounds have bled; His struggling breath will soon have fled. Faint is his voice, and near to die, He scarce can lift his trembling eye. Jamáyus, if thou still can speak, Give, give the answer that I seek. The fate of ravished Sítá tell, And how thy mournful chance befell. Say why the giant stole my dame: What have I done that he could blame? What fault in me has RávaG seen That he should rob me of my queen? How looked the lady's moon-bright cheek? What were the words she found to speak? His strength, his might, his deeds declare: And tell the form he loves to wear. To all my questions make reply: Where does the giant's dwelling lie?” The noble bird his glances bent On Ráma as he made lament, And in low accents faint and weak With anguish thus began to speak: “Fierce RávaG, king of giant race, Stole Sítá from thy dwelling-place. He calls his magic art to aid With wind and cloud and gloomy shade. When in the fight my power was spent My wearied wings he cleft and rent. Then round the dame his arms he threw,
- **Translation**: 

---

### Verse 17 (Ramayan 0.1117)
- **Original**: Canto LXIX. The Death Of Jatáyus. 1099 And to the southern region flew. O Raghu's son, I gasp for breath, My swimming sight is dim in death. E'en now before my vision pass Bright trees of gold with hair of grass, The hour the impious robber chose Brings on the thief a flood of woes. The giant in his haste forgot 'Twas Vinda's hour,513 or heeded not. Those robbed at such a time obtain Their plundered store and wealth again. He, like a fish that takes the bait, In briefest time shall meet his fate. Now be thy troubled heart controlled And for thy lady's loss consoled, For thou wilt slay the fiend in fight And with thy dame have new delight.” With senses clear, though sorely tried, The royal vulture thus replied, While as he sank beneath his pain Forth rushed the tide of blood again. “Him,514 brother of the Lord of Gold, Vi[ravas' self begot of old.” Thus spoke the bird, and stained with gore Resigned the breath that came no more. “Speak, speak again!” thus Ráma cried, With reverent palm to palm applied, But from the frame the spirit fled And to the skiey regions sped. The breath of life had passed away. Stretched on the ground the body lay. 513 From the rootvid, to find. 514 RávaG.
- **Translation**: 

---

### Verse 18 (Ramayan 0.1118)
- **Original**: 1100 The Ramayana When Ráma saw the vulture lie, Huge as a hill, with darksome eye, With many a poignant woe distressed His brother chief he thus addressed: “Amid these haunted shades content Full many a year this bird has spent. His life in home of giants passed, In DaG ak wood he dies at last. The years in lengthened course have fled Untroubled o'er the vulture's head, And now he lies in death, for none The stern decrees of Fate may shun. See, LakshmaG, how the vulture fell While for my sake he battled well. And strove to free with onset bold My Sítá from the giant's hold. Supreme amid the vulture kind His ancient rule the bird resigned, And conquered in the fruitless strife Gave for my sake his noble life. O Lakshma G, many a time we see Great souls who keep the law's decree, With whom the weak sure refuge find, In creatures of inferior kind. The loss of her, my darling queen, Strikes with a pang less fiercely keen Than now this slaughtered bird to see Who nobly fought and died for me. As Da[aratha, good and great, Was glorious in his high estate, Honoured by all, to all endeared, So was this royal bird revered. Bring fuel for the funeral rite: These hands the solemn fire shall light[310]
- **Translation**: 

---

### Verse 19 (Ramayan 0.1119)
- **Original**: Canto LXIX. The Death Of Jatáyus. 1101 And on the burning pyre shall lay The bird who died for me to-day. Now on the gathered wood shall lie The lord of all the birds that fly, And I will burn with honours due My champion whom the giant slew. O royal bird of noblest heart, Graced with all funeral rites depart To bright celestial seats above, Rewarded for thy faithful love. Dwell in thy happy home with those Whose constant fires of worship rose. Live blest amid the unyielding brave, And those who land in largess gave.” Sore grief upon his bosom weighed As on the pyre the bird he laid, And bade the kindled flame ascend To burn the body of his friend. Then with his brother by his side The hero to the forest hied. There many a stately deer he slew, The flesh around the bird to strew. The venison into balls he made, And on fair grass before him laid. Then that the parted soul might rise And find free passage to the skies, Each solemn word and text he said Which Bráhmans utter o'er the dead. Then hastening went the princely pair To bright Godávarí, and there Libations of the stream they poured In honour of the vulture lord, With solemn ritual to the slain,
- **Translation**: 

---

### Verse 20 (Ramayan 0.1120)
- **Original**: 1102 The Ramayana As scripture's holy texts ordain. Thus offerings to the bird they gave And bathed their bodies in the wave. The vulture monarch having wrought A hard and glorious feat, Honoured by Ráma sage in thought, Soared to his blissful seat. The brothers, when each rite was paid To him of birds supreme, Their hearts with new-found comfort stayed, And turned them from the stream. Like sovereigns of celestial race Within the wood they came, Each pondering the means to trace, The captor of the dame. Canto LXX. Kabandha. When every rite was duly paid The princely brothers onward strayed, And eager in the lady's quest They turned their footsteps to the west. Through lonely woods that round them lay Ikshváku's children made their way, And armed with bow and shaft and brand Pressed onward to the southern land. Thick trees and shrubs and creepers grew In the wild grove they hurried through. 'Twas dark and drear and hard to pass For tangled thorns and matted grass.
- **Translation**: 

---

