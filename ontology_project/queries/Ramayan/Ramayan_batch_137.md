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

### Verse 1 (Ramayana 0.766)
- **Original**: 748 The Ramayana Draws water hence which mine requires. This day, for lowly toil unfit, His pious task thy son should quit.” As on the long-eyed lady strayed, On holy grass, whose points were laid Directed to the southern sky, The funeral offering met her eye. When Ráma's humble gift she spied Thus to the queens Kau[alyá cried: “The gift of Ráma's hand behold, His tribute to the king high-souled, Offered to him, as texts require, Lord of Ikshváku's line, his sire! Not such I deem the funeral food Of kings with godlike might endued. Can he who knew all pleasures, he Who ruled the earth from sea to sea, The mighty lord of monarchs, feed On Ingudí's extracted seed? In all the world there cannot be A woe, I ween, more sad to see, Than that my glorious son should make His funeral gift of such a cake. The ancient text I oft have heard This day is true in every word: “Ne'er do the blessed Gods refuse To eat the food their children use.’ ” The ladies soothed the weeping dame: To Ráma's hermitage they came, And there the hero met their eyes Like a God fallen from the skies. Him joyless, reft of all, they viewed,
- **Translation**: 

---

### Verse 2 (Ramayana 0.767)
- **Original**: Canto CIV. The Meeting With The Queens. 749 And tears their mournful eyes bedewed. The truthful hero left his seat, And clasped the ladies' lotus feet, And they with soft hands brushed away The dust that on his shoulders lay. Then LakshmaG, when he saw each queen With weeping eyes and troubled mien, Near to the royal ladies drew And paid them gentle reverence too. He, Da[aratha's offspring, signed The heir of bliss by Fortune kind, Received from every dame no less Each mark of love and tenderness. And Sítá came and bent before The widows, while her eyes ran o'er, And pressed their feet with many a tear. They when they saw the lady dear Pale, worn with dwelling in the wild, Embraced her as a darling child: “Daughter of royal Janak, bride Of Da[aratha's son,” they cried, “How couldst thou, offspring of a king, Endure this woe and suffering In the wild forest? When I trace Each sign of trouble on thy face— That lotus which the sun has dried, That lily by the tempest tried, That gold whereon the dust is spread, That moon whence all the light is fled— Sorrow assails my heart, alas! As fire consumes the wood and grass.” Then Ráma, as she spoke distressed, The feet of Saint Va[ishmha pressed,
- **Translation**: 

---

### Verse 3 (Ramayana 0.768)
- **Original**: 750 The Ramayana Touched them with reverential love, Then near him took his seat: Thus Indra clasps in realms above The Heavenly Teacher's380 feet. Then with each counsellor and peer, Bharat of duteous mind, With citizens and captains near, Sat humbly down behind. When with his hands to him upraised, In devotee's attire, Bharat upon his brother gazed Whose glory shone like fire, As when the pure Mahendra bends To the great Lord of Life, Among his noble crowd of friends This anxious thought was rife: “What words to Raghu's son to-day Will royal Bharat speak, Whose heart has been so prompt to pay Obeisance fond and meek?” Then steadfast Ráma, LakshmaG wise, Bharat for truth renowned,[214] Shone like three fires that heavenward rise With holy priests around. Canto CV. Ráma's Speech. 380 V [ihaspati, the preceptor of the Gods.
- **Translation**: 

---

### Verse 4 (Ramayana 0.769)
- **Original**: Canto CV. Ráma's Speech. 751 A while they sat, each lip compressed, Then Bharat thus his chief addressed: “My mother here was made content; To me was given the government. This now, my lord, I yield to thee: Enjoy it, from all trouble free. Like a great bridge the floods have rent, Impetuous in their wild descent, All other hands but thine in vain Would strive the burthen to maintain. In vain the ass with steeds would vie, With Tárkshya,381 birds that wing the sky; So, lord of men, my power is slight To rival thine imperial might. Great joys his happy days attend On whom the hopes of men depend, But wretched is the life he leads Who still the aid of others needs. And if the seed a man has sown, With care and kindly nurture grown, Rear its huge trunk and spring in time Too bulky for a dwarf to climb, Yet, with perpetual blossom gay, No fruit upon its boughs display, Ne'er can that tree, thus nursed in vain, Approval of the virtuous gain. The simile is meant to be Applied, O mighty-armed, to thee, Because, our lord and leader, thou Protectest not thy people now. O, be the longing wish fulfilled Of every chief of house and guild, 381 Garu , the king of birds.
- **Translation**: 

---

### Verse 5 (Ramayana 0.770)
- **Original**: 752 The Ramayana To see again their sun-bright lord Victorious to his realm restored! As thou returnest through the crowd Let roars of elephants be loud. And each fair woman lift her voice And in her new-found king rejoice.” The people all with longing moved, The words that Bharat spoke approved, And crowding near to Ráma pressed The hero with the same request. The steadfast Ráma, when he viewed His glorious brother's mournful mood, With each ambitious thought controlled, Thus the lamenting prince consoled: “I cannot do the things I will, For Ráma is but mortal still. Fate with supreme, resistless law This way and that its slave will draw, All gathered heaps must waste away, All lofty lore and powers decay. Death is the end of life, and all, Now firmly joined, apart must fall. One fear the ripened fruit must know, To fall upon the earth below; So every man who draws his breath Must fear inevitable death. The pillared mansion, high, compact, Must fall by Time's strong hand attacked; So mortal men, the gradual prey Of old and ruthless death, decay. The night that flies no more returns: Yamuná for the Ocean yearns: Swift her impetuous waters flee,
- **Translation**: 

---

### Verse 6 (Ramayana 0.771)
- **Original**: Canto CV. Ráma's Speech. 753 But roll not backward from the sea. The days and nights pass swiftly by And steal our moments as they fly, E'en as the sun's unpitying rays Drink up the floods in summer blaze. Then for thyself lament and leave For death of other men to grieve, For if thou go or if thou stay, Thy life is shorter day by day. Death travels with us; death attends Our steps until our journey ends, Death, when the traveller wins the goal, Returns with the returning soul. The flowing hair grows white and thin, And wrinkles mark the altered skin. The ills of age man's strength assail: Ah, what can mortal power avail? Men joy to see the sun arise, They watch him set with joyful eyes: But ne'er reflect, too blind to see, How fast their own brief moments flee. With lovely change for ever new The seasons' sweet return they view, Nor think with heedless hearts the while That lives decay as seasons smile. As haply on the boundless main Meet drifting logs and part again, So wives and children, friends and gold, Ours for a little time we hold: Soon by resistless laws of fate To meet no more we separate. In all this changing world not one The common lot of all can shun: Then why with useless tears deplore
- **Translation**: 

---

### Verse 7 (Ramayana 0.772)
- **Original**: 754 The Ramayana The dead whom tears can bring no more? As one might stand upon the way And to a troop of travellers say: “If ye allow it, sirs, I too Will travel on the road with you:” So why should mortal man lament When on that path his feet are bent Which all men living needs must tread, Where sire and ancestors have led? Life flies as torrents downward fall Speeding away without recall, So virtue should our thoughts engage, For bliss382 is mortals' heritage.[215] By ceaseless care and earnest zeal For servants and for people's weal, By gifts, by duty nobly done, Our glorious sire the skies has won. Our lord the king, o'er earth who reigned, A blissful home in heaven has gained By wealth in ample largess spent, And many a rite magnificent: With constant joy from first to last A long and noble life he passed, Praised by the good, no tears should dim Our eyes, O brother dear, for him. His human body, worn and tried By length of days, he cast aside, And gained the godlike bliss to stray In Brahmá's heavenly home for aye. For such the wise as we are, deep In Veda lore, should never weep. Those who are firm and ever wise 382 To be won by virtue.
- **Translation**: 

---

### Verse 8 (Ramayana 0.773)
- **Original**: Canto CVI. Bharat's Speech. 755 Spurn vain lament and idle sighs. Be self-possessed: thy grief restrain: Go, in that city dwell again. Return, O best of men, and be Obedient to our sire's decree, While I with every care fulfil Our holy father's righteous will, Observing in the lonely wood His charge approved by all the good.” Thus Ráma of the lofty mind To Bharat spoke his righteous speech, By every argument designed Obedience to his sire to teach. Canto CVI. Bharat's Speech. Good Bharat, by the river side, To virtuous Ráma's speech replied, And thus with varied lore addressed The prince, while nobles round him pressed: “In all this world whom e'er can we Find equal, scourge of foes, to thee? No ill upon thy bosom weighs, No thoughts of joy thy spirit raise. Approved art thou of sages old, To whom thy doubts are ever told. Alike in death and life, to thee The same to be and not to be. The man who such a soul can gain Can ne'er be crushed by woe or pain. Pure as the Gods, high-minded, wise,
- **Translation**: 

---

### Verse 9 (Ramayana 0.774)
- **Original**: 756 The Ramayana Concealed from thee no secret lies. Such glorious gifts are all thine own, And birth and death to thee are known, That ill can ne'er thy soul depress With all-subduing bitterness. O let my prayer, dear brother, win Thy pardon for my mother's sin. Wrought for my sake who willed it not When absent in a distant spot. Duty alone with binding chains The vengeance due to crime restrains, Or on the sinner I should lift My hand in retribution swift. Can I who know the right, and spring From Da[aratha, purest king— Can I commit a heinous crime, Abhorred by all through endless time? The aged king I dare not blame, Who died so rich in holy fame, My honoured sire, my parted lord, E'en as a present God adored. Yet who in lore of duty skilled So foul a crime has ever willed, And dared defy both gain and right To gratify a woman's spite? When death draws near, so people say, The sense of creatures dies away; And he has proved the ancient saw By acting thus in spite of law. But O my honoured lord, be kind, Dismiss the trespass from thy mind, The sin the king committed, led By haste, his consort's wrath, and dread. For he who veils his sire's offence
- **Translation**: 

---

### Verse 10 (Ramayana 0.775)
- **Original**: Canto CVI. Bharat's Speech. 757 With tender care and reverence— His sons approved by all shall live: Not so their fate who ne'er forgive. Be thou, my lord, the noble son, And the vile deed my sire has done, Abhorred by all the virtuous, ne'er Resent, lest thou the guilt too share. Preserve us, for on thee we call, Our sire, Kaikeyí, me and all Thy citizens, thy kith and kin; Preserve us and reverse the sin. To live in woods a devotee Can scarce with royal tasks agree, Nor can the hermit's matted hair Suit fitly with a ruler's care. Do not, my brother, do not still Pursue this life that suits thee ill. Mid duties of a king we count His consecration paramount, That he with ready heart and hand May keep his people and his land. What Warrior born to royal sway From certain good would turn away, A doubtful duty to pursue, That mocks him with the distant view? Thou wouldst to duty cleave, and gain The meed that follows toil and pain. In thy great task no labour spare: Rule the four castes with justest care. Mid all the four, the wise prefer The order of the householder:383 [216] Canst thou, whose thoughts to duty cleave, 383 The four religious orders, referable to different times of life are, that of the student, that of the householder, that of the anchorite, and that of the mendicant.
- **Translation**: 

---

### Verse 11 (Ramayana 0.776)
- **Original**: 758 The Ramayana The best of all the orders leave? My better thou in lore divine, My birth, my sense must yield to thine: While thou, my lord, art here to reign, How shall my hands the rule maintain? O faithful lover of the right, Take with thy friends the royal might, Let thy sires' realm, from trouble free, Obey her rightful king in thee. Here let the priests and lords of state Our monarch duly consecrate, With prayer and holy verses blessed By saint Va[ishmha and the rest. Anointed king by us, again Seek fair Ayodhyá, there to reign, And like imperial Indra girt By Gods of Storm, thy might assert. From the three debts384 acquittance earn, And with thy wrath the wicked burn, O'er all of us thy rule extend, And cheer with boons each faithful friend. Let thine enthronement, lord, this day Make all thy lovers glad and gay, And let all those who hate thee flee To the ten winds for fear of thee. Dear lord, my mother's words of hate With thy sweet virtues expiate, And from the stain of folly clear The father whom we both revere. Brother, to me compassion show, I pray thee with my head bent low, And to these friends who on thee call,— 384 To Gods, men, and Manes.
- **Translation**: 

---

### Verse 12 (Ramayana 0.777)
- **Original**: Canto CVII. Ráma's Speech. 759 As the Great Father pities all. But if my tears and prayers be vain, And thou in woods wilt still remain, I will with thee my path pursue And make my home in forests too.” Thus Bharat strove to bend his will With suppliant head, but he, Earth's lord, inexorable still Would keep his sire's decree. The firmness of the noble chief The wondering people moved, And rapture mingling with their grief, All wept and all approved. “How firm his steadfast will,” they cried, “Who Keeps his promise thus! Ah, to Ayodhyá's town,” they sighed, “He comes not back with us.” The holy priest, the swains who tilled The earth, the sons of trade, And e'en the mournful queens were filled With joy as Bharat prayed, And bent their heads, then weeping stilled A while, his prayer to aid. Canto CVII. Ráma's Speech.
- **Translation**: 

---

### Verse 13 (Ramayana 0.778)
- **Original**: 760 The Ramayana Thus, by his friends encompassed round, He spoke, and Ráma, far renowned, To his dear brother thus replied, Whom holy rites had purified: “O thou whom Queen Kaikeyí bare The best of kings, thy words are fair, Our royal father, when of yore He wed her, to her father swore The best of kingdoms to confer, A noble dowry meet for her; Then, grateful, on the deadly day Of heavenly Gods' and demons' fray, A future boon on her bestowed To whose sweet care his life he owed. She to his mind that promise brought, And then the best of kings besought To bid me to the forest flee, And give the rule, O Prince, to thee. Thus bound by oath, the king our lord Gave her those boons of free accord, And bade me, O thou chief of men, Live in the woods four years and ten. I to this lonely wood have hied With faithful LakshmaG by my side, And Sítá by no tears deterred, Resolved to keep my father's word. And thou, my noble brother, too Shouldst keep our father's promise true: Anointed ruler of the state Maintain his word inviolate. From his great debt, dear brother, free Our lord the king for love of me, Thy mother's breast with joy inspire, And from all woe preserve thy sire.
- **Translation**: 

---

### Verse 14 (Ramayana 0.779)
- **Original**: Canto CVII. Ráma's Speech. 761 'Tis said, near Gayá's holy town385 Gayá, great saint of high renown, This text recited when he paid Due rites to each ancestral shade: “A son is born his sire to free From Put's infernal pains: Hence, saviour of his father, he The name of Puttra gains.”386 Thus numerous sons are sought by prayer, In Scripture trained with graces fair, [217] That of the number one some day May funeral rites at Gayá pay. The mighty saints who lived of old This holy doctrine ever hold. Then, best of men, our sire release From pains of hell, and give him peace. Now Bharat, to Ayodhyá speed, The braveZatrughna with thee lead, Take with thee all the twice-born men, And please each lord and citizen. I now, O King, without delay To DaG ak wood will bend my way, And Lakshma G and the Maithil dame Will follow still, our path the same. Now, Bharat, lord of men be thou, And o'er Ayodhyá reign: The silvan world to me shall bow, King of the wild domain. 385 Gayá is a very holy city in Behar. Every good Hindu ought once in his life to make funeral offerings in Gayá in honour of his ancestors. 386 Put is the name of that region of hell to which men are doomed who leave no son to perform the funeral rites which are necessary to assure the happiness of the departed.Putra, the common word for a son is said by the highest authority to be derived fromPut and tradeliverer.
- **Translation**: 

---

### Verse 15 (Ramayana 0.780)
- **Original**: 762 The Ramayana Yea, let thy joyful steps be bent To that fair town to-day, And I as happy and content, To DaG ak wood will stray. The white umbrella o'er thy brow Its cooling shade shall throw: I to the shadow of the bough And leafy trees will go. Zatrughna, for wise plans renowned, Shall still on thee attend; And Lakshma G, ever faithful found, Be my familiar friend. Let us his sons, O brother dear, The path of right pursue, And keep the king we all revere Still to his promise true.” Canto CVIII. Jáváli's Speech. Thus Ráma soothed his brother's grief: Then virtuous Jáváli, chief Of twice-born sages, thus replied In words that virtue's law defied: “Hail, Raghu's princely son, dismiss A thought so weak and vain as this. Canst thou, with lofty heart endowed, Think with the dull ignoble crowd? For what are ties of kindred? can One profit by a brother man? Alone the babe first opes his eyes, And all alone at last he dies.
- **Translation**: 

---

### Verse 16 (Ramayana 0.781)
- **Original**: Canto CVIII. Jáváli's Speech. 763 The man, I ween, has little sense Who looks with foolish reverence On father's or on mother's name: In others, none a right may claim. E'en as a man may leave his home And to a distant village roam, Then from his lodging turn away And journey on the following day, Such brief possession mortals hold In sire and mother, house and gold, And never will the good and wise The brief uncertain lodging prize. Nor, best of men, shouldst thou disown Thy sire's hereditary throne, And tread the rough and stony ground Where hardship, danger, woes abound. Come, let Ayodhyá rich and bright See thee enthroned with every rite: Her tresses bound in single braid387 She waits thy coming long delayed. O come, thou royal Prince, and share The kingly joys that wait thee there, And live in bliss transcending price As Indra lives in Paradise. The parted king is naught to thee, Nor right in living man has he: The king is one, thou, Prince of men, Another art: be counselled then. Thy royal sire, O chief, has sped On the long path we all must tread. The common lot of all is this, 387 It was the custom of Indian women when mourning for their absent husbands to bind their hair in a long single braid. Carey and Marshman translate,“the one-tailed city.”
- **Translation**: 

---

### Verse 17 (Ramayana 0.782)
- **Original**: 764 The Ramayana And thou in vain art robbed of bliss. For those— and only those— I weep Who to the path of duty keep; For here they suffer ceaseless woe, And dying to destruction go. With pious care, each solemn day, Will men their funeral offerings pay: See, how the useful food they waste: He who is dead no more can taste. If one is fed, his strength renewed Whene'er his brother takes his food, Then offerings to the parted pay: Scarce will they serve him on his way. By crafty knaves these rules were framed, And to enforce men's gifts proclaimed: “Give, worship, lead a life austere, Keep lustral rites, quit pleasures here.” There is no future life: be wise, And do, O Prince, as I advise. Enjoy, my lord, the present bliss, And things unseen from thought dismiss. Let this advice thy bosom move, The counsel sage which all approve; To Bharat's earnest prayer incline, And take the rule so justly thine.” Canto CIX. The Praises Of Truth. By sage Jáváli thus addressed, Ráma of truthful hearts the best,[218]
- **Translation**: 

---

### Verse 18 (Ramayana 0.783)
- **Original**: Canto CIX. The Praises Of Truth. 765 With perfect skill and wisdom high Thus to his speech made fit reply: “Thy words that tempt to bliss are fair, But virtue's garb they falsely wear. For he from duty's path who strays To wander in forbidden ways, Allured by doctrine false and vain, Praise from the good can never gain. Their lives the true and boaster show, Pure and impure, and high and low, Else were no mark to judge between Stainless and stained and high and mean; They to whose lot fair signs may fall Were but as they who lack them all, And those to virtuous thoughts inclined Were but as men of evil mind. If in the sacred name of right I do this wrong in duty's spite; The path of virtue meanly quit, And this polluting sin commit, What man who marks the bounds between Virtue and vice with insight keen, Would rank me high in after time Stained with this soul destroying crime? Whither could I, the sinner, turn, How hope a seat in heaven to earn, If I my plighted promise break, And thus the righteous path forsake? This world of ours is ever led To walk the ways which others tread, And as their princes they behold, The subjects too their lives will mould. That truth and mercy still must be Beloved of kings, is Heaven's decree.
- **Translation**: 

---

### Verse 19 (Ramayana 0.784)
- **Original**: 766 The Ramayana Upheld by truth the monarch reigns, And truth the very world sustains. Truth evermore has been the love Of holy saints and Gods above, And he whose lips are truthful here Wins after death the highest sphere. As from a serpent's deadly tooth, We shrink from him who scorns the truth. For holy truth is root and spring Of justice and each holy thing, A might that every power transcends, Linked to high bliss that never ends. Truth is all virtue's surest base, Supreme in worth and first in place. Oblations, gifts men offer here, Vows, sacrifice, and rites austere, And Holy Writ, on truth depend: So men must still that truth defend. Truth, only truth protects the land, By truth unharmed our houses stand; Neglect of truth makes men distressed, And truth in highest heaven is blessed. Then how can I, rebellious, break Commandments which my father spake— I ever true and faithful found, And by my word of honour bound? My father's bridge of truth shall stand Unharmed by my destructive hand: Not folly, ignorance, or greed My darkened soul shall thus mislead. Have we not heard that God and shade Turn from the hated offerings paid By him whose false and fickle mind No pledge can hold, no promise bind?
- **Translation**: 

---

### Verse 20 (Ramayana 0.785)
- **Original**: Canto CIX. The Praises Of Truth. 767 Truth is all duty: as the soul, It quickens and supports the whole. The good respect this duty: hence Its sacred claims I reverence. The Warrior's duty I despise That seeks the wrong in virtue's guise: Those claims I shrink from, which the base, Cruel, and covetous embrace. The heart conceives the guilty thought, Then by the hand the sin is wrought, And with the pair is leagued a third, The tongue that speaks the lying word. Fortune and land and name and fame To man's best care have right and claim; The good will aye to truth adhere, And its high laws must men revere. Base were the deed thy lips would teach, Approved as best by subtle speech. Shall I my plighted promise break, That I these woods my home would make? Shall I, as Bharat's words advise, My father's solemn charge despise? Firm stands the oath which then before My father's face I soothly swore, Which Queen Kaikeyí's anxious ear Rejoiced with highest joy to hear. Still in the wood will I remain, With food prescribed my life sustain, And please with fruit and roots and flowers Ancestral shades and heavenly powers. Here every sense contented, still Heeding the bounds of good and ill, My settled course will I pursue, Firm in my faith and ever true.
- **Translation**: 

---

