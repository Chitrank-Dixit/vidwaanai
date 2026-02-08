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

### Verse 1 (Ramayan 0.821)
- **Original**: Canto CXIX. The Forest. 803 The prince the offered gift declined Till he should learn his father's mind; So horsemen swift Ayodhyá sought And back her aged monarch brought. Me then my sire to Ráma gave, Self-ruled, the bravest of the brave. And Urmilá, the next to me, Graced with all gifts, most fair to see, My sire with Raghu's house allied, And gave her to be LakshmaG's bride. Thus from the princes of the land Lord Ráma won my maiden hand, And him exalted high above Heroic chiefs I truly love.” Canto CXIX. The Forest. When Anasúyá, virtuous-souled, Had heard the tale by Sítá told, She kissed the lady's brow and laced Her loving arms around her waist. “With sweet-toned words distinct and clear Thy pleasant tale has charmed mine ear, How the great king thy father held That Maiden's Choice unparalleled. But now the sun has sunk from sight, And left the world to holy Night. Hark! how the leafy thickets sound With gathering birds that twitter round: They sought their food by day, and all Flock homeward when the shadows fall.
- **Translation**: 

---

### Verse 2 (Ramayan 0.822)
- **Original**: 804 The Ramayana See, hither comes the hermit band, Each with his pitcher in his hand: Fresh from the bath, their locks are wet, Their coats of bark are dripping yet. Here saints their fires of worship tend, And curling wreaths of smoke ascend: Borne on the flames they mount above, Dark as the brown wings of the dove. The distant trees, though well-nigh bare, Gloom thickened by the evening air, And in the faint uncertain light Shut the horizon from our sight. The beasts that prowl in darkness rove On every side about the grove, And the tame deer, at ease reclined Their shelter near the altars find. The night o'er all the sky is spread, With lunar stars engarlanded, And risen in his robes of light The moon is beautifully bright. Now to thy lord I bid thee go: Thy pleasant tale has charmed me so: One thing alone I needs must pray, Before me first thyself array: Here in thy heavenly raiment shine, And glad, dear love, these eyes of mine.”[229] Then like a heavenly Goddess shone Fair Sítá with that raiment on. She bowed her to the matron's feet, Then turned away her lord to meet. The hero prince with joy surveyed His Sítá in her robes arrayed, As glorious to his arms she came With love-gifts of the saintly dame.
- **Translation**: 

---

### Verse 3 (Ramayan 0.823)
- **Original**: Canto CXIX. The Forest. 805 She told him how the saint to show Her fond affection would bestow That garland of celestial twine, Those ornaments and robes divine. Then Ráma's heart, nor LakshmaG's less, Was filled with pride and happiness, For honours high had Sítá gained, Which mortal dames have scarce obtained. There honoured by each pious sage Who dwelt within the hermitage, Beside his darling well content That sacred night the hero spent. The princes, when the night had fled, Farewell to all the hermits said, Who gazed upon the distant shade, Their lustral rites and offerings paid. The saints who made their dwelling there In words like these addressed the pair: “O Princes, monsters fierce and fell Around that distant forest dwell: On blood from human veins they feed, And various forms assume at need, With savage beasts of fearful power That human flesh and blood devour. Our holy saints they rend and tear When met alone or unaware, And eat them in their cruel joy: These chase, O Ráma, or destroy. By this one path our hermits go To fetch the fruits that yonder grow: By this, O Prince, thy feet should stray Through pathless forests far away.”
- **Translation**: 

---

### Verse 4 (Ramayan 0.824)
- **Original**: 806 The Ramayana Thus by the reverent saints addressed, And by their prayers auspicious blessed, He left the holy crowd: His wife and brother by his side, Within the mighty wood he hied. So sinks the Day-God in his pride Beneath a bank of cloud.
- **Translation**: 

---

### Verse 5 (Ramayan 0.825)
- **Original**: BOOK III. Canto I. The Hermitage. When Ráma, valiant hero, stood In the vast shade of DaG ak wood, His eyes on every side he bent And saw a hermit settlement, Where coats of bark were hung around, And holy grass bestrewed the ground. Bright with Bráhmanic lustre glowed That circle where the saints abode: Like the hot sun in heaven it shone, Too dazzling to be looked upon. Wild creatures found a refuge where The court, well-swept, was bright and fair, And countless birds and roedeer made Their dwelling in the friendly shade. Beneath the boughs of well-loved trees Oft danced the gay Apsarases.401 Around was many an ample shed Wherein the holy fire was fed; With sacred grass and skins of deer, Ladles and sacrificial gear, And roots and fruit, and wood to burn, 401 Heavenly nymphs.
- **Translation**: 

---

### Verse 6 (Ramayan 0.826)
- **Original**: 808 The Ramayana And many a brimming water-urn. Tall trees their hallowed branches spread, Laden with pleasant fruit, o'erhead; And gifts which holy laws require,402 And solemn offerings burnt with fire,403 And Veda chants on every side That home of hermits sanctified. There many a flower its odour shed, And lotus blooms the lake o'erspred. There, clad in coats of bark and hide,— Their food by roots and fruit supplied,— Dwelt many an old and reverend sire Bright as the sun or Lord of Fire, All with each worldly sense subdued, A pure and saintly multitude. The Veda chants, the saints who trod The sacred ground and mused on God, Made that delightful grove appear Like Brahmá's own most glorious sphere. As Raghu's splendid son surveyed That hermit home and tranquil shade, He loosed his mighty bow-string, then Drew nearer to the holy men.[230] With keen celestial sight endued Those mighty saints the chieftain viewed, With joy to meet the prince they came, And gentle Sítá dear to fame. They looked on virtuous Ráma, fair As Soma 404 in the evening air, And Lakshma G by his brother's side, 402 The ballor present of food to all created beings. 403 The clarified butter &c. cast into the sacred fire. 404 The Moon-God: “he is,” says the commentator,“the special deity of Bráhmans.”
- **Translation**: 

---

### Verse 7 (Ramayan 0.827)
- **Original**: Canto I. The Hermitage. 809 And Sítá long in duty tried, And with glad blessings every sage Received them in the hermitage. Then Ráma's form and stature tall Entranced the wondering eyes of all,— His youthful grace, his strength of limb, And garb that nobly sat on him. To LakshmaG too their looks they raised, And upon Sítá's beauty gazed With eyes that closed not lest their sight Should miss the vision of delight. Then the pure hermits of the wood, Rejoicing in all creatures' good, Their guest, the glorious Ráma, led Within a cot with leaves o'erhead. With highest honour all the best Of radiant saints received their guest, With kind observance, as is meet, And gave him water for his feet. To highest pitch of rapture wrought Their stores of roots and fruit they brought. They poured their blessings on his head, And “All we have is thine,” they said. Then, reverent hand to hand applied,405 Each duty-loving hermit cried: “The king is our protector, bright In fame, maintainer of the right. He bears the awful sword, and hence Deserves an elder's reverence. One fourth of Indra's essence, he Preserves his realm from danger free, 405 “Because he was an incarnation of the deity,” says the commentator,“oth- erwise such honour paid by men of the sacerdotal caste to one of the military would be improper.”
- **Translation**: 

---

### Verse 8 (Ramayan 0.828)
- **Original**: 810 The Ramayana Hence honoured by the world of right The king enjoys each choice delight. Thou shouldst to us protection give, For in thy realm, dear lord, we live: Whether in town or wood thou be, Thou art our king, thy people we. Our wordly aims are laid aside, Our hearts are tamed and purified. To thee our guardian, we who earn Our only wealth by penance turn.” Then the pure dwellers in the shade To Raghu's son due honour paid, And Lakshma G, bringing store of roots, And many a flower, and woodland fruits. And others strove the prince to please With all attentive courtesies. Canto II. Virádha. Thus entertained he passed the night, Then, with the morning's early light, To all the hermits bade adieu And sought his onward way anew. He pierced the mighty forest where Roamed many a deer and pard and bear: Its ruined pools he scarce could see. For creeper rent and prostrate tree, Where shrill cicada's cries were heard, And plaintive notes of many a bird. Deep in the thickets of the wood
- **Translation**: 

---

### Verse 9 (Ramayan 0.829)
- **Original**: Canto II. Virádha. 811 With LakshmaG and his spouse he stood, There in the horrid shade he saw A giant passing nature's law: Vast as some mountain-peak in size, With mighty voice and sunken eyes, Huge, hideous, tall, with monstrous face, Most ghastly of his giant race. A tiger's hide the Rákshas wore Still reeking with the fat and gore: Huge-faced, like Him who rules the dead, All living things he struck with dread. Three lions, tigers four, ten deer He carried on his iron spear, Two wolves, an elephant's head beside With mighty tusks which blood-drops dyed. When on the three his fierce eye fell, He charged them with a roar and yell As furious as the grisly King When stricken worlds are perishing. Then with a mighty roar that shook The earth beneath their feet, he took The trembling Sítá to his side. Withdrew a little space, and cried: “Ha, short lived wretches, ye who dare, In hermit dress with matted hair, Armed each with arrows, sword, and bow, Through DaG ak's pathless wood to go: How with one dame, I bid you tell, Can you among ascetics dwell? Who are ye, sinners, who despise The right, in holy men's disguise? The great Virádha, day by day Through this deep-tangled wood I stray, And ever, armed with trusty steel,
- **Translation**: 

---

### Verse 10 (Ramayan 0.830)
- **Original**: 812 The Ramayana I seize a saint to make my meal. This woman young and fair of frame Shall be the conquering giant's dame: Your blood, ye things of evil life, My lips shall quaff in battle strife.” He spoke: and Janak's hapless child, Scared by his speech so fierce and wild,[231] Trembled for terror, as a frail Young plantain shivers in the gale. When Ráma saw Virádha clasp Fair Sítá in his mighty grasp, Thus with pale lips that terror dried The hero to his brother cried: “O see Virádha's arm enfold My darling in its cursed hold,— The child of Janak best of kings, My spouse whose soul to virtue clings, Sweet princess, with pure glory bright, Nursed in the lap of soft delight. Now falls the blow Kaikeyí meant, Successful in her dark intent: This day her cruel soul will be Triumphant over thee and me. Though Bharat on the throne is set, Her greedy eyes look farther yet: Me from my home she dared expel, Me whom all creatures loved so well. This fatal day at length, I ween, Brings triumph to the younger queen. I see with bitterest grief and shame Another touch the Maithil dame. Not loss of sire and royal power So grieves me as this mournful hour.”
- **Translation**: 

---

### Verse 11 (Ramayan 0.831)
- **Original**: Canto III. Virádha Attacked. 813 Thus in his anguish cried the chief: Then drowned in tears, o'erwhelmed by grief, Thus LakshmaG in his anger spake, Quick panting like a spell-bound snake: “Canst thou, my brother, Indra's peer, When I thy minister am near, Thus grieve like some forsaken thing, Thou, every creature's lord and king? My vengeful shaft the fiend shall slay, And earth shall drink his blood to-day. The fury which my soul at first Upon usurping Bharat nursed, On this Virádha will I wreak As Indra splits the mountain peak. Winged by this arm's impetuous might My shaft with deadly force The monster in the chest shall smite, And fell his shattered corse.” Canto III. Virádha Attacked. Virádha with a fearful shout That echoed through the wood, cried out: “What men are ye, I bid you say, And whither would ye bend your way?”
- **Translation**: 

---

### Verse 12 (Ramayan 0.832)
- **Original**: 814 The Ramayana To him whose mouth shot fiery flame The hero told his race and name: “Two Warriors, nobly bred, are we, And through this wood we wander free. But who art thou, how born and styled, Who roamest here in DaG ak's wild?” To Ráma, bravest of the brave, His answer thus Virádha gave: “Hear, Raghu's son, and mark me well, And I my name and race will tell. Of Zatahradá born, I spring From Java as my sire, O King: Me, of this lofty lineage, all Giants on earth Virádha call. The rites austere I long maintained From Brahmá's grace the boon have gained To bear a charmed frame which ne'er Weapon or shaft may pierce or tear. Go as ye came, untouched by fear, And leave with me this woman here: Go, swiftly from my presence fly, Or by this hand ye both shall die.” Then Ráma with his fierce eyes red With fury to the giant said: “Woe to thee, sinner, fond and weak, Who madly thus thy death wilt seek! Stand, for it waits thee in the fray: With life thou ne'er shalt flee away.”
- **Translation**: 

---

### Verse 13 (Ramayan 0.833)
- **Original**: Canto III. Virádha Attacked. 815 He spoke, and raised the cord whereon A pointed arrow flashed and shone, Then, wild with anger, from his bow, He launched the weapon on the foe. Seven times the fatal cord he drew, And forth seven rapid arrows flew, Shafts winged with gold that left the wind And e'en SuparGa's406 self behind. Full on the giant's breast they smote, And purpled like the peacock's throat, Passed through his mighty bulk and came To earth again like flakes of flame. The fiend the Maithil dame unclasped; In his fierce hand his spear he grasped, And wild with rage, pierced through and through, At Ráma and his brother flew. So loud the roar which chilled with fear, So massy was the monster's spear, He seemed, like Indra's flagstaff, dread As the dark God who rules the dead. On huge Virádha fierce as He407 Who smites, and worlds have ceased to be, The princely brothers poured amain Their fiery flood of arrowy rain. Unmoved he stood, and opening wide His dire mouth laughed unterrified, And ever as the monster gaped Those arrows from his jaws escaped. Preserving still his life unharmed, By Brahmá's saving promise charmed, His mighty spear aloft in air He raised, and rushed upon the pair. 406 The king of birds. 407 Kálántakayamopamam , resembling Yáma the destroyer.
- **Translation**: 

---

### Verse 14 (Ramayan 0.834)
- **Original**: 816 The Ramayana From Ráma's bow two arrows flew And cleft that massive spear in two,[232] Dire as the flaming levin sent From out the cloudy firmament. Cut by the shafts he guided well To earth the giant's weapon fell: As when from Meru's summit, riven By fiery bolts, a rock is driven. Then swift his sword each warrior drew, Like a dread serpent black of hue, And gathering fury for the blow Rushed fiercely on the giant foe. Around each prince an arm he cast, And held the dauntless heroes fast: Then, though his gashes gaped and bled, Bearing the twain he turned and fled. Then Ráma saw the giant's plan, And to his brother thus began: “O Lakshma G, let Virádha still Hurry us onward as he will, For look, Sumitrá's son, he goes Along the path we freely chose.” He spoke: the rover of the night Upraised them with terrific might, Till, to his lofty shoulders swung, Like children to his neck they clung. Then sending far his fearful roar, The princes through the wood he bore,— A wood like some vast cloud to view, Where birds of every plumage flew, And mighty trees o'erarching threw Dark shadows on the ground;
- **Translation**: 

---

### Verse 15 (Ramayan 0.835)
- **Original**: Canto IV. Virádha's Death. 817 Where snakes and silvan creatures made Their dwelling, and the jackal strayed Through tangled brakes around. Canto IV. Virádha's Death. But Sítá viewed with wild affright The heroes hurried from her sight. She tossed her shapely arms on high, And shrieked aloud her bitter cry: “Ah, the dread giant bears away The princely Ráma as his prey, Truthful and pure, and good and great, And Lakshma G shares his brother's fate. The brindled tiger and the bear My mangled limbs for food will tear. Take me, O best of giants, me, And leave the sons of Raghu free.”
- **Translation**: 

---

### Verse 16 (Ramayan 0.836)
- **Original**: 818 The Ramayana Then, by avenging fury spurred, Her mournful cry the heroes heard, And hastened, for the lady's sake, The wicked monster's life to take. Then LakshmaG with resistless stroke The foe's left arm that held him broke, And Ráma too, as swift to smite, Smashed with his heavy hand the right. With broken arms and tortured frame To earth the fainting giant came, Like a huge cloud, or mighty rock Rent, sundered by the levin's shock. Then rushed they on, and crushed and beat Their foe with arms and fists and feet, And nerved each mighty limb to pound And bray him on the level ground. Keen arrows and each biting blade Wide rents in breast and side had made; But crushed and torn and mangled, still The monster lived they could not kill. When Ráma saw no arms might slay The fiend who like a mountain lay, The glorious hero, swift to save In danger, thus his counsel gave: “O Prince of men, his charmed life No arms may take in battle strife: Now dig we in this grove a pit His elephantine bulk to fit, And let the hollowed earth enfold The monster of gigantic mould.” This said, the son of Raghu pressed His foot upon the giant's breast. With joy the prostrate monster heard
- **Translation**: 

---

### Verse 17 (Ramayan 0.837)
- **Original**: Canto IV. Virádha's Death. 819 Victorious Ráma's welcome word, And straight Kakutstha's son, the best Of men, in words like these addressed: “I yield, O chieftain, overthrown By might that vies with Indra's own. Till now my folly-blinded eyes Thee, hero, failed to recognize. Happy Kau[alyá! blest to be The mother of a son like thee! I know thee well, O chieftain, now: Ráma, the prince of men, art thou. There stands the high-born Maithil dame, There LakshmaG, lord of mighty fame. My name was Tumburu,408 for song Renowned among the minstrel throng: Cursed by Kuvera's stern decree I wear the hideous shape you see. But when I sued, his grace to crave, The glorious God this answer gave: “When Ráma, Da [aratha's son, Destroys thee and the fight is won, Thy proper shape once more assume, And heaven again shall give thee room.” When thus the angry God replied, No prayers could turn his wrath aside, And thus on me his fury fell For loving Rambhá's409 charms too well. Now through thy favour am I freed From the stern fate the God decreed, And saved, O tamer of the foe, [233] 408 Somewhat inconsistently with this part of the story Tumburu is mentioned in Book II, Canto XII as one of the Gandharvas or heavenly minstrels summoned to perform at Bharadvája's feast. 409 Rambhá appears in Book I Canto LXIV as the temptress of Vi[vámitra.
- **Translation**: 

---

### Verse 18 (Ramayan 0.838)
- **Original**: 820 The Ramayana By thee, to heaven again shall go. A league, O Prince, beyond this spot Stands holyZarabhanga's cot: The very sun is not more bright Than that most glorious anchorite: To him, O Ráma, quickly turn, And blessings from the hermit earn. First under earth my body throw, Then on thy way rejoicing go. Such is the law ordained of old For giants when their days are told: Their bodies laid in earth, they rise To homes eternal in the skies.” Thus, by the rankling dart oppressed, Kakutstha's offspring he addressed: In earth his mighty body lay, His spirit fled to heaven away. Thus spake Virádha ere he died; And Ráma to his brother cried: “Now dig we in this grove a pit His elephantine bulk to fit. And let the hollowed earth enfold This mighty giant fierce and bold.”
- **Translation**: 

---

### Verse 19 (Ramayan 0.839)
- **Original**: Canto IV. Virádha's Death. 821 This said, the valiant hero put Upon the giant's neck his foot. His spade obedient LakshmaG plied, And dug a pit both deep and wide By lofty souled Virádha's side. Then Raghu's son his foot withdrew, And down the mighty form they threw; One awful shout of joy he gave And sank into the open grave. The heroes, to their purpose true, In fight the cruel demon slew, And radiant with delight Deep in the hollowed earth they cast The monster roaring to the last, In their resistless might. Thus when they saw the warrior's steel No life-destroying blow might deal, The pair, for lore renowned, Deep in the pit their hands had made The unresisting giant laid, And killed him neath the ground. Upon himself the monster brought From Ráma's hand the death he sought With strong desire to gain: And thus the rover of the night Told Ráma, as they strove in fight, That swords might rend and arrows smite Upon his breast in vain. Thus Ráma, when his speech he heard, The giant's mighty form interred, Which mortal arms defied. With thundering crash the giant fell, And rock and cave and forest dell With echoing roar replied.
- **Translation**: 

---

### Verse 20 (Ramayan 0.840)
- **Original**: 822 The Ramayana The princes, when their task was done And freedom from the peril won, Rejoiced to see him die. Then in the boundless wood they strayed, Like the great sun and moon displayed Triumphant in the sky.410 Canto V. Sarabhanga. Then Ráma, having slain in fight Virádha of terrific might, With gentle words his spouse consoled, And clasped her in his loving hold. Then to his brother nobly brave The valiant prince his counsel gave: “Wild are these woods around us spread; And hard and rough the ground to tread: We, O my brother, ne'er have viewed So dark and drear a solitude: To Zarabhanga let us haste, Whom wealth of holy works has graced.” 410 The conclusion of this Canto is all a vain repetition: it is manifestly spurious and a very feeble imitation of Válmíki's style. SeeAdditional Notes.
- **Translation**: 

---

