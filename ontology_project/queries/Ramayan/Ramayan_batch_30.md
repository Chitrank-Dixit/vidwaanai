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

### Verse 1 (Ramayan 0.581)
- **Original**: Canto LVI. Chitrakúta 563 O brother, in that holy shade How happy shall we be!”331 Then Ráma, LakshmaG, Sítá, each Spoke raising suppliant hands this speech To him, in woodland dwelling met, Válmíki, ancient anchoret: “O Saint, this mountain takes the mind, With creepers, trees of every kind, With fruit and roots abounding thus, A pleasant life it offers us: Here for a while we fain would stay, And pass a season blithe and gay.” Then the great saint, in duty trained, With honour gladly entertained: He gave his guests a welcome fair, And bade them sit and rest them there, Ráma of mighty arm and chest His faithful LakshmaG then addressed: “Brother, bring hither from the wood Selected timber strong and good, And build therewith a little cot; My heart rejoices in the spot That lies beneath the mountain's side, Remote, with water well supplied.” 331 “We have often looked on that green hill: it is the holiest spot of that sect of the Hindu faith who devote themselves to this incarnation of VishGu. The whole neighbourhood is Ráma's country. Every headland has some legend, every cavern is connected with his name; some of the wild fruits are still calledSítáphal, being the reputed food of the exile. Thousands and thousands annually visit the spot, and round the hill is a raised foot-path, on which the devotee, with naked feet, treads full of pious awe.” Calcutta Review, Vol. XXIII.
- **Translation**: 

---

### Verse 2 (Ramayan 0.582)
- **Original**: 564 The Ramayana Sumitrá's son his words obeyed, Brought many a tree, and deftly made, With branches in the forest cut, As Ráma bade, a leafy hut. Then Ráma, when the cottage stood Fair, firmly built, and walled with wood, To LakshmaG spake, whose eager mind To do his brother's will inclined: “Now, LakshmaG as our cot is made, Must sacrifice be duly paid By us, for lengthened life who hope, With venison of the antelope. Away, O bright-eyed LakshmaG, speed: Struck by thy bow a deer must bleed: As Scripture bids, we must not slight The duty that commands the rite.” Lakshma G, the chief whose arrows laid His foemen low, his word obeyed; And Ráma thus again addressed The swift performer of his hest: “Prepare the venison thou hast shot, To sacrifice for this our cot. Haste, brother dear, for this the hour, And this the day of certain power.” Then glorious LakshmaG took the buck His arrow in the wood had struck; Bearing his mighty load he came, And laid it in the kindled flame.[162] Soon as he saw the meat was done, And that the juices ceased to run From the broiled carcass, LakshmaG then Spoke thus to Ráma best of men: “The carcass of the buck, entire,
- **Translation**: 

---

### Verse 3 (Ramayan 0.583)
- **Original**: Canto LVI. Chitrakúta 565 Is ready dressed upon the fire. Now be the sacred rites begun To please the God, thou godlike one.” Ráma the good, in ritual trained, Pure from the bath, with thoughts restrained, Hasted those verses to repeat Which make the sacrifice complete. The hosts celestial came in view, And Ráma to the cot withdrew, While a sweet sense of rapture stole Through the unequalled hero's soul. He paid the Vi[vedevas332 due. And Rudra's right, and VishGu's too, Nor wonted blessings, to protect Their new-built home, did he neglect. With voice repressed he breathed the prayer, Bathed duly in the river fair, And gave good offerings that remove The stain of sin, as texts approve. And many an altar there he made, And shrines, to suit the holy shade, All decked with woodland chaplets sweet, And fruit and roots and roasted meat, With muttered prayer, as texts require, Water, and grass and wood and fire. So Ráma, LakshmaG, Sítá paid Their offerings to each God and shade, And entered then their pleasant cot That bore fair signs of happy lot. They entered, the illustrious three, 332 Deities of a particular class in which five or ten are enumerated. They are worshipped particularly at the funeral obsequies in honour of deceased progenitors.
- **Translation**: 

---

### Verse 4 (Ramayan 0.584)
- **Original**: 566 The Ramayana The well-set cottage, fair to see, Roofed with the leaves of many a tree, And fenced from wind and rain: So, at their Father Brahmá's call, The Gods of heaven, assembling all, To their own glorious council hall Advance in shining train. So, resting on that lovely hill, Near the fair lily-covered rill, The happy prince forgot, Surrounded by the birds and deer, The woe, the longing, and the fear That gloom the exile's lot. Canto LVII. Sumantra's Return. When Ráma reached the southern bank, King Guha's heart with sorrow sank: He with Sumantra talked, and spent With his deep sorrow, homeward went. Sumantra, as the king decreed, Yoked to the car each noble steed, And to Ayodhyá's city sped With his sad heart disquieted. On lake and brook and scented grove His glances fell, as on he drove: City and village came in view As o'er the road his coursers flew. On the third day the charioteer, When now the hour of night was near, Came to Ayodhyá's gate, and found
- **Translation**: 

---

### Verse 5 (Ramayan 0.585)
- **Original**: Canto LVII. Sumantra's Return. 567 The city all in sorrow drowned. To him, in spirit quite cast down, Forsaken seemed the silent town, And by the rush of grief oppressed He pondered in his mournful breast: “Is all Ayodhyá burnt with grief, Steed, elephant, and man, and chief? Does her loved Ráma's exile so Afflict her with the fires of woe?” Thus as he mused, his steeds flew fast, And swiftly through the gate he passed. On drove the charioteer, and then In hundreds, yea in thousands, men Ran to the car from every side, And, “Ráma, where is Ráma?” cried. Sumantra said:“My chariot bore The duteous prince to Gangá's shore; I left him there at his behest, And homeward to Ayodhyá pressed.” Soon as the anxious people knew That he was o'er the flood they drew Deep sighs, and crying, Ráma! all Wailed, and big tears began to fall. He heard the mournful words prolonged, As here and there the people thronged: “Woe, woe for us, forlorn, undone, No more to look on Raghu's son! His like again we ne'er shall see, Of heart so true, of hand so free, In gifts, in gatherings for debate, When marriage pomps we celebrate, What should we do? What earthly thing Can rest, or hope, or pleasure bring?”
- **Translation**: 

---

### Verse 6 (Ramayan 0.586)
- **Original**: 568 The Ramayana Thus the sad town, which Ráma kept As a kind father, wailed and wept. Each mansion, as the car went by, Sent forth a loud and bitter cry, As to the window every dame, Mourning for banished Ráma, came. As his sad eyes with tears o'erflowed, He sped along the royal road To Da[aratha's high abode. There leaping down his car he stayed; Within the gates his way he made; Through seven broad courts he onward hied Where people thronged on every side. From each high terrace, wild with woe, The royal ladies flocked below:[163] He heard them talk in gentle tone, As each for Ráma made her moan: “What will the charioteer reply To Queen Kau[alyá's eager cry? With Ráma from the gates he went; Homeward alone, his steps are bent. Hard is a life with woe distressed, But difficult to win is rest, If, when her son is banished, still She lives beneath her load of ill.” Such was the speech Sumantra heard From them whom grief unfeigned had stirred. As fires of anguish burnt him through, Swift to the monarch's hall he drew, Past the eighth court; there met his sight, The sovereign in his palace bright, Still weeping for his son, forlorn, Pale, faint, and all with sorrow worn.
- **Translation**: 

---

### Verse 7 (Ramayan 0.587)
- **Original**: Canto LVII. Sumantra's Return. 569 As there he sat, Sumantra bent And did obeisance reverent, And to the king repeated o'er The message he from Ráma bore. The monarch heard, and well-nigh brake His heart, but yet no word he spake: Fainting to earth he fell, and dumb, By grief for Ráma overcome. Rang through the hall a startling cry, And women's arms were tossed on high, When, with his senses all astray, Upon the ground the monarch lay. Kau [alyá, with Sumitrá's aid, Raised from the ground her lord dismayed: “Sire, of high fate,” she cried,“O, why Dost thou no single word reply To Ráma's messenger who brings News of his painful wanderings? The great injustice done, art thou Shame-stricken for thy conduct now? Rise up, and do thy part: bestow Comfort and help in this our woe. Speak freely, King; dismiss thy fear, For Queen Kaikeyí stands not near, Afraid of whom thou wouldst not seek Tidings of Ráma: freely speak.” When the sad queen had ended so, She sank, insatiate in her woe, And prostrate lay upon the ground, While her faint voice by sobs was drowned. When all the ladies in despair Saw Queen Kau[alyá wailing there, And the poor king oppressed with pain,
- **Translation**: 

---

### Verse 8 (Ramayan 0.588)
- **Original**: 570 The Ramayana They flocked around and wept again. Canto LVIII. Ráma's Message. The king a while had senseless lain, When care brought memory back again. Then straight he called, the news to hear Of Ráma, for the charioteer, With reverent hand to hand applied He waited by the old man's side, Whose mind with anguish was distraught Like a great elephant newly caught. The king with bitter pain distressed The faithful charioteer addressed, Who, sad of mien, with flooded eye, And dust upon his limbs, stood by: “Where will be Ráma's dwelling now At some tree's foot, beneath the bough; Ah, what will be the exile's food, Bred up with kind solicitude? Can he, long lapped in pleasant rest, Unmeet for pain, by pain oppressed, Son of earth's king, his sad night spend Earth-couched, as one that has no friend? Behind him, when abroad he sped, Cars, elephant, and foot were led: Then how shall Ráma dwell afar In the wild woods where no men are? How, tell me, did the princes there, With Sítá good and soft and fair, Alighting from the chariot, tread
- **Translation**: 

---

### Verse 9 (Ramayan 0.589)
- **Original**: Canto LVIII. Ráma's Message. 571 The forest wilds around them spread? A happy lot is thine, I ween, Whose eyes my two dear sons have seen Seeking on foot the forest shade, Like the bright Twins to view displayed, The heavenly A[vins, when they seek The woods that hang 'neath Mandar's peak. What words, Sumantra, quickly tell, From Ráma, LakshmaG, Sítá fell? How in the wood did Ráma eat? What was his bed, and what his seat? Full answer to my questions give, For I on thy replies shall live, As with the saints Yayáti held Sweet converse, from the skies expelled.” Urged by the lord of men to speak, Whose sobbing voice came faint and weak, Thus he, while tears his utterance broke, In answer to the monarch spoke: “Hear then the words that Ráma said, Resolved in duty's path to tread. Joining his hands, his head he bent, And gave this message, reverent: “Sumantra, to my father go, Whose lofty mind all people know: Bow down before him, as is meet, And in my stead salute his feet. Then to the queen my mother bend, And give the greeting that I send: Ne'er may her steps from duty err, And may it still be well with her. And add this word:“O Queen, pursue Thy vows with faithful heart and true;
- **Translation**: 

---

### Verse 10 (Ramayan 0.590)
- **Original**: 572 The Ramayana And ever at due season turn Where holy fires of worship burn. And, lady, on our lord bestow[164] Such honour as to Gods we owe. Be kind to every queen: let pride And thought of self be cast aside. In the king's fond opinion raise Kaikeyí, by respect and praise. Let the young Bharat ever be Loved, honoured as the king by thee: Thy king-ward duty ne'er forget: High over all are monarchs set.” And Bharat, too, for me address: Pray that all health his life may bless. Let every royal lady share, As justice bids, his love and care. Say to the strong-armed chief who brings Joy to Iksváku's line of kings: “As ruling prince thy care be shown Of him, our sire, who holds the throne. Stricken in years he feels their weight; But leave him in his royal state. As regent heir content thee still, Submissive to thy father's will.’ ” Ráma again his charge renewed, As the hot flood his cheek bedewed: “Hold as thine own my mother dear Who drops for me the longing tear.” Then LakshmaG, with his soul on fire, Spake breathing fast these words of ire: “Say, for what sin, for what offence Was royal Ráma banished thence? He is the cause, the king: poor slave
- **Translation**: 

---

### Verse 11 (Ramayan 0.591)
- **Original**: Canto LVIII. Ráma's Message. 573 To the light charge Kaikeyí gave. Let right or wrong the motive be, The author of our woe is he. Whether the exile were decreed Through foolish faith or guilty greed, For promises or empire, still The king has wrought a grievous ill. Grant that the Lord of all saw fit To prompt the deed and sanction it, In Ráma's life no cause I see For which the king should bid him flee. His blinded eyes refused to scan The guilt and folly of the plan, And from the weakness of the king Here and hereafter woe shall spring. No more my sire: the ties that used To bind me to the king are loosed. My brother Ráma, Raghu's son, To me is lord, friend, sire in one. The love of men how can he win, Deserting, by the cruel sin, Their joy, whose heart is swift to feel A pleasure in the people's weal? Shall he whose mandate could expel The virtuous Ráma, loved so well, To whom his subjects' fond hearts cling— Shall he in spite of them be king?” But Janak's child, my lord, stood by, And oft the votaress heaved a sigh. She seemed with dull and wandering sense, Beneath a spirit's influence. The noble princess, pained with woe Which till that hour she ne'er could know,
- **Translation**: 

---

### Verse 12 (Ramayan 0.592)
- **Original**: 574 The Ramayana Tears in her heavy trouble shed, But not a word to me she said. She raised her face which grief had dried And tenderly her husband eyed, Gazed on him as he turned to go While tear chased tear in rapid flow.” Canto LIX. Dasaratha's Lament. As thus Sumantra, best of peers, Told his sad tale with many tears, The monarch cried,“I pray thee, tell At length again what there befell.” Sumantra, at the king's behest, Striving with sobs he scarce repressed, His trembling voice at last controlled, And thus his further tidings told: “Their locks in votive coils they wound, Their coats of bark upon them bound, To Gangá's farther shore they went, Thence to Prayág their steps were bent. I saw that LakshmaG walked ahead To guard the path the two should tread. So far I saw, no more could learn, Forced by the hero to return. Retracing slow my homeward course, Scarce could I move each stubborn horse: Shedding hot tears of grief he stood
- **Translation**: 

---

### Verse 13 (Ramayan 0.593)
- **Original**: Canto LIX. Dasaratha's Lament. 575 When Ráma turned him to the wood.333 As the two princes parted thence I raised my hands in reverence, Mounted my ready car, and bore The grief that stung me to the core. With Guha all that day I stayed, Still by the earnest hope delayed That Ráma, ere the time should end, Some message from the wood might send. Thy realms, great Monarch, mourn the blow, And sympathize with Ráma's woe. [165] Each withering tree hangs low his head, And shoot, and bud, and flower are dead. Dried are the floods that wont to fill The lake, the river, and the rill. Drear is each grove and garden now, Dry every blossom on the bough. Each beast is still, no serpents crawl: A lethargy of woe on all. The very wood is silent: crushed With grief for Ráma, all is hushed. Fair blossoms from the water born, Gay garlands that the earth adorn, And every fruit that gleams like gold, Have lost the scent that charmed of old. Empty is every grove I see, 333 “So in Homer the horses of Achilles lamented with many bitter tears the death of Patroclus slain by Hector:” “=ÀÀ¿¹ ´'0±ºw´±¿,¼qÇ·Â Àq½µÅ¸µ½ yÄµÂ, »¶¹¿½,Àµ¹´t ÀÁöÄ± ÀÅ¸sÃ¸·½ !½¹yÇ¿¹¿ ½ º¿½w½Ã¹ ÀµÃy½Ä¿Â QÆ' ºÄ¿Á¿Â ½´Á¿Æy½¿¹¿” ILIAD .{FNS XVII. 426. “Ancient poesy frequently associated nature with the joys and sorrows of man.” G ORRESIO .{FNS
- **Translation**: 

---

### Verse 14 (Ramayan 0.594)
- **Original**: 576 The Ramayana Or birds sit pensive on the tree. Where'er I look, its beauty o'er, The pleasance charms not as before. I drove through fair Ayodhyá's street: None flew with joy the car to meet. They saw that Ráma was not there, And turned them sighing in despair. The people in the royal way Wept tears of bitter grief, when they Beheld me coming, from afar, No Ráma with me in the car. From palace roof and turret high Each woman bent her eager eye; She looked for Ráma, but in vain; Gazed on the car and shrieked for pain. Their long clear eyes with sorrow drowned They, when this common grief was found, Looked each on other, friend and foe, In sympathy of levelling woe: No shade of difference between Foe, friend, or neutral, there was seen. Without a joy, her bosom rent With grief for Ráma's banishment, Ayodhyá like the queen appears Who mourns her son with many tears.”
- **Translation**: 

---

### Verse 15 (Ramayan 0.595)
- **Original**: Canto LIX. Dasaratha's Lament. 577 He ended: and the king, distressed. With sobbing voice that lord addressed: “Ah me, by false Kaikeyí led, Of evil race, to evil bred, I took no counsel of the sage, Nor sought advice from skill and age, I asked no lord his aid to lend, I called no citizen or friend. Rash was my deed, bereft of sense Slave to a woman's influence. Surely, my lord, a woe so great Falls on us by the will of Fate; It lays the house of Raghu low, For Destiny will have it so. I pray thee, if I e'er have done An act to please thee, yea, but one, Fly, fly, and Ráma homeward lead: My life, departing, counsels speed. Fly, ere the power to bid I lack, Fly to the wood: bring Ráma back. I cannot live for even one Short hour bereaved of my son. But ah, the prince, whose arms are strong, Has journeyed far: the way is long: Me, me upon the chariot place, And let me look on Ráma's face. Ah me, my son, mine eldest-born, Where roams he in the wood forlorn, The wielder of the mighty bow, Whose shoulders like the lion's show? O, ere the light of life be dim, Take me to Sítá and to him. O Ráma, LakshmaG, and O thou Dear Sítá, constant to thy vow,
- **Translation**: 

---

### Verse 16 (Ramayan 0.596)
- **Original**: 578 The Ramayana Beloved ones, you cannot know That I am dying of my woe.” The king to bitter grief a prey, That drove each wandering sense away, Sunk in affliction's sea, too wide To traverse, in his anguish cried: “Hard, hard to pass, my Queen, this sea Of sorrow raging over me: No Ráma near to soothe mine eye, Plunged in its lowest deeps I lie. Sorrow for Ráma swells the tide, And Sítá's absence makes it wide: My tears its foamy flood distain, Made billowy by my sighs of pain: My cries its roar, the arms I throw About me are the fish below, Kaikeyí is the fire that feeds Beneath: my hair the tangled weeds: Its source the tears for Ráma shed: The hump-back's words its monsters dread: The boon I gave the wretch its shore, Till Ráma's banishment be o'er.334 Ah me, that I should long to set My eager eyes to-day On Raghu's son, and he be yet With LakshmaG far away!” Thus he of lofty glory wailed, And sank upon the bed. Beneath the woe his spirit failed, And all his senses fled. 334 The lines containing this heap of forced metaphors are marked as spurious by Schlegel.
- **Translation**: 

---

### Verse 17 (Ramayan 0.597)
- **Original**: Canto LX. Kausalyá Consoled. 579 Canto LX. Kausalyá Consoled. As Queen Kau[alyá, trembling much, As blighted by a goblin's touch, Still lying prostrate, half awoke To consciousness, 'twas thus she spoke: “Bear me away, Sumantra, far, Where Ráma, Sítá, LakshmaG are. Bereft of them I have no power To linger on a single hour. [166] Again, I pray, thy steps retrace, And me in DaG ak forest place, For after them I needs must go, Or sink to Yama's realms below.” His utterance choked by tears that rolled Down from their fountains uncontrolled, With suppliant hands the charioteer Thus spake, the lady's heart to cheer: “Dismiss thy grief, despair, and dread That fills thy soul, of sorrow bred, For pain and anguish thrown aside, Will Ráma in the wood abide. And Lakshma G, with unfailing care Will guard the feet of Ráma there, Earning, with governed sense, the prize That waits on duty in the skies. And Sítá in the wild as well As in her own dear home will dwell; To Ráma all her heart she gives, And free from doubt and terror lives. No faintest sign of care or woe The features of the lady show: Methinks Videha's pride was made
- **Translation**: 

---

### Verse 18 (Ramayan 0.598)
- **Original**: 580 The Ramayana For exile in the forest shade. E'en as of old she used to rove Delighted in the city's grove, Thus, even thus she joys to tread The woodlands uninhabited. Like a young child, her face as fair As the young moon, she wanders there. What though in lonely woods she stray Still Ráma is her joy and stay: All his the heart no sorrow bends, Her very life on him depends. For, if her lord she might not see, Ayodhyá like the wood would be. She bids him, as she roams, declare The names of towns and hamlets there, Marks various trees that meet her eye, And many a brook that hurries by, And Janak's daughter seems to roam One little league away from home When Ráma or his brother speaks And gives the answer that she seeks. This, Lady, I remember well, Nor angry words have I to tell: Reproaches at Kaikeyí shot, Such, Queen, my mind remembers not.” The speech when Sítá's wrath was high, Sumantra passed in silence by, That so his pleasant words might cheer With sweet report Kau[alyá's ear. “Her moonlike beauty suffers not Though winds be rude and suns be hot: The way, the danger, and the toil Her gentle lustre may not soil. Like the red lily's leafy crown
- **Translation**: 

---

### Verse 19 (Ramayan 0.599)
- **Original**: Canto LX. Kausalyá Consoled. 581 Or as the fair full moon looks down, So the Videhan lady's face Still shines with undiminished grace. What if the borrowed colours throw O'er her fine feet no rosy glow, Still with their natural tints they spread A lotus glory where they tread. In sportive grace she walks the ground And sweet her chiming anklets sound. No jewels clasp the faultless limb: She leaves them all for love of him. If in the woods her gentle eye A lion sees, or tiger nigh, Or elephant, she fears no ill For Ráma's arm supports her still. No longer be their fate deplored, Nor thine, nor that of Ko[al's lord, For conduct such as theirs shall buy Wide glory that can never die. For casting grief and care away, Delighting in the forest, they With joyful spirits, blithe and gay, Set forward on the ancient way Where mighty saints have led: Their highest aim, their dearest care To keep their father's honour fair, Observing still the oath he sware, They roam, on wild fruit fed.” Thus with persuasive art he tried To turn her from her grief aside, By soothing fancies won. But still she gave her sorrow vent: “Ah Ráma,” was her shrill lament, “My love, my son, my son!”
- **Translation**: 

---

### Verse 20 (Ramayan 0.600)
- **Original**: 582 The Ramayana Canto LXI. Kausalyá's Lament. When, best of all who give delight, Her Ráma wandered far from sight, Kau [alyá weeping, sore distressed, The king her husband thus addressed: “Thy name, O Monarch, far and wide Through the three worlds is glorified: Yet Ráma's is the pitying mind, His speed is true, his heart is kind. How will thy sons, good lord, sustain With Sítá, all their care and pain? How in the wild endure distress, Nursed in the lap of tenderness? How will the dear Videhan bear The heat and cold when wandering there Bred in the bliss of princely state, So young and fair and delicate? The large-eyed lady, wont to eat The best of finely seasoned meat— How will she now her life sustain With woodland fare of self-sown grain? Will she, with joys encompassed long, Who loved the music and the song, In the wild wood endure to hear The ravening lion's voice of fear? Where sleeps my strong-armed hero, where,[167] Like Lord Mahendra's standard, fair? Where is, by LakshmaG's side, his bed, His club-like arm beneath his head? When shall I see his flower-like eyes, And face that with the lotus vies, Feel his sweet lily breath, and view His glorious hair and lotus hue?
- **Translation**: 

---

