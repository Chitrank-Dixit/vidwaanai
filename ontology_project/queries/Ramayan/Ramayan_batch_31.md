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

### Verse 1 (Ramayan 0.601)
- **Original**: Canto LXI. Kausalyá's Lament. 583 The heart within my breast, I feel, Is adamant or hardest steel, Or, in a thousand fragments split, The loss of him had shattered it, When those I love, who should be blest, Are wandering in the wood distressed, Condemned their wretched lives to lead In exile, by thy ruthless deed. If, when the fourteen years are past, Ráma reseeks his home at last, I think not Bharat will consent To yield the wealth and government. At funeral feasts some mourners deal To kith and kin the solemn meal, And having duly fed them all Some Bráhmans to the banquet call. The best of Bráhmans, good and wise, The tardy summoning despise, And, equal to the Gods, disdain Cups, e'en of Amrit, thus to drain. Nay e'en when Bráhmans first have fed, They loathe the meal for others spread, And from the leavings turn with scorn, As bulls avoid a fractured horn. So Ráma, sovereign lord of men, Will spurn the sullied kingship then: He born the eldest and the best, His younger's leavings will detest, Turning from tasted food away, As tigers scorn another's prey. The sacred post is used not twice, Nor elements, in sacrifice. But once the sacred grass is spread, But once with oil the flame is fed:
- **Translation**: 

---

### Verse 2 (Ramayan 0.602)
- **Original**: 584 The Ramayana So Ráma's pride will ne'er receive The royal power which others leave, Like wine when tasteless dregs are left, Or rites of Soma juice bereft. Be sure the pride of Raghu's race Will never stoop to such disgrace: The lordly lion will not bear That man should beard him in his lair. Were all the worlds against him ranged His dauntless soul were still unchanged: He, dutiful, in duty strong, Would purge the impious world from wrong. Could not the hero, brave and bold, The archer, with his shafts of gold, Burn up the very seas, as doom Will in the end all life consume? Of lion's might, eyed like a bull, A prince so brave and beautiful, Thou hast with wicked hate pursued, Like sea-born tribes who eat their brood. If thou, O Monarch, hadst but known The duty all the Twice-born own, If the good laws had touched thy mind, Which sages in the Scriptures find, Thou ne'er hadst driven forth to pine This brave, this duteous son of thine. First on her lord the wife depends, Next on her son and last on friends: These three supports in life has she, And not a fourth for her may be. Thy heart, O King, I have not won; In wild woods roams my banished son; Far are my friends: ah, hapless me, Quite ruined and destroyed by thee.”
- **Translation**: 

---

### Verse 3 (Ramayan 0.603)
- **Original**: Canto LXII. Dasaratha Consoled. 585 Canto LXII. Dasaratha Consoled. The queen's stern speech the monarch heard, As rage and grief her bosom stirred, And by his anguish sore oppressed Reflected in his secret breast. Fainting and sad, with woe distraught, He wandered in a maze of thought; At length the queller of the foe Grew conscious, rallying from his woe. When consciousness returned anew Long burning sighs the monarch drew, Again immersed in thought he eyed Kau [alyá standing by his side. Back to his pondering soul was brought The direful deed his hand had wrought, When, guiltless of the wrong intent, His arrow at a sound was sent. Distracted by his memory's sting, And mourning for his son, the king To two consuming griefs a prey, A miserable victim lay. The double woe devoured him fast, As on the ground his eyes he cast, Joined suppliant hands, her heart to touch, And spake in the answer, trembling much: “Kau [alyá, for thy grace I sue, Joining these hands as suppliants do. Thou e'en to foes hast ever been A gentle, good, and loving queen. Her lord, with noble virtues graced, Her lord, by lack of all debased, Is still a God in woman's eyes, If duty's law she hold and prize.
- **Translation**: 

---

### Verse 4 (Ramayan 0.604)
- **Original**: 586 The Ramayana Thou, who the right hast aye pursued, Life's changes and its chances viewed, Shouldst never launch, though sorrow-stirred, At me distressed, one bitter word.” She listened, as with sorrow faint He murmured forth his sad complaint: Her brimming eyes with tears ran o'er, As spouts the new fallen water pour;[168] His suppliant hands, with fear dismayed She gently clasped in hers, and laid, Like a fair lotus, on her head, And faltering in her trouble said: “Forgive me; at thy feet I lie, With low bent head to thee I cry. By thee besought, thy guilty dame Pardon from thee can scarcely claim. She merits not the name of wife Who cherishes perpetual strife With her own husband good and wise, Her lord both here and in the skies. I know the claims of duty well, I know thy lips the truth must tell. All the wild words I rashly spoke, Forth from my heart, through anguish, broke; For sorrow bends the stoutest soul, And cancels Scripture's high control. Yea, sorrow's might all else o'erthrows The strongest and the worst of foes. 'Tis thus with all: we keenly feel, Yet bear the blows our foemen deal, But when a slender woe assails The manliest spirit bends and quails. The fifth long night has now begun
- **Translation**: 

---

### Verse 5 (Ramayan 0.605)
- **Original**: Canto LXIII. The Hermit's Son. 587 Since the wild woods have lodged my son: To me whose joy is drowned in tears, Each day a dreary year appears. While all my thoughts on him are set Grief at my heart swells wilder yet: With doubled might thus Ocean raves When rushing floods increase his waves.” As from Kau[alyá reasoning well The gentle words of wisdom fell, The sun went down with dying flame, And darkness o'er the landscape came. His lady's soothing words in part Relieved the monarch's aching heart, Who, wearied out by all his woes, Yielded to sleep and took repose. Canto LXIII. The Hermit's Son. But soon by rankling grief oppressed The king awoke from troubled rest, And his sad heart was tried again With anxious thought where all was pain. Ráma and LakshmaG's mournful fate On Da [aratha, good and great As Indra, pressed with crushing weight, As when the demon's might assails The Sun-God, and his glory pales. Ere yet the sixth long night was spent, Since Ráma to the woods was sent, The king at midnight sadly thought
- **Translation**: 

---

### Verse 6 (Ramayan 0.606)
- **Original**: 588 The Ramayana Of the old crime his hand had wrought, And thus to Queen Kau[alyá cried Who still for Ráma moaned and sighed: “If thou art waking, give, I pray, Attention to the words I say. Whate'er the conduct men pursue, Be good or ill the acts they do, Be sure, dear Queen, they find the meed Of wicked or of virtuous deed. A heedless child we call the man Whose feeble judgment fails to scan The weight of what his hands may do, Its lightness, fault, and merit too. One lays the Mango garden low, And bids the gay Palá[as grow: Longing for fruit their bloom he sees, But grieves when fruit should bend the trees. Cut by my hand, my fruit-trees fell, Palá[a trees I watered well. My hopes this foolish heart deceive, And for my banished son I grieve. Kau [alyá, in my youthful prime Armed with my bow I wrought the crime, Proud of my skill, my name renowned, An archer prince who shoots by sound. The deed this hand unwitting wrought This misery on my soul has brought, As children seize the deadly cup And blindly drink the poison up. As the unreasoning man may be Charmed with the gay Palá[a tree, I unaware have reaped the fruit Of joying at a sound to shoot. As regent prince I shared the throne,
- **Translation**: 

---

### Verse 7 (Ramayan 0.607)
- **Original**: Canto LXIII. The Hermit's Son. 589 Thou wast a maid to me unknown, The early Rain-time duly came, And strengthened love's delicious flame. The sun had drained the earth that lay All glowing 'neath the summer day, And to the gloomy clime had fled Where dwell the spirits of the dead.335 The fervent heat that moment ceased, The darkening clouds each hour increased And frogs and deer and peacocks all Rejoiced to see the torrents fall. Their bright wings heavy from the shower, The birds, new-bathed, had scarce the power To reach the branches of the trees Whose high tops swayed beneath the breeze. The fallen rain, and falling still, Hung like a sheet on every hill, Till, with glad deer, each flooded steep Showed glorious as the mighty deep. The torrents down its wooded side Poured, some unstained, while others dyed [169] Gold, ashy, silver, ochre, bore The tints of every mountain ore. In that sweet time, when all are pleased, My arrows and my bow I seized; Keen for the chase, in field or grove, Down Sarjú's bank my car I drove. I longed with all my lawless will Some elephant by night to kill, Some buffalo that came to drink, Or tiger, at the river's brink. When all around was dark and still, 335 The southern region is the abode of Yama the Indian Pluto, and of departed spirits.
- **Translation**: 

---

### Verse 8 (Ramayan 0.608)
- **Original**: 590 The Ramayana I heard a pitcher slowly fill, And thought, obscured in deepest shade, An elephant the sound had made. I drew a shaft that glittered bright, Fell as a serpent's venomed bite; I longed to lay the monster dead, And to the mark my arrow sped. Then in the calm of morning, clear A hermit's wailing smote my ear: “Ah me, ah me,” he cried, and sank, Pierced by my arrow, on the bank. E'en as the weapon smote his side, I heard a human voice that cried: “Why lights this shaft on one like me, A poor and harmless devotee? I came by night to fill my jar From this lone stream where no men are. Ah, who this deadly shaft has shot? Whom have I wronged, and knew it not? Why should a boy so harmless feel The vengeance of the winged steel? Or who should slay the guiltless son Of hermit sire who injures none, Who dwells retired in woods, and there Supports his life on woodland fare? Ah me, ah me, why am I slain, What booty will the murderer gain? In hermit coils I bind my hair, Coats made of skin and bark I wear. Ah, who the cruel deed can praise Whose idle toil no fruit repays, As impious as the wretch's crime Who dares his master's bed to climb? Nor does my parting spirit grieve
- **Translation**: 

---

### Verse 9 (Ramayan 0.609)
- **Original**: Canto LXIII. The Hermit's Son. 591 But for the life which thus I leave: Alas, my mother and my sire,— I mourn for them when I expire. Ah me, that aged, helpless pair, Long cherished by my watchful care, How will it be with them this day When to the Five336 I pass away? Pierced by the self-same dart we die, Mine aged mother, sire, and I. Whose mighty hand, whose lawless mind Has all the three to death consigned?” When I, by love of duty stirred, That touching lamentation heard, Pierced to the heart by sudden woe, I threw to earth my shafts and bow. My heart was full of grief and dread As swiftly to the place I sped, Where, by my arrow wounded sore, A hermit lay on Sarjú's shore. His matted hair was all unbound, His pitcher empty on the ground, And by the fatal arrow pained, He lay with dust and gore distained. I stood confounded and amazed: His dying eyes to mine he raised, And spoke this speech in accents stern, As though his light my soul would burn: “How have I wronged thee, King, that I Struck by thy mortal arrow die? The wood my home, this jar I brought, And water for my parents sought. This one keen shaft that strikes me through 336 The five elements of which the body consists, and to which it returns.
- **Translation**: 

---

### Verse 10 (Ramayan 0.610)
- **Original**: 592 The Ramayana Slays sire and aged mother too. Feeble and blind, in helpless pain, They wait for me and thirst in vain. They with parched lips their pangs must bear, And hope will end in blank despair. Ah me, there seems no fruit in store For holy zeal or Scripture lore, Or else ere now my sire would know That his dear son is lying low. Yet, if my mournful fate he knew, What could his arm so feeble do? The tree, firm-rooted, ne'er may be The guardian of a stricken tree. Haste to my father, and relate While time allows, my sudden fate, Lest he consume thee as the fire Burns up the forest, in his ire. This little path, O King, pursue: My father's cot thou soon wilt view. There sue for pardon to the sage, Lest he should curse thee in his rage. First from the wound extract the dart That kills me with its deadly smart, E'en as the flushed impetuous tide Eats through the river's yielding side.” I feared to draw the arrow out, And pondered thus in painful doubt: “Now tortured by the shaft he lies, But if I draw it forth he dies.” Helpless I stood, faint, sorely grieved: The hermit's son my thought perceived; As one o'ercome by direst pain He scarce had strength to speak again.
- **Translation**: 

---

### Verse 11 (Ramayan 0.611)
- **Original**: Canto LXIV. Dasaratha's Death. 593 With writhing limb and struggling breath, Nearer and ever nearer death “My senses undisturbed remain, And fortitude has conquered pain: Now from one tear thy soul be freed. Thy hand has made a Bráhman bleed. Let not this pang thy bosom wring: No twice-born youth am I, O King, [170] For of a Vai[ya sire I came, Who wedded with aZúdra dame.” These words the boy could scarcely say, As tortured by the shaft he lay, Twisting his helpless body round, Then trembling senseless on the ground. Then from his bleeding side I drew The rankling shaft that pierced him through. With death's last fear my face he eyed, And, rich in store of penance, died.” Canto LXIV. Dasaratha's Death. The son of Raghu to his queen Thus far described the unequalled scene, And, as the hermit's death he rued, The mournful story thus renewed: “The deed my heedless hand had wrought Perplexed me with remorseful thought, And all alone I pondered still How kindly deed might salve the ill. The pitcher from the ground I took,
- **Translation**: 

---

### Verse 12 (Ramayan 0.612)
- **Original**: 594 The Ramayana And filled it from that fairest brook, Then, by the path the hermit showed, I reached his sainted sire's abode. I came, I saw: the aged pair, Feeble and blind, were sitting there, Like birds with clipped wings, side by side, With none their helpless steps to guide. Their idle hours the twain beguiled With talk of their returning child, And still the cheering hope enjoyed, The hope, alas, by me destroyed. Then spoke the sage, as drawing near The sound of footsteps reached his ear: “Dear son, the water quickly bring; Why hast thou made this tarrying? Thy mother thirsts, and thou hast played, And bathing in the brook delayed. She weeps because thou camest not; Haste, O my son, within the cot. If she or I have ever done A thing to pain thee, dearest son, Dismiss the memory from thy mind: A hermit thou, be good and kind. On thee our lives, our all, depend: Thou art thy friendless parents' friend. The eyeless couple's eye art thou: Then why so cold and silent now?” With sobbing voice and bosom wrung I scarce could move my faltering tongue, And with my spirit filled with dread I looked upon the sage, and said, While mind, and sense, and nerve I strung To fortify my trembling tongue,
- **Translation**: 

---

### Verse 13 (Ramayan 0.613)
- **Original**: Canto LXIV. Dasaratha's Death. 595 And let the aged hermit know His son's sad fate, my fear and woe: “High-minded Saint, not I thy child, A warrior, Da[aratha styled. I bear a grievous sorrow's weight Born of a deed which good men hate. My lord, I came to Sarjú's shore, And in my hand my bow I bore For elephant or beast of chase That seeks by night his drinking place. There from the stream a sound I heard As if a jar the water stirred. An elephant, I thought, was nigh: I aimed, and let an arrow fly. Swift to the place I made my way, And there a wounded hermit lay Gasping for breath: the deadly dart Stood quivering in his youthful heart. I hastened near with pain oppressed; He faltered out his last behest. And quickly, as he bade me do, From his pierced side the shaft I drew. I drew the arrow from the rent, And up to heaven the hermit went, Lamenting, as from earth he passed, His aged parents to the last. Thus, unaware, the deed was done: My hand, unwitting, killed thy son. For what remains, O, let me win Thy pardon for my heedless sin.” As the sad tale of sin I told The hermit's grief was uncontrolled. With flooded eyes, and sorrow-faint,
- **Translation**: 

---

### Verse 14 (Ramayan 0.614)
- **Original**: 596 The Ramayana Thus spake the venerable saint: I stood with hand to hand applied, And listened as he spoke and sighed: “If thou, O King, hadst left unsaid By thine own tongue this tale of dread, Thy head for hideous guilt accursed Had in a thousand pieces burst. A hermit's blood by warrior spilt, In such a case, with purposed guilt, Down from his high estate would bring Even the thunder's mighty King. And he a dart who conscious sends Against the devotee who spends His pure life by the law of Heaven— That sinner's head will split in seven. Thou livest, for thy heedless hand Has wrought a deed thou hast not planned, Else thou and all of Raghu's line Had perished by this act of thine. Now guide us,” thus the hermit said, “Forth to the spot where he lies dead. Guide us, this day, O Monarch, we For the last time our son would see: The hermit dress of skin he wore Rent from his limbs distained with gore; His senseless body lying slain, His soul in Yama's dark domain.” Alone the mourning pair I led, Their souls with woe disquieted, And let the dame and hermit lay[171] Their hands upon the breathless clay. The father touched his son, and pressed The body to his aged breast;
- **Translation**: 

---

### Verse 15 (Ramayan 0.615)
- **Original**: Canto LXIV. Dasaratha's Death. 597 Then falling by the dead boy's side, He lifted up his voice, and cried: “Hast thou no word, my child, to say? No greeting for thy sire to-day? Why art thou angry, darling? why Wilt thou upon the cold earth lie? If thou, my son, art wroth with me, Here, duteous child, thy mother see. What! no embrace for me, my son? No word of tender love— not one? Whose gentle voice, so soft and clear, Soothing my spirit, shall I hear When evening comes, with accents sweet Scripture or ancient lore repeat? Who, having fed the sacred fire, And duly bathed, as texts require, Will cheer, when evening rites are done, The father mourning for his son? Who will the daily meal provide For the poor wretch who lacks a guide, Feeding the helpless with the best Berries and roots, like some dear guest? How can these hands subsistence find For thy poor mother, old and blind? The wretched votaress how sustain, Who mourns her child in ceaseless pain? Stay yet a while, my darling, stay, Nor fly to Yama's realm to-day. To-morrow I thy sire and she Who bare thee, child, will go with, thee.337 337 So dying York cries over the body of Suffolk: “Tarry, dear cousin Suffolk! My soul shall thine keep company to heaven:
- **Translation**: 

---

### Verse 16 (Ramayan 0.616)
- **Original**: 598 The Ramayana Then when I look on Yama, I To great Vivasvat's son will cry: “Hear, King of justice, and restore Our child to feed us, I implore. Lord of the world, of mighty fame, Faithful and just, admit my claim, And grant this single boon to free My soul from fear, to one like me.” Because, my son, untouched by stain, By sinful hands thou fallest slain, Win, through thy truth, the sphere where those Who die by hostile darts repose. Seek the blest home prepared for all The valiant who in battle fall, Who face the foe and scorn to yield, In glory dying on the field. Rise to the heaven where Dhundhumár And Nahush, mighty heroes, are, Where Janamejay and the blest Dilípa, Sagar, Saivya, rest: Home of all virtuous spirits, earned By fervent rites and Scripture learned: By those whose sacred fires have glowed, Whose liberal hands have fields bestowed: By givers of a thousand cows, By lovers of one faithful spouse: By those who serve their masters well, And cast away this earthly shell. None of my race can ever know The bitter pain of lasting woe. But doomed to that dire fate is he Tarry, sweet soul, for mine, then fly abreast.” King Henry V, Act IV, 6.
- **Translation**: 

---

### Verse 17 (Ramayan 0.617)
- **Original**: Canto LXIV. Dasaratha's Death. 599 Whose guilty hand has slaughtered thee.” Thus with wild tears the aged saint Made many a time his piteous plaint, Then with his wife began to shed The funeral water for the dead. But in a shape celestial clad, Won by the merits of the lad, The spirit from the body brake And to the mourning parents spake: “A glorious home in realms above Rewards my care and filial love. You, honoured parents, soon shall be Partakers of that home with me.” He spake, and swiftly mounting high, With Indra near him, to the sky On a bright car, with flame that glowed, Sublime the duteous hermit rode. The father, with his consort's aid, The funeral rites with water paid, And thus his speech to me renewed Who stood in suppliant attitude: “Slay me this day, O, slay me, King, For death no longer has a sting. Childless am I: thy dart has done To death my dear, my only son. Because the boy I loved so well Slain by thy heedless arrow fell, My curse upon thy soul shall press With bitter woe and heaviness. I mourn a slaughtered child, and thou Shalt feel the pangs that kill me now. Bereft and suffering e'en as I,
- **Translation**: 

---

### Verse 18 (Ramayan 0.618)
- **Original**: 600 The Ramayana So shalt thou mourn thy son, and die. Thy hand unwitting dealt the blow That laid a holy hermit low, And distant, therefore, is the time When thou shalt suffer for the crime. The hour shall come when, crushed by woes Like these I feel, thy life shall close: A debt to pay in after days Like his the priestly fee who pays.” This curse on me the hermit laid, Nor yet his tears and groans were stayed. Then on the pyre their bodies cast The pair; and straight to heaven they passed. As in sad thought I pondered long Back to my memory came the wrong Done in wild youth, O lady dear, When 'twas my boast to shoot by ear.[172] The deed has borne the fruit, which now Hangs ripe upon the bending bough: Thus dainty meats the palate please, And lure the weak to swift disease. Now on my soul return with dread The words that noble hermit said, That I for a dear son should grieve, And of the woe my life should leave.” Thus spake the king with many a tear; Then to his wife he cried in fear: “I cannot see thee, love; but lay Thy gentle hand in mine, I pray. Ah me, if Ráma touched me thus, If once, returning home to us, He bade me wealth and lordship give,
- **Translation**: 

---

### Verse 19 (Ramayan 0.619)
- **Original**: Canto LXIV. Dasaratha's Death. 601 Then, so I think, my soul would live. Unlike myself, unjust and mean Have been my ways with him, my Queen, But like himself is all that he, My noble son, has done to me. His son, though far from right he stray, What prudent sire would cast away? What banished son would check his ire, Nor speak reproaches of his sire? I see thee not: these eyes grow blind, And memory quits my troubled mind. Angels of Death are round me: they Summon my soul with speed away. What woe more grievous can there be, That, when from light and life I flee, I may not, ere I part, behold My virtuous Ráma, true and bold? Grief for my son, the brave and true, Whose joy it was my will to do, Dries up my breath, as summer dries The last drop in the pool that lies. Not men, but blessed Gods, are they Whose eyes shall see his face that day; See him, when fourteen years are past, With earrings decked return at last. My fainting mind forgets to think: Low and more low my spirits sink. Each from its seat, my senses steal: I cannot hear, or taste, or feel. This lethargy of soul o'ercomes Each organ, and its function numbs: So when the oil begins to fail, The torch's rays grow faint and pale. This flood of woe caused by this hand
- **Translation**: 

---

### Verse 20 (Ramayan 0.620)
- **Original**: 602 The Ramayana Destroys me helpless and unmanned, Resistless as the floods that bore A passage through the river shore. Ah Raghu's son, ah mighty-armed, By whom my cares were soothed and charmed, My son in whom I took delight, Now vanished from thy father's sight! Kau [alyá, ah, I cannot see; Sumitrá, gentle devotee! Alas, Kaikeyí, cruel dame, My bitter foe, thy father's shame!” Kau [alyá and Sumitrá kept Their watch beside him as he wept. And Da [aratha moaned and sighed, And grieving for his darling died. Canto LXV. The Women's Lament. And now the night had past away, And brightly dawned another day; The minstrels, trained to play and sing, Flocked to the chamber of the king: Bards, who their gayest raiment wore, And heralds famed for ancient lore: And singers, with their songs of praise, Made music in their several ways. There as they poured their blessings choice And hailed their king with hand and voice, Their praises with a swelling roar Echoed through court and corridor.
- **Translation**: 

---

