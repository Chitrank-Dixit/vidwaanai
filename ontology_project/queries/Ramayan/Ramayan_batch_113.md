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

### Verse 1 (Ramayana 0.286)
- **Original**: 268 The Ramayana Nor let occasion idly by.” He ceased. There came a glad reply From priest and mighty saint and all The councillors who thronged the hall. Then cried the king with joyous heart: “To-morrow let us all depart.” That night the envoys entertained With honour and all care remained. Canto LXIX. Dasaratha's Visit. Soon as the shades of night had fled, Thus to the wise Sumantra said The happy king, while priest and peer, Each in his place, were standing near: “Let all my treasurers to-day, Set foremost in the long array, With gold and precious gems supplied In bounteous store, together ride. And send you out a mighty force, Foot, chariot, elephant, and horse. Besides, let many a car of state, And noblest steeds, my will await. Va [ishmha, Vámadeva sage, And MárkaGdeya's reverend age, Jáváli, Ka[yap's godlike seed, And wise Kátyáyana, shall lead. Thy care, Sumantra, let it be To yoke a chariot now for me, That so we part without delay: These envoys hasten me away.”
- **Translation**: 

---

### Verse 2 (Ramayana 0.287)
- **Original**: Canto LXIX. Dasaratha's Visit. 269 So fared he forth. That host, with speed, Quadruple, as the king decreed, With priests to head the bright array, Followed the monarch on his way. Four days they travelled on the road, And eve Videha's kingdom showed. Janak had left his royal seat The venerable king to greet, And, noblest, with these words addressed That noblest lord, his happy guest: “Hail, best of kings: a blessed fate Has led thee, Monarch, to my state. Thy sons, supreme in high emprise, Will gladden now their father's eyes. And high my fate, that hither leads Va [ishmha, bright with holy deeds, Girt with these sages far-renowned, Like Indra with the Gods around. Joy! joy! for vanquished are my foes: Joy! for my house in glory grows, With Raghu's noblest sons allied, Supreme in strength and valour's pride. To-morrow with its early light Will shine on my completed rite. Then, sanctioned by the saints and thee, The marriage of thy Ráma see.” Then Da[aratha, best of those Whose speech in graceful order flows, With gathered saints on every side, Thus to the lord of earth replied: “A truth is this I long have known, A favour is the giver's own. What thou shalt bid, O good and true,
- **Translation**: 

---

### Verse 3 (Ramayana 0.288)
- **Original**: 270 The Ramayana We, as our power permits, will do.” That answer of the truthful lord, With virtuous worth and honour stored, Janak, Videha's noble king, Heard gladly, greatly marvelling. With bosoms filled with pleasure met Long-parted saint and anchoret, And linked in friendship's tie they spent The peaceful night in great content. Ráma and LakshmaG thither sped, By sainted Vi[vámitra led, And bent in filial love to greet Their father, and embraced his feet. The aged king, rejoiced to hear And see again his children dear, Honoured by Janak's thoughtful care, With great enjoyment rested there. King Janak, with attentive heed, Consulted first his daughters' need, And ordered all to speed the rite; Then rested also for the night. Canto LXX. The Maidens Sought.
- **Translation**: 

---

### Verse 4 (Ramayana 0.289)
- **Original**: Canto LXX. The Maidens Sought. 271 Then with the morn's returning sun. King Janak, when his rites were done, Skilled all the charms of speech to know, Spoke to wiseZatánanda so: “My brother, lord of glorious fame, My younger, Ku[adhwaj by name, Whose virtuous life has won renown, Has settled in a lovely town, Sánká[yá, decked with grace divine, Whose glories bright as Pushpak's shine, While Ikshumatí rolls her wave Her lofty rampart's foot to lave. Him, holy priest, I long to see: The guardian of my rite is he: That my dear brother may not miss A share of mine expected bliss.” Thus in the presence of the priest The royal Janak spoke, and ceased. Then came his henchmen, prompt and brave, [081] To whom his charge the monarch gave. Soon as they heard his will, in haste With fleetest steeds away they raced, To lead with them that lord of kings, As Indra's call Lord VishGu brings. Sánká[yá's walls they duly gained, And audience of the king obtained. To him they told the news they brought Of marvels past and Janak's thought. Soon as the king the story knew From those good envoys swift and true, To Janak's wish he gave assent, And swift to Míthilá he went. He paid to Janak reverence due,
- **Translation**: 

---

### Verse 5 (Ramayana 0.290)
- **Original**: 272 The Ramayana And holyZatánanda too, Then sate him on a glorious seat For kings or Gods celestial meet. Soon as the brothers, noble pair Peerless in might, were seated there, They gave the wise Sudáman, best Of councillors, their high behest: “Go, noble councillor,” they cried, “And hither to our presence guide Ikshváku's son, Ayodhyá's lord, Invincible by foeman's sword, With both his sons, each holy seer, And every minister and peer.” Sudáman to the palace flew, And saw the mighty king who threw Splendour on Raghu's splendid race, Then bowed his head with seemly grace: “O King, whose hand Ayodhyá sways, My lord, whom Míthilá obeys, Yearns with desire, if thou agree, Thee with thy guide and priest to see.” Soon as the councillor had ceased, The king, with saint and peer and priest, Sought, speeding through the palace gate, The hall where Janak held his state. There, with his nobles round him spread, Thus to Videha's lord be said: “Thou knowest, King, whose aid divine Protects Ikshváku's royal line. In every need, whate'er befall, The saint Va[ishmha speaks for all. If Vi[vámitra so allow, And all the saints around me now, The sage will speak, at my desire,
- **Translation**: 

---

### Verse 6 (Ramayana 0.291)
- **Original**: Canto LXX. The Maidens Sought. 273 As order and the truth require.” Soon as the king his lips had stilled, Up rose Va[ishmha, speaker skilled. And to Videha's lord began In flowing words that holy man: “From viewless Nature Brahmá rose, No change, no end, no waste he knows. A son had he Maríchi styled, And Ka [yap was Maríchi's child. From him Vivasvat sprang: from him Manu whose fame shall ne'er be dim. Manu, who life to mortals gave, Begot Ikshváku good and brave. First of Ayodhyá's kings was he, Pride of her famous dynasty. From him the glorious Kukshi sprang, Whose fame through all the regions rang. Rival of Kukshi's ancient fame, His heir, the great Vikukshi, came, His son was VáGa, lord of might; His AnaraGya, strong to fight. His son was Prithu, glorious name; From him the good Tri[anku came. He left a son renowned afar, Known by the name of Dhundhumár. His son, who drove the mighty car, Was Yuvaná [va, feared in war. He passed away. Him followed then His son Mándhátá, king of men. His son was blest in high emprise, Susandhi, fortunate and wise. Two noble sons had he, to wit Dhruvasandhi and Prasenajit.
- **Translation**: 

---

### Verse 7 (Ramayana 0.292)
- **Original**: 274 The Ramayana Bharat was Dhruvasandhi's son, And glorious fame that monarch won. The warrior Asit he begot. Asit had warfare, fierce and hot, With rival kings in many a spot, Haihayas, Tálajanghas styled, And Za[ivindus, strong and wild. Long time he strove, but forced to yield Fled from his kingdom and the field. With his two wives away he fled Where high Himálaya lifts his head, And, all his wealth and glory past, He paid the dues of Fate at last. The wives he left had both conceived— So is the ancient tale believed— One, of her rival's hopes afraid Fell poison in her viands laid. It chanced that Chyavan, Bhrigu's child, Had wandered to that pathless wild, And there Himálaya's lovely height Detained him with a strange delight. There came the other widowed queen, With lotus eyes and beauteous mien, Longing a noble son to bear, And wooed the saint with earnest prayer. When thus Kálindi,248 fairest dame, With reverent supplication came, To her the holy sage replied: “Born with the poison from thy side, O happy Queen, shall spring ere long An infant fortunate and strong. Then weep no more, and check thy sighs, 248 A different lady from the Goddess of the Jumna who bears the same name.
- **Translation**: 

---

### Verse 8 (Ramayana 0.293)
- **Original**: Canto LXX. The Maidens Sought. 275 Sweet lady of the lotus eyes.” The queen, who loved her perished lord, For meet reply, the saint adored, And, of her husband long bereaved, She bore a son by him conceived. Because her rival mixed the bane [082] To render her conception vain, And fruit unripened to destroy, Sagar249 she called her darling boy. To Sagar Asamanj was heir: Bright An[umán his consort bare. An [umán's son, Dilípa famed, Begot a son Bhagírath named. From him the great Kakutstha rose: From him came Raghu, feared by foes, Of him sprang Purushádak bold, Fierce hero of gigantic mould: Kalmáshapáda's name he bore, Because his feet were spotted o'er.250 From him cameZankaG, and from him Sudar[an, fair in face and limb. From beautiful Sudar[an came Prince AgnivarGa, bright as flame. His son wasZíghraga, for speed Unmatched; and Maru was his seed. Pra[u[ruka was Maru's child; His son was Ambarísha styled. Nahush was Ambarísha's heir, The mighty lord of regions fair: Nahush begot Yayáti: he, 249 This is another fanciful derivation,Sa— with, andgara— poison. 250 Purushádak means a cannibal. First calledKalmáshapáda on account of his spotted feet he is said to have been turned into a cannibal for killing the son of Va[ishmha.
- **Translation**: 

---

### Verse 9 (Ramayana 0.294)
- **Original**: 276 The Ramayana Nábhág of happy destiny. Son of Nábhág was Aja: his, The glorious Da[aratha is, Whose noble children boast to be Ráma and LakshmaG, whom we see. Thus do those kings of purest race Their lineage from Ikshváku trace: Their hero lives the right maintained, Their lips with falsehood ne'er were stained. In Ráma's and in LakshmaG's name Thy daughters as their wives I claim, So shall in equal bands be tied Each peerless youth with peerless bride.” Canto LXXI. Janak's Pedigree. Then to the saint supremely wise King Janak spoke in suppliant guise: “Deign, Hermit, with attentive ear, Mv race's origin to hear. When kings a daughter's hand bestow, 'Tis right their line and fame to show. There was a king whose deeds and worth Spread wide his name through heaven and earth, Nimi, most virtuous e'en from youth, The best of all who love the truth. His son and heir was Mithi, and His Janak, first who ruled this land. He left a son Udávasu, Blest with all virtues, good and true. His son was Nandivardhan, dear
- **Translation**: 

---

### Verse 10 (Ramayana 0.295)
- **Original**: Canto LXXI. Janak's Pedigree. 277 For pious heart and worth sincere. His son Suketu, hero brave, To Devarát, existence gave. King Devarát, a royal sage, For virtue, glory of the age, Begot Vrihadratha; and he Begot, his worthy heir to be, The splendid hero Mahábír Who long in glory governed here. His son was Sudhriti, a youth Firm in his purpose, brave in sooth, His son was Dhrismaketu, blest With pious will and holy breast. The fame of royal saint he won: Harya[va was his princely son. Harya[va's son was Maru, who Begot Pratíndhak, wise and true. Next Kírtiratha held the throne, His son, for gentle virtues known. Then followed Devamidha, then Vibudh, Mahándhrak, kings of men. Mahándhrak's son, of boundless might, Was Kírtirát, who loved the right. He passed away, a sainted king, And Maháromá following To SwarGaromá left the state. Then Hra[varomá, good and great, Succeeded, and to him a pair Of sons his royal consort bare, Elder of these I boast to be: Brave Ku[adhwaj is next to me.251 251 “In the setting forth of these royal genealogies the Bengal recension varies but slightly from the Northern. The first six names of the genealogy of the Kings of Ayodhyá are partly theogonical and partly cosmogonical; the
- **Translation**: 

---

### Verse 11 (Ramayana 0.296)
- **Original**: 278 The Ramayana Me then, the elder of the twain, My sire anointed here to reign. He bade me tend my brother well, Then to the forest went to dwell. He sought the heavens, and I sustained The burden as by law ordained, And noble Ku[adhwaj, the peer Of Gods, I ever held most dear. Then came Sánká[yá's mighty lord, Sudhanvá, threatening siege and sword, And bade me swift on him bestow Ziva's incomparable bow,[083] And Sítá of the lotus eyes: But I refused each peerless prize. Then, host to host, we met the foes, And fierce the din of battle rose, Sudhanvá, foremost of his band, Fell smitten by my single hand. When thus Sánká[yá's lord was slain, I sanctified, as laws ordain, My brother in his stead to reign, Thus are we brothers, Saint most high The younger he, the elder I. Now, mighty Sage, my spirit joys To give these maidens to the boys. Let Sítá be to Ráma tied. And Urmilá be LakshmaG's bride. First give, O King, the gift of cows, As dowry of each royal spouse, Due offerings to the spirits pay, And solemnize the wedding-day. other names are no doubt in accordance with tradition and deserve the same amount of credence as the ancient traditional genealogies of other nations.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 12 (Ramayana 0.297)
- **Original**: Canto LXXII. The Gift Of Kine. 279 The moon tonight, O royal Sage, In Maghá's252 House takes harbourage; On the third night his rays benign In second Phálguni253 will shine: Be that the day, with prosperous fate, The nuptial rites to celebrate.” Canto LXXII. The Gift Of Kine. When royal Janak's words were done, Joined with Va[ishmha Ku[ik's son, The mighty sage began his speech: “No mind may soar, no thought can reach The glories of Ikshváku's line, Or, great Videha's King, of thine: None in the whole wide world may vie With them in fame and honours high. Well matched, I ween, in holy bands, These peerless pairs will join their hands. But hear me as I speak once more; Thy brother, skilled in duty's lore, Has at his home a royal pair Of daughters most divinely fair. I for the hands of these sweet two For Bharat andZatrughna sue, Both princes of heroic mould, Wise, fair of form, and lofty-souled. All Da[aratha's sons, I ween, 252 The tenth of the lunar asterisms, composed of five stars. 253 There are two lunar asterisms of this name, one following the other immediately, forming the eleventh and twelfth of the lunar mansions.
- **Translation**: 

---

### Verse 13 (Ramayana 0.298)
- **Original**: 280 The Ramayana Own each young grace of form and mien: Brave as the Gods are they, nor yield To the great Lords the worlds who shield. By these, good Prince of merits high, Ikshváku's house with thine ally.” The suit the holy sage preferred, With willing ear the monarch heard: Va [ishmha's lips the counsel praised: Then spake the king with hands upraised: “Now blest indeed my race I deem, Which your high will, O Saints supreme, With Da[aratha's house unites In bonds of love and marriage rites. So be it done. My nieces twain Let Bharat andZatrughna gain, And the four youths the selfsame day Four maiden hands in theirs shall lay. No day so lucky may compare, For marriage— so the wise declare— With the last day of Phálguni Ruled by the genial deity.” Then with raised hands in reverence due To those arch-saints he spoke anew: “I am your pupil, ever true: To me high favour have ye shown; Come, sit ye on my royal throne, For Da[aratha rules these towers E'en as Ayodhyá now is ours. Do with your own whate'er ye choose: Your lordship here will none refuse.”
- **Translation**: 

---

### Verse 14 (Ramayana 0.299)
- **Original**: Canto LXXIII. The Nuptials. 281 He spoke, and to Videha's king Thus Da[aratha, answering: “Boundless your virtues, lords, whose sway The realms of Mithilá obey. With honouring care you entertain. Both holy sage and royal train. Now to my house my steps I bend— May blessings still on you at end— Due offerings to the shades to pay.” Thus spoke the king, and turned away: To Janak first he bade adieu, Then followed fast those holy two. The monarch reached his palace where The rites were paid with solemn care. When the next sun began to shine He rose and made his gift of kine. A hundred thousand cows prepared For each young prince the Bráhmans shared. Each had her horns adorned with gold; And duly was the number told, Four hundred thousand perfect tale: Each brought a calf, each filled a pail. And when that glorious task was o'er, The monarch with his children four, Showed like the Lord of Life divine When the worlds' guardians round him shine. [084] Canto LXXIII. The Nuptials.
- **Translation**: 

---

### Verse 15 (Ramayana 0.300)
- **Original**: 282 The Ramayana On that same day that saw the king His gift of kine distributing, The lord of Kekaya's son, by name Yudhájit, Bharat's uncle, came, Asked of the monarch's health, and then Addressed the reverend king of men: “The lord of Kekaya's realm by me Sends greeting, noble King, to thee: Asks if the friends thy prayers would bless Uninterrupted health possess. Right anxious, mighty King, is he My sister's princely boy to see. For this I sought Ayodhyá fair The message of my sire to bear. There learning, O my liege, that thou With sons and noble kinsmen now Wast resting here, I sought the place Longing to see my nephew's face.” The king with kind observance cheered His friend by tender ties endeared, And every choicest honour pressed Upon his honourable guest. That night with all his children spent, At morn King Da[aratha went, Behind Va[ishmha and the rest, To the fair ground for rites addressed. Then when the lucky hour was nigh Called Victory, of omen high, Came Ráma, after vow and prayer For nuptial bliss and fortune fair, With the three youths in bright attire, And stood beside his royal sire. To Janak then Va[ishmha sped,
- **Translation**: 

---

### Verse 16 (Ramayana 0.301)
- **Original**: Canto LXXIII. The Nuptials. 283 And to Videha's monarch said: “O King, Ayodhyá's ruler now Has breathed the prayer and vowed the vow, And with his sons expecting stands The giver of the maidens' hands. The giver and the taker both Must ratify a mutual oath. Perform the part for which we wait, And rites of marriage celebrate.” Skilled in the laws which Scriptures teach, He answered thus Va[ishmha's speech: “O Saint, what warder bars the gate? Whose bidding can the king await? In one's own house what doubt is shown? This kingdom, Sage, is all thine own. E'en now the maidens may be found Within the sacrificial ground: Each vow is vowed and prayed each prayer, And they, like fire, are shining there. Here by the shrine my place I took Expecting thee with eager look, No bar the nuptial rites should stay: What cause have we for more delay?” When Janak's speech the monarch heard, To sons and saints he gave the word, And set them in the holy ring, Then to Va[ishmha spoke the king Of Mithilá:“O mighty Sage, Now let this task thy care engage, And lend thine aid and counsel wise The nuptial rites to solemnize.”
- **Translation**: 

---

### Verse 17 (Ramayana 0.302)
- **Original**: 284 The Ramayana The saint Va[ishmha gave assent, And quickly to the task he went, With Vi[vámitra, nothing loth, And Zatánanda aiding both. Then, as the rules prescribe, they made An altar in the midst, and laid Fresh wreaths of fragrant flowers thereon. The golden ladles round it shone; And many a vase, which branches hid Fixed in the perforated lid, And sprays, and cups, and censers there Stood filled with incense rich and rare; Shell-bowls, and spoons, and salvers dressed With gifts that greet the honoured guest; Piles of parched rice some dishes bore, Others with corn prepared ran o'er; And holy grass was duly spread In equal lengths, while prayers were said. Next chief of saints, Va[ishmha came And laid the offering in the flame. Then by the hand King Janak drew His Sítá, beautiful to view, And placed her, bright in rich attire, Ráma to face, before the fire, Thus speaking to the royal boy Who filled Kau[alyá's heart with joy: “Here Sítá stands, my daughter fair, The duties of thy life to share. Take from her father, take thy bride; Join hand to hand, and bliss betide! A faithful wife, most blest is she, And as thy shade will follow thee.”
- **Translation**: 

---

### Verse 18 (Ramayana 0.303)
- **Original**: Canto LXXIII. The Nuptials. 285 Thus as he spoke the monarch threw O'er her young limbs the holy dew, While Gods and saints were heard to swell The joyous cry, 'Tis well! 'Tis well! His daughter Sítá thus bestowed, O'er whom the sacred drops had flowed. King Janak's heart with rapture glowed. Then to Prince LakshmaG thus he cried: “Take Urmilá thine offered bride, And clasp her hand within thine own Ere yet the lucky hour be flown.” Then to Prince Bharat thus cried he; “Come, take the hand of Mándavi.” Then toZatrughna:“In thy grasp The hand of Srutakírti clasp. Now, Raghu's sons, may all of you Be gentle to your wives and true; [085] Keep well the vows you make to-day, Nor let occasion slip away.” King Janak's word the youths obeyed; The maidens' hands in theirs they laid. Then with their brides the princes went With ordered steps and reverent Round both the fire and Janak, round The sages and the sacred ground. A flowery flood of lucid dyes In rain descended from the skies, While with celestial voices blent Sweet strains from many an instrument, And the nymphs danced in joyous throng Responsive to the minstrel's song. Such signs of exultation they
- **Translation**: 

---

### Verse 19 (Ramayana 0.304)
- **Original**: 286 The Ramayana Saw on the princes' wedding day. Still rang the heavenly music's sound When Raghu's sons thrice circled round The fire, each one with reverent head, And homeward then their brides they led. They to the sumptuous palace hied That Janak's care had seen supplied. The monarch girt with saint and peer Still fondly gazing followed near. Canto LXXIV. Ráma With The Axe.254 Soon as the night had reached its close The hermit Vi[vámitra rose; To both the kings he bade adieu And to the northern hill withdrew. Ayodhyá's lord of high renown Received farewell, and sought his town. Then as each daughter left her bower King Janak gave a splendid dower, Rugs, precious silks, a warrior force, Cars, elephants, and foot, and horse, Divine to see and well arrayed; And many a skilful tiring-maid, And many a young and trusty slave The father of the ladies gave. 254 This is another Ráma, son of Jamadagni, called Para[uráma, or Ráma with the axe, from the weapon which he carried. He was while he lived the terror of the Warrior caste, and his name recalls long and fierce struggles between the sacerdotal and military order in which the latter suffered severely at the hands of their implacable enemy.
- **Translation**: 

---

### Verse 20 (Ramayana 0.305)
- **Original**: Canto LXXIV. Ráma With The Axe. 287 Silver and coral, gold and pearls He gave to his beloved girls. These precious gifts the king bestowed And sped his guest upon his road. The lord of Mithilá's sweet town Rode to his court and lighted down. Ayodhyá's monarch, glad and gay, Led by the seers pursued his way With his dear sons of lofty mind: The royal army marched behind. As on he fared the voice he heard Around of many a dismal bird, And every beast in wild affright Began to hurry to the right. The monarch to Va[ishmha cried: “What strange misfortune will betide? Why do the beasts in terror fly, And birds of evil omen cry? What is it shakes my heart with dread? Why is my soul disquieted?” Soon as he heard, the mighty saint Thus answered Da[aratha's plaint In sweetest tone:“Now, Monarch, mark, And learn from me the meaning dark. The voices of the birds of air Great peril to the host declare: The moving beasts the dread allay, So drive thy whelming fear away,”
- **Translation**: 

---

