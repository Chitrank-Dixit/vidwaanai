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

### Verse 1 (Ramayan 0.241)
- **Original**: Canto LV. The Hermitage Burnt. 223 That Gods, and saints, and Titans wield, And every dart that arms the hands Of spirits, fiends and minstrel bands, Be mine, O Lord supreme in place, This token of thy boundless grace.” The Lord of Gods then gave consent, And to his heavenly mansion went. Triumphant in the arms he held, The monarch's breast with glory swelled. So swells the ocean, when upon His breast the full moon's beams have shone. Already in his mind he viewed Va [ishmha at his feet subdued. He sought that hermit's grove, and there Launched his dire weapons through the air, Till scorched by might that none could stay The hermitage in ashes lay. Where'er the inmates saw, aghast, The dart that Vi[vámitra cast, To every side they turned and fled In hundreds forth disquieted. Va [ishmha's pupils caught the fear, And every bird and every deer, And fled in wild confusion forth Eastward and westward, south and north, And so Va[ishmha's holy shade A solitary wild was made, Silent awhile, for not a sound Disturbed the hush that was around.
- **Translation**: 

---

### Verse 2 (Ramayan 0.242)
- **Original**: 224 The Ramayana Va [ishmha then, with eager cry, Called,“Fear not, friends, nor seek to fly. This son of Gádhi dies to-day, Like hoar-frost in the morning's ray.” Thus having said, the glorious sage Spoke to the king in words of rage: “Because thou hast destroyed this grove Which long in holy quiet throve, By folly urged to senseless crime, Now shalt thou die before thy time.” Canto LVI. Visvámitra's Vow. But Vi[vámitra, at the threat Of that illustrious anchoret, Cried, as he launched with ready hand A fiery weapon,“Stand, O Stand!” Va [ishmha, wild with rage and hate, Raising, as 'twere the Rod of Fate, His mighty Bráhman wand on high, To Vi[vámitra made reply: “Nay, stand, O Warrior thou, and show What soldier can, 'gainst Bráhman foe. O Gádhi's son, thy days are told; Thy pride is tamed, thy dart is cold. How shall a warrior's puissance dare With Bráhman's awful strength compare? To-day, base Warrior, shall thou feel That God-sent might is more than steel.” He raised his Bráhman staff, nor missed The fiery dart that near him hissed:
- **Translation**: 

---

### Verse 3 (Ramayan 0.243)
- **Original**: Canto LVI. Visvámitra's Vow. 225 And quenched the fearful weapon fell, As flame beneath the billow's swell. Then Gádhi's son in fury threw Lord VaruG's arm and Rudra's too: Indra's fierce bolt that all destroys; That which the Lord of Herds employs: The Human, that which minstrels keep, The deadly Lure, the endless Sleep: The Yawner, and the dart which charms; Lament and Torture, fearful arms: The Terrible, the dart which dries, The Thunderbolt which quenchless flies, And Fate's dread net, and Brahmá's noose, And that which waits for VaruG's use: The dart he loves who wields the bow Pináka, and twin bolts that glow With fury as they flash and fly, The quenchless Liquid and the Dry: The dart of Vengeance, swift to kill: The Goblins' dart, the Curlew's Bill: [068] The discus both of Fate and Right, And VishGu's, of unerring flight: The Wind-God's dart, the Troubler dread, The weapon named the Horse's Head. From his fierce hand two spears were thrown, And the great mace that smashes bone; The dart of spirits of the air, And that which Fate exults to bear: The Trident dart which slaughters foes, And that which hanging skulls compose:233 233 “The names of many of these weapons which are mythical and partly alle- gorical have occurred in Canto XXIX. The general signification of the story is clear enough. It is a contest for supremacy between the regal or military order
- **Translation**: 

---

### Verse 4 (Ramayan 0.244)
- **Original**: 226 The Ramayana These fearful darts in fiery rain He hurled upon the saint amain, An awful miracle to view. But as the ceaseless tempest flew, The sage with wand of God-sent power Still swallowed up that fiery shower. Then Gádhi's son, when these had failed, With Brahmá's dart his foe assailed. The Gods, with Indra at their head, And Nágas, quailed disquieted, And saints and minstrels, when they saw The king that awful weapon draw; And the three worlds were filled with dread, And trembled as the missile sped. The saint, with Bráhman wand, empowered By lore divine that dart devoured. Nor could the triple world withdraw Rapt gazes from that sight of awe; For as he swallowed down the dart Of Brahmá, sparks from every part, From finest pore and hair-cell, broke Enveloped in a veil of smoke. The staff he waved was all aglow Like Yáma's sceptre, King below, Or like the lurid fire of Fate Whose rage the worlds will desolate. and Bráhmanical or priestly authority, like one of those struggles which our own Europe saw in the middle ages when without employing warlike weapons the priesthood frequently gained the victory.” SCHLEGEL {FNS . For a full account of the early contests between the Bráhmans and the Kshattriyas, see Muir's Original Sanskrit Texts (Second edition) Vol. I. Ch. IV.
- **Translation**: 

---

### Verse 5 (Ramayan 0.245)
- **Original**: Canto LVII. Trisanku. 227 The hermits, whom that sight had awed, Extolled the saint, with hymn and laud: “Thy power, O Sage, is ne'er in vain: Now with thy might thy might restrain. Be gracious, Master, and allow The worlds to rest from trouble now; For Vi[vámitra, strong and dread, By thee has been discomfited.” Then, thus addressed, the saint, well pleased, The fury of his wrath appeased. The king, o'erpowered and ashamed, With many a deep-drawn sigh exclaimed: “Ah! Warriors' strength is poor and slight; A Bráhman's power is truly might. This Bráhman staff the hermit held The fury of my darts has quelled. This truth within my heart impressed, With senses ruled and tranquil breast My task austere will I begin, And Bráhmanhood will strive to win.” Canto LVII. Trisanku. Then with his heart consumed with woe, Still brooding on his overthrow By the great saint he had defied, At every breath the monarch sighed. Forth from his home his queen he led, And to a land far southward fled. There, fruit and roots his only food,
- **Translation**: 

---

### Verse 6 (Ramayan 0.246)
- **Original**: 228 The Ramayana He practised penance, sense-subdued, And in that solitary spot Four virtuous sons the king begot: Havishyand, from the offering named, And Madhushyand, for sweetness famed, Mahárath, chariot-borne in fight, And Dri hanetra strong of sight. A thousand years had passed away, When Brahmá, Sire whom all obey, Addressed in pleasant words like these Him rich in long austerities: “Thou by the penance, Ku[ik's son, A place 'mid royal saints hast won. Pleased with thy constant penance, we This lofty rank assign to thee.” Thus spoke the glorious Lord most High Father of earth and air and sky, And with the Gods around him spread Home to his changeless sphere he sped. But Vi[vámitra scorned the grace, And bent in shame his angry face. Burning with rage, o'erwhelmed with grief, Thus in his heart exclaimed the chief: “No fruit, I ween, have I secured By strictest penance long endured, If Gods and all the saints decree To make but royal saint of me.” Thus pondering, he with sense subdued, With sternest zeal his vows renewed.[069]
- **Translation**: 

---

### Verse 7 (Ramayan 0.247)
- **Original**: Canto LVII. Trisanku. 229 Then reigned a monarch, true of soul, Who kept each sense in firm control; Of old Ikshváku's line he came, That glories in Tri[anku's234 name. Within his breast, O Raghu's child, Arose a longing, strong and wild, Great offerings to the Gods to pay, And win, alive, to heaven his way. His priest Va[ishmha's aid he sought, And told him of his secret thought. But wise Va[ishmha showed the hope Was far beyond the monarch's scope. Tri[anku then, his suit denied, Far to the southern region hied, To beg Va[ishmha's sons to aid The mighty plan his soul had made. There King Tri[anku, far renowned, Va [ishmha's hundred children found, Each on his fervent vows intent, For mind and fame preëminent. To these the famous king applied, Wise children of his holy guide. Saluting each in order due. His eyes, for shame, he downward threw, And reverent hands together pressed, The glorious company addressed: “I as a humble suppliant seek Succour of you who aid the weak. A mighty offering I would pay, 234 “Tri[anku, king of Ayodhyá, was seventh in descent from Ikshváku, and Da [aratha holds the thirty-fourth place in the same genealogy. See Canto LXX. We are thrown back, therefore, to very ancient times, and it occasions some surprise to find Va[ishmha and Vi[vámitra, actors in these occurences, still alive in Rama's time.”
- **Translation**: 

---

### Verse 8 (Ramayan 0.248)
- **Original**: 230 The Ramayana But sage Va[ishmha answered, Nay. Be yours permission to accord, And to my rites your help afford. Sons of my guide, to each of you With lowly reverence here I sue; To each, intent on penance-vow, O Bráhmans, low my head I bow, And pray you each with ready heart In my great rite to bear a part, That in the body I may rise And dwell with Gods within the skies. Sons of my guide, none else I see Can give what he refuses me. Ikshváku's children still depend Upon their guide most reverend; And you, as nearest in degree To him, my deities shall be!” Canto LVIII. Trisanku Cursed. Tri[anku's speech the hundred heard, And thus replied, to anger stirred: “Why foolish King, by him denied, Whose truthful lips have never lied, Dost thou transgress his prudent rule, And seek, for aid, another school?235 235 “It does not appear how Tri[anku, in asking the aid of Va[ishmha's sons after applying in vain to their father, could be charged with resorting to another [ákhá (School) in the ordinary sense of that word; as it is not conceivable that the sons should have been of anotherZákhá from the father, whose cause they espouse with so much warmth. The commentator in the Bombay edition
- **Translation**: 

---

### Verse 9 (Ramayan 0.249)
- **Original**: Canto LVIII. Trisanku Cursed. 231 Ikshváku's sons have aye relied Most surely on their holy guide: Then how dost thou, fond Monarch, dare Transgress the rule his lips declare? “Thy wish is vain,” the saint replied, And bade thee cast the plan aside. Then how can we, his sons, pretend In such a rite our aid to lend? O Monarch, of the childish heart, Home to thy royal town depart. That mighty saint, thy priest and guide, At noblest rites may well preside: The worlds for sacrifice combined A worthier priest could never find.” Such speech of theirs the monarch heard, Though rage distorted every word, And to the hermits made reply: “You, like your sire, my suit deny. For other aid I turn from you: So, rich in penance, Saints, adieu!” Va [ishmha's children heard, and guessed His evil purpose scarce expressed, And cried, while rage their bosoms burned, “Be to a vile ChaG ála236 turned!” [070] This said, with lofty thoughts inspired, Each to his own retreat retired. explains the wordZákhantaram as Yájanádiná rakshántaram,‘one who by sacrificing for thee, etc., will be another protector.’ Gorresio's Gau a text, which may often be used as a commentary on the older one, has the following paraphrase of the words in question, ch. 60, 3. Múlam uts[ijya kasmát tvam sákhásv ichhasi lambitum.‘Why, forsaking the root, dost thou desire to hang upon the branches?’ ”M UIR {FNS , Sanskrit Texts, Vol. I., p. 401. 236 A ChaG ála was a man born of the illegal and impure union of aZúdra with a woman of one of the three higher castes.
- **Translation**: 

---

### Verse 10 (Ramayan 0.250)
- **Original**: 232 The Ramayana That night Tri[anku underwent Sad change in shape and lineament. Next morn, an outcast swart of hue, His dusky cloth he round him drew. His hair had fallen from his head, And roughness o'er his skin was spread. Such wreaths adorned him as are found To flourish on the funeral ground. Each armlet was an iron ring: Such was the figure of the king, That every counsellor and peer, And following townsman, fled in fear. Alone, unyielding to dismay, Though burnt by anguish night and day, Great Vi[vámitra's side he sought, Whose treasures were by penance bought. The hermit with his tender eyes Looked on Tri[anku's altered guise, And grieving at his ruined state Addressed him thus, compassionate: “Great King,” the pious hermit said, “What cause thy steps has hither led, Ayodhyá's mighty Sovereign, whom A curse has plagued with outcast's doom?” In vile ChaG ála237 shape, the king Heard Vi[vámitra's questioning, And, suppliant palm to palm applied, With answering eloquence he cried: 237 “The ChaG ála was regarded as the vilest and most abject of the men sprung from wedlock forbidden by the law (Mánavadharma[ástra, Lib. X. 12.); a kind of social malediction weighed upon his head and rejected him from human society.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 11 (Ramayan 0.251)
- **Original**: Canto LVIII. Trisanku Cursed. 233 “My priest and all his sons refused To aid the plan on which I mused. Failing to win the boon I sought, To this condition I was brought. I, in the body, Saint, would fain A mansion in the skies obtain. I planned a hundred rites for this, But still was doomed the fruit to miss. Pure are my lips from falsehood's stain, And pure they ever shall remain,— Yea, by a Warrior's faith I swear,— Though I be tried with grief and care. Unnumbered rites to Heaven I paid, With righteous care the sceptre swayed; And holy priest and high-souled guide My modest conduct gratified. But, O thou best of hermits, they Oppose my wish these rites to pay; They one and all refuse consent, Nor aid me in my high intent. Fate is, I ween, the power supreme, Man's effort but an idle dream, Fate whirls our plans, our all away; Fate is our only hope and stay; Now deign, O blessed Saint, to aid Me, even me by Fate betrayed, Who come, a suppliant, sore distressed, One grace, O Hermit, to request. No other hope or way I see: No other refuge waits for me. Oh, aid me in my fallen state, And human will shall conquer Fate.”
- **Translation**: 

---

### Verse 12 (Ramayan 0.252)
- **Original**: 234 The Ramayana Canto LIX. The Sons Of Vasishtha. Then Ku[ik's son, by pity warmed, Spoke sweetly to the king transformed: “Hail! glory of Ikshváku's line: I know how bright thy virtues shine. Dismiss thy fear, O noblest Chief, For I myself will bring relief. The holiest saints will I invite To celebrate thy purposed rite: So shall thy vow, O King, succeed, And from thy cares shalt thou be freed. Thou in the form which now thou hast, Transfigured by the curse they cast,— Yea, in the body, King, shalt flee, Transported, where thou fain wouldst be. O Lord of men, I ween that thou Hast heaven within thy hand e'en now, For very wisely hast thou done, And refuge sought with Ku[ik's son.” Thus having said, the sage addressed His sons, of men the holiest, And bade the prudent saints whate'er Was needed for the rite prepare. The pupils he was wont to teach He summoned next, and spoke this speech: “Go bid Va[ishmha'a sons appear, And all the saints be gathered here. And what they one and all reply When summoned by this mandate high, To me with faithful care report, Omit no word and none distort.”
- **Translation**: 

---

### Verse 13 (Ramayan 0.253)
- **Original**: Canto LIX. The Sons Of Vasishtha. 235 The pupils heard, and prompt obeyed, To every side their way they made. Then swift from every quarter sped The sages in the Vedas read. Back to that saint the envoys came, Whose glory shone like burning flame, And told him in their faithful speech The answer that they bore from each: “Submissive to thy word, O Seer, The holy men are gathering here. By all was meet obedience shown: Mahodaya 238 refused alone. [071] And now, O Chief of hermits, hear What answer, chilling us with fear, Va [ishmha's hundred sons returned, Thick-speaking as with rage they burned: “How will the Gods and saints partake The offerings that the prince would make, And he a vile and outcast thing, His ministrant one born a king? Can we, great Bráhmans, eat his food, And think to win beatitude, By Vi[vámitra purified?” Thus sire and sons in scorn replied, And as these bitter words they said, Wild fury made their eyeballs red. Their answer when the arch-hermit heard, His tranquil eyes with rage were blurred; Great fury in his bosom woke, And thus unto the youths he spoke: “Me, blameless me they dare to blame, 238 This appellation, occuring nowhere else in the poem except as the name of a city, appears twice in this Canto as a name of Va[ishmha.
- **Translation**: 

---

### Verse 14 (Ramayan 0.254)
- **Original**: 236 The Ramayana And disallow the righteous claim My fierce austerities have earned: To ashes be the sinners turned. Caught in the noose of Fate shall they To Yáma's kingdom sink to-day. Seven hundred times shall they be born To wear the clothes the dead have worn. Dregs of the dregs, too vile to hate, The flesh of dogs their maws shall sate. In hideous form, in loathsome weed, A sad existence each shall lead. Mahodaya too, the fool who fain My stainless life would try to stain, Stained in the world with long disgrace Shall sink into a fowler's place. Rejoicing guiltless blood to spill, No pity through his breast shall thrill. Cursed by my wrath for many a day, His wretched life for sin shall pay.” Thus, girt with hermit, saint, and priest, Great Vi[vámitra spoke— and ceased. Canto LX. Trisanku's Ascension.
- **Translation**: 

---

### Verse 15 (Ramayan 0.255)
- **Original**: Canto LX. Trisanku's Ascension. 237 So with ascetic might, in ire, He smote the children and the sire. Then Vi[vámitra, far-renowned, Addressed the saints who gathered round: “See by my side Tri[anku stand, Ikshváku's son, of liberal hand. Most virtuous and gentle, he Seeks refuge in his woe with me. Now, holy men, with me unite, And order so his purposed rite That in the body he may rise And win a mansion in the skies.” They heard his speech with ready ear And, every bosom filled with fear Of Vi[vámitra, wise and great, Spoke each to each in brief debate: “The breast of Ku[ik's son, we know, With furious wrath is quick to glow. Whate'er the words he wills to say, We must, be very sure, obey. Fierce is our lord as fire, and straight May curse us all infuriate. So let us in these rites engage, As ordered by the holy sage. And with our best endeavour strive That King Ikshváku's son, alive, In body to the skies may go By his great might who wills it so.”
- **Translation**: 

---

### Verse 16 (Ramayan 0.256)
- **Original**: 238 The Ramayana Then was the rite begun with care: All requisites and means were there: And glorious Vi[vámitra lent His willing aid as president. And all the sacred rites were done By rule and use, omitting none. By chaplain-priest, the hymns who knew, In decent form and order due. Some time in sacrifice had past, And Vi[vámitra made, at last, The solemn offering with the prayer That all the Gods might come and share. But the Immortals, one and all, Refused to hear the hermit's call. Then red with rage his eyeballs blazed: The sacred ladle high he raised, And cried to King Ikshváku's son: “Behold my power, by penance won: Now by the might my merits lend, Ikshváku's child, to heaven ascend. In living frame the skies attain, Which mortals thus can scarcely gain. My vows austere, so long endured, Have, as I ween, some fruit assured. Upon its virtue, King, rely, And in thy body reach the sky.” His speech had scarcely reached its close, When, as he stood, the sovereign rose, And mounted swiftly to the skies Before the wondering hermits' eyes.
- **Translation**: 

---

### Verse 17 (Ramayan 0.257)
- **Original**: Canto LX. Trisanku's Ascension. 239 But Indra, when he saw the king His blissful regions entering, With all the army of the Blest Thus cried unto the unbidden guest: “With thy best speed, Tri[anku, flee: Here is no home prepared for thee. By thy great master's curse brought low, Go, falling headlong, earthward go.” Thus by the Lord of Gods addressed, Tri[anku fell from fancied rest, And screaming in his swift descent, “O, save me, Hermit!” down he went. And Vi[vámitra heard his cry, And marked him falling from the sky, And giving all his passion sway, Cried out in fury,“Stay, O stay!” [072] By penance-power and holy lore, Like Him who framed the worlds of yore, Seven other saints he fixed on high To star with light the southern sky. Girt with his sages forth he went, And southward in the firmament New wreathed stars prepared to set In many a sparkling coronet. He threatened, blind with rage and hate, Another Indra to create, Or, from his throne the ruler hurled, All Indraless to leave the world. Yea, borne away by passion's storm, The sage began new Gods to form. But then each Titan, God, and saint, Confused with terror, sick and faint, To high souled Vi[vámitra hied,
- **Translation**: 

---

### Verse 18 (Ramayan 0.258)
- **Original**: 240 The Ramayana And with soft words to soothe him tried: “Lord of high destiny, this king, To whom his master's curses cling, No heavenly home deserves to gain, Unpurified from curse and stain.” The son of Ku[ik, undeterred, The pleading of the Immortals heard, And thus in haughty words expressed The changeless purpose of his breast: “Content ye, Gods: I soothly sware Tri[anku to the skies to bear Clothed in his body, nor can I My promise cancel or deny. Embodied let the king ascend To life in heaven that ne'er shall end. And let these new-made stars of mine Firm and secure for ever shine. Let these, my work, remain secure Long as the earth and heaven endure. This, all ye Gods, I crave: do you Allow the boon for which I sue.” Then all the Gods their answer made: “So be it, Saint, as thou hast prayed. Beyond the sun's diurnal way Thy countless stars in heaven shall stay: And 'mid them hung, as one divine, Head downward shall Tri[anku shine; And all thy stars shall ever fling Their rays attendant on the king.”239 239 “The seven ancient rishis or saints, as has been said before, were the seven stars of Ursa Major. The seven other new saints which are here said to have been created by Vi[vámitra should be seven new southern stars, a sort of new Ursa. Von Schlegel thinks that this mythical fiction of new stars created by
- **Translation**: 

---

### Verse 19 (Ramayan 0.259)
- **Original**: Canto LXI. Sunahsepha. 241 The mighty saint, with glory crowned, With all the sages compassed round, Praised by the Gods, gave full assent, And Gods and sages homeward went. Canto LXI. Sunahsepha. Then Vi[vámitra, when the Blest Had sought their homes of heavenly rest, Thus, mighty Prince, his counsel laid Before the dwellers of the shade: “The southern land where now we are Offers this check our rites to bar:240 To other regions let us speed, And ply our tasks from trouble freed. Now turn we to the distant west. To Pushkar's241 wood where hermits rest, Vi[vámitra may signify that these southern stars, unknown to the Indians as long as they remained in the neighbourhood of the Ganges, became known to them at a later date when they colonized the southern regions of India.” G ORRESIO {FNS . 240 “This cannot refer to the events just related: for Vi[vámitra was successful in the sacrifice performed for Tri[anku. And yet no other impediment is mentioned. Still his restless mind would not allow him to remain longer in the same spot. So the character of Vi[vámitra is ingeniously and skilfully shadowed forth: as he had been formerly a most warlike king, loving battle and glory, bold, active, sometimes unjust, and more frequently magnanimous, such also he always shows himself in his character of anchorite and ascetic.” SCHLEGEL {FNS . 241 Near the modern city of Ajmere. The place is sacred still, and the name is preserved in the Hindí. Lassen, however, says that this Pushkala or Pushkara, called by the Grecian writers µÅºµ»wÄ¹Â, the earliest place of pilgrimage mentioned by name, is not to be confounded with the modern Pushkara in Ajmere.
- **Translation**: 

---

### Verse 20 (Ramayan 0.260)
- **Original**: 242 The Ramayana And there to rites austere apply, For not a grove with that can vie.” The saint, in glory's light arrayed, In Pushkar's wood his dwelling made, And living there on roots and fruit Did penance stern and resolute. The king who filled Ayodhyá's throne, By Ambarísha's name far known, At that same time, it chanced, began A sacrificial rite to plan. But Indra took by force away The charger that the king would slay. The victim lost, the Bráhman sped To Ambarísha's side, and said: “Gone is the steed, O King, and this Is due to thee, in care remiss.[073] Such heedless faults will kings destroy Who fail to guard what they enjoy. The flaw is desperate: we need The charger, or a man to bleed. Quick! bring a man if not the horse, That so the rite may have its course.”
- **Translation**: 

---

