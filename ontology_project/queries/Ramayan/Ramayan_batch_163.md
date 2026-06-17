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

### Verse 1 (Ramayana 0.1286)
- **Original**: 1268 The Ramayana Brave brother, let us here remain Throughout the season of the rain. For in mine eyes this mountain crest Is above all, the loveliest. Where copper-hued and black and white Show the huge blocks that face the height; Where gleams the shine of varied ore, Where dark clouds hang and torrents roar; Where waving woods are fair to see, And creepers climb from tree to tree; Where the gay peacock's voice is shrill, And sweet birds carol on the hill; Where odorous breath is wafted far From Jessamine and Sinduvár;617 And opening flowers of every hue Give wondrous beauty to the view. See, too, this pleasant water near Our cavern home is fresh and clear; And lilies gay with flower and bud Are glorious on the lovely flood. This cave that fares north and east Will shelter us till rain has ceased; And towering hills that rise behind Will screen us from the furious wind. Close by the cavern's portal lies And level stone of ample size And sable hue, a mighty block Long severed from the parent rock. Now let thine eye bent northward rest A while upon that mountain crest, High as a cloud that brings the rain, And dark as iron rent in twain. 617 Vitex Negundo.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1287)
- **Original**: Canto XXVII. Ráma On The Hill. 1269 Look southward, brother, now and view A cloudy pile of paler hue Like Mount Kailása's topmost height Where ores of every tint are bright. See, Lakshman, see before our cave That clear brook eastward roll its wave As though 'twere Gangá's infant rill Down streaming from the three-peaked hill. See, by the water's gentle flow A [oka, sál, and sandal grow. And every lovely tree most fair With leaf and bud and flower is there. See there, beneath the bending trees That fringe her bank, the river flees, Clothed with their beauty like a maid In all her robes and gems arrayed, While from the sedgy banks are heard The soft notes of each amorous bird. O see what lovely islets stud Like gems the bosom of the flood, And sárases and wild swans crowd About her till she laughs aloud. See, lotus blooms the brook o'erspread, Some tender blue, some dazzling red, And opening lilies white as snow Their buds in rich profusion show. There rings the joyous peacock's scream, There stands the curlew by the stream, And holy hermits love to throng Where the sweet waters speed along. Ranged on the grassy margin shine Gay sandal trees in glittering line, And all the wondrous verdure seems The offspring of creative dreams.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1288)
- **Original**: 1270 The Ramayana O conquering Prince, there cannot be A lovelier place than this we see. Here sheltered on the beauteous height Our days will pass in calm delight. Nor is Kishkindhá's city, gay With grove and garden, far away. Thence will the breeze of evening bring Sweet music as the minstrels sing; And, when the Vánars dance, will come The sound of tabour and of drum. Again to spouse and realm restored, Girt by his friends, the Vánar lord Great glory has acquired; and how Can he be less than happy now?” This said, the son of Raghu made His dwelling in that pleasant shade Upon the mountain's shelving side That sweetly all his wants supplied. But still the hero's troubled mind No comfort in his woe could find, Yet mourning for his stolen wife Dearer to Ráma than his life, Chief when he saw the Lord of Night Rise slowly o'er the eastern height,[358] He tossed upon his leafy bed With eyes by sleep unvisited. Outwelled the tears in ceaseless flow, And every sense was numbed by woe. Each pang that pierced the mourner through Smote LakshmaG's faithful bosom too, Who, troubled for his brother's sake, With wisest words the prince bespake: “Arise, my brother, and be strong:
- **Translation**: 

---

### Verse 4 (Ramayana 0.1289)
- **Original**: Canto XXVII. Ráma On The Hill. 1271 Thy hero heart has mourned too long. Thou knowest well that tears and sighs Will mar the mightiest enterprise. Thine was the soul that loved to dare: To serve the Gods was still thy care; And ne'er may sorrow's sting subdue A heart so resolute and true. How canst thou hope to slay in fight The giant cruel in his might? Unwearied must the champion be Who strives with such a foe as he. Tear out this sorrow by the root; Again be bold and resolute. Arise, my brother, and subdue The demon and his wicked crew. Thou canst destroy the earth, her seas, Her rooted hills and giant trees Unseated by thy furious hand: And shall one fiend thy power withstand? Wait through this season of the rain Till suns of autumn dry the plain, Then shall thy giant foe, and all His host and realm, before thee fall. I wake thy valour that has slept Amid the tears thine eyes have wept; As drops of oil in worship raise The dormant flame to sudden blaze.” The son of Raghu heard: he knew His brother's rede was wise and true; And, honouring his friendly guide, In gentle words he thus replied: “Whate'er a hero firm and bold, Devoted, true, and lofty-souled
- **Translation**: 

---

### Verse 5 (Ramayana 0.1290)
- **Original**: 1272 The Ramayana Should speak by deep affection led, Such are the words which thou hast said. I cast away each pensive thought That brings the noblest plans to naught, And each uninjured power will strain Until the purposed end we gain. Thy prudent words will I obey, And till the close of rain-time stay, When King Sugríva will invite To action, and the streams be bright. The hero saved in hour of need Repays the debt with friendly deed: But hated by the good are they Who take the boon and ne'er repay.” Canto XXVIII. The Rains. “See, brother, see” thus Ráma cried On Mályavat's618 dark-wooded side, “A chain of clouds, like lofty hills, The sky with gathering shadow fills. Nine months those clouds have borne the load Conceived from sunbeams as they glowed, And, having drunk the seas, give birth, And drop their offspring on the earth. Easy it seems at such a time That flight of cloudy stairs to climb, 618 Mályavat:“The name of this mountain appears to me to be erroneous, and I think that instead of Mályavat should be read Malayavat, Malaya is a group of mountains situated exactly in that southern part of India where Ráma now was, while Mályavat is placed to the north east.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 6 (Ramayana 0.1291)
- **Original**: Canto XXVIII. The Rains. 1273 And, from their summit, safely won, Hang flowery wreaths about the sun. See how the flash of evening's red Fringes the fleecy clouds o'erhead Till all the sky is streaked and lined With bleeding wounds incarnadined, Or the wide firmament above Shows like a lover sick with love And, pale with cloudlets, heaves a sigh In the soft breeze that wanders by. See, by the fervent heat embrowned, How drenched with recent showers, the ground Pours out in floods her gushing tears, Like Sítá wild with torturing fears. So softly blows this cloud-born breeze Cool through the boughs of camphor trees That one might hold it in the cup Of hollowed hands and drink it up. See, brother, where that rocky steep, Where odorous shrubs in rain-drops weep, Shows like Sugríva when they shed Tne royal balm upon his head. Like students at their task appear These hills whose misty peaks are near: Black deerskin619 garments wrought of cloud Their forms with fitting mantles shroud, Each torrent from the summit poured Supplies the place of sacred cord.620 And winds that in their caverns moan [359] 619 Mantles of the skin of the black antelope were the prescribed dress of ascetics and religious students. 620 The sacred cord worn as the badge of religious initiation by men of the three twice-born castes.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1292)
- **Original**: 1274 The Ramayana Sound like the voice's undertone.621 From east to west red lightnings flash, And, quivering neath the golden lash, The great sky like a generous steed Groans inly at each call to speed. Yon lightning, as it flashes through The giant cloud of sable hue, Recalls my votaress Sítá pressed Mid struggles to the demon's breast. See, on those mountain ridges stand Sweet shrubs that bud and bloom expand. The soft rain ends their pangs of grief, And drops its pearls on flower and leaf. But all their raptures stab me through And wake my pining love anew.622 Now through the air no wild bird flies, Each lily shuts her weary eyes; And blooms of opening jasmin show The parting sun has ceased to glow. No captain now for conquest burns, But homeward with his host returns; For roads and kings' ambitious dreams Have vanished neath descending streams. This is the watery month623 wherein 621 The hum with which students conduct their tasks. 622 I omit here a long general description of the rainy season which is not found in the Bengal recension and appears to have been interpolated by a far inferior and much later hand than Valmiki's. It is composed in a metre different from that of the rest of the Canto, and contains figures of poetical rhetoric and common-places which are the delight of more recent poets. 623 Praushthapada or Bhadra, the modern Bhadon, corresponds to half of August and half of September.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1293)
- **Original**: Canto XXVIII. The Rains. 1275 The Sámar's624 sacred chants begin. Áshádha625 past, now Ko[al's lord626 The harvest of the spring has stored,627 And dwells within his palace freed From every care of pressing need. Full is the moon, and fierce and strong Impetuous Sarjú628 roars along As though Ayodhyá's crowds ran out To greet their king with echoing shout. In this sweet time of ease and rest No care disturbs Sugríva's breast, The foe that marred his peace o'erthrown, And queen and realm once more his own. Alas, a harder fate is mine, Reft both of realm and queen to pine, And, like the bank which floods erode, I sink beneath my sorrow's load. Sore on my soul my miseries weigh, And these long rains our action stay, While Rávan seems a mightier foe Than I dare hope to overthrow. I saw the roads were barred by rain, I knew the hopes of war were vain; Nor could I bid Sugríva rise, Though prompt to aid my enterprise. E'en now I scarce can urge my friend 624 The Sáman or Sáma-veda, the third of the four Vedas, is really merely a reproduction of parts of the Rig-veda, transposed and scattered about piece- meal, only 78 verses in the whole being, it is said, untraceable to the present recension of the Rig-veda. 625 Áshádha is the month corresponding to parts of June and July. 626 Bharat, who was regent during Ráma's absence. 627 Or with Gorresio, following the gloss of another commentary:“Has com- pleted every holy rite and accumulated stores of merit.” 628 The river on which Ayodhyá was built.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1294)
- **Original**: 1276 The Ramayana On whom his house and realm depend, Who, after toil and peril past, Is happy with his queen at last. Sugríva after rest will know The hour is come to strike the blow, Nor will his grateful soul forget My succour, or deny the debt I know his generous heart, and hence Await the time with confidence When he his friendly zeal will show, And brooks again untroubled flow.”629 Canto XXIX. Hanumán's Counsel. No flash of lightning lit the sky, No cloudlet marred the blue on high. The Saras630 missed the welcome rain, The moon's full beams were bright again. Sugríva, lapped in bliss, forgot The claims of faith, or heeded not; And by alluring joys misled The path of falsehood learned to tread. In careless ease he passed each hour, And dallied in his lady's bower. Each longing of his heart was stilled, And every lofty hope fulfilled. With royal Rumá by his side, Or Tárá yet a dearer bride,[360] 629 I omit a[lokaor four lines on gratitude and ingratitude repeated word for word from the last Canto. 630 The Indian crane; a magnificent bird easily domesticated.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1295)
- **Original**: Canto XXIX. Hanumán's Counsel. 1277 He spent each joyous day and night In revelry and wild delight, Like Indra whom the nymphs entice To taste the joys of Paradise. The power to courtiers' hands resigned, To all their acts his eyes were blind. All doubt, all fear he cast aside And lived with pleasure for his guide. But sage Hanúmán, firm and true, Whose heart the lore of Scripture knew, Well trained to meet occasion, trained In all by duty's law ordained, Strove with his prudent speech to find Soft access to the monarch's mind. He, skilled in every gentle art Of eloquence that wins the heart, Sugríva from his trance to wake, His salutary counsel spake: “The realm is won, thy name advanced, The glory of thy house enhanced, And now thy foremost care should be To aid the friends who succoured thee. He who is firm and faithful found To friendly ties in honour bound, Will see his name and fame increase And his blest kingdom thrive in peace. Wide sway is his who truly boasts That friends and treasure, self and hosts, All blent in one harmonious whole, Are subject to his firm control. Do thou, whose footsteps never stray From the clear bounds of duty's way, Assist, as honour bids thee, now
- **Translation**: 

---

### Verse 11 (Ramayana 0.1296)
- **Original**: 1278 The Ramayana Thy friends, observant of thy vow. For if all cares we lay not by, And to our friend's assistance fly, We, after, toil in idle haste, And all the late endeavour waste. Up! nor the promised help delay Until the hour have slipped away. Up! and with Raghu's son renew The search for Sítá lost to view. The hour is come: he hears the call, But not on thee reproaches fall From him who labours to repress His eager spirit's restlessness. Long joined to thee in friendly ties He made thy fame and fortune rise, In gentle gifts by none excelled. In splendid might unparalleled. Up, to his succour, King! repay The favour of that prosperous day, And to thy bravest captains send Prompt mandates to assist thy friend. The cry for help thou wilt not spurn Although no grace demands return: And wilt thou not thine aid afford To him who realm and life restored? Exert thy power, and thou hast won The love of Da[aratha's son: And wilt thou for his summons wait, And, till he call thee, hesitate? Think not the hero needs thy power To save him in the desperate hour: He with his arrows could subdue The Gods and all the demon crew, And only waits that he may see
- **Translation**: 

---

### Verse 12 (Ramayana 0.1297)
- **Original**: Canto XXIX. Hanumán's Counsel. 1279 Redeemed the promise made by thee. For thee he risked his life and fought, For thee that great deliverance wrought. Then let us trace through earth and skies His lady wheresoe'er she lies. Through realms above, beneath, we flee, And plant our footsteps on the sea. Then why, O Lord of Vánars, still Delay us waiting for thy will? Give thy commands, O King, and say What task has each and where the way. Before thee myriad Vánars stand To sweep through heaven, o'er seas and land.” Sugríva heard the timely rede That roused him in the day of need, And thus to Níla prompt and brave His hest the imperial Vánar gave: “Go, Níla, to the distant hosts That keep in arms their several posts, And all the armies that protect The quarters,631 with their chiefs, collect. To all the luminaries placed In intermediate regions haste, And bid each captain rise and lead His squadrons to their king with speed. Do thou meanwhile with strictest care All that the time requires prepare. The loitering Vánar who delays To gather here ere thrice five days, Shall surely die for his offence, Condemned for sinful negligence.” 631 The troops who guard the frontiers on the north, south, east and west.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1298)
- **Original**: 1280 The Ramayana Canto XXX. Ráma's Lament. But Ráma in the autumn night Stood musing on the mountain height, While grief and love that scorned control Shook with wild storms the hero's soul. Clear was the sky, without a cloud The glory of the moon to shroud. And bright with purest silver shone Each hill the soft beams looked upon. He knew Sugríva's heart was bent On pleasure, gay and negligent. He thought on Janak's child forlorn From his fond arms for ever torn. He mourned occasion slipping by, And faint with anguish heaved each sigh.[361] He sat where many a varied streak Of rich ore marked the mountain peak. He raised his eyes the sky to view, And to his love his sad thoughts flew. He heard the Sáras cry, and faint With sorrow poured his love-born plaint: “She, she who mocked the softest tone Of wild birds' voices with her own,— Where strays she now, my love who played So happy in our hermit shade? How can my absent love behold The bright trees with their flowers of gold, And all their gleaming glory see With eyes that vainly look for me? How is it with my darling when From the deep tangles of the glen Float carols of each bird elate With rapture singing to his mate?
- **Translation**: 

---

### Verse 14 (Ramayana 0.1299)
- **Original**: Canto XXX. Ráma's Lament. 1281 In vain my weary glances rove From lake to hill, from stream to grove: I find no rapture in the scene, And languish for my fawn-eyed queen. Ah, does strong love with wild unrest, Born of the autumn, stir her breast? And does the gentle lady pine Till her bright eyes shall look in mine?” Thus Raghu's son in piteous tone, O'erwhelmed with sorrow, made his moan. E'en as the bird that drinks the rains632 To Indra thousand-eyed complains. Then LakshmaG who had wandered through The copses where the berries grew, Returning to the cavern found His brother chief in sorrow drowned, And pitying the woes that broke The spirit of the hero spoke: “Why cast thy strength of soul away, And weakly yield to passion's sway? Arise, my brother, do and dare Ere action perish in despair. Recall the firmness of thy heart, And nerve thee for a hero's part. Whose is the hand unscathed to sieze The red flame quickened by the breeze? Where is the foe will dare to wrong Or keep the Maithil lady long?” Then with pale lips that sorrow dried The son of Raghu thus replied: 632 The Chátaka, Cuculus, Melanoleucus, is supposed to drink nothing but the water for the clouds.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1300)
- **Original**: 1282 The Ramayana “Lord Indra thousand-eyed, has sent The sweet rain from the firmament, Sees the rich promise of the grain, And turns him to his rest again. The clouds with voices loud and deep, Veiling each tree upon the steep, Up on the thirsty earth have shed Their precious burden and are fled. Now in kings' hearts ambition glows: They rush to battle with their foes;633 But in Sugríva's sloth I see No care for deeds of chivalry. See, LakshmaG, on each breezy height A thousand autumn blooms are bright. See how the wings of wild swans gleam On every islet of the stream. Four months of flood and rain are past: A hundred years they seemed to last To me whom toil and trouble tried, My Sítá severed from my side. She, gentlest woman, weak and young, Still to her lord unwearied clung. Still by the exile's side she stood In the wild ways of DaG ak wood, Like a fond bird disconsolate If parted from her darling mate. Sugríva, lapped in soft repose, Untouched by pity for my woes, Scorns the poor exile, dispossessed, By RávaG's mightier arm oppressed, The wretch who comes to sue and pray From his lost kingdom far away. 633 The time for warlike expeditions began when the rains had ceased.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1301)
- **Original**: Canto XXX. Ráma's Lament. 1283 Hence falls on me the Vánar's scorn, A suitor friendless and forlorn. The time is come: with heedless eye He sees the hour of action fly,— Unmindful, now his hopes succeed, Of promise made in stress of need. Go seek him sunk in bliss and sloth, Forgetful of his royal oath, And as mine envoy thus upbraid The monarch for his help delayed: “Vile is the wretch who will not pay The favour of an earlier day, Hope in the supplicant's breast awakes, And then his plighted promise breaks. Noblest, mid all of women born, Who keeps the words his lips have sworn, Yea, if those words be good or ill, Maintains his faith unbroken still. The thankless who forget to aid The friend who helped them when they prayed, Dishonoured in their death shall lie, And dogs shall pass their corpses by. Sure thou wouldst see my strained arm hold My bow of battle backed with gold, Wouldst gaze upon its awful form Like lightning flashing through the storm, And hear the clanging bowstring loud As thunder from a labouring cloud.” His valour and his strength I know: But pleasure's sway now sinks them low, With thee, my brother, for ally That strength and valour I defy. [362]
- **Translation**: 

---

### Verse 17 (Ramayana 0.1302)
- **Original**: 1284 The Ramayana He promised, when the rains should end, The succour of his arm to lend. Those months are past: he dares forget, And, lapped in pleasure, slumbers yet. No thought disturbs his careless breast For us impatient and distressed, And, while we sadly wait and pine, Girt by his lords he quaffs the wine. Go, brother, go, his palace seek, And boldly to Sugríva speak, Thus give the listless king to know What waits him if my anger glow: Still open, to the gloomy God, Lies the sad path that Báli trod. “Still to thy plighted word be true, Lest thou, O King, that path pursue. I launched the shaft I pointed well. And Báli, only Báli, fell. But, if from truth thou dare to stray, Both thee and thine this hand shall slay.” Thus be the Vánar king addressed, Then add thyself what seems the best.” Canto XXXI. The Envoy. Thus Ráma spoke, and LakshmaG then Made answer to the prince of men: “Yea, if the Vánar, undeterred By fear of vengeance, break his word, Loss of his royal power ere long Shall pay the traitor for the wrong.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1303)
- **Original**: Canto XXXI. The Envoy. 1285 Nor deem I him so void of sense To brave the bitter consequence. But if enslaved to joy he lie, And scorn thy grace with blinded eye, Then let him join his brother slain: Unmeet were such a wretch to reign. Quick rises, kindling in my breast, The wrath that will not be repressed, And bids me in my fury slay The breaker of his faith to-day. Let Báli's son thy consort trace With bravest chiefs of Vánar race.” Thus spoke the hero, and aglow With rage of battle seized his bow. But Ráma thus in gentler mood With fitting words his speech renewed: “No hero with a soul like thine To paths of sin will e'er incline, He who his angry heart can tame Is worthiest of a hero's name. Not thine, my brother, be the part So alien from the tender heart, Nor let thy feet by wrath misled Forsake the path they loved to tread. From harsh and angry words abstain: With gentle speech a hearing gain, And tax Sugríva with the crime Of failing faith and wasted time.”
- **Translation**: 

---

### Verse 19 (Ramayana 0.1304)
- **Original**: 1286 The Ramayana Then LakshmaG, bravest of the brave, Obeyed the hest that Ráma gave, To whom devoting every thought The Vánar's royal town he sought. As Mandar's mountain heaves on high His curved peak soaring to the sky, So LakshmaG showed, his dread bow bent Like Indra's634 in the firmament. His brother's wrath, his brother's woe Inflamed his soul to fiercest glow. The tallest trees to earth were cast As furious on his way he passed, And where he stepped, so fiercely fleet, The stones were shivered by his feet. He reached Kishkindhá's city deep Embosomed where the hills were steep, Where street and open square were lined With legions of the Vánar kind. Then, as his lips with fury swelled, The lord of Raghu's line beheld A stream of Vánar chiefs outpoured To do obeisance to their lord. But when the mighty prince in view Of the thick coming Vánars drew, They turned them in amaze to seize Crags of the rock and giant trees. He saw, and fiercer waxed his ire, As oil lends fury to the fire. Scarce had the Vánar chieftains seen That wrathful eye, that troubled mien Fierce as the God's who rules the dead, When, turned in wild affright, they fled. 634 The rainbow.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1305)
- **Original**: Canto XXXI. The Envoy. 1287 Speeding in breathless terror all Sought King Sugríva's council hall, And there made known their tale of fear, That LakshmaG wild with rage, was near. The king, untroubled by alarms, Held Tárá in his amorous arms, And in the distant bower with her Heard not each clamorous messenger. Then, summoned at the lords' behest Forth from the city portals pressed, Each like some elephant or cloud, The Vánars in a trembling crowd: Fierce warriors all with massive jaws And terrors of their tiger claws, Some matched ten elephants, and some A hundred's strength could overcome. Some chieftains, mightier than the rest, Ten times a hundred's force possessed. With eyes of fury LakshmaG viewed The Vánars' tree-armed multitude. Thus garrisoned from side to side The city walls assault defied. Beyond the moat that girt the wall Advanced the Vánar chiefs; and all Upon the plain in firm brigade, Impetuous warriors, stood arrayed. [363] Red at the sight flashed LakshmaG's eyes, His bosom heaved tumultuous sighs, And forth the fire of fury broke Like flame that flashes through the smoke. Like some fierce snake the hero stood: His bow recalled the expanded hood, And in his shaft-head bright and keen The flickering of its tongue was seen:
- **Translation**: 

---

