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

### Verse 1 (Ramayan 0.181)
- **Original**: Canto XXXIX. The Sons Of Sagar. 163 For piety and love of truth. Aríshmanemi's daughter fair, With whom no maiden might compare In beauty, though the earth is wide, Sumati, was his second bride. With his two queens afar he went, And weary days in penance spent, Fervent, upon Himálaya's hill Where springs the stream called Bhrigu' rill. Nor did he fail that saint to please With his devout austerities. And, when a hundred years had fled, Thus the most truthful Bhrigu said: “From thee, O Sagar, blameless King, A mighty host of sons shall spring, And thou shalt win a glorious name Which none, O Chief, but thou shall claim. One of thy queens a son shall bear, Maintainer of thy race and heir; And of the other there shall be Sons sixty thousand born to thee.” Thus as he spake, with one accord, To win the grace of that high lord, The queens, with palms together laid, In humble supplication prayed: “Which queen, O Bráhman, of the pair, The many, or the one shall bear? Most eager, Lord, are we to know, And as thou sayest be it so.” [050] With his sweet speech the saint replied: “Yourselves, O Queens, the choice decide. Your own discretion freely use Which shall the one or many choose:
- **Translation**: 

---

### Verse 2 (Ramayan 0.182)
- **Original**: 164 The Ramayana One shall the race and name uphold, The host be famous, strong, and bold. Which will have which?” Then Ke[ini The mother of one heir would be. Sumati, sister of the king181 Of all the birds that ply the wing, To that illustrious Bráhman sued That she might bear the multitude Whose fame throughout the world should sound For mighty enterprise renowned. Around the saint the monarch went, Bowing his head, most reverent. Then with his wives, with willing feet, Resought his own imperial seat. Time passed. The elder consort bare A son called Asamanj, the heir. Then Sumati, the younger, gave Birth to a gourd,182 O hero brave, Whose rind, when burst and cleft in two, Gave sixty thousand babes to view. All these with care the nurses laid In jars of oil; and there they stayed, Till, youthful age and strength complete, Forth speeding from each dark retreat, All peers in valour, years, and might, The sixty thousand came to light. Prince Asamanj, brought up with care, Scourge of his foes, was made the heir. But liegemen's boys he used to cast To Sarjú's waves that hurried past, Laughing the while in cruel glee 181 Garu a. 182 Ikshváku, the name of a king of Ayodhyá who is regarded as the founder of the Solar race, means also agourd. Hence, perhaps, the myth.
- **Translation**: 

---

### Verse 3 (Ramayan 0.183)
- **Original**: Canto XL. The Cleaving Of The Earth. 165 Their dying agonies to see. This wicked prince who aye withstood The counsel of the wise and good, Who plagued the people in his hate, His father banished from the state. His son, kind-spoken, brave, and tall, Was An [umán, beloved of all. Long years flew by. The king decreed To slay a sacrificial steed. Consulting with his priestly band He vowed the rite his soul had planned, And, Veda skilled, by their advice Made ready for the sacrifice. Canto XL. The Cleaving Of The Earth. The hermit ceased: the tale was done: Then in a transport Raghu's son Again addressed the ancient sire Resplendent as a burning fire: “O holy man, I fain would hear The tale repeated full and clear How he from whom my sires descend Brought the great rite to happy end.” The hermit answered with a smile: “Then listen, son of Raghu, while My legendary tale proceeds To tell of high-souled Sagar's deeds. Within the spacious plain that lies From where Himálaya's heights arise
- **Translation**: 

---

### Verse 4 (Ramayan 0.184)
- **Original**: 166 The Ramayana To where proud Vindhya's rival chain Looks down upon the subject plain— A land the best for rites declared183. — His sacrifice the king prepared. And An [umán the prince— for so Sagar advised— with ready bow Was borne upon a mighty car To watch the steed who roamed afar. But Indra, monarch of the skies, Veiling his form in demon guise, Came down upon the appointed day And drove the victim horse away. Reft of the steed the priests, distressed, The master of the rite addressed: “Upon the sacred day by force A robber takes the victim horse. Haste, King! now let the thief be slain; Bring thou the charger back again: The sacred rite prevented thus Brings scathe and woe to all of us. Rise, monarch, and provide with speed That naught its happy course impede.” 183 “The region here spoken of is called in the Laws of ManuMadhyade [a or the middle region.‘The region situated between the Himálaya and the Vindhya Mountains… is calledMadhyade [a, or the middle region; the space comprised between these two mountains from the eastern to the western sea is called by sages Áryávartta,the seat of honourable men.’(M ANU {FNS , II, 21, 22.) The Sanskrit Indians called themselves Áryans, which meanshonourable,noble, to distinguish themselves from the surrounding nations of different origin.” G ORRESIO {FNS
- **Translation**: 

---

### Verse 5 (Ramayan 0.185)
- **Original**: Canto XL. The Cleaving Of The Earth. 167 King Sagar in his crowded court Gave ear unto the priests' report. He summoned straightway to his side His sixty thousand sons, and cried: “Brave sons of mine, I knew not how These demons are so mighty now: The priests began the rite so well All sanctified with prayer and spell. If in the depths of earth he hide, Or lurk beneath the ocean's tide, [051] Pursue, dear sons, the robber's track; Slay him and bring the charger back. The whole of this broad earth explore, Sea-garlanded, from shore to shore: Yea, dig her up with might and main Until you see the horse again. Deep let your searching labour reach, A league in depth dug out by each. The robber of our horse pursue, And please your sire who orders you. My grandson, I, this priestly train, Till the steed comes, will here remain.” Their eager hearts with transport burned As to their task the heroes turned. Obedient to their father, they Through earth's recesses forced their way. With iron arms' unflinching toil Each dug a league beneath the soil. Earth, cleft asunder, groaned in pain, As emulous they plied amain Sharp-pointed coulter, pick, and bar, Hard as the bolts of Indra are. Then loud the horrid clamour rose
- **Translation**: 

---

### Verse 6 (Ramayan 0.186)
- **Original**: 168 The Ramayana Of monsters dying neath their blows, Giant and demon, fiend and snake, That in earth's core their dwelling make. They dug, in ire that naught could stay, Through sixty thousand leagues their way, Cleaving the earth with matchless strength Till hell itself they reached at length. Thus digging searched they Jambudvip184 With all its hills and mountains steep. Then a great fear began to shake The heart of God, bard, fiend, and snake, And all distressed in spirit went Before the Sire Omnipotent. With signs of woe in every face They sought the mighty Father's grace, And trembling still and ill at ease Addressed their Lord in words like these: “The sons of Sagar, Sire benign, Pierce the whole earth with mine on mine, And as their ruthless work they ply Innumerable creatures die. “This is the thief,” the princes say, “Who stole our victim steed away. This marred the rite, and caused us ill, And so their guiltless blood they spill.” Canto XLI. Kapil. 184 Said to be so called from the Jambu, or Rose Apple, abounding in it, and signifying according to the Puránas the central division of the world, the known world.
- **Translation**: 

---

### Verse 7 (Ramayan 0.187)
- **Original**: Canto XLI. Kapil. 169 The father lent a gracious ear And listened to their tale of fear, And kindly to the Gods replied Whom woe and death had terrified: “The wisest Vásudeva,185 who The Immortals' foe, fierce Madhu, slew, Regards broad Earth with love and pride And guards, in Kapil's form, his bride.186 His kindled wrath will quickly fall On the king's sons and burn them all. This cleaving of the earth his eye Foresaw in ages long gone by: He knew with prescient soul the fate That Sagar's children should await.” The Three-and-thirty,187 freed from fear, Sought their bright homes with hopeful cheer. Still rose the great tempestuous sound As Sagar's children pierced the ground. When thus the whole broad earth was cleft, And not a spot unsearched was left, 185 Here used as a name of VishGu. 186 Kings are called the husbands of their kingdoms or of the earth;“She and his kingdom were his only brides.” RaghuvaE[a. “Doubly divorced! Bad men, you violate A double marriage, 'twixt my crown and me, And then between me and my married wife.” King Richard II. Act V. Sc. I. 187 The thirty-three Gods are said in theAitareya BráhmaGa, Book I. ch. II. 10. to be the eight Vasus, the eleven Rudras, the twelve Ádityas, Prajápati, either Brahmá or Daksha, and Vashatkára or deified oblation. This must have been the actual number at the beginning of the Vedic religion gradually increased by successive mythical and religious creations till the Indian Pantheon was crowded with abstractions of every kind. Through the reverence with which the words of the Veda were regarded, the immense host of multiplied divinities, in later times, still bore the name of the Thirty-three Gods.
- **Translation**: 

---

### Verse 8 (Ramayan 0.188)
- **Original**: 170 The Ramayana Back to their home the princes sped, And thus unto their father said: “We searched the earth from side to side, While countless hosts of creatures died. Our conquering feet in triumph trod On snake and demon, fiend and God; But yet we failed, with all our toil, To find the robber and the spoil. What can we more? If more we can, Devise, O King, and tell thy plan.” His children's speech King Sagar heard, And answered thus, to anger stirred: “Dig on, and ne'er your labour stay Till through earth's depths you force your way. Then smite the robber dead, and bring The charger back with triumphing.”[052] The sixty thousand chiefs obeyed: Deep through the earth their way they made. Deep as they dug and deeper yet The immortal elephant they met, Famed Vírúpáksha188 vast of size, Upon whose head the broad earth lies: The mighty beast who earth sustains 188 “One of the elephants which, according to an ancient belief popular in India, supported the earth with their enormous backs; when one of these elephants shook his wearied head the earth trembled with its woods and hills. An idea, or rather a mythical fancy, similar to this, but reduced to proportions less grand, is found in Virgil when he speaks of Enceladus buried under Ætna:” “adi semiustum fulmine corpus Urgeri mole hac, ingentemque insuper Ætnam Impositam, ruptis flammam expirare caminis; Et fessum quoties mutat latus, intre mere omnem iam, et cœ lum subtexere fumo.” Æneid. Lib. III. GORRESIO {FNS .
- **Translation**: 

---

### Verse 9 (Ramayan 0.189)
- **Original**: Canto XLI. Kapil. 171 With shaggy hills and wooded plains. When, with the changing moon, distressed, And longing for a moment's rest, His mighty head the monster shakes, Earth to the bottom reels and quakes. Around that warder strong and vast With reverential steps they passed. Nor, when the honour due was paid, Their downward search through earth delayed. But turning from the east aside Southward again their task they plied. There Mahápadma held his place, The best of all his mighty race, Like some huge hill, of monstrous girth, Upholding on his head the earth. When the vast beast the princes saw, They marvelled and were filled with awe. The sons of high-souled Sagar round That elephant in reverence wound. Then in the western region they With might unwearied cleft their way. There saw they with astonisht eyes Saumanas, beast of mountain size. Round him with circling steps they went With greetings kind and reverent.
- **Translation**: 

---

### Verse 10 (Ramayan 0.190)
- **Original**: 172 The Ramayana On, on— no thought of rest or stay— They reached the seat of Soma's sway. There saw they Bhadra, white as snow, With lucky marks that fortune show, Bearing the earth upon his head. Round him they paced with solemn tread, And honoured him with greetings kind, Then downward yet their way they mined. They gained the tract 'twixt east and north Whose fame is ever blazoned forth,189 And by a storm of rage impelled, Digging through earth their course they held. Then all the princes, lofty-souled, Of wondrous vigour, strong and bold, Saw Vásudeva190 standing there In Kapil's form he loved to wear, And near the everlasting God The victim charger cropped the sod. They saw with joy and eager eyes The fancied robber and the prize, And on him rushed the furious band Crying aloud, Stand, villain! stand! “Avaunt! avaunt!” great Kapil cried, His bosom flusht with passion's tide; 189 “The Devas and Asuras (Gods and Titans) fought in the east, the south, the west, and the north, and the Devas were defeated by the Asuras in all these directions. They then fought in the north-eastern direction; there the Devas did not sustain defeat. This direction isaparájitá,i.e.unconquerable. Thence one should do work in this direction, and have it done there; for such a one (alone) is able to clear off his debts.” H AUG 'S{FNS Aitareya Bráhmanam, Vol. II, p. 33. The debts here spoken of are a man's religious obligations to the Gods, the Pitaras or Manes, and men. 190 VishGu.
- **Translation**: 

---

### Verse 11 (Ramayan 0.191)
- **Original**: Canto XLII. Sagar's Sacrifice. 173 Then by his might that proud array All scorcht to heaps of ashes lay.191 Canto XLII. Sagar's Sacrifice. Then to the prince his grandson, bright With his own fame's unborrowed light, King Sagar thus began to say, Marvelling at his sons' delay: “Thou art a warrior skilled and bold, Match for the mighty men of old. Now follow on thine uncles' course And track the robber of the horse. [053] To guard thee take thy sword and bow, for huge and strong are beasts below. There to the reverend reverence pay, And kill the foes who check thy way; Then turn successful home and see My sacrifice complete through thee.” 191 “It appears to me that this mythical story has reference to the volcanic phenomena of nature. Kapil may very possibly be that hidden fiery force which suddenly unprisons itself and bursts forth in volcanic effects. Kapil is, moreover, one of the names of Agni the God of Fire.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 12 (Ramayan 0.192)
- **Original**: 174 The Ramayana Obedient to the high-souled lord Grasped An[umán his bow and sword, And hurried forth the way to trace With youth and valour's eager pace. On sped he by the path he found Dug by his uncles underground. The warder elephant he saw Whose size and strength pass Nature's law, Who bears the world's tremendous weight, Whom God, fiend, giant venerate, Bird, serpent, and each flitting shade, To him the honour meet he paid With circling steps and greeting due, And further prayed him, if he knew, To tell him of his uncles' weal, And who had dared the horse to steal. To him in war and council tried The warder elephant replied: “Thou, son of Asamanj, shalt lead In triumph back the rescued steed.” As to each warder beast he came And questioned all, his words the same, The honoured youth with gentle speech Drew eloquent reply from each, That fortune should his steps attend, And with the horse he home should wend. Cheered with the grateful answer, he Passed on with step more light and free, And reached with careless heart the place Where lay in ashes Sagar's race. Then sank the spirit of the chief Beneath that shock of sudden grief, And with a bitter cry of woe
- **Translation**: 

---

### Verse 13 (Ramayan 0.193)
- **Original**: Canto XLII. Sagar's Sacrifice. 175 He mourned his kinsmen fallen so. He saw, weighed down by woe and care, The victim charger roaming there. Yet would the pious chieftain fain Oblations offer to the slain: But, needing water for the rite, He looked and there was none in sight His quick eye searching all around The uncle of his kinsmen found, King Garu , best beyond compare Of birds who wing the fields of air. Then thus unto the weeping man The son of Vinatá192 began: “Grieve not, O hero, for their fall Who died a death approved of all. Of mighty strength, they met their fate By Kapil's hand whom none can mate. Pour forth for them no earthly wave, A holier flood their spirits crave. If, daughter of the Lord of Snow, Gangá would turn her stream below, Her waves that cleanse all mortal stain Would wash their ashes pure again. Yea, when her flood whom all revere Rolls o'er the dust that moulders here, The sixty thousand, freed from sin, A home in Indra's heaven shall win. Go, and with ceaseless labour try To draw the Goddess from the sky. Return, and with thee take the steed; So shall thy grandsire's rite succeed.” 192 Garu was the son of Ka[yap and Vinatá.
- **Translation**: 

---

### Verse 14 (Ramayan 0.194)
- **Original**: 176 The Ramayana Prince An[umán the strong and brave Followed the rede SuparGa193 gave. The glorious hero took the horse, And homeward quickly bent his course. Straight to the anxious king he hied, Whom lustral rites had purified, The mournful story to unfold And all the king of birds had told. The tale of woe the monarch heard, Nor longer was the rite deferred: With care and just observance he Accomplished all, as texts decree. The rites performed, with brighter fame, Mighty in counsel, home he came. He longed to bring the river down, But found no plan his wish to crown. He pondered long with anxious thought But saw no way to what he sought. Thus thirty thousand years he spent, And then to heaven the monarch went. Canto XLIII. Bhagírath. When Sagar thus had bowed to fate, The lords and commons of the state Approved with ready heart and will Prince An[umán his throne to fill. He ruled, a mighty king, unblamed, Sire of Dilípa justly famed. 193 Garu .
- **Translation**: 

---

### Verse 15 (Ramayan 0.195)
- **Original**: Canto XLIII. Bhagírath. 177 To him, his child and worthy heir, The king resigned his kingdom's care, And on Himálaya's pleasant side His task austere of penance plied. Bright as a God in clear renown He planned to bring pure Gangá down. There on his fruitless hope intent Twice sixteen thousand years he spent, And in the grove of hermits stayed Till bliss in heaven his rites repaid. Dilípa then, the good and great, Soon as he learnt his kinsmen's fate, Bowed down by woe, with troubled mind, [054] Pondering long no cure could find. “How can I bring,” the mourner sighed, “To cleanse their dust, the heavenly tide? How can I give them rest, and save Their spirits with the offered wave?” Long with this thought his bosom skilled In holy discipline was filled. A son was born, Bhagírath named, Above all men for virtue famed. Dilípa many a rite ordained, And thirty thousand seasons reigned. But when no hope the king could see His kinsmen from their woe to free, The lord of men, by sickness tried, Obeyed the law of fate, and died; He left the kingdom to his son, And gained the heaven his deeds had won. The good Bhagírath, royal sage, Had no fair son to cheer his age. He, great in glory, pure in will, Longing for sons was childless still.
- **Translation**: 

---

### Verse 16 (Ramayan 0.196)
- **Original**: 178 The Ramayana Then on one wish, one thought intent, Planning the heavenly stream's descent, Leaving his ministers the care And burden of his state to bear, Dwelling in far Gokarna194 he Engaged in long austerity. With senses checked, with arms upraised, Five fires195 around and o'er him blazed. Each weary month the hermit passed Breaking but once his awful fast. In winter's chill the brook his bed, In rain, the clouds to screen his head. Thousands of years he thus endured Till Brahmá's favour was assured, And the high Lord of living things Looked kindly on his sufferings. With trooping Gods the Sire came near The king who plied his task austere: “Blest Monarch, of a glorious race, Thy fervent rites have won my grace. Well hast thou wrought thine awful task: Some boon in turn, O Hermit, ask.” Bhagírath, rich in glory's light, The hero with the arm of might, Thus to the Lord of earth and sky Raised suppliant hands and made reply: “If the great God his favour deigns, And my long toil its fruit obtains, Let Sagar's sons receive from me Libations that they long to see. Let Gangá with her holy wave 194 A famous and venerated region near the Malabar coast. 195 That is four fires and the sun.
- **Translation**: 

---

### Verse 17 (Ramayan 0.197)
- **Original**: Canto XLIV. The Descent Of Gangá. 179 The ashes of the heroes lave, That so my kinsmen may ascend To heavenly bliss that ne'er shall end. And give, I pray, O God, a son, Nor let my house be all undone. Sire of the worlds! be this the grace Bestowed upon Ikshváku's race.” The Sire, when thus the king had prayed, In sweet kind words his answer made. “High, high thy thought and wishes are, Bhagírath of the mighty car! Ikshváku's line is blest in thee, And as thou prayest it shall be. Gangá, whose waves in Swarga196 flow, Is daughter of the Lord of Snow. Win Ziva that his aid be lent To hold her in her mid descent, For earth alone will never bear Those torrents hurled from upper air; And none may hold her weight but He, The Trident wielding deity.” Thus having said, the Lord supreme Addressed him to the heavenly stream; And then with Gods and Maruts197 went To heaven above the firmament. Canto XLIV. The Descent Of Gangá. 196 Heaven. 197 Wind-Gods.
- **Translation**: 

---

### Verse 18 (Ramayan 0.198)
- **Original**: 180 The Ramayana The Lord of life the skies regained: The fervent king a year remained With arms upraised, refusing rest While with one toe the earth he pressed, Still as a post, with sleepless eye, The air his food, his roof the sky. The year had past. Then Umá's lord,198 King of creation, world adored, Thus spoke to great Bhagírath:“I, Well pleased thy wish will gratify, And on my head her waves shall fling The daughter of the Mountains' King!” He stood upon the lofty crest That crowns the Lord of Snow, And bade the river of the Blest Descend on earth below. Himálaya's child, adored of all, The haughty mandate heard, And her proud bosom, at the call, With furious wrath was stirred. Down from her channel in the skies With awful might she sped With a giant's rush, in a giant's size, On Ziva's holy head. “He calls me,” in her wrath she cried, “And all my flood shall sweep And whirl him in its whelming tide To hell's profoundest deep.” He held the river on his head, And kept her wandering, where, Dense as Himálaya's woods, were spread The tangles of his hair.[055] 198 Ziva.
- **Translation**: 

---

### Verse 19 (Ramayan 0.199)
- **Original**: Canto XLIV. The Descent Of Gangá. 181 No way to earth she found, ashamed, Though long and sore she strove, Condemned, until her pride were tamed, Amid his locks to rove. There, many lengthening seasons through, The wildered river ran: Bhagírath saw it, and anew His penance dire began. Then Ziva, for the hermit's sake, Bade her long wanderings end, And sinking into Vindu's lake Her weary waves descend. From Gangá, by the God set free, Seven noble rivers came; Hládiní, Pávaní, and she Called Naliní by name: These rolled their lucid waves along And sought the eastern side. Suchakshu, Sítá fair and strong, And Sindhu's mighty tide— 199 These to the region of the west With joyful waters sped: The seventh, the brightest and the best, Flowed where Bhagírath led. On Ziva's head descending first A rest the torrents found: Then down in all their might they burst And roared along the ground. On countless glittering scales the beam Of rosy morning flashed, 199 The lake Vindu does not exist. Of the seven rivers here mentioned two only, the Ganges and the Sindhu or Indus, are known to geographers. Hládiní means the Gladdener, Pávaní the Purifier, Naliní the Lotus-Clad, and Suchakshu the Fair-eyed.
- **Translation**: 

---

### Verse 20 (Ramayan 0.200)
- **Original**: 182 The Ramayana Where fish and dolphins through the stream Fallen and falling dashed. Then bards who chant celestial lays And nymphs of heavenly birth Flocked round upon that flood to gaze That streamed from sky to earth. The Gods themselves from every sphere, Incomparably bright, Borne in their golden cars drew near To see the wondrous sight. The cloudless sky was all aflame With the light of a hundred suns Where'er the shining chariots came That bore those holy ones. So flashed the air with crested snakes And fish of every hue As when the lightning's glory breaks Through fields of summer blue. And white foam-clouds and silver spray Were wildly tossed on high, Like swans that urge their homeward way Across the autumn sky. Now ran the river calm and clear With current strong and deep: Now slowly broadened to a mere, Or scarcely seemed to creep. Now o'er a length of sandy plain Her tranquil course she held; Now rose her waves and sank again, By refluent waves repelled. So falling first onZiva's head, Thence rushing to their earthly bed, In ceaseless fall the waters streamed, And pure with holy lustre gleamed.
- **Translation**: 

---

