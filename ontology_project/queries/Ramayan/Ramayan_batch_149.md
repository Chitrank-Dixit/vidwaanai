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

### Verse 1 (Ramayana 0.1006)
- **Original**: 988 The Ramayana And sapphires tip its branching horns. Resplendent as the lunar way, Or the first blush of opening day, With graceful form and radiant hue It charmed thy heart, O chieftain, too.” He heard her speech with willing ear, He looked again upon the deer. Its lovely shape his breast beguiled Moved by the prayer of Janak's child, And yielding for her pleasure's sake, To LakshmaG Ráma turned and spake: “Mark, LakshmaG, mark how Sítá's breast With eager longing is possessed. To-day this deer of wondrous breed Must for his passing beauty bleed, Brighter than e'er in Nandan strayed, Or Chaitraratha's heavenly shade. How should the groves of earth possess Such all-surpassing loveliness! The hair lies smooth and bright and fine, Or waves upon each curving line, And drops of living gold bedeck The beauty of his side and neck. O look, his crimson tongue between His teeth like flaming fire is seen, Flashing, whene'er his lips he parts, As from a cloud the lightning darts. O see his sunlike forehead shine With emerald tints and almandine, While pearly light and roseate glow Of shells adorn his neck below. No eye on such a deer can rest
- **Translation**: 

---

### Verse 2 (Ramayana 0.1007)
- **Original**: Canto XLIII. The Wondrous Deer. 989 But soft enchantment takes the breast: No man so fair a thing behold Ablaze with light of radiant gold, Celestial, bright with jewels' sheen, Nor marvel when his eyes have seen. A king equipped with bow and shaft Delights in gentle forest craft, And as in boundless woods he strays The quarry for the venison slays. There as he wanders with his train A store of wealth he oft may gain. He claims by right the precious ore, He claims the jewels' sparkling store. Such gains are dearer in his eyes Than wealth that in his chamber lies, The dearest things his spirit knows, Dear as the bliss whichZukra chose. But oft the rich expected gain Which heedless men pursue in vain, The sage, who prudent counsels know, Explain and in a moment show. This best of deer, this gem of all, To yield his precious spoils must fall, And tender Sítá by my side Shall sit upon the golden hide. Ne'er could I find so rich a coat On spotted deer or sheep or goat. No buck or antelope has such, So bright to view, so soft to touch. This radiant deer and one on high That moves in glory through the sky, Alike in heavenly beauty are, One on the earth and one a star. But, brother, if thy fears be true,
- **Translation**: 

---

### Verse 3 (Ramayana 0.1008)
- **Original**: 990 The Ramayana And this bright creature that we view Be fierce Márícha in disguise, Then by this hand he surely dies. For that dire fiend who spurns control With bloody hand and cruel soul, Has roamed this forest and dismayed The holiest saints who haunt the shade. Great archers, sprung of royal race, Pursuing in the wood the chase, Have fallen by his wicked art, And now my shaft shall strike his heart. Vatápi, by his magic power[280] Made heedless saints his flesh devour, Then, from within their frames he rent Forth bursting from imprisonment. But once his art in senseless pride Upon the mightiest saint he tried, Agastya's self, and caused him taste The baited meal before him placed. Vátápi, when the rite was o'er, Would take the giant form he wore, But Saint Agastya knew his wile And checked the giant with smile. “Vátápi, thou with cruel spite Hast conquered many an anchorite The noblest of the Bráhman caste,— And now thy ruin comes at last.” Now if my power he thus defies, This giant, like Vátápi dies, Daring to scorn a man like me, A self subduing devotee. Yea, as Agastya slew the foe, My hand shall lay Márícha low Clad in thine arms thy bow in hand,
- **Translation**: 

---

### Verse 4 (Ramayana 0.1009)
- **Original**: Canto XLIV. Márícha's Death. 991 To guard the Maithil lady stand, With watchful eye and thoughtful breast Keeping each word of my behest I go, and hunting through the brake This wondrous deer will bring or take. Yea surely I will bring the spoil Returning from my hunter's toil See, LakshmaG how my consort's eyes Are longing for the lovely prize. This day it falls, that I may win The treasure of so fair a skin. Do thou and Sítá watch with care Lest danger seize you unaware. Swift from my bow one shaft will fly; The stricken deer will fall and die Then quickly will I strip the game And bring the trophy to my dame. Jamáyus, guardian good and wise, Our old and faithful friend, The best and strongest bird that flies, His willing aid will lend The Maithil lady well protect, For every chance provide, And in thy tender care suspect A foe on every side.” Canto XLIV. Márícha's Death.
- **Translation**: 

---

### Verse 5 (Ramayana 0.1010)
- **Original**: 992 The Ramayana Thus having warned his brother bold He grasped his sword with haft of gold, And bow with triple flexure bent, His own delight and ornament; Then bound two quivers to his side, And hurried forth with eager stride. Soon as the antlered monarch saw The lord of monarchs near him draw, A while with trembling heart he fled, Then turned and showed his stately head. With sword and bow the chief pursued Where'er the fleeing deer he viewed Sending from dell and lone recess The splendour of his loveliness. Now full in view the creature stood Now vanished in the depth of wood; Now running with a languid flight, Now like a meteor lost to sight. With trembling limbs away he sped; Then like the moon with clouds o'erspread Gleamed for a moment bright between The trees, and was again unseen. Thus in the magic deer's disguise Márícha lured him to the prize, And seen a while, then lost to view, Far from his cot the hero drew. Still by the flying game deceived The hunter's heart was wroth and grieved, And wearied with the fruitless chase He stayed him in a shady place. Again the rover of the night Enraged the chieftain, full in sight, Slow moving in the coppice near, Surrounded by the woodland deer.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1011)
- **Original**: Canto XLIV. Márícha's Death. 993 Again the hunter sought the game That seemed a while to court his aim: But seized again with sudden dread, Beyond his sight the creature fled. Again the hero left the shade, Again the deer before him strayed. With surer hope and stronger will The hunter longed his prey to kill. Then as his soul impatient grew, An arrow from his side he drew, Resplendent at the sunbeam's glow, The crusher of the smitten foe. With skillful heed the mighty lord Fixed well shaft and strained the cord. Upon the deer his eyes he bent, And like a fiery serpent went The arrow Brahma's self had framed, Alive with sparks that hissed and flamed, Like Indra's flashing levin, true To the false deer the missile flew Cleaving his flesh that wonderous dart Stood quivering in Márícha's heart. Scarce from the ground one foot he sprang, Then stricken fell with deadly pang. Half lifeless, as he pressed the ground, He gave a roar of awful sound And ere the wounded giant died He threw his borrowed form aside Remembering still his lord's behest He pondered in his heart how best Sítá might send her guard away, And RávaG seize the helpless prey. The monster knew the time was nigh, And called aloud with eager cry,
- **Translation**: 

---

### Verse 7 (Ramayana 0.1012)
- **Original**: 994 The Ramayana “Ho, Sítá, LakshmaG” and the tone[281] He borrowed was like Ráma's own. So by that matchless arrow cleft, The deer's bright form Márícha left, Resumed his giant shape and size And closed in death his languid eyes. When Ráma saw his awful foe Gasp, smeared with blood, in deadly throe, His anxious thoughts to Sítá sped, And the wise words that LakshmaG said, That this was false Márícha's art, Returned again upon his heart. He knew the foe he triumphed o'er The name of great Márícha bore. “The fiend,” he pondered, 'ere he died, “Ho, LakshmaG! ho, my Sítá!” cried Ah, if that cry has reached her ear, How dire must be my darling's fear! And Lakshma G of the mighty arm, What thinks he in his wild alarm? As thus he thought in sad surmise, Each startled hair began to rise, And when he saw the giant slain And thought upon that cry again, His spirit sank and terror pressed Full sorely on the hero's breast. Another deer he chased and struck, He bore away the the fallen buck, To Janasthán then turned his face And hastened to his dwelling place.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1013)
- **Original**: Canto XLV. Lakshman's Departure. 995 Canto XLV. Lakshman's Departure. But Sítá hearing as she thought, Her husband's cry with anguish fraught, Called to her guardian,“Lakshma G, run And in the wood seek Raghu's son. Scarce can my heart retain its throne, Scarce can my life be called mine own, As all my powers and senses fail At that long, loud and bitter wail. Haste to the wood with all thy speed And save thy brother in his need. Go, save him in the distant glade Where loud he calls, for timely aid. He falls beneath some giant foe— A bull whom lions overthrow.” Deaf to her prayer, no step he stirred Obedient to his mother's word, Then Janak's child, with ire inflamed, In words of bitter scorn exclaimed exclaimed “Sumitrá's son, a friend in show, Thou art in truth thy brother's foe, Who canst at such any hour deny Thy succour and neglect his cry. Yes, LakshmaG, smit with love of me Thy brother's death thou fain wouldst see. This guilty love thy heart has swayed And makes thy feet so loth to aid. Thou hast no love for Ráma, no: Thy joy is vice, thy thoughts are low Hence thus unmoved thou yet canst stay While my dear lord is far away.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1014)
- **Original**: 996 The Ramayana If aught of ill my lord betide Who led thee here, thy chief and guide, Ah, what will be my hapless fate Left in the wild wood desolate!” Thus spoke the lady sad with fear, With many a sigh and many a tear, Still trembling like a captured doe: And Lakshma G spoke to calm her woe: “Videhan Queen, be sure of this,— And at the thought thy fear dismiss,— Thy husband's mightier power defies All Gods and angels of the skies, Gandharvas, and the sons of light, Serpents, and rovers of the night. I tell thee, of the sons of earth, Of Gods who boast celestial birth, Of beasts and birds and giant hosts, Of demigods, Gandharvas, ghosts, Of awful fiends, O thou most fair, There lives not one whose heart would dare To meet thy Ráma in the fight, Like Indra's self unmatched in might. Such idle words thou must not say Thy Ráma lives whom none may slay. I will not, cannot leave thee here In the wild wood till he be near. The mightiest strength can ne'er withstand His eager force, his vigorous hand. No, not the triple world allied With all the immortal Gods beside. Dismiss thy fear, again take heart, Let all thy doubt and woe depart.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1015)
- **Original**: Canto XLV. Lakshman's Departure. 997 Thy lord, be sure, will soon be here And bring thee back that best of deer. Not his, not his that mournful cry, Nor haply came it from the sky. Some giant's art was busy there And framed a castle based on air. A precious pledge art thou, consigned To me by him of noblest mind, Nor can I fairest dame, forsake The pledge which Ráma bade me take. Upon our heads, O Queen, we drew The giants' hate when Ráma slew Their chieftain Khara, and the shade Of Janasthán in ruin laid. Through all this mighty wood they rove With varied cries from grove to grove On rapine bent they wander here: But O, dismiss thy causeless fear.” Bright flashed her eye as LakshmaG spoke And forth her words of fury broke Upon her truthful guardian, flung With bitter taunts that pierced and stung: “Shame on such false compassion, base Defiler of thy glorious race! 'Twere joyous sight I ween to thee [282] My lord in direst strait to see. Thou knowest Ráma sore bested, Or word like this thou ne'er hadst said. No marvel if we find such sin In rivals false to kith and kin. Wretches like thee of evil kind, Concealing crime with crafty mind. Thou, wretch, thine aid wilt still deny,
- **Translation**: 

---

### Verse 11 (Ramayana 0.1016)
- **Original**: 998 The Ramayana And leave my lord alone to die. Has love of me unnerved thy hand, Or Bharat's art this ruin planned? But be the treachery his or thine, In vain, in vain the base design. For how shall I, the chosen bride Of dark-hued Ráma, lotus-eyed, The queen who once called Ráma mine, To love of other men decline? Believe me, LakshmaG, Ráma's wife Before thine eyes will quit this life, And not a moment will she stay If her dear lord have passed away.” The lady's bitter speech, that stirred Each hair upon his frame, he heard. With lifted hands together laid, His calm reply he gently made: “No words have I to answer now: My deity, O Queen, art thou. But 'tis no marvel, dame, to find Such lack of sense in womankind. Throughout this world, O Maithil dame, Weak women's hearts are still the same. Inconstant, urged by envious spite, They sever friends and hate the right. I cannot brook, Videhan Queen, Thy words intolerably keen. Mine ears thy fierce reproaches pain As boiling water seethes the brain. And now to bear me witness all The dwellers in the wood I call, That, when with words of truth I plead,
- **Translation**: 

---

### Verse 12 (Ramayana 0.1017)
- **Original**: Canto XLV. Lakshman's Departure. 999 This harsh reply is all my meed. Ah, woe is thee! Ah, grief, that still Eager to do my brother's will, Mourning thy woman's nature, I Must see thee doubt my truth and die. I fly to Ráma's side, and Oh, May bliss attend thee while I go! May all attendant wood-gods screen Thy head from harm, O large-eyed Queen! And though dire omens meet my sight And fill my soul with wild affright, May I return in peace and see The son of Raghu safe with thee!” The child of Janak heard him speak, And the hot tear-drops down her cheek, Increasing to a torrent, ran, As thus once more the dame began: “O Lakshma G, if I widowed be Godávarí's flood shall cover me, Or I will die by cord, or leap, Life weary, from yon rocky steep; Or deadly poison will I drink, Or 'neath the kindled flames will sink, But never, reft of Ráma, can Consent to touch a meaner man.” The Maithil dame with many sighs, And torrents pouring from her eyes, The faithful LakshmaG thus addressed, And smote her hands upon her breast. >Sumitrá's son, o'erwhelmed by fears, Looked on the large-eyed queen: He saw that flood of burning tears,
- **Translation**: 

---

### Verse 13 (Ramayana 0.1018)
- **Original**: 1000 The Ramayana He saw that piteous mien. He yearned sweet comfort to afford, He strove to soothe her pain; But to the brother of her lord She spoke no word again. His reverent hands once more he raised, His head he slightly bent, Upon her face he sadly gazed, And then toward Ráma went. Canto XLVI. The Guest. The angry LakshmaG scarce could brook Her bitter words, her furious look. With dark forebodings in his breast To Ráma's side he quickly pressed. Then ten necked RávaG saw the time Propitious for his purposed crime. A mendicant in guise he came And stood before the Maithil dame. His garb was red, with tufted hair And sandalled feet a shade he bare, And from the fiend's left shoulder slung A staff and water-vessel hung. Near to the lovely dame he drew, While both the chiefs were far from view, As darkness takes the evening air When neither sun nor moon is there. He bent his eye upon the dame, A princess fair, of spotless fame:
- **Translation**: 

---

### Verse 14 (Ramayana 0.1019)
- **Original**: Canto XLVI. The Guest. 1001 So might some baleful planet be Near Moon-forsaken RohiGí.495 As the fierce tyrant nearer drew, The trees in Janasthán that grew Waved not a leaf for fear and woe, And the hushed wind forbore to blow. Godávarí's waters as they fled, Saw his fierce eye-balls flashing red, And from each swiftly-gliding wave A melancholy murmur gave. Then RávaG, when his eager eye Beheld the longed-for moment nigh, In mendicant's apparel dressed Near to the Maithil lady pressed. [283] In holy guise, a fiend abhorred, He found her mourning for her lord. Thus threatening drawsZani[char496 nigh To Chitrá497 in the evening sky; Thus the deep well by grass concealed Yawns treacherous in the verdant field. He stood and looked upon the dame Of Ráma, queen of spotless fame With her bright teeth and each fair limb Like the full moon she seemed to him, Sitting within her leafy cot, Weeping for woe that left her not. Thus, while with joy his pulses beat, He saw her in her lone retreat, Eyed like the lotus, fair to view In silken robes of amber hue. Pierced to the core by Káma's dart 495 The favourite wife of the Moon. 496 The planet Saturn. 497 Another favourite of the Moon; one of the lunar mansions.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1020)
- **Original**: 1002 The Ramayana He murmured texts with lying art, And questioned with a soft address The lady in her loneliness. The fiend essayed with gentle speech The heart of that fair dame to reach, Pride of the worlds, like Beauty's Queen Without her darling lotus seen: “O thou whose silken robes enfold A form more fair than finest gold, With lotus garland on thy head, Like a sweet spring with bloom o'erspread, Who art thou, fair one, what thy name, Beauty, or Honour, Fortune, Fame, Spirit, or nymph, or Queen of love Descended from thy home above? Bright as the dazzling jasmine shine Thy small square teeth in level line. Like two black stars aglow with light Thine eyes are large and pure and bright. Thy charms of smile and teeth and hair And winning eyes, O thou most fair, Steal all my spirit, as the flow Of rivers mines the bank below. How bright, how fine each flowing tress! How firm those orbs beneath thy dress! That dainty waist with ease were spanned, Sweet lady, by a lover's hand. Mine eyes, O beauty, ne'er have seen Goddess or nymph so fair of mien, Or bright Gandharva's heavenly dame, Or woman of so perfect frame. In youth's soft prime thy years are few, And earth has naught so fair to view.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1021)
- **Original**: Canto XLVI. The Guest. 1003 I marvel one like thee in face Should make the woods her dwelling-place. Leave, lady, leave this lone retreat In forest wilds for thee unmeet, Where giants fierce and strong assume All shapes and wander in the gloom. These dainty feet were formed to tread Some palace floor with carpets spread, Or wander in trim gardens where Each opening bud perfumes the air. The richest robe thy form should deck, The rarest gems adorn thy neck, The sweetest wreath should bind thy hair, The noblest lord thy bed should share. Art thou akin, O fair of form, To Rudras,498 or the Gods of storm,499 Or to the glorious Vasus500? How Can less than these be bright as thou? But never nymph or heavenly maid Or Goddess haunts this gloomy shade. Here giants roam, a savage race; What led thee to so dire a place? Here monkeys leap from tree to tree, And bears and tigers wander free; Here ravening lions prowl, and fell Hyenas in the thickets yell, And elephants infuriate roam, Mighty and fierce, their woodland home. Dost thou not dread, so soft and fair, Tiger and lion, wolf and bear? 498 The Rudras, agents in creation, are eight in number; they sprang from the forehead of Brahmá. 499 Maruts, the attendants of Indra. 500 Radiant demi-gods.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1022)
- **Original**: 1004 The Ramayana Hast thou, O beauteous dame, no fear In the wild wood so lone and drear? Whose and who art thou? whence and why Sweet lady, with no guardian nigh, Dost thou this awful forest tread By giant bands inhabited?” The praise the high-souled RávaG spoke No doubt within her bosom woke. His saintly look and Bráhman guise Deceived the lady's trusting eyes. With due attention on the guest Her hospitable rites she pressed. She bade the stranger to a seat, And gave him water for his feet. The bowl and water-pot he bare, And garb which wandering Bráhmans wear Forbade a doubt to rise. Won by his holy look she deemed The stranger even as he seemed To her deluded eyes. Intent on hospitable care, She brought her best of woodland fare, And showed her guest a seat. She bade the saintly stranger lave His feet in water which she gave, And sit and rest and eat. He kept his eager glances bent On her so kindly eloquent, Wife of the noblest king; And longed in heart to steal her thence, Preparing by the dire offence, Death on his head to bring.[284]
- **Translation**: 

---

### Verse 18 (Ramayana 0.1023)
- **Original**: Canto XLVII. Rávan's Wooing. 1005 The lady watched with anxious face For Ráma coming from the chase With LakshmaG by his side: But nothing met her wandering glance Save the wild forest's green expanse Extending far and wide. Canto XLVII. Rávan's Wooing. As, clad in mendicant's disguise, He questioned thus his destined prize, She to the seeming saintly man The story of her life began. “My guest is he,” she thought,“and I, To 'scape his curse, must needs reply:” “Child of a noble sire I spring From Janak, fair Videha's king. May every good be thine! my name Is Sítá, Ráma's cherished dame. Twelve winters with my lord I spent Most happily with sweet content In the rich home of Raghu's line, And every earthly joy was mine. Twelve pleasant years flew by, and then His peers advised the king of men, Ráma, my lord, to consecrate Joint ruler of his ancient state. But when the rites were scarce begun, To consecrate Ikshváku's son, The queen Kaikeyí, honoured dame, Sought of her lord an ancient claim.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1024)
- **Original**: 1006 The Ramayana Her plea of former service pressed, And made him grant her new request, To banish Ráma to the wild And consecrate instead her child. This double prayer on him, the best And truest king, she strongly pressed: “Mine eyes in sleep I will not close, Nor eat, nor drink, nor take repose. This very day my death shall bring If Ráma be anointed king.” As thus she spake in envious ire, The aged king, my husband's sire, Besought with fitting words; but she Was cold and deaf to every plea. As yet my days are few; eighteen The years of life that I have seen; And Ráma, best of all alive, Has passed of years a score and five— Ráma the great and gentle, through All region famed as pure and true, Large-eyed and mighty-armed and tall, With tender heart that cares for all. But Da[aratha, led astray By woman's wile and passion's sway, By his strong love of her impelled, The consecrating rites withheld. When, hopeful of the promised grace, My Ráma sought his father's face, The queen Kaikeyí, ill at ease, Spoke to my lord brief words like these: “Hear, son of Raghu, hear from me The words thy father says to thee: “I yield this day to Bharat's hand, Free from all foes, this ancient land.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1025)
- **Original**: Canto XLVII. Rávan's Wooing. 1007 Fly from this home no longer thine, And dwell in woods five years and nine. Live in the forest and maintain Mine honour pure from falsehood's stain.’ ” Then Ráma spoke, untouched by dread: “Yea, it shall be as thou hast said.” And answered, faithful to his vows, Obeying Da[aratha's spouse: “The offered realm I would not take, But still keep true the words he spake.” Thus, gentle Bráhman, Ráma still Clung to his vow with firmest will. And valiant LakshmaG, dear to fame, His brother by a younger dame, Bold victor in the deadly fray, Would follow Ráma on his way. On sternest vows his heart was set, And he, a youthful anchoret, Bound up in twisted coil his hair And took the garb which hermits wear; Then with his bow to guard us, he Went forth with Ráma and with me. By Queen Kaikeyí's art bereft The kingdom and our home we left, And bound by stern religious vows We sought this shade of forest boughs. Now, best of Bráhmans, here we tread These pathless regions dark and dread. But come, refresh thy soul, and rest Here for a while an honoured guest, For he, my lord, will soon be here With fresh supply of woodland cheer, Large store of venison of the buck, Or some great boar his hand has struck.
- **Translation**: 

---

