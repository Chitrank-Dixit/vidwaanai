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

### Verse 1 (Ramayana 0.846)
- **Original**: 828 The Ramayana And Brahmá joying at the sight Welcomed the glorious anchorite. Canto VI. Ráma's Promise. When he his heavenly home had found, The holy men who dwelt around To Ráma flocked, whose martial fame Shone glorious as the kindled flame: Vaikhánasas415 who love the wild, Pure hermits Bálakhilyas416 styled, Good Samprakshálas,417 saints who live On rays which moon and daystar give: Those who with leaves their lives sustain And those who pound with stones their grain: And they who lie in pools, and those Whose corn, save teeth, no winnow knows: Those who for beds the cold earth use, And those who every couch refuse: And those condemned to ceaseless pains, Whose single foot their weight sustains: And those who sleep neath open skies, Whose food the wave or air supplies, And hermits pure who spend their nights 415 Hermits who live upon roots which they dig out of the earth: literally diggers, derived from the prefixviand khan to dig. 416 Generally, divine personages of the height of a man's thumb, produced from Brahmá's hair: here, according to the commentator followed by Gorresio, hermits who when they have obtained fresh food throw away what they had laid up before. 417 Sprung from the washings of VishGuu's feet.
- **Translation**: 

---

### Verse 2 (Ramayana 0.847)
- **Original**: Canto VI. Ráma's Promise. 829 On ground prepared for sacred rites; Those who on hills their vigil hold, Or dripping clothes around them fold: The devotees who live for prayer, Or the five fires418 unflinching bear. On contemplation all intent, With light that heavenly knowledge lent, They came to Ráma, saint and sage, InZarabhanga's hermitage. The hermit crowd around him pressed, And thus the virtuous chief addressed: “The lordship of the earth is thine, O Prince of old Ikshváku's line. Lord of the Gods is Indra, so Thou art our lord and guide below. Thy name, the glory of thy might, Throughout the triple world are bright: Thy filial love so nobly shown, Thy truth and virtue well are known. To thee, O lord, for help we fly, And on thy love of right rely: With kindly patience hear us speak, And grant the boon we humbly seek. That lord of earth were most unjust, Foul traitor to his solemn trust, Who should a sixth of all419 require, Nor guard his people like a sire. But he who ever watchful strives To guard his subjects' wealth and lives, Dear as himself or, dearer still, His sons, with earnest heart and will,— That king, O Raghu's son, secures 418 Four fires burning round them, and the sun above. 419 The tax allowed to the king by the Laws of Manu.
- **Translation**: 

---

### Verse 3 (Ramayana 0.848)
- **Original**: 830 The Ramayana High fame that endless years endures, And he to Brahmá's world shall rise, Made glorious in the eternal skies. Whate'er, by duty won, the meed Of saints whom roots and berries feed, One fourth thereof, for tender care Of subjects, is the monarch's share. These, mostly of the Bráhman race, Who make the wood their dwelling-place, Although a friend in thee they view, Fall friendless neath the giant crew. Come, Ráma, come, and see hard by The holy hermits' corpses lie, Where many a tangled pathway shows The murderous work of cruel foes. These wicked fiends the hermits kill— Who live on Chitrakúma's hill, And blood of slaughtered saints has dyed Mandákiní and Pampá's side. No longer can we bear to see The death of saint and devotee Whom through the forest day by day These Rákshasas unpitying slay. To thee, O Prince, we flee, and crave Thy guardian help our lives to save. From these fierce rovers of the night Defend each stricken anchorite. Throughout the world 'twere vain to seek An arm like thine to aid the weak. O Prince, we pray thee hear our call, And from these fiends preserve us all.” The son of Raghu heard the plaint Of penance-loving sage and saint,
- **Translation**: 

---

### Verse 4 (Ramayana 0.849)
- **Original**: Canto VII. Sutíkshna. 831 And the good prince his speech renewed To all the hermit multitude: “To me, O saints, ye need not sue: I wait the hests of all of you. I by mine own occasion led This mighty forest needs must tread, [236] And while I keep my sire's decree Your lives from threatening foes will free. I hither came of free accord To lend the aid by you implored, And richest meed my toil shall pay, While here in forest shades I stay. I long in battle strife to close. And slay these fiends, the hermits' foes, That saint and sage may learn aright My prowess and my brother's might.” Thus to the saints his promise gave That prince who still to virtue clave With never-wandering thought: And then with LakshmaG by his side, With penance-wealthy men to guide, SutíkshGa's home he sought. Canto VII. Sutíkshna.
- **Translation**: 

---

### Verse 5 (Ramayana 0.850)
- **Original**: 832 The Ramayana So Raghu's son, his foemen's dread, With Sítá and his brother sped, Girt round by many a twice-born sage, To good SutíkshGa's hermitage.420 Through woods for many a league he passed, O'er rushing rivers full and fast, Until a mountain fair and bright As lofty Meru rose in sight. Within its belt of varied wood Ikshváku's sons and Sítá stood, Where trees of every foliage bore Blossom and fruit in endless store. There coats of bark, like garlands strung, Before a lonely cottage hung, And there a hermit, dust-besmeared, A lotus on his breast, appeared. Then Ráma with obeisance due Addressed the sage, as near he drew: “My name is Ráma, lord; I seek Thy presence, saint, with thee to speak. O sage, whose merits ne'er decay, Some word unto thy servant say.” The sage his eyes on Ráma bent, Of virtue's friends preëminent; Then words like these he spoke, and pressed The son of Raghu to his breast: “Welcome to thee, illustrious youth, Best champion of the rights of truth! By thine approach this holy ground A worthy lord this day has found. I could not quit this mortal frame 420 Near the celebrated Rámagiri or Ráma's Hill, now Rám-mek, near Nag- pore— the scene of the Yaksha's exile in theMessenger Cloud.
- **Translation**: 

---

### Verse 6 (Ramayana 0.851)
- **Original**: Canto VII. Sutíkshna. 833 Till thou shouldst come, O dear to fame: To heavenly spheres I would not rise, Expecting thee with eager eyes. I knew that thou, unkinged, hadst made Thy home in Chitrakúma's shade. E'en now, O Ráma, Indra, lord Supreme by all the Gods adored, King of the Hundred Offerings,421 said, When he my dwelling visited, That the good works that I have done My choice of all the worlds have won. Accept this meed of holy vows, And with thy brother and thy spouse, Roam, through my favour, in the sky Which saints celestial glorify.” To that bright sage, of penance stern, The high-souled Ráma spake in turn, As Vásava422 who rules the skies To Brahmá's gracious speech replies: “I of myself those worlds will win, O mighty hermit pure from sin: But now, O saint, I pray thee tell Where I within this wood may dwell: For I byZarabhanga old, The son of Gautama, was told That thou in every lore art wise, And seest all with loving eyes.” 421 A hundred A[vamedhas or sacrifices of a horse raise the sacrificer to the dignity of Indra. 422 Indra.
- **Translation**: 

---

### Verse 7 (Ramayana 0.852)
- **Original**: 834 The Ramayana Thus to the saint, whose glories high Filled all the world, he made reply: And thus again the holy man His pleasant speech with joy began: “This calm retreat, O Prince, is blest With many a charm: here take thy rest. Here roots and kindly fruits abound, And hermits love the holy ground. Fair silvan beasts and gentle deer In herds unnumbered wander here: And as they roam, secure from harm, Our eyes with grace and beauty charm: Except the beasts in thickets bred, This grove of ours has naught to dread.” The hermit's speech when Ráma heard,— The hero ne'er by terror stirred,— On his great bow his hand he laid, And thus in turn his answer made: “O saint, my darts of keenest steel, Armed with their murderous barbs, would deal Destruction mid the silvan race That flocks around thy dwelling-place. Most wretched then my fate would be For such dishonour shown to thee: And only for the briefest stay Would I within this grove delay.” He spoke and ceased. With pious care He turned him to his evening prayer, Performed each customary rite, And sought his lodging for the night, With Sítá and his brother laid[237]
- **Translation**: 

---

### Verse 8 (Ramayana 0.853)
- **Original**: Canto VIII. The Hermitage. 835 Beneath the grove's delightful shade, First good SutíkshGa, as elsewhere, when he saw The shades of night around them draw, With hospitable care The princely chieftains entertained With store of choicest food ordained For holy hermit's fare. Canto VIII. The Hermitage. So Ráma and Sumitrá's son, When every honour due was done, Slept through the night. When morning broke, The heroes from their rest awoke. Betimes the son of Raghu rose, With gentle Sítá, from repose, And sipped the cool delicious wave Sweet with the scent the lotus gave, Then to the Gods and sacred flame The heroes and the lady came, And bent their heads in honour meet Within the hermit's pure retreat. When every stain was purged away, They saw the rising Lord of Day: Then to SutíkshGa's side they went, And softly spoke, most reverent:
- **Translation**: 

---

### Verse 9 (Ramayana 0.854)
- **Original**: 836 The Ramayana “Well have we slept, O holy lord, Honoured of thee by all adored: Now leave to journey forth we pray: These hermits urge us on our way. We haste to visit, wandering by, The ascetics' homes that round you lie, And roaming DaG ak's mighty wood To view each saintly brotherhood, For thy permission now we sue, With these high saints to duty true, By penance taught each sense to tame,— In lustre like the smokeless flame. Ere on our brows the sun can beat With fierce intolerable heat. Like some unworthy lord who wins His power by tyranny and sins, O saint, we fain would part.” The three Bent humbly to the devotee. He raised the princes as they pressed His feet, and strained them to his breast; And then the chief of devotees Bespake them both in words like these: “Go with thy brother, Ráma, go, Pursue thy path untouched by woe: Go with thy faithful Sítá, she Still like a shadow follows thee. Roam Da G ak wood observing well The pleasant homes where hermits dwell,— Pure saints whose ordered souls adhere To penance rites and vows austere. There plenteous roots and berries grow, And noble trees their blossoms show, And gentle deer and birds of air In peaceful troops are gathered there.
- **Translation**: 

---

### Verse 10 (Ramayana 0.855)
- **Original**: Canto VIII. The Hermitage. 837 There see the full-blown lotus stud The bosom of the lucid flood, And watch the joyous mallard shake The reeds that fringe the pool and lake. See with delighted eye the rill Leap sparkling from her parent hill, And hear the woods that round thee lie Reëcho to the peacock's cry. And as I bid thy brother, so, Sumitrá's child, I bid thee go. Go forth, these varied beauties see, And then once more return to me.” Thus spake the sage SutíkshGa: both The chiefs assented, nothing loth, Round him with circling steps they paced, Then for the road prepared with haste. There Sítá stood, the dame long-eyed, Fair quivers round their waists she tied, And gave each prince his trusty bow, And sword which ne'er a spot might know. Each took his quiver from her hand. And clanging bow and gleaming brand: Then from the hermits' home the two Went forth each woodland scene to view. Each beauteous in the bloom of age, Dismissed by that illustrious sage, With bow and sword accoutred, hied Away, and Sítá by their side.
- **Translation**: 

---

### Verse 11 (Ramayana 0.856)
- **Original**: 838 The Ramayana Canto IX. Sítá's Speech. Blest by the sage, when Raghu's son His onward journey had begun, Thus in her soft tone Sítá, meek With modest fear, began to speak: “One little slip the great may lead To shame that follows lawless deed: Such shame, my lord, as still must cling To faults from low desire that spring. Three several sins defile the soul, Born of desire that spurns control: First, utterance of a lying word, Then, viler both, the next, and third: The lawless love of other's wife, The thirst of blood uncaused by strife. The first, O Raghu's son, in thee None yet has found, none e'er shall see. Love of another's dame destroys All merit, lost for guilty joys: Ráma, such crime in thee, I ween, Has ne'er been found, shall ne'er be seen: The very thought, my princely lord, Is in thy secret soul abhorred.[238] For thou hast ever been the same Fond lover of thine own dear dame, Content with faithful heart to do Thy father's will, most just and true: Justice, and faith, and many a grace In thee have found a resting-place. Such virtues, Prince, the good may gain Who empire o'er each sense retain; And well canst thou, with loving view Regarding all, each sense subdue.
- **Translation**: 

---

### Verse 12 (Ramayana 0.857)
- **Original**: Canto IX. Sítá's Speech. 839 But for the third, the lust that strives, Insatiate still, for others' lives,— Fond thirst of blood where hate is none,— This, O my lord, thou wilt not shun. Thou hast but now a promise made, The saints of DaG ak wood to aid: And to protect their lives from ill The giants' blood in tight wilt spill: And from thy promise lasting fame Will glorify the forest's name. Armed with thy bow and arrows thou Forth with thy brother journeyest now, While as I think how true thou art Fears for thy bliss assail my heart, And all my spirit at the sight Is troubled with a strange affright. I like it not— it seems not good— Thy going thus to DaG ak wood: And I, if thou wilt mark me well, The reason of my fear will tell. Thou with thy brother, bow in hand, Beneath those ancient trees wilt stand, And thy keen arrows will not spare Wood-rovers who will meet thee there. For as the fuel food supplies That bids the dormant flame arise, Thus when the warrior grasps his bow He feels his breast with ardour glow. Deep in a holy grove, of yore, Where bird and beast from strife forbore, Zuchi beneath the sheltering boughs, A truthful hermit kept his vows. Then Indra,Zachí's heavenly lord, Armed like a warrior with a sword,
- **Translation**: 

---

### Verse 13 (Ramayana 0.858)
- **Original**: 840 The Ramayana Came to his tranquil home to spoil The hermit of his holy toil, And left the glorious weapon there Entrusted to the hermit's care, A pledge for him to keep, whose mind To fervent zeal was all resigned. He took the brand: with utmost heed He kept it for the warrior's need: To keep his trust he fondly strove When roaming in the neighbouring grove: Whene'er for roots and fruit he strayed Still by his side he bore the blade: Still on his sacred charge intent, He took his treasure when he went. As day by day that brand he wore, The hermit, rich in merit's store From penance rites each thought withdrew, And fierce and wild his spirit grew. With heedless soul he spurned the right, And found in cruel deeds delight. So, living with the sword, he fell, A ruined hermit, down to hell. This tale applies to those who deal Too closely with the warrior's steel: The steel to warriors is the same As fuel to the smouldering flame. Sincere affection prompts my speech: I honour where I fain would teach. Mayst thou, thus armed with shaft and bow, So dire a longing never know As, when no hatred prompts the fray, These giants of the wood to slay: For he who kills without offence Shall win but little glory thence.
- **Translation**: 

---

### Verse 14 (Ramayana 0.859)
- **Original**: Canto IX. Sítá's Speech. 841 The bow the warrior joys to bend Is lent him for a nobler end, That he may save and succour those Who watch in woods when pressed by foes. What, matched with woods, is bow or steel? What, warrior's arm with hermit's zeal? We with such might have naught to do: The forest rule should guide us too. But when Ayodhyá hails thee lord, Be then thy warrior life restored: So shall thy sire423 and mother joy In bliss that naught may e'er destroy. And if, resigning empire, thou Submit thee to the hermit's vow, The noblest gain from virtue springs, And virtue joy unending brings. All earthly blessings virtue sends: On virtue all the world depends. Those who with vow and fasting tame To due restraint the mind and frame, Win by their labour, nobly wise, The highest virtue for their prize. Pure in the hermit's grove remain, True to thy duty, free from stain. But the three worlds are open thrown To thee, by whom all things are known. Who gave me power that I should dare His duty to my lord declare? 'Tis woman's fancy, light as air, That moves my foolish breast. 423 Gorresio observes that Da[aratha was dead and that Sítá had been informed of his death. In his translation he substitutes for the words of the text“thy relations and mine.” This is quite superfluous. Da[aratha though in heaven still took a loving interest in the fortunes of his son.
- **Translation**: 

---

### Verse 15 (Ramayana 0.860)
- **Original**: 842 The Ramayana Now with thy brother counsel take, Reflect, thy choice with judgment make, And do what seems the best.” [239] Canto X. Ráma's Reply. The words that Sítá uttered, spurred By truest love, the hero heard: Then he who ne'er from virtue strayed To Janak's child his answer made: “In thy wise speech, sweet love, I find True impress of thy gentle mind, Well skilled the warrior's path to trace, Thou pride of Janak's ancient race. What fitting answer shall I frame To thy good words, my honoured dame? Thou sayst the warrior bears the bow That misery's tears may cease to flow; And those pure saints who love the shade Of DaG ak wood are sore dismayed. They sought me of their own accord, With suppliant prayers my aid implored: They, fed on roots and fruit, who spend Their lives where bosky wilds extend, My timid love, enjoy no rest By these malignant fiends distressed. These make the flesh of man their meat: The helpless saints they kill and eat. The hermits sought my side, the chief
- **Translation**: 

---

### Verse 16 (Ramayana 0.861)
- **Original**: Canto X. Ráma's Reply. 843 Of Bráhman race declared their grief. I heard, and from my lips there fell The words which thou rememberest well: I listened as the hermits cried, And to their prayers I thus replied: “Your favour, gracious lords, I claim, O'erwhelmed with this enormous shame That Bráhmans, great and pure as you, Who should be sought, to me should sue.” And then before the saintly crowd, “What can I do?” I cried aloud. Then from the trembling hermits broke One long sad cry, and thus they spoke: “Fiends of the wood, who wear at will Each varied shape, afflict us still. To thee in our distress we fly: O help us, Ráma, or we die. When sacred rites of fire are due, When changing moons are full or new, These fiends who bleeding flesh devour Assail us with resistless power. They with their cruel might torment The hermits on their vows intent: We look around for help and see Our surest refuge, Prince, in thee. We, armed with powers of penance, might Destroy the rovers of the night: But loth were we to bring to naught The merit years of toil have bought. Our penance rites are grown too hard, By many a check and trouble barred, But though our saints for food are slain The withering curse we yet restrain.
- **Translation**: 

---

### Verse 17 (Ramayana 0.862)
- **Original**: 844 The Ramayana Thus many a weary day distressed By giants who this wood infest, We see at length deliverance, thou With LakshmaG art our guardian now.” As thus the troubled hermits prayed, I promised, dame, my ready aid, And now — for truth I hold most dear— Still to my word must I adhere. My love, I might endure to be Deprived of LakshmaG, life, and thee, But ne'er deny my promise, ne'er To Bráhmans break the oath I sware. I must, enforced by high constraint, Protect them all. Each suffering saint In me, unasked, his help had found; Still more in one by promise bound. I know thy words, mine own dear dame, From thy sweet heart's affection came: I thank thee for thy gentle speech, For those we love are those we teach. 'Tis like thyself, O fair of face, 'Tis worthy of thy noble race: Dearer than life, thy feet are set In righteous paths they ne'er forget.” Thus to the Maithil monarch's child, His own dear wife, in accents mild The high-souled hero said: Then to the holy groves which lay Beyond them fair to see, their way The bow-armed chieftain led.
- **Translation**: 

---

### Verse 18 (Ramayana 0.863)
- **Original**: Canto XI. Agastya. 845 Canto XI. Agastya. Ráma went foremost of the three, Next Sítá, followed, fair to see, And Lakshma G with his bow in hand Walked hindmost of the little band. As onward through the wood they went, With great delight their eyes were bent On rocky heights beside the way And lofty trees with blossoms gay; And streamlets running fair and fast The royal youths with Sítá passed. They watched the sáras and the drake On islets of the stream and lake, And gazed delighted on the floods Bright with gay birds and lotus buds. They saw in startled herds the roes, The passion-frenzied buffaloes, Wild elephants who fiercely tore The tender trees, and many a boar. A length of woodland way they passed, And when the sun was low at last A lovely stream-fed lake they spied, Two leagues across from side to side. Tall elephants fresh beauty gave To grassy bank and lilied wave, [240] By many a swan and sáras stirred, Mallard, and gay-winged water-bird. From those sweet waters, loud and long, Though none was seen to wake the song, Swelled high the singer's music blent With each melodious instrument. Ráma and car-borne LakshmaG heard The charming strain, with wonder stirred,
- **Translation**: 

---

### Verse 19 (Ramayana 0.864)
- **Original**: 846 The Ramayana Turned on the margent of the lake To Dharmabhrit424 the sage, and spake: “Our longing souls, O hermit, burn This music of the lake to learn: We pray thee, noblest sage, explain The cause of the mysterious strain.” He, as the son of Raghu prayed, With swift accord his answer made, And thus the hermit, virtuous-souled, The story of the fair lake told: “Through every age 'tis known to fame, Panchápsaras425 its glorious name, By holy MáG akarGi wrought With power his rites austere had bought. For he, great votarist, intent On strictest rule his stern life spent. Ten thousand years the stream his bed, Ten thousand years on air he fed. Then on the blessed Gods who dwell In heavenly homes great terror fell: They gathered all, by Agni led, And counselled thus disquieted: “The hermit by ascetic pain The seat of one of us would gain.” Thus with their hearts by fear oppressed In full assembly spoke the Blest, And bade five loveliest nymphs, as fair As lightning in the evening air, Armed with their winning wiles, seduce From his stern vows the great recluse. 424 One of the hermits who had followed Ráma. 425 The lake of the five nymphs.
- **Translation**: 

---

### Verse 20 (Ramayana 0.865)
- **Original**: Canto XI. Agastya. 847 Though lore of earth and heaven he knew, The hermit from his task they drew, And made the great ascetic slave To conquering love, the Gods to save. Each of the heavenly five became, Bound to the sage, his wedded dame; And he, for his beloved's sake, Formed a fair palace neath the lake. Under the flood the ladies live, To joy and ease their days they give, And lap in bliss the hermit wooed From penance rites to youth renewed. So when the sportive nymphs within Those secret bowers their play begin, You hear the singers' dulcet tones Blend sweetly with their tinkling zones.” “How wondrous are these words of thine!” Cried the famed chiefs of Raghu's line, As thus they heard the sage unfold The marvels of the tale he told. As Ráma spake, his eyes were bent Upon a hermit settlement With light of heavenly lore endued, With sacred grass and vesture strewed. His wife and brother by his side, Within the holy bounds he hied, And there, with honour entertained By all the saints, a while remained. In time, by due succession led, Each votary's cot he visited, And then the lord of martial lore, Returned where he had lodged before.
- **Translation**: 

---

