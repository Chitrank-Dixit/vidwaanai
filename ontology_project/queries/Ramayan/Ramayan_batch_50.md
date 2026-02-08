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

### Verse 1 (Ramayan 0.981)
- **Original**: Canto XXXVII. Márícha's Speech. 963 The monarch's will he strove to stay, Distracted with alarm, For well he knew the might that lay In Ráma's matchless arm. With suppliant hands Márícha stood And thus began to tell His counsel for the tyrant's good, And for his own as well: Canto XXXVII. Márícha's Speech. Márícha gave attentive ear The ruler of the fiends to hear: Then, trained in all the rules that teach The eloquent, began his speech: “'Tis easy task, O King, to find Smooth speakers who delight the mind. But they who urge and they who do Distasteful things and wise, are few. Thou hast not learnt, by proof untaught, And borne away by eager thought, That Ráma, formed for high emprise, With VaruG or with Indra vies. Still let thy people live in peace, Nor let their name and lineage cease, For Ráma with his vengeful hand Can sweep the giants from the land. O, let not Janak's daughter bring Destruction on the giant king. Let not the lady Sítá wake A tempest, on thy head to break.
- **Translation**: 

---

### Verse 2 (Ramayan 0.982)
- **Original**: 964 The Ramayana Still let the dame, by care untried, Be happy by her husband's side, Lest swift avenging ruin fall On glorious Lanká, thee, and all. Men such as thou with wills unchained, Advised by sin and unrestrained, Destroy themselves, the king, the state, And leave the people desolate. Ráma, in bonds of duty held, Was never by his sire expelled. He is no wretch of greedy mind, Dishonour of his Warrior kind. Free from all touch of rancorous spite, All creatures' good is his delight. He saw his sire of truthful heart Deceived by Queen Kaikeyí's art, And said, a true and duteous son, “What thou hast promised shall be done.” To gratify the lady's will, His father's promise to fulfil, He left his realm and all delight For DaG ak wood, an anchorite. No cruel wretch, no senseless fool Is Ráma, unrestrained by rule. This groundless charge has ne'er been heard, Nor shouldst thou speak the slanderous word. Ráma in truth and goodness bold Is Virtue's self in human mould, The sovereign of the world confessed As Indra rules among the Blest. And dost thou plot from him to rend The darling whom his arms defend? Less vain the hope to steal away The glory of the Lord of Day.[273]
- **Translation**: 

---

### Verse 3 (Ramayan 0.983)
- **Original**: Canto XXXVII. Márícha's Speech. 965 O RávaG, guard thee from the fire Of vengeful Ráma's kindled ire,— Each spark a shaft with deadly aim, While bow and falchion feed the flame. Cast not away in hopeless strife Thy realm, thy bliss, thine own dear life. O RávaG of his might beware, A God of Death who will not spare. That bow he knows so well to draw Is the destroyer's flaming jaw, And with his shafts which flash and glow He slays the armies of the foe. Thou ne'er canst win— the thought forego— From the safe guard of shaft and bow King Janak's child, the dear delight Of Ráma unapproached in might. The spouse of Raghu's son, confessed Lion of men with lion chest,— Dearer than life, through good and ill Devoted to her husband's will, The slender-waisted, still must be From thy polluting touches free. Far better grasp with venturous hand The flame to wildest fury fanned. What, King of giants, canst thou gain From this attempt so wild and vain? If in the fight his eye he bend Upon thee, Lord, thy days must end, So life and bliss and royal sway, Lost beyond hope, will pass away. Summon each lord of high estate, And chief, VibhishaG490 to debate. 490 “The younger brother of the giant RávaG; when he and his brother had practiced austerities for a long series of years, Brahmá appeared to offer
- **Translation**: 

---

### Verse 4 (Ramayan 0.984)
- **Original**: 966 The Ramayana With peers in lore of counsel tried Consider, reason, and decide Scan strength and weakness, count the cost, What may be gained and what be lost. Examine and compare aright Thy proper power and Ráma's might, Then if thy weal be still thy care, Thou wilt be prudent and forbear. O giant King, the contest shun, Thy force is all too weak The lord of Kosál's mighty son In deadly fray to seek. King of the hosts that rove at night, O hear what I advise: My prudent counsel do not slight; Be patient and be wise.” Canto XXXVIII. Márícha's Speech. them boons: VibhishaGa asked that he might never meditate any unrighteous- ness.… On the death of RávaG VibhishaGa was installed as Rája of Lanká.” G ARRETT 'S{FNS Classical Dictionary of India.
- **Translation**: 

---

### Verse 5 (Ramayan 0.985)
- **Original**: Canto XXXVIII. Márícha's Speech. 967 “Once in my strength and vigour's pride I roamed this earth from side to side, And towering like a mountain's crest, A thousand Nágas'491 might possessed. Like some vast sable cloud I showed: My golden armlets flashed and glowed. A crown I wore, an axe I swayed, And all I met were sore afraid. I roved where DaG ak wood is spread; On flesh of slaughtered saints I fed. Then Vi[vámitra, sage revered, Holy of heart, my fury feared. To Da[aratha's court he sped And went before the king and said:492 “With me, my lord, thy Ráma send On holy days his aid to lend. Márícha fills my soul with dread And keeps me sore disquieted.” The monarch heard the saint's request And thus the glorious sage addressed: “My boy as yet in arms untrained The age of twelve has scarce attained. But I myself a host will lead To guard thee in the hour of need. My host with fourfold troops complete, The rover of the night shall meet, And I, O best of saints, will kill Thy foeman and thy prayer fulfil.” The king vouchsafed his willing aid: The saint again this answer made: 491 Serpent-gods. 492 See p. 33.
- **Translation**: 

---

### Verse 6 (Ramayan 0.986)
- **Original**: 968 The Ramayana “By Ráma's might, and his alone, Can this great fiend be overthrown. I know in days of yore the Blest Thy saving help in fight confessed. Still of thy famous deeds they tell In heaven above, in earth, and hell, A mighty host obeys thy hest: Here let it still, I pray thee, rest. Thy glorious son, though yet a boy, Will in the fight that fiend destroy. Ráma alone with me shall go: Be happy, victor of the foe.” He spoke: the monarch gave assent, And Ráma to the hermit lent. So to his woodland home in joy Went Vi[vámitra with the boy. With ready bow the champion stood To guard the rites in DaG ak wood. With glorious eyes, most bright to view, Beardless as yet and dark of hue; A single robe his only wear, His temples veiled with waving hair,[274] Around his neck a chain of gold, He grasped the bow he loved to hold; And the young hero's presence made A glory in the forest shade. Thus Ráma with his beauteous mien, Like the young rising moon was seen, I, like a cloud which tempest brings, My arms adorned with golden rings, Proud of the boon which lent me might, Approached where dwelt the anchorite. But Ráma saw me venturing nigh,
- **Translation**: 

---

### Verse 7 (Ramayan 0.987)
- **Original**: Canto XXXVIII. Márícha's Speech. 969 Raising my murderous axe on high; He saw, and fearless of the foe, Strung with calm hand his trusty bow. By pride of conscious strength beguiled, I scorned him as a feeble child, And rushed with an impetuous bound On Vi[vámitra's holy ground. A keen swift shaft he pointed well, The foeman's rage to check and quell, And hurled a hundred leagues away Deep in the ocean waves I lay. He would not kill, but, nobly brave, My forfeit life he chose to save. So there I lay with wandering sense Dazed by that arrow's violence. Long in the sea I lay: at length Slowly returned my sense and strength, And rising from my watery bed To Lanká's town again I sped. Thus was I spared, but all my band Fell slain by Ráma's conquering hand,— A boy, untrained in warrior's skill, Of iron arm and dauntless will. If thou with Ráma still, in spite Of warning and of prayer, wilt fight, I see terrific woes impend, And dire defeat thy days will end. Thy giants all will feel the blow And share the fatal overthrow, Who love the taste of joy and play, The banquet and the festal day. Thine eyes will see destruction take Thy Lanká, lost for Sítá's sake, And stately pile and palace fall
- **Translation**: 

---

### Verse 8 (Ramayan 0.988)
- **Original**: 970 The Ramayana With terrace, dome, and jewelled wall. The good will die: the crime of kings Destruction on the people brings: The sinless die, as in the lake The fish must perish with the snake. The prostrate giants thou wilt see Slain for this folly wrought by thee, Their bodies bright with precious scent And sheen of heavenly ornament; Or see the remnant of thy train Seek refuge far, when help is vain And with their wives, or widowed, fly To every quarter of the sky; Thy mournful eyes, where'er they turn, Will see thy stately city burn, When royal homes with fire are red, And arrowy nets around are spread. A sin that tops all sins in shame Is outrage to another's dame, A thousand wives thy palace fill, And countless beauties wait thy will. O rest contented with thine own, Nor let thy race be overthrown. If thou, O King, hast still delight In rank and wealth and power and might, In noble wives, in troops of friends, In all that royal state attends, I warn thee, cast not all away, Nor challenge Ráma to the fray. If deaf to every friendly prayer, Thou still wilt seek the strife, And from the side of Ráma tear His lovely Maithil wife, Soon will thy life and empire end
- **Translation**: 

---

### Verse 9 (Ramayan 0.989)
- **Original**: Canto XXXIX. Márícha's Speech. 971 Destroyed by Ráma's bow, And thou, with kith and kin and friend, To Yáma's realm must go.” Canto XXXIX. Márícha's Speech. “I told thee of that dreadful day When Ráma smote and spared to slay. Now hear me, RávaG, while I tell What in the after time befell. At length, restored to strength and pride, I and two mighty fiends beside Assumed the forms of deer and strayed Through DaG ak wood in lawn and glade, I reared terrific horns: beneath Were flaming tongue and pointed teeth. I roamed where'er my fancy led, And on the flesh of hermits fed, In sacred haunt, by hallowed tree, Where'er the ritual fires might be. A fearful shape, I wandered through The wood, and many a hermit slew. With ruthless rage the saints I killed Who in the grove their tasks fulfilled. When smitten to the earth they sank, Their flesh I ate, their blood I drank, And with my cruel deeds dismayed All dwellers in the forest shade, Spoiling their rites in bitter hate, With human blood inebriate. Once in the wood I chanced to see
- **Translation**: 

---

### Verse 10 (Ramayan 0.990)
- **Original**: 972 The Ramayana Ráma again, a devotee, A hermit, fed on scanty fare, Who made the good of all his care. His noble wife was by his side, And Lakshma G in the battle tried. In senseless pride I scorned the might Of that illustrious anchorite, And heedless of a hermit foe, Recalled my earlier overthrow.[275] I charged him in my rage and scorn To slay him with my pointed horn, In heedless haste, to fury wrought As on my former wounds I thought. Then from the mighty bow he drew Three foe-destroying arrows flew, Keen-pointed, leaping from the string, Swift as the wind or feathered king. Dire shafts, on flesh of foemen fed, Like rushing thunderbolts they sped, With knots well smoothed and barbs well bent, Shot e'en as one, the arrows went. But I who Ráma's might had felt, And knew the blows the hero dealt, Escaped by rapid flight. The two Who lingered on the spot, he slew. I fled from mortal danger, freed From the dire shaft by timely speed. Now to deep thought my days I give, And as a humble hermit live. In every shrub, in every tree I view that noblest devotee. In every knotted trunk I mark His deerskin and his coat of bark, And see the bow-armed Ráma stand
- **Translation**: 

---

### Verse 11 (Ramayan 0.991)
- **Original**: Canto XXXIX. Márícha's Speech. 973 Like Yáma with his noose in hand. I tell thee RávaG, in my fright A thousand Rámas mock my sight, This wood with every bush and bough Seems all one fearful Ráma now. Throughout the grove there is no spot So lonely where I see him not. He haunts me in my dreams by night, And wakes me with the wild affright. The letter that begins his name Sends terror through my startled frame. The rapid cars whereon we ride, The rich rare jewels, once my pride, Have names493 that strike upon mine ear With hated sound that counsels fear. His mighty strength too well I know, Nor art thou match for such a foe. Too strong were Raghus's son in fight For Namuchi or Bali's might. Then Ráma to the battle dare, Or else be patient and forbear; But, wouldst thou see me live in peace, Let mention of the hero cease. The good whose holy lives were spent In deepest thought, most innocent, With all their people many a time Have perished through another's crime. So in the common ruin, I Must for another's folly die, Do all thy strength and courage can, But ne'er will I approve the plan. For he, in might supremely great, 493 The Sanskrit words for car and jewels begin withra.
- **Translation**: 

---

### Verse 12 (Ramayan 0.992)
- **Original**: 974 The Ramayana The giant world could extirpate, Since, when impetuous Khara sought The grove of Janasthán and fought For ZúrpaGakhá's sake, he died By Ráma's hand in battle tried. How has he wronged thee? Soothly swear, And Ráma's fault and sin declare. I warn thee, and my words are wise, I seek thy people's weal: But if this rede thou wilt despise, Nor hear my last appeal, Thou with thy kin and all thy friends In fight this day wilt die, When his great bow the hero bends, And shafts unerring fly.” Canto XL. Rávan's Speech. But RávaG scorned the rede he gave In timely words to warn and save, E'en as the wretch who hates to live Rejects the herb the leeches give. By fate to sin and ruin spurred, That sage advice the giant heard, Then in reproaches hard and stern Thus to Márícha spoke in turn:
- **Translation**: 

---

### Verse 13 (Ramayan 0.993)
- **Original**: Canto XL. Rávan's Speech. 975 “Is this thy counsel, weak and base, Unworthy of thy giant race? Thy speech is fruitless, vain, thy toil Like casting seed on barren soil. No words of thine shall drive me back From Ráma and the swift attack. A fool is he, inured to sin, And more, of human origin. The craven, at a woman's call To leave his sire, his mother, all The friends he loved, the power and sway, And hasten to the woods away! But now his anger will I rouse, Stealing away his darling spouse. I in thy sight will ravish her From Khara's cruel murderer. Upon this plan my soul is bent, And naught shall move my firm intent, Not if the way through demons led And Gods with Indra at their head. 'Tis thine, when questioned, to explain The hope and fear, the loss and gain, And, when thy king thy thoughts would know, The triumph or the danger show. A prudent counsellor should wait, And speak when ordered in debate, With hands uplifted, calm and meek, If honour and reward he seek. Or, when some prudent course he sees Which, spoken, may his king displease [276] He should by hints of dexterous art His counsel to his lord impart. But prudent words are said in vain When the blunt speech brings grief and pain.
- **Translation**: 

---

### Verse 14 (Ramayan 0.994)
- **Original**: 976 The Ramayana A high-souled king will scarcely thank The man who shames his royal rank. Five are the shapes that kings assume, Of majesty, of grace, and gloom: Like Indra now, or Agni, now Like the dear Moon, with placid brow: Like mighty VaruG now they show, Now fierce as He who rules below. O giant, monarchs lofty-souled Are kind and gentle, stern and bold, With gracious love their gifts dispense And swiftly punish each offence. Thus subjects should their rulers view With all respect and honour due. But folly leads thy heart to slight Thy monarch and neglect his right. Thou hast in lawless pride addressed With bitter words thy royal guest. I asked thee not my strength to scan, Or loss and profit in the plan. I only spoke to tell the deed O mighty one, by me decreed, And bid thee in the peril lend Thy succour to support thy friend. Hear me again, and I will tell How thou canst aid my venture well. In semblance of a golden deer Adorned with silver drops, appear: And near the cottage in the way Of Ráma and his consort stray. Draw nigh, and wandering through the brake With thy strange form her fancy take. The Maithil dame with wondering eyes Will took upon thy fair disguise,
- **Translation**: 

---

### Verse 15 (Ramayan 0.995)
- **Original**: Canto XL. Rávan's Speech. 977 And quickly bid her husband go And bring the deer that charms her so, When Raghu's son has left the place, Still pressing onward in the chase, Cry out,“O Lakshma G! Ah, mine own!” With voice resembling Ráma's tone. When Lakshma G hears his brother's cry, Impelled by Sítá he will fly, Restless with eager love, to aid The hunter in the distant shade. When both her guards have left her side, Even as Indra, thousand-eyed, ClaspsZachí, will I bear away The Maithil dame an easy prey. When thou, my friend, this aid hast lent, Go where thou wilt and live content. True servant, faithful to thy vow, With half my realm I thee endow. Go forth, may luck thy way attend That leads thee to the happy end. I in my car will quickly be In DaG ak wood, and follow thee. So will I cheat this Ráma's eyes And win without a blow the prize; And safe return to Lanká's town With thee, my friend, this day shall crown. But if thou wilt not aid my will, My hand this day thy blood shall spill. Yea, thou must share the destined task, For force will take the help I ask. No bliss that rebel's life attends Whose stubborn will his lord offends. Thy life, if thou the task assay, In jeopardy may stand;
- **Translation**: 

---

### Verse 16 (Ramayan 0.996)
- **Original**: 978 The Ramayana Oppose me, and this very day Thou diest by this hand. Now ponder all that thou hast heard Within thy prudent breast: Reflect with care on every word, And do what seems the best.” Canto XLI. Márícha's Reply. Against his judgment sorely pressed By his imperious lord's behest, Márícha threats of death defied And thus with bitter words replied: “Ah, who, my King, with sinful thought This wild and wicked counsel taught, By which destruction soon will fall On thee, thy sons, thy realm and all? Who is the guilty wretch who sees With envious eye thy blissful ease, And by this plan, so falsely shown, Death's gate for thee has open thrown? With souls impelled by mean desire Thy foes against thy life conspire. They urge thee to destruction's brink, And gladly would they see thee sink. Who with base thought to work thee woe This fatal road has dared to show, And, triumph in his wicked eye, Would see thee enter in and die? To all thy counsellors, untrue, The punishment of death is due,
- **Translation**: 

---

### Verse 17 (Ramayan 0.997)
- **Original**: Canto XLI. Márícha's Reply. 979 Who see thee tempt the dangerous way, Nor strain each nerve thy foot to stay. Wise lords, whose king, by passion led, The path of sin begins to tread, Restrain him while there yet is time: But thine,— they see nor heed the crime. These by their master's will obtain Merit and fame and joy and gain. 'Tis only by their master's grace That servants hold their lofty place. But when the monarch stoops to sin They lose each joy they strive to win, And all the people people high and low Fall in the common overthrow. [277] Merit and fame and honour spring, Best of the mighty, from the king. So all should strive with heart and will To keep the king from every ill. Pride, violence, and sullen hate Will ne'er maintain a monarch's state, And those who cruel deeds advise Must perish when their master dies, Like drivers with their cars o'erthrown In places rough with root and stone. The good whose holy lives were spent On duty's highest laws intent, With wives and children many a time Have perished for another's crime. Hapless are they whose sovereign lord, Opposed to all, by all abhorred, Is cruel-hearted, harsh, severe: Thus might a jackal tend the deer. Now all the giant race await, Destroyed by thee, a speedy fate,
- **Translation**: 

---

### Verse 18 (Ramayan 0.998)
- **Original**: 980 The Ramayana Ruled by a king so cruel-souled, Foolish in heart and uncontrolled. Think not I fear the sudden blow That threatens now to lay me low: I mourn the ruin that I see Impending o'er thy host and thee. Me first perchance will Ráma kill, But soon his hand thy blood will spill. I die, and if by Ráma slain And not by thee, I count it gain. Soon as the hero's face I see His angry eyes will murder me, And if on her thy hands thou lay Thy friends and thou are dead this day. If with my help thou still must dare The lady from her lord to tear, Farewell to all our days are o'er, Lanká and giants are no more. In vain, in vain, an earnest friend, I warn thee, King, and pray. Thou wilt not to my prayers attend, Or heed the words I say So men, when life is fleeting fast And death's sad hour is nigh, Heedless and blinded to the last Reject advice and die.” Canto XLII. Márícha Transformed.
- **Translation**: 

---

### Verse 19 (Ramayan 0.999)
- **Original**: Canto XLII. Márícha Transformed. 981 Márícha thus in wild unrest With bitter words the king addressed. Then to his giant lord in dread, “Arise, and let us go,” he said. “Ah, I have met that mighty lord Armed with his shafts and bow and sword, And if again that bow he bend Our lives that very hour will end. For none that warrior can provoke And think to fly his deadly stroke. Like Yáma with his staff is he, And his dread hand will slaughter thee. What can I more? My words can find No passage to thy stubborn mind. I go, great King, thy task to share, And may success attend thee there.” With that reply and bold consent The giant king was well content. He strained Márícha to his breast And thus with joyful words addressed: “There spoke a hero dauntless still, Obedient to his master's will, Márícha's proper self once more: Some other took thy shape before. Come, mount my jewelled car that flies. Will-governed, through the yielding skies. These asses, goblin-faced, shall bear Us quickly through the fields of air. Attract the lady with thy shape, Then through the wood, at will, escape. And I, when she has no defence, Will seize the dame and bear her thence.”
- **Translation**: 

---

### Verse 20 (Ramayan 0.1000)
- **Original**: 982 The Ramayana Again Márícha made reply, Consent and will to signify. With rapid speed the giants two From the calm hermit dwelling flew, Borne in that wondrous chariot, meet For some great God's celestial seat. They from their airy path looked down On many a wood and many a town, On lake and river, brook and rill, City and realm and towering hill. Soon he whom giant hosts obeyed, Márícha by his side, surveyed The dark expanse of DaG ak wood Where Ráma's hermit cottage stood. They left the flying car, whereon The wealth of gold and jewels shone, And thus the giant king addressed Márícha as his hand he pressed: “Márícha, look! before our eyes Round Ráma's home the plantains rise. His hermitage is now in view: Quick to the work we came to do!” Thus RávaG spoke, Márícha heard Obedient to his master's word, Threw off his giant shape and near The cottage strayed a beauteous deer. With magic power, by rapid change, His borrowed form was fair and strange. A sapphire tipped each horn with light; His face was black relieved with white. The turkis and the ruby shed A glory from his ears and head.
- **Translation**: 

---

