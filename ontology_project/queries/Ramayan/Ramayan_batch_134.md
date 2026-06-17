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

### Verse 1 (Ramayana 0.706)
- **Original**: 688 The Ramayana The speech of Bharat Guha heard, And swift to do his bidding stirred. Within the town the monarch sped And to his ready kinsmen said: “Awake, each kinsman, rise, each friend! May every joy your lives attend. Gather each boat upon the shore And ferry all the army o'er.” Thus Guha spoke: nor they delayed, But, rising quick, their lord obeyed, And soon, from every side secured, Five hundred boats were ready moored. Some reared aloft the mystic sign,363 And mighty bells were hung in line: Of firmest build, gay flags they bore, And sailors for the helm and oar. One such King Guha chose, whereon, Of fair white cloth, an awning shone, And sweet musicians charmed the ear,— And bade his servants urge it near. Then Bharat swiftly sprang on board, And thenZatrughna, famous lord, To whom, with many a royal dame, Kau [alyá and Sumitrá came. The household priest went first in place, The elders, and the Bráhman race, And after them the monarch's train Of women borne in many a wain. Then high to heaven the shouts of those Who fired the army's huts,364 arose, With theirs who bathed along the shore, 363 The svastika, a little cross with a transverse line at each extremity. 364 When an army marched it was customary to burn the huts in which it had spent the night.
- **Translation**: 

---

### Verse 2 (Ramayana 0.707)
- **Original**: Canto XC. The Hermitage. 689 Or to the boats the baggage bore. Full freighted with that mighty force The boats sped swiftly on their course, By royal Guha's servants manned, And gentle gales the banners fanned. Some boats a crowd of dames conveyed, In others noble coursers neighed; Some chariots and their cattle bore, Some precious wealth and golden store. Across the stream each boat was rowed, There duly disembarked its load, And then returning on its way, Sped here and there in merry play. Then swimming elephants appeared With flying pennons high upreared. And as the drivers urged them o'er, The look of winged mountains wore. Some men in barges reached the strand, Others on rafts came safe to land: Some buoyed with pitchers crossed the tide, And others on their arms relied. Thus with the help the monarch gave The army crossed pure Gangá's wave: Then in auspicious hour it stood Within Prayága's famous wood. The prince with cheering words addressed His weary men, and bade them rest Where'er they chose and he, With priest and deacon by his side, To Bharadvája's dwelling hied That best of saints to see. [197]
- **Translation**: 

---

### Verse 3 (Ramayana 0.708)
- **Original**: 690 The Ramayana Canto XC. The Hermitage. The prince of men a league away Saw where the hermit's dwelling lay, Then with his lords his path pursued, And left his warrior multitude. On foot, as duty taught his mind, He left his warlike gear behind; Two robes of linen cloth he wore, And bade Va[ishmha walk before. Then Bharat from his lords withdrew When Bharadvája came in view, And toward the holy hermit went Behind Va[ishmha, reverent. When Bharadvája, saint austere, Saw good Va[ishmha drawing near, He cried, upspringing from his seat, “The grace-gift bring, my friend to greet.” When Saint Va[ishmha near him drew, And Bharat paid the reverence due, The glorious hermit was aware That Da[aratha's son was there. The grace-gift, water for their feet He gave, and offered fruit to eat; Then, duty-skilled, with friendly speech In seemly order questioned each: “How fares it in Ayodhyá now With treasury and army? how With kith and kin and friends most dear, With councillor, and prince, and peer?” But, for he knew the king was dead, Of Da[aratha naught he said. Va [ishmha and the prince in turn Would of the hermit's welfare learn:
- **Translation**: 

---

### Verse 4 (Ramayana 0.709)
- **Original**: Canto XC. The Hermitage. 691 Of holy fires they fain would hear, Of pupils, trees, and birds, and deer. The glorious saint his answer made That all was well in holy shade: Then love of Ráma moved his breast, And thus he questioned of his guest: “Why art thou here, O Prince, whose band With kingly sway protects the land? Declare the cause, explain the whole, For yet some doubt disturbs my soul. He whom Kau [alyá bare, whose might The foemen slays, his line's delight, He who with wife and brother sent Afar now roam in banishment, Famed prince, to whom his father spake This order for a woman's sake: “Away! and in the forest spend Thy life till fourteen years shall end”— Has thou the wish to harm him, bent On sin against the innocent? Wouldst thou thine elder's realm enjoy Without a thorn that can annoy?” With sobbing voice and tearful eye Thus Bharat sadly made reply: “Ah lost am I, if thou, O Saint, Canst thus in thought my heart attaint: No warning charge from thee I need; Ne'er could such crime from me proceed. The words my guilty mother spake When fondly jealous for my sake— Think not that I, to triumph moved, Those words approve or e'er approved. O Hermit, I have sought this place
- **Translation**: 

---

### Verse 5 (Ramayana 0.710)
- **Original**: 692 The Ramayana To win the lordly hero's grace, To throw me at my brother's feet And lead him to his royal seat. To this, my journey's aim and end, Thou shouldst, O Saint, thy favour lend: Where is the lord of earth? do thou, Most holy, say, where roams he now?” Then, by the saint Va[ishmha pressed, And all the gathered priests beside, To Bharat's dutiful request The hermit graciously replied: “Worthy of thee, O Prince, this deed, True son of Raghu's ancient seed. I know thee reverent, well-controlled, The glory of the good of old. I grant thy prayer: in this pursuit I know thy heart is resolute. 'Tis for thy sake those words I said That wider still thy fame may spread. I know where Ráma, duty-tried, His brother, and his wife abide. Where Chitrakúma's heights arise Thy brother Ráma's dwelling lies. Go thither with the morning's light, And stay with all thy lords tonight: For I would show thee honour high, And do not thou my wish deny.” Canto XCI. Bharadvája's Feast.
- **Translation**: 

---

### Verse 6 (Ramayana 0.711)
- **Original**: Canto XCI. Bharadvája's Feast. 693 Soon as he saw the prince's mind To rest that day was well inclined, He sought Kaikeyí's son to please With hospitable courtesies. Then Bharat to the saint replied: “Our wants are more than satisfied. The gifts which honoured strangers greet, And water for our weary feet Hast thou bestowed with friendly care, And every choice of woodland fare.” Then Bharadvája spoke, a smile Playing upon his lips the while: “I know, dear Prince, thy friendly mind Will any fare sufficient find, But gladly would I entertain And banquet all thine armed train: Such is my earnest wish: do thou This longing of my heart allow, Why hast thou hither bent thy way, And made thy troops behind thee stay? [198] Why unattended? couldst thou not With friends and army seek this spot?” Bharat, with reverent hands raised high, To that great hermit made reply: “My troops, for awe of thee, O Sage, I brought not to thy hermitage: Troops of a king or monarch's son A hermit's home should ever shun. Behind me comes a mighty train Wide spreading o'er the ample plain, Where every chief and captain leads Men, elephants, and mettled steeds.
- **Translation**: 

---

### Verse 7 (Ramayana 0.712)
- **Original**: 694 The Ramayana I feared, O reverend Sage, lest these Might harm the holy ground and trees, Springs might be marred and cots o'erthrown, So with the priests I came alone.” “Bring all thy host,” the hermit cried, And Bharat, to his joy, complied. Then to the chapel went the sire, Where ever burnt the sacred fire, And first, in order due, with sips Of water purified his lips: To Vi[vakarmá, then he prayed, His hospitable feast to aid: “Let Vi[vakarmá hear my call, The God who forms and fashions all: A mighty banquet I provide, Be all my wants this day supplied. Lord Indra at their head, the three365 Who guard the worlds I call to me: A mighty host this day I feed, Be now supplied my every need. Let all the streams that eastward go, And those whose waters westering flow, Both on the earth and in the sky, Flow hither and my wants supply. Be some with ardent liquor filled, And some with wine from flowers distilled, While some their fresh cool streams retain Sweet as the juice of sugar-cane. I call the Gods, I call the band Of minstrels that around them stand: I call the Háhá and Huhú, I call the sweet Vi[vávasu, 365 Yáma, VaruGa, and Kuvera.
- **Translation**: 

---

### Verse 8 (Ramayana 0.713)
- **Original**: Canto XCI. Bharadvája's Feast. 695 I call the heavenly wives of these With all the bright Apsarases, Alambúshá of beauty rare, The charmer of the tangled hair, Ghritáchí and Vi[váchi fair, Hemá and Bhímá sweet to view, And lovely Nágadantá too, And all the sweetest nymphs who stand By Indra or by Brahmá's hand— I summon these with all their train And Tumburu to lead the strain. Here let Kuvera's garden rise Which far in Northern Kuru366 lies: For leaves let cloth and gems entwine, And let its fruit be nymphs divine. Let Soma367 give the noblest food To feed the mighty multitude, Of every kind, for tooth and lip, To chew, to lick, to suck, and sip. Let wreaths, where fairest flowers abound, Spring from the trees that bloom around. Each sort of wine to woo the taste, And meats of every kind be placed.” 366 “A happy land in the remote north where the inhabitants enjoy a natural pefection attended with complete happiness obtained without exertion. There is there no vicissitude, nor decrepitude, nor death, nor fear: no distinction of virtue and vice, none of the inequalities denoted by the words best, worst, and intermediate, nor any change resulting from the succession of the four Yugas.” See MUIR 'S{FNS Sanskrit Texts, Vol. I. p. 492. 367 The Moon.
- **Translation**: 

---

### Verse 9 (Ramayana 0.714)
- **Original**: 696 The Ramayana Thus spake the hermit self-restrained, With proper tone by rules ordained, On deepest meditation bent, In holy might preëminent. Then as with hands in reverence raised Absorbed in thought he eastward gazed, The deities he thus addressed Came each in semblance manifest. Delicious gales that cooled the frame From Malaya and Dardar came, That kissed those scented hills and threw Auspicious fragrance where they blew. Then falling fast in sweetest showers Came from the sky immortal flowers, And all the airy region round With heavenly drums was made to sound. Then breathed a soft celestial breeze, Then danced the bright Apsarases, The minstrels and the Gods advanced, And warbling lutes the soul entranced. The earth and sky that music filled, And through each ear it softly thrilled, As from the heavenly quills it fell With time and tune attempered well. Soon as the minstrels ceased to play And airs celestial died away, The troops of Bharat saw amazed What Vi[vakarmá's art had raised. On every side, five leagues around, All smooth and level lay the ground, With fresh green grass that charmed the sight Like sapphires blent with lazulite. There the Wood-apple hung its load, The Mango and the Citron glowed,
- **Translation**: 

---

### Verse 10 (Ramayana 0.715)
- **Original**: Canto XCI. Bharadvája's Feast. 697 The Bel and scented Jak were there, And Apelá with fruitage fair. There, brought from Northern Kuru, stood Rich in delights, the glorious wood, And many a stream was seen to glide [199] With flowering trees along its side. There mansions rose with four wide halls, And elephants and chargers' stalls, And many a house of royal state, Triumphal arc and bannered gate. With noble doorways, sought the sky, Like a pale cloud, a palace high, Which far and wide rare fragrance shed, With wreaths of white engarlanded. Square was its shape, its halls were wide, With many a seat and couch supplied, Drink of all kinds, and every meat Such as celestial Gods might eat. Then at the bidding of the seer Kaikeyí's strong-armed son drew near, And passed within that fair abode Which with the noblest jewels glowed. Then, as Va[ishmha led the way, The councillors, in due array, Followed delighted and amazed And on the glorious structure gazed. Then Bharat, Raghu's son, drew near The kingly throne, with prince and peer, Whereby the chouri in the shade Of the white canopy was laid. Before the throne he humbly bent And honoured Ráma, reverent, Then in his hand the chouri bore, And sat where sits a councillor.
- **Translation**: 

---

### Verse 11 (Ramayana 0.716)
- **Original**: 698 The Ramayana His ministers and household priest Sat by degrees from chief to least, Then sat the captain of the host And all the men he honoured most. Then when the saint his order gave, Each river with enchanted wave Rolled milk and curds divinely sweet Before the princely Bharat's feet; And dwellings fair on either side, With gay white plaster beautified, Their heavenly roofs were seen to lift, The Bráhman Bharadvája's gift. Then straight by Lord Kuvera sent, Gay with celestial ornament Of bright attire and jewels' shine, Came twenty thousand nymphs divine: The man on whom those beauties glanced That moment felt his soul entranced. With them from Nandan's blissful shades Came twenty thousand heavenly maids. Tumburu, Nárad, Gopa came, And Sutanu, like radiant flame, The kings of the Gandharva throng, And ravished Bharat with their song. Then spoke the saint, and swift obeyed Alambúshá, the fairest maid, And Mi [rake[í bright to view, Rama Gá, PuG ríká too, And danced to him with graceful ease The dances of Apsarases. All chaplets that by Gods are worn, Or Chaitraratha's graves adorn, Bloomed by the saint's command arrayed On branches in Prayága's shade.
- **Translation**: 

---

### Verse 12 (Ramayana 0.717)
- **Original**: Canto XCI. Bharadvája's Feast. 699 When at the saint's command the breeze Made music with the Vilva trees, To wave in rhythmic beat began The boughs of each Myrobolan, And holy fig-trees wore the look Of dancers, as their leaflets shook. The fair Tamála, palm, and pine, With trees that tower and plants that twine, The sweetly varying forms displayed Of stately dame or bending maid. Here men the foaming winecup quaffed, Here drank of milk full many a draught, And tasted meats of every kind, Well dressed, whatever pleased their mind. Then beauteous women, seven or eight, Stood ready by each man to wait: Beside the stream his limbs they stripped And in the cooling water dipped. And then the fair ones, sparkling eyed, With soft hands rubbed his limbs and dried, And sitting on the lovely bank Held up the winecup as he drank. Nor did the grooms forget to feed Camel and mule and ox and steed, For there were stores of roasted grain, Of honey and of sugar-cane. So fast the wild excitement spread Among the warriors Bharat led, That all the mighty army through The groom no more his charger knew, And he who drove might seek in vain To tell his elephant again. With every joy and rapture fired, Entranced with all the heart desired,
- **Translation**: 

---

### Verse 13 (Ramayana 0.718)
- **Original**: 700 The Ramayana The myriads of the host that night Revelled delirious with delight. Urged by the damsels at their side In wild delight the warriors cried: “Ne'er will we seek Ayodhyá, no, Nor yet to DaG ak forest go: Here will we stay: may happy fate On Bharat and on Ráma wait.” Thus cried the army gay and free Exulting in their lawless glee, Both infantry and those who rode On elephants, or steeds bestrode, Ten thousand voices shouting,“This Is heaven indeed for perfect bliss.” With garlands decked they idly strayed, And danced and laughed and sang and played. At length as every soldier eyed, With food like Amrit satisfied, Each dainty cate and tempting meat, No longer had he care to eat. Thus soldier, servant, dame, and slave Received whate'er the wish might crave. As each in new-wrought clothes arrayed Enjoyed the feast before him laid.[200] Each man was seen in white attire Unstained by spot or speck of mire: None was athirst or hungry there, And none had dust upon his hair. On every side in woody dells Was milky food in bubbling wells, And there were all-supplying cows And honey dropping from the boughs. Nor wanted lakes of flower-made drink With piles of meat upon the brink,
- **Translation**: 

---

### Verse 14 (Ramayana 0.719)
- **Original**: Canto XCI. Bharadvája's Feast. 701 Boiled, stewed, and roasted, varied cheer, Peachick and jungle-fowl and deer, There was the flesh of kid and boar, And dainty sauce in endless store, With juice of flowers concocted well, And soup that charmed the taste and smell, And pounded fruits of bitter taste, And many a bath was ready placed Down by each river's shelving side There stood great basins well supplied, And laid therein, of dazzling sheen, White brushes for the teeth were seen, And many a covered box wherein Was sandal powdered for the skin. And mirrors bright with constant care, And piles of new attire were there, And store of sandals and of shoes, Thousands of pairs, for all to choose: Eye-unguents, combs for hair and beard, Umbrellas fair and bows appeared. Lakes gleamed, that lent digestive aid,368 And some for pleasant bathing made, With waters fair, and smooth incline For camels, horses, mules, and kine. There saw they barley heaped on high The countless cattle to supply: The golden grain shone fair and bright As sapphires or the lazulite. To all the gathered host it seemed As if that magic scene they dreamed, And wonder, as they gazed, increased At Bharadvája's glorious feast. 368 The poet does not tell us what these lakes contained.
- **Translation**: 

---

### Verse 15 (Ramayana 0.720)
- **Original**: 702 The Ramayana Thus in the hermit's grove they spent That night in joy and merriment, Blest as the Gods who take their ease Under the shade of Nandan's trees. Each minstrel bade the saint adieu, And to his blissful mansion flew, And every stream and heavenly dame Returned as swiftly as she came. Canto XCII. Bharat's Farewell. So Bharat with his army spent The watches of the night content, And gladly, with the morning's light Drew near his host the anchorite. When Bharadvája saw him stand With hand in reverence joined to hand, When fires of worship had been fed, He looked upon the prince and said: “O blameless son, I pray thee tell, Did the past night content thee well? Say if the feast my care supplied Thy host of followers gratified.”
- **Translation**: 

---

### Verse 16 (Ramayana 0.721)
- **Original**: Canto XCII. Bharat's Farewell. 703 His hands he joined, his head he bent And spoke in answer reverent To the most high and radiant sage Who issued from his hermitage: “Well have I passed the night: thy feast Gave joy to every man and beast; And I, great lord, and every peer Were satisfied with sumptuous cheer, Thy banquet has delighted all From highest chief to meanest thrall, And rich attire and drink and meat Banished the thought of toil and heat. And now, O Hermit good and great, A boon of thee I supplicate. To Ráma's side my steps I bend: Do thou with friendly eye commend. O tell me how to guide my feet To virtuous Ráma's lone retreat: Great Hermit, I entreat thee, say How far from here and which the way.” Thus by fraternal love inspired The chieftain of the saint inquired: Then thus replied the glorious seer Of matchless might, of vows austere: “Ere the fourth league from here be passed, Amid a forest wild and vast, Stands Chitrakúma's mountain tall, Lovely with wood and waterfall. North of the mountain thou wilt see The beauteous stream Mandákiní, Where swarm the waterfowl below, And gay trees on the margin grow. Then will a leafy cot between
- **Translation**: 

---

### Verse 17 (Ramayana 0.722)
- **Original**: 704 The Ramayana The river and the hill be seen: 'Tis Ráma's, and the princely pair Of brothers live for certain there. Hence to the south thine army lead, And then more southward still proceed, So shalt thou find his lone retreat, And there the son of Raghu meet.” Soon as the ordered march they knew, The widows of the monarch flew, Leaving their cars, most meet to ride, And flocked to Bharadvája's side. There with the good Sumitrá Queen Kau [alyá, sad and worn, was seen, Caressing, still with sorrow faint, The feet of that illustrious saint, Kaikeyí too, her longings crossed, Reproached of all, her object lost, Before the famous hermit came,[201] And clasped his feet, o'erwhelmed with shame. With circling steps she humbly went Around the saint preëminent, And stood not far from Bharat's side With heart oppressed, and heavy-eyed. Then the great seer, who never broke One holy vow, to Bharat spoke: “Speak, Raghu's son: I fain would learn The story of each queen in turn.”
- **Translation**: 

---

### Verse 18 (Ramayana 0.723)
- **Original**: Canto XCII. Bharat's Farewell. 705 Obedient to the high request By Bharadvája thus addressed, His reverent hands together laid, He, skilled in speech, his answer made: “She whom, O Saint, thou seest here A Goddess in her form appear, Was the chief consort of the king, Now worn with fast and sorrowing. As Aditi in days of yore The all-preserving VishGu bore, Kau [alyá bore with happy fate Lord Ráma of the lion's gait. She who, transfixed with torturing pangs, On her left arm so fondly hangs, As when her withering leaves decay Droops by the wood the Cassia spray, Sumitrá, pained with woe, is she, The consort second of the three: Two princely sons the lady bare, Fair as the Gods in heaven are fair. And she, the wicked dame through whom My brothers' lives are wrapped in gloom, And mourning for his offspring dear, The king has sought his heavenly sphere,— Proud, foolish-hearted, swift to ire, Self-fancied darling of my sire, Kaikeyí, most ambitious queen, Unlovely with her lovely mien, My mother she, whose impious will Is ever bent on deeds of ill, In whom the root and spring I see Of all this woe which crushes me.”
- **Translation**: 

---

### Verse 19 (Ramayana 0.724)
- **Original**: 706 The Ramayana Quick breathing like a furious snake, With tears and sobs the hero spake, With reddened eyes aglow with rage. And Bharadvája, mighty sage, Supreme in wisdom, calm and grave, In words like these good counsel gave: “O Bharat, hear the words I say; On her the fault thou must not lay: For many a blessing yet will spring From banished Ráma's wandering.” And Bharat, with that promise cheered, Went circling round that saint revered, He humbly bade farewell, and then Gave orders to collect his men. Prompt at the summons thousands flew To cars which noble coursers drew, Bright-gleaming, glorious to behold, Adorned with wealth of burnished gold. Then female elephants and male, Gold-girthed, with flags that wooed the gale, Marched with their bright bells' tinkling chime Like clouds when ends the summer time: Some cars were huge and some were light, For heavy draught or rapid flight, Of costly price, of every kind, With clouds of infantry behind. The dames, Kau[alyá at their head, Were in the noblest chariots led, And every gentle bosom beat With hope the banished prince to meet. The royal Bharat, glory-crowned, With all his retinue around, Borne in a beauteous litter rode, Like the young moon and sun that glowed.
- **Translation**: 

---

### Verse 20 (Ramayana 0.725)
- **Original**: Canto XCIII. Chitrakúta In Sight. 707 The army as it streamed along, Cars, elephants, in endless throng, Showed, marching on its southward way, Like autumn clouds in long array. Canto XCIII. Chitrakúta In Sight. As through the woods its way pursued That mighty bannered multitude, Wild elephants in terror fled With all the startled herds they led, And bears and deer were seen on hill, In forest glade, by every rill. Wide as the sea from coast to coast, The high-souled Bharat's mighty host Covered the earth as cloudy trains Obscure the sky when fall the rains. The stately elephants he led, And countless steeds the land o'erspread, So closely crowded that between Their serried ranks no ground was seen. Then when the host had travelled far, And steeds were worn who drew the car, The glorious Bharat thus addressed Va [ishmha, of his lords the best: “The spot, methinks, we now behold Of which the holy hermit told, For, as his words described, I trace Each several feature of the place: Before us Chitrakúma shows, Mandákiní beside us flows:
- **Translation**: 

---

