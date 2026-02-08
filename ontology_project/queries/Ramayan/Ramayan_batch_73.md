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

### Verse 1 (Ramayan 0.1441)
- **Original**: Canto XIII. Despair And Hope. 1423 His well-beloved consort's fate, My crime the same if I reveal The mournful story or conceal? If with no happier tale to tell I seek our mountain citadel, How shall I face our lord the king, And meet his angry questioning? How shall I greet my friends, and brook The muttered taunt, the scornful look? How to the son of Raghu go And kill him with my tale of woe? For sure the mournful tale I bear Will strike him dead with wild despair. And Lakshma G ever fond and true, Will, undivided, perish too. Bharat will learn his brother's fate, And die of grief disconsolate, And sadZatrughna with a cry Of anguish on his corpse will die. Our king Sugríva, ever found True to each bond in honour bound, Will mourn the pledge he vainly gave, And die with him he could not save. Then Rumá his devoted wife For her dead lord will leave her life, And Tárá, widowed and forlorn, Will die in anguish, sorrow-worn. On Angad too the blow will fall Killing the hope and joy of all. The ruin of their prince and king The Vánars' souls with woe will wring. And each, overwhelmed with dark despair, Will beat his head and rend his hair. Each, graced and honoured long, will miss
- **Translation**: 

---

### Verse 2 (Ramayan 0.1442)
- **Original**: 1424 The Ramayana His careless life of easy bliss, In happy troops will play no more On breezy rock and shady shore, But with his darling wife and child Will seek the mountain top, and wild With hopeless desolation, throw Himself, his wife, and babe, below. Ah no: unless the dame I find I ne'er will meet my Vánar kind. Here rather in some distant dell A lonely hermit will I dwell, Where roots and berries will supply My humble wants until I die; Or on the shore will raise a pyre And perish in the kindled fire. Or I will strictly fast until With slow decay my life I kill, And ravening dogs and birds of air The limbs of Hanumán shall tear. Here will I die, but never bring Destruction on my race and king. But still unsearched one grove I see With many a bright A[oka tree. There will I enter in, and through The tangled shade my search renew. Be glory to the host on high, The Sun and Moon who light the sky, The Vasus818 and the Maruts'819 train, 818 The Vasus are a class of eight deities, originally personifications of natural phenomena. 819 The Maruts are the winds or Storm-Gods.
- **Translation**: 

---

### Verse 3 (Ramayan 0.1443)
- **Original**: Canto XIV. The Asoka Grove. 1425 Ádityas820 and the A[vins821 twain. So may I win success, and bring The lady back with triumphing.” Canto XIV. The Asoka Grove. He cleared the barrier at a bound; He stood within the pleasant ground, [404] And with delighted eyes surveyed The climbing plants and varied shade, He saw unnumbered trees unfold The treasures of their pendent gold, As, searching for the Maithil queen, He strayed through alleys soft and green; And when a spray he bent or broke Some little bird that slept awoke. Whene'er the breeze of morning blew, Where'er a startled peacock flew, The gaily coloured branches shed Their flowery rain upon his head That clung around the Vánar till He seemed a blossom-covered hill,822 The earth, on whose fair bosom lay The flowers that fell from every spray, Was glorious as a lovely maid In all her brightest robes arrayed, 820 The Ádityas originally seven deities of the heavenly sphere of whom VaruGa is the chief. The name Áditya was afterwards given to any God, specially to Súrya the Sun. 821 The A[vins are the Heavenly Twins, the Castor and Pollux of the Hindus. 822 The poet forgets that Hanumán has reduced himself to the size of a cat.
- **Translation**: 

---

### Verse 4 (Ramayan 0.1444)
- **Original**: 1426 The Ramayana He saw the breath of morning shake The lilies on the rippling lake Whose waves a pleasant lapping made On crystal steps with gems inlaid. Then roaming through the enchanted ground, A pleasant hill the Vánar found, And grottoes in the living stone With grass and flowery trees o'ergrown. Through rocks and boughs a brawling rill Leapt from the bosom of the hill, Like a proud beauty when she flies From her love's arms with angry eyes. He clomb a tree that near him grew And leafy shade around him threw. “Hence,” thought the Vánar,“shall I see The Maithil dame, if here she be, These lovely trees, this cool retreat Will surely tempt her wandering feet. Here the sad queen will roam apart. And dream of Ráma in her heart.” Canto XV. Sítá. Fair as Kailása white with snow He saw a palace flash and glow, A crystal pavement gem-inlaid, And coral steps and colonnade, And glittering towers that kissed the skies, Whose dazzling splendour charmed his eyes. There pallid, with neglected dress,
- **Translation**: 

---

### Verse 5 (Ramayan 0.1445)
- **Original**: Canto XVI. Hanumán's Lament. 1427 Watched close by fiend and giantess, Her sweet face thin with constant flow Of tears, with fasting and with woe; Pale as the young moon's crescent when The first faint light returns to men: Dim as the flame when clouds of smoke The latent glory hide and choke; Like RohiGí the queen of stars Oppressed by the red planet Mars; From her dear friends and husband torn, Amid the cruel fiends, forlorn, Who fierce-eyed watch around her kept, A tender woman sat and wept. Her sobs, her sighs, her mournful mien, Her glorious eyes, proclaimed the queen. “This, this is she,” the Vánar cried, “Fair as the moon and lotus-eyed, I saw the giant Rávan bear A captive through the fields of air. Such was the beauty of the dame; Her form, her lips, her eyes the same. This peerless queen whom I behold Is Ráma's wife with limbs of gold. Best of the sons of men is he, And worthy of her lord is she.” Canto XVI. Hanumán's Lament.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1446)
- **Original**: 1428 The Ramayana Then, all his thoughts on Sítá bent, The Vánar chieftain made lament: “The queen to Ráma's soul endeared, By LakshmaG's pious heart revered, Lies here,— for none may strive with Fate, A captive, sad and desolate. The brothers' might full well she knows, And bravely bears the storm of woes, As swelling Gangá in the rains The rush of every flood sustains. Her lord, for her, fierce Báli slew, Virádha's monstrous might o'erthrew, For her the fourteen thousand slain In Janasthán bedewed the plain. And if for her Ikshváku's son Destroyed the world 'twere nobly done. This, this is she, so far renowned, Who sprang from out the furrowed ground,823 Child of the high-souled king whose sway The men of Míthilá obey: The glorious lady wooed and won By Da[aratha's noblest son; And now these sad eyes look on her Mid hostile fiends a prisoner. From home and every bliss she fled By wifely love and duty led, And heedless of a wanderer's woes, A life in lonely forests chose. This, this is she so fair of mould. Whose limbs are bright as burnished gold.[405] Whose voice was ever soft and mild, Who sweetly spoke and sweetly smiled. 823 Sítá“not of woman born,” was found by King Janak as he was turning up the ground in preparation for a sacrifice. See Book II, Canto CXVIII.
- **Translation**: 

---

### Verse 7 (Ramayan 0.1447)
- **Original**: Canto XVII. Sítá's Guard. 1429 O, what is Ráma's misery! how He longs to see his darling now! Pining for one of her fond looks As one athirst for water brooks. Absorbed in woe the lady sees No Rákshas guard, no blooming trees. Her eyes are with her thoughts, and they Are fixed on Ráma far away.” Canto XVII. Sítá's Guard. His pitying eyes with tears bedewed, The weeping queen again he viewed, And saw around the prisoner stand Her demon guard, a fearful band. Some earless, some with ears that hung Low as their feet and loosely swung: Some fierce with single ears and eyes, Some dwarfish, some of monstrous size: Some with their dark necks long and thin With hair upon the knotty skin: Some with wild locks, some bald and bare, Some covered o'er with bristly hair: Some tall and straight, some bowed and bent With every foul disfigurement: All black and fierce with eyes of fire, Ruthless and stern and swift to ire: Some with the jackal's jaw and nose, Some faced like boars and buffaloes: Some with the heads of goats and kine, Of elephants, and dogs, and swine:
- **Translation**: 

---

### Verse 8 (Ramayan 0.1448)
- **Original**: 1430 The Ramayana With lions' lips and horses' brows, They walked with feet of mules and cows: Swords, maces, clubs, and spears they bore In hideous hands that reeked with gore, And, never sated, turned afresh To bowls of wine and piles of flesh. Such were the awful guards who stood Round Sítá in that lovely wood, While in her lonely sorrow she Wept sadly neath a spreading tree. He watched the spouse of Ráma there Regardless of her tangled hair, Her jewels stripped from neck and limb, Decked only with her love of him. Canto XVIII. Rávan. While from his shelter in the boughs The Vánar looked on Ráma's spouse He heard the gathered giants raise The solemn hymn of prayer and praise.— Priests skilled in rite and ritual, who The Vedas and their branches824 knew. Then, as loud strains of music broke His sleep, the giant monarch woke. Swift to his heart the thought returned 824 The sixAngas or subordinate branches of the Vedas are 1.Sikshá, the science of proper articulation and pronunciation: 2.Chhandas, metre: 3. Vyákarana, linguistic analysis or grammar: 4.Nirukta, explanation of difficult Vedic words: 5.Jyotishmom , Astronomy, or rather the Vedic Calendar: 6. Kalpa, ceremonial.
- **Translation**: 

---

### Verse 9 (Ramayan 0.1449)
- **Original**: Canto XVIII. Rávan. 1431 Of the fair queen for whom he burned; Nor could the amorous fiend control The passion that absorbed his soul. In all his brightest garb arrayed He hastened to that lovely shade, Where glowed each choicest flower and fruit, And the sweet birds were never mute, And tall deer bent their heads to drink On the fair streamlet's grassy brink. Near that A[oka grove he drew,— A hundred dames his retinue. Like Indra with the thousand eyes Girt with the beauties of the skies. Some walked beside their lord to hold The chouries, fans, and lamps of gold. And others purest water bore In golden urns, and paced before. Some carried, piled on golden plates, Delicious food of dainty cates; Some wine in massive bowls whereon The fairest gems resplendent shone. Some by the monarch's side displayed, Wrought like a swan, a silken shade: Another beauty walked behind, The sceptre to her care assigned. Around the monarch gleamed the crowd As lightnings flash about a cloud, And each made music as she went With zone and tinkling ornament. Attended thus in royal state The monarch reached the garden gate, While gold and silver torches, fed With scented oil a soft light shed.825 [406] 825 There appears to be some confusion of time here. It was already morning
- **Translation**: 

---

### Verse 10 (Ramayan 0.1450)
- **Original**: 1432 The Ramayana He, while the flame of fierce desire Burnt in his eyes like kindled fire, Seemed Love incarnate in his pride, His bow and arrows laid aside.826 His robe, from spot and blemish free Like Amrit foamy from the sea,827 Hung down in many a loosened fold Inwrought with flowers and bright with gold. The Vánar from his station viewed, Amazed, the wondrous multitude, Where, in the centre of that ring Of noblest women, stood the king, As stands the full moon fair to view, Girt by his starry retinue. Canto XIX. Sítá's Fear. Then o'er the lady's soul and frame A sudden fear and trembling came, When, glowing in his youthful pride, She saw the monarch by her side. Silent she sat, her eyes depressed, Her soft arms folded o'er her breast, And,— all she could,— her beauties screened From the bold gazes of the fiend. when Hanumán entered the grove, and the torches would be needless. 826 RávaG is one of those beings who can“climb them as they will,” and can of course assume the loveliest form to please human eyes as well as the terrific shape that suits the king of the Rákshases. 827 White and lovely as the Arant or nectar recovered from the depths of the Milky Sea when churned by the assembled Gods. See Book I, Canto XLV.
- **Translation**: 

---

### Verse 11 (Ramayan 0.1451)
- **Original**: Canto XX. Rávan's Wooing. 1433 There where the wild she-demons kept Their watch around, she sighed and wept. Then, like a severed bough, she lay Prone on the bare earth in dismay. The while her thoughts on love's fleet wings Flew to her lord the best of kings. She fell upon the ground, and there Lay struggling with her wild despair, Sad as a lady born again To misery and woe and pain, Now doomed to grief and low estate, Once noble fair and delicate: Like faded light of holy lore, Like Hope when all her dreams are o'er; Like ruined power and rank debased, Like majesty of kings disgraced: Like worship foiled by erring slips, The moon that labours in eclipse; A pool with all her lilies dead, An army when its king has fled: So sad and helpless wan and worn, She lay among the fiends forlorn. Canto XX. Rávan's Wooing. With amorous look and soft address The fiend began his suit to press: “Why wouldst thou, lady lotus-eyed, From my fond glance those beauties hide? Mine eager suit no more repel: But love me, for I love thee well.
- **Translation**: 

---

### Verse 12 (Ramayan 0.1452)
- **Original**: 1434 The Ramayana Dismiss, sweet dame, dismiss thy fear; No giant and no man is near. Ours is the right by force to seize What dames soe'er our fancy please.828 But I with rude hands will not touch A lady whom I love so much. Fear not, dear queen: no fear is nigh: Come, on thy lover's love rely, Some little sign of favor show, Nor lie enamoured of thy woe. Those limbs upon that cold earth laid, Those tresses twined in single braid,829 The fast and woe that wear thy frame, Beseem not thee, O beauteous dame. For thee the fairest wreaths were meant, The sandal and the aloe's scent, Rich ornaments and pearls of price, And vesture meet for Paradise. With dainty cates shouldst thou be fed, And rest upon a sumptuous bed. And festive joys to thee belong, The music, and the dance and song. Rise, pearl of women, rise and deck With gems and chains thine arms and neck. Shall not the dame I love be seen In vesture worthy of a queen? 828 RávaG in his magic car carrying off the most beautiful women reminds us of the magician inOrlando Furioso, possesor of the flying horse. “Volando talor s'alza ne le stelle, E poi quasi talor la terra rade; E ne porta con lui tutte le belle Donne che trova per quelle contrade.” 829 Indian women twisted their long hair in a single braid as a sign of mourning for their absent husbands.
- **Translation**: 

---

### Verse 13 (Ramayan 0.1453)
- **Original**: Canto XX. Rávan's Wooing. 1435 Methinks when thy sweet form was made His hand the wise Creator stayed; For never more did he design A beauty meet to rival thine. Come, let us love while yet we may, For youth will fly and charms decay, Come cast thy grief and fear aside, And be my love, my chosen bride. The gems and jewels that my hand Has reft from every plundered land,— To thee I give them all this day, And at thy feet my kingdom lay. [407] The broad rich earth will I o'errun, And leave no town unconquered, none; Then of the whole an offering make To Janak,830 dear, for thy sweet sake. In all the world no power I see Of God or man can strive with me. Of old the Gods and Asurs set In terrible array I met: Their scattered hosts to earth I beat, And trod their flags beneath my feet. Come, taste of bliss and drink thy fill, And rule the slave who serves thy will. Think not of wretched Ráma: he Is less than nothing now to thee. Stript of his glory, poor, dethroned, A wanderer by his friends disowned, On the cold earth he lays his head, Or is with toil and misery dead. And if perchance he lingers yet, His eyes on thee shall ne'er be set. 830 Janak, king of Míthilá, was Sítá's father.
- **Translation**: 

---

### Verse 14 (Ramayan 0.1454)
- **Original**: 1436 The Ramayana Could he, that mighty monarch, who Was named HiraGyaka[ipu, Could he who wore the garb of gold Win Glory back from Indra's hold?831 O lady of the lovely smile, Whose eyes the sternest heart beguile, In all thy radiant beauty dressed My heart and soul thou ravishest. What though thy robe is soiled and worn, And no bright gems thy limbs adorn, Thou unadorned art dearer far Than all my loveliest consorts are. My royal home is bright and fair; A thousand beauties meet me there, But come, my glorious love, and be The queen of all those dames and me.” Canto XXI. Sítá's Scorn. She thought upon her lord and sighed, And thus in gentle tones replied: “Beseems thee not, O King, to woo A matron, to her husband true. Thus vainly one might hope by sin And evil deeds success to win. Shall I, so highly born, disgrace My husband's house, my royal race? 831 HiraGyaka[ipu was a king of the Daityas celebrated for his blasphemous impieties. When his pious son Prahlada praised VishGu the Daitya tried to kill him, when the God appeared in the incarnation of the man-lion and tore the tyrant to pieces.
- **Translation**: 

---

### Verse 15 (Ramayan 0.1455)
- **Original**: Canto XXI. Sítá's Scorn. 1437 Shall I, a true and loyal dame, Defile my soul with deed of shame?” Then on the king her back she turned, And answered thus the prayer she spurned: “Turn, RávaG, turn thee from thy sin; Seek virtue's paths and walk therein. To others dames be honour shown; Protect them as thou wouldst thine own. Taught by thyself, from wrong abstain Which, wrought on thee, thy heart would pain.832 Beware: this lawless love of thine Will ruin thee and all thy line; And for thy sin, thy sin alone, Will Lanká perish overthrown. Dream not that wealth and power can sway My heart from duty's path to stray. Linked like the Day-God and his shine, I am my lord's and he is mine. Repent thee of thine impious deed; To Ráma's side his consort lead. Be wise; the hero's friendship gain, Nor perish in his fury slain. Go, ask the God of Death to spare, Or red bolt flashing through the air, But look in vain for spell or charm To stay my Ráma's vengeful arm. Thou, when the hero bends his bow, Shalt hear the clang that heralds woe, Loud as the clash when clouds are rent 832 Do unto others as thou wouldst they should do unto thee, is a precept frequently occurring in the old Indian poems. This charity is to embrace not human beings only, but bird and beast as well:“He prayeth best who loveth best all things both great and small.”
- **Translation**: 

---

### Verse 16 (Ramayan 0.1456)
- **Original**: 1438 The Ramayana And Indra's bolt to earth is sent. Then shall his furious shafts be sped, Each like a snake with fiery head, And in their flight shall hiss and flame Marked with the mighty archer's name.833 Then in the fiery deluge all Thy giants round their king shall fall.” [408] Canto XXII. Rávan's Threat. Then anger swelled in RávaG's breast, Who fiercely thus the dame addressed: “'Tis ever thus: in vain we sue To woman, and her favour woo. A lover's humble words impel Her wayward spirit to rebel. The love of thee that fills my soul Still keeps my anger in control, As charioteers with bit and rein The swerving of the steed restrain. The love that rules me bids me spare Thy forfeit life, O thou most fair. For this, O Sítá, have I borne 833 It was the custom of Indian warriors to mark their arrows with their ciphers or names, and it seems to have been regarded as a point of honour to give an enemy the satisfaction of knowing who had shot at him. This passage however contains, if my memory serves me well, the first mention in the poem of this practice, and as arrows have been so frequently mentioned and described with almost every conceivable epithet, its occurrence here seems suspicious. No mention of, or allusion to writing has hitherto occurred in the poem.
- **Translation**: 

---

### Verse 17 (Ramayan 0.1457)
- **Original**: Canto XXII. Rávan's Threat. 1439 The keen reproach, the bitter scorn, And the fond love thou boastest yet For that poor wandering anchoret; Else had the words which thou hast said Brought death upon thy guilty head. Two months, fair dame, I grant thee still To bend thee to thy lover's will. If when that respite time is fled Thou still refuse to share my bed, My cooks shall mince thy limbs with steel And serve thee for my morning meal.”834 The minstrel daughters of the skies Looked on her woe with pitying eyes, And sun-bright children of the Gods835 Consoled the queen with smiles and nods. She saw, and with her heart at ease, Addressed the fiend in words like these; “Hast thou no friend to love thee, none In all this isle to bid thee shun The ruin which thy crime will bring On thee and thine, O impious King? Who in all worlds save thee could woo Me, Ráma's consort pure and true, As though he tempted with his love Queen Zachí836 on her throne above? How canst thou hope, vile wretch, to fly The vengeance that e'en now is nigh, When thou hast dared, untouched by shame, To press thy suit on Ráma's dame? 834 This threat in the same words occurs in Book III, Canto LVI. 835 RávaG carried off and kept in his palace not only earthly princesses but the daughters of Gods and Gandharvas. 836 The wife of Indra.
- **Translation**: 

---

### Verse 18 (Ramayan 0.1458)
- **Original**: 1440 The Ramayana Where woods are thick and grass is high A lion and a hare may lie; My Ráma is the lion, thou Art the poor hare beneath the bough. Thou railest at the lord of men, But wilt not stand within his ken. What! is that eye unstricken yet Whose impious glance on me was set? Still moves that tongue that would not spare The wife of Da[aratha's heir?” Then, hissing like a furious snake, The fiend again to Sítá spake: “Deaf to all prayers and threats art thou, Devoted to thy senseless vow. No longer respite will I give, And thou this day shalt cease to live; For I, as sunlight kills the morn, Will slay thee for thy scathe and scorn.” The Rákshas guard was summoned: all The monstrous crew obeyed the call, And hastened to the king to take The orders which he fiercely spake: “See that ye guard her well, and tame, Like some wild thing, the stubborn dame, Until her haughty soul be bent By mingled threat and blandishment.”837 The monsters heard: away he strode, And passed within his queens' abode. 837 These four lines have occurred before. Book III, Canto LVI.
- **Translation**: 

---

### Verse 19 (Ramayan 0.1459)
- **Original**: Canto XXIII. The Demons' Threats. 1441 Canto XXIII. The Demons' Threats. Then round the helpless Sítá drew With fiery eyes the hideous crew, And thus assailed her, all and each, With insult, taunt, and threatening speech: “What! can it be thou prizest not This happy chance, this glorious lot, To be the chosen wife of one So strong and great, Pulastya's son? Pulastya— thus have sages told— Is mid the Lords of Life838 enrolled. Lord Brahmá's mind-born son was he, Fourth of that glorious company. Vi[ravas from Pulastya sprang,— Through all the worlds his glory rang. And of Vi[ravas, large-eyed dame! Our king the mighty RávaG came. His happy consort thou mayst be: Scorn not the words we say to thee.” One awful demon, fiery-eyed, Stood by the Maithil queen and cried: 'Come and be his, if thou art wise, Who smote the sovereign of the skies, And made the thirty Gods and three,839 O'ercome in furious battle, flee. [409] 838 Prajápatis are the ten lords of created beings first created by Brahmá; somewhat like the Demiurgi of the Gnostics. 839 “This is the number of the Vedic divinities mentioned in the Rig-veda. In Ashmaka I. Súkta XXXIV, the Rishi HiraGyastúpa invoking the A[vins says: Á Násatyá tribhirekáda[airiha devebniryátam:‘O Násatyas (A[vins) come hither with the thrice eleven Gods.’And in Súkta XLV, the Rishi Praskanva address- ing his hymn to Agni (ignis, fire), thus invokes him:‘Lord of the red steeds,
- **Translation**: 

---

### Verse 20 (Ramayan 0.1460)
- **Original**: 1442 The Ramayana Thy lover turns away with scorn From wives whom grace and youth adorn. Thou art his chosen consort, thou Shall be his pride and darling now.” Another, Vikatá by name, In words like these addressed the dame: “The king whose blows, in fury dealt, The Nágas840 and Gandharvas841 felt, In battle's fiercest brunt subdued, Has stood by thee and humbly wooed. And wilt thou in thy folly miss The glory of a love like this? Scared by his eye the sun grows chill, The wanderer wind is hushed and still. The rains at his command descend, And trees with new-blown blossoms bend. His word the hosts of demons fear, And wilt thou, dame, refuse to hear? Be counselled; with his will comply, Or, lady, thou shalt surely die.” propitiated by our prayers lead hither the thirty-three Gods.’This number must certainly have been the actual number in the early days of the Vedic religion: although it appears probable enough that the thirty-three Vedic divinities could not then be found co-ordinated in so systematic a way as they were arranged more recently by the authors of the Upanishads. In the later ages of Bramanism the number went on increasing without measure by successive mythical and religious creations which peopled the Indian Olympus with abstract beings of every kind. But through lasting veneration of the word of the Veda the custom regained of giving the name of‘the thirty-three Gods’to the immense phalanx of the multiplied deities.” G ORRESIO .{FNS 840 Serpent-Gods who dwell in the regions under the earth. 841 In the mythology of the epics the Gandharvas are the heavenly singers or musicians who form the orchestra at the banquets of the Gods, and they belong to the heaven of India in whose battles they share.
- **Translation**: 

---

