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

### Verse 1 (Ramayan 0.781)
- **Original**: Canto CVIII. Jáváli's Speech. 763 The man, I ween, has little sense Who looks with foolish reverence On father's or on mother's name: In others, none a right may claim. E'en as a man may leave his home And to a distant village roam, Then from his lodging turn away And journey on the following day, Such brief possession mortals hold In sire and mother, house and gold, And never will the good and wise The brief uncertain lodging prize. Nor, best of men, shouldst thou disown Thy sire's hereditary throne, And tread the rough and stony ground Where hardship, danger, woes abound. Come, let Ayodhyá rich and bright See thee enthroned with every rite: Her tresses bound in single braid387 She waits thy coming long delayed. O come, thou royal Prince, and share The kingly joys that wait thee there, And live in bliss transcending price As Indra lives in Paradise. The parted king is naught to thee, Nor right in living man has he: The king is one, thou, Prince of men, Another art: be counselled then. Thy royal sire, O chief, has sped On the long path we all must tread. The common lot of all is this, 387 It was the custom of Indian women when mourning for their absent husbands to bind their hair in a long single braid. Carey and Marshman translate,“the one-tailed city.”
- **Translation**: 

---

### Verse 2 (Ramayan 0.782)
- **Original**: 764 The Ramayana And thou in vain art robbed of bliss. For those— and only those— I weep Who to the path of duty keep; For here they suffer ceaseless woe, And dying to destruction go. With pious care, each solemn day, Will men their funeral offerings pay: See, how the useful food they waste: He who is dead no more can taste. If one is fed, his strength renewed Whene'er his brother takes his food, Then offerings to the parted pay: Scarce will they serve him on his way. By crafty knaves these rules were framed, And to enforce men's gifts proclaimed: “Give, worship, lead a life austere, Keep lustral rites, quit pleasures here.” There is no future life: be wise, And do, O Prince, as I advise. Enjoy, my lord, the present bliss, And things unseen from thought dismiss. Let this advice thy bosom move, The counsel sage which all approve; To Bharat's earnest prayer incline, And take the rule so justly thine.” Canto CIX. The Praises Of Truth. By sage Jáváli thus addressed, Ráma of truthful hearts the best,[218]
- **Translation**: 

---

### Verse 3 (Ramayan 0.783)
- **Original**: Canto CIX. The Praises Of Truth. 765 With perfect skill and wisdom high Thus to his speech made fit reply: “Thy words that tempt to bliss are fair, But virtue's garb they falsely wear. For he from duty's path who strays To wander in forbidden ways, Allured by doctrine false and vain, Praise from the good can never gain. Their lives the true and boaster show, Pure and impure, and high and low, Else were no mark to judge between Stainless and stained and high and mean; They to whose lot fair signs may fall Were but as they who lack them all, And those to virtuous thoughts inclined Were but as men of evil mind. If in the sacred name of right I do this wrong in duty's spite; The path of virtue meanly quit, And this polluting sin commit, What man who marks the bounds between Virtue and vice with insight keen, Would rank me high in after time Stained with this soul destroying crime? Whither could I, the sinner, turn, How hope a seat in heaven to earn, If I my plighted promise break, And thus the righteous path forsake? This world of ours is ever led To walk the ways which others tread, And as their princes they behold, The subjects too their lives will mould. That truth and mercy still must be Beloved of kings, is Heaven's decree.
- **Translation**: 

---

### Verse 4 (Ramayan 0.784)
- **Original**: 766 The Ramayana Upheld by truth the monarch reigns, And truth the very world sustains. Truth evermore has been the love Of holy saints and Gods above, And he whose lips are truthful here Wins after death the highest sphere. As from a serpent's deadly tooth, We shrink from him who scorns the truth. For holy truth is root and spring Of justice and each holy thing, A might that every power transcends, Linked to high bliss that never ends. Truth is all virtue's surest base, Supreme in worth and first in place. Oblations, gifts men offer here, Vows, sacrifice, and rites austere, And Holy Writ, on truth depend: So men must still that truth defend. Truth, only truth protects the land, By truth unharmed our houses stand; Neglect of truth makes men distressed, And truth in highest heaven is blessed. Then how can I, rebellious, break Commandments which my father spake— I ever true and faithful found, And by my word of honour bound? My father's bridge of truth shall stand Unharmed by my destructive hand: Not folly, ignorance, or greed My darkened soul shall thus mislead. Have we not heard that God and shade Turn from the hated offerings paid By him whose false and fickle mind No pledge can hold, no promise bind?
- **Translation**: 

---

### Verse 5 (Ramayan 0.785)
- **Original**: Canto CIX. The Praises Of Truth. 767 Truth is all duty: as the soul, It quickens and supports the whole. The good respect this duty: hence Its sacred claims I reverence. The Warrior's duty I despise That seeks the wrong in virtue's guise: Those claims I shrink from, which the base, Cruel, and covetous embrace. The heart conceives the guilty thought, Then by the hand the sin is wrought, And with the pair is leagued a third, The tongue that speaks the lying word. Fortune and land and name and fame To man's best care have right and claim; The good will aye to truth adhere, And its high laws must men revere. Base were the deed thy lips would teach, Approved as best by subtle speech. Shall I my plighted promise break, That I these woods my home would make? Shall I, as Bharat's words advise, My father's solemn charge despise? Firm stands the oath which then before My father's face I soothly swore, Which Queen Kaikeyí's anxious ear Rejoiced with highest joy to hear. Still in the wood will I remain, With food prescribed my life sustain, And please with fruit and roots and flowers Ancestral shades and heavenly powers. Here every sense contented, still Heeding the bounds of good and ill, My settled course will I pursue, Firm in my faith and ever true.
- **Translation**: 

---

### Verse 6 (Ramayan 0.786)
- **Original**: 768 The Ramayana Here in this wild and far retreat Will I my noble task complete; And Fire and Wind and Moon shall be Partakers of its fruit with me. A hundred offerings duly wrought His rank o'er Gods for Indra bought, And mighty saints their heaven secured By torturing years on earth endured.” That scoffing plea the hero spurned, And thus he spake once more, Chiding, the while his bosom burned, Jáváli's impious lore: “Justice, and courage ne'er dismayed, Pity for all distressed, Truth, loving honour duly paid To Bráhman, God, and guest— In these, the true and virtuous say, Should lives of men be passed: They form the right and happy way That leads to heaven at last.[219] My father's thoughtless act I chide That gave thee honoured place, Whose soul, from virtue turned aside, Is faithless, dark, and base. We rank the Buddhist with the thief,388 And all the impious crew Who share his sinful disbelief, And hate the right and true. Hence never should wise kings who seek To rule their people well, Admit, before their face to speak, 388 The verses in a different metre with which some cantos end are all to be regarded with suspicion. Schlegel regrets that he did not exclude them all from his edition. These lines are manifestly spurious. SeeAdditional Notes.
- **Translation**: 

---

### Verse 7 (Ramayan 0.787)
- **Original**: Canto CIX. The Praises Of Truth. 769 The cursed infidel. But twice-born men in days gone by, Of other sort than thou, Have wrought good deeds, whose glories high Are fresh among us now: This world they conquered, nor in vain They strove to win the skies: The twice-born hence pure lives maintain, And fires of worship rise. Those who in virtue's path delight, And with the virtuous live,— Whose flames of holy zeal are bright, Whose hands are swift to give, Who injure none, and good and mild In every grace excel, Whose lives by sin are undefiled, We love and honour well.” Thus Ráma spoke in righteous rage Jáváli's speech to chide, When thus again the virtuous sage In truthful words replied: “The atheist's lore I use no more, Not mine his impious creed: His words and doctrine I abhor, Assumed at time of need. E'en as I rose to speak with thee, The fit occasion came That bade me use the atheist's plea To turn thee from thine aim. The atheist creed I disavow, Unsay the words of sin, And use the faithful's language now Thy favour, Prince, to win.”
- **Translation**: 

---

### Verse 8 (Ramayan 0.788)
- **Original**: 770 The Ramayana Canto CX. The Sons Of Ikshváku.389 Then spake Va[ishmha who perceived That Ráma's soul was wroth and grieved: “Well knows the sage Jáváli all The changes that the world befall; And but to lead thee to revoke Thy purpose were the words he spoke. Lord of the world, now hear from me How first this world began to be. First water was, and naught beside; There earth was formed that stretches wide. Then with the Gods from out the same The Self-existent Brahmá came. Then Brahmá390 in a boar's disguise Bade from the deep this earth arise; Then, with his sons of tranquil soul, He made the world and framed the whole. From subtlest ether Brahmá rose: No end, no loss, no change he knows. A son had he, Maríchi styled, And Ka [yap was Maríchi's child. From him Vivasvat sprang: from him Manu, whose fame shall ne'er be dim. Manu, who life to mortals gave, Begot Ikshváku good and brave: First of Ayodhyá's kings was he, Pride of her famous dynasty. From him the glorious Kukshi sprang, 389 This genealogy is a repetition with slight variation of that given in Book I, Canto LXX. 390 In Gorresio's recension identified with VishGu. See Muir'sSanskrit Texts, Vol. IV. pp 29, 30.
- **Translation**: 

---

### Verse 9 (Ramayan 0.789)
- **Original**: Canto CX. The Sons Of Ikshváku. 771 Whose fame through all the regions rang. Rival of Kukshi's ancient fame, His heir the great Vikukshi came. His son was VáGa, lord of might, His AnaraGya, strong in fight. No famine marred his blissful reign, No drought destroyed the kindly grain; Amid the sons of virtue chief, His happy realm ne'er held a thief, His son was Prithu, glorious name, From him the wise Tri[anku came: Embodied to the skies he went For love of truth preëminent. He left a son renowned afar, Known by the name of Dhundhumár. His son succeeding bore the name Of Yuvaná[va dear to fame. He passed away. Him followed then His son Mándhátá, king of men. His son was blest in high emprise, Susandhi, fortunate and wise. Two noble sons had he, to wit Dhruvasandhi and Prasenajit. Bharat was Dhruvasandhi's son: His glorious arm the conquest won, Against his son King Asit, rose In fierce array his royal foes, Haihayas, Tálajanghas styled, And Za[ivindhus fierce and wild. [220] Long time he strove, but forced to yield Fled from his kingdom and the field. The wives he left had both conceived— So is the ancient tale believed:— One, of her rival's hopes afraid,
- **Translation**: 

---

### Verse 10 (Ramayan 0.790)
- **Original**: 772 The Ramayana Fell poison in the viands laid. It chanced that Chyavan, Bhrigu's child, Had wandered to the pathless wild Where proud Himálaya's lovely height Detained him with a strange delight. Then came the other widowed queen With lotus eyes and beauteous mien, Longing a noble son to bear, And wooed the saint with earnest prayer. When thus Kálindí, fairest dame With reverent supplication came, To her the holy sage replied: “O royal lady, from thy side A glorious son shall spring ere long, Righteous and true and brave and strong; He, scourge of foes and lofty-souled, His ancient race shall still uphold.” Then round the sage the lady went, And bade farewell, most reverent. Back to her home she turned once more, And there her promised son she bore. Because her rival mixed the bane To render her conception vain, And her unripened fruit destroy, Sagar she called her rescued boy.391 He, when he paid that solemn rite,392 Filled living creatures with affright: Obedient to his high decree His countless sons dug out the sea. Prince Asamanj was Sagar's child: But him with cruel sin defiled 391 From sa with, andgara poison. 392 See Book I. Canto XL.
- **Translation**: 

---

### Verse 11 (Ramayan 0.791)
- **Original**: Canto CX. The Sons Of Ikshváku. 773 And loaded with the people's hate His father banished from the state. To Asamanj his consort bare Bright An[umán his valiant heir. An [umán's son, Dilípa famed, Begot a son Bhagírath named. From him renowned Kakutstha came: Thou bearest still the lineal name. Kakutstha's son was Raghu: thou Art styled the son of Raghu now. From him came Purushádak bold, Fierce hero of gigantic mould: Kalmáshapáda's name he bore, Because his feet were spotted o'er. Zankhan his son, to manhood grown, Died sadly with his host o'erthrown, But ere he perished sprang from him Sudar[an fair in face and limb. From beautiful Sudar[an came Prince AgnivarGa, bright as flame. His son wasZíghraga, for speed Unmatched; and Maru was his seed. Prasusruka was Maru's child: His son was Ambarísha styled. Nahush was Ambarísha's heir With hand to strike and heart to dare. His son was good Nábhág, from youth Renowned for piety and truth. From great Nábhág sprang children two Aja and Suvrat pure and true. From Aja Da[aratha came, Whose virtuous life was free from blame. His eldest son art thou: his throne, O famous Ráma, is thine own.
- **Translation**: 

---

### Verse 12 (Ramayan 0.792)
- **Original**: 774 The Ramayana Accept the sway so justly thine, And view the world with eyes benign. For ever in Ikshváku's race The eldest takes his father's place, And while he lives no son beside As lord and king is sanctified. The rule by Raghu's children kept Thou must not spurn to-day. This realm of peerless wealth accept, And like thy father sway.” Canto CXI. Counsel To Bharat. Thus said Va[ishmha, and again To Ráma spake in duteous strain: “All men the light of life who see With high respect should look on three: High honour ne'er must be denied To father, mother, holy guide. First to their sires their birth they owe, Nursed with maternal love they grow: Their holy guides fair knowledge teach: So men should love and honour each. Thy sire and thou have learned of me, The sacred guide of him and thee, And if my word thou wilt obey Thou still wilt keep the virtuous way. See, with the chiefs of every guild And all thy friends, this place is filled: All these, as duty bids, protect; So still the righteous path respect.
- **Translation**: 

---

### Verse 13 (Ramayan 0.793)
- **Original**: Canto CXI. Counsel To Bharat. 775 O, for thine aged mother feel, Nor spurn the virtuous dame's appeal: Obey, O Prince, thy mother dear, And still to virtue's path adhere. Yield thou to Bharat's fond request, With earnest supplication pressed, So wilt thou to thyself be true, And faith and duty still pursue.” Thus by his saintly guide addressed With pleas in sweetest tones expressed, The lord of men in turn replied To wise Va[ishmha by his side: “The fondest son's observance ne'er Repays the sire and mother's care: [221] The constant love that food provides, And dress, and every need besides: Their pleasant words still soft and mild, Their nurture of the helpless child: The words which Da[aratha spake, My king and sire, I ne'er will break.” Then Bharat of the ample chest The wise Sumantra thus addressed; “Bring sacred grass, O charioteer, And strew it on the level here. For I will sit and watch his face Until I win my brother's grace. Like a robbed Bráhman will I lie,393 Nor taste of food nor turn my eye, In front of Ráma's leafy cot, And till he yield will leave him not.” 393 A practice which has frequently been described, under the name ofdherna, by European travellers in India.
- **Translation**: 

---

### Verse 14 (Ramayan 0.794)
- **Original**: 776 The Ramayana When Bharat saw Sumantra's eye Looked up to Ráma for reply, The Prince himself in eager haste The sacred grass in order placed. Him great and mighty Ráma, best Of royal saints, in turn addressed: “What, Bharat, have I done, that thou Besiegest me,394 a suppliant now? Thus streched, to force redress for wrongs To men of Bráhman birth belongs, Not those upon whose kingly head The consecrating drops are shed. Up, lord of men! arise, and quit This fearful vow for thee unfit. Go, brother, seek Ayodhyá's town, Fair city of supreme renown.” But Bharat, as his seat he took, Cast all around an eager look: “O people, join your prayers with mine, And so his stubborn heart incline.” And all the people answered thus: “Full well is Ráma known to us. Right is the word he speaks and he Is faithful to his sire's decree: Nor can we rashly venture now To turn him from his purposed vow.” 394 Compare Milton's“beseeching or beseiging.”
- **Translation**: 

---

### Verse 15 (Ramayan 0.795)
- **Original**: Canto CXI. Counsel To Bharat. 777 Then Ráma spoke:“O Bharat, heed Thy virtuous friends, and mark their rede. Mark well what I and these advise, And duty view with clearer eyes. Thy hand on mine, O hero, place, Touch water, and thy sin efface.” Then Bharat rose: his hand he dipped, And purifying water sipped: “Each citizen,” he cried,“give ear, Attend, each counsellor and peer. My mother planned, by me untaught, To win the sway I never sought: Ne'er Raghu's son could I despise, In duty's lore supremely wise. Now if obedience to our sire This dwelling in the woods require, I, till the destined years be spent, Will dwell alone in banishment.” The virtuous Ráma, wonder-stirred, The faithful speech of Bharat heard, And thus the hero's feelings found Due utterance, as he gazed around: “Still to my father's word I hold, Whate'er he bought, or pledged, or sold: Ne'er shall his living promise be Annulled by Bharat or by me. Not thus my task will I evade, My exile on another laid: Most wise was Queen Kaikeyí's rede, And just and good my father's deed. Dear Bharat's patient soul I know, How reverence due he loves to show;
- **Translation**: 

---

### Verse 16 (Ramayan 0.796)
- **Original**: 778 The Ramayana In him, high-souled and faithful found, Must each auspicious grace abound. When from the woods I turn again I with his aid shall nobly reign, With one so good, of peerless worth, A glorious lord of happy earth. Her boon Kaikeyí sought and won. I, as my father swore, have done: And O, do thou, my brother dear, The monarch's name from falsehood clear. Canto CXII. The Sandals. High wonder mingled with delight Took the great sages at the sight, Thrilling their breasts who came to view The meeting of the peerless two. The saints and sages' holy train Departed to their home again. And high each holy voice was raised, And thus the glorious brothers praised. “High fate is his, the sire of two Most virtuous souls, so brave and true: With wonder and with joy intense Our ears have heard their conference.” Then the great sages, longing all To see the ten-necked tyrant395 fall, To Bharat, bravest of the brave, Their salutary counsel gave: 395 Ten-headed, ten-necked, ten faced, are common epithets of RávaG the giant king of Lanká.
- **Translation**: 

---

### Verse 17 (Ramayan 0.797)
- **Original**: Canto CXII. The Sandals. 779 “O thou of lofty lineage born, Whom wisdom, conduct, fame adorn, Thou for thy honoured father's sake Shouldst Ráma's righteous counsel take. [222] All debts to Queen Kaikeyí paid, Thy sire his home in heaven has made, So virtuous Ráma we would see From filial obligation free.” Thus gave each royal sage advice, High saint, and bard of Paradise; Then quickly vanishing from view Each to his proper home withdrew. Then Ráma's face his rapture showed, And his full heart with joy o'erflowed, While, as the sages parted thence, He paid his humble reverence. Then Bharat shook in every limb As suppliant thus he spake to him: “The duty of a king respect, Held by our race in high respect: And O, thy gracious ear incline To heed my mother's prayer and mine. The mighty realm to rule and guard For me alone is task too hard. No power have I the love to gain Of noble, citizen, and swain. All those who know thee, warrior, friend, On thee their eager glances bend, As labouring hinds who till the plain Look fondly for the Lord of Rain. O wisest Prince, thy realm secure, And make its firm foundations sure. Kakutstha's son, thy mighty arm
- **Translation**: 

---

### Verse 18 (Ramayan 0.798)
- **Original**: 780 The Ramayana Can keep the nation free from harm.” He spoke, and fell in sorrow drowned At Ráma's feet upon the ground, And there the hero sued and sighed, And “Hear me, Raghu's son,” he cried. Then Ráma raised him up, and pressed His brother to his loving breast, And sweetly as a wild swan cried To Bharat dark and lotus-eyed: “So just and true thy generous soul, Thy hand may well this earth control: But many a sage his aid will lend, With counsellor, and peer, and friend: With these advise: their counsel ask, And so perform thy arduous task. The moon his beauty may forgo, The cold forsake the Hills of Snow, And Ocean o'er his banks may sweep, But I my father's word will keep. Now whether love of thee or greed Thy mother led to plan the deed, Forth from thy breast the memory throw, And filial love and reverence show.” Thus spake Kau[alyá's son: again Bharat replied in humble strain To him who matched the sun in might And lovely as the young moon's light: “Put, noble brother, I entreat, These sandals on thy blessed feet: These, lord of men, with gold bedecked, The realm and people will protect.”
- **Translation**: 

---

### Verse 19 (Ramayan 0.799)
- **Original**: Canto CXII. The Sandals. 781 Then Ráma, as his brother prayed Beneath his feet the sandals laid, And these with fond affection gave To Bharat's hand, the good and brave. Then Bharat bowed his reverent head And thus again to Ráma said: “Through fourteen seasons will I wear The hermit's dress and matted hair: With fruit and roots my life sustain, And still beyond the realm remain, Longing for thee to come again. The rule and all affairs of state I to these shoes will delegate. And if, O tamer of thy foes, When fourteen years have reached their close, I see thee not that day return, The kindled fire my frame shall burn.” Then Ráma to his bosom drew Dear Bharat andZatrughna too: “Be never wroth,” he cried,“with her, Kaikeyí's guardian minister: This, glory of Ikshváku's line, Is Sítá's earnest prayer and mine.” He spoke, and as the big tears fell, To his dear brother bade farewell. Round Ráma, Bharat strong and bold In humble reverence paced, When the bright sandals wrought with gold Above his brows were placed. The royal elephant who led The glorious pomp he found, And on the monster's mighty head Those sandals duly bound.
- **Translation**: 

---

### Verse 20 (Ramayan 0.800)
- **Original**: 782 The Ramayana Then noble Ráma, born to swell The glories of his race, To all in order bade farewell With love and tender grace— To brothers, counsellers, and peers,— Still firm, in duty proved, Firm, as the Lord of Snow uprears His mountains unremoved. No queen, for choking sobs and sighs, Could say her last adieu: Then Ráma bowed, with flooded eyes, And to his cot withdrew. Canto CXIII. Bharat's Return. Bearing the sandals on his head Away triumphant Bharat sped, And clomb,Zatrughna by his side, The car wherein he wont to ride. Before the mighty army went The lords for counsel eminent, Va [ishmha, Vámadeva next, Jáváli, pure with prayer and text.[223] Then from that lovely river they Turned eastward on their homeward way: With reverent steps from left to right They circled Chitrakúma's height, And viewed his peaks on every side With stains of thousand metals dyed. Then Bharat saw, not far away, Where Bharadvája's dwelling lay,
- **Translation**: 

---

