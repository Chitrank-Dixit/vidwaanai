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

### Verse 1 (Ramayana 0.1366)
- **Original**: 1348 The Ramayana Come, cast your grief and sloth aside: Again be every effort tried; So haply may our toil attain The sweet success that follows pain. Laborious effort, toil, and skill, The firm resolve, the constant will Secure at last the ends we seek: Hence, O my friends, I boldly speak. Once more then, noble hearts, once more Let us to-day this wood explore, And, languor and despair subdued, Purchase success with toil renewed. Sugríva is a king austere, And Ráma's wrath we needs must fear. Come, Vánars, ye think it wise, And do the thing that I advise.” Then Gandhamádan thus replied With lips that toil and thirst had dried; “Obey his words, for wise and true Is all that he has counselled you. Come, let your hosts their toil renew And search each grove and desert through, Each towering hill and forest glade. By lake and brook and white cascade, Till every spot, as our great lord Commanded, be again explored.” Uprose the Vánars one and all, Obedient to the chieftain's call, And over the southern region sped Where Vindhya's tangled forests spread. They clomb that hill that towers on high Like a huge cloud in autumn's sky,
- **Translation**: 

---

### Verse 2 (Ramayana 0.1367)
- **Original**: Canto L. The Enchanted Cave. 1349 Where many a cavern yawns, and streaks Of radiant silver deck the peaks. In eager search they wandered through The forests where the Lodh trees grew, Where the dark leaves were thick and green, But found not Ráma's darling queen. Then faint with toil, their hearts depressed, Descending from the mountain's crest, Their weary limbs a while to ease They lay beneath the spreading trees. Canto L. The Enchanted Cave. Angad and Tára by his side, Again rose Hanumán and tried Each mountain cavern, dark and deep, And stony pass and wooded steep, The lion's and the tiger's home, By rushing torrents white with foam. Then with new ardour, south and west, O'er Vindhya's height the search they pressed. The day prescribed was near and they Still wandered on their weary way. They reached the southern land beset With woody mountains like a net. At length a mighty cave they spied That opened in a mountain's side. Where many a verdant creeper grew And o'er the mouth its tendrils threw. Thence issued crane, and swan, and drake, And trooping birds that love the lake.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1368)
- **Original**: 1350 The Ramayana The Vánars rushed within to cool Their fevered lips in spring or pool. Vast was the cavern dark and dread, Where not a ray of light was shed; Yet not the more their eyesight failed,[382] Their courage sank or valour quailed. On through the gloom the Vánars pressed With hunger, thirst, and toil distressed, Poor helpless wanderers, sad, forlorn, With wasted faces wan and worn. At length, when life seemed lost for aye, They saw a splendour as of day, A wondrous forest, fair and bright, Where golden trees shot flamy light. And lotus-covered pools were there With pleasant waters fresh and fair, And streams their rippling currents rolled By seats of silver and of gold. Fair houses reared their stately height Of burnished gold and lazulite, And glorious was the lustre thrown Through lattices of precious stone. And there were flowers and fruit on stems Of coral decked with rarest gems, And emerald leaves on silver trees, And honeycomb and golden bees. Then as the Vánars nearer drew, A holy woman met their view, Around her form was duly tied A garment of the blackdeer's hide.751 Pure votaress she shone with light Of fervent zeal and holy rite. 751 The skin of the black antelope was the ascetic's proper garb.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1369)
- **Original**: Canto LI. Svayamprabhá. 1351 Then Hanumán before the rest With reverent words the dame addressed: “Who art thou? say: and who is lord Of this vast cave with treasures stored?” Canto LI. Svayamprabhá. “Assailed by thirst and hunger, dame, Within a gloomy vault we came. We saw the cavern opening wide, And straight within its depths we hied. But utterly amazed are we At all the marvels that we see. Whose are the golden trees that gleam With splendour like the morning's beam? These cates of noblest sort? these roots? This wondrous store of rarest fruits? Whose are these calm and cool retreats, These silver homes and golden seats, And lattices of precious stones? Who is the happy lord that owns The golden trees, of rarest scent, Neath loads of fruit and blossom bent? Who, strong in holy zeal, had power To deck the streams with richest dower, And bade the lilies bright with gold The glory of their blooms unfold, Where fish in living gold below The sheen of changing colours show? Thine is the holy power, I ween, That beautified the wondrous scene;
- **Translation**: 

---

### Verse 5 (Ramayana 0.1370)
- **Original**: 1352 The Ramayana But if another's, lady, deign To tell us, and the whole explain.” To him the lady of the cave In words like these her answer gave: “Skilled Maya framed in days of old This magic wood of growing gold. The chief artificer in place Was he of all the Dánav race. He, for his wise enchantments famed, This glorious dwelling planned and framed He for a thousand years endured The sternest penance, and secured From Brahmá of all boons the best, The knowledge U[anas752 possessed. Lord, by that boon, of all his will, He fashioned all with perfect skill; And, with his blissful state content, In this vast grove a season spent. By Indra's jealous bolt he fell For loving Hemá's753 charms too well. And Brahmá on that nymph bestowed The treasures of this fair abode, Wherein her tranquil days to spend In happiness that ne'er may end. Sprung of a lineage old and high, MerusávarGi's754 daughter, I Guard ever for that heavenly dame 752 U [anas is the name of a sage mentioned in the Vedas. In the epic poems he is identified withZukra, the regent of the planet Venus, and described as the preceptor of the Asuras or Daityas, and possessor of vast knowledge. 753 Hemá is one of the nymphs of Paradise. 754 MerusávarGi is a general name for the last four of the fourteen Manus.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1371)
- **Original**: Canto LII. The Exit. 1353 This home, Svayamprabhá755 my name,— For I have loved the lady long, So skilled in arts of dance and song. But say what cause your steps has led The mazes of this grove to tread. [383] How, strangers did ye chance to spy The wood concealed from wanderer's eye? Tell clearly why ye come: but first Eat of this fruit and quench your thirst.” Canto LII. The Exit. “Ráma,” he cried,“a prince whose sway All peoples of the earth obey, To DaG ak's tangled forest came With his brave brother and his dame. From that dark shade of forest boughs The giant RávaG stole his spouse. Our king Sugríva's orders send These Vánars forth to aid his friend, That so the lady be restored Uninjured to her sorrowing lord. With Angad and the rest, this band Has wandered through the southern land, 755 Svayamprabhá, the“self-luminous,” is according to DE G UBERNATIS {FNS the moon:“In theSvayamprabhá too, we meet with the moon as a good fairy who, from the golden palace which she reserves for her friend Hemá (the golden one:) is during a month the guide, in the vast cavern of Hanumant and his companions, who have lost their way in the search of the dawn Sítá.” This is is not quite accurate: Hanumán and his companions wander for a month in the cavern without a guide, and then Svayamprabhá leads them out.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1372)
- **Original**: 1354 The Ramayana With careful search in every place The lady and the fiend to trace. We roamed the southern region o'er, And stood upon the ocean's shore. By hunger pressed our strength gave way; Beneath the spreading trees we lay, And cried, worn out with toil and woe, “No farther, comrades, can we go.” Then as our sad eyes looked around We spied an opening in the ground, Where all was gloomy dark behind The creeping plants that o'er it twined. Forth trooping from the dark-recess Came swans and mallards numberless, With drops upon their shining wings As newly bathed where water springs. “On, comrades, to the cave,” I cried And all within the portal hied. Each clasping fast another's hand Far onward pressed the Vánar band; And still, as thirst and hunger drove, We traced the mazes of the grove. Here thou with hospitable care Hast fed us with the noblest fare, Preserving us, about to die, With this thy plentiful supply. But how, O pious lady, say, May we thy gracious boon repay?” He ceased: the ascetic dame replied: “Well, Vánars, am I satisfied. A life of holy works I lead, And from your hands no service need.” Then spake again the Vánar chief:
- **Translation**: 

---

### Verse 8 (Ramayana 0.1373)
- **Original**: Canto LII. The Exit. 1355 “We came to thee and found relief. Now listen to a new distress, And aid us, holy votaress. Our wanderings in this vasty cave Exhaust the time Sugríva gave. Once more then, lady, grant release, And let thy suppliants go in peace Again upon their errand sped, For King Sugríva's ire we dread. And the great task our sovereign set, Alas, is unaccomplished yet.” Thus Hanumán their leader prayed, And thus the dame her answer made: “Scarce may the living find their way Returning hence to light of day; But I will free you through the might Of penance, fast, and holy rite. Close for a while your eyes, or ne'er May you return to upper air.” She ceased: the Vánars all obeyed; Their fingers on their eyes they laid, And, ere a moment's time had fled, Were through the mazy cavern led. Again the gracious lady spoke, And joy in every bosom woke: “Lo, here again is Vindhya's hill, Whose valleys trees and creepers fill; And, by the margin of the sea, Pra[ravaG where you fain would be.” With blessings then she bade adieu, And swift within the cave withdrew.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1374)
- **Original**: 1356 The Ramayana Canto LIII. Angad's Counsel. They looked upon the boundless main The awful seat of VaruG's reign. And heard his waters roar and rave Terrific with each crested wave. Then, in the depths of sorrow drowned, They sat upon the bosky ground, And sadly, as they pondered, grieved For days gone by and naught achieved. Pain pierced them through with sharper sting When, gazing on the trees of spring, They saw each waving bough that showed The treasures of its glorious load, And helpless, fainting with the weight Of woe they sank disconsolate. Then, lion-shouldered, stout and strong, The noblest of the Vánar throng, Angad the prince imperial rose, And, deeply stricken by the woes That his impetuous spirit broke, Thus gently to the chieftains spoke: “Mark ye not, Vánars, that the day Our monarch fixed has passed away? The month is lost in toil and pain, And now, my friends, what hopes remain? On you, in lore of counsel tried, Our king Sugríva most relied. Your hearts, with strong affection fraught,[384] His weal in every labour sought, And the true valour of your band Was blazoned wide in every land. Forth on the toilsome search you sped, By me — for so he willed it— led,
- **Translation**: 

---

### Verse 10 (Ramayana 0.1375)
- **Original**: Canto LIII. Angad's Counsel. 1357 To us, of every hope bereft, Death is the only refuge left. For none a happy life may see Who fails to do our king's decree. Come, let us all from food abstain, And perish thus, since hope is vain. Stern is our king and swift to ire, Imperious, proud, and fierce like fire, And ne'er will pardon us the crime Of fruitless search and wasted time. Far better thus to end our lives, And leave our wealth, our homes and wives, Leave our dear little ones and all, Than by his vengeful hand to fall. Think not Sugríva's wrath will spare Me Báli's son, imperial heir: For Raghu's royal son, not he, To this high place anointed me. Sugríva, long my bitter foe, With eager hand will strike the blow, And, mindful of the old offence, Will slay me now for negligence, Nor will my pitying friends have power To save me in the deadly hour. No — here, O chieftains, will I lie By ocean's marge, and fast and die.” They heard the royal prince declare The purpose of his fixt despair; And all, by common terror moved, His speech in these sad words approved: “Sugríva's heart is hard and stern, And Ráma's thoughts for Sítá yearn. Our forfeit lives will surely pay
- **Translation**: 

---

### Verse 11 (Ramayana 0.1376)
- **Original**: 1358 The Ramayana For idle search and long delay, And our fierce king will bid us die The favour of his friend to buy.” Then Tára softly spake to cheer The Vánars' hearts oppressed by fear: “Despair no more, your doubts dispel: Come in this ample cavern dwell. There may we live in blissful ease Mid springs and fruit and bloomy trees, Secure from every foe's assault, For magic framed the wondrous vault. Protected there we need not fear Though Ráma and our king come near; Nor dread e'en him who batters down The portals of the foeman's town.”756 Canto LIV. Hanumán's Speech. But Hanumán, while Tára, best Of splendid chiefs his thought expressed, Perceived that Báli's princely son A kingdom for himself had won.757 His keen eye marked in him combined The warrior's arm, the ruler's mind, 756 Purandara, the destroyer of cities; the cities being the clouds which the God of the firmament bursts open with his thunderbolts, to release the waters imprisoned in these fortresses of the demons of drought. 757 Perceived that Angad had secured, through the love of the Vánars, the reversion of Sugríva's kingdom; or, as another commentator explains it, per- ceived that Angad had obtained a new kingdom in the enchanted cave which the Vánars, through love of him, would consent to occupy.
- **Translation**: 

---

### Verse 12 (Ramayana 0.1377)
- **Original**: Canto LIV. Hanumán's Speech. 1359 And every noble gift should grace The happy sovereign of his race: Marked how he grew with ripening age More glorious and bold and sage,— Like the young moon that night by night Shines on with ever waxing light,— Brave as his royal father, wise As he who counsels in the skies:758 Marked how, forwearied with the quest, He heeded not his liege's hest, But Tára's every word obeyed Like Indra still byZukra759 swayed. Then with his prudent speech he tried To better thoughts the prince to guide, And by division's skilful art The Vánars and the youth to part: “Illustrious Angad, thou in fight Hast far surpassed thy father's might, Most worthy, like thy sire of old, The empire of our race to hold. The Vánars' fickle people range From wish to wish and welcome change. Their wives and babes they will not leave And to their new-made sovereign cleave. No art, no gifts will draw away The Vánars from Sugríva's sway, Through hope of wealth, through fear of pain Still faithful will they all remain. Thou fondly hopest in this cave The vengeance of the foe to brave. But LakshmaG's arm a shower will send Of deadly shafts those walls to rend. 758 V [ihaspati, Lord of Speech, the Preceptor of the Gods. 759 Zukra is the regent of the planet Venus, and the preceptor of the Daityas.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1378)
- **Original**: 1360 The Ramayana Like Indra's bolts his shafts have power To cleave the mountain like a flower. O Angad, mark my counsel well: If in this cave thou choose to dwell,[385] These Vánar hosts with one accord Will quit thee for their lawful lord, And turn again with thirsty eyes To wife and babe and all they prize. Thou in the lonely cavern left Of followers and friends bereft, Wilt be in all thy woe, alas, Weak as a blade of trembling grass: And Lakshma G's arrows, keen and fierce From his strong bow, thy heart will pierce. But if in lowly reverence meek Sugríva's court with us thou seek, He, as thy birth demands, will share The kingdom with the royal heir. Thy loving kinsman, true and wise, Looks on thee still with favouring eyes. Firm in his promise, pure is he, And ne'er will vex or injure thee. He loves thy mother, lives for her A faithful friend and worshipper. That mother's love thou mayst not spurn: Her only child, return, return.” Canto LV. Angad's Reply.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1379)
- **Original**: Canto LV. Angad's Reply. 1361 “What truth or justice canst thou find,” Cried Angad,“in Sugríva's mind? Where is his high and generous soul, His purity and self-control? How is he worthy of our trust, Righteous, and true, and wise, and just, Who, shrinking not from sin and shame, Durst take his living brother's dame? Who, when, in stress of mortal strife His noble brother fought for life, Against the valiant warrior barred The portal which he stood to guard? Can he be grateful— he who took The hand of Ráma, and forsook That friend who saved him in his woes, To whom his life and fame he owes? Ah no! his heart is cold and mean, What bids him search for Ráma's queen? Not honour's law, not friendship's debt, But angry LakshmaG's timely threat. No prudent heart will ever place Its trust in one so false and base, Who heeds not friendship, kith or kin, Who scorns the law and cleaves to sin. But true or false, whate'er he be, One consequence I clearly see; Me, in my youth anointed heir Against his wish, he will not spare, But strike with eager hand the blow That rids him of a household foe. Shall I of power and friends despoiled, In all my purpose crossed and foiled,— Shall I Kishkindhá seek, and wait, Like some poor helpless thing, my fate?
- **Translation**: 

---

### Verse 15 (Ramayana 0.1380)
- **Original**: 1362 The Ramayana The cruel wretch through lust of sway Will seize upon his hapless prey, And to a prison's secret gloom The remnant of my years will doom. 'Tis better far to fast and die Than hopeless bound in chains to lie, Your steps, O Vánars, homeward bend And leave me here my life to end. Better to die of hunger here Than meet at home the fate I fear. Go, bow you at Sugríva's feet, And in my name the monarch greet. Before the sons of Raghu bend, And give the greeting that I send. Greet kindly Rumá too, for she A son's affection claims from me, And gently calm with friendly care My mother Tárá's wild despair; Or when she hears her darling's fate The queen will die disconsolate.” Thus Angad bade the chiefs adieu: Then on the ground his limbs he threw Where sacred Darbha760 grass was spread, And wept as every hope had fled. The moving words of Angad drew Down aged cheeks the piteous dew. And, as the chieftains' eyes grew dim, They swore to stay and die with him. On holy grass whose every blade 760 The name of various kinds of grass used at sacrificial ceremonies, especial- ly, of the Ku[a grass, Poa cynosuroides, which was used to strew the ground in preparing for a sacrifice, the officiating Brahmans being purified by sitting on it.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1381)
- **Original**: Canto LVI. Sampáti. 1363 Was duly, pointing southward, laid, The Vánars sat them down and bent Their faces to the orient, While “Here, O comrades, let us die With Angad,” was the general cry. Canto LVI. Sampáti. Then came the vultures' mighty king Where sat the Vánars sorrowing,— Sampáti,761 best of birds that fly On sounding pinions through the sky, Jamáyus' brother, famed of old, Most glorious and strong and bold. Upon the slope of Vindhya's hill He saw the Vánars calm and still. [386] These words he uttered while the sight Filled his fierce spirit with delight: “Behold how Fate with changeless laws Within his toils the sinner draws, And brings me, after long delay, A rich and noble feast to-day, These Vánars who are doomed to die My hungry maw to satisfy.” 761 Sampáti is the eldest son of the celebrated Garu a the king of birds.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1382)
- **Original**: 1364 The Ramayana He spoke no more: and Angad heard The menace of the mighty bird; And thus, while anguish filled his breast, The noble Hanumán addressed: “Vivasvat's762 son has sought this place For vengeance on the Vánar race. See, Yáma, wroth for Sítá's sake, Is come our guilty lives to take. Our king's decree is left undone, And naught achieved for Raghu's son. In duty have we failed, and hence Comes punishment for dire offence. Have we not heard the marvels wrought By King Jamáyus,763 how he fought With RávaG's might, and, nobly brave, Perished, the Maithil queen to save? There is no living creature, none, But loves to die for Raghu's son, And in long toils and dangers we Have placed our lives in jeopardy. Blest is Jamáyus, he who gave His life the Maithil queen to save, And proved his love for Ráma well When by the giant's hand he fell. Now raised to bliss and high renown He fears not fierce Sugríva's frown. Alas, alas! what miseries spring From that rash promise of the king!764 His own sad death, and Ráma sent With LakshmaG forth to banishment: The Maithil lady borne away: 762 Vivasvat or the Sun is the father of Yáma the God of Death. 763 Book III, Canto LI. 764 Da [aratha's rash oath and fatal promise to his wife Kaikeyí.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1383)
- **Original**: Canto LVII. Angad's Speech. 1365 Jamáyus slain in mortal fray: The fall of Báli when the dart Of Ráma quivered in his heart: And, after toil and pain and care, Our misery and deep despair.” He ceased: the feathered monarch heard, His heart with ruth and wonder stirred: “Whose is that voice,” the vulture cried, “That tells me how Jamáyus died, And shakes my inmost soul with woe For a loved brother's overthrow? After long days at length I hear The glorious name of one so dear. Once more, O Vánar chieftains, tell How King Jamáyus fought and fell. But first your aid, I pray you, lend, And from this peak will I descend. The sun has burnt my wings, and I No longer have the power to fly.” Canto LVII. Angad's Speech. Though grief and woe his utterance broke They trusted not the words he spoke; But, looking still for secret guile, Reflected in their hearts a while: “If on our mangled limbs he feed, We gain the death ourselves decreed.”
- **Translation**: 

---

### Verse 19 (Ramayana 0.1384)
- **Original**: 1366 The Ramayana Then rose the Vánar chiefs, and lent Their arms to aid the bird's descent; And Angad spake:“There lived of yore A noble Vánar king who bore The name of Riksharajas, great And brave and strong and fortunate. His sons were like their father: fame Knows Báli and Sugríva's name. Praised in all lands, a glorious king Was Báli, and from him I spring. Brave Ráma, Da[aratha's heir, A glorious prince beyond compare, His sire and duty's law obeyed, And sought the depths of DaG ak' shade Sítá his well-beloved dame, And Lakshma G, with the wanderer came. A giant watched his hour, and stole The sweet delight of Ráma's soul. Jamáyus, Da[aratha's friend, Swift succour to the dame would lend. Fierce RávaG from his car he felled, And for a time the prize withheld. But bleeding, weak with years, and tired, Beneath the demon's blows expired, Due rites at Ráma's hands obtained, And bliss that ne'er shall minish, gained. Then Ráma with Sugríva made A covenant for mutual aid, And Báli, to the field defied, By conquering Ráma's arrow died. Sugríva then, by Ráma's grace, Was monarch of the Vánar race. By his command a mighty host Seeks Ráma's queen from coast to coast.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1385)
- **Original**: Canto LVIII. Tidings Of Sítá. 1367 Sent forth by him, in every spot We looked for her, but find her not. Vain is the toil, as though by night We sought to find the Day-God's light. In lands unknown at length we found A spacious cavern under ground, Whose vaults that stretch beneath the hill Were formed by Maya's magic skill. Through the dark maze our steps were bent, And wandering there a month we spent, [387] And lost, in fruitless error, thus The days our king allotted us. Thus we though faithful have transgressed, And failed to keep our lord's behest. No chance of safety can we see, No lingering hope of life have we. Sugríva's wrath and Ráma's hate Press on our souls with grievous weight: And we, because 'tis vain to fly, Resolve at length to fast and die.” Canto LVIII. Tidings Of Sítá. The piteous tears his eye bedewed As thus his speech the bird renewed; “Alas my brother, slain in fight By RávaG's unresisted might! I, old and wingless, weak and worn, O'er his sad fate can only mourn. Fled is my youth: in life's decline My former strength no more is mine.
- **Translation**: 

---

