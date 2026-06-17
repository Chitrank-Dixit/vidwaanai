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

### Verse 1 (Ramayan 0.301)
- **Original**: Canto LXXIII. The Nuptials. 283 And to Videha's monarch said: “O King, Ayodhyá's ruler now Has breathed the prayer and vowed the vow, And with his sons expecting stands The giver of the maidens' hands. The giver and the taker both Must ratify a mutual oath. Perform the part for which we wait, And rites of marriage celebrate.” Skilled in the laws which Scriptures teach, He answered thus Va[ishmha's speech: “O Saint, what warder bars the gate? Whose bidding can the king await? In one's own house what doubt is shown? This kingdom, Sage, is all thine own. E'en now the maidens may be found Within the sacrificial ground: Each vow is vowed and prayed each prayer, And they, like fire, are shining there. Here by the shrine my place I took Expecting thee with eager look, No bar the nuptial rites should stay: What cause have we for more delay?” When Janak's speech the monarch heard, To sons and saints he gave the word, And set them in the holy ring, Then to Va[ishmha spoke the king Of Mithilá:“O mighty Sage, Now let this task thy care engage, And lend thine aid and counsel wise The nuptial rites to solemnize.”
- **Translation**: 

---

### Verse 2 (Ramayan 0.302)
- **Original**: 284 The Ramayana The saint Va[ishmha gave assent, And quickly to the task he went, With Vi[vámitra, nothing loth, And Zatánanda aiding both. Then, as the rules prescribe, they made An altar in the midst, and laid Fresh wreaths of fragrant flowers thereon. The golden ladles round it shone; And many a vase, which branches hid Fixed in the perforated lid, And sprays, and cups, and censers there Stood filled with incense rich and rare; Shell-bowls, and spoons, and salvers dressed With gifts that greet the honoured guest; Piles of parched rice some dishes bore, Others with corn prepared ran o'er; And holy grass was duly spread In equal lengths, while prayers were said. Next chief of saints, Va[ishmha came And laid the offering in the flame. Then by the hand King Janak drew His Sítá, beautiful to view, And placed her, bright in rich attire, Ráma to face, before the fire, Thus speaking to the royal boy Who filled Kau[alyá's heart with joy: “Here Sítá stands, my daughter fair, The duties of thy life to share. Take from her father, take thy bride; Join hand to hand, and bliss betide! A faithful wife, most blest is she, And as thy shade will follow thee.”
- **Translation**: 

---

### Verse 3 (Ramayan 0.303)
- **Original**: Canto LXXIII. The Nuptials. 285 Thus as he spoke the monarch threw O'er her young limbs the holy dew, While Gods and saints were heard to swell The joyous cry, 'Tis well! 'Tis well! His daughter Sítá thus bestowed, O'er whom the sacred drops had flowed. King Janak's heart with rapture glowed. Then to Prince LakshmaG thus he cried: “Take Urmilá thine offered bride, And clasp her hand within thine own Ere yet the lucky hour be flown.” Then to Prince Bharat thus cried he; “Come, take the hand of Mándavi.” Then toZatrughna:“In thy grasp The hand of Srutakírti clasp. Now, Raghu's sons, may all of you Be gentle to your wives and true; [085] Keep well the vows you make to-day, Nor let occasion slip away.” King Janak's word the youths obeyed; The maidens' hands in theirs they laid. Then with their brides the princes went With ordered steps and reverent Round both the fire and Janak, round The sages and the sacred ground. A flowery flood of lucid dyes In rain descended from the skies, While with celestial voices blent Sweet strains from many an instrument, And the nymphs danced in joyous throng Responsive to the minstrel's song. Such signs of exultation they
- **Translation**: 

---

### Verse 4 (Ramayan 0.304)
- **Original**: 286 The Ramayana Saw on the princes' wedding day. Still rang the heavenly music's sound When Raghu's sons thrice circled round The fire, each one with reverent head, And homeward then their brides they led. They to the sumptuous palace hied That Janak's care had seen supplied. The monarch girt with saint and peer Still fondly gazing followed near. Canto LXXIV. Ráma With The Axe.254 Soon as the night had reached its close The hermit Vi[vámitra rose; To both the kings he bade adieu And to the northern hill withdrew. Ayodhyá's lord of high renown Received farewell, and sought his town. Then as each daughter left her bower King Janak gave a splendid dower, Rugs, precious silks, a warrior force, Cars, elephants, and foot, and horse, Divine to see and well arrayed; And many a skilful tiring-maid, And many a young and trusty slave The father of the ladies gave. 254 This is another Ráma, son of Jamadagni, called Para[uráma, or Ráma with the axe, from the weapon which he carried. He was while he lived the terror of the Warrior caste, and his name recalls long and fierce struggles between the sacerdotal and military order in which the latter suffered severely at the hands of their implacable enemy.
- **Translation**: 

---

### Verse 5 (Ramayan 0.305)
- **Original**: Canto LXXIV. Ráma With The Axe. 287 Silver and coral, gold and pearls He gave to his beloved girls. These precious gifts the king bestowed And sped his guest upon his road. The lord of Mithilá's sweet town Rode to his court and lighted down. Ayodhyá's monarch, glad and gay, Led by the seers pursued his way With his dear sons of lofty mind: The royal army marched behind. As on he fared the voice he heard Around of many a dismal bird, And every beast in wild affright Began to hurry to the right. The monarch to Va[ishmha cried: “What strange misfortune will betide? Why do the beasts in terror fly, And birds of evil omen cry? What is it shakes my heart with dread? Why is my soul disquieted?” Soon as he heard, the mighty saint Thus answered Da[aratha's plaint In sweetest tone:“Now, Monarch, mark, And learn from me the meaning dark. The voices of the birds of air Great peril to the host declare: The moving beasts the dread allay, So drive thy whelming fear away,”
- **Translation**: 

---

### Verse 6 (Ramayan 0.306)
- **Original**: 288 The Ramayana As he and Da[aratha spoke A tempest from the welkin broke, That shook the spacious earth amain And hurled high trees upon the plain. The sun grew dark with murky cloud, And o'er the skies was cast a shroud, While o'er the army, faint with dread, A veil of dust and ashes spread. King, princes, saints their sense retained, Fear-stupefied the rest remained. At length, their wits returning, all Beneath the gloom and ashy pall Saw Jamadagni's son with dread, His long hair twisted round his head, Who, sprung from Bhrigu, loved to beat The proudest kings beneath his feet. Firm as Kailása's hill he showed, Fierce as the fire of doom he glowed. His axe upon his shoulder lay, His bow was ready for the fray, With thirsty arrows wont to fly Like Lightnings from the angry sky. A long keen arrow forth he drew, Invincible like those which flew From Ziva's ever-conquering bow And Tripura in death laid low. When his wild form, that struck with awe, Fearful as ravening flame, they saw, Va [ishmha and the saints whose care Was sacrifice and muttered prayer, Drew close together, each to each, And questioned thus with bated speech: “Indignant at his father's fate
- **Translation**: 

---

### Verse 7 (Ramayan 0.307)
- **Original**: Canto LXXV. The Parle. 289 Will he on warriors vent his hate, The slayers of his father slay, And sweep the loathed race away? But when of old his fury raged Seas of their blood his wrath assuaged: [086] So doubtless now he has not planned To slay all warriors in the land.” Then with a gift the saints drew near To Bhrigu's son whose look was fear, And Ráma! Ráma! soft they cried. The gift he took, no word replied. Then Bhrigu's son his silence broke And thus to Ráma Ráma spoke: Canto LXXV. The Parle. “Heroic Ráma, men proclaim The marvels of thy matchless fame, And I from loud-voiced rumour know The exploit of the broken bow, Yea, bent and broken, mighty Chief, A feat most wondrous, past belief. Stirred by thy fame thy face I sought: A peerless bow I too have brought. This mighty weapon, strong and dire, Great Jamadagni owned, my sire. Draw with its shaft my father's bow, And thus thy might, O Ráma, show. This proof of prowess let me see— The weapon bent and drawn by thee;
- **Translation**: 

---

### Verse 8 (Ramayan 0.308)
- **Original**: 290 The Ramayana Then single fight our strength shall try, And this shall raise thy glory high.” King Da[aratha heard with dread The boastful speech, and thus he said; Raising his hands in suppliant guise, With pallid cheek and timid eyes: “Forgetful of the bloody feud Ascetic toils hast thou pursued; Then, Bráhman, let thy children be Untroubled and from danger free. Sprung of the race of Bhrigu, who Read holy lore, to vows most true, Thou swarest to the Thousand-eyed And thy fierce axe was cast aside. Thou turnedst to thy rites away Leaving the earth to Ka[yap's sway, And wentest far a grove to seek Beneath Mahendra's255 mountain peak. Now, mighty Hermit, art thou here To slay us all with doom severe? For if alone my Ráma fall, We share his fate and perish all.” 255 “The author of theRaghuvaE[a places the mountain Mahendra in the territo- ry of the king of the Kalingans, whose palace commanded a view of the ocean. It is well known that the country along the coast to the south of the mouths of the Ganges was the seat of this people. Hence it may be suspected that this Mahendra is what Pliny calls‘promontorium Calingon.’ The modern name, Cape Palmyras, from the palmyras Borassus flabelliformis, which abound there agrees remarkably with the description of the poet who speaks of the groves of these trees.RaghuvaE[a, VI. 51.” SCHLEGEL {FNS .
- **Translation**: 

---

### Verse 9 (Ramayan 0.309)
- **Original**: Canto LXXV. The Parle. 291 As thus the aged sire complained The mighty chief no answer deigned. To Ráma only thus he cried: “Two bows, the Heavenly Artist's pride, Celestial, peerless, vast, and strong, By all the worlds were honoured long. One to the Three-eyed God256 was given, By glory to the conflict driven, Thus armed fierce Tripura he slew: And then by thee 'twas burst in two. The second bow, which few may brave, The highest Gods to VishGu gave. This bow I hold; before it fall The foeman's fenced tower and wall. Then prayed the Gods the Sire Most High By some unerring proof to try Were praise for might Lord VishGu's due, Or his whose Neck is stained with Blue.257 The mighty Sire their wishes knew, And he whose lips are ever true Caused the two Gods to meet as foes. Then fierce the rage of battle rose: Bristled in dread each starting hair As Ziva strove with VishGu there. But VishGu raised his voice amain. And Ziva's bowstring twanged in vain; Its master of the Three bright Eyes Stood fixt in fury and surprise. Then all the dwellers in the sky, Minstrel, and saint, and God drew nigh, And prayed them that the strife might cease, And the great rivals met in peace. 256 Ziva. 257 Siva. God of the Azure Neck.
- **Translation**: 

---

### Verse 10 (Ramayan 0.310)
- **Original**: 292 The Ramayana 'Twas seen howZiva's bow has failed Unnerved, when VishGu's might assailed, And Gods and heavenly sages thence To Vishnu gave preëminence. Then gloriousZiva in his rage Gave it to Devarát the sage Who ruled Videha's fertile land, To pass it down from hand to hand. But this my bow, whose shafts smite down The foeman's fenced tower and town, To great Richíka VishGu lent To be a pledge and ornament, Then Jamadagni, Bráhman dread, My sire, the bow inherited. But Arjun stooped to treachery vile And slew my noble sire by guile, Whose penance awful strength had gained, Whose hand the God-given bow retained.[087] I heard indignant how he fell By mournful fate, too sad to tell. My vengeful fury since that time Scourges all Warriors for the crime. As generations spring to life I war them down in endless strife. All earth I brought beneath my sway, And gave it for his meed and pay To holy Ka[yap, when of yore The rites performed by him were o'er. Then to Mahendra's hill I turned Strong in the strength that penance earned, And toiled upon his lofty head By Gods immortal visited. The breaking of the bow I knew From startled Gods conversing, through
- **Translation**: 

---

### Verse 11 (Ramayan 0.311)
- **Original**: Canto LXXVI. Debarred From Heaven. 293 The airy regions, of thy deed, And hither came with swiftest speed. Now, for thy Warrior's honour sake, This best of bows, O Ráma, take: This, owned by VishGu's self of old, My sire and grandsire loved to hold. Drawn to its head upon the string, One town-destroying arrow bring; If this thou can, O hero, I In single fight thy strength will try.” Canto LXXVI. Debarred From Heaven. The haughty challenge, undeterred The son of Da[aratha heard, And cried, while reverence for his sire Checked the full torrent of his ire: “Before this day have I been told The deed that stained thy hands of old. But pity bids my soul forget: Thy father, murdered, claimed the debt. My strength, O Chief, thou deemest slight, Too feeble for a Warrior's might. Now will I show thy wondering eyes The prowess which they dare despise.”
- **Translation**: 

---

### Verse 12 (Ramayan 0.312)
- **Original**: 294 The Ramayana He hastened then with graceful ease That mighty bow and shaft to seize. His hand the weapon strung and swayed: The arrow on the string was laid. Then Jamadagni's son he eyed, And thus in words of fury cried: “Thou art a Bráhman, still to be Most highly honoured, Chief, by me. For Vi[vámitra's sake beside Shall reverence due be ne'er denied. Though mine the power, I would not send A dart at thee thy life to end. But thy great power to wander free, Which penance-rites have won for thee, Or glorious worlds from thee to wrest, Is the firm purpose of my breast, And VishGu's dart which now I strain Can ne'er be shot to fall in vain: It strikes the mighty, and it stuns The madness of the haughty ones.” Then Gods, and saints and heavenly choir Preceded by the General Sire, Met in the air and gazed below On Ráma with that wondrous bow. Nymph, minstrel, angel, all were there, Snake-God, and spirit of the air, Giant, and bard, and gryphon, met, Their eyes upon the marvel set. In senseless hush the world was chained While Ráma's hand the bow retained, And Jamadagni's son amazed And powerless on the hero gazed. Then when his swelling heart had shrunk,
- **Translation**: 

---

### Verse 13 (Ramayan 0.313)
- **Original**: Canto LXXVI. Debarred From Heaven. 295 And his proud strength in torpor sunk, Scarce his voice ventured, low and weak, To Ráma lotus-eyed, to speak: “When long ago I gave away The whole broad land to Ka[yap's sway He charged me never to remain Within the limits of his reign. Obedient to my guide's behest On earth by night I never rest. My choice is made, I will not dim Mine honour and be false to him. So, son of Raghu, leave me still The power to wander where I will, And swifter than the thought my flight Shall place me on Mahendra's height. My mansions of eternal joy, By penance won, thou mayst destroy, My path to these thy shaft may stay. Now to the work! No more delay! I know thee Lord of Gods; I know Thy changeless might laid Madhu low. All other hands would surely fail To bend this bow. All hail! all hail! See! all the Gods have left the skies To bend on thee their eager eyes, With whose achievements none compete, Whose arm in war no God can meet. No shame is mine, I ween, for thou, Lord of the Worlds, hast dimmed my brow. Now, pious Ráma, 'tis thy part To shoot afar that glorious dart: I, when the fatal shaft is shot, Will seek that hill and tarry not.”
- **Translation**: 

---

### Verse 14 (Ramayan 0.314)
- **Original**: 296 The Ramayana He ceased. The wondrous arrow flew, And Jamadagni's offspring knew Those glorious worlds to him were barred, Once gained by penance long and hard. Then straight the airy quarters cleared, And the mid regions bright appeared, While Gods and saints unnumbered praised Ráma, the mighty bow who raised. And Jamadagni's son, o'erawed. Extolled his name with highest laud,[088] With reverent steps around him strode, Then hastened on his airy road. Far from the sight of all he fled, And rested on Mahendra's head. Canto LXXVII. Bharat's Departure. Then Ráma with a cheerful mind The bow to VaruG's hand resigned. Due reverence to the saints he paid, And thus addressed his sire dismayed: “As Bhrigu's son is far from view, Now let the host its march pursue, And to Ayodhyá's town proceed In four-fold bands, with thee to lead.”
- **Translation**: 

---

### Verse 15 (Ramayan 0.315)
- **Original**: Canto LXXVII. Bharat's Departure. 297 King Da[aratha thus addressed His lips to Ráma's forehead pressed, And held him to his aged breast. Rejoiced in sooth was he to know That Bhrigu's son had parted so, And hailed a second life begun For him and his victorious son. He urged the host to speed renewed, And soon Ayodhyá's gates he viewed. High o'er the roofs gay pennons played; Tabour and drum loud music made; Fresh water cooled the royal road, And flowers in bright profusion glowed. Glad crowds with garlands thronged the ways Rejoicing on their king to gaze And all the town was bright and gay Exalting in the festive day. People and Bráhmans flocked to meet Their monarch ere he gained the street. The glorious king amid the throng Rode with his glorious sons along, And passed within his dear abode That like Himálaya's mountain showed. And there Kau[alyá, noble queen, Sumitrá with her lovely mien, Kaikeyí of the dainty waist, And other dames his bowers who graced, Stood in the palace side by side And welcomed home each youthful bride: Fair Sítá, lofty-fated dame, Urmilá of the glorious fame, And Ku [adhwaj's children fair, With joyous greeting and with prayer, As all in linen robes arrayed
- **Translation**: 

---

### Verse 16 (Ramayan 0.316)
- **Original**: 298 The Ramayana With offerings at the altars prayed. Due reverence paid to God above, Each princess gave her soul to love, And hidden in her inmost bower Passed with her lord each blissful hour. The royal youths, of spirit high, With whom in valor none could vie, Lived each within his palace bounds Bright as Kuvera's pleasure-grounds, With riches, troops of faithful friends, And bliss that wedded life attends: Brave princes trained in warlike skill, And duteous to their father's will. At length the monarch called one morn Prince Bharat, of Kaikeyí born, And cried:“My son, within our gates Lord Yudhájit thine uncle waits. The son of Kekaya's king is he, And came, my child, to summon thee.” Then Bharat for the road prepared, And withZatrughna forth he fared. First to his sire he bade adieu, Brave Ráma, and his mothers too. Lord Yudhájit with joyful pride Went forth, the brothers by his side, And reached the city where he dwelt: And mighty joy his father felt.
- **Translation**: 

---

### Verse 17 (Ramayan 0.317)
- **Original**: Canto LXXVII. Bharat's Departure. 299 Ráma and LakshmaG honoured still Their godlike sire with duteous will. Two constant guides for Ráma stood, His father's wish, the people's good. Attentive to the general weal He thought and wrought to please and heal. His mothers too he strove to please With love and sonly courtesies. At every time, in every spot, His holy guides he ne'er forgot. So for his virtues kind and true Dearer and dearer Ráma grew To Da[aratha, Bráhmans, all In town and country, great and small. And Ráma by his darling's side Saw many a blissful season glide, Lodged in her soul, each thought on her, Lover, and friend, and worshipper. He loved her for his father's voice Had given her and approved the choice: He loved her for each charm she wore And her sweet virtues more and more. So he her lord and second life Dwelt in the bosom of his wife, In double form, that, e'en apart, Each heart could commune free with heart. Still grew that child of Janak's race, More goddess-fair in form and face, The loveliest wife that e'er was seen, In mortal mould sweet Beauty's Queen. Then shone the son Kau[alyá bore, With this bright dame allied, Like VishGu whom the Gods adore,
- **Translation**: 

---

### Verse 18 (Ramayan 0.318)
- **Original**: 300 The Ramayana With Lakshmi by his side. [089]
- **Translation**: 

---

### Verse 19 (Ramayan 0.319)
- **Original**: BOOK II. Canto I. The Heir Apparent. So Bharat to his grandsire went Obedient to the message sent, And for his fond companion chose Zatrughna slayer of his foes.258 There Bharat for a time remained With love and honour entertained, King A[vapati's constant care, Beloved as a son and heir. Yet ever, as they lived at ease, While all around combined to please, The aged sire they left behind Was present to each hero's mind. Nor could the king's fond memory stray From his brave children far away, Dear Bharat andZatrughna dear, Each VaruG's match or Indra's peer. 258 Zatrughna means slayer of foes, and the word is repeated as an intensive epithet.
- **Translation**: 

---

### Verse 20 (Ramayan 0.320)
- **Original**: 302 The Ramayana To all the princes, young and brave, His soul with fond affection clave; Around his loving heart they clung Like arms from his own body sprung.259 But best and noblest of the four, Good as the God whom all adore, Lord of all virtues, undefiled, His darling was his eldest child. For he was beautiful and strong, From envy free, the foe of wrong, With all his father's virtues blest, And peerless in the world confessed. With placid soul he softly spoke: No harsh reply could taunts provoke. He ever loved the good and sage Revered for virtue and for age, And when his martial tasks were o'er Sate listening to their peaceful lore. Wise, modest, pure, he honoured eld, His lips from lying tales withheld; Due reverence to the Bráhmans gave, And ruled each passion like a slave. Most tender, prompt at duty's call, Loved by all men he loved them all. Proud of the duties of his race, With spirit meet for Warrior's place. He strove to win by glorious deed, Throned with the Gods, a priceless meed. With him in speech and quick reply Vrihaspati might hardly vie, But never would his accents flow For evil or for empty show. 259 Alluding to the images of VishGu, which have four arms, the four princes being portions of the substance of that God.
- **Translation**: 

---

