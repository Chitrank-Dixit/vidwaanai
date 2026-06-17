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

### Verse 1 (Ramayan 0.481)
- **Original**: Canto XXXIII. The People's Lament. 463 Ah, for that gently-nurtured form! How will it fade with sun and storm! How will the rain, the cold, the heat Mar fragrant breast and tinted feet! Surely some demon has possessed His sire, and speaks within his breast, Or how could one that is a king Thus send his dear son wandering? It were a deed unkindly done To banish e'en a worthless son: But what, when his pure life has gained The hearts of all, by love enchained? Six sovereign virtues join to grace Ráma the foremost of his race: Tender and kind and pure is he, Docile, religious, passion-free. Hence misery strikes not him alone: In bitterest grief the people moan, Like creatures of the stream, when dry In the great heat the channels lie. The world is mournful with the grief That falls on its beloved chief, As, when the root is hewn away, Tree, fruit, and flower, and bud decay. The soul of duty, bright to see, He is the root of you and me; And all of us, who share his grief, His branches, blossom, fruit, and leaf. Now like the faithful LakshmaG, we Will follow and be true as he; Our wives and kinsmen call with speed, And hasten where our lord shall lead. Yes, we will leave each well-loved spot, The field, the garden, and the cot,
- **Translation**: 

---

### Verse 2 (Ramayan 0.482)
- **Original**: 464 The Ramayana And, sharers of his weal and woe, Behind the pious Ráma go. Our houses, empty of their stores, With ruined courts and broken doors, With all their treasures borne away. And gear that made them bright and gay: O'errun by rats, with dust o'erspread, Shrines, whence the deities have fled, Where not a hand the water pours, Or sweeps the long-neglected floors, No incense loads the evening air, No Bráhmans chant the text and prayer, No fire of sacrifice is bright, No gift is known, no sacred rite; With floors which broken vessels strew, As if our woes had crushed them too— Of these be stern Kaikeyí queen, And rule o'er homes where we have been. The wood where Ráma's feet may roam Shall be our city and our home, And this fair city we forsake, Our flight a wilderness shall make. Each serpent from his hole shall hie, The birds and beasts from mountain fly, Lions and elephants in fear Shall quit the woods when we come near, Yield the broad wilds for us to range, And take our city in exchange. With Ráma will we hence, content If, where he is, our days be spent.” Such were the varied words the crowd Of all conditions spoke aloud. And Ráma heard their speeches, yet
- **Translation**: 

---

### Verse 3 (Ramayan 0.483)
- **Original**: Canto XXXIV. Ráma In The Palace. 465 Changed not his purpose firmly set. His father's palace soon he neared, That like Kailása's hill appeared. Like a wild elephant he strode Right onward to the bright abode. Within the palace court he stepped, Where ordered bands their station kept, And saw Sumantra standing near With down-cast eye and gloomy cheer. Canto XXXIV. Ráma In The Palace. The dark incomparable chief Whose eye was like a lotus leaf, Cried to the mournful charioteer, “Go tell my sire that I am here.” Sumantra, sad and all dismayed, The chieftain's order swift obeyed. Within the palace doors he hied And saw the king, who wept and sighed. Like the great sun when wrapped in shade Like fire by ashes overlaid, Or like a pool with waters dried, So lay the world's great lord and pride, A while the wise Sumantra gazed On him whose senses woe has dazed, Grieving for Ráma. Near he drew With hands upraised in reverence due. With blessing first his king he hailed; Then with a voice that well-nigh failed,
- **Translation**: 

---

### Verse 4 (Ramayan 0.484)
- **Original**: 466 The Ramayana In trembling accents soft and low Addressed the monarch in his woe: “The prince of men, thy Ráma, waits Before thee at the palace gates. His wealth to Bráhmans he has dealt, And all who in his home have dwelt. Admit thy son. His friends have heard His kind farewell and parting word, He longs to see thee first, and then Will seek the wilds, O King of men. He, with each princely virtue's blaze, Shines as the sun engirt by rays.” The truthful King who loved to keep The law profound as Ocean's deep, And stainless as the dark blue sky, Thus to Sumantra made reply:[135] “Go then, Sumantra, go and call My wives and ladies one and all. Drawn round me shall they fill the place When I behold my Ráma's face.” Quick to the inner rooms he sped, And thus to all the women said, “Come, at the summons of the king: Come all, and make no tarrying.”
- **Translation**: 

---

### Verse 5 (Ramayan 0.485)
- **Original**: Canto XXXIV. Ráma In The Palace. 467 Their husband's word, by him conveyed, Soon as they heard, the dames obeyed, And following his guidance all Came thronging to the regal hall. In number half seven hundred, they, All lovely dames, in long array, With their bright eyes for weeping red, To stand round Queen Kau[alyá, sped. They gathered, and the monarch viewed One moment all the multitude, Then to Sumantra spoke and said: “Now let my son be hither led.” Sumantra went. Then Ráma came, And Lakshma G, and the Maithil dame, And, as he led them on, their guide Straight to the monarch's presence hied. When yet far off the father saw His son with raised palms toward him draw, Girt by his ladies, sick with woes, Swift from his royal seat he rose. With all his strength the aged man To meet his darling Ráma ran, But trembling, wild with dark despair, Fell on the ground and fainted there. And Lakshma G, wont in cars to ride, And Ráma, threw them by the side Of the poor miserable king, Half lifeless with his sorrow's sting. Throughout the spacious hall up went A thousand women's wild lament: “Ah Ráma! ” thus they wailed and wept, And anklets tinkled as they stepped Around his body, weeping, threw
- **Translation**: 

---

### Verse 6 (Ramayan 0.486)
- **Original**: 468 The Ramayana Their loving arms the brothers two, And then, with Sítá's gentle aid, The king upon a couch was laid. At length to earth's imperial lord, When life and knowledge were restored, Though seas of woe went o'er his head, With suppliant hand, thus Ráma said: “Lord of us all, great King, thou art: Bid me farewell before we part, To DaG ak wood this day I go: One blessing and one look bestow. Let LakshmaG my companion be, And Sítá also follow me. With truthful pleas I sought to bend Their purpose; but no ear they lend. Now cast this sorrow from thy heart, And let us all, great King, depart. As Brahmá sends his children, so Let LakshmaG, me, and Sítá go.” He stood unmoved, and watched intent Until the king should grant consent. Upon his son his eyes he cast, And thus the monarch spake at last: “O Ráma, by her arts enslaved, I gave the boons Kaikeyí craved, Unfit to reign, by her misled: Be ruler in thy father's stead.”
- **Translation**: 

---

### Verse 7 (Ramayan 0.487)
- **Original**: Canto XXXIV. Ráma In The Palace. 469 Thus by the lord of men addressed, Ráma, of virtue's friends the best, In lore of language duly learned, His answer, reverent, thus returned: “A thousand years, O King, remain O'er this our city still to reign. I in the woods my life will lead: The lust of rule no more I heed. Nine years and five I there will spend, And when the portioned days shall end, Will come, my vows and exile o'er, And clasp thy feet, my King, once more.” A captive in the snare of truth, Weeping, distressed with woe and ruth, Thus spake the monarch, while the queen Kaikeyí urged him on unseen: “Go then, O Ráma, and begin Thy course unvext by fear and sin: Go, my beloved son, and earn Success, and joy, and safe return. So fast the bonds of duty bind. O Raghu's son, thy truthful mind, That naught can turn thee back, or guide Thy will so strongly fortified. But O, a little longer stay, Nor turn thy steps this night away, That I one little day-— alas! One only— -with my son may pass. Me and thy mother do not slight, But stay, my son, with me to-night; With every dainty please thy taste, And seek to-morrow morn the waste. Hard is thy task, O Raghu's son,
- **Translation**: 

---

### Verse 8 (Ramayan 0.488)
- **Original**: 470 The Ramayana Dire is the toil thou wilt not shun, Far to the lonely wood to flee, And leave thy friends for love of me. I swear it by my truth, believe, For thee, my son, I deeply grieve, Misguided by the traitress dame With hidden guile like smouldering flame. Now, by her wicked counsel stirred, Thou fain wouldst keep my plighted word. No marvel that my eldest born Would hold me true when I have sworn.” Then Ráma having calmly heard His wretched father speak each word, With LakshmaG standing by his side Thus, humbly, to the King replied: “If dainties now my taste regale, To-morrow must those dainties fail. This day departure I prefer To all that wealth can minister. O'er this fair land, no longer mine, Which I, with all her realms, resign,[136] Her multitudes of men, her grain, Her stores of wealth, let Bharat reign. And let the promised boon which thou Wast pleased to grant the queen ere now, Be hers in full. Be true, O King, Kind giver of each precious thing. Thy spoken word I still will heed, Obeying all thy lips decreed: And fourteen years in woods will dwell With those who live in glade and dell. No hopes of power my heart can touch, No selfish joys attract so much
- **Translation**: 

---

### Verse 9 (Ramayan 0.489)
- **Original**: Canto XXXIV. Ráma In The Palace. 471 As son of Raghu, to fulfil With heart and soul my father's will. Dismiss, dismiss thy needless woe, Nor let those drowning torrents flow: The Lord of Rivers in his pride Keeps to the banks that bar his tide. Here in thy presence I declare; By thy good deeds, thy truth, I swear; Nor lordship, joy, nor lands I prize; Life, heaven, all blessings I despise. I wish to see thee still remain Most true, O King, and free from stain. It must not, Sire, it must not be: I cannot rest one hour with thee. Then bring this sorrow to an end, For naught my settled will can bend. I gave a pledge that binds me too, And to that pledge I still am true. Kaikeyí bade me speed away: She prayed me, and I answered yea. Pine not for me, and weep no more; The wood for us has joy in store, Filled with the wild deer's peaceful herds And voices of a thousand birds. A father is the God of each, Yea, e'en of Gods, so Scriptures teach: And I will keep my sire's decree, For as a God I honour thee. O best of men, the time is nigh, The fourteen years will soon pass by And to thine eyes thy son restore: Be comforted, and weep no more. Thou with thy firmness shouldst support These weeping crowds who throng the court;
- **Translation**: 

---

### Verse 10 (Ramayan 0.490)
- **Original**: 472 The Ramayana Then why, O chief of high renown, So troubled, and thy soul cast down?” Canto XXXV. Kaikeyí Reproached. Wild with the rage he could not calm, Sumantra, grinding palm on palm, His head in quick impatience shook, And sighed with woe he could not brook. He gnashed his teeth, his eyes were red, From his changed face the colour fled. In rage and grief that knew no law, The temper of the king he saw. With his word-arrows swift and keen He shook the bosom of the queen. With scorn, as though its lightning stroke Would blast her body, thus he spoke: “Thou, who, of no dread sin afraid, Hast Da[aratha's self betrayed, Lord of the world, whose might sustains Each thing that moves or fixed remains, What direr crime is left thee now? Death to thy lord and house art thou, Whose cruel deeds the king distress, Mahendra's peer in mightiness, Firm as the mountain's rooted steep, Enduring as the Ocean's deep. Despise not Da[aratha, he Is a kind lord and friend to thee. A loving wife in worth outruns The mother of ten million sons.
- **Translation**: 

---

### Verse 11 (Ramayan 0.491)
- **Original**: Canto XXXV. Kaikeyí Reproached. 473 Kings, when their sires have passed away, Succeed by birthright to the sway. Ikshváku's son still rules the state, Yet thou this rule wouldst violate. Yea, let thy son, Kaikeyí, reign, Let Bharat rule his sire's domain. Thy will, O Queen, shall none oppose: We all will go where Ráma goes. No Bráhman, scorning thee, will rest Within the realm thou governest, But all will fly indignant hence: So great thy trespass and offence. I marvel, when thy crime I see, Earth yawns not quick to swallow thee; And that the Bráhman saints prepare No burning scourge thy soul to scare, With cries of shame to smite thee, bent Upon our Ráma's banishment. The Mango tree with axes fell, And tend instead the Neem tree well, Still watered with all care the tree Will never sweet and pleasant be. Thy mother's faults to thee descend, And with thy borrowed nature blend. True is the ancient saw: the Neem Can ne'er distil a honeyed stream. Taught by the tale of long ago Thy mother's hateful sin we know. A bounteous saint, as all have heard, A boon upon thy sire conferred, And all the eloquence revealed That fills the wood, the flood, the field. No creature walked, or swam, or flew, But he its varied language knew.
- **Translation**: 

---

### Verse 12 (Ramayan 0.492)
- **Original**: 474 The Ramayana One morn upon his couch he heard The chattering of a gorgeous bird. And as he marked its close intent He laughed aloud in merriment. Thy mother furious with her lord, And fain to perish by the cord, Said to her husband:“I would know, O Monarch, why thou laughest so.”[137] The king in answer spake again: “If I this laughter should explain, This very hour would be my last, For death, be sure would follow fast.” Again thy mother, flushed with ire, To Kekaya spake, thy royal sire: “Tell me the cause; then live or die: I will not brook thy laugh, not I.” Thus by his darling wife addressed, The king whose might all earth confessed, To that kind saint his story told Who gave the wondrous gift of old. He listened to the king's complaint, And thus in answer spoke the saint: “King, let her quit thy home or die, But never with her prayer comply.” The saint's reply his trouble stilled, And all his heart with pleasure filled. Thy mother from his home he sent, And days like Lord Kuvera's spent. So thou wouldst force the king, misled By thee, in evil paths to tread, And bent on evil wouldst begin, Through folly, this career of sin. Most true, methinks, in thee is shown The ancient saw so widely known:
- **Translation**: 

---

### Verse 13 (Ramayan 0.493)
- **Original**: Canto XXXV. Kaikeyí Reproached. 475 The sons their fathers' worth declare And girls their mothers' nature share. So be not thou. For pity's sake Accept the word the monarch spake. Thy husband's will, O Queen, obey, And be the people's hope and stay, O, do not, urged by folly, draw The king to tread on duty's law. The lord who all the world sustains, Bright as the God o'er Gods who reigns. Our glorious king, by sin unstained, Will never grant what fraud obtained; No shade of fault in him is seen: Let Ráma be anointed, Queen. Remember, Queen, undying shame Will through the world pursue thy name, If Ráma leave the king his sire, And, banished, to the wood retire. Come, from thy breast this fever fling: Of his own realm be Ráma king. None in this city e'er can dwell To tend and love thee half so well. When Ráma sits in royal place, True to the custom of his race Our monarch of the mighty bow A hermit to the woods will go.”310 310 It was the custom of the kings of the solar dynasty to resign in their extreme old age the kingdom to the heir, and spend the remainder of their days in holy meditation in the forest: “For such through ages in their life's decline Is the good custom of Ikshváku's line.” RaghuraE[a.
- **Translation**: 

---

### Verse 14 (Ramayan 0.494)
- **Original**: 476 The Ramayana Sumantra thus, palm joined to palm, Poured forth his words of bane and balm, With keen reproach, with pleading kind, Striving to move Kaikeyí's mind. In vain he prayed, in vain reproved, She heard unsoftened and unmoved. Nor could the eyes that watched her view One yielding look, one change of hue. Canto XXXVI. Siddhárth's Speech. Ikshváku's son with anguish torn For the great oath his lips had sworn, With tears and sighs of sharpest pain Thus to Sumantra spake again: “Prepare thou quick a perfect force, Cars, elephants, and foot, and horse, To follow Raghu's scion hence Equipped with all magnificence. Let traders with the wealth they sell, And those who charming stories tell, And dancing-women fair of face, The prince's ample chariots grace. On all the train who throng his courts, And those who share his manly sports, Great gifts of precious wealth bestow, And bid them with their master go. Let noble arms, and many a wain, And townsmen swell the prince's train; And hunters best for woodland skill Their places in the concourse fill.
- **Translation**: 

---

### Verse 15 (Ramayan 0.495)
- **Original**: Canto XXXVI. Siddhárth's Speech. 477 While elephants and deer he slays, Drinking wood honey as he strays, And looks on streams each fairer yet, His kingdom he may chance forget. Let all my gold and wealth of corn With Ráma to the wilds be borne; For it will soothe the exile's lot To sacrifice in each pure spot, Deal ample largess forth, and meet Each hermit in his calm retreat. The wealth shall Ráma with him bear, Ayodhyá shall be Bharat's share.” As thus Kakutstha's offspring spoke, Fear in Kaikeyí's breast awoke. The freshness of her face was dried, Her trembling tongue was terror-tied. Alarmed and sad, with bloodless cheek, She turned to him and scarce could speak: “Nay, Sire, but Bharat shall not gain An empty realm where none remain. My Bharat shall not rule a waste Reft of all sweets to charm the taste— The wine-cup's dregs, all dull and dead, Whence the light foam and life are fled.” Thus in her rage the long-eyed dame Spoke her dire speech untouched by shame. [138] Then, answering, Da[aratha spoke: “Why, having bowed me to the yoke, Dost thou, must cruel, spur and goad Me who am struggling with the load? Why didst thou not oppose at first This hope, vile Queen, so fondly nursed?”
- **Translation**: 

---

### Verse 16 (Ramayan 0.496)
- **Original**: 478 The Ramayana Scarce could the monarch's angry speech The ears of the fair lady reach, When thus, with double wrath inflamed, Kaikeyí to the king exclaimed: “Sagar, from whom thy line is traced, Drove forth his eldest son disgraced, Called Asamanj, whose fate we know: Thus should thy son to exile go.” “Fie on thee, dame!” the monarch said; Each of her people bent his head, And stood in shame and sorrow mute: She marked not, bold and resolute. Then great Siddhárth, inflamed with rage, The good old councillor and sage On whose wise rede the king relied, To Queen Kaikeyí thus replied: “But Asamanj the cruel laid His hands on infants as they played, Cast them to Sarjú's flood, and smiled For pleasure when he drowned a child.”311 The people saw, and, furious, sped Straight the the king his sire and said: “Choose us, O glory of the throne, Choose us, or Asamanj alone.” 311 See Book I, Canto XXXIX. An Indian prince in more modern times appears to have diverted himself in a similar way. It is still reported in Belgaum that Appay Deasy was wont to amuse himself “by making several young and beautiful women stand side by side on a narrow balcony, without a parapet, overhanging the deep reservoir at the new palace in Nipani. He used then to pass along the line of trembling creatures, and suddenly thrusting one of them headlong into the water below, he used to watch her drowning, and derive pleasure from her dying agonies.”— History of the Belgaum District. By H. J. Stokes, M. S. C.
- **Translation**: 

---

### Verse 17 (Ramayan 0.497)
- **Original**: Canto XXXVI. Siddhárth's Speech. 479 “Whence comes this dread?” the monarch cried; And all the people thus replied: “In folly, King, he loves to lay Fierce hands upon our babes at play, Casts them to Sarjú's flood and joys To murder our bewildered boys.” With heedful ear the king of men Heard each complaining citizen. To please their troubled minds he strove, And from the state his son he drove. With wife and gear upon a car He placed him quick, and sent him far. And thus he gave commandment,“He Shall all his days an exile be.” With basket and with plough he strayed O'er mountain heights, through pathless shade, Roaming all lands a weary time, An outcast wretch defiled with crime. Sagar, the righteous path who held, His wicked offspring thus expelled. But what has Ráma done to blame? Why should his sentence be the same? No sin his stainless name can dim; We see no fault at all in him. Pure as the moon, no darkening blot On his sweet life has left a spot. If thou canst see one fault, e'en one, To dim the fame of Raghu's son, That fault this hour, O lady, show, And Ráma to the wood shall go. To drive the guiltless to the wild, Truth's constant lover, undefiled, Would, by defiance of the right, The glory e'en of Indra blight.
- **Translation**: 

---

### Verse 18 (Ramayan 0.498)
- **Original**: 480 The Ramayana Then cease, O lady, and dismiss Thy hope to ruin Ráma's bliss, Or all thy gain, O fair of face, Will be men's hatred, and disgrace.” Canto XXXVII. The Coats Of Bark. Thus spake the virtuous sage: and then Ráma addressed the king of men. In laws of meek behaviour bred, Thus to his sire he meekly said: “King, I renounce all earthly care, And live in woods on woodland fare. What, dead to joys, have I to do With lordly train and retinue! Who gives his elephant and yet Upon the girths his heart will set? How can a cord attract his eyes Who gives away the nobler prize? Best of the good, with me be led No host, my King with banners spread. All wealth, all lordship I resign: The hermit's dress alone be mine. Before I go, have here conveyed A little basket and a spade. With these alone I go, content, For fourteen years of banishment.”
- **Translation**: 

---

### Verse 19 (Ramayan 0.499)
- **Original**: Canto XXXVII. The Coats Of Bark. 481 With her own hands Kaikeyí took The hermit coats of bark, and,“Look,” She cried with bold unblushing brow Before the concourse,“Dress thee now.” That lion leader of the brave Took from her hand the dress she gave, Cast his fine raiment on the ground, [139] And round his waist the vesture bound. Then quick the hero LakshmaG too His garment from his shoulders threw, And, in the presence of his sire, Indued the ascetic's rough attire. But Sítá, in her silks arrayed, Threw glances, trembling and afraid, On the bark coat she had to wear, Like a shy doe that eyes the snare. Ashamed and weeping for distress From the queen's hand she took the dress. The fair one, by her husband's side Who matched heaven's minstrel monarch,312 cried: “How bind they on their woodland dress, Those hermits of the wilderness?” There stood the pride of Janak's race Perplexed, with sad appealing face. One coat the lady's fingers grasped, One round her neck she feebly clasped, But failed again, again, confused By the wild garb she ne'er had used. Then quickly hastening Ráma, pride Of all who cherish virtue, tied The rough bark mantle on her, o'er The silken raiment that she wore. 312 Chitraratha, King of the celestial choristers.
- **Translation**: 

---

### Verse 20 (Ramayan 0.500)
- **Original**: 482 The Ramayana Then the sad women when they saw Ráma the choice bark round her draw, Rained water from each tender eye, And cried aloud with bitter cry: “O, not on her, beloved, not On Sítá falls thy mournful lot. If, faithful to thy father's will, Thou must go forth, leave Sítá still. Let Sítá still remaining here Our hearts with her loved presence cheer. With LakshmaG by thy side to aid Seek thou, dear son, the lonely shade. Unmeet, one good and fair as she Should dwell in woods a devotee. Let not our prayers be prayed in vain: Let beauteous Sítá yet remain; For by thy love of duty tied Thou wilt not here thyself abide.” Then the king's venerable guide Va [ishmha, when he saw each coat Enclose the lady's waist and throat, Her zeal with gentle words repressed, And Queen Kaikeyí thus addressed: “O evil-hearted sinner, shame Of royal Kekaya's race and name; Who matchless in thy sin couldst cheat Thy lord the king with vile deceit; Lost to all sense of duty, know Sítá to exile shall not go. Sítá shall guard, as 'twere her own, The precious trust of Ráma's throne. Those joined by wedlock's sweet control Have but one self and common soul.
- **Translation**: 

---

