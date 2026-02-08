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

### Verse 1 (Ramayana 0.346)
- **Original**: 328 The Ramayana Good Da [aratha, free from stain, By whose most gracious favour we Ráma anointed king shall see.” Such were the words the townsmen spoke Heard by the gathering countryfolk, Who from the south, north, east, and west, Stirred by the joyful tidings, pressed. For by their eager longing led To Ráma's consecration sped The villagers from every side, And filled Ayodhyá's city wide. This way and that way strayed the crowd, While rose a murmur long and loud, As when the full moon floods the skies And Ocean's waves with thunder rise. That town, like Indra's city fair, While peasants thronged her ways, Tumultuous roared like Ocean, where Each flood-born monster plays. Canto VII. Manthará's Lament. It chanced a slave-born handmaid, bred With Queen Kaikeyí, fancy-led, Mounted the stair and stood upon The terrace like the moon that shone. Thence Manthará at ease surveyed Ayodhyá to her eyes displayed, Where water cooled the royal street, Where heaps of flowers were fresh and sweet,
- **Translation**: 

---

### Verse 2 (Ramayana 0.347)
- **Original**: Canto VII. Manthará's Lament. 329 And costly flags and pennons hung On roof and tower their shadow flung; With covered ways prepared in haste, And many an awning newly placed; With sandal-scented streams bedewed, Thronged by a new bathed multitude: Whose streets were full of Bráhman bands With wreaths and sweetmeats in their hands. Loud instruments their music raised, And through the town, where'er she gazed, The doors of temples glittered white, And the maid marvelled at the sight. Of Ráma's nurse who, standing by, Gazed with a joy-expanded eye, In robes of purest white attired, The wondering damsel thus inquired: “Does Ráma's mother give away Rich largess to the crowds to-day, On some dear object fondly bent, Or blest with measureless content? What mean these signs of rare delight On every side that meet my sight? Say, will the king with joy elate Some happy triumph celebrate?”
- **Translation**: 

---

### Verse 3 (Ramayana 0.348)
- **Original**: 330 The Ramayana The nurse, with transport uncontrolled, Her glad tale to the hump-back told: “Our lord the king to-morrow morn Will consecrate his eldest-born, And raise, in Pushya's favouring hour, Prince Ráma to the royal power.” As thus the nurse her tidings spoke, Rage in the hump-back's breast awoke. Down from the terrace, like the head Of high Kailása's hill, she sped. Sin in her thoughts, her soul aflame, Where Queen Kaikeyí slept, she came:[097] “Why sleepest thou?” she cried,“arise, Peril is near, unclose thine eyes. Ah, heedless Queen, too blind to know What floods of sin above thee flow! Thy boasts of love and grace are o'er: Thine is the show and nothing more. His favour is an empty cheat, A torrent dried by summer's heat.” Thus by the artful maid addressed In cruel words from raging breast, The queen, sore troubled, spoke in turn; “What evil news have I to learn? That mournful eye, that altered cheek Of sudden woe or danger speak.” Such were the words Kaikeyí said: Then Manthará, her eyeballs red With fury, skilled with treacherous art To grieve yet more her lady's heart, From Ráma, in her wicked hate, Kaikeyí's love to alienate,
- **Translation**: 

---

### Verse 4 (Ramayana 0.349)
- **Original**: Canto VII. Manthará's Lament. 331 Upon her evil purpose bent Began again most eloquent: “Peril awaits thee swift and sure, And utter woe defying cure; King Da[aratha will create Prince Ráma Heir Associate. Plunged in the depths of wild despair, My soul a prey to pain and care, As though the flames consumed me, zeal Has brought me for my lady's weal, Thy grief, my Queen, is grief to me: Thy gain my greatest gain would be. Proud daughter of a princely line, The rights of consort queen are thine. How art thou, born of royal race, Blind to the crimes that kings debase? Thy lord is gracious, to deceive, And flatters, but thy soul to grieve, While thy pure heart that thinks no sin Knows not the snares that hem thee in. Thy husband's lips on thee bestow Soft soothing word, an empty show: The wealth, the substance, and the power This day will be Kau[alyá's dower. With crafty soul thy child he sends To dwell among thy distant friends, And, every rival far from sight, To Ráma gives the power and might. Ah me! for thou, unhappy dame, Deluded by a husband's name, With more than mother's love hast pressed A serpent to thy heedless breast, And cherished him who works thee woe, No husband but a deadly foe.
- **Translation**: 

---

### Verse 5 (Ramayana 0.350)
- **Original**: 332 The Ramayana For like a snake, unconscious Queen, Or enemy who stabs unseen, King Da[aratha all untrue Has dealt with thee and Bharat too. Ah, simple lady, long beguiled By his soft words who falsely smiled! Poor victim of the guileless breast, A happier fate thou meritest. For thee and thine destruction waits When he Prince Ráma consecrates. Up, lady, while there yet is time; Preserve thyself, prevent the crime. Up, from thy careless ease, and free Thyself, O Queen, thy son, and me!” Delighted at the words she said, Kaikeyí lifted from the bed, Like autumn's moon, her radiant head, And joyous at the tidings gave A jewel to the hump-back slave; And as she gave the precious toy She cried in her exceeding joy: “Take this, dear maiden, for thy news Most grateful to mine ear, and choose What grace beside most fitly may The welcome messenger repay. I joy that Ráma gains the throne: Kau [alyá's son is as mine own.” Canto VIII. Manthará's Speech.
- **Translation**: 

---

### Verse 6 (Ramayana 0.351)
- **Original**: Canto VIII. Manthará's Speech. 333 The damsel's breast with fury burned: She answered, as the gift she spurned: “What time, O simple Queen, is this For idle dreams of fancied bliss? Hast thou not sense thy state to know, Engulfed in seas of whelming woe; Sick as I am with grief and pain My lips can scarce a laugh restrain To see thee hail with ill-timed joy A peril mighty to destroy. I mourn for one so fondly blind: What woman of a prudent mind Would welcome, e'en as thou hast done, The lordship of a rival's son, Rejoiced to find her secret foe Empowered, like death, to launch the blow; I see that Ráma still must fear Thy Bharat, to his throne too near. Hence is my heart disquieted, For those who fear are those we dread. Lakshma G, the mighty bow who draws, With all his soul serves Ráma's cause; And chains as strong to Bharat bind Zatrughna, with his heart and mind, Now next to Ráma, lady fair, Thy Bharat is the lawful heir: And far remote, I ween, the chance That might the younger two advance. Yes, Queen, 'tis Ráma that I dread, Wise, prompt, in warlike science bred; And oh, I tremble when I think Of thy dear child on ruin's brink. [098] Blest with a lofty fate is she, Kau [alyá; for her son will be
- **Translation**: 

---

### Verse 7 (Ramayana 0.352)
- **Original**: 334 The Ramayana Placed, when the moon and Pushya meet, By Bráhmans on the royal seat, Thou as a slave in suppliant guise Must wait upon Kau[alyá's eyes, With all her wealth and bliss secured And glorious from her foes assured. Her slave with us who serve thee, thou Wilt see thy son to Ráma bow, And Sítá's friends exult o'er all, While Bharat's wife shares Bharat's fall.” As thus the maid in wrath complained, Kaikeyí saw her heart was pained, And answered eager in defence Of Ráma's worth and excellence: “Nay, Ráma, born the monarch's heir, By holy fathers trained with care, Virtuous, grateful, pure, and true, Claims royal sway as rightly due. He, like a sire, will long defend Each brother, minister, and friend. Then why, O hump-back, art thou pained To hear that he the throne has gained? Be sure when Ráma's empire ends, The kingdom to my son descends, Who, when a hundred years are flown, Shall sit upon his fathers' throne. Why is thine heart thus sad to see The joy that is and long shall be, This fortune by possession sure And hopes which we may count secure? Dear as the darling son I bore Is Ráma, yea, or even more. Most duteous to Kau[alyá, he
- **Translation**: 

---

### Verse 8 (Ramayana 0.353)
- **Original**: Canto VIII. Manthará's Speech. 335 Is yet more dutiful to me. What though he rule, we need not fear: His brethren to his soul are dear. And if the throne Prince Ráma fill Bharat will share the empire still.” She ceased. The troubled damsel sighed Sighs long and hot, and thus replied: “What madness has possessed thy mind, To warnings deaf, to dangers blind? Canst thou not see the floods of woe That threaten o'er thine head to flow: First Ráma will the throne acquire, Then Ráma's son succeed his sire, While Bharat will neglected pine Excluded from the royal line. Not all his sons, O lady fair, The kingdom of a monarch share: All ruling when a sovereign dies Wild tumult in the state would rise. The eldest, be he good or ill, Is ruler by the father's will. Know, tender mother, that thy son Without a friend and all undone, Far from the joyous ease of home An alien from his race will roam. I sped to thee for whom I feel, But thy fond heart mistakes my zeal, Thy hand a present would bestow Because thy rival triumphs so. When Ráma once begins his sway Without a foe his will to stay, Thy darling Bharat he will drive To distant lands if left alive.
- **Translation**: 

---

### Verse 9 (Ramayana 0.354)
- **Original**: 336 The Ramayana By thee the child was sent away Beneath his grandsire's roof to stay. Even in stocks and stones perforce Will friendship spring from intercourse. The youngZatrughna too would go With Bharat, for he loved him so. As LakshmaG still to Ráma cleaves, He his dear Bharat never leaves. There is an ancient tale they tell: A tree the foresters would fell Was saved by reeds that round it stood, For love that sprang of neighbourhood. So LakshmaG Ráma will defend, And each on each for aid depend. Such fame on earth their friendship wins As that which binds the Heavenly Twins. And Ráma ne'er will purpose wrong To LakshmaG, for their love is strong. But Bharat, Oh, of this be sure, Must evil at his hands endure. Come, Ráma from his home expel An exile in the woods to dwell. The plan, O Queen, which I advise Secures thy weal if thou be wise. So we and all thy kith and kin Advantage from thy gain shall win. Shall Bharat, meet for happier fate, Born to endure his rival's hate, With all his fortune ruined cower And dread his brother's mightier power! Up, Queen, to save thy son, arise; Prostrate at Ráma's feet he lies. So the proud elephant who leads His trooping consorts through the reeds
- **Translation**: 

---

### Verse 10 (Ramayana 0.355)
- **Original**: Canto IX. The Plot. 337 Falls in the forest shade beneath The lion's spring and murderous teeth. Scorned by thee in thy bliss and pride Kau [alyá was of old defied, And will she now forbear to show The vengeful rancour of a foe? O Queen, thy darling is undone When Ráma's hand has once begun Ayodhyá's realm to sway, Come, win the kingdom for thy child And drive the alien to the wild In banishment to-day.” Canto IX. The Plot. As fury lit Kaikeyí's eyes She spoke with long and burning sighs: [099] “This day my son enthroned shall see, And Ráma to the woods shall flee. But tell me, damsel, if thou can, A certain way, a skilful plan That Bharat may the empire gain, And Ráma's hopes be nursed in vain.” The lady ceased. The wicked maid The mandate of her queen obeyed, And darkly plotting Ráma's fall Responded to Kaikeyí's call.
- **Translation**: 

---

### Verse 11 (Ramayana 0.356)
- **Original**: 338 The Ramayana “I will declare, do thou attend, How Bharat may his throne ascend. Dost thou forget what things befell? Or dost thou feign, remembering well? Or wouldst thou hear my tongue repeat A story for thy need so meet? Gay lady, if thy will be so, Now hear the tale of long ago, And when my tongue has done its part Ponder the story in thine heart. When Gods and demons fought of old, Thy lord, with royal saints enrolled, Sped to the war with thee to bring His might to aid the Immortals' King. Far to the southern land he sped Where DaG ak's mighty wilds are spread, To Vaijayanta's city swayed By Zambara, whose flag displayd The hugest monster of the sea. Lord of a hundred wiles was be; With might which Gods could never blame Against the King of Heaven he came. Then raged the battle wild and dread, And mortal warriors fought and bled; The fiends by night with strength renewed Charged, slew the sleeping multitude. Thy lord, King Da[aratha, long Stood fighting with the demon throng, But long of arm, unmatched in strength, Fell wounded by their darts at length. Thy husband, senseless, by thine aid Was from the battle field conveyed, And wounded nigh to death thy lord Was by thy care to health restored.
- **Translation**: 

---

### Verse 12 (Ramayana 0.357)
- **Original**: Canto IX. The Plot. 339 Well pleased the grateful monarch sware To grant thy first and second prayer. Thou for no favour then wouldst sue, The gifts reserved for season due; And he, thy high-souled lord, agreed To give the boons when thou shouldst need. Myself I knew not what befell, But oft the tale have heard thee tell, And close to thee in friendship knit Deep in my heart have treasured it. Remind thy husband of his oath, Recall the boons and claim them both, That Bharat on the throne be placed With rites of consecration graced, And Ráma to the woods be sent For twice seven years of banishment. Go, Queen, the mourner's chamber270 seek, With angry eye and burning cheek; And with disordered robes and hair On the cold earth lie prostrate there. When the king comes still mournful lie, Speak not a word nor meet his eye, But let thy tears in torrent flow, And lie enamoured of thy woe. Well do I know thou long hast been, And ever art, his darling queen. For thy dear sake, O well-loved dame, The mighty king would brave the flame, But ne'er would anger thee, or brook To meet his favourite's wrathful look. Thy loving lord would even die 270 Literallythe chamber of wrath,a “growlery,” a small, dark, unfurnished room to which it seems, the wives and ladies of the king betook themselves when offended and sulky.
- **Translation**: 

---

### Verse 13 (Ramayana 0.358)
- **Original**: 340 The Ramayana Thy fancy, Queen, to gratify, And never could he arm his breast To answer nay to thy request. Listen and learn, O dull of sense, Thine all-resistless influence. Gems he will offer, pearls and gold: Refuse his gifts, be stern and cold. Those proffered boons at length recall, And claim them till he grants thee all. And O my lady, high in bliss, With heedful thought forget not this. When from the ground his queen he lifts And grants again the promised gifts, Bind him with oaths he cannot break And thy demands unflnching, make. That Ráma travel to the wild Five years and nine from home exiled, And Bharat, best of all who reign, The empire of the land obtain. For when this term of years has fled Over the banished Ráma's head, Thy royal son to vigour grown And rooted firm will stand alone. The king, I know, is well inclined, And this the hour to move his mind. Be bold: the threatened rite prevent, And force the king from his intent.” She ceased. So counselled to her bane Disguised beneath a show of gain, Kaikeyí in her joy and pride To Manthará again replied: “Thy sense I envy, prudent maid; With sagest lore thy lids persuade.
- **Translation**: 

---

### Verse 14 (Ramayana 0.359)
- **Original**: Canto IX. The Plot. 341 No hump-back maid in all the earth, For wise resolve, can match thy worth. Thou art alone with constant zeal Devoted to thy lady's weal. Dear girl, without thy faithful aid I had not marked the plot he laid. [100] Full of all guile and sin and spite Misshapen hump-backs shock the sight: But thou art fair and formed to please, Bent like a lily by the breeze. I look thee o'er with watchful eye, And in thy frame no fault can spy; The chest so deep, the waist so trim, So round the lines of breast and limb.271 Thy cheeks with moonlike beauty shine, And the warm wealth of youth is thine. Thy legs, my girl, are long and neat, And somewhat long thy dainty feet, While stepping out before my face Thou seemest like a crane to pace. The thousand wiles are in thy breast Which Zambara the fiend possessed, And countless others all thine own, O damsel sage, to thee are known. Thy very hump becomes thee too, O thou whose face is fair to view, For there reside in endless store Plots, wizard wiles, and warrior lore. A golden chain I'll round it fling When Ráma's flight makes Bharat king: Yea, polished links of finest gold, When once the wished for prize I hold 271 In these four lines I do not translate faithfully, and I do not venture to follow Kaikeyí farther in her eulogy of the hump-back's charms.
- **Translation**: 

---

### Verse 15 (Ramayana 0.360)
- **Original**: 342 The Ramayana With naught to fear and none to hate, Thy hump, dear maid, shall decorate. A golden frontlet wrought with care, And precious jewels shalt thou wear: Two lovely robes around thee fold, And walk a Goddess to behold, Bidding the moon himself compare His beauty with a face so fair. With scent of precious sandal sweet Down to the nails upon thy feet, First of the household thou shalt go And pay with scorn each battled foe.” Kaikeyí's praise the damsel heard, And thus again her lady stirred, Who lay upon her beauteous bed Like fire upon the altar fed: “Dear Queen, they build the bridge in vain When swollen streams are dry again. Arise, thy glorious task complete, And draw the king to thy retreat.” The large-eyed lady left her bower Exulting in her pride of power, And with the hump-back sought the gloom And silence of the mourner's room. The string of priceless pearls that hung Around her neck to earth she flung, With all the wealth and lustre lent By precious gem and ornament. Then, listening to her slave's advice, Lay, like a nymph from Paradise. As on the ground her limbs she laid Once more she cried unto the maid:
- **Translation**: 

---

### Verse 16 (Ramayana 0.361)
- **Original**: Canto IX. The Plot. 343 “Soon must thou to the monarch say Kaikeyí's soul has past away, Or, Ráma banished as we planned, My son made king shall rule the land. No more for gold and gems I care, For brave attire or dainty fare. If Ráma should the throne ascend, That very hour my life will end.” The royal lady wounded through The bosom with the darts that flew Launched from the hump-back's tongue Pressed both her hands upon her side, And o'er and o'er again she cried With wildering fury stung: “Yes, it shall be thy task to tell That I have hurried hence to dwell In Yáma's realms of woe, Or happy Bharat shall be king, And doomed to years of wandering Kau [alyá's son shall go. I heed not dainty viands now Fair wreaths of flowers to twine my brow, Soft balm or precious scent: My very life I count as naught, Nothing on earth can claim my thought But Ráma's banishment.” She spoke these words of cruel ire; Then stripping off her gay attire, The cold bare floor she pressed. So, falling from her home on high, Some lovely daughter of the sky Upon the ground might rest. With darkened brow and furious mien,
- **Translation**: 

---

### Verse 17 (Ramayana 0.362)
- **Original**: 344 The Ramayana Stripped of her gems and wreath, the queen In spotless beauty lay, Like heaven obscured with gathering cloud, When shades of midnight darkness shroud Each star's expiring ray. Canto X. Dasaratha's Speech. As Queen Kaikeyí thus obeyed The sinful counsel of her maid She sank upon the chamber floor, As sinks in anguish, wounded sore, An elephant beneath the smart Of the wild hunter's venomed dart. The lovely lady in her mind Revolved the plot her maid designed, And prompt the gain and risk to scan She step by step approved the plan. Misguided by the hump-back's guile She pondered her resolve awhile, As the fair path that bliss secured The miserable lady lured,[101] Devoted to her queen, and swayed By hopes of gain and bliss, the maid Rejoiced, her lady's purpose known, And deemed the prize she sought her own. Then bent upon her purpose dire, Kaikeyí with her soul on fire, Upon the floor lay, languid, down, Her brows contracted in a frown. The bright-hued wreath that bound her hair,
- **Translation**: 

---

### Verse 18 (Ramayana 0.363)
- **Original**: Canto X. Dasaratha's Speech. 345 Chains, necklets, jewels rich and rare, Stripped off by her own fingers lay Spread on the ground in disarray, And to the floor a lustre lent As stars light up the firmament. Thus prostrate in the mourner's cell, In garb of woe the lady fell, Her long hair in a single braid, Like some fair nymph of heaven dismayed.272 The monarch, Ráma to install, With thoughtful care had ordered all, And now within his home withdrew, Dismissing first his retinue. Now all the town has heard, thought he, What joyful rite the morn will see. So turned he to her bower to cheer With the glad news his darling's ear. Majestic, as the Lord of Night, When threatened by the Dragon's might, Bursts radiant on the evening sky Pale with the clouds that wander by, So Da[aratha, great in fame, To Queen Kaikeyí's palace came. There parrots flew from tree to tree, And gorgeous peacocks wandered free, While ever and anon was heard The note of some glad water-bird. Here loitered dwarf and hump-backed maid, There lute and lyre sweet music played. 272 These verses are evidently an interpolation. They contain nothing that has not been already related: the words only are altered. As the whole poem could not be recited at once, the rhapsodists at the beginning of a fresh recitation would naturally remind their hearers of the events immediately preceding.
- **Translation**: 

---

### Verse 19 (Ramayana 0.364)
- **Original**: 346 The Ramayana Here, rich in blossom, creepers twined O'er grots with wondrous art designed, There Champac and A[oka flowers Hung glorious o'er the summer bowers, And mid the waving verdure rose Gold, silver, ivory porticoes. Through all the months in ceaseless store The trees both fruit and blossom bore. With many a lake the grounds were graced; Seats gold and silver, here were placed; Here every viand wooed the taste, It was a garden meet to vie E'en with the home of Gods on high. Within the mansion rich and vast The mighty Da[aratha passed: Not there was his beloved queen On her fair couch reclining seen. With love his eager pulses beat For the dear wife he came to meet, And in his blissful hopes deceived, He sought his absent love and grieved. For never had she missed the hour Of meeting in her sumptuous bower, And never had the king of men Entered the empty room till then. Still urged by love and anxious thought News of his favourite queen he sought, For never had his loving eyes Found her or selfish or unwise. Then spoke at length the warder maid, With hands upraised and sore afraid: “My Lord and King, the queen has sought The mourner's cell with rage distraught.”
- **Translation**: 

---

### Verse 20 (Ramayana 0.365)
- **Original**: Canto X. Dasaratha's Speech. 347 The words the warder maiden said He heard with soul disquieted, And thus as fiercer grief assailed, His troubled senses wellnigh failed. Consumed by torturing fires of grief The king, the world's imperial chief, His lady lying on the ground In most unqueenly posture, found. The aged king, all pure within, Saw the young queen resolved on sin, Low on the ground, his own sweet wife, To him far dearer than his life, Like some fair creeping plant uptorn, Or like a maid of heaven forlorn, A nymph of air or Goddess sent From Swarga down in banishment. As some wild elephant who tries To soothe his consort as she lies Struck by the hunter's venomed dart, So the great king disturbed in heart, Strove with soft hand and fond caress To soothe his darling queen's distress, And in his love addressed with sighs The lady of the lotus eyes: “I know not, Queen, why thou shouldst be Thus angered to the heart with me. Say, who has slighted thee, or whence Has come the cause of such offence That in the dust thou liest low, And rendest my fond heart with woe, As if some goblin of the night Had struck thee with a deadly blight, And cast foul influence on her
- **Translation**: 

---

