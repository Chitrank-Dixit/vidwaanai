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

