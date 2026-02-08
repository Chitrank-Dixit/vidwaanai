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

### Verse 1 (Ramayana 0.606)
- **Original**: 588 The Ramayana Of the old crime his hand had wrought, And thus to Queen Kau[alyá cried Who still for Ráma moaned and sighed: “If thou art waking, give, I pray, Attention to the words I say. Whate'er the conduct men pursue, Be good or ill the acts they do, Be sure, dear Queen, they find the meed Of wicked or of virtuous deed. A heedless child we call the man Whose feeble judgment fails to scan The weight of what his hands may do, Its lightness, fault, and merit too. One lays the Mango garden low, And bids the gay Palá[as grow: Longing for fruit their bloom he sees, But grieves when fruit should bend the trees. Cut by my hand, my fruit-trees fell, Palá[a trees I watered well. My hopes this foolish heart deceive, And for my banished son I grieve. Kau [alyá, in my youthful prime Armed with my bow I wrought the crime, Proud of my skill, my name renowned, An archer prince who shoots by sound. The deed this hand unwitting wrought This misery on my soul has brought, As children seize the deadly cup And blindly drink the poison up. As the unreasoning man may be Charmed with the gay Palá[a tree, I unaware have reaped the fruit Of joying at a sound to shoot. As regent prince I shared the throne,
- **Translation**: 

---

### Verse 2 (Ramayana 0.607)
- **Original**: Canto LXIII. The Hermit's Son. 589 Thou wast a maid to me unknown, The early Rain-time duly came, And strengthened love's delicious flame. The sun had drained the earth that lay All glowing 'neath the summer day, And to the gloomy clime had fled Where dwell the spirits of the dead.335 The fervent heat that moment ceased, The darkening clouds each hour increased And frogs and deer and peacocks all Rejoiced to see the torrents fall. Their bright wings heavy from the shower, The birds, new-bathed, had scarce the power To reach the branches of the trees Whose high tops swayed beneath the breeze. The fallen rain, and falling still, Hung like a sheet on every hill, Till, with glad deer, each flooded steep Showed glorious as the mighty deep. The torrents down its wooded side Poured, some unstained, while others dyed [169] Gold, ashy, silver, ochre, bore The tints of every mountain ore. In that sweet time, when all are pleased, My arrows and my bow I seized; Keen for the chase, in field or grove, Down Sarjú's bank my car I drove. I longed with all my lawless will Some elephant by night to kill, Some buffalo that came to drink, Or tiger, at the river's brink. When all around was dark and still, 335 The southern region is the abode of Yama the Indian Pluto, and of departed spirits.
- **Translation**: 

---

### Verse 3 (Ramayana 0.608)
- **Original**: 590 The Ramayana I heard a pitcher slowly fill, And thought, obscured in deepest shade, An elephant the sound had made. I drew a shaft that glittered bright, Fell as a serpent's venomed bite; I longed to lay the monster dead, And to the mark my arrow sped. Then in the calm of morning, clear A hermit's wailing smote my ear: “Ah me, ah me,” he cried, and sank, Pierced by my arrow, on the bank. E'en as the weapon smote his side, I heard a human voice that cried: “Why lights this shaft on one like me, A poor and harmless devotee? I came by night to fill my jar From this lone stream where no men are. Ah, who this deadly shaft has shot? Whom have I wronged, and knew it not? Why should a boy so harmless feel The vengeance of the winged steel? Or who should slay the guiltless son Of hermit sire who injures none, Who dwells retired in woods, and there Supports his life on woodland fare? Ah me, ah me, why am I slain, What booty will the murderer gain? In hermit coils I bind my hair, Coats made of skin and bark I wear. Ah, who the cruel deed can praise Whose idle toil no fruit repays, As impious as the wretch's crime Who dares his master's bed to climb? Nor does my parting spirit grieve
- **Translation**: 

---

### Verse 4 (Ramayana 0.609)
- **Original**: Canto LXIII. The Hermit's Son. 591 But for the life which thus I leave: Alas, my mother and my sire,— I mourn for them when I expire. Ah me, that aged, helpless pair, Long cherished by my watchful care, How will it be with them this day When to the Five336 I pass away? Pierced by the self-same dart we die, Mine aged mother, sire, and I. Whose mighty hand, whose lawless mind Has all the three to death consigned?” When I, by love of duty stirred, That touching lamentation heard, Pierced to the heart by sudden woe, I threw to earth my shafts and bow. My heart was full of grief and dread As swiftly to the place I sped, Where, by my arrow wounded sore, A hermit lay on Sarjú's shore. His matted hair was all unbound, His pitcher empty on the ground, And by the fatal arrow pained, He lay with dust and gore distained. I stood confounded and amazed: His dying eyes to mine he raised, And spoke this speech in accents stern, As though his light my soul would burn: “How have I wronged thee, King, that I Struck by thy mortal arrow die? The wood my home, this jar I brought, And water for my parents sought. This one keen shaft that strikes me through 336 The five elements of which the body consists, and to which it returns.
- **Translation**: 

---

### Verse 5 (Ramayana 0.610)
- **Original**: 592 The Ramayana Slays sire and aged mother too. Feeble and blind, in helpless pain, They wait for me and thirst in vain. They with parched lips their pangs must bear, And hope will end in blank despair. Ah me, there seems no fruit in store For holy zeal or Scripture lore, Or else ere now my sire would know That his dear son is lying low. Yet, if my mournful fate he knew, What could his arm so feeble do? The tree, firm-rooted, ne'er may be The guardian of a stricken tree. Haste to my father, and relate While time allows, my sudden fate, Lest he consume thee as the fire Burns up the forest, in his ire. This little path, O King, pursue: My father's cot thou soon wilt view. There sue for pardon to the sage, Lest he should curse thee in his rage. First from the wound extract the dart That kills me with its deadly smart, E'en as the flushed impetuous tide Eats through the river's yielding side.” I feared to draw the arrow out, And pondered thus in painful doubt: “Now tortured by the shaft he lies, But if I draw it forth he dies.” Helpless I stood, faint, sorely grieved: The hermit's son my thought perceived; As one o'ercome by direst pain He scarce had strength to speak again.
- **Translation**: 

---

### Verse 6 (Ramayana 0.611)
- **Original**: Canto LXIV. Dasaratha's Death. 593 With writhing limb and struggling breath, Nearer and ever nearer death “My senses undisturbed remain, And fortitude has conquered pain: Now from one tear thy soul be freed. Thy hand has made a Bráhman bleed. Let not this pang thy bosom wring: No twice-born youth am I, O King, [170] For of a Vai[ya sire I came, Who wedded with aZúdra dame.” These words the boy could scarcely say, As tortured by the shaft he lay, Twisting his helpless body round, Then trembling senseless on the ground. Then from his bleeding side I drew The rankling shaft that pierced him through. With death's last fear my face he eyed, And, rich in store of penance, died.” Canto LXIV. Dasaratha's Death. The son of Raghu to his queen Thus far described the unequalled scene, And, as the hermit's death he rued, The mournful story thus renewed: “The deed my heedless hand had wrought Perplexed me with remorseful thought, And all alone I pondered still How kindly deed might salve the ill. The pitcher from the ground I took,
- **Translation**: 

---

### Verse 7 (Ramayana 0.612)
- **Original**: 594 The Ramayana And filled it from that fairest brook, Then, by the path the hermit showed, I reached his sainted sire's abode. I came, I saw: the aged pair, Feeble and blind, were sitting there, Like birds with clipped wings, side by side, With none their helpless steps to guide. Their idle hours the twain beguiled With talk of their returning child, And still the cheering hope enjoyed, The hope, alas, by me destroyed. Then spoke the sage, as drawing near The sound of footsteps reached his ear: “Dear son, the water quickly bring; Why hast thou made this tarrying? Thy mother thirsts, and thou hast played, And bathing in the brook delayed. She weeps because thou camest not; Haste, O my son, within the cot. If she or I have ever done A thing to pain thee, dearest son, Dismiss the memory from thy mind: A hermit thou, be good and kind. On thee our lives, our all, depend: Thou art thy friendless parents' friend. The eyeless couple's eye art thou: Then why so cold and silent now?” With sobbing voice and bosom wrung I scarce could move my faltering tongue, And with my spirit filled with dread I looked upon the sage, and said, While mind, and sense, and nerve I strung To fortify my trembling tongue,
- **Translation**: 

---

### Verse 8 (Ramayana 0.613)
- **Original**: Canto LXIV. Dasaratha's Death. 595 And let the aged hermit know His son's sad fate, my fear and woe: “High-minded Saint, not I thy child, A warrior, Da[aratha styled. I bear a grievous sorrow's weight Born of a deed which good men hate. My lord, I came to Sarjú's shore, And in my hand my bow I bore For elephant or beast of chase That seeks by night his drinking place. There from the stream a sound I heard As if a jar the water stirred. An elephant, I thought, was nigh: I aimed, and let an arrow fly. Swift to the place I made my way, And there a wounded hermit lay Gasping for breath: the deadly dart Stood quivering in his youthful heart. I hastened near with pain oppressed; He faltered out his last behest. And quickly, as he bade me do, From his pierced side the shaft I drew. I drew the arrow from the rent, And up to heaven the hermit went, Lamenting, as from earth he passed, His aged parents to the last. Thus, unaware, the deed was done: My hand, unwitting, killed thy son. For what remains, O, let me win Thy pardon for my heedless sin.” As the sad tale of sin I told The hermit's grief was uncontrolled. With flooded eyes, and sorrow-faint,
- **Translation**: 

---

### Verse 9 (Ramayana 0.614)
- **Original**: 596 The Ramayana Thus spake the venerable saint: I stood with hand to hand applied, And listened as he spoke and sighed: “If thou, O King, hadst left unsaid By thine own tongue this tale of dread, Thy head for hideous guilt accursed Had in a thousand pieces burst. A hermit's blood by warrior spilt, In such a case, with purposed guilt, Down from his high estate would bring Even the thunder's mighty King. And he a dart who conscious sends Against the devotee who spends His pure life by the law of Heaven— That sinner's head will split in seven. Thou livest, for thy heedless hand Has wrought a deed thou hast not planned, Else thou and all of Raghu's line Had perished by this act of thine. Now guide us,” thus the hermit said, “Forth to the spot where he lies dead. Guide us, this day, O Monarch, we For the last time our son would see: The hermit dress of skin he wore Rent from his limbs distained with gore; His senseless body lying slain, His soul in Yama's dark domain.” Alone the mourning pair I led, Their souls with woe disquieted, And let the dame and hermit lay[171] Their hands upon the breathless clay. The father touched his son, and pressed The body to his aged breast;
- **Translation**: 

---

### Verse 10 (Ramayana 0.615)
- **Original**: Canto LXIV. Dasaratha's Death. 597 Then falling by the dead boy's side, He lifted up his voice, and cried: “Hast thou no word, my child, to say? No greeting for thy sire to-day? Why art thou angry, darling? why Wilt thou upon the cold earth lie? If thou, my son, art wroth with me, Here, duteous child, thy mother see. What! no embrace for me, my son? No word of tender love— not one? Whose gentle voice, so soft and clear, Soothing my spirit, shall I hear When evening comes, with accents sweet Scripture or ancient lore repeat? Who, having fed the sacred fire, And duly bathed, as texts require, Will cheer, when evening rites are done, The father mourning for his son? Who will the daily meal provide For the poor wretch who lacks a guide, Feeding the helpless with the best Berries and roots, like some dear guest? How can these hands subsistence find For thy poor mother, old and blind? The wretched votaress how sustain, Who mourns her child in ceaseless pain? Stay yet a while, my darling, stay, Nor fly to Yama's realm to-day. To-morrow I thy sire and she Who bare thee, child, will go with, thee.337 337 So dying York cries over the body of Suffolk: “Tarry, dear cousin Suffolk! My soul shall thine keep company to heaven:
- **Translation**: 

---

### Verse 11 (Ramayana 0.616)
- **Original**: 598 The Ramayana Then when I look on Yama, I To great Vivasvat's son will cry: “Hear, King of justice, and restore Our child to feed us, I implore. Lord of the world, of mighty fame, Faithful and just, admit my claim, And grant this single boon to free My soul from fear, to one like me.” Because, my son, untouched by stain, By sinful hands thou fallest slain, Win, through thy truth, the sphere where those Who die by hostile darts repose. Seek the blest home prepared for all The valiant who in battle fall, Who face the foe and scorn to yield, In glory dying on the field. Rise to the heaven where Dhundhumár And Nahush, mighty heroes, are, Where Janamejay and the blest Dilípa, Sagar, Saivya, rest: Home of all virtuous spirits, earned By fervent rites and Scripture learned: By those whose sacred fires have glowed, Whose liberal hands have fields bestowed: By givers of a thousand cows, By lovers of one faithful spouse: By those who serve their masters well, And cast away this earthly shell. None of my race can ever know The bitter pain of lasting woe. But doomed to that dire fate is he Tarry, sweet soul, for mine, then fly abreast.” King Henry V, Act IV, 6.
- **Translation**: 

---

### Verse 12 (Ramayana 0.617)
- **Original**: Canto LXIV. Dasaratha's Death. 599 Whose guilty hand has slaughtered thee.” Thus with wild tears the aged saint Made many a time his piteous plaint, Then with his wife began to shed The funeral water for the dead. But in a shape celestial clad, Won by the merits of the lad, The spirit from the body brake And to the mourning parents spake: “A glorious home in realms above Rewards my care and filial love. You, honoured parents, soon shall be Partakers of that home with me.” He spake, and swiftly mounting high, With Indra near him, to the sky On a bright car, with flame that glowed, Sublime the duteous hermit rode. The father, with his consort's aid, The funeral rites with water paid, And thus his speech to me renewed Who stood in suppliant attitude: “Slay me this day, O, slay me, King, For death no longer has a sting. Childless am I: thy dart has done To death my dear, my only son. Because the boy I loved so well Slain by thy heedless arrow fell, My curse upon thy soul shall press With bitter woe and heaviness. I mourn a slaughtered child, and thou Shalt feel the pangs that kill me now. Bereft and suffering e'en as I,
- **Translation**: 

---

### Verse 13 (Ramayana 0.618)
- **Original**: 600 The Ramayana So shalt thou mourn thy son, and die. Thy hand unwitting dealt the blow That laid a holy hermit low, And distant, therefore, is the time When thou shalt suffer for the crime. The hour shall come when, crushed by woes Like these I feel, thy life shall close: A debt to pay in after days Like his the priestly fee who pays.” This curse on me the hermit laid, Nor yet his tears and groans were stayed. Then on the pyre their bodies cast The pair; and straight to heaven they passed. As in sad thought I pondered long Back to my memory came the wrong Done in wild youth, O lady dear, When 'twas my boast to shoot by ear.[172] The deed has borne the fruit, which now Hangs ripe upon the bending bough: Thus dainty meats the palate please, And lure the weak to swift disease. Now on my soul return with dread The words that noble hermit said, That I for a dear son should grieve, And of the woe my life should leave.” Thus spake the king with many a tear; Then to his wife he cried in fear: “I cannot see thee, love; but lay Thy gentle hand in mine, I pray. Ah me, if Ráma touched me thus, If once, returning home to us, He bade me wealth and lordship give,
- **Translation**: 

---

### Verse 14 (Ramayana 0.619)
- **Original**: Canto LXIV. Dasaratha's Death. 601 Then, so I think, my soul would live. Unlike myself, unjust and mean Have been my ways with him, my Queen, But like himself is all that he, My noble son, has done to me. His son, though far from right he stray, What prudent sire would cast away? What banished son would check his ire, Nor speak reproaches of his sire? I see thee not: these eyes grow blind, And memory quits my troubled mind. Angels of Death are round me: they Summon my soul with speed away. What woe more grievous can there be, That, when from light and life I flee, I may not, ere I part, behold My virtuous Ráma, true and bold? Grief for my son, the brave and true, Whose joy it was my will to do, Dries up my breath, as summer dries The last drop in the pool that lies. Not men, but blessed Gods, are they Whose eyes shall see his face that day; See him, when fourteen years are past, With earrings decked return at last. My fainting mind forgets to think: Low and more low my spirits sink. Each from its seat, my senses steal: I cannot hear, or taste, or feel. This lethargy of soul o'ercomes Each organ, and its function numbs: So when the oil begins to fail, The torch's rays grow faint and pale. This flood of woe caused by this hand
- **Translation**: 

---

### Verse 15 (Ramayana 0.620)
- **Original**: 602 The Ramayana Destroys me helpless and unmanned, Resistless as the floods that bore A passage through the river shore. Ah Raghu's son, ah mighty-armed, By whom my cares were soothed and charmed, My son in whom I took delight, Now vanished from thy father's sight! Kau [alyá, ah, I cannot see; Sumitrá, gentle devotee! Alas, Kaikeyí, cruel dame, My bitter foe, thy father's shame!” Kau [alyá and Sumitrá kept Their watch beside him as he wept. And Da [aratha moaned and sighed, And grieving for his darling died. Canto LXV. The Women's Lament. And now the night had past away, And brightly dawned another day; The minstrels, trained to play and sing, Flocked to the chamber of the king: Bards, who their gayest raiment wore, And heralds famed for ancient lore: And singers, with their songs of praise, Made music in their several ways. There as they poured their blessings choice And hailed their king with hand and voice, Their praises with a swelling roar Echoed through court and corridor.
- **Translation**: 

---

### Verse 16 (Ramayana 0.621)
- **Original**: Canto LXV. The Women's Lament. 603 Then as the bards his glory sang, From beaten palms loud answer rang, As glad applauders clapped their hands, And told his deeds in distant lands. The swelling concert woke a throng Of sleeping birds to life and song: Some in the branches of the trees, Some caged in halls and galleries. Nor was the soft string music mute; The gentle whisper of the lute, And blessings sung by singers skilled The palace of the monarch filled. Eunuchs and dames of life unstained, Each in the arts of waiting trained, Drew near attentive as before, And crowded to the chamber door: These skilful when and how to shed The lustral stream o'er limb and head, Others with golden ewers stood Of water stained with sandal wood. And many a maid, pure, young, and fair, Her load of early offerings bare, Cups of the flood which all revere, And sacred things, and toilet gear. Each several thing was duly brought As rule of old observance taught, And lucky signs on each impressed Stamped it the fairest and the best. There anxious, in their long array, All waited till the shine of day: But when the king nor rose nor spoke, Doubt and alarm within them woke. Forthwith the dames, by duty led, Attendants on the monarch's bed,
- **Translation**: 

---

### Verse 17 (Ramayana 0.622)
- **Original**: 604 The Ramayana Within the royal chamber pressed To wake their master from his rest. Skilled in the lore of dreaming, they First touched the bed on which he lay. But none replied; no sound was heard,[173] Nor hand, nor head, nor body stirred. They trembled, and their dread increased, Fearing his breath of life had ceased, And bending low their heads, they shook Like the tall reeds that fringe the brook. In doubt and terror down they knelt, Looked on his face, his cold hand felt, And then the gloomy truth appeared Of all their hearts had darkly feared. Kau [alyá and Sumitrá, worn With weeping for their sons, forlorn, Woke not, but lay in slumber deep And still as death's unending sleep. Bowed down by grief, her colour fled, Her wonted lustre dull and dead, Kau [alyá shone not, like a star Obscured behind a cloudy bar. Beside the king's her couch was spread, And next was Queen Sumitrá's bed, Who shone no more with beauty's glow, Her face bedewed with tears of woe. There lapped in sleep each wearied queen, There as in sleep, the king was seen; And swift the troubling thought came o'er Their spirits that he breathed no more. At once with wailing loud and high The matrons shrieked a bitter cry, As widowed elephants bewail Their dead lord in the woody vale.
- **Translation**: 

---

### Verse 18 (Ramayana 0.623)
- **Original**: Canto LXV. The Women's Lament. 605 At the loud shriek that round them rang, Kau [alyá and Sumitrá sprang Awakened from their beds, with eyes Wide open in their first surprise. Quick to the monarch's side they came, And saw and touched his lifeless frame; One cry, O husband! forth they sent, And prostrate to the ground they went. The king of Ko[al's daughter338 there Writhed, with the dust on limb and hair Lustreless, as a star might lie Hurled downward from the glorious sky. When the king's voice in death was stilled, The women who the chamber filled Saw, like a widow elephant slain, Kau [alyá prostrate in her pain. Then all the monarch's ladies led By Queen Kaikeyí at their head, Poured forth their tears, and weeping so, Sank on the ground, consumed by woe. The cry of grief so long and loud Went up from all the royal crowd, That, doubled by the matron train, It made the palace ring again. Filled with dark fear and eager eyes, Anxiety and wild surmise; Echoing with the cries of grief Of sorrowing friends who mourned their chief, Dejected, pale with deep distress, Hurled from their height of happiness: Such was the look the palace wore Where lay the king who breathed no more. 338 Kau [alyá, daughter of the king of another Ko[al.
- **Translation**: 

---

### Verse 19 (Ramayana 0.624)
- **Original**: 606 The Ramayana Canto LXVI. The Embalming. Kau [alyá's eyes with tears o'erflowed, Weighed down by varied sorrows' load; On her dead lord her gaze she bent, Who lay like fire whose might is spent, Like the great deep with waters dry, Or like the clouded sun on high. Then on her lap she laid his head. And on Kaikeyí looked and said: “Triumphant now enjoy thy reign Without a thorn thy side to pain. Thou hast pursued thy single aim, And killed the king, O wicked dame. Far from my sight my Ráma flies, My perished lord has sought the skies. No friend, no hope my life to cheer, I cannot tread the dark path here. Who would forsake her husband, who That God to whom her love is due, And wish to live one hour, but she Whose heart no duty owns, like thee? The ravenous sees no fault: his greed Will e'en on poison blindly feed. Kaikeyí, through a hump-back maid, This royal house in death has laid. King Janak, with his queen, will hear Heart rent like me the tidings drear Of Ráma banished by the king, Urged by her impious counselling. No son has he, his age is great, And sinking with the double weight, He for his darling child will pine, And pierced with woe his life resign.
- **Translation**: 

---

### Verse 20 (Ramayana 0.625)
- **Original**: Canto LXVI. The Embalming. 607 Sprung from Videha's monarch, she A sad and lovely devotee, Roaming the wood, unmeet for woe, Will toil and trouble undergo. She in the gloomy night with fear The cries of beast and bird will hear, And trembling in her wild alarm Will cling to Ráma's sheltering arm. Ah, little knows my duteous son That I am widowed and undone— My Ráma of the lotus eye, Gone hence, gone hence, alas, to die. Now, as a living wife and true, I, e'en this day, will perish too: Around his form these arms will throw And to the fire with him will go.” Clasping her husband's lifeless clay A while the weeping votaress lay, Till chamberlains removed her thence [174] O'ercome by sorrow's violence. Then in a cask of oil they laid Him who in life the world had swayed, And finished, as the lords desired, All rites for parted souls required. The lords, all-wise, refused to burn The monarch ere his son's return; So for a while the corpse they set Embalmed in oil, and waited yet. The women heard: no doubt remained, And wildly for the king they plained. With gushing tears that drowned each eye Wildly they waved their arms on high, And each her mangling nails impressed
- **Translation**: 

---

