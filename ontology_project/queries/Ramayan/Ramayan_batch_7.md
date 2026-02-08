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

### Verse 1 (Ramayan 0.121)
- **Original**: Canto XIX. The Birth Of The Princes. 103 The spacious square, the ample road With mimes and dancers overflowed, And with the voice of music rang Where minstrels played and singers sang, And shone, a wonder to behold, With dazzling show of gems and gold. Nor did the king his largess spare, For minstrel, driver, bard, to share; Much wealth the Bráhmans bore away, And many thousand dine that day. Soon as each babe was twelve days old 'Twas time the naming rite to hold. When Saint Va[ishmha, rapt with joy, Assigned a name to every boy. Ráma, to him the high-souled heir, Bharat, to him Kaikeyí bare: Of Queen Sumitrá one fair son Was Lakshma G, andZatrughna136 one Ráma, his sire's supreme delight, Like some proud banner cheered his sight, And to all creatures seemed to be The self-existent deity. All heroes, versed in holy lore, To all mankind great love they bore. Fair stores of wisdom all possessed, With princely graces all were blest. But mid those youths of high descent, With lordly light preëminent. Like the full moon unclouded, shone Ráma, the world's dear paragon. 136 Ráma means the Delight (of the World); Bharat, the Supporter; LakshmaG, the Auspicious;Zatrughna, the Slayer of Foes.
- **Translation**: 

---

### Verse 2 (Ramayan 0.122)
- **Original**: 104 The Ramayana He best the elephant could guide.137 Urge the fleet car, the charger ride: A master he of bowman's skill, Joying to do his father's will. The world's delight and darling, he Loved LakshmaG best from infancy And Lakshma G, lord of lofty fate, Upon his elder joyed to wait, Striving his second self to please With friendship's sweet observances. His limbs the hero ne'er would rest Unless the couch his brother pressed; Except beloved Ráma shared He could not taste the meal prepared. When Ráma, pride of Reghu's race, Sprang on his steed to urge the chase, Behind him LakshmaG loved to go And guard him with his trusty bow. As Ráma was to LakshmaG dear More than his life and ever near, So fondZatrughna prized above His very life his Bharat's love. Illustrious heroes, nobly kind In mutual love they all combined, And gave their royal sire delight With modest grace and warrior might: Supported by the glorious four Shone Da[aratha more and more, As though, with every guardian God 137 Schlegel, in theIndische Bibliothek, remarks that the proficiency of the Indians in this art early attracted the attention of Alexander's successors, and natives of India were so long exclusively employed in this service that the name Indian was applied to any elephant-driver, to whatever country he might belong.
- **Translation**: 

---

### Verse 3 (Ramayan 0.123)
- **Original**: Canto XX. Visvámitra's Visit. 105 Who keeps the land and skies, The Father of all creatures trod The earth before men's eyes. Canto XX. Visvámitra's Visit. Now Da [aratha's pious mind Meet wedlock for his sons designed; [033] With priests and friends the king began To counsel and prepare his plan. Such thoughts engaged his bosom, when, To see Ayodhyá's lord of men, A mighty saint of glorious fame, The hermit Vi[vámitra138 came. For evil fiends that roam by night Disturbed him in each holy rite, And in their strength and frantic rage Assailed with witcheries the sage. He came to seek the monarch's aid To guard the rites the demons stayed, Unable to a close to bring One unpolluted offering. Seeking the king in this dire strait He said to those who kept the gate: “Haste, warders, to your master run, And say that here stands Gádhi's son.” 138 The story of this famous saint is given at sufficient length in Cantos LI-LV. This saint has given his name to the district and city to the east of Benares. The original name, preserved in a land-grant on copper now in the Museum of the Benares College, has been Moslemized into Ghazeepore (the City of the Soldier-martyr).
- **Translation**: 

---

### Verse 4 (Ramayan 0.124)
- **Original**: 106 The Ramayana Soon as they heard the holy man, To the king's chamber swift they ran With minds disordered all, and spurred To wildest zeal by what they heard. On to the royal hall they sped, There stood and lowly bowed the head, And made the lord of men aware That the great saint was waiting there. The king with priest and peer arose And ran the sage to meet, As Indra from his palace goes Lord Brahmá's self to greet. When glowing with celestial light The pious hermit was in sight, The king, whose mien his transport showed, The honoured gift for guests bestowed. Nor did the saint that gift despise, Offered as holy texts advise; He kindly asked the earth's great king How all with him was prospering. The son of Ku[ik139 bade him tell If all in town and field were well, All well with friends, and kith and kin, And royal treasure stored within: “Do all thy neighbours own thy sway? Thy foes confess thee yet? Dost thou continue still to pay To Gods and men each debt?” Then he, of hermits first and best, Va [ishmha with a smile140 addressed, And asked him of his welfare too, Showing him honour as was due. 139 The son of Ku[ik is Vi[vámitra. 140 At the recollection of their former enmity, to be described hereafter.
- **Translation**: 

---

### Verse 5 (Ramayan 0.125)
- **Original**: Canto XX. Visvámitra's Visit. 107 Then with the sainted hermit all Went joyous to the monarch's hall, And sate them down by due degree, Each one, of rank and dignity. Joy filled the noble prince's breast Who thus bespoke the honoured guest: “As amrit141 by a mortal found, As rain upon the thirsty ground, As to an heirless man a son Born to him of his precious one, As gain of what we sorely miss, As sudden dawn of mighty bliss, So is thy coming here to me: All welcome, mighty Saint, to thee. What wish within thy heart hast thou? If I can please thee, tell me how. Hail, Saint, from whom all honours flow, Worthy of all I can bestow. Blest is my birth with fruit to-day, Nor has my life been thrown away. I see the best of Bráhman race And night to glorious morn gives place. Thou, holy Sage, in days of old Among the royal saints enrolled, Didst, penance-glorified, within The Bráhman caste high station win. 'Tis meet and right in many a way That I to thee should honour pay. This seems a marvel to mine eyes: All sin thy visit purifies; And I by seeing thee, O Sage, Have reaped the fruit of pilgrimage. 141 The Indian nectar or drink of the Gods.
- **Translation**: 

---

### Verse 6 (Ramayan 0.126)
- **Original**: 108 The Ramayana Then say what thou wouldst have me do, That thou hast sought this interview. Favoured by thee, my wish is still, O Hermit, to perform thy will. Nor needest thou at length explain The object that thy heart would gain. Without reserve I grant it now: My deity, O Lord, art thou.” The glorious hermit, far renowned, With highest fame and virtue crowned, Rejoiced these modest words to hear Delightful to the mind and ear. Canto XXI. Visvámitra's Speech. The hermit heard with high content That speech so wondrous eloquent, And while each hair with joy arose,142[034] 142 Great joy, according to the Hindu belief, has this effect, not causing each particular hair to stand on end, but gently raising all the down upon the body.
- **Translation**: 

---

### Verse 7 (Ramayan 0.127)
- **Original**: Canto XXI. Visvámitra's Speech. 109 He thus made answer at the close: “Good is thy speech O noble King, And like thyself in everything. So should their lips be wisdom-fraught Whom kings begot, Va[ishmha taught. The favour which I came to seek Thou grantest ere my tongue can speak. But let my tale attention claim, And hear the need for which I came. O King, as Scripture texts allow, A holy rite employs me now. Two fiends who change their forms at will Impede that rite with cursed skill.143 Oft when the task is nigh complete, These worst of fiends my toil defeat, Throw bits of bleeding flesh, and o'er The altar shed a stream of gore. When thus the rite is mocked and stayed, And all my pious hopes delayed, Cast down in heart the spot I leave, And spent with fruitless labour grieve. Nor can I, checked by prudence, dare Let loose my fury on them there: The muttered curse, the threatening word, In such a rite must ne'er be heard. Thy grace the rite from check can free. And yield the fruit I long to see. Thy duty bids thee, King, defend The suffering guest, the suppliant friend. Give me thy son, thine eldest born, Whom locks like raven's wings adorn. 143 The Rákshasas, giants, or fiends who are represented as disturbing the sacrifice, signify here, as often elsewhere, merely the savage tribes which placed themselves in hostile opposition to Bráhmanical institutions.
- **Translation**: 

---

### Verse 8 (Ramayan 0.128)
- **Original**: 110 The Ramayana That hero youth, the truly brave, Of thee, O glorious King, I crave. For he can lay those demons low Who mar my rites and work me woe: My power shall shield the youth from harm, And heavenly might shall nerve his arm. And on my champion will I shower Unnumbered gifts of varied power, Such gifts as shall ensure his fame And spread through all the worlds his name. Be sure those fiends can never stand Before the might of Ráma's hand, And mid the best and bravest none Can slay that pair but Raghu's son. Entangled in the toils of Fate Those sinners, proud and obstinate, Are, in their fury overbold, No match for Ráma mighty-souled. Nor let a father's breast give way Too far to fond affection's sway. Count thou the fiends already slain: My word is pledged, nor pledged in vain. I know the hero Ráma well In whom high thoughts and valour dwell; So does Va[ishmha, so do these Engaged in long austerities. If thou would do the righteous deed, And win high fame, thy virtue's meed, Fame that on earth shall last and live, To me, great King, thy Ráma give. If to the words that I have said, With Saint Va[ishmha at their head Thy holy men, O King, agree, Then let thy Ráma go with me.
- **Translation**: 

---

### Verse 9 (Ramayan 0.129)
- **Original**: Canto XXII. Dasaratha's Speech. 111 Ten nights my sacrifice will last, And ere the stated time be past Those wicked fiends, those impious twain, Must fall by wondrous Ráma slain. Let not the hours, I warn thee, fly, Fixt for the rite, unheeded by; Good luck have thou, O royal Chief, Nor give thy heart to needless grief.” Thus in fair words with virtue fraught The pious glorious saint besought. But the good speech with poignant sting Pierced ear and bosom of the king, Who, stabbed with pangs too sharp to bear, Fell prostrate and lay fainting there. Canto XXII. Dasaratha's Speech. His tortured senses all astray, While the hapless monarch lay, Then slowly gathering thought and strength To Vi[vámitra spoke at length: “My son is but a child, I ween; This year he will be just sixteen. How is he fit for such emprise, My darling with the lotus eyes? A mighty army will I bring That calls me master, lord, and king, And with its countless squadrons fight Against these rovers of the night. My faithful heroes skilled to wield
- **Translation**: 

---

### Verse 10 (Ramayan 0.130)
- **Original**: 112 The Ramayana The arms of war will take the field; Their skill the demons' might may break: Ráma, my child, thou must not take. I, even I, my bow in hand, Will in the van of battle stand, And, while my soul is left alive, With the night-roaming demons strive. Thy guarded sacrifice shall be Completed, from all hindrance free. Thither will I my journey make: Ráma, my child, thou must not take. A boy unskilled, he knows not yet The bounds to strength and weakness set. No match is he for demon foes Who magic arts to arms oppose.[035] O chief of saints, I have no power, Of Ráma reft, to live one hour: Mine aged heart at once would break: Ráma, my child, thou must not take. Nine thousand circling years have fled With all their seasons o'er my head, And as a hard-won boon, O sage, These sons have come to cheer mine age. My dearest love amid the four Is he whom first his mother bore, Still dearer for his virtues' sake: Ráma, my child, thou must not take. But if, unmoved by all I say, Thou needs must bear my son away, Let me lead with him, I entreat, A four-fold army144 all complete. What is the demons' might, O Sage? 144 Consisting of horse, foot, chariots, and elephants.
- **Translation**: 

---

### Verse 11 (Ramayan 0.131)
- **Original**: Canto XXII. Dasaratha's Speech. 113 Who are they? What their parentage? What is their size? What beings lend Their power to guard them and befriend? How can my son their arts withstand? Or I or all my armed band? Tell me the whole that I may know To meet in war each evil foe Whom conscious might inspires with pride.” And Vi[vámitra thus replied: “Sprung from Pulastya's race there came A giant known by RávaG's name. Once favoured by the Eternal Sire He plagues the worlds in ceaseless ire, For peerless power and might renowned, By giant bands encompassed round. Vi[ravas for his sire they hold, His brother is the Lord of Gold. King of the giant hosts is he, And worst of all in cruelty. This RávaG's dread commands impel Two demons who in might excel, Márícha and Suváhu hight, To trouble and impede the rite.” Then thus the king addressed the sage: “No power have I, my lord, to wage War with this evil-minded foe; Now pity on my darling show, And upon me of hapless fate, For thee as God I venerate. Gods, spirits, bards of heavenly birth,145 145 “The Gandharvas, or heavenly bards, had originally a warlike character but were afterwards reduced to the office of celestial musicians cheering the
- **Translation**: 

---

### Verse 12 (Ramayan 0.132)
- **Original**: 114 The Ramayana The birds of air, the snakes of earth Before the might of RávaG quail, Much less can mortal man avail. He draws, I hear, from out the breast The valour of the mightiest. No, ne'er can I with him contend, Or with the forces he may send. How can I then my darling lend, Godlike, unskilled in battle? No, I will not let my young child go. Foes of thy rite, those mighty ones, Sunda and Upasunda's sons, Are fierce as Fate to overthrow: I will not let my young child go. Márícha and Suváhu fell Are valiant and instructed well. One of the twain I might attack. With all my friends their lord to back.” Canto XXIII. Vasishtha's Speech. banquets of the Gods. Dr. Kuhn has shown their identity with the Centaurs in name, origin and attributes.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 13 (Ramayan 0.133)
- **Original**: Canto XXIII. Vasishtha's Speech. 115 While thus the hapless monarch spoke, Paternal love his utterance broke. Then words like these the saint returned, And fury in his bosom burned: “Didst thou, O King, a promise make, And wishest now thy word to break? A son of Raghu's line should scorn To fail in faith, a man forsworn. But if thy soul can bear the shame I will return e'en as I came. Live with thy sons, and joy be thine, False scion of Kakutstha's line.” As Vi[vámitra, mighty sage, Was moved with this tempestuous rage, Earth rocked and reeled throughout her frame, And fear upon the Immortals came. But Saint Va[ishmha, wisest seer, Observant of his vows austere, Saw the whole world convulsed with dread, And thus unto the monarch said: “Thou, born of old Ikshváku's seed, Art Justice' self in mortal weed. Constant and pious, blest by fate, The right thou must not violate. Thou, Raghu's son, so famous through The triple world as just and true, Perform thy bounden duty still, Nor stain thy race by deed of ill. If thou have sworn and now refuse Thou must thy store of merit lose. Then, Monarch, let thy Ráma go, Nor fear for him the demon foe. The fiends shall have no power to hurt
- **Translation**: 

---

### Verse 14 (Ramayan 0.134)
- **Original**: 116 The Ramayana Him trained to war or inexpert, Nor vanquish him in battle field, For Ku[ik's son the youth will shield. He is incarnate Justice, he The best of men for bravery. Embodied love of penance drear, Among the wise without a peer.[036] Full well he knows, great Ku[ik's son, The arms celestial, every one, Arms from the Gods themselves concealed, Far less to other men revealed. These arms to him, when earth he swayed, Mighty Kri[á[va, pleased, conveyed. Kri[á[va's sons they are indeed, Brought forth by Daksha's lovely seed,146 Heralds of conquest, strong and bold, Brilliant, of semblance manifold. Jayá and Vijayá, most fair, And hundred splendid weapons bare. Of Jayá, glorious as the morn, First fifty noble sons were born, Boundless in size yet viewless too, They came the demons to subdue. And fifty children also came Of Vijayá the beauteous dame, Sanháras named, of mighty force, Hard to assail or check in course. Of these the hermit knows the use, And weapons new can he produce. All these the mighty saint will yield To Ráma's hand, to own and wield; 146 These mysterious animated weapons are enumerated in Cantos XXIX and XXX. Daksha was the son of Brahmá and one of the Prajápatis, Demiurgi, or secondary authors of creation.
- **Translation**: 

---

### Verse 15 (Ramayan 0.135)
- **Original**: Canto XXIV. The Spells. 117 And armed with these, beyond a doubt Shall Ráma put those fiends to rout. For Ráma and the people's sake, For thine own good my counsel take, Nor seek, O King, with fond delay, The parting of thy son to stay.” Canto XXIV. The Spells. Va [ishmha thus was speaking still: The monarch, of his own free will, Bade with quick zeal and joyful cheer Ráma and LakshmaG hasten near. Mother and sire in loving care Sped their dear son with rite and prayer: Va [ishmha blessed him ere he went; O'er his loved head the father bent, And then to Ku[ik's son resigned Ráma with LakshmaG close behind. Standing by Vi[vámitra's side, The youthful hero, lotus-eyed, The Wind-God saw, and sent a breeze Whose sweet pure touch just waved the trees. There fell from heaven a flowery rain, And with the song and dance the strain Of shell and tambour sweetly blent As forth the son of Raghu went. The hermit led: behind him came The bow-armed Ráma, dear to fame,
- **Translation**: 

---

### Verse 16 (Ramayan 0.136)
- **Original**: 118 The Ramayana Whose locks were like the raven's wing:147 Then LakshmaG, closely following. The Gods and Indra, filled with joy, Looked down upon the royal boy, And much they longed the death to see Of their ten-headed enemy.148 Ráma and LakshmaG paced behind That hermit of the lofty mind, As the young A[vins,149 heavenly pair, Follow Lord Indra through the air. On arm and hand the guard they wore, Quiver and bow and sword they bore; Two fire-born Gods of War seemed they.150 He, Ziva's self who led the way. Upon fair Sarjú's southern shore They now had walked a league and more, When thus the sage in accents mild To Ráma said:“Beloved child, This lustral water duly touch: My counsel will avail thee much. Forget not all the words I say, 147 Youths of the Kshatriya class used to leave unshorn the side locks of their hair. These were calledKáka-paksha, or raven's wings. 148 The Rákshas or giant RávaG, king of Lanká. 149 “The meaning of A[vins (froma[va a horse, Persian asp, Greek5ÀÀ¿Â, Latin equus, Welsh ech) is Horsemen. They were twin deities of whom frequent mention is made in the Vedas and the Indian myths. The A[vins have much in common with the Dioscuri of Greece, and their mythical genealogy seems to indicate that their origin was astronomical. They were, perhaps, at first the morning star and evening star. They are said to be the children of the sun and the nymph A[viní, who is one of the lunar asterisms personified. In the popular mythology they are regarded as the physicians of the Gods.” G ORRESIO {FNS . 150 The word Kumára (a young prince, a Childe) is also a proper name of Skanda or Kártikeya God of War, the son ofZiva and Umá. The babe was matured in the fire.
- **Translation**: 

---

### Verse 17 (Ramayan 0.137)
- **Original**: Canto XXIV. The Spells. 119 Nor let the occasion slip away. Lo, with two spells I thee invest, The mighty and the mightiest. O'er thee fatigue shall ne'er prevail, Nor age or change thy limbs assail. Thee powers of darkness ne'er shall smite In tranquil sleep or wild delight. No one is there in all the land Thine equal for the vigorous hand. [037] Thou, when thy lips pronounce the spell, Shalt have no peer in heaven or hell. None in the world with thee shall vie, O sinless one, in apt reply, In fortune, knowledge, wit, and tact, Wisdom to plan and skill to act. This double science take, and gain Glory that shall for aye remain. Wisdom and judgment spring from each Of these fair spells whose use I teach. Hunger and thirst unknown to thee, High in the worlds thy rank shall be. For these two spells with might endued, Are the Great Father's heavenly brood, And thee, O Chief, may fitly grace, Thou glory of Kakutstha's race. Virtues which none can match are thine, Lord, from thy birth, of gifts divine, And now these spells of might shall cast Fresh radiance o'er the gifts thou hast.” Then Ráma duly touched the wave, Raised suppliant hands, bowed low his head, And took the spells the hermit gave, Whose soul on contemplation fed. From him whose might these gifts enhanced,
- **Translation**: 

---

### Verse 18 (Ramayan 0.138)
- **Original**: 120 The Ramayana A brighter beam of glory glanced: So shines in all his autumn blaze The Day-God of the thousand rays. The hermit's wants those youths supplied, As pupils use to holy guide. And then the night in sweet content On Sarjú's pleasant bank they spent. Canto XXV. The Hermitage Of Love. Soon as appeared the morning light Up rose the mighty anchorite, And thus to youthful Ráma said, Who lay upon his leafy bed: “High fate is hers who calls thee son: Arise, 'tis break of day; Rise, Chief, and let those rites be done Due at the morning's ray.”151 At that great sage's high behest Up sprang the princely pair, To bathing rites themselves addressed, And breathed the holiest prayer. Their morning task completed, they To Vi[vámitra came That store of holy works, to pay The worship saints may claim. Then to the hallowed spot they went 151 “At the rising of the sun as well as at noon certain observances, invocations, and prayers were prescribed which might under no circumstances be omitted. One of these observances was the recitation of the Sávitrí, a Vedic hymn to the Sun of wonderful beauty.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 19 (Ramayan 0.139)
- **Original**: Canto XXV. The Hermitage Of Love. 121 Along fair Sarjú's side Where mix her waters confluent With three-pathed Gangá's tide.152 There was a sacred hermitage Where saints devout of mind Their lives through many a lengthened age To penance had resigned. That pure abode the princes eyed With unrestrained delight, And thus unto the saint they cried, Rejoicing at the sight: “Whose is that hermitage we see? Who makes his dwelling there? Full of desire to hear are we: O Saint, the truth declare.” The hermit smiling made reply To the two boys' request: “Hear, Ráma, who in days gone by This calm retreat possessed. Kandarpa in apparent form, Called Káma153 by the wise, Dared Umá's154 new-wed lord to storm And make the God his prize. 'Gainst StháGu's155 self, on rites austere 152 Tripathaga, Three-path-go,flowing in heaven, on earth, and under the earth. See Canto XLV. 153 Tennyson's“Indian Cama,” the God of Love, known also by many other names. 154 Umá , orParvatí, was daughter of Himálaya, Monarch of mountains, and wife ofZiva. See Kálidasa'sKumára Sambhava , orBirth of the War-God. 155 StháGu. The Unmoving one, a name ofZiva.
- **Translation**: 

---

### Verse 20 (Ramayan 0.140)
- **Original**: 122 The Ramayana And vows intent,156 they say, His bold rash hand he dared to rear, Though StháGu cried, Away! But the God's eye with scornful glare Fell terrible on him. Dissolved the shape that was so fair[038] And burnt up every limb. Since the great God's terrific rage Destroyed his form and frame, Káma in each succeeding age Has borne Ananga's157 name. So, where his lovely form decayed, This land is Anga styled: Sacred to him of old this shade, And hermits undefiled. Here Scripture-talking elders sway Each sense with firm control, And penance-rites have washed away All sin from every soul. One night, fair boy, we here will spend, A pure stream on each hand, And with to-morrow's light will bend Our steps to yonder strand. Here let us bathe, and free from stain To that pure grove repair, 156 “The practice of austerities, voluntary tortures, and mortifications was anciently universal in India, and was held by the Indians to be of immense efficacy. Hence they mortified themselves to expiate sins, to acquire merits, and to obtain superhuman gifts and powers; the Gods themselves sometimes exercised themselves in such austerities, either to raise themselves to greater power and grandeur, or to counteract the austerities of man which threatened to prevail over them and to deprive them of heaven.… Such austerities were called in Indiatapas(burning ardour, fervent devotion) and he who practised them tapasvin.” G ORRESIO {FNS . 157 The Bodiless one.
- **Translation**: 

---

