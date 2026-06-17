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

### Verse 1 (Ramayana 0.186)
- **Original**: 168 The Ramayana Of monsters dying neath their blows, Giant and demon, fiend and snake, That in earth's core their dwelling make. They dug, in ire that naught could stay, Through sixty thousand leagues their way, Cleaving the earth with matchless strength Till hell itself they reached at length. Thus digging searched they Jambudvip184 With all its hills and mountains steep. Then a great fear began to shake The heart of God, bard, fiend, and snake, And all distressed in spirit went Before the Sire Omnipotent. With signs of woe in every face They sought the mighty Father's grace, And trembling still and ill at ease Addressed their Lord in words like these: “The sons of Sagar, Sire benign, Pierce the whole earth with mine on mine, And as their ruthless work they ply Innumerable creatures die. “This is the thief,” the princes say, “Who stole our victim steed away. This marred the rite, and caused us ill, And so their guiltless blood they spill.” Canto XLI. Kapil. 184 Said to be so called from the Jambu, or Rose Apple, abounding in it, and signifying according to the Puránas the central division of the world, the known world.
- **Translation**: 

---

### Verse 2 (Ramayana 0.187)
- **Original**: Canto XLI. Kapil. 169 The father lent a gracious ear And listened to their tale of fear, And kindly to the Gods replied Whom woe and death had terrified: “The wisest Vásudeva,185 who The Immortals' foe, fierce Madhu, slew, Regards broad Earth with love and pride And guards, in Kapil's form, his bride.186 His kindled wrath will quickly fall On the king's sons and burn them all. This cleaving of the earth his eye Foresaw in ages long gone by: He knew with prescient soul the fate That Sagar's children should await.” The Three-and-thirty,187 freed from fear, Sought their bright homes with hopeful cheer. Still rose the great tempestuous sound As Sagar's children pierced the ground. When thus the whole broad earth was cleft, And not a spot unsearched was left, 185 Here used as a name of VishGu. 186 Kings are called the husbands of their kingdoms or of the earth;“She and his kingdom were his only brides.” RaghuvaE[a. “Doubly divorced! Bad men, you violate A double marriage, 'twixt my crown and me, And then between me and my married wife.” King Richard II. Act V. Sc. I. 187 The thirty-three Gods are said in theAitareya BráhmaGa, Book I. ch. II. 10. to be the eight Vasus, the eleven Rudras, the twelve Ádityas, Prajápati, either Brahmá or Daksha, and Vashatkára or deified oblation. This must have been the actual number at the beginning of the Vedic religion gradually increased by successive mythical and religious creations till the Indian Pantheon was crowded with abstractions of every kind. Through the reverence with which the words of the Veda were regarded, the immense host of multiplied divinities, in later times, still bore the name of the Thirty-three Gods.
- **Translation**: 

---

### Verse 3 (Ramayana 0.188)
- **Original**: 170 The Ramayana Back to their home the princes sped, And thus unto their father said: “We searched the earth from side to side, While countless hosts of creatures died. Our conquering feet in triumph trod On snake and demon, fiend and God; But yet we failed, with all our toil, To find the robber and the spoil. What can we more? If more we can, Devise, O King, and tell thy plan.” His children's speech King Sagar heard, And answered thus, to anger stirred: “Dig on, and ne'er your labour stay Till through earth's depths you force your way. Then smite the robber dead, and bring The charger back with triumphing.”[052] The sixty thousand chiefs obeyed: Deep through the earth their way they made. Deep as they dug and deeper yet The immortal elephant they met, Famed Vírúpáksha188 vast of size, Upon whose head the broad earth lies: The mighty beast who earth sustains 188 “One of the elephants which, according to an ancient belief popular in India, supported the earth with their enormous backs; when one of these elephants shook his wearied head the earth trembled with its woods and hills. An idea, or rather a mythical fancy, similar to this, but reduced to proportions less grand, is found in Virgil when he speaks of Enceladus buried under Ætna:” “adi semiustum fulmine corpus Urgeri mole hac, ingentemque insuper Ætnam Impositam, ruptis flammam expirare caminis; Et fessum quoties mutat latus, intre mere omnem iam, et cœ lum subtexere fumo.” Æneid. Lib. III. GORRESIO {FNS .
- **Translation**: 

---

### Verse 4 (Ramayana 0.189)
- **Original**: Canto XLI. Kapil. 171 With shaggy hills and wooded plains. When, with the changing moon, distressed, And longing for a moment's rest, His mighty head the monster shakes, Earth to the bottom reels and quakes. Around that warder strong and vast With reverential steps they passed. Nor, when the honour due was paid, Their downward search through earth delayed. But turning from the east aside Southward again their task they plied. There Mahápadma held his place, The best of all his mighty race, Like some huge hill, of monstrous girth, Upholding on his head the earth. When the vast beast the princes saw, They marvelled and were filled with awe. The sons of high-souled Sagar round That elephant in reverence wound. Then in the western region they With might unwearied cleft their way. There saw they with astonisht eyes Saumanas, beast of mountain size. Round him with circling steps they went With greetings kind and reverent.
- **Translation**: 

---

### Verse 5 (Ramayana 0.190)
- **Original**: 172 The Ramayana On, on— no thought of rest or stay— They reached the seat of Soma's sway. There saw they Bhadra, white as snow, With lucky marks that fortune show, Bearing the earth upon his head. Round him they paced with solemn tread, And honoured him with greetings kind, Then downward yet their way they mined. They gained the tract 'twixt east and north Whose fame is ever blazoned forth,189 And by a storm of rage impelled, Digging through earth their course they held. Then all the princes, lofty-souled, Of wondrous vigour, strong and bold, Saw Vásudeva190 standing there In Kapil's form he loved to wear, And near the everlasting God The victim charger cropped the sod. They saw with joy and eager eyes The fancied robber and the prize, And on him rushed the furious band Crying aloud, Stand, villain! stand! “Avaunt! avaunt!” great Kapil cried, His bosom flusht with passion's tide; 189 “The Devas and Asuras (Gods and Titans) fought in the east, the south, the west, and the north, and the Devas were defeated by the Asuras in all these directions. They then fought in the north-eastern direction; there the Devas did not sustain defeat. This direction isaparájitá,i.e.unconquerable. Thence one should do work in this direction, and have it done there; for such a one (alone) is able to clear off his debts.” H AUG 'S{FNS Aitareya Bráhmanam, Vol. II, p. 33. The debts here spoken of are a man's religious obligations to the Gods, the Pitaras or Manes, and men. 190 VishGu.
- **Translation**: 

---

### Verse 6 (Ramayana 0.191)
- **Original**: Canto XLII. Sagar's Sacrifice. 173 Then by his might that proud array All scorcht to heaps of ashes lay.191 Canto XLII. Sagar's Sacrifice. Then to the prince his grandson, bright With his own fame's unborrowed light, King Sagar thus began to say, Marvelling at his sons' delay: “Thou art a warrior skilled and bold, Match for the mighty men of old. Now follow on thine uncles' course And track the robber of the horse. [053] To guard thee take thy sword and bow, for huge and strong are beasts below. There to the reverend reverence pay, And kill the foes who check thy way; Then turn successful home and see My sacrifice complete through thee.” 191 “It appears to me that this mythical story has reference to the volcanic phenomena of nature. Kapil may very possibly be that hidden fiery force which suddenly unprisons itself and bursts forth in volcanic effects. Kapil is, moreover, one of the names of Agni the God of Fire.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 7 (Ramayana 0.192)
- **Original**: 174 The Ramayana Obedient to the high-souled lord Grasped An[umán his bow and sword, And hurried forth the way to trace With youth and valour's eager pace. On sped he by the path he found Dug by his uncles underground. The warder elephant he saw Whose size and strength pass Nature's law, Who bears the world's tremendous weight, Whom God, fiend, giant venerate, Bird, serpent, and each flitting shade, To him the honour meet he paid With circling steps and greeting due, And further prayed him, if he knew, To tell him of his uncles' weal, And who had dared the horse to steal. To him in war and council tried The warder elephant replied: “Thou, son of Asamanj, shalt lead In triumph back the rescued steed.” As to each warder beast he came And questioned all, his words the same, The honoured youth with gentle speech Drew eloquent reply from each, That fortune should his steps attend, And with the horse he home should wend. Cheered with the grateful answer, he Passed on with step more light and free, And reached with careless heart the place Where lay in ashes Sagar's race. Then sank the spirit of the chief Beneath that shock of sudden grief, And with a bitter cry of woe
- **Translation**: 

---

### Verse 8 (Ramayana 0.193)
- **Original**: Canto XLII. Sagar's Sacrifice. 175 He mourned his kinsmen fallen so. He saw, weighed down by woe and care, The victim charger roaming there. Yet would the pious chieftain fain Oblations offer to the slain: But, needing water for the rite, He looked and there was none in sight His quick eye searching all around The uncle of his kinsmen found, King Garu , best beyond compare Of birds who wing the fields of air. Then thus unto the weeping man The son of Vinatá192 began: “Grieve not, O hero, for their fall Who died a death approved of all. Of mighty strength, they met their fate By Kapil's hand whom none can mate. Pour forth for them no earthly wave, A holier flood their spirits crave. If, daughter of the Lord of Snow, Gangá would turn her stream below, Her waves that cleanse all mortal stain Would wash their ashes pure again. Yea, when her flood whom all revere Rolls o'er the dust that moulders here, The sixty thousand, freed from sin, A home in Indra's heaven shall win. Go, and with ceaseless labour try To draw the Goddess from the sky. Return, and with thee take the steed; So shall thy grandsire's rite succeed.” 192 Garu was the son of Ka[yap and Vinatá.
- **Translation**: 

---

### Verse 9 (Ramayana 0.194)
- **Original**: 176 The Ramayana Prince An[umán the strong and brave Followed the rede SuparGa193 gave. The glorious hero took the horse, And homeward quickly bent his course. Straight to the anxious king he hied, Whom lustral rites had purified, The mournful story to unfold And all the king of birds had told. The tale of woe the monarch heard, Nor longer was the rite deferred: With care and just observance he Accomplished all, as texts decree. The rites performed, with brighter fame, Mighty in counsel, home he came. He longed to bring the river down, But found no plan his wish to crown. He pondered long with anxious thought But saw no way to what he sought. Thus thirty thousand years he spent, And then to heaven the monarch went. Canto XLIII. Bhagírath. When Sagar thus had bowed to fate, The lords and commons of the state Approved with ready heart and will Prince An[umán his throne to fill. He ruled, a mighty king, unblamed, Sire of Dilípa justly famed. 193 Garu .
- **Translation**: 

---

### Verse 10 (Ramayana 0.195)
- **Original**: Canto XLIII. Bhagírath. 177 To him, his child and worthy heir, The king resigned his kingdom's care, And on Himálaya's pleasant side His task austere of penance plied. Bright as a God in clear renown He planned to bring pure Gangá down. There on his fruitless hope intent Twice sixteen thousand years he spent, And in the grove of hermits stayed Till bliss in heaven his rites repaid. Dilípa then, the good and great, Soon as he learnt his kinsmen's fate, Bowed down by woe, with troubled mind, [054] Pondering long no cure could find. “How can I bring,” the mourner sighed, “To cleanse their dust, the heavenly tide? How can I give them rest, and save Their spirits with the offered wave?” Long with this thought his bosom skilled In holy discipline was filled. A son was born, Bhagírath named, Above all men for virtue famed. Dilípa many a rite ordained, And thirty thousand seasons reigned. But when no hope the king could see His kinsmen from their woe to free, The lord of men, by sickness tried, Obeyed the law of fate, and died; He left the kingdom to his son, And gained the heaven his deeds had won. The good Bhagírath, royal sage, Had no fair son to cheer his age. He, great in glory, pure in will, Longing for sons was childless still.
- **Translation**: 

---

### Verse 11 (Ramayana 0.196)
- **Original**: 178 The Ramayana Then on one wish, one thought intent, Planning the heavenly stream's descent, Leaving his ministers the care And burden of his state to bear, Dwelling in far Gokarna194 he Engaged in long austerity. With senses checked, with arms upraised, Five fires195 around and o'er him blazed. Each weary month the hermit passed Breaking but once his awful fast. In winter's chill the brook his bed, In rain, the clouds to screen his head. Thousands of years he thus endured Till Brahmá's favour was assured, And the high Lord of living things Looked kindly on his sufferings. With trooping Gods the Sire came near The king who plied his task austere: “Blest Monarch, of a glorious race, Thy fervent rites have won my grace. Well hast thou wrought thine awful task: Some boon in turn, O Hermit, ask.” Bhagírath, rich in glory's light, The hero with the arm of might, Thus to the Lord of earth and sky Raised suppliant hands and made reply: “If the great God his favour deigns, And my long toil its fruit obtains, Let Sagar's sons receive from me Libations that they long to see. Let Gangá with her holy wave 194 A famous and venerated region near the Malabar coast. 195 That is four fires and the sun.
- **Translation**: 

---

### Verse 12 (Ramayana 0.197)
- **Original**: Canto XLIV. The Descent Of Gangá. 179 The ashes of the heroes lave, That so my kinsmen may ascend To heavenly bliss that ne'er shall end. And give, I pray, O God, a son, Nor let my house be all undone. Sire of the worlds! be this the grace Bestowed upon Ikshváku's race.” The Sire, when thus the king had prayed, In sweet kind words his answer made. “High, high thy thought and wishes are, Bhagírath of the mighty car! Ikshváku's line is blest in thee, And as thou prayest it shall be. Gangá, whose waves in Swarga196 flow, Is daughter of the Lord of Snow. Win Ziva that his aid be lent To hold her in her mid descent, For earth alone will never bear Those torrents hurled from upper air; And none may hold her weight but He, The Trident wielding deity.” Thus having said, the Lord supreme Addressed him to the heavenly stream; And then with Gods and Maruts197 went To heaven above the firmament. Canto XLIV. The Descent Of Gangá. 196 Heaven. 197 Wind-Gods.
- **Translation**: 

---

### Verse 13 (Ramayana 0.198)
- **Original**: 180 The Ramayana The Lord of life the skies regained: The fervent king a year remained With arms upraised, refusing rest While with one toe the earth he pressed, Still as a post, with sleepless eye, The air his food, his roof the sky. The year had past. Then Umá's lord,198 King of creation, world adored, Thus spoke to great Bhagírath:“I, Well pleased thy wish will gratify, And on my head her waves shall fling The daughter of the Mountains' King!” He stood upon the lofty crest That crowns the Lord of Snow, And bade the river of the Blest Descend on earth below. Himálaya's child, adored of all, The haughty mandate heard, And her proud bosom, at the call, With furious wrath was stirred. Down from her channel in the skies With awful might she sped With a giant's rush, in a giant's size, On Ziva's holy head. “He calls me,” in her wrath she cried, “And all my flood shall sweep And whirl him in its whelming tide To hell's profoundest deep.” He held the river on his head, And kept her wandering, where, Dense as Himálaya's woods, were spread The tangles of his hair.[055] 198 Ziva.
- **Translation**: 

---

### Verse 14 (Ramayana 0.199)
- **Original**: Canto XLIV. The Descent Of Gangá. 181 No way to earth she found, ashamed, Though long and sore she strove, Condemned, until her pride were tamed, Amid his locks to rove. There, many lengthening seasons through, The wildered river ran: Bhagírath saw it, and anew His penance dire began. Then Ziva, for the hermit's sake, Bade her long wanderings end, And sinking into Vindu's lake Her weary waves descend. From Gangá, by the God set free, Seven noble rivers came; Hládiní, Pávaní, and she Called Naliní by name: These rolled their lucid waves along And sought the eastern side. Suchakshu, Sítá fair and strong, And Sindhu's mighty tide— 199 These to the region of the west With joyful waters sped: The seventh, the brightest and the best, Flowed where Bhagírath led. On Ziva's head descending first A rest the torrents found: Then down in all their might they burst And roared along the ground. On countless glittering scales the beam Of rosy morning flashed, 199 The lake Vindu does not exist. Of the seven rivers here mentioned two only, the Ganges and the Sindhu or Indus, are known to geographers. Hládiní means the Gladdener, Pávaní the Purifier, Naliní the Lotus-Clad, and Suchakshu the Fair-eyed.
- **Translation**: 

---

### Verse 15 (Ramayana 0.200)
- **Original**: 182 The Ramayana Where fish and dolphins through the stream Fallen and falling dashed. Then bards who chant celestial lays And nymphs of heavenly birth Flocked round upon that flood to gaze That streamed from sky to earth. The Gods themselves from every sphere, Incomparably bright, Borne in their golden cars drew near To see the wondrous sight. The cloudless sky was all aflame With the light of a hundred suns Where'er the shining chariots came That bore those holy ones. So flashed the air with crested snakes And fish of every hue As when the lightning's glory breaks Through fields of summer blue. And white foam-clouds and silver spray Were wildly tossed on high, Like swans that urge their homeward way Across the autumn sky. Now ran the river calm and clear With current strong and deep: Now slowly broadened to a mere, Or scarcely seemed to creep. Now o'er a length of sandy plain Her tranquil course she held; Now rose her waves and sank again, By refluent waves repelled. So falling first onZiva's head, Thence rushing to their earthly bed, In ceaseless fall the waters streamed, And pure with holy lustre gleamed.
- **Translation**: 

---

### Verse 16 (Ramayana 0.201)
- **Original**: Canto XLIV. The Descent Of Gangá. 183 Then every spirit, sage, and bard, Condemned to earth by sentence hard, Pressed eagerly around the tide ThatZiva's touch had sanctified. Then they whom heavenly doom had hurled, Accursed, to this lower world, Touched the pure wave, and freed from sin Resought the skies and entered in. And all the world was glad, whereon The glorious water flowed and shone, For sin and stain were banished thence By the sweet river's influence. First, in a car of heavenly frame, The royal saint of deathless name, Bhagírath, very glorious rode, And after him fair Gangá flowed. God, sage, and bard, the chief in place Of spirits and the Nága race, Nymph, giant, fiend, in long array Sped where Bhagírath led the way; And all the hosts the flood that swim Followed the stream that followed him. Where'er the great Bhagírath led, There ever glorious Gangá fled, The best of floods, the rivers' queen, Whose waters wash the wicked clean. It chanced that Jahnu, great and good, Engaged with holy offerings stood; The river spread her waves around Flooding his sacrificial ground. The saint in anger marked her pride, And at one draught her stream he dried. Then God, and sage, and bard, afraid,
- **Translation**: 

---

### Verse 17 (Ramayana 0.202)
- **Original**: 184 The Ramayana To noble high-souled Jahnu prayed, And begged that he would kindly deem His own dear child that holy stream. Moved by their suit, he soothed their fears And loosed her waters from his ears. Hence Gangá through the world is styled Both Jáhnavi and Jahnu's child. Then onward still she followed fast, And reached the great sea bank at last. Thence deep below her way she made To end those rites so long delayed. The monarch reached the Ocean's side, And still behind him Gangá hied. He sought the depths which open lay Where Sagar's sons had dug their way. So leading through earth's nether caves The river's purifying waves,[056] Over his kinsmen's dust the lord His funeral libation poured. Soon as the flood their dust bedewed, Their spirits gained beatitude, And all in heavenly bodies dressed Rose to the skies' eternal rest. Then thus to King Bhagírath said Brahmá, when, coming at the head Of all his bright celestial train, He saw those spirits freed from stain: “Well done! great Prince of men, well done! Thy kinsmen bliss and heaven have won. The sons of Sagar mighty-souled, Are with the Blest, as Gods, enrolled, Long as the Ocean's flood shall stand Upon the border of the land,
- **Translation**: 

---

### Verse 18 (Ramayana 0.203)
- **Original**: Canto XLIV. The Descent Of Gangá. 185 So long shall Sagar's sons remain, And, godlike, rank in heaven retain. Gangá thine eldest child shall be, Called from thy name Bhágirathí; Named also— for her waters fell From heaven and flow through earth and hell— Tripathagá, stream of the skies, Because three paths she glorifies. And, mighty King, 'tis given thee now To free thee and perform thy vow. No longer, happy Prince, delay Drink-offerings to thy kin to pay. For this the holiest Sagar sighed, But mourned the boon he sought denied. Then An[umán, dear Prince! although No brighter name the world could show, Strove long the heavenly flood to gain To visit earth, but strove in vain. Nor was she by the sages' peer, Blest with all virtues, most austere, Thy sire Dilípa, hither brought, Though with fierce prayers the boon he sought. But thou, O King, earned success, And won high fame which God will bless. Through thee, O victor of thy foes, On earth this heavenly Gangá flows, And thou hast gained the meed divine That waits on virtue such as thine. Now in her ever holy wave Thyself, O best of heroes, lave: So shalt thou, pure from every sin, The blessed fruit of merit win. Now for thy kin who died of yore The meet libations duly pour.
- **Translation**: 

---

### Verse 19 (Ramayana 0.204)
- **Original**: 186 The Ramayana Above the heavens I now ascend: Depart, and bliss thy steps attend.” Thus to the mighty king who broke His foemens' might, Lord Brahmá spoke, And with his Gods around him rose To his own heaven of blest repose. The royal sage no more delayed, But, the libation duly paid, Home to his regal city hied With water cleansed and purified. There ruled he his ancestral state, Best of all men, most fortunate. And all the people joyed again In good Bhagírath's gentle reign. Rich, prosperous, and blest were they, And grief and sickness fled away. Thus, Ráma, I at length have told How Gangá came from heaven of old. Now, for the evening passes swift, I wish thee each auspicious gift. This story of the flood's descent Will give— for 'tis most excellent— Wealth, purity, fame, length of days, And to the skies its hearers raise” Canto XLV. The Quest Of The Amrit.
- **Translation**: 

---

### Verse 20 (Ramayana 0.205)
- **Original**: Canto XLV. The Quest Of The Amrit. 187 High and more high their wonder rose As the strange story reached its close, And thus, with LakshmaG, Ráma, best Of Raghu's sons, the saint addressed: “Most wondrous is the tale which thou Hast told of heavenly Gangá, how From realms above descending she Flowed through the land and filled the sea. In thinking o'er what thou hast said The night has like a moment fled, Whose hours in musing have been spent Upon thy words most excellent: So much, O holy Sage, thy lore Has charmed us with this tale of yore.” Day dawned. The morning rites were done And the victorious Raghu's son Addressed the sage in words like these, Rich in his long austerities: “The night is past: the morn is clear; Told is the tale so good to hear: Now o'er that river let us go, Three-pathed, the best of all that flow. This boat stands ready on the shore To bear the holy hermits o'er, Who of thy coming warned, in haste, The barge upon the bank have placed.” And Ku [ik's son approved his speech, And moving to the sandy beach, Placed in the boat the hermit band, And reached the river's further strand. On the north bank their feet they set, And greeted all the saints they met.
- **Translation**: 

---

