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

### Verse 1 (Ramayana 0.1446)
- **Original**: 1428 The Ramayana Then, all his thoughts on Sítá bent, The Vánar chieftain made lament: “The queen to Ráma's soul endeared, By LakshmaG's pious heart revered, Lies here,— for none may strive with Fate, A captive, sad and desolate. The brothers' might full well she knows, And bravely bears the storm of woes, As swelling Gangá in the rains The rush of every flood sustains. Her lord, for her, fierce Báli slew, Virádha's monstrous might o'erthrew, For her the fourteen thousand slain In Janasthán bedewed the plain. And if for her Ikshváku's son Destroyed the world 'twere nobly done. This, this is she, so far renowned, Who sprang from out the furrowed ground,823 Child of the high-souled king whose sway The men of Míthilá obey: The glorious lady wooed and won By Da[aratha's noblest son; And now these sad eyes look on her Mid hostile fiends a prisoner. From home and every bliss she fled By wifely love and duty led, And heedless of a wanderer's woes, A life in lonely forests chose. This, this is she so fair of mould. Whose limbs are bright as burnished gold.[405] Whose voice was ever soft and mild, Who sweetly spoke and sweetly smiled. 823 Sítá“not of woman born,” was found by King Janak as he was turning up the ground in preparation for a sacrifice. See Book II, Canto CXVIII.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1447)
- **Original**: Canto XVII. Sítá's Guard. 1429 O, what is Ráma's misery! how He longs to see his darling now! Pining for one of her fond looks As one athirst for water brooks. Absorbed in woe the lady sees No Rákshas guard, no blooming trees. Her eyes are with her thoughts, and they Are fixed on Ráma far away.” Canto XVII. Sítá's Guard. His pitying eyes with tears bedewed, The weeping queen again he viewed, And saw around the prisoner stand Her demon guard, a fearful band. Some earless, some with ears that hung Low as their feet and loosely swung: Some fierce with single ears and eyes, Some dwarfish, some of monstrous size: Some with their dark necks long and thin With hair upon the knotty skin: Some with wild locks, some bald and bare, Some covered o'er with bristly hair: Some tall and straight, some bowed and bent With every foul disfigurement: All black and fierce with eyes of fire, Ruthless and stern and swift to ire: Some with the jackal's jaw and nose, Some faced like boars and buffaloes: Some with the heads of goats and kine, Of elephants, and dogs, and swine:
- **Translation**: 

---

### Verse 3 (Ramayana 0.1448)
- **Original**: 1430 The Ramayana With lions' lips and horses' brows, They walked with feet of mules and cows: Swords, maces, clubs, and spears they bore In hideous hands that reeked with gore, And, never sated, turned afresh To bowls of wine and piles of flesh. Such were the awful guards who stood Round Sítá in that lovely wood, While in her lonely sorrow she Wept sadly neath a spreading tree. He watched the spouse of Ráma there Regardless of her tangled hair, Her jewels stripped from neck and limb, Decked only with her love of him. Canto XVIII. Rávan. While from his shelter in the boughs The Vánar looked on Ráma's spouse He heard the gathered giants raise The solemn hymn of prayer and praise.— Priests skilled in rite and ritual, who The Vedas and their branches824 knew. Then, as loud strains of music broke His sleep, the giant monarch woke. Swift to his heart the thought returned 824 The sixAngas or subordinate branches of the Vedas are 1.Sikshá, the science of proper articulation and pronunciation: 2.Chhandas, metre: 3. Vyákarana, linguistic analysis or grammar: 4.Nirukta, explanation of difficult Vedic words: 5.Jyotishmom , Astronomy, or rather the Vedic Calendar: 6. Kalpa, ceremonial.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1449)
- **Original**: Canto XVIII. Rávan. 1431 Of the fair queen for whom he burned; Nor could the amorous fiend control The passion that absorbed his soul. In all his brightest garb arrayed He hastened to that lovely shade, Where glowed each choicest flower and fruit, And the sweet birds were never mute, And tall deer bent their heads to drink On the fair streamlet's grassy brink. Near that A[oka grove he drew,— A hundred dames his retinue. Like Indra with the thousand eyes Girt with the beauties of the skies. Some walked beside their lord to hold The chouries, fans, and lamps of gold. And others purest water bore In golden urns, and paced before. Some carried, piled on golden plates, Delicious food of dainty cates; Some wine in massive bowls whereon The fairest gems resplendent shone. Some by the monarch's side displayed, Wrought like a swan, a silken shade: Another beauty walked behind, The sceptre to her care assigned. Around the monarch gleamed the crowd As lightnings flash about a cloud, And each made music as she went With zone and tinkling ornament. Attended thus in royal state The monarch reached the garden gate, While gold and silver torches, fed With scented oil a soft light shed.825 [406] 825 There appears to be some confusion of time here. It was already morning
- **Translation**: 

---

### Verse 5 (Ramayana 0.1450)
- **Original**: 1432 The Ramayana He, while the flame of fierce desire Burnt in his eyes like kindled fire, Seemed Love incarnate in his pride, His bow and arrows laid aside.826 His robe, from spot and blemish free Like Amrit foamy from the sea,827 Hung down in many a loosened fold Inwrought with flowers and bright with gold. The Vánar from his station viewed, Amazed, the wondrous multitude, Where, in the centre of that ring Of noblest women, stood the king, As stands the full moon fair to view, Girt by his starry retinue. Canto XIX. Sítá's Fear. Then o'er the lady's soul and frame A sudden fear and trembling came, When, glowing in his youthful pride, She saw the monarch by her side. Silent she sat, her eyes depressed, Her soft arms folded o'er her breast, And,— all she could,— her beauties screened From the bold gazes of the fiend. when Hanumán entered the grove, and the torches would be needless. 826 RávaG is one of those beings who can“climb them as they will,” and can of course assume the loveliest form to please human eyes as well as the terrific shape that suits the king of the Rákshases. 827 White and lovely as the Arant or nectar recovered from the depths of the Milky Sea when churned by the assembled Gods. See Book I, Canto XLV.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1451)
- **Original**: Canto XX. Rávan's Wooing. 1433 There where the wild she-demons kept Their watch around, she sighed and wept. Then, like a severed bough, she lay Prone on the bare earth in dismay. The while her thoughts on love's fleet wings Flew to her lord the best of kings. She fell upon the ground, and there Lay struggling with her wild despair, Sad as a lady born again To misery and woe and pain, Now doomed to grief and low estate, Once noble fair and delicate: Like faded light of holy lore, Like Hope when all her dreams are o'er; Like ruined power and rank debased, Like majesty of kings disgraced: Like worship foiled by erring slips, The moon that labours in eclipse; A pool with all her lilies dead, An army when its king has fled: So sad and helpless wan and worn, She lay among the fiends forlorn. Canto XX. Rávan's Wooing. With amorous look and soft address The fiend began his suit to press: “Why wouldst thou, lady lotus-eyed, From my fond glance those beauties hide? Mine eager suit no more repel: But love me, for I love thee well.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1452)
- **Original**: 1434 The Ramayana Dismiss, sweet dame, dismiss thy fear; No giant and no man is near. Ours is the right by force to seize What dames soe'er our fancy please.828 But I with rude hands will not touch A lady whom I love so much. Fear not, dear queen: no fear is nigh: Come, on thy lover's love rely, Some little sign of favor show, Nor lie enamoured of thy woe. Those limbs upon that cold earth laid, Those tresses twined in single braid,829 The fast and woe that wear thy frame, Beseem not thee, O beauteous dame. For thee the fairest wreaths were meant, The sandal and the aloe's scent, Rich ornaments and pearls of price, And vesture meet for Paradise. With dainty cates shouldst thou be fed, And rest upon a sumptuous bed. And festive joys to thee belong, The music, and the dance and song. Rise, pearl of women, rise and deck With gems and chains thine arms and neck. Shall not the dame I love be seen In vesture worthy of a queen? 828 RávaG in his magic car carrying off the most beautiful women reminds us of the magician inOrlando Furioso, possesor of the flying horse. “Volando talor s'alza ne le stelle, E poi quasi talor la terra rade; E ne porta con lui tutte le belle Donne che trova per quelle contrade.” 829 Indian women twisted their long hair in a single braid as a sign of mourning for their absent husbands.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1453)
- **Original**: Canto XX. Rávan's Wooing. 1435 Methinks when thy sweet form was made His hand the wise Creator stayed; For never more did he design A beauty meet to rival thine. Come, let us love while yet we may, For youth will fly and charms decay, Come cast thy grief and fear aside, And be my love, my chosen bride. The gems and jewels that my hand Has reft from every plundered land,— To thee I give them all this day, And at thy feet my kingdom lay. [407] The broad rich earth will I o'errun, And leave no town unconquered, none; Then of the whole an offering make To Janak,830 dear, for thy sweet sake. In all the world no power I see Of God or man can strive with me. Of old the Gods and Asurs set In terrible array I met: Their scattered hosts to earth I beat, And trod their flags beneath my feet. Come, taste of bliss and drink thy fill, And rule the slave who serves thy will. Think not of wretched Ráma: he Is less than nothing now to thee. Stript of his glory, poor, dethroned, A wanderer by his friends disowned, On the cold earth he lays his head, Or is with toil and misery dead. And if perchance he lingers yet, His eyes on thee shall ne'er be set. 830 Janak, king of Míthilá, was Sítá's father.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1454)
- **Original**: 1436 The Ramayana Could he, that mighty monarch, who Was named HiraGyaka[ipu, Could he who wore the garb of gold Win Glory back from Indra's hold?831 O lady of the lovely smile, Whose eyes the sternest heart beguile, In all thy radiant beauty dressed My heart and soul thou ravishest. What though thy robe is soiled and worn, And no bright gems thy limbs adorn, Thou unadorned art dearer far Than all my loveliest consorts are. My royal home is bright and fair; A thousand beauties meet me there, But come, my glorious love, and be The queen of all those dames and me.” Canto XXI. Sítá's Scorn. She thought upon her lord and sighed, And thus in gentle tones replied: “Beseems thee not, O King, to woo A matron, to her husband true. Thus vainly one might hope by sin And evil deeds success to win. Shall I, so highly born, disgrace My husband's house, my royal race? 831 HiraGyaka[ipu was a king of the Daityas celebrated for his blasphemous impieties. When his pious son Prahlada praised VishGu the Daitya tried to kill him, when the God appeared in the incarnation of the man-lion and tore the tyrant to pieces.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1455)
- **Original**: Canto XXI. Sítá's Scorn. 1437 Shall I, a true and loyal dame, Defile my soul with deed of shame?” Then on the king her back she turned, And answered thus the prayer she spurned: “Turn, RávaG, turn thee from thy sin; Seek virtue's paths and walk therein. To others dames be honour shown; Protect them as thou wouldst thine own. Taught by thyself, from wrong abstain Which, wrought on thee, thy heart would pain.832 Beware: this lawless love of thine Will ruin thee and all thy line; And for thy sin, thy sin alone, Will Lanká perish overthrown. Dream not that wealth and power can sway My heart from duty's path to stray. Linked like the Day-God and his shine, I am my lord's and he is mine. Repent thee of thine impious deed; To Ráma's side his consort lead. Be wise; the hero's friendship gain, Nor perish in his fury slain. Go, ask the God of Death to spare, Or red bolt flashing through the air, But look in vain for spell or charm To stay my Ráma's vengeful arm. Thou, when the hero bends his bow, Shalt hear the clang that heralds woe, Loud as the clash when clouds are rent 832 Do unto others as thou wouldst they should do unto thee, is a precept frequently occurring in the old Indian poems. This charity is to embrace not human beings only, but bird and beast as well:“He prayeth best who loveth best all things both great and small.”
- **Translation**: 

---

### Verse 11 (Ramayana 0.1456)
- **Original**: 1438 The Ramayana And Indra's bolt to earth is sent. Then shall his furious shafts be sped, Each like a snake with fiery head, And in their flight shall hiss and flame Marked with the mighty archer's name.833 Then in the fiery deluge all Thy giants round their king shall fall.” [408] Canto XXII. Rávan's Threat. Then anger swelled in RávaG's breast, Who fiercely thus the dame addressed: “'Tis ever thus: in vain we sue To woman, and her favour woo. A lover's humble words impel Her wayward spirit to rebel. The love of thee that fills my soul Still keeps my anger in control, As charioteers with bit and rein The swerving of the steed restrain. The love that rules me bids me spare Thy forfeit life, O thou most fair. For this, O Sítá, have I borne 833 It was the custom of Indian warriors to mark their arrows with their ciphers or names, and it seems to have been regarded as a point of honour to give an enemy the satisfaction of knowing who had shot at him. This passage however contains, if my memory serves me well, the first mention in the poem of this practice, and as arrows have been so frequently mentioned and described with almost every conceivable epithet, its occurrence here seems suspicious. No mention of, or allusion to writing has hitherto occurred in the poem.
- **Translation**: 

---

### Verse 12 (Ramayana 0.1457)
- **Original**: Canto XXII. Rávan's Threat. 1439 The keen reproach, the bitter scorn, And the fond love thou boastest yet For that poor wandering anchoret; Else had the words which thou hast said Brought death upon thy guilty head. Two months, fair dame, I grant thee still To bend thee to thy lover's will. If when that respite time is fled Thou still refuse to share my bed, My cooks shall mince thy limbs with steel And serve thee for my morning meal.”834 The minstrel daughters of the skies Looked on her woe with pitying eyes, And sun-bright children of the Gods835 Consoled the queen with smiles and nods. She saw, and with her heart at ease, Addressed the fiend in words like these; “Hast thou no friend to love thee, none In all this isle to bid thee shun The ruin which thy crime will bring On thee and thine, O impious King? Who in all worlds save thee could woo Me, Ráma's consort pure and true, As though he tempted with his love Queen Zachí836 on her throne above? How canst thou hope, vile wretch, to fly The vengeance that e'en now is nigh, When thou hast dared, untouched by shame, To press thy suit on Ráma's dame? 834 This threat in the same words occurs in Book III, Canto LVI. 835 RávaG carried off and kept in his palace not only earthly princesses but the daughters of Gods and Gandharvas. 836 The wife of Indra.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1458)
- **Original**: 1440 The Ramayana Where woods are thick and grass is high A lion and a hare may lie; My Ráma is the lion, thou Art the poor hare beneath the bough. Thou railest at the lord of men, But wilt not stand within his ken. What! is that eye unstricken yet Whose impious glance on me was set? Still moves that tongue that would not spare The wife of Da[aratha's heir?” Then, hissing like a furious snake, The fiend again to Sítá spake: “Deaf to all prayers and threats art thou, Devoted to thy senseless vow. No longer respite will I give, And thou this day shalt cease to live; For I, as sunlight kills the morn, Will slay thee for thy scathe and scorn.” The Rákshas guard was summoned: all The monstrous crew obeyed the call, And hastened to the king to take The orders which he fiercely spake: “See that ye guard her well, and tame, Like some wild thing, the stubborn dame, Until her haughty soul be bent By mingled threat and blandishment.”837 The monsters heard: away he strode, And passed within his queens' abode. 837 These four lines have occurred before. Book III, Canto LVI.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1459)
- **Original**: Canto XXIII. The Demons' Threats. 1441 Canto XXIII. The Demons' Threats. Then round the helpless Sítá drew With fiery eyes the hideous crew, And thus assailed her, all and each, With insult, taunt, and threatening speech: “What! can it be thou prizest not This happy chance, this glorious lot, To be the chosen wife of one So strong and great, Pulastya's son? Pulastya— thus have sages told— Is mid the Lords of Life838 enrolled. Lord Brahmá's mind-born son was he, Fourth of that glorious company. Vi[ravas from Pulastya sprang,— Through all the worlds his glory rang. And of Vi[ravas, large-eyed dame! Our king the mighty RávaG came. His happy consort thou mayst be: Scorn not the words we say to thee.” One awful demon, fiery-eyed, Stood by the Maithil queen and cried: 'Come and be his, if thou art wise, Who smote the sovereign of the skies, And made the thirty Gods and three,839 O'ercome in furious battle, flee. [409] 838 Prajápatis are the ten lords of created beings first created by Brahmá; somewhat like the Demiurgi of the Gnostics. 839 “This is the number of the Vedic divinities mentioned in the Rig-veda. In Ashmaka I. Súkta XXXIV, the Rishi HiraGyastúpa invoking the A[vins says: Á Násatyá tribhirekáda[airiha devebniryátam:‘O Násatyas (A[vins) come hither with the thrice eleven Gods.’And in Súkta XLV, the Rishi Praskanva address- ing his hymn to Agni (ignis, fire), thus invokes him:‘Lord of the red steeds,
- **Translation**: 

---

### Verse 15 (Ramayana 0.1460)
- **Original**: 1442 The Ramayana Thy lover turns away with scorn From wives whom grace and youth adorn. Thou art his chosen consort, thou Shall be his pride and darling now.” Another, Vikatá by name, In words like these addressed the dame: “The king whose blows, in fury dealt, The Nágas840 and Gandharvas841 felt, In battle's fiercest brunt subdued, Has stood by thee and humbly wooed. And wilt thou in thy folly miss The glory of a love like this? Scared by his eye the sun grows chill, The wanderer wind is hushed and still. The rains at his command descend, And trees with new-blown blossoms bend. His word the hosts of demons fear, And wilt thou, dame, refuse to hear? Be counselled; with his will comply, Or, lady, thou shalt surely die.” propitiated by our prayers lead hither the thirty-three Gods.’This number must certainly have been the actual number in the early days of the Vedic religion: although it appears probable enough that the thirty-three Vedic divinities could not then be found co-ordinated in so systematic a way as they were arranged more recently by the authors of the Upanishads. In the later ages of Bramanism the number went on increasing without measure by successive mythical and religious creations which peopled the Indian Olympus with abstract beings of every kind. But through lasting veneration of the word of the Veda the custom regained of giving the name of‘the thirty-three Gods’to the immense phalanx of the multiplied deities.” G ORRESIO .{FNS 840 Serpent-Gods who dwell in the regions under the earth. 841 In the mythology of the epics the Gandharvas are the heavenly singers or musicians who form the orchestra at the banquets of the Gods, and they belong to the heaven of India in whose battles they share.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1461)
- **Original**: Canto XXIV. Sítá's Reply. 1443 Canto XXIV. Sítá's Reply. Still with reproaches rough and rude Those fiends the gentle queen pursued: “What! can so fair a life displease, To dwell with him in joyous ease? Dwell in his bowers a happy queen In silk and gold and jewels' sheen? Still must thy woman fancy cling To Ráma and reject our king? Die in thy folly, or forget That wretched wandering anchoret. Come, Sítá, in luxurious bowers Spend with our lord thy happy hours; The mighty lord who makes his own The treasures of the worlds o'erthrown.” Then, as a tear bedewed her eye, The hapless lady made reply: “I loathe, with heart and soul detest The shameful life your words suggest. Eat, if you will, this mortal frame: My soul rejects the sin and shame. A homeless wanderer though he be, In him my lord, my life I see, And, till my earthly days be done, Will cling to great Ikshváku's son.”
- **Translation**: 

---

### Verse 17 (Ramayana 0.1462)
- **Original**: 1444 The Ramayana Then with fierce eyes on Sítá set They cried again with taunt and threat: Each licking with her fiery tongue The lip that to her bosom hung, And menacing the lady's life With axe, or spear or murderous knife: “Hear, Sítá, and our words obey, Or perish by our hands to-day. Thy love for Raghu's son forsake, And RávaG for thy husband take, Or we will rend thy limbs apart And banquet on thy quivering heart. Now from her body strike the head, And tell the king the dame is dead. Then by our lord's commandment she A banquet for our band shall be. Come, let the wine be quickly brought That frees each heart from saddening thought. Then to the western gate repair, And we will dance and revel there.” Canto XXV. Sítá's Lament. On the bare earth the lady sank, And trembling from their presence shrank Like a strayed fawn, when night is dark, And hungry wolves around her bark.[410]
- **Translation**: 

---

### Verse 18 (Ramayana 0.1463)
- **Original**: Canto XXV. Sítá's Lament. 1445 Then to a shady tree she crept, And thought upon her lord and wept. By fear and bitter woe oppressed She bathed the beauties of her breast With her hot tears' incessant flow, And found no respite from her woe. As shakes a plantain in the breeze She shook, and fell on trembling knees; While at each demon's furious look Her cheek its native hue forsook. She lay and wept and made her moan In sorrow's saddest undertone, And, wild with grief, with fear appalled, On Ráma and his brother called: “O dear Kau[alyá,842 hear me cry! Sweet Queen Sumitrá,843 list my sigh! True is the saw the wise declare: Death comes not to relieve despair. 'Tis vain for dame or man to pray; Death will not hear before his day; Since I, from Ráma's sight debarred, And tortured by my cruel guard, Still live in hopeless woe to grieve And loathe the life I may not leave, Here, like a poor deserted thing, My limbs upon the ground I fling, And, like a bark beneath the blast, Shall sink oppressed with woes at last. Ah, blest are they, supremely blest, Whose eyes upon my lord may rest; Who mark his lion port, and hear His gentle speech that charms the ear. 842 The mother of Ráma. 843 The mother of LakshmaG.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1464)
- **Original**: 1446 The Ramayana Alas, what antenatal crime, What trespass of forgotten time Weighs on my soul, and bids me bow Beneath this load of misery now?” Canto XXVI. Sítá's Lament. “I Ráma's wife, on that sad day, By RávaG's arm was borne away, Seized, while I sat and feared no ill, By him who wears each form at will. A helpless captive, left forlorn To demons' threats and taunts and scorn, Here for my lord I weep and sigh, And worn with woe would gladly die. For what is life to me afar From Ráma of the mighty car? The robber in his fruitless sin Would hope his captive's love to win. My meaner foot shall never touch The demon whom I loathe so much. The senseless fool! he knows me not, Nor the proud soul his love would blot. Yea, limb from limb will I be rent, But never to his prayer consent; Be burnt and perish in the fire, But never meet his base desire. My lord was grateful, true and wise, And looked on woe with pitying eyes; But now, recoiling from the strife He pities not his captive wife.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1465)
- **Original**: Canto XXVII. Trijatá's Dream. 1447 Alone in Janasthán he slew The thousands of the Rákshas crew. His arm was strong, his heart was brave, Why comes he not to free and save? Why blame my lord in vain surmise? He knows not where his lady lies. O, if he knew, o'er land and sea His feet were swift to set me free; This Lanká, girdled by the deep, Would fall consumed, a shapeless heap, And from each ruined home would rise A Rákshas widow's groans and cries.” Canto XXVII. Trijatá's Dream. Their threats unfeared, their counsel spurned, The demons' breasts with fury burned. Some sought the giant king to bear The tale of Sítá's fixt despair. With threats and taunts renewed the rest Around the weeping lady pressed. But Trijamá, of softer mould, A Rákshas matron wise and old, With pity for the captive moved, In words like these the fiends reproved: “Me, me,” she cried,“eat me, but spare The spouse of Da[aratha's heir. Last night I dreamt a dream; and still The fear and awe my bosom chill; For in that dream I saw foreshown Our race by Ráma's hand o'erthrown.
- **Translation**: 

---

