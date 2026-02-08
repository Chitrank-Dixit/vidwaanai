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

### Verse 1 (Ramayan 0.801)
- **Original**: Canto CXIII. Bharat's Return. 783 And when the chieftain bold and sage Had reached that holy hermitage, Down from the car he sprang to greet The saint, and bowed before his feet. High rapture filled the hermit's breast, Who thus the royal prince addressed: “Say, Bharat, is thy duty done? Hast thou with Ráma met, my son?” The chief whose soul to virtue clave This answer to the hermit gave: “I prayed him with our holy guide: But Raghu's son our prayer denied, And long besought by both of us He answered Saint Va[ishmha thus: “True to my vow, I still will be Observant of my sire's decree: Till fourteen years complete their course That promise shall remain in force.” The saint in highest wisdom taught, These solemn words with wisdom fraught, To him in lore of language learned Most eloquent himself returned: “Obey my rede: let Bharat hold This pair of sandals decked with gold: They in Ayodhyá shall ensure Our welfare, and our bliss secure.” When Ráma heard the royal priest He rose, and looking to the east Consigned the sandals to my hand That they for him might guard the land. Then from the high-souled chief's abode I turned upon my homeward road, Dismissed by him, and now this pair
- **Translation**: 

---

### Verse 2 (Ramayan 0.802)
- **Original**: 784 The Ramayana Of sandals to Ayodhyá bear.” To him the hermit thus replied, By Bharat's tidings gratified: “No marvel thoughts so just and true, Thou best of all who right pursue, Should dwell in thee, O Prince of men, As waters gather in the glen. He is not dead, we mourn in vain: Thy blessed father lives again, Whose noble son we thus behold Like Virtue's self in human mould.” He ceased: before him Bharat fell To clasp his feet, and said farewell: His reverent steps around him bent, And onward to Ayodhyá went. His host of followers stretching far With many an elephant and car, Waggon and steed, and mighty train, Traversed their homeward way again. O'er holy Yamuná they sped, Fair stream, with waves engarlanded, And then once more the rivers' queen, The blessed Gangá's self was seen. Then making o'er that flood his way, Where crocodiles and monsters lay, The king toZringavera drew His host and royal retinue. His onward way he thence pursued, And soon renowned Ayodhyá viewed. Then burnt by woe and sad of cheer Bharat addressed the charioteer: “Ah, see, Ayodhyá dark and sad,
- **Translation**: 

---

### Verse 3 (Ramayan 0.803)
- **Original**: Canto CXIV. Bharat's Departure. 785 Her glory gone, once bright and glad: Of joy and beauty reft, forlorn, In silent grief she seems to mourn.” Canto CXIV. Bharat's Departure. Deep, pleasant was the chariot's sound As royal Bharat, far renowned, Whirled by his mettled coursers fast Within Ayodhyá's city passed. There dark and drear was every home Where cats and owls had space to roam, As when the shades of midnight fall With blackest gloom, and cover all: As RohiGí, dear spouse of him Whom Ráhu hates,396 grows faint and dim, When, as she shines on high alone The demon's shade is o'er her thrown: As burnt by summer's heat a rill Scarce trickling from her parent hill, With dying fish in pools half dried, And fainting birds upon her side: As sacrificial flames arise When holy oil their food supplies, But when no more the fire is fed Sink lustreless and cold and dead: Like some brave host that filled the plain, With harness rent and captains slain, When warrior, elephant, and steed 396 The spouse of RohiGí is the Moon: Ráhu is the demon who causes eclipses.
- **Translation**: 

---

### Verse 4 (Ramayan 0.804)
- **Original**: 786 The Ramayana Mingled in wild confusion bleed: As when, all spent her store of worth, Rocks from her base the loosened earth: Like a sad fallen star no more Wearing the lovely light it wore: So mournful in her lost estate Was that sad town disconsolate. Then car-borne Bharat, good and brave, Thus spake to him the steeds who drave: “Why are Ayodhyá's streets so mute? Where is the voice of lyre and lute? Why sounds not, as of old, to-day The music of the minstrel's lay?[224] Where are the wreaths they used to twine? Where are the blossoms and the wine? Where is the cool refreshing scent Of sandal dust with aloe blent? The elephant's impatient roar, The din of cars, I hear no more: No more the horse's pleasant neigh Rings out to meet me on my way. Ayodhyá's youths, since Ráma's flight, Have lost their relish for delight: Her men roam forth no more, nor care Bright garlands round their necks to wear. All grieve for banished Ráma: feast, And revelry and song have ceased: Like a black night when floods pour down, So dark and gloomy is the town. When will he come to make them gay Like some auspicious holiday? When will my brother, like a cloud At summer's close, make glad the crowd?”
- **Translation**: 

---

### Verse 5 (Ramayan 0.805)
- **Original**: Canto CXV. Nandigrám. 787 Then through the streets the hero rode, And passed within his sire's abode, Like some deserted lion's den, Forsaken by the lord of men. Then to the inner bowers he came, Once happy home of many a dame, Now gloomy, sad, and drear, Dark as of old that sunless day When wept the Gods in wild dismay;397 There poured he many a tear. Canto CXV. Nandigrám.398 Then when the pious chief had seen Lodged in her home each widowed queen, Still with his burning grief oppressed His holy guides he thus addressed: “I go to Nandigrám: adieu, This day, my lords to all of you: I go, my load of grief to bear, Reft of the son of Raghu, there. The king my sire, alas, is dead, And Ráma to the forest fled; There will I wait till he, restored, Shall rule the realm, its rightful lord.” 397 “Once,” says the Commentator Tírtha,“in the battle between the Gods and demons the Gods were vanquished, and the sun was overthrown by Ráhu. At the request of the Gods Atri undertook the management of the sun for a week.” 398 Now Nundgaon, in Oudh.
- **Translation**: 

---

### Verse 6 (Ramayan 0.806)
- **Original**: 788 The Ramayana They heard the high-souled prince's speech, And thus with ready answer each Of those great lords their chief addressed, With saint Va[ishmha and the rest: “Good are the words which thou hast said, By brotherly affection led, Like thine own self, a faithful friend, True to thy brother to the end: A heart like thine must all approve, Which naught from virtue's path can move.” Soon as the words he loved to hear Fell upon Bharat's joyful ear, Thus to the charioteer he spoke: “My car with speed, Sumantra, yoke.” Then Bharat with delighted mien Obeisance paid to every queen, And withZatrughna by his side Mounting the car away he hied. With lords, and priests in long array The brothers hastened on their way. And the great pomp the Bráhmans led With Saint Va[ishmha at their head. Then every face was eastward bent As on to Nandigrám they went. Behind the army followed, all Unsummoned by their leader's call, And steeds and elephants and men Streamed forth with every citizen. As Bharat in his chariot rode His heart with love fraternal glowed, And with the sandals on his head To Nandigrám he quickly sped. Within the town he swiftly pressed,
- **Translation**: 

---

### Verse 7 (Ramayan 0.807)
- **Original**: Canto CXV. Nandigrám. 789 Alighted, and his guides addressed: “To me in trust my brother's hand Consigned the lordship of the land, When he these gold-wrought sandals gave As emblems to protect and save.” Then Bharat bowed, and from his head The sacred pledge deposited, And thus to all the people cried Who ringed him round on every side: “Haste, for these sandals quickly bring The canopy that shades the king. Pay ye to them all reverence meet As to my elder brother's feet, For they will right and law maintain Until King Ráma come again. My brother with a loving mind These sandals to my charge consigned: I till he come will guard with care The sacred trust for Raghu's heir. My watchful task will soon be done, The pledge restored to Raghu's son; Then shall I see, his wanderings o'er, These sandals on his feet once more. My brother I shall meet at last, The burthen from my shoulders cast, To Ráma's hand the realm restore And serve my elder as before. When Ráma takes again this pair Of sandals kept with pious care, And here his glorious reign begins, I shall be cleansed from all my sins, [225] When the glad people's voices ring With welcome to the new-made king, Joy will be mine four-fold as great
- **Translation**: 

---

### Verse 8 (Ramayan 0.808)
- **Original**: 790 The Ramayana As if supreme I ruled the state.” Thus humbly spoke in sad lament The chief in fame preëminent: Thus, by his reverent lords obeyed, At Nandigrám the kingdom swayed. With hermit's dress and matted hair He dwelt with all his army there. The sandals of his brother's feet Installed upon the royal seat, He, all his powers to them referred, Affairs of state administered. In every care, in every task, When golden store was brought, He first, as though their rede to ask, Those royal sandals sought. Canto CXVI. The Hermit's Speech. When Bharat took his homeward road Still Ráma in the wood abode: But soon he marked the fear and care That darkened all the hermits there. For all who dwelt before the hill Were sad with dread of coming ill: Each holy brow was lined by thought, And Ráma's side they often sought. With gathering frowns the prince they eyed, And then withdrew and talked aside.
- **Translation**: 

---

### Verse 9 (Ramayan 0.809)
- **Original**: Canto CXVI. The Hermit's Speech. 791 Then Raghu's son with anxious breast The leader of the saints addressed: “Can aught that I have done displease, O reverend Sage, the devotees? Why are their loving looks, O say, Thus sadly changed or turned away? Has LakshmaG through his want of heed Offended with unseemly deed? Or is the gentle Sítá, she Who loved to honour you and me— Is she the cause of this offence, Failing in lowly reverence?” One sage, o'er whom, exceeding old, Had many a year of penance rolled, Trembling in every aged limb Thus for the rest replied to him: “How could we, O beloved, blame Thy lofty-souled Videhan dame, Who in the good of all delights, And more than all of anchorites? But yet through thee a numbing dread Of fiends among our band has spread; Obstructed by the demons' art The trembling hermits talk apart. For RávaG's brother, overbold, Named Khara, of gigantic mould, Vexes with fury fierce and fell All those in Janasthán399 who dwell. Resistless in his cruel deeds, On flesh of men the monster feeds: Sinful and arrogant is he, And looks with special hate on thee. 399 A part of the great DaG ak forest.
- **Translation**: 

---

### Verse 10 (Ramayan 0.810)
- **Original**: 792 The Ramayana Since thou, beloved son, hast made Thy home within this holy shade, The fiends have vexed with wilder rage The dwellers of the hermitage. In many a wild and dreadful form Around the trembling saints they swarm, With hideous shape and foul disguise They terrify our holy eyes. They make our loathing souls endure Insult and scorn and sights impure, And flocking round the altars stay The holy rites we love to pay. In every spot throughout the grove With evil thoughts the monsters rove, Assailing with their secret might Each unsuspecting anchorite. Ladle and dish away they fling, Our fires with floods extinguishing, And when the sacred flame should burn They trample on each water-urn. Now when they see their sacred wood Plagued by this impious brotherhood, The troubled saints away would roam And seek in other shades a home: Hence will we fly, O Ráma, ere The cruel fiends our bodies tear. Not far away a forest lies Rich in the roots and fruit we prize, To this will I and all repair And join the holy hermits there; Be wise, and with us thither flee Before this Khara injure thee. Mighty art thou, O Ráma, yet Each day with peril is beset.
- **Translation**: 

---

### Verse 11 (Ramayan 0.811)
- **Original**: Canto CXVII. Anasúyá. 793 If with thy consort by thy side Thou in this wood wilt still abide.” He ceased: the words the hero spake The hermit's purpose failed to break: To Raghu's son farewell he said, And blessed the chief and comforted; Then with the rest the holy sage Departed from the hermitage. So from the wood the saints withdrew, And Ráma bidding all adieu In lowly reverence bent: Instructed by their friendly speech, Blest with the gracious love of each, To his pure home he went. Nor would the son of Raghu stray A moment from that grove away From which the saints had fled. And many a hermit thither came Attracted by his saintly fame And the pure life he led. [226] Canto CXVII. Anasúyá.
- **Translation**: 

---

### Verse 12 (Ramayan 0.812)
- **Original**: 794 The Ramayana But dwelling in that lonely spot Left by the hermits pleased him not. “I met the faithful Bharat here, The townsmen, and my mother dear: The painful memory lingers yet, And stings me with a vain regret. And here the host of Bharat camped, And many a courser here has stamped, And elephants with ponderous feet Have trampled through the calm retreat.” So forth to seek a home he hied, His spouse and LakshmaG by his side. He came to Atri's pure retreat, Paid reverence to his holy feet, And from the saint such welcome won As a fond father gives his son. The noble prince with joy unfeigned As a dear guest he entertained, And cheered the glorious LakshmaG too And Sítá with observance due. Then Anasúyá at the call Of him who sought the good of all, His blameless venerable spouse, Delighting in her holy vows, Came from her chamber to his side: To her the virtuous hermit cried: “Receive, I pray, with friendly grace This dame of Maithil monarchs' race:” To Ráma next made known his wife, The devotee of saintliest life: “Ten thousand years this votaress bent On sternest rites of penance spent; She when the clouds withheld their rain, And drought ten years consumed the plain,
- **Translation**: 

---

### Verse 13 (Ramayan 0.813)
- **Original**: Canto CXVII. Anasúyá. 795 Caused grateful roots and fruit to grow And ordered Gangá here to flow: So from their cares the saints she freed, Nor let these checks their rites impede, She wrought in Heaven's behalf, and made Ten nights of one, the Gods to aid:400 Let holy Anasúyá be An honoured mother, Prince, to thee. Let thy Videhan spouse draw near To her whom all that live revere, Stricken in years, whose loving mind Is slow to wrath and ever kind.” He ceased: and Ráma gave assent, And said, with eyes on Sítá bent: “O Princess, thou hast heard with me This counsel of the devotee: Now that her touch thy soul may bless, Approach the saintly votaress: Come to the venerable dame, Far known by Anasúyá's name: The mighty things that she has done High glory in the world have won.” Thus spoke the son of Raghu: she Approached the saintly devotee, Who with her white locks, old and frail, Shook like a plantain in the gale. To that true spouse she bowed her head, And “Lady, I am Sítá,” said: Raised suppliant hands and prayed her tell That all was prosperous and well. 400 When the saint MáG avya had doomed some saint's wife, who was Anasúyá's friend, to become a widow on the morrow.
- **Translation**: 

---

### Verse 14 (Ramayan 0.814)
- **Original**: 796 The Ramayana The aged matron, when she saw Fair Sítá true to duty's law, Addressed her thus:“High fate is thine Whose thoughts to virtue still incline. Thou, lady of the noble mind, Hast kin and state and wealth resigned To follow Ráma forced to tread Where solitary woods are spread. Those women gain high spheres above Who still unchanged their husbands love, Whether they dwell in town or wood, Whether their hearts be ill or good. Though wicked, poor, or led away In love's forbidden paths to stray, The noble matron still will deem Her lord a deity supreme. Regarding kin and friendship, I Can see no better, holier tie, And every penance-rite is dim Beside the joy of serving him. But dark is this to her whose mind Promptings of idle fancy blind, Who led by evil thoughts away Makes him who should command obey. Such women, O dear Maithil dame, Their virtue lose and honest fame, Enslaved by sin and folly, led In these unholy paths to tread. But they who good and true like thee The present and the future see, Like men by holy deeds will rise To mansions in the blissful skies. So keep thee pure from taint of sin, Still to thy lord be true,
- **Translation**: 

---

### Verse 15 (Ramayan 0.815)
- **Original**: Canto CXVIII. Anasúyá's Gifts. 797 And fame and merit shalt thou win, To thy devotion due.” Canto CXVIII. Anasúyá's Gifts. Thus by the holy dame addressed Who banished envy from her breast, Her lowly reverence Sítá paid, And softly thus her answer made: “No marvel, best of dames, thy speech The duties of a wife should teach; [227] Yet I, O lady, also know Due reverence to my lord to show. Were he the meanest of the base, Unhonoured with a single grace, My husband still I ne'er would leave, But firm through all to him would cleave: Still rather to a lord like mine Whose virtues high-exalted shine, Compassionate, of lofty soul, With every sense in due control, True in his love, of righteous mind, Like a dear sire and mother kind. E'en as he ever loves to treat Kau [alyá with observance meet, Has his behaviour ever been To every other honoured queen. Nay, more, a sonlike reverence shows The noble Ráma e'en to those On whom the king his father set His eyes one moment, to forget.
- **Translation**: 

---

### Verse 16 (Ramayan 0.816)
- **Original**: 798 The Ramayana Deep in my heart the words are stored, Said by the mother of my lord, When from my home I turned away In the lone fearful woods to stray. The counsel of my mother deep Impressed upon my soul I keep, When by the fire I took my stand, And Ráma clasped in his my hand. And in my bosom cherished yet, My friends' advice I ne'er forget: Woman her holiest offering pays When she her husband's will obeys. Good Sávitrí her lord obeyed, And a high saint in heaven was made, And for the self-same virtue thou Hast heaven in thy possession now. And she with whom no dame could vie, Now a bright Goddess in the sky, Sweet RohiGí the Moon's dear Queen, Without her lord is never seen: And many a faithful wife beside For her pure love is glorified.” Thus Sítá spake: soft rapture stole Through Anasúyá's saintly soul: Kisses on Sítá's head she pressed, And thus the Maithil dame addressed: “I by long rites and toils endured Rich store of merit have secured: From this my wealth will I bestow A blessing ere I let thee go. So right and wise and true each word That from thy lips mine ears have heard, I love thee: be my pleasing task
- **Translation**: 

---

### Verse 17 (Ramayan 0.817)
- **Original**: Canto CXVIII. Anasúyá's Gifts. 799 To grant the boon that thou shalt ask.” Then Sítá marvelled much, and while Played o'er her lips a gentle smile, “All has been done, O Saint,” she cried, “And naught remains to wish beside.” She spake; the lady's meek reply Swelled Anasúyá's rapture high. “Sítá,” she said,“my gift to-day Thy sweet contentment shall repay. Accept this precious robe to wear, Of heavenly fabric, rich and rare, These gems thy limbs to ornament, This precious balsam sweet of scent. O Maithil dame, this gift of mine Shall make thy limbs with beauty shine, And breathing o'er thy frame dispense Its pure and lasting influence. This balsam on thy fair limbs spread New radiance on thy lord shall shed, As Lakshmí's beauty lends a grace To VishGu's own celestial face.” Then Sítá took the gift the dame Bestowed on her in friendship's name, The balsam, gems, and robe divine, And garlands wreathed of bloomy twine; Then sat her down, with reverence meet, At saintly Anasúyá's feet. The matron rich in rites and vows Turned her to Ráma's Maithil spouse, And questioned thus in turn to hear A pleasant tale to charm her ear: “Sítá, 'tis said that Raghu's son
- **Translation**: 

---

### Verse 18 (Ramayan 0.818)
- **Original**: 800 The Ramayana Thy hand, mid gathered suitors, won. I fain would hear thee, lady, tell The story as it all befell: Do thou repeat each thing that passed, Reviewing all from first to last.” Thus spake the dame to Sítá: she Replying to the devotee, “Then, lady, thy attention lend,” Rehearsed the story to the end: “King Janak, just and brave and strong, Who loves the right and hates the wrong, Well skilled in what the law ordains For Warriors, o'er Videha reigns. Guiding one morn the plough, his hand Marked out, for rites the sacred land, When, as the ploughshare cleft the earth, Child of the king I leapt to birth. Then as the ground he smoothed and cleared, He saw me all with dust besmeared, And on the new-found babe, amazed The ruler of Videha gazed. In childless love the monarch pressed The welcome infant to his breast: “My daughter,” thus he cried,“is she:” And as his child he cared for me. Forth from the sky was heard o'erhead As 'twere a human voice that said: “Yea, even so: great King, this child Henceforth thine own be justly styled.” Videha's monarch, virtuous souled, Rejoiced o'er me with joy untold, Delighting in his new-won prize,
- **Translation**: 

---

### Verse 19 (Ramayan 0.819)
- **Original**: Canto CXVIII. Anasúyá's Gifts. 801 The darling of his heart and eyes. To his chief queen of saintly mind The precious treasure he consigned, And by her side she saw me grow, Nursed with the love which mothers know. [228] Then as he saw the seasons fly, And knew my marriage-time was nigh, My sire was vexed with care, as sad As one who mourns the wealth he had: “Scorn on the maiden's sire must wait From men of high and low estate: The virgin's father all despise, Though Indra's peer, who rules the skies.” More near he saw, and still more near, The scorn that filled his soul with fear, On trouble's billowy ocean tossed, Like one whose shattered bark is lost. My father knowing how I came, No daughter of a mortal dame, In all the regions failed to see A bridegroom meet to match with me. Each way with anxious thought he scanned, And thus at length the monarch planned: “The Bride's Election will I hold, With every rite prescribed of old.” It pleased King VaruG to bestow Quiver and shafts and heavenly bow Upon my father's sire who reigned, When Daksha his great rite ordained. Where was the man might bend or lift With utmost toil that wondrous gift? Not e'en in dreams could mortal king Strain the great bow or draw the string. Of this tremendous bow possessed,
- **Translation**: 

---

### Verse 20 (Ramayan 0.820)
- **Original**: 802 The Ramayana My truthful father thus addressed The lords of many a region, all Assembled at the monarch's call: “Whoe'er this bow can manage, he The husband of my child shall be.” The suitors viewed with hopeless eyes That wondrous bow of mountain size, Then to my sire they bade adieu, And all with humbled hearts withdrew. At length with Vi[vámitra came This son of Raghu, dear to fame, The royal sacrifice to view. Near to my father's home he drew, His brother LakshmaG by his side, Ráma, in deeds heroic tried. My sire with honour entertained The saint in lore of duty trained, Who thus in turn addressed the king: “Ráma and LakshmaG here who spring From royal Da[aratha, long To see thy bow so passing strong.” Before the prince's eyes was laid That marvel, as the Bráhman prayed. One moment on the bow he gazed, Quick to the notch the string he raised, Then, in the wandering people's view, The cord with mighty force he drew. Then with an awful crash as loud As thunderbolts that cleave the cloud, The bow beneath the matchless strain Of arms heroic snapped in twain. Thus, giving purest water, he, My sire, to Ráma offered me.
- **Translation**: 

---

