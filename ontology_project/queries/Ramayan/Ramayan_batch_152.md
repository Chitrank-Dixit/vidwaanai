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

### Verse 1 (Ramayana 0.1066)
- **Original**: 1048 The Ramayana Yet from his hand shall come thy fate, Struck down before his vengeful hate. That mighty lord will strike and end The days of life thou hast to spend. Thy days are doomed, thy life is sped Like victims to the pillar led. Yea, if the glance of Ráma bright With fury on thy form should light, Thou scorched this day wouldst fall and die[296] Like Káma slain by Rudra's eye.506 He who from heaven the moon could throw, Or bid its bright rays cease to glow,— He who could drain the mighty sea Will set his darling Sítá free. Fled is thy life, thy glory, fled Thy strength and power: each sense is dead. Soon Lanká widowed by thy guilt Will see the blood of giants spilt. This wicked deed, O cruel King, No triumph, no delight will bring. Thou with outrageous might and scorn A woman from her lord hast torn. My glorious husband far away, Making heroic strength his stay, Dwells with his brother, void of fear, In DaG ak forest lone and drear. No more in force of arms confide: That haughty strength, that power and pride My hero with his arrowy rain From all thy bleeding limbs will drain. When urged by fate's dire mandate, nigh Comes the fixt hour for men to die. 506 See Book I Canto XXV.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1067)
- **Original**: Canto LVI. Sítá's Disdain. 1049 Caught in Death's toils their eyes are blind, And folly takes each wandering mind. So for the outrage thou hast done The fate is near thou canst not shun,— The fate that on thyself and all Thy giants and thy town shall fall. I spurn thee: can the altar dight With vessels for the sacred rite, O'er which the priest his prayer has said, Be sullied by an outcaste's tread? So me, the consort dear and true Of him who clings to virtue too, Thy hated touch shall ne'er defile, Base tyrant lord of Lanká's isle. Can the white swan who floats in pride Through lilies by her consort's side, Look for one moment, as they pass, On the poor diver in the grass? This senseless body waits thy will, To torture, chain, to wound or kill. I will not, King of giants, strive To keep this fleeting soul alive But never shall they join the name Of Sítá with reproach and shame.” Thus as her breast with fury burned Her bitter speech the dame returned. Such words of rage and scorn, the last She uttered, at the fiend she cast. Her taunting speech the giant heard, And every hair with anger stirred. Then thus with fury in his eye He made in threats his fierce reply: “Hear Maithil lady, hear my speech:
- **Translation**: 

---

### Verse 3 (Ramayana 0.1068)
- **Original**: 1050 The Ramayana List to my words and ponder each. If o'er thy head twelve months shall fly And thou thy love wilt still deny, My cooks shall mince thy flesh with steel And serve it for my morning meal.” Thus with terrific threats to her Spake RávaG, cruel ravener. Mad with the rage her answer woke He called the fiendish train and spoke: “Take her, ye Rákshas dames, who fright With hideous form and mien the sight, Who make the flesh of men your food,— And let her pride be soon subdued.” He spoke, and at his word the band Of fiendish monsters raised each hand In reverence to the giant king, And pressed round Sítá in a ring. RávaG once more with stern behest To those she-fiends his speech addressed: Shaking the earth beneath his tread, He stamped his furious foot and said: “To the A[oka garden bear The dame, and guard her safely there Until her stubborn pride be bent By mingled threat and blandishment. See that ye watch her well, and tame, Like some she-elephant, the dame.”
- **Translation**: 

---

### Verse 4 (Ramayana 0.1069)
- **Original**: Canto LVII. Sítá Comforted. 1051 They led her to that garden where The sweetest flowers perfumed the air, Where bright trees bore each rarest fruit, And birds, enamoured, ne'er were mute. Bowed down with terror and distress, Watched by each cruel giantess,— Like a poor solitary deer When ravening tigresses are near,— The hapless lady lay distraught Like some wild thing but newly caught, And found no solace, no relief From agonizing fear and grief; Not for one moment could forget Each terrifying word and threat, Or the fierce eyes upon her set By those who watched around. She thought of Ráma far away, She mourned for LakshmaG as she lay In grief and terror and dismay Half fainting on the ground. Canto LVII. Sítá Comforted. Soon as the fiend had set her down Within his home in Lanká's town Triumph and joy filled Indra's breast, Whom thus the Eternal Sire addressed:
- **Translation**: 

---

### Verse 5 (Ramayana 0.1070)
- **Original**: 1052 The Ramayana “This deed will free the worlds from woe And cause the giants' overthrow. The fiend has borne to Lanká's isle The lady of the lovely smile, True consort born to happy fate With features fair and delicate.[297] She looks and longs for Ráma's face, But sees a crowd of demon race, And guarded by the giant's train Pines for her lord and weeps in vain. But Lanká founded on a steep Is girdled by the mighty deep, And how will Ráma know his fair And blameless wife is prisoned there? She on her woe will sadly brood And pine away in solitude, And heedless of herself, will cease To live, despairing of release. Yes, pondering on her fate, I see Her gentle life in jeopardy. Go, Indra, swiftly seek the place, And look upon her lovely face. Within the city make thy way: Let heavenly food her spirit stay.” Thus Brahma spake: and He who slew The cruel demon Páka, flew Where Lanká's royal city lay, And Sleep went with him on his way. “Sleep,” cried the heavenly Monarch,“close Each giant's eye in deep repose.”
- **Translation**: 

---

### Verse 6 (Ramayana 0.1071)
- **Original**: Canto LVII. Sítá Comforted. 1053 Thus Indra spoke, and Sleep fulfilled With joy his mandate, as he willed, To aid the plan the Gods proposed, The demons' eyes in sleep she closed. Then Zachí's lord, the Thousand-eyed, To the A[oka garden hied. He came and stood where Sítá lay, And gently thus began to say: “Lord of the Gods who hold the sky, Dame of the lovely smile, am I. Weep no more, lady, weep no more; Thy days of woe will soon be o'er. I come, O Janak's child, to be The helper of thy lord and thee. He through my grace, with hosts to aid, This sea-girt land will soon invade. 'Tis by my art that slumbers close The eyelids of thy giant foes. Now I, with Sleep, this place have sought, Videhan lady, and have brought A gift of heaven's ambrosial food To stay thee in thy solitude. Receive it from my hand, and taste, O lady of the dainty waist: For countless ages thou shall be From pangs of thirst and hunger free.” But doubt within her bosom woke As to the Lord of Gods she spoke: “How may I know for truth that thou Whose form I see before me now Art verily the King adored By heavenly Gods, andZachí's lord? With Raghu's sons I learnt to know
- **Translation**: 

---

### Verse 7 (Ramayana 0.1072)
- **Original**: 1054 The Ramayana The certain signs which Godhead show. These marks before mine eyes display If o'er the Gods thou bear the sway.” The heavenly lord ofZachí heard, And did according to her word. Above the ground his feet were raised; With eyelids motionless he gazed. No dust upon his raiment lay, And his bright wreath was fresh and gay. Nor was the lady's glad heart slow The Monarch of the Gods to know, And while the tears unceasing ran From her sweet eyes she thus began: “My lord has gained a friend in thee, And I this day thy presence see Shown clearly to mine eyes, as when Ráma and LakshmaG, lords of men, Beheld it, and their sire the king, And Janak too from whom I spring. Now I, O Monarch of the Blest, Will eat this food at thy behest, Which thou hast brought me, of thy grace, To aid and strengthen Raghu's race.” She spoke, and by his words relieved, The food from Indra's hand received, Yet ere she ate the balm he brought, On Lakshma G and her lord she thought. “If my brave lord be still alive, If valiant LakshmaG yet survive, May this my taste of heavenly food Bring health to them and bliss renewed!” She ate, and that celestial food
- **Translation**: 

---

### Verse 8 (Ramayana 0.1073)
- **Original**: Canto LVIII. The Brothers' Meeting. 1055 Stayed hunger, thirst, and lassitude, And all her strength restored. Great joy her hopeful spirit stirred At the glad tidings newly heard Of LakshmaG and her lord. And Indra's heart was joyful too: He bade the Maithil dame adieu, His saving errand done. With Sleep beside him parting thence He sought his heavenly residence To prosper Raghu's son. Canto LVIII. The Brothers' Meeting. When Ráma's deadly shaft had struck The giant in the seeming buck, The chieftain turned him from the place His homeward way again to trace. Then as he hastened onward, fain To look upon his spouse again, Behind him from a thicket nigh Rang out a jackal's piercing cry. Alarmed he heard the startling shriek That raised his hair and dimmed his cheek, And all his heart was filled with doubt As the shrill jackal's cry rang out: “Alas, some dire disaster seems Portended by the jackal's screams. O may the Maithil dame be screened From outrage of each hungry fiend! [298]
- **Translation**: 

---

### Verse 9 (Ramayana 0.1074)
- **Original**: 1056 The Ramayana Alas, if LakshmaG chanced to hear That bitter cry of woe and fear What time Márícha, as he died, With voice that mocked my accents cried, Swift to my side the prince would flee And quit the dame to succour me. Too well I see the demon band The slaughter of my love have planned. Me far from home and Sítá's view The seeming deer Márícha drew. He led me far through brake and dell Till wounded by my shaft he fell, And as he sank rang out his cry, “O save me, LakshmaG, or I die.” May it be well with both who stayed In the great wood with none to aid, For every fiend is now my foe For Janasthán's great overthrow, And many an omen seen to-day Has filled my heart with sore dismay.” Such were the thoughts and sad surmise Of Ráma at the jackal's cries, And all his heart within him burned As to his cot his steps he turned. He pondered on the deer that led His feet to follow where it fled, And sad with many a bitter thought His home in Janasthán he sought. His soul was dark with woe and fear When flocks of birds and troops of deer Move round him from the left, and raised Discordant voices as they gazed. The omens which the chieftain viewed
- **Translation**: 

---

### Verse 10 (Ramayana 0.1075)
- **Original**: Canto LVIII. The Brothers' Meeting. 1057 The terror of his soul renewed, When lo, to meet him LakshmaG sped With brows whence all the light had fled. Near and more near the princes came, Each brother's heart and look the same; Alike on each sad visage lay The signs of misery and dismay, Then Ráma by his terror moved His brother for his fault reproved In leaving Sítá far from aid In the wild wood where giants strayed. Lakshma G's left hand he took, and then In gentle tones the prince of men, Though sharp and fierce their tenour ran, Thus to his brother chief began: “O Lakshma G, thou art much to blame Leaving alone the Maithil dame, And flying hither to my side: O, may no ill my spouse betide! But ah, I know my wife is dead, And giants on her limbs have fed, So strange, so terrible are all The omens which my heart appal. O Lakshma G, may we yet return The safety of my love to learn. To find the child of Janak still Alive and free from scathe and ill! Each bird with notes of warning screams, Though the hot sun still darts his beams. The moan of deer, the jackal's yell Of some o'erwhelming misery tell. O mighty brother, still may she, My princess, live from danger free!
- **Translation**: 

---

### Verse 11 (Ramayana 0.1076)
- **Original**: 1058 The Ramayana That semblance of a golden deer Allured me far away, I followed nearer and more near, And longed to take the prey. I followed where the quarry fled: My deadly arrow flew, And as the dying creature bled, The giant met my view. Great fear and pain oppress my heart That dreads the coming blow, And through my left eye keenly dart The throbs that herald woe. Ah Lakshma G, all these signs dismay, My soul that sinks with dread, I know my love is torn away, Or, haply, she is dead.” Canto LIX. Ráma's Return. When Ráma saw his brother stand With none beside him, all unmanned, Eager he questioned why he came So far without the Maithil dame: “Where is my wife, my darling, she Who to the wild wood followed me? Where hast thou left my lady, where The dame who chose my lot to share? Where is my love who balms my woe As through the forest wilds I go, Unkinged and banished and disgraced,— My darling of the dainty waist?
- **Translation**: 

---

### Verse 12 (Ramayana 0.1077)
- **Original**: Canto LIX. Ráma's Return. 1059 She nerves my spirit for the strife, She, only she gives zest to life, Dear as my breath is she who vies In charms with daughters of the skies. If Janak's child be mine no more, In splendour fair as virgin ore, The lordship of the skies and earth To me were prize of little worth. Ah, lives she yet, the Maithil dame, Dear as the soul within this frame? O, let not all my toil be vain, The banishment, the woe and pain! O, let not dark Kaikeyí win The guerdon of her treacherous sin, If, Sítá lost, my days I end, And thou without me homeward wend! O, let not good Kau[alyá shed Her bitter tears to mourn me dead, Nor her proud rival's hest obey, Strong in her son and queenly sway! Back to my cot will I repair If Sítá live to greet me there, [299] But if my wife have perished, I Reft of my love will surely die. O Lakshma G, if I seek my cot, Look for my love and find her not Sweet welcome with her smile to give, I tell thee, I will cease to live. O answer,— let thy words be plain,— Lives Sítá yet, or is she slain? Didst thou thy sacred trust betray Till ravening giants seized the prey? Ah me, so young, so soft and fair, Lapped in all bliss, untried by care,
- **Translation**: 

---

### Verse 13 (Ramayana 0.1078)
- **Original**: 1060 The Ramayana Rent from her own dear husband, how Will she support her misery now? That voice, O LakshmaG smote thine ear, And filled, I ween, thy heart with fear, When on thy name for succour cried The treacherous giant ere he died. That voice too like mine own, I ween, Was heard by the Videhan queen. She bade thee seek my side to aid, And quickly was the hest obeyed, But ah, thy fault I needs must blame, To leave alone the helpless dame, And let the cruel giants sate The fury of their murderous hate. Those blood-devouring demons all Grieve in their souls for Khara's fall, And Sítá, none to guard her side, Torn by their cruel hands has died. I sink, O tamer of thy foes, Deep in the sea of whelming woes. What can I now? I must endure The mighty grief that mocks at cure.” Thus, all his thoughts on Sítá bent, To Janasthán the chieftain went, Hastening on with eager stride, And Lakshma G hurried by his side. With toil and thirst and hunger worn, His breast with doubt and anguish torn, He sought the well-known spot. Again, again he turned to chide With quivering lips which terror dried: He looked, and found her not. Within his leafy home he sped,
- **Translation**: 

---

### Verse 14 (Ramayana 0.1079)
- **Original**: Canto LX. Lakshman Reproved. 1061 Each pleasant spot he visited Where oft his darling strayed. “'Tis as I feared,” he cried, and there, Yielding to pangs too great to bear, He sank by grief dismayed. Canto LX. Lakshman Reproved. But Ráma ceased not to upbraid, His brother for untimely aid, And thus, while anguish wrung his breast, The chief with eager question pressed: “Why, LakshmaG, didst thou hurry hence And leave my wife without defence? I left her in the wood with thee, And deemed her safe from jeopardy. When first thy form appeared in view, I marked that Sítá came not too. With woe my troubled soul was rent, Prophetic of the dire event. Thy coming steps afar I spied, I saw no Sítá by thy side, And felt a sudden throbbing dart Through my left eye, and arm, and heart.”
- **Translation**: 

---

### Verse 15 (Ramayana 0.1080)
- **Original**: 1062 The Ramayana Lakshma G, with Fortune's marks impressed, His brother mournfully addressed: “Not by my heart's free impulse led, Leaving thy wife to thee I sped; But by her keen reproaches sent, O Ráma, to thine aid I went. She heard afar a mournful cry, “O save me, LakshmaG, or I die.” The voice that spoke in moving tone Smote on her ear and seemed thine own. Soon as those accents reached her ear She yielded to her woe and fear, She wept o'ercome by grief, and cried, “Fly, LakshmaG, fly to Ráma's side.” Though many a time she bade me speed, Her urgent prayer I would not heed. I bade her in thy strength confide, And thus with tender words replied: “No giant roams the forest shade From whom thy lord need shrink dismayed. No human voice, believe me, spoke Those words thy causeless fear that woke. Can he whose might can save in woe The heavenly Gods e'er stoop so low, And with those piteous accents call For succour like a caitiff thrall? And why should wandering giants choose The accents of thy lord to use, In alien tones my help to crave, And cry aloud, O LakshmaG, save? Now let my words thy spirit cheer, Compose thy thoughts and banish fear. In hell, in earth, or in the skies There is not, and there cannot rise
- **Translation**: 

---

### Verse 16 (Ramayana 0.1081)
- **Original**: Canto LX. Lakshman Reproved. 1063 A champion whose strong arm can slay Thy Ráma in the battle fray. To heavenly hosts he ne'er would yield Though Indra led them to the field.” To soothe her thus I vainly sought: Her heart with woe was still distraught. While from her eyes the waters ran Her bitter speech she thus began: “Too well I see thy dark intent: Thy lawless thoughts on me are bent. Thou hopest, but thy hope is vain, To win my love, thy brother slain. Not love, but Bharat's dark decree To share his exile counselled thee, [300] Or hearing now his bitter cry Thou surely to his aid wouldst fly. For love of me, a stealthy foe Thou choosest by his side to go, And now thou longest that my lord Should die, and wilt no help afford.” Such were the words the lady said: With angry fire my eyes were red. With pale lips quivering in my rage I hastened from the hermitage.” He ceased; and frenzied by his pain The son of Raghu spoke again: “O brother, for thy fault I grieve, The Maithil dame alone to leave. Thou knowest that my arm is strong To save me from the giant throng, And yet couldst leave the cottage, spurred To folly by her angry word. For this thy deed I praise thee not,—
- **Translation**: 

---

### Verse 17 (Ramayana 0.1082)
- **Original**: 1064 The Ramayana To leave her helpless in the cot, And thus thy sacred charge forsake For the wild words a woman spake. Yea thou art all to blame herein, And very grievous is thy sin. That anger swayed thy faithless breast And made thee false to my behest. An arrow speeding from my bow Has laid the treacherous giant low, Who lured me eager for the chase Far from my hermit dwelling-place. The string with easy hand I drew, The arrow as in pastime flew, The wounded quarry bled. The borrowed form was cast away, Before mine eye a giant lay With bright gold braceleted. My arrow smote him in the chest: The giant by the pain distressed Raised his loud voice on high. Far rang the mournful sound: mine own, It seemed, were accent, voice, and tone, They made thee leave my spouse alone And to my rescue fly.” Canto LXI. Ráma's Lament. As Ráma sought his leafy cot Through his left eye keen throbbings shot, His wonted strength his frame forsook, And all his body reeled and shook.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1083)
- **Original**: Canto LXI. Ráma's Lament. 1065 Still on those dreadful signs he thought,— Sad omens with disaster fraught, And from his troubled heart he cried, “O, may no ill my spouse betide!” Longing to gaze on Sítá's face He hastened to his dwelling-place, Then sinking neath his misery's weight, He looked and found it desolate. Tossing his mighty arms on high He sought her with an eager cry, From spot to spot he wildly ran Each corner of his home to scan. He looked, but Sítá was not there; His cot was disolate and bare, Like streamlet in the winter frost, The glory of her lilies lost. With leafy tears the sad trees wept As a wild wind their branches swept. Mourned bird and deer, and every flower Drooped fainting round the lonely bower. The silvan deities had fled The spot where all the light was dead, Where hermit coats of skin displayed, And piles of sacred grass were laid. He saw, and maddened by his pain Cried in lament again, again: “Where is she, dead or torn away, Lost, or some hungry giant's prey? Or did my darling chance to rove For fruit and blossoms though the grove? Or has she sought the pool or rill, Her pitcher from the wave to fill?” His eager eyes on fire with pain He roamed about with maddened brain.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1084)
- **Original**: 1066 The Ramayana Each grove and glade he searched with care, He sought, but found no Sítá there. He wildly rushed from hill to hill; From tree to tree, from rill to rill, As bitter woe his bosom rent Still Ráma roamed with fond lament: “O sweet Kadamba say has she Who loved thy bloom been seen by thee? If thou have seen her face most fair, Say, gentle tree, I pray thee, where. O Bel tree with thy golden fruit Round as her breast, no more be mute, Where is my radiant darling, gay In silk that mocks thy glossy spray? O Arjun, say, where is she now Who loved to touch thy scented bough? Do not thy graceful friend forget, But tell me, is she living yet? Speak, Basil, thou must surely know, For like her limbs thy branches show,— Most lovely in thy fair array Of twining plant and tender spray. Sweet Tila, fairest of the trees, Melodious with the hum of bees, Where is my darling Sítá, tell,— The dame who loved thy flowers so well? A [oka, act thy gentle part,— Named Heartsease,507 give me what thou art, To these sad eyes my darling show And free me from this load of woe. O Palm, in rich ripe fruitage dressed Round as the beauties of her breast,[301] 507 A[oka is compounded ofa not and[oka grief.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1085)
- **Original**: Canto LXI. Ráma's Lament. 1067 If thou have heart to know and feel, My peerless consort's fate reveal. Hast thou, Rose-apple, chanced to view My darling bright with golden hue? If thou have seen her quickly speak, Where is the dame I wildly seek? O glorious Cassia, thou art gay With all thy loveliest bloom to-day, Where is my dear who loved to hold In her full lap thy flowery gold?” To many a tree and plant beside, To Jasmin, Mango, Sál, he cried. “Say, hast thou seen, O gentle deer, The fawn-eyed Sítá wandering here? It may be that my love has strayed To sport with fawns beneath the shade, If thou, great elephant, have seen My darling of the lovely mien, Whose rounded limbs are soft and fine As is that lissome trunk of thine, O noblest of wild creatures, show Where is the dame thou needs must know. O tiger, hast thou chanced to see My darling? very fair is she, Cast all thy fear away, declare, Where is my moon-faced darling, where? There, darling of the lotus eye, I see thee, and 'tis vain to fly, Wilt thou not speak, dear love? I see Thy form half hidden by the tree. Stay if thou love me, Sítá, stay In pity cease thy heartless play. Why mock me now? thy gentle breast Was never prone to cruel jest.
- **Translation**: 

---

