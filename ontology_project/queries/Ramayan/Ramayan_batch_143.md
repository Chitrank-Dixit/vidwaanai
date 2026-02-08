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

### Verse 1 (Ramayana 0.886)
- **Original**: 868 The Ramayana All swans and geese on mere and brook Their birth from Dhritaráshtrí took, And all the river-haunting brood Of ducks, a countless multitude. From Zukí Nalá sprang, who bare Dame Vinatá surpassing fair. From fiery Krodhava[á, ten Bright daughters sprang, O King of men: Mrigí and Mrigamandá named, Hari and Bhadramadá famed, Zárdúlí,Zvetá fair to see, Mátangí bright, and Surabhí, Surasá marked with each fair sign, And Kadrumá, all maids divine. Mrigí, O Prince without a peer, Was mother of the herds of deer, The bear, the yak, the mountain roe Their birth to Mrigamandá owe; And Bhadramadá joyed to be Mother of fair Irávatí, Who bare Airávat,444 huge of mould, Mid warders of the earth enrolled, From Harí lordly lions trace, With monkeys of the wild, their race. From the great dameZárdúlí styled Sprung pards, Lángúrs,445 and tigers wild. Mátangí, Prince, gave birth to all Mátangas, elephants strong and tall, And Zvetá bore the beasts who stand One at each wind, earth's warder band.446 444 The elephant of Indra. 445 Golángúlas, described as a kind of monkey, of a black colour, and having a tail like a cow. 446 Eight elephants attached to the four quarters and intermediate points of the
- **Translation**: 

---

### Verse 2 (Ramayana 0.887)
- **Original**: Canto XIV. Jatáyus. 869 Next Surabhí the Goddess bore Two heavenly maids, O Prince, of yore, Gandharví— dear to fame is she— And her sweet sister RohiGí. With kine this daughter filled each mead, And bright Gandharví bore the steed.447 Surasá bore the serpents:448 all The snakes Kadrú their mother call. Then Manu, high-souled Ka[yap's449 wife, To all the race of men gave life, The Bráhmans first, the Kshatriya caste, Then Vai[yas, and theZúdras last. Sprang from her mouth the Bráhman race; Her chest the Kshatriyas' natal place: The Vai[yas from her thighs, 'tis said, The Zúdras from her feet were bred. From Analá all trees that hang Their fair fruit-laden branches sprang. The child of beauteousZukí bore Vinatá, as I taught before: And Surasá and Kadrú were Born of one dame, a noble pair. Kadrú gave birth to countless snakes That roam the earth in woods and brakes. AruG and Garu swift of flight compass, to support and guard the earth. 447 Some scholars identify the centaurs with the Gandharvas. 448 The hooded serpents, says the commentator Tírtha, were the offspring of Surasá: all others of Kadrú. 449 The text reads Ka[yapa,“a descendant of Ka[yapa,” who according to Rám. II. l0, 6, ought to be Vivasvat. But as it is stated in the preceding part of this passage III. 14, 11 f. that Manu was one of Ka[yapa's eight wives, we must here read Ka[yap. The Ganda recension reads (III, 20, 30)Manur manushyáms cha tatha janayámása Rághana, instead of the corresponding line in the Bombay edition.Muir's Sanskrit Text, Vol I, p. 117.
- **Translation**: 

---

### Verse 3 (Ramayana 0.888)
- **Original**: 870 The Ramayana By Vinatá were given to light, And sons of AruG red as morn Sampati first, then I was born, Me then, O tamer of the foe, Jamáyus, son ofZyení, know. Thy ready helper will I be, And guard thy house, if thou agree: When thou and LakshmaG urge the chase By Sítá's side shall be my place.” With courteous thanks for promised aid, The prince, to rapture stirred, Bent low, and due obeisance paid, Embraced the royal bird.[247] He often in the days gone by Had heard his father tell How, linked with him in friendship's tie, He loved Jamáyus well. He hastened to his trusted friend His darling to confide, And through the wood his steps to bend By strong Jamáyus' side. On to the grove, with LakshmaG near, The prince his way pursued To free those pleasant shades from fear And slay the giant brood. Canto XV. Panchavatí.
- **Translation**: 

---

### Verse 4 (Ramayana 0.889)
- **Original**: Canto XV. Panchavatí. 871 Arrived at Panchavamí's shade Where silvan life and serpents strayed, Ráma in words like these addressed Lakshma G of vigour unrepressed: “Brother, our home is here: behold The grove of which the hermit told: The bowers of Panchavamí see Made fair by every blooming tree. Now, brother, bend thine eyes around; With skilful glance survey the ground: Here be some spot selected, best Approved for gentle hermits' rest, Where thou, the Maithil dame, and I May dwell while seasons sweetly fly. Some pleasant spot be chosen where Pure waters gleam and trees are fair, Some nook where flowers and wood are found And sacred grass and springs abound.” Then LakshmaG, Sítá standing by, Raised reverent hands, and made reply: “A hundred years shall flee, and still Will I obey my brother's will: Select thyself a pleasant spot; Be mine the care to rear the cot.” The glorious chieftain, pleased to hear That loving speech that soothed his ear, Selected with observant care A spot with every charm most fair. He stood within that calm retreat, A shade for hermits' home most meet, And thus Sumitrá's son addressed, While his dear hand in his he pressed:
- **Translation**: 

---

### Verse 5 (Ramayana 0.890)
- **Original**: 872 The Ramayana “See, see this smooth and lovely glade Which flowery trees encircling shade: Do thou, beloved LakshmaG rear A pleasant cot to lodge us here. I see beyond that feathery brake The gleaming of a lilied lake, Where flowers in sunlike glory throw Fresh odours from the wave below. Agastya's words now find we true, He told the charms which here we view: Here are the trees that blossom o'er Godávarí's most lovely shore. Whose pleasant flood from side to side With swans and geese is beautified, And fair banks crowded with the deer That steal from every covert near. The peacock's cry is loud and shrill From many a tall and lovely hill, Green-belted by the trees that wave Full blossoms o'er the rock and cave. Like elephants whose huge fronts glow With painted streaks, the mountains show Long lines of gold and silver sheen With copper's darker hues between. With every tree each hill is graced, Where creepers blossom interlaced. Look where the Sál's long branches sway, And palms their fanlike leaves display; The date-tree and the Jak are near, And their long stems Tamálas rear. See the tall Mango lift his head, A [okas all their glory spread, The Ketak her sweet buds unfold,
- **Translation**: 

---

### Verse 6 (Ramayana 0.891)
- **Original**: Canto XV. Panchavatí. 873 And Champacs hang their cups of gold.450 The spot is pure and pleasant: here Are multitudes of birds and deer. O Lakshma G, with our father's friend What happy hours we here shall spend!” He spoke: the conquering LakshmaG heard, Obedient to his brother's word. Raised by his toil a cottage stood To shelter Ráma in the wood, Of ample size, with leaves o'erlaid, Of hardened earth the walls were made. The strong bamboos his hands had felled For pillars fair the roof upheld, And rafter, beam, and lath supplied Well interwrought from side to side. Then Zamí451 boughs he deftly spread Enlaced with knotted cord o'erhead, Well thatched above from ridge to eaves With holy grass, and reed, and leaves. The mighty chief with careful toil Had cleared the ground and smoothed the soil [248] Where now, his loving labour done, Rose a fair home for Raghu's son. Then when his work was duly wrought, Godávarís sweet stream he sought, Bathed, plucked the lilies, and a store 450 The original verses merely name the trees. I have been obliged to amplify slightly and to omit some quas versu dicere non est;e.g.thetini[a (Dalber- gia ougeiniensis),punnága (Rottleria tinctoria),tilaka(not named),syandana (Dalbergia ougeiniensis again),vandana (unknown),nípa(Nauclea Kadamba), lakucha(Artœ arpus lacucha),dhava (Grislea tomentosa), A[vakarna (another name for the Sál),Zamí (Acacia Suma),khadira(Mimosa catechu),kin[uka (Butea frondosa),pátala(Bignonia suaveolens). 451 Acacia Suma.
- **Translation**: 

---

### Verse 7 (Ramayana 0.892)
- **Original**: 874 The Ramayana Of fruit and berries homeward bore. Then sacrifice he duly paid, And wooed the Gods their hopes to aid, And then to Ráma proudly showed The cot prepared for his abode. Then Raghu's son with Sítá gazed Upon the home his hands had raised, And transport thrilled his bosom through His leafy hermitage to view. The glorious son of Raghu round His brother's neck his arms enwound, And thus began his sweet address Of deep-felt joy and gentleness: “Well pleased am I, dear lord, to see This noble work performed by thee. For this,— sole grace I can bestow,— About thy neck mine arms I throw. So wise art thou, thy breast is filled With grateful thoughts, in duty skilled, Our mighty father, free from stain, In thee, his offspring, lives again.” Thus spoke the prince, who lent a grace To fortune, pride of Raghu's race; Then in that spot whose pleasant shade Gave store of fruit, content he stayed. With LakshmaG and his Maithil spouse He spent his day's neath sheltering boughs, As happy as a God on high Lives in his mansion in the sky.
- **Translation**: 

---

### Verse 8 (Ramayana 0.893)
- **Original**: Canto XVI. Winter. 875 Canto XVI. Winter. While there the high-souled hero spent His tranquil hours in sweet content, The glowing autumn passed, and then Came winter so beloved of men. One morn, to bathe, at break of day To the fair stream he took his way. Behind him, with the Maithil dame Bearing a pitcher LakshmaG came, And as he went the mighty man Thus to his brother chief began: “The time is come, to thee more dear Than all the months that mark the year: The gracious seasons' joy and pride, By which the rest are glorified. A robe of hoary rime is spread O'er earth, with corn engarlanded. The streams we loved no longer please, But near the fire we take our ease. Now pious men to God and shade Offer young corn's fresh sprouted blade, And purge away their sins with rice Bestowed in humble sacrifice. Rich stores of milk delight the swain, And hearts are cheered that longed for gain, Proud kings whose breasts for conquests glow Lead bannered troops to smite the foe. Dark is the north: the Lord of Day To Yáma's south452 has turned away: 452 The south is supposed to be the residence of the departed.
- **Translation**: 

---

### Verse 9 (Ramayana 0.894)
- **Original**: 876 The Ramayana And she— sad widow— shines no more, Reft of the bridal mark453 she wore. Himálaya's hill, ordained of old The treasure-house of frost and cold, Scarce conscious of the feebler glow, Is truly now the Lord of Snow. Warmed by the noontide's genial rays Delightful are the glorious days: But how we shudder at the chill Of evening shadows and the rill! How weak the sun, how cold the breeze! How white the rime on grass and trees! The leaves are sere, the woods have lost Their blossoms killed by nipping frost. Neath open skies we sleep no more: December's nights with rime are hoar: Their triple watch454 in length extends With hours the shortened daylight lends. No more the moon's sun-borrowed rays Are bright, involved in misty haze, As when upon the mirror's sheen The breath's obscuring cloud is seen. E'en at the full the faint beams fail To struggle through the darksome veil: Changed like her hue, they want the grace That parts not yet from Sítá's face. Cold is the western wind, but how Its piercing chill is heightened now, Blowing at early morning twice As furious with its breath of ice! See how the dewy tears they weep The barley, wheat, and woodland steep, 453 The sun. 454 The night is divided into three watches of four hours each.
- **Translation**: 

---

### Verse 10 (Ramayana 0.895)
- **Original**: Canto XVI. Winter. 877 Where, as the sun goes up the sky, The curlew and the sáras cry. See where the rice plants scarce uphold Their full ears tinged with paly gold, Bending their ripe heads slowly down Fair as the date tree's flowery crown. Though now the sun has mounted high Seeking the forehead of the sky, Such mist obscures his struggling beams, No bigger than the moon he seems. Though weak at first, his rays at length Grow pleasant in their noonday strength, And where a while they chance to fall Fling a faint splendour over all. [249] See, o'er the woods where grass is wet With hoary drops that cling there yet, With soft light clothing earth and bough There steals a tender glory now. Yon elephant who longs to drink, Still standing on the river's brink, Plucks back his trunk in shivering haste From the cold wave he fain would taste. The very fowl that haunt the mere Stand doubtful on the bank, and fear To dip them in the wintry wave As cowards dread to meet the brave. The frost of night, the rime of dawn Bind flowerless trees and glades of lawn: Benumbed in apathetic chill Of icy chains they slumber still. You hear the hidden sáras cry From floods that wrapped in vapour lie, And frosty-shining sands reveal Where the unnoticed rivers steal.
- **Translation**: 

---

### Verse 11 (Ramayana 0.896)
- **Original**: 878 The Ramayana The hoary rime of dewy night, And suns that glow with tempered light Lend fresh cool flavours to the rill That sparkles from the topmost hill. The cold has killed the lily's pride: Leaf, filament, and flower have died: With chilling breath rude winds have blown, The withered stalk is left alone. At this gay time, O noblest chief, The faithful Bharat, worn by grief, Lives in the royal town where he Spends weary hours for love of thee. From titles, honour, kingly sway, From every joy he turns away: Couched on cold earth, his days are passed With scanty fare and hermit's fast. This moment from his humble bed He lifts, perhaps, his weary head, And girt by many a follower goes To bathe where silver Sarjú flows. How, when the frosty morn is dim, Shall Sarjú be a bath for him Nursed with all love and tender care, So delicate and young and fair. How bright his hue! his brilliant eye With the broad lotus leaf may vie. By fortune stamped for happy fate, His graceful form is tall and straight. In duty skilled, his words are truth: He proudly rules each lust of youth. Though his strong arm smites down the foe, In gentle speech his accents flow. Yet every joy has he resigned And cleaves to thee with heart and mind.
- **Translation**: 

---

### Verse 12 (Ramayana 0.897)
- **Original**: Canto XVI. Winter. 879 Thus by the deeds that he has done A name in heaven has Bharat won, For in his life he follows yet Thy steps, O banished anchoret. Thus faithful Bharat, nobly wise, The proverb of the world belies: “No men, by mothers' guidance led, The footsteps of their fathers tread.” How could Kaikeyí, blest to be Spouse of the king our sire, and see A son like virtuous Bharat, blot Her glory with so foul a plot!” Thus in fraternal love he spoke, And from his lips reproaches broke: But Ráma grieved to hear him chide The absent mother, and replied: “Cease, O beloved, cease to blame Our royal father's second dame. Still speak of Bharat first in place Of old Ikshváku's princely race. My heart, so firmly bent but now To dwell in woods and keep my vow, Half melting as I hear thee speak Of Bharat's love, grows soft and weak, With tender joy I bring to mind His speeches ever sweet and kind. That dear as Amrit took the sense With most enchanting influence. Ah, when shall I, no more to part, Meet Bharat of the mighty heart? When, O my brother, when shall we The good and braveZatrughna see?”
- **Translation**: 

---

### Verse 13 (Ramayana 0.898)
- **Original**: 880 The Ramayana Thus as he poured his fond lament The son of Raghu onward went: They reached the river, and the three Bathed them in fair Godávarí. Libations of the stream they paid To every deity and shade, With hymns of praise, the Sun on high And sinless Gods to glorify. Fresh from the purifying tide Resplendent Ráma came, With LakshmaG ever by his side, And the sweet Maithil dame. So Rudra shines by worlds adored, In glory undefiled, When Nandi455 stands beside his lord, And King Himálaya's child.456 Canto XVII. Súrpanakhá. The bathing and the prayer were o'er; He turned him from the grassy shore, And with his brother and his spouse Sought his fair home beneath the boughs. Sítá and LakshmaG by his side, On to his cot the hero hied, And after rites at morning due Within the leafy shade withdrew.[250] 455 The chief chamberlain and attendant ofZiva or Rudra. 456 Umá or Párvati, the consort ofZiva.
- **Translation**: 

---

### Verse 14 (Ramayana 0.899)
- **Original**: Canto XVII. Súrpanakhá. 881 Then, honoured by the devotees, As royal Ráma sat at ease, With Sítá near him, o'er his head A canopy of green boughs spread, He shone as shines the Lord of Night By Chitrá's457 side, his dear delight. With LakshmaG there he sat and told Sweet stories of the days of old, And as the pleasant time he spent With heart upon each tale intent, A giantess, by fancy led, Came wandering to his leafy shed. FierceZúrpaGakhá,— her of yore The Ten-necked tyrant's mother bore,— Saw Ráma with his noble mien Bright as the Gods in heaven are seen; Him from whose brow a glory gleamed, Like lotus leaves his full eyes beamed: Long-armed, of elephantine gait, With hair close coiled in hermit plait: In youthful vigour, nobly framed, By glorious marks a king proclaimed: Like some bright lotus lustrous-hued, With young Kandarpa's458 grace endued: As there like Indra's self he shone, She loved the youth she gazed upon. She grim of eye and foul of face Loved his sweet glance and forehead's grace: She of unlovely figure, him Of stately form and shapely limb: She whose dim locks disordered hung, Him whose bright hair on high brows clung: 457 A star, one of the favourites of the Moon. 458 The God of love.
- **Translation**: 

---

### Verse 15 (Ramayana 0.900)
- **Original**: 882 The Ramayana She whose fierce accents counselled fear, Him whose soft tones were sweet to hear: She whose dire form with age was dried, Him radiant in his youthful pride: She whose false lips maintained the wrong, Him in the words of virtue strong: She cruel-hearted, stained with sin, Him just in deed and pure within. She, hideous fiend, a thing to hate, Him formed each eye to captivate: Fierce passion in her bosom woke, And thus to Raghu's son she spoke: “With matted hair above thy brows, With bow and shaft and this thy spouse, How hast thou sought in hermit dress The giant-haunted wilderness? What dost thou here? The cause explain: Why art thou come, and what to gain?” As ZúrpaGakhá questioned so, Ráma, the terror of the foe, In answer to the monster's call, With fearless candour told her all. “King Da[aratha reigned of old, Like Gods celestial brave and bold. I am his eldest son and heir, And Ráma is the name I bear. This brother, LakshmaG, younger born, Most faithful love to me has sworn. My wife, this princess, dear to fame, Is Sitá the Videhan dame. Obedient to my sire's behest And by the queen my mother pressed, To keep the law and merit win,
- **Translation**: 

---

### Verse 16 (Ramayana 0.901)
- **Original**: Canto XVII. Súrpanakhá. 883 I sought this wood to harbour in. But speak, for I of thee in turn Thy name, and race, and sire would learn. Thou art of giant race, I ween. Changing at will thy form and mien. Speak truly, and the cause declare That bids thee to these shades repair.” Thus Ráma spoke: the demon heard, And thus replied by passion spurred: “Of giant race, what form soe'er My fancy wills, 'tis mine to wear. Named ZúrpaGakhá here I stray, And where I walk spread wild dismay. King RávaG is my brother: fame Has taught perchance his dreaded name, Strong KumbhakarGa slumbering deep In chains of never-ending sleep: VibhíshaG of the duteous mind, In needs unlike his giant kind: DúshaG and Khara, brave and bold Whose fame by every tongue is told: Their might by mine is far surpassed; But when, O best of men, I cast These fond eyes on thy form, I see My chosen love and lord in thee. Endowed with wondrous might am I: Where'er my fancy leads I fly. The poor misshapen Sítá leave, And me, thy worthier bride receive. Look on my beauty, and prefer A spouse more meet than one like her: I'll eat that ill-formed woman there: Thy brother too her fate shall share.
- **Translation**: 

---

### Verse 17 (Ramayana 0.902)
- **Original**: 884 The Ramayana But come, beloved, thou shalt roam With me through all our woodland home; Each varied grove with me shalt seek, And gaze upon each mountain peak.” As thus she spoke, the monster gazed With sparkling eyes where passion blazed: Then he, in lore of language learned, This answer eloquent returned: Canto XVIII. The Mutilation. On her ensnared in Káma's net His eyes the royal Ráma set,[251] And thus, her passion to beguile, Addressed her with a gentle smile: “I have a wife: behold her here, My Sítá ever true and dear: And one like thee will never brook Upon a rival spouse to look. But there my brother LakshmaG stands: Unchained is he by nuptial bands: A youth heroic, loved of all, Gracious and gallant, fair and tall. With winning looks, most nobly bred, Unmatched till now, he longs to wed. Meet to enjoy thy youthful charms, O take him to thy loving arms. Enamoured on his bosom lie, Fair damsel of the radiant eye, As the warm sunlight loves to rest Upon her darling Meru's breast.”
- **Translation**: 

---

### Verse 18 (Ramayana 0.903)
- **Original**: Canto XVIII. The Mutilation. 885 The hero spoke, the monster heard, While passion still her bosom stirred. Away from Ráma's side she broke, And thus in turn to LakshmaG spoke: “Come, for thy bride take me who shine In fairest grace that suits with thine. Thou by my side from grove to grove Of DaG ak's wild in bliss shalt rove.” Then LakshmaG, skilled in soft address, Wooed by the amorous giantess, With art to turn her love aside, To ZúrpaGakhá thus replied: “And can so high a dame agree The slave-wife of a slave to be? I, lotus-hued! in good and ill Am bondsman to my brother's will. Be thou, fair creature radiant-eyed, My honoured brother's younger bride: With faultless tint and dainty limb, A happy wife, bring joy to him. He from his spouse grown old and grey, Deformed, untrue, will turn away, Her withered charms will gladly leave, And to his fair young darling cleave. For who could be so fond and blind, O loveliest of all female kind, To love another dame and slight Thy beauties rich in all delight?”
- **Translation**: 

---

### Verse 19 (Ramayana 0.904)
- **Original**: 886 The Ramayana Thus LakshmaG praised in scornful jest The long-toothed fiend with loathly breast, Who fondly heard his speech, nor knew His mocking words were aught but true. Again inflamed with love she fled To Ráma, in his leafy shed Where Sítá rested by his side, And to the mighty victor cried: “What, Ráma, canst thou blindly cling To this old false misshapen thing? Wilt thou refuse the charms of youth For withered breast and grinning tooth! Canst thou this wretched creature prize And look on me with scornful eyes? This aged crone this very hour Before thy face will I devour: Then joyous, from all rivals free. Through DaG ak will I stray with thee.” She spoke, and with a glance of flame Rushed on the fawn-eyed Maithil dame: So would a horrid meteor mar Fair RohiGí's soft beaming star. But as the furious fiend drew near, Like Death's dire noose which chills with fear, The mighty chief her purpose stayed, And spoke, his brother to upbraid: “Ne'er should we jest with creatures rude, Of savage race and wrathful mood. Think, LakshmaG, think how nearly slain My dear Videhan breathes again. Let not the hideous wretch escape Without a mark to mar her shape.
- **Translation**: 

---

### Verse 20 (Ramayana 0.905)
- **Original**: Canto XVIII. The Mutilation. 887 Strike, lord of men, the monstrous fiend, Deformed, and foul, and evil-miened.” He spoke: then LakshmaG's wrath rose high, And there before his brother's eye, He drew that sword which none could stay, And cleft her nose and ears away. Noseless and earless, torn and maimed, With fearful shrieks the fiend exclaimed, And frantic in her wild distress Resought the distant wilderness. Deformed, terrific, huge, and dread, As on she moved, her gashes bled, And groan succeeded groan as loud As roars, ere rain, the thunder cloud. Still on the fearful monster passed, While streams of blood kept falling fast, And with a roar, and arms outspread Within the boundless wood she fled. To Janasthán the monster flew; Fierce Khara there she found, With chieftains of the giant crew In thousands ranged around. Before his awful feet she bent And fell with piercing cries, As when a bolt in swift descent Comes flashing from the skies. There for a while with senses dazed Silent she lay and scared: At length her drooping head she raised, And all the tale declared, How Ráma, Lakshma G, and the dame Had reached that lonely place: Then told her injuries and shame,
- **Translation**: 

---

