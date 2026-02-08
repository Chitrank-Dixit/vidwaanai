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

### Verse 1 (Ramayana 0.1046)
- **Original**: 1028 The Ramayana The talons stripped the flesh away. He fought with claws and beak and wing, And tore the long hair of the king. Still as the royal vulture beat The giant with his wings and feet, Swelled the fiend's lips, his body shook With furious rage too great to brook. About the Maithil dame he cast One huge left arm and held her fast. In furious rage to frenzy fanned He struck the vulture with his hand. Jatáyus mocked the vain assay, And rent his ten left arms away. Down dropped the severed limbs: anew Ten others from his body grew: Thus bright with pearly radiance glide Dread serpents from the hillock side, Again in wrath the giant pressed The lady closer to his breast, And foot and fist sent blow on blow In ceaseless fury at the foe. So fierce and dire the battle, waged Between those mighty champions, raged: Here was the lord of giants, there The noblest of the birds of air. Thus, as his love of Ráma taught, The faithful vulture strove and fought. But RávaG seized his sword and smote His wings and side and feet and throat. At mangled side and wing he bled; He fell, and life was almost fled. The lady saw her champion lie, His plumes distained with gory dye, And hastened to the vulture's side
- **Translation**: 

---

### Verse 2 (Ramayana 0.1047)
- **Original**: Canto LII. Rávan's Flight. 1029 Grieving as though a kinsman died. The lord of Lanká's island viewed The vulture as he lay: Whose back like some dark cloud was hued, His breast a paly grey, Like ashes, when by none renewed, The flame has died away. The lady saw with mournful eye, Her champion press the plain,— The royal bird, her true ally Whom Ráva G's might had slain. Her soft arms locked in strict embrace Around his neck she kept, And lovely with her moon-bright face Bent o'er her friend and wept. Canto LII. Rávan's Flight. Fair as the lord of silvery rays Whom every star in heaven obeys, The Maithil dame her plaint renewed O'er him by RávaG's might subdued: “Dreams, omens, auguries foreshow Our coming lot of weal and woe: But thou, my Ráma, couldst not see The grievous blow which falls on thee. The birds and deer desert the brakes And show the path my captor takes, And thus e'en now this royal bird Flew to mine aid by pity stirred. Slain for my sake in death he lies,
- **Translation**: 

---

### Verse 3 (Ramayana 0.1048)
- **Original**: 1030 The Ramayana The broad-winged rover of the skies. O Ráma, haste, thine aid I crave: O Lakshma G, why delay to save? Brave sons of old Ikshváku, hear And rescue in this hour of fear.” Her flowery wreath was torn and rent, Crushed was each sparkling ornament. She with weak arms and trembling knees Clung like a creeper to the trees, And like some poor deserted thing With wild shrieks made the forest ring. But swift the giant reached her side,[291] As loud on Ráma's name she cried. Fierce as grim Death one hand he laid Upon her tresses' lovely braid. “That touch, thou impious King, shall be The ruin of thy race and thee.” The universal world in awe That outrage on the lady saw, All nature shook convulsed with dread, And darkness o'er the land was spread. The Lord of Day grew dark and chill, And every breath of air was still. The Eternal Father of the sky Beheld the crime with heavenly eye, And spake with solemn voice,“The deed, The deed is done, of old decreed.” Sad were the saints within the grove, But triumph with their sorrow strove. They wept to see the Maithil dame Endure the outrage, scorn, and shame: They joyed because his life should pay The penalty incurred that day.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1049)
- **Original**: Canto LII. Rávan's Flight. 1031 Then RávaG raised her up, and bare His captive through the fields of air, Calling with accents loud and shrill On Ráma and on LakshmaG still. With sparkling gems on arm and breast, In silk of paly amber dressed, High in the air the Maithil dame Gleamed like the lightning's flashing flame. The giant, as the breezes blew Upon her robes of amber hue, And round him twined that gay attire, Showed like a mountain girt with fire. The lady, fairest of the fair, Had wreathed a garland round her hair; Its lotus petals bright and sweet Rained down about the giant's feet. Her vesture, bright as burning gold, Gave to the wind each glittering fold, Fair as a gilded cloud that gleams Touched by the Day-God's tempered beams. Yet struggling in the fiend's embrace, The lady with her sweet pure face, Far from her lord, no longer wore The light of joy that shone before. Like some sad lily by the side Of waters which the sun has dried; Like the pale moon uprising through An autumn cloud of darkest hue, So was her perfect face between The arms of giant RávaG seen: Fair with the charm of braided tress And forehead's finished loveliness; Fair with the ivory teeth that shed White lustre through the lips' fine red,
- **Translation**: 

---

### Verse 5 (Ramayana 0.1050)
- **Original**: 1032 The Ramayana Fair as the lotus when the bud Is rising from the parent flood. With faultless lip and nose and eye, Dear as the moon that floods the sky With gentle light, of perfect mould, She seemed a thing of burnished gold, Though on her cheek the traces lay Of tears her hand had brushed away. But as the moon-beams swiftly fade Ere the great Day-God shines displayed, So in that form of perfect grace Still trembling in the fiend's embrace, From her beloved Ráma reft, No light of pride or joy was left. The lady with her golden hue O'er the swart fiend a lustre threw, As when embroidered girths enfold An elephant with gleams of gold. Fair as the lily's bending stem,— Her arms adorned with many a gem, A lustre to the fiend she lent Gleaming from every ornament, As when the cloud-shot flashes light The shadows of a mountain height. Whene'er the breezes earthward bore The tinkling of the zone she wore, He seemed a cloud of darkness hue Sending forth murmurs as it flew. As on her way the dame was sped From her sweet neck fair flowers were shed, The swift wind caught the flowery rain And poured it o'er the fiend again. The wind-stirred blossoms, sweet to smell, On the dark brows of RávaG fell,
- **Translation**: 

---

### Verse 6 (Ramayana 0.1051)
- **Original**: Canto LII. Rávan's Flight. 1033 Like lunar constellations set On Meru for a coronet. From her small foot an anklet fair With jewels slipped, and through the air, Like a bright circlet of the flame Of thunder, to the valley came. The Maithil lady, fair to see As the young leaflet of a tree Clad in the tender hues of spring, Flashed glory on the giant king, As when a gold-embroidered zone Around an elephant is thrown. While, bearing far the lady, through The realms of sky the giant flew, She like a gleaming meteor cast A glory round her as she passed. Then from each limb in swift descent Dropped many a sparkling ornament: On earth they rested dim and pale Like fallen stars when virtues fail.504 Around her neck a garland lay Bright as the Star-God's silvery ray: It fell and flashed like Gangá sent From heaven above the firmament.505 The birds of every wing had flocked To stately trees by breezes rocked: [292] These bowed their wind-swept heads and said: “My lady sweet, be comforted.” With faded blooms each brook within Whose waters moved no gleamy fin, Stole sadly through the forest dell 504 The spirits of the good dwell in heaven until their store of accumulated merit is exhausted. Then they redescend to earth in the form of falling stars. 505 See The Descent of Gangá, Book I Canto XLIV.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1052)
- **Original**: 1034 The Ramayana Mourning the dame it loved so well. From every woodland region near Came lions, tigers, birds, and deer, And followed, each with furious look, The way her flying shadow took. For Sítá's loss each lofty hill Whose tears were waterfall, and rill, Lifting on high each arm-like steep, Seemed in the general woe to weep. When the great sun, the lord of day, Saw RávaG tear the dame away, His glorious light began to fail And all his disk grew cold and pale. “If RávaG from the forest flies With Ráma's Sítá as his prize, Justice and truth have vanished hence, Honour and right and innocence.” Thus rose the cry of wild despair From spirits as they gathered there. In trembling troops in open lawns Wept, wild with woe, the startled fawns, And a strange terror changed the eyes They lifted to the distant skies. On silvan Gods who love the dell A sudden fear and trembling fell, As in the deepest woe they viewed The lady by the fiend subdued. Still in loud shrieks was heard afar That voice whose sweetness naught could mar, While eager looks of fear and woe She bent upon the earth below. The lady of each winning wile With pearly teeth and lovely smile, Seized by the lord of Lanká's isle,
- **Translation**: 

---

### Verse 8 (Ramayana 0.1053)
- **Original**: Canto LIII. Sítá's Threats. 1035 Looked down for friends in vain. She saw no friend to aid her, none, Not Ráma nor the younger son Of Da[aratha, and undone She swooned with fear and pain. Canto LIII. Sítá's Threats. Soon as the Maithil lady knew That high through air the giant flew, Distressed with grief and sore afraid Her troubled spirit sank dismayed. Then, as anew the waters welled From those red eyes which sorrow swelled, Forth in keen words her passion broke, And to the fierce-eyed fiend she spoke: “Canst thou attempt a deed so base, Untroubled by the deep disgrace,— To steal me from my home and fly, When friend or guardian none was nigh? Thy craven soul that longed to steal, Fearing the blows that warriors deal, Upon a magic deer relied To lure my husband from my side, Friend of his sire, the vulture king Lies low on earth with mangled wing, Who gave his aged life for me And died for her he sought to free. Ah, glorious strength indeed is thine, Thou meanest of thy giant line, Whose courage dared to tell thy name
- **Translation**: 

---

### Verse 9 (Ramayana 0.1054)
- **Original**: 1036 The Ramayana And conquer in the fight a dame. Does the vile deed that thou hast done Cause thee no shame, thou wicked one— A woman from her home to rend When none was near his aid to lend? Through all the worlds, O giant King, The tidings of this deed will ring, This deed in law and honour's spite By one who claims a hero's might. Shame on thy boasted valour, shame! Thy prowess is an empty name. Shame, giant, on this cursed deed For which thy race is doomed to bleed! Thou fliest swifter than the gale, For what can strength like thine avail? Stay for one hour, O RávaG, stay; Thou shalt not flee with life away. Soon as the royal chieftains' sight Falls on the thief who roams by night, Thou wilt not, tyrant, live one hour Though backed by all thy legions' power. Ne'er can thy puny strength sustain The tempest of their arrowy rain: Have e'er the trembling birds withstood The wild flames raging in the wood? Hear me, O RávaG, let me go, And save thy soul from coming woe. Or if thou wilt not set me free, Wroth for this insult done to me. With his brave brother's aid my lord Against thy life will raise his sword. A guilty hope inflames thy breast His wife from Ráma's home to wrest. Ah fool, the hope thou hast is vain;
- **Translation**: 

---

### Verse 10 (Ramayana 0.1055)
- **Original**: Canto LIII. Sítá's Threats. 1037 Thy dreams of bliss shall end in pain. If torn from all I love by thee My godlike lord no more I see, Soon will I die and end my woes, Nor live the captive of my foes. Ah fool, with blinded eyes to choose The evil and the good refuse! So the sick wretch with stubborn will Turns fondly to the cates that kill, And madly draws his lips away From medicine that would check decay. About thy neck securely wound [293] The deadly coil of Fate is bound, And thou, O RávaG, dost not fear Although the hour of death is near. With death-doomed sight thine eyes behold The gleaming of the trees of gold,— See dread VaitaraGi, the flood That rolls a stream of foamy blood,— See the dark wood by all abhorred— Its every leaf a threatening sword. The tangled thickets thou shall tread Where thorns with iron points are spread. For never can thy days be long, Base plotter of this shame and wrong To Ráma of the lofty soul: He dies who drinks the poisoned bowl. The coils of death around thee lie: They hold thee and thou canst not fly. Ah whither, tyrant, wouldst thou run The vengeance of my lord to shun? By his unaided arm alone Were twice seven thousand fiends o'erthrown: Yes, in the twinkling of an eye
- **Translation**: 

---

### Verse 11 (Ramayana 0.1056)
- **Original**: 1038 The Ramayana He forced thy mightiest fiends to die. And shall that lord of lion heart, Skilled in the bow and spear and dart, Spare thee, O fiend, in battle strife, The robber of his darling wife?” These were her words, and more beside, By wrath and bitter hate supplied. Then by her woe and fear o'erthrown She wept again and made her moan. As long she wept in grief and dread, Scarce conscious of the words she said, The wicked giant onward fled And bore her through the air. As firm he held the Maithil dame, Still wildly struggling, o'er her frame With grief and bitter misery came The trembling of despair. Canto LIV. Lanká. He bore her on in rapid flight, And not a friend appeared in sight. But on a hill that o'er the wood Raised its high top five monkeys stood. From her fair neck her scarf she drew, And down the glittering vesture flew. With earring, necklet, chain, and gem, Descending in the midst of them: “For these,” she thought,“my path may show, And tell my lord the way I go.”
- **Translation**: 

---

### Verse 12 (Ramayana 0.1057)
- **Original**: Canto LIV. Lanká. 1039 Nor did the fiend, in wild alarm, Mark when she drew from neck and arm And foot the gems and gold, and sent To earth each gleaming ornament. The monkeys raised their tawny eyes That closed not in their first surprise, And saw the dark-eyed lady, where She shrieked above them in the air. High o'er their heads the giant passed Holding the weeping lady fast. O'er Pampa's flashing flood he sped And on to Lanká's city fled. He bore away in senseless joy The prize that should his life destroy, Like the rash fool who hugs beneath His robe a snake with venomed teeth. Swift as an arrow from a bow, Speeding o'er lands that lay below, Sublime in air his course he took O'er wood and rock and lake and brook. He passed at length the sounding sea Where monstrous creatures wander free,— Seat of Lord VaruG's ancient reign, Controller of the eternal main. The angry waves were raised and tossed As RávaG with the lady crossed, And fish and snake in wild unrest Showed flashing fin and gleaming crest. Then from the blessed troops who dwell In air celestial voices fell: “O ten-necked King,” they cried,“attend: This guilty deed will bring thine end.”
- **Translation**: 

---

### Verse 13 (Ramayana 0.1058)
- **Original**: 1040 The Ramayana Then RávaG speeding like the storm, Bearing his death in human form, The struggling Sítá, lighted down In royal Lanká's glorious town; A city bright and rich, that showed Well-ordered street and noble road; Arranged with just division, fair With multitudes in court and square. Thus, all his journey done, he passed Within his royal home at last. There in a queenly bower he placed The black-eyed dame with dainty waist: Thus in her chamber Máyá laid The lovely Máyá, demon maid. Then RávaG gave command to all The dread she-fiends who filled the hall: “This captive lady watch and guard From sight of man and woman barred. But all the fair one asks beside Be with unsparing hand supplied: As though 'twere I that asked, withhold No pearls or dress or gems or gold. And she among you that shall dare Of purpose or through want of care One word to vex her soul to say, Throws her unvalued life away.” Thus spake the monarch of their race To those she-fiends who thronged the place, And pondering on the course to take Went from the chamber as he spake. He saw eight giants, strong and dread, On flesh of bleeding victims fed, Proud in the boon which Brahmá gave,[294]
- **Translation**: 

---

### Verse 14 (Ramayana 0.1059)
- **Original**: Canto LIV. Lanká. 1041 And trusting in its power to save. He thus the mighty chiefs addressed Of glorious power and strength possessed: “Arm, warriors, with the spear and bow; With all your speed from Lanká go, For Janasthán, our own no more, Is now defiled with giants' gore; The seat of Khara's royal state Is left unto us desolate. In your brave hearts and might confide, And cast ignoble fear aside. Go, in that desert region dwell Where the fierce giants fought and fell. A glorious host that region held, For power and might unparalleled, By DúshaG and brave Khara led,— All, slain by Ráma's arrows, bled. Hence boundless wrath that spurns control Reigns paramount within my soul, And naught but Ráma's death can sate The fury of my vengeful hate. I will not close my slumbering eyes Till by this hand my foeman dies. And when mine arm has slain the foe Who laid those giant princes low, Long will I triumph in the deed, Like one enriched in utmost need. Now go; that I this end may gain, In Janasthán, O chiefs, remain. Watch Ráma there with keenest eye, And all his deeds and movements spy. Go forth, no helping art neglect, Be brave and prompt and circumspect, And be your one endeavour still
- **Translation**: 

---

### Verse 15 (Ramayana 0.1060)
- **Original**: 1042 The Ramayana To aid mine arm this foe to kill. Oft have I seen your warrior might Proved in the forehead of the fight, And sure of strength I know so well Send you in Janasthán to dwell.” The giants heard with prompt assent The pleasant words he said, And each before his master bent For meet salute, his head. Then as he bade, without delay, From Lanká's gate they passed, And hurried forward on their way Invisible and fast. Canto LV. Sítá In Prison. Thus RávaG his commandment gave To those eight giants strong and brave, So thinking in his foolish pride Against all dangers to provide. Then with his wounded heart aflame With love he thought upon the dame, And took with hasty steps the way To the fair chamber where she lay. He saw the gentle lady there Weighed down by woe too great to bear, Amid the throng of fiends who kept Their watch around her as she wept: A pinnace sinking neath the wave When mighty winds around her rave: A lonely herd-forsaken deer,
- **Translation**: 

---

### Verse 16 (Ramayana 0.1061)
- **Original**: Canto LV. Sítá In Prison. 1043 When hungry dogs are pressing near. Within the bower the giant passed: Her mournful looks were downward cast. As there she lay with streaming eyes The giant bade the lady rise, And to the shrinking captive showed The glories of his rich abode, Where thousand women spent their days In palaces with gold ablaze; Where wandered birds of every sort, And jewels flashed in hall and court. Where noble pillars charmed the sight With diamond and lazulite, And others glorious to behold With ivory, crystal, silver, gold. There swelled on high the tambour's sound, And burnished ore was bright around He led the mournful lady where Resplendent gold adorned the stair, And showed each lattice fair to see With silver work and ivory: Showed his bright chambers, line on line, Adorned with nets of golden twine. Beyond he showed the Maithil dame His gardens bright as lightning's flame, And many a pool and lake he showed Where blooms of gayest colour glowed. Through all his home from view to view The lady sunk in grief he drew. Then trusting in her heart to wake Desire of all she saw, he spake: “Three hundred million giants, all Obedient to their master's call, Not counting young and weak and old,
- **Translation**: 

---

### Verse 17 (Ramayana 0.1062)
- **Original**: 1044 The Ramayana Serve me with spirits fierce and bold. A thousand culled from all of these Wait on the lord they long to please. This glorious power, this pomp and sway, Dear lady, at thy feet I lay: Yea, with my life I give the whole, O dearer than my life and soul. A thousand beauties fill my hall: Be thou my wife and rule them all. O hear my supplication! why This reasonable prayer deny? Some pity to thy suitor show, For love's hot flames within me glow. This isle a hundred leagues in length, Encompassed by the ocean's strength, Would all the Gods and fiends defy Though led by Him who rules the sky. No God in heaven, no sage on earth, No minstrel of celestial birth,[295] No spirit in the worlds I see A match in power and might for me. What wilt thou do with Ráma, him Whose days are short, whose light is dim, Expelled from home and royal sway, Who treads on foot his weary way? Leave the poor mortal to his fate, And wed thee with a worthier mate. My timid love, enjoy with me The prime of youth before it flee. Do not one hour the hope retain To look on Ráma's face again. For whom would wildest thought beguile To seek thee in the giants' isle? Say who is he has power to bind
- **Translation**: 

---

### Verse 18 (Ramayana 0.1063)
- **Original**: Canto LV. Sítá In Prison. 1045 In toils of net the rushing wind. Whose is the mighty hand will tame And hold the glory of the flame? In all the worlds above, below, Not one, O fair of form, I know Who from this isle in fight could rend The lady whom these arms defend. Fair Queen, o'er Lanká's island reign, Sole mistress of the wide domain. Gods, rovers of the night like me, And all the world thy slaves will be. O'er thy fair brows and queenly head Let consecrating balm be shed, And sorrow banished from thy breast, Enjoy my love and take thy rest. Here never more thy soul shall know The memory of thy former woe, And here shall thou enjoy the meed Deserved by every virtuous deed. Here garlands glow of flowery twine, With gorgeous hues and scent divine. Take gold and gems and rich attire: Enjoy with me thy heart's desire. There stand, of chariots far the best, The car my brother once possessed. Which, victor in the stricken field, I forced the Lord of Gold to yield. 'Tis wide and high and nobly wrought, Bright as the sun and swift as thought. Therein O Sítá, shalt thou ride Delighted by thy lover's side. But sorrow mars with lingering trace The splendour of thy lotus face. A cloud of woe is o'er it spread,
- **Translation**: 

---

### Verse 19 (Ramayana 0.1064)
- **Original**: 1046 The Ramayana And all the light of joy is fled.” The lady, by her woe distressed, One corner of her raiment pressed To her sad cheek like moonlight clear, And wiped away a falling tear. The rover of the night renewed His eager pleading as he viewed The lady stand like one distraught, Striving to fix her wandering thought: “Think not, sweet lady, of the shame Of broken vows, nor fear the blame. The saints approve with favouring eyes This union knit with marriage ties. O beauty, at thy radiant feet I lay my heads, and thus entreat. One word of grace, one look I crave: Have pity on thy prostrate slave. These idle words I speak are vain, Wrung forth by love's consuming pain, And ne'er of RávaG be it said He wooed a dame with prostrate head.” Thus to the Maithil lady sued The monarch of the giant brood, And “She is now mine own,” he thought, In Death's dire coils already caught.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1065)
- **Original**: Canto LVI. Sítá's Disdain. 1047 Canto LVI. Sítá's Disdain. His words the Maithil lady heard Oppressed by woe but undeterred. Fear of the fiend she cast aside, And thus in noble scorn replied: “His word of honour never stained King Da[aratha nobly reigned, The bridge of right, the friend of truth. His eldest son, a noble youth, Is Ráma, virtue's faithful friend, Whose glories through the worlds extend. Long arms and large full eyes has he, My husband, yea a God to me. With shoulders like the forest king's, From old Ikshváku's line he springs. He with his brother LakshmaG's aid Will smite thee with the vengeful blade. Hadst thou but dared before his eyes To lay thine hand upon the prize, Thou stretched before his feet hadst lain In Janasthán like Khara slain. Thy boasted rovers of the night With hideous shapes and giant might,— Like serpents when the feathered king Swoops down with his tremendous wing,— Will find their useless venom fail When Ráma's mighty arms assail. The rapid arrows bright with gold, Shot from the bow he loves to hold, Will rend thy frame from flank to flank As Gangá's waves erode the bank. Though neither God nor fiend have power To slay thee in the battle hour,
- **Translation**: 

---

