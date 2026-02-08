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

### Verse 1 (Ramayana 0.646)
- **Original**: 628 The Ramayana No grateful incense loads the air, And all therein, with brows o'ercast, Sit joyless on the ground and fast. Their lovely chaplets dry and dead,[180] Their courts unswept, with dust o'erspread, The temples of the Gods to-day No more look beautiful and gay. Neglected stands each holy shrine, Each image of a Lord divine. No shop where flowery wreaths are sold Is bright and busy as of old. The women and the men I mark Absorbed in fancies dull and dark, Their gloomy eyes with tears bedewed, A poor afflicted multitude.” His mind oppressed with woe and dread, Thus Bharat to his driver said, Viewed the dire signs Ayodhyá showed, And onward to the palace rode. Canto LXXII. Bharat's Inquiry. He entered in, he looked around, Nor in the house his father found; Then to his mother's dwelling, bent To see her face, he quickly went. She saw her son, so long away, Returning after many a day, And from her golden seat in joy Sprung forward to her darling boy.
- **Translation**: 

---

### Verse 2 (Ramayana 0.647)
- **Original**: Canto LXXII. Bharat's Inquiry. 629 Within the bower, no longer bright, Came Bharat lover of the right, And bending with observance sweet Clasped his dear mother's lovely feet. Long kisses on his brow she pressed, And held her hero to her breast, Then fondly drew him to her knees, And questioned him in words like these: “How many nights have fled, since thou Leftest thy grandsire's home, till now? By flying steeds so swiftly borne, Art thou not weak and travel-worn? How fares the king my father, tell: Is Yudhájit thine uncle well? And now, my son, at length declare The pleasure of the visit there.” Thus to the offspring of the king She spake with tender questioning, And to his mother made reply Young Bharat of the lotus eye: “The seventh night has come and fled Since from my grandsire's home I sped: My mother's sire is well, and he, Yudhájit, from all trouble free. The gold and every precious thing Presented by the conqueror king, The slower guards behind convey: I left them weary on the way. Urged by the men my father sent, My hasty course I hither bent: Now, I implore, an answer deign, And all I wish to know, explain. Unoccupied I now behold
- **Translation**: 

---

### Verse 3 (Ramayana 0.648)
- **Original**: 630 The Ramayana This couch of thine adorned with gold, And each of King Ikshváku's race Appears with dark and gloomy face. The king is aye, my mother dear, Most constant in his visits here. To meet my sire I sought this spot: How is it that I find him not? I long to clasp my father's feet: Say where he lingers, I entreat. Perchance the monarch may be seen Where dwells Kau[alyá, eldest queen.” His father's fate, from him concealed, Kaikeyí to her son revealed: Told as glad news the story sad, For lust of sway had made her mad: “Thy father, O my darling, know, Has gone the way all life must go: Devout and famed, of lofty thought, In whom the good their refuge sought.” When Bharat pious, pure, and true, Heard the sad words which pierced him through, Grieved for the sire he loved so well Prostrate upon the ground he fell: Down fell the strong-armed hero, high Tossing his arms, and a sad cry, “Ah, woe is me, unhappy, slain!” Burst from his lips again, again, Afflicted for his father's fate By grief's intolerable weight, With every sense amazed and cowed The splendid hero wailed aloud: “Ah me, my royal father's bed
- **Translation**: 

---

### Verse 4 (Ramayana 0.649)
- **Original**: Canto LXXII. Bharat's Inquiry. 631 Of old a gentle radiance shed, Like the pure sky when clouds are past, And the moon's light is o'er it cast: Ah, of its wisest lord bereft, It shows to-day faint radiance left, As when the moon has left the sky. Or mighty Ocean's depths are dry.” With choking sobs, with many a tear, Pierced to the heart with grief sincere, The best of conquerors poured his sighs, And with his robe veiled face and eyes. Kaikeyí saw him fallen there, Godlike, afflicted, in despair, Used every art to move him thence, And tried him thus with eloquence: “Arise, arise, my dearest; why Wilt thou, famed Prince, so lowly lie? Not by such grief as this are moved Good men like thee, by all approved. The earth thy father nobly swayed, And rites to Heaven he duly paid. At length his race of life was run: Thou shouldst not mourn for him, my son.” Long on the ground he wept, and rolled From side to side, still unconsoled, And then, with bitter grief oppressed, His mother with these words addressed: [181]
- **Translation**: 

---

### Verse 5 (Ramayana 0.650)
- **Original**: 632 The Ramayana “This joyful hope my bosom fed When from my grandsire's halls I sped— “The king will throne his eldest son, And sacrifice, as should be done.” But all is changed, my hope was vain, And this sad heart is rent in twain, For my dear father's face I miss, Who ever sought his loved ones' bliss. But in my absence, mother, say, What sickness took my sire away? Ah, happy Ráma, happy they Allowed his funeral rites to pay! The glorious monarch has not learned That I his darling have returned, Or quickly had he hither sped, And pressed his kisses on my head. Where is that hand whose gentle touch, Most soft and kind I loved so much, The hand that loved to brush away The dust that on his darling lay? Quick, bear the news to Ráma's ear; Tell the great chief that I am here: Brother, and sire, and friend, and all Is he, and I his trusty thrall. For noble hearts, to virtue true, Their sires in elder brothers view. To clasp his feet I fain would bow: He is my hope and refuge now. What said my glorious sire, who knew Virtue and vice, so brave and true? Firm in his vows, dear lady, say, What said he ere he passed away? What was his rede to me? I crave To hear the last advice he gave.”
- **Translation**: 

---

### Verse 6 (Ramayana 0.651)
- **Original**: Canto LXXII. Bharat's Inquiry. 633 Thus closely questioned by the youth, Kaikeyí spoke the mournful truth: “The high-souled monarch wept and sighed, For Ráma, Sítá, LakshmaG, cried, Then, best of all who go to bliss, Passed to the world which follows this. “Ah, blessed are the people who Shall Ráma and his Sítá view, And Lakshma G of the mighty arm, Returning free from scathe and harm.” Such were the words, the last of all, Thy father, ere he died, let fall, By Fate and Death's dread coils enwound, As some great elephant is bound.” He heard, yet deeper in despair, Her lips this double woe declare, And with sad brow that showed his pain Questioned his mother thus again: “But where is he, of virtue tried, Who fills Kau[alyá's heart with pride, Where is the noble Ráma? where Is LakshmaG brave, and Sítá fair?” Thus pressed, the queen began to tell The story as each thing befell, And gave her son in words like these, The mournful news she meant to please: “The prince is gone in hermit dress To DaG ak's mighty wilderness, And Lakshma G brave and Sítá share The wanderings of the exile there.”
- **Translation**: 

---

### Verse 7 (Ramayana 0.652)
- **Original**: 634 The Ramayana Then Bharat's soul with fear was stirred Lest Ráma from the right had erred, And jealous for ancestral fame, He put this question to the dame: “Has Ráma grasped with lawless hold A Bráhman's house, or land, or gold? Has Ráma harmed with ill intent Some poor or wealthy innocent? Was Ráma, faithless to his vows, Enamoured of anothers spouse? Why was he sent to DaG ak's wild, Like one who kills an unborn child?” He questioned thus: and she began To tell her deeds and crafty plan. Deceitful-hearted, fond, and blind As is the way of womankind: “No Bráhman's wealth has Ráma seized, No dame his wandering fancy pleased; His very eyes he ne'er allows To gaze upon a neighbour's spouse. But when I heard the monarch planned To give the realm to Ráma's hand, I prayed that Ráma hence might flee, And claimed the throne, my son, for thee. The king maintained the name he bare, And did according to my prayer, And Ráma, with his brother, sent, And Sítá, forth to banishment. When his dear son was seen no more, The lord of earth was troubled sore: Too feeble with his grief to strive, He joined the elemental Five. Up then, most dutiful! maintain
- **Translation**: 

---

### Verse 8 (Ramayana 0.653)
- **Original**: Canto LXXIII. Kaikeyí Reproached. 635 The royal state, arise, and reign. For thee, my darling son, for thee All this was planned and wrought by me. Come, cast thy grief and pain aside, With manly courage fortified. This town and realm are all thine own, And fear and grief are here unknown. Come, with Va[ishmha's guiding aid, And priests in ritual skilled Let the king's funeral dues be paid, And every claim fulfilled. Perform his obsequies with all That suits his rank and worth, Then give the mandate to install Thyself as lord of earth.” Canto LXXIII. Kaikeyí Reproached. But when he heard the queen relate His brothers' doom, his father's fate, Thus Bharat to his mother said With burning grief disquieted: [182] “Alas, what boots it now to reign, Struck down by grief and well-nigh slain? Ah, both are gone, my sire, and he Who was a second sire to me. Grief upon grief thy hand has made, And salt upon gashes laid: For my dear sire has died through thee, And Ráma roams a devotee. Thou camest like the night of Fate
- **Translation**: 

---

### Verse 9 (Ramayana 0.654)
- **Original**: 636 The Ramayana This royal house to devastate. Unwitting ill, my hapless sire Placed in his bosom coals of fire, And through thy crimes his death he met, O thou whose heart on sin is set. Shame of thy house! thy senseless deed Has reft all joy from Raghu's seed. The truthful monarch, dear to fame, Received thee as his wedded dame, And by thy act to misery doomed Has died by flames of grief consumed. Kau [alyá and Sumitrá too The coming of my mother rue, And if they live oppressed by woe, For their dear sons their sad tears flow. Was he not ever good and kind,— That hero of the duteous mind? Skilled in all filial duties, he As a dear mother treated thee. Kau [alyá too, the eldest queen, Who far foresees with insight keen, Did she not ever show thee all A sister's love at duty's call? And hast thou from the kingdom chased Her son, with bark around his waist, To the wild wood, to dwell therein, And dost not sorrow for thy sin? The love I bare to Raghu's son Thou knewest not, ambitious one, If thou hast wrought this impious deed For royal sway, in lawless greed. With him and LakshmaG far away, What power have I the realm to sway? What hope will fire my bosom when
- **Translation**: 

---

### Verse 10 (Ramayana 0.655)
- **Original**: Canto LXXIII. Kaikeyí Reproached. 637 I see no more these lords of men? The holy king, who loved the right Relied on Ráma's power and might, His guardian and his glory, so Joys Meru in his woods below. How can I bear, a steer untrained, The load his mightier strength sustained? What power have I to brook alone This weight on feeble shoulders thrown? But if the needful power were bought By strength of mind and brooding thought, No triumph shall attend the dame Who dooms her son to lasting shame. Now should no doubt that son prevent From quitting thee on evil bent. But Ráma's love o'erpowers my will, Who holds thee as his mother still. Whence did the thought, O thou whose eyes Are turned to sinful deeds, arise— A plan our ancient sires would hate, O fallen from thy virtuous state? For in the line from which we spring The eldest is anointed king: No monarchs from the rule decline, And, least of all, Ikshváku's line. Our holy sires, to virtue true, Upon our race a lustre threw, But with subversive frenzy thou Hast marred our lineal honour now, Of lofty birth, a noble line Of previous kings is also thine: Then whence this hated folly? whence This sudden change that steals thy sense? Thou shalt not gain thine impious will,
- **Translation**: 

---

### Verse 11 (Ramayana 0.656)
- **Original**: 638 The Ramayana O thou whose thoughts are bent on ill, Thou from whose guilty hand descend These sinful blows my life to end. Now to the forest will I go, Thy cherished plans to overthrow, And bring my brother, free from stain, His people's darling, home again. And Ráma, when again he turns, Whose glory like a beacon burns, In me a faithful slave shall find To serve him with contented mind.” Canto LXXIV. Bharat's Lament. When Bharat's anger-sharpened tongue Reproaches on the queen had flung, Again, with mighty rage possessed, The guilty dame he thus addressed: “Flee, cruel, wicked sinner, flee, Let not this kingdom harbour thee. Thou who hast thrown all right aside, Weep thou for me when I have died. Canst thou one charge against the king, Or the most duteous Ráma bring? The one thy sin to death has sent, The other chased to banishment. Our line's destroyer, sin defiled Like one who kills an unborn child, Ne'er with thy lord in heaven to dwell, Thy portion shall be down in hell Because thy hand, that stayed for naught,
- **Translation**: 

---

### Verse 12 (Ramayana 0.657)
- **Original**: Canto LXXIV. Bharat's Lament. 639 This awful wickedness has wrought, And ruined him whom all held dear, My bosom too is stirred with fear. My father by thy sin is dead, And Ráma to the wood is fled; And of thy deed I bear the stain, And fameless in the world remain. Ambitious, evil-souled, in show My mother, yet my direst foe. My throning ne'er thine eyes shall bless, Thy husband's wicked murderess. [183] Thou art not A[vapati's child, That righteous king most sage and mild, But thou wast born a fiend, a foe My father's house to overthrow. Thou who hast made Kau[alyá, pure, Gentle, affectionate, endure The loss of him who was her bliss,— What worlds await thee, Queen, for this? Was it not patent to thy sense That Ráma was his friends' defence, Kau [alyá's own true child most dear, The eldest and his father's peer? Men in the son not only trace The father's figure, form, and face, But in his heart they also find The offspring of the father's mind; And hence, though dear their kinsmen are, To mothers sons are dearer far. There goes an ancient legend how Good Surabhí, the God-loved cow, Saw two of her dear children strain, Drawing a plough and faint with pain. She saw them on the earth outworn,
- **Translation**: 

---

### Verse 13 (Ramayana 0.658)
- **Original**: 640 The Ramayana Toiling till noon from early morn, And as she viewed her children's woe, A flood of tears began to flow. As through the air beneath her swept The Lord of Gods, the drops she wept, Fine, laden with delicious smell, Upon his heavenly body fell. And Indra lifted up his eyes And saw her standing in the skies, Afflicted with her sorrow's weight, Sad, weeping, all disconsolate. The Lord of Gods in anxious mood Thus spoke in suppliant attitude: “No fear disturbs our rest, and how Come this great dread upon thee now? Whence can this woe upon thee fall, Say, gentle one who lovest all?” Thus spake the God who rules the skies, Indra, the Lord supremely wise; And gentle Surabhí, well learned In eloquence, this speech returned: “Not thine the fault, great God, not thine And guiltless are the Lords divine: I mourn two children faint with toil, Labouring hard in stubborn soil. Wasted and sad I see them now, While the sun beats on neck and brow, Still goaded by the cruel hind,— No pity in his savage mind. O Indra, from this body sprang These children, worn with many a pang. For this sad sight I mourn, for none Is to the mother like her son.”
- **Translation**: 

---

### Verse 14 (Ramayana 0.659)
- **Original**: Canto LXXIV. Bharat's Lament. 641 He saw her weep whose offspring feed In thousands over hill and mead, And knew that in a mother's eye Naught with a son, for love, can vie. He deemed her, when the tears that came From her sad eyes bedewed his frame, Laden with their celestial scent, Of living things most excellent. If she these tears of sorrow shed Who many a thousand children bred, Think what a life of woe is left Kau [alyá, of her Ráma reft. An only son was hers and she Is rendered childless now by thee. Here and hereafter, for thy crime, Woe is thy lot through endless time. And now, O Queen, without delay, With all due honour will I pay Both to my brother and my sire The rites their several fates require. Back to Ayodhyá will I bring The long-armed chief, her lord and king, And to the wood myself betake Where hermit saints their dwelling make. For, sinner both in deed and thought! This hideous crime which thou hast wrought I cannot bear, or live to see The people's sad eyes bent on me. Begone, to DaG ak wood retire, Or cast thy body to the fire, Or bind around thy neck the rope: No other refuge mayst thou hope. When Ráma, lord of valour true, Has gained the earth, his right and due,
- **Translation**: 

---

### Verse 15 (Ramayana 0.660)
- **Original**: 642 The Ramayana Then, free from duty's binding debt, My vanished sin shall I forget.” Thus like an elephant forced to brook The goading of the driver's hook, Quick panting like a serpent maimed, He fell to earth with rage inflamed. Canto LXXV. The Abjuration. A while he lay: he rose at length, And slowly gathering sense and strength, With angry eyes which tears bedewed, The miserable queen he viewed, And spake with keen reproach to her Before each lord and minister: “No lust have I for kingly sway, My mother I no more obey: Naught of this consecration knew Which Da[aratha kept in view. I withZatrughna all the time Was dwelling in a distant clime: I knew of Ráma's exile naught, That hero of the noble thought: I knew not how fair Sítá went, And Lakshma G, forth to banishment.”
- **Translation**: 

---

### Verse 16 (Ramayana 0.661)
- **Original**: Canto LXXV. The Abjuration. 643 Thus high-souled Bharat, mid the crowd, Lifted his voice and cried aloud.[184] Kau [alyá heard, she raised her head, And quickly to Sumitrá said: “Bharat, Kaikeyí's son is here,— Hers whose fell deeds I loathe and fear: That youth of foresight keen I fain Would meet and see his face again.” Thus to Sumitrá spake the dame, And straight to Bharat's presence came With altered mien, neglected dress, Trembling and faint with sore distress. Bharat,Zatrughna by his side, To meet her, toward her palace hied. And when the royal dame they viewed Distressed with dire solicitude, Sad, fallen senseless on the ground, About her neck their arms they wound. The noble matron prostrate there, Embraced, with tears, the weeping pair, And with her load of grief oppressed, To Bharat then these words addressed: “Now all is thine, without a foe, This realm for which thou longest so. Ah, soon Kaikeyí's ruthless hand Has won the empire of the land, And made my guiltless Ráma flee Dressed like some lonely devotee. Herein what profit has the queen, Whose eye delights in havoc, seen? Me also, me 'twere surely good To banish to the distant wood, To dwell amid the shades that hold My famous son with limbs like gold.
- **Translation**: 

---

### Verse 17 (Ramayana 0.662)
- **Original**: 644 The Ramayana Nay, with the sacred fire to guide, Will I, Sumitrá by my side, Myself to the drear wood repair And seek the son of Raghu there. This land which rice and golden corn And wealth of every kind adorn, Car, elephant, and steed, and gem,— She makes thee lord of it and them.” With taunts like these her bitter tongue The heart of blameless Bharat wrung And direr pangs his bosom tore Than when the lancet probes a sore. With troubled senses all astray Prone at her feet he fell and lay. With loud lament a while he plained, And slowly strength and sense regained. With suppliant hand to hand applied He turned to her who wept and sighed, And thus bespake the queen, whose breast With sundry woes was sore distressed: “Why these reproaches, noble dame? I, knowing naught, am free from blame. Thou knowest well what love was mine For Ráma, chief of Raghu's line. O, never be his darkened mind To Scripture's guiding lore inclined, By whose consent the prince who led The good, the truthful hero, fled. May he obey the vilest lord, Offend the sun with act abhorred,350 And strike a sleeping cow, who lent 350 Súryamcha pratimehatu, adversus solem mingat. An offence expressly forbidden by the Laws of Manu.
- **Translation**: 

---

### Verse 18 (Ramayana 0.663)
- **Original**: Canto LXXV. The Abjuration. 645 His voice to Ráma's banishment. May the good king who all befriends, And, like his sons, the people tends, Be wronged by him who gave consent To noble Ráma's banishment. On him that king's injustice fall, Who takes, as lord, a sixth of all, Nor guards, neglectful of his trust, His people, as a ruler must. The crime of those who swear to fee, At holy rites, some devotee, And then the promised gift deny, Be his who willed the prince should fly. When weapons clash and heroes bleed, With elephant and harnessed steed, Ne'er, like the good, be his to fight Whose heart allowed the prince's flight. Though taught with care by one expert May he the Veda's text pervert, With impious mind on evil bent, Whose voice approved the banishment. May he with traitor lips reveal Whate'er he promised to conceal, And bruit abroad his friend's offence, Betrayed by generous confidence. No wife of equal lineage born The wretch's joyless home adorn: Ne'er may he do one virtuous deed, And dying see no child succeed. When in the battle's awful day Fierce warriors stand in dread array, Let the base coward turn and fly, And smitten by the foeman, die. Long may he wander, rags his wear,
- **Translation**: 

---

### Verse 19 (Ramayana 0.664)
- **Original**: 646 The Ramayana Doomed in his hand a skull to bear, And like an idiot beg his bread, Who gave consent when Ráma fled. His sin who holy rites forgets, Asleep when shows the sun and sets, A load upon his soul shall lie Whose will allowed the prince to fly. His sin who loves his Master's dame, His, kindler of destructive flame, His who betrays his trusting friend Shall, mingled all, on him descend. By him no reverence due be paid To blessed God or parted shade: May sire and mother's sacred name In vain from him obedience claim. Ne'er may he go where dwell the good, Nor win their fame and neighbourhood, But lose all hopes of bliss to-day, Who willed the prince should flee away. May he deceive the poor and weak Who look to him and comfort seek,[185] Betray the suppliants who complain, And make the hopeful hope in vain. Long may his wife his kiss expect, And pine away in cold neglect. May he his lawful love despise, And turn on other dames his eyes, Fool, on forbidden joys intent, Whose will allowed the banishment. His sin who deadly poison throws To spoil the water as it flows, Lay on the wretch its burden dread Who gave consent when Ráma fled.”351 351 Bharat does not intend these curses for any particular person: he merely
- **Translation**: 

---

### Verse 20 (Ramayana 0.665)
- **Original**: Canto LXXV. The Abjuration. 647 Thus with his words he undeceived Kau [alyá's troubled heart, who grieved For son and husband reft away; Then prostrate on the ground he lay. Him as he lay half-senseless there, Freed by the mighty oaths he sware, Kau [alyá, by her woe distressed, With melancholy words addressed: “Anew, my son, this sorrow springs To rend my heart with keener stings: These awful oaths which thou hast sworn My breast with double grief have torn. Thy soul, and faithful LakshmaG's too, Are still, thank Heaven! to virtue true. True to thy promise, thou shalt gain The mansions which the good obtain.” Then to her breast that youth she drew, Whose sweet fraternal love she knew, And there in strict embraces held The hero, as her tears outwelled. And Bharat's heart grew sick and faint With grief and oft-renewed complaint, And all his senses were distraught By the great woe that in him wrought. Thus he lay and still bewailed With sighs and loud lament Till all his strength and reason failed, The hours of night were spent. wishes to prove his own innocence by invoking them on his own head if he had any share in banishing Ráma.
- **Translation**: 

---

