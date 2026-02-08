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

### Verse 1 (Ramayana 0.506)
- **Original**: 488 The Ramayana This seems the fruit that virtues bear, The meed of worth which texts declare— The sending of the brave and good By sire and mother to the wood.'” He heard the monarch, and obeyed, With ready feet that ne'er delayed, And brought before the palace gate The horses and the car of state. Then to the monarch's son he sped, And raising hands of reverence said[141] That the light car which gold made fair, With best of steeds, was standing there. King Da[aratha called in haste The lord o'er all his treasures placed. And spoke, well skilled in place and time, His will to him devoid of crime: “Count all the years she has to live Afar in forest wilds, and give To Sítá robes and gems of price As for the time may well suffice.” Quick to the treasure-room he went, Charged by that king most excellent, Brought the rich stores, and gave them all To Sítá in the monarch's hall. The Maithil dame of high descent Received each robe and ornament, And tricked those limbs, whose lines foretold High destiny, with gems and gold. So well adorned, so fair to view, A glory through the hall she threw: So, when the Lord of Light upsprings, His radiance o'er the sky he flings. Then Queen Kau[alyá spake at last,
- **Translation**: 

---

### Verse 2 (Ramayana 0.507)
- **Original**: Canto XXXIX. Counsel To Sítá. 489 With loving arms about her cast, Pressed lingering kisses on her head, And to the high-souled lady said: “Ah, in this faithless world below When dark misfortune comes and woe, Wives, loved and cherished every day, Neglect their lords and disobey. Yes, woman's nature still is this:— After long days of calm and bliss When some light grief her spirit tries, She changes all her love, or flies. Young wives are thankless, false in soul, With roving hearts that spurn control. Brooding on sin and quickly changed, In one short hour their love estranged. Not glorious deed or lineage fair, Not knowledge, gift, or tender care In chains of lasting love can bind A woman's light inconstant mind. But those good dames who still maintain What right, truth, Scripture, rule ordain— No holy thing in their pure eyes With one beloved husband vies. Nor let thy lord my son, condemned To exile, be by thee contemned, For be he poor or wealthy, he Is as a God, dear child, to thee.” When Sítá heard Kau[alyá's speech Her duty and her gain to teach, She joined her palms with reverent grace And gave her answer face to face: “All will I do, forgetting naught, Which thou, O honoured Queen, hast taught.
- **Translation**: 

---

### Verse 3 (Ramayana 0.508)
- **Original**: 490 The Ramayana I know, have heard, and deep have stored The rules of duty to my lord. Not me, good Queen, shouldst thou include Among the faithless multitude. Its own sweet light the moon shall leave Ere I to duty cease to cleave. The stringless lute gives forth no strain, The wheelless car is urged in vain; No joy a lordless dame, although Blest with a hundred sons, can know. From father, brother, and from son A measured share of joy is won: Who would not honour, love, and bless Her lord, whose gifts are measureless? Thus trained to think, I hold in awe Scripture's command and duty's law. Him can I hold in slight esteem? Her lord is woman's God, I deem.” Kau [alyá heard the lady's speech, Nor failed those words her heart to reach. Then, pure in mind, she gave to flow The tear that sprang of joy and woe. Then duteous Ráma forward came And stood before the honoured dame, And joining reverent hands addressed The queen in rank above the rest: “O mother, from these tears refrain; Look on my sire and still thy pain. To thee my days afar shall fly As if sweet slumber closed thine eye, And fourteen years of exile seem To thee, dear mother, like a dream. On me returning safe and well, Girt by my friends, thine eyes shall dwell.”
- **Translation**: 

---

### Verse 4 (Ramayana 0.509)
- **Original**: Canto XL. Ráma's Departure. 491 Thus for their deep affection's sake The hero to his mother spake, Then to the half seven hundred too, Wives of his sire, paid reverence due. Thus Da[aratha's son addressed That crowd of matrons sore distressed: “If from these lips, while here I dwelt, One heedless taunt you e'er have felt, Forgive me, pray. And now adieu, I bid good-bye to all of you.” Then straight, like curlews' cries, upwent The voices of their wild lament, While, as he bade farewell, the crowd Of royal women wept aloud, And through the ample hall's extent. Where erst the sound of tabour, blent With drum and shrill-toned instrument, In joyous concert rose, Now rang the sound of wailing high, The lamentation and the cry, The shriek, the choking sob, the sigh That told the ladies' woes. Canto XL. Ráma's Departure. Then Ráma, Sítá, LakshmaG bent At the king's feet, and sadly went [142]
- **Translation**: 

---

### Verse 5 (Ramayana 0.510)
- **Original**: 492 The Ramayana Round him with slow steps reverent. When Ráma of the duteous heart Had gained his sire's consent to part, With Sítá by his side he paid Due reverence to the queen dismayed. And Lakshma G, with affection meet, Bowed down and clasped his mother's feet. Sumitrá viewed him as he pressed Her feet, and thus her son addressed: “Neglect not Ráma wandering there, But tend him with thy faithful care. In hours of wealth, in time of woe, Him, sinless son, thy refuge know. From this good law the just ne'er swerve, That younger sons the eldest serve, And to this righteous rule incline All children of thine ancient line— Freely to give, reward each rite, Nor spare their bodies in the fight. Let Ráma Da[aratha be, Look upon Sítá as on me, And let the cot wherein you dwell Be thine Ayodhyá. Fare thee well.” Her blessing thus Sumitrá gave To him whose soul to Ráma clave, Exclaiming, when her speech was done, “Go forth, O LakshmaG, go, my son. Go forth, my son to win success, High victory and happiness. Go forth thy foemen to destroy, And turn again at last with joy.” As Mátali his charioteer Speaks for the Lord of Gods to hear,
- **Translation**: 

---

### Verse 6 (Ramayana 0.511)
- **Original**: Canto XL. Ráma's Departure. 493 Sumantra, palm to palm applied, In reverence trained, to Ráma cried: “O famous Prince, my car ascend,— May blessings on thy course attend,— And swiftly shall my horses flee And place thee where thou biddest me. The fourteen years thou hast to stay Far in the wilds, begin to-day; For Oueen Kaikeyí cries, Away.” Then Sítá, best of womankind, Ascended, with a tranquil mind, Soon as her toilet task was done, That chariot brilliant as the sun. Ráma and LakshmaG true and bold Sprang on the car adorned with gold. The king those years had counted o'er, And given Sítá robes and store Of precious ornaments to wear When following her husband there. The brothers in the car found place For nets and weapons of the chase, There warlike arms and mail they laid, A leathern basket and a spade. Soon as Sumantra saw the three Were seated in the chariot, he Urged on each horse of noble breed, Who matched the rushing wind in speed. As thus the son of Raghu went Forth for his dreary banishment, Chill numbing grief the town assailed, All strength grew weak, all spirit failed, Ayodhyá through her wide extent Was filled with tumult and lament:
- **Translation**: 

---

### Verse 7 (Ramayana 0.512)
- **Original**: 494 The Ramayana Steeds neighed and shook the bells they bore, Each elephant returned a roar. Then all the city, young and old, Wild with their sorrow uncontrolled, Rushed to the car, as, from the sun The panting herds to water run. Before the car, behind, they clung, And there as eagerly they hung, With torrents streaming from their eyes, Called loudly with repeated cries: “Listen, Sumantra: draw thy rein; Drive gently, and thy steeds restrain. Once more on Ráma will we gaze, Now to be lost for many days. The queen his mother has, be sure, A heart of iron, to endure To see her godlike Ráma go, Nor feel it shattered by the blow. Sítá, well done! Videha's pride, Still like his shadow by his side; Rejoicing in thy duty still As sunlight cleaves to Meru's hill. Thou, LakshmaG, too, hast well deserved, Who from thy duty hast not swerved, Tending the peer of Gods above, Whose lips speak naught but words of love. Thy firm resolve is nobly great, And high success on thee shall wait. Yea, thou shalt win a priceless meed— Thy path with him to heaven shall lead.” As thus they spake, they could not hold The tears that down their faces rolled, While still they followed for a space Their darling of Ikshváku's race.
- **Translation**: 

---

### Verse 8 (Ramayana 0.513)
- **Original**: Canto XL. Ráma's Departure. 495 There stood surrounded by a ring Of mournful wives the mournful king; For,“I will see once more,” he cried, “Mine own dear son,” and forth he hied. As he came near, there rose the sound Of weeping, as the dames stood round. So the she-elephants complain When their great lord and guide is slain. Kakutstha's son, the king of men, The glorious sire, looked troubled then, As the full moon is when dismayed By dark eclipse's threatening shade. Then Da[aratha's son, designed For highest fate of lofty mind, Urged to more speed the charioteer, “Away, away! why linger here? Urge on thy horses,” Rama cried, And “Stay, O stay,” the people sighed. Sumantra, urged to speed away, The townsmen's call must disobey, Forth as the long-armed hero went, [143] The dust his chariot wheels up sent Was laid by streams that ever flowed From their sad eyes who filled the road. Then, sprung of woe, from eyes of all The women drops began to fall, As from each lotus on the lake The darting fish the water shake. When he, the king of high renown, Saw that one thought held all the town, Like some tall tree he fell and lay, Whose root the axe has hewn away. Then straight a mighty cry from those Who followed Ráma's car arose,
- **Translation**: 

---

### Verse 9 (Ramayana 0.514)
- **Original**: 496 The Ramayana Who saw their monarch fainting there Beneath that grief too great to bear. Then “Ráma, Ráma!” with the cry Of “Ah, his mother!” sounded high, As all the people wept aloud Around the ladies' sorrowing crowd. When Ráma backward turned his eye, And saw the king his father lie With troubled sense and failing limb, And the sad queen, who followed him, Like some young creature in the net, That will not, in its misery, let Its wild eyes on its mother rest, So, by the bonds of duty pressed, His mother's look he could not meet. He saw them with their weary feet, Who, used to bliss, in cars should ride, Who ne'er by sorrow should be tried, And, as one mournful look he cast, “Drive on,” he cried,“Sumantra, fast.” As when the driver's torturing hook Goads on an elephant, the look Of sire and mother in despair Was more than Ráma's heart could bear. As mother kine to stalls return Which hold the calves for whom they yearn, So to the car she tried to run As a cow seeks her little one. Once and again the hero's eyes Looked on his mother, as with cries Of woe she called and gestures wild, “O Sítá, LakshmaG, O my child!” “Stay,” cried the king,“thy chariot stay:” “On, on,” cried Ráma,“speed away.”
- **Translation**: 

---

### Verse 10 (Ramayana 0.515)
- **Original**: Canto XLI. The Citizens' Lament. 497 As one between two hosts, inclined To neither was Sumantra's mind. But Ráma spake these words again: “A lengthened woe is bitterest pain. On, on; and if his wrath grow hot, Thine answer be,‘I heard thee not.’ ” Sumantra, at the chief's behest, Dismissed the crowd that toward him pressed, And, as he bade, to swiftest speed Urged on his way each willing steed. The king's attendants parted thence, And paid him heart-felt reverence: In mind, and with the tears he wept, Each still his place near Ráma kept. As swift away the horses sped, His lords to Da[aratha said: “To follow him whom thou again Wouldst see returning home is vain.” With failing limb and drooping mien He heard their counsel wise: Still on their son the king and queen Kept fast their lingering eyes.314 Canto XLI. The Citizens' Lament. 314 “Thirty centuries have passed since he began this memorable journey. Every step of it is known and is annually traversed by thousands: hero worship is not extinct. What can Faith do! How strong are the ties of religion when entwined with the legends of a country! How many a cart creeps creaking and weary along the road from Ayodhyá to Chitrakúm. It is this that gives the Rámáyan a strange interest, the story still lives.” Calcutta Review: Vol. XXIII.
- **Translation**: 

---

### Verse 11 (Ramayana 0.516)
- **Original**: 498 The Ramayana The lion chief with hands upraised Was born from eyes that fondly gazed. But then the ladies' bower was rent With cries of weeping and lament: “Where goes he now, our lord, the sure Protector of the friendless poor, In whom the wretched and the weak Defence and aid were wont to seek? All words of wrath he turned aside, And ne'er, when cursed, in ire replied. He shared his people's woe, and stilled The troubled breast which rage had filled. Our chief, on lofty thoughts intent, In glorious fame preëminent: As on his own dear mother, thus He ever looked on each of us. Where goes he now? His sire's behest, By Queen Kaikeyí's guile distressed, Has banished to the forest hence Him who was all the world's defence. Ah, senseless King, to drive away The hope of men, their guard and stay, To banish to the distant wood Ráma the duteous, true, and good!” The royal dames, like cows bereaved Of their young calves, thus sadly grieved. The monarch heard them as they wailed, And by the fire of grief assailed For his dear son, he bowed his head, And all his sense and memory fled. Then were no fires of worship fed, Thick darkness o'er the sun was spread. The cows their thirsty calves denied,
- **Translation**: 

---

### Verse 12 (Ramayana 0.517)
- **Original**: Canto XLI. The Citizens' Lament. 499 And elephants flung their food aside. [144] Tri[anku,315 Jupiter looked dread, And Mercury and Mars the red, In direful opposition met, The glory of the moon beset. The lunar stars withheld their light, The planets were no longer bright, But meteors with their horrid glare, And dire Vi[ákhás316 lit the air. As troubled Ocean heaves and raves When Doom's wild tempest sweeps the waves, Thus all Ayodhyá reeled and bent When Ráma to the forest went. And chilling grief and dark despair Fell suddenly on all men there. Their wonted pastime all forgot, Nor thought of food, or touched it not. Crowds in the royal street were seen With weeping eye and troubled mien: No more a people gay and glad, Each head and heart was sick and sad. No more the cool wind softly blew, The moon no more was fair to view, No more the sun with genial glow Cherished the world now plunged in woe. Sons, brothers, husbands, wedded wives Forgot the ties that joined their lives; No thought for kith and kin was spared, But all for only Ráma cared. And Ráma's friends who loved him best, Their minds disordered and distressed. By the great burthen of their woes 315 See p. 72. 316 Four stars of the sixteenth lunar asterism.
- **Translation**: 

---

### Verse 13 (Ramayana 0.518)
- **Original**: 500 The Ramayana Turned not to slumber or repose. Like Earth with all her hills bereft Of Indra's guiding care. Ayodhyá in her sorrow left By him, the high souled heir, Was bowed by fear and sorrow's force, And shook with many a throe, While warrior, elephant, and horse Sent up the cry of woe. Canto XLII. Dasaratha's Lament. While yet the dust was seen afar That marked the course of Ráma's car, The glory of Ikshváku's race Turned not away his eager face. While yet his duteous son he saw He could not once his gaze withdraw, But rooted to the spot remained With eyes that after Ráma strained. But when that dust no more he viewed, Fainting he fell by grief subdued. To his right hand Kau[alyá went, And ready aid the lady lent, While Bharat's loving mother tried To raise him on the other side. The king, within whose ordered soul Justice and virtue held control, To Queen Kaikeyí turned and said, With every sense disquieted: “Touch me not, thou whose soul can plot
- **Translation**: 

---

### Verse 14 (Ramayana 0.519)
- **Original**: Canto XLII. Dasaratha's Lament. 501 All sin. Kaikeyí, touch me not. No loving wife, no friend to me, I ne'er again would look on thee; Ne'er from this day have aught to do With thee and all thy retinue; Thee whom no virtuous thoughts restrain, Whose selfish heart seeks only gain. The hand I laid in mine, O dame, The steps we took around the flame,317 And all that links thy life to mine Here and hereafter I resign. If Bharat too, thy darling son, Joy in the rule thy art has won, Ne'er may the funeral offerings paid By his false hand approach my shade.” Then while the dust upon him hung, The monarch to Kau[alyá clung, And she with mournful steps and slow Turned to the palace, worn with woe. As one whose hand has touched the fire, Or slain a Bráhman in his ire, He felt his heart with sorrow torn Still thinking of his son forlorn. Each step was torture, as the road The traces of the chariot showed, And as the shadowed sun grows dim So care and anguish darkened him. He raised a cry, by woe distraught, As of his son again he thought. And judging that the car had sped Beyond the city, thus he said: “I still behold the foot-prints made 317 In the marriage service.
- **Translation**: 

---

### Verse 15 (Ramayana 0.520)
- **Original**: 502 The Ramayana By the good horses that conveyed My son afar: these marks I see, But high-souled Ráma, where is he? Ah me, my son! my first and best, On pleasant couches wont to rest, With limbs perfumed with sandal, fanned By many a beauty's tender hand: Where will he lie with log or stone Beneath him for a pillow thrown, To leave at morn his earthy bed, Neglected, and with dust o'erspread, As from the flood with sigh and pant Comes forth the husband elephant? The men who make the woods their home Shall see the long-armed hero roam Roused from his bed, though lord of all, In semblance of a friendless thrall. Janak's dear child who ne'er has met[145] With aught save joy and comfort yet, Will reach to-day the forest, worn And wearied with the brakes of thorn. Ah, gentle girl, of woods unskilled, How will her heart with dread be filled At the wild beasts' deep roaring there, Whose voices lift the shuddering hair! Kaikeyí, glory in thy gain, And, widow queen, begin to reign: No will, no power to live have I When my brave son no more is nigh.” Thus pouring forth laments, the king Girt by the people's crowded ring, Entered the noble bower like one New-bathed when funeral rites are done.
- **Translation**: 

---

### Verse 16 (Ramayana 0.521)
- **Original**: Canto XLII. Dasaratha's Lament. 503 Where'er he looked naught met his gaze But empty houses, courts, and ways. Closed were the temples: countless feet No longer trod the royal street, And thinking of his son he viewed Men weak and worn and woe-subdued. As sinks the sun into a cloud, So passed he on, and wept aloud, Within that house no more to be The dwelling of the banished three, Brave Ráma, his Vedehan bride, And Lakshma G by his brother's side: Like broad still waters, when the king Of all the birds that ply the wing Has swooped from heaven and borne away The glittering snakes that made them gay. With choking sobs and voice half spent The king renewed his sad lament: With broken utterance faint and low Scarce could he speak these words of woe: “My steps to Ráma's mother guide, And place me by Kau[alyá's side: There, only there my heart may know Some little respite from my woe.” The warders of the palace led The monarch, when his words were said, To Queen Kau[alyá's bower, and there Laid him with reverential care. But while he rested on the bed Still was his soul disquieted. In grief he tossed his arms on high Lamenting with a piteous cry: “O Ráma, Ráma,” thus said he,
- **Translation**: 

---

### Verse 17 (Ramayana 0.522)
- **Original**: 504 The Ramayana “My son, thou hast forsaken me. High bliss awaits those favoured men Left living in Ayodhyá then, Whose eyes shall see my son once more Returning when the time is o'er.” Then came the night, whose hated gloom Fell on him like the night of doom. At midnight Da[aratha cried To Queen Kau[alyá by his side: “I see thee not, Kau[alyá; lay Thy gentle hand in mine, I pray. When Ráma left his home my sight Went with him, nor returns to-night.” Canto XLIII. Kausalyá's Lament. Kau [alyá saw the monarch lie With drooping frame and failing eye, And for her banished son distressed With these sad words her lord addressed: “Kaikeyí, cruel, false, and vile Has cast the venom of her guile On Ráma lord of men, and she Will ravage like a snake set free; And more and more my soul alarm, Like a dire serpent bent on harm, For triumph crowns each dark intent, And Ráma to the wild is sent. Ah, were he doomed but here to stray Begging his food from day to day, Or do, enslaved, Kaikeyí's will,
- **Translation**: 

---

### Verse 18 (Ramayana 0.523)
- **Original**: Canto XLIII. Kausalyá's Lament. 505 This were a boon, a comfort still. But she, as chose her cruel hate, Has hurled him from his high estate, As Bráhmans when the moon is new Cast to the ground the demons' due.318 The long-armed hero, like the lord Of Nágas, with his bow and sword Begins, I ween, his forest life With LakshmaG and his faithful wife. Ah, how will fare the exiles now, Whom, moved by Queen Kaikeyí, thou Hast sent in forests to abide, Bred in delights, by woe untried? Far banished when their lives are young, With the fair fruit before them hung, Deprived of all their rank that suits, How will they live on grain and roots? O, that my years of woe were passed, And the glad hour were come at last When I shall see my children dear, Ráma, his wife, and LakshmaG here! When shall Ayodhyá, wild with glee, Again those mighty heroes see, And decked with wreaths her banners wave To welcome home the true and brave? When will the beautiful city view With happy eyes the lordly two Returning, joyful as the main When the dear moon is full again? When, like some mighty bull who leads The cow exulting through the meads, Will Ráma through the city ride, 318 The husks and chaff of the rice offered to the Gods.
- **Translation**: 

---

### Verse 19 (Ramayana 0.524)
- **Original**: 506 The Ramayana Strong-armed, with Sítá at his side? When will ten thousand thousand meet And crowd Ayodhyá's royal street, And grain in joyous welcome throw Upon my sons who tame the foe? When with delight shall youthful bands Of Bráhman maidens in their hands[146] Bear fruit and flowers in goodly show, And circling round Ayodhyá go? With ripened judgment of a sage, And godlike in his blooming age, When shall my virtuous son appear, Like kindly rain, our hearts to cheer? Ah, in a former life, I ween, This hand of mine, most base and mean, Has dried the udders of the kine And left the thirsty calves to pine. Hence, as the lion robs the cow, Kaikeyí makes me childless now, Exulting from her feebler foe To rend the son she cherished so. I had but him, in Scripture skilled, With every grace his soul was filled. Now not a joy has life to give, And robbed of him I would not live: Yea, all my days are dark and drear If he, my darling, be not near, And Lakshma G brave, my heart to cheer. As for my son I mourn and yearn, The quenchless flames of anguish burn And kill me with the pain, As in the summer's noontide blaze The glorious Day-God with his rays Consumes the parching plain.”
- **Translation**: 

---

### Verse 20 (Ramayana 0.525)
- **Original**: Canto XLIV. Sumitrá's Speech. 507 Canto XLIV. Sumitrá's Speech. Kau [alyá ceased her sad lament, Of beauteous dames most excellent. Sumitrá who to duty clave, In righteous words this answer gave: “Dear Queen, all noble virtues grace Thy son, of men the first in place. Why dost thou shed these tears of woe With bitter grief lamenting so? If Ráma, leaving royal sway Has hastened to the woods away, 'Tis for his high-souled father's sake That he his premise may not break. He to the path of duty clings Which lordly fruit hereafter brings— The path to which the righteous cleave— For him, dear Queen, thou shouldst not grieve. And Lakshma G too, the blameless-souled, The same high course with him will hold, And mighty bliss on him shall wait, So tenderly compassionate. And Sítá, bred with tender care, Well knows what toils await her there, But in her love she will not part From Ráma of the virtuous heart. Now has thy son through all the world The banner of his fame unfurled; True, modest, careful of his vow, What has he left to aim at now? The sun will mark his mighty soul, His wisdom, sweetness, self-control, Will spare from pain his face and limb, And with soft radiance shine for him.
- **Translation**: 

---

