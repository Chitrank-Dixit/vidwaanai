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

### Verse 1 (Ramayana 0.946)
- **Original**: 928 The Ramayana E'en as a Bráhman's dame, unwise, Eats of the fallen hail475 and dies.[263] Thy hand has slain the pure and good, The hermit saints of DaG ak wood, Of holy life, the heirs of bliss; And thou shalt reap the fruit of this. Not long shall they whose cruel breasts Joy in the sin the world detests Retain their guilty power and pride, But fade like trees whose roots are dried. Yes, as the seasons come and go, Each tree its kindly fruit must show, And sinners reap in fitting time The harvest of each earlier crime. As those must surely die who eat Unwittingly of poisoned meat, They too whose lives in sin are spent Receive ere long the punishment. And know, thou rover of the night, That I, a king, am sent to smite The wicked down, who court the hate Of men whose laws they violate. This day my vengeful hand shall send Shafts bright with gold to tear and rend, And pass with fury through thy breast As serpents pierce an emmet's nest. Thou with thy host this day shalt be Among the dead below, and see The saints beneath thy hand who bled, Whose flesh thy cruel maw has fed. They, glorious on their seats of gold, Their slayer shall in hell behold. 475 Popularly supposed to cause death.
- **Translation**: 

---

### Verse 2 (Ramayana 0.947)
- **Original**: Canto XXIX. Khara's Defeat. 929 Fight with all strength thou callest thine, Mean scion of ignoble line, Still, like the palm-tree's fruit, this day My shafts thy head in dust shall lay.” Such were the words that Ráma said: Then Khara's eyes with wrath glowed red, Who, maddened by the rage that burned Within him, with a smile returned: “Thou Da[aratha's son, hast slain The meaner giants of my train: And canst thou idly vaunt thy might And claim the praise not thine by right? Not thus in self-laudation rave The truly great, the nobly brave: No empty boasts like thine disgrace The foremost of the human race. The mean of soul, unknown to fame, Who taint their warrior race with shame, Thus speak in senseless pride as thou, O Raghu's son, hast boasted now. What hero, when the war-cry rings, Vaunts the high race from which he springs, Or seeks, when warriors meet and die, His own descent to glorify? Weakness and folly show confessed In every vaunt thou utterest, As when the flames fed high with grass Detect the simulating brass. Dost thou not see me standing here Armed with the mighty mace I rear, Firm as an earth upholding hill Whose summit veins of metal fill?
- **Translation**: 

---

### Verse 3 (Ramayana 0.948)
- **Original**: 930 The Ramayana Lo, here I stand before thy face To slay thee with my murderous mace, As Death, the universal lord, Stands threatening with his fatal cord. Enough of this. Much more remains That should be said: but time constrains. Ere to his rest the sun descend, And shades of night the combat end, The twice seven thousand of my band Who fell beneath thy bloody hand Shall have their tears all wiped away And triumph in thy fall to-day.” He spoke, and loosing from his hold His mighty mace ringed round with gold, Like some red bolt alive with fire Hurled it at Ráma, mad with ire. The ponderous mace which Khara threw Sent fiery flashes as it flew. Trees, shrubs were scorched beneath the blast, As onward to its aim it passed. But Ráma, watching as it sped Dire as His noose who rules the dead, Cleft it with arrows as it came On rushing with a hiss and flame. Its fury spent and burnt away, Harmless upon the ground it lay Like a great snake in furious mood By herbs of numbing power subdued.
- **Translation**: 

---

### Verse 4 (Ramayana 0.949)
- **Original**: Canto XXX. Khara's Death. 931 Canto XXX. Khara's Death. When Ráma, pride of Raghu's race, Virtue's dear son, had cleft the mace, Thus with superior smile the best Of chiefs the furious fiend addressed: “Thou, worst of giant blood, at length Hast shown the utmost of thy strength, And forced by greater might to bow, Thy vaunting threats are idle now. My shafts have cut thy club in twain: Useless it lies upon the plain, And all thy pride and haughty trust Lie with it levelled in the dust. The words that thou hast said to-day, That thou wouldst wipe the tears away Of all the giants I have slain, My deeds shall render void and vain. Thou meanest of the giants' breed, Evil in thought and word and deed, My hand shall take that life of thine As Garu 476 seized the juice divine. [264] Thou, rent by shafts, this day shalt die: Low on the ground thy corse shall lie, And bubbles from the cloven neck With froth and blood thy skin shall deck. With dust and mire all rudely dyed, Thy torn arms lying by thy side, While streams of blood each limb shall steep, Thou on earth's breast shalt take thy sleep 476 Garu , the King of Birds, carried off the Amrit or drink of Paradise from Indra's custody.
- **Translation**: 

---

### Verse 5 (Ramayana 0.950)
- **Original**: 932 The Ramayana Like a fond lover when he strains The beauty whom at length he gains. Now when thy heavy eyelids close For ever in thy deep repose, Again shall DaG ak forest be Safe refuge for the devotee. Thou slain, and all thy race who held The realm of Janasthán expelled, Again shall happy hermits rove, Fearing no danger, through the grove. Within those bounds, their brethren slain, No giant shall this day remain, But all shall fly with many a tear And fearing, rid the saints of fear. This bitter day shall misery bring On all the race that calls thee king. Fierce as their lord, thy dames shall know, Bereft of joys, the taste of woe. Base, cruel wretch, of evil mind, Plaguer of Bráhmans and mankind, With trembling hands each devotee Feeds holy fires in dread of thee.” Thus with wild fury unrepressed Raghu's brave son the fiend addressed; And Khara, as his wrath grew high, Thus thundered forth his fierce reply: “By senseless pride to madness wrought, By danger girt thou fearest naught, Nor heedest, numbered with the dead, What thou shouldst say and leave unsaid. When Fate's tremendous coils enfold The captive in resistless hold,
- **Translation**: 

---

### Verse 6 (Ramayana 0.951)
- **Original**: Canto XXX. Khara's Death. 933 He knows not right from wrong, each sense Numbed by that deadly influence.” He spoke, and when his speech was done Bent his fierce brows on Raghu's son. With eager eyes he looked around If lethal arms might yet be found. Not far away and full in view A Sál-tree towering upward grew. His lips in mighty strain compressed, He tore it up with root and crest, With huge arms waved it o'er his head And hurled it shouting, Thou art dead. But Ráma, unsurpassed in might, Stayed with his shafts its onward flight, And furious longing seized his soul The giant in the dust to roll. Great drops of sweat each limb bedewed, His red eyes showed his wrathful mood. A thousand arrows, swiftly sent, The giant's bosom tore and rent. From every gash his body showed The blood in foamy torrents flowed, As springing from their caverns leap Swift rivers down the mountain steep. When Khara felt each deadened power Yielding beneath that murderous shower, He charged, infuriate with the scent Of blood, in dire bewilderment. But Ráma watched, with ready bow, The onset of his bleeding foe, And ere the monster reached him, drew Backward in haste a yard or two. Then from his side a shaft he took
- **Translation**: 

---

### Verse 7 (Ramayana 0.952)
- **Original**: 934 The Ramayana Whose mortal stroke no life might brook: Of peerless might, it bore the name Of Brahmá's staff, and glowed with flame: Lord Indra, ruler of the skies, Himself had given the glorious prize. His bow the virtuous hero drew, And at the fiend the arrow flew. Hissing and roaring like the blast Of tempest through the air it passed, And fixed, by Ráma's vigour sped, In the foe's breast its pointed head. Then fell the fiend: the quenchless flame Burnt furious in his wounded frame. So burnt by Rudra Andhak477 fell InZvetáraGya's silvery dell: So Namuchi and Vritra478 died By steaming bolts that tamed their pride: So Bala479 fell by lightning sent By Him who rules the firmament. Then all the Gods in close array With the bright hosts who sing and play, Filled full of rapture and amaze, Sang hymns of joy in Ráma's praise, Beat their celestial drums and shed Rain of sweet flowers upon his head. For three short hours had scarcely flown, And by his pointed shafts o'erthrown The twice seven thousand fiends, whose will 477 A demon, son of Ka[yap and Diti, slain by Rudra orZiva when he attempted to carry off the tree of Paradise. 478 Namuchi and Vritra were two demons slain by Indra. Vritra personifies drought, the enemy of Indra, who imprisons the rain in the cloud. 479 Another demon slain by Indra.
- **Translation**: 

---

### Verse 8 (Ramayana 0.953)
- **Original**: Canto XXX. Khara's Death. 935 Could change their shapes, in death were still, With Tri[irás and DúshaG slain, And Khara, leader of the train. “O wondrous deed,” the bards began, “The noblest deed of virtuous man! Heroic strength that stood alone, And firmness e'en as VishGu's own!” Thus having sung, the shining train Turned to their heavenly homes again. [265] Then the high saints of royal race And loftiest station sought the place, And by the great Agastya led, With reverence to Ráma said: “For this, Lord Indra, glorious sire, Majestic as the burning fire, Who crushes cities in his rage, SoughtZarabhanga's hermitage. Thou wast, this great design to aid, Led by the saints to seek this shade, And with thy mighty arm to kill The giants who delight in ill. Thou Da[aratha's noble son, The battle for our sake hast won, And saints in DaG ak's wild who live Their days to holy tasks can give.”
- **Translation**: 

---

### Verse 9 (Ramayana 0.954)
- **Original**: 936 The Ramayana Forth from the mountain cavern came The hero LakshmaG with the dame. And rapture beaming from his face, Resought the hermit dwelling-place. Then when the mighty saints had paid Due honour for the victor's aid, The glorious Ráma honoured too By LakshmaG to his cot withdrew. When Sítá looked upon her lord, His foemen slain, the saints restored, In pride and rapture uncontrolled She clasped him in her loving hold. On the dead fiends her glances fell: She saw her lord alive and well, Victorious after toil and pain, And Janak's child was blest again. Once more, once more with new delight Her tender arms she threw Round Ráma whose victorious might Had crushed the demon crew. Then as his grateful reverence paid Each saint of lofty soul, O'er her sweet face, all fears allayed, The flush of transport stole. Canto XXXI. Rávan. But of the host of giants one, Akampan, from the field had run And sped to Lanká480 to relate 480 The capital of the giant king RávaG.
- **Translation**: 

---

### Verse 10 (Ramayana 0.955)
- **Original**: Canto XXXI. Rávan. 937 In RávaG's ear the demons' fate: “King, many a giant from the shade Of Janasthán in death is laid: Khara the chief is slain, and I Could scarcely from the battle fly.” Fierce anger, as the monarch heard, Inflamed his look, his bosom stirred, And while with scorching glance he eyed The messenger, he thus replied: “What fool has dared, already dead, Strike Janasthán, the general dread? Who is the wretch shall vainly try In earth, heaven, hell, from me to fly? Vai[ravaG,481 Indra, VishGu, He Who rules the dead, must reverence me; For not the mightiest lord of these Can brave my will and live at ease. Fate finds in me a mightier fate To burn the fires that devastate. With unresisted influence I Can force e'en Death himself to die, With all-surpassing might restrain The fury of the hurricane, And burn in my tremendous ire The glory of the sun and fire.” 481 Kuvera, the God of gold.
- **Translation**: 

---

### Verse 11 (Ramayana 0.956)
- **Original**: 938 The Ramayana As thus the fiend's hot fury blazed, His trembling hands Akampan raised, And with a voice which fear made weak, Permission craved his tale to speak. King RávaG gave the leave he sought, And bade him tell the news he brought. His courage rose, his voice grew bold, And thus his mournful tale he told: “A prince with mighty shoulders, sprung From Da[aratha, brave and young, With arms well moulded, bears the name Of Ráma with a lion's frame. Renowned, successful, dark of limb, Earth has no warrior equals him. He fought in Janasthán and slew DúshaG the fierce and Khara too.” RávaG the giants' royal chief. Received Akampan's tale of grief. Then, panting like an angry snake, These words in turn the monarch spake: “Say quick, did Ráma seek the shade Of Janasthán with Indra's aid, And all the dwellers in the skies To back his hardy enterprise?” Akampan heard, and straight obeyed His master, and his answer made. Then thus the power and might he told Of Raghu's son the lofty-souled:
- **Translation**: 

---

### Verse 12 (Ramayana 0.957)
- **Original**: Canto XXXI. Rávan. 939 “Best is that chief of all who know With deftest art to draw the bow. His are strange arms of heavenly might, And none can match him in the fight. His brother LakshmaG brave as he, Fair as the rounded moon to see, With eyes like night and voice that comes Deep as the roll of beaten drums, By Ráma's side stands ever near, Like wind that aids the flame's career. That glorious chief, that prince of kings, On Janasthán this ruin brings. No Gods were there,— dismiss the thought No heavenly legions came and fought. His swift-winged arrows Ráma sent, Each bright with gold and ornament. To serpents many-faced they turned: [266] The giant hosts they ate and burned. Where'er these fled in wild dismay Ráma was there to strike and slay. By him O King of high estate, Is Janasthán left desolate.” Akampan ceased: in angry pride The giant monarch thus replied: “To Janasthán myself will go And lay these daring brothers low.” Thus spoke the king in furious mood: Akampan then his speech renewed: “O listen while I tell at length The terror of the hero's strength. No power can check, no might can tame Ráma, a chief of noblest fame.
- **Translation**: 

---

### Verse 13 (Ramayana 0.958)
- **Original**: 940 The Ramayana He with resistless shafts can stay The torrent foaming on its way. Sky, stars, and constellations, all To his fierce might would yield and fall. His power could earth itself uphold Down sinking as it sank of old.482 Or all its plains and cities drown, Breaking the wild sea's barrier down; Crush the great deep's impetuous will, Or bid the furious wind be still. He glorious in his high estate The triple world could devastate, And there, supreme of men, could place His creatures of a new-born race. Never can mighty Ráma be O'ercome in fight, my King, by thee. Thy giant host the day might win From him, if heaven were gained by sin. If Gods were joined with demons, they Could ne'er, I ween, that hero slay, But guile may kill the wondrous man; Attend while I disclose the plan. His wife, above all women graced, Is Sítá of the dainty waist, With limbs to fair proportion true, And a soft skin of lustrous hue, Round neck and arm rich gems are twined: She is the gem of womankind. With her no bright Gandharví vies, No nymph or Goddess in the skies; And none to rival her would dare 'Mid dames who part the long black hair. 482 In the great deluge.
- **Translation**: 

---

### Verse 14 (Ramayana 0.959)
- **Original**: Canto XXXI. Rávan. 941 That hero in the wood beguile, And steal his lovely spouse the while. Reft of his darling wife, be sure, Brief days the mourner will endure.” With flattering hope of triumph moved The giant king that plan approved, Pondered the counsel in his breast, And then Akampan thus addressed: “Forth in my car I go at morn, None but the driver with me borne, And this fair Sítá will I bring Back to my city triumphing.” Forth in his car by asses drawn The giant monarch sped at dawn, Bright as the sun, the chariot cast Light through the sky as on it passed. Then high in air that best of cars Traversed the path of lunar stars, Sending a fitful radiance pale As moonbeams shot through cloudy veil. Far on his airy way he flew: Near Tá akeya's483 grove he drew. Márícha welcomed him, and placed Before him food which giants taste, With honour led him to a seat, And brought him water for his feet; And then with timely words addressed Such question to his royal guest: 483 The giant Márícha, son of Tá aká. Tá aká was slain by Ráma. See p. 39.
- **Translation**: 

---

### Verse 15 (Ramayana 0.960)
- **Original**: 942 The Ramayana “Speak, is it well with thee whose sway The giant multitudes obey? I know not all, and ask in fear The cause, O King, why thou art here.” Ráva, the giants' mighty king, Heard wise Márícha's questioning, And told with ready answer, taught In eloquence, the cause he sought: “My guards, the bravest of my band, Are slain by Ráma's vigorous hand, And Janasthán, that feared no hate Of foes, is rendered desolate. Come, aid me in the plan I lay To steal the conqueror's wife away.” Márícha heard the king's request, And thus the giant chief addressed: “What foe in friendly guise is he Who spoke of Sítá's name to thee? Who is the wretch whose thought would bring Destruction on the giants' king? Whose is the evil counsel, say, That bids thee bear his wife away, And careless of thy life provoke Earth's loftiest with threatening stroke? A foe is he who dared suggest This hopeless folly to thy breast, Whose ill advice would bid thee draw The venomed fang from serpent's jaw. By whose unwise suggestion led Wilt thou the path of ruin tread? Whence falls the blow that would destroy Thy gentle sleep of ease and joy?
- **Translation**: 

---

### Verse 16 (Ramayana 0.961)
- **Original**: Canto XXXI. Rávan. 943 Like some wild elephant is he That rears his trunk on high, Lord of an ancient pedigree, Huge tusks, and furious eye. RávaG, no rover of the night With bravest heart can brook, Met in the front of deadly fight, On Raghu's son to look. [267] The giant hosts were brave and strong, Good at the bow and spear: But Ráma slew the routed throng, A lion 'mid the deer. No lion's tooth can match his sword, Or arrows fiercely shot: He sleeps, he sleeps— the lion lord; Be wise and rouse him not. O Monarch of the giants, well Upon my counsel think, Lest thou for ever in the hell Of Ráma's vengeance sink: A hell, where deadly shafts are sent From his tremendous-bow, While his great arms all flight prevent, Like deepest mire below: Where the wild floods of battle rave Above the foeman's head, And each with many a feathery wave Of shafts is garlanded. O, quench the flames that in thy breast With raging fury burn; And pacified and self-possessed To Lanká's town return. Rest thou in her imperial bowers With thine own wives content,
- **Translation**: 

---

### Verse 17 (Ramayana 0.962)
- **Original**: 944 The Ramayana And in the wood let Ráma's hours With Sítá still be spent.” The lord of Lanká's isle obeyed The counsel, and his purpose stayed. Borne on his car he parted thence And gained his royal residence. Canto XXXII. Rávan Roused. But ZúrpaGakhá saw the plain Spread with the fourteen thousand slain, Doers of cruel deeds o'erthrown By Ráma's mighty arm alone, Add Tri[irás and DúshaG dead, And Khara, with the hosts they led. Their death she saw, and mad with pain, Roared like a cloud that brings the rain, And fled in anger and dismay To Lanká, seat of RávaG's sway. There on a throne of royal state Exalted sat the potentate, Begirt with counsellor and peer, Like Indra with the Storm Gods near. Bright as the sun's full splendour shone The glorious throne he sat upon, As when the blazing fire is red Upon a golden altar fed. Wide gaped his mouth at every breath, Tremendous as the jaws of Death. With him high saints of lofty thought,
- **Translation**: 

---

### Verse 18 (Ramayana 0.963)
- **Original**: Canto XXXII. Rávan Roused. 945 Gandharvas, Gods, had vainly fought. The wounds were on his body yet From wars where Gods and demons met. And scars still marked his ample chest By fierce Airávat's484 tusk impressed. A score of arms, ten necks, had he, His royal gear was brave to see. His massive form displayed each sign That marks the heir of kingly line. In stature like a mountain height, His arms were strong, his teeth were white, And all his frame of massive mould Seemed lazulite adorned with gold. A hundred seams impressed each limp Where VishGu's arm had wounded him, And chest and shoulder bore the print Of sword and spear and arrow dint, Where every God had struck a blow In battle with the giant foe. His might to wildest rage could wake The sea whose faith naught else can shake, Hurl towering mountains to the earth, And crush e'en foes of heavenly birth. The bonds of law and right he spurned: To others' wives his fancy turned. Celestial arms he used in fight, And loved to mar each holy rite. He went to Bhogavatí's town,485 Where Vásuki was beaten down, And stole, victorious in the strife, Lord Takshaka's beloved wife. 484 Indra's elephant. 485 Bhogavatí, in Pátála in the regions under the earth, is the capital of the serpent race whose king is Vásuki.
- **Translation**: 

---

### Verse 19 (Ramayana 0.964)
- **Original**: 946 The Ramayana Kailása's lofty crest he sought, And when in vain Kuvera fought, Stole Pushpak thence, the car that through The air, as willed the master, flew. Impelled by furious anger, he Spoiled Nandan's486 shade and Naliní, And Chaitraratha's heavenly grove, The haunts where Gods delight to rove. Tall as a hill that cleaves the sky, He raised his mighty arms on high To check the blessed moon, and stay The rising of the Lord of Day. Ten thousand years the giant spent On dire austerities intent, And of his heads an offering, laid Before the Self-existent, made. No God or fiend his life could take, Gandharva, goblin, bird, or snake: Safe from all fears of death, except From human arm, that life was kept. Oft when the priests began to raise Their consecrating hymns of praise, He spoiled the Soma's sacred juice Poured forth by them in solemn use.[268] The sacrifice his hands o'erthrew, And cruelly the Bráhmans slew. His was a heart that naught could melt, Joying in woes which others felt. She saw the ruthless monster there, Dread of the worlds, unused to spare. In robes of heavenly texture dressed, Celestial wreaths adorned his breast. 486 the grove of Indra.
- **Translation**: 

---

### Verse 20 (Ramayana 0.965)
- **Original**: Canto XXXIII. Súrpanakhá's Speech. 947 He sat a shape of terror, like Destruction ere the worlds it strike. She saw him in his pride of place, The joy of old Pulastya's487 race, Begirt by counsellor and peer, RávaG, the foeman's mortal fear, And terror in her features shown, The giantess approached the throne. Then ZúrpaGakhá bearing yet Each deeply printed trace Where the great-hearted chief had set A mark upon her face, Impelled by terror and desire, Still fierce, no longer bold, To RávaG of the eyes of fire Her tale, infuriate, told. Canto XXXIII. Súrpanakhá's Speech. Burning with anger, in the ring Of counsellors who girt their king, To RávaG, ravener of man, With bitter words she thus began: 487 Pulastya is considered as the ancestor of the Rakshases or giants, as he is the father of Vi[ravas, the father of RávaG and his brethren.
- **Translation**: 

---

