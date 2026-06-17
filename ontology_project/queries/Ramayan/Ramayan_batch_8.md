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

### Verse 1 (Ramayan 0.141)
- **Original**: Canto XXVI. The Forest Of Tádaká. 123 Sacred to Káma, and remain One night in comfort there.” With penance' far-discerning eye The saintly men beheld Their coming, and with transport high Each holy bosom swelled. To Ku[ik's son the gift they gave That honoured guest should greet, Water they brought his feet to lave, And showed him honor meet. Ráma and LakshmaG next obtained In due degree their share. Then with sweet talk the guests remained, And charmed each listener there. The evening prayers were duly said With voices calm and low: Then on the ground each laid his head And slept till morning's glow. Canto XXVI. The Forest Of Tádaká. When the fair light of morning rose The princely tamers of their foes Followed, his morning worship o'er, The hermit to the river's shore. The high-souled men with thoughtful care A pretty barge had stationed there. All cried,“O lord, this barge ascend, And with thy princely followers bend To yonder side thy prosperous way With naught to check thee or delay.”
- **Translation**: 

---

### Verse 2 (Ramayan 0.142)
- **Original**: 124 The Ramayana Nor did the saint their rede reject: He bade farewell with due respect, And crossed, attended by the twain, That river rushing to the main. When now the bark was half way o'er, Ráma and LakshmaG heard the roar, That louder grew and louder yet, Of waves by dashing waters met. Then Ráma asked the mighty seer: “What is the tumult that I hear Of waters cleft in mid career?” Soon as the speech of Ráma, stirred By deep desire to know, he heard, The pious saint began to tell What paused the waters' roar and swell: “On high Kailása's distant hill There lies a noble lake Whose waters, born from Brahmá's will, The name of Mánas158 take. Thence, hallowing where'er they flow, The streams of Sarjú fall, And wandering through the plains below Embrace Ayodhyá's wall. Still, still preserved in Sarjú's name Sarovar's159 fame we trace. The flood of Brahma whence she came 158 “A celebrated lake regarded in India as sacred. It lies in the lofty region between the northern highlands of the Himálayas and mount Kailása, the region of the sacred lakes. The poem, following the popular Indian belief, makes the river Sarayú (now Sarjú) flow from the Mánasa lake; the sources of the river are a little to the south about a day's journey from the lake. See Lassen, Indische Alterthumshunde, page 34.” G ORRESIO {FNS . Manas means mind; mánasa, mental, mind-born. 159 Sarovarmeans best of lakes. This is another of the poet's fanciful etymolo- gies.
- **Translation**: 

---

### Verse 3 (Ramayan 0.143)
- **Original**: Canto XXVI. The Forest Of Tádaká. 125 To run her holy race. To meet great Gangá here she hies With tributary wave: Hence the loud roar ye hear arise, Of floods that swell and rave. Here, pride of Raghu's line, do thou In humble adoration bow.” He spoke. The princes both obeyed, And reverence to each river paid.160 They reached the southern shore at last, And gaily on their journey passed. A little space beyond there stood A gloomy awe-inspiring wood. The monarch's noble son began To question thus the holy man: “Whose gloomy forest meets mine eye Like some vast cloud that fills the sky? Pathless and dark it seems to be, Where birds in thousands wander free; Where shrill cicadas' cries resound, [039] And fowl of dismal note abound. Lion, rhinoceros, and bear, Boar, tiger, elephant, are there, There shrubs and thorns run wild: Dháo, Sál, Bignonia, Bel,161 are found, And every tree that grows on ground. How is the forest styled?” 160 The confluence of two or more rivers is often a venerated and holy place. The most famous is Prayág or Allahabad, where the Sarasvatí by an underground course is believed to join the Jumna and the Ganges. 161 The botanical names of the trees mentioned in the text are Grislea Tormen- tosa, Shorea Robusta, Echites Antidysenterica, Bignonia Suaveolens,Œ gle Marmelos, and Diospyrus Glutinosa. I have omitted theKutaja(Echites) and theTiG uka (Diospyrus).
- **Translation**: 

---

### Verse 4 (Ramayan 0.144)
- **Original**: 126 The Ramayana The glorious saint this answer made: “Dear child of Raghu, hear Who dwells within the horrid shade That looks so dark and drear. Where now is wood, long ere this day Two broad and fertile lands, Malaja and Karúsha lay, Adorned by heavenly hands. Here, mourning friendship's broken ties, Lord Indra of the thousand eyes Hungered and sorrowed many a day, His brightness soiled with mud and clay, When in a storm of passion he Had slain his dear friend Namuchi. Then came the Gods and saints who bore Their golden pitchers brimming o'er With holy streams that banish stain, And bathed Lord Indra pure again. When in this land the God was freed From spot and stain of impious deed For that his own dear friend he slew, High transport thrilled his bosom through. Then in his joy the lands he blessed, And gave a boon they long possessed: “Because these fertile lands retain The washings of the blot and stain,” 'Twas thus Lord Indra sware, “Malaja and Karúsha's name Shall celebrate with deathless fame My malady and care.”162 162 Here we meet with a fresh myth to account for the name of these regions. Malaja is probably a non-Aryan word signifying a hilly country: taken as a Sanskrit compound it meanssprung from defilement. The word Karúsha appears to have a somewhat similar meaning.
- **Translation**: 

---

### Verse 5 (Ramayan 0.145)
- **Original**: Canto XXVI. The Forest Of Tádaká. 127 “So be it,” all the Immortals cried, When Indra's speech they heard, And with acclaim they ratified The names his lips conferred. Long time, O victor of thy foes, These happy lands had sweet repose, And higher still in fortune rose. At length a spirit, loving ill, Tá aká, wearing shapes at will, Whose mighty strength, exceeding vast, A thousand elephants, surpassed, Was to fierce Sunda, lord and head Of all the demon armies, wed. From her, Lord Indra's peer in might Giant Márícha sprang to light: And she, a constant plague and pest, These two fair realms has long distressed. Now dwelling in her dark abode A league away she bars the road: And we, O Ráma, hence must go Where lies the forest of the foe. Now on thine own right arm rely, And my command obey: Smite the foul monster that she die, And take the plague away. To reach this country none may dare Fallen from its old estate, Which she, whose fury naught can bear, Has left so desolate. And now my truthful tale is told How with accursed sway The spirit plagued this wood of old, And ceases not to-day.”
- **Translation**: 

---

### Verse 6 (Ramayan 0.146)
- **Original**: 128 The Ramayana Canto XXVII. The Birth Of Tádaká. When thus the sage without a peer Had closed that story strange to hear, Ráma again the saint addressed To set one lingering doubt at rest: “O holy man, 'tis said by all That spirits' strength is weak and small: How can she match, of power so slight, A thousand elephants in might?” And Vi[vámitra thus replied To Raghu's son the glorified: “Listen, and I will tell thee how She gained the strength that arms her now. A mighty spirit lived of yore; Suketu was the name he bore. Childless was he, and free from crime In rites austere he passed his time. The mighty Sire was pleased to show His favour, and a child bestow. Tá aká named, most fair to see, A pearl among the maids was she, And matched, for such was Brahmá's dower, A thousand elephants in power. Nor would the Eternal Sire, although The spirit longed, a son bestow That maid in beauty's youthful pride Was given to Sunda for a bride. Her son, Márícha was his name, A giant, through a curse, became. She, widowed, dared with him molest[040]
- **Translation**: 

---

### Verse 7 (Ramayan 0.147)
- **Original**: Canto XXVII. The Birth Of Tádaká. 129 Agastya,163 of all saints the best. Inflamed with hunger's wildest rage, Roaring she rushed upon the sage. When the great hermit saw her near, On speeding in her fierce career, He thus pronounced Márícha's doom: “A giant's form and shape assume.” And then, by mighty anger swayed, On Tá aká this curse he laid: “Thy present form and semblance quit, And wear a shape thy mood to fit; Changed form and feature by my ban, A fearful thing that feeds on man.” She, by his awful curse possessed, And mad with rage that fills her breast, Has on this land her fury dealt Where once the saint Agastya dwelt. Go, Ráma, smite this monster dead, The wicked plague, of power so dread, And further by this deed of thine The good of Bráhmans and of kine. Thy hand alone can overthrow, In all the worlds, this impious foe. Nor let compassion lead thy mind To shrink from blood of womankind; A monarch's son must ever count The people's welfare paramount, And whether pain or joy he deal 163 “This is one of those indefinable mythic personages who are found in the ancient traditions of many nations, and in whom cosmogonical or astronomical notions are generally figured. Thus it is related of Agastya that the Vindhyan mountains prostrated themselves before him; and yet the same Agastya is believed to be regent of the star Canopus.” G ORRESIO {FNS . He will appear as the friend and helper of Ráma farther on in the poem.
- **Translation**: 

---

### Verse 8 (Ramayan 0.148)
- **Original**: 130 The Ramayana Dare all things for his subjects' weal; Yea, if the deed bring praise or guilt, If life be saved or blood be spilt: Such, through all time, should be the care Of those a kingdom's weight who bear. Slay, Ráma, slay this impious fiend, For by no law her life is screened. So Manthará, as bards have told, Virochan's child, was slain of old By Indra, when in furious hate She longed the earth to devastate. So Kávya's mother, Bhrigu's wife, Who loved her husband as her life, When Indra's throne she sought to gain, By VishGu's hand of yore was slain. By these and high-souled kings beside, Struck down, have lawless women died.” Canto XXVIII. The Death Of Tádaká. Thus spoke the saint. Each vigorous word The noble monarch's offspring heard, And, reverent hands together laid, His answer to the hermit made: “My sire and mother bade me aye Thy word, O mighty Saint, obey So will I, O most glorious, kill This Tá aká who joys in ill, For such my sire's, and such thy will. To aid with mine avenging hand The Bráhmans, kine, and all the land,
- **Translation**: 

---

### Verse 9 (Ramayan 0.149)
- **Original**: Canto XXVIII. The Death Of Tádaká. 131 Obedient, heart and soul, I stand.” Thus spoke the tamer of the foe, And by the middle grasped his bow. Strongly he drew the sounding string That made the distant welkin ring. Scared by the mighty clang the deer That roamed the forest shook with fear, And Tá aká the echo heard, And rose in haste from slumber stirred. In wild amaze, her soul aflame With fury toward the spot she came. When that foul shape of evil mien And stature vast as e'er was seen The wrathful son of Raghu eyed, He thus unto his brother cried: “Her dreadful shape, O LakshmaG, see, A form to shudder at and flee. The hideous monster's very view Would cleave a timid heart in two. Behold the demon hard to smite, Defended by her magic might. My hand shall stay her course to-day, And shear her nose and ears away. No heart have I her life to take: I spare it for her sex's sake. My will is but, with minished force, To check her in her evil course.” While thus he spoke, by rage impelled Roaring as she came nigh, The fiend her course at Ráma held With huge arms tossed on high. Her, rushing on, the seer assailed With a loud cry of hate;
- **Translation**: 

---

### Verse 10 (Ramayan 0.150)
- **Original**: 132 The Ramayana And thus the sons of Raghu hailed: “Fight, and be fortunate.” Then from the earth a horrid cloud Of dust the demon raised, And for awhile in darkling shroud Wrapt Raghu's sons amazed. Then calling on her magic power The fearful fight to wage, She smote him with a stony shower, Till Ráma burned with rage. Then pouring forth his arrowy rain That stony flood to stay,[041] With winged darts, as she charged amain, He shore her hands away. As Tá aká still thundered near Thus maimed by Ráma's blows, Lakshma G in fury severed sheer The monster's ears and nose. Assuming by her magic skill A fresh and fresh disguise, She tried a thousand shapes at will, Then vanished from their eyes. When Gádhi's son of high renown Still saw the stony rain pour down Upon each princely warrior's head, With words of wisdom thus he said: “Enough of mercy, Ráma, lest This sinful evil-working pest, Disturber of each holy rite, Repair by magic arts her might. Without delay the fiend should die, For, see, the twilight hour is nigh. And at the joints of night and day Such giant foes are hard to slay.”
- **Translation**: 

---

### Verse 11 (Ramayan 0.151)
- **Original**: Canto XXVIII. The Death Of Tádaká. 133 Then Ráma, skilful to direct His arrow to the sound, With shafts the mighty demon checked Who rained her stones around. She sore impeded and beset By Ráma and his arrowy net, Though skilled in guile and magic lore, Rushed on the brothers with a roar. Deformed, terrific, murderous, dread, Swift as the levin on she sped, Like cloudy pile in autumn's sky, Lifting her two vast arms on high, When Ráma smote her with a dart, Shaped like a crescent, to the heart. Sore wounded by the shaft that came With lightning speed and surest aim, Blood spouting from her mouth and side, She fell upon the earth and died. Soon as the Lord who rules the sky Saw the dread monster lifeless lie, He called aloud, Well done! well done! And the Gods honoured Raghu's son. Standing in heaven the Thousand-eyed, With all the Immortals, joying cried: “Lift up thine eyes, O Saint, and see The Gods and Indra nigh to thee. This deed of Ráma's boundless might Has filled our bosoms with delight, Now, for our will would have it so, To Raghu's son some favour show. Invest him with the power which naught But penance gains and holy thought, Those heavenly arms on him bestow To thee entrusted long ago
- **Translation**: 

---

### Verse 12 (Ramayan 0.152)
- **Original**: 134 The Ramayana By great Kri[á[va best of kings, Son of the Lord of living things. More fit recipient none can be Than he who joys it following thee; And for our sakes the monarch's seed Has yet to do a mighty deed.” He spoke; and all the heavenly train Rejoicing sought their homes again, While honour to the saint they paid. Then came the evening's twilight shade, The best of hermits overjoyed To know the monstrous fiend destroyed, His lips on Ráma's forehead pressed, And thus the conquering chief addressed: “O Ráma gracious to the sight. Here will we pass the present night, And with the morrow's earliest ray Bend to my hermitage our way.” The son of Da[aratha heard, Delighted, Vi[vámitra's word, And as he bade, that night he spent In Tá aká's wild wood, content. And the grove shone that happy day, Freed from the curse that on it lay, Like Chaitraratha164 fair and gay. Canto XXIX. The Celestial Arms. 164 The famous pleasure-garden of Kuvera the God of Wealth.
- **Translation**: 

---

### Verse 13 (Ramayan 0.153)
- **Original**: Canto XXIX. The Celestial Arms. 135 That night they slept and took their rest; And then the mighty saint addressed, With pleasant smile and accents mild These words to Raghu's princely child: “Well pleased am I. High fate be thine, Thou scion of a royal line. Now will I, for I love thee so, All heavenly arms on thee bestow. Victor with these, whoe'er oppose, Thy hand shall conquer all thy foes, Though Gods and spirits of the air, Serpents and fiends, the conflict dare. I'll give thee as a pledge of love The mystic arms they use above, For worthy thou to have revealed The weapons I have learnt to wield.165 [042] First, son of Raghu, shall be thine The arm of Vengeance, strong, divine: The arm of Fate, the arm of Right, And VishGu's arm of awful might: That, before which no foe can stand, The thunderbolt of Indra's hand; And Ziva's trident, sharp and dread, And that dire weapon Brahmá's Head. And two fair clubs, O royal child, One Charmer and one Pointed styled With flame of lambent fire aglow, 165 “The whole of this Canto together with the following one, regards the belief, formerly prevalent in India, that by virtue of certain spells, to be learnt and muttered, secret knowledge and superhuman powers might be acquired. To this the poet has already alluded in Canto xxiii. These incorporeal weapons are partly represented according to the fashion of those ascribed to the Gods and the different orders of demi-gods, partly are the mere creations of fancy; and it would not be easy to say what idea the poet had of them in his own mind, or what powers he meant to assign to each.” SCHLEGEL {FNS .
- **Translation**: 

---

### Verse 14 (Ramayan 0.154)
- **Original**: 136 The Ramayana On thee, O Chieftain, I bestow. And Fate's dread net and Justice' noose That none may conquer, for thy use: And the great cord, renowned of old, Which VaruG ever loves to hold. Take these two thunderbolts, which I Have got for thee, the Moist and Dry. Here Ziva's dart to thee I yield, And that which VishGu wont to wield. I give to thee the arm of Fire, Desired by all and named the Spire. To thee I grant the Wind-God's dart, Named Crusher, O thou pure of heart, This arm, the Horse's Head, accept, And this, the Curlew's Bill yclept, And these two spears, the best e'er flew, Named the Invincible and True. And arms of fiends I make thine own, Skull-wreath and mace that smashes bone. And Joyous, which the spirits bear, Great weapon of the sons of air. Brave offspring of the best of lords, I give thee now the Gem of swords, And offer next, thine hand to arm, The heavenly bards' beloved charm. Now with two arms I thee invest Of never-ending Sleep and Rest, With weapons of the Sun and Rain, And those that dry and burn amain; And strong Desire with conquering touch, The dart that Káma prizes much. I give the arm of shadowy powers That bleeding flesh of men devours. I give the arms the God of Gold
- **Translation**: 

---

### Verse 15 (Ramayan 0.155)
- **Original**: Canto XXIX. The Celestial Arms. 137 And giant fiends exult to hold. This smites the foe in battle-strife, And takes his fortune, strength, and life. I give the arms called False and True, And great Illusion give I too; The hero's arm called Strong and Bright That spoils the foeman's strength in fight. I give thee as a priceless boon The Dew, the weapon of the Moon, And add the weapon, deftly planned, That strengthens Vi[vakarmá's hand. The Mortal dart whose point is chill, And Slaughter, ever sure to kill; All these and other arms, for thou Art very dear, I give thee now. Receive these weapons from my hand, Son of the noblest in the land.” Facing the east, the glorious saint Pure from all spot of earthly taint, To Ráma, with delighted mind, That noble host of spells consigned. He taught the arms, whose lore is won Hardly by Gods, to Raghu's son. He muttered low the spell whose call Summons those arms and rules them all And, each in visible form and frame, Before the monarch's son they came. They stood and spoke in reverent guise To Ráma with exulting cries: “O noblest child of Raghu, see, Thy ministers and thralls are we.” With joyful heart and eager hand Ráma received the wondrous band,
- **Translation**: 

---

### Verse 16 (Ramayan 0.156)
- **Original**: 138 The Ramayana And thus with words of welcome cried: “Aye present to my will abide.” Then hasted to the saint to pay Due reverence, and pursued his way. Canto XXX. The Mysterious Powers.166 Pure, with glad cheer and joyful breast, Of those mysterious arms possessed, Ráma, now passing on his way, Thus to the saint began to say: “Lord of these mighty weapons, I Can scarce be harmed by Gods on high; Now, best of saints, I long to gain The powers that can these arms restrain.” Thus spoke the prince. The sage austere, True to his vows, from evil clear, Called forth the names of those great charms Whose powers restrain the deadly arms. “Receive thou True and Truly famed, And Bold and Fleet: the weapons named[043] 166 “In SanskritSankára, a word which has various significations but the primary meaning of which isthe act of seizing. A magical power seems to be implied of employing the weapons when and where required. The remarks I have made on the preceding Canto apply with still greater force to this. The MSS. greatly vary in the enumeration of theseSankáras, and it is not surprising that copyists have incorrectly written the names which they did not well understand. The commentators throw no light upon the subject.” SCHLEGEL {FNS . I have taken the liberty of omitting four of these which Schlegel translates“Scleromphalum, Euomphalum, Centiventrem, and Chrysomphalum.”
- **Translation**: 

---

### Verse 17 (Ramayan 0.157)
- **Original**: Canto XXX. The Mysterious Powers. 139 Warder and Progress, swift of pace, Averted-head and Drooping-face; The Seen, and that which Secret flies; The weapon of the thousand eyes; Ten-headed, and the Hundred-faced, Star-gazer and the Layer-waste: The Omen-bird, the Pure-from-spot, The pair that wake and slumber not: The Fiendish, that which shakes amain, The Strong-of-Hand, the Rich-in-Gain: The Guardian, and the Close-allied, The Gaper, Love, and Golden-side: O Raghu's son receive all these, Bright ones that wear what forms they please; Kri[á[va's mystic sons are they, And worthy thou their might to sway.” With joy the pride of Raghu's race Received the hermit's proffered grace, Mysterious arms, to check and stay, Or smite the foeman in the fray. Then, all with heavenly forms endued, Nigh came the wondrous multitude. Celestial in their bright attire Some shone like coals of burning fire; Some were like clouds of dusky smoke; And suppliant thus they sweetly spoke: “Thy thralls, O Ráma, here we stand: Command, we pray, thy faithful band” “Depart,” he cried,“where each may list, But when I call you to assist, Be present to my mind with speed, And aid me in the hour of need.”
- **Translation**: 

---

### Verse 18 (Ramayan 0.158)
- **Original**: 140 The Ramayana To Ráma then they lowly bent, And round him in due reverence went, To his command, they answered, Yea, And as they came so went away. When thus the arms had homeward flown, With pleasant words and modest tone, E'en as he walked, the prince began To question thus the holy man: “What cloudlike wood is that which near The mountain's side I see appear? O tell me, for I long to know; Its pleasant aspect charms me so. Its glades are full of deer at play, And sweet birds sing on every spray, Past is the hideous wild; I feel So sweet a tremor o'er me steal, And hail with transport fresh and new A land that is so fair to view. Then tell me all, thou holy Sage, And whose this pleasant hermitage In which those wicked ones delight To mar and kill each holy rite. And with foul heart and evil deed Thy sacrifice, great Saint, impede. To whom, O Sage, belongs this land In which thine altars ready stand! 'Tis mine to guard them, and to slay The giants who the rites would stay. All this, O best of saints, I burn From thine own lips, my lord, to learn.” Canto XXXI. The Perfect Hermitage.
- **Translation**: 

---

### Verse 19 (Ramayan 0.159)
- **Original**: Canto XXXI. The Perfect Hermitage. 141 Thus spoke the prince of boundless might, And thus replied the anchorite: “Chief of the mighty arm, of yore Lord VishGu whom the Gods adore, For holy thought and rites austere Of penance made his dwelling here. This ancient wood was called of old Grove of the Dwarf, the mighty-souled, And when perfection he attained The grove the name of Perfect gained. Bali of yore, Virochan's son, Dominion over Indra won, And when with power his proud heart swelled, O'er the three worlds his empire held. When Bali then began a rite, The Gods and Indra in affright Sought VishGu in this place of rest, And thus with prayers the God addressed: “Bali. Virochan's mighty son, His sacrifice has now begun: Of boundless wealth, that demon king Is bounteous to each living thing. Though suppliants flock from every side The suit of none is e'er denied. Whate'er, where'er howe'er the call, He hears the suit and gives to all. Now with thine own illusive art Perform, O Lord, the helper's part: Assume a dwarfish form, and thus From fear and danger rescue us.”167 167 I omit, after this line, eight[lokeswhich, as Schlegel allows, are quite out of place.
- **Translation**: 

---

### Verse 20 (Ramayan 0.160)
- **Original**: 142 The Ramayana Thus in their dread the Immortals sued: The God a dwarflike shape indued:168 Before Virochan's son he came, Three steps of land his only claim. The boon obtained, in wondrous wise Lord VishGu's form increased in size; Through all the worlds, tremendous, vast, God of the Triple Step, he passed.169 The whole broad earth from side to side He measured with one mighty stride, Spanned with the next the firmament, And with the third through heaven he went.[044] Thus was the king of demons hurled By VishGu to the nether world, And thus the universe restored To Indra's rule, its ancient lord. And now because the immortal God This spot in dwarflike semblance trod, The grove has aye been loved by me For reverence of the devotee. But demons haunt it, prompt to stay Each holy offering I would pay. Be thine, O lion-lord, to kill These giants that delight in ill. This day, beloved child, our feet Shall rest within the calm retreat: And know, thou chief of Raghu's line, My hermitage is also thine.” 168 This is the fifth of theavatárs, descents or incarnations of VishGu. 169 This is a solar allegory. VishGu is the sun, the three steps being his rising, culmination, and setting.
- **Translation**: 

---

