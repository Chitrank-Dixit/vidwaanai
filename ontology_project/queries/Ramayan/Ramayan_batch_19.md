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

### Verse 1 (Ramayan 0.361)
- **Original**: Canto IX. The Plot. 343 “Soon must thou to the monarch say Kaikeyí's soul has past away, Or, Ráma banished as we planned, My son made king shall rule the land. No more for gold and gems I care, For brave attire or dainty fare. If Ráma should the throne ascend, That very hour my life will end.” The royal lady wounded through The bosom with the darts that flew Launched from the hump-back's tongue Pressed both her hands upon her side, And o'er and o'er again she cried With wildering fury stung: “Yes, it shall be thy task to tell That I have hurried hence to dwell In Yáma's realms of woe, Or happy Bharat shall be king, And doomed to years of wandering Kau [alyá's son shall go. I heed not dainty viands now Fair wreaths of flowers to twine my brow, Soft balm or precious scent: My very life I count as naught, Nothing on earth can claim my thought But Ráma's banishment.” She spoke these words of cruel ire; Then stripping off her gay attire, The cold bare floor she pressed. So, falling from her home on high, Some lovely daughter of the sky Upon the ground might rest. With darkened brow and furious mien,
- **Translation**: 

---

### Verse 2 (Ramayan 0.362)
- **Original**: 344 The Ramayana Stripped of her gems and wreath, the queen In spotless beauty lay, Like heaven obscured with gathering cloud, When shades of midnight darkness shroud Each star's expiring ray. Canto X. Dasaratha's Speech. As Queen Kaikeyí thus obeyed The sinful counsel of her maid She sank upon the chamber floor, As sinks in anguish, wounded sore, An elephant beneath the smart Of the wild hunter's venomed dart. The lovely lady in her mind Revolved the plot her maid designed, And prompt the gain and risk to scan She step by step approved the plan. Misguided by the hump-back's guile She pondered her resolve awhile, As the fair path that bliss secured The miserable lady lured,[101] Devoted to her queen, and swayed By hopes of gain and bliss, the maid Rejoiced, her lady's purpose known, And deemed the prize she sought her own. Then bent upon her purpose dire, Kaikeyí with her soul on fire, Upon the floor lay, languid, down, Her brows contracted in a frown. The bright-hued wreath that bound her hair,
- **Translation**: 

---

### Verse 3 (Ramayan 0.363)
- **Original**: Canto X. Dasaratha's Speech. 345 Chains, necklets, jewels rich and rare, Stripped off by her own fingers lay Spread on the ground in disarray, And to the floor a lustre lent As stars light up the firmament. Thus prostrate in the mourner's cell, In garb of woe the lady fell, Her long hair in a single braid, Like some fair nymph of heaven dismayed.272 The monarch, Ráma to install, With thoughtful care had ordered all, And now within his home withdrew, Dismissing first his retinue. Now all the town has heard, thought he, What joyful rite the morn will see. So turned he to her bower to cheer With the glad news his darling's ear. Majestic, as the Lord of Night, When threatened by the Dragon's might, Bursts radiant on the evening sky Pale with the clouds that wander by, So Da[aratha, great in fame, To Queen Kaikeyí's palace came. There parrots flew from tree to tree, And gorgeous peacocks wandered free, While ever and anon was heard The note of some glad water-bird. Here loitered dwarf and hump-backed maid, There lute and lyre sweet music played. 272 These verses are evidently an interpolation. They contain nothing that has not been already related: the words only are altered. As the whole poem could not be recited at once, the rhapsodists at the beginning of a fresh recitation would naturally remind their hearers of the events immediately preceding.
- **Translation**: 

---

### Verse 4 (Ramayan 0.364)
- **Original**: 346 The Ramayana Here, rich in blossom, creepers twined O'er grots with wondrous art designed, There Champac and A[oka flowers Hung glorious o'er the summer bowers, And mid the waving verdure rose Gold, silver, ivory porticoes. Through all the months in ceaseless store The trees both fruit and blossom bore. With many a lake the grounds were graced; Seats gold and silver, here were placed; Here every viand wooed the taste, It was a garden meet to vie E'en with the home of Gods on high. Within the mansion rich and vast The mighty Da[aratha passed: Not there was his beloved queen On her fair couch reclining seen. With love his eager pulses beat For the dear wife he came to meet, And in his blissful hopes deceived, He sought his absent love and grieved. For never had she missed the hour Of meeting in her sumptuous bower, And never had the king of men Entered the empty room till then. Still urged by love and anxious thought News of his favourite queen he sought, For never had his loving eyes Found her or selfish or unwise. Then spoke at length the warder maid, With hands upraised and sore afraid: “My Lord and King, the queen has sought The mourner's cell with rage distraught.”
- **Translation**: 

---

### Verse 5 (Ramayan 0.365)
- **Original**: Canto X. Dasaratha's Speech. 347 The words the warder maiden said He heard with soul disquieted, And thus as fiercer grief assailed, His troubled senses wellnigh failed. Consumed by torturing fires of grief The king, the world's imperial chief, His lady lying on the ground In most unqueenly posture, found. The aged king, all pure within, Saw the young queen resolved on sin, Low on the ground, his own sweet wife, To him far dearer than his life, Like some fair creeping plant uptorn, Or like a maid of heaven forlorn, A nymph of air or Goddess sent From Swarga down in banishment. As some wild elephant who tries To soothe his consort as she lies Struck by the hunter's venomed dart, So the great king disturbed in heart, Strove with soft hand and fond caress To soothe his darling queen's distress, And in his love addressed with sighs The lady of the lotus eyes: “I know not, Queen, why thou shouldst be Thus angered to the heart with me. Say, who has slighted thee, or whence Has come the cause of such offence That in the dust thou liest low, And rendest my fond heart with woe, As if some goblin of the night Had struck thee with a deadly blight, And cast foul influence on her
- **Translation**: 

---

### Verse 6 (Ramayan 0.366)
- **Original**: 348 The Ramayana Whose spells my loving bosom stir? I have Physicians famed for skill, Each trained to cure some special ill: My sweetest lady, tell thy pain, And they shall make thee well again. Whom, darling, wouldst thou punished see? Or whom enriched with lordly fee?[102] Weep not, my lovely Queen, and stay This grief that wears thy frame away; Speak, and the guilty shall be freed. The guiltless be condemned to bleed, The poor enriched, the rich abased, The low set high, the proud disgraced. My lords and I thy will obey, All slaves who own thy sovereign sway; And I can ne'er my heart incline To check in aught one wish of thine. Now by my life I pray thee tell The thoughts that in thy bosom dwell. The power and might thou knowest well, Should from thy breast all doubt expel. I swear by all my merit won, Speak, and thy pleasure shall be done. Far as the world's wide bounds extend My glorious empire knows no end. Mine are the tribes in eastern lands, And those who dwell on Sindhu's sands: Mine is Suráshmra, far away, Suvíra's realm admits my sway. My best the southern nations fear, The Angas and the Vangas hear. And as lord paramount I reign O'er Magadh and the Matsyas' plain,
- **Translation**: 

---

### Verse 7 (Ramayan 0.367)
- **Original**: Canto XI. The Queen's Demand. 349 Ko [al, and Ká[i's wide domain:273 All rich in treasures of the mine, In golden corn, sheep, goats, and kine. Choose what thou wilt. Kaikeyí, thence: But tell me, O my darling, whence Arose thy grief, and it shall fly Like hoar-frost when the sun is high.” She, by his loving words consoled, Longed her dire purpose to unfold, And sought with sharper pangs to wring The bosom of her lord the king. Canto XI. The Queen's Demand. To him enthralled by love, and blind, Pierced by his darts who shakes the mind,274 Kaikeyí with remorseless breast Her grand purpose thus expressed: “O King, no insult or neglect Have I endured, or disrespect. One wish I have, and faith would see That longing granted, lord, by thee. Now pledge thy word if thou incline To listen to this prayer of mine, Then I with confidence will speak, And thou shalt hear the boon I seek.” 273 The [lokaor distich which I have been forced to expand into these nine lines is evidently spurious, but is found in all the commented MSS. which Schlegel consulted. 274 Manmatha, Mind-disturber, a name of Káma or Love.
- **Translation**: 

---

### Verse 8 (Ramayan 0.368)
- **Original**: 350 The Ramayana Ere she had ceased, the monarch fell, A victim to the lady's spell, And to the deadly snare she set Sprang, like a roebuck to the net. Her lover raised her drooping head, Smiled, playing with her hair, and said: “Hast thou not learnt, wild dame, till now That there is none so dear as thou To me thy loving husband, save My Ráma bravest of the brave? By him my race's high-souled heir, By him whom none can match, I swear, Now speak the wish that on thee weighs: By him whose right is length of days, Whom if my fond paternal eye Saw not one hour I needs must die,— I swear by Ráma my dear son, Speak, and thy bidding shall be done. Speak, darling; if thou choose, request To have the heart from out my breast; Regard my words, sweet love, and name The wish thy mind thinks fit to frame. Nor let thy soul give way to doubt: My power should drive suspicion out. Yea, by my merits won I swear, Speak, darling, I will grant thy prayer.” The queen, ambitious, overjoyed To see him by her plot decoyed, More eager still her aims to reach, Spoke her abominable speech: “A boon thou grantest, nothing loth, And swearest with repeated oath. Now let the thirty Gods and three
- **Translation**: 

---

### Verse 9 (Ramayan 0.369)
- **Original**: Canto XI. The Queen's Demand. 351 My witnesses, with Indra, be. Let sun and moon and planets hear, Heaven, quarters, day and night, give ear. The mighty world, the earth outspread, With bards of heaven and demons dread; The ghosts that walk in midnight shade, And household Gods, our present aid, A every being great and small To hear and mark the oath I call.” When thus the archer king was bound, With treacherous arts and oaths enwound, She to her bounteous lord subdued By blinding love, her speech renewed: “Remember, King, that long-past day Of Gods' and demons' battle fray. And how thy foe in doubtful strife Had nigh bereft thee of thy life. Remember, it was only I Preserved thee when about to die, And thou for watchful love and care Wouldst grant my first and second prayer. Those offered boons, pledged with thee then, I now demand, O King of men, [103] Of thee, O Monarch, good and just, Whose righteous soul observes each trust. If thou refuse thy promise sworn, I die, despised, before the morn. These rites in Ráma's name begun— Transfer them, and enthrone my son. The time is come to claim at last The double boon of days long-past, When Gods and demons met in fight, And thou wouldst fain my care requite.
- **Translation**: 

---

### Verse 10 (Ramayan 0.370)
- **Original**: 352 The Ramayana Now forth to DaG ak's forest drive Thy Ráma for nine years and five, And let him dwell a hermit there With deerskin coat and matted hair. Without a rival let my boy The empire of the land enjoy, And let mine eyes ere morning see Thy Ráma to the forest flee.” Canto XII. Dasaratha's Lament. The monarch, as Kaikeyí pressed With cruel words her dire request, Stood for a time absorbed in thought While anguish in his bosom wrought. “Does some wild dream my heart assail? Or do my troubled senses fail? Does some dire portent scare my view? Or frenzy's stroke my soul subdue?” Thus as he thought, his troubled mind In doubt and dread no rest could find, Distressed and trembling like a deer Who sees the dreaded tigress near. On the bare ground his limbs he threw, And many a long deep sigh he drew, Like a wild snake, with fury blind, By charms within a ring confined. Once as the monarch's fury woke, “Shame on thee!” from his bosom broke, And then in sense-bewildering pain He fainted on the ground again.
- **Translation**: 

---

### Verse 11 (Ramayan 0.371)
- **Original**: Canto XII. Dasaratha's Lament. 353 At length, when slowly strength returned, He answered as his eyeballs burned With the wild fury of his ire Consuming her, as 'twere, with fire: “Fell traitress, thou whose thoughts design The utter ruin of my line, What wrong have I or Ráma done? Speak murderess, speak thou wicked one, Seeks he not evermore to please Thee with all sonlike courtesies? By what persuasion art thou led To bring this ruin on his head? Ah me, that fondly unaware I brought thee home my life to share, Called daughter of a king, in truth A serpent with a venomed tooth! What fault can I pretend to find In Ráma praised by all mankind, That I my darling should forsake? No, take my life, my glory take: Let either queen be from me torn, But not my well-loved eldest-born. Him but to see is highest bliss, And death itself his face to miss. The world may sunless stand, the grain May thrive without the genial rain, But if my Ráma be not nigh My spirit from its frame will fly. Enough, thine impious plan forgo, O thou who plottest sin and woe. My head before thy feet, I kneel, And pray thee some compassion feel. O wicked dame, what can have led Thy heart to dare a plot so dread?
- **Translation**: 

---

### Verse 12 (Ramayan 0.372)
- **Original**: 354 The Ramayana Perchance thy purpose is to sound The grace thy son with me has found; Perchance the words that, all these days, Thou still hast said in Ráma's praise, Were only feigned, designed to cheer With flatteries a father's ear. Soon as thy grief, my Queen, I knew, My bosom felt the anguish too. In empty halls art thou possessed, And subject to anothers' hest? Now on Ikshváku's ancient race Falls foul disorder and disgrace, If thou, O Queen, whose heart so long Has loved the good should choose the wrong. Not once, O large-eyed dame, hast thou Been guilty of offence till now, Nor said a word to make me grieve, Now will I now thy sin believe. With thee my Ráma used to hold Like place with Bharat lofty-souled. As thou so often, when the pair Were children yet, wouldst fain declare. And can thy righteous soul endure That Ráma glorious, pious, pure, Should to the distant wilds be sent For fourteen years of banishment? Yea, Ráma Bharat's self exceeds In love to thee and sonlike deeds, And, for deserving love of thee, As Bharat, even so is he. Who better than that chieftain may Obedience, love, and honour pay, Thy dignity with care protect, Thy slightest word and wish respect?
- **Translation**: 

---

### Verse 13 (Ramayan 0.373)
- **Original**: Canto XII. Dasaratha's Lament. 355 Of all his countless followers none Can breathe a word against my son; Of many thousands not a dame Can hint reproach or whisper blame. All creatures feel the sweet control Of Ráma's pure and gentle soul. The pride of Manu's race he binds To him the people's grateful minds. He wins the subjects with his truth, [104] The poor with gifts and gentle ruth, His teachers with his docile will, The foemen with his archer skill. Truth, purity, religious zeal, The hand to give, the heart to feel, The love that ne'er betrays a friend, The rectitude that naught can bend, Knowledge, and meek obedience grace My Ráma pride of Raghu's race. Canst thou thine impious plot design 'Gainst him in whom these virtues shine, Whose glory with the sages vies, Peer of the Gods who rule the skies! From him no harsh or bitter word To pain one creature have I heard, And how can I my son address, For thee, with words of bitterness? Have mercy, Queen: some pity show To see my tears of anguish flow, And listen to my mournful cry, A poor old man who soon must die. Whate'er this sea-girt land can boast Of rich and rare from coast to coast, To thee, my Queen, I give it all: But O, thy deadly words recall:
- **Translation**: 

---

### Verse 14 (Ramayan 0.374)
- **Original**: 356 The Ramayana O see, my suppliant hands entreat, Again my lips are on thy feet: Save Ráma, save my darling child, Nor kill me with this sin defiled.” He grovelled on the ground, and lay To burning grief a senseless prey, And ever and anon, assailed By floods of woe he wept and wailed, Striving with eager speed to gain The margent of his sea of pain. With fiercer words she fiercer yet The hapless father's pleading met: “O Monarch, if thy soul repent The promise and thy free consent, How wilt thou in the world maintain Thy fame for truth unsmirched with stain? When gathered kings with thee converse, And bid thee all the tale rehearse, What wilt thou say, O truthful King, In answer to their questioning? “She to whose love my life I owe, Who saved me smitten by the foe, Kaikeyí, for her tender care, Was cheated of the oath I sware.” Thus wilt thou answer, and forsworn Wilt draw on thee the princes' scorn. Learn from that tale, the Hawk and Dove,275 How strong for truth was Saivya's love. Pledged by his word the monarch gave His flesh the suppliant bird to save. So King Alarka gave his eyes, 275 This story is told in the Mahábhárat. A free version of it may be found in Scenes from the Rámáyan, etc.
- **Translation**: 

---

### Verse 15 (Ramayan 0.375)
- **Original**: Canto XII. Dasaratha's Lament. 357 And gained a mansion in the skies. The Sea himself his promise keeps, And ne'er beyond his limit sweeps. My deeds of old again recall, Nor let thy bond dishonoured fall. The rights of truth thou wouldst forget, Thy Ráma on the throne to set, And let thy days in pleasure glide, Fond King, Kau[alyá by thy side. Now call it by what name thou wilt, Justice, injustice, virtue, guilt, Thy word and oath remain the same, And thou must yield what thus I claim. If Ráma be anointed, I This very day will surely die, Before thy face will poison drink, And lifeless at thy feet will sink. Yea, better far to die than stay Alive to see one single day The crowds before Kau[alyá stand And hail her queen with reverent hand. Now by my son, myself, I swear, No gift, no promise whatsoe'er My steadfast soul shall now content, But only Ráma's banishment.” So far she spake by rage impelled, And then the queen deep silence held. He heard her speech full fraught with ill, But spoke no word bewildered still, Gazed on his love once held so dear Who spoke unlovely rede to hear; Then as he slowly pondered o'er The queen's resolve and oath she swore.
- **Translation**: 

---

### Verse 16 (Ramayan 0.376)
- **Original**: 358 The Ramayana Once sighing forth, Ah Ráma! he Fell prone as falls a smitten tree. His senses lost like one insane, Faint as a sick man weak with pain, Or like a wounded snake dismayed, So lay the king whom earth obeyed. Long burning sighs he slowly heaved, As, conquered by his woe, he grieved, And thus with tears and sobs between His sad faint words addressed the queen: “By whom, Kaikeyí, wast thou taught This flattering hope with ruin fraught? Have goblins seized thy soul, O dame, Who thus canst speak and feel no shame? Thy mind with sin is sicklied o'er, From thy first youth ne'er seen before. A good and loving wife wast thou, But all, alas! is altered now. What terror can have seized thy breast To make thee frame this dire request, That Bharat o'er the land may reign, And Ráma in the woods remain? Turn from thine evil ways, O turn, And thy perfidious counsel spurn, If thou would fain a favour do To people, lord, and Bharat too. O wicked traitress, fierce and vile, Who lovest deeds of sin and guile,[105] What crime or grievance dost thou see, What fault in Ráma or in me? Thy son will ne'er the throne accept If Ráma from his rights be kept, For Bharat's heart more firmly yet
- **Translation**: 

---

### Verse 17 (Ramayan 0.377)
- **Original**: Canto XII. Dasaratha's Lament. 359 Than Ráma's is on justice set. How shall I say, Go forth, and brook Upon my Ráma's face to look, See his pale cheek and ashy lips Dimmed like the moon in sad eclipse? How see the plan so well prepared When prudent friends my counsels shared, All ruined, like a host laid low Beneath some foeman's murderous blow. What will these gathered princes say, From regions near and far away? “O'erlong endures the monarch's reign, or now he is a child again.” When many a good and holy sage In Scripture versed, revered for age, Shall ask for Ráma, what shall I Unhappy, what shall I reply? “By Queen Kaikeyí long distressed I drove him forth and dispossessed.” Although herein the truth I speak, They all will hold me false and weak. What will Kau[alyá say when she Demands her son exiled by me? Alas! what answer shall I frame, Or how console the injured dame? She like a slave on me attends, And with a sister's care she blends A mother's love, a wife's, a friend's. In spite of all her tender care, Her noble son, her face most fair, Another queen I could prefer And for thy sake neglected her, But now, O Queen, my heart is grieved For love and care by thee received,
- **Translation**: 

---

### Verse 18 (Ramayan 0.378)
- **Original**: 360 The Ramayana E'en as the sickening wretch repents His dainty meal and condiments. And how will Queen Sumitrá trust The husband whom she finds unjust, Seeing my Ráma driven hence Dishonoured, and for no offence? Ah! the Videhan bride will hear A double woe, a double fear, Two whelming sorrows at one breath, Her lord's disgrace, his father's death. Mine aged bosom she will wring And kill me with her sorrowing, Sad as a fair nymph left to weep Deserted on Himálaya's steep. For short will be my days, I ween, When I with mournful eyes have seen My Ráma wandering forth alone And heard dear Sítá sob and moan. Ah me! my fond belief I rue. Vile traitress, loved as good and true, As one who in his thirst has quaffed, Deceived by looks, a deadly draught. Ah! thou hast slain me, murderess, while Soothing my soul with words of guile, As the wild hunter kills the deer Lured from the brake his song to hear. Soon every honest tongue will fling Reproach on the dishonest king; The people's scorn in every street The seller of his child will meet, And such dishonour will be mine As whelms a Bráhman drunk with wine. Ah me, for my unhappy fate, Compelled thy words to tolerate!
- **Translation**: 

---

### Verse 19 (Ramayan 0.379)
- **Original**: Canto XII. Dasaratha's Lament. 361 Such woe is sent to scourge a crime Committed in some distant time. For many a day with sinful care I cherished thee, thou sin and snare, Kept thee, unwitting, like a cord Destined to bind its hapless lord. Mine hours of ease I spent with thee, Nor deemed my love my death would be, While like a heedless child I played, On a black snake my hand I laid. A cry from every mouth will burst And all the world will hold me curst, Because I saw my high-souled son Unkinged, unfathered, and undone; “The king by power of love beguiled Is weaker than a foolish child, His own beloved son to make An exile for a woman's sake. By chaste and holy vows restrained, By reverend teachers duly trained. When he his virtue's fruit should taste He falls by sin and woe disgraced.” Two words will all his answer be When I pronounce the stern decree, “Hence, Ráma, to the woods away,” All he will say is, I obey. O, if he would my will withstand When banished from his home and land, This were a comfort in my woe; But he will ne'er do this, I know. My Ráma to the forest fled, And curses thick upon my head, Grim Death will bear me hence away, His world-abominated prey.
- **Translation**: 

---

### Verse 20 (Ramayan 0.380)
- **Original**: 362 The Ramayana When I am gone and Ráma too. How wilt thou those I love pursue? What vengeful sin will be designed Against the queens I leave behind? When thou hast slain her son and me Kau [alyá soon will follow: she Will sink beneath her sorrows' weight, And die like me disconsolate. Exist, Kaikeyí, in thy pride, And let thy heart be gratified, When thou my queens and me hast hurled, And children, to the under world. Soon wilt thou rule as empress o'er My noble house unvext before. But then to wild confusion left,[106] Of Ráma and of me bereft. If Bharat to thy plan consent And long for Ráma's banishment, Ne'er let his hands presume to pay The funeral honours to my clay. Vile foe, thou cause of all mine ill, Obtain at last thy cursed will. A widow soon shalt thou enjoy The sweets of empire with thy boy. O Princess, sure some evil fate First brought thee here to devastate, In whom the night of ruin lies Veiled in a consort's fair disguise. The scorn of all and deepest shame Will long pursue my hated name, And dire disgrace on me will press, Misled by thee to wickedness. How shall my Ráma, whom, before, His elephant or chariot bore,
- **Translation**: 

---

