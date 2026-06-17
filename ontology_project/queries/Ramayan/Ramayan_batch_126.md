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

### Verse 1 (Ramayana 0.546)
- **Original**: 528 The Ramayana Before the high souled chief they bent, With circling steps around him went, And then with bitter wailing, they Departed each his several way. Like the great sun engulfed by night, The hero sped beyond their sight, While still the people mourned his fate And wept aloud disconsolate. The car-borne chieftain passed the bound Of Ko[ala's delightful ground, Where grain and riches bless the land, And people give with liberal hand: A lovely realm unvexed by fear, Where countless shrines and stakes323 appear: Where mango-groves and gardens grow, And streams of pleasant water flow: Where dwells content a well-fed race, And countless kine the meadows grace: Filled with the voice of praise and prayer: Each hamlet worth a monarch's care. Before him three-pathed Gangá rolled Her heavenly waters bright and cold; O'er her pure breast no weeds were spread, Her banks were hermit-visited. The car-borne hero saw the tide That ran with eddies multiplied, And thus the charioteer addressed: “Here on the bank to-day we rest. Not distant from the river, see! There grows a lofty Ingudí With blossoms thick on every spray: There rest we, charioteer, to-day. 323 Sacrificial posts to which the victims were tied.
- **Translation**: 

---

### Verse 2 (Ramayana 0.547)
- **Original**: Canto L. The Halt Under The Ingudí. 529 I on the queen of floods will gaze, Whose holy stream has highest praise, Where deer, and bird, and glittering snake, God, Daitya, bard their pastime take.” Sumantra, LakshmaG gave assent, And with the steeds they thither went. When Ráma reached the lovely tree, With Sítá and with LakshmaG, he Alighted from the car: with speed Sumantra loosed each weary steed. And, hand to hand in reverence laid, Stood near to Ráma in the shade. Ráma's dear friend, renowned by fame, Who of Nisháda lineage came, Guha, the mighty chief, adored Through all the land as sovereign lord, Soon as he heard that prince renowned Was resting on Nisháda ground, Begirt by counsellor and peer And many an honoured friend drew near. Soon as the monarch came in view, Ráma and LakshmaG toward him flew. Then Guha, at the sight distressed, His arms around the hero pressed, Laid both his hands upon his head Bowed to those lotus feet, and said: “O Ráma, make thy wishes known, And be this kingdom as thine own. Who, mighty-armed, will ever see A guest so dear as thou to me?”
- **Translation**: 

---

### Verse 3 (Ramayana 0.548)
- **Original**: 530 The Ramayana He placed before him dainty fare Of every flavour, rich and rare, Brought forth the gift for honoured guest, And thus again the chief addressed: “Welcome, dear Prince, whose arms are strong; These lands and all to thee belong. Thy servants we, our lord art thou; Begin, good king, thine empire now. See, various food before thee placed, And cups to drink and sweets to taste For thee soft beds are hither borne, And for thy horses grass and corn.” To Guha as he pressed and prayed, Thus Raghu's son his answer made: “'Twas aye thy care my heart to please With honour, love, and courtesies, And friendship brings thee now to greet Thy guest thus humbly on thy feet.” Again the hero spake, as round The king his shapely arms he wound: “Guha, I see that all is well With thee and those who with thee dwell; That health and bliss and wealth attend Thy realm, thyself, and every friend. But all these friendly gifts of thine, Bound to refuse, I must decline. Grass, bark, and hide my only wear, And woodland roots and fruit my fare, On duty all my heart is set; I seek the woods, an anchoret. A little grass and corn to feed The horses— this is all I need.
- **Translation**: 

---

### Verse 4 (Ramayana 0.549)
- **Original**: Canto L. The Halt Under The Ingudí. 531 So by this favour, King, alone Shall honour due to me be shown. For these good steeds who brought me here Are to my sire supremely dear; And kind attention paid to these Will honour me and highly please.” Then Guha quickly bade his train Give water to the steeds, and grain. And Ráma, ere the night grew dark, Paid evening rites in dress of bark, And tasted water, on the strand, Drawn from the stream by LakshmaG's hand. And Lakshma G with observance meet Bathed his beloved brother's feet, [153] Who rested with his Maithil spouse: Then sat him down 'neath distant boughs. And Guha with his bow sat near To LakshmaG and the charioteer, And with the prince conversing kept His faithful watch while Ráma slept. As Da[aratha's glorious heir, Of lofty soul and wisdom rare, Reclining with his Sítá there Beside the river lay— He who no troubles e'er had seen, Whose life a life of bliss had been— That night beneath the branches green Passed pleasantly away.
- **Translation**: 

---

### Verse 5 (Ramayana 0.550)
- **Original**: 532 The Ramayana Canto LI. Lakshman's Lament. As LakshmaG still his vigil held By unaffected love impelled, Guha, whose heart the sight distressed, With words like these the prince addressed: “Beloved youth, this pleasant bed Was brought for thee, for thee is spread; On this, my Prince, thine eyelids close, And heal fatigue with sweet repose. My men are all to labour trained, But hardship thou hast ne'er sustained. All we this night our watch will keep And guard Kakutstha's son asleep. In all the world there breathes not one More dear to me than Raghu's son. The words I speak, heroic youth, Are true: I swear it by my truth. Through his dear grace supreme renown Will, so I trust, my wishes crown. So shall my life rich store obtain Of merit, blest with joy and gain. While Raghu's son and Sítá lie Entranced in happy slumber, I Will, with my trusty bow in hand, Guard my dear friend with all my band. To me, who oft these forests range, Is naught therein or new or strange. We could with equal might oppose A four-fold army led by foes.”
- **Translation**: 

---

### Verse 6 (Ramayana 0.551)
- **Original**: Canto LI. Lakshman's Lament. 533 Then royal LakshmaG made reply: “With thee to stand as guardian nigh, Whose faithful soul regards the right, Fearless we well might rest to-night. But how, when Ráma lays his head With Sítá on his lowly bed,— How can I sleep? how can I care For life, or aught that's bright and fair? Behold the conquering chief, whose might Is match for Gods and fiends in fight; With Sítá now he rests his head Asleep on grass beneath him spread. Won by devotion, text, and prayer, And many a rite performed with care, Chief of our father's sons he shines Well marked, like him, with favouring signs. Brief, brief the monarch's life will be Now his dear son is forced to flee; And quickly will the widowed state Mourn for her lord disconsolate. Each mourner there has wept her fill; The cries of anguish now are still: In the king's hall each dame, o'ercome With weariness of woe is dumb. This first sad night of grief, I ween, Will do to death each sorrowing queen: Scarce is Kau[alyá left alive; My mother, too, can scarce survive. If when her heart is fain to break, She lingers forZatrughna's sake, Kau [alyá, mother of the chief, Must sink beneath the chilling grief. That town which countless thousands fill, Whose hearts with love of Ráma thrill,—
- **Translation**: 

---

### Verse 7 (Ramayana 0.552)
- **Original**: 534 The Ramayana The world's delight, so rich and fair,— Grieved for the king, his death will share. The hopes he fondly cherished, crossed Ayodhyá's throne to Ráma lost,— With mournful cries, Too late, too late! The king my sire will meet his fate. And when my sire has passed away, Most happy in their lot are they, Allowed, with every pious care, Part in his funeral rites to bear. And O, may we with joy at last,— These years of forest exile past,— Turn to Ayodhyá's town to dwell With him who keeps his promise well!” While thus the hero mighty-souled, In wild lament his sorrow told, Faint with the load that on him lay, The hours of darkness passed away. As thus the prince, impelled by zeal For his loved brother, prompt to feel Strong yearnings for the people's weal, His words of truth outspake, King Guha grieved to see his woe, Heart-stricken, gave his tears to flow, Tormented by the common blow, Sad, as a wounded snake. Canto LII. The Crossing Of Gangá.
- **Translation**: 

---

### Verse 8 (Ramayana 0.553)
- **Original**: Canto LII. The Crossing Of Gangá. 535 Soon as the shades of night had fled, Uprising from his lowly bed, Ráma the famous, broad of chest, His brother LakshmaG thus addressed: “Now swift upsprings the Lord of Light, And fled is venerable night. [154] That dark-winged bird the Koïl now Is calling from the topmost bough, And sounding from the thicket nigh Is heard the peacock's early cry. Come, cross the flood that seeks the sea, The swiftly flowing Jáhnaví.”324 King Guha heard his speech, agreed, And called his minister with speed: “A boat,” he cried,“swift, strong, and fair, With rudder, oars, and men, prepare, And place it ready by the shore To bear the pilgrims quickly o'er.” Thus Guha spake: his followers all Bestirred them at their master's call; Then told the king that ready manned A gay boat waited near the strand. Then Guha, hand to hand applied, With reverence thus to Ráma cried: “The boat is ready by the shore: How, tell me, can I aid thee more? O lord of men, it waits for thee To cross the flood that seeks the sea. O godlike keeper of thy vow, Embark: the boat is ready now.” 324 Daughter of Jahnu, a name of the Ganges. See p. 55.
- **Translation**: 

---

### Verse 9 (Ramayana 0.554)
- **Original**: 536 The Ramayana Then Ráma, lord of glory high, Thus to King Guha made reply: “Thanks for thy gracious care, my lord: Now let the gear be placed on board.” Each bow-armed chief, in mail encased, Bound sword and quiver to his waist, And then with Sítá near them hied Down the broad river's shelving side. Then with raised palms the charioteer, In lowly reverence drawing near, Cried thus to Ráma good and true: “Now what remains for me to do?” With his right hand, while answering The hero touched his friend: “Go back,” he said,“and on the king With watchful care attend. Thus far, Sumantra, thou wast guide; Now to Ayodhyá turn,” he cried: “Hence seek we leaving steeds and car, On foot the wood that stretches far.” Sumantra, when, with grieving heart, He heard the hero bid him part, Thus to the bravest of the brave, Ikshváku's son, his answer gave: “In all the world men tell of naught, To match thy deed, by heroes wrought— Thus with thy brother and thy wife Thrall-like to lead a forest life. No meet reward of fruit repays Thy holy lore, thy saintlike days, Thy tender soul, thy love of truth, If woe like this afflicts thy youth. Thou, roaming under forest boughs
- **Translation**: 

---

### Verse 10 (Ramayana 0.555)
- **Original**: Canto LII. The Crossing Of Gangá. 537 With thy dear brother and thy spouse Shalt richer meed of glory gain Than if three worlds confessed thy reign. Sad is our fate, O Ráma: we, Abandoned and repelled by thee, Must serve as thralls Kaikeyí's will, Imperious, wicked, born to ill.” Thus cried the faithful charioteer, As Raghu's son, in rede his peer, Was fast departing on his road,— And long his tears of anguish flowed. But Ráma, when those tears were dried His lips with water purified, And in soft accents, sweet and clear, Again addressed the charioteer: “I find no heart, my friend, like thine, So faithful to Ikshváku's line. Still first in view this object keep, That ne'er for me my sire may weep. For he, the world's far-ruling king, Is old, and wild with sorrow's sting; With love's great burthen worn and weak: Deem this the cause that thus I speak Whate'er the high-souled king decrees His loved Kaikeyí's heart to please, Yea, be his order what it may, Without demur thou must obey, For this alone great monarchs reign, That ne'er a wish be formed in vain. Then, O Sumantra, well provide That by no check the king be tried: Nor let his heart in sorrow pine: This care, my faithful friend, be thine.
- **Translation**: 

---

### Verse 11 (Ramayana 0.556)
- **Original**: 538 The Ramayana The honoured king my father greet, And thus for me my words repeat To him whose senses are controlled, Untired till now by grief, and old; “I, Sítá, LakshmaG sorrow not, O Monarch, for our altered lot: The same to us, if here we roam, Or if Ayodhyá be our home, The fourteen years will quickly fly, The happy hour will soon be nigh When thou, my lord, again shalt see Lakshma G, the Maithil dame, and me.” Thus having soothed, O charioteer, My father and my mother dear, Let all the queens my message learn, But to Kaikeyí chiefly turn. With loving blessings from the three, From LakshmaG, Sítá, and from me, My mother, Queen Kau[alyá, greet With reverence to her sacred feet. And add this prayer of mine:“O King; Send quickly forth and Bharat bring, And set him on the royal throne Which thy decree has made his own. When he upon the throne is placed, When thy fond arms are round him laced, Thine aged heart will cease to ache With bitter pangs for Ráma's sake.”[155] And say to Bharat:“See thou treat The queens with all observance meet: What care the king receives, the same Show thou alike to every dame. Obedience to thy father's will Who chooses thee the throne to fill,
- **Translation**: 

---

### Verse 12 (Ramayana 0.557)
- **Original**: Canto LII. The Crossing Of Gangá. 539 Will earn for thee a store of bliss Both in the world to come and this.’ ” Thus Ráma bade Sumantra go With thoughtful care instructed so. Sumantra all his message heard, And spake again, by passion stirred: “O, should deep feeling mar in aught The speech by fond devotion taught, Forgive whate'er I wildly speak: My love is strong, my tongue is weak. How shall I, if deprived of thee, Return that mournful town to see: Where sick at heart the people are Because their Ráma roams afar. Woe will be theirs too deep to brook When on the empty car they look, As when from hosts, whose chiefs are slain, One charioteer comes home again. This very day, I ween, is food Forsworn by all the multitude, Thinking that thou, with hosts to aid, Art dwelling in the wild wood's shade. The great despair, the shriek of woe They uttered when they saw thee go, Will, when I come with none beside, A hundred-fold be multiplied. How to Kau[alyá can I say: “O Queen, I took thy son away, And with thy brother left him well: Weep not for him; thy woe dispel?” So false a tale I cannot frame, Yet how speak truth and grieve the dame? How shall these horses, fleet and bold,
- **Translation**: 

---

### Verse 13 (Ramayana 0.558)
- **Original**: 540 The Ramayana Whom not a hand but mine can hold, Bear others, wont to whirl the car Wherein Ikshváku's children are! Without thee, Prince, I cannot, no, I cannot to Ayodhyá go. Then deign, O Ráma, to relent, And let me share thy banishment. But if no prayers can move thy heart, If thou wilt quit me and depart, The flames shall end my car and me, Deserted thus and reft of thee. In the wild wood when foes are near, When dangers check thy vows austere, Borne in my car will I attend, All danger and all care to end. For thy dear sake I love the skill That guides the steed and curbs his will: And soon a forest life will be As pleasant, for my love of thee. And if these horses near thee dwell, And serve thee in the forest well, They, for their service, will not miss The due reward of highest bliss. Thine orders, as with thee I stray, Will I with heart and head obey, Prepared, for thee, without a sigh, To lose Ayodhyá or the sky. As one defiled with hideous sin, I never more can pass within Ayodhyá, city of our king, Unless beside me thee I bring. One wish is mine, I ask no more, That, when thy banishment is o'er I in my car may bear my lord,
- **Translation**: 

---

### Verse 14 (Ramayana 0.559)
- **Original**: Canto LII. The Crossing Of Gangá. 541 Triumphant, to his home restored. The fourteen years, if spent with thee, Will swift as light-winged moments flee; But the same years, without thee told, Were magnified a hundred-fold. Do not, kind lord, thy servant leave, Who to his master's son would cleave, And the same path with him pursue, Devoted, tender, just and true.” Again, again Sumantra made His varied plaint, and wept and prayed. Him Raghu's son, whose tender breast Felt for his servants, thus addressed: “O faithful servant, well my heart Knows how attached and true thou art. Hear thou the words I speak, and know Why to the town I bid thee go. Soon as Kaikeyí, youngest queen, Thy coming to the town has seen, No doubt will then her mind oppress That Ráma roams the wilderness. And so the dame, her heart content With proof of Ráma's banishment, Will doubt the virtuous king no more As faithless to the oath he swore. Chief of my cares is this, that she, Youngest amid the queens, may see Bharat her son securely reign O'er rich Ayodhyá's wide domain. For mine and for the monarch's sake Do thou thy journey homeward take, And, as I bade, repeat each word That from my lips thou here hast heard.”
- **Translation**: 

---

### Verse 15 (Ramayana 0.560)
- **Original**: 542 The Ramayana Thus spake the prince, and strove to cheer The sad heart of the charioteer, And then to royal Guha said These words most wise and spirited: “Guha, dear friend, it is not meet That people throng my calm retreat: For I must live a strict recluse, And mould my life by hermits' use. I now the ancient rule accept By good ascetics gladly kept. I go: bring fig-tree juice that I In matted coils my hair may tie.” Quick Guha hastened to produce, For the king's son, that sacred juice. Then Ráma of his long locks made, And Lakshma G's too, the hermit braid.[156] And the two royal brothers there With coats of bark and matted hair, Transformed in lovely likeness stood To hermit saints who love the wood. So Ráma, with his brother bold, A pious anchorite enrolled, Obeyed the vow which hermits take, And to his friend, King Guha, spake: “May people, treasure, army share, And fenced forts, thy constant care: Attend to all: supremely hard The sovereign's task, to watch and guard.”
- **Translation**: 

---

### Verse 16 (Ramayana 0.561)
- **Original**: Canto LII. The Crossing Of Gangá. 543 Ikshváku's son, the good and brave, This last farewell to Guha gave, And then, with LakshmaG and his bride, Determined, on his way he hied. Soon as he viewed, upon the shore, The bark prepared to waft them o'er Impetuous Gangá's rolling tide, To LakshmaG thus the chieftain cried: “Brother, embark; thy hand extend, Thy gentle aid to Sítá lend: With care her trembling footsteps guide, And place the lady by thy side.” When Lakshma G heard, prepared to aid, His brother's words he swift obeyed. Within the bark he placed the dame, Then to her side the hero came. Next LakshmaG's elder brother, lord Of brightest glory, when on board, Breathing a prayer for blessings, meet For priest or warrior to repeat, Then he and car-borne LakshmaG bent, Well-pleased, their heads, most reverent, Their hands, with Sítá, having dipped, As Scripture bids, and water sipped, Farewell to wise Sumantra said, And Guha, with the train he led. So Ráma took, on board, his stand, And urged the vessel from the land. Then swift by vigorous arms impelled Her onward course the vessel held, And guided by the helmsman through The dashing waves of Gangá flew. Half way across the flood they came, When Sítá, free from spot and blame,
- **Translation**: 

---

### Verse 17 (Ramayana 0.562)
- **Original**: 544 The Ramayana Her reverent hands together pressed, The Goddess of the stream addressed: “May the great chieftain here who springs From Da[aratha, best of kings, Protected by thy care, fulfil His prudent father's royal will. When in the forest he has spent His fourteen years of banishment, With his dear brother and with me His home again my lord shall see. Returning on that blissful day, I will to thee mine offerings pay, Dear Queen, whose waters gently flow, Who canst all blessed gifts bestow. For, three-pathed Queen, though wandering here, Thy waves descend from Brahmá's sphere, Spouse of the God o'er floods supreme, Though rolling here thy glorious stream. To thee, fair Queen, my head shall bend, To thee shall hymns of praise ascend, When my brave lord shall turn again, And, joyful, o'er his kingdom reign. To win thy grace, O Queen divine, A hundred thousand fairest kine, And precious robes and finest meal Among the Bráhmans will I deal. A hundred jars of wine shall flow, When to my home, O Queen, I go; With these, and flesh, and corn, and rice, Will I, delighted, sacrifice. Each hallowed spot, each holy shrine That stands on these fair shores of thine, Each fane and altar on thy banks Shall share my offerings and thanks.
- **Translation**: 

---

### Verse 18 (Ramayana 0.563)
- **Original**: Canto LII. The Crossing Of Gangá. 545 With me and LakshmaG, free from harm, May he the blameless, strong of arm, Reseek Ayodhyá from the wild, O blameless Lady undefiled!” As, praying for her husband's sake, The faultless dame to Gangá spake, To the right bank the vessel flew With her whose heart was right and true. Soon as the bark had crossed the wave, The lion leader of the brave, Leaving the vessel on the strand, With wife and brother leapt to land. Then Ráma thus the prince addressed Who filled with joy Sumitrá's breast: “Be thine alike to guard and aid In peopled spot, in lonely shade. Do thou, Sumitrá's son, precede: Let Sítá walk where thou shalt lead. Behind you both my place shall be, To guard the Maithil dame and thee. For she, to woe a stranger yet, No toil or grief till now has met; The fair Videhan will assay The pains of forest life to-day. To-day her tender feet must tread Rough rocky wilds around her spread: No tilth is there, no gardens grow, No crowding people come and go.”
- **Translation**: 

---

### Verse 19 (Ramayana 0.564)
- **Original**: 546 The Ramayana The hero ceased: and LakshmaG led Obedient to the words he said: And Sítá followed him, and then Came Raghu's pride, the lord of men. With Sítá walking o'er the sand They sought the forest, bow in hand, But still their lingering glances threw Where yet Sumantra stood in view. Sumantra, when his watchful eye The royal youths no more could spy, Turned from the spot whereon he stood Homeward with Guha from the wood.[157] Still on the brothers forced their way Where sweet birds sang on every spray, Though scarce the eye a path could find Mid flowering trees where creepers twined. Far on the princely brothers pressed, And stayed their feet at length to rest Beneath a fig tree's mighty shade With countless pendent shoots displayed. Reclining there a while at ease, They saw, not far, beneath fair trees A lake with many a lotus bright That bore the name of Lovely Sight. Ráma his wife's attention drew, And Lakshma G's, to the charming view: “Look, brother, look how fair the flood Glows with the lotus, flower and bud!” They drank the water fresh and clear, And with their shafts they slew a deer. A fire of boughs they made in haste, And in the flame the meat they placed. So Raghu's sons with Sítá shared
- **Translation**: 

---

### Verse 20 (Ramayana 0.565)
- **Original**: Canto LIII. Ráma's Lament. 547 The hunter's meal their hands prepared, Then counselled that the spreading tree Their shelter and their home should be. Canto LIII. Ráma's Lament. When evening rites were duly paid, Reclined beneath the leafy shade, To LakshmaG thus spake Ráma, best Of those who glad a people's breast: “Now the first night has closed the day That saw us from our country stray, And parted from the charioteer; Yet grieve not thou, my brother dear. Henceforth by night, when others sleep, Must we our careful vigil keep, Watching for Sítá's welfare thus, For her dear life depends on us. Bring me the leaves that lie around, And spread them here upon the ground, That we on lowly beds may lie, And let in talk the night go by.”
- **Translation**: 

---

