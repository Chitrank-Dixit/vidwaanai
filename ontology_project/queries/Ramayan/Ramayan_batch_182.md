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

### Verse 1 (Ramayana 0.1666)
- **Original**: 1648 The Ramayana Then raged the battle fiercer yet When Angad and the giant met. A hundred thousand arrows, hot With flames of fire, the giant shot; And every shaft he deftly sent His foeman's body pierced and rent. From Angad's limbs ran floods of gore: A stately tree from earth he tore, Which, maddened as his gashes bled, He hurled at his opponent's head. His bow the dauntless giant drew; To meet the tree swift arrows flew, Checked the huge missile's onward way, And harmless on the earth it lay. A while the Vánar chieftain gazed, Then from the earth a rock he raised Rent from a thunder-splitten height, And cast it with resistless might. The giant marked, and, mace in hand, Leapt from his chariot to the sand, Ere the rough mass descending broke The seat, the wheel, the pole and yoke. Then Angad seized a shattered hill, Whereon the trees were flowering still, And with full force the jagged peak Fell crashing on the giant's cheek. He staggered, reeled, and fell: the blood Gushed from the giant in a flood. Reft of his might, each sense astray, A while upon the sand he lay. But strength and wandering sense returned Again his eyes with fury burned, And with his mace upraised on high
- **Translation**: 

---

### Verse 2 (Ramayana 0.1667)
- **Original**: Canto LIV. Vajradanshtra's Death. 1649 He wounded Angad on the thigh. Then from his hand his mace he threw, And closer to his foeman drew. Then with their fists they fought, and smote On brow and cheek and chest and throat. Worn out with toil, their limbs bedewed, With blood, the strife they still renewed, Like Mercury and fiery Mars Met in fierce battle mid the stars. A while the deadly fight was stayed: Each armed him with his trusty blade Whose sheath with tinkling bells supplied, And golden net, adorned his side; And grasped his ponderous leather shield To fight till one should fall or yield. Unnumbered wounds they gave and took: Their wearied bodies reeled and shook. At length upon the sand that drank Streams of their blood the warriors sank, But as a serpent rears his head Sore wounded by a peasant's tread, So Angad, fallen on his knees, Yet gathered strength his sword to seize; And, severed by the glittering blade, The giant's head on earth was laid. [I omit Cantos LV, LVI, LVII, and LVIII, which relate how Akampan and Prahasta sally out and fall. There is little novelty of incident in these Cantos and the results are exactly the same as before. In Canto LV, Akampan, at the command of RávaG, leads forth his troops. Evil omens are seen and heard. The enemies meet, and many fall on each side, the Vánars transfixed with arrows, the Rákshases crushed with rocks and trees.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1668)
- **Original**: 1650 The Ramayana In Canto LVI Akampan sees that the Rákshases are worsted, and fights with redoubled rage and vigour. The Vánars fall fast under his“nets of arrows.” Hanumán comes to the rescue. He throws mountain peaks at the giant which are dexterously stopped with flights of arrows; and at last beats him down and kills him with a tree. In Canto LVII, RávaG is seriously alarmed. He declares that he himself, KumbhakarGa or Prahasta, must go forth. Prahasta sallies out vaunting that the fowls of the air shall eat their fill of Vánar flesh. In Canto LVIII, the two armies meet. Dire is the conflict; ceaseless is the rain of stones and arrows. At last Níla meets Prahasta and breaks his bow. Prahasta leaps from his car, and the giant and the Vánar fight on foot. Níla with a huge tree crushes his opponent who falls like a tree when its roots are cut.] [468] Canto LIX. Rávan's Sally. They told him that the chief was killed, And RávaG's breast with rage was filled. Then, fiercely moved by wrath and pride, Thus to his lords the tyrant cried: “No longer, nobles, may we show This lofty scorn for such a foe By whom our bravest, with his train Of steeds and elephants, is slain. Myself this day will take the field, And Raghu's sons their lives shall yield.”
- **Translation**: 

---

### Verse 4 (Ramayana 0.1669)
- **Original**: Canto LIX. Rávan's Sally. 1651 High on the royal car, that glowed With glory from his face, he rode; And tambour shell and drum pealed out, And joyful was each giant's shout. A mighty host, with eyeballs red Like flames of kindled fire, he led. He passed the city gate, and viewed, Arrayed, the Vánar multitude, Those wielding massy rocks, and these Armed with the stems of uptorn trees, And Ráma with his eyes aglow With warlike ardour viewed the foe, And thus the brave VibhishaG, best Of weapon-wielding chiefs, addressed: “What captain leads this bright array Where lances gleam and banners play, And thousands armed with spear and sword Await the bidding of their lord?” “Seest, thou,” VibhishaG answered,“one Whose face is as the morning sun, Preëminent for hugest frame? Akampan 962 is the giant's name. Behold that chieftain, chariot-borne, Whom Brahmá's chosen gifts adorn. He wields a bow like Indra's own; A lion on his flag is shown, His eyes with baleful fire are lit: 'Tis RávaG's son, 'tis Indrajít. There, brandishing in mighty hands His huge bow, Atikáya stands. And that proud warrior o'er whose head 962 “It is to be understood,” says the commentator,“that this is not the Akampan who has already been slain.”
- **Translation**: 

---

### Verse 5 (Ramayana 0.1670)
- **Original**: 1652 The Ramayana A moon-bright canopy is spread: Whose might, in many a battle tried, Has tamed imperial Indra's pride; Who wears a crown of burnished gold, Is Lanká's lord the lofty-souled.” He ceased: and Ráma knew his foe, And laid an arrow on his bow: “Woe to the wretch,” he cried,“whom fate Abandons to my deadly hate.” He spoke, and, firm by LakshmaG's side, The giant to the fray defied. The lord of Lanká bade his train Of warriors by the gates remain, To guard the city from surprise By Ráma's forest born allies. Then as some monster of the sea Cleaves swift-advancing billows, he Charged with impetuous onset through The foe, and cleft the host in two. Sugríva ran, the king to meet: A hill uprooted from its seat He hurled, with trees that graced the height Against the rover of the night: But cleft with shafts that checked its way Harmless upon the earth it lay. Then fiercer RávaG's fury grew, An arrow from his side he drew, Swift as a thunderbolt, aglow With fire, and launched it at the foe. Through flesh and bone a way it found, And stretched Sugríva on the ground. SusheG and Nala saw him fall, Gaváksha, Gavaya heard their call,
- **Translation**: 

---

### Verse 6 (Ramayana 0.1671)
- **Original**: Canto LIX. Rávan's Sally. 1653 And, poising hills, in act to fling They charged amain the giant king. They charged, they hurled the hills in vain, He checked them with his arrowy rain, And every brave assailant felt The piercing wounds his missiles dealt, Then smitten by the shafts that came Keen, fleet, and thick, with certain aim, They fled to Ráma, sure defence Against the oppressor's violence, Then, reverent palm to palm applied, Thus LakshmaG to his brother cried: “To me, my lord, the task entrust To lay this giant in the dust.” “Go, then,” said Ráma,“bravely fight; Beat down this rover of the night. But he, unmatched in bold emprise, Fears not the Lord of earth and skies, Keep on thy guard: with keenest eye Thy moments of attack espy. Let hand and eye in due accord Protect thee with the bow and sword.” Then LakshmaG round his brother threw His mighty arms in honour due, Bent lowly down his reverent head, And onward to the battle sped. Hanúmán from afar beheld How Ráva G's shafts the Vánars quelled: To meet the giant's car he ran, Raised his right arm and thus began: “If Brahmá's boon thy life has screened From Yaksha, God, Gandharva, fiend, With these contending fear no ill,
- **Translation**: 

---

### Verse 7 (Ramayana 0.1672)
- **Original**: 1654 The Ramayana But tremble at a Vánar still.” With fury flashing from his eye The lord of Lanká made reply: “Strike, Vánar, strike: the fray begin, And hope eternal fame to win. This arm shall prove thee in the strife[469] And end thy glory and thy life.” “Remember, ” cried the Wind-God's son, “Remember all that I have done, My prowess, King, thou knowest well, Shown in the fight when Aksha963 fell.” With heavy hand the giant smote Hanúmán on the chest and throat, Who reeled and staggered to and fro, Stunned for a moment by the blow. Till, mustering strength, his hand he reared And struck the foe whom Indra feared. His huge limbs bent beneath the shock, As mountains, in an earthquake, rock, And from the Gods and sages pealed Shouts of loud triumph as he reeled. But strength returning nerved his frame: His eyeballs flashed with fiercer flame. No living creature might resist That blow of his tremendous fist Which fell upon Hanúmán's flank: And to the ground the Vánar sank, No sign of life his body showed: And RávaG in his chariot rode At Níla; and his arrowy rain Fell on the captain and his train. Fierce Níla stayed his Vánar band, 963 RávaG's son, whom Hanumán killed when he first visited Lanká.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1673)
- **Original**: Canto LIX. Rávan's Sally. 1655 And, heaving with his single hand A mountain peak, with vigorous swing Hurled the huge missile at the king. Hanúmán life and strength regained, Burned for the fight and thus complained: “Why, coward giant, didst thou flee And leave the doubtful fight with me?” Seven mighty arrows keen and fleet The giant launched, the hill to meet; And, all its force and fury stayed, The harmless mass on earth was laid. Enraged the Vánar chief beheld The mountain peak by force repelled, And rained upon the foe a shower Of trees uptorn with branch and flower. Still his keen shafts which pierced and rent Each flying tree the giant sent: Still was the Vánar doomed to feel The tempest of the winged steel. Then, smarting from that arrowy storm, The Vánar chief condensed his form,964 And lightly leaping from the ground On RávaG's standard footing found; Then springing unimpeded down Stood on his bow and golden crown. The Vánar's nimble leaps amazed Ikshváku's son who stood and gazed. The giant, raging in his heart, Laid on his bow a fiery dart; The Vánar on his flagstaff eyed, And thus in tones of fury cried: 964 Níla was the son of Agni the God of Fire, and possessed, like Milton's demons, the power of dilating and condensing his form at pleasure.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1674)
- **Original**: 1656 The Ramayana “Well skilled in magic lore art thou: But will thine art avail thee now? See if thy magic will defend Thy life against the dart I send.” Thus RávaG spake, the giant king, And loosed the arrow from the string. It pierced, with direst fury sped, The Vánar with its flaming head. His father's might, his power innate Preserved him from the threatened fate. Upon his knees he fell, distained With streams of blood, but life remained. Still RávaG for the battle burned: At LakshmaG next his car he turned, And charged amain with furious show, Straining in mighty hands his bow. “Come, ” Lakshma G cried,“assay the fight: Leave foes unworthy of thy might.” Thus LakshmaG spoke: and Lanká's lord Heard the dread thunder of the cord. And mad with burning rage and pride In hasty words like these replied: “Joy, joy is mine, O Raghu's son: Thy fate to-day thou canst not shun. Slain by mine arrows thou shalt tread The gloomy pathway of the dead.”
- **Translation**: 

---

### Verse 10 (Ramayana 0.1675)
- **Original**: Canto LIX. Rávan's Sally. 1657 Thus as he spoke his bow he drew, And seven keen shafts at LakshmaG flew, But Raghu's son with surest aim Cleft every arrow as it came. Thus with fleet shafts each warrior shot Against his foe, and rested not. Then one choice weapon from his store, By Brahmá's self bestowed of yore, Fierce as the flames that end the world, The giant king at LakshmaG hurled. The hero fell, and racked with pain, Scarce could his hand his bow retain. But sense and strength resumed their seat And, lightly springing to his feet, He struck with one tremendous stroke And RávaG's bow in splinters broke. From LakshmaG's cord three arrows flew And pierced the giant monarch through. Sore wounded RávaG closed, and round Ikshváku's son his strong arms wound. With strength unrivalled, Brahmá's gift, He strove from earth his foe to lift. “Shall I,” he cried,“who overthrow Mount Meru and the Lord of Snow, And heaven and all who dwell therein, Be foiled by one of Ráma's kin?” But though he heaved, and toiled, and strained, Unmoved Ikshváku's son remained. His frame by those huge arms compressed The giant's God-given force confessed, But conscious that himself was part [470] Of VishGu, he was firm in heart.
- **Translation**: 

---

### Verse 11 (Ramayana 0.1676)
- **Original**: 1658 The Ramayana The Wind-God's son the fight beheld, And rushed at RávaG, rage-impelled. Down crashed his mighty hand; the foe Full in the chest received the blow. His eyes grew dim, his knees gave way, And senseless on the earth he lay. The Wind-God's son to Ráma bore Deep-wounded LakshmaG stained with gore. He whom no foe might lift or bend Was light as air to such a friend. The dart that LakshmaG's side had cleft, Untouched, the hero's body left, And flashing through the air afar Resumed its place in RávaG's car; And, waxing well though wounded sore, He felt the deadly pain no more. And RávaG, though with deep wounds pained, Slowly his sense and strength regained, And furious still and undismayed On bow and shaft his hand he laid. Then Hanumán to Ráma cried: “Ascend my back, great chief, and ride Like VishGu borne on Garu 's wing, To battle with the giant king.” So, burning for the dire attack, Rode Ráma on the Vánar's back, And with fierce accents loud and slow Thus gave defiance to the foe, While his strained bowstring made a sound Like thunder when it shakes the ground: “Stay, Monarch of the giants, stay, The penalty of sin to pay.
- **Translation**: 

---

### Verse 12 (Ramayana 0.1677)
- **Original**: Canto LIX. Rávan's Sally. 1659 Stay! whither wilt thou fly, and how Escape the death that waits thee now?” No word the giant king returned: His eyes with flames of fury burned. His arm was stretched, his bow was bent, And swift his fiery shafts were sent. Red torrents from the Vánar flowed: Then Ráma near to RávaG strode, And with keen darts that never failed, The chariot of the king assailed. With surest aim his arrows flew: The driver and the steeds he slew. And shattered with the pointed steel Car, flag, and pole and yoke and wheel. As Indra hurls his bolt to smite Mount Meru's heaven-ascending height, So Ráma with a flaming dart Struck Lanká's monarch near the heart, Who reeled and fell beneath the blow And from loose fingers dropped his bow. Bright as the sun, with crescent head, From Ráma's bow an arrow sped, And from his forehead, proud no more, Cleft the bright coronet he wore. Then Ráma stood by RávaG's side And to the conquered giant cried: “Well hast thou fought: thine arm has slain Strong heroes of the Vánar train. I will not strike or slay thee now, For weary, faint with fight art thou. To Lanká's town thy footsteps bend, And there the night securely spend. To-morrow come with car and bow,
- **Translation**: 

---

### Verse 13 (Ramayana 0.1678)
- **Original**: 1660 The Ramayana And then my prowess shalt thou know.” He ceased: the king in humbled pride Rose from the earth and naught replied. With wounded limbs and shattered crown He sought again his royal town. Canto LX. Kumbhakarna Roused. With humbled heart and broken pride Through Lanká's gate the giant hied, Crushed, like an elephant beneath A lion's spring and murderous teeth, Or like a serpent 'neath the wing And talons of the Feathered King. Such was the giant's wild alarm At arrows shot by Ráma's arm; Shafts with red lightning round them curled, Like Brahmá's bolts that end the world.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1679)
- **Original**: Canto LX. Kumbhakarna Roused. 1661 Supported on his golden throne, With failing eye and humbled tone, “Giants,” he cried,“the toil is vain, Fruitless the penance and the pain, If I whom Indra owned his peer, Secure from Gods, a mortal fear. My soul remembers, now too late, Lord Brahmá's words who spoke my fate: “Tremble, proud Giant,” thus they ran, “And dread thy death from slighted man. Secure from Gods and demons live, And serpents, by the boon I give. Against their power thy life is charmed, But against man is still unarmed.” This Ráma is the man foretold By AnaraGya's965 lips of old: “Fear, RávaG, basest of the base: For of mine own imperial race A prince in after time shall spring And thee and thine to ruin bring. And Vedavatí,966 ere she died Slain by my ruthless insult, cried: [471] “A scion of my royal line Shall slay, vile wretch, both thee and thine.” She in a later birth became King Janak's child, now Ráma's dame. 965 An ancient king of Ayodhyá said by some to have been Prithu's father. 966 The daughter of King Ku[adhwaja. She became an ascetic, and being insulted by RávaG in the woods where she was performing penance, destroyed herself by entering fire, but was born again as Sítá to be in turn the destruction of him who had insulted her.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1680)
- **Original**: 1662 The Ramayana Nandí[vara967 foretold this fate, And Umá 968 when I moved her hate, And Rambhá,969 and the lovely child Of VaruG970 by my touch defiled. I know the fated hour is nigh: Hence, captains, to your stations fly. Let warders on the rampart stand: Place at each gate a watchful band; And, terror of immortal eyes, Let mightiest KumbhakarGa rise. He, slumbering, free from care and pain, By Brahmá's curse, for months has lain. But when Prahasta's death he hears, Mine own defeat and doubts and fears, The chief will rise to smite the foe And his unrivalled valour show. Then Raghu's royal sons and all The Vánars neath his might will fall.” The giant lords his hest obeyed, They left him, trembling and afraid, And from the royal palace strode To KumbhakarGa's vast abode. They carried garlands sweet and fresh, And reeking loads of blood and flesh. 967 Nandí[vara wasZiva's chief attendant. RávaG had despised and laughed at him for appearing in the form of a monkey and the irritated Nandí[vara cursed him and foretold his destruction by monkeys. 968 RávaG once upheaved and shook Mount Kailása the favourite dwelling place ofZiva the consort of Umá, and was cursed in consequence by the offended Goddess. 969 Rambhá, who has several times been mentioned in the course of the poem, was one of the nymphs of heaven, and had been insulted by RávaG. 970 Punjikasthalá was the daughter of VaruG. RávaG himself has mentioned in this book his insult to her, and the curse pronounced in consequence by Brahmá.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1681)
- **Original**: Canto LX. Kumbhakarna Roused. 1663 They reached the dwelling where he lay, A cave that reached a league each way, Sweet with fair blooms of lovely scent And bright with golden ornament. His breathings came so fierce and fast, Scarce could the giants brook the blast. They found him on a golden bed With his huge limbs at length outspread. They piled their heaps of venison near, Fat buffaloes and boars and deer. With wreaths of flowers they fanned his face, And incense sweetened all the place. Each raised his mighty voice as loud As thunders of an angry cloud, And conchs their stirring summons gave That echoed through the giant's cave. Then on his breast they rained their blows, And high the wild commotion rose When cymbal vied with drum and horn. And war cries on the gale upborne. Through all the air loud discord spread, And, struck with fear, the birds fell dead. But still he slept and took his rest. Then dashed they on his shaggy chest Clubs, maces, fragments of the rock: He moved not once, nor felt the shock. The giants made one effort more With shell and drum and shout and roar. Club, mallet, mace, in fury plied, Rained blows upon his breast and side. And elephants were urged to aid, And camels groaned and horses neighed. They drenched him with a hundred pails, They tore his ears with teeth and nails.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1682)
- **Original**: 1664 The Ramayana They bound together many a mace And beat him on the head and face; And elephants with ponderous tread Stamped on his limbs and chest and head. The unusual weight his slumber broke: He started, shook his sides, and woke; And, heedless of the wounds and blows, Yawning with thirst and hunger rose, His jaws like hell gaped fierce and wide, Dire as the flame neath ocean's tide. Red as the sun on Meru's crest The giant's face his wrath expressed, And every burning breath he drew Was like the blast that rushes through The mountain cedars. Up he raised His awful head with eyes that blazed Like comets, dire as Death in form Who threats the worlds with fire and storm. The giants pointed to their stores Of buffaloes and deer and boars, And straight he gorged him with a flood Of wine, with marrow, flesh, and blood. He ceased: the giants ventured near And bent their lowly heads in fear. Then Kumbhakar[n.]a glared with eyes Still heavy in their first surprise, Still drowsy from his troubled rest, And thus the giant band addressed. “How have ye dared my sleep to break? No trifling cause should bid me wake. Say, is all well? or tell the need That drives you with unruly speed To wake me. Mark the words I say, The king shall tremble in dismay,[472]
- **Translation**: 

---

### Verse 18 (Ramayana 0.1683)
- **Original**: Canto LX. Kumbhakarna Roused. 1665 The fire be quenched and Indra slain Ere ye shall break my rest in vain.” Yúpáksha answered:“Chieftain, hear; No God or fiend excites our fear. But men in arms our walls assail: We tremble lest their might prevail. For vengeful Ráma vows to slay The foe who stole his queen away, And, matchless for his warlike deeds, A host of mighty Vánars leads. Ere now a monstrous Vánar came, Laid Lanká waste with ruthless flame, And Aksha, RávaG's offspring, slew With all his warrior retinue. Our king who never trembled yet For heavenly hosts in battle met, At length the general dread has shared, O'erthrown by Ráma's arm and spared.” He ceased: and KumbhakarGa spake: “I will go forth and vengeance take; Will tread their hosts beneath my feet, Then triumph-flushed our king will meet. Our giant bands shall eat their fill Of Vánars whom this arm shall kill. The princes' blood shall be my draught, The chieftains' shall by you be quaffed.” He spake, and, with an eager stride That shook the earth, to RávaG hied.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1684)
- **Original**: 1666 The Ramayana Canto LXI. The Vánars' Alarm. The son of Raghu near the wall Saw, proudly towering over all, The mighty giant stride along Attended by the warrior throng; Heard KumbhakarGa's heavy feet Awake the echoes of the street; And, with the lust of battle fired, Turned to VibhishaG and inquired: “VibhishaG, tell that chieftain's name Who rears so high his mountain frame; With glittering helm and lion eyes, Preëminent in might and size Above the rest of giant birth, He towers the standard of the earth; And all the Vánars when they see The mighty warrior turn and flee.” “In him,” VibhishaG answered,“know Vi[ravas' son, the Immortals' foe, Fierce KumbhakarGa, mightier far Than Gods and fiends and giants are. He conquered Yáma in the fight, And Indra trembling owned his might. His arm the Gods and fiends subdued, Gandharvas and the serpent brood. The rest of his gigantic race Are wondrous strong by God-giving grace; But nature at his birth to him Gave matchless power and strength of limb. Scarce was he born, fierce monster, when He killed and ate a thousand men. The trembling race of men, appalled,
- **Translation**: 

---

### Verse 20 (Ramayana 0.1685)
- **Original**: Canto LXI. The Vánars' Alarm. 1667 On Indra for protection called; And he, to save the suffering world, His bolt at KumbhakarGa hurled. So awful was the monster's yell That fear on all the nations fell, He, rushing on with furious roar, A tusk from huge Airávat tore, And dealt the God so dire a blow That Indra reeling left his foe, And with the Gods and mortals fled To Brahmá's throne dispirited. “O Brahmá,” thus the suppliants cried, “Some refuge for this woe provide. If thus his maw the giant sate Soon will the world be desolate.” The Self-existent calmed their woe, And spake in anger to their foe: “As thou wast born, Pulastya's son, That worlds might weep by thee undone, Thou like the dead henceforth shalt be: Such is the curse I lay on thee.” Senseless he lay, nor spoke nor stirred; Such was the power of Brahmá's word. But RávaG, troubled for his sake, Thus to the Self-existent spake: “Who lops the tree his care has reared When golden fruit has first appeared? Not thus, O Brahmá, deal with one Descended from thine own dear son.971 Still thou, O Lord, thy word must keep, He may not die, but let him sleep. Yet fix a time for him to break 971 Pulastya was the son of Brahmá and father of Vi[ravas or Paulastya the father of RávaG and KumbhakarGa.
- **Translation**: 

---

