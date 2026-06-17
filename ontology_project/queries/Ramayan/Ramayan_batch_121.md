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

### Verse 1 (Ramayana 0.446)
- **Original**: 428 The Ramayana And that obedience, naught can tire, To me thy mother and thy sire. May fanes where holy fires are fed, Altars with grass and fuel spread, Each sacrificial ground, each tree, Rock, lake, and mountain, prosper thee. Let old Viráj,293 and Him who made The universe, combine to aid; Let Indra and each guardian Lord Who keeps the worlds, their help afford, And be thy constant friend the Sun, Lord Púshá, Bhaga, Aryuman.294 Fortnights and seasons, nights and days, Years, months, and hours, protect thy ways, Vrihaspati shall still be nigh, The War-God, and the Moon on high, And Nárad295 and the sainted seven296 Shall watch thee from their starry heaven. The mountains, and the seas which ring The world, and VaruGa the King, Sky, ether, and the wind, whate'er Moves not or moves, for thee shall care. Each lunar mansion be benign, With happier light the planets shine; All gods, each light in heaven that glows, Protect my child where'er he goes. The twilight hours, the day and night, Keep in the wood thy steps aright. Watch, minute, instant, as they flee, Shall all bring happiness to thee. 293 The first progeny of Brahmá or Brahmá himself. 294 These are three names of the Sun. 295 See P. 1. 296 The saints who form the constellation of Ursa Major.
- **Translation**: 

---

### Verse 2 (Ramayana 0.447)
- **Original**: Canto XXV. Kausalyá's Blessing. 429 Celestials and the Titan brood Protect thee in thy solitude, And haunt the mighty wood to bless The wanderer in his hermit dress. Fear not, by mightier guardians screened, The giant or night-roving fiend; Nor let the cruel race who tear Man's flesh for food thy bosom scare. Far be the ape, the scorpion's sting, Fly, gnat, and worm, and creeping thing. Thee shall the hungry lion spare, The tiger, elephant, and bear: Safe, from their furious might repose, Safe from the horned buffaloes. Each savage thing the forests breed, That love on human flesh to feed, Shall for my child its rage abate, When thus its wrath I deprecate. Blest be thy ways: may sweet success The valour of my darling bless. To all that Fortune can bestow, Go forth, my child, my Ráma, go. Go forth, O happy in the love Of all the Gods below, above; And in those guardian powers confide Thy paths who keep, thy steps who guide. May Zukra,297 Yáma, Sun, and Moon, And He who gives each golden boon,298 Won by mine earnest prayers, be good To thee, my son, in DaG ak wood. Fire, wind, and smoke, each text and spell From mouths of holy seers that fell, 297 The regent of the planet Venus. 298 Kuvera.
- **Translation**: 

---

### Verse 3 (Ramayana 0.448)
- **Original**: 430 The Ramayana Guard Ráma when his limbs he dips, Or with the stream makes pure his lips! May the great saints and He, the Lord Who made the worlds, by worlds adored, And every God in heaven beside My banished Ráma keep and guide.” Thus with due praise the long-eyed dame, Ennobled by her spotless fame, With wreaths of flowers and precious scent Worshipped the Gods, most reverent. A high-souled Bráhman lit the fire, And offered, at the queen's desire, The holy oil ordained to burn For Ráma's weal and safe return. Kau [alyá best of dames, with care Set oil, wreaths, fuel, mustard, there. Then when the rites of fire had ceased, For Ráma's bliss and health, the priest, Standing without gave what remained In general offering,299 as ordained.[125] Dealing among the twice-horn train Honey, and curds, and oil, and grain, He bade each heart and voice unite To bless the youthful anchorite. Then Ráma's mother, glorious dame Bestowed, to meet the Bráhman's claim, A lordly fee for duty done: And thus again addressed her son: 299 Bali, or the presentation of food to all created beings, is one of the five great sacraments of the Hindu religion: it consists in throwing a small parcel of the offering,Ghee, or rice, or the like, into the open air at the back of the house.
- **Translation**: 

---

### Verse 4 (Ramayana 0.449)
- **Original**: Canto XXV. Kausalyá's Blessing. 431 “Such blessings as the Gods o'erjoyed Poured forth, when Vritra300 was destroyed, On Indra of the thousand eyes, Attend, my child, thine enterprise! Yea, such as Vinatá once gave To King SuparGa301 swift and brave, Who sought the drink that cheers the skies, Attend, my child, thine enterprise! Yea, such as, when the Amrit rose,302 And Indra slew his Daitya foes, The royal Aditi bestowed On Him whose hand with slaughter glowed Of that dire brood of monstrous size, Attend, my child, thine enterprise! E'en such as peerless VishGu graced, When with his triple step he paced, Outbursting from the dwarf's disguise,303 Attend, my child, thine enterprise! Floods, isles, and seasons as they fly, Worlds, Vedas, quarters of the sky, Combine, O mighty-armed, to bless Thee destined heir of happiness!” The long-eyed lady ceased: she shed Pure scent and grain upon his head. And that prized herb whose sovereign power Preserves from dark misfortune's hour, Upon the hero's arm she set, To be his faithful amulet. While holy texts she murmured low, 300 In mythology, a demon slain by Indra. 301 Called also Garu , the King of the birds, offspring of Vinatá. See p. 53. 302 See P. 56. 303 See P. 43.
- **Translation**: 

---

### Verse 5 (Ramayana 0.450)
- **Original**: 432 The Ramayana And spoke glad words though crushed by woe, Concealing with obedient tongue The pangs with which her heart was wrung. She bent, she kissed his brow, she pressed Her darling to her troubled breast: “Firm in thy purpose, go,” she cried, “Go Ráma, and may bliss betide. Attain returning safe and well, Triumphant in Ayodhyá, dwell. Then shall my happy eyes behold The empire by thy will controlled. Then grief and care shall leave no trace, Joy shall light up thy mother's face, And I shall see my darling reign, In moonlike glory come again. These eyes shall fondly gaze on thee So faithful to thy sire's decree, When thou the forest wild shalt quit On thine ancestral throne to sit. Yea, thou shalt turn from exile back, Nor choicest blessings ever lack, Then fill with rapture ever new My bosom and thy consort's too. To Ziva and the heavenly host My worship has been paid, To mighty saint, to godlike ghost, To every wandering shade. Forth to the forest thou wilt hie, Therein to dwell so long: Let all the quarters of the sky Protect my child from wrong.” Her blessings thus the queen bestowed; Then round him fondly paced, And often, while her eyes o'erflowed,
- **Translation**: 

---

### Verse 6 (Ramayana 0.451)
- **Original**: Canto XXVI. Alone With Sítá. 433 Her dearest son embraced. Kau [alyá's honoured feet he pressed, As round her steps she bent, And radiant with her prayers that blessed, To Sítá's home he went. Canto XXVI. Alone With Sítá. So Ráma, to his purpose true, To Queen Kau[alyá bade adieu, Received the benison she gave, And to the path of duty clave. As through the crowded street he passed, A radiance on the way he cast, And each fair grace, by all approved, The bosoms of the people moved. Now of the woeful change no word The fair Videhan bride had heard; The thought of that imperial rite Still filled her bosom with delight. With grateful heart and joyful thought The Gods in worship she had sought, And, well in royal duties learned, Sat longing till her lord returned, Not all unmarked by grief and shame Within his sumptuous home he came, And hurried through the happy crowd With eye dejected, gloomy-browed. Up Sítá sprang, and every limb Trembled with fear at sight of him.
- **Translation**: 

---

### Verse 7 (Ramayana 0.452)
- **Original**: 434 The Ramayana She marked that cheek where anguish fed, Those senses care-disquieted. For, when he looked on her, no more Could his heart hide the load it bore, Nor could the pious chief control The paleness o'er his cheek that stole. His altered cheer, his brow bedewed With clammy drops, his grief she viewed, And cried, consumed with fires of woe, “What, O my lord, has changed thee so?[126] Vrihaspati looks down benign, And the moon rests in Pushya's sign, As Bráhmans sage this day declare: Then whence, my lord, this grief and care? Why does no canopy, like foam For its white beauty, shade thee home, Its hundred ribs spread wide to throw Splendour on thy fair head below? Where are the royal fans, to grace The lotus beauty of thy face, Fair as the moon or wild-swan's wing, And waving round the new-made king? Why do no sweet-toned bards rejoice To hail thee with triumphant voice? No tuneful heralds love to raise Loud music in their monarch's praise? Why do no Bráhmans, Scripture-read, Pour curds and honey on thy head, Anointed, as the laws ordain, With holy rites, supreme to reign? Where are the chiefs of every guild? Where are the myriads should have filled The streets, and followed home their king With merry noise and triumphing?
- **Translation**: 

---

### Verse 8 (Ramayana 0.453)
- **Original**: Canto XXVI. Alone With Sítá. 435 Why does no gold-wrought chariot lead With four brave horses, best for speed? No elephant precede the crowd Like a huge hill or thunder cloud, Marked from his birth for happy fate, Whom signs auspicious decorate? Why does no henchman, young and fair, Precede thee, and delight to bear Entrusted to his reverent hold The burthen of thy throne of gold? Why, if the consecrating rite Be ready, why this mournful plight? Why do I see this sudden change, This altered mien so sad and strange?” To her, as thus she weeping cried, Raghu's illustrious son replied: “Sítá, my honoured sire's decree Commands me to the woods to flee. O high-born lady, nobly bred In the good paths thy footsteps tread, Hear, Janak's daughter, while I tell The story as it all befell. Of old my father true and brave Two boons to Queen Kaikeyí gave. Through these the preparations made For me to-day by her are stayed, For he is bound to disallow This promise by that earlier vow. In DaG ak forest wild and vast Must fourteen years by me be passed. My father's will makes Bharat heir, The kingdom and the throne to share. Now, ere the lonely wild I seek,
- **Translation**: 

---

### Verse 9 (Ramayana 0.454)
- **Original**: 436 The Ramayana I come once more with thee to speak. In Bharat's presence, O my dame, Ne'er speak with pride of Ráma's name: Another's eulogy to hear Is hateful to a monarch's ear. Thou must with love his rule obey To whom my father yields the sway. With love and sweet observance learn His grace, and more the king's, to earn. Now, that my father may not break The words of promise that he spake, To the drear wood my steps are bent: Be firm, good Sítá, and content. Through all that time, my blameless spouse, Keep well thy fasts and holy vows. Rise from thy bed at break of day, And to the Gods due worship pay. With meek and lowly love revere The lord of men, my father dear, And reverence to Kau[alyá show, My mother, worn with eld and woe: By duty's law, O best of dames, High worship from thy love she claims, Nor to the other queens refuse Observance, rendering each her dues: By love and fond attention shown They are my mothers like mine own. Let Bharat andZatrughna bear In thy sweet love a special share: Dear as my life, O let them be Like brother and like son to thee. In every word and deed refrain From aught that Bharat's soul may pain: He is Ayodhyá's king and mine,
- **Translation**: 

---

### Verse 10 (Ramayana 0.455)
- **Original**: Canto XXVII. Sítá's Speech. 437 The head and lord of all our line. For those who serve and love them much With weariless endeavour, touch And win the gracious hearts of kings. While wrath from disobedience springs. Great monarchs from their presence send Their lawful sons who still offend, And welcome to the vacant place Good children of an alien race. Then, best of women, rest thou here, And Bharat's will with love revere. Obedient to thy king remain, And still thy vows of truth maintain. To the wide wood my steps I bend: Make thou thy dwelling here; See that thy conduct ne'er offend, And keep my words, my dear.” Canto XXVII. Sítá's Speech. His sweetly-speaking bride, who best Deserved her lord, he thus addressed. Then tender love bade passion wake, And thus the fair Videhan spake: “What words are these that thou hast said? Contempt of me the thought has bred. O best of heroes, I dismiss With bitter scorn a speech like this: [127]
- **Translation**: 

---

### Verse 11 (Ramayana 0.456)
- **Original**: 438 The Ramayana Unworthy of a warrior's fame It taints a monarch's son with shame, Ne'er to be heard from those who know The science of the sword and bow. My lord, the mother, sire, and son Receive their lots by merit won; The brother and the daughter find The portions to their deeds assigned. The wife alone, whate'er await, Must share on earth her husband's fate. So now the king's command which sends Thee to the wild, to me extends. The wife can find no refuge, none, In father, mother, self, or son: Both here, and when they vanish hence, Her husband is her sole defence. If, Raghu's son, thy steps are led Where DaG ak's pathless wilds are spread, My foot before thine own shall pass Through tangled thorn and matted grass. Dismiss thine anger and thy doubt: Like refuse water cast them out, And lead me, O my hero, hence— I know not sin— with confidence. Whate'er his lot, 'tis far more sweet To follow still a husband's feet Than in rich palaces to lie, Or roam at pleasure through the sky. My mother and my sire have taught What duty bids, and trained each thought, Nor have I now mine ear to turn The duties of a wife to learn. I'll seek with thee the woodland dell And pathless wild where no men dwell,
- **Translation**: 

---

### Verse 12 (Ramayana 0.457)
- **Original**: Canto XXVII. Sítá's Speech. 439 Where tribes of silvan creatures roam, And many a tiger makes his home. My life shall pass as pleasant there As in my father's palace fair. The worlds shall wake no care in me; My only care be truth to thee. There while thy wish I still obey, True to my vows with thee I'll stray, And there shall blissful hours be spent In woods with honey redolent. In forest shades thy mighty arm Would keep a stranger's life from harm, And how shall Sítá think of fear When thou, O glorious lord, art near? Heir of high bliss, my choice is made, Nor can I from my will be stayed. Doubt not; the earth will yield me roots, These will I eat, and woodland fruits; And as with thee I wander there I will not bring thee grief or care. I long, when thou, wise lord, art nigh, All fearless, with delighted eye To gaze upon the rocky hill, The lake, the fountain, and the rill; To sport with thee, my limbs to cool, In some pure lily-covered pool, While the white swan's and mallard's wings Are plashing in the water-springs. So would a thousand seasons flee Like one sweet day, if spent with thee. Without my lord I would not prize A home with Gods above the skies: Without my lord, my life to bless, Where could be heaven or happiness?
- **Translation**: 

---

### Verse 13 (Ramayana 0.458)
- **Original**: 440 The Ramayana Forbid me not: with thee I go The tangled wood to tread. There will I live with thee, as though This roof were o'er my head. My will for thine shall be resigned; Thy feet my steps shall guide. Thou, only thou, art in my mind: I heed not all beside. Thy heart shall ne'er by me be grieved; Do not my prayer deny: Take me, dear lord; of thee bereaved Thy Sítá swears to die.” These words the duteous lady spake, Nor would he yet consent His faithful wife with him to take To share his banishment. He soothed her with his gentle speech; To change her will he strove; And much he said the woes to teach Of those in wilds who rove. Canto XXVIII. The Dangers Of The Wood. Thus Sítá spake, and he who knew His duty, to its orders true, Was still reluctant as the woes Of forest life before him rose. He sought to soothe her grief, to dry The torrent from each brimming eye, And then, her firm resolve to shake, These words the pious hero spake:
- **Translation**: 

---

### Verse 14 (Ramayana 0.459)
- **Original**: Canto XXVIII. The Dangers Of The Wood. 441 “O daughter of a noble line, Whose steps from virtue ne'er decline, Remain, thy duties here pursue, As my fond heart would have thee do. Now hear me, Sítá, fair and weak, And do the words that I shall speak. Attend and hear while I explain Each danger in the wood, each pain. Thy lips have spoken: I condemn The foolish words that fell from them. This senseless plan, this wish of thine To live a forest life, resign. The names of trouble and distress Suit well the tangled wilderness. In the wild wood no joy I know, A forest life is nought but woe. The lion in his mountain cave Answers the torrents as they rave, And forth his voice of terror throws: The wood, my love, is full of woes. [128] There mighty monsters fearless play, And in their maddened onset slay The hapless wretch who near them goes: The wood, my love, is full of woes. 'Tis hard to ford each treacherous flood, So thick with crocodiles and mud, Where the wild elephants repose: The wood, my love, is full of woes. Or far from streams the wanderer strays Through thorns and creeper-tangled ways, While round him many a wild-cock crows: The wood, my love, is full of woes. On the cold ground upon a heap Of gathered leaves condemned to sleep,
- **Translation**: 

---

### Verse 15 (Ramayana 0.460)
- **Original**: 442 The Ramayana Toil-wearied, will his eyelids close: The wood, my love, is full of woes. Long days and nights must he content His soul with scanty aliment, What fruit the wind from branches blows: The wood, my love, is full of woes. O Sítá, while his strength may last, The ascetic in the wood must fast, Coil on his head his matted hair, And bark must be his only wear. To Gods and spirits day by day The ordered worship he must pay, And honour with respectful care Each wandering guest who meets him there. The bathing rites he ne'er must shun At dawn, at noon, at set of sun, Obedient to the law he knows: The wood, my love, is full of woes. To grace the altar must be brought The gift of flowers his hands have sought— The debt each pious hermit owes: The wood, my love, is full of woes. The devotee must be content To live, severely abstinent, On what the chance of fortune shows: The wood, my love, is full of woes. Hunger afflicts him evermore: The nights are black, the wild winds roar; And there are dangers worse than those: The wood, my love, is full of woes. There creeping things in every form Infest the earth, the serpents swarm, And each proud eye with fury glows: The wood, my love, is full of woes.
- **Translation**: 

---

### Verse 16 (Ramayana 0.461)
- **Original**: Canto XXIX. Sítá's Appeal. 443 The snakes that by the rives hide In sinuous course like rivers glide, And line the path with deadly foes: The wood, my love, is full of woes. Scorpions, and grasshoppers, and flies Disturb the wanderer as he lies, And wake him from his troubled doze: The wood, my love, is full of woes. Trees, thorny bushes, intertwined, Their branched ends together bind, And dense with grass the thicket grows: The wood, my dear, is full of woes, With many ills the flesh is tried, When these and countless fears beside Vex those who in the wood remain: The wilds are naught but grief and pain. Hope, anger must be cast aside, To penance every thought applied: No fear must be of things to fear: Hence is the wood for ever drear. Enough, my love: thy purpose quit: For forest life thou art not fit. As thus I think on all, I see The wild wood is no place for thee.” Canto XXIX. Sítá's Appeal. Thus Ráma spake. Her lord's address The lady heard with deep distress, And, as the tear bedimmed her eye, In soft low accents made reply:
- **Translation**: 

---

### Verse 17 (Ramayana 0.462)
- **Original**: 444 The Ramayana “The perils of the wood, and all The woes thou countest to appal, Led by my love I deem not pain; Each woe a charm, each loss a gain. Tiger, and elephant, and deer, Bull, lion, buffalo, in fear, Soon as thy matchless form they see, With every silvan beast will flee. With thee, O Ráma, I must go: My sire's command ordains it so. Bereft of thee, my lonely heart Must break, and life and I must part. While thou, O mighty lord, art nigh, Not even He who rules the sky, Though He is strongest of the strong, With all his might can do me wrong. Nor can a lonely woman left By her dear husband live bereft. In my great love, my lord, I ween, The truth of this thou mayst have seen. In my sire's palace long ago I heard the chief of those who know, The truth-declaring Bráhmans, tell My fortune, in the wood to dwell. I heard their promise who divine The future by each mark and sign, And from that hour have longed to lead The forest life their lips decreed. Now, mighty Ráma, I must share Thy father's doom which sends thee there; In this I will not be denied, But follow, love, where thou shalt guide. O husband, I will go with thee, Obedient to that high decree.
- **Translation**: 

---

### Verse 18 (Ramayana 0.463)
- **Original**: Canto XXIX. Sítá's Appeal. 445 Now let the Bráhmans' words be true, For this the time they had in view. I know full well the wood has woes; But they disturb the lives of those Who in the forest dwell, nor hold Their rebel senses well controlled. [129] In my sire's halls, ere I was wed, I heard a dame who begged her bread Before my mother's face relate What griefs a forest life await. And many a time in sport I prayed To seek with thee the greenwood shade, For O, my heart on this is set, To follow thee, dear anchoret. May blessings on thy life attend: I long with thee my steps to bend, For with such hero as thou art This pilgrimage enchants my heart. Still close, my lord, to thy dear side My spirit will be purified: Love from all sin my soul will free: My husband is a God to me. So, love, with thee shall I have bliss And share the life that follows this. I heard a Bráhman, dear to fame, This ancient Scripture text proclaim: “The woman whom on earth below Her parents on a man bestow, And lawfully their hands unite With water and each holy rite, She in this world shall be his wife, His also in the after life.” Then tell me, O beloved, why Thou wilt this earnest prayer deny,
- **Translation**: 

---

### Verse 19 (Ramayana 0.464)
- **Original**: 446 The Ramayana Nor take me with thee to the wood, Thine own dear wife so true and good. But if thou wilt not take me there Thus grieving in my wild despair, To fire or water I will fly, Or to the poisoned draught, and die.” So thus to share his exile, she Besought him with each earnest plea, Nor could she yet her lord persuade To take her to the lonely shade. The answer of the strong-armed chief Smote the Videhan's soul with grief, And from her eyes the torrents came bathing the bosom of the dame. Canto XXX. The Triumph Of Love. The daughter of Videha's king, While Ráma strove to soothe the sting Of her deep anguish, thus began Once more in furtherance of her plan: And with her spirit sorely tried By fear and anger, love and pride, With keenly taunting words addressed Her hero of the stately breast: “Why did the king my sire, who reigns O'er fair Videha's wide domains, Hail Ráma son with joy unwise, A woman in a man's disguise? Now falsely would the people say,
- **Translation**: 

---

### Verse 20 (Ramayana 0.465)
- **Original**: Canto XXX. The Triumph Of Love. 447 By idle fancies led astray, That Ráma's own are power and might, As glorious as the Lord of Light. Why sinkest thou in such dismay? What fears upon thy spirit weigh, That thou, O Ráma, fain wouldst flee From her who thinks of naught but thee? To thy dear will am I resigned In heart and body, soul and mind, As Sávitrí gave all to one, Satyaván, Dyumatsena's son.304 Not e'en in fancy can I brook To any guard save thee to look: Let meaner wives their houses shame, To go with thee is all my claim. Like some low actor, deemst thou fit Thy wife to others to commit— Thine own, espoused in maiden youth, Thy wife so long, unblamed for truth? Do thou, my lord, his will obey For whom thou losest royal sway, To whom thou wouldst thy wife confide— Not me, but thee, his wish may guide. Thou must not here thy wife forsake, And to the wood thy journey make, Whether stern penance, grief, and care, Or rule or heaven await thee there. Nor shall fatigue my limbs distress When wandering in the wilderness: Each path which near to thee I tread Shall seem a soft luxurious bed. 304 The story of Sávitrí, told in the Mahábhárat, has been admirably translated by Rückert, and elegantly epitomized by Mrs. Manning inIndia, Ancient and Mediæval. There is a free rendering of the story inIdylls from the Sanskrit.
- **Translation**: 

---

