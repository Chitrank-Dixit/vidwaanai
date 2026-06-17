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

### Verse 1 (Ramayan 0.901)
- **Original**: Canto XVII. Súrpanakhá. 883 I sought this wood to harbour in. But speak, for I of thee in turn Thy name, and race, and sire would learn. Thou art of giant race, I ween. Changing at will thy form and mien. Speak truly, and the cause declare That bids thee to these shades repair.” Thus Ráma spoke: the demon heard, And thus replied by passion spurred: “Of giant race, what form soe'er My fancy wills, 'tis mine to wear. Named ZúrpaGakhá here I stray, And where I walk spread wild dismay. King RávaG is my brother: fame Has taught perchance his dreaded name, Strong KumbhakarGa slumbering deep In chains of never-ending sleep: VibhíshaG of the duteous mind, In needs unlike his giant kind: DúshaG and Khara, brave and bold Whose fame by every tongue is told: Their might by mine is far surpassed; But when, O best of men, I cast These fond eyes on thy form, I see My chosen love and lord in thee. Endowed with wondrous might am I: Where'er my fancy leads I fly. The poor misshapen Sítá leave, And me, thy worthier bride receive. Look on my beauty, and prefer A spouse more meet than one like her: I'll eat that ill-formed woman there: Thy brother too her fate shall share.
- **Translation**: 

---

### Verse 2 (Ramayan 0.902)
- **Original**: 884 The Ramayana But come, beloved, thou shalt roam With me through all our woodland home; Each varied grove with me shalt seek, And gaze upon each mountain peak.” As thus she spoke, the monster gazed With sparkling eyes where passion blazed: Then he, in lore of language learned, This answer eloquent returned: Canto XVIII. The Mutilation. On her ensnared in Káma's net His eyes the royal Ráma set,[251] And thus, her passion to beguile, Addressed her with a gentle smile: “I have a wife: behold her here, My Sítá ever true and dear: And one like thee will never brook Upon a rival spouse to look. But there my brother LakshmaG stands: Unchained is he by nuptial bands: A youth heroic, loved of all, Gracious and gallant, fair and tall. With winning looks, most nobly bred, Unmatched till now, he longs to wed. Meet to enjoy thy youthful charms, O take him to thy loving arms. Enamoured on his bosom lie, Fair damsel of the radiant eye, As the warm sunlight loves to rest Upon her darling Meru's breast.”
- **Translation**: 

---

### Verse 3 (Ramayan 0.903)
- **Original**: Canto XVIII. The Mutilation. 885 The hero spoke, the monster heard, While passion still her bosom stirred. Away from Ráma's side she broke, And thus in turn to LakshmaG spoke: “Come, for thy bride take me who shine In fairest grace that suits with thine. Thou by my side from grove to grove Of DaG ak's wild in bliss shalt rove.” Then LakshmaG, skilled in soft address, Wooed by the amorous giantess, With art to turn her love aside, To ZúrpaGakhá thus replied: “And can so high a dame agree The slave-wife of a slave to be? I, lotus-hued! in good and ill Am bondsman to my brother's will. Be thou, fair creature radiant-eyed, My honoured brother's younger bride: With faultless tint and dainty limb, A happy wife, bring joy to him. He from his spouse grown old and grey, Deformed, untrue, will turn away, Her withered charms will gladly leave, And to his fair young darling cleave. For who could be so fond and blind, O loveliest of all female kind, To love another dame and slight Thy beauties rich in all delight?”
- **Translation**: 

---

### Verse 4 (Ramayan 0.904)
- **Original**: 886 The Ramayana Thus LakshmaG praised in scornful jest The long-toothed fiend with loathly breast, Who fondly heard his speech, nor knew His mocking words were aught but true. Again inflamed with love she fled To Ráma, in his leafy shed Where Sítá rested by his side, And to the mighty victor cried: “What, Ráma, canst thou blindly cling To this old false misshapen thing? Wilt thou refuse the charms of youth For withered breast and grinning tooth! Canst thou this wretched creature prize And look on me with scornful eyes? This aged crone this very hour Before thy face will I devour: Then joyous, from all rivals free. Through DaG ak will I stray with thee.” She spoke, and with a glance of flame Rushed on the fawn-eyed Maithil dame: So would a horrid meteor mar Fair RohiGí's soft beaming star. But as the furious fiend drew near, Like Death's dire noose which chills with fear, The mighty chief her purpose stayed, And spoke, his brother to upbraid: “Ne'er should we jest with creatures rude, Of savage race and wrathful mood. Think, LakshmaG, think how nearly slain My dear Videhan breathes again. Let not the hideous wretch escape Without a mark to mar her shape.
- **Translation**: 

---

### Verse 5 (Ramayan 0.905)
- **Original**: Canto XVIII. The Mutilation. 887 Strike, lord of men, the monstrous fiend, Deformed, and foul, and evil-miened.” He spoke: then LakshmaG's wrath rose high, And there before his brother's eye, He drew that sword which none could stay, And cleft her nose and ears away. Noseless and earless, torn and maimed, With fearful shrieks the fiend exclaimed, And frantic in her wild distress Resought the distant wilderness. Deformed, terrific, huge, and dread, As on she moved, her gashes bled, And groan succeeded groan as loud As roars, ere rain, the thunder cloud. Still on the fearful monster passed, While streams of blood kept falling fast, And with a roar, and arms outspread Within the boundless wood she fled. To Janasthán the monster flew; Fierce Khara there she found, With chieftains of the giant crew In thousands ranged around. Before his awful feet she bent And fell with piercing cries, As when a bolt in swift descent Comes flashing from the skies. There for a while with senses dazed Silent she lay and scared: At length her drooping head she raised, And all the tale declared, How Ráma, Lakshma G, and the dame Had reached that lonely place: Then told her injuries and shame,
- **Translation**: 

---

### Verse 6 (Ramayan 0.906)
- **Original**: 888 The Ramayana And showed her bleeding face. Canto XIX. The Rousing Of Khara. When Khara saw his sister lie With blood-stained limbs and troubled eye,[252] Wild fury in his bosom woke, And thus the monstrous giant spoke; “Arise, my sister; cast away This numbing terror and dismay, And straight the impious hand declare That marred those features once so fair. For who his finger tip will lay On the black snake in childish play, And unattacked, with idle stroke His poison-laden fang provoke? Ill-fated fool, he little knows Death's noose around his neck he throws, Who rashly met thee, and a draught Of life-destroying poison quaffed. Strong, fierce as death, 'twas thine to choose Thy way at will, each shape to use; In power and might like one of us: What hand has maimed and marred thee thus? What God or fiend this deed has wrought, What bard or sage of lofty thought Was armed with power supremely great Thy form to mar and mutilate? In all the worlds not one I see Would dare a deed to anger me:
- **Translation**: 

---

### Verse 7 (Ramayan 0.907)
- **Original**: Canto XIX. The Rousing Of Khara. 889 Not Indra's self, the Thousand-eyed, Beneath whose hand fierce Páka459 died. My life-destroying darts this day His guilty breath shall rend away, E'en as the thirsty wild swan drains Each milk-drop that the wave retains. Whose blood in foaming streams shall burst O'er the dry ground which lies athirst, When by my shafts transfixed and slain He falls upon the battle plain? From whose dead corpse shall birds of air The mangled flesh and sinews tear, And in their gory feast delight, When I have slain him in the fight? Not God or bard or wandering ghost, No giant of our mighty host Shall step between us, or avail To save the wretch when I assail. Collect each scattered sense, recall Thy troubled thoughts, and tell me all. What wretch attacked thee in the way, And quelled thee in victorious fray?” His breast with burning fury fired, Thus Khara of the fiend inquired: And then with many a tear and sigh Thus ZúrpaGakhá made reply: “'Tis Da[aratha's sons, a pair Strong, resolute, and young, and fair: In coats of dark and blackdeer's hide, And like the radiant lotus eyed: On berries roots and fruit they feed, And lives of saintly virtue lead: 459 A demon slain by Indra.
- **Translation**: 

---

### Verse 8 (Ramayan 0.908)
- **Original**: 890 The Ramayana With ordered senses undefiled, Ráma and LakshmaG are they styled. Fair as the Minstrels' King460 are they, And stamped with signs of regal sway. I know not if the heroes trace Their line from Gods or Dánav461 race. There by these wondering eyes between The noble youths a dame was seen, Fair, blooming, young, with dainty waist, And all her bright apparel graced. For her with ready heart and mind The royal pair their strength combined, And brought me to this last distress, Like some lost woman, comfortless. Perfidious wretch! my soul is fain Her foaming blood and theirs to drain. O let me head the vengeful fight, And with this hand my murderers smite. Come, brother, hasten to fulfil This longing of my eager will. On to the battle! Let me drink Their lifeblood as to earth they sink.” Then Khara, by his sister pressed, Inflamed with fury, gave his hest To twice seven giants of his crew, Fierce as the God of death to view: 460 Chitraratha, King of the Gandharvas. 461 Titanic.
- **Translation**: 

---

### Verse 9 (Ramayan 0.909)
- **Original**: Canto XX. The Giants' Death. 891 'Two men equipped with arms, who wear Deerskin and bark and matted hair, Leading a beauteous dame, have strayed To the wild gloom of DaG ak's shade. These men, this cursed woman slay, And hasten back without delay, That this my sister's lips may be Red with the lifeblood of the three. Giants, my wounded sister longs To take this vengeance for her wrongs. With speed her dearest wish fulfil, And with your might these creatures kill. Soon as your matchless strength shall lay These brothers dead in battle fray, She in triumphant joy will laugh, And their hearts' blood delighted quaff.” The giants heard the words he said, And forth withZúrpaGakhá sped, As mighty clouds in autumn fly Urged by the wind along the sky. Canto XX. The Giants' Death. FierceZúrpaGakhá with her train To Ráma's dwelling came again, And to the eager giants showed Where Sítá and the youths abode. Within the leafy cot they spied The hero by his consort's side, And faithful LakshmaG ready still To wait upon his brother's will. [253]
- **Translation**: 

---

### Verse 10 (Ramayan 0.910)
- **Original**: 892 The Ramayana Then noble Ráma raised his eye And saw the giants standing nigh, And then, as nearer still they pressed. His glorious brother thus addressed, “Be thine a while, my brother dear, To watch o'er Sítá's safety here, And I will slay these creatures who The footsteps of my spouse pursue.” He spoke, and reverent LakshmaG heard Submissive to his brother's word. The son of Raghu, virtuous-souled, Strung his great bow adorned with gold, And, with the weapon in his hand, Addressed him to the giant band: “Ráma and LakshmaG we, who spring From Da[aratha, mighty king; We dwell a while with Sítá here In DaG ak forest wild and drear. On woodland roots and fruit we feed, And lives of strictest rule we lead. Say why would ye our lives oppress Who sojourn in the wilderness. Sent hither by the hermits' prayer With bow and darts unused to spare, For vengeance am I come to slay Your sinful band in battle fray. Rest as ye are: remain content, Nor try the battle's dire event. Unless your offered lives ye spurn, O rovers of the night, return.”
- **Translation**: 

---

### Verse 11 (Ramayan 0.911)
- **Original**: Canto XX. The Giants' Death. 893 They listened while the hero spoke, And fury in each breast awoke. The Bráhman-slayers raised on high Their mighty spears and made reply: They spoke with eyes aglow with ire, While Ráma's burnt with vengeful tire, And answered thus, in fury wild, That peerless chief whose tones were mild: “Nay thou hast angered, overbold, Khara our lord, the mighty-souled, And for thy sin, in battle strife Shalt yield to us thy forfeit life. No power hast thou alone to stand Against the numbers of our band. 'Twere vain to match thy single might Against us in the front of fight. When we equipped for fight advance With brandished pike and mace and lance, Thou, vanquished in the desperate field, Thy bow, thy strength, thy life shalt yield.” With bitter words and threatening mien Thus furious spoke the fierce fourteen, And raising scimitar and spear On Ráma rushed in wild career. Their levelled spears the giant crew Against the matchless hero threw. His bow the son of Raghu bent, And twice seven shafts to meet them sent, And every javelin sundered fell By the bright darts he aimed so well.
- **Translation**: 

---

### Verse 12 (Ramayan 0.912)
- **Original**: 894 The Ramayana The hero saw: his anger grew To fury: from his side he drew Fresh sunbright arrows pointed keen, In number, like his foes, fourteen. His bow he grasped, the string he drew, And gazing on the giant crew, As Indra casts the levin, so Shot forth his arrows at the foe. The hurtling arrows, stained with gore, Through the fiends' breasts a passage tore, And in the earth lay buried deep As serpents through an ant-hill creep Like trees uptorn by stormy blast The shattered fiends to earth were cast, And there with mangled bodies they, Bathed in their blood and breathless, lay. With fainting heart and furious eye The demon saw her champions die. With drying wounds that scarcely bled Back to her brother's home she fled. Oppressed with pain, with loud lament At Khara's feet the monster bent. There like a plant whence slowly come The trickling drops of oozy gum, With her grim features pale with pain She poured her tears in ceaseless rain, There routedZúrpaGakhá lay, And told her brother all, The issue of the bloody fray, Her giant champions' fall.
- **Translation**: 

---

### Verse 13 (Ramayan 0.913)
- **Original**: Canto XXI. The Rousing Of Khara. 895 Canto XXI. The Rousing Of Khara. Low in the dust he saw her lie, And Khara's wrath grew fierce and high. Aloud he cried to her who came Disgracefully with baffled aim: “I sent with thee at thy request The bravest of my giants, best Of all who feed upon the slain: Why art thou weeping here again? Still to their master's interest true, My faithful, noble, loyal crew, Though slaughtered in the bloody fray, Would yet their monarch's word obey. Now I, my sister, fain would know The cause of this thy fear and woe, Why like a snake thou writhest there, Calling for aid in wild despair. Nay, lie not thus in lowly guise: Cast off thy weakness and arise!” With soothing words the giant chief Assuaged the fury of her grief. Her weeping eyes she slowly dried And to her brother thus replied: “I sought thee in my shame and fear With severed nose and mangled ear: My gashes like a river bled, I sought thee and was comforted. [254]
- **Translation**: 

---

### Verse 14 (Ramayan 0.914)
- **Original**: 896 The Ramayana Those twice seven giants, brave and strong, Thou sentest to avenge the wrong, To lay the savage Ráma low, And Lakshma G who misused me so. But ah, the shafts of Ráma through The bodies of my champions flew: Though madly fierce their spears they plied, Beneath his conquering might they died. I saw them, famed for strength and speed, I saw my heroes fall and bleed: Great trembling seized my every limb At the great deed achieved by him. In trouble, horror, doubt, and dread, Again to thee for help I fled. While terror haunts my troubled sight, I seek thee, rover of the night. And canst thou not thy sister free From this wide waste of troublous sea Whose sharks are doubt and terror, where Each wreathing wave is dark despair? Low lie on earth thy giant train By ruthless Ráma's arrows slain, And all the mighty demons, fed On blood, who followed me are dead. Now if within thy breast may be Pity for them and love for me, If thou, O rover of the night, Have valour and with him can fight, Subdue the giants' cruel foe Who dwells where DaG ak's thickets grow. But if thine arm in vain assay This queller of his foes to slay, Now surely here before thine eyes, Wronged and ashamed thy sister dies.
- **Translation**: 

---

### Verse 15 (Ramayan 0.915)
- **Original**: Canto XXII. Khara's Wrath. 897 Too well, alas, too well I see That, strong in war as thou mayst be, Thou canst not in the battle stand When Ráma meets thee hand to hand. Go forth, thou hero but in name, Assuming might thou canst not claim; Call friend and kin, no longer stay: Away from Janasthán, away! Shame of thy race! the weak alone Beneath thine arm may sink o'erthrown: Fly Ráma and his brother: they Are men too strong for thee to slay. How canst thou hope, O weak and base, To make this grove thy dwelling-place? With Ráma's might unmeet to vie, O'ermastered thou wilt quickly die. A hero strong in valorous deed Is Ráma, Da[aratha's seed: And scarce of weaker might than he His brother chief who mangled me.” Thus wept and wailed in deep distress The grim misshapen giantess: Before her brother's feet she lay O'erwhelmed with grief, and swooned away. Canto XXII. Khara's Wrath. Roused by the taunting words she spoke, The mighty Khara's wrath awoke, And there, while giants girt him round, In these fierce words an utterance found:
- **Translation**: 

---

### Verse 16 (Ramayan 0.916)
- **Original**: 898 The Ramayana “I cannot, peerless one, contain Mine anger at this high disdain, Galling as salt when sprinkled o'er The rawness of a bleeding sore. Ráma in little count I hold, Weak man whose days are quickly told. The caitiff with his life to-day For all his evil deeds shall pay. Dry, sister, dry each needless tear, Stint thy lament and banish fear, For Ráma and his brother go This day to Yáma's realm below. My warrior's axe shall stretch him slain, Ere set of sun, upon the plain, Then shall thy sated lips be red With his warm blood in torrents shed.” As Khara's speech the demon heard, With sudden joy her heart was stirred: She fondly praised him as the boast And glory of the giant host. First moved to ire by taunts and stings, Now soothed by gentle flatterings, To DúshaG, who his armies led, The demon Khara spoke, and said: “Friend, from the host of giants call Full fourteen thousand, best of all, Slaves of my will, of fearful might, Who never turn their backs in fight: Fiends who rejoice to slay and mar, Dark as the clouds of autumn are: Make ready quickly, O my friend, My chariot and the bows I bend.
- **Translation**: 

---

### Verse 17 (Ramayan 0.917)
- **Original**: Canto XXII. Khara's Wrath. 899 My swords, my shafts of brilliant sheen, My divers lances long and keen. On to the battle will I lead These heroes of Pulastya's seed, And thus, O famed for warlike skill, Ráma my wicked foeman kill.” He spoke, and ere his speech was done, His chariot glittering like the sun, Yoked and announced, by Dúshan's care, With dappled steeds was ready there. High as a peak from Meru rent It burned with golden ornament: The pole of lazulite, of gold Were the bright wheels whereon it rolled. With gold and moonstone blazoned o'er, Fish, flowers, trees, rocks, the panels bore; Auspicious birds embossed thereon, And stars in costly emblem shone. O'er flashing swords his banner hung, And sweet bells, ever tinkling, swung. [255] That mighty host with sword and shield And oar was ready for the field: And Khara saw, and Dúshan cried, “Forth to the fight, ye giants, ride.” Then banners waved, and shield and sword Flashed as the host obeyed its lord. From Janasthán they sallied out With eager speed, and din, and shout, Armed with the mace for close attacks, The bill, the spear, the battle-axe, Steel quoit and club that flashed afar, Huge bow and sword and scimitar, The dart to pierce, the bolt to strike,
- **Translation**: 

---

### Verse 18 (Ramayan 0.918)
- **Original**: 900 The Ramayana The murderous bludgeon, lance, and pike. So forth from Janasthán, intent On Khara's will, the monsters went. He saw their awful march: not far Behind the host he drove his car. Ware of his master's will, to speed The driver urged each gold-decked steed. Then forth the warrior's coursers sprang, And with tumultuous murmur rang Each distant quarter of the sky And realms that intermediate lie. High and more high within his breast His pride triumphant rose, While terrible as Death he pressed Onward to slay his foes, “More swiftly yet,” as on they fled, He cried in thundering tones Loud as a cloud that overhead Hails down a flood of stones. Canto XXIII. The Omens. As forth upon its errand went That huge ferocious armament, An awful cloud, in dust and gloom, With threatening thunders from its womb Poured in sad augury a flood Of rushing water mixt with blood. The monarch's steeds, though strong and fleet, Stumbled and fell: and yet their feet Passed o'er the bed of flowers that lay
- **Translation**: 

---

### Verse 19 (Ramayan 0.919)
- **Original**: Canto XXIII. The Omens. 901 Fresh gathered on the royal way. No gleam of sunlight struggled through The sombre pall of midnight hue, Edged with a line of bloody red, Like whirling torches overhead. A vulture, fierce, of mighty size. Terrific with his cruel eyes, Perched on the staff enriched with gold, Whence hung the flag in many a fold. Each ravening bird, each beast of prey Where Janasthán's wild thickets lay, Rose with a long discordant cry And gathered as the host went by. And from the south long, wild, and shrill, Came spirit voices boding ill. Like elephants in frantic mood, Vast clouds terrific, sable-hued, Hid all the sky where'er they bore Their load of water mixt with gore. Above, below, around were spread Thick shades of darkness strange and dread, Nor could the wildered glance descry A point or quarter of the sky. Then came o'er heaven a sanguine hue, Though evening's flush not yet was due, While each ill-omened bird that flies Assailed the king with harshest cries. There screamed the vulture and the crane, And the loud jackal shrieked again. Each hideous thing that bodes aright Disaster in the coming fight, With gaping mouth that hissed and flamed, The ruin of the host proclaimed. Eclipse untimely reft away
- **Translation**: 

---

### Verse 20 (Ramayan 0.920)
- **Original**: 902 The Ramayana The brightness of the Lord of Day, And near his side was seen to glow A mace-like comet boding woe. Then while the sun was lost to view A mighty wind arose and blew, And stars like fireflies shed their light, Nor waited for the distant night. The lilies drooped, the brooks were dried, The fish and birds that swam them died, And every tree that was so fair With flower and fruit was stripped and bare. The wild wind ceased, yet, raised on high, Dark clouds of dust involved the sky. In doleful twitter long sustained The restless Sárikás462 complained, And from the heavens with flash and flame Terrific meteors roaring came. Earth to her deep foundation shook With rock and tree and plain and brook, As Khara with triumphant shout, Borne in his chariot, sallied out. His left arm throbbed: he knew full well That omen, and his visage fell. Each awful sign the giant viewed, And sudden tears his eye bedewed. Care on his brow sat chill and black, Yet mad with wrath he turned not back. Upon each fearful sight that raised The shuddering hair the chieftain gazed, And laughing in his senseless pride Thus to his giant legions cried: “By sense of mightiest strength upborne, 462 The Sáriká is the Maina, a bird like a starling.
- **Translation**: 

---

