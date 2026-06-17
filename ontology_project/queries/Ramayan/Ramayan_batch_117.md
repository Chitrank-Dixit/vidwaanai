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

### Verse 1 (Ramayana 0.366)
- **Original**: 348 The Ramayana Whose spells my loving bosom stir? I have Physicians famed for skill, Each trained to cure some special ill: My sweetest lady, tell thy pain, And they shall make thee well again. Whom, darling, wouldst thou punished see? Or whom enriched with lordly fee?[102] Weep not, my lovely Queen, and stay This grief that wears thy frame away; Speak, and the guilty shall be freed. The guiltless be condemned to bleed, The poor enriched, the rich abased, The low set high, the proud disgraced. My lords and I thy will obey, All slaves who own thy sovereign sway; And I can ne'er my heart incline To check in aught one wish of thine. Now by my life I pray thee tell The thoughts that in thy bosom dwell. The power and might thou knowest well, Should from thy breast all doubt expel. I swear by all my merit won, Speak, and thy pleasure shall be done. Far as the world's wide bounds extend My glorious empire knows no end. Mine are the tribes in eastern lands, And those who dwell on Sindhu's sands: Mine is Suráshmra, far away, Suvíra's realm admits my sway. My best the southern nations fear, The Angas and the Vangas hear. And as lord paramount I reign O'er Magadh and the Matsyas' plain,
- **Translation**: 

---

### Verse 2 (Ramayana 0.367)
- **Original**: Canto XI. The Queen's Demand. 349 Ko [al, and Ká[i's wide domain:273 All rich in treasures of the mine, In golden corn, sheep, goats, and kine. Choose what thou wilt. Kaikeyí, thence: But tell me, O my darling, whence Arose thy grief, and it shall fly Like hoar-frost when the sun is high.” She, by his loving words consoled, Longed her dire purpose to unfold, And sought with sharper pangs to wring The bosom of her lord the king. Canto XI. The Queen's Demand. To him enthralled by love, and blind, Pierced by his darts who shakes the mind,274 Kaikeyí with remorseless breast Her grand purpose thus expressed: “O King, no insult or neglect Have I endured, or disrespect. One wish I have, and faith would see That longing granted, lord, by thee. Now pledge thy word if thou incline To listen to this prayer of mine, Then I with confidence will speak, And thou shalt hear the boon I seek.” 273 The [lokaor distich which I have been forced to expand into these nine lines is evidently spurious, but is found in all the commented MSS. which Schlegel consulted. 274 Manmatha, Mind-disturber, a name of Káma or Love.
- **Translation**: 

---

### Verse 3 (Ramayana 0.368)
- **Original**: 350 The Ramayana Ere she had ceased, the monarch fell, A victim to the lady's spell, And to the deadly snare she set Sprang, like a roebuck to the net. Her lover raised her drooping head, Smiled, playing with her hair, and said: “Hast thou not learnt, wild dame, till now That there is none so dear as thou To me thy loving husband, save My Ráma bravest of the brave? By him my race's high-souled heir, By him whom none can match, I swear, Now speak the wish that on thee weighs: By him whose right is length of days, Whom if my fond paternal eye Saw not one hour I needs must die,— I swear by Ráma my dear son, Speak, and thy bidding shall be done. Speak, darling; if thou choose, request To have the heart from out my breast; Regard my words, sweet love, and name The wish thy mind thinks fit to frame. Nor let thy soul give way to doubt: My power should drive suspicion out. Yea, by my merits won I swear, Speak, darling, I will grant thy prayer.” The queen, ambitious, overjoyed To see him by her plot decoyed, More eager still her aims to reach, Spoke her abominable speech: “A boon thou grantest, nothing loth, And swearest with repeated oath. Now let the thirty Gods and three
- **Translation**: 

---

### Verse 4 (Ramayana 0.369)
- **Original**: Canto XI. The Queen's Demand. 351 My witnesses, with Indra, be. Let sun and moon and planets hear, Heaven, quarters, day and night, give ear. The mighty world, the earth outspread, With bards of heaven and demons dread; The ghosts that walk in midnight shade, And household Gods, our present aid, A every being great and small To hear and mark the oath I call.” When thus the archer king was bound, With treacherous arts and oaths enwound, She to her bounteous lord subdued By blinding love, her speech renewed: “Remember, King, that long-past day Of Gods' and demons' battle fray. And how thy foe in doubtful strife Had nigh bereft thee of thy life. Remember, it was only I Preserved thee when about to die, And thou for watchful love and care Wouldst grant my first and second prayer. Those offered boons, pledged with thee then, I now demand, O King of men, [103] Of thee, O Monarch, good and just, Whose righteous soul observes each trust. If thou refuse thy promise sworn, I die, despised, before the morn. These rites in Ráma's name begun— Transfer them, and enthrone my son. The time is come to claim at last The double boon of days long-past, When Gods and demons met in fight, And thou wouldst fain my care requite.
- **Translation**: 

---

### Verse 5 (Ramayana 0.370)
- **Original**: 352 The Ramayana Now forth to DaG ak's forest drive Thy Ráma for nine years and five, And let him dwell a hermit there With deerskin coat and matted hair. Without a rival let my boy The empire of the land enjoy, And let mine eyes ere morning see Thy Ráma to the forest flee.” Canto XII. Dasaratha's Lament. The monarch, as Kaikeyí pressed With cruel words her dire request, Stood for a time absorbed in thought While anguish in his bosom wrought. “Does some wild dream my heart assail? Or do my troubled senses fail? Does some dire portent scare my view? Or frenzy's stroke my soul subdue?” Thus as he thought, his troubled mind In doubt and dread no rest could find, Distressed and trembling like a deer Who sees the dreaded tigress near. On the bare ground his limbs he threw, And many a long deep sigh he drew, Like a wild snake, with fury blind, By charms within a ring confined. Once as the monarch's fury woke, “Shame on thee!” from his bosom broke, And then in sense-bewildering pain He fainted on the ground again.
- **Translation**: 

---

### Verse 6 (Ramayana 0.371)
- **Original**: Canto XII. Dasaratha's Lament. 353 At length, when slowly strength returned, He answered as his eyeballs burned With the wild fury of his ire Consuming her, as 'twere, with fire: “Fell traitress, thou whose thoughts design The utter ruin of my line, What wrong have I or Ráma done? Speak murderess, speak thou wicked one, Seeks he not evermore to please Thee with all sonlike courtesies? By what persuasion art thou led To bring this ruin on his head? Ah me, that fondly unaware I brought thee home my life to share, Called daughter of a king, in truth A serpent with a venomed tooth! What fault can I pretend to find In Ráma praised by all mankind, That I my darling should forsake? No, take my life, my glory take: Let either queen be from me torn, But not my well-loved eldest-born. Him but to see is highest bliss, And death itself his face to miss. The world may sunless stand, the grain May thrive without the genial rain, But if my Ráma be not nigh My spirit from its frame will fly. Enough, thine impious plan forgo, O thou who plottest sin and woe. My head before thy feet, I kneel, And pray thee some compassion feel. O wicked dame, what can have led Thy heart to dare a plot so dread?
- **Translation**: 

---

### Verse 7 (Ramayana 0.372)
- **Original**: 354 The Ramayana Perchance thy purpose is to sound The grace thy son with me has found; Perchance the words that, all these days, Thou still hast said in Ráma's praise, Were only feigned, designed to cheer With flatteries a father's ear. Soon as thy grief, my Queen, I knew, My bosom felt the anguish too. In empty halls art thou possessed, And subject to anothers' hest? Now on Ikshváku's ancient race Falls foul disorder and disgrace, If thou, O Queen, whose heart so long Has loved the good should choose the wrong. Not once, O large-eyed dame, hast thou Been guilty of offence till now, Nor said a word to make me grieve, Now will I now thy sin believe. With thee my Ráma used to hold Like place with Bharat lofty-souled. As thou so often, when the pair Were children yet, wouldst fain declare. And can thy righteous soul endure That Ráma glorious, pious, pure, Should to the distant wilds be sent For fourteen years of banishment? Yea, Ráma Bharat's self exceeds In love to thee and sonlike deeds, And, for deserving love of thee, As Bharat, even so is he. Who better than that chieftain may Obedience, love, and honour pay, Thy dignity with care protect, Thy slightest word and wish respect?
- **Translation**: 

---

### Verse 8 (Ramayana 0.373)
- **Original**: Canto XII. Dasaratha's Lament. 355 Of all his countless followers none Can breathe a word against my son; Of many thousands not a dame Can hint reproach or whisper blame. All creatures feel the sweet control Of Ráma's pure and gentle soul. The pride of Manu's race he binds To him the people's grateful minds. He wins the subjects with his truth, [104] The poor with gifts and gentle ruth, His teachers with his docile will, The foemen with his archer skill. Truth, purity, religious zeal, The hand to give, the heart to feel, The love that ne'er betrays a friend, The rectitude that naught can bend, Knowledge, and meek obedience grace My Ráma pride of Raghu's race. Canst thou thine impious plot design 'Gainst him in whom these virtues shine, Whose glory with the sages vies, Peer of the Gods who rule the skies! From him no harsh or bitter word To pain one creature have I heard, And how can I my son address, For thee, with words of bitterness? Have mercy, Queen: some pity show To see my tears of anguish flow, And listen to my mournful cry, A poor old man who soon must die. Whate'er this sea-girt land can boast Of rich and rare from coast to coast, To thee, my Queen, I give it all: But O, thy deadly words recall:
- **Translation**: 

---

### Verse 9 (Ramayana 0.374)
- **Original**: 356 The Ramayana O see, my suppliant hands entreat, Again my lips are on thy feet: Save Ráma, save my darling child, Nor kill me with this sin defiled.” He grovelled on the ground, and lay To burning grief a senseless prey, And ever and anon, assailed By floods of woe he wept and wailed, Striving with eager speed to gain The margent of his sea of pain. With fiercer words she fiercer yet The hapless father's pleading met: “O Monarch, if thy soul repent The promise and thy free consent, How wilt thou in the world maintain Thy fame for truth unsmirched with stain? When gathered kings with thee converse, And bid thee all the tale rehearse, What wilt thou say, O truthful King, In answer to their questioning? “She to whose love my life I owe, Who saved me smitten by the foe, Kaikeyí, for her tender care, Was cheated of the oath I sware.” Thus wilt thou answer, and forsworn Wilt draw on thee the princes' scorn. Learn from that tale, the Hawk and Dove,275 How strong for truth was Saivya's love. Pledged by his word the monarch gave His flesh the suppliant bird to save. So King Alarka gave his eyes, 275 This story is told in the Mahábhárat. A free version of it may be found in Scenes from the Rámáyan, etc.
- **Translation**: 

---

### Verse 10 (Ramayana 0.375)
- **Original**: Canto XII. Dasaratha's Lament. 357 And gained a mansion in the skies. The Sea himself his promise keeps, And ne'er beyond his limit sweeps. My deeds of old again recall, Nor let thy bond dishonoured fall. The rights of truth thou wouldst forget, Thy Ráma on the throne to set, And let thy days in pleasure glide, Fond King, Kau[alyá by thy side. Now call it by what name thou wilt, Justice, injustice, virtue, guilt, Thy word and oath remain the same, And thou must yield what thus I claim. If Ráma be anointed, I This very day will surely die, Before thy face will poison drink, And lifeless at thy feet will sink. Yea, better far to die than stay Alive to see one single day The crowds before Kau[alyá stand And hail her queen with reverent hand. Now by my son, myself, I swear, No gift, no promise whatsoe'er My steadfast soul shall now content, But only Ráma's banishment.” So far she spake by rage impelled, And then the queen deep silence held. He heard her speech full fraught with ill, But spoke no word bewildered still, Gazed on his love once held so dear Who spoke unlovely rede to hear; Then as he slowly pondered o'er The queen's resolve and oath she swore.
- **Translation**: 

---

### Verse 11 (Ramayana 0.376)
- **Original**: 358 The Ramayana Once sighing forth, Ah Ráma! he Fell prone as falls a smitten tree. His senses lost like one insane, Faint as a sick man weak with pain, Or like a wounded snake dismayed, So lay the king whom earth obeyed. Long burning sighs he slowly heaved, As, conquered by his woe, he grieved, And thus with tears and sobs between His sad faint words addressed the queen: “By whom, Kaikeyí, wast thou taught This flattering hope with ruin fraught? Have goblins seized thy soul, O dame, Who thus canst speak and feel no shame? Thy mind with sin is sicklied o'er, From thy first youth ne'er seen before. A good and loving wife wast thou, But all, alas! is altered now. What terror can have seized thy breast To make thee frame this dire request, That Bharat o'er the land may reign, And Ráma in the woods remain? Turn from thine evil ways, O turn, And thy perfidious counsel spurn, If thou would fain a favour do To people, lord, and Bharat too. O wicked traitress, fierce and vile, Who lovest deeds of sin and guile,[105] What crime or grievance dost thou see, What fault in Ráma or in me? Thy son will ne'er the throne accept If Ráma from his rights be kept, For Bharat's heart more firmly yet
- **Translation**: 

---

### Verse 12 (Ramayana 0.377)
- **Original**: Canto XII. Dasaratha's Lament. 359 Than Ráma's is on justice set. How shall I say, Go forth, and brook Upon my Ráma's face to look, See his pale cheek and ashy lips Dimmed like the moon in sad eclipse? How see the plan so well prepared When prudent friends my counsels shared, All ruined, like a host laid low Beneath some foeman's murderous blow. What will these gathered princes say, From regions near and far away? “O'erlong endures the monarch's reign, or now he is a child again.” When many a good and holy sage In Scripture versed, revered for age, Shall ask for Ráma, what shall I Unhappy, what shall I reply? “By Queen Kaikeyí long distressed I drove him forth and dispossessed.” Although herein the truth I speak, They all will hold me false and weak. What will Kau[alyá say when she Demands her son exiled by me? Alas! what answer shall I frame, Or how console the injured dame? She like a slave on me attends, And with a sister's care she blends A mother's love, a wife's, a friend's. In spite of all her tender care, Her noble son, her face most fair, Another queen I could prefer And for thy sake neglected her, But now, O Queen, my heart is grieved For love and care by thee received,
- **Translation**: 

---

### Verse 13 (Ramayana 0.378)
- **Original**: 360 The Ramayana E'en as the sickening wretch repents His dainty meal and condiments. And how will Queen Sumitrá trust The husband whom she finds unjust, Seeing my Ráma driven hence Dishonoured, and for no offence? Ah! the Videhan bride will hear A double woe, a double fear, Two whelming sorrows at one breath, Her lord's disgrace, his father's death. Mine aged bosom she will wring And kill me with her sorrowing, Sad as a fair nymph left to weep Deserted on Himálaya's steep. For short will be my days, I ween, When I with mournful eyes have seen My Ráma wandering forth alone And heard dear Sítá sob and moan. Ah me! my fond belief I rue. Vile traitress, loved as good and true, As one who in his thirst has quaffed, Deceived by looks, a deadly draught. Ah! thou hast slain me, murderess, while Soothing my soul with words of guile, As the wild hunter kills the deer Lured from the brake his song to hear. Soon every honest tongue will fling Reproach on the dishonest king; The people's scorn in every street The seller of his child will meet, And such dishonour will be mine As whelms a Bráhman drunk with wine. Ah me, for my unhappy fate, Compelled thy words to tolerate!
- **Translation**: 

---

### Verse 14 (Ramayana 0.379)
- **Original**: Canto XII. Dasaratha's Lament. 361 Such woe is sent to scourge a crime Committed in some distant time. For many a day with sinful care I cherished thee, thou sin and snare, Kept thee, unwitting, like a cord Destined to bind its hapless lord. Mine hours of ease I spent with thee, Nor deemed my love my death would be, While like a heedless child I played, On a black snake my hand I laid. A cry from every mouth will burst And all the world will hold me curst, Because I saw my high-souled son Unkinged, unfathered, and undone; “The king by power of love beguiled Is weaker than a foolish child, His own beloved son to make An exile for a woman's sake. By chaste and holy vows restrained, By reverend teachers duly trained. When he his virtue's fruit should taste He falls by sin and woe disgraced.” Two words will all his answer be When I pronounce the stern decree, “Hence, Ráma, to the woods away,” All he will say is, I obey. O, if he would my will withstand When banished from his home and land, This were a comfort in my woe; But he will ne'er do this, I know. My Ráma to the forest fled, And curses thick upon my head, Grim Death will bear me hence away, His world-abominated prey.
- **Translation**: 

---

### Verse 15 (Ramayana 0.380)
- **Original**: 362 The Ramayana When I am gone and Ráma too. How wilt thou those I love pursue? What vengeful sin will be designed Against the queens I leave behind? When thou hast slain her son and me Kau [alyá soon will follow: she Will sink beneath her sorrows' weight, And die like me disconsolate. Exist, Kaikeyí, in thy pride, And let thy heart be gratified, When thou my queens and me hast hurled, And children, to the under world. Soon wilt thou rule as empress o'er My noble house unvext before. But then to wild confusion left,[106] Of Ráma and of me bereft. If Bharat to thy plan consent And long for Ráma's banishment, Ne'er let his hands presume to pay The funeral honours to my clay. Vile foe, thou cause of all mine ill, Obtain at last thy cursed will. A widow soon shalt thou enjoy The sweets of empire with thy boy. O Princess, sure some evil fate First brought thee here to devastate, In whom the night of ruin lies Veiled in a consort's fair disguise. The scorn of all and deepest shame Will long pursue my hated name, And dire disgrace on me will press, Misled by thee to wickedness. How shall my Ráma, whom, before, His elephant or chariot bore,
- **Translation**: 

---

### Verse 16 (Ramayana 0.381)
- **Original**: Canto XII. Dasaratha's Lament. 363 Now with his feet, a wanderer, tread The forest wilds around him spread? How shall my son, to please whose taste, The deftest cooks, with earrings graced, With rivalry and jealous care The dainty meal and cates prepare— How shall he now his life sustain With acid fruit and woodland grain? He spends his time unvext by cares, And robes of precious texture wears: How shall he, with one garment round His limbs recline upon the ground? Whose was this plan, this cruel thought Unheard till now, with ruin fraught, To make thy son Ayodhyá's king, And send my Ráma wandering? Shame, shame on women! Vile, untrue, Their selfish ends they still pursue. Not all of womankind I mean. But more than all this wicked queen. O worthless, cruel, selfish dame, I brought thee home, my plague and woe. What fault in me hast thou to blame, Or in my son who loves thee so? Fond wives may from their husbands flee, And fathers may their sons desert, But all the world would rave to see My Ráma touched with deadly hurt. I joy his very step to hear, As though his godlike form I viewed; And when I see my Ráma near I feel my youth again renewed. There might be life without the sun, Yea, e'en if Indra sent no rain,
- **Translation**: 

---

### Verse 17 (Ramayana 0.382)
- **Original**: 364 The Ramayana But, were my Ráma banished, none Would, so I think, alive remain. A foe that longs my life to take, I brought thee here my death to be, Caressed thee long, a venomed snake, And through my folly die. Ah me! Ráma and me and LakshmaG slay, And then with Bharat rule the state; So bring the kingdom to decay, And fawn on those thy lord who hate, Plotter of woe, for evil bred, For such a speech why do not all Thy teeth from out thy wicked head Split in a thousand pieces fall? My Ráma's words are ever kind, He knows not how to speak in ire: Then how canst thou presume to find A fault in him whom all admire? Yield to despair, go mad, or die, Or sink within the rifted earth; Thy fell request will I deny, Thou shamer of thy royal birth. Thy longer life I scarce can bear, Thou ruin of my home and race, Who wouldst my heart and heartstrings tear, Keen as a razor, false and base. My life is gone, why speak of joy? For what, without my son, were sweet? Spare, lady, him thou canst destroy; I pray thee as I touch thy feet.” He fell and wept with wild complaint, Heart-struck by her presumptuous speech, But could not touch, so weak and faint, The cruel feet he strove to reach.
- **Translation**: 

---

### Verse 18 (Ramayana 0.383)
- **Original**: Canto XIII. Dasaratha's Distress. 365 Canto XIII. Dasaratha's Distress. Unworthy of his mournful fate, The mighty king, unfortunate, Lay prostrate in unseemly guise, As, banished from the blissful skies, Yayáti, in his evil day. His merit all exhausted, lay.276 The queen, triumphant in the power Won by her beauty's fatal dower, Still terrible and unsubdued, Her dire demand again renewed: “Great Monarch, 'twas thy boast till now To love the truth and keep the vow; Then wherefore would thy lips refuse The promised boon 'tis mine to choose?” King Da[aratha, thus addressed, With anger raging in his breast, Sank for a while beneath the pain, Then to Kaikeyí spoke again: [107] “Childless so long, at length I won, With mighty toil, from Heaven a son, Ráma, the mighty-armed; and how Shall I desert my darling now? A scholar wise, a hero bold, Of patient mood, with wrath controlled, How can I bid my Ráma fly, My darling of the lotus eye? 276 Only the highest merit obtains a home in heaven for ever. Minor degrees of merit procure only leases of heavenly mansions terminable after periods proportioned to the fund which buys them. King Yayáti went to heaven and when his term expired was unceremoniously ejected, and thrown down to earth.
- **Translation**: 

---

### Verse 19 (Ramayana 0.384)
- **Original**: 366 The Ramayana In heaven itself I scarce could bear, When asking of my Ráma there, To hear the Gods his griefs declare, And O, that death would take me hence Before I wrong his innocence!” As thus the monarch wept and wailed, And maddening grief his heart assailed, The sun had sought his resting-place, And night was closing round apace. But yet the moon-crowned night could bring No comfort to the wretched king. As still he mourned with burning sighs And fixed his gaze upon the skies: “O Night whom starry fires adorn, I long not for the coming morn. Be kind and show some mercy: see, My suppliant hands are raised to thee. Nay, rather fly with swifter pace; No longer would I see the face Of Queen Kaikeyí, cruel, dread, Who brings this woe upon mine head.” Again with suppliant hands he tried To move the queen, and wept and sighed: “To me, unhappy me, inclined To good, sweet dame, thou shouldst be kind; Whose life is well-nigh fled, who cling To thee for succour, me thy king. This, only this, is all my claim: Have mercy, O my lovely dame. None else have I to take my part, Have mercy: thou art good at heart. Hear, lady of the soft black eye, And win a name that ne'er shall die:
- **Translation**: 

---

### Verse 20 (Ramayana 0.385)
- **Original**: Canto XIV. Ráma Summoned. 367 Let Ráma rule this glorious land, The gift of thine imperial hand. O lady of the dainty waist, With eyes and lips of beauty graced, Please Ráma, me, each saintly priest, Bharat, and all from chief to least.” She heard his wild and mournful cry, She saw the tears his speech that broke, Saw her good husband's reddened eye, But, cruel still, no word she spoke. His eyes upon her face he bent, And sought for mercy, but in vain: She claimed his darling's banishment, He swooned upon the ground again. Canto XIV. Ráma Summoned. The wicked queen her speech renewed, When rolling on the earth she viewed Ikshváku's son, Ayodhyá's king, For his dear Ráma sorrowing: “Why, by a simple promise bound, Liest thou prostrate on the ground, As though a grievous sin dismayed Thy spirit! Why so sore afraid? Keep still thy word. The righteous deem That truth, mid duties, is supreme: And now in truth and honour's name I bid thee own the binding claim. Zaivya, a king whom earth obeyed, Once to a hawk a promise made,
- **Translation**: 

---

