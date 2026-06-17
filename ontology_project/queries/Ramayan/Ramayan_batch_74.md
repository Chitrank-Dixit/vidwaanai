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

### Verse 1 (Ramayan 0.1461)
- **Original**: Canto XXIV. Sítá's Reply. 1443 Canto XXIV. Sítá's Reply. Still with reproaches rough and rude Those fiends the gentle queen pursued: “What! can so fair a life displease, To dwell with him in joyous ease? Dwell in his bowers a happy queen In silk and gold and jewels' sheen? Still must thy woman fancy cling To Ráma and reject our king? Die in thy folly, or forget That wretched wandering anchoret. Come, Sítá, in luxurious bowers Spend with our lord thy happy hours; The mighty lord who makes his own The treasures of the worlds o'erthrown.” Then, as a tear bedewed her eye, The hapless lady made reply: “I loathe, with heart and soul detest The shameful life your words suggest. Eat, if you will, this mortal frame: My soul rejects the sin and shame. A homeless wanderer though he be, In him my lord, my life I see, And, till my earthly days be done, Will cling to great Ikshváku's son.”
- **Translation**: 

---

### Verse 2 (Ramayan 0.1462)
- **Original**: 1444 The Ramayana Then with fierce eyes on Sítá set They cried again with taunt and threat: Each licking with her fiery tongue The lip that to her bosom hung, And menacing the lady's life With axe, or spear or murderous knife: “Hear, Sítá, and our words obey, Or perish by our hands to-day. Thy love for Raghu's son forsake, And RávaG for thy husband take, Or we will rend thy limbs apart And banquet on thy quivering heart. Now from her body strike the head, And tell the king the dame is dead. Then by our lord's commandment she A banquet for our band shall be. Come, let the wine be quickly brought That frees each heart from saddening thought. Then to the western gate repair, And we will dance and revel there.” Canto XXV. Sítá's Lament. On the bare earth the lady sank, And trembling from their presence shrank Like a strayed fawn, when night is dark, And hungry wolves around her bark.[410]
- **Translation**: 

---

### Verse 3 (Ramayan 0.1463)
- **Original**: Canto XXV. Sítá's Lament. 1445 Then to a shady tree she crept, And thought upon her lord and wept. By fear and bitter woe oppressed She bathed the beauties of her breast With her hot tears' incessant flow, And found no respite from her woe. As shakes a plantain in the breeze She shook, and fell on trembling knees; While at each demon's furious look Her cheek its native hue forsook. She lay and wept and made her moan In sorrow's saddest undertone, And, wild with grief, with fear appalled, On Ráma and his brother called: “O dear Kau[alyá,842 hear me cry! Sweet Queen Sumitrá,843 list my sigh! True is the saw the wise declare: Death comes not to relieve despair. 'Tis vain for dame or man to pray; Death will not hear before his day; Since I, from Ráma's sight debarred, And tortured by my cruel guard, Still live in hopeless woe to grieve And loathe the life I may not leave, Here, like a poor deserted thing, My limbs upon the ground I fling, And, like a bark beneath the blast, Shall sink oppressed with woes at last. Ah, blest are they, supremely blest, Whose eyes upon my lord may rest; Who mark his lion port, and hear His gentle speech that charms the ear. 842 The mother of Ráma. 843 The mother of LakshmaG.
- **Translation**: 

---

### Verse 4 (Ramayan 0.1464)
- **Original**: 1446 The Ramayana Alas, what antenatal crime, What trespass of forgotten time Weighs on my soul, and bids me bow Beneath this load of misery now?” Canto XXVI. Sítá's Lament. “I Ráma's wife, on that sad day, By RávaG's arm was borne away, Seized, while I sat and feared no ill, By him who wears each form at will. A helpless captive, left forlorn To demons' threats and taunts and scorn, Here for my lord I weep and sigh, And worn with woe would gladly die. For what is life to me afar From Ráma of the mighty car? The robber in his fruitless sin Would hope his captive's love to win. My meaner foot shall never touch The demon whom I loathe so much. The senseless fool! he knows me not, Nor the proud soul his love would blot. Yea, limb from limb will I be rent, But never to his prayer consent; Be burnt and perish in the fire, But never meet his base desire. My lord was grateful, true and wise, And looked on woe with pitying eyes; But now, recoiling from the strife He pities not his captive wife.
- **Translation**: 

---

### Verse 5 (Ramayan 0.1465)
- **Original**: Canto XXVII. Trijatá's Dream. 1447 Alone in Janasthán he slew The thousands of the Rákshas crew. His arm was strong, his heart was brave, Why comes he not to free and save? Why blame my lord in vain surmise? He knows not where his lady lies. O, if he knew, o'er land and sea His feet were swift to set me free; This Lanká, girdled by the deep, Would fall consumed, a shapeless heap, And from each ruined home would rise A Rákshas widow's groans and cries.” Canto XXVII. Trijatá's Dream. Their threats unfeared, their counsel spurned, The demons' breasts with fury burned. Some sought the giant king to bear The tale of Sítá's fixt despair. With threats and taunts renewed the rest Around the weeping lady pressed. But Trijamá, of softer mould, A Rákshas matron wise and old, With pity for the captive moved, In words like these the fiends reproved: “Me, me,” she cried,“eat me, but spare The spouse of Da[aratha's heir. Last night I dreamt a dream; and still The fear and awe my bosom chill; For in that dream I saw foreshown Our race by Ráma's hand o'erthrown.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1466)
- **Original**: 1448 The Ramayana I saw a chariot high in air, Of ivory exceeding fair. A hundred steeds that chariot drew As swiftly through the clouds it flew, And, clothed in white, with wreaths that shone, The sons of Raghu rode thereon. I looked and saw this lady here, Clad in the purest white, appear High on the snow white hill whose feet The angry waves of ocean beat. And she and Ráma met at last Like light and sun when night is past. Again I saw them side by side. On RávaG's car they seemed to ride, And with the princely LakshmaG flee To northern realms beyond the sea.[411] Then RávaG, shaved and shorn, besmeared With oil from head to foot, appeared. He quaffed, he raved: his robes were red: Fierce was his eye, and bare his head. I saw him from his chariot thrust; I saw him rolling in the dust. A woman came and dragged away The stricken giant where he lay, And on a car which asses drew The monarch of our race she threw. He rose erect, he danced and laughed, With thirsty lips the oil he quaffed, Then with wild eyes and streaming mouth Sped on the chariot to the south.844 Then, dropping oil from every limb, His sons the princes followed him, 844 In the south is the region of Yáma the God of Death, the place of departed spirits.
- **Translation**: 

---

### Verse 7 (Ramayan 0.1467)
- **Original**: Canto XXX. Hanumán's Deliberation. 1449 And Kumbhakar Ga,845 shaved and shorn, Was southward on a camel borne. Then royal Lanká reeled and fell With gate and tower and citadel. This ancient city, far-renowned: All life within her walls was drowned; And the wild waves of ocean rolled O'er Lanká and her streets of gold. Warned by these signs I bid you fly; Or by the hand of Ráma die, Whose vengeance will not spare the life Of one who vexed his faithful wife. Your bitter taunts and threats forgo: Comfort the lady in her woe, And humbly pray her to forgive; For so you may be spared and live.” [I omit the 28th and 29th Cantos as an unmistakeable interpola- tion. Instead of advancing the story it goes back to Canto XVII, containing a lamentation of Sítá after RávaG has left her, and describes the the auspicious signs sent to cheer her, the throbbing of her left eye, arm, and side. The Canto is found in the Bengal recension. Gorresio translates it. and observes:“I think that Chapter XXVIII.— The Auspicious Signs— is an addition, a later interpolation by the Rhapsodists. It has no bond of connexion either with what precedes or follows it, and may be struck out not only without injury to, but positively to the advantage of the poem. The metre in which this chapter is written differs from that which is generally adopted in the course of the poem.”] Canto XXX. Hanumán's Deliberation. 845 Kumbhakar Ga was one of RávaG's brothers.
- **Translation**: 

---

### Verse 8 (Ramayan 0.1468)
- **Original**: 1450 The Ramayana The Vánar watched concealed: each word Of Sítá and the fiends he heard, And in a maze of anxious thought His quick-conceiving bosom wrought. “At length my watchful eyes have seen, Pursued so long, the Maithil queen, Sought by our Vánar hosts in vain From east to west, from main to main. A cautious spy have I explored The palace of the Rákhshas lord, And thoroughly learned, concealed from sight, The giant monarch's power and might. And now my task must be to cheer The royal dame who sorrows here. For if I go, and soothe her not, A captive in this distant spot, She, when she finds no comfort nigh, Will sink beneath her woes and die. How shall my tale, if unconsoled I leave her, be to Ráma told? How shall I answer Raghu's son, “No message from my darling, none?” The husband's wrath, to fury fanned, Will scorch me lifeless where I stand, Or if I urge my lord the king To Lanká's isle his hosts to bring, In vain will be his zeal, in vain The toil, the danger, and the pain. Yea, this occasion must I seize That from her guard the lady frees,846 To win her ear with soft address And whisper hope in dire distress. 846 The guards are still in the grove, but they are asleep; and Sítá has crept to a tree at some distance from them.
- **Translation**: 

---

### Verse 9 (Ramayan 0.1469)
- **Original**: Canto XXX. Hanumán's Deliberation. 1451 Shall I, a puny Vánar, choose The Sanskrit men delight to use? If, as a man of Bráhman kind, I speak the tongue by rules refined, The lady, yielding to her fears, Will think 'tis RávaG's voice she hears. I must assume my only plan— The language of a common847 man. Yet, if the lady sees me nigh, [412] In terror she will start and cry; And all the demon band, alarmed, Will come with various weapons armed, With their wild shouts the grove will fill, And strive to take me, or to kill. And, at my death or capture, dies The hope of Ráma`s enterprise. For none can leap, save only me, A hundred leagues across the sea. It is a sin in me, I own, To talk with Janak's child alone. Yet greater is the sin if I Be silent, and the lady die. First I will utter Ráma's name, And laud the hero's gifts and fame. Perchance the name she holds so dear 847 “As the reason assigned in these passages for not addressing Sítá in Sanskrit such as a Bráhman would use is not that she would not understand it, but that it would alarm her and be unsuitable to the speaker, we must take them as indicating that Sanskrit, if not spoken by women of the upper classes at the time when the RámáyaGa was written (whenever that may have been), was at least understood by them, and was commonly spoken by men of the priestly class, and other educated persons. By the Sanskrit proper to an [ordinary] man, alluded to in the second passage, may perhaps be understood not a language in which words different from Sanskrit were used, but the employment of formal and elaborate diction.” M UIR 'S{FNS Sanskrit Texts, Part II. p. 166.
- **Translation**: 

---

### Verse 10 (Ramayan 0.1470)
- **Original**: 1452 The Ramayana Will soothe the faithful lady's fear.” Canto XXXI. Hanumán's Speech. Then in sweet accents low and mild The Vánar spoke to Janak's child: “A noble king, by sin unstained, The mighty Da[aratha reigned. Lord of the warrior's car and steed, The pride of old Ikshváku's seed. A faithful friend, a blameless king, Protector of each living thing. A glorious monarch, strong to save, Blest with the bliss he freely gave. His son, the best of all who know The science of the bended bow, Was moon-bright Ráma, brave and strong, Who loved the right and loathed the wrong, Who ne'er from kingly duty swerved, Loved by the lands his might preserved. His feet the path of law pursued; His arm rebellious foes subdued. His sire's command the prince obeyed And, banished, sought the forest shade, Where with his wife and brother he Wandered a saintly devotee. There as he roamed the wilds he slew The bravest of the Rákshas crew. The giant king the prince beguiled, And stole his consort, Janak's child. Then Ráma roamed the country round,
- **Translation**: 

---

### Verse 11 (Ramayan 0.1471)
- **Original**: Canto XXXII. Sítá's Doubt. 1453 And a firm friend, Sugríva, found, Lord of the Vánar race, expelled From his own realm which Báli held, He conquered Báli and restored The kingdom to the rightful lord. Then by Sugríva's high decree The Vánar legions searched for thee, Sampáti's counsel bade me leap A hundred leagues across the deep. And now my happy eyes have seen At last the long-sought Maithil queen. Such was the form, the eye, the grace Of her whom Ráma bade me trace.” He ceased: her flowing locks she drew To shield her from a stranger's view; Then, trembling in her wild surprise, Raised to the tree her anxious eyes. Canto XXXII. Sítá's Doubt. Her eyes the Maithil lady raised And on the monkey speaker gazed. She looked, and trembling at the sight Wept bitter tears in wild affright. She shrank a while with fear distraught, Then, nerved again, the lady thought: “Is this a dream mine eyes have seen, This creature, by our laws unclean? O, may the Gods keep Ráma, still, And Lakshma G, and my sire, from ill!
- **Translation**: 

---

### Verse 12 (Ramayan 0.1472)
- **Original**: 1454 The Ramayana It is no dream: I have not slept, But, trouble-worn, have watched and wept Afar from that dear lord of mine For whom in ceaseless woe I pine, No art may soothe my wild distress Or lull me to forgetfulness. I see but him: my lips can frame No syllable but Ráma's name. Each sight I see, each sound I hear, Brings Ráma to mine eye or ear, The wish was in my heart, and hence The sweet illusion mocked my sense. 'Twas but a phantom of the mind, And yet the voice was soft and kind. Be glory to the Eternal Sire,848 Be glory to the Lord of Fire, The mighty Teacher in the skies,849 And Indra with his thousand eyes, And may they grant the truth to be E'en as the words that startled me.” [413] Canto XXXIII. The Colloquy. 848 Svayambhu, the Self-existent, Brahmá. 849 V [ihaspati or Váchaspati, the Lord of Speech and preceptor of the Gods.
- **Translation**: 

---

### Verse 13 (Ramayan 0.1473)
- **Original**: Canto XXXIII. The Colloquy. 1455 Down from the tree Hanumán came And humbly stood before the dame. Then joining reverent palm to palm Addressed her thus with words of balm: “Why should the tears of sorrow rise, Sweet lady, to those lovely eyes, As when the wind-swept river floods Two half expanded lotus buds? Who art thou, O most fair of face? Of Asur,850 or celestial race? Did Nága mother give thee birth? For sure thou art no child of earth. Do Rudras851 claim that heavenly form? Or the swift Gods852 who ride the storm? Or art thou RohiGí853 the blest, That star more lovely than the rest,— Reft from the Moon thou lovest well And doomed a while on earth to dwell? Or canst thou, fairest wonder, be The starry queen Arundhatí,854 Fled in thy wrath or jealous pride From her dear lord Va[ishmha's side? Who is the husband, father, son Or brother, O thou loveliest one, Gone from this world in heaven to dwell, For whom those eyes with weeping swell? Yet, by the tears those sweet eyes shed, 850 The Asurs were the fierce enemies of the Gods. 851 The Rudras are manifestations ofZiva. 852 The Maruts or Storm Gods. 853 RohiGí is an asterism personified as the daughter of Daksha and the favourite wife of the Moon. The chief star in the constellation is Aldebaran. 854 Arundhatí was the wife of the great sage Va[ishmha, and regarded as the pattern of conjugal excellence. She was raised to the heavens as one of the Pleiades.
- **Translation**: 

---

### Verse 14 (Ramayan 0.1474)
- **Original**: 1456 The Ramayana Yet, by the earth that bears thy tread,855 By calling on a monarch's name, No Goddess but a royal dame. Art thou the queen, fair lady, say, Whom Ráva G stole and bore away? Yea, by that agony of woe, That form unrivalled here below, That votive garb, thou art, I ween, King Janak's child and Ráma's queen.” Hope at the name of Ráma woke, And thus the gentle lady spoke: “I am that Sítá wooed and won By Da[aratha's royal son, The noblest of Ikshváku's line; And every earthly joy was mine. But Ráma left his royal home In DaG ak's tangled wilds to roam. Where with Sumitrá's son and me, He lived a saintly devotee. The giant RávaG came with guile And bore me thence to Lanká's isle. Some respite yet the fiend allows, Two months of life, to Ráma's spouse. Two moons of hopeless woe remain, And then the captive will be slain.” 855 The Gods do not shed tears; nor do they touch the ground when they walk or stand. Similarly Milton's angels marched above the ground and“the passive air upbore their nimble tread.” Virgil's“vera incessu patuit dea” may refer to the same belief.
- **Translation**: 

---

### Verse 15 (Ramayan 0.1475)
- **Original**: Canto XXXIV. Hanumán's Speech. 1457 Canto XXXIV. Hanumán's Speech. Thus spoke the dame in mournful mood, And Hanumán his speech renewed: “O lady, by thy lord's decree I come a messenger to thee. Thy lord is safe with steadfast friends, And greeting to his queen he sends, And Lakshma G, ever faithful bows His reverent head to Ráma's spouse.” Through all her frame the rapture ran, As thus again the dame began: “Now verily the truth I know Of the wise saw of long ago: “Once only in a hundred years True joy to living man appears.” He marked her rapture-beaming hue, And nearer to the lady drew, But at each onward step he took Suspicious fear her spirit shook. “Alas, Alas,” she cried in fear. “False is the tale I joyed to hear. 'Tis RávaG, 'tis the fiend, who tries To mock me with a new disguise. If thou, to wring my woman's heart, Hast changed thy shape by magic art, And wouldst a helpless dame beguile, The wicked deed is doubly vile. But no: that fiend thou canst not be: Such joy I had from seeing thee. But if my fancy does not err, And thou art Ráma's messenger,
- **Translation**: 

---

### Verse 16 (Ramayan 0.1476)
- **Original**: 1458 The Ramayana The glories of my lord repeat: For to these ears such words are sweet.” The Vánar knew the lady's thought,856 And gave the answer fondly sought:[414] “Bright as the sun that lights the sky Dear as the Moon to every eye. He scatters blessings o'er the land Like bounties from Vai[ravaG's857 hand. Like VishGu strong and unsubdued, Unmatched in might and fortitude. Wise, truthful as the Lord of Speech, With gentle words he welcomes each. Of noblest mould and form is he, Like love's incarnate deity. He quells the fury of the foe, And strikes when justice prompts the blow. Safe in the shadow of his arm The world is kept from scathe and harm. Now soon shall RávaG rue his theft, And fall, of realm and life bereft. For Ráma's wrathful hand shall wing His shafts against the giant king. The day, O Maithil Queen, is near When he and LakshmaG will be here, And by their side Sugríva lead His countless hosts of Vánar breed. Sugríva's servant, I, by name Hanumán, by his order came. With desperate leap I crossed the sea To Lanká's isle in search of thee, 856 That a friend of Ráma would praise him as he should be praised, and that if the stranger were RávaG in disguise he would avoid the subject. 857 Kuvera the God of Gold.
- **Translation**: 

---

### Verse 17 (Ramayan 0.1477)
- **Original**: Canto XXXV. Hanumán's Speech. 1459 No traitor, gentle dame, am I: Upon my word and faith rely.” Canto XXXV. Hanumán's Speech. With joyous heart she heard him tell Of the great lord she loved so well, And in sweet accents, soft and low, Spoke, half forgetful of her woe: “How didst thou stand by Ráma's side? How came my lord and thou allied? How met the people of the wood With men on terms of brotherhood? Declare each grace and regal sign That decks the lords of Raghu's line. Each circumstance and look relate: Tell Ráma's form and speech, and gait.” “Thy fear and doubt,” he cried,“dispelled, Hear, lady, what mine eyes beheld. Hear the imperial signs that grace The glory of Ikshváku's race. With moon-bright face and lotus eyes, Most beautiful and good and wise, With sun-like glory round his head, Long-suffering as the earth we tread, He from all foes his realm defends. Yea, o'er the world his care extends. He follows right in all his ways, And ne'er from royal duty strays. He knows the lore that strengthens kings;
- **Translation**: 

---

### Verse 18 (Ramayan 0.1478)
- **Original**: 1460 The Ramayana His heart to truth and honour clings. Each grace and gift of form and mind Adorns that prince of human kind; And virtues like his own endue His brother ever firm and true. O'er all the land they roamed distraught, And thee with vain endeavour sought, Until at length their wandering feet Trod wearily our wild retreat. Our banished king Sugríva spied The princes from the mountain side. By his command I sought the pair And led them to our monarch there. Thus Ráma and Sugríva met, And joined the bonds that knit them yet, When each besought the other's aid, And friendship and alliance made. An arrow launched from Ráma's bow Laid Báli dead, Sugríva's foe. Then by commandment of our lord The Vánar hosts each land explored. We reached the coast: I crossed the sea And found my way at length to thee.”858 Canto XXXVI. Ráma's Ring. 858 Sítá of course knows nothing of what has happened to Ráma since the time when she was carried away by RávaG. The poet therefore thinks it necessary to repeat the whole story of the meeting between Ráma and Sugríva, the defeat of Bálí, and subsequent events. I give the briefest possible outline of the story.
- **Translation**: 

---

### Verse 19 (Ramayan 0.1479)
- **Original**: Canto XXXVI. Ráma's Ring. 1461 “Receive,” he cried,“this precious ring,859 Sure token from thy lord the king: The golden ring he wont to wear: See, Ráma's name engraven there.” Then, as she took the ring he showed, The tears that spring of rapture flowed. She seemed to touch the hand that sent The dearly valued ornament, And with her heart again at ease, Replied in gentle words like these: “O thou, whose soul no fears deter, Wise, brave, and faithful messenger! And hast thou dared, o'er wave and foam, To seek me in the giants' home? In thee, true messenger, I find The noblest of thy woodland kind. Who couldst, unmoved by terror, brook On RávaG, king of fiends, to look. [415] Now may we commune here as friends, For he whom royal Ráma sends Must needs be one in danger tried, A valiant, wise, and faithful guide. Say, is it well with Ráma still? Lives LakshmaG yet untouched by ill? Then why should Ráma's hand be slow To free his consort from her woe? Why spare to burn, in search of me, The land encircled by the sea? Can Bharat send no army out With banners, cars and battle shout? Cannot thy king Sugríva lend His legions to assist his friend?” 859 D E G UBERNATIS {FNS thinks that this ring which the Sun Ráma sends to the Dawn Sítá is a symbol of the sun's disc.
- **Translation**: 

---

### Verse 20 (Ramayan 0.1480)
- **Original**: 1462 The Ramayana His hands upon his head he laid And thus again his answer made: “Not yet has Ráma learnt where lies His lady of the lotus eyes, Or he like Indra from the sky To Zachí's860 aid, to thee would fly. Soon will he hear the tale, and then, Roused to revenge, the lord of men Will to the giants' island lead Fierce myriads of the woodland breed, Bridging his conquering way, and make The town a ruin for thy sake. Believe my words, sweet dame; I swear By roots and fruit, my woodland fare, By Meru's peak and Vindhva's chain, And Mandar of the Milky Main, Soon shalt thou see thy lord, though now He waits upon Pra[ravaG's861 brow, Come glorious as the breaking morn, Like Indra on Airávat862 borne. For thee he looks with longing eyes; The wood his scanty food supplies. For thee his brow is pale and worn, For thee are meat and wine forsworn. Thine image in his heart he keeps, For thee by night he wakes and weeps. Or if perchance his eyes he close And win brief respite from his woes, E'en then the name of Sítá slips In anguish from his murmuring lips. 860 Zachí is the loved and lovely wife of Indra, and she is taken as the type of a woman protected by a jealous and all-powerful husband. 861 The mountain near Kishkindhá. 862 Airávat is the mighty elephant on which Indra delights to ride.
- **Translation**: 

---

