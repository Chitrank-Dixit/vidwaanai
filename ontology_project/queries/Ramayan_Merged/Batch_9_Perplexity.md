# Merged Batch 9 (Files 129-144)
# Assigned Agent: Perplexity



--- Start of Ramayan_batch_129.md ---

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



--- End of Ramayan_batch_129.md ---


--- Start of Ramayan_batch_130.md ---

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

### Verse 1 (Ramayana 0.626)
- **Original**: 608 The Ramayana Deep in her head and knee and breast: “Of Ráma reft,— who ever spake The sweetest words the heart to take, Who firmly to the truth would cling,— Why dost thou leave us, mighty King? How can the consorts thou hast left Widowed, of Raghu's son bereft, Live with our foe Kaikeyí near, The wicked queen we hate and fear? She threw away the king, her spite Drove Ráma forth and LakshmaG's might, And gentle Sítá: how will she Spare any, whosoe'er it be?” Oppressed with sorrow, tear-distained, The royal women thus complained. Like night when not a star appears, Like a sad widow drowned in tears, Ayodhyá's city, dark and dim, Reft of her lord was sad for him. When thus for woe the king to heaven had fled, And still on earth his lovely wives remained. With dying light the sun to rest had sped, And night triumphant o'er the landscape reigned. Canto LXVII. The Praise Of Kings.
- **Translation**: 

---

### Verse 2 (Ramayana 0.627)
- **Original**: Canto LXVII. The Praise Of Kings. 609 That night of sorrow passed away, And rose again the God of Day. Then all the twice-born peers of state Together met for high debate. Jáválí, lord of mighty fame. And Gautam, and Kátyáyan came, And Márkandeya's reverend age, And Vámadeva, glorious sage: Sprung from Mudgalya's seed the one, The other ancient Ka[yap's son. With lesser lords these Bráhmans each Spoke in his turn his several speech, And turning to Va[ishmha, best Of household priests him thus addressed: “The night of bitter woe has past, Which seemed a hundred years to last, Our king, in sorrow for his son, Reunion with the Five has won. His soul is where the blessed are, While Ráma roams in woods afar, And Lakshma G, bright in glorious deeds, Goes where his well-loved brother leads. And Bharat andZatrughna, they Who smite their foes in battle fray, Far in the realm of Kekaya stay, Where their maternal grandsire's care Keeps Rájagriha's city fair. Let one of old Ikshváku's race Obtain this day the sovereign's place, Or havoc and destruction straight Our kingless land will devastate. In kingless lands no thunder's voice, No lightning wreaths the heart rejoice, Nor does Parjanya's heavenly rain
- **Translation**: 

---

### Verse 3 (Ramayana 0.628)
- **Original**: 610 The Ramayana Descend upon the burning plain. Where none is king, the sower's hand Casts not the seed upon the land; The son against the father strives. And husbands fail to rule their wives. In kingless realms no princes call Their friends to meet in crowded hall; No joyful citizens resort To garden trim or sacred court. In kingless realms no Twice-born care To sacrifice with text and prayer, Nor Bráhmans, who their vows maintain, The great solemnities ordain. The joys of happier days have ceased: No gathering, festival, or feast Together calls the merry throng Delighted with the play and song. In kingless lands it ne'er is well With sons of trade who buy and sell: No men who pleasant tales repeat Delight the crowd with stories sweet. In kingless realms we ne'er behold Young maidens decked with gems and gold, Flock to the gardens blithe and gay To spend their evening hours in play. No lover in the flying car Rides with his love to woods afar. In kingless lands no wealthy swain Who keeps the herd and reaps the grain, Lies sleeping, blest with ample store, Securely near his open door. Upon the royal roads we see No tusked elephant roaming free, Of three-score years, whose head and neck
- **Translation**: 

---

### Verse 4 (Ramayana 0.629)
- **Original**: Canto LXVII. The Praise Of Kings. 611 Sweet tinkling bells of silver deck. We hear no more the glad applause When his strong bow each rival draws, No clap of hands, no eager cries That cheer each martial exercise. In kingless realms no merchant bands Who travel forth to distant lands, With precious wares their wagons load, [175] And fear no danger on the road. No sage secure in self-control, Brooding on God with mind and soul, In lonely wanderings finds his home Where'er at eve his feet may roam. In kingless realms no man is sure He holds his life and wealth secure. In kingless lands no warriors smite The foeman's host in glorious fight. In kingless lands the wise no more, Well trained in Scripture's holy lore, In shady groves and gardens meet To argue in their calm retreat. No longer, in religious fear, Do they who pious vows revere, Bring dainty cates and wreaths of flowers As offerings to the heavenly powers. No longer, bright as trees in spring, Shine forth the children of the king Resplendent in the people's eyes With aloe wood and sandal dyes. A brook where water once has been, A grove where grass no more is green, Kine with no herdsman's guiding hand— So wretched is a kingless land. The car its waving banner rears,
- **Translation**: 

---

### Verse 5 (Ramayana 0.630)
- **Original**: 612 The Ramayana Banner of fire the smoke appears: Our king, the banner of our pride, A God with Gods is glorified. In kingless lands no law is known, And none may call his wealth his own, Each preys on each from hour to hour, As fish the weaker fish devour. Then fearless, atheists overleap The bounds of right the godly keep, And when no royal powers restrain, Preëminence and lordship gain. As in the frame of man the eye Keeps watch and ward, a careful spy, The monarch in his wide domains Protects the truth, the right maintains. He is the right, the truth is he, Their hopes in him the well-born see. On him his people's lives depend, Mother is he, and sire, and friend. The world were veiled in blinding night, And none could see or know aright, Ruled there no king in any state The good and ill to separate. We will obey thy word and will As if our king were living still: As keeps his bounds the faithful sea, So we observe thy high decree. O best of Bráhmans, first in place, Our kingless land lies desolate: Some scion of Ikshváku's race Do thou as monarch consecrate.”
- **Translation**: 

---

### Verse 6 (Ramayana 0.631)
- **Original**: Canto LXVIII. The Envoys. 613 Canto LXVIII. The Envoys. Va [ishmha heard their speech and prayer, And thus addressed the concourse there, Friends, Bráhmans, counsellors, and all Assembled in the palace hall: “Ye know that Bharat, free from care, Still lives in Rájagriha339 where The father of his mother reigns: Zatrughna by his side remains. Let active envoys, good at need, Thither on fleetest horses speed, To bring the hero youths away: Why waste the time in dull delay?” Quick came from all the glad reply: “Va [ishmha, let the envoys fly!” He heard their speech, and thus renewed His charge before the multitude: “Nandan, A[ok, Siddhárth, attend, Your ears, Jayanta, Vijay, lend: Be yours, what need requires, to do: I speak these words to all of you. With coursers of the fleetest breed To Rájagriha's city speed. Then rid your bosoms of distress, And Bharat thus from me address: “The household priest and peers by us Send health to thee and greet thee thus: Come to thy father's home with haste: Thine absent time no longer waste.” 339 Rájagriha, or Girivraja was the capital of A[vapati, Bharat's maternal grandfather.
- **Translation**: 

---

### Verse 7 (Ramayana 0.632)
- **Original**: 614 The Ramayana But speak no word of Ráma fled, Tell not the prince his sire is dead, Nor to the royal youth the fate That ruins Raghu's race relate. Go quickly hence, and with you bear Fine silken vestures rich and rare, And gems and many a precious thing As gifts to Bharat and the king.” With ample stores of food supplied, Each to his home the envoys hied, Prepared, with steeds of swiftest race, To Kekaya's land340 their way to trace. They made all due provision there, And every need arranged with care, Then ordered by Va[ishmha, they Went forth with speed upon their way. Then northward of Pralamba, west Of Apartála, on they pressed, Crossing the Máliní that flowed With gentle stream athwart the road. They traversed Gangá's holy waves[176] Where she Hástinapura341 laves, Thence to Panchála342 westward fast Through Kurujángal's land343 Note. 340 The Kekayas or Kaikayas in the Punjab appear amongst the chief nations in the war of the Mahábhárata; their king being a kinsman of KrishGa. 341 Hástinapura was the capital of the kingdom of Kuru, near the modern Delhi. 342 The Panchálas occupied the upper part of the Doab. 343 “Kurujángala and its inhabitants are frequently mentioned in the Mahábhárata, as in theÁdi-parv.3789, 4337,et al.” W ILSON 'S{FNS VishGu PuráGa,Vol. II. p. 176. DR . HALL 'S{FNS
- **Translation**: 

---

### Verse 8 (Ramayana 0.633)
- **Original**: Canto LXVIII. The Envoys. 615 they passed. On, on their course the envoys held By urgency of task impelled. Quick glancing at each lucid flood And sweet lake gay with flower and bud. Beyond, they passed unwearied o'er, Where glad birds fill the flood and shore Of ZaradaG á racing fleet With heavenly water clear and sweet, Thereby a tree celestial grows Which every boon on prayer bestows: To its blest shade they humbly bent, Then to Kulingá's town they went. Then, having passed the Warrior's Wood, In Abhikála next they stood, O'er sacred Ikshumatí344 Edition. The Ikshumatí was a river in Kurukshetra. came, Their ancient kings' ancestral claim. They saw the learned Bráhmans stand, Each drinking from his hollowed hand, And through Báhíka345 journeying still They reached at length Sudáman's hill: There VishGu's footstep turned to see, Vipá[á346 viewed, andZálmalí, And many a lake and river met, Tank, pool, and pond, and rivulet. 344 “The I¾{¼±Ä¹Â of Arrian. SeeAs. Res. Vol. XV. p. 420, 421, also Indische Alterthumskunde, Vol. I. p. 602, first footnote.” W ILSON 'S{FNS VishGu PuráGa, Vol. I. p. 421. DR . HALL 'S{FNS 345 “The Báhíkas are described in the Mahábhárata, KarGa Parvan, with some detail, and comprehend the different nations of the Punjab from the Sutlej to the Indus.” W ILSON 'S{FNS VishGu PuráGa, Vol. I. p. 167. 346 The Beas, Hyphasis, or Bibasis.
- **Translation**: 

---

### Verse 9 (Ramayana 0.634)
- **Original**: 616 The Ramayana And lions saw, and tigers near, And elephants and herds of deer, And still, by prompt obedience led, Along the ample road they sped. Then when their course so swift and long, Had worn their steeds though fleet and strong, To Girivraja's splendid town They came by night, and lighted down. To please their master, and to guard The royal race, the lineal right, The envoys, spent with riding hard, To that fair city came by night.347 347 It would be lost labour to attempt to verify all the towns and streams mentioned in Cantos LXVIII and LXXII. Professor Wilson observes (VishGu PuráGa, p. 139. Dr. Hall's Edition)“States, and tribes, and cities have disap- peared, even from recollection; and some of the natural features of the country, especially the rivers, have undergone a total alteration.… Notwithstanding these impediments, however, we should be able to identify at least mountains and rivers, to a much greater extent than is now practicable, if our maps were not so miserably defective in their nomenclature. None of our surveyors or geographers have been oriental scholars. It may be doubted if any of them have been conversant with the spoken language of the country. They have, consequently, put down names at random, according to their own inaccurate appreciation of sounds carelessly, vulgarly, and corruptly uttered; and their maps of India are crowded with appellations which bear no similitude whatever either to past or present denominations. We need not wonder that we cannot discover Sanskrit names in English maps, when, in the immediate vicinity of Calcutta, Barnagore represents Baráhanagar, Dakshine[war is metamorphosed into Duckinsore, Ulubaría into Willoughbury.… There is scarcely a name in our Indian maps that does not afford proof of extreme indifference to accuracy in nomenclature, and of an incorrectness in estimating sounds, which is, in some degree, perhaps, a national defect.” For further information regarding the road from Ayodhyá to Rájagriha, see
- **Translation**: 

---

### Verse 10 (Ramayana 0.635)
- **Original**: Canto LXIX. Bharat's Dream. 617 Canto LXIX. Bharat's Dream. The night those messengers of state Had past within the city's gate, In dreams the slumbering Bharat saw A sight that chilled his soul with awe. The dream that dire events foretold Left Bharat's heart with horror cold, [177] And with consuming woes distraught, Upon his aged sire he thought. His dear companions, swift to trace The signs of anguish on his face, Drew near, his sorrow to expel, And pleasant tales began to tell. Some woke sweet music's cheering sound, And others danced in lively round. With joke and jest they strove to raise His spirits, quoting ancient plays; But Bharat still, the lofty-souled, Deaf to sweet tales his fellows told, Unmoved by music, dance, and jest, Sat silent, by his woe oppressed. To him, begirt by comrades near, Thus spoke the friend he held most dear: “Why ringed around by friends, art thou So silent and so mournful now?” “Hear thou,” thus Bharat made reply, “What chills my heart and dims mine eye. I dreamt I saw the king my sire Sink headlong in a lake of mire Down from a mountain high in air, His body soiled, and loose his hair. Additional Notes.
- **Translation**: 

---

### Verse 11 (Ramayana 0.636)
- **Original**: 618 The Ramayana Upon the miry lake he seemed To lie and welter, as I dreamed; With hollowed hands full many a draught Of oil he took, and loudly laughed. With head cast down I saw him make A meal on sesamum and cake; The oil from every member dripped, And in its clammy flood he dipped. The ocean's bed was bare and dry, The moon had fallen from the sky, And all the world lay still and dead, With whelming darkness overspread. The earth was rent and opened wide, The leafy trees were scorched, and died; I saw the seated mountains split, And wreaths of rising smoke emit. The stately beast the monarch rode His long tusks rent and splintered showed; And flames that quenched and cold had lain Blazed forth with kindled light again. I looked, and many a handsome dame, Arrayed in brown and sable came And bore about the monarch, dressed, On iron stool, in sable vest. And then the king, of virtuous mind, A blood-red wreath around him twined, Forth on an ass-drawn chariot sped, As southward still he bent his head. Then, crimson-clad, a dame appeared Who at the monarch laughed and jeered; And a she-monster, dire to view, Her hand upon his body threw. Such is the dream I dreamt by night, Which chills me yet with wild affright:
- **Translation**: 

---

### Verse 12 (Ramayana 0.637)
- **Original**: Canto LXX. Bharat's Departure. 619 Either the king or Ráma, I Or LakshmaG now must surely die. For when an ass-drawn chariot seems To bear away a man in dreams, Be sure above his funeral pyre The smoke soon rears its cloudy spire. This makes my spirit low and weak, My tongue is slow and loth to speak: My lips and throat are dry for dread, And all my soul disquieted. My lips, relaxed, can hardly speak, And chilling dread has changed my cheek I blame myself in aimless fears, And still no cause of blame appears. I dwell upon this dream of ill Whose changing scenes I viewed, And on the startling horror still My troubled thoughts will brood. Still to my soul these terrors cling, Reluctant to depart, And the strange vision of the king Still weighs upon my heart.” Canto LXX. Bharat's Departure. While thus he spoke, the envoys borne On horses faint and travel-worn Had gained the city fenced around With a deep moat's protecting bound. An audience of the king they gained, And honours from the prince obtained;
- **Translation**: 

---

### Verse 13 (Ramayana 0.638)
- **Original**: 620 The Ramayana The monarch's feet they humbly pressed, To Bharat next these words addressed: “The household priest and peers by us Send health to thee and greet thee thus: “Come to thy father's house with haste: Thine absent time no longer waste.” Receive these vestures rich and rare, These costly gems and jewels fair, And to thy uncle here present Each precious robe and ornament. These for the king and him suffice— Two hundred millions is their price— These, worth a hundred millions, be Reserved, O large-eyed Prince, for thee.” Loving his friends with heart and soul, The joyful prince received the whole, Due honour to the envoys paid, And thus in turn his answer made: “Of Da[aratha tidings tell: Is the old king my father well? Is Ráma, and is LakshmaG, he Of the high-soul, from sickness free? And she who walks where duty leads, Kau [alyá, known for gracious deeds, Mother of Ráma, loving spouse, Bound to her lord by well kept vows? And Lakshma G's mother too, the dame Sumitrá skilled in duty's claim, Who brave Zatrughna also bare, Second in age,— her health declare.[178] And she, in self-conceit most sage, With selfish heart most prone to rage, My mother, fares she well? has she
- **Translation**: 

---

### Verse 14 (Ramayana 0.639)
- **Original**: Canto LXX. Bharat's Departure. 621 Sent message or command to me?” Thus Bharat spake, the mighty-souled, And they in brief their tidings told: “All they of whom thou askest dwell, O lion lord, secure and well: Thine all the smiles of fortune are: Make ready; let them yoke the car.” Thus by the royal envoys pressed, Bharat again the band addressed: “I go with you: no long delay, A single hour I bid you stay.” Thus Bharat, son of him who swayed Ayodhyás realm, his answer made, And then bespoke, his heart to please, His mother's sire in words like these: “I go to see my father, King, Urged by the envoys' summoning; And when thy soul desires to see Thy grandson, will return to thee.” The king his grandsire kissed his head, And in reply to Bharat said: “Go forth, dear child: how blest is she, The mother of a son like thee! Greet well thy sire, thy mother greet, O thou whose arms the foe defeat; The household priest, and all the rest Amid the Twice-born chief and best; And Ráma and brave LakshmaG, who Shoot the long shaft with aim so true.”
- **Translation**: 

---

### Verse 15 (Ramayana 0.640)
- **Original**: 622 The Ramayana To him the king high honour showed, And store of wealth and gifts bestowed, The choicest elephants to ride, And skins and blankets deftly dyed, A thousand strings of golden beads, And sixteen hundred mettled steeds: And boundless wealth before him piled Gave Kekaya to Kaikeyí's child. And men of counsel, good and tried, On whose firm truth he aye relied, King A[vapati gave with speed Prince Bharat on his way to lead. And noble elephants, strong and young, From sires of Indra[ira sprung, And others tall and fair to view Of great Airávat's lineage true: And well yoked asses fleet of limb The prince his uncle gave to him. And dogs within the palace bred, Of body vast and massive head, With mighty fangs for battle, brave, The tiger's match in strength, he gave. Yet Bharat's bosom hardly glowed To see the wealth the king bestowed; For he would speed that hour away, Such care upon his bosom lay: Those eager envoys urged him thence, And that sad vision's influence. He left his court-yard, crowded then With elephants and steeds and men, And, peerless in immortal fame, To the great royal street he came. He saw, as farther still he went, The inner rooms most excellent,
- **Translation**: 

---

### Verse 16 (Ramayana 0.641)
- **Original**: Canto LXXI. Bharat's Return. 623 And passed the doors, to him unclosed, Where check nor bar his way oppossd. There Bharat stayed to bid adieu To grandsire and to uncle too, Then, withZatrughna by his side, Mounting his car, away he hied. The strong-wheeled cars were yoked, and they More than a hundred, rolled away: Servants, with horses, asses, kine, Followed their lord in endless line. So, guarded by his own right hand, Forth high-souled Bharat hied, Surrounded by a lordly band On whom the king relied. Beside him satZatrughna dear, The scourge of trembling foes: Thus from the light of Indra's sphere A saint made perfect goes. Canto LXXI. Bharat's Return. Then Bharat's face was eastward bent As from the royal town he went. He reached Sudámá's farther side, And glorious, gazed upon the tide; Passed Hládiní, and saw her toss Her westering billows hard to cross. Then old Ikshváku's famous son O'erZatadrú348 his passage won, 348 “The Zatadrú,‘the hundred-channeled’— the Zaradrus of Ptolemy, Hesydrus of Pliny— is the Sutlej.” W ILSON 'S{FNS VishGu PuráGa, Vol. II. p. 130.
- **Translation**: 

---

### Verse 17 (Ramayana 0.642)
- **Original**: 624 The Ramayana Near Ailadhána on the strand, And came to Aparparyat's land. O'erZilá's flood he hurried fast, Akurvatí's fair stream he passed, Crossed o'er Ágneya's rapid rill, And Zalyakartan onward still. Zilávahá's swift stream he eyed, True to his vows and purified, Then crossed the lofty hills, and stood In Chaitraratha's mighty wood. He reached the confluence where meet Sarasvatí349 and Gangá fleet, And through BháruG a forest, spread Northward of Viramatsya, sped. He sought Kálinda's child, who fills[179] The soul with joy, begirt by hills, Reached Yamuná, and passing o'er, Rested his army on the shore: He gave his horses food and rest, Bathed reeking limb and drooping crest. They drank their fill and bathed them there, And water for their journey bare. Thence through a mighty wood he sped All wild and uninhabited, As in fair chariot through the skies, Most fair in shape a Storm-God flies. At An[udhána Gangá, hard To cross, his onward journey barred, So turning quickly thence he came To Prágvam's city dear to fame. There having gained the farther side To Kumikoshmiká he hied: 349 The Sarasvatí or Sursooty is a tributary of the Caggar or Guggur in Sirhind.
- **Translation**: 

---

### Verse 18 (Ramayana 0.643)
- **Original**: Canto LXXI. Bharat's Return. 625 The stream he crossed, and onward then To Dharmavardhan brought his men. Thence, leaving ToraG on the north, To Jambuprastha journeyed forth. Then onward to a pleasant grove By fair Varútha's town he drove, And when a while he there had stayed, Went eastward from the friendly shade. Eastward of Ujjiháná where The Priyak trees are tall and fair, He passed, and rested there each steed Exhausted with the journey's speed. There orders to his men addressed, With quickened pace he onward pressed, A while at Sarvatírtha spent, Then o'er Uttániká he went. O'er many a stream beside he sped With coursers on the mountains bred, And passing Hastiprishmhak, took The road o'er Kumiká's fair brook. Then, at Lohitya's village, he Crossed o'er the swift Kapívatí, Then passed, where Eka[ála stands, The StháGumatí's flood and sands, And Gomatí of fair renown By Vinata's delightful town. When to Kalinga near he drew, A wood of Sal trees charmed the view; That passed, the sun began to rise, And Bharat saw with happy eyes, Ayodhyá's city, built and planned By ancient Manu's royal hand. Seven nights upon the road had passed, And when he saw the town at last
- **Translation**: 

---

### Verse 19 (Ramayana 0.644)
- **Original**: 626 The Ramayana Before him in her beauty spread, Thus Bharat to the driver said: “This glorious city from afar, Wherein pure groves and gardens are, Seems to my eager eyes to-day A lifeless pile of yellow clay. Through all her streets where erst a throng Of men and women streamed along, Uprose the multitudinous roar: To-day I hear that sound no more. No longer do mine eyes behold The leading people, as of old, On elephants, cars, horses, go Abroad and homeward, to and fro. The brilliant gardens, where we heard The wild note of each rapturous bird, Where men and women loved to meet, In pleasant shades, for pastime sweet,— These to my eyes this day appear Joyless, and desolate, and drear: Each tree that graced the garden grieves, And every path is spread with leaves. The merry cry of bird and beast, That spake aloud their joy, has ceased: Still is the long melodious note That charmed us from each warbling throat. Why blows the blessed air no more, The incense-breathing air that bore Its sweet incomparable scent Of sandal and of aloe blent? Why are the drum and tabour mute? Why is the music of the lute That woke responsive to the quill, Loved by the happy, hushed and still?
- **Translation**: 

---

### Verse 20 (Ramayana 0.645)
- **Original**: Canto LXXI. Bharat's Return. 627 My boding spirit gathers hence Dire sins of awful consequence, And omens, crowding on my sight, Weigh down my soul with wild affright. Scarce shall I find my friends who dwell Here in Ayodhyá safe and well: For surely not without a cause This crushing dread my soul o'erawes.” Heart sick, dejected, every sense Confused by terror's influence, On to the town he quickly swept Which King Ikshváku's children kept. He passed through Vaijayanta's gate, With weary steeds, disconsolate, And all who near their station held, His escort, crying Victory, swelled, With heart distracted still he bowed Farewell to all the following crowd, Turned to the driver and began To question thus the weary man: “Why was I brought, O free from blame, So fast, unknown for what I came? Yet fear of ill my heart appals, And all my wonted courage falls. For I have heard in days gone by The changes seen when monarchs die; And all those signs, O charioteer, I see to-day surround me here: Each kinsman's house looks dark and grim, No hand delights to keep it trim: The beauty vanished, and the pride, The doors, unkept, stand open wide. No morning rites are offered there,
- **Translation**: 

---



--- End of Ramayan_batch_130.md ---


--- Start of Ramayan_batch_131.md ---

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

### Verse 1 (Ramayana 0.646)
- **Original**: 628 The Ramayana No grateful incense loads the air, And all therein, with brows o'ercast, Sit joyless on the ground and fast. Their lovely chaplets dry and dead,[180] Their courts unswept, with dust o'erspread, The temples of the Gods to-day No more look beautiful and gay. Neglected stands each holy shrine, Each image of a Lord divine. No shop where flowery wreaths are sold Is bright and busy as of old. The women and the men I mark Absorbed in fancies dull and dark, Their gloomy eyes with tears bedewed, A poor afflicted multitude.” His mind oppressed with woe and dread, Thus Bharat to his driver said, Viewed the dire signs Ayodhyá showed, And onward to the palace rode. Canto LXXII. Bharat's Inquiry. He entered in, he looked around, Nor in the house his father found; Then to his mother's dwelling, bent To see her face, he quickly went. She saw her son, so long away, Returning after many a day, And from her golden seat in joy Sprung forward to her darling boy.
- **Translation**: 

---

### Verse 2 (Ramayana 0.647)
- **Original**: Canto LXXII. Bharat's Inquiry. 629 Within the bower, no longer bright, Came Bharat lover of the right, And bending with observance sweet Clasped his dear mother's lovely feet. Long kisses on his brow she pressed, And held her hero to her breast, Then fondly drew him to her knees, And questioned him in words like these: “How many nights have fled, since thou Leftest thy grandsire's home, till now? By flying steeds so swiftly borne, Art thou not weak and travel-worn? How fares the king my father, tell: Is Yudhájit thine uncle well? And now, my son, at length declare The pleasure of the visit there.” Thus to the offspring of the king She spake with tender questioning, And to his mother made reply Young Bharat of the lotus eye: “The seventh night has come and fled Since from my grandsire's home I sped: My mother's sire is well, and he, Yudhájit, from all trouble free. The gold and every precious thing Presented by the conqueror king, The slower guards behind convey: I left them weary on the way. Urged by the men my father sent, My hasty course I hither bent: Now, I implore, an answer deign, And all I wish to know, explain. Unoccupied I now behold
- **Translation**: 

---

### Verse 3 (Ramayana 0.648)
- **Original**: 630 The Ramayana This couch of thine adorned with gold, And each of King Ikshváku's race Appears with dark and gloomy face. The king is aye, my mother dear, Most constant in his visits here. To meet my sire I sought this spot: How is it that I find him not? I long to clasp my father's feet: Say where he lingers, I entreat. Perchance the monarch may be seen Where dwells Kau[alyá, eldest queen.” His father's fate, from him concealed, Kaikeyí to her son revealed: Told as glad news the story sad, For lust of sway had made her mad: “Thy father, O my darling, know, Has gone the way all life must go: Devout and famed, of lofty thought, In whom the good their refuge sought.” When Bharat pious, pure, and true, Heard the sad words which pierced him through, Grieved for the sire he loved so well Prostrate upon the ground he fell: Down fell the strong-armed hero, high Tossing his arms, and a sad cry, “Ah, woe is me, unhappy, slain!” Burst from his lips again, again, Afflicted for his father's fate By grief's intolerable weight, With every sense amazed and cowed The splendid hero wailed aloud: “Ah me, my royal father's bed
- **Translation**: 

---

### Verse 4 (Ramayana 0.649)
- **Original**: Canto LXXII. Bharat's Inquiry. 631 Of old a gentle radiance shed, Like the pure sky when clouds are past, And the moon's light is o'er it cast: Ah, of its wisest lord bereft, It shows to-day faint radiance left, As when the moon has left the sky. Or mighty Ocean's depths are dry.” With choking sobs, with many a tear, Pierced to the heart with grief sincere, The best of conquerors poured his sighs, And with his robe veiled face and eyes. Kaikeyí saw him fallen there, Godlike, afflicted, in despair, Used every art to move him thence, And tried him thus with eloquence: “Arise, arise, my dearest; why Wilt thou, famed Prince, so lowly lie? Not by such grief as this are moved Good men like thee, by all approved. The earth thy father nobly swayed, And rites to Heaven he duly paid. At length his race of life was run: Thou shouldst not mourn for him, my son.” Long on the ground he wept, and rolled From side to side, still unconsoled, And then, with bitter grief oppressed, His mother with these words addressed: [181]
- **Translation**: 

---

### Verse 5 (Ramayana 0.650)
- **Original**: 632 The Ramayana “This joyful hope my bosom fed When from my grandsire's halls I sped— “The king will throne his eldest son, And sacrifice, as should be done.” But all is changed, my hope was vain, And this sad heart is rent in twain, For my dear father's face I miss, Who ever sought his loved ones' bliss. But in my absence, mother, say, What sickness took my sire away? Ah, happy Ráma, happy they Allowed his funeral rites to pay! The glorious monarch has not learned That I his darling have returned, Or quickly had he hither sped, And pressed his kisses on my head. Where is that hand whose gentle touch, Most soft and kind I loved so much, The hand that loved to brush away The dust that on his darling lay? Quick, bear the news to Ráma's ear; Tell the great chief that I am here: Brother, and sire, and friend, and all Is he, and I his trusty thrall. For noble hearts, to virtue true, Their sires in elder brothers view. To clasp his feet I fain would bow: He is my hope and refuge now. What said my glorious sire, who knew Virtue and vice, so brave and true? Firm in his vows, dear lady, say, What said he ere he passed away? What was his rede to me? I crave To hear the last advice he gave.”
- **Translation**: 

---

### Verse 6 (Ramayana 0.651)
- **Original**: Canto LXXII. Bharat's Inquiry. 633 Thus closely questioned by the youth, Kaikeyí spoke the mournful truth: “The high-souled monarch wept and sighed, For Ráma, Sítá, LakshmaG, cried, Then, best of all who go to bliss, Passed to the world which follows this. “Ah, blessed are the people who Shall Ráma and his Sítá view, And Lakshma G of the mighty arm, Returning free from scathe and harm.” Such were the words, the last of all, Thy father, ere he died, let fall, By Fate and Death's dread coils enwound, As some great elephant is bound.” He heard, yet deeper in despair, Her lips this double woe declare, And with sad brow that showed his pain Questioned his mother thus again: “But where is he, of virtue tried, Who fills Kau[alyá's heart with pride, Where is the noble Ráma? where Is LakshmaG brave, and Sítá fair?” Thus pressed, the queen began to tell The story as each thing befell, And gave her son in words like these, The mournful news she meant to please: “The prince is gone in hermit dress To DaG ak's mighty wilderness, And Lakshma G brave and Sítá share The wanderings of the exile there.”
- **Translation**: 

---

### Verse 7 (Ramayana 0.652)
- **Original**: 634 The Ramayana Then Bharat's soul with fear was stirred Lest Ráma from the right had erred, And jealous for ancestral fame, He put this question to the dame: “Has Ráma grasped with lawless hold A Bráhman's house, or land, or gold? Has Ráma harmed with ill intent Some poor or wealthy innocent? Was Ráma, faithless to his vows, Enamoured of anothers spouse? Why was he sent to DaG ak's wild, Like one who kills an unborn child?” He questioned thus: and she began To tell her deeds and crafty plan. Deceitful-hearted, fond, and blind As is the way of womankind: “No Bráhman's wealth has Ráma seized, No dame his wandering fancy pleased; His very eyes he ne'er allows To gaze upon a neighbour's spouse. But when I heard the monarch planned To give the realm to Ráma's hand, I prayed that Ráma hence might flee, And claimed the throne, my son, for thee. The king maintained the name he bare, And did according to my prayer, And Ráma, with his brother, sent, And Sítá, forth to banishment. When his dear son was seen no more, The lord of earth was troubled sore: Too feeble with his grief to strive, He joined the elemental Five. Up then, most dutiful! maintain
- **Translation**: 

---

### Verse 8 (Ramayana 0.653)
- **Original**: Canto LXXIII. Kaikeyí Reproached. 635 The royal state, arise, and reign. For thee, my darling son, for thee All this was planned and wrought by me. Come, cast thy grief and pain aside, With manly courage fortified. This town and realm are all thine own, And fear and grief are here unknown. Come, with Va[ishmha's guiding aid, And priests in ritual skilled Let the king's funeral dues be paid, And every claim fulfilled. Perform his obsequies with all That suits his rank and worth, Then give the mandate to install Thyself as lord of earth.” Canto LXXIII. Kaikeyí Reproached. But when he heard the queen relate His brothers' doom, his father's fate, Thus Bharat to his mother said With burning grief disquieted: [182] “Alas, what boots it now to reign, Struck down by grief and well-nigh slain? Ah, both are gone, my sire, and he Who was a second sire to me. Grief upon grief thy hand has made, And salt upon gashes laid: For my dear sire has died through thee, And Ráma roams a devotee. Thou camest like the night of Fate
- **Translation**: 

---

### Verse 9 (Ramayana 0.654)
- **Original**: 636 The Ramayana This royal house to devastate. Unwitting ill, my hapless sire Placed in his bosom coals of fire, And through thy crimes his death he met, O thou whose heart on sin is set. Shame of thy house! thy senseless deed Has reft all joy from Raghu's seed. The truthful monarch, dear to fame, Received thee as his wedded dame, And by thy act to misery doomed Has died by flames of grief consumed. Kau [alyá and Sumitrá too The coming of my mother rue, And if they live oppressed by woe, For their dear sons their sad tears flow. Was he not ever good and kind,— That hero of the duteous mind? Skilled in all filial duties, he As a dear mother treated thee. Kau [alyá too, the eldest queen, Who far foresees with insight keen, Did she not ever show thee all A sister's love at duty's call? And hast thou from the kingdom chased Her son, with bark around his waist, To the wild wood, to dwell therein, And dost not sorrow for thy sin? The love I bare to Raghu's son Thou knewest not, ambitious one, If thou hast wrought this impious deed For royal sway, in lawless greed. With him and LakshmaG far away, What power have I the realm to sway? What hope will fire my bosom when
- **Translation**: 

---

### Verse 10 (Ramayana 0.655)
- **Original**: Canto LXXIII. Kaikeyí Reproached. 637 I see no more these lords of men? The holy king, who loved the right Relied on Ráma's power and might, His guardian and his glory, so Joys Meru in his woods below. How can I bear, a steer untrained, The load his mightier strength sustained? What power have I to brook alone This weight on feeble shoulders thrown? But if the needful power were bought By strength of mind and brooding thought, No triumph shall attend the dame Who dooms her son to lasting shame. Now should no doubt that son prevent From quitting thee on evil bent. But Ráma's love o'erpowers my will, Who holds thee as his mother still. Whence did the thought, O thou whose eyes Are turned to sinful deeds, arise— A plan our ancient sires would hate, O fallen from thy virtuous state? For in the line from which we spring The eldest is anointed king: No monarchs from the rule decline, And, least of all, Ikshváku's line. Our holy sires, to virtue true, Upon our race a lustre threw, But with subversive frenzy thou Hast marred our lineal honour now, Of lofty birth, a noble line Of previous kings is also thine: Then whence this hated folly? whence This sudden change that steals thy sense? Thou shalt not gain thine impious will,
- **Translation**: 

---

### Verse 11 (Ramayana 0.656)
- **Original**: 638 The Ramayana O thou whose thoughts are bent on ill, Thou from whose guilty hand descend These sinful blows my life to end. Now to the forest will I go, Thy cherished plans to overthrow, And bring my brother, free from stain, His people's darling, home again. And Ráma, when again he turns, Whose glory like a beacon burns, In me a faithful slave shall find To serve him with contented mind.” Canto LXXIV. Bharat's Lament. When Bharat's anger-sharpened tongue Reproaches on the queen had flung, Again, with mighty rage possessed, The guilty dame he thus addressed: “Flee, cruel, wicked sinner, flee, Let not this kingdom harbour thee. Thou who hast thrown all right aside, Weep thou for me when I have died. Canst thou one charge against the king, Or the most duteous Ráma bring? The one thy sin to death has sent, The other chased to banishment. Our line's destroyer, sin defiled Like one who kills an unborn child, Ne'er with thy lord in heaven to dwell, Thy portion shall be down in hell Because thy hand, that stayed for naught,
- **Translation**: 

---

### Verse 12 (Ramayana 0.657)
- **Original**: Canto LXXIV. Bharat's Lament. 639 This awful wickedness has wrought, And ruined him whom all held dear, My bosom too is stirred with fear. My father by thy sin is dead, And Ráma to the wood is fled; And of thy deed I bear the stain, And fameless in the world remain. Ambitious, evil-souled, in show My mother, yet my direst foe. My throning ne'er thine eyes shall bless, Thy husband's wicked murderess. [183] Thou art not A[vapati's child, That righteous king most sage and mild, But thou wast born a fiend, a foe My father's house to overthrow. Thou who hast made Kau[alyá, pure, Gentle, affectionate, endure The loss of him who was her bliss,— What worlds await thee, Queen, for this? Was it not patent to thy sense That Ráma was his friends' defence, Kau [alyá's own true child most dear, The eldest and his father's peer? Men in the son not only trace The father's figure, form, and face, But in his heart they also find The offspring of the father's mind; And hence, though dear their kinsmen are, To mothers sons are dearer far. There goes an ancient legend how Good Surabhí, the God-loved cow, Saw two of her dear children strain, Drawing a plough and faint with pain. She saw them on the earth outworn,
- **Translation**: 

---

### Verse 13 (Ramayana 0.658)
- **Original**: 640 The Ramayana Toiling till noon from early morn, And as she viewed her children's woe, A flood of tears began to flow. As through the air beneath her swept The Lord of Gods, the drops she wept, Fine, laden with delicious smell, Upon his heavenly body fell. And Indra lifted up his eyes And saw her standing in the skies, Afflicted with her sorrow's weight, Sad, weeping, all disconsolate. The Lord of Gods in anxious mood Thus spoke in suppliant attitude: “No fear disturbs our rest, and how Come this great dread upon thee now? Whence can this woe upon thee fall, Say, gentle one who lovest all?” Thus spake the God who rules the skies, Indra, the Lord supremely wise; And gentle Surabhí, well learned In eloquence, this speech returned: “Not thine the fault, great God, not thine And guiltless are the Lords divine: I mourn two children faint with toil, Labouring hard in stubborn soil. Wasted and sad I see them now, While the sun beats on neck and brow, Still goaded by the cruel hind,— No pity in his savage mind. O Indra, from this body sprang These children, worn with many a pang. For this sad sight I mourn, for none Is to the mother like her son.”
- **Translation**: 

---

### Verse 14 (Ramayana 0.659)
- **Original**: Canto LXXIV. Bharat's Lament. 641 He saw her weep whose offspring feed In thousands over hill and mead, And knew that in a mother's eye Naught with a son, for love, can vie. He deemed her, when the tears that came From her sad eyes bedewed his frame, Laden with their celestial scent, Of living things most excellent. If she these tears of sorrow shed Who many a thousand children bred, Think what a life of woe is left Kau [alyá, of her Ráma reft. An only son was hers and she Is rendered childless now by thee. Here and hereafter, for thy crime, Woe is thy lot through endless time. And now, O Queen, without delay, With all due honour will I pay Both to my brother and my sire The rites their several fates require. Back to Ayodhyá will I bring The long-armed chief, her lord and king, And to the wood myself betake Where hermit saints their dwelling make. For, sinner both in deed and thought! This hideous crime which thou hast wrought I cannot bear, or live to see The people's sad eyes bent on me. Begone, to DaG ak wood retire, Or cast thy body to the fire, Or bind around thy neck the rope: No other refuge mayst thou hope. When Ráma, lord of valour true, Has gained the earth, his right and due,
- **Translation**: 

---

### Verse 15 (Ramayana 0.660)
- **Original**: 642 The Ramayana Then, free from duty's binding debt, My vanished sin shall I forget.” Thus like an elephant forced to brook The goading of the driver's hook, Quick panting like a serpent maimed, He fell to earth with rage inflamed. Canto LXXV. The Abjuration. A while he lay: he rose at length, And slowly gathering sense and strength, With angry eyes which tears bedewed, The miserable queen he viewed, And spake with keen reproach to her Before each lord and minister: “No lust have I for kingly sway, My mother I no more obey: Naught of this consecration knew Which Da[aratha kept in view. I withZatrughna all the time Was dwelling in a distant clime: I knew of Ráma's exile naught, That hero of the noble thought: I knew not how fair Sítá went, And Lakshma G, forth to banishment.”
- **Translation**: 

---

### Verse 16 (Ramayana 0.661)
- **Original**: Canto LXXV. The Abjuration. 643 Thus high-souled Bharat, mid the crowd, Lifted his voice and cried aloud.[184] Kau [alyá heard, she raised her head, And quickly to Sumitrá said: “Bharat, Kaikeyí's son is here,— Hers whose fell deeds I loathe and fear: That youth of foresight keen I fain Would meet and see his face again.” Thus to Sumitrá spake the dame, And straight to Bharat's presence came With altered mien, neglected dress, Trembling and faint with sore distress. Bharat,Zatrughna by his side, To meet her, toward her palace hied. And when the royal dame they viewed Distressed with dire solicitude, Sad, fallen senseless on the ground, About her neck their arms they wound. The noble matron prostrate there, Embraced, with tears, the weeping pair, And with her load of grief oppressed, To Bharat then these words addressed: “Now all is thine, without a foe, This realm for which thou longest so. Ah, soon Kaikeyí's ruthless hand Has won the empire of the land, And made my guiltless Ráma flee Dressed like some lonely devotee. Herein what profit has the queen, Whose eye delights in havoc, seen? Me also, me 'twere surely good To banish to the distant wood, To dwell amid the shades that hold My famous son with limbs like gold.
- **Translation**: 

---

### Verse 17 (Ramayana 0.662)
- **Original**: 644 The Ramayana Nay, with the sacred fire to guide, Will I, Sumitrá by my side, Myself to the drear wood repair And seek the son of Raghu there. This land which rice and golden corn And wealth of every kind adorn, Car, elephant, and steed, and gem,— She makes thee lord of it and them.” With taunts like these her bitter tongue The heart of blameless Bharat wrung And direr pangs his bosom tore Than when the lancet probes a sore. With troubled senses all astray Prone at her feet he fell and lay. With loud lament a while he plained, And slowly strength and sense regained. With suppliant hand to hand applied He turned to her who wept and sighed, And thus bespake the queen, whose breast With sundry woes was sore distressed: “Why these reproaches, noble dame? I, knowing naught, am free from blame. Thou knowest well what love was mine For Ráma, chief of Raghu's line. O, never be his darkened mind To Scripture's guiding lore inclined, By whose consent the prince who led The good, the truthful hero, fled. May he obey the vilest lord, Offend the sun with act abhorred,350 And strike a sleeping cow, who lent 350 Súryamcha pratimehatu, adversus solem mingat. An offence expressly forbidden by the Laws of Manu.
- **Translation**: 

---

### Verse 18 (Ramayana 0.663)
- **Original**: Canto LXXV. The Abjuration. 645 His voice to Ráma's banishment. May the good king who all befriends, And, like his sons, the people tends, Be wronged by him who gave consent To noble Ráma's banishment. On him that king's injustice fall, Who takes, as lord, a sixth of all, Nor guards, neglectful of his trust, His people, as a ruler must. The crime of those who swear to fee, At holy rites, some devotee, And then the promised gift deny, Be his who willed the prince should fly. When weapons clash and heroes bleed, With elephant and harnessed steed, Ne'er, like the good, be his to fight Whose heart allowed the prince's flight. Though taught with care by one expert May he the Veda's text pervert, With impious mind on evil bent, Whose voice approved the banishment. May he with traitor lips reveal Whate'er he promised to conceal, And bruit abroad his friend's offence, Betrayed by generous confidence. No wife of equal lineage born The wretch's joyless home adorn: Ne'er may he do one virtuous deed, And dying see no child succeed. When in the battle's awful day Fierce warriors stand in dread array, Let the base coward turn and fly, And smitten by the foeman, die. Long may he wander, rags his wear,
- **Translation**: 

---

### Verse 19 (Ramayana 0.664)
- **Original**: 646 The Ramayana Doomed in his hand a skull to bear, And like an idiot beg his bread, Who gave consent when Ráma fled. His sin who holy rites forgets, Asleep when shows the sun and sets, A load upon his soul shall lie Whose will allowed the prince to fly. His sin who loves his Master's dame, His, kindler of destructive flame, His who betrays his trusting friend Shall, mingled all, on him descend. By him no reverence due be paid To blessed God or parted shade: May sire and mother's sacred name In vain from him obedience claim. Ne'er may he go where dwell the good, Nor win their fame and neighbourhood, But lose all hopes of bliss to-day, Who willed the prince should flee away. May he deceive the poor and weak Who look to him and comfort seek,[185] Betray the suppliants who complain, And make the hopeful hope in vain. Long may his wife his kiss expect, And pine away in cold neglect. May he his lawful love despise, And turn on other dames his eyes, Fool, on forbidden joys intent, Whose will allowed the banishment. His sin who deadly poison throws To spoil the water as it flows, Lay on the wretch its burden dread Who gave consent when Ráma fled.”351 351 Bharat does not intend these curses for any particular person: he merely
- **Translation**: 

---

### Verse 20 (Ramayana 0.665)
- **Original**: Canto LXXV. The Abjuration. 647 Thus with his words he undeceived Kau [alyá's troubled heart, who grieved For son and husband reft away; Then prostrate on the ground he lay. Him as he lay half-senseless there, Freed by the mighty oaths he sware, Kau [alyá, by her woe distressed, With melancholy words addressed: “Anew, my son, this sorrow springs To rend my heart with keener stings: These awful oaths which thou hast sworn My breast with double grief have torn. Thy soul, and faithful LakshmaG's too, Are still, thank Heaven! to virtue true. True to thy promise, thou shalt gain The mansions which the good obtain.” Then to her breast that youth she drew, Whose sweet fraternal love she knew, And there in strict embraces held The hero, as her tears outwelled. And Bharat's heart grew sick and faint With grief and oft-renewed complaint, And all his senses were distraught By the great woe that in him wrought. Thus he lay and still bewailed With sighs and loud lament Till all his strength and reason failed, The hours of night were spent. wishes to prove his own innocence by invoking them on his own head if he had any share in banishing Ráma.
- **Translation**: 

---



--- End of Ramayan_batch_131.md ---


--- Start of Ramayan_batch_132.md ---

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

### Verse 1 (Ramayana 0.666)
- **Original**: 648 The Ramayana Canto LXXVI. The Funeral. The saint Va[ishmha, best of all Whose words with moving wisdom fall, Bharat, Kaikeyí's son, addressed, Whom burning fires of grief distressed: “O Prince, whose fame is widely spread, Enough of grief: be comforted. The time is come: arise, and lay Upon the pyre the monarch's clay.” He heard the words Va[ishmha spoke, And slumbering resolution woke. Then skilled in all the laws declare, He bade his friends the rites prepare. They raised the body from the oil, And placed it, dripping, on the soil; Then laid it on a bed, whereon Wrought gold and precious jewels shone. There, pallor o'er his features spread, The monarch, as in sleep, lay dead. Then Bharat sought his father's side, And lifted up his voice and cried: “O King, and has thy heart designed To part and leave thy son behind? Make Ráma flee, who loves the right, And Lakshma G of the arm of might? Whither, great Monarch, wilt thou go And leave this people in their woe, Mourning their hero, wild with grief, Of Ráma reft, their lion chief? Ah, who will guard the people well Who in Ayodhyá's city dwell, When thou, my sire, hast sought the sky,
- **Translation**: 

---

### Verse 2 (Ramayana 0.667)
- **Original**: Canto LXXVI. The Funeral. 649 And Ráma has been forced to fly? In widowed woe, bereft of thee, The land no more is fair to see: The city, to my aching sight, Is gloomy as a moonless night.” Thus, with o'erwhelming sorrow pained, Sad Bharat by the bed complained: And thus Va[ishmha, holy sage, Spoke his deep anguish to assuage: “O Lord of men, no longer stay; The last remaining duties pay: Haste, mighty-armed, as I advise, The funeral rites to solemnize.” And Bharat heard Va[ishmha's rede With due attention and agreed. He summoned straight from every side Chaplain, and priest, and holy guide. The sacred fires he bade them bring Forth from the chapel of the king, Wherein the priests in order due, And ministers, the offerings threw. Distraught in mind, with sob and tear, They laid the body on a bier, And servants, while their eyes brimmed o'er The monarch from the palace bore. Another band of mourners led The long procession of the dead: Rich garments in the way they cast, And gold and silver, as they passed. Then other hands the corse bedewed With fragrant juices that exude From sandal, cedar, aloe, pine,
- **Translation**: 

---

### Verse 3 (Ramayana 0.668)
- **Original**: 650 The Ramayana And every perfume rare and fine. Then priestly hands the mighty dead Upon the pyre deposited. The sacred fires they tended next, And muttered low each funeral text; And priestly singers who rehearse[186] The Zaman 352 sang their holy verse. Forth from the town in litters came, Or chariots, many a royal dame, And honoured so the funeral ground, With aged followers ringed around. With steps in inverse order bent,353 The priests in sad procession went Around the monarch's burning pyre Who well had nursed each sacred fire: With Queen Kau[alyá and the rest, Their tender hearts with woe distressed. The voice of women, shrill and clear As screaming curlews, smote the ear, As from a thousand voices rose The shriek that tells of woman's woes. Then weeping, faint, with loud lament, Down Sarjú's shelving bank they went. There standing on the river side With Bharat, priest, and peer, Their lips the women purified With water fresh and clear. Returning to the royal town, Their eyes with tear-drops filled, Ten days on earth they laid them down, And wept till grief was stilled. 352 The Sáma-veda, the hymns of which are chanted aloud. 353 Walking from right to left.
- **Translation**: 

---

### Verse 4 (Ramayana 0.669)
- **Original**: Canto LXXVII. The Gathering Of The Ashes. 651 Canto LXXVII. The Gathering Of The Ashes. The tenth day passed: the prince again Was free from every legal stain. He bade them on the twelfth the great Remaining honour celebrate. Much gold he gave, and gems, and food, To all the Bráhman multitude, And goats whose hair was white and fine, And many a thousand head of kine: Slaves, men and damsels, he bestowed, And many a car and fair abode: Such gifts he gave the Bráhman race His father's obsequies to grace. Then when the morning's earliest ray Appeared upon the thirteenth day, Again the hero wept and sighed Distraught and sorrow-stupefied; Drew, sobbing in his anguish, near, The last remaining debt to clear, And at the bottom of the pyre, He thus bespake his royal sire: “O father, hast thou left me so, Deserted in my friendless woe, When he to whom the charge was given To keep me, to the wood is driven? Her only son is forced away Who was his helpless mother's stay: Ah, whither, father, art thou fled; Leaving the queen uncomforted?”
- **Translation**: 

---

### Verse 5 (Ramayana 0.670)
- **Original**: 652 The Ramayana He looked upon the pile where lay The bones half-burnt and ashes grey, And uttering a piteous moan, Gave way, by anguish overthrown. Then as his tears began to well, Prostrate to earth the hero fell; So from its seat the staff they drag, And cast to earth some glorious flag. The ministers approached again The prince whom rites had freed from stain; So when Yayáti fell, each seer, In pity for his fate, drew near. Zatrughna saw him lying low O'erwhelmed beneath the crush of woe, And as upon the king he thought, He fell upon the earth distraught. When to his loving memory came Those noble gifts, that kingly frame, He sorrowed, by his woe distressed, As one by frenzied rage possessed: “Ah me, this surging sea of woe Has drowned us with its overflow: The source is Manthará, dire and dark, Kaikeyí is the ravening shark: And the great boons the monarch gave Lend conquering might to every wave. Ah, whither wilt thou go, and leave Thy Bharat in his woe to grieve, Whom ever 'twas thy greatest joy To fondle as a tender boy? Didst thou not give with thoughtful care Our food, our drink, our robes to wear? Whose love will now for us provide, When thou, our king and sire, hast died?
- **Translation**: 

---

### Verse 6 (Ramayana 0.671)
- **Original**: Canto LXXVII. The Gathering Of The Ashes. 653 At such a time bereft, forlorn, Why is not earth in sunder torn, Missing her monarch's firm control, His love of right, his lofty soul? Ah me, for Ráma roams afar, My sire is where the Blessed are; How can I live deserted? I Will pass into the fire and die. Abandoned thus, I will not brook Upon Ayodhyá's town to look, Once guarded by Ikshváku's race: The wood shall be my dwelling place.” Then when the princes' mournful train Heard the sad brothers thus complain, And saw their misery, at the view Their grief burst wilder out anew. Faint with lamenting, sad and worn, Each like a bull with broken horn, The brothers in their wild despair Lay rolling, mad with misery, there. Then old Va[ishmha good and true, Their father's priest, all lore who knew, Raised weeping Bharat on his feet, And thus bespake with counsel meet: “Twelve days, my lord, have past away [187] Since flames consumed thy father's clay: Delay no more: as rules ordain, Gather what bones may yet remain. Three constant pairs are ever found To hem all mortal creatures round:354 Then mourn not thus, O Prince, for none Their close companionship may shun.” 354 Birth and death, pleasure and pain, loss and gain.
- **Translation**: 

---

### Verse 7 (Ramayana 0.672)
- **Original**: 654 The Ramayana Sumantra badeZatrughna rise, And soothed his soul with counsel wise, And skilled in truth, his hearer taught How all things are and come to naught. When rose each hero from the ground, A lion lord of men, renowned, He showed like Indra's flag,355 whereon Fierce rains have dashed and suns have shone. They wiped their red and weeping eyes, And gently made their sad replies: Then, urged to haste, the royal pair Performed the rites that claimed their care. Canto LXXVIII. Manthará Punished. Zatrughna thus to Bharat spake Who longed the forest road to take: “He who in woe was wont to give Strength to himself and all that live— Dear Ráma, true and pure in heart, Is banished by a woman's art. Yet here was LakshmaG, brave and strong, Could not his might prevent the wrong? Could not his arm the king restrain, Or make the banished free again? One loving right and fearing crime Had checked the monarch's sin in time, When, vassal of a woman's will, His feet approached the path of ill.” 355 Erected upon a tree or high staff in honour of Indra.
- **Translation**: 

---

### Verse 8 (Ramayana 0.673)
- **Original**: Canto LXXVIII. Manthará Punished. 655 While LakshmaG's younger brother, dread Zatrughna, thus to Bharat said, Came to the fronting door, arrayed In glittering robes, the hump-back maid. There she, with sandal-oil besmeared, In garments meet for queens appeared: And lustre to her form was lent By many a gem and ornament. She girdled with her broidered zone, And many a chain about her thrown, Showed like a female monkey round Whose body many a string is bound. When on that cause of evil fell The quick eye of the sentinel, He grasped her in his ruthless hold, And hastening in,Zatrughna told: “Here is the wicked pest,” he cried, “Through whom the king thy father died, And Ráma wanders in the wood: Do with her as thou deemest good.” The warder spoke: and every word Zatrughna's breast to fury stirred: He called the servants, all and each. And spake in wrath his hasty speech: “This is the wretch my sire who slew, And misery on my brothers drew: Let her this day obtain the meed, Vile sinner, of her cruel deed.” He spake; and moved by fury laid His mighty hand upon the maid, Who as her fellows ringed her round, Made with her cries the hall resound. Soon as the gathered women viewed Zatrughna in his angry mood,
- **Translation**: 

---

### Verse 9 (Ramayana 0.674)
- **Original**: 656 The Ramayana Their hearts disturbed by sudden dread, They turned and from his presence fled. “His rage,” they cried,“on us will fall, And ruthless, he will slay us all. Come, to Kau[alyá let us flee: Our hope, our sure defence is she, Approved by all, of virtuous mind, Compassionate, and good, and kind.” His eyes with burning wrath aglow, Zatrughna, shatterer of the foe, Dragged on the ground the hump-back maid Who shrieked aloud and screamed for aid. This way and that with no remorse He dragged her with resistless force, And chains and glittering trinkets burst Lay here and there with gems dispersed, Till like the sky of Autumn shone The palace floor they sparkled on. The lord of men, supremely strong, Haled in his rage the wretch along: Where Queen Kaikeyí dwelt he came, And sternly then addressed the dame. Deep in her heart Kaikeyí felt The stabs his keen reproaches dealt, And ofZatrughna's ire afraid, To Bharat flew and cried for aid. He looked and saw the prince inflamed With burning rage, and thus exclaimed: “Forgive! thine angry arm restrain: A woman never may be slain. My hand Kaikeyí's blood would spill, The sinner ever bent on ill, But Ráma, long in duty tried,
- **Translation**: 

---

### Verse 10 (Ramayana 0.675)
- **Original**: Canto LXXIX. Bharat's Commands. 657 Would hate the impious matricide: And if he knew thy vengeful blade Had slaughtered e'en this hump-back maid, Never again, be sure, would he Speak friendly word to thee or me.” When Bharat's speechZatrughna heard He calmed the rage his breast that stirred, [188] Releasing from her dire constraint The trembling wretch with terror faint. Then to Kaikeyí's feet she crept, And prostrate in her misery wept. Kaikeyí on the hump-back gazed, And saw her weep and gasp. Still quivering, with her senses dazed, From fierceZatrughna's grasp. With gentle words of pity she Assuaged her wild despair, E'en as a tender hand might free A curlew from the snare. Canto LXXIX. Bharat's Commands. Now when the sun's returning ray Had ushered in the fourteenth day, The gathered peers of state addressed To Bharat's ear their new request: “Our lord to heaven has parted hence, Long served with deepest reverence; Ráma, the eldest, far from home, And Lakshma G, in the forest roam.
- **Translation**: 

---

### Verse 11 (Ramayana 0.676)
- **Original**: 658 The Ramayana O Prince, of mighty fame, be thou Our guardian and our monarch now, Lest secret plot or foeman's hate Assail our unprotected state. With longing eyes, O Lord of men, To thee look friend and citizen, And ready is each sacred thing To consecrate our chosen king. Come, Bharat, and accept thine own Ancient hereditary throne. Thee let the priests this day install As monarch to preserve us all.” Around the sacred gear he bent His circling footsteps reverent, And, firm to vows he would not break, Thus to the gathered people spake: “The eldest son is ever king: So rules the house from which we spring: Nor should ye, Lords, like men unwise, With words like these to wrong advise. Ráma is eldest born, and he The ruler of the land shall be. Now to the woods will I repair, Five years and nine to lodge me there. Assemble straight a mighty force, Cars, elephants, and foot and horse, For I will follow on his track And bring my eldest brother back. Whate'er the rites of throning need Placed on a car the way shall lead: The sacred vessels I will take To the wild wood for Ráma's sake. I o'er the lion prince's head
- **Translation**: 

---

### Verse 12 (Ramayana 0.677)
- **Original**: Canto LXXX. The Way Prepared. 659 The sanctifying balm will shed, And bring him, as the fire they bring Forth from the shrine, with triumphing. Nor will I let my mother's greed In this her cherished aim succeed: In pathless wilds will I remain, And Ráma here as king shall reign. To make the rough ways smooth and clear Send workman out and pioneer: Let skilful men attend beside Our way through pathless spots to guide.” As thus the royal Bharat spake, Ordaining all for Ráma's sake, The audience gave with one accord Auspicious answer to their lord: “Be royal Fortune aye benign To thee for this good speech of thine, Who wishest still thine elder's hand To rule with kingly sway the land.” Their glorious speech, their favouring cries Made his proud bosom swell: And from the prince's noble eyes The tears of rapture fell.356 Canto LXXX. The Way Prepared. 356 I follow in this stanza the Bombay edition in preference to Schlegel's which gives the tears of joy to the courtiers.
- **Translation**: 

---

### Verse 13 (Ramayana 0.678)
- **Original**: 660 The Ramayana All they who knew the joiner's art, Or distant ground in every part; Each busied in his several trade, To work machines or ply the spade; Deft workmen skilled to frame the wheel, Or with the ponderous engine deal; Guides of the way, and craftsmen skilled, To sink the well, make bricks, and build; And those whose hands the tree could hew, And work with slips of cut bamboo, Went forward, and to guide them, they Whose eyes before had seen the way. Then onward in triumphant mood Went all the mighty multitude. Like the great sea whose waves leap high When the full moon is in the sky. Then, in his proper duty skilled, Each joined him to his several guild, And onward in advance they went With every tool and implement. Where bush and tangled creeper lay With trenchant steel they made the way; They felled each stump, removed each stone, And many a tree was overthrown. In other spots, on desert lands, Tall trees were reared by busy hands. Where'er the line of road they took, They plied the hatchet, axe, and hook.[189] Others, with all their strength applied, Cast vigorous plants and shrubs aside, In shelving valleys rooted deep, And levelled every dale and steep. Each pit and hole that stopped the way They filled with stones, and mud, and clay,
- **Translation**: 

---

### Verse 14 (Ramayana 0.679)
- **Original**: Canto LXXX. The Way Prepared. 661 And all the ground that rose and fell With busy care was levelled well. They bridged ravines with ceaseless toil, And pounded fine the flinty soil. Now here, now there, to right and left, A passage through the ground they cleft, And soon the rushing flood was led Abundant through the new-cut bed, Which by the running stream supplied With ocean's boundless waters vied. In dry and thirsty spots they sank Full many a well and ample tank, And altars round about them placed To deck the station in the waste. With well-wrought plaster smoothly spread, With bloomy trees that rose o'erhead, With banners waving in the air, And wild birds singing here and there, With fragrant sandal-water wet, With many a flower beside it set, Like the Gods' heavenly pathway showed That mighty host's imperial road. Deft workmen, chosen for their skill To do the high-souled Bharat's will, In every pleasant spot where grew Trees of sweet fruit and fair to view, As he commanded, toiled to grace With all delights his camping-place. And they who read the stars, and well Each lucky sign and hour could tell, Raised carefully the tented shade Wherein high-minded Bharat stayed. With ample space of level ground, With broad deep moat encompassed round;
- **Translation**: 

---

### Verse 15 (Ramayana 0.680)
- **Original**: 662 The Ramayana Like Mandar in his towering pride, With streets that ran from side to side; Enwreathed with many a palace tall Surrounded by its noble wall; With roads by skilful workmen made, Where many a glorious banner played; With stately mansions, where the dove Sat nestling in her cote above. Rising aloft supremely fair Like heavenly cars that float in air, Each camp in beauty and in bliss Matched Indra's own metropolis. As shines the heaven on some fair night, With moon and constellations filled, The prince's royal road was bright, Adorned by art of workmen skilled. Canto LXXXI. The Assembly. Ere yet the dawn had ushered in The day should see the march begin, Herald and bard who rightly knew Each nice degree of honour due, Their loud auspicious voices raised, And royal Bharat blessed and praised. With sticks of gold the drum they smote, Which thundered out its deafening note, Blew loud the sounding shell, and blent Each high and low-toned instrument. The mingled sound of drum and horn Through all the air was quickly borne,
- **Translation**: 

---

### Verse 16 (Ramayana 0.681)
- **Original**: Canto LXXXI. The Assembly. 663 And as in Bharat's ear it rang, Gave the sad prince another pang. Then Bharat, starting from repose, Stilled the glad sounds that round him rose, “I am not king; no more mistake:” Then toZatrughna thus he spake: “O see what general wrongs succeed Sprung from Kaikeyí's evil deed! The king my sire has died and thrown Fresh miseries on me alone. The royal bliss, on duty based, Which our just high-souled father graced, Wanders in doubt and sore distress Like a tossed vessel rudderless. And he who was our lordly stay Roams in the forest far away, Expelled by this my mother, who To duty's law is most untrue.” As royal Bharat thus gave vent To bitter grief in wild lament, Gazing upon his face the crowd Of pitying women wept aloud. His lamentation scarce was o'er, When Saint Va[ishmha, skilled in lore Of royal duty, dear to fame, To join the great assembly came. Girt by disciples ever true Still nearer to that hall he drew, Resplendent, heavenly to behold, Adorned with wealth of gems and gold: E'en so a man in duty tried Draws near to meet his virtuous bride.
- **Translation**: 

---

### Verse 17 (Ramayana 0.682)
- **Original**: 664 The Ramayana He reached his golden seat o'erlaid With coverlet of rich brocade, There sat, in all the Vedas read, And called the messengers, and said: “Go forth, let Bráhman, Warrior, peer, And every captain gather here: Let all attentive hither throng: Go, hasten: we delay too long. Zatrughna, glorious Bharat bring, The noble children of the king,357[190] Yudhájit358 and Sumantra, all The truthful and the virtuous call.” He ended: soon a mighty sound Of thickening tumult rose around, As to the hall they bent their course With car, and elephant, and horse, The people all with glad acclaim Welcomed Prince Bharat as he came: E'en as they loved their king to greet, Or as the Gods Lord Indra359 meet. The vast assembly shone as fair With Bharat's kingly face As Da[aratha's self were there To glorify the place. It gleamed like some unruffled lake Where monsters huge of mould With many a snake their pastime take O'er shells, sand, gems, and gold. 357 The commentator says“Zatrughna accompanied by the other sons of the king.” 358 Not Bharat's uncle, but some councillor. 359 Zatakratu, Lord of a hundred sacrifices, the performance of a hundred A[vamedhas or sacrifices of a horse entitling the sacrificer to this exalted dignity.
- **Translation**: 

---

### Verse 18 (Ramayana 0.683)
- **Original**: Canto LXXXII. The Departure. 665 Canto LXXXII. The Departure. The prudent prince the assembly viewed Thronged with its noble multitude, Resplendent as a cloudless night When the full moon is in his height; While robes of every varied hue A glory o'er the synod threw. The priest in lore of duty skilled Looked on the crowd the hall that filled, And then in accents soft and grave To Bharat thus his counsel gave: “The king, dear son, so good and wise, Has gone from earth and gained the skies, Leaving to thee, her rightful lord, This rich wide land with foison stored. And still has faithful Ráma stood Firm to the duty of the good, And kept his father's hest aright, As the moon keeps its own dear light. Thus sire and brother yield to thee This realm from all annoyance free: Rejoice thy lords: enjoy thine own: Anointed king, ascend the throne. Let vassal Princes hasten forth From distant lands, west, south, and north, From Kerala,360 from every sea, And bring ten million gems to thee.” As thus the sage Va[ishmha spoke, A storm of grief o'er Bharat broke. And longing to be just and true, His thoughts to duteous Ráma flew. 360 The modern Malabar.
- **Translation**: 

---

### Verse 19 (Ramayana 0.684)
- **Original**: 666 The Ramayana With sobs and sighs and broken tones, E'en as a wounded mallard moans, He mourned with deepest sorrow moved, And thus the holy priest reproved: “O, how can such as Bharat dare The power and sway from him to tear, Wise, and devout, and true, and chaste, With Scripture lore and virtue graced? Can one of Da[aratha's seed Be guilty of so vile a deed? The realm and I are Ráma's: thou, Shouldst speak the words of justice now. For he, to claims of virtue true, Is eldest born and noblest too: Nahush, Dilípa could not be More famous in their lives than he. As Da[aratha ruled of right, So Ráma's is the power and right. If I should do this sinful deed And forfeit hope of heavenly meed, My guilty act would dim the shine Of old Ikshváku's glorious line. Nay, as the sin my mother wrought Is grievous to my inmost thought, I here, my hands together laid, Will greet him in the pathless shade. To Ráma shall my steps be bent, My King, of men most excellent, Raghu's illustrious son, whose sway Might hell, and earth, and heaven obey.” That righteous speech, whose every word Bore virtue's stamp, the audience heard; On Ráma every thought was set,
- **Translation**: 

---

### Verse 20 (Ramayana 0.685)
- **Original**: Canto LXXXII. The Departure. 667 And with glad tears each eye was wet. “Then, if the power I still should lack To bring my noble brother back, I in the wood will dwell, and share His banishment with LakshmaG there. By every art persuasive I To bring him from the wood will try, And show him to your loving eyes, O Bráhmans noble, good, and wise. E'en now, the road to make and clear, Each labourer pressed, and pioneer Have I sent forward to precede The army I resolve to lead.” Thus, by fraternal love possessed, His firm resolve the prince expressed, Then to Sumantra, deeply read In holy texts, he turned and said: “Sumantra, rise without delay, And as I bid my words obey. Give orders for the march with speed, And all the army hither lead.” The wise Sumantra, thus addressed, Obeyed the high-souled chief's behest. He hurried forth with joy inspired And gave the orders he desired. Delight each soldier's bosom filled, And through each chief and captain thrilled, [191]
- **Translation**: 

---



--- End of Ramayan_batch_132.md ---


--- Start of Ramayan_batch_133.md ---

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

### Verse 1 (Ramayana 0.686)
- **Original**: 668 The Ramayana To hear that march proclaimed, to bring Dear Ráma back from wandering. From house to house the tidings flew: Each soldier's wife the order knew, And as she listened blithe and gay Her husband urged to speed away. Captain and soldier soon declared The host equipped and all prepared With chariots matching thought for speed, And wagons drawn by ox and steed. When Bharat by Va[ishmha's side, His ready host of warriors eyed, Thus in Sumantra's ear he spoke: “My car and horses quickly yoke.” Sumantra hastened to fulfil With ready joy his master's will, And quickly with the chariot sped Drawn by fleet horses nobly bred. Then glorious Bharat, true, devout, Whose genuine valour none could doubt, Gave in fit words his order out; For he would seek the shade Of the great distant wood, and there Win his dear brother with his prayer: “Sumantra, haste! my will declare The host be all arrayed. I to the wood my way will take, To Ráma supplication make, And for the world's advantage sake, Will lead him home again.” Then, ordered thus, the charioteer Who listened with delighted ear, Went forth and gave his orders clear To captains of the train.
- **Translation**: 

---

### Verse 2 (Ramayana 0.687)
- **Original**: Canto LXXXIII. The Journey Begun. 669 He gave the popular chiefs the word, And with the news his friends he stirred, And not a single man deferred Preparing for the road. Then Bráhman, Warrior, Merchant, thrall, Obedient to Sumantra's call, Each in his house arose, and all Yoked elephant or camel tall, Or ass or noble steed in stall, And full appointed showed. Canto LXXXIII. The Journey Begun. Then Bharat rose at early morn, And in his noble chariot borne Drove forward at a rapid pace Eager to look on Ráma's face. The priests and lords, a fair array, In sun-bright chariots led the way. Behind, a well appointed throng, Nine thousand elephants streamed along. Then sixty thousand cars, and then, With various arms, came fighting men. A hundred thousand archers showed In lengthened line the steeds they rode— A mighty host, the march to grace Of Bharat, pride of Raghu's race. Kaikeyí and Sumitrá came, And good Kau[alyá, dear to fame: By hopes of Ráma's coming cheered They in a radiant car appeared.
- **Translation**: 

---

### Verse 3 (Ramayana 0.688)
- **Original**: 670 The Ramayana On fared the noble host to see Ráma and LakshmaG, wild with glee, And still each other's ear to please, Of Ráma spoke in words like these: “When shall our happy eyes behold Our hero true, and pure, and bold, So lustrous dark, so strong of arm, Who keeps the world from woe and harm? The tears that now our eyeballs dim Will vanish at the sight of him, As the whole world's black shadows fly When the bright sun ascends the sky.” Conversing thus their way pursued The city's joyous multitude, And each in mutual rapture pressed A friend or neighbour to his breast. Thus every man of high renown, And every merchant of the town, And leading subjects, joyous went Toward Ráma in his banishment. And those who worked the potter's wheel, And artists skilled in gems to deal; And masters of the weaver's art, And those who shaped the sword and dart; And they who golden trinkets made, And those who plied the fuller's trade; And servants trained the bath to heat, And they who dealt in incense sweet; Physicians in their business skilled, And those who wine and mead distilled; And workmen deft in glass who wrought, And those whose snares the peacock caught; With them who bored the ear for rings,
- **Translation**: 

---

### Verse 4 (Ramayana 0.689)
- **Original**: Canto LXXXIII. The Journey Begun. 671 Or sawed, or fashioned ivory things; And those who knew to mix cement, Or lived by sale of precious scent; And men who washed, and men who sewed, And thralls who mid the herds abode; And fishers of the flood, and they Who played and sang, and women gay; And virtuous Bráhmans, Scripture-wise, Of life approved in all men's eyes; These swelled the prince's lengthened train, Borne each in car or bullock wain. Fair were the robes they wore upon Their limbs where red-hued unguents shone. These all in various modes conveyed Their journey after Bharat made; The soldiers' hearts with rapture glowed, Following Bharat on his road, Their chief whose tender love would fain Bring his dear brother home again. With elephant, and horse, and car, The vast procession travelled far, [192] And came where Gangá's waves below The town ofZringavera361 flow. There, with his friends and kinsmen nigh, Dwelt Guha, Ráma's dear ally, Heroic guardian of the land With dauntless heart and ready hand. There for a while the mighty force That followed Bharat stayed its course, Gazing on Gangá's bosom stirred By many a graceful water-bird. When Bharat viewed his followers there, 361 Now Sungroor, in the Allahabad district.
- **Translation**: 

---

### Verse 5 (Ramayana 0.690)
- **Original**: 672 The Ramayana And Gangá's water, blest and fair, The prince, who lore of words possessed, His councillors and lords addressed: “The captains of the army call: Proclaim this day a halt for all, That so to-morrow, rested, we May cross this flood that seeks the sea. Meanwhile, descending to the shore, The funeral stream I fain would pour From Gangá's fair auspicious tide To him, my father glorified.” Thus Bharat spoke: each peer and lord Approved his words with one accord, And bade the weary troops repose In separate spots where'er they chose. There by the mighty stream that day, Most glorious in its vast array The prince's wearied army lay In various groups reclined. There Bharat's hours of night were spent, While every eager thought he bent On bringing home from banishment His brother, great of mind. Canto LXXXIV. Guha's Anger.
- **Translation**: 

---

### Verse 6 (Ramayana 0.691)
- **Original**: Canto LXXXIV. Guha's Anger. 673 King Guha saw the host spread o'er The wide expanse of Gangá's shore, With waving flag and pennon graced, And to his followers spoke in haste: “A mighty army meets my eyes, That rivals Ocean's self in size: Where'er I look my very mind No limit to the host can find. Sure Bharat with some evil thought His army to our land has brought. See, huge of form, his flag he rears, That like an Ebony-tree appears. He comes with bonds to take and chain, Or triumph o'er our people slain: And after, Ráma will he slay,— Him whom his father drove away: The power complete he longs to gain, And — task too hard— usurp the reign. So Bharat comes with wicked will His brother Ráma's blood to spill. But Ráma's slave and friend am I; He is my lord and dear ally. Keep here your watch in arms arrayed Near Gangá's flood to lend him aid, And let my gathered servants stand And line with troops the river strand. Here let the river keepers meet, Who flesh and roots and berries eat; A hundred fishers man each boat Of the five hundred here afloat, And let the youthful and the strong Assemble in defensive throng. But yet, if, free from guilty thought 'Gainst Ráma, he this land have sought,
- **Translation**: 

---

### Verse 7 (Ramayana 0.692)
- **Original**: 674 The Ramayana The prince's happy host to-day Across the flood shall make its way.” He spoke: then bearing in a dish A gift of honey, meat, and fish, The king of the Nishádas drew Toward Bharat for an interview. When Bharat's noble charioteer Observed the monarch hastening near, He duly, skilled in courteous lore, The tidings to his master bore: “This aged prince who hither bends His footsteps with a thousand friends, Knows, firm ally of Ráma, all That may in DaG ak wood befall: Therefore, Kakutstha's son, admit The monarch, as is right and fit: For doubtless he can clearly tell Where Ráma now and LakshmaG dwell.” When Bharat heard Sumantra's rede, To his fair words the prince agreed: “Go quickly forth,” he cried,“and bring Before my face the aged king.” King Guha, with his kinsmen near, Rejoiced the summoning to hear: He nearer drew, bowed low his head, And thus to royal Bharat said: “No mansions can our country boast, And unexpected comes thy host: But what we have I give thee all: Rest in the lodging of thy thrall. See, the Nishádas here have brought The fruit and roots their hands have sought:
- **Translation**: 

---

### Verse 8 (Ramayana 0.693)
- **Original**: Canto LXXXV. Guha And Bharat. 675 And we have woodland fare beside, And store of meat both fresh and dried. To rest their weary limbs, I pray This night at least thy host may stay: Then cheered with all we can bestow To-morrow thou with it mayst go.” Canto LXXXV. Guha And Bharat. Thus the Nishádas' king besought: The prince with spirit wisdom-fraught [193] Replied in seemly words that blent Deep matter with the argument: “Thou, friend of him whom I revere, With honours high hast met me here, For thou alone wouldst entertain And feed to-day so vast a train.” In such fair words the prince replied, Then, pointing to the path he cried: “Which way aright will lead my feet To Bharadvája's calm retreat; For all this land near Gangá's streams Pathless and hard to traverse seems?”
- **Translation**: 

---

### Verse 9 (Ramayana 0.694)
- **Original**: 676 The Ramayana Thus spoke the prince: King Guha heard Delighted every prudent word, And gazing on that forest wide, Raised suppliant hands, and thus replied: “My servants, all the ground who know, O glorious Prince, with thee shall go With constant care thy way to guide, And I will journey by thy side. But this thy host so wide dispread Wakes in my heart one doubt and dread, Lest, threatening Ráma good and great, Ill thoughts thy journey stimulate.” But when King Guha, ill at ease, Declared his fear in words like these, As pure as is the cloudless sky With soft voice Bharat made reply: “Suspect me not: ne'er come the time For me to plot so foul a crime! He is my eldest brother, he Is like a father dear to me. I go to lead my brother thence Who makes the wood his residence. No thought but this thy heart should frame: This simple truth my lips proclaim.” Then with glad cheer King Guha cried, With Bharat's answer gratified: “Blessed art thou: on earth I see None who may vie, O Prince, with thee, Who canst of thy free will resign The kingdom which unsought is thine. For this, a name that ne'er shall die, Thy glory through the worlds shall fly,
- **Translation**: 

---

### Verse 10 (Ramayana 0.695)
- **Original**: Canto LXXXV. Guha And Bharat. 677 Who fain wouldst balm thy brother's pain And lead the exile home again.” As Guha thus, and Bharat, each To other spoke in friendly speech, The Day-God sank with glory dead, And night o'er all the sky was spread. Soon as King Guha's thoughtful care Had quartered all the army there, Well honoured, Bharat laid his head BesideZatrughna on a bed. But grief for Ráma yet oppressed High-minded Bharat's faithful breast— Such torment little was deserved By him who ne'er from duty swerved. The fever raged through every vein And burnt him with its inward pain: So when in woods the flames leap free The fire within consumes the tree. From heat of burning anguish sprung The sweat upon his body hung, As when the sun with fervid glow On high Himálaya melts the snow. As, banished from the herd, a bull Wanders alone and sorrowful. Thus sighing and distressed, In misery and bitter grief, With fevered heart that mocked relief, Distracted in his mind, the chief Still mourned and found no rest.
- **Translation**: 

---

### Verse 11 (Ramayana 0.696)
- **Original**: 678 The Ramayana Canto LXXXVI. Guha's Speech. Guha the king, acquainted well With all that in the wood befell, To Bharat the unequalled told The tale of LakshmaG mighty-souled: “With many an earnest word I spake To LakshmaG as he stayed awake, And with his bow and shaft in hand To guard his brother kept his stand: “Now sleep a little, LakshmaG, see This pleasant bed is strewn for thee: Hereon thy weary body lay, And strengthen thee with rest, I pray, Inured to toil are men like these, But thou hast aye been nursed in ease. Rest, duteous-minded! I will keep My watch while Ráma lies asleep: For in the whole wide world is none Dearer to me than Raghu's son. Harbour no doubt or jealous fear: I speak the truth with heart sincere: For from the grace which he has shown Will glory on my name be thrown: Great store of merit shall I gain, And duteous, form no wish in vain. Let me enforced by many a row Of followers, armed with shaft and bow For well-loved Ráma's weal provide Who lies asleep by Sítá's side. For through this wood I often go, And all its shades conceal I know: And we with conquering arms can meet A four-fold host arrayed complete.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.697)
- **Original**: Canto LXXXVI. Guha's Speech. 679 “With words like these I spoke, designed To move the high-souled Bharat's mind, But he upon his duty bent, Plied his persuasive argument: “O, how can slumber close mine eyes When lowly couched with Sítá lies The royal Ráma? can I give My heart to joy, or even live? He whom no mighty demon, no, Nor heavenly God can overthrow, See, Guha, how he lies, alas, [194] With Sítá couched on gathered grass. By varied labours, long, severe, By many a prayer and rite austere, He, Da[aratha's cherished son, By Fortune stamped, from Heaven was won. Now as his son is forced to fly, The king ere long will surely die: Reft of his guardian hand, forlorn In widowed grief this land will mourn. E'en now perhaps, with toil o'erspent, The women cease their loud lament, And cries of woe no longer ring Throughout the palace of the king. But ah for sad Kau[alyá! how Fare she and mine own mother now? How fares the king? this night, I think, Some of the three in death will sink. With hopes uponZatrughna set My mother may survive as yet, But the sad queen will die who bore The hero, for her grief is sore. His cherished wish that would have made Dear Ráma king, so long delayed,
- **Translation**: 

---

### Verse 13 (Ramayana 0.698)
- **Original**: 680 The Ramayana “Too late! too late!” the king will cry, And conquered by his misery die. When Fate has brought the mournful day Which sees my father pass away, How happy in their lives are they Allowed his funeral rites to pay. Our exile o'er, with him who ne'er Turns from the oath his lips may swear, May we returning safe and well gain in fair Ayodhyá dwell.” Thus Bharat stood with many a sigh Lamenting, and the night went by. Soon as the morning light shone fair In votive coils both bound their hair. And then I sent them safely o'er And left them on the farther shore. With Sítá then they onward passed, Their coats of bark about them cast, Their locks like hermits' bound, The mighty tamers of the foe, Each with his arrows and his bow, Went over the rugged ground, Proud in their strength and undeterred Like elephants that lead the herd, And gazing oft around.” Canto LXXXVII. Guha's Story.
- **Translation**: 

---

### Verse 14 (Ramayana 0.699)
- **Original**: Canto LXXXVII. Guha's Story. 681 That speech of Guha Bharat heard With grief and tender pity stirred, And as his ears the story drank, Deep in his thoughtful heart it sank. His large full eyes in anguish rolled, His trembling limbs grew stiff and cold; Then fell he, like a tree uptorn, In woe too grievous to be borne. When Guha saw the long-armed chief Whose eye was like a lotus leaf, With lion shoulders strong and fair, High-mettled, prostrate in despair,— Pale, bitterly afflicted, he Reeled as in earthquake reels a tree. But whenZatrughna standing nigh Saw his dear brother helpless lie, Distraught with woe his head he bowed, Embraced him oft and wept aloud. Then Bharat's mothers came, forlorn Of their dear king, with fasting worn, And stood with weeping eyes around The hero prostrate on the ground. Kau [alyá, by her woe oppressed, The senseless Bharat's limbs caressed, As a fond cow in love and fear Caresses oft her youngling dear: Then yielding to her woe she said, Weeping and sore disquieted: “What torments, O my son, are these Of sudden pain or swift disease? The lives of us and all the line Depend, dear child, on only thine. Ráma and LakshmaG forced to flee, I live by naught but seeing thee:
- **Translation**: 

---

### Verse 15 (Ramayana 0.700)
- **Original**: 682 The Ramayana For as the king has past away Thou art my only help to-day. Hast thou, perchance, heard evil news Of LakshmaG, which thy soul subdues, Or Ráma dwelling with his spouse— My all is he— neath forest boughs?” Then slowly gathering sense and strength The weeping hero rose at length, And words like these to Guha spake, That bade Kau[alyá comfort take: “Where lodged the prince that night? and where Lakshma G the brave, and Sítá fair? Show me the couch whereon he lay, Tell me the food he ate, I pray.” Then Guha the Nishádas' king Replied to Bharat's questioning: “Of all I had I brought the best To serve my good and honoured guest Food of each varied kind I chose, And every fairest fruit that grows. Ráma the hero truly brave Declined the gift I humbly gave: His Warrior part he ne'er forgot, And what I brought accepted not: “No gifts, my friend, may we accept: Our law is, Give, and must be kept.” The high-souled chief, O Monarch, thus With gracious words persuaded us. Then calm and still, absorbed in thought, He drank the water LakshmaG brought, And then, obedient to his vows, He fasted with his gentle spouse. So LakshmaG too from food abstained,[195]
- **Translation**: 

---

### Verse 16 (Ramayana 0.701)
- **Original**: Canto LXXXVIII. The Ingudí Tree. 683 And sipped the water that remained: Then with ruled lips, devoutly staid, The three362 their evening worship paid. Then LakshmaG with unwearied care Brought heaps of sacred grass, and there With his own hands he quickly spread, For Ráma's rest, a pleasant bed, And faithful Sítá's too, where they Reclining each by other lay. Then LakshmaG bathed their feet, and drew A little distance from the two. Here stands the tree which lent them shade, Here is the grass beneath it laid, Where Ráma and his consort spent The night together ere they went. Lakshma G, whose arms the foeman quell, Watched all the night as sentinel, And kept his great bow strung: His hand was gloved, his arm was braced, Two well-filled quivers at his waist, With deadly arrows, hung. I took my shafts and trusty bow, And with that tamer of the foe Stood ever wakeful near, And with my followers, bow in hand, Behind me ranged, a ready band, Kept watch o'er Indra's peer.” Canto LXXXVIII. The Ingudí Tree. 362 Ráma, LakshmaG, and Sumantra.
- **Translation**: 

---

### Verse 17 (Ramayana 0.702)
- **Original**: 684 The Ramayana When Bharat with each friend and peer Had heard that tale so full and clear, They went together to the tree The bed which Ráma pressed to see. Then Bharat to his mothers said: “Behold the high-souled hero's bed: These tumbled heaps of grass betray Where he that night with Sítá lay: Unmeet, the heir of fortune high Thus on the cold bare earth should lie, The monarch's son, in counsel sage, Of old imperial lineage. That lion-lord whose noble bed With finest skins of deer was spread,— How can he now endure to press The bare earth, cold and comfortless! This sudden fall from bliss to grief Appears untrue, beyond belief: My senses are distraught: I seem To view the fancies of a dream. There is no deity so great, No power in heaven can master Fate, If Ráma, Da[aratha's heir, Lay on the ground and slumbered there; And lovely Sítá, she who springs From fair Videha's ancient kings, Ráma's dear wife, by all adored, Lay on the earth beside her lord. Here was his couch, upon this heap He tossed and turned in restless sleep: On the hard soil each manly limb Has stamped the grass with signs of him. That night, it seems, fair Sítá spent Arrayed in every ornament,
- **Translation**: 

---

### Verse 18 (Ramayana 0.703)
- **Original**: Canto LXXXVIII. The Ingudí Tree. 685 For here and there my eyes behold Small particles of glistering gold. She laid her outer garment here, For still some silken threads appear, How dear in her devoted eyes Must be the bed where Ráma lies, Where she so tender could repose And by his side forget her woes. Alas, unhappy, guilty me! For whom the prince was forced to flee, And chief of Raghu's sons and best, A bed like this with Sítá pressed. Son of a royal sire whose hand Ruled paramount o'er every land, Could he who every joy bestows, Whose body like the lotus shows, The friend of all, who charms the sight, Whose flashing eyes are darkly bright, Leave the dear kingdom, his by right, Unmeet for woe, the heir of bliss, And lie upon a bed like this? Great joy and happy fate are thine, O Lakshma G, marked with each fair sign, Whose faithful footsteps follow still Thy brother in his hour of ill. And blest is Sítá, nobly good, Who dwells with Ráma in the wood. Ours is, alas, a doubtful fate Of Ráma reft and desolate. My royal sire has gained the skies, In woods the high-souled hero lies; The state is wrecked and tempest-tossed, A vessel with her rudder lost. Yet none in secret thought has planned
- **Translation**: 

---

### Verse 19 (Ramayana 0.704)
- **Original**: 686 The Ramayana With hostile might to seize the land: Though forced in distant wilds to dwell, The hero's arm protects it well. Unguarded, with deserted wall, No elephant or steed in stall, My father's royal city shows Her portals open to her foes, Of bold protectors reft and bare, Defenceless in her dark despair: But still her foes the wish restrain, As men from poisoned cates refrain. I from this hour my nights will pass Couched on the earth or gathered grass, Eat only fruit and roots, and wear A coat of bark, and matted hair. I in the woods will pass, content, For him the term of banishment; So shall I still unbroken save The promise which the hero gave.[196] While I remain for Ráma there, Zatrughna will my exile share, And Ráma in his home again, With LakshmaG, o'er Ayodhyá reign, for him, to rule and guard the state, The twice-born men shall consecrate. O, may the Gods I serve incline To grant this earnest wish of mine! If when I bow before his feet And with all moving arts entreat, He still deny my prayer, Then with my brother will I live: He must, he must permission give, Roaming in forests there.”
- **Translation**: 

---

### Verse 20 (Ramayana 0.705)
- **Original**: Canto LXXXIX. The Passage Of Gangá. 687 Canto LXXXIX. The Passage Of Gangá. That night the son of Raghu lay On Gangá's bank till break of day: Then with the earliest light he woke And thus to braveZatrughna spoke. “Rise up,Zatrughna, from thy bed: Why sleepest thou the night is fled. See how the sun who chases night Wakes every lotus with his light. Arise, arise, and first of all The lord ofZringavera call, For he his friendly aid will lend Our army o'er the flood to send.” Thus urged,Zatrughna answered:“I, Remembering Ráma, sleepless lie.” As thus the brothers, each to each, The lion-mettled, ended speech, Came Guha, the Nishádas' king, And spoke with kindly questioning: “Hast thou in comfort passed,” he cried, “The night upon the river side? With thee how fares it? and are these, Thy soldiers, healthy and at ease?” Thus the Nishádas' lord inquired In gentle words which love inspired, And Bharat, Ráma's faithful slave, Thus to the king his answer gave: “The night has sweetly passed, and we Are highly honoured, King, by thee. Now let thy servants boats prepare, Our army o'er the stream to bear.”
- **Translation**: 

---



--- End of Ramayan_batch_133.md ---


--- Start of Ramayan_batch_134.md ---

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

### Verse 1 (Ramayana 0.706)
- **Original**: 688 The Ramayana The speech of Bharat Guha heard, And swift to do his bidding stirred. Within the town the monarch sped And to his ready kinsmen said: “Awake, each kinsman, rise, each friend! May every joy your lives attend. Gather each boat upon the shore And ferry all the army o'er.” Thus Guha spoke: nor they delayed, But, rising quick, their lord obeyed, And soon, from every side secured, Five hundred boats were ready moored. Some reared aloft the mystic sign,363 And mighty bells were hung in line: Of firmest build, gay flags they bore, And sailors for the helm and oar. One such King Guha chose, whereon, Of fair white cloth, an awning shone, And sweet musicians charmed the ear,— And bade his servants urge it near. Then Bharat swiftly sprang on board, And thenZatrughna, famous lord, To whom, with many a royal dame, Kau [alyá and Sumitrá came. The household priest went first in place, The elders, and the Bráhman race, And after them the monarch's train Of women borne in many a wain. Then high to heaven the shouts of those Who fired the army's huts,364 arose, With theirs who bathed along the shore, 363 The svastika, a little cross with a transverse line at each extremity. 364 When an army marched it was customary to burn the huts in which it had spent the night.
- **Translation**: 

---

### Verse 2 (Ramayana 0.707)
- **Original**: Canto XC. The Hermitage. 689 Or to the boats the baggage bore. Full freighted with that mighty force The boats sped swiftly on their course, By royal Guha's servants manned, And gentle gales the banners fanned. Some boats a crowd of dames conveyed, In others noble coursers neighed; Some chariots and their cattle bore, Some precious wealth and golden store. Across the stream each boat was rowed, There duly disembarked its load, And then returning on its way, Sped here and there in merry play. Then swimming elephants appeared With flying pennons high upreared. And as the drivers urged them o'er, The look of winged mountains wore. Some men in barges reached the strand, Others on rafts came safe to land: Some buoyed with pitchers crossed the tide, And others on their arms relied. Thus with the help the monarch gave The army crossed pure Gangá's wave: Then in auspicious hour it stood Within Prayága's famous wood. The prince with cheering words addressed His weary men, and bade them rest Where'er they chose and he, With priest and deacon by his side, To Bharadvája's dwelling hied That best of saints to see. [197]
- **Translation**: 

---

### Verse 3 (Ramayana 0.708)
- **Original**: 690 The Ramayana Canto XC. The Hermitage. The prince of men a league away Saw where the hermit's dwelling lay, Then with his lords his path pursued, And left his warrior multitude. On foot, as duty taught his mind, He left his warlike gear behind; Two robes of linen cloth he wore, And bade Va[ishmha walk before. Then Bharat from his lords withdrew When Bharadvája came in view, And toward the holy hermit went Behind Va[ishmha, reverent. When Bharadvája, saint austere, Saw good Va[ishmha drawing near, He cried, upspringing from his seat, “The grace-gift bring, my friend to greet.” When Saint Va[ishmha near him drew, And Bharat paid the reverence due, The glorious hermit was aware That Da[aratha's son was there. The grace-gift, water for their feet He gave, and offered fruit to eat; Then, duty-skilled, with friendly speech In seemly order questioned each: “How fares it in Ayodhyá now With treasury and army? how With kith and kin and friends most dear, With councillor, and prince, and peer?” But, for he knew the king was dead, Of Da[aratha naught he said. Va [ishmha and the prince in turn Would of the hermit's welfare learn:
- **Translation**: 

---

### Verse 4 (Ramayana 0.709)
- **Original**: Canto XC. The Hermitage. 691 Of holy fires they fain would hear, Of pupils, trees, and birds, and deer. The glorious saint his answer made That all was well in holy shade: Then love of Ráma moved his breast, And thus he questioned of his guest: “Why art thou here, O Prince, whose band With kingly sway protects the land? Declare the cause, explain the whole, For yet some doubt disturbs my soul. He whom Kau [alyá bare, whose might The foemen slays, his line's delight, He who with wife and brother sent Afar now roam in banishment, Famed prince, to whom his father spake This order for a woman's sake: “Away! and in the forest spend Thy life till fourteen years shall end”— Has thou the wish to harm him, bent On sin against the innocent? Wouldst thou thine elder's realm enjoy Without a thorn that can annoy?” With sobbing voice and tearful eye Thus Bharat sadly made reply: “Ah lost am I, if thou, O Saint, Canst thus in thought my heart attaint: No warning charge from thee I need; Ne'er could such crime from me proceed. The words my guilty mother spake When fondly jealous for my sake— Think not that I, to triumph moved, Those words approve or e'er approved. O Hermit, I have sought this place
- **Translation**: 

---

### Verse 5 (Ramayana 0.710)
- **Original**: 692 The Ramayana To win the lordly hero's grace, To throw me at my brother's feet And lead him to his royal seat. To this, my journey's aim and end, Thou shouldst, O Saint, thy favour lend: Where is the lord of earth? do thou, Most holy, say, where roams he now?” Then, by the saint Va[ishmha pressed, And all the gathered priests beside, To Bharat's dutiful request The hermit graciously replied: “Worthy of thee, O Prince, this deed, True son of Raghu's ancient seed. I know thee reverent, well-controlled, The glory of the good of old. I grant thy prayer: in this pursuit I know thy heart is resolute. 'Tis for thy sake those words I said That wider still thy fame may spread. I know where Ráma, duty-tried, His brother, and his wife abide. Where Chitrakúma's heights arise Thy brother Ráma's dwelling lies. Go thither with the morning's light, And stay with all thy lords tonight: For I would show thee honour high, And do not thou my wish deny.” Canto XCI. Bharadvája's Feast.
- **Translation**: 

---

### Verse 6 (Ramayana 0.711)
- **Original**: Canto XCI. Bharadvája's Feast. 693 Soon as he saw the prince's mind To rest that day was well inclined, He sought Kaikeyí's son to please With hospitable courtesies. Then Bharat to the saint replied: “Our wants are more than satisfied. The gifts which honoured strangers greet, And water for our weary feet Hast thou bestowed with friendly care, And every choice of woodland fare.” Then Bharadvája spoke, a smile Playing upon his lips the while: “I know, dear Prince, thy friendly mind Will any fare sufficient find, But gladly would I entertain And banquet all thine armed train: Such is my earnest wish: do thou This longing of my heart allow, Why hast thou hither bent thy way, And made thy troops behind thee stay? [198] Why unattended? couldst thou not With friends and army seek this spot?” Bharat, with reverent hands raised high, To that great hermit made reply: “My troops, for awe of thee, O Sage, I brought not to thy hermitage: Troops of a king or monarch's son A hermit's home should ever shun. Behind me comes a mighty train Wide spreading o'er the ample plain, Where every chief and captain leads Men, elephants, and mettled steeds.
- **Translation**: 

---

### Verse 7 (Ramayana 0.712)
- **Original**: 694 The Ramayana I feared, O reverend Sage, lest these Might harm the holy ground and trees, Springs might be marred and cots o'erthrown, So with the priests I came alone.” “Bring all thy host,” the hermit cried, And Bharat, to his joy, complied. Then to the chapel went the sire, Where ever burnt the sacred fire, And first, in order due, with sips Of water purified his lips: To Vi[vakarmá, then he prayed, His hospitable feast to aid: “Let Vi[vakarmá hear my call, The God who forms and fashions all: A mighty banquet I provide, Be all my wants this day supplied. Lord Indra at their head, the three365 Who guard the worlds I call to me: A mighty host this day I feed, Be now supplied my every need. Let all the streams that eastward go, And those whose waters westering flow, Both on the earth and in the sky, Flow hither and my wants supply. Be some with ardent liquor filled, And some with wine from flowers distilled, While some their fresh cool streams retain Sweet as the juice of sugar-cane. I call the Gods, I call the band Of minstrels that around them stand: I call the Háhá and Huhú, I call the sweet Vi[vávasu, 365 Yáma, VaruGa, and Kuvera.
- **Translation**: 

---

### Verse 8 (Ramayana 0.713)
- **Original**: Canto XCI. Bharadvája's Feast. 695 I call the heavenly wives of these With all the bright Apsarases, Alambúshá of beauty rare, The charmer of the tangled hair, Ghritáchí and Vi[váchi fair, Hemá and Bhímá sweet to view, And lovely Nágadantá too, And all the sweetest nymphs who stand By Indra or by Brahmá's hand— I summon these with all their train And Tumburu to lead the strain. Here let Kuvera's garden rise Which far in Northern Kuru366 lies: For leaves let cloth and gems entwine, And let its fruit be nymphs divine. Let Soma367 give the noblest food To feed the mighty multitude, Of every kind, for tooth and lip, To chew, to lick, to suck, and sip. Let wreaths, where fairest flowers abound, Spring from the trees that bloom around. Each sort of wine to woo the taste, And meats of every kind be placed.” 366 “A happy land in the remote north where the inhabitants enjoy a natural pefection attended with complete happiness obtained without exertion. There is there no vicissitude, nor decrepitude, nor death, nor fear: no distinction of virtue and vice, none of the inequalities denoted by the words best, worst, and intermediate, nor any change resulting from the succession of the four Yugas.” See MUIR 'S{FNS Sanskrit Texts, Vol. I. p. 492. 367 The Moon.
- **Translation**: 

---

### Verse 9 (Ramayana 0.714)
- **Original**: 696 The Ramayana Thus spake the hermit self-restrained, With proper tone by rules ordained, On deepest meditation bent, In holy might preëminent. Then as with hands in reverence raised Absorbed in thought he eastward gazed, The deities he thus addressed Came each in semblance manifest. Delicious gales that cooled the frame From Malaya and Dardar came, That kissed those scented hills and threw Auspicious fragrance where they blew. Then falling fast in sweetest showers Came from the sky immortal flowers, And all the airy region round With heavenly drums was made to sound. Then breathed a soft celestial breeze, Then danced the bright Apsarases, The minstrels and the Gods advanced, And warbling lutes the soul entranced. The earth and sky that music filled, And through each ear it softly thrilled, As from the heavenly quills it fell With time and tune attempered well. Soon as the minstrels ceased to play And airs celestial died away, The troops of Bharat saw amazed What Vi[vakarmá's art had raised. On every side, five leagues around, All smooth and level lay the ground, With fresh green grass that charmed the sight Like sapphires blent with lazulite. There the Wood-apple hung its load, The Mango and the Citron glowed,
- **Translation**: 

---

### Verse 10 (Ramayana 0.715)
- **Original**: Canto XCI. Bharadvája's Feast. 697 The Bel and scented Jak were there, And Apelá with fruitage fair. There, brought from Northern Kuru, stood Rich in delights, the glorious wood, And many a stream was seen to glide [199] With flowering trees along its side. There mansions rose with four wide halls, And elephants and chargers' stalls, And many a house of royal state, Triumphal arc and bannered gate. With noble doorways, sought the sky, Like a pale cloud, a palace high, Which far and wide rare fragrance shed, With wreaths of white engarlanded. Square was its shape, its halls were wide, With many a seat and couch supplied, Drink of all kinds, and every meat Such as celestial Gods might eat. Then at the bidding of the seer Kaikeyí's strong-armed son drew near, And passed within that fair abode Which with the noblest jewels glowed. Then, as Va[ishmha led the way, The councillors, in due array, Followed delighted and amazed And on the glorious structure gazed. Then Bharat, Raghu's son, drew near The kingly throne, with prince and peer, Whereby the chouri in the shade Of the white canopy was laid. Before the throne he humbly bent And honoured Ráma, reverent, Then in his hand the chouri bore, And sat where sits a councillor.
- **Translation**: 

---

### Verse 11 (Ramayana 0.716)
- **Original**: 698 The Ramayana His ministers and household priest Sat by degrees from chief to least, Then sat the captain of the host And all the men he honoured most. Then when the saint his order gave, Each river with enchanted wave Rolled milk and curds divinely sweet Before the princely Bharat's feet; And dwellings fair on either side, With gay white plaster beautified, Their heavenly roofs were seen to lift, The Bráhman Bharadvája's gift. Then straight by Lord Kuvera sent, Gay with celestial ornament Of bright attire and jewels' shine, Came twenty thousand nymphs divine: The man on whom those beauties glanced That moment felt his soul entranced. With them from Nandan's blissful shades Came twenty thousand heavenly maids. Tumburu, Nárad, Gopa came, And Sutanu, like radiant flame, The kings of the Gandharva throng, And ravished Bharat with their song. Then spoke the saint, and swift obeyed Alambúshá, the fairest maid, And Mi [rake[í bright to view, Rama Gá, PuG ríká too, And danced to him with graceful ease The dances of Apsarases. All chaplets that by Gods are worn, Or Chaitraratha's graves adorn, Bloomed by the saint's command arrayed On branches in Prayága's shade.
- **Translation**: 

---

### Verse 12 (Ramayana 0.717)
- **Original**: Canto XCI. Bharadvája's Feast. 699 When at the saint's command the breeze Made music with the Vilva trees, To wave in rhythmic beat began The boughs of each Myrobolan, And holy fig-trees wore the look Of dancers, as their leaflets shook. The fair Tamála, palm, and pine, With trees that tower and plants that twine, The sweetly varying forms displayed Of stately dame or bending maid. Here men the foaming winecup quaffed, Here drank of milk full many a draught, And tasted meats of every kind, Well dressed, whatever pleased their mind. Then beauteous women, seven or eight, Stood ready by each man to wait: Beside the stream his limbs they stripped And in the cooling water dipped. And then the fair ones, sparkling eyed, With soft hands rubbed his limbs and dried, And sitting on the lovely bank Held up the winecup as he drank. Nor did the grooms forget to feed Camel and mule and ox and steed, For there were stores of roasted grain, Of honey and of sugar-cane. So fast the wild excitement spread Among the warriors Bharat led, That all the mighty army through The groom no more his charger knew, And he who drove might seek in vain To tell his elephant again. With every joy and rapture fired, Entranced with all the heart desired,
- **Translation**: 

---

### Verse 13 (Ramayana 0.718)
- **Original**: 700 The Ramayana The myriads of the host that night Revelled delirious with delight. Urged by the damsels at their side In wild delight the warriors cried: “Ne'er will we seek Ayodhyá, no, Nor yet to DaG ak forest go: Here will we stay: may happy fate On Bharat and on Ráma wait.” Thus cried the army gay and free Exulting in their lawless glee, Both infantry and those who rode On elephants, or steeds bestrode, Ten thousand voices shouting,“This Is heaven indeed for perfect bliss.” With garlands decked they idly strayed, And danced and laughed and sang and played. At length as every soldier eyed, With food like Amrit satisfied, Each dainty cate and tempting meat, No longer had he care to eat. Thus soldier, servant, dame, and slave Received whate'er the wish might crave. As each in new-wrought clothes arrayed Enjoyed the feast before him laid.[200] Each man was seen in white attire Unstained by spot or speck of mire: None was athirst or hungry there, And none had dust upon his hair. On every side in woody dells Was milky food in bubbling wells, And there were all-supplying cows And honey dropping from the boughs. Nor wanted lakes of flower-made drink With piles of meat upon the brink,
- **Translation**: 

---

### Verse 14 (Ramayana 0.719)
- **Original**: Canto XCI. Bharadvája's Feast. 701 Boiled, stewed, and roasted, varied cheer, Peachick and jungle-fowl and deer, There was the flesh of kid and boar, And dainty sauce in endless store, With juice of flowers concocted well, And soup that charmed the taste and smell, And pounded fruits of bitter taste, And many a bath was ready placed Down by each river's shelving side There stood great basins well supplied, And laid therein, of dazzling sheen, White brushes for the teeth were seen, And many a covered box wherein Was sandal powdered for the skin. And mirrors bright with constant care, And piles of new attire were there, And store of sandals and of shoes, Thousands of pairs, for all to choose: Eye-unguents, combs for hair and beard, Umbrellas fair and bows appeared. Lakes gleamed, that lent digestive aid,368 And some for pleasant bathing made, With waters fair, and smooth incline For camels, horses, mules, and kine. There saw they barley heaped on high The countless cattle to supply: The golden grain shone fair and bright As sapphires or the lazulite. To all the gathered host it seemed As if that magic scene they dreamed, And wonder, as they gazed, increased At Bharadvája's glorious feast. 368 The poet does not tell us what these lakes contained.
- **Translation**: 

---

### Verse 15 (Ramayana 0.720)
- **Original**: 702 The Ramayana Thus in the hermit's grove they spent That night in joy and merriment, Blest as the Gods who take their ease Under the shade of Nandan's trees. Each minstrel bade the saint adieu, And to his blissful mansion flew, And every stream and heavenly dame Returned as swiftly as she came. Canto XCII. Bharat's Farewell. So Bharat with his army spent The watches of the night content, And gladly, with the morning's light Drew near his host the anchorite. When Bharadvája saw him stand With hand in reverence joined to hand, When fires of worship had been fed, He looked upon the prince and said: “O blameless son, I pray thee tell, Did the past night content thee well? Say if the feast my care supplied Thy host of followers gratified.”
- **Translation**: 

---

### Verse 16 (Ramayana 0.721)
- **Original**: Canto XCII. Bharat's Farewell. 703 His hands he joined, his head he bent And spoke in answer reverent To the most high and radiant sage Who issued from his hermitage: “Well have I passed the night: thy feast Gave joy to every man and beast; And I, great lord, and every peer Were satisfied with sumptuous cheer, Thy banquet has delighted all From highest chief to meanest thrall, And rich attire and drink and meat Banished the thought of toil and heat. And now, O Hermit good and great, A boon of thee I supplicate. To Ráma's side my steps I bend: Do thou with friendly eye commend. O tell me how to guide my feet To virtuous Ráma's lone retreat: Great Hermit, I entreat thee, say How far from here and which the way.” Thus by fraternal love inspired The chieftain of the saint inquired: Then thus replied the glorious seer Of matchless might, of vows austere: “Ere the fourth league from here be passed, Amid a forest wild and vast, Stands Chitrakúma's mountain tall, Lovely with wood and waterfall. North of the mountain thou wilt see The beauteous stream Mandákiní, Where swarm the waterfowl below, And gay trees on the margin grow. Then will a leafy cot between
- **Translation**: 

---

### Verse 17 (Ramayana 0.722)
- **Original**: 704 The Ramayana The river and the hill be seen: 'Tis Ráma's, and the princely pair Of brothers live for certain there. Hence to the south thine army lead, And then more southward still proceed, So shalt thou find his lone retreat, And there the son of Raghu meet.” Soon as the ordered march they knew, The widows of the monarch flew, Leaving their cars, most meet to ride, And flocked to Bharadvája's side. There with the good Sumitrá Queen Kau [alyá, sad and worn, was seen, Caressing, still with sorrow faint, The feet of that illustrious saint, Kaikeyí too, her longings crossed, Reproached of all, her object lost, Before the famous hermit came,[201] And clasped his feet, o'erwhelmed with shame. With circling steps she humbly went Around the saint preëminent, And stood not far from Bharat's side With heart oppressed, and heavy-eyed. Then the great seer, who never broke One holy vow, to Bharat spoke: “Speak, Raghu's son: I fain would learn The story of each queen in turn.”
- **Translation**: 

---

### Verse 18 (Ramayana 0.723)
- **Original**: Canto XCII. Bharat's Farewell. 705 Obedient to the high request By Bharadvája thus addressed, His reverent hands together laid, He, skilled in speech, his answer made: “She whom, O Saint, thou seest here A Goddess in her form appear, Was the chief consort of the king, Now worn with fast and sorrowing. As Aditi in days of yore The all-preserving VishGu bore, Kau [alyá bore with happy fate Lord Ráma of the lion's gait. She who, transfixed with torturing pangs, On her left arm so fondly hangs, As when her withering leaves decay Droops by the wood the Cassia spray, Sumitrá, pained with woe, is she, The consort second of the three: Two princely sons the lady bare, Fair as the Gods in heaven are fair. And she, the wicked dame through whom My brothers' lives are wrapped in gloom, And mourning for his offspring dear, The king has sought his heavenly sphere,— Proud, foolish-hearted, swift to ire, Self-fancied darling of my sire, Kaikeyí, most ambitious queen, Unlovely with her lovely mien, My mother she, whose impious will Is ever bent on deeds of ill, In whom the root and spring I see Of all this woe which crushes me.”
- **Translation**: 

---

### Verse 19 (Ramayana 0.724)
- **Original**: 706 The Ramayana Quick breathing like a furious snake, With tears and sobs the hero spake, With reddened eyes aglow with rage. And Bharadvája, mighty sage, Supreme in wisdom, calm and grave, In words like these good counsel gave: “O Bharat, hear the words I say; On her the fault thou must not lay: For many a blessing yet will spring From banished Ráma's wandering.” And Bharat, with that promise cheered, Went circling round that saint revered, He humbly bade farewell, and then Gave orders to collect his men. Prompt at the summons thousands flew To cars which noble coursers drew, Bright-gleaming, glorious to behold, Adorned with wealth of burnished gold. Then female elephants and male, Gold-girthed, with flags that wooed the gale, Marched with their bright bells' tinkling chime Like clouds when ends the summer time: Some cars were huge and some were light, For heavy draught or rapid flight, Of costly price, of every kind, With clouds of infantry behind. The dames, Kau[alyá at their head, Were in the noblest chariots led, And every gentle bosom beat With hope the banished prince to meet. The royal Bharat, glory-crowned, With all his retinue around, Borne in a beauteous litter rode, Like the young moon and sun that glowed.
- **Translation**: 

---

### Verse 20 (Ramayana 0.725)
- **Original**: Canto XCIII. Chitrakúta In Sight. 707 The army as it streamed along, Cars, elephants, in endless throng, Showed, marching on its southward way, Like autumn clouds in long array. Canto XCIII. Chitrakúta In Sight. As through the woods its way pursued That mighty bannered multitude, Wild elephants in terror fled With all the startled herds they led, And bears and deer were seen on hill, In forest glade, by every rill. Wide as the sea from coast to coast, The high-souled Bharat's mighty host Covered the earth as cloudy trains Obscure the sky when fall the rains. The stately elephants he led, And countless steeds the land o'erspread, So closely crowded that between Their serried ranks no ground was seen. Then when the host had travelled far, And steeds were worn who drew the car, The glorious Bharat thus addressed Va [ishmha, of his lords the best: “The spot, methinks, we now behold Of which the holy hermit told, For, as his words described, I trace Each several feature of the place: Before us Chitrakúma shows, Mandákiní beside us flows:
- **Translation**: 

---



--- End of Ramayan_batch_134.md ---


--- Start of Ramayan_batch_135.md ---

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

### Verse 1 (Ramayana 0.726)
- **Original**: 708 The Ramayana Afar umbrageous woods arise Like darksome clouds that veil the skies. Now tread these mountain-beasts of mine On Chitrakúma's fair incline. The trees their rain of blossoms shed On table-lands beneath them spread, As from black clouds the floods descend When the hot days of summer end. Zatrughna, look, the mountain see Where heavenly minstrels wander free,[202] And horses browse beneath the steep, Countless as monsters in the deep. Scared by my host the mountain deer Starting with tempest speed appear Like the long lines of cloud that fly In autumn through the windy sky. See, every warrior shows his head With fragrant blooms engarlanded; All look like southern soldiers who Lift up their shields of azure hue. This lonely wood beneath the hill, That was so dark and drear and still, Covered with men in endless streams Now like Ayodhyá's city seems. The dust which countless hoofs excite Obscures the sky and veils the light; But see, swift winds those clouds dispel As if they strove to please me well. See, guided in their swift career By many a skilful charioteer, Those cars by fleetest coursers drawn Race onward over glade and lawn. Look, startled as the host comes near The lovely peacocks fly in fear,
- **Translation**: 

---

### Verse 2 (Ramayana 0.727)
- **Original**: Canto XCIII. Chitrakúta In Sight. 709 Gorgeous as if the fairest blooms Of earth had glorified their plumes. Look where the sheltering covert shows The trooping deer, both bucks and does, That occupy in countless herds This mountain populous with birds. Most lovely to my mind appears This place which every charm endears: Fair as the road where tread the Blest; Here holy hermits take their rest. Then let the army onward press And duly search each green recess For the two lion-lords, till we Ráma once more and LakshmaG see.” Thus Bharat spoke: and hero bands Of men with weapons in their hands Entered the tangled forest: then A spire of smoke appeared in ken. Soon as they saw the rising smoke To Bharat they returned and spoke: “No fire where men are not: 'tis clear That Raghu's sons are dwelling here. Or if not here those heroes dwell Whose mighty arms their foeman quell, Still other hermits here must be Like Ráma, true and good as he.” His ears attentive Bharat lent To their resistless argument, Then to his troops the chief who broke His foe's embattled armies spoke: “Here let the troops in silence stay; One step beyond they must not stray.
- **Translation**: 

---

### Verse 3 (Ramayana 0.728)
- **Original**: 710 The Ramayana Come Dhrishmi and Sumantra, you With me alone the path pursue.” Their leader's speech the warriors heard, And from his place no soldier stirred, And Bharat bent his eager eyes Where curling smoke was seen to rise. The host his order well obeyed, And halting there in silence stayed Watching where from the thicket's shade They saw the smoke appear. And joy through all the army ran, “Soon shall we meet,” thought every man, “The prince we hold so dear.” Canto XCIV. Chitrakúta. There long the son of Raghu dwelt And love for hill and wood he felt. Then his Videhan spouse to please And his own heart of woe to ease, Like some Immortal— Indra so Might Swarga's charms toZachí show— Drew her sweet eyes to each delight Of Chitrakúma's lovely height: “Though reft of power and kingly sway, Though friends and home are far away, I cannot mourn my altered lot, Enamoured of this charming spot. Look, darling, on this noble hill Which sweet birds with their music fill,
- **Translation**: 

---

### Verse 4 (Ramayana 0.729)
- **Original**: Canto XCIV. Chitrakúta. 711 Bright with a thousand metal dyes His lofty summits cleave the skies. See, there a silvery sheen is spread, And there like blood the rocks are red. There shows a streak of emerald green, And pink and yellow glow between. There where the higher peaks ascend, Crystal and flowers and topaz blend, And others flash their light afar Like mercury or some fair star: With such a store of metals dyed The king of hills is glorified. There through the wild birds' populous home The harmless bear and tiger roam: Hyænas range the woody slopes With herds of deer and antelopes. See, love, the trees that clothe his side All lovely in their summer pride, In richest wealth of leaves arrayed, With flower and fruit and light and shade, Look where the young Rose-apple glows; What loaded boughs the Mango shows; See, waving in the western wind The light leaves of the Tamarind, And mark that giant Peepul through The feathery clump of tall bamboo.369 [203] Look, on the level lands above, Delighting in successful love 369 These ten lines are a substitution for, and not a translation of the text which Carey and Marshman thus render:“This mountain adorned with mango, jumboo, usuna, lodhra, piala, punusa, dhava, unkotha, bhuvya, tinisha, vilwa, tindooka, bamboo, kashmaree, urista, uruna, madhooka, tilaka, vuduree, am- luka, nipa, vetra, dhunwuna, veejaka, and other trees affording flowers, and fruits, and the most delightful shade, how charming does it appear!”
- **Translation**: 

---

### Verse 5 (Ramayana 0.730)
- **Original**: 712 The Ramayana In sweet enjoyment many a pair Of heavenly minstrels revels there, While overhanging boughs support Their swords and mantles as they sport: Then see that pleasant shelter where Play the bright Daughters of the Air.370 The mountain seems with bright cascade And sweet rill bursting from the shade, Like some majestic elephant o'er Whose burning head the torrents pour. Where breathes the man who would not feel Delicious languor o'er him steal, As the young morning breeze that springs From the cool cave with balmy wings, Breathes round him laden with the scent Of bud and blossom dew-besprent? If many autumns here I spent With thee, my darling innocent, And Lakshma G, I should never know The torture of the fires of woe, This varied scene so charms my sight, This mount so fills me with delight, Where flowers in wild profusion spring, And ripe fruits glow and sweet birds sing. My beauteous one, a double good Springs from my dwelling in the wood: Loosed is the bond my sire that tied, And Bharat too is gratified. My darling, dost thou feel with me Delight from every charm we see, Of which the mind and every sense Feel the enchanting influence? 370 Vidyadharis, Spirits of Air, sylphs.
- **Translation**: 

---

### Verse 6 (Ramayana 0.731)
- **Original**: Canto XCIV. Chitrakúta. 713 My fathers who have passed away, The royal saints, were wont to say, That life in woodland shades like this Secures a king immortal bliss. See, round the hill at random thrown, Huge masses lie of rugged stone Of every shape and many a hue, Yellow and white and red and blue. But all is fairer still by night: Each rock reflects a softer light, When the whole mount from foot to crest In robes of lambent flame is dressed; When from a million herbs a blaze Of their own luminous glory plays, And clothed in fire each deep ravine, Each pinnacle and crag is seen. Some parts the look of mansions wear, And others are as gardens fair, While others seem a massive block Of solid undivided rock. Behold those pleasant beds o'erlaid With lotus leaves, for lovers made, Where mountain birch and costus throw Cool shadows on the pair below. See where the lovers in their play Have cast their flowery wreaths away, And fruit and lotus buds that crowned Their brows lie trodden on the ground. North Kuru's realm is fair to see, Vasvaukasárá,371 Naliní,372 But rich in fruit and blossom still 371 A lake attached either to Amarávatí the residence of Indra, or Alaká that of Kuvera. 372 The Ganges of heaven.
- **Translation**: 

---

### Verse 7 (Ramayana 0.732)
- **Original**: 714 The Ramayana More fair is Chitrakúma's hill. Here shall the years appointed glide With thee, my beauty, by my side, And Lakshma G ever near; Here shall I live in all delight, Make my ancestral fame more bright, Tread in their path who walk aright, And to my oath adhere.” Canto XCV. Mandákiní. Then Ráma, like the lotus eyed, Descended from the mountain side, And to the Maithil lady showed The lovely stream that softly flowed. And thus Ayodhyá's lord addressed His bride, of dames the loveliest, Child of Videha's king, her face Bright with the fair moon's tender grace: “How sweetly glides, O darling, look, Mandákiní's delightful brook, Adorned with islets, blossoms gay, And sárases and swans at play![204] The trees with which her banks are lined Show flowers and fruit of every kind: The match in radiant sheen is she Of King Kuvera's Naliní.373 My heart exults with pleasure new The shelving band and ford to view, 373 Naliní, as here, may be the name of any lake covered with lotuses.
- **Translation**: 

---

### Verse 8 (Ramayana 0.733)
- **Original**: Canto XCV. Mandákiní. 715 Where gathering herds of thirsty deer Disturb the wave that ran so clear. Now look, those holy hermits mark In skins of deer and coats of bark; With twisted coils of matted hair, The reverend men are bathing there, And as they lift their arms on high The Lord of Day they glorify: These best of saints, my large-eyed spouse, Are constant to their sacred vows. The mountain dances while the trees Bend their proud summits to the breeze, And scatter many a flower and bud From branches that o'erhang the flood. There flows the stream like lucid pearl, Round islets here the currents whirl, And perfect saints from middle air Are flocking to the waters there. See, there lie flowers in many a heap From boughs the whistling breezes sweep, And others wafted by the gale Down the swift current dance and sail. Now see that pair of wild-fowl rise, Exulting with their joyful cries: Hark, darling, wafted from afar How soft their pleasant voices are. To gaze on Chitrakúma's hill, To look upon this lovely rill, To bend mine eyes on thee, dear wife, Is sweeter than my city life. Come, bathe we in the pleasant rill Whose dancing waves are never still, Stirred by those beings pure from sin, The sanctities who bathe therein:
- **Translation**: 

---

### Verse 9 (Ramayana 0.734)
- **Original**: 716 The Ramayana Come, dearest, to the stream descend, Approach her as a darling friend, And dip thee in the silver flood Which lotuses and lilies stud. Let this fair hill Ayodhyá seem, Its silvan things her people deem, And let these waters as they flow Our own beloved Sarjú show. How blest, mine own dear love, am I; Thou, fond and true, art ever nigh, And duteous, faithful LakshmaG stays Beside me, and my word obeys. Here every day I bathe me thrice, Fruit, honey, roots for food suffice, And ne'er my thoughts with longing stray To distant home or royal sway. For who this charming brook can see Where herds of roedeer wander free, And on the flowery-wooded brink Apes, elephants, and lions drink, Nor feel all sorrow fly?” Thus eloquently spoke the pride Of Raghu's children to his bride, And wandered happy by her side Where Chitrakúma azure-dyed Uprears his peaks on high. Canto XCVI. The Magic Shaft.374 374 This canto is allowed, by Indian commentators, to be an interpolation. It cannot be the work of Válmíki.
- **Translation**: 

---

### Verse 10 (Ramayana 0.735)
- **Original**: Canto XCVI. The Magic Shaft. 717 Thus Ráma showed to Janak's child The varied beauties of the wild, The hill, the brook and each fair spot, Then turned to seek their leafy cot. North of the mountain Ráma found A cavern in the sloping ground, Charming to view, its floor was strown With many a mass of ore and stone, In secret shadow far retired Where gay birds sang with joy inspired, And trees their graceful branches swayed With loads of blossom downward weighed. Soon as he saw the cave which took Each living heart and chained the look, Thus Ráma spoke to Sítá who Gazed wondering on the silvan view: “Does this fair cave beneath the height, Videhan lady, charm thy sight? Then let us resting here a while The languor of the way beguile. That block of stone so smooth and square Was set for thee to rest on there, And like a thriving Ke[ar tree This flowery shrub o'ershadows thee.” Thus Ráma spoke, and Janak's child, By nature ever soft and mild, In tender words which love betrayed Her answer to the hero made: “O pride of Raghu's children, still My pleasure is to do thy will. Enough for me thy wish to know: Far hast thou wandered to and fro.”
- **Translation**: 

---

### Verse 11 (Ramayana 0.736)
- **Original**: 718 The Ramayana Thus Sítá spake in gentle tone, And went obedient to the stone, Of perfect face and faultless limb Prepared to rest a while with him. And Ráma, as she thus replied, Turned to his spouse again and cried: “Thou seest, love, this flowery shade For silvan creatures' pleasure made, How the gum streams from trees and plants Torn by the tusks of elephants![205] Through all the forest clear and high Resounds the shrill cicala's cry. Hark how the kite above us moans, And calls her young in piteous tones; So may my hapless mother be Still mourning in her home for me. There mounted on that lofty Sál The loud Bhringráj375 repeats his call: How sweetly now he tunes his throat Responsive to the Koïl's note. Or else the bird that now has sung May be himself the Koïl's young, Linked with such winning sweetness are The notes he pours irregular. See, round the blooming Mango clings That creeper with her tender rings, So in thy love, when none is near, Thine arms are thrown round me, my dear.” Thus in his joy he cried; and she, Sweet speaker, on her lover's knee, Of faultless limb and perfect face, Grew closer to her lord's embrace. 375 A fine bird with a strong, sweet note, and great imitative powers.
- **Translation**: 

---

### Verse 12 (Ramayana 0.737)
- **Original**: Canto XCVI. The Magic Shaft. 719 Reclining in her husband's arms, A goddess in her wealth of charms, She filled his loving breast anew With mighty joy that thrilled him through. His finger on the rock he laid, Which veins of sanguine ore displayed, And painted o'er his darling's eyes The holy sign in mineral dyes. Bright on her brow the metal lay Like the young sun's first gleaming ray, And showed her in her beauty fair As the soft light of morning's air. Then from the Ke[ar's laden tree He picked fair blossoms in his glee, And as he decked each lovely tress, His heart o'erflowed with happiness. So resting on that rocky seat A while they spent in pastime sweet, Then onward neath the shady boughs Went Ráma with his Maithil spouse. She roaming in the forest shade Where every kind of creature strayed Observed a monkey wandering near, And clung to Ráma's arm in fear. The hero Ráma fondly laced His mighty arms around her waist, Consoled his beauty in her dread, And scared the Monkey till he fled. That holy mark of sanguine ore That gleamed on Sítá's brow before, Shone by that close embrace impressed Upon the hero's ample chest. Then Sítá, when the beast who led The monkey troop, afar had fled,
- **Translation**: 

---

### Verse 13 (Ramayana 0.738)
- **Original**: 720 The Ramayana Laughed loudly in light-hearted glee That mark on Ráma's chest to see. A clump of bright A[okas fired The forest in their bloom attired: The restless blossoms as they gleamed A host of threatening monkeys seemed. Then Sítá thus to Ráma cried, As longingly the flowers she eyed: “Pride of thy race, now let us go Where those A[oka blossoms grow.” He on his darling's pleasure bent With his fair goddess thither went And roamed delighted through the wood Where blossoming A[okas stood, As Ziva with Queen Umá roves Through Himaván's majestic groves. Bright with purpureal glow the pair Of happy lovers sported there, And each upon the other set A flower-inwoven coronet. There many a crown and chain they wove Of blooms from that A[oka grove, And in their graceful sport the two Fresh beauty o'er the mountain threw. The lover let his love survey Each pleasant spot that round them lay, Then turned they to their green retreat Where all was garnished, gay, and neat. By brotherly affection led, Sumitrá's son to meet them sped, And showed the labours of the day Done while his brother was away. There lay ten black-deer duly slain With arrows pure of poison stain,
- **Translation**: 

---

### Verse 14 (Ramayana 0.739)
- **Original**: Canto XCVI. The Magic Shaft. 721 Piled in a mighty heap to dry, With many another carcass nigh. And Lakshma G's brother saw, o'erjoyed, The work that had his hands employed, Then to his consort thus he cried: “Now be the general gifts supplied.” Then Sítá, fairest beauty, placed The food for living things to taste, And set before the brothers meat And honey that the pair might eat. They ate the meal her hands supplied, Their lips with water purified: Then Janak's daughter sat at last And duly made her own repast. The other venison, to be dried, Piled up in heaps was set aside, And Ráma told his wife to stay And drive the flocking crows away. Her husband saw her much distressed By one more bold than all the rest, Whose wings where'er he chose could fly, Now pierce the earth, now roam the sky. Then Ráma laughed to see her stirred To anger by the plaguing bird: Proud of his love the beauteous dame With burning rage was all aflame. Now here, now there, again, again She chased the crow, but all in vain, Enraging her, so quick to strike [206] With beak and wing and claw alike: Then how the proud lip quivered, how The dark frown marked her angry brow! When Ráma saw her cheek aglow With passion, he rebuked the crow.
- **Translation**: 

---

### Verse 15 (Ramayana 0.740)
- **Original**: 722 The Ramayana But bold in impudence the bird, With no respect for Ráma's word, Fearless again at Sítá flew: Then Ráma's wrath to fury grew. The hero of the mighty arm Spoke o'er a shaft the mystic charm, Laid the dire weapon on his bow And launched it at the shameless crow. The bird, empowered by Gods to spring Through earth itself on rapid wing, Through the three worlds in terror fled Still followed by that arrow dread. Where'er he flew, now here now there, A cloud of weapons filled the air. Back to the high-souled prince he fled And bent at Ráma's feet his head, And then, as Sítá looked, began His speech in accents of a man: “O pardon, and for pity's sake Spare, Ráma, spare my life to take! Where'er I turn, where'er I flee, No shelter from this shaft I see.” The chieftain heard the crow entreat Helpless and prostrate at his feet, And while soft pity moved his breast, With wisest speech the bird addressed: “I took the troubled Sítá's part, And furious anger filled my heart. Then on the string my arrow lay Charmed with a spell thy life to slay. Thou seekest now my feet, to crave Forgiveness and thy life to save. So shall thy prayer have due respect:
- **Translation**: 

---

### Verse 16 (Ramayana 0.741)
- **Original**: Canto XCVII. Lakshman's Anger. 723 The suppliant I must still protect. But ne'er in vain this dart may flee; Yield for thy life a part of thee, What portion of thy body, say, Shall this mine arrow rend away? Thus far, O bird, thus far alone On thee my pity may be shown. Forfeit a part thy life to buy: 'Tis better so to live than die.” Thus Ráma spoke: the bird of air Pondered his speech with anxious care, And wisely deemed it good to give One of his eyes that he might live. To Raghu's son he made reply: “O Ráma, I will yield an eye. So let me in thy grace confide And live hereafter single-eyed.” Then Ráma charged the shaft, and lo, Full in the eye it smote the crow. And the Videhan lady gazed Upon the ruined eye amazed. The crow to Ráma humbly bent, Then where his fancy led he went. Ráma with LakshmaG by his side With needful work was occupied. Canto XCVII. Lakshman's Anger.
- **Translation**: 

---

### Verse 17 (Ramayana 0.742)
- **Original**: 724 The Ramayana Thus Ráma showed his love the rill Whose waters ran beneath the hill, Then resting on his mountain seat Refreshed her with the choicest meat. So there reposed the happy two: Then Bharat's army nearer drew: Rose to the skies a dusty cloud, The sound of trampling feet was loud. The swelling roar of marching men Drove the roused tiger from his den, And scared amain the serpent race Flying to hole and hiding-place. The herds of deer in terror fled, The air was filled with birds o'erhead, The bear began to leave his tree, The monkey to the cave to flee. Wild elephants were all amazed As though the wood around them blazed. The lion oped his ponderous jaw, The buffalo looked round in awe. The prince, who heard the deafening sound, And saw the silvan creatures round Fly wildly startled from their rest, The glorious LakshmaG thus addressed: “Sumitrá's noble son most dear, Hark, LakshmaG, what a roar I hear, The tumult of a coming crowd, Appalling, deafening, deep, and loud! The din that yet more fearful grows Scares elephants and buffaloes, Or frightened by the lions, deer Are flying through the wood in fear. I fain would know who seeks this place Comes prince or monarch for the chase?
- **Translation**: 

---

### Verse 18 (Ramayana 0.743)
- **Original**: Canto XCVII. Lakshman's Anger. 725 Or does some mighty beast of prey Frighten the silvan herds away? 'Tis hard to reach this mountain height, Yea, e'en for birds in airy flight. Then fain, O LakshmaG, would I know What cause disturbs the forest so.” Lakshma G in haste, the wood to view, Climbed a high Sál that near him grew, The forest all around he eyed, First gazing on the eastern side. Then northward when his eyes he bent He saw a mighty armament Of elephants, and cars, and horse, And men on foot, a mingled force, And banners waving in the breeze, And spoke to Ráma words like these: “Quick, quick, my lord, put out the fire, Let Sítá to the cave retire. [207] Thy coat of mail around thee throw, Prepare thine arrows and thy bow.” In eager haste thus LakshmaG cried, And Ráma, lion lord, replied: “Still closer be the army scanned, And say who leads the warlike band.” Lakshma G his answer thus returned, As furious rage within him burned, Exciting him like kindled fire To scorch the army in his ire: “'Tis Bharat: he has made the throne By consecrating rites his own: To gain the whole dominion thus He comes in arms to slaughter us.
- **Translation**: 

---

### Verse 19 (Ramayana 0.744)
- **Original**: 726 The Ramayana I mark tree-high upon his car His flagstaff of the Kovidár,376 I see his glittering banner glance, I see his chivalry advance: I see his eager warriors shine On elephants in lengthened line. Now grasp we each the shafts and bow, And higher up the mountain go. Or in this place, O hero, stand With weapons in each ready hand. Perhaps beneath our might may fall This leader of the standard tall, And Bharat I this day may see Who brought this mighty woe on thee, Sítá, and me, who drove away My brother from the royal sway. Bharat our foe at length is nigh, And by this hand shall surely die: Brother, I see no sin at all If Bharat by my weapon fall. No fault is his who slays the foe Whose hand was first to strike the blow: With Bharat now the crime begins Who against thee and duty sins. The queen athirst for royal sway Will see her darling son to-day Fall by this hand, like some fair tree Struck by an elephant, slain by me. Kaikeyí's self shall perish too With kith and kin and retinue, And earth by my avenging deed Shall from this mass of sin be freed. 376 Bauhinea variegata, a species of ebony.
- **Translation**: 

---

### Verse 20 (Ramayana 0.745)
- **Original**: Canto XCVIII. Lakshman Calmed. 727 This day my wrath, too long restrained, Shall fall upon the foe, unchained, Mad as the kindled flame that speeds Destroying through the grass and reeds. This day mine arrows keen and fierce The bodies of the foe shall pierce: The woods on Chitrakúma's side Shall run with torrents crimson-dyed. The wandering beasts of prey shall feed On heart-cleft elephant and steed, And drag to mountain caves away The bodies that my arrows slay. Doubt not that Bharat and his train Shall in this mighty wood be slain: So shall I pay the debt my bow And these my deadly arrows owe.” Canto XCVIII. Lakshman Calmed. Then Ráma nobly calm allayed The wrath that LakshmaG's bosom swayed: “What need have we the sword to wield, To bend the bow or lift the shield, If Bharat brave, and wise, and good, Himself has sought this sheltering wood? I sware my father's will to do, And if I now my brother slew What gain in kingship should I find, Despised and scorned by all mankind? Believe me, e'en as I would shrink From poisoned meat or deadly drink,
- **Translation**: 

---



--- End of Ramayan_batch_135.md ---


--- Start of Ramayan_batch_136.md ---

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

### Verse 1 (Ramayana 0.746)
- **Original**: 728 The Ramayana No power or treasure would I win By fall of friend or kith or kin. Brother, believe the words I speak: For your dear sakes alone I seek Duty and pleasure, wealth and gain: A holy life, a happy reign. If royal sway my heart desires, My brothers' weal the wish inspires: Their bliss and safety is my care, By this uplifted bow I swear. 'Twere not so hard for me to gain This broad land girdled by the main, But even Indra's royal might Should ne'er be mine in duty's spite. If any bliss my soul can see Deprived of dearZatrughna, thee, And Bharat, may the flame destroy With ashy gloom the selfish joy. Far dearer than this life of mine, Knowing the custom of our line, His heart with fond affection fraught, Bharat Ayodhyá's town resought And hearing when he came that I, With thee and Sítá, forced to fly With matted hair and hermit dress Am wandering in the wilderness. While grief his troubled senses storms, And tender love his bosom warms, From every thought of evil clear, Is come to meet his brother here. Some grievous words perchance he spoke Kaikeyí's anger to provoke, Then won the king, and comes to lay Before my feet the royal sway.
- **Translation**: 

---

### Verse 2 (Ramayana 0.747)
- **Original**: Canto XCVIII. Lakshman Calmed. 729 Hither, methinks, in season due Comes Bharat for an interview, Nor in his secret heart has he One evil thought 'gainst thee or me. What has he done ere now, reflect! How failed in love or due respect [208] To make thee doubt his faith and lay This evil to his charge to-day? Thou shouldst not join with Bharat's name So harsh a speech and idle blame. The blows thy tongue at Bharat deals, My sympathizing bosom feels. How, urged by stress of any ill, Should sons their father's life-blood spill, Or brother slay in impious strife A brother dearer than his life? If thou these cruel words hast said By strong desire of empire led, My brother Bharat will I pray To give to thee the kingly sway. “Give him the realm,” my speech shall be, And Bharat will, methinks, agree.” Thus spoke the prince whose chief delight Was duty, and to aid the right: And Lakshma G keenly felt the blame, And shrank within himself for shame: And then his answer thus returned, With downcast eye and cheek that burned: “Brother, I ween, to see thy face Our sire himself has sought this place.” Thus LakshmaG spoke and stood ashamed, And Ráma saw and thus exclaimed: “It is the strong-armed monarch: he
- **Translation**: 

---

### Verse 3 (Ramayana 0.748)
- **Original**: 730 The Ramayana Is come, methinks, his sons to see, To bid us both the forest quit For joys for which he deems us fit: He thinks on all our care and pain, And now would lead us home again. My glorious father hence will bear Sítá who claims all tender care. I see two coursers fleet as storms, Of noble breed and lovely forms. I see the beast of mountain size Who bears the king our father wise, The aged Victor, march this way In front of all the armed array. But doubt and fear within me rise, For when I look with eager eyes I see no white umbrella spread, World-famous, o'er the royal head. Now, LakshmaG, from the tree descend, And to my words attention lend.” Thus spoke the pious prince: and he Descended from the lofty tree, And reverent hand to hand applied, Stood humbly by his brother's side. The host, compelled by Bharat's care, The wood from trampling feet to spare, Dense crowding half a league each way Encamped around the mountain lay. Below the tall hill's shelving side Gleamed the bright army far and wide Spread o'er the ample space, By Bharat led who firmly true In duty from his bosom threw
- **Translation**: 

---

### Verse 4 (Ramayana 0.749)
- **Original**: Canto XCIX. Bharat's Approach. 731 All pride, and near his brother drew To win the hero's grace. Canto XCIX. Bharat's Approach. Soon as the warriors took their rest Obeying Bharat's high behest, Thus Bharat toZatrughna spake: “A band of soldiers with thee take, And with these hunters o'er and o'er The thickets of the wood explore. With bow, sword, arrows in their hands Let Guha with his kindred bands Within this grove remaining trace The children of Kakutstha's race. And I meanwhile on foot will through This neighbouring wood my way pursue, With elders and the twice-born men, And every lord and citizen. There is, I feel, no rest for me Till Ráma's face again I see, Lakshma G, in arms and glory great, And Sítá born to happy fate: No rest, until his cheek as bright As the fair moon rejoice my sight, No rest until I see the eye With which the lotus petals vie; Till on my head those dear feet rest With signs of royal rank impressed; None, till my kingly brother gain His old hereditary reign,
- **Translation**: 

---

### Verse 5 (Ramayana 0.750)
- **Original**: 732 The Ramayana Till o'er his limbs and noble head The consecrating drops be shed. How blest is Janak's daughter, true To every wifely duty, who Cleaves faithful to her husband's side Whose realm is girt by Ocean's tide! This mountain too above the rest E'en as the King of Hills is blest,— Whose shades Kakutstha's scion hold As Nandan charms the Lord of Gold. Yea, happy is this tangled grove Where savage beasts unnumbered rove, Where, glory of the Warrior race, King Ráma finds a dwelling-place.” Thus Bharat, strong-armed hero spake, And walked within the pathless brake. O'er plains where gay trees bloomed he went, Through boughs in tangled net-work bent, And then from Ráma's cot appeared The banner which the flame upreared. And Bharat joyed with every friend To mark those smoky wreaths ascend: “Here Ráma dwells,” he thought;“at last The ocean of our toil is passed.” Then sure that Ráma's hermit cot Was on the mountain's side He stayed his army on the spot, And on with Guha hied. [209]
- **Translation**: 

---

### Verse 6 (Ramayana 0.751)
- **Original**: Canto C. The Meeting. 733 Canto C. The Meeting. Then Bharat toZatrughna showed The spot, and eager onward strode, First bidding Saint Va[ishmha bring The widowed consorts of the king. As by fraternal love impelled His onward course the hero held, Sumantra followed close behind Zatrughna with an anxious mind: Not Bharat's self more fain could be To look on Ráma's face than he. As, speeding on, the spot he neared, Amid the hermits' homes appeared His brother's cot with leaves o'erspread, And by its side a lowly shed. Before the shed great heaps were left Of gathered flowers and billets cleft, And on the trees hung grass and bark Ráma and LakshmaG's path to mark: And heaps of fuel to provide Against the cold stood ready dried. The long-armed chief, as on he went In glory's light preëminent, With joyous words like these addressed The braveZatrughna and the rest: “This is the place, I little doubt, Which Bharadvája pointed out, Not far from where we stand must be The woodland stream, Mandákiní. Here on the mountain's woody side Roam elephants in tusked pride, And ever with a roar and cry Each other, as they meet, defy.
- **Translation**: 

---

### Verse 7 (Ramayana 0.752)
- **Original**: 734 The Ramayana And see those smoke-wreaths thick and dark: The presence of the flame they mark, Which hermits in the forest strive By every art to keep alive. O happy me! my task is done, And I shall look on Raghu's son, Like some great saint, who loves to treat His elders with all reverence meet.” Thus Bharat reached that forest rill, Thus roamed on Chitrakúma's hill; Then pity in his breast awoke, And to his friends the hero spoke: “Woe, woe upon my life and birth! The prince of men, the lord of earth Has sought the lonely wood to dwell Sequestered in a hermit's cell. Through me, through me these sorrows fall On him the splendid lord of all: Through me resigning earthly bliss He hides him in a home like this. Now will I, by the world abhorred, Fall at the dear feet of my lord, And at fair Sítá's too, to win His pardon for my heinous sin.” As thus he sadly mourned and sighed, The son of Da[aratha spied A bower of leafy branches made, Sacred and lovely in the shade, Of fair proportions large and tall, Well roofed with boughs of palm, and Sál, Arranged in order due o'erhead Like grass upon an altar spread.
- **Translation**: 

---

### Verse 8 (Ramayana 0.753)
- **Original**: Canto C. The Meeting. 735 Two glorious bows were gleaming there, Like Indra's377 in the rainy air, Terror of foemen, backed with gold, Meet for the mightiest hand to hold: And quivered arrows cast a blaze Bright gleaming like the Day-God's rays: Thus serpents with their eyes aglow Adorn their capital below.378 Great swords adorned the cottage, laid Each in a case of gold brocade; There hung the trusty shields, whereon With purest gold the bosses shone. The brace to bind the bowman's arm, The glove to shield his hand from harm, A lustre to the cottage lent From many a golden ornament: Safe was the cot from fear of men As from wild beasts the lion's den. The fire upon the altar burned, That to the north and east was turned. Bharat his eager glances bent And gazed within the cot intent; In deerskin dress, with matted hair, Ráma his chief was sitting there: With lion-shoulders broad and strong, With lotus eyes, arms thick and long. The righteous sovereign, who should be Lord paramount from sea to sea, High-minded, born to lofty fate, Like Brahmá's self supremely great; With LakshmaG by his side, and her, Fair Sítá, for his minister. 377 The rainbow is called the bow of Indra. 378 Bhogavatí, the abode of the Nágas or Serpent race.
- **Translation**: 

---

### Verse 9 (Ramayana 0.754)
- **Original**: 736 The Ramayana And Bharat gazing, overcome By sorrow for a while was dumb, Then, yielding to his woe, he ran To Ráma and with sobs began: “He who a royal seat should fill With subjects round to do his will, My elder brother,— see him here, With silvan creatures waiting near. The high-souled hero, wont to wear The costliest robes exceeding fair, Now banished, in a deerskin dress, Here keeps the path of righteousness. How brooks the son of Raghu now The matted locks which load his brow, Around whose princely head were twined Sweet blossoms of the rarest kind? The prince whose merits grew, acquired[210] By rites performed as he desired, Would now a store of merit gain Bought by his body's toil and pain. Those limbs to which pure sandal lent The freshness of its fragrant scent, Exposed to sun, and dust, and rain, Are now defiled with many a stain. And I the wretched cause why this Falls on the prince whose right is bliss! Ah me, that ever I was born To be the people's hate and scorn!” Thus Bharat cried: of anguish sprung, Great drops upon his forehead hung. He fell o'erpowered— his grief was such— Ere he his brother's feet could touch. As on the glorious prince he gazed
- **Translation**: 

---

### Verse 10 (Ramayana 0.755)
- **Original**: Canto CI. Bharata Questioned. 737 In vain his broken voice he raised: “Dear lord”— through tears and sobbing came, The only words his lips could frame. And braveZatrughna wept aloud, As low at Ráma's feet he bowed. Then Ráma, while his tears ran fast, His arms around his brothers cast. Guha, Sumantra came to meet The princes in their wild retreat. Vrihaspati andZukra bright Their greeting thus rejoice to pay To the dear Lord who brings the night, And the great God who rules the day. Then wept the dwellers of the shade, Whose eyes the princes, meet to ride On mighty elephants, surveyed; And cast all thought of joy aside. Canto CI. Bharata Questioned. Then Ráma gazed, and scarcely knew Bharat so worn and changed in hue. He raised him, kissed him on the head, Embraced him, and thus kindly said: “Where was thy father, brother dear, That thou art come to seek me here? Unmeet, if he be living yet, Thy feet within the wood to set. I pray thee now the cause declare Why thou hast left the kingdom there, With matted locks and deerskin dress To roam the distant wilderness.”
- **Translation**: 

---

### Verse 11 (Ramayana 0.756)
- **Original**: 738 The Ramayana Thus questioned by the prince, at length Kaikeyí's son regained his strength, And hand to hand in reverence laid, To Ráma thus his answer made: “The great-armed monarch, O my lord, Has dared to do a thing abhorred, Left us, and grieving for his son, A home among the Gods has won. My mother Queen Kaikeyí gave The order to the king her slave, And at the bidding of the dame He wrought the sin which mars his fame. Athirst for sway, her hopes are crossed, She mourns her son, her husband lost, And through her impious crime will go For punishment to hell below. Now O my lord, forgive me all; Be gracious to thy lowly thrall: Anointed king, accept to-day Like Indra's self, the royal sway. Be gracious, Prince, to lord and peer, And widowed queens who seek thee here Accept the kingdom thine by right, And so thy faithful friends delight. Let the broad land no longer be All widowed and forlorn of thee: Let the full moon of autumn reign Triumphant o'er the night again. These lords and I before thee bend: O Ráma, to our prayer attend. O do not thou this grace deny: Thy brother, pupil, slave am I. Look on this venerable ring, Advisers of our sire the king,
- **Translation**: 

---

### Verse 12 (Ramayana 0.757)
- **Original**: Canto CI. Bharata Questioned. 739 From age to age so honoured: thou Shouldst grant their supplication now.” As weeping thus the hero prayed, His head at Ráma's feet he laid. Like a mad elephant he sighed: And Ráma gazed and thus replied: “How, brother, can a man of worth, True to his vows, of noble birth— A man like me, commit a sin The lordship of the land to win? No slightest shade of fault I see, O tamer of thy foes, in thee. But ne'er shouldst thou in childish thought The queen thy mother blame in aught. O brother wise and sinless, know The sacred laws would have it so, That from good wife and son require Obedience to their lord and sire. And we are all the king's, for thus The virtuous ever reckon us: Yea brother, be it known to thee, His wives, and sons, and pupils we. His is the right, if he deem fit, To bid me, throned as monarch, sit, Or in a coat of bark expel, And deerskin, in the wood to dwell. And O remember, best of all Who act as claims of duty call, As to a virtuous sire is due, Such honour claims a mother too. So they whose lives have ever been By duty led, the king and queen, Said,“Ráma, seek the forest shade:”
- **Translation**: 

---

### Verse 13 (Ramayana 0.758)
- **Original**: 740 The Ramayana And I (what could I else?) obeyed. Thou must the royal power retain,[211] And o'er the famed Ayodhyá reign: I dressed in bark my days will spend Where DaG ak's forest wilds extend. So Da[aratha spoke, our king, His share to each apportioning Before his honoured servants' eyes: Then, heir of bliss, he sought the skies. The righteous monarch's honoured will, Whom all revered, must guide thee still, And thou must still enjoy the share Assigned thee by our father's care. So I till twice seven years are spent Will roam this wood in banishment, Contented with the lot which he, My high-souled sire, has given me. The charge the monarch gave, endeared To all mankind, by all revered, Peer of the Lord Supreme, Far better, richer far in gain Of every blessing than to reign O'er all the worlds I deem.” Canto CII. Bharat's Tidings. He spoke: and Bharat thus replied: “If, false to every claim beside, I ne'er in kingly duties fail, What will my royal life avail? Still should the custom be observed,
- **Translation**: 

---

### Verse 14 (Ramayana 0.759)
- **Original**: Canto CIII. The Funeral Libation. 741 From which our line has never swerved, Which to the younger son ne'er gives The kingdom while the elder lives. Now to Ayodhyá rich and fair With me, O Raghu's son, repair, And to protect and gladden all Our house, thyself as king install. A king the world's opinion deems A man: to me a God he seems, Whose life in virtuous thoughts and deeds The lives of other men exceeds. When I in distant Kekaya stayed, And thou hadst sought the forest shade, Our father died, the saints' delight, So constant in each holy rite. Scarce with thy wife and LakshmaG thou Hadst journeyed forth to keep the vow, When mourning for his son, forspent, To heavenly rest the monarch went. Then up, O lord of men, away! His funeral rites of water pay: I andZatrughna, ere we came, Neglected not the sacred claim. But in the spirit-world, they say, That gift alone is fresh for aye Which best beloved hands have poured; And thou his dearest art, my lord. For thee he longed, for thee he grieved, His every thought on thee was bent, And crushed by woe, of thee bereaved, He thought of thee as hence he went.”
- **Translation**: 

---

### Verse 15 (Ramayana 0.760)
- **Original**: 742 The Ramayana Canto CIII. The Funeral Libation. When Ráma heard from Bharat each Dark sorrow of his mournful speech, And tidings of his father dead, His spirits fell, his senses fled. For the sad words his brother spoke Struck on him like a thunder stroke, Fierce as the bolt which Indra throws, The victor of his Daitya foes. Raising his arms in anguish, he, As when the woodman hews a tree With its fair flowery branches crowned, Fainted and fell upon the ground. Lord of the earth to earth he sank, Helpless, as when a towering bank With sudden ruin buries deep An elephant who lay asleep. Then swift his wife and brothers flew, And water, weeping, o'er him threw. As slowly sense and strength he gained, Fast from his eyes the tears he rained, And then in accents sad and weak Kakutstha's son began to speak, And mourning for the monarch dead, With righteous words to Bharat said: “What calls me home, when he, alas, Has gone the way which all must pass? Of him, the best of kings bereft What guardian has Ayodhyá left? How may I please his spirit? how Delight the high-souled monarch now, Who wept for me and went above By me ungraced with mourning love?
- **Translation**: 

---

### Verse 16 (Ramayana 0.761)
- **Original**: Canto CIII. The Funeral Libation. 743 Ah, happy brothers! you have paid Due offerings to his parting shade. E'en when my banishment is o'er, Back to my home I go no more, To look upon the widowed state Reft of her king, disconsolate. E'en then, O tamer of the foe, If to Ayodhyá's town I go, Who will direct me as of old, Now other worlds our father hold? From whom, my brother, shall I hear Those words which ever charmed mine ear And filled my bosom with delight Whene'er he saw me act aright?” Thus Ráma spoke: then nearer came And looking on his moonbright dame, “Sítá, the king is gone,” he said: “And Lakshma G, know thy sire is dead, [212] And with the Gods on high enrolled: This mournful news has Bharat told.” He spoke: the noble youths with sighs Rained down the torrents from their eyes. And then the brothers of the chief With words of comfort soothed his grief: “Now to the king our sire who swayed The earth be due libations paid.” Soon as the monarch's fate she knew, Sharp pangs of grief smote Sítá through: Nor could she look upon her lord With eyes from which the torrents poured. And Ráma strove with tender care To soothe the weeping dame's despair, And then, with piercing woe distressed,
- **Translation**: 

---

### Verse 17 (Ramayana 0.762)
- **Original**: 744 The Ramayana The mournful LakshmaG thus addressed: “Brother, I pray thee bring for me The pressed fruit of the Ingudí, And a bark mantle fresh and new, That I may pay this offering due. First of the three shall Sítá go, Next thou, and I the last: for so Moves the funereal pomp of woe.”379 Sumantra of the noble mind, Gentle and modest, meek and kind, Who, follower of each princely youth, To Ráma clung with constant truth, Now with the royal brothers' aid The grief of Ráma soothed and stayed, And lent his arm his lord to guide Down to the river's holy side. That lovely stream the heroes found, With woods that ever blossomed crowned, And there in bitter sorrow bent Their footsteps down the fair descent. Then where the stream that swiftly flowed A pure pellucid shallow showed, The funeral drops they duly shed, And “Father, this be thine,” they said. But he, the lord who ruled the land, Filled from the stream his hollowed hand, And turning to the southern side Stretched out his arm and weeping cried: “This sacred water clear and pure, 379 “The order of the procession on these occasions is that the children pre- cede according to age, then the women and after that the men according to age, the youngest first and the eldest last: when they descend into the water this is reversed and resumed when they come out of it.” C AREY AND M ARSHMAN .{FNS
- **Translation**: 

---

### Verse 18 (Ramayana 0.763)
- **Original**: Canto CIII. The Funeral Libation. 745 An offering which shall aye endure To thee, O lord of kings, I give: Accept it where the spirits live!” Then, when the solemn rite was o'er, Came Ráma to the river shore, And offered, with his brothers' aid, Fresh tribute to his father's shade. With jujube fruit he mixed the seed Of Ingudís from moisture freed, And placed it on a spot o'erspread With sacred grass, and weeping said: “Enjoy, great King, the cake which we Thy children eat and offer thee! For ne'er do blessed Gods refuse To share the food which mortals use.” Then Ráma turned him to retrace The path that brought him to the place, And up the mountain's pleasant side Where lovely lawns lay fair, he hied. Soon as his cottage door he gained His brothers to his breast he strained. From them and Sítá in their woes So loud the cry of weeping rose, That like the roar of lions round The mountain rolled the echoing sound. And Bharat's army shook with fear The weeping of the chiefs to hear. “Bharat,” the soldiers cried,“'tis plain, His brother Ráma meets again, And with these cries that round us ring They sorrow for their sire the king.” Then leaving car and wain behind,
- **Translation**: 

---

### Verse 19 (Ramayana 0.764)
- **Original**: 746 The Ramayana One eager thought in every mind, Swift toward the weeping, every man, As each could find a passage, ran. Some thither bent their eager course With car, and elephant, and horse, And youthful captains on their feet With longing sped their lord to meet, As though the new-come prince had been An exile for long years unseen. Earth beaten in their frantic zeal By clattering hoof and rumbling wheel, Sent forth a deafening noise as loud As heaven when black with many a cloud. Then, with their consorts gathered near, Wild elephants in sudden fear Rushed to a distant wood, and shed An odour round them as they fled. And every silvan thing that dwelt Within those shades the terror felt, Deer, lion, tiger, boar and roe, Bison, wild-cow, and buffalo. And when the tumult wild they heard, With trembling pinions flew each bird, From tree, from thicket, and from lake, Swan, koïl, curlew, crane, and drake. With men the ground was overspread, With startled birds the sky o'erhead. Then on his sacrificial ground The sinless, glorious chief was found. Loading with curses deep and loud The hump-back and the queen, the crowd Whose cheeks were wet, whose eyes were dim, In fond affection ran to him. While the big tears their eyes bedewed,
- **Translation**: 

---

### Verse 20 (Ramayana 0.765)
- **Original**: Canto CIV. The Meeting With The Queens. 747 He looked upon the multitude, [213] And then as sire and mother do, His arms about his loved ones threw. Some to his feet with reverence pressed, Some in his arms he strained: Each friend, with kindly words addressed, Due share of honour gained. Then, by their mighty woe o'ercome, The weeping heroes' cry Filled, like the roar of many a drum, Hill, cavern, earth, and sky. Canto CIV. The Meeting With The Queens. Va [ishmha with his soul athirst To look again on Ráma, first In line the royal widows placed, And then the way behind them traced. The ladies moving, faint and slow, Saw the fair stream before them flow, And by the bank their steps were led Which the two brothers visited. Kau [alyá with her faded cheek And weeping eyes began to speak, And thus in mournful tones addressed The queen Sumitrá and the rest: “See in the wood the bank's descent, Which the two orphan youths frequent, Whose noble spirits never fall, Though woes surround them, reft of all. Thy son with love that never tires
- **Translation**: 

---



--- End of Ramayan_batch_136.md ---


--- Start of Ramayan_batch_137.md ---

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

### Verse 1 (Ramayana 0.766)
- **Original**: 748 The Ramayana Draws water hence which mine requires. This day, for lowly toil unfit, His pious task thy son should quit.” As on the long-eyed lady strayed, On holy grass, whose points were laid Directed to the southern sky, The funeral offering met her eye. When Ráma's humble gift she spied Thus to the queens Kau[alyá cried: “The gift of Ráma's hand behold, His tribute to the king high-souled, Offered to him, as texts require, Lord of Ikshváku's line, his sire! Not such I deem the funeral food Of kings with godlike might endued. Can he who knew all pleasures, he Who ruled the earth from sea to sea, The mighty lord of monarchs, feed On Ingudí's extracted seed? In all the world there cannot be A woe, I ween, more sad to see, Than that my glorious son should make His funeral gift of such a cake. The ancient text I oft have heard This day is true in every word: “Ne'er do the blessed Gods refuse To eat the food their children use.’ ” The ladies soothed the weeping dame: To Ráma's hermitage they came, And there the hero met their eyes Like a God fallen from the skies. Him joyless, reft of all, they viewed,
- **Translation**: 

---

### Verse 2 (Ramayana 0.767)
- **Original**: Canto CIV. The Meeting With The Queens. 749 And tears their mournful eyes bedewed. The truthful hero left his seat, And clasped the ladies' lotus feet, And they with soft hands brushed away The dust that on his shoulders lay. Then LakshmaG, when he saw each queen With weeping eyes and troubled mien, Near to the royal ladies drew And paid them gentle reverence too. He, Da[aratha's offspring, signed The heir of bliss by Fortune kind, Received from every dame no less Each mark of love and tenderness. And Sítá came and bent before The widows, while her eyes ran o'er, And pressed their feet with many a tear. They when they saw the lady dear Pale, worn with dwelling in the wild, Embraced her as a darling child: “Daughter of royal Janak, bride Of Da[aratha's son,” they cried, “How couldst thou, offspring of a king, Endure this woe and suffering In the wild forest? When I trace Each sign of trouble on thy face— That lotus which the sun has dried, That lily by the tempest tried, That gold whereon the dust is spread, That moon whence all the light is fled— Sorrow assails my heart, alas! As fire consumes the wood and grass.” Then Ráma, as she spoke distressed, The feet of Saint Va[ishmha pressed,
- **Translation**: 

---

### Verse 3 (Ramayana 0.768)
- **Original**: 750 The Ramayana Touched them with reverential love, Then near him took his seat: Thus Indra clasps in realms above The Heavenly Teacher's380 feet. Then with each counsellor and peer, Bharat of duteous mind, With citizens and captains near, Sat humbly down behind. When with his hands to him upraised, In devotee's attire, Bharat upon his brother gazed Whose glory shone like fire, As when the pure Mahendra bends To the great Lord of Life, Among his noble crowd of friends This anxious thought was rife: “What words to Raghu's son to-day Will royal Bharat speak, Whose heart has been so prompt to pay Obeisance fond and meek?” Then steadfast Ráma, LakshmaG wise, Bharat for truth renowned,[214] Shone like three fires that heavenward rise With holy priests around. Canto CV. Ráma's Speech. 380 V [ihaspati, the preceptor of the Gods.
- **Translation**: 

---

### Verse 4 (Ramayana 0.769)
- **Original**: Canto CV. Ráma's Speech. 751 A while they sat, each lip compressed, Then Bharat thus his chief addressed: “My mother here was made content; To me was given the government. This now, my lord, I yield to thee: Enjoy it, from all trouble free. Like a great bridge the floods have rent, Impetuous in their wild descent, All other hands but thine in vain Would strive the burthen to maintain. In vain the ass with steeds would vie, With Tárkshya,381 birds that wing the sky; So, lord of men, my power is slight To rival thine imperial might. Great joys his happy days attend On whom the hopes of men depend, But wretched is the life he leads Who still the aid of others needs. And if the seed a man has sown, With care and kindly nurture grown, Rear its huge trunk and spring in time Too bulky for a dwarf to climb, Yet, with perpetual blossom gay, No fruit upon its boughs display, Ne'er can that tree, thus nursed in vain, Approval of the virtuous gain. The simile is meant to be Applied, O mighty-armed, to thee, Because, our lord and leader, thou Protectest not thy people now. O, be the longing wish fulfilled Of every chief of house and guild, 381 Garu , the king of birds.
- **Translation**: 

---

### Verse 5 (Ramayana 0.770)
- **Original**: 752 The Ramayana To see again their sun-bright lord Victorious to his realm restored! As thou returnest through the crowd Let roars of elephants be loud. And each fair woman lift her voice And in her new-found king rejoice.” The people all with longing moved, The words that Bharat spoke approved, And crowding near to Ráma pressed The hero with the same request. The steadfast Ráma, when he viewed His glorious brother's mournful mood, With each ambitious thought controlled, Thus the lamenting prince consoled: “I cannot do the things I will, For Ráma is but mortal still. Fate with supreme, resistless law This way and that its slave will draw, All gathered heaps must waste away, All lofty lore and powers decay. Death is the end of life, and all, Now firmly joined, apart must fall. One fear the ripened fruit must know, To fall upon the earth below; So every man who draws his breath Must fear inevitable death. The pillared mansion, high, compact, Must fall by Time's strong hand attacked; So mortal men, the gradual prey Of old and ruthless death, decay. The night that flies no more returns: Yamuná for the Ocean yearns: Swift her impetuous waters flee,
- **Translation**: 

---

### Verse 6 (Ramayana 0.771)
- **Original**: Canto CV. Ráma's Speech. 753 But roll not backward from the sea. The days and nights pass swiftly by And steal our moments as they fly, E'en as the sun's unpitying rays Drink up the floods in summer blaze. Then for thyself lament and leave For death of other men to grieve, For if thou go or if thou stay, Thy life is shorter day by day. Death travels with us; death attends Our steps until our journey ends, Death, when the traveller wins the goal, Returns with the returning soul. The flowing hair grows white and thin, And wrinkles mark the altered skin. The ills of age man's strength assail: Ah, what can mortal power avail? Men joy to see the sun arise, They watch him set with joyful eyes: But ne'er reflect, too blind to see, How fast their own brief moments flee. With lovely change for ever new The seasons' sweet return they view, Nor think with heedless hearts the while That lives decay as seasons smile. As haply on the boundless main Meet drifting logs and part again, So wives and children, friends and gold, Ours for a little time we hold: Soon by resistless laws of fate To meet no more we separate. In all this changing world not one The common lot of all can shun: Then why with useless tears deplore
- **Translation**: 

---

### Verse 7 (Ramayana 0.772)
- **Original**: 754 The Ramayana The dead whom tears can bring no more? As one might stand upon the way And to a troop of travellers say: “If ye allow it, sirs, I too Will travel on the road with you:” So why should mortal man lament When on that path his feet are bent Which all men living needs must tread, Where sire and ancestors have led? Life flies as torrents downward fall Speeding away without recall, So virtue should our thoughts engage, For bliss382 is mortals' heritage.[215] By ceaseless care and earnest zeal For servants and for people's weal, By gifts, by duty nobly done, Our glorious sire the skies has won. Our lord the king, o'er earth who reigned, A blissful home in heaven has gained By wealth in ample largess spent, And many a rite magnificent: With constant joy from first to last A long and noble life he passed, Praised by the good, no tears should dim Our eyes, O brother dear, for him. His human body, worn and tried By length of days, he cast aside, And gained the godlike bliss to stray In Brahmá's heavenly home for aye. For such the wise as we are, deep In Veda lore, should never weep. Those who are firm and ever wise 382 To be won by virtue.
- **Translation**: 

---

### Verse 8 (Ramayana 0.773)
- **Original**: Canto CVI. Bharat's Speech. 755 Spurn vain lament and idle sighs. Be self-possessed: thy grief restrain: Go, in that city dwell again. Return, O best of men, and be Obedient to our sire's decree, While I with every care fulfil Our holy father's righteous will, Observing in the lonely wood His charge approved by all the good.” Thus Ráma of the lofty mind To Bharat spoke his righteous speech, By every argument designed Obedience to his sire to teach. Canto CVI. Bharat's Speech. Good Bharat, by the river side, To virtuous Ráma's speech replied, And thus with varied lore addressed The prince, while nobles round him pressed: “In all this world whom e'er can we Find equal, scourge of foes, to thee? No ill upon thy bosom weighs, No thoughts of joy thy spirit raise. Approved art thou of sages old, To whom thy doubts are ever told. Alike in death and life, to thee The same to be and not to be. The man who such a soul can gain Can ne'er be crushed by woe or pain. Pure as the Gods, high-minded, wise,
- **Translation**: 

---

### Verse 9 (Ramayana 0.774)
- **Original**: 756 The Ramayana Concealed from thee no secret lies. Such glorious gifts are all thine own, And birth and death to thee are known, That ill can ne'er thy soul depress With all-subduing bitterness. O let my prayer, dear brother, win Thy pardon for my mother's sin. Wrought for my sake who willed it not When absent in a distant spot. Duty alone with binding chains The vengeance due to crime restrains, Or on the sinner I should lift My hand in retribution swift. Can I who know the right, and spring From Da[aratha, purest king— Can I commit a heinous crime, Abhorred by all through endless time? The aged king I dare not blame, Who died so rich in holy fame, My honoured sire, my parted lord, E'en as a present God adored. Yet who in lore of duty skilled So foul a crime has ever willed, And dared defy both gain and right To gratify a woman's spite? When death draws near, so people say, The sense of creatures dies away; And he has proved the ancient saw By acting thus in spite of law. But O my honoured lord, be kind, Dismiss the trespass from thy mind, The sin the king committed, led By haste, his consort's wrath, and dread. For he who veils his sire's offence
- **Translation**: 

---

### Verse 10 (Ramayana 0.775)
- **Original**: Canto CVI. Bharat's Speech. 757 With tender care and reverence— His sons approved by all shall live: Not so their fate who ne'er forgive. Be thou, my lord, the noble son, And the vile deed my sire has done, Abhorred by all the virtuous, ne'er Resent, lest thou the guilt too share. Preserve us, for on thee we call, Our sire, Kaikeyí, me and all Thy citizens, thy kith and kin; Preserve us and reverse the sin. To live in woods a devotee Can scarce with royal tasks agree, Nor can the hermit's matted hair Suit fitly with a ruler's care. Do not, my brother, do not still Pursue this life that suits thee ill. Mid duties of a king we count His consecration paramount, That he with ready heart and hand May keep his people and his land. What Warrior born to royal sway From certain good would turn away, A doubtful duty to pursue, That mocks him with the distant view? Thou wouldst to duty cleave, and gain The meed that follows toil and pain. In thy great task no labour spare: Rule the four castes with justest care. Mid all the four, the wise prefer The order of the householder:383 [216] Canst thou, whose thoughts to duty cleave, 383 The four religious orders, referable to different times of life are, that of the student, that of the householder, that of the anchorite, and that of the mendicant.
- **Translation**: 

---

### Verse 11 (Ramayana 0.776)
- **Original**: 758 The Ramayana The best of all the orders leave? My better thou in lore divine, My birth, my sense must yield to thine: While thou, my lord, art here to reign, How shall my hands the rule maintain? O faithful lover of the right, Take with thy friends the royal might, Let thy sires' realm, from trouble free, Obey her rightful king in thee. Here let the priests and lords of state Our monarch duly consecrate, With prayer and holy verses blessed By saint Va[ishmha and the rest. Anointed king by us, again Seek fair Ayodhyá, there to reign, And like imperial Indra girt By Gods of Storm, thy might assert. From the three debts384 acquittance earn, And with thy wrath the wicked burn, O'er all of us thy rule extend, And cheer with boons each faithful friend. Let thine enthronement, lord, this day Make all thy lovers glad and gay, And let all those who hate thee flee To the ten winds for fear of thee. Dear lord, my mother's words of hate With thy sweet virtues expiate, And from the stain of folly clear The father whom we both revere. Brother, to me compassion show, I pray thee with my head bent low, And to these friends who on thee call,— 384 To Gods, men, and Manes.
- **Translation**: 

---

### Verse 12 (Ramayana 0.777)
- **Original**: Canto CVII. Ráma's Speech. 759 As the Great Father pities all. But if my tears and prayers be vain, And thou in woods wilt still remain, I will with thee my path pursue And make my home in forests too.” Thus Bharat strove to bend his will With suppliant head, but he, Earth's lord, inexorable still Would keep his sire's decree. The firmness of the noble chief The wondering people moved, And rapture mingling with their grief, All wept and all approved. “How firm his steadfast will,” they cried, “Who Keeps his promise thus! Ah, to Ayodhyá's town,” they sighed, “He comes not back with us.” The holy priest, the swains who tilled The earth, the sons of trade, And e'en the mournful queens were filled With joy as Bharat prayed, And bent their heads, then weeping stilled A while, his prayer to aid. Canto CVII. Ráma's Speech.
- **Translation**: 

---

### Verse 13 (Ramayana 0.778)
- **Original**: 760 The Ramayana Thus, by his friends encompassed round, He spoke, and Ráma, far renowned, To his dear brother thus replied, Whom holy rites had purified: “O thou whom Queen Kaikeyí bare The best of kings, thy words are fair, Our royal father, when of yore He wed her, to her father swore The best of kingdoms to confer, A noble dowry meet for her; Then, grateful, on the deadly day Of heavenly Gods' and demons' fray, A future boon on her bestowed To whose sweet care his life he owed. She to his mind that promise brought, And then the best of kings besought To bid me to the forest flee, And give the rule, O Prince, to thee. Thus bound by oath, the king our lord Gave her those boons of free accord, And bade me, O thou chief of men, Live in the woods four years and ten. I to this lonely wood have hied With faithful LakshmaG by my side, And Sítá by no tears deterred, Resolved to keep my father's word. And thou, my noble brother, too Shouldst keep our father's promise true: Anointed ruler of the state Maintain his word inviolate. From his great debt, dear brother, free Our lord the king for love of me, Thy mother's breast with joy inspire, And from all woe preserve thy sire.
- **Translation**: 

---

### Verse 14 (Ramayana 0.779)
- **Original**: Canto CVII. Ráma's Speech. 761 'Tis said, near Gayá's holy town385 Gayá, great saint of high renown, This text recited when he paid Due rites to each ancestral shade: “A son is born his sire to free From Put's infernal pains: Hence, saviour of his father, he The name of Puttra gains.”386 Thus numerous sons are sought by prayer, In Scripture trained with graces fair, [217] That of the number one some day May funeral rites at Gayá pay. The mighty saints who lived of old This holy doctrine ever hold. Then, best of men, our sire release From pains of hell, and give him peace. Now Bharat, to Ayodhyá speed, The braveZatrughna with thee lead, Take with thee all the twice-born men, And please each lord and citizen. I now, O King, without delay To DaG ak wood will bend my way, And Lakshma G and the Maithil dame Will follow still, our path the same. Now, Bharat, lord of men be thou, And o'er Ayodhyá reign: The silvan world to me shall bow, King of the wild domain. 385 Gayá is a very holy city in Behar. Every good Hindu ought once in his life to make funeral offerings in Gayá in honour of his ancestors. 386 Put is the name of that region of hell to which men are doomed who leave no son to perform the funeral rites which are necessary to assure the happiness of the departed.Putra, the common word for a son is said by the highest authority to be derived fromPut and tradeliverer.
- **Translation**: 

---

### Verse 15 (Ramayana 0.780)
- **Original**: 762 The Ramayana Yea, let thy joyful steps be bent To that fair town to-day, And I as happy and content, To DaG ak wood will stray. The white umbrella o'er thy brow Its cooling shade shall throw: I to the shadow of the bough And leafy trees will go. Zatrughna, for wise plans renowned, Shall still on thee attend; And Lakshma G, ever faithful found, Be my familiar friend. Let us his sons, O brother dear, The path of right pursue, And keep the king we all revere Still to his promise true.” Canto CVIII. Jáváli's Speech. Thus Ráma soothed his brother's grief: Then virtuous Jáváli, chief Of twice-born sages, thus replied In words that virtue's law defied: “Hail, Raghu's princely son, dismiss A thought so weak and vain as this. Canst thou, with lofty heart endowed, Think with the dull ignoble crowd? For what are ties of kindred? can One profit by a brother man? Alone the babe first opes his eyes, And all alone at last he dies.
- **Translation**: 

---

### Verse 16 (Ramayana 0.781)
- **Original**: Canto CVIII. Jáváli's Speech. 763 The man, I ween, has little sense Who looks with foolish reverence On father's or on mother's name: In others, none a right may claim. E'en as a man may leave his home And to a distant village roam, Then from his lodging turn away And journey on the following day, Such brief possession mortals hold In sire and mother, house and gold, And never will the good and wise The brief uncertain lodging prize. Nor, best of men, shouldst thou disown Thy sire's hereditary throne, And tread the rough and stony ground Where hardship, danger, woes abound. Come, let Ayodhyá rich and bright See thee enthroned with every rite: Her tresses bound in single braid387 She waits thy coming long delayed. O come, thou royal Prince, and share The kingly joys that wait thee there, And live in bliss transcending price As Indra lives in Paradise. The parted king is naught to thee, Nor right in living man has he: The king is one, thou, Prince of men, Another art: be counselled then. Thy royal sire, O chief, has sped On the long path we all must tread. The common lot of all is this, 387 It was the custom of Indian women when mourning for their absent husbands to bind their hair in a long single braid. Carey and Marshman translate,“the one-tailed city.”
- **Translation**: 

---

### Verse 17 (Ramayana 0.782)
- **Original**: 764 The Ramayana And thou in vain art robbed of bliss. For those— and only those— I weep Who to the path of duty keep; For here they suffer ceaseless woe, And dying to destruction go. With pious care, each solemn day, Will men their funeral offerings pay: See, how the useful food they waste: He who is dead no more can taste. If one is fed, his strength renewed Whene'er his brother takes his food, Then offerings to the parted pay: Scarce will they serve him on his way. By crafty knaves these rules were framed, And to enforce men's gifts proclaimed: “Give, worship, lead a life austere, Keep lustral rites, quit pleasures here.” There is no future life: be wise, And do, O Prince, as I advise. Enjoy, my lord, the present bliss, And things unseen from thought dismiss. Let this advice thy bosom move, The counsel sage which all approve; To Bharat's earnest prayer incline, And take the rule so justly thine.” Canto CIX. The Praises Of Truth. By sage Jáváli thus addressed, Ráma of truthful hearts the best,[218]
- **Translation**: 

---

### Verse 18 (Ramayana 0.783)
- **Original**: Canto CIX. The Praises Of Truth. 765 With perfect skill and wisdom high Thus to his speech made fit reply: “Thy words that tempt to bliss are fair, But virtue's garb they falsely wear. For he from duty's path who strays To wander in forbidden ways, Allured by doctrine false and vain, Praise from the good can never gain. Their lives the true and boaster show, Pure and impure, and high and low, Else were no mark to judge between Stainless and stained and high and mean; They to whose lot fair signs may fall Were but as they who lack them all, And those to virtuous thoughts inclined Were but as men of evil mind. If in the sacred name of right I do this wrong in duty's spite; The path of virtue meanly quit, And this polluting sin commit, What man who marks the bounds between Virtue and vice with insight keen, Would rank me high in after time Stained with this soul destroying crime? Whither could I, the sinner, turn, How hope a seat in heaven to earn, If I my plighted promise break, And thus the righteous path forsake? This world of ours is ever led To walk the ways which others tread, And as their princes they behold, The subjects too their lives will mould. That truth and mercy still must be Beloved of kings, is Heaven's decree.
- **Translation**: 

---

### Verse 19 (Ramayana 0.784)
- **Original**: 766 The Ramayana Upheld by truth the monarch reigns, And truth the very world sustains. Truth evermore has been the love Of holy saints and Gods above, And he whose lips are truthful here Wins after death the highest sphere. As from a serpent's deadly tooth, We shrink from him who scorns the truth. For holy truth is root and spring Of justice and each holy thing, A might that every power transcends, Linked to high bliss that never ends. Truth is all virtue's surest base, Supreme in worth and first in place. Oblations, gifts men offer here, Vows, sacrifice, and rites austere, And Holy Writ, on truth depend: So men must still that truth defend. Truth, only truth protects the land, By truth unharmed our houses stand; Neglect of truth makes men distressed, And truth in highest heaven is blessed. Then how can I, rebellious, break Commandments which my father spake— I ever true and faithful found, And by my word of honour bound? My father's bridge of truth shall stand Unharmed by my destructive hand: Not folly, ignorance, or greed My darkened soul shall thus mislead. Have we not heard that God and shade Turn from the hated offerings paid By him whose false and fickle mind No pledge can hold, no promise bind?
- **Translation**: 

---

### Verse 20 (Ramayana 0.785)
- **Original**: Canto CIX. The Praises Of Truth. 767 Truth is all duty: as the soul, It quickens and supports the whole. The good respect this duty: hence Its sacred claims I reverence. The Warrior's duty I despise That seeks the wrong in virtue's guise: Those claims I shrink from, which the base, Cruel, and covetous embrace. The heart conceives the guilty thought, Then by the hand the sin is wrought, And with the pair is leagued a third, The tongue that speaks the lying word. Fortune and land and name and fame To man's best care have right and claim; The good will aye to truth adhere, And its high laws must men revere. Base were the deed thy lips would teach, Approved as best by subtle speech. Shall I my plighted promise break, That I these woods my home would make? Shall I, as Bharat's words advise, My father's solemn charge despise? Firm stands the oath which then before My father's face I soothly swore, Which Queen Kaikeyí's anxious ear Rejoiced with highest joy to hear. Still in the wood will I remain, With food prescribed my life sustain, And please with fruit and roots and flowers Ancestral shades and heavenly powers. Here every sense contented, still Heeding the bounds of good and ill, My settled course will I pursue, Firm in my faith and ever true.
- **Translation**: 

---



--- End of Ramayan_batch_137.md ---


--- Start of Ramayan_batch_138.md ---

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

### Verse 1 (Ramayana 0.786)
- **Original**: 768 The Ramayana Here in this wild and far retreat Will I my noble task complete; And Fire and Wind and Moon shall be Partakers of its fruit with me. A hundred offerings duly wrought His rank o'er Gods for Indra bought, And mighty saints their heaven secured By torturing years on earth endured.” That scoffing plea the hero spurned, And thus he spake once more, Chiding, the while his bosom burned, Jáváli's impious lore: “Justice, and courage ne'er dismayed, Pity for all distressed, Truth, loving honour duly paid To Bráhman, God, and guest— In these, the true and virtuous say, Should lives of men be passed: They form the right and happy way That leads to heaven at last.[219] My father's thoughtless act I chide That gave thee honoured place, Whose soul, from virtue turned aside, Is faithless, dark, and base. We rank the Buddhist with the thief,388 And all the impious crew Who share his sinful disbelief, And hate the right and true. Hence never should wise kings who seek To rule their people well, Admit, before their face to speak, 388 The verses in a different metre with which some cantos end are all to be regarded with suspicion. Schlegel regrets that he did not exclude them all from his edition. These lines are manifestly spurious. SeeAdditional Notes.
- **Translation**: 

---

### Verse 2 (Ramayana 0.787)
- **Original**: Canto CIX. The Praises Of Truth. 769 The cursed infidel. But twice-born men in days gone by, Of other sort than thou, Have wrought good deeds, whose glories high Are fresh among us now: This world they conquered, nor in vain They strove to win the skies: The twice-born hence pure lives maintain, And fires of worship rise. Those who in virtue's path delight, And with the virtuous live,— Whose flames of holy zeal are bright, Whose hands are swift to give, Who injure none, and good and mild In every grace excel, Whose lives by sin are undefiled, We love and honour well.” Thus Ráma spoke in righteous rage Jáváli's speech to chide, When thus again the virtuous sage In truthful words replied: “The atheist's lore I use no more, Not mine his impious creed: His words and doctrine I abhor, Assumed at time of need. E'en as I rose to speak with thee, The fit occasion came That bade me use the atheist's plea To turn thee from thine aim. The atheist creed I disavow, Unsay the words of sin, And use the faithful's language now Thy favour, Prince, to win.”
- **Translation**: 

---

### Verse 3 (Ramayana 0.788)
- **Original**: 770 The Ramayana Canto CX. The Sons Of Ikshváku.389 Then spake Va[ishmha who perceived That Ráma's soul was wroth and grieved: “Well knows the sage Jáváli all The changes that the world befall; And but to lead thee to revoke Thy purpose were the words he spoke. Lord of the world, now hear from me How first this world began to be. First water was, and naught beside; There earth was formed that stretches wide. Then with the Gods from out the same The Self-existent Brahmá came. Then Brahmá390 in a boar's disguise Bade from the deep this earth arise; Then, with his sons of tranquil soul, He made the world and framed the whole. From subtlest ether Brahmá rose: No end, no loss, no change he knows. A son had he, Maríchi styled, And Ka [yap was Maríchi's child. From him Vivasvat sprang: from him Manu, whose fame shall ne'er be dim. Manu, who life to mortals gave, Begot Ikshváku good and brave: First of Ayodhyá's kings was he, Pride of her famous dynasty. From him the glorious Kukshi sprang, 389 This genealogy is a repetition with slight variation of that given in Book I, Canto LXX. 390 In Gorresio's recension identified with VishGu. See Muir'sSanskrit Texts, Vol. IV. pp 29, 30.
- **Translation**: 

---

### Verse 4 (Ramayana 0.789)
- **Original**: Canto CX. The Sons Of Ikshváku. 771 Whose fame through all the regions rang. Rival of Kukshi's ancient fame, His heir the great Vikukshi came. His son was VáGa, lord of might, His AnaraGya, strong in fight. No famine marred his blissful reign, No drought destroyed the kindly grain; Amid the sons of virtue chief, His happy realm ne'er held a thief, His son was Prithu, glorious name, From him the wise Tri[anku came: Embodied to the skies he went For love of truth preëminent. He left a son renowned afar, Known by the name of Dhundhumár. His son succeeding bore the name Of Yuvaná[va dear to fame. He passed away. Him followed then His son Mándhátá, king of men. His son was blest in high emprise, Susandhi, fortunate and wise. Two noble sons had he, to wit Dhruvasandhi and Prasenajit. Bharat was Dhruvasandhi's son: His glorious arm the conquest won, Against his son King Asit, rose In fierce array his royal foes, Haihayas, Tálajanghas styled, And Za[ivindhus fierce and wild. [220] Long time he strove, but forced to yield Fled from his kingdom and the field. The wives he left had both conceived— So is the ancient tale believed:— One, of her rival's hopes afraid,
- **Translation**: 

---

### Verse 5 (Ramayana 0.790)
- **Original**: 772 The Ramayana Fell poison in the viands laid. It chanced that Chyavan, Bhrigu's child, Had wandered to the pathless wild Where proud Himálaya's lovely height Detained him with a strange delight. Then came the other widowed queen With lotus eyes and beauteous mien, Longing a noble son to bear, And wooed the saint with earnest prayer. When thus Kálindí, fairest dame With reverent supplication came, To her the holy sage replied: “O royal lady, from thy side A glorious son shall spring ere long, Righteous and true and brave and strong; He, scourge of foes and lofty-souled, His ancient race shall still uphold.” Then round the sage the lady went, And bade farewell, most reverent. Back to her home she turned once more, And there her promised son she bore. Because her rival mixed the bane To render her conception vain, And her unripened fruit destroy, Sagar she called her rescued boy.391 He, when he paid that solemn rite,392 Filled living creatures with affright: Obedient to his high decree His countless sons dug out the sea. Prince Asamanj was Sagar's child: But him with cruel sin defiled 391 From sa with, andgara poison. 392 See Book I. Canto XL.
- **Translation**: 

---

### Verse 6 (Ramayana 0.791)
- **Original**: Canto CX. The Sons Of Ikshváku. 773 And loaded with the people's hate His father banished from the state. To Asamanj his consort bare Bright An[umán his valiant heir. An [umán's son, Dilípa famed, Begot a son Bhagírath named. From him renowned Kakutstha came: Thou bearest still the lineal name. Kakutstha's son was Raghu: thou Art styled the son of Raghu now. From him came Purushádak bold, Fierce hero of gigantic mould: Kalmáshapáda's name he bore, Because his feet were spotted o'er. Zankhan his son, to manhood grown, Died sadly with his host o'erthrown, But ere he perished sprang from him Sudar[an fair in face and limb. From beautiful Sudar[an came Prince AgnivarGa, bright as flame. His son wasZíghraga, for speed Unmatched; and Maru was his seed. Prasusruka was Maru's child: His son was Ambarísha styled. Nahush was Ambarísha's heir With hand to strike and heart to dare. His son was good Nábhág, from youth Renowned for piety and truth. From great Nábhág sprang children two Aja and Suvrat pure and true. From Aja Da[aratha came, Whose virtuous life was free from blame. His eldest son art thou: his throne, O famous Ráma, is thine own.
- **Translation**: 

---

### Verse 7 (Ramayana 0.792)
- **Original**: 774 The Ramayana Accept the sway so justly thine, And view the world with eyes benign. For ever in Ikshváku's race The eldest takes his father's place, And while he lives no son beside As lord and king is sanctified. The rule by Raghu's children kept Thou must not spurn to-day. This realm of peerless wealth accept, And like thy father sway.” Canto CXI. Counsel To Bharat. Thus said Va[ishmha, and again To Ráma spake in duteous strain: “All men the light of life who see With high respect should look on three: High honour ne'er must be denied To father, mother, holy guide. First to their sires their birth they owe, Nursed with maternal love they grow: Their holy guides fair knowledge teach: So men should love and honour each. Thy sire and thou have learned of me, The sacred guide of him and thee, And if my word thou wilt obey Thou still wilt keep the virtuous way. See, with the chiefs of every guild And all thy friends, this place is filled: All these, as duty bids, protect; So still the righteous path respect.
- **Translation**: 

---

### Verse 8 (Ramayana 0.793)
- **Original**: Canto CXI. Counsel To Bharat. 775 O, for thine aged mother feel, Nor spurn the virtuous dame's appeal: Obey, O Prince, thy mother dear, And still to virtue's path adhere. Yield thou to Bharat's fond request, With earnest supplication pressed, So wilt thou to thyself be true, And faith and duty still pursue.” Thus by his saintly guide addressed With pleas in sweetest tones expressed, The lord of men in turn replied To wise Va[ishmha by his side: “The fondest son's observance ne'er Repays the sire and mother's care: [221] The constant love that food provides, And dress, and every need besides: Their pleasant words still soft and mild, Their nurture of the helpless child: The words which Da[aratha spake, My king and sire, I ne'er will break.” Then Bharat of the ample chest The wise Sumantra thus addressed; “Bring sacred grass, O charioteer, And strew it on the level here. For I will sit and watch his face Until I win my brother's grace. Like a robbed Bráhman will I lie,393 Nor taste of food nor turn my eye, In front of Ráma's leafy cot, And till he yield will leave him not.” 393 A practice which has frequently been described, under the name ofdherna, by European travellers in India.
- **Translation**: 

---

### Verse 9 (Ramayana 0.794)
- **Original**: 776 The Ramayana When Bharat saw Sumantra's eye Looked up to Ráma for reply, The Prince himself in eager haste The sacred grass in order placed. Him great and mighty Ráma, best Of royal saints, in turn addressed: “What, Bharat, have I done, that thou Besiegest me,394 a suppliant now? Thus streched, to force redress for wrongs To men of Bráhman birth belongs, Not those upon whose kingly head The consecrating drops are shed. Up, lord of men! arise, and quit This fearful vow for thee unfit. Go, brother, seek Ayodhyá's town, Fair city of supreme renown.” But Bharat, as his seat he took, Cast all around an eager look: “O people, join your prayers with mine, And so his stubborn heart incline.” And all the people answered thus: “Full well is Ráma known to us. Right is the word he speaks and he Is faithful to his sire's decree: Nor can we rashly venture now To turn him from his purposed vow.” 394 Compare Milton's“beseeching or beseiging.”
- **Translation**: 

---

### Verse 10 (Ramayana 0.795)
- **Original**: Canto CXI. Counsel To Bharat. 777 Then Ráma spoke:“O Bharat, heed Thy virtuous friends, and mark their rede. Mark well what I and these advise, And duty view with clearer eyes. Thy hand on mine, O hero, place, Touch water, and thy sin efface.” Then Bharat rose: his hand he dipped, And purifying water sipped: “Each citizen,” he cried,“give ear, Attend, each counsellor and peer. My mother planned, by me untaught, To win the sway I never sought: Ne'er Raghu's son could I despise, In duty's lore supremely wise. Now if obedience to our sire This dwelling in the woods require, I, till the destined years be spent, Will dwell alone in banishment.” The virtuous Ráma, wonder-stirred, The faithful speech of Bharat heard, And thus the hero's feelings found Due utterance, as he gazed around: “Still to my father's word I hold, Whate'er he bought, or pledged, or sold: Ne'er shall his living promise be Annulled by Bharat or by me. Not thus my task will I evade, My exile on another laid: Most wise was Queen Kaikeyí's rede, And just and good my father's deed. Dear Bharat's patient soul I know, How reverence due he loves to show;
- **Translation**: 

---

### Verse 11 (Ramayana 0.796)
- **Original**: 778 The Ramayana In him, high-souled and faithful found, Must each auspicious grace abound. When from the woods I turn again I with his aid shall nobly reign, With one so good, of peerless worth, A glorious lord of happy earth. Her boon Kaikeyí sought and won. I, as my father swore, have done: And O, do thou, my brother dear, The monarch's name from falsehood clear. Canto CXII. The Sandals. High wonder mingled with delight Took the great sages at the sight, Thrilling their breasts who came to view The meeting of the peerless two. The saints and sages' holy train Departed to their home again. And high each holy voice was raised, And thus the glorious brothers praised. “High fate is his, the sire of two Most virtuous souls, so brave and true: With wonder and with joy intense Our ears have heard their conference.” Then the great sages, longing all To see the ten-necked tyrant395 fall, To Bharat, bravest of the brave, Their salutary counsel gave: 395 Ten-headed, ten-necked, ten faced, are common epithets of RávaG the giant king of Lanká.
- **Translation**: 

---

### Verse 12 (Ramayana 0.797)
- **Original**: Canto CXII. The Sandals. 779 “O thou of lofty lineage born, Whom wisdom, conduct, fame adorn, Thou for thy honoured father's sake Shouldst Ráma's righteous counsel take. [222] All debts to Queen Kaikeyí paid, Thy sire his home in heaven has made, So virtuous Ráma we would see From filial obligation free.” Thus gave each royal sage advice, High saint, and bard of Paradise; Then quickly vanishing from view Each to his proper home withdrew. Then Ráma's face his rapture showed, And his full heart with joy o'erflowed, While, as the sages parted thence, He paid his humble reverence. Then Bharat shook in every limb As suppliant thus he spake to him: “The duty of a king respect, Held by our race in high respect: And O, thy gracious ear incline To heed my mother's prayer and mine. The mighty realm to rule and guard For me alone is task too hard. No power have I the love to gain Of noble, citizen, and swain. All those who know thee, warrior, friend, On thee their eager glances bend, As labouring hinds who till the plain Look fondly for the Lord of Rain. O wisest Prince, thy realm secure, And make its firm foundations sure. Kakutstha's son, thy mighty arm
- **Translation**: 

---

### Verse 13 (Ramayana 0.798)
- **Original**: 780 The Ramayana Can keep the nation free from harm.” He spoke, and fell in sorrow drowned At Ráma's feet upon the ground, And there the hero sued and sighed, And “Hear me, Raghu's son,” he cried. Then Ráma raised him up, and pressed His brother to his loving breast, And sweetly as a wild swan cried To Bharat dark and lotus-eyed: “So just and true thy generous soul, Thy hand may well this earth control: But many a sage his aid will lend, With counsellor, and peer, and friend: With these advise: their counsel ask, And so perform thy arduous task. The moon his beauty may forgo, The cold forsake the Hills of Snow, And Ocean o'er his banks may sweep, But I my father's word will keep. Now whether love of thee or greed Thy mother led to plan the deed, Forth from thy breast the memory throw, And filial love and reverence show.” Thus spake Kau[alyá's son: again Bharat replied in humble strain To him who matched the sun in might And lovely as the young moon's light: “Put, noble brother, I entreat, These sandals on thy blessed feet: These, lord of men, with gold bedecked, The realm and people will protect.”
- **Translation**: 

---

### Verse 14 (Ramayana 0.799)
- **Original**: Canto CXII. The Sandals. 781 Then Ráma, as his brother prayed Beneath his feet the sandals laid, And these with fond affection gave To Bharat's hand, the good and brave. Then Bharat bowed his reverent head And thus again to Ráma said: “Through fourteen seasons will I wear The hermit's dress and matted hair: With fruit and roots my life sustain, And still beyond the realm remain, Longing for thee to come again. The rule and all affairs of state I to these shoes will delegate. And if, O tamer of thy foes, When fourteen years have reached their close, I see thee not that day return, The kindled fire my frame shall burn.” Then Ráma to his bosom drew Dear Bharat andZatrughna too: “Be never wroth,” he cried,“with her, Kaikeyí's guardian minister: This, glory of Ikshváku's line, Is Sítá's earnest prayer and mine.” He spoke, and as the big tears fell, To his dear brother bade farewell. Round Ráma, Bharat strong and bold In humble reverence paced, When the bright sandals wrought with gold Above his brows were placed. The royal elephant who led The glorious pomp he found, And on the monster's mighty head Those sandals duly bound.
- **Translation**: 

---

### Verse 15 (Ramayana 0.800)
- **Original**: 782 The Ramayana Then noble Ráma, born to swell The glories of his race, To all in order bade farewell With love and tender grace— To brothers, counsellers, and peers,— Still firm, in duty proved, Firm, as the Lord of Snow uprears His mountains unremoved. No queen, for choking sobs and sighs, Could say her last adieu: Then Ráma bowed, with flooded eyes, And to his cot withdrew. Canto CXIII. Bharat's Return. Bearing the sandals on his head Away triumphant Bharat sped, And clomb,Zatrughna by his side, The car wherein he wont to ride. Before the mighty army went The lords for counsel eminent, Va [ishmha, Vámadeva next, Jáváli, pure with prayer and text.[223] Then from that lovely river they Turned eastward on their homeward way: With reverent steps from left to right They circled Chitrakúma's height, And viewed his peaks on every side With stains of thousand metals dyed. Then Bharat saw, not far away, Where Bharadvája's dwelling lay,
- **Translation**: 

---

### Verse 16 (Ramayana 0.801)
- **Original**: Canto CXIII. Bharat's Return. 783 And when the chieftain bold and sage Had reached that holy hermitage, Down from the car he sprang to greet The saint, and bowed before his feet. High rapture filled the hermit's breast, Who thus the royal prince addressed: “Say, Bharat, is thy duty done? Hast thou with Ráma met, my son?” The chief whose soul to virtue clave This answer to the hermit gave: “I prayed him with our holy guide: But Raghu's son our prayer denied, And long besought by both of us He answered Saint Va[ishmha thus: “True to my vow, I still will be Observant of my sire's decree: Till fourteen years complete their course That promise shall remain in force.” The saint in highest wisdom taught, These solemn words with wisdom fraught, To him in lore of language learned Most eloquent himself returned: “Obey my rede: let Bharat hold This pair of sandals decked with gold: They in Ayodhyá shall ensure Our welfare, and our bliss secure.” When Ráma heard the royal priest He rose, and looking to the east Consigned the sandals to my hand That they for him might guard the land. Then from the high-souled chief's abode I turned upon my homeward road, Dismissed by him, and now this pair
- **Translation**: 

---

### Verse 17 (Ramayana 0.802)
- **Original**: 784 The Ramayana Of sandals to Ayodhyá bear.” To him the hermit thus replied, By Bharat's tidings gratified: “No marvel thoughts so just and true, Thou best of all who right pursue, Should dwell in thee, O Prince of men, As waters gather in the glen. He is not dead, we mourn in vain: Thy blessed father lives again, Whose noble son we thus behold Like Virtue's self in human mould.” He ceased: before him Bharat fell To clasp his feet, and said farewell: His reverent steps around him bent, And onward to Ayodhyá went. His host of followers stretching far With many an elephant and car, Waggon and steed, and mighty train, Traversed their homeward way again. O'er holy Yamuná they sped, Fair stream, with waves engarlanded, And then once more the rivers' queen, The blessed Gangá's self was seen. Then making o'er that flood his way, Where crocodiles and monsters lay, The king toZringavera drew His host and royal retinue. His onward way he thence pursued, And soon renowned Ayodhyá viewed. Then burnt by woe and sad of cheer Bharat addressed the charioteer: “Ah, see, Ayodhyá dark and sad,
- **Translation**: 

---

### Verse 18 (Ramayana 0.803)
- **Original**: Canto CXIV. Bharat's Departure. 785 Her glory gone, once bright and glad: Of joy and beauty reft, forlorn, In silent grief she seems to mourn.” Canto CXIV. Bharat's Departure. Deep, pleasant was the chariot's sound As royal Bharat, far renowned, Whirled by his mettled coursers fast Within Ayodhyá's city passed. There dark and drear was every home Where cats and owls had space to roam, As when the shades of midnight fall With blackest gloom, and cover all: As RohiGí, dear spouse of him Whom Ráhu hates,396 grows faint and dim, When, as she shines on high alone The demon's shade is o'er her thrown: As burnt by summer's heat a rill Scarce trickling from her parent hill, With dying fish in pools half dried, And fainting birds upon her side: As sacrificial flames arise When holy oil their food supplies, But when no more the fire is fed Sink lustreless and cold and dead: Like some brave host that filled the plain, With harness rent and captains slain, When warrior, elephant, and steed 396 The spouse of RohiGí is the Moon: Ráhu is the demon who causes eclipses.
- **Translation**: 

---

### Verse 19 (Ramayana 0.804)
- **Original**: 786 The Ramayana Mingled in wild confusion bleed: As when, all spent her store of worth, Rocks from her base the loosened earth: Like a sad fallen star no more Wearing the lovely light it wore: So mournful in her lost estate Was that sad town disconsolate. Then car-borne Bharat, good and brave, Thus spake to him the steeds who drave: “Why are Ayodhyá's streets so mute? Where is the voice of lyre and lute? Why sounds not, as of old, to-day The music of the minstrel's lay?[224] Where are the wreaths they used to twine? Where are the blossoms and the wine? Where is the cool refreshing scent Of sandal dust with aloe blent? The elephant's impatient roar, The din of cars, I hear no more: No more the horse's pleasant neigh Rings out to meet me on my way. Ayodhyá's youths, since Ráma's flight, Have lost their relish for delight: Her men roam forth no more, nor care Bright garlands round their necks to wear. All grieve for banished Ráma: feast, And revelry and song have ceased: Like a black night when floods pour down, So dark and gloomy is the town. When will he come to make them gay Like some auspicious holiday? When will my brother, like a cloud At summer's close, make glad the crowd?”
- **Translation**: 

---

### Verse 20 (Ramayana 0.805)
- **Original**: Canto CXV. Nandigrám. 787 Then through the streets the hero rode, And passed within his sire's abode, Like some deserted lion's den, Forsaken by the lord of men. Then to the inner bowers he came, Once happy home of many a dame, Now gloomy, sad, and drear, Dark as of old that sunless day When wept the Gods in wild dismay;397 There poured he many a tear. Canto CXV. Nandigrám.398 Then when the pious chief had seen Lodged in her home each widowed queen, Still with his burning grief oppressed His holy guides he thus addressed: “I go to Nandigrám: adieu, This day, my lords to all of you: I go, my load of grief to bear, Reft of the son of Raghu, there. The king my sire, alas, is dead, And Ráma to the forest fled; There will I wait till he, restored, Shall rule the realm, its rightful lord.” 397 “Once,” says the Commentator Tírtha,“in the battle between the Gods and demons the Gods were vanquished, and the sun was overthrown by Ráhu. At the request of the Gods Atri undertook the management of the sun for a week.” 398 Now Nundgaon, in Oudh.
- **Translation**: 

---



--- End of Ramayan_batch_138.md ---


--- Start of Ramayan_batch_139.md ---

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

### Verse 1 (Ramayana 0.806)
- **Original**: 788 The Ramayana They heard the high-souled prince's speech, And thus with ready answer each Of those great lords their chief addressed, With saint Va[ishmha and the rest: “Good are the words which thou hast said, By brotherly affection led, Like thine own self, a faithful friend, True to thy brother to the end: A heart like thine must all approve, Which naught from virtue's path can move.” Soon as the words he loved to hear Fell upon Bharat's joyful ear, Thus to the charioteer he spoke: “My car with speed, Sumantra, yoke.” Then Bharat with delighted mien Obeisance paid to every queen, And withZatrughna by his side Mounting the car away he hied. With lords, and priests in long array The brothers hastened on their way. And the great pomp the Bráhmans led With Saint Va[ishmha at their head. Then every face was eastward bent As on to Nandigrám they went. Behind the army followed, all Unsummoned by their leader's call, And steeds and elephants and men Streamed forth with every citizen. As Bharat in his chariot rode His heart with love fraternal glowed, And with the sandals on his head To Nandigrám he quickly sped. Within the town he swiftly pressed,
- **Translation**: 

---

### Verse 2 (Ramayana 0.807)
- **Original**: Canto CXV. Nandigrám. 789 Alighted, and his guides addressed: “To me in trust my brother's hand Consigned the lordship of the land, When he these gold-wrought sandals gave As emblems to protect and save.” Then Bharat bowed, and from his head The sacred pledge deposited, And thus to all the people cried Who ringed him round on every side: “Haste, for these sandals quickly bring The canopy that shades the king. Pay ye to them all reverence meet As to my elder brother's feet, For they will right and law maintain Until King Ráma come again. My brother with a loving mind These sandals to my charge consigned: I till he come will guard with care The sacred trust for Raghu's heir. My watchful task will soon be done, The pledge restored to Raghu's son; Then shall I see, his wanderings o'er, These sandals on his feet once more. My brother I shall meet at last, The burthen from my shoulders cast, To Ráma's hand the realm restore And serve my elder as before. When Ráma takes again this pair Of sandals kept with pious care, And here his glorious reign begins, I shall be cleansed from all my sins, [225] When the glad people's voices ring With welcome to the new-made king, Joy will be mine four-fold as great
- **Translation**: 

---

### Verse 3 (Ramayana 0.808)
- **Original**: 790 The Ramayana As if supreme I ruled the state.” Thus humbly spoke in sad lament The chief in fame preëminent: Thus, by his reverent lords obeyed, At Nandigrám the kingdom swayed. With hermit's dress and matted hair He dwelt with all his army there. The sandals of his brother's feet Installed upon the royal seat, He, all his powers to them referred, Affairs of state administered. In every care, in every task, When golden store was brought, He first, as though their rede to ask, Those royal sandals sought. Canto CXVI. The Hermit's Speech. When Bharat took his homeward road Still Ráma in the wood abode: But soon he marked the fear and care That darkened all the hermits there. For all who dwelt before the hill Were sad with dread of coming ill: Each holy brow was lined by thought, And Ráma's side they often sought. With gathering frowns the prince they eyed, And then withdrew and talked aside.
- **Translation**: 

---

### Verse 4 (Ramayana 0.809)
- **Original**: Canto CXVI. The Hermit's Speech. 791 Then Raghu's son with anxious breast The leader of the saints addressed: “Can aught that I have done displease, O reverend Sage, the devotees? Why are their loving looks, O say, Thus sadly changed or turned away? Has LakshmaG through his want of heed Offended with unseemly deed? Or is the gentle Sítá, she Who loved to honour you and me— Is she the cause of this offence, Failing in lowly reverence?” One sage, o'er whom, exceeding old, Had many a year of penance rolled, Trembling in every aged limb Thus for the rest replied to him: “How could we, O beloved, blame Thy lofty-souled Videhan dame, Who in the good of all delights, And more than all of anchorites? But yet through thee a numbing dread Of fiends among our band has spread; Obstructed by the demons' art The trembling hermits talk apart. For RávaG's brother, overbold, Named Khara, of gigantic mould, Vexes with fury fierce and fell All those in Janasthán399 who dwell. Resistless in his cruel deeds, On flesh of men the monster feeds: Sinful and arrogant is he, And looks with special hate on thee. 399 A part of the great DaG ak forest.
- **Translation**: 

---

### Verse 5 (Ramayana 0.810)
- **Original**: 792 The Ramayana Since thou, beloved son, hast made Thy home within this holy shade, The fiends have vexed with wilder rage The dwellers of the hermitage. In many a wild and dreadful form Around the trembling saints they swarm, With hideous shape and foul disguise They terrify our holy eyes. They make our loathing souls endure Insult and scorn and sights impure, And flocking round the altars stay The holy rites we love to pay. In every spot throughout the grove With evil thoughts the monsters rove, Assailing with their secret might Each unsuspecting anchorite. Ladle and dish away they fling, Our fires with floods extinguishing, And when the sacred flame should burn They trample on each water-urn. Now when they see their sacred wood Plagued by this impious brotherhood, The troubled saints away would roam And seek in other shades a home: Hence will we fly, O Ráma, ere The cruel fiends our bodies tear. Not far away a forest lies Rich in the roots and fruit we prize, To this will I and all repair And join the holy hermits there; Be wise, and with us thither flee Before this Khara injure thee. Mighty art thou, O Ráma, yet Each day with peril is beset.
- **Translation**: 

---

### Verse 6 (Ramayana 0.811)
- **Original**: Canto CXVII. Anasúyá. 793 If with thy consort by thy side Thou in this wood wilt still abide.” He ceased: the words the hero spake The hermit's purpose failed to break: To Raghu's son farewell he said, And blessed the chief and comforted; Then with the rest the holy sage Departed from the hermitage. So from the wood the saints withdrew, And Ráma bidding all adieu In lowly reverence bent: Instructed by their friendly speech, Blest with the gracious love of each, To his pure home he went. Nor would the son of Raghu stray A moment from that grove away From which the saints had fled. And many a hermit thither came Attracted by his saintly fame And the pure life he led. [226] Canto CXVII. Anasúyá.
- **Translation**: 

---

### Verse 7 (Ramayana 0.812)
- **Original**: 794 The Ramayana But dwelling in that lonely spot Left by the hermits pleased him not. “I met the faithful Bharat here, The townsmen, and my mother dear: The painful memory lingers yet, And stings me with a vain regret. And here the host of Bharat camped, And many a courser here has stamped, And elephants with ponderous feet Have trampled through the calm retreat.” So forth to seek a home he hied, His spouse and LakshmaG by his side. He came to Atri's pure retreat, Paid reverence to his holy feet, And from the saint such welcome won As a fond father gives his son. The noble prince with joy unfeigned As a dear guest he entertained, And cheered the glorious LakshmaG too And Sítá with observance due. Then Anasúyá at the call Of him who sought the good of all, His blameless venerable spouse, Delighting in her holy vows, Came from her chamber to his side: To her the virtuous hermit cried: “Receive, I pray, with friendly grace This dame of Maithil monarchs' race:” To Ráma next made known his wife, The devotee of saintliest life: “Ten thousand years this votaress bent On sternest rites of penance spent; She when the clouds withheld their rain, And drought ten years consumed the plain,
- **Translation**: 

---

### Verse 8 (Ramayana 0.813)
- **Original**: Canto CXVII. Anasúyá. 795 Caused grateful roots and fruit to grow And ordered Gangá here to flow: So from their cares the saints she freed, Nor let these checks their rites impede, She wrought in Heaven's behalf, and made Ten nights of one, the Gods to aid:400 Let holy Anasúyá be An honoured mother, Prince, to thee. Let thy Videhan spouse draw near To her whom all that live revere, Stricken in years, whose loving mind Is slow to wrath and ever kind.” He ceased: and Ráma gave assent, And said, with eyes on Sítá bent: “O Princess, thou hast heard with me This counsel of the devotee: Now that her touch thy soul may bless, Approach the saintly votaress: Come to the venerable dame, Far known by Anasúyá's name: The mighty things that she has done High glory in the world have won.” Thus spoke the son of Raghu: she Approached the saintly devotee, Who with her white locks, old and frail, Shook like a plantain in the gale. To that true spouse she bowed her head, And “Lady, I am Sítá,” said: Raised suppliant hands and prayed her tell That all was prosperous and well. 400 When the saint MáG avya had doomed some saint's wife, who was Anasúyá's friend, to become a widow on the morrow.
- **Translation**: 

---

### Verse 9 (Ramayana 0.814)
- **Original**: 796 The Ramayana The aged matron, when she saw Fair Sítá true to duty's law, Addressed her thus:“High fate is thine Whose thoughts to virtue still incline. Thou, lady of the noble mind, Hast kin and state and wealth resigned To follow Ráma forced to tread Where solitary woods are spread. Those women gain high spheres above Who still unchanged their husbands love, Whether they dwell in town or wood, Whether their hearts be ill or good. Though wicked, poor, or led away In love's forbidden paths to stray, The noble matron still will deem Her lord a deity supreme. Regarding kin and friendship, I Can see no better, holier tie, And every penance-rite is dim Beside the joy of serving him. But dark is this to her whose mind Promptings of idle fancy blind, Who led by evil thoughts away Makes him who should command obey. Such women, O dear Maithil dame, Their virtue lose and honest fame, Enslaved by sin and folly, led In these unholy paths to tread. But they who good and true like thee The present and the future see, Like men by holy deeds will rise To mansions in the blissful skies. So keep thee pure from taint of sin, Still to thy lord be true,
- **Translation**: 

---

### Verse 10 (Ramayana 0.815)
- **Original**: Canto CXVIII. Anasúyá's Gifts. 797 And fame and merit shalt thou win, To thy devotion due.” Canto CXVIII. Anasúyá's Gifts. Thus by the holy dame addressed Who banished envy from her breast, Her lowly reverence Sítá paid, And softly thus her answer made: “No marvel, best of dames, thy speech The duties of a wife should teach; [227] Yet I, O lady, also know Due reverence to my lord to show. Were he the meanest of the base, Unhonoured with a single grace, My husband still I ne'er would leave, But firm through all to him would cleave: Still rather to a lord like mine Whose virtues high-exalted shine, Compassionate, of lofty soul, With every sense in due control, True in his love, of righteous mind, Like a dear sire and mother kind. E'en as he ever loves to treat Kau [alyá with observance meet, Has his behaviour ever been To every other honoured queen. Nay, more, a sonlike reverence shows The noble Ráma e'en to those On whom the king his father set His eyes one moment, to forget.
- **Translation**: 

---

### Verse 11 (Ramayana 0.816)
- **Original**: 798 The Ramayana Deep in my heart the words are stored, Said by the mother of my lord, When from my home I turned away In the lone fearful woods to stray. The counsel of my mother deep Impressed upon my soul I keep, When by the fire I took my stand, And Ráma clasped in his my hand. And in my bosom cherished yet, My friends' advice I ne'er forget: Woman her holiest offering pays When she her husband's will obeys. Good Sávitrí her lord obeyed, And a high saint in heaven was made, And for the self-same virtue thou Hast heaven in thy possession now. And she with whom no dame could vie, Now a bright Goddess in the sky, Sweet RohiGí the Moon's dear Queen, Without her lord is never seen: And many a faithful wife beside For her pure love is glorified.” Thus Sítá spake: soft rapture stole Through Anasúyá's saintly soul: Kisses on Sítá's head she pressed, And thus the Maithil dame addressed: “I by long rites and toils endured Rich store of merit have secured: From this my wealth will I bestow A blessing ere I let thee go. So right and wise and true each word That from thy lips mine ears have heard, I love thee: be my pleasing task
- **Translation**: 

---

### Verse 12 (Ramayana 0.817)
- **Original**: Canto CXVIII. Anasúyá's Gifts. 799 To grant the boon that thou shalt ask.” Then Sítá marvelled much, and while Played o'er her lips a gentle smile, “All has been done, O Saint,” she cried, “And naught remains to wish beside.” She spake; the lady's meek reply Swelled Anasúyá's rapture high. “Sítá,” she said,“my gift to-day Thy sweet contentment shall repay. Accept this precious robe to wear, Of heavenly fabric, rich and rare, These gems thy limbs to ornament, This precious balsam sweet of scent. O Maithil dame, this gift of mine Shall make thy limbs with beauty shine, And breathing o'er thy frame dispense Its pure and lasting influence. This balsam on thy fair limbs spread New radiance on thy lord shall shed, As Lakshmí's beauty lends a grace To VishGu's own celestial face.” Then Sítá took the gift the dame Bestowed on her in friendship's name, The balsam, gems, and robe divine, And garlands wreathed of bloomy twine; Then sat her down, with reverence meet, At saintly Anasúyá's feet. The matron rich in rites and vows Turned her to Ráma's Maithil spouse, And questioned thus in turn to hear A pleasant tale to charm her ear: “Sítá, 'tis said that Raghu's son
- **Translation**: 

---

### Verse 13 (Ramayana 0.818)
- **Original**: 800 The Ramayana Thy hand, mid gathered suitors, won. I fain would hear thee, lady, tell The story as it all befell: Do thou repeat each thing that passed, Reviewing all from first to last.” Thus spake the dame to Sítá: she Replying to the devotee, “Then, lady, thy attention lend,” Rehearsed the story to the end: “King Janak, just and brave and strong, Who loves the right and hates the wrong, Well skilled in what the law ordains For Warriors, o'er Videha reigns. Guiding one morn the plough, his hand Marked out, for rites the sacred land, When, as the ploughshare cleft the earth, Child of the king I leapt to birth. Then as the ground he smoothed and cleared, He saw me all with dust besmeared, And on the new-found babe, amazed The ruler of Videha gazed. In childless love the monarch pressed The welcome infant to his breast: “My daughter,” thus he cried,“is she:” And as his child he cared for me. Forth from the sky was heard o'erhead As 'twere a human voice that said: “Yea, even so: great King, this child Henceforth thine own be justly styled.” Videha's monarch, virtuous souled, Rejoiced o'er me with joy untold, Delighting in his new-won prize,
- **Translation**: 

---

### Verse 14 (Ramayana 0.819)
- **Original**: Canto CXVIII. Anasúyá's Gifts. 801 The darling of his heart and eyes. To his chief queen of saintly mind The precious treasure he consigned, And by her side she saw me grow, Nursed with the love which mothers know. [228] Then as he saw the seasons fly, And knew my marriage-time was nigh, My sire was vexed with care, as sad As one who mourns the wealth he had: “Scorn on the maiden's sire must wait From men of high and low estate: The virgin's father all despise, Though Indra's peer, who rules the skies.” More near he saw, and still more near, The scorn that filled his soul with fear, On trouble's billowy ocean tossed, Like one whose shattered bark is lost. My father knowing how I came, No daughter of a mortal dame, In all the regions failed to see A bridegroom meet to match with me. Each way with anxious thought he scanned, And thus at length the monarch planned: “The Bride's Election will I hold, With every rite prescribed of old.” It pleased King VaruG to bestow Quiver and shafts and heavenly bow Upon my father's sire who reigned, When Daksha his great rite ordained. Where was the man might bend or lift With utmost toil that wondrous gift? Not e'en in dreams could mortal king Strain the great bow or draw the string. Of this tremendous bow possessed,
- **Translation**: 

---

### Verse 15 (Ramayana 0.820)
- **Original**: 802 The Ramayana My truthful father thus addressed The lords of many a region, all Assembled at the monarch's call: “Whoe'er this bow can manage, he The husband of my child shall be.” The suitors viewed with hopeless eyes That wondrous bow of mountain size, Then to my sire they bade adieu, And all with humbled hearts withdrew. At length with Vi[vámitra came This son of Raghu, dear to fame, The royal sacrifice to view. Near to my father's home he drew, His brother LakshmaG by his side, Ráma, in deeds heroic tried. My sire with honour entertained The saint in lore of duty trained, Who thus in turn addressed the king: “Ráma and LakshmaG here who spring From royal Da[aratha, long To see thy bow so passing strong.” Before the prince's eyes was laid That marvel, as the Bráhman prayed. One moment on the bow he gazed, Quick to the notch the string he raised, Then, in the wandering people's view, The cord with mighty force he drew. Then with an awful crash as loud As thunderbolts that cleave the cloud, The bow beneath the matchless strain Of arms heroic snapped in twain. Thus, giving purest water, he, My sire, to Ráma offered me.
- **Translation**: 

---

### Verse 16 (Ramayana 0.821)
- **Original**: Canto CXIX. The Forest. 803 The prince the offered gift declined Till he should learn his father's mind; So horsemen swift Ayodhyá sought And back her aged monarch brought. Me then my sire to Ráma gave, Self-ruled, the bravest of the brave. And Urmilá, the next to me, Graced with all gifts, most fair to see, My sire with Raghu's house allied, And gave her to be LakshmaG's bride. Thus from the princes of the land Lord Ráma won my maiden hand, And him exalted high above Heroic chiefs I truly love.” Canto CXIX. The Forest. When Anasúyá, virtuous-souled, Had heard the tale by Sítá told, She kissed the lady's brow and laced Her loving arms around her waist. “With sweet-toned words distinct and clear Thy pleasant tale has charmed mine ear, How the great king thy father held That Maiden's Choice unparalleled. But now the sun has sunk from sight, And left the world to holy Night. Hark! how the leafy thickets sound With gathering birds that twitter round: They sought their food by day, and all Flock homeward when the shadows fall.
- **Translation**: 

---

### Verse 17 (Ramayana 0.822)
- **Original**: 804 The Ramayana See, hither comes the hermit band, Each with his pitcher in his hand: Fresh from the bath, their locks are wet, Their coats of bark are dripping yet. Here saints their fires of worship tend, And curling wreaths of smoke ascend: Borne on the flames they mount above, Dark as the brown wings of the dove. The distant trees, though well-nigh bare, Gloom thickened by the evening air, And in the faint uncertain light Shut the horizon from our sight. The beasts that prowl in darkness rove On every side about the grove, And the tame deer, at ease reclined Their shelter near the altars find. The night o'er all the sky is spread, With lunar stars engarlanded, And risen in his robes of light The moon is beautifully bright. Now to thy lord I bid thee go: Thy pleasant tale has charmed me so: One thing alone I needs must pray, Before me first thyself array: Here in thy heavenly raiment shine, And glad, dear love, these eyes of mine.”[229] Then like a heavenly Goddess shone Fair Sítá with that raiment on. She bowed her to the matron's feet, Then turned away her lord to meet. The hero prince with joy surveyed His Sítá in her robes arrayed, As glorious to his arms she came With love-gifts of the saintly dame.
- **Translation**: 

---

### Verse 18 (Ramayana 0.823)
- **Original**: Canto CXIX. The Forest. 805 She told him how the saint to show Her fond affection would bestow That garland of celestial twine, Those ornaments and robes divine. Then Ráma's heart, nor LakshmaG's less, Was filled with pride and happiness, For honours high had Sítá gained, Which mortal dames have scarce obtained. There honoured by each pious sage Who dwelt within the hermitage, Beside his darling well content That sacred night the hero spent. The princes, when the night had fled, Farewell to all the hermits said, Who gazed upon the distant shade, Their lustral rites and offerings paid. The saints who made their dwelling there In words like these addressed the pair: “O Princes, monsters fierce and fell Around that distant forest dwell: On blood from human veins they feed, And various forms assume at need, With savage beasts of fearful power That human flesh and blood devour. Our holy saints they rend and tear When met alone or unaware, And eat them in their cruel joy: These chase, O Ráma, or destroy. By this one path our hermits go To fetch the fruits that yonder grow: By this, O Prince, thy feet should stray Through pathless forests far away.”
- **Translation**: 

---

### Verse 19 (Ramayana 0.824)
- **Original**: 806 The Ramayana Thus by the reverent saints addressed, And by their prayers auspicious blessed, He left the holy crowd: His wife and brother by his side, Within the mighty wood he hied. So sinks the Day-God in his pride Beneath a bank of cloud.
- **Translation**: 

---

### Verse 20 (Ramayana 0.825)
- **Original**: BOOK III. Canto I. The Hermitage. When Ráma, valiant hero, stood In the vast shade of DaG ak wood, His eyes on every side he bent And saw a hermit settlement, Where coats of bark were hung around, And holy grass bestrewed the ground. Bright with Bráhmanic lustre glowed That circle where the saints abode: Like the hot sun in heaven it shone, Too dazzling to be looked upon. Wild creatures found a refuge where The court, well-swept, was bright and fair, And countless birds and roedeer made Their dwelling in the friendly shade. Beneath the boughs of well-loved trees Oft danced the gay Apsarases.401 Around was many an ample shed Wherein the holy fire was fed; With sacred grass and skins of deer, Ladles and sacrificial gear, And roots and fruit, and wood to burn, 401 Heavenly nymphs.
- **Translation**: 

---



--- End of Ramayan_batch_139.md ---


--- Start of Ramayan_batch_140.md ---

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

### Verse 1 (Ramayana 0.826)
- **Original**: 808 The Ramayana And many a brimming water-urn. Tall trees their hallowed branches spread, Laden with pleasant fruit, o'erhead; And gifts which holy laws require,402 And solemn offerings burnt with fire,403 And Veda chants on every side That home of hermits sanctified. There many a flower its odour shed, And lotus blooms the lake o'erspred. There, clad in coats of bark and hide,— Their food by roots and fruit supplied,— Dwelt many an old and reverend sire Bright as the sun or Lord of Fire, All with each worldly sense subdued, A pure and saintly multitude. The Veda chants, the saints who trod The sacred ground and mused on God, Made that delightful grove appear Like Brahmá's own most glorious sphere. As Raghu's splendid son surveyed That hermit home and tranquil shade, He loosed his mighty bow-string, then Drew nearer to the holy men.[230] With keen celestial sight endued Those mighty saints the chieftain viewed, With joy to meet the prince they came, And gentle Sítá dear to fame. They looked on virtuous Ráma, fair As Soma 404 in the evening air, And Lakshma G by his brother's side, 402 The ballor present of food to all created beings. 403 The clarified butter &c. cast into the sacred fire. 404 The Moon-God: “he is,” says the commentator,“the special deity of Bráhmans.”
- **Translation**: 

---

### Verse 2 (Ramayana 0.827)
- **Original**: Canto I. The Hermitage. 809 And Sítá long in duty tried, And with glad blessings every sage Received them in the hermitage. Then Ráma's form and stature tall Entranced the wondering eyes of all,— His youthful grace, his strength of limb, And garb that nobly sat on him. To LakshmaG too their looks they raised, And upon Sítá's beauty gazed With eyes that closed not lest their sight Should miss the vision of delight. Then the pure hermits of the wood, Rejoicing in all creatures' good, Their guest, the glorious Ráma, led Within a cot with leaves o'erhead. With highest honour all the best Of radiant saints received their guest, With kind observance, as is meet, And gave him water for his feet. To highest pitch of rapture wrought Their stores of roots and fruit they brought. They poured their blessings on his head, And “All we have is thine,” they said. Then, reverent hand to hand applied,405 Each duty-loving hermit cried: “The king is our protector, bright In fame, maintainer of the right. He bears the awful sword, and hence Deserves an elder's reverence. One fourth of Indra's essence, he Preserves his realm from danger free, 405 “Because he was an incarnation of the deity,” says the commentator,“oth- erwise such honour paid by men of the sacerdotal caste to one of the military would be improper.”
- **Translation**: 

---

### Verse 3 (Ramayana 0.828)
- **Original**: 810 The Ramayana Hence honoured by the world of right The king enjoys each choice delight. Thou shouldst to us protection give, For in thy realm, dear lord, we live: Whether in town or wood thou be, Thou art our king, thy people we. Our wordly aims are laid aside, Our hearts are tamed and purified. To thee our guardian, we who earn Our only wealth by penance turn.” Then the pure dwellers in the shade To Raghu's son due honour paid, And Lakshma G, bringing store of roots, And many a flower, and woodland fruits. And others strove the prince to please With all attentive courtesies. Canto II. Virádha. Thus entertained he passed the night, Then, with the morning's early light, To all the hermits bade adieu And sought his onward way anew. He pierced the mighty forest where Roamed many a deer and pard and bear: Its ruined pools he scarce could see. For creeper rent and prostrate tree, Where shrill cicada's cries were heard, And plaintive notes of many a bird. Deep in the thickets of the wood
- **Translation**: 

---

### Verse 4 (Ramayana 0.829)
- **Original**: Canto II. Virádha. 811 With LakshmaG and his spouse he stood, There in the horrid shade he saw A giant passing nature's law: Vast as some mountain-peak in size, With mighty voice and sunken eyes, Huge, hideous, tall, with monstrous face, Most ghastly of his giant race. A tiger's hide the Rákshas wore Still reeking with the fat and gore: Huge-faced, like Him who rules the dead, All living things he struck with dread. Three lions, tigers four, ten deer He carried on his iron spear, Two wolves, an elephant's head beside With mighty tusks which blood-drops dyed. When on the three his fierce eye fell, He charged them with a roar and yell As furious as the grisly King When stricken worlds are perishing. Then with a mighty roar that shook The earth beneath their feet, he took The trembling Sítá to his side. Withdrew a little space, and cried: “Ha, short lived wretches, ye who dare, In hermit dress with matted hair, Armed each with arrows, sword, and bow, Through DaG ak's pathless wood to go: How with one dame, I bid you tell, Can you among ascetics dwell? Who are ye, sinners, who despise The right, in holy men's disguise? The great Virádha, day by day Through this deep-tangled wood I stray, And ever, armed with trusty steel,
- **Translation**: 

---

### Verse 5 (Ramayana 0.830)
- **Original**: 812 The Ramayana I seize a saint to make my meal. This woman young and fair of frame Shall be the conquering giant's dame: Your blood, ye things of evil life, My lips shall quaff in battle strife.” He spoke: and Janak's hapless child, Scared by his speech so fierce and wild,[231] Trembled for terror, as a frail Young plantain shivers in the gale. When Ráma saw Virádha clasp Fair Sítá in his mighty grasp, Thus with pale lips that terror dried The hero to his brother cried: “O see Virádha's arm enfold My darling in its cursed hold,— The child of Janak best of kings, My spouse whose soul to virtue clings, Sweet princess, with pure glory bright, Nursed in the lap of soft delight. Now falls the blow Kaikeyí meant, Successful in her dark intent: This day her cruel soul will be Triumphant over thee and me. Though Bharat on the throne is set, Her greedy eyes look farther yet: Me from my home she dared expel, Me whom all creatures loved so well. This fatal day at length, I ween, Brings triumph to the younger queen. I see with bitterest grief and shame Another touch the Maithil dame. Not loss of sire and royal power So grieves me as this mournful hour.”
- **Translation**: 

---

### Verse 6 (Ramayana 0.831)
- **Original**: Canto III. Virádha Attacked. 813 Thus in his anguish cried the chief: Then drowned in tears, o'erwhelmed by grief, Thus LakshmaG in his anger spake, Quick panting like a spell-bound snake: “Canst thou, my brother, Indra's peer, When I thy minister am near, Thus grieve like some forsaken thing, Thou, every creature's lord and king? My vengeful shaft the fiend shall slay, And earth shall drink his blood to-day. The fury which my soul at first Upon usurping Bharat nursed, On this Virádha will I wreak As Indra splits the mountain peak. Winged by this arm's impetuous might My shaft with deadly force The monster in the chest shall smite, And fell his shattered corse.” Canto III. Virádha Attacked. Virádha with a fearful shout That echoed through the wood, cried out: “What men are ye, I bid you say, And whither would ye bend your way?”
- **Translation**: 

---

### Verse 7 (Ramayana 0.832)
- **Original**: 814 The Ramayana To him whose mouth shot fiery flame The hero told his race and name: “Two Warriors, nobly bred, are we, And through this wood we wander free. But who art thou, how born and styled, Who roamest here in DaG ak's wild?” To Ráma, bravest of the brave, His answer thus Virádha gave: “Hear, Raghu's son, and mark me well, And I my name and race will tell. Of Zatahradá born, I spring From Java as my sire, O King: Me, of this lofty lineage, all Giants on earth Virádha call. The rites austere I long maintained From Brahmá's grace the boon have gained To bear a charmed frame which ne'er Weapon or shaft may pierce or tear. Go as ye came, untouched by fear, And leave with me this woman here: Go, swiftly from my presence fly, Or by this hand ye both shall die.” Then Ráma with his fierce eyes red With fury to the giant said: “Woe to thee, sinner, fond and weak, Who madly thus thy death wilt seek! Stand, for it waits thee in the fray: With life thou ne'er shalt flee away.”
- **Translation**: 

---

### Verse 8 (Ramayana 0.833)
- **Original**: Canto III. Virádha Attacked. 815 He spoke, and raised the cord whereon A pointed arrow flashed and shone, Then, wild with anger, from his bow, He launched the weapon on the foe. Seven times the fatal cord he drew, And forth seven rapid arrows flew, Shafts winged with gold that left the wind And e'en SuparGa's406 self behind. Full on the giant's breast they smote, And purpled like the peacock's throat, Passed through his mighty bulk and came To earth again like flakes of flame. The fiend the Maithil dame unclasped; In his fierce hand his spear he grasped, And wild with rage, pierced through and through, At Ráma and his brother flew. So loud the roar which chilled with fear, So massy was the monster's spear, He seemed, like Indra's flagstaff, dread As the dark God who rules the dead. On huge Virádha fierce as He407 Who smites, and worlds have ceased to be, The princely brothers poured amain Their fiery flood of arrowy rain. Unmoved he stood, and opening wide His dire mouth laughed unterrified, And ever as the monster gaped Those arrows from his jaws escaped. Preserving still his life unharmed, By Brahmá's saving promise charmed, His mighty spear aloft in air He raised, and rushed upon the pair. 406 The king of birds. 407 Kálántakayamopamam , resembling Yáma the destroyer.
- **Translation**: 

---

### Verse 9 (Ramayana 0.834)
- **Original**: 816 The Ramayana From Ráma's bow two arrows flew And cleft that massive spear in two,[232] Dire as the flaming levin sent From out the cloudy firmament. Cut by the shafts he guided well To earth the giant's weapon fell: As when from Meru's summit, riven By fiery bolts, a rock is driven. Then swift his sword each warrior drew, Like a dread serpent black of hue, And gathering fury for the blow Rushed fiercely on the giant foe. Around each prince an arm he cast, And held the dauntless heroes fast: Then, though his gashes gaped and bled, Bearing the twain he turned and fled. Then Ráma saw the giant's plan, And to his brother thus began: “O Lakshma G, let Virádha still Hurry us onward as he will, For look, Sumitrá's son, he goes Along the path we freely chose.” He spoke: the rover of the night Upraised them with terrific might, Till, to his lofty shoulders swung, Like children to his neck they clung. Then sending far his fearful roar, The princes through the wood he bore,— A wood like some vast cloud to view, Where birds of every plumage flew, And mighty trees o'erarching threw Dark shadows on the ground;
- **Translation**: 

---

### Verse 10 (Ramayana 0.835)
- **Original**: Canto IV. Virádha's Death. 817 Where snakes and silvan creatures made Their dwelling, and the jackal strayed Through tangled brakes around. Canto IV. Virádha's Death. But Sítá viewed with wild affright The heroes hurried from her sight. She tossed her shapely arms on high, And shrieked aloud her bitter cry: “Ah, the dread giant bears away The princely Ráma as his prey, Truthful and pure, and good and great, And Lakshma G shares his brother's fate. The brindled tiger and the bear My mangled limbs for food will tear. Take me, O best of giants, me, And leave the sons of Raghu free.”
- **Translation**: 

---

### Verse 11 (Ramayana 0.836)
- **Original**: 818 The Ramayana Then, by avenging fury spurred, Her mournful cry the heroes heard, And hastened, for the lady's sake, The wicked monster's life to take. Then LakshmaG with resistless stroke The foe's left arm that held him broke, And Ráma too, as swift to smite, Smashed with his heavy hand the right. With broken arms and tortured frame To earth the fainting giant came, Like a huge cloud, or mighty rock Rent, sundered by the levin's shock. Then rushed they on, and crushed and beat Their foe with arms and fists and feet, And nerved each mighty limb to pound And bray him on the level ground. Keen arrows and each biting blade Wide rents in breast and side had made; But crushed and torn and mangled, still The monster lived they could not kill. When Ráma saw no arms might slay The fiend who like a mountain lay, The glorious hero, swift to save In danger, thus his counsel gave: “O Prince of men, his charmed life No arms may take in battle strife: Now dig we in this grove a pit His elephantine bulk to fit, And let the hollowed earth enfold The monster of gigantic mould.” This said, the son of Raghu pressed His foot upon the giant's breast. With joy the prostrate monster heard
- **Translation**: 

---

### Verse 12 (Ramayana 0.837)
- **Original**: Canto IV. Virádha's Death. 819 Victorious Ráma's welcome word, And straight Kakutstha's son, the best Of men, in words like these addressed: “I yield, O chieftain, overthrown By might that vies with Indra's own. Till now my folly-blinded eyes Thee, hero, failed to recognize. Happy Kau[alyá! blest to be The mother of a son like thee! I know thee well, O chieftain, now: Ráma, the prince of men, art thou. There stands the high-born Maithil dame, There LakshmaG, lord of mighty fame. My name was Tumburu,408 for song Renowned among the minstrel throng: Cursed by Kuvera's stern decree I wear the hideous shape you see. But when I sued, his grace to crave, The glorious God this answer gave: “When Ráma, Da [aratha's son, Destroys thee and the fight is won, Thy proper shape once more assume, And heaven again shall give thee room.” When thus the angry God replied, No prayers could turn his wrath aside, And thus on me his fury fell For loving Rambhá's409 charms too well. Now through thy favour am I freed From the stern fate the God decreed, And saved, O tamer of the foe, [233] 408 Somewhat inconsistently with this part of the story Tumburu is mentioned in Book II, Canto XII as one of the Gandharvas or heavenly minstrels summoned to perform at Bharadvája's feast. 409 Rambhá appears in Book I Canto LXIV as the temptress of Vi[vámitra.
- **Translation**: 

---

### Verse 13 (Ramayana 0.838)
- **Original**: 820 The Ramayana By thee, to heaven again shall go. A league, O Prince, beyond this spot Stands holyZarabhanga's cot: The very sun is not more bright Than that most glorious anchorite: To him, O Ráma, quickly turn, And blessings from the hermit earn. First under earth my body throw, Then on thy way rejoicing go. Such is the law ordained of old For giants when their days are told: Their bodies laid in earth, they rise To homes eternal in the skies.” Thus, by the rankling dart oppressed, Kakutstha's offspring he addressed: In earth his mighty body lay, His spirit fled to heaven away. Thus spake Virádha ere he died; And Ráma to his brother cried: “Now dig we in this grove a pit His elephantine bulk to fit. And let the hollowed earth enfold This mighty giant fierce and bold.”
- **Translation**: 

---

### Verse 14 (Ramayana 0.839)
- **Original**: Canto IV. Virádha's Death. 821 This said, the valiant hero put Upon the giant's neck his foot. His spade obedient LakshmaG plied, And dug a pit both deep and wide By lofty souled Virádha's side. Then Raghu's son his foot withdrew, And down the mighty form they threw; One awful shout of joy he gave And sank into the open grave. The heroes, to their purpose true, In fight the cruel demon slew, And radiant with delight Deep in the hollowed earth they cast The monster roaring to the last, In their resistless might. Thus when they saw the warrior's steel No life-destroying blow might deal, The pair, for lore renowned, Deep in the pit their hands had made The unresisting giant laid, And killed him neath the ground. Upon himself the monster brought From Ráma's hand the death he sought With strong desire to gain: And thus the rover of the night Told Ráma, as they strove in fight, That swords might rend and arrows smite Upon his breast in vain. Thus Ráma, when his speech he heard, The giant's mighty form interred, Which mortal arms defied. With thundering crash the giant fell, And rock and cave and forest dell With echoing roar replied.
- **Translation**: 

---

### Verse 15 (Ramayana 0.840)
- **Original**: 822 The Ramayana The princes, when their task was done And freedom from the peril won, Rejoiced to see him die. Then in the boundless wood they strayed, Like the great sun and moon displayed Triumphant in the sky.410 Canto V. Sarabhanga. Then Ráma, having slain in fight Virádha of terrific might, With gentle words his spouse consoled, And clasped her in his loving hold. Then to his brother nobly brave The valiant prince his counsel gave: “Wild are these woods around us spread; And hard and rough the ground to tread: We, O my brother, ne'er have viewed So dark and drear a solitude: To Zarabhanga let us haste, Whom wealth of holy works has graced.” 410 The conclusion of this Canto is all a vain repetition: it is manifestly spurious and a very feeble imitation of Válmíki's style. SeeAdditional Notes.
- **Translation**: 

---

### Verse 16 (Ramayana 0.841)
- **Original**: Canto V. Sarabhanga. 823 Thus Ráma spoke, and took the road To Zarabhanga's pure abode. But near that saint whose lustre vied With Gods, by penance purified, With startled eyes the prince beheld A wondrous sight unparalleled. In splendour like the fire and sun He saw a great and glorious one. Upon a noble car he rode, And many a God behind him glowed: And earth beneath his feet unpressed411 The monarch of the skies confessed. Ablaze with gems, no dust might dim The bright attire that covered him. Arrayed like him, on every side High saints their master glorified. Near, borne in air, appeared in view His car which tawny coursers drew, Like silver cloud, the moon, or sun Ere yet the day is well begun. Wreathed with gay garlands, o'er his head A pure white canopy was spread, And lovely nymphs stood nigh to hold Fair chouris with their sticks of gold, Which, waving in each gentle hand, The forehead of their monarch fanned. God, saint, and bard, a radiant ring, Sang glory to their heavenly King: Forth into joyful lauds they burst As Indra with the sage conversed. Then Ráma, when his wondering eyes Beheld the monarch of the skies, [234] 411 “Even when he had alighted,” says the commentator: The feet of Gods do not touch the ground.
- **Translation**: 

---

### Verse 17 (Ramayana 0.842)
- **Original**: 824 The Ramayana To LakshmaG quickly called, and showed The car wherein Lord Indra rode: “See, brother, see that air-borne car, Whose wondrous glory shines afar: Wherefrom so bright a lustre streams That like a falling sun it seems: These are the steeds whose fame we know, Of heavenly race through heaven they go: These are the steeds who bear the yoke Of Zakra,412 Him whom all invoke. Behold these youths, a glorious band, Toward every wind a hundred stand: A sword in each right hand is borne, And rings of gold their arms adorn. What might in every broad deep chest And club-like arm is manifest! Clothed in attire of crimson hue They show like tigers fierce to view. Great chains of gold each warder deck, Gleaming like fire beneath his neck. The age of each fair youth appears Some score and five of human years: The ever-blooming prime which they Who live in heaven retain for aye: Such mien these lordly beings wear, Heroic youths, most bright and fair. Now, brother, in this spot, I pray, With the Videhan lady stay, Till I have certain knowledge who This being is, so bright to view.” 412 A name of Indra.
- **Translation**: 

---

### Verse 18 (Ramayana 0.843)
- **Original**: Canto V. Sarabhanga. 825 He spoke, and turning from the spot SoughtZarabhanga's hermit cot. But when the lord ofZachí413 saw The son of Raghu near him draw, He hastened of the sage to take His leave, and to his followers spake: “See, Ráma bends his steps this way, But ere he yet a word can say, Come, fly to our celestial sphere; It is not meet he see me here. Soon victor and triumphant he In fitter time shall look on me. Before him still a great emprise, A task too hard for others, lies.” Then with all marks of honour high The Thunderer bade the saint good-bye, And in his car which coursers drew Away to heaven the conqueror flew. Then Ráma, LakshmaG, and the dame, To Zarabhanga nearer came, Who sat beside the holy flame. Before the ancient sage they bent, And clasped his feet most reverent; Then at his invitation found A seat beside him on the ground. Then Ráma prayed the sage would deign Lord Indra's visit to explain; And thus at length the holy man In answer to his prayer began: 413 Zachí is the consort of Indra.
- **Translation**: 

---

### Verse 19 (Ramayana 0.844)
- **Original**: 826 The Ramayana “This Lord of boons has sought me here To waft me hence to Brahmá's sphere, Won by my penance long and stern,— A home the lawless ne'er can earn. But when I knew that thou wast nigh, To Brahmá's world I could not fly Until these longing eyes were blest With seeing thee, mine honoured guest. Since thou, O Prince, hast cheered my sight, Great-hearted lover of the right, To heavenly spheres will I repair And bliss supreme that waits me there. For I have won, dear Prince, my way To those fair worlds which ne'er decay, Celestial seat of Brahmá's reign: Be thine, with me, those worlds to gain.” Then master of all sacred lore, Spake Ráma to the saint once more: “I, even I, illustrious sage, Will make those worlds mine heritage: But now, I pray, some home assign Within this holy grove of thine.” Thus Ráma, Indra's peer in might, Addressed the aged anchorite: And he, with wisdom well endued, To Raghu's son his speech renewed:
- **Translation**: 

---

### Verse 20 (Ramayana 0.845)
- **Original**: Canto V. Sarabhanga. 827 “SutíkshGa's woodland home is near, A glorious saint of life austere, True to the path of duty; he With highest bliss will prosper thee. Against the stream thy course must be Of this fair brook Mandákiní, Whereon light rafts like blossoms glide; Then to his cottage turn aside. There lies thy path: but ere thou go, Look on me, dear one, till I throw Aside this mould that girds me in, As casts the snake his withered skin.” He spoke, the fire in order laid With holy oil due offerings made, And Zarabhanga, glorious sire, Laid down his body in the fire. Then rose the flame above his head, On skin, blood, flesh, and bones it fed, Till forth, transformed, with radiant hue Of tender youth, he rose anew, Far-shining in his bright attire Came Zarabhanga from the pyre: Above the home of saints, and those Who feed the quenchless flame,414 he rose: Beyond the seat of Gods he passed, And Brahmá's sphere was gained at last. [235] The noblest of the twice-born race, For holy works supreme in place, The Mighty Father there beheld Girt round by hosts unparalleled; 414 The spheres or mansions gained by those who have duly performed the sacrifices required of them. Different situations are assigned to these spheres, some placing them near the sun, others near the moon.
- **Translation**: 

---



--- End of Ramayan_batch_140.md ---


--- Start of Ramayan_batch_141.md ---

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

### Verse 1 (Ramayana 0.846)
- **Original**: 828 The Ramayana And Brahmá joying at the sight Welcomed the glorious anchorite. Canto VI. Ráma's Promise. When he his heavenly home had found, The holy men who dwelt around To Ráma flocked, whose martial fame Shone glorious as the kindled flame: Vaikhánasas415 who love the wild, Pure hermits Bálakhilyas416 styled, Good Samprakshálas,417 saints who live On rays which moon and daystar give: Those who with leaves their lives sustain And those who pound with stones their grain: And they who lie in pools, and those Whose corn, save teeth, no winnow knows: Those who for beds the cold earth use, And those who every couch refuse: And those condemned to ceaseless pains, Whose single foot their weight sustains: And those who sleep neath open skies, Whose food the wave or air supplies, And hermits pure who spend their nights 415 Hermits who live upon roots which they dig out of the earth: literally diggers, derived from the prefixviand khan to dig. 416 Generally, divine personages of the height of a man's thumb, produced from Brahmá's hair: here, according to the commentator followed by Gorresio, hermits who when they have obtained fresh food throw away what they had laid up before. 417 Sprung from the washings of VishGuu's feet.
- **Translation**: 

---

### Verse 2 (Ramayana 0.847)
- **Original**: Canto VI. Ráma's Promise. 829 On ground prepared for sacred rites; Those who on hills their vigil hold, Or dripping clothes around them fold: The devotees who live for prayer, Or the five fires418 unflinching bear. On contemplation all intent, With light that heavenly knowledge lent, They came to Ráma, saint and sage, InZarabhanga's hermitage. The hermit crowd around him pressed, And thus the virtuous chief addressed: “The lordship of the earth is thine, O Prince of old Ikshváku's line. Lord of the Gods is Indra, so Thou art our lord and guide below. Thy name, the glory of thy might, Throughout the triple world are bright: Thy filial love so nobly shown, Thy truth and virtue well are known. To thee, O lord, for help we fly, And on thy love of right rely: With kindly patience hear us speak, And grant the boon we humbly seek. That lord of earth were most unjust, Foul traitor to his solemn trust, Who should a sixth of all419 require, Nor guard his people like a sire. But he who ever watchful strives To guard his subjects' wealth and lives, Dear as himself or, dearer still, His sons, with earnest heart and will,— That king, O Raghu's son, secures 418 Four fires burning round them, and the sun above. 419 The tax allowed to the king by the Laws of Manu.
- **Translation**: 

---

### Verse 3 (Ramayana 0.848)
- **Original**: 830 The Ramayana High fame that endless years endures, And he to Brahmá's world shall rise, Made glorious in the eternal skies. Whate'er, by duty won, the meed Of saints whom roots and berries feed, One fourth thereof, for tender care Of subjects, is the monarch's share. These, mostly of the Bráhman race, Who make the wood their dwelling-place, Although a friend in thee they view, Fall friendless neath the giant crew. Come, Ráma, come, and see hard by The holy hermits' corpses lie, Where many a tangled pathway shows The murderous work of cruel foes. These wicked fiends the hermits kill— Who live on Chitrakúma's hill, And blood of slaughtered saints has dyed Mandákiní and Pampá's side. No longer can we bear to see The death of saint and devotee Whom through the forest day by day These Rákshasas unpitying slay. To thee, O Prince, we flee, and crave Thy guardian help our lives to save. From these fierce rovers of the night Defend each stricken anchorite. Throughout the world 'twere vain to seek An arm like thine to aid the weak. O Prince, we pray thee hear our call, And from these fiends preserve us all.” The son of Raghu heard the plaint Of penance-loving sage and saint,
- **Translation**: 

---

### Verse 4 (Ramayana 0.849)
- **Original**: Canto VII. Sutíkshna. 831 And the good prince his speech renewed To all the hermit multitude: “To me, O saints, ye need not sue: I wait the hests of all of you. I by mine own occasion led This mighty forest needs must tread, [236] And while I keep my sire's decree Your lives from threatening foes will free. I hither came of free accord To lend the aid by you implored, And richest meed my toil shall pay, While here in forest shades I stay. I long in battle strife to close. And slay these fiends, the hermits' foes, That saint and sage may learn aright My prowess and my brother's might.” Thus to the saints his promise gave That prince who still to virtue clave With never-wandering thought: And then with LakshmaG by his side, With penance-wealthy men to guide, SutíkshGa's home he sought. Canto VII. Sutíkshna.
- **Translation**: 

---

### Verse 5 (Ramayana 0.850)
- **Original**: 832 The Ramayana So Raghu's son, his foemen's dread, With Sítá and his brother sped, Girt round by many a twice-born sage, To good SutíkshGa's hermitage.420 Through woods for many a league he passed, O'er rushing rivers full and fast, Until a mountain fair and bright As lofty Meru rose in sight. Within its belt of varied wood Ikshváku's sons and Sítá stood, Where trees of every foliage bore Blossom and fruit in endless store. There coats of bark, like garlands strung, Before a lonely cottage hung, And there a hermit, dust-besmeared, A lotus on his breast, appeared. Then Ráma with obeisance due Addressed the sage, as near he drew: “My name is Ráma, lord; I seek Thy presence, saint, with thee to speak. O sage, whose merits ne'er decay, Some word unto thy servant say.” The sage his eyes on Ráma bent, Of virtue's friends preëminent; Then words like these he spoke, and pressed The son of Raghu to his breast: “Welcome to thee, illustrious youth, Best champion of the rights of truth! By thine approach this holy ground A worthy lord this day has found. I could not quit this mortal frame 420 Near the celebrated Rámagiri or Ráma's Hill, now Rám-mek, near Nag- pore— the scene of the Yaksha's exile in theMessenger Cloud.
- **Translation**: 

---

### Verse 6 (Ramayana 0.851)
- **Original**: Canto VII. Sutíkshna. 833 Till thou shouldst come, O dear to fame: To heavenly spheres I would not rise, Expecting thee with eager eyes. I knew that thou, unkinged, hadst made Thy home in Chitrakúma's shade. E'en now, O Ráma, Indra, lord Supreme by all the Gods adored, King of the Hundred Offerings,421 said, When he my dwelling visited, That the good works that I have done My choice of all the worlds have won. Accept this meed of holy vows, And with thy brother and thy spouse, Roam, through my favour, in the sky Which saints celestial glorify.” To that bright sage, of penance stern, The high-souled Ráma spake in turn, As Vásava422 who rules the skies To Brahmá's gracious speech replies: “I of myself those worlds will win, O mighty hermit pure from sin: But now, O saint, I pray thee tell Where I within this wood may dwell: For I byZarabhanga old, The son of Gautama, was told That thou in every lore art wise, And seest all with loving eyes.” 421 A hundred A[vamedhas or sacrifices of a horse raise the sacrificer to the dignity of Indra. 422 Indra.
- **Translation**: 

---

### Verse 7 (Ramayana 0.852)
- **Original**: 834 The Ramayana Thus to the saint, whose glories high Filled all the world, he made reply: And thus again the holy man His pleasant speech with joy began: “This calm retreat, O Prince, is blest With many a charm: here take thy rest. Here roots and kindly fruits abound, And hermits love the holy ground. Fair silvan beasts and gentle deer In herds unnumbered wander here: And as they roam, secure from harm, Our eyes with grace and beauty charm: Except the beasts in thickets bred, This grove of ours has naught to dread.” The hermit's speech when Ráma heard,— The hero ne'er by terror stirred,— On his great bow his hand he laid, And thus in turn his answer made: “O saint, my darts of keenest steel, Armed with their murderous barbs, would deal Destruction mid the silvan race That flocks around thy dwelling-place. Most wretched then my fate would be For such dishonour shown to thee: And only for the briefest stay Would I within this grove delay.” He spoke and ceased. With pious care He turned him to his evening prayer, Performed each customary rite, And sought his lodging for the night, With Sítá and his brother laid[237]
- **Translation**: 

---

### Verse 8 (Ramayana 0.853)
- **Original**: Canto VIII. The Hermitage. 835 Beneath the grove's delightful shade, First good SutíkshGa, as elsewhere, when he saw The shades of night around them draw, With hospitable care The princely chieftains entertained With store of choicest food ordained For holy hermit's fare. Canto VIII. The Hermitage. So Ráma and Sumitrá's son, When every honour due was done, Slept through the night. When morning broke, The heroes from their rest awoke. Betimes the son of Raghu rose, With gentle Sítá, from repose, And sipped the cool delicious wave Sweet with the scent the lotus gave, Then to the Gods and sacred flame The heroes and the lady came, And bent their heads in honour meet Within the hermit's pure retreat. When every stain was purged away, They saw the rising Lord of Day: Then to SutíkshGa's side they went, And softly spoke, most reverent:
- **Translation**: 

---

### Verse 9 (Ramayana 0.854)
- **Original**: 836 The Ramayana “Well have we slept, O holy lord, Honoured of thee by all adored: Now leave to journey forth we pray: These hermits urge us on our way. We haste to visit, wandering by, The ascetics' homes that round you lie, And roaming DaG ak's mighty wood To view each saintly brotherhood, For thy permission now we sue, With these high saints to duty true, By penance taught each sense to tame,— In lustre like the smokeless flame. Ere on our brows the sun can beat With fierce intolerable heat. Like some unworthy lord who wins His power by tyranny and sins, O saint, we fain would part.” The three Bent humbly to the devotee. He raised the princes as they pressed His feet, and strained them to his breast; And then the chief of devotees Bespake them both in words like these: “Go with thy brother, Ráma, go, Pursue thy path untouched by woe: Go with thy faithful Sítá, she Still like a shadow follows thee. Roam Da G ak wood observing well The pleasant homes where hermits dwell,— Pure saints whose ordered souls adhere To penance rites and vows austere. There plenteous roots and berries grow, And noble trees their blossoms show, And gentle deer and birds of air In peaceful troops are gathered there.
- **Translation**: 

---

### Verse 10 (Ramayana 0.855)
- **Original**: Canto VIII. The Hermitage. 837 There see the full-blown lotus stud The bosom of the lucid flood, And watch the joyous mallard shake The reeds that fringe the pool and lake. See with delighted eye the rill Leap sparkling from her parent hill, And hear the woods that round thee lie Reëcho to the peacock's cry. And as I bid thy brother, so, Sumitrá's child, I bid thee go. Go forth, these varied beauties see, And then once more return to me.” Thus spake the sage SutíkshGa: both The chiefs assented, nothing loth, Round him with circling steps they paced, Then for the road prepared with haste. There Sítá stood, the dame long-eyed, Fair quivers round their waists she tied, And gave each prince his trusty bow, And sword which ne'er a spot might know. Each took his quiver from her hand. And clanging bow and gleaming brand: Then from the hermits' home the two Went forth each woodland scene to view. Each beauteous in the bloom of age, Dismissed by that illustrious sage, With bow and sword accoutred, hied Away, and Sítá by their side.
- **Translation**: 

---

### Verse 11 (Ramayana 0.856)
- **Original**: 838 The Ramayana Canto IX. Sítá's Speech. Blest by the sage, when Raghu's son His onward journey had begun, Thus in her soft tone Sítá, meek With modest fear, began to speak: “One little slip the great may lead To shame that follows lawless deed: Such shame, my lord, as still must cling To faults from low desire that spring. Three several sins defile the soul, Born of desire that spurns control: First, utterance of a lying word, Then, viler both, the next, and third: The lawless love of other's wife, The thirst of blood uncaused by strife. The first, O Raghu's son, in thee None yet has found, none e'er shall see. Love of another's dame destroys All merit, lost for guilty joys: Ráma, such crime in thee, I ween, Has ne'er been found, shall ne'er be seen: The very thought, my princely lord, Is in thy secret soul abhorred.[238] For thou hast ever been the same Fond lover of thine own dear dame, Content with faithful heart to do Thy father's will, most just and true: Justice, and faith, and many a grace In thee have found a resting-place. Such virtues, Prince, the good may gain Who empire o'er each sense retain; And well canst thou, with loving view Regarding all, each sense subdue.
- **Translation**: 

---

### Verse 12 (Ramayana 0.857)
- **Original**: Canto IX. Sítá's Speech. 839 But for the third, the lust that strives, Insatiate still, for others' lives,— Fond thirst of blood where hate is none,— This, O my lord, thou wilt not shun. Thou hast but now a promise made, The saints of DaG ak wood to aid: And to protect their lives from ill The giants' blood in tight wilt spill: And from thy promise lasting fame Will glorify the forest's name. Armed with thy bow and arrows thou Forth with thy brother journeyest now, While as I think how true thou art Fears for thy bliss assail my heart, And all my spirit at the sight Is troubled with a strange affright. I like it not— it seems not good— Thy going thus to DaG ak wood: And I, if thou wilt mark me well, The reason of my fear will tell. Thou with thy brother, bow in hand, Beneath those ancient trees wilt stand, And thy keen arrows will not spare Wood-rovers who will meet thee there. For as the fuel food supplies That bids the dormant flame arise, Thus when the warrior grasps his bow He feels his breast with ardour glow. Deep in a holy grove, of yore, Where bird and beast from strife forbore, Zuchi beneath the sheltering boughs, A truthful hermit kept his vows. Then Indra,Zachí's heavenly lord, Armed like a warrior with a sword,
- **Translation**: 

---

### Verse 13 (Ramayana 0.858)
- **Original**: 840 The Ramayana Came to his tranquil home to spoil The hermit of his holy toil, And left the glorious weapon there Entrusted to the hermit's care, A pledge for him to keep, whose mind To fervent zeal was all resigned. He took the brand: with utmost heed He kept it for the warrior's need: To keep his trust he fondly strove When roaming in the neighbouring grove: Whene'er for roots and fruit he strayed Still by his side he bore the blade: Still on his sacred charge intent, He took his treasure when he went. As day by day that brand he wore, The hermit, rich in merit's store From penance rites each thought withdrew, And fierce and wild his spirit grew. With heedless soul he spurned the right, And found in cruel deeds delight. So, living with the sword, he fell, A ruined hermit, down to hell. This tale applies to those who deal Too closely with the warrior's steel: The steel to warriors is the same As fuel to the smouldering flame. Sincere affection prompts my speech: I honour where I fain would teach. Mayst thou, thus armed with shaft and bow, So dire a longing never know As, when no hatred prompts the fray, These giants of the wood to slay: For he who kills without offence Shall win but little glory thence.
- **Translation**: 

---

### Verse 14 (Ramayana 0.859)
- **Original**: Canto IX. Sítá's Speech. 841 The bow the warrior joys to bend Is lent him for a nobler end, That he may save and succour those Who watch in woods when pressed by foes. What, matched with woods, is bow or steel? What, warrior's arm with hermit's zeal? We with such might have naught to do: The forest rule should guide us too. But when Ayodhyá hails thee lord, Be then thy warrior life restored: So shall thy sire423 and mother joy In bliss that naught may e'er destroy. And if, resigning empire, thou Submit thee to the hermit's vow, The noblest gain from virtue springs, And virtue joy unending brings. All earthly blessings virtue sends: On virtue all the world depends. Those who with vow and fasting tame To due restraint the mind and frame, Win by their labour, nobly wise, The highest virtue for their prize. Pure in the hermit's grove remain, True to thy duty, free from stain. But the three worlds are open thrown To thee, by whom all things are known. Who gave me power that I should dare His duty to my lord declare? 'Tis woman's fancy, light as air, That moves my foolish breast. 423 Gorresio observes that Da[aratha was dead and that Sítá had been informed of his death. In his translation he substitutes for the words of the text“thy relations and mine.” This is quite superfluous. Da[aratha though in heaven still took a loving interest in the fortunes of his son.
- **Translation**: 

---

### Verse 15 (Ramayana 0.860)
- **Original**: 842 The Ramayana Now with thy brother counsel take, Reflect, thy choice with judgment make, And do what seems the best.” [239] Canto X. Ráma's Reply. The words that Sítá uttered, spurred By truest love, the hero heard: Then he who ne'er from virtue strayed To Janak's child his answer made: “In thy wise speech, sweet love, I find True impress of thy gentle mind, Well skilled the warrior's path to trace, Thou pride of Janak's ancient race. What fitting answer shall I frame To thy good words, my honoured dame? Thou sayst the warrior bears the bow That misery's tears may cease to flow; And those pure saints who love the shade Of DaG ak wood are sore dismayed. They sought me of their own accord, With suppliant prayers my aid implored: They, fed on roots and fruit, who spend Their lives where bosky wilds extend, My timid love, enjoy no rest By these malignant fiends distressed. These make the flesh of man their meat: The helpless saints they kill and eat. The hermits sought my side, the chief
- **Translation**: 

---

### Verse 16 (Ramayana 0.861)
- **Original**: Canto X. Ráma's Reply. 843 Of Bráhman race declared their grief. I heard, and from my lips there fell The words which thou rememberest well: I listened as the hermits cried, And to their prayers I thus replied: “Your favour, gracious lords, I claim, O'erwhelmed with this enormous shame That Bráhmans, great and pure as you, Who should be sought, to me should sue.” And then before the saintly crowd, “What can I do?” I cried aloud. Then from the trembling hermits broke One long sad cry, and thus they spoke: “Fiends of the wood, who wear at will Each varied shape, afflict us still. To thee in our distress we fly: O help us, Ráma, or we die. When sacred rites of fire are due, When changing moons are full or new, These fiends who bleeding flesh devour Assail us with resistless power. They with their cruel might torment The hermits on their vows intent: We look around for help and see Our surest refuge, Prince, in thee. We, armed with powers of penance, might Destroy the rovers of the night: But loth were we to bring to naught The merit years of toil have bought. Our penance rites are grown too hard, By many a check and trouble barred, But though our saints for food are slain The withering curse we yet restrain.
- **Translation**: 

---

### Verse 17 (Ramayana 0.862)
- **Original**: 844 The Ramayana Thus many a weary day distressed By giants who this wood infest, We see at length deliverance, thou With LakshmaG art our guardian now.” As thus the troubled hermits prayed, I promised, dame, my ready aid, And now — for truth I hold most dear— Still to my word must I adhere. My love, I might endure to be Deprived of LakshmaG, life, and thee, But ne'er deny my promise, ne'er To Bráhmans break the oath I sware. I must, enforced by high constraint, Protect them all. Each suffering saint In me, unasked, his help had found; Still more in one by promise bound. I know thy words, mine own dear dame, From thy sweet heart's affection came: I thank thee for thy gentle speech, For those we love are those we teach. 'Tis like thyself, O fair of face, 'Tis worthy of thy noble race: Dearer than life, thy feet are set In righteous paths they ne'er forget.” Thus to the Maithil monarch's child, His own dear wife, in accents mild The high-souled hero said: Then to the holy groves which lay Beyond them fair to see, their way The bow-armed chieftain led.
- **Translation**: 

---

### Verse 18 (Ramayana 0.863)
- **Original**: Canto XI. Agastya. 845 Canto XI. Agastya. Ráma went foremost of the three, Next Sítá, followed, fair to see, And Lakshma G with his bow in hand Walked hindmost of the little band. As onward through the wood they went, With great delight their eyes were bent On rocky heights beside the way And lofty trees with blossoms gay; And streamlets running fair and fast The royal youths with Sítá passed. They watched the sáras and the drake On islets of the stream and lake, And gazed delighted on the floods Bright with gay birds and lotus buds. They saw in startled herds the roes, The passion-frenzied buffaloes, Wild elephants who fiercely tore The tender trees, and many a boar. A length of woodland way they passed, And when the sun was low at last A lovely stream-fed lake they spied, Two leagues across from side to side. Tall elephants fresh beauty gave To grassy bank and lilied wave, [240] By many a swan and sáras stirred, Mallard, and gay-winged water-bird. From those sweet waters, loud and long, Though none was seen to wake the song, Swelled high the singer's music blent With each melodious instrument. Ráma and car-borne LakshmaG heard The charming strain, with wonder stirred,
- **Translation**: 

---

### Verse 19 (Ramayana 0.864)
- **Original**: 846 The Ramayana Turned on the margent of the lake To Dharmabhrit424 the sage, and spake: “Our longing souls, O hermit, burn This music of the lake to learn: We pray thee, noblest sage, explain The cause of the mysterious strain.” He, as the son of Raghu prayed, With swift accord his answer made, And thus the hermit, virtuous-souled, The story of the fair lake told: “Through every age 'tis known to fame, Panchápsaras425 its glorious name, By holy MáG akarGi wrought With power his rites austere had bought. For he, great votarist, intent On strictest rule his stern life spent. Ten thousand years the stream his bed, Ten thousand years on air he fed. Then on the blessed Gods who dwell In heavenly homes great terror fell: They gathered all, by Agni led, And counselled thus disquieted: “The hermit by ascetic pain The seat of one of us would gain.” Thus with their hearts by fear oppressed In full assembly spoke the Blest, And bade five loveliest nymphs, as fair As lightning in the evening air, Armed with their winning wiles, seduce From his stern vows the great recluse. 424 One of the hermits who had followed Ráma. 425 The lake of the five nymphs.
- **Translation**: 

---

### Verse 20 (Ramayana 0.865)
- **Original**: Canto XI. Agastya. 847 Though lore of earth and heaven he knew, The hermit from his task they drew, And made the great ascetic slave To conquering love, the Gods to save. Each of the heavenly five became, Bound to the sage, his wedded dame; And he, for his beloved's sake, Formed a fair palace neath the lake. Under the flood the ladies live, To joy and ease their days they give, And lap in bliss the hermit wooed From penance rites to youth renewed. So when the sportive nymphs within Those secret bowers their play begin, You hear the singers' dulcet tones Blend sweetly with their tinkling zones.” “How wondrous are these words of thine!” Cried the famed chiefs of Raghu's line, As thus they heard the sage unfold The marvels of the tale he told. As Ráma spake, his eyes were bent Upon a hermit settlement With light of heavenly lore endued, With sacred grass and vesture strewed. His wife and brother by his side, Within the holy bounds he hied, And there, with honour entertained By all the saints, a while remained. In time, by due succession led, Each votary's cot he visited, And then the lord of martial lore, Returned where he had lodged before.
- **Translation**: 

---



--- End of Ramayan_batch_141.md ---


--- Start of Ramayan_batch_142.md ---

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

### Verse 1 (Ramayana 0.866)
- **Original**: 848 The Ramayana Here for the months, content, he stayed, There for a year his visit paid: Here for four months his home would fix, There, as it chanced, for five or six. Here for eight months and there for three The son of Raghu's stay would be: Here weeks, there fortnights, more or less, He spent in tranquil happiness. As there the hero dwelt at ease Among those holy devotees, In days untroubled o'er his head Ten circling years of pleasure fled. So Raghu's son in duty trained A while in every cot remained, Then with his dame retraced the road To good SutíkshGa's calm abode. Hailed by the saints with honours due Near to the hermit's home he drew, And there the tamer of his foes Dwelt for a time in sweet repose. One day within that holy wood By saint SutíkshGa Ráma stood, And thus the prince with reverence meek To that high sage began to speak: “In the wide woodlands that extend Around us, lord most reverend, As frequent voice of rumour tells, Agastya, saintliest hermit, dwells. So vast the wood, I cannot trace The path to reach his dwelling place, Nor, searching unassisted, find That hermit of the thoughtful mind. I with my wife and brother fain
- **Translation**: 

---

### Verse 2 (Ramayana 0.867)
- **Original**: Canto XI. Agastya. 849 Would go, his favour to obtain, Would seek him in his lone retreat And the great saint with reverence greet. This one desire, O Master, long Cherished within my heart, is strong, That I may pay of free accord My duty to that hermit lord.” As thus the prince whose heart was bent On virtue told his firm intent, The good SutíkshGa's joy rose high, And thus in turn he made reply: “The very thing, O Prince, which thou Hast sought, I wished to urge but now, Bid thee with wife and brother see [241] Agastya, glorious devotee. I count this thing an omen fair That thou shouldst thus thy wish declare, And I, my Prince, will gladly teach The way Agastya's home to reach. Southward, dear son, direct thy feet Eight leagues beyond this still retreat: Agastya's hermit brother there Dwells in a home most bright and fair. 'Tis on a knoll of woody ground, With many a branching Pippal426 crowned: There sweet birds' voices ne'er are mute, And trees are gay with flower and fruit. There many a lake gleams bright and cool, And lilies deck each pleasant pool, While swan, and crane, and mallard's wings Are lovely in the water-springs. There for one night, O Ráma, stay, 426 The holy fig-tree.
- **Translation**: 

---

### Verse 3 (Ramayana 0.868)
- **Original**: 850 The Ramayana And with the dawn pursue thy way. Still farther, bending southward, by The thicket's edge the course must lie, And thou wilt see, two leagues from thence Agastya's lovely residence, Set in the woodland's fairest spot, All varied foliage decks the cot: There Sítá, LakshmaG thou, at ease May spend sweet hours neath shady trees, For all of noblest growth are found Luxuriant on that bosky ground. If it be still thy firm intent To see that saint preëminent, O mighty counsellor, this day Depart upon thine onward way.” The hermit spake, and Ráma bent His head, with LakshmaG, reverent, And then with him and Janak's child Set out to trace the forest wild. He saw dark woods that fringed the road, And distant hills like clouds that showed, And, as the way he followed, met With many a lake and rivulet. So passing on with ease where led The path SutíkshGa bade him tread, The hero with exulting breast His brother in these words addressed: “Here, surely, is the home, in sight, Of that illustrious anchorite: Here great Agastya's brother leads A life intent on holy deeds. Warned of each guiding mark and sign,
- **Translation**: 

---

### Verse 4 (Ramayana 0.869)
- **Original**: Canto XI. Agastya. 851 I see them all herein combine: I see the branches bending low Beneath the flowers and fruit they show. A soft air from the forest springs, Fresh from the odorous grass, and brings A spicy fragrance as it flees O'er the ripe fruit of Pippal trees. See, here and there around us high Piled up in heaps cleft billets lie, And holy grass is gathered, bright As strips of shining lazulite. Full in the centre of the shade The hermits' holy fire is laid: I see its smoke the pure heaven streak Dense as a big cloud's dusky peak. The twice-born men their steps retrace From each sequestered bathing-place, And each his sacred gift has brought Of blossoms which his hands have sought. Of all these signs, dear brother, each Agrees with good SutíkshGa's speech, And doubtless in this holy bound Agastya's brother will be found. Agastya once, the worlds who viewed With love, a Deathlike fiend subdued, And armed with mighty power, obtained By holy works, this grove ordained To be a refuge and defence From all oppressors' violence. In days of yore within this place Two brothers fierce of demon race, Vátápi dire and Ilval, dwelt, And slaughter mid the Bráhmans dealt. A Bráhman's form, the fiend to cloak,
- **Translation**: 

---

### Verse 5 (Ramayana 0.870)
- **Original**: 852 The Ramayana Fierce Ilval wore, and Sanskrit spoke, And twice-born sages would invite To solemnize some funeral rite. His brother's flesh, concealed within A ram's false shape and borrowed skin,— As men are wont at funeral feasts,— He dressed and fed those gathered priests. The holy men, unweeting ill, Took of the food and ate their fill. Then Ilval with a mighty shout Exclaimed“Vátápi, issue out.” Soon as his brother's voice he heard, The fiend with ram-like bleating stirred: Rending in pieces every frame, Forth from the dying priests he came. So they who changed their forms at will Thousands of Bráhmans dared to kill,— Fierce fiends who loved each cruel deed, And joyed on bleeding flesh to feed. Agastya, mighty hermit, pressed To funeral banquet like the rest, Obedient to the Gods' appeal Ate up the monster at a meal. “'Tis done, 'tis done,” fierce Ilval cried, And water for his hands supplied: Then lifting up his voice he spake: “Forth, brother, from thy prison break.” Then him who called the fiend, who long Had wrought the suffering Bráhmans wrong, Thus thoughtful-souled Agastya, best Of hermits, with a smile addressed: “How, Rákshas, is the fiend empowered To issue forth whom I devoured? Thy brother in a ram's disguise
- **Translation**: 

---

### Verse 6 (Ramayana 0.871)
- **Original**: Canto XI. Agastya. 853 Is gone where Yáma's kingdom lies.” [242] When from the words Agastya said He knew his brother fiend was dead, His soul on fire with vengeful rage, Rushed the night-rover at the sage. One lightning glance of fury, hot As fire, the glorious hermit shot, As the fiend neared him in his stride, And straight, consumed to dust, he died. In pity for the Bráhmans' plight Agastya wrought this deed of might: This grove which lakes and fair trees grace In his great brother's dwelling place.” As Ráma thus the tale rehearsed, And with Sumitrá's son conversed, The setting sun his last rays shed, And evening o'er the land was spread. A while the princely brothers stayed And even rites in order paid, Then to the holy grove they drew And hailed the saint with honour due. With courtesy was Ráma met By that illustrious anchoret, And for one night he rested there Regaled with fruit and hermit fare. But when the night had reached its close, And the sun's glorious circle rose, The son of Raghu left his bed And to the hermit's brother said: “Well rested in thy hermit cell, I stand, O saint, to bid farewell; For with thy leave I journey hence Thy brother saint to reverence.”
- **Translation**: 

---

### Verse 7 (Ramayana 0.872)
- **Original**: 854 The Ramayana “Go, Ráma go,” the sage replied: Then from the cot the chieftain hied. And while the pleasant grove he viewed, The path the hermit showed, pursued. Of every leaf, of changing hue. Plants, trees by hundreds round him grew, With joyous eyes he looked on all, Then Jak,427 the wild rice, and Sál;428 He saw the red Hibiscus glow, He saw the flower-tipped creeper throw The glory of her clusters o'er Tall trees that loads of blossom bore. Some, elephants had prostrate laid, In some the monkeys leapt and played, And through the whole wide forest rang The charm of gay birds as they sang. Then Ráma of the lotus eye To LakshmaG turned who followed nigh, And thus the hero youth impressed With Fortune's favouring signs, addressed: “How soft the leaves of every tree, How tame each bird and beast we see! Soon the fair home shall we behold Of that great hermit tranquil-souled. The deed the good Agastya wrought High fame throughout the world has bought: I see, I see his calm retreat That balms the pain of weary feet. Where white clouds rise from flames beneath, Where bark-coats lie with many a wreath, Where silvan things, made gentle, throng, 427 The bread-fruit tree, Artocarpus integrifolia. 428 A fine timber tree, Shorea robusta.
- **Translation**: 

---

### Verse 8 (Ramayana 0.873)
- **Original**: Canto XI. Agastya. 855 And every bird is loud in song. With ruth for suffering creatures filled, A deathlike fiend with might he killed, And gave this southern realm to be A refuge, from oppression free. There stands his home, whose dreaded might Has put the giant crew to flight, Who view with envious eyes afar The peaceful shades they cannot mar. Since that most holy saint has made His dwelling in this lovely shade, Checked by his might the giant brood Have dwelt in peace with souls subdued. And all this southern realm, within Whose bounds no fiend may entrance win, Now bears a name which naught may dim, Made glorious through the worlds by him. When Vindhya, best of hills, would stay The journey of the Lord of Day, Obedient to the saint's behest He bowed for aye his humbled crest. That hoary hermit, world-renowned For holy deeds, within this ground Has set his pure and blessed home, Where gentle silvan creatures roam. Agastya, whom the worlds revere, Pure saint to whom the good are dear, To us his guests all grace will show, Enriched with blessings ere we go. I to this aim each thought will turn, The favour of the saint to earn, That here in comfort may be spent The last years of our banishment. Here sanctities and high saints stand,
- **Translation**: 

---

### Verse 9 (Ramayana 0.874)
- **Original**: 856 The Ramayana Gods, minstrels of the heavenly band; Upon Agastya's will they wait, And serve him, pure and temperate. The liar's tongue, the tyrant's mind Within these bounds no home may find: No cheat, no sinner here can be: So holy and so good is he. Here birds and lords of serpent race, Spirits and Gods who haunt the place, Content with scanty fare remain, As merit's meed they strive to gain. Made perfect here, the saints supreme, On cars that mock the Day-God's gleam,— Their mortal bodies cast aside,— Sought heaven transformed and glorified, Here Gods to living things, who win Their favour, pure from cruel sin, Give royal rule and many a good,[243] Immortal life and spirithood. Now, LakshmaG, we are near the place: Do thou precede a little space, And tell the mighty saint that I With Sítá at my side am nigh.” Canto XII. The Heavenly Bow. He spoke: the younger prince obeyed: Within the bounds his way he made, And thus addressed, whom first he met, A pupil of the anchoret:
- **Translation**: 

---

### Verse 10 (Ramayana 0.875)
- **Original**: Canto XII. The Heavenly Bow. 857 “Brave Ráma, eldest born, who springs, From Da[aratha, hither brings His wife the lady Sítá: he Would fain the holy hermit see. Lakshma G am I— if happy fame E'er to thine ears has brought the name— His younger brother, prompt to do His will, devoted, fond, and true. We, through our royal sire's decree, To the dread woods were forced to flee. Tell the great Master, I entreat, Our earnest wish our lord to greet.” He spoke: the hermit rich in store Of fervid zeal and sacred lore, Sought the pure shrine which held the fire, To bear his message to the sire. Soon as he reached the saint most bright In sanctity's surpassing might, He cried, uplifting reverent hands: “Lord Ráma near thy cottage stands.” Then spoke Agastya's pupil dear The message for his lord to hear: “Ráma and LakshmaG, chiefs who spring From Da[aratha, glorious king, Thy hermitage e'en now have sought, And lady Sítá with them brought. The tamers of the foe are here To see thee, Master, and revere. 'Tis thine thy further will to say: Deign to command, and we obey.”
- **Translation**: 

---

### Verse 11 (Ramayana 0.876)
- **Original**: 858 The Ramayana When from his pupil's lips he knew The presence of the princely two, And Sítá born to fortune high. The glorious hermit made reply: “Great joy at last is mine this day That Ráma hither finds his way, For long my soul has yearned to see The prince who comes to visit me. Go forth, go forth, and hither bring The royal three with welcoming: Lead Ráma in and place him near: Why stands he not already here?” Thus ordered by the hermit, who, Lord of his thought, all duty knew, His reverent hands together laid, The pupil answered and obeyed. Forth from the place with speed he ran, To LakshmaG came and thus began: “Where is he? let not Ráma wait, But speed, the sage to venerate.” Then with the pupil LakshmaG went Across the hermit settlement, And showed him Ráma where he stood With Janak's daughter in the wood. The pupil then his message spake Which the kind hermit bade him take; Then led the honoured Ráma thence And brought him in with reverence. As nigh the royal Ráma came With LakshmaG and the Maithil dame, He viewed the herds of gentle deer Roaming the garden free from fear.
- **Translation**: 

---

### Verse 12 (Ramayana 0.877)
- **Original**: Canto XII. The Heavenly Bow. 859 As through the sacred grove he trod He viewed the seat of many a God, Brahmá and Agni,429 Sun and Moon, And His who sends each golden boon;430 Here VishGu's stood, there Bhaga's431 shrine, And there Mahendra's, Lord divine; Here His who formed this earthly frame,432 His there from whom all beings came.433 Váyu's,434 and His who loves to hold The great noose, VaruG435 mighty-souled: Here was the Vasus'436 shrine to see, Here that of sacred Gáyatrí,437 The king of serpents438 here had place, And he who rules the feathered race.439 Here Kártikeya,440 warrior lord, And there was Justice King adored. Then with disciples girt about The mighty saint himself came out: Through fierce devotion bright as flame Before the rest the Master came: And then to LakshmaG, fortune blest, Ráma these hasty words addressed: “Behold, Agastya's self draws near, 429 The God of fire. 430 Kuvera, the God of riches. 431 The Sun. 432 Brahmá, the creator. 433 Ziva. 434 The Wind-God. 435 The God of the sea. 436 A class of demi-gods, eight in number. 437 The holiest text of the Vedas, deified. 438 Vásuki. 439 Garu . 440 The War-God.
- **Translation**: 

---

### Verse 13 (Ramayana 0.878)
- **Original**: 860 The Ramayana The mighty saint, whom all revere: With spirit raised I meet my lord With richest wealth of penance stored.” The strong-armed hero spake, and ran Forward to meet the sunbright man. Before him, as he came, he bent And clasped his feet most reverent, Then rearing up his stately height Stood suppliant by the anchorite, While LakshmaG's strength and Sítá's grace Stood by the pride of Raghu's race.[244] The sage his arms round Ráma threw And welcomed him with honours due, Asked, was all well, with question sweet, And bade the hero to a seat. With holy oil he fed the flame, He brought the gifts which strangers claim, And kindly waiting on the three With honours due to high degree, He gave with hospitable care A simple hermit's woodland fare. Then sat the reverend father, first Of hermits, deep in duty versed. And thus to suppliant Ráma, bred In all the lore of virtue, said: “Did the false hermit, Prince, neglect To hail his guest with due respect, He must,— the doom the perjured meet,— His proper flesh hereafter eat. A car-borne king, a lord who sways The earth, and virtue's law obeys, Worthy of highest honour, thou Hast sought, dear guest, my cottage now.”
- **Translation**: 

---

### Verse 14 (Ramayana 0.879)
- **Original**: Canto XII. The Heavenly Bow. 861 He spoke: with fruit and hermit fare, With every bloom the branches bare, Agastya graced his honoured guest, And thus with gentle words addressed: “Accept this mighty bow, divine, Whereon red gold and diamonds shine; 'Twas by the Heavenly Artist planned For VishGu's own almighty hand; This God-sent shaft of sunbright hue, Whose deadly flight is ever true, By Lord Mahendra given of yore: This quiver with its endless store. Keen arrows hurtling to their aim Like kindled fires that flash and flame: Accept, in golden sheath encased, This sword with hilt of rich gold graced. Armed with this best of bows Lord VishGu slew his demon foes, And mid the dwellers in the skies Won brilliant glory for his prize. The bow, the quivers, shaft, and sword Received from me, O glorious lord: These conquest to thine arm shall bring, As thunder to the thunder's King.” The splendid hermit bade him take The noble weapons as he spake, And as the prince accepted each In words like these renewed his speech:
- **Translation**: 

---

### Verse 15 (Ramayana 0.880)
- **Original**: 862 The Ramayana Canto XIII. Agastya's Counsel. “O Ráma, great delight I feel, Pleased, LakshmaG, with thy faithful zeal, That you within these shades I see With Sítá come to honour me. But wandering through the rough rude wild Has wearied Janak's gentle child: With labours of the way oppressed The Maithil lady longs for rest. Young, delicate, and soft, and fair, Such toils as these untrained to bear, Her wifely love the dame has led The forest's troubled ways to tread. Here, Ráma, see that naught annoy Her easy hours of tranquil joy: A glorious task has she assayed, To follow thee through woodland shade. Since first from Nature's hand she came, A woman's mood is still the same, When Fortune smiles, her love to show, And leave her lord in want and woe. No pity then her heart can feel, She arms her soul with warrior's steel, Swift as the storm or Feathered King, Uncertain as the lightning's wing. Not so thy spouse: her purer mind Shrinks from the faults of womankind; Like chaste Arundhatí441 above, A paragon of faithful love. Let these blest shades, dear Ráma, be A home for LakshmaG, her, and thee.” 441 One of the Pleiades generally regarded as the model of wifely excellence.
- **Translation**: 

---

### Verse 16 (Ramayana 0.881)
- **Original**: Canto XIII. Agastya's Counsel. 863 With raised hands reverently meek He heard the holy hermit speak, And humbly thus addressed the sire Whose glory shone like kindled fire: “How blest am I, what thanks I owe That our great Master deigns to show His favour, that his heart can be Content with LakshmaG, Sítá, me. Show me, I pray, some spot of ground Where thick trees wave and springs abound, That I may raise my hermit cell And there in tranquil pleasure dwell.” Then thus replied Agastya, best Of hermits, to the chief's request: When for a little he had bent His thoughts, upon that prayer intent: “Beloved son, four leagues away Is Panchavamí bright and gay: Thronged with its deer, most fair it looks With berries, fruit, and water-brooks. There build thee with thy brother's aid A cottage in the quiet shade, And faithful to thy sire's behest, Obedient to the sentence, rest. For well, O sinless chieftain, well I know thy tale, how all befell: Stern penance and the love I bore Thy royal sire supply the lore. To me long rites and fervid zeal The wish that stirs thy heart reveal, And hence my guest I bade thee be, That this pure grove might shelter thee. [245]
- **Translation**: 

---

### Verse 17 (Ramayana 0.882)
- **Original**: 864 The Ramayana So now, thereafter, thus I speak: The shades of Panchavamí seek; That tranquil spot is bright and fair, And Sítá will be happy there. Not far remote from here it lies, A grove to charm thy loving eyes, Godávarí's pure stream is nigh: There Sítá's days will sweetly fly. Pure, lovely, rich in many a charm, O hero of the mighty arm, 'Tis gay with every plant and fruit, And throngs of gay buds never mute. Thou, true to virtue's path, hast might To screen each trusting anchorite, And wilt from thy new home defend The hermits who on thee depend. Now yonder, Prince, direct thine eyes Where dense Madhúka442 woods arise: Pierce their dark shade, and issuing forth Turn to a fig-tree on the north: Then onward up a sloping mead Flanked by a hill the way will lead: There Panchavamí, ever gay With ceaseless bloom, thy steps will stay.” The hermit ceased: the princely two With seemly honours bade adieu: With reverential awe each youth Bowed to the saint whose word was truth, And then, dismissed with Sítá, they To Panchavamí took their way. Thus when each royal prince had grasped 442 The Madhúka, or, as it is now called, Mahuwá, is the Bassia latifolia, a tree from whose blossoms a spirit is extracted.
- **Translation**: 

---

### Verse 18 (Ramayana 0.883)
- **Original**: Canto XIV. Jatáyus. 865 His warrior's mighty bow, and clasped His quiver to his side, With watchful eyes along the road The glorious saint Agastya showed, Dauntless in fight the brothers strode, And Sítá with them hied. Canto XIV. Jatáyus. Then as the son of Raghu made His way to Panchavamí's shade, A mighty vulture he beheld Of size and strength unparalleled. The princes, when the bird they saw, Approached with reverence and awe, And as his giant form they eyed, “Tell who thou art,” in wonder cried. The bird, as though their hearts to gain, Addressed them thus in gentlest strain; “In me, dear sons, the friend behold Your royal father loved of old.” He spoke: nor long did Ráma wait His sire's dear friend to venerate: He bade the bird declare his name And the high race of which he came. When Raghu's son had spoken, he Declared his name and pedigree, His words prolonging to disclose How all the things that be arose:
- **Translation**: 

---

### Verse 19 (Ramayana 0.884)
- **Original**: 866 The Ramayana “List while I tell, O Raghu's son, The first-born Fathers, one by one, Great Lords of Life, whence all in earth And all in heaven derive their birth. First Kardam heads the glorious race Where Vikrit holds the second place, With Zesha, San[ray next in line, And Bahuputra's might divine. Then StháGu and Maríchi came, Atri, and Kratu's forceful frame. Pulastya followed, next to him Angiras' name shall ne'er be dim. Prachetas, Pulah next, and then Daksha, Vivasvat praised of men: Aríshmanemi next, and last Ka [yap in glory unsurpassed. From Daksha,— fame the tale has told— : Three-score bright daughters sprang of old. Of these fair-waisted nymphs the great Lord Ka[yap sought and wedded eight, Aditi, Diti, Kálaká, Támrá, Danú, and Analá, And Krodhavasá swift to ire, And Manu 443 glorious as her sire. 443 “I should have doubted whether Manu could have been the right reading here, but that it occurs again in verse 29, where it is in like manner followed in verse 31 by Analá, so that it would certainly seem that the name Manu is intended to stand for a female, the daughter of Daksha. The Gau a recension, followed by Signor Gorresio (III 20, 12), adopts an entirely different reading at the end of the line, viz.Balám Atibalám api,‘Balá and Atibilá,’instead of Manu and Analá. I see that Professor Roth s.v. adduces the authority of the Amara Kosha and of the Commentator on PáGini for stating that the word sometimes means ‘the wife of Manu.’ In the following text of the Mahábhárata I. 2553. also, Manu appears to be the name of a female:‘Anaradyam ,Manum ,Vañsám , Asurám,Márga Gapriyám,Anúpám ,Subhagám ,Bhásím iti,Prádhá vyajayata.
- **Translation**: 

---

### Verse 20 (Ramayana 0.885)
- **Original**: Canto XIV. Jatáyus. 867 Then when the mighty Ka[yap cried Delighted to each tender bride: “Sons shalt thou bear, to rule the three Great worlds, in might resembling me.” [246] Aditi, Diti, and Danú Obeyed his will as consorts true, And Kálaká; but all the rest Refused to hear their lord's behest. First Aditi conceived, and she, Mother of thirty Gods and three, The Vasus and Ádityas bare, Rudras, and A[vins, heavenly pair. Of Diti sprang the Daityas: fame Delights to laud their ancient name. In days of yore their empire dread O'er earth and woods and ocean spread. Danú was mother of a child, O hero, A[vagríva styled, And Narak next and Kálak came Of Kálaká, celestial dame. Of Támrá, too, five daughters bright In deathless glory sprang to light. Ennobling fame still keeps alive The titles of the lovely five: Immortal honour still she claims For Kraunchí, Bhasí,Zyení's names. And wills not that the world forget Zukí or Dhritaráshtrí yet. Then Kraunchí bare the crane and owl, And Bhásí tribes of water fowl: Vultures and hawks that race through air With storm-fleet pinionsZyení bare. Prádhá (daughter of Daksha) bore Anavadyá, Manu, Van[á, MárgaGapriyá, Anúpá, Subhagá. and Bhásí.’ ”Muir's Sanskrit Text, Vol. I. p. 116.
- **Translation**: 

---



--- End of Ramayan_batch_142.md ---


--- Start of Ramayan_batch_143.md ---

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

### Verse 1 (Ramayana 0.886)
- **Original**: 868 The Ramayana All swans and geese on mere and brook Their birth from Dhritaráshtrí took, And all the river-haunting brood Of ducks, a countless multitude. From Zukí Nalá sprang, who bare Dame Vinatá surpassing fair. From fiery Krodhava[á, ten Bright daughters sprang, O King of men: Mrigí and Mrigamandá named, Hari and Bhadramadá famed, Zárdúlí,Zvetá fair to see, Mátangí bright, and Surabhí, Surasá marked with each fair sign, And Kadrumá, all maids divine. Mrigí, O Prince without a peer, Was mother of the herds of deer, The bear, the yak, the mountain roe Their birth to Mrigamandá owe; And Bhadramadá joyed to be Mother of fair Irávatí, Who bare Airávat,444 huge of mould, Mid warders of the earth enrolled, From Harí lordly lions trace, With monkeys of the wild, their race. From the great dameZárdúlí styled Sprung pards, Lángúrs,445 and tigers wild. Mátangí, Prince, gave birth to all Mátangas, elephants strong and tall, And Zvetá bore the beasts who stand One at each wind, earth's warder band.446 444 The elephant of Indra. 445 Golángúlas, described as a kind of monkey, of a black colour, and having a tail like a cow. 446 Eight elephants attached to the four quarters and intermediate points of the
- **Translation**: 

---

### Verse 2 (Ramayana 0.887)
- **Original**: Canto XIV. Jatáyus. 869 Next Surabhí the Goddess bore Two heavenly maids, O Prince, of yore, Gandharví— dear to fame is she— And her sweet sister RohiGí. With kine this daughter filled each mead, And bright Gandharví bore the steed.447 Surasá bore the serpents:448 all The snakes Kadrú their mother call. Then Manu, high-souled Ka[yap's449 wife, To all the race of men gave life, The Bráhmans first, the Kshatriya caste, Then Vai[yas, and theZúdras last. Sprang from her mouth the Bráhman race; Her chest the Kshatriyas' natal place: The Vai[yas from her thighs, 'tis said, The Zúdras from her feet were bred. From Analá all trees that hang Their fair fruit-laden branches sprang. The child of beauteousZukí bore Vinatá, as I taught before: And Surasá and Kadrú were Born of one dame, a noble pair. Kadrú gave birth to countless snakes That roam the earth in woods and brakes. AruG and Garu swift of flight compass, to support and guard the earth. 447 Some scholars identify the centaurs with the Gandharvas. 448 The hooded serpents, says the commentator Tírtha, were the offspring of Surasá: all others of Kadrú. 449 The text reads Ka[yapa,“a descendant of Ka[yapa,” who according to Rám. II. l0, 6, ought to be Vivasvat. But as it is stated in the preceding part of this passage III. 14, 11 f. that Manu was one of Ka[yapa's eight wives, we must here read Ka[yap. The Ganda recension reads (III, 20, 30)Manur manushyáms cha tatha janayámása Rághana, instead of the corresponding line in the Bombay edition.Muir's Sanskrit Text, Vol I, p. 117.
- **Translation**: 

---

### Verse 3 (Ramayana 0.888)
- **Original**: 870 The Ramayana By Vinatá were given to light, And sons of AruG red as morn Sampati first, then I was born, Me then, O tamer of the foe, Jamáyus, son ofZyení, know. Thy ready helper will I be, And guard thy house, if thou agree: When thou and LakshmaG urge the chase By Sítá's side shall be my place.” With courteous thanks for promised aid, The prince, to rapture stirred, Bent low, and due obeisance paid, Embraced the royal bird.[247] He often in the days gone by Had heard his father tell How, linked with him in friendship's tie, He loved Jamáyus well. He hastened to his trusted friend His darling to confide, And through the wood his steps to bend By strong Jamáyus' side. On to the grove, with LakshmaG near, The prince his way pursued To free those pleasant shades from fear And slay the giant brood. Canto XV. Panchavatí.
- **Translation**: 

---

### Verse 4 (Ramayana 0.889)
- **Original**: Canto XV. Panchavatí. 871 Arrived at Panchavamí's shade Where silvan life and serpents strayed, Ráma in words like these addressed Lakshma G of vigour unrepressed: “Brother, our home is here: behold The grove of which the hermit told: The bowers of Panchavamí see Made fair by every blooming tree. Now, brother, bend thine eyes around; With skilful glance survey the ground: Here be some spot selected, best Approved for gentle hermits' rest, Where thou, the Maithil dame, and I May dwell while seasons sweetly fly. Some pleasant spot be chosen where Pure waters gleam and trees are fair, Some nook where flowers and wood are found And sacred grass and springs abound.” Then LakshmaG, Sítá standing by, Raised reverent hands, and made reply: “A hundred years shall flee, and still Will I obey my brother's will: Select thyself a pleasant spot; Be mine the care to rear the cot.” The glorious chieftain, pleased to hear That loving speech that soothed his ear, Selected with observant care A spot with every charm most fair. He stood within that calm retreat, A shade for hermits' home most meet, And thus Sumitrá's son addressed, While his dear hand in his he pressed:
- **Translation**: 

---

### Verse 5 (Ramayana 0.890)
- **Original**: 872 The Ramayana “See, see this smooth and lovely glade Which flowery trees encircling shade: Do thou, beloved LakshmaG rear A pleasant cot to lodge us here. I see beyond that feathery brake The gleaming of a lilied lake, Where flowers in sunlike glory throw Fresh odours from the wave below. Agastya's words now find we true, He told the charms which here we view: Here are the trees that blossom o'er Godávarí's most lovely shore. Whose pleasant flood from side to side With swans and geese is beautified, And fair banks crowded with the deer That steal from every covert near. The peacock's cry is loud and shrill From many a tall and lovely hill, Green-belted by the trees that wave Full blossoms o'er the rock and cave. Like elephants whose huge fronts glow With painted streaks, the mountains show Long lines of gold and silver sheen With copper's darker hues between. With every tree each hill is graced, Where creepers blossom interlaced. Look where the Sál's long branches sway, And palms their fanlike leaves display; The date-tree and the Jak are near, And their long stems Tamálas rear. See the tall Mango lift his head, A [okas all their glory spread, The Ketak her sweet buds unfold,
- **Translation**: 

---

### Verse 6 (Ramayana 0.891)
- **Original**: Canto XV. Panchavatí. 873 And Champacs hang their cups of gold.450 The spot is pure and pleasant: here Are multitudes of birds and deer. O Lakshma G, with our father's friend What happy hours we here shall spend!” He spoke: the conquering LakshmaG heard, Obedient to his brother's word. Raised by his toil a cottage stood To shelter Ráma in the wood, Of ample size, with leaves o'erlaid, Of hardened earth the walls were made. The strong bamboos his hands had felled For pillars fair the roof upheld, And rafter, beam, and lath supplied Well interwrought from side to side. Then Zamí451 boughs he deftly spread Enlaced with knotted cord o'erhead, Well thatched above from ridge to eaves With holy grass, and reed, and leaves. The mighty chief with careful toil Had cleared the ground and smoothed the soil [248] Where now, his loving labour done, Rose a fair home for Raghu's son. Then when his work was duly wrought, Godávarís sweet stream he sought, Bathed, plucked the lilies, and a store 450 The original verses merely name the trees. I have been obliged to amplify slightly and to omit some quas versu dicere non est;e.g.thetini[a (Dalber- gia ougeiniensis),punnága (Rottleria tinctoria),tilaka(not named),syandana (Dalbergia ougeiniensis again),vandana (unknown),nípa(Nauclea Kadamba), lakucha(Artœ arpus lacucha),dhava (Grislea tomentosa), A[vakarna (another name for the Sál),Zamí (Acacia Suma),khadira(Mimosa catechu),kin[uka (Butea frondosa),pátala(Bignonia suaveolens). 451 Acacia Suma.
- **Translation**: 

---

### Verse 7 (Ramayana 0.892)
- **Original**: 874 The Ramayana Of fruit and berries homeward bore. Then sacrifice he duly paid, And wooed the Gods their hopes to aid, And then to Ráma proudly showed The cot prepared for his abode. Then Raghu's son with Sítá gazed Upon the home his hands had raised, And transport thrilled his bosom through His leafy hermitage to view. The glorious son of Raghu round His brother's neck his arms enwound, And thus began his sweet address Of deep-felt joy and gentleness: “Well pleased am I, dear lord, to see This noble work performed by thee. For this,— sole grace I can bestow,— About thy neck mine arms I throw. So wise art thou, thy breast is filled With grateful thoughts, in duty skilled, Our mighty father, free from stain, In thee, his offspring, lives again.” Thus spoke the prince, who lent a grace To fortune, pride of Raghu's race; Then in that spot whose pleasant shade Gave store of fruit, content he stayed. With LakshmaG and his Maithil spouse He spent his day's neath sheltering boughs, As happy as a God on high Lives in his mansion in the sky.
- **Translation**: 

---

### Verse 8 (Ramayana 0.893)
- **Original**: Canto XVI. Winter. 875 Canto XVI. Winter. While there the high-souled hero spent His tranquil hours in sweet content, The glowing autumn passed, and then Came winter so beloved of men. One morn, to bathe, at break of day To the fair stream he took his way. Behind him, with the Maithil dame Bearing a pitcher LakshmaG came, And as he went the mighty man Thus to his brother chief began: “The time is come, to thee more dear Than all the months that mark the year: The gracious seasons' joy and pride, By which the rest are glorified. A robe of hoary rime is spread O'er earth, with corn engarlanded. The streams we loved no longer please, But near the fire we take our ease. Now pious men to God and shade Offer young corn's fresh sprouted blade, And purge away their sins with rice Bestowed in humble sacrifice. Rich stores of milk delight the swain, And hearts are cheered that longed for gain, Proud kings whose breasts for conquests glow Lead bannered troops to smite the foe. Dark is the north: the Lord of Day To Yáma's south452 has turned away: 452 The south is supposed to be the residence of the departed.
- **Translation**: 

---

### Verse 9 (Ramayana 0.894)
- **Original**: 876 The Ramayana And she— sad widow— shines no more, Reft of the bridal mark453 she wore. Himálaya's hill, ordained of old The treasure-house of frost and cold, Scarce conscious of the feebler glow, Is truly now the Lord of Snow. Warmed by the noontide's genial rays Delightful are the glorious days: But how we shudder at the chill Of evening shadows and the rill! How weak the sun, how cold the breeze! How white the rime on grass and trees! The leaves are sere, the woods have lost Their blossoms killed by nipping frost. Neath open skies we sleep no more: December's nights with rime are hoar: Their triple watch454 in length extends With hours the shortened daylight lends. No more the moon's sun-borrowed rays Are bright, involved in misty haze, As when upon the mirror's sheen The breath's obscuring cloud is seen. E'en at the full the faint beams fail To struggle through the darksome veil: Changed like her hue, they want the grace That parts not yet from Sítá's face. Cold is the western wind, but how Its piercing chill is heightened now, Blowing at early morning twice As furious with its breath of ice! See how the dewy tears they weep The barley, wheat, and woodland steep, 453 The sun. 454 The night is divided into three watches of four hours each.
- **Translation**: 

---

### Verse 10 (Ramayana 0.895)
- **Original**: Canto XVI. Winter. 877 Where, as the sun goes up the sky, The curlew and the sáras cry. See where the rice plants scarce uphold Their full ears tinged with paly gold, Bending their ripe heads slowly down Fair as the date tree's flowery crown. Though now the sun has mounted high Seeking the forehead of the sky, Such mist obscures his struggling beams, No bigger than the moon he seems. Though weak at first, his rays at length Grow pleasant in their noonday strength, And where a while they chance to fall Fling a faint splendour over all. [249] See, o'er the woods where grass is wet With hoary drops that cling there yet, With soft light clothing earth and bough There steals a tender glory now. Yon elephant who longs to drink, Still standing on the river's brink, Plucks back his trunk in shivering haste From the cold wave he fain would taste. The very fowl that haunt the mere Stand doubtful on the bank, and fear To dip them in the wintry wave As cowards dread to meet the brave. The frost of night, the rime of dawn Bind flowerless trees and glades of lawn: Benumbed in apathetic chill Of icy chains they slumber still. You hear the hidden sáras cry From floods that wrapped in vapour lie, And frosty-shining sands reveal Where the unnoticed rivers steal.
- **Translation**: 

---

### Verse 11 (Ramayana 0.896)
- **Original**: 878 The Ramayana The hoary rime of dewy night, And suns that glow with tempered light Lend fresh cool flavours to the rill That sparkles from the topmost hill. The cold has killed the lily's pride: Leaf, filament, and flower have died: With chilling breath rude winds have blown, The withered stalk is left alone. At this gay time, O noblest chief, The faithful Bharat, worn by grief, Lives in the royal town where he Spends weary hours for love of thee. From titles, honour, kingly sway, From every joy he turns away: Couched on cold earth, his days are passed With scanty fare and hermit's fast. This moment from his humble bed He lifts, perhaps, his weary head, And girt by many a follower goes To bathe where silver Sarjú flows. How, when the frosty morn is dim, Shall Sarjú be a bath for him Nursed with all love and tender care, So delicate and young and fair. How bright his hue! his brilliant eye With the broad lotus leaf may vie. By fortune stamped for happy fate, His graceful form is tall and straight. In duty skilled, his words are truth: He proudly rules each lust of youth. Though his strong arm smites down the foe, In gentle speech his accents flow. Yet every joy has he resigned And cleaves to thee with heart and mind.
- **Translation**: 

---

### Verse 12 (Ramayana 0.897)
- **Original**: Canto XVI. Winter. 879 Thus by the deeds that he has done A name in heaven has Bharat won, For in his life he follows yet Thy steps, O banished anchoret. Thus faithful Bharat, nobly wise, The proverb of the world belies: “No men, by mothers' guidance led, The footsteps of their fathers tread.” How could Kaikeyí, blest to be Spouse of the king our sire, and see A son like virtuous Bharat, blot Her glory with so foul a plot!” Thus in fraternal love he spoke, And from his lips reproaches broke: But Ráma grieved to hear him chide The absent mother, and replied: “Cease, O beloved, cease to blame Our royal father's second dame. Still speak of Bharat first in place Of old Ikshváku's princely race. My heart, so firmly bent but now To dwell in woods and keep my vow, Half melting as I hear thee speak Of Bharat's love, grows soft and weak, With tender joy I bring to mind His speeches ever sweet and kind. That dear as Amrit took the sense With most enchanting influence. Ah, when shall I, no more to part, Meet Bharat of the mighty heart? When, O my brother, when shall we The good and braveZatrughna see?”
- **Translation**: 

---

### Verse 13 (Ramayana 0.898)
- **Original**: 880 The Ramayana Thus as he poured his fond lament The son of Raghu onward went: They reached the river, and the three Bathed them in fair Godávarí. Libations of the stream they paid To every deity and shade, With hymns of praise, the Sun on high And sinless Gods to glorify. Fresh from the purifying tide Resplendent Ráma came, With LakshmaG ever by his side, And the sweet Maithil dame. So Rudra shines by worlds adored, In glory undefiled, When Nandi455 stands beside his lord, And King Himálaya's child.456 Canto XVII. Súrpanakhá. The bathing and the prayer were o'er; He turned him from the grassy shore, And with his brother and his spouse Sought his fair home beneath the boughs. Sítá and LakshmaG by his side, On to his cot the hero hied, And after rites at morning due Within the leafy shade withdrew.[250] 455 The chief chamberlain and attendant ofZiva or Rudra. 456 Umá or Párvati, the consort ofZiva.
- **Translation**: 

---

### Verse 14 (Ramayana 0.899)
- **Original**: Canto XVII. Súrpanakhá. 881 Then, honoured by the devotees, As royal Ráma sat at ease, With Sítá near him, o'er his head A canopy of green boughs spread, He shone as shines the Lord of Night By Chitrá's457 side, his dear delight. With LakshmaG there he sat and told Sweet stories of the days of old, And as the pleasant time he spent With heart upon each tale intent, A giantess, by fancy led, Came wandering to his leafy shed. FierceZúrpaGakhá,— her of yore The Ten-necked tyrant's mother bore,— Saw Ráma with his noble mien Bright as the Gods in heaven are seen; Him from whose brow a glory gleamed, Like lotus leaves his full eyes beamed: Long-armed, of elephantine gait, With hair close coiled in hermit plait: In youthful vigour, nobly framed, By glorious marks a king proclaimed: Like some bright lotus lustrous-hued, With young Kandarpa's458 grace endued: As there like Indra's self he shone, She loved the youth she gazed upon. She grim of eye and foul of face Loved his sweet glance and forehead's grace: She of unlovely figure, him Of stately form and shapely limb: She whose dim locks disordered hung, Him whose bright hair on high brows clung: 457 A star, one of the favourites of the Moon. 458 The God of love.
- **Translation**: 

---

### Verse 15 (Ramayana 0.900)
- **Original**: 882 The Ramayana She whose fierce accents counselled fear, Him whose soft tones were sweet to hear: She whose dire form with age was dried, Him radiant in his youthful pride: She whose false lips maintained the wrong, Him in the words of virtue strong: She cruel-hearted, stained with sin, Him just in deed and pure within. She, hideous fiend, a thing to hate, Him formed each eye to captivate: Fierce passion in her bosom woke, And thus to Raghu's son she spoke: “With matted hair above thy brows, With bow and shaft and this thy spouse, How hast thou sought in hermit dress The giant-haunted wilderness? What dost thou here? The cause explain: Why art thou come, and what to gain?” As ZúrpaGakhá questioned so, Ráma, the terror of the foe, In answer to the monster's call, With fearless candour told her all. “King Da[aratha reigned of old, Like Gods celestial brave and bold. I am his eldest son and heir, And Ráma is the name I bear. This brother, LakshmaG, younger born, Most faithful love to me has sworn. My wife, this princess, dear to fame, Is Sitá the Videhan dame. Obedient to my sire's behest And by the queen my mother pressed, To keep the law and merit win,
- **Translation**: 

---

### Verse 16 (Ramayana 0.901)
- **Original**: Canto XVII. Súrpanakhá. 883 I sought this wood to harbour in. But speak, for I of thee in turn Thy name, and race, and sire would learn. Thou art of giant race, I ween. Changing at will thy form and mien. Speak truly, and the cause declare That bids thee to these shades repair.” Thus Ráma spoke: the demon heard, And thus replied by passion spurred: “Of giant race, what form soe'er My fancy wills, 'tis mine to wear. Named ZúrpaGakhá here I stray, And where I walk spread wild dismay. King RávaG is my brother: fame Has taught perchance his dreaded name, Strong KumbhakarGa slumbering deep In chains of never-ending sleep: VibhíshaG of the duteous mind, In needs unlike his giant kind: DúshaG and Khara, brave and bold Whose fame by every tongue is told: Their might by mine is far surpassed; But when, O best of men, I cast These fond eyes on thy form, I see My chosen love and lord in thee. Endowed with wondrous might am I: Where'er my fancy leads I fly. The poor misshapen Sítá leave, And me, thy worthier bride receive. Look on my beauty, and prefer A spouse more meet than one like her: I'll eat that ill-formed woman there: Thy brother too her fate shall share.
- **Translation**: 

---

### Verse 17 (Ramayana 0.902)
- **Original**: 884 The Ramayana But come, beloved, thou shalt roam With me through all our woodland home; Each varied grove with me shalt seek, And gaze upon each mountain peak.” As thus she spoke, the monster gazed With sparkling eyes where passion blazed: Then he, in lore of language learned, This answer eloquent returned: Canto XVIII. The Mutilation. On her ensnared in Káma's net His eyes the royal Ráma set,[251] And thus, her passion to beguile, Addressed her with a gentle smile: “I have a wife: behold her here, My Sítá ever true and dear: And one like thee will never brook Upon a rival spouse to look. But there my brother LakshmaG stands: Unchained is he by nuptial bands: A youth heroic, loved of all, Gracious and gallant, fair and tall. With winning looks, most nobly bred, Unmatched till now, he longs to wed. Meet to enjoy thy youthful charms, O take him to thy loving arms. Enamoured on his bosom lie, Fair damsel of the radiant eye, As the warm sunlight loves to rest Upon her darling Meru's breast.”
- **Translation**: 

---

### Verse 18 (Ramayana 0.903)
- **Original**: Canto XVIII. The Mutilation. 885 The hero spoke, the monster heard, While passion still her bosom stirred. Away from Ráma's side she broke, And thus in turn to LakshmaG spoke: “Come, for thy bride take me who shine In fairest grace that suits with thine. Thou by my side from grove to grove Of DaG ak's wild in bliss shalt rove.” Then LakshmaG, skilled in soft address, Wooed by the amorous giantess, With art to turn her love aside, To ZúrpaGakhá thus replied: “And can so high a dame agree The slave-wife of a slave to be? I, lotus-hued! in good and ill Am bondsman to my brother's will. Be thou, fair creature radiant-eyed, My honoured brother's younger bride: With faultless tint and dainty limb, A happy wife, bring joy to him. He from his spouse grown old and grey, Deformed, untrue, will turn away, Her withered charms will gladly leave, And to his fair young darling cleave. For who could be so fond and blind, O loveliest of all female kind, To love another dame and slight Thy beauties rich in all delight?”
- **Translation**: 

---

### Verse 19 (Ramayana 0.904)
- **Original**: 886 The Ramayana Thus LakshmaG praised in scornful jest The long-toothed fiend with loathly breast, Who fondly heard his speech, nor knew His mocking words were aught but true. Again inflamed with love she fled To Ráma, in his leafy shed Where Sítá rested by his side, And to the mighty victor cried: “What, Ráma, canst thou blindly cling To this old false misshapen thing? Wilt thou refuse the charms of youth For withered breast and grinning tooth! Canst thou this wretched creature prize And look on me with scornful eyes? This aged crone this very hour Before thy face will I devour: Then joyous, from all rivals free. Through DaG ak will I stray with thee.” She spoke, and with a glance of flame Rushed on the fawn-eyed Maithil dame: So would a horrid meteor mar Fair RohiGí's soft beaming star. But as the furious fiend drew near, Like Death's dire noose which chills with fear, The mighty chief her purpose stayed, And spoke, his brother to upbraid: “Ne'er should we jest with creatures rude, Of savage race and wrathful mood. Think, LakshmaG, think how nearly slain My dear Videhan breathes again. Let not the hideous wretch escape Without a mark to mar her shape.
- **Translation**: 

---

### Verse 20 (Ramayana 0.905)
- **Original**: Canto XVIII. The Mutilation. 887 Strike, lord of men, the monstrous fiend, Deformed, and foul, and evil-miened.” He spoke: then LakshmaG's wrath rose high, And there before his brother's eye, He drew that sword which none could stay, And cleft her nose and ears away. Noseless and earless, torn and maimed, With fearful shrieks the fiend exclaimed, And frantic in her wild distress Resought the distant wilderness. Deformed, terrific, huge, and dread, As on she moved, her gashes bled, And groan succeeded groan as loud As roars, ere rain, the thunder cloud. Still on the fearful monster passed, While streams of blood kept falling fast, And with a roar, and arms outspread Within the boundless wood she fled. To Janasthán the monster flew; Fierce Khara there she found, With chieftains of the giant crew In thousands ranged around. Before his awful feet she bent And fell with piercing cries, As when a bolt in swift descent Comes flashing from the skies. There for a while with senses dazed Silent she lay and scared: At length her drooping head she raised, And all the tale declared, How Ráma, Lakshma G, and the dame Had reached that lonely place: Then told her injuries and shame,
- **Translation**: 

---



--- End of Ramayan_batch_143.md ---


--- Start of Ramayan_batch_144.md ---

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

### Verse 1 (Ramayana 0.906)
- **Original**: 888 The Ramayana And showed her bleeding face. Canto XIX. The Rousing Of Khara. When Khara saw his sister lie With blood-stained limbs and troubled eye,[252] Wild fury in his bosom woke, And thus the monstrous giant spoke; “Arise, my sister; cast away This numbing terror and dismay, And straight the impious hand declare That marred those features once so fair. For who his finger tip will lay On the black snake in childish play, And unattacked, with idle stroke His poison-laden fang provoke? Ill-fated fool, he little knows Death's noose around his neck he throws, Who rashly met thee, and a draught Of life-destroying poison quaffed. Strong, fierce as death, 'twas thine to choose Thy way at will, each shape to use; In power and might like one of us: What hand has maimed and marred thee thus? What God or fiend this deed has wrought, What bard or sage of lofty thought Was armed with power supremely great Thy form to mar and mutilate? In all the worlds not one I see Would dare a deed to anger me:
- **Translation**: 

---

### Verse 2 (Ramayana 0.907)
- **Original**: Canto XIX. The Rousing Of Khara. 889 Not Indra's self, the Thousand-eyed, Beneath whose hand fierce Páka459 died. My life-destroying darts this day His guilty breath shall rend away, E'en as the thirsty wild swan drains Each milk-drop that the wave retains. Whose blood in foaming streams shall burst O'er the dry ground which lies athirst, When by my shafts transfixed and slain He falls upon the battle plain? From whose dead corpse shall birds of air The mangled flesh and sinews tear, And in their gory feast delight, When I have slain him in the fight? Not God or bard or wandering ghost, No giant of our mighty host Shall step between us, or avail To save the wretch when I assail. Collect each scattered sense, recall Thy troubled thoughts, and tell me all. What wretch attacked thee in the way, And quelled thee in victorious fray?” His breast with burning fury fired, Thus Khara of the fiend inquired: And then with many a tear and sigh Thus ZúrpaGakhá made reply: “'Tis Da[aratha's sons, a pair Strong, resolute, and young, and fair: In coats of dark and blackdeer's hide, And like the radiant lotus eyed: On berries roots and fruit they feed, And lives of saintly virtue lead: 459 A demon slain by Indra.
- **Translation**: 

---

### Verse 3 (Ramayana 0.908)
- **Original**: 890 The Ramayana With ordered senses undefiled, Ráma and LakshmaG are they styled. Fair as the Minstrels' King460 are they, And stamped with signs of regal sway. I know not if the heroes trace Their line from Gods or Dánav461 race. There by these wondering eyes between The noble youths a dame was seen, Fair, blooming, young, with dainty waist, And all her bright apparel graced. For her with ready heart and mind The royal pair their strength combined, And brought me to this last distress, Like some lost woman, comfortless. Perfidious wretch! my soul is fain Her foaming blood and theirs to drain. O let me head the vengeful fight, And with this hand my murderers smite. Come, brother, hasten to fulfil This longing of my eager will. On to the battle! Let me drink Their lifeblood as to earth they sink.” Then Khara, by his sister pressed, Inflamed with fury, gave his hest To twice seven giants of his crew, Fierce as the God of death to view: 460 Chitraratha, King of the Gandharvas. 461 Titanic.
- **Translation**: 

---

### Verse 4 (Ramayana 0.909)
- **Original**: Canto XX. The Giants' Death. 891 'Two men equipped with arms, who wear Deerskin and bark and matted hair, Leading a beauteous dame, have strayed To the wild gloom of DaG ak's shade. These men, this cursed woman slay, And hasten back without delay, That this my sister's lips may be Red with the lifeblood of the three. Giants, my wounded sister longs To take this vengeance for her wrongs. With speed her dearest wish fulfil, And with your might these creatures kill. Soon as your matchless strength shall lay These brothers dead in battle fray, She in triumphant joy will laugh, And their hearts' blood delighted quaff.” The giants heard the words he said, And forth withZúrpaGakhá sped, As mighty clouds in autumn fly Urged by the wind along the sky. Canto XX. The Giants' Death. FierceZúrpaGakhá with her train To Ráma's dwelling came again, And to the eager giants showed Where Sítá and the youths abode. Within the leafy cot they spied The hero by his consort's side, And faithful LakshmaG ready still To wait upon his brother's will. [253]
- **Translation**: 

---

### Verse 5 (Ramayana 0.910)
- **Original**: 892 The Ramayana Then noble Ráma raised his eye And saw the giants standing nigh, And then, as nearer still they pressed. His glorious brother thus addressed, “Be thine a while, my brother dear, To watch o'er Sítá's safety here, And I will slay these creatures who The footsteps of my spouse pursue.” He spoke, and reverent LakshmaG heard Submissive to his brother's word. The son of Raghu, virtuous-souled, Strung his great bow adorned with gold, And, with the weapon in his hand, Addressed him to the giant band: “Ráma and LakshmaG we, who spring From Da[aratha, mighty king; We dwell a while with Sítá here In DaG ak forest wild and drear. On woodland roots and fruit we feed, And lives of strictest rule we lead. Say why would ye our lives oppress Who sojourn in the wilderness. Sent hither by the hermits' prayer With bow and darts unused to spare, For vengeance am I come to slay Your sinful band in battle fray. Rest as ye are: remain content, Nor try the battle's dire event. Unless your offered lives ye spurn, O rovers of the night, return.”
- **Translation**: 

---

### Verse 6 (Ramayana 0.911)
- **Original**: Canto XX. The Giants' Death. 893 They listened while the hero spoke, And fury in each breast awoke. The Bráhman-slayers raised on high Their mighty spears and made reply: They spoke with eyes aglow with ire, While Ráma's burnt with vengeful tire, And answered thus, in fury wild, That peerless chief whose tones were mild: “Nay thou hast angered, overbold, Khara our lord, the mighty-souled, And for thy sin, in battle strife Shalt yield to us thy forfeit life. No power hast thou alone to stand Against the numbers of our band. 'Twere vain to match thy single might Against us in the front of fight. When we equipped for fight advance With brandished pike and mace and lance, Thou, vanquished in the desperate field, Thy bow, thy strength, thy life shalt yield.” With bitter words and threatening mien Thus furious spoke the fierce fourteen, And raising scimitar and spear On Ráma rushed in wild career. Their levelled spears the giant crew Against the matchless hero threw. His bow the son of Raghu bent, And twice seven shafts to meet them sent, And every javelin sundered fell By the bright darts he aimed so well.
- **Translation**: 

---

### Verse 7 (Ramayana 0.912)
- **Original**: 894 The Ramayana The hero saw: his anger grew To fury: from his side he drew Fresh sunbright arrows pointed keen, In number, like his foes, fourteen. His bow he grasped, the string he drew, And gazing on the giant crew, As Indra casts the levin, so Shot forth his arrows at the foe. The hurtling arrows, stained with gore, Through the fiends' breasts a passage tore, And in the earth lay buried deep As serpents through an ant-hill creep Like trees uptorn by stormy blast The shattered fiends to earth were cast, And there with mangled bodies they, Bathed in their blood and breathless, lay. With fainting heart and furious eye The demon saw her champions die. With drying wounds that scarcely bled Back to her brother's home she fled. Oppressed with pain, with loud lament At Khara's feet the monster bent. There like a plant whence slowly come The trickling drops of oozy gum, With her grim features pale with pain She poured her tears in ceaseless rain, There routedZúrpaGakhá lay, And told her brother all, The issue of the bloody fray, Her giant champions' fall.
- **Translation**: 

---

### Verse 8 (Ramayana 0.913)
- **Original**: Canto XXI. The Rousing Of Khara. 895 Canto XXI. The Rousing Of Khara. Low in the dust he saw her lie, And Khara's wrath grew fierce and high. Aloud he cried to her who came Disgracefully with baffled aim: “I sent with thee at thy request The bravest of my giants, best Of all who feed upon the slain: Why art thou weeping here again? Still to their master's interest true, My faithful, noble, loyal crew, Though slaughtered in the bloody fray, Would yet their monarch's word obey. Now I, my sister, fain would know The cause of this thy fear and woe, Why like a snake thou writhest there, Calling for aid in wild despair. Nay, lie not thus in lowly guise: Cast off thy weakness and arise!” With soothing words the giant chief Assuaged the fury of her grief. Her weeping eyes she slowly dried And to her brother thus replied: “I sought thee in my shame and fear With severed nose and mangled ear: My gashes like a river bled, I sought thee and was comforted. [254]
- **Translation**: 

---

### Verse 9 (Ramayana 0.914)
- **Original**: 896 The Ramayana Those twice seven giants, brave and strong, Thou sentest to avenge the wrong, To lay the savage Ráma low, And Lakshma G who misused me so. But ah, the shafts of Ráma through The bodies of my champions flew: Though madly fierce their spears they plied, Beneath his conquering might they died. I saw them, famed for strength and speed, I saw my heroes fall and bleed: Great trembling seized my every limb At the great deed achieved by him. In trouble, horror, doubt, and dread, Again to thee for help I fled. While terror haunts my troubled sight, I seek thee, rover of the night. And canst thou not thy sister free From this wide waste of troublous sea Whose sharks are doubt and terror, where Each wreathing wave is dark despair? Low lie on earth thy giant train By ruthless Ráma's arrows slain, And all the mighty demons, fed On blood, who followed me are dead. Now if within thy breast may be Pity for them and love for me, If thou, O rover of the night, Have valour and with him can fight, Subdue the giants' cruel foe Who dwells where DaG ak's thickets grow. But if thine arm in vain assay This queller of his foes to slay, Now surely here before thine eyes, Wronged and ashamed thy sister dies.
- **Translation**: 

---

### Verse 10 (Ramayana 0.915)
- **Original**: Canto XXII. Khara's Wrath. 897 Too well, alas, too well I see That, strong in war as thou mayst be, Thou canst not in the battle stand When Ráma meets thee hand to hand. Go forth, thou hero but in name, Assuming might thou canst not claim; Call friend and kin, no longer stay: Away from Janasthán, away! Shame of thy race! the weak alone Beneath thine arm may sink o'erthrown: Fly Ráma and his brother: they Are men too strong for thee to slay. How canst thou hope, O weak and base, To make this grove thy dwelling-place? With Ráma's might unmeet to vie, O'ermastered thou wilt quickly die. A hero strong in valorous deed Is Ráma, Da[aratha's seed: And scarce of weaker might than he His brother chief who mangled me.” Thus wept and wailed in deep distress The grim misshapen giantess: Before her brother's feet she lay O'erwhelmed with grief, and swooned away. Canto XXII. Khara's Wrath. Roused by the taunting words she spoke, The mighty Khara's wrath awoke, And there, while giants girt him round, In these fierce words an utterance found:
- **Translation**: 

---

### Verse 11 (Ramayana 0.916)
- **Original**: 898 The Ramayana “I cannot, peerless one, contain Mine anger at this high disdain, Galling as salt when sprinkled o'er The rawness of a bleeding sore. Ráma in little count I hold, Weak man whose days are quickly told. The caitiff with his life to-day For all his evil deeds shall pay. Dry, sister, dry each needless tear, Stint thy lament and banish fear, For Ráma and his brother go This day to Yáma's realm below. My warrior's axe shall stretch him slain, Ere set of sun, upon the plain, Then shall thy sated lips be red With his warm blood in torrents shed.” As Khara's speech the demon heard, With sudden joy her heart was stirred: She fondly praised him as the boast And glory of the giant host. First moved to ire by taunts and stings, Now soothed by gentle flatterings, To DúshaG, who his armies led, The demon Khara spoke, and said: “Friend, from the host of giants call Full fourteen thousand, best of all, Slaves of my will, of fearful might, Who never turn their backs in fight: Fiends who rejoice to slay and mar, Dark as the clouds of autumn are: Make ready quickly, O my friend, My chariot and the bows I bend.
- **Translation**: 

---

### Verse 12 (Ramayana 0.917)
- **Original**: Canto XXII. Khara's Wrath. 899 My swords, my shafts of brilliant sheen, My divers lances long and keen. On to the battle will I lead These heroes of Pulastya's seed, And thus, O famed for warlike skill, Ráma my wicked foeman kill.” He spoke, and ere his speech was done, His chariot glittering like the sun, Yoked and announced, by Dúshan's care, With dappled steeds was ready there. High as a peak from Meru rent It burned with golden ornament: The pole of lazulite, of gold Were the bright wheels whereon it rolled. With gold and moonstone blazoned o'er, Fish, flowers, trees, rocks, the panels bore; Auspicious birds embossed thereon, And stars in costly emblem shone. O'er flashing swords his banner hung, And sweet bells, ever tinkling, swung. [255] That mighty host with sword and shield And oar was ready for the field: And Khara saw, and Dúshan cried, “Forth to the fight, ye giants, ride.” Then banners waved, and shield and sword Flashed as the host obeyed its lord. From Janasthán they sallied out With eager speed, and din, and shout, Armed with the mace for close attacks, The bill, the spear, the battle-axe, Steel quoit and club that flashed afar, Huge bow and sword and scimitar, The dart to pierce, the bolt to strike,
- **Translation**: 

---

### Verse 13 (Ramayana 0.918)
- **Original**: 900 The Ramayana The murderous bludgeon, lance, and pike. So forth from Janasthán, intent On Khara's will, the monsters went. He saw their awful march: not far Behind the host he drove his car. Ware of his master's will, to speed The driver urged each gold-decked steed. Then forth the warrior's coursers sprang, And with tumultuous murmur rang Each distant quarter of the sky And realms that intermediate lie. High and more high within his breast His pride triumphant rose, While terrible as Death he pressed Onward to slay his foes, “More swiftly yet,” as on they fled, He cried in thundering tones Loud as a cloud that overhead Hails down a flood of stones. Canto XXIII. The Omens. As forth upon its errand went That huge ferocious armament, An awful cloud, in dust and gloom, With threatening thunders from its womb Poured in sad augury a flood Of rushing water mixt with blood. The monarch's steeds, though strong and fleet, Stumbled and fell: and yet their feet Passed o'er the bed of flowers that lay
- **Translation**: 

---

### Verse 14 (Ramayana 0.919)
- **Original**: Canto XXIII. The Omens. 901 Fresh gathered on the royal way. No gleam of sunlight struggled through The sombre pall of midnight hue, Edged with a line of bloody red, Like whirling torches overhead. A vulture, fierce, of mighty size. Terrific with his cruel eyes, Perched on the staff enriched with gold, Whence hung the flag in many a fold. Each ravening bird, each beast of prey Where Janasthán's wild thickets lay, Rose with a long discordant cry And gathered as the host went by. And from the south long, wild, and shrill, Came spirit voices boding ill. Like elephants in frantic mood, Vast clouds terrific, sable-hued, Hid all the sky where'er they bore Their load of water mixt with gore. Above, below, around were spread Thick shades of darkness strange and dread, Nor could the wildered glance descry A point or quarter of the sky. Then came o'er heaven a sanguine hue, Though evening's flush not yet was due, While each ill-omened bird that flies Assailed the king with harshest cries. There screamed the vulture and the crane, And the loud jackal shrieked again. Each hideous thing that bodes aright Disaster in the coming fight, With gaping mouth that hissed and flamed, The ruin of the host proclaimed. Eclipse untimely reft away
- **Translation**: 

---

### Verse 15 (Ramayana 0.920)
- **Original**: 902 The Ramayana The brightness of the Lord of Day, And near his side was seen to glow A mace-like comet boding woe. Then while the sun was lost to view A mighty wind arose and blew, And stars like fireflies shed their light, Nor waited for the distant night. The lilies drooped, the brooks were dried, The fish and birds that swam them died, And every tree that was so fair With flower and fruit was stripped and bare. The wild wind ceased, yet, raised on high, Dark clouds of dust involved the sky. In doleful twitter long sustained The restless Sárikás462 complained, And from the heavens with flash and flame Terrific meteors roaring came. Earth to her deep foundation shook With rock and tree and plain and brook, As Khara with triumphant shout, Borne in his chariot, sallied out. His left arm throbbed: he knew full well That omen, and his visage fell. Each awful sign the giant viewed, And sudden tears his eye bedewed. Care on his brow sat chill and black, Yet mad with wrath he turned not back. Upon each fearful sight that raised The shuddering hair the chieftain gazed, And laughing in his senseless pride Thus to his giant legions cried: “By sense of mightiest strength upborne, 462 The Sáriká is the Maina, a bird like a starling.
- **Translation**: 

---

### Verse 16 (Ramayana 0.921)
- **Original**: Canto XXIII. The Omens. 903 These feeble signs I laugh to scorn. I could bring down the stars that shine In heaven with these keen shafts of mine. Impelled by warlike fury I Could cause e'en Death himself to die. [256] I will not seek my home again Until my pointed shafts have slain This Raghu's son so fierce in pride, And Lakshma G by his brother's side. And she, my sister, she for whom These sons of Raghu meet their doom, She with delighted lips shall drain The lifeblood of her foemen slain. Fear not for me: I ne'er have known Defeat, in battle overthrown. Fear not for me, O giants; true Are the proud words I speak to you. The king of Gods who rules on high, If wild Airávat bore him nigh, Should fall before me bolt in hand: And shall these two my wrath withstand!” He ended and the giant host Who heard their chief's triumphant boast, Rejoiced with equal pride elate, Entangled in the noose of Fate. Then met on high in bright array, With eyes that longed to see the fray, God and Gandharva, sage and saint, With beings pure from earthly taint. Blest for good works aforetime wrought, Thus each to other spake his thought: “Now joy to Bráhmans, joy to kine,
- **Translation**: 

---

### Verse 17 (Ramayana 0.922)
- **Original**: 904 The Ramayana And all whom world count half divine! May Raghu's offspring slay in fight Pulastya's sons who roam by night!” In words like these and more, the best Of high-souled saints their hopes expressed, Bending their eager eyes from where Car-borne with Gods they rode in air. Beneath them stretching far, they viewed The giants' death-doomed multitude. They saw where, urged with fury, far Before the host rolled Khara's car, And close beside their leader came Twelve giant peers of might and fame. Four other chiefs463 before the rest Behind their leader DúshaG pressed. Impetuous, cruel, dark, and dread, All thirsting for the fray, The hosts of giant warriors sped Onward upon their way. With eager speed they reached the spot Where dwelt the princely two,— Like planets in a league to blot The sun and moon from view. Canto XXIV. The Host In Sight. 463 Mahákapála, Sthúláksha, Pramátha, Tri[iras.
- **Translation**: 

---

### Verse 18 (Ramayana 0.923)
- **Original**: Canto XXIV. The Host In Sight. 905 While Khara, urged by valiant rage, Drew near that little hermitage, Those wondrous signs in earth and sky Smote on each prince's watchful eye. When Ráma saw those signs of woe Fraught with destruction to the foe, With bold impatience scarce repressed His brother chief he thus addressed: “These fearful signs, my brother bold, Which threaten all our foes, behold: All laden, as they strike the view, With ruin to the fiendish crew. The angry clouds are gathering fast, Their skirts with dusty gloom o'ercast, And harsh with loud-voiced thunder, rain Thick drops of blood upon the plain. See, burning for the coming fight, My shafts with wreaths of smoke are white, And my great bow embossed with gold Throbs eager for the master's hold. Each bird that through the forest flies Sends out its melancholy cries. All signs foretell the dangerous strife, The jeopardy of limb and life. Each sight, each sound gives warning clear That foemen meet and death is near. But courage, valiant brother! well The throbbings of mine arm foretell That ruin waits the hostile powers, And triumph in the fight is ours. I hail the welcome omen: thou Art bright of face and clear of brow. For LakshmaG, when the eye can trace
- **Translation**: 

---

### Verse 19 (Ramayana 0.924)
- **Original**: 906 The Ramayana A cloud upon the warrior's face Stealing the cheerful light away, His life is doomed in battle fray. List, brother, to that awful cry: With shout and roar the fiends draw nigh. With thundering beat of many a drum The savage-hearted giants come. The wise who value safety know To meet, prepared, the coming blow: In paths of prudence trained aright They watch the stroke before it smite. Take thou thine arrows and thy bow, And with the Maithil lady go For shelter to the mountain cave Where thickest trees their branches wave. I will not have thee, LakshmaG, say One word in answer, but obey. By all thy honour for these feet Of mine, dear brother, I entreat. Thy warlike arm, I know could, smite To death these rovers of the night; But I this day would fight alone Till all the fiends be overthrown.”[257] He spake: and LakshmaG answered naught: His arrows and his bow he brought, And then with Sítá following hied For shelter to the mountain side. As LakshmaG and the lady through The forest to the cave withdrew, “'Tis well,” cried Ráma. Then he braced His coat of mail around his waist. When, bright as blazing fire, upon His mighty limbs that armour shone, The hero stood like some great light
- **Translation**: 

---

### Verse 20 (Ramayana 0.925)
- **Original**: Canto XXIV. The Host In Sight. 907 Uprising in the dark of night. His dreadful shafts were by his side; His trusty bow he bent and plied, Prepared he stood: the bowstring rang, Filling the welkin with the clang. The high-souled Gods together drew The wonder of the fight to view, The saints made free from spot and stain, And bright Gandharvas' heavenly train. Each glorious sage the assembly sought, Each saint divine of loftiest thought, And filled with zeal for Ráma's sake. Thus they whose deeds were holy spake: “Now be it well with Bráhmans, now Well with the worlds and every cow! Let Ráma in the deadly fray The fiends who walk in darkness slay, As He who bears the discus464 slew The chieftains of the Asur crew.” Then each with anxious glances viewed His fellow and his speech renewed: “There twice seven thousand giants stand With impious heart and cruel hand: Here Ráma stands, by virtue known: How can the hero fight alone?” 464 VishGu, who bears achakraor discus.
- **Translation**: 

---



--- End of Ramayan_batch_144.md ---
