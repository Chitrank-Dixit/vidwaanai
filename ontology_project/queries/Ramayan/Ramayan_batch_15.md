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

### Verse 1 (Ramayan 0.281)
- **Original**: Canto LXVII. The Breaking Of The Bow. 263 Wrong-doers, with their lords and host, And all their valour's idle boast. This heavenly bow, exceeding bright, These youths shall see, O Anchorite. Then if young Ráma's hand can string The bow that baffled lord and king, To him I give, as I have sworn, My Sítá, not of woman born.” Canto LXVII. The Breaking Of The Bow. Then spoke again the great recluse: “This mighty bow, O King, produce.” King Janak, at the saint's request, This order to his train addressed: “Let the great bow be hither borne, Which flowery wreaths and scents adorn.” Soon as the monarch's words were said, His servants to the city sped, Five thousand youths in number, all Of manly strength and stature tall, The ponderous eight-wheeled chest that held The heavenly bow, with toil propelled. At length they brought that iron chest, And thus the godlike king addressed: “This best of bows, O lord, we bring, Respected by each chief and king, And place it for these youths to see, If, Sovereign, such thy pleasure be.”
- **Translation**: 

---

### Verse 2 (Ramayan 0.282)
- **Original**: 264 The Ramayana With suppliant palm to palm applied King Janak to the strangers cried: “This gem of bows, O Bráhman Sage, Our race has prized from age to age, Too strong for those who yet have reigned, Though great in might each nerve they strained.[079] Titan and fiend its strength defies, God, spirit, minstrel of the skies. And bard above and snake below Are baffled by this glorious bow. Then how may human prowess hope With such a bow as this to cope? What man with valour's choicest gift This bow can draw, or string, or lift? Yet let the princes, holy Seer, Behold it: it is present here.” Then spoke the hermit pious-souled: “Ráma, dear son, the bow behold.” Then Ráma at his word unclosed The chest wherein its might reposed, Thus crying, as he viewed it:“Lo! I lay mine hand upon the bow: May happy luck my hope attend Its heavenly strength to lift or bend.” “Good luck be thine,” the hermit cried: “Assay the task!” the king replied. Then Raghu's son, as if in sport, Before the thousands of the court, The weapon by the middle raised That all the crowd in wonder gazed. With steady arm the string he drew Till burst the mighty bow in two. As snapped the bow, an awful clang,
- **Translation**: 

---

### Verse 3 (Ramayan 0.283)
- **Original**: Canto LXVII. The Breaking Of The Bow. 265 Loud as the shriek of tempests, rang. The earth, affrighted, shook amain As when a hill is rent in twain. Then, senseless at the fearful sound, The people fell upon the ground: None save the king, the princely pair, And the great saint, the shock could bear. When woke to sense the stricken train, And Janak's soul was calm again, With suppliant hands and reverent head, These words, most eloquent, he said: “O Saint, Prince Ráma stands alone: His peerless might he well has shown. A marvel has the hero wrought Beyond belief, surpassing thought. My child, to royal Ráma wed, New glory on our line will shed: And true my promise will remain That hero's worth the bride should gain. Dearer to me than light and life, My Sítá shall be Ráma's wife. If thou, O Bráhman, leave concede, My counsellors, with eager speed, Borne in their flying cars, to fair Ayodhyá's town the news shall bear, With courteous message to entreat The king to grace my royal seat. This to the monarch shall they tell, The bride is his who won her well: And his two sons are resting here Protected by the holy seer. So, at his pleasure, let them lead The sovereign to my town with speed.”
- **Translation**: 

---

### Verse 4 (Ramayan 0.284)
- **Original**: 266 The Ramayana The hermit to his prayer inclined And Janak, lord of virtuous mind, With charges, to Ayodhyá sent His ministers: and forth they went. Canto LXVIII. The Envoys' Speech. Three nights upon the road they passed To rest the steeds that bore them fast, And reached Ayodhyá's town at last. Then straight at Da[aratha's call They stood within the royal hall, Where, like a God, inspiring awe, The venerable king they saw. With suppliant palm to palm applied, And all their terror laid aside, They spoke to him upon the throne With modest words, in gentle tone: “Janak, Videha's king, O Sire, Has sent us hither to inquire The health of thee his friend most dear, Of all thy priests and every peer. Next Ku[ik's son consenting, thus King Janak speaks, dread liege, by us: “I made a promise and decree That valour's prize my child should be. Kings, worthless found in worth's assay, With mien dejected turned away. Thy sons, by Vi[vámitra led, Unurged, my city visited, And peerless in their might have gained
- **Translation**: 

---

### Verse 5 (Ramayan 0.285)
- **Original**: Canto LXVIII. The Envoys' Speech. 267 My daughter, as my vow ordained. Full in a vast assembly's view Thy hero Ráma broke in two The gem of bows, of monstrous size, That came a treasure from the skies. Ordained the prize of hero's might, Sítá my child is his by right. Fain would I keep my promise made, If thou, O King, approve and aid. Come to my town thy son to see: Bring holy guide and priest with thee. O lord of kings, my suit allow, And let me keep my promised vow. So joying for thy children's sake Their triumph too shalt thou partake, With Vi[vámitra's high consent.” Such words with friendship eloquent Spoke Janak, fair Videha's king, By Zatánanda's counselling.” The envoys thus the king addressed, And mighty joy his heart possessed. To Vámadeva quick he cried, Va [ishmha, and his lords beside: “Lakshma G, and he, my princely boy Who fills Kau[alyá's soul with joy, By Vi[vámitra guarded well Among the good Videhans dwell. [080] Their ruler Janak, prompt to own The peerless might my child has shown, To him would knit in holy ties His daughter, valour's lovely prize. If Janak's plan seem good to you, Come, speed we to his city too,
- **Translation**: 

---

### Verse 6 (Ramayan 0.286)
- **Original**: 268 The Ramayana Nor let occasion idly by.” He ceased. There came a glad reply From priest and mighty saint and all The councillors who thronged the hall. Then cried the king with joyous heart: “To-morrow let us all depart.” That night the envoys entertained With honour and all care remained. Canto LXIX. Dasaratha's Visit. Soon as the shades of night had fled, Thus to the wise Sumantra said The happy king, while priest and peer, Each in his place, were standing near: “Let all my treasurers to-day, Set foremost in the long array, With gold and precious gems supplied In bounteous store, together ride. And send you out a mighty force, Foot, chariot, elephant, and horse. Besides, let many a car of state, And noblest steeds, my will await. Va [ishmha, Vámadeva sage, And MárkaGdeya's reverend age, Jáváli, Ka[yap's godlike seed, And wise Kátyáyana, shall lead. Thy care, Sumantra, let it be To yoke a chariot now for me, That so we part without delay: These envoys hasten me away.”
- **Translation**: 

---

### Verse 7 (Ramayan 0.287)
- **Original**: Canto LXIX. Dasaratha's Visit. 269 So fared he forth. That host, with speed, Quadruple, as the king decreed, With priests to head the bright array, Followed the monarch on his way. Four days they travelled on the road, And eve Videha's kingdom showed. Janak had left his royal seat The venerable king to greet, And, noblest, with these words addressed That noblest lord, his happy guest: “Hail, best of kings: a blessed fate Has led thee, Monarch, to my state. Thy sons, supreme in high emprise, Will gladden now their father's eyes. And high my fate, that hither leads Va [ishmha, bright with holy deeds, Girt with these sages far-renowned, Like Indra with the Gods around. Joy! joy! for vanquished are my foes: Joy! for my house in glory grows, With Raghu's noblest sons allied, Supreme in strength and valour's pride. To-morrow with its early light Will shine on my completed rite. Then, sanctioned by the saints and thee, The marriage of thy Ráma see.” Then Da[aratha, best of those Whose speech in graceful order flows, With gathered saints on every side, Thus to the lord of earth replied: “A truth is this I long have known, A favour is the giver's own. What thou shalt bid, O good and true,
- **Translation**: 

---

### Verse 8 (Ramayan 0.288)
- **Original**: 270 The Ramayana We, as our power permits, will do.” That answer of the truthful lord, With virtuous worth and honour stored, Janak, Videha's noble king, Heard gladly, greatly marvelling. With bosoms filled with pleasure met Long-parted saint and anchoret, And linked in friendship's tie they spent The peaceful night in great content. Ráma and LakshmaG thither sped, By sainted Vi[vámitra led, And bent in filial love to greet Their father, and embraced his feet. The aged king, rejoiced to hear And see again his children dear, Honoured by Janak's thoughtful care, With great enjoyment rested there. King Janak, with attentive heed, Consulted first his daughters' need, And ordered all to speed the rite; Then rested also for the night. Canto LXX. The Maidens Sought.
- **Translation**: 

---

### Verse 9 (Ramayan 0.289)
- **Original**: Canto LXX. The Maidens Sought. 271 Then with the morn's returning sun. King Janak, when his rites were done, Skilled all the charms of speech to know, Spoke to wiseZatánanda so: “My brother, lord of glorious fame, My younger, Ku[adhwaj by name, Whose virtuous life has won renown, Has settled in a lovely town, Sánká[yá, decked with grace divine, Whose glories bright as Pushpak's shine, While Ikshumatí rolls her wave Her lofty rampart's foot to lave. Him, holy priest, I long to see: The guardian of my rite is he: That my dear brother may not miss A share of mine expected bliss.” Thus in the presence of the priest The royal Janak spoke, and ceased. Then came his henchmen, prompt and brave, [081] To whom his charge the monarch gave. Soon as they heard his will, in haste With fleetest steeds away they raced, To lead with them that lord of kings, As Indra's call Lord VishGu brings. Sánká[yá's walls they duly gained, And audience of the king obtained. To him they told the news they brought Of marvels past and Janak's thought. Soon as the king the story knew From those good envoys swift and true, To Janak's wish he gave assent, And swift to Míthilá he went. He paid to Janak reverence due,
- **Translation**: 

---

### Verse 10 (Ramayan 0.290)
- **Original**: 272 The Ramayana And holyZatánanda too, Then sate him on a glorious seat For kings or Gods celestial meet. Soon as the brothers, noble pair Peerless in might, were seated there, They gave the wise Sudáman, best Of councillors, their high behest: “Go, noble councillor,” they cried, “And hither to our presence guide Ikshváku's son, Ayodhyá's lord, Invincible by foeman's sword, With both his sons, each holy seer, And every minister and peer.” Sudáman to the palace flew, And saw the mighty king who threw Splendour on Raghu's splendid race, Then bowed his head with seemly grace: “O King, whose hand Ayodhyá sways, My lord, whom Míthilá obeys, Yearns with desire, if thou agree, Thee with thy guide and priest to see.” Soon as the councillor had ceased, The king, with saint and peer and priest, Sought, speeding through the palace gate, The hall where Janak held his state. There, with his nobles round him spread, Thus to Videha's lord be said: “Thou knowest, King, whose aid divine Protects Ikshváku's royal line. In every need, whate'er befall, The saint Va[ishmha speaks for all. If Vi[vámitra so allow, And all the saints around me now, The sage will speak, at my desire,
- **Translation**: 

---

### Verse 11 (Ramayan 0.291)
- **Original**: Canto LXX. The Maidens Sought. 273 As order and the truth require.” Soon as the king his lips had stilled, Up rose Va[ishmha, speaker skilled. And to Videha's lord began In flowing words that holy man: “From viewless Nature Brahmá rose, No change, no end, no waste he knows. A son had he Maríchi styled, And Ka [yap was Maríchi's child. From him Vivasvat sprang: from him Manu whose fame shall ne'er be dim. Manu, who life to mortals gave, Begot Ikshváku good and brave. First of Ayodhyá's kings was he, Pride of her famous dynasty. From him the glorious Kukshi sprang, Whose fame through all the regions rang. Rival of Kukshi's ancient fame, His heir, the great Vikukshi, came, His son was VáGa, lord of might; His AnaraGya, strong to fight. His son was Prithu, glorious name; From him the good Tri[anku came. He left a son renowned afar, Known by the name of Dhundhumár. His son, who drove the mighty car, Was Yuvaná [va, feared in war. He passed away. Him followed then His son Mándhátá, king of men. His son was blest in high emprise, Susandhi, fortunate and wise. Two noble sons had he, to wit Dhruvasandhi and Prasenajit.
- **Translation**: 

---

### Verse 12 (Ramayan 0.292)
- **Original**: 274 The Ramayana Bharat was Dhruvasandhi's son, And glorious fame that monarch won. The warrior Asit he begot. Asit had warfare, fierce and hot, With rival kings in many a spot, Haihayas, Tálajanghas styled, And Za[ivindus, strong and wild. Long time he strove, but forced to yield Fled from his kingdom and the field. With his two wives away he fled Where high Himálaya lifts his head, And, all his wealth and glory past, He paid the dues of Fate at last. The wives he left had both conceived— So is the ancient tale believed— One, of her rival's hopes afraid Fell poison in her viands laid. It chanced that Chyavan, Bhrigu's child, Had wandered to that pathless wild, And there Himálaya's lovely height Detained him with a strange delight. There came the other widowed queen, With lotus eyes and beauteous mien, Longing a noble son to bear, And wooed the saint with earnest prayer. When thus Kálindi,248 fairest dame, With reverent supplication came, To her the holy sage replied: “Born with the poison from thy side, O happy Queen, shall spring ere long An infant fortunate and strong. Then weep no more, and check thy sighs, 248 A different lady from the Goddess of the Jumna who bears the same name.
- **Translation**: 

---

### Verse 13 (Ramayan 0.293)
- **Original**: Canto LXX. The Maidens Sought. 275 Sweet lady of the lotus eyes.” The queen, who loved her perished lord, For meet reply, the saint adored, And, of her husband long bereaved, She bore a son by him conceived. Because her rival mixed the bane [082] To render her conception vain, And fruit unripened to destroy, Sagar249 she called her darling boy. To Sagar Asamanj was heir: Bright An[umán his consort bare. An [umán's son, Dilípa famed, Begot a son Bhagírath named. From him the great Kakutstha rose: From him came Raghu, feared by foes, Of him sprang Purushádak bold, Fierce hero of gigantic mould: Kalmáshapáda's name he bore, Because his feet were spotted o'er.250 From him cameZankaG, and from him Sudar[an, fair in face and limb. From beautiful Sudar[an came Prince AgnivarGa, bright as flame. His son wasZíghraga, for speed Unmatched; and Maru was his seed. Pra[u[ruka was Maru's child; His son was Ambarísha styled. Nahush was Ambarísha's heir, The mighty lord of regions fair: Nahush begot Yayáti: he, 249 This is another fanciful derivation,Sa— with, andgara— poison. 250 Purushádak means a cannibal. First calledKalmáshapáda on account of his spotted feet he is said to have been turned into a cannibal for killing the son of Va[ishmha.
- **Translation**: 

---

### Verse 14 (Ramayan 0.294)
- **Original**: 276 The Ramayana Nábhág of happy destiny. Son of Nábhág was Aja: his, The glorious Da[aratha is, Whose noble children boast to be Ráma and LakshmaG, whom we see. Thus do those kings of purest race Their lineage from Ikshváku trace: Their hero lives the right maintained, Their lips with falsehood ne'er were stained. In Ráma's and in LakshmaG's name Thy daughters as their wives I claim, So shall in equal bands be tied Each peerless youth with peerless bride.” Canto LXXI. Janak's Pedigree. Then to the saint supremely wise King Janak spoke in suppliant guise: “Deign, Hermit, with attentive ear, Mv race's origin to hear. When kings a daughter's hand bestow, 'Tis right their line and fame to show. There was a king whose deeds and worth Spread wide his name through heaven and earth, Nimi, most virtuous e'en from youth, The best of all who love the truth. His son and heir was Mithi, and His Janak, first who ruled this land. He left a son Udávasu, Blest with all virtues, good and true. His son was Nandivardhan, dear
- **Translation**: 

---

### Verse 15 (Ramayan 0.295)
- **Original**: Canto LXXI. Janak's Pedigree. 277 For pious heart and worth sincere. His son Suketu, hero brave, To Devarát, existence gave. King Devarát, a royal sage, For virtue, glory of the age, Begot Vrihadratha; and he Begot, his worthy heir to be, The splendid hero Mahábír Who long in glory governed here. His son was Sudhriti, a youth Firm in his purpose, brave in sooth, His son was Dhrismaketu, blest With pious will and holy breast. The fame of royal saint he won: Harya[va was his princely son. Harya[va's son was Maru, who Begot Pratíndhak, wise and true. Next Kírtiratha held the throne, His son, for gentle virtues known. Then followed Devamidha, then Vibudh, Mahándhrak, kings of men. Mahándhrak's son, of boundless might, Was Kírtirát, who loved the right. He passed away, a sainted king, And Maháromá following To SwarGaromá left the state. Then Hra[varomá, good and great, Succeeded, and to him a pair Of sons his royal consort bare, Elder of these I boast to be: Brave Ku[adhwaj is next to me.251 251 “In the setting forth of these royal genealogies the Bengal recension varies but slightly from the Northern. The first six names of the genealogy of the Kings of Ayodhyá are partly theogonical and partly cosmogonical; the
- **Translation**: 

---

### Verse 16 (Ramayan 0.296)
- **Original**: 278 The Ramayana Me then, the elder of the twain, My sire anointed here to reign. He bade me tend my brother well, Then to the forest went to dwell. He sought the heavens, and I sustained The burden as by law ordained, And noble Ku[adhwaj, the peer Of Gods, I ever held most dear. Then came Sánká[yá's mighty lord, Sudhanvá, threatening siege and sword, And bade me swift on him bestow Ziva's incomparable bow,[083] And Sítá of the lotus eyes: But I refused each peerless prize. Then, host to host, we met the foes, And fierce the din of battle rose, Sudhanvá, foremost of his band, Fell smitten by my single hand. When thus Sánká[yá's lord was slain, I sanctified, as laws ordain, My brother in his stead to reign, Thus are we brothers, Saint most high The younger he, the elder I. Now, mighty Sage, my spirit joys To give these maidens to the boys. Let Sítá be to Ráma tied. And Urmilá be LakshmaG's bride. First give, O King, the gift of cows, As dowry of each royal spouse, Due offerings to the spirits pay, And solemnize the wedding-day. other names are no doubt in accordance with tradition and deserve the same amount of credence as the ancient traditional genealogies of other nations.” G ORRESIO {FNS .
- **Translation**: 

---

### Verse 17 (Ramayan 0.297)
- **Original**: Canto LXXII. The Gift Of Kine. 279 The moon tonight, O royal Sage, In Maghá's252 House takes harbourage; On the third night his rays benign In second Phálguni253 will shine: Be that the day, with prosperous fate, The nuptial rites to celebrate.” Canto LXXII. The Gift Of Kine. When royal Janak's words were done, Joined with Va[ishmha Ku[ik's son, The mighty sage began his speech: “No mind may soar, no thought can reach The glories of Ikshváku's line, Or, great Videha's King, of thine: None in the whole wide world may vie With them in fame and honours high. Well matched, I ween, in holy bands, These peerless pairs will join their hands. But hear me as I speak once more; Thy brother, skilled in duty's lore, Has at his home a royal pair Of daughters most divinely fair. I for the hands of these sweet two For Bharat andZatrughna sue, Both princes of heroic mould, Wise, fair of form, and lofty-souled. All Da[aratha's sons, I ween, 252 The tenth of the lunar asterisms, composed of five stars. 253 There are two lunar asterisms of this name, one following the other immediately, forming the eleventh and twelfth of the lunar mansions.
- **Translation**: 

---

### Verse 18 (Ramayan 0.298)
- **Original**: 280 The Ramayana Own each young grace of form and mien: Brave as the Gods are they, nor yield To the great Lords the worlds who shield. By these, good Prince of merits high, Ikshváku's house with thine ally.” The suit the holy sage preferred, With willing ear the monarch heard: Va [ishmha's lips the counsel praised: Then spake the king with hands upraised: “Now blest indeed my race I deem, Which your high will, O Saints supreme, With Da[aratha's house unites In bonds of love and marriage rites. So be it done. My nieces twain Let Bharat andZatrughna gain, And the four youths the selfsame day Four maiden hands in theirs shall lay. No day so lucky may compare, For marriage— so the wise declare— With the last day of Phálguni Ruled by the genial deity.” Then with raised hands in reverence due To those arch-saints he spoke anew: “I am your pupil, ever true: To me high favour have ye shown; Come, sit ye on my royal throne, For Da[aratha rules these towers E'en as Ayodhyá now is ours. Do with your own whate'er ye choose: Your lordship here will none refuse.”
- **Translation**: 

---

### Verse 19 (Ramayan 0.299)
- **Original**: Canto LXXIII. The Nuptials. 281 He spoke, and to Videha's king Thus Da[aratha, answering: “Boundless your virtues, lords, whose sway The realms of Mithilá obey. With honouring care you entertain. Both holy sage and royal train. Now to my house my steps I bend— May blessings still on you at end— Due offerings to the shades to pay.” Thus spoke the king, and turned away: To Janak first he bade adieu, Then followed fast those holy two. The monarch reached his palace where The rites were paid with solemn care. When the next sun began to shine He rose and made his gift of kine. A hundred thousand cows prepared For each young prince the Bráhmans shared. Each had her horns adorned with gold; And duly was the number told, Four hundred thousand perfect tale: Each brought a calf, each filled a pail. And when that glorious task was o'er, The monarch with his children four, Showed like the Lord of Life divine When the worlds' guardians round him shine. [084] Canto LXXIII. The Nuptials.
- **Translation**: 

---

### Verse 20 (Ramayan 0.300)
- **Original**: 282 The Ramayana On that same day that saw the king His gift of kine distributing, The lord of Kekaya's son, by name Yudhájit, Bharat's uncle, came, Asked of the monarch's health, and then Addressed the reverend king of men: “The lord of Kekaya's realm by me Sends greeting, noble King, to thee: Asks if the friends thy prayers would bless Uninterrupted health possess. Right anxious, mighty King, is he My sister's princely boy to see. For this I sought Ayodhyá fair The message of my sire to bear. There learning, O my liege, that thou With sons and noble kinsmen now Wast resting here, I sought the place Longing to see my nephew's face.” The king with kind observance cheered His friend by tender ties endeared, And every choicest honour pressed Upon his honourable guest. That night with all his children spent, At morn King Da[aratha went, Behind Va[ishmha and the rest, To the fair ground for rites addressed. Then when the lucky hour was nigh Called Victory, of omen high, Came Ráma, after vow and prayer For nuptial bliss and fortune fair, With the three youths in bright attire, And stood beside his royal sire. To Janak then Va[ishmha sped,
- **Translation**: 

---

