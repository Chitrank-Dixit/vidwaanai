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

### Verse 1 (Ramayana 0.426)
- **Original**: 408 The Ramayana Thus LakshmaG cried, the mighty-souled: Down her sad cheeks the torrents rolled, As to her son Kau[alyá spake: “Now thou hast heard thy brother, take His counsel if thou hold it wise, And do the thing his words advise, Do not, my son, with tears I pray, My rival's wicked word obey, Leave me not here consumed with woe, Nor to the wood, an exile, go. If thou, to virtue ever true, Thy duty's path would still pursue, The highest duty bids thee stay And thus thy mother's voice obey. Thus Ka[yap's great ascetic son A seat among the Immortals won: In his own home, subdued, he stayed, And honour to his mother paid. If reverence to thy sire be due, Thy mother claims like honour too, And thus I charge thee, O my child, Thou must not seek the forest wild. Ah, what to me were life and bliss, Condemned my darling son to miss? But with my Ráma near, to eat The very grass itself were sweet. But if thou still wilt go and leave Thy hapless mother here to grieve, I from that hour will food abjure, Nor life without my son endure. Then it will be thy fate to dwell In depth of world-detested hell. As Ocean in the olden time
- **Translation**: 

---

### Verse 2 (Ramayana 0.427)
- **Original**: Canto XXI. Kausalyá Calmed. 409 Was guilty of an impious crime That marked the lord of each fair flood As one who spills a Bráhman's blood.”288 Thus spake the queen, and wept, and sighed: Then righteous Ráma thus replied: “I have no power to slight or break Commandments which my father spake. I bend my head, dear lady, low, Forgive me, for I needs must go. Once KaGdu, mighty saint, who made His dwelling in the forest shade, [119] A cow — and duty's claims he knew— Obedient to his father, slew. And in the line from which we spring, When ordered by their sire the king, Through earth the sons of Sagar cleft, And countless things of life bereft.289 So Jamadagní's son290 obeyed His sire, when in the wood he laid His hand upon his axe, and smote Through Renuká his mother's throat. The deeds of these and more beside. Peers of the Gods, my steps shall guide, And resolute will I fulfil My father's word, my father's will. Nor I, O Queen, unsanctioned tread This righteous path, by duty led: The road my footsteps journey o'er Was traversed by the great of yore. 288 The commentators say that, in a former creation, Ocean grieved his mother and suffered in consequence the pains of hell. 289 As described in Book I Canto XL. 290 Parasúráma.
- **Translation**: 

---

### Verse 3 (Ramayana 0.428)
- **Original**: 410 The Ramayana This high command which all accept Shall faithfully by me be kept, For duty ne'er will him forsake Who fears his sire's command to break.” Thus to his mother wild with grief: Then thus to LakshmaG spake the chief Of those by whom the bow is bent, Mid all who speak, most eloquent: “I know what love for me thou hast, What firm devotion unsurpassed: Thy valour and thy worth I know, And glory that appals the foe. Blest youth, my mother's woe is great, It bends her 'neath its matchless weight: No claims will she, with blinded eyes, Of truth and patience recognize. For duty is supreme in place, And truth is duty's noblest base. Obedient to my sire's behest I serve the cause of duty best. For man should truly do whate'er To mother, Bráhman, sire, he sware: He must in duty's path remain, Nor let his word be pledged in vain. And, O my brother, how can I Obedience to this charge deny? Kaikeyí's tongue my purpose spurred, But 'twas my sire who gave the word. Cast these unholy thoughts aside Which smack of war and Warriors' pride; To duty's call, not wrath attend, And tread the path which I commend.”
- **Translation**: 

---

### Verse 4 (Ramayana 0.429)
- **Original**: Canto XXI. Kausalyá Calmed. 411 Ráma by fond affection moved His brother LakshmaG thus reproved; Then with joined hands and reverent head Again to Queen Kau[alyá said: “I needs must go— do thou consent— To the wild wood in banishment. O give me, by my life I pray, Thy blessing ere I go away. I, when the promised years are o'er, Shall see Ayodhyá's town once more. Then, mother dear, thy tears restrain, Nor let thy heart be wrung by pain: In time, my father's will obeyed, Shall I return from greenwood shade. My dear Videhan, thou, and I, Lakshma G, Sumitrá, feel this tie, And must my father's word obey, As duty bids that rules for aye. Thy preparations now forgo, And lock within thy breast thy woe, Nor be my pious wish withstood To go an exile to the wood.” Calm and unmoved the prince explained His duty's claim and purpose high, The mother life and sense regained, Looked on her son and made reply: “If reverence be thy father's due, The same by right and love is mine: Go not, my charge I thus renew, Nor leave me here in woe to pine, What were such lonely life to me, Rites to the shades, or deathless lot?
- **Translation**: 

---

### Verse 5 (Ramayana 0.430)
- **Original**: 412 The Ramayana More dear, my son, one hour with thee Than all the world where thou art not.” As bursts to view, when brands blaze high, Some elephant concealed by night, So, when he heard his mother's cry, Burnt Ráma's grief with fiercer might. Thus to the queen, half senseless still, And Lakshma G, burnt with heart-felt pain, True to the right, with steadfast will, His duteous speech he spoke again: “Brother, I know thy loving mind, Thy valour and thy truth I know, But now to claims of duty blind Thou and my mother swell my woe. The fruits of deeds in human life Make love, gain, duty, manifest, Dear when they meet as some fond wife With her sweet babes upon her breast. But man to duty first should turn Whene'er the three are not combined: For those who heed but gain we spurn, And those to pleasure all resigned. Shall then the virtuous disobey Hosts of an aged king and sire, Though feverous joy that father sway, Or senseless love or causeless ire? I have no power, commanded thus, To slight his promise and decree: The honoured sire of both of us, My mother's lord and life is he. Shall she, while yet the holy king Is living, on the right intent,— Shall she, like some poor widowed thing, Go forth with me to banishment?
- **Translation**: 

---

### Verse 6 (Ramayana 0.431)
- **Original**: Canto XXII. Lakshman Calmed. 413 Now, mother, speed thy parting son, And let thy blessing soothe my pain, [120] That I may turn, mine exile done, Like King Yayáti, home again. Fair glory and the fruit she gives, For lust of sway I ne'er will slight: What, for the span a mortal lives. Were rule of faith without the right?” He soothed her thus, firm to the last His counsel to his brother told: Then round the queen in reverence passed, And held her in his loving hold. Canto XXII. Lakshman Calmed. So Ráma kept unshaken still His noble heart with iron will. To his dear brother next he turned, Whose glaring eyes with fury burned, Indignant, panting like a snake, And thus again his counsel spake: “Thine anger and thy grief restrain, And firm in duty's path remain. Dear brother, lay thy scorn aside, And be the right thy joy and pride. Thy ready zeal and thoughtful care To aid what rites should grace the heir,— These 'tis another's now to ask; Come, gird thee for thy noble task, That Bharat's throning rites may he Graced with the things prepared for me.
- **Translation**: 

---

### Verse 7 (Ramayana 0.432)
- **Original**: 414 The Ramayana And with thy gentle care provide That her fond heart, now sorely tried With fear and longing for my sake, With doubt and dread may never ache. To know that thoughts of coming ill One hour that tender bosom fill With agony and dark despair Is grief too great for me to bear. I cannot, brother, call to mind One wilful fault or undesigned, When I have pained in anything My mothers or my sire the king. The right my father keeps in view, In promise, word, and action true; Let him then all his fear dismiss, Nor dread the loss of future bliss. He fears his truth herein will fail: Hence bitter thoughts his heart assail. He trembles lest the rites proceed, And at his pangs my heart should bleed. So now this earnest wish is mine, The consecration to resign, And from this city turn away To the wild wood with no delay. My banishment to-day will free Kaikeyí from her cares, that she, At last contented and elate, May Bharat's throning celebrate. Then will the lady's trouble cease, Then will her heart have joy and peace, When wandering in the wood I wear Deerskin, and bark, and matted hair. Nor shall by me his heart be grieved Whose choice approved, whose mind conceived
- **Translation**: 

---

### Verse 8 (Ramayana 0.433)
- **Original**: Canto XXII. Lakshman Calmed. 415 This counsel which I follow. No, Forth to the forest will I go. 'Tis Fate, Sumitrás son, confess, That sends me to the wilderness. 'Tis Fate alone that gives away To other hands the royal sway. How could Kaikeyí's purpose bring On me this pain and suffering, Were not her change of heart decreed By Fate whose will commands the deed? I know my filial love has been The same throughout for every queen, And with the same affection she Has treated both her son and me. Her shameful words of cruel spite To stay the consecrating rite, And drive me banished from the throne,— These I ascribe to Fate alone, How could she, born of royal race, Whom nature decks with fairest grace, Speak like a dame of low degree Before the king to torture me? But Fate, which none may comprehend, To which all life must bow and bend, In her and me its power has shown, And all my hopes are overthrown. What man, Sumitrá's darling, may Contend with Fate's resistless sway, Whose all-commanding power we find Our former deeds alone can bind? Our life and death, our joy and pain, Anger and fear, and loss and gain, Each thing that is, in every state, All is the work of none but Fate.
- **Translation**: 

---

### Verse 9 (Ramayana 0.434)
- **Original**: 416 The Ramayana E'en saints, inspired with rigid zeal, When once the stroke of Fate they feel, In sternest vows no more engage, And fall enslaved by love and rage. So now the sudden stroke whose weight Descends unlooked for, comes of Fate, And with unpitying might destroys The promise of commencing joys. Weigh this true counsel in thy soul: With thy firm heart thy heart control; Then, brother, thou wilt cease to grieve For hindered rites which now I leave. So cast thy needless grief away, And strictly my commands obey. Those preparations check with speed, Nor let my throning rites proceed. Those urns that stand prepared to shed King-making drops upon my head, Shall, with their pure lustrations now Inaugurate my hermit's vow.[121] Yet what have I to do with things That touch the state and pomp of kings? These hands of mine shall water take To sanctify the vow I make. Now Lakshma G, let thy heart no more My fortune changed and lost deplore. A forest life more joys may bring Than those that wait upon a king, Now though her arts successful mar My consecrating rite, Let not the youngest queen too far Thy jealous fear excite. Nor let one thought suggesting ill Upon our father fall,
- **Translation**: 

---

### Verse 10 (Ramayana 0.435)
- **Original**: Canto XXIII. Lakshman's Anger. 417 But let thy heart remember still That Fate is lord of all.” Canto XXIII. Lakshman's Anger. Thus Ráma to his brother said; And Lakshma G bent his drooping head. In turns by grief and pride impelled, A middle course of thought he held, Then in a frown of anger, bent His brows that chief most excellent, And like a serpent in his hole, Breathed fierce and fast in wrath of soul. His threatening brows so darkly frowned, His eyes so fiercely glanced around, They made his glare, which none might brook, Like some infuriate lion's look. Like some wild elephant, full oft He raised and shook his hand291 aloft. Now turned his neck to left and right Now bent, now raised its stately height. Now in his rage that sword he felt Which mangling wounds to foemen dealt, With sidelong glance his brother eyed, And thus in burning words replied: “Thy rash resolve, thy eager haste, Thy mighty fear, are all misplaced: No room is here for duty's claim, 291 The Sanskrit wordhastasignifies bothhand, and the trunk of“The beast that bears between his eyes a serpent for a head.”
- **Translation**: 

---

### Verse 11 (Ramayana 0.436)
- **Original**: 418 The Ramayana No cause to dread the people's blame. Can one as brave as thou consent To use a coward's argument? The glory of the Warrior race With craven speech his lips debase? Can one like thee so falsely speak, Exalting Fate, confessed so weak? Canst thou, undoubting still restrain? Suspicions of those sinful twain? Canst thou, most duteous, fail to know Their hearts are set on duty's show? They with deceit have set their trains, And now the fruit rewards their pains. Had they not long ago agreed, O Ráma, on this treacherous deed, That promised boon, so long retained, He erst had given and she had gained. I cannot, O my brother, bear To see another throned as heir With rites which all our people hate: Then, O, this passion tolerate. This vaunted duty which can guide Thy steps from wisdom's path aside, And change the counsel of thy breast, O lofty-hearted, I detest. Wilt thou, when power and might are thine, Submit to this abhorred design? Thy father's impious hest fulfil, That vassal of Kaikeyí's will? But if thou still wilt shut thine eyes, Nor see the guile herein that lies, My soul is sad, I deeply mourn, And duty seems a thing to scorn. Canst thou one moment think to please
- **Translation**: 

---

### Verse 12 (Ramayana 0.437)
- **Original**: Canto XXIII. Lakshman's Anger. 419 This pair who live for love and ease, And 'gainst thy peace, as foes, allied, With tenderest names their hatred hide? Now if thy judgment still refers To Fate this plot of his and hers, My mind herein can ne'er agree: And O, in this be ruled by me. Weak, void of manly pride are they Who bend to Fate's imputed sway: The choicest souls, the nobly great Disdain to bow their heads to Fate. And he who dares his Fate control With vigorous act and manly soul, Though threatening Fate his hopes assail, Unmoved through all need never quail. This day mankind shall learn aright The power of Fate and human might, So shall the gulf that lies between A man and Fate be clearly seen. The might of Fate subdued by me This hour the citizens shall see, Who saw its intervention stay Thy consecrating rites to-day. My power shall turn this Fate aside, That threatens, as, with furious stride, An elephant who scorns to feel, In rage unchecked, the driver's steel. Not the great Lords whose sleepless might Protects the worlds, shall stay the rite Though earth, hell, heaven combine their powers: And shall we fear this sire of ours? Then if their minds are idly bent To doom thee, King, to banishment, Through twice seven years of exile they [122]
- **Translation**: 

---

### Verse 13 (Ramayana 0.438)
- **Original**: 420 The Ramayana Shall in the lonely forest stay. I will consume the hopes that fire The queen Kaikeyí and our sire, That to her son this check will bring Advantage, making Bharat king. The power of Fate will ne'er withstand The might that arms my vigorous hand; If danger and distress assail, My fearless strength will still prevail. A thousand circling years shall flee: The forest then thy home shall be, And thy good sons, succeeding, hold The empire which their sire controlled. The royal saints, of old who reigned, For aged kings this rest ordained: These to their sons their realm commit That they, like sires, may cherish it. O pious soul, if thou decline The empire which is justly thine, Lest, while the king distracted lies, Disorder in the state should rise, I,— or no mansion may I find In worlds to hero souls assigned,— The guardian of thy realm will be, As the sea-bank protects the sea. Then cast thine idle fears aside: With prosperous rites be sanctified. The lords of earth may strive in vain: My power shall all their force restrain. My pair of arms, my warrior's bow Are not for pride or empty show: For no support these shafts were made; And binding up ill suits my blade: To pierce the foe with deadly breach—
- **Translation**: 

---

### Verse 14 (Ramayana 0.439)
- **Original**: Canto XXIII. Lakshman's Anger. 421 This is the work of all and each. But small, methinks the love I show For him I count my mortal foe. Soon as my trenchant steel is bare, Flashing its lightning through the air, I heed no foe, nor stand aghast Though Indra's self the levin cast. Then shall the ways be hard to pass, Where chariots lie in ruinous mass; When elephant and man and steed Crushed in the murderous onslaught bleed, And legs and heads fall, heap on heap, Beneath my sword's tremendous sweep. Struck by my keen brand's trenchant blade, Thine enemies shall fall dismayed, Like towering mountains rent in twain, Or lightning clouds that burst in rain. When armed with brace and glove I stand, And take my trusty bow in hand, Who then shall vaunt his might? who dare Count him a man to meet me there? Then will I loose my shafts, and strike Man, elephant, and steed alike: At one shall many an arrow fly, And many a foe with one shall die. This day the world my power shall see, That none in arms can rival me: My strength the monarch shall abase, And set thee, lord, in lordliest place. These arms which breathe the sandal's scent, Which golden bracelets ornament, These hands which precious gifts bestow, Which guard the friend and smite the foe, A nobler service shall assay,
- **Translation**: 

---

### Verse 15 (Ramayana 0.440)
- **Original**: 422 The Ramayana And fight in Ráma's cause to-day, The robbers of thy rights to stay. Speak, brother, tell thy foeman's name Whom I, in conquering strife, May strip of followers and fame, Of fortune, or of life. Say, how may all this sea-girt land Be brought to own thy sway: Thy faithful servant here I stand To listen and obey.” Then strove the bride of Raghu's race Sad LakshmaG's heart to cheer, While slowly down the hero's face, Unchecked, there rolled a tear. “The orders of my sire,” he cried, “My will shall ne'er oppose: I follow still, whate'er betide, The path which duty shows.” Canto XXIV. Kausalyá Calmed. But when Kau[alyásaw that he Resolved to keep his sire's decree, While tears and sobs her utterance broke, Her very righteous speech she spoke: “Can he, a stranger yet to pain, Whose pleasant words all hearts enchain, Son of the king and me the queen, Live on the grain his hands may glean; Can he, whose slaves and menials eat The finest cakes of sifted wheat—
- **Translation**: 

---

### Verse 16 (Ramayana 0.441)
- **Original**: Canto XXIV. Kausalyá Calmed. 423 Can Ráma in the forest live On roots and fruit which woodlands give; Who will believe, who will not fear When the sad story smites his ear, That one so dear, so noble held, Is by the king his sire expelled? Now surely none may Fate resist, Which orders all as it may list, If, Ráma, in thy strength and grace, The woods become thy dwelling-place. A childless mother long I grieved, And many a sigh for offspring heaved, With wistful longing weak and worn Till thou at last, my son, wast born. Fanned by the storm of that desire Deep in my soul I felt the fire, Whose offerings flowed from weeping eyes, With fuel fed of groans and sighs, [123] While round the flame the smoke grew hot Of tears because thou camest not. Now reft of thee, too fiery fierce The flame of woe my heart will pierce, As, when the days of spring return, The sun's hot beams the forest burn. The mother cow still follows near The wanderings of her youngling dear. So close to thine my feet shall be, Where'er thou goest following thee.” Ráma, the noblest lord of men, Heard his fond mother's speech, and then In soothing words like these replied To the sad queen who wept and sighed: “Nay, by Kaikeyí's art beguiled,
- **Translation**: 

---

### Verse 17 (Ramayana 0.442)
- **Original**: 424 The Ramayana When I am banished to the wild, If thou, my mother, also fly, The aged king will surely die. When wedded dames their lords forsake, Long for the crime their souls shall ache. Thou must not e'en in thought within Thy bosom frame so dire a sin. Long as Kakutstha's son, who reigns Lord of the earth, in life remains, Thou must with love his will obey: This duty claims, supreme for aye. Yes, mother, thou and I must be Submissive to my sire's decree, King, husband, sire is he confessed, The lord of all, the worthiest. I in the wilds my days will spend Till twice seven years have reached an end, Then with great joy will come again, And faithful to thy hests remain.” Kau [alyá by her son addressed, With love and passion sore distressed, Afflicted, with her eyes bedewed, To Ráma thus her speech renewed: “Nay, Ráma, but my heart will break If with these queens my home I make. Lead me too with thee; let me go And wander like a woodland roe.” Then, while no tear the hero shed, Thus to the weeping queen he said: “Mother, while lives the husband, he Is woman's lord and deity. O dearest lady, thou and I Our lord and king must ne'er deny;
- **Translation**: 

---

### Verse 18 (Ramayana 0.443)
- **Original**: Canto XXIV. Kausalyá Calmed. 425 The lord of earth himself have we Our guardian wise and friend to be. And Bharat, true to duty's call, Whose sweet words take the hearts of all, Will serve thee well, and ne'er forget The virtuous path before him set. Be this, I pray, thine earnest care, That the old king my father ne'er, When I have parted hence, may know, Grieved for his son, a pang of woe. Let not this grief his soul distress, To kill him with the bitterness. With duteous care, in every thing, Love, comfort, cheer the aged king. Though, best of womankind, a spouse Keeps firmly all her fasts and vows, Nor yet her husband's will obeys, She treads in sin's forbidden ways. She to her husband's will who bends, Goes to high bliss that never ends, Yea, though the Gods have found in her No reverential worshipper. Bent on his weal, a woman still Must seek to do her husband's will: For Scripture, custom, law uphold This duty Heaven revealed of old. Honour true Bráhmans for my sake, And constant offerings duly make, With fire-oblations and with flowers, To all the host of heavenly powers. Look to the coming time, and yearn For the glad hour of my return. And still thy duteous course pursue, Abstemious, humble, kind, and true.
- **Translation**: 

---

### Verse 19 (Ramayana 0.444)
- **Original**: 426 The Ramayana The highest bliss shalt thou obtain When I from exile come again, If, best of those who keep the right, The king my sire still see the light.” The queen, by Ráma thus addressed, Still with a mother's grief oppressed, While her long eyes with tears were dim, Began once more and answered him: “Not by my pleading may be stayed The firm resolve thy soul has made. My hero, thou wilt go; and none The stern commands of Fate may shun. Go forth, dear child whom naught can bend, And may all bliss thy steps attend. Thou wilt return, and that dear day Will chase mine every grief away. Thou wilt return, thy duty done, Thy vows discharged, high glory won; From filial debt wilt thou be free, And sweetest joy will come on me. My son, the will of mighty Fate At every time must dominate, If now it drives thee hence to stray Heedless of me who bid thee stay. Go, strong of arm, go forth, my boy, Go forth, again to come with joy, And thine expectant mother cheer With those sweet tones she loves to hear. O that the blessed hour were nigh When thou shalt glad this anxious eye, With matted hair and hermit dress returning from the wilderness.” Kau [alyá's conscious soul approved,
- **Translation**: 

---

### Verse 20 (Ramayana 0.445)
- **Original**: Canto XXV. Kausalyá's Blessing. 427 As her proud glance she bent On Ráma constant and unmoved, Resolved on banishment. Such words, with happy omens fraught To her dear son she said, Invoking with each eager thought A blessing on his head. [124] Canto XXV. Kausalyá's Blessing. Her grief and woe she cast aside, Her lips with water purified, And thus her benison began That mother of the noblest man: “If thou wilt hear no words of mine, Go forth, thou pride of Raghu's line. Go, darling, and return with speed, Walking where noble spirits lead. May virtue on thy steps attend, And be her faithful lover's friend. May Those to whom thy vows are paid In temple and in holy shade, With all the mighty saints combine To keep that precious life of thine. The arms wise Vi[vámitra292 gave Thy virtuous soul from danger save. Long be thy life: thy sure defence Shall be thy truthful innocence, 292 See P. 41.
- **Translation**: 

---

