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

### Verse 1 (Ramayana 0.126)
- **Original**: 108 The Ramayana Then say what thou wouldst have me do, That thou hast sought this interview. Favoured by thee, my wish is still, O Hermit, to perform thy will. Nor needest thou at length explain The object that thy heart would gain. Without reserve I grant it now: My deity, O Lord, art thou.” The glorious hermit, far renowned, With highest fame and virtue crowned, Rejoiced these modest words to hear Delightful to the mind and ear. Canto XXI. Visvámitra's Speech. The hermit heard with high content That speech so wondrous eloquent, And while each hair with joy arose,142[034] 142 Great joy, according to the Hindu belief, has this effect, not causing each particular hair to stand on end, but gently raising all the down upon the body.
- **Translation**: 

---

### Verse 2 (Ramayana 0.127)
- **Original**: Canto XXI. Visvámitra's Speech. 109 He thus made answer at the close: “Good is thy speech O noble King, And like thyself in everything. So should their lips be wisdom-fraught Whom kings begot, Va[ishmha taught. The favour which I came to seek Thou grantest ere my tongue can speak. But let my tale attention claim, And hear the need for which I came. O King, as Scripture texts allow, A holy rite employs me now. Two fiends who change their forms at will Impede that rite with cursed skill.143 Oft when the task is nigh complete, These worst of fiends my toil defeat, Throw bits of bleeding flesh, and o'er The altar shed a stream of gore. When thus the rite is mocked and stayed, And all my pious hopes delayed, Cast down in heart the spot I leave, And spent with fruitless labour grieve. Nor can I, checked by prudence, dare Let loose my fury on them there: The muttered curse, the threatening word, In such a rite must ne'er be heard. Thy grace the rite from check can free. And yield the fruit I long to see. Thy duty bids thee, King, defend The suffering guest, the suppliant friend. Give me thy son, thine eldest born, Whom locks like raven's wings adorn. 143 The Rákshasas, giants, or fiends who are represented as disturbing the sacrifice, signify here, as often elsewhere, merely the savage tribes which placed themselves in hostile opposition to Bráhmanical institutions.
- **Translation**: 

---

### Verse 3 (Ramayana 0.128)
- **Original**: 110 The Ramayana That hero youth, the truly brave, Of thee, O glorious King, I crave. For he can lay those demons low Who mar my rites and work me woe: My power shall shield the youth from harm, And heavenly might shall nerve his arm. And on my champion will I shower Unnumbered gifts of varied power, Such gifts as shall ensure his fame And spread through all the worlds his name. Be sure those fiends can never stand Before the might of Ráma's hand, And mid the best and bravest none Can slay that pair but Raghu's son. Entangled in the toils of Fate Those sinners, proud and obstinate, Are, in their fury overbold, No match for Ráma mighty-souled. Nor let a father's breast give way Too far to fond affection's sway. Count thou the fiends already slain: My word is pledged, nor pledged in vain. I know the hero Ráma well In whom high thoughts and valour dwell; So does Va[ishmha, so do these Engaged in long austerities. If thou would do the righteous deed, And win high fame, thy virtue's meed, Fame that on earth shall last and live, To me, great King, thy Ráma give. If to the words that I have said, With Saint Va[ishmha at their head Thy holy men, O King, agree, Then let thy Ráma go with me.
- **Translation**: 

---

### Verse 4 (Ramayana 0.129)
- **Original**: Canto XXII. Dasaratha's Speech. 111 Ten nights my sacrifice will last, And ere the stated time be past Those wicked fiends, those impious twain, Must fall by wondrous Ráma slain. Let not the hours, I warn thee, fly, Fixt for the rite, unheeded by; Good luck have thou, O royal Chief, Nor give thy heart to needless grief.” Thus in fair words with virtue fraught The pious glorious saint besought. But the good speech with poignant sting Pierced ear and bosom of the king, Who, stabbed with pangs too sharp to bear, Fell prostrate and lay fainting there. Canto XXII. Dasaratha's Speech. His tortured senses all astray, While the hapless monarch lay, Then slowly gathering thought and strength To Vi[vámitra spoke at length: “My son is but a child, I ween; This year he will be just sixteen. How is he fit for such emprise, My darling with the lotus eyes? A mighty army will I bring That calls me master, lord, and king, And with its countless squadrons fight Against these rovers of the night. My faithful heroes skilled to wield
- **Translation**: 

---

### Verse 5 (Ramayana 0.130)
- **Original**: 112 The Ramayana The arms of war will take the field; Their skill the demons' might may break: Ráma, my child, thou must not take. I, even I, my bow in hand, Will in the van of battle stand, And, while my soul is left alive, With the night-roaming demons strive. Thy guarded sacrifice shall be Completed, from all hindrance free. Thither will I my journey make: Ráma, my child, thou must not take. A boy unskilled, he knows not yet The bounds to strength and weakness set. No match is he for demon foes Who magic arts to arms oppose.[035] O chief of saints, I have no power, Of Ráma reft, to live one hour: Mine aged heart at once would break: Ráma, my child, thou must not take. Nine thousand circling years have fled With all their seasons o'er my head, And as a hard-won boon, O sage, These sons have come to cheer mine age. My dearest love amid the four Is he whom first his mother bore, Still dearer for his virtues' sake: Ráma, my child, thou must not take. But if, unmoved by all I say, Thou needs must bear my son away, Let me lead with him, I entreat, A four-fold army144 all complete. What is the demons' might, O Sage? 144 Consisting of horse, foot, chariots, and elephants.
- **Translation**: 

---

### Verse 6 (Ramayana 0.131)
- **Original**: Canto XXII. Dasaratha's Speech. 113 Who are they? What their parentage? What is their size? What beings lend Their power to guard them and befriend? How can my son their arts withstand? Or I or all my armed band? Tell me the whole that I may know To meet in war each evil foe Whom conscious might inspires with pride.” And Vi[vámitra thus replied: “Sprung from Pulastya's race there came A giant known by RávaG's name. Once favoured by the Eternal Sire He plagues the worlds in ceaseless ire, For peerless power and might renowned, By giant bands encompassed round. Vi[ravas for his sire they hold, His brother is the Lord of Gold. King of the giant hosts is he, And worst of all in cruelty. This RávaG's dread commands impel Two demons who in might excel, Márícha and Suváhu hight, To trouble and impede the rite.” Then thus the king addressed the sage: “No power have I, my lord, to wage War with this evil-minded foe; Now pity on my darling show, And upon me of hapless fate, For thee as God I venerate. Gods, spirits, bards of heavenly birth,145 145 “The Gandharvas, or heavenly bards, had originally a warlike character but were afterwards reduced to the office of celestial musicians cheering the
- **Translation**: 

---

### Verse 7 (Ramayana 0.132)
- **Original**: 114 The Ramayana The birds of air, the snakes of earth Before the might of RávaG quail, Much less can mortal man avail. He draws, I hear, from out the breast The valour of the mightiest. No, ne'er can I with him contend, Or with the forces he may send. How can I then my darling lend, Godlike, unskilled in battle? No, I will not let my young child go. Foes of thy rite, those mighty ones, Sunda and Upasunda's sons, Are fierce as Fate to overthrow: I will not let my young child go. Márícha and Suváhu fell Are valiant and instructed well. One of the twain I might attack. With all my friends their lord to back.” Canto XXIII. Vasishtha's Speech. banquets of the Gods. Dr. Kuhn has shown their identity with the Centaurs in name, origin and attributes.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 8 (Ramayana 0.133)
- **Original**: Canto XXIII. Vasishtha's Speech. 115 While thus the hapless monarch spoke, Paternal love his utterance broke. Then words like these the saint returned, And fury in his bosom burned: “Didst thou, O King, a promise make, And wishest now thy word to break? A son of Raghu's line should scorn To fail in faith, a man forsworn. But if thy soul can bear the shame I will return e'en as I came. Live with thy sons, and joy be thine, False scion of Kakutstha's line.” As Vi[vámitra, mighty sage, Was moved with this tempestuous rage, Earth rocked and reeled throughout her frame, And fear upon the Immortals came. But Saint Va[ishmha, wisest seer, Observant of his vows austere, Saw the whole world convulsed with dread, And thus unto the monarch said: “Thou, born of old Ikshváku's seed, Art Justice' self in mortal weed. Constant and pious, blest by fate, The right thou must not violate. Thou, Raghu's son, so famous through The triple world as just and true, Perform thy bounden duty still, Nor stain thy race by deed of ill. If thou have sworn and now refuse Thou must thy store of merit lose. Then, Monarch, let thy Ráma go, Nor fear for him the demon foe. The fiends shall have no power to hurt
- **Translation**: 

---

### Verse 9 (Ramayana 0.134)
- **Original**: 116 The Ramayana Him trained to war or inexpert, Nor vanquish him in battle field, For Ku[ik's son the youth will shield. He is incarnate Justice, he The best of men for bravery. Embodied love of penance drear, Among the wise without a peer.[036] Full well he knows, great Ku[ik's son, The arms celestial, every one, Arms from the Gods themselves concealed, Far less to other men revealed. These arms to him, when earth he swayed, Mighty Kri[á[va, pleased, conveyed. Kri[á[va's sons they are indeed, Brought forth by Daksha's lovely seed,146 Heralds of conquest, strong and bold, Brilliant, of semblance manifold. Jayá and Vijayá, most fair, And hundred splendid weapons bare. Of Jayá, glorious as the morn, First fifty noble sons were born, Boundless in size yet viewless too, They came the demons to subdue. And fifty children also came Of Vijayá the beauteous dame, Sanháras named, of mighty force, Hard to assail or check in course. Of these the hermit knows the use, And weapons new can he produce. All these the mighty saint will yield To Ráma's hand, to own and wield; 146 These mysterious animated weapons are enumerated in Cantos XXIX and XXX. Daksha was the son of Brahmá and one of the Prajápatis, Demiurgi, or secondary authors of creation.
- **Translation**: 

---

### Verse 10 (Ramayana 0.135)
- **Original**: Canto XXIV. The Spells. 117 And armed with these, beyond a doubt Shall Ráma put those fiends to rout. For Ráma and the people's sake, For thine own good my counsel take, Nor seek, O King, with fond delay, The parting of thy son to stay.” Canto XXIV. The Spells. Va [ishmha thus was speaking still: The monarch, of his own free will, Bade with quick zeal and joyful cheer Ráma and LakshmaG hasten near. Mother and sire in loving care Sped their dear son with rite and prayer: Va [ishmha blessed him ere he went; O'er his loved head the father bent, And then to Ku[ik's son resigned Ráma with LakshmaG close behind. Standing by Vi[vámitra's side, The youthful hero, lotus-eyed, The Wind-God saw, and sent a breeze Whose sweet pure touch just waved the trees. There fell from heaven a flowery rain, And with the song and dance the strain Of shell and tambour sweetly blent As forth the son of Raghu went. The hermit led: behind him came The bow-armed Ráma, dear to fame,
- **Translation**: 

---

### Verse 11 (Ramayana 0.136)
- **Original**: 118 The Ramayana Whose locks were like the raven's wing:147 Then LakshmaG, closely following. The Gods and Indra, filled with joy, Looked down upon the royal boy, And much they longed the death to see Of their ten-headed enemy.148 Ráma and LakshmaG paced behind That hermit of the lofty mind, As the young A[vins,149 heavenly pair, Follow Lord Indra through the air. On arm and hand the guard they wore, Quiver and bow and sword they bore; Two fire-born Gods of War seemed they.150 He, Ziva's self who led the way. Upon fair Sarjú's southern shore They now had walked a league and more, When thus the sage in accents mild To Ráma said:“Beloved child, This lustral water duly touch: My counsel will avail thee much. Forget not all the words I say, 147 Youths of the Kshatriya class used to leave unshorn the side locks of their hair. These were calledKáka-paksha, or raven's wings. 148 The Rákshas or giant RávaG, king of Lanká. 149 “The meaning of A[vins (froma[va a horse, Persian asp, Greek5ÀÀ¿Â, Latin equus, Welsh ech) is Horsemen. They were twin deities of whom frequent mention is made in the Vedas and the Indian myths. The A[vins have much in common with the Dioscuri of Greece, and their mythical genealogy seems to indicate that their origin was astronomical. They were, perhaps, at first the morning star and evening star. They are said to be the children of the sun and the nymph A[viní, who is one of the lunar asterisms personified. In the popular mythology they are regarded as the physicians of the Gods.” G ORRESIO {FNS . 150 The word Kumára (a young prince, a Childe) is also a proper name of Skanda or Kártikeya God of War, the son ofZiva and Umá. The babe was matured in the fire.
- **Translation**: 

---

### Verse 12 (Ramayana 0.137)
- **Original**: Canto XXIV. The Spells. 119 Nor let the occasion slip away. Lo, with two spells I thee invest, The mighty and the mightiest. O'er thee fatigue shall ne'er prevail, Nor age or change thy limbs assail. Thee powers of darkness ne'er shall smite In tranquil sleep or wild delight. No one is there in all the land Thine equal for the vigorous hand. [037] Thou, when thy lips pronounce the spell, Shalt have no peer in heaven or hell. None in the world with thee shall vie, O sinless one, in apt reply, In fortune, knowledge, wit, and tact, Wisdom to plan and skill to act. This double science take, and gain Glory that shall for aye remain. Wisdom and judgment spring from each Of these fair spells whose use I teach. Hunger and thirst unknown to thee, High in the worlds thy rank shall be. For these two spells with might endued, Are the Great Father's heavenly brood, And thee, O Chief, may fitly grace, Thou glory of Kakutstha's race. Virtues which none can match are thine, Lord, from thy birth, of gifts divine, And now these spells of might shall cast Fresh radiance o'er the gifts thou hast.” Then Ráma duly touched the wave, Raised suppliant hands, bowed low his head, And took the spells the hermit gave, Whose soul on contemplation fed. From him whose might these gifts enhanced,
- **Translation**: 

---

### Verse 13 (Ramayana 0.138)
- **Original**: 120 The Ramayana A brighter beam of glory glanced: So shines in all his autumn blaze The Day-God of the thousand rays. The hermit's wants those youths supplied, As pupils use to holy guide. And then the night in sweet content On Sarjú's pleasant bank they spent. Canto XXV. The Hermitage Of Love. Soon as appeared the morning light Up rose the mighty anchorite, And thus to youthful Ráma said, Who lay upon his leafy bed: “High fate is hers who calls thee son: Arise, 'tis break of day; Rise, Chief, and let those rites be done Due at the morning's ray.”151 At that great sage's high behest Up sprang the princely pair, To bathing rites themselves addressed, And breathed the holiest prayer. Their morning task completed, they To Vi[vámitra came That store of holy works, to pay The worship saints may claim. Then to the hallowed spot they went 151 “At the rising of the sun as well as at noon certain observances, invocations, and prayers were prescribed which might under no circumstances be omitted. One of these observances was the recitation of the Sávitrí, a Vedic hymn to the Sun of wonderful beauty.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 14 (Ramayana 0.139)
- **Original**: Canto XXV. The Hermitage Of Love. 121 Along fair Sarjú's side Where mix her waters confluent With three-pathed Gangá's tide.152 There was a sacred hermitage Where saints devout of mind Their lives through many a lengthened age To penance had resigned. That pure abode the princes eyed With unrestrained delight, And thus unto the saint they cried, Rejoicing at the sight: “Whose is that hermitage we see? Who makes his dwelling there? Full of desire to hear are we: O Saint, the truth declare.” The hermit smiling made reply To the two boys' request: “Hear, Ráma, who in days gone by This calm retreat possessed. Kandarpa in apparent form, Called Káma153 by the wise, Dared Umá's154 new-wed lord to storm And make the God his prize. 'Gainst StháGu's155 self, on rites austere 152 Tripathaga, Three-path-go,flowing in heaven, on earth, and under the earth. See Canto XLV. 153 Tennyson's“Indian Cama,” the God of Love, known also by many other names. 154 Umá , orParvatí, was daughter of Himálaya, Monarch of mountains, and wife ofZiva. See Kálidasa'sKumára Sambhava , orBirth of the War-God. 155 StháGu. The Unmoving one, a name ofZiva.
- **Translation**: 

---

### Verse 15 (Ramayana 0.140)
- **Original**: 122 The Ramayana And vows intent,156 they say, His bold rash hand he dared to rear, Though StháGu cried, Away! But the God's eye with scornful glare Fell terrible on him. Dissolved the shape that was so fair[038] And burnt up every limb. Since the great God's terrific rage Destroyed his form and frame, Káma in each succeeding age Has borne Ananga's157 name. So, where his lovely form decayed, This land is Anga styled: Sacred to him of old this shade, And hermits undefiled. Here Scripture-talking elders sway Each sense with firm control, And penance-rites have washed away All sin from every soul. One night, fair boy, we here will spend, A pure stream on each hand, And with to-morrow's light will bend Our steps to yonder strand. Here let us bathe, and free from stain To that pure grove repair, 156 “The practice of austerities, voluntary tortures, and mortifications was anciently universal in India, and was held by the Indians to be of immense efficacy. Hence they mortified themselves to expiate sins, to acquire merits, and to obtain superhuman gifts and powers; the Gods themselves sometimes exercised themselves in such austerities, either to raise themselves to greater power and grandeur, or to counteract the austerities of man which threatened to prevail over them and to deprive them of heaven.… Such austerities were called in Indiatapas(burning ardour, fervent devotion) and he who practised them tapasvin.” G ORRESIO {FNS . 157 The Bodiless one.
- **Translation**: 

---

### Verse 16 (Ramayana 0.141)
- **Original**: Canto XXVI. The Forest Of Tádaká. 123 Sacred to Káma, and remain One night in comfort there.” With penance' far-discerning eye The saintly men beheld Their coming, and with transport high Each holy bosom swelled. To Ku[ik's son the gift they gave That honoured guest should greet, Water they brought his feet to lave, And showed him honor meet. Ráma and LakshmaG next obtained In due degree their share. Then with sweet talk the guests remained, And charmed each listener there. The evening prayers were duly said With voices calm and low: Then on the ground each laid his head And slept till morning's glow. Canto XXVI. The Forest Of Tádaká. When the fair light of morning rose The princely tamers of their foes Followed, his morning worship o'er, The hermit to the river's shore. The high-souled men with thoughtful care A pretty barge had stationed there. All cried,“O lord, this barge ascend, And with thy princely followers bend To yonder side thy prosperous way With naught to check thee or delay.”
- **Translation**: 

---

### Verse 17 (Ramayana 0.142)
- **Original**: 124 The Ramayana Nor did the saint their rede reject: He bade farewell with due respect, And crossed, attended by the twain, That river rushing to the main. When now the bark was half way o'er, Ráma and LakshmaG heard the roar, That louder grew and louder yet, Of waves by dashing waters met. Then Ráma asked the mighty seer: “What is the tumult that I hear Of waters cleft in mid career?” Soon as the speech of Ráma, stirred By deep desire to know, he heard, The pious saint began to tell What paused the waters' roar and swell: “On high Kailása's distant hill There lies a noble lake Whose waters, born from Brahmá's will, The name of Mánas158 take. Thence, hallowing where'er they flow, The streams of Sarjú fall, And wandering through the plains below Embrace Ayodhyá's wall. Still, still preserved in Sarjú's name Sarovar's159 fame we trace. The flood of Brahma whence she came 158 “A celebrated lake regarded in India as sacred. It lies in the lofty region between the northern highlands of the Himálayas and mount Kailása, the region of the sacred lakes. The poem, following the popular Indian belief, makes the river Sarayú (now Sarjú) flow from the Mánasa lake; the sources of the river are a little to the south about a day's journey from the lake. See Lassen, Indische Alterthumshunde, page 34.” G ORRESIO {FNS . Manas means mind; mánasa, mental, mind-born. 159 Sarovarmeans best of lakes. This is another of the poet's fanciful etymolo- gies.
- **Translation**: 

---

### Verse 18 (Ramayana 0.143)
- **Original**: Canto XXVI. The Forest Of Tádaká. 125 To run her holy race. To meet great Gangá here she hies With tributary wave: Hence the loud roar ye hear arise, Of floods that swell and rave. Here, pride of Raghu's line, do thou In humble adoration bow.” He spoke. The princes both obeyed, And reverence to each river paid.160 They reached the southern shore at last, And gaily on their journey passed. A little space beyond there stood A gloomy awe-inspiring wood. The monarch's noble son began To question thus the holy man: “Whose gloomy forest meets mine eye Like some vast cloud that fills the sky? Pathless and dark it seems to be, Where birds in thousands wander free; Where shrill cicadas' cries resound, [039] And fowl of dismal note abound. Lion, rhinoceros, and bear, Boar, tiger, elephant, are there, There shrubs and thorns run wild: Dháo, Sál, Bignonia, Bel,161 are found, And every tree that grows on ground. How is the forest styled?” 160 The confluence of two or more rivers is often a venerated and holy place. The most famous is Prayág or Allahabad, where the Sarasvatí by an underground course is believed to join the Jumna and the Ganges. 161 The botanical names of the trees mentioned in the text are Grislea Tormen- tosa, Shorea Robusta, Echites Antidysenterica, Bignonia Suaveolens,Œ gle Marmelos, and Diospyrus Glutinosa. I have omitted theKutaja(Echites) and theTiG uka (Diospyrus).
- **Translation**: 

---

### Verse 19 (Ramayana 0.144)
- **Original**: 126 The Ramayana The glorious saint this answer made: “Dear child of Raghu, hear Who dwells within the horrid shade That looks so dark and drear. Where now is wood, long ere this day Two broad and fertile lands, Malaja and Karúsha lay, Adorned by heavenly hands. Here, mourning friendship's broken ties, Lord Indra of the thousand eyes Hungered and sorrowed many a day, His brightness soiled with mud and clay, When in a storm of passion he Had slain his dear friend Namuchi. Then came the Gods and saints who bore Their golden pitchers brimming o'er With holy streams that banish stain, And bathed Lord Indra pure again. When in this land the God was freed From spot and stain of impious deed For that his own dear friend he slew, High transport thrilled his bosom through. Then in his joy the lands he blessed, And gave a boon they long possessed: “Because these fertile lands retain The washings of the blot and stain,” 'Twas thus Lord Indra sware, “Malaja and Karúsha's name Shall celebrate with deathless fame My malady and care.”162 162 Here we meet with a fresh myth to account for the name of these regions. Malaja is probably a non-Aryan word signifying a hilly country: taken as a Sanskrit compound it meanssprung from defilement. The word Karúsha appears to have a somewhat similar meaning.
- **Translation**: 

---

### Verse 20 (Ramayana 0.145)
- **Original**: Canto XXVI. The Forest Of Tádaká. 127 “So be it,” all the Immortals cried, When Indra's speech they heard, And with acclaim they ratified The names his lips conferred. Long time, O victor of thy foes, These happy lands had sweet repose, And higher still in fortune rose. At length a spirit, loving ill, Tá aká, wearing shapes at will, Whose mighty strength, exceeding vast, A thousand elephants, surpassed, Was to fierce Sunda, lord and head Of all the demon armies, wed. From her, Lord Indra's peer in might Giant Márícha sprang to light: And she, a constant plague and pest, These two fair realms has long distressed. Now dwelling in her dark abode A league away she bars the road: And we, O Ráma, hence must go Where lies the forest of the foe. Now on thine own right arm rely, And my command obey: Smite the foul monster that she die, And take the plague away. To reach this country none may dare Fallen from its old estate, Which she, whose fury naught can bear, Has left so desolate. And now my truthful tale is told How with accursed sway The spirit plagued this wood of old, And ceases not to-day.”
- **Translation**: 

---

