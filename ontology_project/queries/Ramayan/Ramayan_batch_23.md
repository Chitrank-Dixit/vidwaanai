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

### Verse 1 (Ramayan 0.441)
- **Original**: Canto XXIV. Kausalyá Calmed. 423 Can Ráma in the forest live On roots and fruit which woodlands give; Who will believe, who will not fear When the sad story smites his ear, That one so dear, so noble held, Is by the king his sire expelled? Now surely none may Fate resist, Which orders all as it may list, If, Ráma, in thy strength and grace, The woods become thy dwelling-place. A childless mother long I grieved, And many a sigh for offspring heaved, With wistful longing weak and worn Till thou at last, my son, wast born. Fanned by the storm of that desire Deep in my soul I felt the fire, Whose offerings flowed from weeping eyes, With fuel fed of groans and sighs, [123] While round the flame the smoke grew hot Of tears because thou camest not. Now reft of thee, too fiery fierce The flame of woe my heart will pierce, As, when the days of spring return, The sun's hot beams the forest burn. The mother cow still follows near The wanderings of her youngling dear. So close to thine my feet shall be, Where'er thou goest following thee.” Ráma, the noblest lord of men, Heard his fond mother's speech, and then In soothing words like these replied To the sad queen who wept and sighed: “Nay, by Kaikeyí's art beguiled,
- **Translation**: 

---

### Verse 2 (Ramayan 0.442)
- **Original**: 424 The Ramayana When I am banished to the wild, If thou, my mother, also fly, The aged king will surely die. When wedded dames their lords forsake, Long for the crime their souls shall ache. Thou must not e'en in thought within Thy bosom frame so dire a sin. Long as Kakutstha's son, who reigns Lord of the earth, in life remains, Thou must with love his will obey: This duty claims, supreme for aye. Yes, mother, thou and I must be Submissive to my sire's decree, King, husband, sire is he confessed, The lord of all, the worthiest. I in the wilds my days will spend Till twice seven years have reached an end, Then with great joy will come again, And faithful to thy hests remain.” Kau [alyá by her son addressed, With love and passion sore distressed, Afflicted, with her eyes bedewed, To Ráma thus her speech renewed: “Nay, Ráma, but my heart will break If with these queens my home I make. Lead me too with thee; let me go And wander like a woodland roe.” Then, while no tear the hero shed, Thus to the weeping queen he said: “Mother, while lives the husband, he Is woman's lord and deity. O dearest lady, thou and I Our lord and king must ne'er deny;
- **Translation**: 

---

### Verse 3 (Ramayan 0.443)
- **Original**: Canto XXIV. Kausalyá Calmed. 425 The lord of earth himself have we Our guardian wise and friend to be. And Bharat, true to duty's call, Whose sweet words take the hearts of all, Will serve thee well, and ne'er forget The virtuous path before him set. Be this, I pray, thine earnest care, That the old king my father ne'er, When I have parted hence, may know, Grieved for his son, a pang of woe. Let not this grief his soul distress, To kill him with the bitterness. With duteous care, in every thing, Love, comfort, cheer the aged king. Though, best of womankind, a spouse Keeps firmly all her fasts and vows, Nor yet her husband's will obeys, She treads in sin's forbidden ways. She to her husband's will who bends, Goes to high bliss that never ends, Yea, though the Gods have found in her No reverential worshipper. Bent on his weal, a woman still Must seek to do her husband's will: For Scripture, custom, law uphold This duty Heaven revealed of old. Honour true Bráhmans for my sake, And constant offerings duly make, With fire-oblations and with flowers, To all the host of heavenly powers. Look to the coming time, and yearn For the glad hour of my return. And still thy duteous course pursue, Abstemious, humble, kind, and true.
- **Translation**: 

---

### Verse 4 (Ramayan 0.444)
- **Original**: 426 The Ramayana The highest bliss shalt thou obtain When I from exile come again, If, best of those who keep the right, The king my sire still see the light.” The queen, by Ráma thus addressed, Still with a mother's grief oppressed, While her long eyes with tears were dim, Began once more and answered him: “Not by my pleading may be stayed The firm resolve thy soul has made. My hero, thou wilt go; and none The stern commands of Fate may shun. Go forth, dear child whom naught can bend, And may all bliss thy steps attend. Thou wilt return, and that dear day Will chase mine every grief away. Thou wilt return, thy duty done, Thy vows discharged, high glory won; From filial debt wilt thou be free, And sweetest joy will come on me. My son, the will of mighty Fate At every time must dominate, If now it drives thee hence to stray Heedless of me who bid thee stay. Go, strong of arm, go forth, my boy, Go forth, again to come with joy, And thine expectant mother cheer With those sweet tones she loves to hear. O that the blessed hour were nigh When thou shalt glad this anxious eye, With matted hair and hermit dress returning from the wilderness.” Kau [alyá's conscious soul approved,
- **Translation**: 

---

### Verse 5 (Ramayan 0.445)
- **Original**: Canto XXV. Kausalyá's Blessing. 427 As her proud glance she bent On Ráma constant and unmoved, Resolved on banishment. Such words, with happy omens fraught To her dear son she said, Invoking with each eager thought A blessing on his head. [124] Canto XXV. Kausalyá's Blessing. Her grief and woe she cast aside, Her lips with water purified, And thus her benison began That mother of the noblest man: “If thou wilt hear no words of mine, Go forth, thou pride of Raghu's line. Go, darling, and return with speed, Walking where noble spirits lead. May virtue on thy steps attend, And be her faithful lover's friend. May Those to whom thy vows are paid In temple and in holy shade, With all the mighty saints combine To keep that precious life of thine. The arms wise Vi[vámitra292 gave Thy virtuous soul from danger save. Long be thy life: thy sure defence Shall be thy truthful innocence, 292 See P. 41.
- **Translation**: 

---

### Verse 6 (Ramayan 0.446)
- **Original**: 428 The Ramayana And that obedience, naught can tire, To me thy mother and thy sire. May fanes where holy fires are fed, Altars with grass and fuel spread, Each sacrificial ground, each tree, Rock, lake, and mountain, prosper thee. Let old Viráj,293 and Him who made The universe, combine to aid; Let Indra and each guardian Lord Who keeps the worlds, their help afford, And be thy constant friend the Sun, Lord Púshá, Bhaga, Aryuman.294 Fortnights and seasons, nights and days, Years, months, and hours, protect thy ways, Vrihaspati shall still be nigh, The War-God, and the Moon on high, And Nárad295 and the sainted seven296 Shall watch thee from their starry heaven. The mountains, and the seas which ring The world, and VaruGa the King, Sky, ether, and the wind, whate'er Moves not or moves, for thee shall care. Each lunar mansion be benign, With happier light the planets shine; All gods, each light in heaven that glows, Protect my child where'er he goes. The twilight hours, the day and night, Keep in the wood thy steps aright. Watch, minute, instant, as they flee, Shall all bring happiness to thee. 293 The first progeny of Brahmá or Brahmá himself. 294 These are three names of the Sun. 295 See P. 1. 296 The saints who form the constellation of Ursa Major.
- **Translation**: 

---

### Verse 7 (Ramayan 0.447)
- **Original**: Canto XXV. Kausalyá's Blessing. 429 Celestials and the Titan brood Protect thee in thy solitude, And haunt the mighty wood to bless The wanderer in his hermit dress. Fear not, by mightier guardians screened, The giant or night-roving fiend; Nor let the cruel race who tear Man's flesh for food thy bosom scare. Far be the ape, the scorpion's sting, Fly, gnat, and worm, and creeping thing. Thee shall the hungry lion spare, The tiger, elephant, and bear: Safe, from their furious might repose, Safe from the horned buffaloes. Each savage thing the forests breed, That love on human flesh to feed, Shall for my child its rage abate, When thus its wrath I deprecate. Blest be thy ways: may sweet success The valour of my darling bless. To all that Fortune can bestow, Go forth, my child, my Ráma, go. Go forth, O happy in the love Of all the Gods below, above; And in those guardian powers confide Thy paths who keep, thy steps who guide. May Zukra,297 Yáma, Sun, and Moon, And He who gives each golden boon,298 Won by mine earnest prayers, be good To thee, my son, in DaG ak wood. Fire, wind, and smoke, each text and spell From mouths of holy seers that fell, 297 The regent of the planet Venus. 298 Kuvera.
- **Translation**: 

---

### Verse 8 (Ramayan 0.448)
- **Original**: 430 The Ramayana Guard Ráma when his limbs he dips, Or with the stream makes pure his lips! May the great saints and He, the Lord Who made the worlds, by worlds adored, And every God in heaven beside My banished Ráma keep and guide.” Thus with due praise the long-eyed dame, Ennobled by her spotless fame, With wreaths of flowers and precious scent Worshipped the Gods, most reverent. A high-souled Bráhman lit the fire, And offered, at the queen's desire, The holy oil ordained to burn For Ráma's weal and safe return. Kau [alyá best of dames, with care Set oil, wreaths, fuel, mustard, there. Then when the rites of fire had ceased, For Ráma's bliss and health, the priest, Standing without gave what remained In general offering,299 as ordained.[125] Dealing among the twice-horn train Honey, and curds, and oil, and grain, He bade each heart and voice unite To bless the youthful anchorite. Then Ráma's mother, glorious dame Bestowed, to meet the Bráhman's claim, A lordly fee for duty done: And thus again addressed her son: 299 Bali, or the presentation of food to all created beings, is one of the five great sacraments of the Hindu religion: it consists in throwing a small parcel of the offering,Ghee, or rice, or the like, into the open air at the back of the house.
- **Translation**: 

---

### Verse 9 (Ramayan 0.449)
- **Original**: Canto XXV. Kausalyá's Blessing. 431 “Such blessings as the Gods o'erjoyed Poured forth, when Vritra300 was destroyed, On Indra of the thousand eyes, Attend, my child, thine enterprise! Yea, such as Vinatá once gave To King SuparGa301 swift and brave, Who sought the drink that cheers the skies, Attend, my child, thine enterprise! Yea, such as, when the Amrit rose,302 And Indra slew his Daitya foes, The royal Aditi bestowed On Him whose hand with slaughter glowed Of that dire brood of monstrous size, Attend, my child, thine enterprise! E'en such as peerless VishGu graced, When with his triple step he paced, Outbursting from the dwarf's disguise,303 Attend, my child, thine enterprise! Floods, isles, and seasons as they fly, Worlds, Vedas, quarters of the sky, Combine, O mighty-armed, to bless Thee destined heir of happiness!” The long-eyed lady ceased: she shed Pure scent and grain upon his head. And that prized herb whose sovereign power Preserves from dark misfortune's hour, Upon the hero's arm she set, To be his faithful amulet. While holy texts she murmured low, 300 In mythology, a demon slain by Indra. 301 Called also Garu , the King of the birds, offspring of Vinatá. See p. 53. 302 See P. 56. 303 See P. 43.
- **Translation**: 

---

### Verse 10 (Ramayan 0.450)
- **Original**: 432 The Ramayana And spoke glad words though crushed by woe, Concealing with obedient tongue The pangs with which her heart was wrung. She bent, she kissed his brow, she pressed Her darling to her troubled breast: “Firm in thy purpose, go,” she cried, “Go Ráma, and may bliss betide. Attain returning safe and well, Triumphant in Ayodhyá, dwell. Then shall my happy eyes behold The empire by thy will controlled. Then grief and care shall leave no trace, Joy shall light up thy mother's face, And I shall see my darling reign, In moonlike glory come again. These eyes shall fondly gaze on thee So faithful to thy sire's decree, When thou the forest wild shalt quit On thine ancestral throne to sit. Yea, thou shalt turn from exile back, Nor choicest blessings ever lack, Then fill with rapture ever new My bosom and thy consort's too. To Ziva and the heavenly host My worship has been paid, To mighty saint, to godlike ghost, To every wandering shade. Forth to the forest thou wilt hie, Therein to dwell so long: Let all the quarters of the sky Protect my child from wrong.” Her blessings thus the queen bestowed; Then round him fondly paced, And often, while her eyes o'erflowed,
- **Translation**: 

---

### Verse 11 (Ramayan 0.451)
- **Original**: Canto XXVI. Alone With Sítá. 433 Her dearest son embraced. Kau [alyá's honoured feet he pressed, As round her steps she bent, And radiant with her prayers that blessed, To Sítá's home he went. Canto XXVI. Alone With Sítá. So Ráma, to his purpose true, To Queen Kau[alyá bade adieu, Received the benison she gave, And to the path of duty clave. As through the crowded street he passed, A radiance on the way he cast, And each fair grace, by all approved, The bosoms of the people moved. Now of the woeful change no word The fair Videhan bride had heard; The thought of that imperial rite Still filled her bosom with delight. With grateful heart and joyful thought The Gods in worship she had sought, And, well in royal duties learned, Sat longing till her lord returned, Not all unmarked by grief and shame Within his sumptuous home he came, And hurried through the happy crowd With eye dejected, gloomy-browed. Up Sítá sprang, and every limb Trembled with fear at sight of him.
- **Translation**: 

---

### Verse 12 (Ramayan 0.452)
- **Original**: 434 The Ramayana She marked that cheek where anguish fed, Those senses care-disquieted. For, when he looked on her, no more Could his heart hide the load it bore, Nor could the pious chief control The paleness o'er his cheek that stole. His altered cheer, his brow bedewed With clammy drops, his grief she viewed, And cried, consumed with fires of woe, “What, O my lord, has changed thee so?[126] Vrihaspati looks down benign, And the moon rests in Pushya's sign, As Bráhmans sage this day declare: Then whence, my lord, this grief and care? Why does no canopy, like foam For its white beauty, shade thee home, Its hundred ribs spread wide to throw Splendour on thy fair head below? Where are the royal fans, to grace The lotus beauty of thy face, Fair as the moon or wild-swan's wing, And waving round the new-made king? Why do no sweet-toned bards rejoice To hail thee with triumphant voice? No tuneful heralds love to raise Loud music in their monarch's praise? Why do no Bráhmans, Scripture-read, Pour curds and honey on thy head, Anointed, as the laws ordain, With holy rites, supreme to reign? Where are the chiefs of every guild? Where are the myriads should have filled The streets, and followed home their king With merry noise and triumphing?
- **Translation**: 

---

### Verse 13 (Ramayan 0.453)
- **Original**: Canto XXVI. Alone With Sítá. 435 Why does no gold-wrought chariot lead With four brave horses, best for speed? No elephant precede the crowd Like a huge hill or thunder cloud, Marked from his birth for happy fate, Whom signs auspicious decorate? Why does no henchman, young and fair, Precede thee, and delight to bear Entrusted to his reverent hold The burthen of thy throne of gold? Why, if the consecrating rite Be ready, why this mournful plight? Why do I see this sudden change, This altered mien so sad and strange?” To her, as thus she weeping cried, Raghu's illustrious son replied: “Sítá, my honoured sire's decree Commands me to the woods to flee. O high-born lady, nobly bred In the good paths thy footsteps tread, Hear, Janak's daughter, while I tell The story as it all befell. Of old my father true and brave Two boons to Queen Kaikeyí gave. Through these the preparations made For me to-day by her are stayed, For he is bound to disallow This promise by that earlier vow. In DaG ak forest wild and vast Must fourteen years by me be passed. My father's will makes Bharat heir, The kingdom and the throne to share. Now, ere the lonely wild I seek,
- **Translation**: 

---

### Verse 14 (Ramayan 0.454)
- **Original**: 436 The Ramayana I come once more with thee to speak. In Bharat's presence, O my dame, Ne'er speak with pride of Ráma's name: Another's eulogy to hear Is hateful to a monarch's ear. Thou must with love his rule obey To whom my father yields the sway. With love and sweet observance learn His grace, and more the king's, to earn. Now, that my father may not break The words of promise that he spake, To the drear wood my steps are bent: Be firm, good Sítá, and content. Through all that time, my blameless spouse, Keep well thy fasts and holy vows. Rise from thy bed at break of day, And to the Gods due worship pay. With meek and lowly love revere The lord of men, my father dear, And reverence to Kau[alyá show, My mother, worn with eld and woe: By duty's law, O best of dames, High worship from thy love she claims, Nor to the other queens refuse Observance, rendering each her dues: By love and fond attention shown They are my mothers like mine own. Let Bharat andZatrughna bear In thy sweet love a special share: Dear as my life, O let them be Like brother and like son to thee. In every word and deed refrain From aught that Bharat's soul may pain: He is Ayodhyá's king and mine,
- **Translation**: 

---

### Verse 15 (Ramayan 0.455)
- **Original**: Canto XXVII. Sítá's Speech. 437 The head and lord of all our line. For those who serve and love them much With weariless endeavour, touch And win the gracious hearts of kings. While wrath from disobedience springs. Great monarchs from their presence send Their lawful sons who still offend, And welcome to the vacant place Good children of an alien race. Then, best of women, rest thou here, And Bharat's will with love revere. Obedient to thy king remain, And still thy vows of truth maintain. To the wide wood my steps I bend: Make thou thy dwelling here; See that thy conduct ne'er offend, And keep my words, my dear.” Canto XXVII. Sítá's Speech. His sweetly-speaking bride, who best Deserved her lord, he thus addressed. Then tender love bade passion wake, And thus the fair Videhan spake: “What words are these that thou hast said? Contempt of me the thought has bred. O best of heroes, I dismiss With bitter scorn a speech like this: [127]
- **Translation**: 

---

### Verse 16 (Ramayan 0.456)
- **Original**: 438 The Ramayana Unworthy of a warrior's fame It taints a monarch's son with shame, Ne'er to be heard from those who know The science of the sword and bow. My lord, the mother, sire, and son Receive their lots by merit won; The brother and the daughter find The portions to their deeds assigned. The wife alone, whate'er await, Must share on earth her husband's fate. So now the king's command which sends Thee to the wild, to me extends. The wife can find no refuge, none, In father, mother, self, or son: Both here, and when they vanish hence, Her husband is her sole defence. If, Raghu's son, thy steps are led Where DaG ak's pathless wilds are spread, My foot before thine own shall pass Through tangled thorn and matted grass. Dismiss thine anger and thy doubt: Like refuse water cast them out, And lead me, O my hero, hence— I know not sin— with confidence. Whate'er his lot, 'tis far more sweet To follow still a husband's feet Than in rich palaces to lie, Or roam at pleasure through the sky. My mother and my sire have taught What duty bids, and trained each thought, Nor have I now mine ear to turn The duties of a wife to learn. I'll seek with thee the woodland dell And pathless wild where no men dwell,
- **Translation**: 

---

### Verse 17 (Ramayan 0.457)
- **Original**: Canto XXVII. Sítá's Speech. 439 Where tribes of silvan creatures roam, And many a tiger makes his home. My life shall pass as pleasant there As in my father's palace fair. The worlds shall wake no care in me; My only care be truth to thee. There while thy wish I still obey, True to my vows with thee I'll stray, And there shall blissful hours be spent In woods with honey redolent. In forest shades thy mighty arm Would keep a stranger's life from harm, And how shall Sítá think of fear When thou, O glorious lord, art near? Heir of high bliss, my choice is made, Nor can I from my will be stayed. Doubt not; the earth will yield me roots, These will I eat, and woodland fruits; And as with thee I wander there I will not bring thee grief or care. I long, when thou, wise lord, art nigh, All fearless, with delighted eye To gaze upon the rocky hill, The lake, the fountain, and the rill; To sport with thee, my limbs to cool, In some pure lily-covered pool, While the white swan's and mallard's wings Are plashing in the water-springs. So would a thousand seasons flee Like one sweet day, if spent with thee. Without my lord I would not prize A home with Gods above the skies: Without my lord, my life to bless, Where could be heaven or happiness?
- **Translation**: 

---

### Verse 18 (Ramayan 0.458)
- **Original**: 440 The Ramayana Forbid me not: with thee I go The tangled wood to tread. There will I live with thee, as though This roof were o'er my head. My will for thine shall be resigned; Thy feet my steps shall guide. Thou, only thou, art in my mind: I heed not all beside. Thy heart shall ne'er by me be grieved; Do not my prayer deny: Take me, dear lord; of thee bereaved Thy Sítá swears to die.” These words the duteous lady spake, Nor would he yet consent His faithful wife with him to take To share his banishment. He soothed her with his gentle speech; To change her will he strove; And much he said the woes to teach Of those in wilds who rove. Canto XXVIII. The Dangers Of The Wood. Thus Sítá spake, and he who knew His duty, to its orders true, Was still reluctant as the woes Of forest life before him rose. He sought to soothe her grief, to dry The torrent from each brimming eye, And then, her firm resolve to shake, These words the pious hero spake:
- **Translation**: 

---

### Verse 19 (Ramayan 0.459)
- **Original**: Canto XXVIII. The Dangers Of The Wood. 441 “O daughter of a noble line, Whose steps from virtue ne'er decline, Remain, thy duties here pursue, As my fond heart would have thee do. Now hear me, Sítá, fair and weak, And do the words that I shall speak. Attend and hear while I explain Each danger in the wood, each pain. Thy lips have spoken: I condemn The foolish words that fell from them. This senseless plan, this wish of thine To live a forest life, resign. The names of trouble and distress Suit well the tangled wilderness. In the wild wood no joy I know, A forest life is nought but woe. The lion in his mountain cave Answers the torrents as they rave, And forth his voice of terror throws: The wood, my love, is full of woes. [128] There mighty monsters fearless play, And in their maddened onset slay The hapless wretch who near them goes: The wood, my love, is full of woes. 'Tis hard to ford each treacherous flood, So thick with crocodiles and mud, Where the wild elephants repose: The wood, my love, is full of woes. Or far from streams the wanderer strays Through thorns and creeper-tangled ways, While round him many a wild-cock crows: The wood, my love, is full of woes. On the cold ground upon a heap Of gathered leaves condemned to sleep,
- **Translation**: 

---

### Verse 20 (Ramayan 0.460)
- **Original**: 442 The Ramayana Toil-wearied, will his eyelids close: The wood, my love, is full of woes. Long days and nights must he content His soul with scanty aliment, What fruit the wind from branches blows: The wood, my love, is full of woes. O Sítá, while his strength may last, The ascetic in the wood must fast, Coil on his head his matted hair, And bark must be his only wear. To Gods and spirits day by day The ordered worship he must pay, And honour with respectful care Each wandering guest who meets him there. The bathing rites he ne'er must shun At dawn, at noon, at set of sun, Obedient to the law he knows: The wood, my love, is full of woes. To grace the altar must be brought The gift of flowers his hands have sought— The debt each pious hermit owes: The wood, my love, is full of woes. The devotee must be content To live, severely abstinent, On what the chance of fortune shows: The wood, my love, is full of woes. Hunger afflicts him evermore: The nights are black, the wild winds roar; And there are dangers worse than those: The wood, my love, is full of woes. There creeping things in every form Infest the earth, the serpents swarm, And each proud eye with fury glows: The wood, my love, is full of woes.
- **Translation**: 

---

