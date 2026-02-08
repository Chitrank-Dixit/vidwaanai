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

### Verse 1 (Ramayana 0.906)
- **Original**: 888 The Ramayana And showed her bleeding face. Canto XIX. The Rousing Of Khara. When Khara saw his sister lie With blood-stained limbs and troubled eye,[252] Wild fury in his bosom woke, And thus the monstrous giant spoke; “Arise, my sister; cast away This numbing terror and dismay, And straight the impious hand declare That marred those features once so fair. For who his finger tip will lay On the black snake in childish play, And unattacked, with idle stroke His poison-laden fang provoke? Ill-fated fool, he little knows Death's noose around his neck he throws, Who rashly met thee, and a draught Of life-destroying poison quaffed. Strong, fierce as death, 'twas thine to choose Thy way at will, each shape to use; In power and might like one of us: What hand has maimed and marred thee thus? What God or fiend this deed has wrought, What bard or sage of lofty thought Was armed with power supremely great Thy form to mar and mutilate? In all the worlds not one I see Would dare a deed to anger me:
- **Translation**: 

---

### Verse 2 (Ramayana 0.907)
- **Original**: Canto XIX. The Rousing Of Khara. 889 Not Indra's self, the Thousand-eyed, Beneath whose hand fierce Páka459 died. My life-destroying darts this day His guilty breath shall rend away, E'en as the thirsty wild swan drains Each milk-drop that the wave retains. Whose blood in foaming streams shall burst O'er the dry ground which lies athirst, When by my shafts transfixed and slain He falls upon the battle plain? From whose dead corpse shall birds of air The mangled flesh and sinews tear, And in their gory feast delight, When I have slain him in the fight? Not God or bard or wandering ghost, No giant of our mighty host Shall step between us, or avail To save the wretch when I assail. Collect each scattered sense, recall Thy troubled thoughts, and tell me all. What wretch attacked thee in the way, And quelled thee in victorious fray?” His breast with burning fury fired, Thus Khara of the fiend inquired: And then with many a tear and sigh Thus ZúrpaGakhá made reply: “'Tis Da[aratha's sons, a pair Strong, resolute, and young, and fair: In coats of dark and blackdeer's hide, And like the radiant lotus eyed: On berries roots and fruit they feed, And lives of saintly virtue lead: 459 A demon slain by Indra.
- **Translation**: 

---

### Verse 3 (Ramayana 0.908)
- **Original**: 890 The Ramayana With ordered senses undefiled, Ráma and LakshmaG are they styled. Fair as the Minstrels' King460 are they, And stamped with signs of regal sway. I know not if the heroes trace Their line from Gods or Dánav461 race. There by these wondering eyes between The noble youths a dame was seen, Fair, blooming, young, with dainty waist, And all her bright apparel graced. For her with ready heart and mind The royal pair their strength combined, And brought me to this last distress, Like some lost woman, comfortless. Perfidious wretch! my soul is fain Her foaming blood and theirs to drain. O let me head the vengeful fight, And with this hand my murderers smite. Come, brother, hasten to fulfil This longing of my eager will. On to the battle! Let me drink Their lifeblood as to earth they sink.” Then Khara, by his sister pressed, Inflamed with fury, gave his hest To twice seven giants of his crew, Fierce as the God of death to view: 460 Chitraratha, King of the Gandharvas. 461 Titanic.
- **Translation**: 

---

### Verse 4 (Ramayana 0.909)
- **Original**: Canto XX. The Giants' Death. 891 'Two men equipped with arms, who wear Deerskin and bark and matted hair, Leading a beauteous dame, have strayed To the wild gloom of DaG ak's shade. These men, this cursed woman slay, And hasten back without delay, That this my sister's lips may be Red with the lifeblood of the three. Giants, my wounded sister longs To take this vengeance for her wrongs. With speed her dearest wish fulfil, And with your might these creatures kill. Soon as your matchless strength shall lay These brothers dead in battle fray, She in triumphant joy will laugh, And their hearts' blood delighted quaff.” The giants heard the words he said, And forth withZúrpaGakhá sped, As mighty clouds in autumn fly Urged by the wind along the sky. Canto XX. The Giants' Death. FierceZúrpaGakhá with her train To Ráma's dwelling came again, And to the eager giants showed Where Sítá and the youths abode. Within the leafy cot they spied The hero by his consort's side, And faithful LakshmaG ready still To wait upon his brother's will. [253]
- **Translation**: 

---

### Verse 5 (Ramayana 0.910)
- **Original**: 892 The Ramayana Then noble Ráma raised his eye And saw the giants standing nigh, And then, as nearer still they pressed. His glorious brother thus addressed, “Be thine a while, my brother dear, To watch o'er Sítá's safety here, And I will slay these creatures who The footsteps of my spouse pursue.” He spoke, and reverent LakshmaG heard Submissive to his brother's word. The son of Raghu, virtuous-souled, Strung his great bow adorned with gold, And, with the weapon in his hand, Addressed him to the giant band: “Ráma and LakshmaG we, who spring From Da[aratha, mighty king; We dwell a while with Sítá here In DaG ak forest wild and drear. On woodland roots and fruit we feed, And lives of strictest rule we lead. Say why would ye our lives oppress Who sojourn in the wilderness. Sent hither by the hermits' prayer With bow and darts unused to spare, For vengeance am I come to slay Your sinful band in battle fray. Rest as ye are: remain content, Nor try the battle's dire event. Unless your offered lives ye spurn, O rovers of the night, return.”
- **Translation**: 

---

### Verse 6 (Ramayana 0.911)
- **Original**: Canto XX. The Giants' Death. 893 They listened while the hero spoke, And fury in each breast awoke. The Bráhman-slayers raised on high Their mighty spears and made reply: They spoke with eyes aglow with ire, While Ráma's burnt with vengeful tire, And answered thus, in fury wild, That peerless chief whose tones were mild: “Nay thou hast angered, overbold, Khara our lord, the mighty-souled, And for thy sin, in battle strife Shalt yield to us thy forfeit life. No power hast thou alone to stand Against the numbers of our band. 'Twere vain to match thy single might Against us in the front of fight. When we equipped for fight advance With brandished pike and mace and lance, Thou, vanquished in the desperate field, Thy bow, thy strength, thy life shalt yield.” With bitter words and threatening mien Thus furious spoke the fierce fourteen, And raising scimitar and spear On Ráma rushed in wild career. Their levelled spears the giant crew Against the matchless hero threw. His bow the son of Raghu bent, And twice seven shafts to meet them sent, And every javelin sundered fell By the bright darts he aimed so well.
- **Translation**: 

---

### Verse 7 (Ramayana 0.912)
- **Original**: 894 The Ramayana The hero saw: his anger grew To fury: from his side he drew Fresh sunbright arrows pointed keen, In number, like his foes, fourteen. His bow he grasped, the string he drew, And gazing on the giant crew, As Indra casts the levin, so Shot forth his arrows at the foe. The hurtling arrows, stained with gore, Through the fiends' breasts a passage tore, And in the earth lay buried deep As serpents through an ant-hill creep Like trees uptorn by stormy blast The shattered fiends to earth were cast, And there with mangled bodies they, Bathed in their blood and breathless, lay. With fainting heart and furious eye The demon saw her champions die. With drying wounds that scarcely bled Back to her brother's home she fled. Oppressed with pain, with loud lament At Khara's feet the monster bent. There like a plant whence slowly come The trickling drops of oozy gum, With her grim features pale with pain She poured her tears in ceaseless rain, There routedZúrpaGakhá lay, And told her brother all, The issue of the bloody fray, Her giant champions' fall.
- **Translation**: 

---

### Verse 8 (Ramayana 0.913)
- **Original**: Canto XXI. The Rousing Of Khara. 895 Canto XXI. The Rousing Of Khara. Low in the dust he saw her lie, And Khara's wrath grew fierce and high. Aloud he cried to her who came Disgracefully with baffled aim: “I sent with thee at thy request The bravest of my giants, best Of all who feed upon the slain: Why art thou weeping here again? Still to their master's interest true, My faithful, noble, loyal crew, Though slaughtered in the bloody fray, Would yet their monarch's word obey. Now I, my sister, fain would know The cause of this thy fear and woe, Why like a snake thou writhest there, Calling for aid in wild despair. Nay, lie not thus in lowly guise: Cast off thy weakness and arise!” With soothing words the giant chief Assuaged the fury of her grief. Her weeping eyes she slowly dried And to her brother thus replied: “I sought thee in my shame and fear With severed nose and mangled ear: My gashes like a river bled, I sought thee and was comforted. [254]
- **Translation**: 

---

### Verse 9 (Ramayana 0.914)
- **Original**: 896 The Ramayana Those twice seven giants, brave and strong, Thou sentest to avenge the wrong, To lay the savage Ráma low, And Lakshma G who misused me so. But ah, the shafts of Ráma through The bodies of my champions flew: Though madly fierce their spears they plied, Beneath his conquering might they died. I saw them, famed for strength and speed, I saw my heroes fall and bleed: Great trembling seized my every limb At the great deed achieved by him. In trouble, horror, doubt, and dread, Again to thee for help I fled. While terror haunts my troubled sight, I seek thee, rover of the night. And canst thou not thy sister free From this wide waste of troublous sea Whose sharks are doubt and terror, where Each wreathing wave is dark despair? Low lie on earth thy giant train By ruthless Ráma's arrows slain, And all the mighty demons, fed On blood, who followed me are dead. Now if within thy breast may be Pity for them and love for me, If thou, O rover of the night, Have valour and with him can fight, Subdue the giants' cruel foe Who dwells where DaG ak's thickets grow. But if thine arm in vain assay This queller of his foes to slay, Now surely here before thine eyes, Wronged and ashamed thy sister dies.
- **Translation**: 

---

### Verse 10 (Ramayana 0.915)
- **Original**: Canto XXII. Khara's Wrath. 897 Too well, alas, too well I see That, strong in war as thou mayst be, Thou canst not in the battle stand When Ráma meets thee hand to hand. Go forth, thou hero but in name, Assuming might thou canst not claim; Call friend and kin, no longer stay: Away from Janasthán, away! Shame of thy race! the weak alone Beneath thine arm may sink o'erthrown: Fly Ráma and his brother: they Are men too strong for thee to slay. How canst thou hope, O weak and base, To make this grove thy dwelling-place? With Ráma's might unmeet to vie, O'ermastered thou wilt quickly die. A hero strong in valorous deed Is Ráma, Da[aratha's seed: And scarce of weaker might than he His brother chief who mangled me.” Thus wept and wailed in deep distress The grim misshapen giantess: Before her brother's feet she lay O'erwhelmed with grief, and swooned away. Canto XXII. Khara's Wrath. Roused by the taunting words she spoke, The mighty Khara's wrath awoke, And there, while giants girt him round, In these fierce words an utterance found:
- **Translation**: 

---

### Verse 11 (Ramayana 0.916)
- **Original**: 898 The Ramayana “I cannot, peerless one, contain Mine anger at this high disdain, Galling as salt when sprinkled o'er The rawness of a bleeding sore. Ráma in little count I hold, Weak man whose days are quickly told. The caitiff with his life to-day For all his evil deeds shall pay. Dry, sister, dry each needless tear, Stint thy lament and banish fear, For Ráma and his brother go This day to Yáma's realm below. My warrior's axe shall stretch him slain, Ere set of sun, upon the plain, Then shall thy sated lips be red With his warm blood in torrents shed.” As Khara's speech the demon heard, With sudden joy her heart was stirred: She fondly praised him as the boast And glory of the giant host. First moved to ire by taunts and stings, Now soothed by gentle flatterings, To DúshaG, who his armies led, The demon Khara spoke, and said: “Friend, from the host of giants call Full fourteen thousand, best of all, Slaves of my will, of fearful might, Who never turn their backs in fight: Fiends who rejoice to slay and mar, Dark as the clouds of autumn are: Make ready quickly, O my friend, My chariot and the bows I bend.
- **Translation**: 

---

### Verse 12 (Ramayana 0.917)
- **Original**: Canto XXII. Khara's Wrath. 899 My swords, my shafts of brilliant sheen, My divers lances long and keen. On to the battle will I lead These heroes of Pulastya's seed, And thus, O famed for warlike skill, Ráma my wicked foeman kill.” He spoke, and ere his speech was done, His chariot glittering like the sun, Yoked and announced, by Dúshan's care, With dappled steeds was ready there. High as a peak from Meru rent It burned with golden ornament: The pole of lazulite, of gold Were the bright wheels whereon it rolled. With gold and moonstone blazoned o'er, Fish, flowers, trees, rocks, the panels bore; Auspicious birds embossed thereon, And stars in costly emblem shone. O'er flashing swords his banner hung, And sweet bells, ever tinkling, swung. [255] That mighty host with sword and shield And oar was ready for the field: And Khara saw, and Dúshan cried, “Forth to the fight, ye giants, ride.” Then banners waved, and shield and sword Flashed as the host obeyed its lord. From Janasthán they sallied out With eager speed, and din, and shout, Armed with the mace for close attacks, The bill, the spear, the battle-axe, Steel quoit and club that flashed afar, Huge bow and sword and scimitar, The dart to pierce, the bolt to strike,
- **Translation**: 

---

### Verse 13 (Ramayana 0.918)
- **Original**: 900 The Ramayana The murderous bludgeon, lance, and pike. So forth from Janasthán, intent On Khara's will, the monsters went. He saw their awful march: not far Behind the host he drove his car. Ware of his master's will, to speed The driver urged each gold-decked steed. Then forth the warrior's coursers sprang, And with tumultuous murmur rang Each distant quarter of the sky And realms that intermediate lie. High and more high within his breast His pride triumphant rose, While terrible as Death he pressed Onward to slay his foes, “More swiftly yet,” as on they fled, He cried in thundering tones Loud as a cloud that overhead Hails down a flood of stones. Canto XXIII. The Omens. As forth upon its errand went That huge ferocious armament, An awful cloud, in dust and gloom, With threatening thunders from its womb Poured in sad augury a flood Of rushing water mixt with blood. The monarch's steeds, though strong and fleet, Stumbled and fell: and yet their feet Passed o'er the bed of flowers that lay
- **Translation**: 

---

### Verse 14 (Ramayana 0.919)
- **Original**: Canto XXIII. The Omens. 901 Fresh gathered on the royal way. No gleam of sunlight struggled through The sombre pall of midnight hue, Edged with a line of bloody red, Like whirling torches overhead. A vulture, fierce, of mighty size. Terrific with his cruel eyes, Perched on the staff enriched with gold, Whence hung the flag in many a fold. Each ravening bird, each beast of prey Where Janasthán's wild thickets lay, Rose with a long discordant cry And gathered as the host went by. And from the south long, wild, and shrill, Came spirit voices boding ill. Like elephants in frantic mood, Vast clouds terrific, sable-hued, Hid all the sky where'er they bore Their load of water mixt with gore. Above, below, around were spread Thick shades of darkness strange and dread, Nor could the wildered glance descry A point or quarter of the sky. Then came o'er heaven a sanguine hue, Though evening's flush not yet was due, While each ill-omened bird that flies Assailed the king with harshest cries. There screamed the vulture and the crane, And the loud jackal shrieked again. Each hideous thing that bodes aright Disaster in the coming fight, With gaping mouth that hissed and flamed, The ruin of the host proclaimed. Eclipse untimely reft away
- **Translation**: 

---

### Verse 15 (Ramayana 0.920)
- **Original**: 902 The Ramayana The brightness of the Lord of Day, And near his side was seen to glow A mace-like comet boding woe. Then while the sun was lost to view A mighty wind arose and blew, And stars like fireflies shed their light, Nor waited for the distant night. The lilies drooped, the brooks were dried, The fish and birds that swam them died, And every tree that was so fair With flower and fruit was stripped and bare. The wild wind ceased, yet, raised on high, Dark clouds of dust involved the sky. In doleful twitter long sustained The restless Sárikás462 complained, And from the heavens with flash and flame Terrific meteors roaring came. Earth to her deep foundation shook With rock and tree and plain and brook, As Khara with triumphant shout, Borne in his chariot, sallied out. His left arm throbbed: he knew full well That omen, and his visage fell. Each awful sign the giant viewed, And sudden tears his eye bedewed. Care on his brow sat chill and black, Yet mad with wrath he turned not back. Upon each fearful sight that raised The shuddering hair the chieftain gazed, And laughing in his senseless pride Thus to his giant legions cried: “By sense of mightiest strength upborne, 462 The Sáriká is the Maina, a bird like a starling.
- **Translation**: 

---

### Verse 16 (Ramayana 0.921)
- **Original**: Canto XXIII. The Omens. 903 These feeble signs I laugh to scorn. I could bring down the stars that shine In heaven with these keen shafts of mine. Impelled by warlike fury I Could cause e'en Death himself to die. [256] I will not seek my home again Until my pointed shafts have slain This Raghu's son so fierce in pride, And Lakshma G by his brother's side. And she, my sister, she for whom These sons of Raghu meet their doom, She with delighted lips shall drain The lifeblood of her foemen slain. Fear not for me: I ne'er have known Defeat, in battle overthrown. Fear not for me, O giants; true Are the proud words I speak to you. The king of Gods who rules on high, If wild Airávat bore him nigh, Should fall before me bolt in hand: And shall these two my wrath withstand!” He ended and the giant host Who heard their chief's triumphant boast, Rejoiced with equal pride elate, Entangled in the noose of Fate. Then met on high in bright array, With eyes that longed to see the fray, God and Gandharva, sage and saint, With beings pure from earthly taint. Blest for good works aforetime wrought, Thus each to other spake his thought: “Now joy to Bráhmans, joy to kine,
- **Translation**: 

---

### Verse 17 (Ramayana 0.922)
- **Original**: 904 The Ramayana And all whom world count half divine! May Raghu's offspring slay in fight Pulastya's sons who roam by night!” In words like these and more, the best Of high-souled saints their hopes expressed, Bending their eager eyes from where Car-borne with Gods they rode in air. Beneath them stretching far, they viewed The giants' death-doomed multitude. They saw where, urged with fury, far Before the host rolled Khara's car, And close beside their leader came Twelve giant peers of might and fame. Four other chiefs463 before the rest Behind their leader DúshaG pressed. Impetuous, cruel, dark, and dread, All thirsting for the fray, The hosts of giant warriors sped Onward upon their way. With eager speed they reached the spot Where dwelt the princely two,— Like planets in a league to blot The sun and moon from view. Canto XXIV. The Host In Sight. 463 Mahákapála, Sthúláksha, Pramátha, Tri[iras.
- **Translation**: 

---

### Verse 18 (Ramayana 0.923)
- **Original**: Canto XXIV. The Host In Sight. 905 While Khara, urged by valiant rage, Drew near that little hermitage, Those wondrous signs in earth and sky Smote on each prince's watchful eye. When Ráma saw those signs of woe Fraught with destruction to the foe, With bold impatience scarce repressed His brother chief he thus addressed: “These fearful signs, my brother bold, Which threaten all our foes, behold: All laden, as they strike the view, With ruin to the fiendish crew. The angry clouds are gathering fast, Their skirts with dusty gloom o'ercast, And harsh with loud-voiced thunder, rain Thick drops of blood upon the plain. See, burning for the coming fight, My shafts with wreaths of smoke are white, And my great bow embossed with gold Throbs eager for the master's hold. Each bird that through the forest flies Sends out its melancholy cries. All signs foretell the dangerous strife, The jeopardy of limb and life. Each sight, each sound gives warning clear That foemen meet and death is near. But courage, valiant brother! well The throbbings of mine arm foretell That ruin waits the hostile powers, And triumph in the fight is ours. I hail the welcome omen: thou Art bright of face and clear of brow. For LakshmaG, when the eye can trace
- **Translation**: 

---

### Verse 19 (Ramayana 0.924)
- **Original**: 906 The Ramayana A cloud upon the warrior's face Stealing the cheerful light away, His life is doomed in battle fray. List, brother, to that awful cry: With shout and roar the fiends draw nigh. With thundering beat of many a drum The savage-hearted giants come. The wise who value safety know To meet, prepared, the coming blow: In paths of prudence trained aright They watch the stroke before it smite. Take thou thine arrows and thy bow, And with the Maithil lady go For shelter to the mountain cave Where thickest trees their branches wave. I will not have thee, LakshmaG, say One word in answer, but obey. By all thy honour for these feet Of mine, dear brother, I entreat. Thy warlike arm, I know could, smite To death these rovers of the night; But I this day would fight alone Till all the fiends be overthrown.”[257] He spake: and LakshmaG answered naught: His arrows and his bow he brought, And then with Sítá following hied For shelter to the mountain side. As LakshmaG and the lady through The forest to the cave withdrew, “'Tis well,” cried Ráma. Then he braced His coat of mail around his waist. When, bright as blazing fire, upon His mighty limbs that armour shone, The hero stood like some great light
- **Translation**: 

---

### Verse 20 (Ramayana 0.925)
- **Original**: Canto XXIV. The Host In Sight. 907 Uprising in the dark of night. His dreadful shafts were by his side; His trusty bow he bent and plied, Prepared he stood: the bowstring rang, Filling the welkin with the clang. The high-souled Gods together drew The wonder of the fight to view, The saints made free from spot and stain, And bright Gandharvas' heavenly train. Each glorious sage the assembly sought, Each saint divine of loftiest thought, And filled with zeal for Ráma's sake. Thus they whose deeds were holy spake: “Now be it well with Bráhmans, now Well with the worlds and every cow! Let Ráma in the deadly fray The fiends who walk in darkness slay, As He who bears the discus464 slew The chieftains of the Asur crew.” Then each with anxious glances viewed His fellow and his speech renewed: “There twice seven thousand giants stand With impious heart and cruel hand: Here Ráma stands, by virtue known: How can the hero fight alone?” 464 VishGu, who bears achakraor discus.
- **Translation**: 

---

