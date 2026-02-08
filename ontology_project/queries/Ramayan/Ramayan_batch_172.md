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

### Verse 1 (Ramayana 0.1466)
- **Original**: 1448 The Ramayana I saw a chariot high in air, Of ivory exceeding fair. A hundred steeds that chariot drew As swiftly through the clouds it flew, And, clothed in white, with wreaths that shone, The sons of Raghu rode thereon. I looked and saw this lady here, Clad in the purest white, appear High on the snow white hill whose feet The angry waves of ocean beat. And she and Ráma met at last Like light and sun when night is past. Again I saw them side by side. On RávaG's car they seemed to ride, And with the princely LakshmaG flee To northern realms beyond the sea.[411] Then RávaG, shaved and shorn, besmeared With oil from head to foot, appeared. He quaffed, he raved: his robes were red: Fierce was his eye, and bare his head. I saw him from his chariot thrust; I saw him rolling in the dust. A woman came and dragged away The stricken giant where he lay, And on a car which asses drew The monarch of our race she threw. He rose erect, he danced and laughed, With thirsty lips the oil he quaffed, Then with wild eyes and streaming mouth Sped on the chariot to the south.844 Then, dropping oil from every limb, His sons the princes followed him, 844 In the south is the region of Yáma the God of Death, the place of departed spirits.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1467)
- **Original**: Canto XXX. Hanumán's Deliberation. 1449 And Kumbhakar Ga,845 shaved and shorn, Was southward on a camel borne. Then royal Lanká reeled and fell With gate and tower and citadel. This ancient city, far-renowned: All life within her walls was drowned; And the wild waves of ocean rolled O'er Lanká and her streets of gold. Warned by these signs I bid you fly; Or by the hand of Ráma die, Whose vengeance will not spare the life Of one who vexed his faithful wife. Your bitter taunts and threats forgo: Comfort the lady in her woe, And humbly pray her to forgive; For so you may be spared and live.” [I omit the 28th and 29th Cantos as an unmistakeable interpola- tion. Instead of advancing the story it goes back to Canto XVII, containing a lamentation of Sítá after RávaG has left her, and describes the the auspicious signs sent to cheer her, the throbbing of her left eye, arm, and side. The Canto is found in the Bengal recension. Gorresio translates it. and observes:“I think that Chapter XXVIII.— The Auspicious Signs— is an addition, a later interpolation by the Rhapsodists. It has no bond of connexion either with what precedes or follows it, and may be struck out not only without injury to, but positively to the advantage of the poem. The metre in which this chapter is written differs from that which is generally adopted in the course of the poem.”] Canto XXX. Hanumán's Deliberation. 845 Kumbhakar Ga was one of RávaG's brothers.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1468)
- **Original**: 1450 The Ramayana The Vánar watched concealed: each word Of Sítá and the fiends he heard, And in a maze of anxious thought His quick-conceiving bosom wrought. “At length my watchful eyes have seen, Pursued so long, the Maithil queen, Sought by our Vánar hosts in vain From east to west, from main to main. A cautious spy have I explored The palace of the Rákhshas lord, And thoroughly learned, concealed from sight, The giant monarch's power and might. And now my task must be to cheer The royal dame who sorrows here. For if I go, and soothe her not, A captive in this distant spot, She, when she finds no comfort nigh, Will sink beneath her woes and die. How shall my tale, if unconsoled I leave her, be to Ráma told? How shall I answer Raghu's son, “No message from my darling, none?” The husband's wrath, to fury fanned, Will scorch me lifeless where I stand, Or if I urge my lord the king To Lanká's isle his hosts to bring, In vain will be his zeal, in vain The toil, the danger, and the pain. Yea, this occasion must I seize That from her guard the lady frees,846 To win her ear with soft address And whisper hope in dire distress. 846 The guards are still in the grove, but they are asleep; and Sítá has crept to a tree at some distance from them.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1469)
- **Original**: Canto XXX. Hanumán's Deliberation. 1451 Shall I, a puny Vánar, choose The Sanskrit men delight to use? If, as a man of Bráhman kind, I speak the tongue by rules refined, The lady, yielding to her fears, Will think 'tis RávaG's voice she hears. I must assume my only plan— The language of a common847 man. Yet, if the lady sees me nigh, [412] In terror she will start and cry; And all the demon band, alarmed, Will come with various weapons armed, With their wild shouts the grove will fill, And strive to take me, or to kill. And, at my death or capture, dies The hope of Ráma`s enterprise. For none can leap, save only me, A hundred leagues across the sea. It is a sin in me, I own, To talk with Janak's child alone. Yet greater is the sin if I Be silent, and the lady die. First I will utter Ráma's name, And laud the hero's gifts and fame. Perchance the name she holds so dear 847 “As the reason assigned in these passages for not addressing Sítá in Sanskrit such as a Bráhman would use is not that she would not understand it, but that it would alarm her and be unsuitable to the speaker, we must take them as indicating that Sanskrit, if not spoken by women of the upper classes at the time when the RámáyaGa was written (whenever that may have been), was at least understood by them, and was commonly spoken by men of the priestly class, and other educated persons. By the Sanskrit proper to an [ordinary] man, alluded to in the second passage, may perhaps be understood not a language in which words different from Sanskrit were used, but the employment of formal and elaborate diction.” M UIR 'S{FNS Sanskrit Texts, Part II. p. 166.
- **Translation**: 

---

### Verse 5 (Ramayana 0.1470)
- **Original**: 1452 The Ramayana Will soothe the faithful lady's fear.” Canto XXXI. Hanumán's Speech. Then in sweet accents low and mild The Vánar spoke to Janak's child: “A noble king, by sin unstained, The mighty Da[aratha reigned. Lord of the warrior's car and steed, The pride of old Ikshváku's seed. A faithful friend, a blameless king, Protector of each living thing. A glorious monarch, strong to save, Blest with the bliss he freely gave. His son, the best of all who know The science of the bended bow, Was moon-bright Ráma, brave and strong, Who loved the right and loathed the wrong, Who ne'er from kingly duty swerved, Loved by the lands his might preserved. His feet the path of law pursued; His arm rebellious foes subdued. His sire's command the prince obeyed And, banished, sought the forest shade, Where with his wife and brother he Wandered a saintly devotee. There as he roamed the wilds he slew The bravest of the Rákshas crew. The giant king the prince beguiled, And stole his consort, Janak's child. Then Ráma roamed the country round,
- **Translation**: 

---

### Verse 6 (Ramayana 0.1471)
- **Original**: Canto XXXII. Sítá's Doubt. 1453 And a firm friend, Sugríva, found, Lord of the Vánar race, expelled From his own realm which Báli held, He conquered Báli and restored The kingdom to the rightful lord. Then by Sugríva's high decree The Vánar legions searched for thee, Sampáti's counsel bade me leap A hundred leagues across the deep. And now my happy eyes have seen At last the long-sought Maithil queen. Such was the form, the eye, the grace Of her whom Ráma bade me trace.” He ceased: her flowing locks she drew To shield her from a stranger's view; Then, trembling in her wild surprise, Raised to the tree her anxious eyes. Canto XXXII. Sítá's Doubt. Her eyes the Maithil lady raised And on the monkey speaker gazed. She looked, and trembling at the sight Wept bitter tears in wild affright. She shrank a while with fear distraught, Then, nerved again, the lady thought: “Is this a dream mine eyes have seen, This creature, by our laws unclean? O, may the Gods keep Ráma, still, And Lakshma G, and my sire, from ill!
- **Translation**: 

---

### Verse 7 (Ramayana 0.1472)
- **Original**: 1454 The Ramayana It is no dream: I have not slept, But, trouble-worn, have watched and wept Afar from that dear lord of mine For whom in ceaseless woe I pine, No art may soothe my wild distress Or lull me to forgetfulness. I see but him: my lips can frame No syllable but Ráma's name. Each sight I see, each sound I hear, Brings Ráma to mine eye or ear, The wish was in my heart, and hence The sweet illusion mocked my sense. 'Twas but a phantom of the mind, And yet the voice was soft and kind. Be glory to the Eternal Sire,848 Be glory to the Lord of Fire, The mighty Teacher in the skies,849 And Indra with his thousand eyes, And may they grant the truth to be E'en as the words that startled me.” [413] Canto XXXIII. The Colloquy. 848 Svayambhu, the Self-existent, Brahmá. 849 V [ihaspati or Váchaspati, the Lord of Speech and preceptor of the Gods.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1473)
- **Original**: Canto XXXIII. The Colloquy. 1455 Down from the tree Hanumán came And humbly stood before the dame. Then joining reverent palm to palm Addressed her thus with words of balm: “Why should the tears of sorrow rise, Sweet lady, to those lovely eyes, As when the wind-swept river floods Two half expanded lotus buds? Who art thou, O most fair of face? Of Asur,850 or celestial race? Did Nága mother give thee birth? For sure thou art no child of earth. Do Rudras851 claim that heavenly form? Or the swift Gods852 who ride the storm? Or art thou RohiGí853 the blest, That star more lovely than the rest,— Reft from the Moon thou lovest well And doomed a while on earth to dwell? Or canst thou, fairest wonder, be The starry queen Arundhatí,854 Fled in thy wrath or jealous pride From her dear lord Va[ishmha's side? Who is the husband, father, son Or brother, O thou loveliest one, Gone from this world in heaven to dwell, For whom those eyes with weeping swell? Yet, by the tears those sweet eyes shed, 850 The Asurs were the fierce enemies of the Gods. 851 The Rudras are manifestations ofZiva. 852 The Maruts or Storm Gods. 853 RohiGí is an asterism personified as the daughter of Daksha and the favourite wife of the Moon. The chief star in the constellation is Aldebaran. 854 Arundhatí was the wife of the great sage Va[ishmha, and regarded as the pattern of conjugal excellence. She was raised to the heavens as one of the Pleiades.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1474)
- **Original**: 1456 The Ramayana Yet, by the earth that bears thy tread,855 By calling on a monarch's name, No Goddess but a royal dame. Art thou the queen, fair lady, say, Whom Ráva G stole and bore away? Yea, by that agony of woe, That form unrivalled here below, That votive garb, thou art, I ween, King Janak's child and Ráma's queen.” Hope at the name of Ráma woke, And thus the gentle lady spoke: “I am that Sítá wooed and won By Da[aratha's royal son, The noblest of Ikshváku's line; And every earthly joy was mine. But Ráma left his royal home In DaG ak's tangled wilds to roam. Where with Sumitrá's son and me, He lived a saintly devotee. The giant RávaG came with guile And bore me thence to Lanká's isle. Some respite yet the fiend allows, Two months of life, to Ráma's spouse. Two moons of hopeless woe remain, And then the captive will be slain.” 855 The Gods do not shed tears; nor do they touch the ground when they walk or stand. Similarly Milton's angels marched above the ground and“the passive air upbore their nimble tread.” Virgil's“vera incessu patuit dea” may refer to the same belief.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1475)
- **Original**: Canto XXXIV. Hanumán's Speech. 1457 Canto XXXIV. Hanumán's Speech. Thus spoke the dame in mournful mood, And Hanumán his speech renewed: “O lady, by thy lord's decree I come a messenger to thee. Thy lord is safe with steadfast friends, And greeting to his queen he sends, And Lakshma G, ever faithful bows His reverent head to Ráma's spouse.” Through all her frame the rapture ran, As thus again the dame began: “Now verily the truth I know Of the wise saw of long ago: “Once only in a hundred years True joy to living man appears.” He marked her rapture-beaming hue, And nearer to the lady drew, But at each onward step he took Suspicious fear her spirit shook. “Alas, Alas,” she cried in fear. “False is the tale I joyed to hear. 'Tis RávaG, 'tis the fiend, who tries To mock me with a new disguise. If thou, to wring my woman's heart, Hast changed thy shape by magic art, And wouldst a helpless dame beguile, The wicked deed is doubly vile. But no: that fiend thou canst not be: Such joy I had from seeing thee. But if my fancy does not err, And thou art Ráma's messenger,
- **Translation**: 

---

### Verse 11 (Ramayana 0.1476)
- **Original**: 1458 The Ramayana The glories of my lord repeat: For to these ears such words are sweet.” The Vánar knew the lady's thought,856 And gave the answer fondly sought:[414] “Bright as the sun that lights the sky Dear as the Moon to every eye. He scatters blessings o'er the land Like bounties from Vai[ravaG's857 hand. Like VishGu strong and unsubdued, Unmatched in might and fortitude. Wise, truthful as the Lord of Speech, With gentle words he welcomes each. Of noblest mould and form is he, Like love's incarnate deity. He quells the fury of the foe, And strikes when justice prompts the blow. Safe in the shadow of his arm The world is kept from scathe and harm. Now soon shall RávaG rue his theft, And fall, of realm and life bereft. For Ráma's wrathful hand shall wing His shafts against the giant king. The day, O Maithil Queen, is near When he and LakshmaG will be here, And by their side Sugríva lead His countless hosts of Vánar breed. Sugríva's servant, I, by name Hanumán, by his order came. With desperate leap I crossed the sea To Lanká's isle in search of thee, 856 That a friend of Ráma would praise him as he should be praised, and that if the stranger were RávaG in disguise he would avoid the subject. 857 Kuvera the God of Gold.
- **Translation**: 

---

### Verse 12 (Ramayana 0.1477)
- **Original**: Canto XXXV. Hanumán's Speech. 1459 No traitor, gentle dame, am I: Upon my word and faith rely.” Canto XXXV. Hanumán's Speech. With joyous heart she heard him tell Of the great lord she loved so well, And in sweet accents, soft and low, Spoke, half forgetful of her woe: “How didst thou stand by Ráma's side? How came my lord and thou allied? How met the people of the wood With men on terms of brotherhood? Declare each grace and regal sign That decks the lords of Raghu's line. Each circumstance and look relate: Tell Ráma's form and speech, and gait.” “Thy fear and doubt,” he cried,“dispelled, Hear, lady, what mine eyes beheld. Hear the imperial signs that grace The glory of Ikshváku's race. With moon-bright face and lotus eyes, Most beautiful and good and wise, With sun-like glory round his head, Long-suffering as the earth we tread, He from all foes his realm defends. Yea, o'er the world his care extends. He follows right in all his ways, And ne'er from royal duty strays. He knows the lore that strengthens kings;
- **Translation**: 

---

### Verse 13 (Ramayana 0.1478)
- **Original**: 1460 The Ramayana His heart to truth and honour clings. Each grace and gift of form and mind Adorns that prince of human kind; And virtues like his own endue His brother ever firm and true. O'er all the land they roamed distraught, And thee with vain endeavour sought, Until at length their wandering feet Trod wearily our wild retreat. Our banished king Sugríva spied The princes from the mountain side. By his command I sought the pair And led them to our monarch there. Thus Ráma and Sugríva met, And joined the bonds that knit them yet, When each besought the other's aid, And friendship and alliance made. An arrow launched from Ráma's bow Laid Báli dead, Sugríva's foe. Then by commandment of our lord The Vánar hosts each land explored. We reached the coast: I crossed the sea And found my way at length to thee.”858 Canto XXXVI. Ráma's Ring. 858 Sítá of course knows nothing of what has happened to Ráma since the time when she was carried away by RávaG. The poet therefore thinks it necessary to repeat the whole story of the meeting between Ráma and Sugríva, the defeat of Bálí, and subsequent events. I give the briefest possible outline of the story.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1479)
- **Original**: Canto XXXVI. Ráma's Ring. 1461 “Receive,” he cried,“this precious ring,859 Sure token from thy lord the king: The golden ring he wont to wear: See, Ráma's name engraven there.” Then, as she took the ring he showed, The tears that spring of rapture flowed. She seemed to touch the hand that sent The dearly valued ornament, And with her heart again at ease, Replied in gentle words like these: “O thou, whose soul no fears deter, Wise, brave, and faithful messenger! And hast thou dared, o'er wave and foam, To seek me in the giants' home? In thee, true messenger, I find The noblest of thy woodland kind. Who couldst, unmoved by terror, brook On RávaG, king of fiends, to look. [415] Now may we commune here as friends, For he whom royal Ráma sends Must needs be one in danger tried, A valiant, wise, and faithful guide. Say, is it well with Ráma still? Lives LakshmaG yet untouched by ill? Then why should Ráma's hand be slow To free his consort from her woe? Why spare to burn, in search of me, The land encircled by the sea? Can Bharat send no army out With banners, cars and battle shout? Cannot thy king Sugríva lend His legions to assist his friend?” 859 D E G UBERNATIS {FNS thinks that this ring which the Sun Ráma sends to the Dawn Sítá is a symbol of the sun's disc.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1480)
- **Original**: 1462 The Ramayana His hands upon his head he laid And thus again his answer made: “Not yet has Ráma learnt where lies His lady of the lotus eyes, Or he like Indra from the sky To Zachí's860 aid, to thee would fly. Soon will he hear the tale, and then, Roused to revenge, the lord of men Will to the giants' island lead Fierce myriads of the woodland breed, Bridging his conquering way, and make The town a ruin for thy sake. Believe my words, sweet dame; I swear By roots and fruit, my woodland fare, By Meru's peak and Vindhva's chain, And Mandar of the Milky Main, Soon shalt thou see thy lord, though now He waits upon Pra[ravaG's861 brow, Come glorious as the breaking morn, Like Indra on Airávat862 borne. For thee he looks with longing eyes; The wood his scanty food supplies. For thee his brow is pale and worn, For thee are meat and wine forsworn. Thine image in his heart he keeps, For thee by night he wakes and weeps. Or if perchance his eyes he close And win brief respite from his woes, E'en then the name of Sítá slips In anguish from his murmuring lips. 860 Zachí is the loved and lovely wife of Indra, and she is taken as the type of a woman protected by a jealous and all-powerful husband. 861 The mountain near Kishkindhá. 862 Airávat is the mighty elephant on which Indra delights to ride.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1481)
- **Original**: Canto XXXVII. Sítá's Speech. 1463 If lovely flowers or fruit he sees, Which women love, upon the trees, To thee, to thee his fancy flies. And ‘Sítá! O my love!’he cries.” Canto XXXVII. Sítá's Speech. “Thou bringest me,” she cried again, “A mingled draught of bliss and pain: Bliss, that he wears me in his heart, Pain, that he wakes and weeps apart, O, see how Fate is king of all, Now lifts us high, now bids us fall, And leads a captive bound with cord The meanest slave, the proudest lord, Thus even now Fate's stern decree Has struck with grief my lord and me. Say, how shall Ráma reach the shore Of sorrow's waves that rise and roar, A shipwrecked sailor, well nigh drowned In the wild sea that foams around? When will he smite the demon down, Lay low in dust the giants' town, And, glorious from his foes' defeat, His wife, his long-lost Sítá, meet? Go, bid him speed to smite his foes Before the year shall reach its close. Ten months are fled but two remain, Then RávaG's captive must be slain. Oft has VibhishaG,863 just and wise, 863 VibhishaG is the wicked RávaG's good brother.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1482)
- **Original**: 1464 The Ramayana Besought him to restore his prize. But deaf is RávaG's senseless ear: His brother's rede he will not hear. VibhishaG's daughter864 loves me well: From her I learnt the tale I tell. Avindhva865 prudent, just, and old, The giant's fall has oft foretold; But Fate impels him to despise His word on whom he most relies. In Ráma's love I rest secure, For my fond heart is true and pure, And him, my noblest lord, I deem In valour, power, and might supreme.” As from her eyes the waters ran, The Vánar chief again began: “Yea, Ráma, when he hears my tale, Will with our hosts these walls assail. Or I myself, O Queen, this day Will bear thee from the fiend away, Will lift thee up, and take thee hence To him thy refuge and defence; Will take thee in my arms, and flee To Ráma far beyond the sea; Will place thee on Pra[ravaG hill Where Raghu's son is waiting still.”[416] “How canst thou bear me hence?” she cried, “The way is long, the sea is wide. To bear my very weight would be A task too hard for one like thee.”866 864 Her name is Kalá, or in the Bengal recension Nandá. 865 One of RávaG's chief councillors. 866 Hanumán when he entered the city had in order to escape observation condensed himself to the size of a cat.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1483)
- **Original**: Canto XXXVII. Sítá's Speech. 1465 Swift rose before her startled eyes The Vánar in his native size, Like Mandar's hill or Meru's height, Encircled with a blaze of light. “O come,” he cried,“thy fears dispel, Nor doubt that I will bear thee well. Come, in my strength and care confide, And sit in joy by Ráma's side.” Again she spake:“I know thee now, Brave, resolute, and strong art thou; In glory like the Lord of Fire With storm-swift feet which naught may tire But yet with thee I may not fly: For, borne so swiftly through the sky, Mine eyes would soon grow faint and dim, My dizzy brain would reel and swim, My yielding arms relax their hold, And I in terror uncontrolled Should fall into the raging sea Where hungry sharks would feed on me. Nor can I touch, of free accord, The limbs of any save my lord. If, by the giant forced away, In his enfolding arms I lay, Not mine, O Vánar, was the blame; What could I do, a helpless dame? Go, to my lord my message bear, And bid him end my long despair.”
- **Translation**: 

---

### Verse 19 (Ramayana 0.1484)
- **Original**: 1466 The Ramayana Canto XXXVIII. Sítá's Gem. Again the Vánar chief replied, With her wise answer satisfied: “Well hast thou said: thou canst not brave The rushing wind, the roaring wave. Thy woman's heart would sink with fear Before the ocean shore were near. And for thy dread lest limb of thine Should for a while be touched by mine, The modest fear is worthy one Whose cherished lord is Raghu's son. Yet when I sought to bear thee hence I spoke the words of innocence, Impelled to set the captive free By friendship for thy lord and thee. But if with me thou wilt not try The passage of the windy sky, Give me a gem that I may show, Some token which thy lord may know.” Again the Maithil lady spoke, While tears and sobs her utterance broke: “The surest of all signs is this, To tell the tale of vanished bliss. Thus in my name to Ráma speak: “Remember Chitrakúma's peak And the green margin of the rill867 That flows beside that pleasant hill, Where thou and I together strayed Delighting in the tangled shade. 867 The brook Mandákiní, not far from Chitrakúma where Ráma sojourned for a time.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1485)
- **Original**: Canto XXXVIII. Sítá's Gem. 1467 There on the grass I sat with thee And laid my head upon thy knee. There came a greedy crow and pecked The meat I waited to protect And, heedless of the clods I threw, About my head in circles flew, Until by darling hunger pressed He boldly pecked me on the breast. I ran to thee in rage and grief And prayed for vengeance on the thief. Then Ráma 868 from his slumber rose And smiled with pity at my woes. Upon my bleeding breast he saw The scratches made by beak and claw. He laid an arrow on his bow, And launched it at the shameless crow. That shaft, with magic power endued, The bird, where'er he flew, pursued, Till back to Raghu's son he fled And bent at Ráma's feet his head.869 Couldst thou for me with anger stirred Launch that dire shaft upon a bird, And yet canst pardon him who stole The darling of thy heart and soul? Rise up, O bravest of the brave, And come in all thy might to save. Come with the thunders of thy bow, And smite to earth the Rákshas foe.” She ceased; and from her glorious hair She took a gem that sparkled there 868 The poet here changes from the second person to the third. 869 The whole long story is repeated with some slight variations and additions from Book II, Canto XCVI. I give here only the outline.
- **Translation**: 

---

