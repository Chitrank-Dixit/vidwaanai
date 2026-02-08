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

### Verse 1 (Ramayana 0.1906)
- **Original**: 1888 The Ramayana my opinion impossible. Father Paolíno da S. Bartolommeo,1182 had already, together with other strange opinions of his own on Indian matters, brought forward a similar idea, that is to say that the exploit of Ráma which is the subject of the Rámáyan was a symbol and represented the course of the sun: thus he imagined that Brahmá was the earth, VishGu the water, and that his avatárs were the blessings brought by the fertilizing waters, etc. But such ideas, born at a time when Indo-sanskrit antiquities were enveloped in darkness, have been dissipated by the light of new studies. How could an epic so dear in India to the memory of the people, so deeply rooted for many centuries in the minds of all, so propagated and diffused through all the dialects and languages of those regions, which had become the source of many dramas which are still represented in India, which is itself represented every year with such magnificence and to such crowds of people in the neighbourhood of Ayodhyá, a poem welcomed at its very birth with such favour, as the legend relates, that the recitation of it by the first wandering Rhapsodists has consecrated and made famous all the places celebrated by them,[563] and where Ráma made a shorter or longer stay, how, I ask, could such an epic have been purely allegorical? How, upon a pure invention, upon a simple allegory, could a poem have been composed of about fifty thousand verses, relating with such force and power the events, and giving details with such exactness? On a theme purely allegorical there may easily be composed a short mythical poem, as for example a poem on Proserpine or Psyche: but never an epic so full of traditions and historical memories, so intimately connected with the life of the people, as the Rámáyan.1183 Excessive readiness to find allegory whenever some traces of symbolism occur, where the myth partly veils 1182 Systema brahmanicum, liturgicum, mythologicum, civile, exmonumentis Indicis, etc. 1183 Not only have the races of India translated or epitomized it, but foreign nations have appropriated it wholly or in part, Persia, Java, and Japan itself.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1907)
- **Original**: Final Notes. 1889 the historical reality, may lead and often has led to error. What poetical work of mythical times could stand this mode of trial? could there not be made, or rather has there not been made a work altogether allegorical, out of the Homeric poems? We have all heard of the ingenious idea of the anonymous writer, who in order to prove how easily we may pass beyond the truth in our wish to seek and find allegory everywhere, undertook with keen subtlety to prove that the great personality of Napoleon I. was altogether allegorical and represented the sun. Napoleon was born in an island, his course was from west to east, his twelve marshals were the twelve signs of the zodiac, etc. I conclude then, that the fundamental theme of the Rámáyan, that is to say the war of the Aryan Ráma against the Rákshases, an Hamitic race settled in the south, ought to be regarded as real and historical as far as regards its substance, although the mythic element intermingled with the true sometimes alters its natural and genuine aspect. How then did the Indo-Sanskrit epopeia form and complete it- self? What elements did it interweave in its progress? How did it embody, how did it clothe the naked and simple primitive datum? We must first of all remember that the Indo-European races pos- sessed the epic genius in the highest degree, and that they alone in the different regions they occupied produced epic poetry… But other causes and particular influences combined to nourish and develop the epic germ of the Sanskrit-Indians. Already in the Rig-veda are found hymns in which the Aryan genius preluded, so to speak, to the future epopeia, in songs that celebrated the heroic deeds of Indra, the combats and the victories of the tutelary Gods of the Aryan races over enemies secret or open, human or superhuman, the exploits and the memories of ancient heroes. More recently, at certain solemn occasions, as the very learned A. Weber remarks, at the solemnity, for example of the A[vamedha or sacrifice of the horse, the praises of the king who ordained the great rite were sung by bards and minstrels in songs composed
- **Translation**: 

---

### Verse 3 (Ramayana 0.1908)
- **Original**: 1890 The Ramayana for the purpose, the memories of past times were recalled and honourable mention was made of the just and pious kings of old. In theBráhma Gas, a sort of prose commentaries annexed to the Vedas, are found recorded stories and legends which allude to historical events of the past ages, to ancient memories, and to mythical events. Such popular legends which theBráhma Gas undoubtedly gathered from tradition admirably suited the epic tissue with which they were interwoven by successive hands.… Many and various mythico-historical traditions, suitable for epic development, were diffused among the Aryan races, those for example which are related in the four chapters containing the[564] description of the earth, the Descent of the Ganges, etc. The epic genius however sometimes created beings of its own and gave body and life to ideal conceptions. Some of the persons in the Rámáyan must be, in my opinion, either personifications of the forces of nature like those which are described with such vigour in theSháhnámah , or if not exactly created, exaggerated beyond human proportions; others, vedic personages much more ancient than Ráma, were introduced into the epic and woven into its narrations, to bring together men who lived in different and distant ages, as has been the case in times nearer to our own, in the epics, I mean, of the middle ages. In the introduction I have discussed the antiquity of the Rámáyan; and by means of those critical and inductive proofs which are all that an antiquity without precise historical dates can furnish I have endeavoured to establish with all the certainty that the subject admitted, that the original composition of the Rámáyan is to be assigned to about the twelfth century before the Christian era. Not that I believe that the epic then sprang to life in the form in which we now possess it; I think, and I have elsewhere expressed the opinion, that the poem during the course of its rhapsodical and oral propagation appropriated by way of episodes, traditions, legends and ancient myths.… But as far as regards the epic poem properly so called which celebrates
- **Translation**: 

---

### Verse 4 (Ramayana 0.1909)
- **Original**: Final Notes. 1891 the expedition of Ráma against the Rákshases I think that I have sufficiently shown that its origin and first appearance should be placed about the twelfth century B.C.; nor have I hitherto met with anything to oppose this chronological result, or to oblige me to rectify or reject it.… But an eminent philologist already quoted, deeply versed in these studies, A. Weber, has expressed in some of his writings a totally different opinion; and the authority of his name, if not the number and cogency of his arguments, compels me to say something on the subject. From the fact or rather the assumption that Megasthenes1184 who lived some time in India has made no mention either of the Mahábhárat or the Rámáyan Professor Weber argues that neither of these poems could have existed at that time; as regards the Rámáyan, the unity of its composition, the chain that binds together its different parts, and its allegorical character, show it, says Professor Weber, to be much more recent than the age to which I have assigned it, near to our own era, and according to him, later than the Mahábhárat. As for Megasthenes it should be observed, that he did not write a history of India, much less a literary history or anything at all resembling one, but a simple description, in great part physical, of India: whence, from his silence on literary matters to draw inferences regarding the history of Sanskrit literature would be the same thing as from the silence of a geologist with respect to the literature of a country whose valleys, mountains, and internal structure he is exploring, to conjecture that such and such a poem or history not mentioned by him did not exist at his time. We have only to look at the fragments of Megasthenes collected and published by Schwanbeck to see what was the nature and scope of hisIndica.… But only a few fragments of Megasthenes are extant; and to pretend that they should be argument and proof enough to judge the antiquity of a poem is to press the laws of criticism too far. To Professor Weber's argument as to the 1184 In the third century B.C.
- **Translation**: 

---

### Verse 5 (Ramayana 0.1910)
- **Original**: 1892 The Ramayana more or less recent age of the Rámáyan from the unity of its[565] composition, I will make one sole reply, which is that if unity of composition were really a proof of a more recent age, it would be necessary to reduce by a thousand years at least the age of Homer and bring him down to the age of Augustus and Virgil; for certainly there is much more unity of composition, a greater accord and harmony of parts in the Iliad and the Odyssey than in the Rámáyan. But in the fine arts perfection is no proof of a recent age: while the experience and the continuous labour of successive ages are necessary to extend and perfect the physical or natural sciences, art which is spontaneous in its nature can pro- duce and has produced in remote times works of such perfection as later ages have not been able to equal.” [566]
- **Translation**: 

---

### Verse 6 (Ramayana 0.1911)
- **Original**: INDEX OF PRINCIPAL NAMES Abhijit, 24. Abhikála, 176. Abhíra, 444. Abravanti, 374. Aditi, 31, 57, 58, 125, 201, 245, 246. Ádityas, 246, 403. Agastya, 5, 9, 40, 132, 151, 239, 240, 242, 244, 262, 265, 280, 375, 480, 491, 500. Ágneya, 178. Agni, 28, 74, 109, 132, 240, 243, 276. AgnivarGa, 82, 220. Agniketu, 433 note, 459. Ahalyá, 60, 61, 62. Ailadhána, 178. Air, 2, 28, 203. Airávat, 14, 110, 178, 246, 256, 267, 335, 399, 402, 415, 429, 437, 472. Aja, 82, 220, 465. Ájas, 270, 271. Akampan, 265, 266, 468, 481. Aksha, 6, 420, 469, 471. Akurvati, 178. Alaka, 203 note. Alambúshá, 59, 198, 199. Alarka, 104, 107. Amarávatí, 13, 203 note, 286. Ambarísha, 72, 73, 74, 82, 220. Amúrtarajas, 46. Anala, 455 note.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1912)
- **Original**: 1894 The Ramayana Analá, 245, 246. Ananta, 373. AnaraGya, 81, 219, 470. Anasúyá, 9, 226, 227, 228. Andhak, 264. Andhras, 549. Anga, 38. Angad, 342, 348, 350, 352 ff., 363, 364 note, 367, 374, 379 ff, 391, 402, 425 ff., 439, 442, 445, 448, 456, 458, 459, 475, 479 ff, 505. Angas, 15, 18, 19, 21, 102. Angiras, 133, 245. Anjan, 14, 368, 369. Anjaná, 392. An [udhána, 179. An [umán, 50, 53, 56, 82, 220. Anuhláda, 370. Aparparyat, 178. Apartála, 175. Apsarases, 57, 198, 199, 229, 378. Aptoryám, 24. Arishta, 424, 425. Aríshmanemi, 49, 245, 392. Arjun, 86. Arjuna, 518. Arthasádhak, 14. AruG, 246, Arundhatí, 19, 244, 413. Aryaman, 124. Áryan, 92. Asamanj, 50, 53, 82, 138, 220. Asit, 81, 219. A [ok, 14, 175.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1913)
- **Original**: INDEX OF PRINCIPAL NAMES 1895 A [oka, 6, 10, 101, 205, 278, 296, 297, 300, 318, 321, 357, 403, 444, 452, 456. Asta, 377, 379 note. Asurs, 57, 58, 380, 381, 387, 394, 407, 413, 420. A [vagríva, 246. A [vamedh, 29, 236 note. A [vapati, 89, 131, 178, 183. A [vatarí, 346. A [vin, 371. A [víní, 343. A [vins, 28, 36, 60, 62, 163, 246, 339, 343, 403, 490. Atikáya, 468, 478 ff. Atirátra, 24. Atri, 245, 561. Aurva, 373 note. Avantí, 374. Avindhya, 415. Ayodhyá, 4, 6, 11, 12, 14, 19, 32, 33, 38, 49, 70, 72, 79, 81, 83, 84, 85, 88, 95, 96,passim. Ayomukh, 374. Ayomukhi, 310. [567] Báhíka, 176. Bahuputra, 245. Bala, 264. Bálakhilyas, 63, 235, 270, 271, 374. Bali, 43, 59, 107, 275, 302, 421. Báli, 5, 9, 29, 318, 324, 328, 329, 333 ff., 344, 356 ff., 362, 364, 366, 367, 379, 380, 391, 404, 412, 420, 440, 442, 448, 456, 458, 475, 478, 500, 503, 505. Barbars, 66. Beauty, 26, 29, 58, 88, 283, 455. Bhadamadrá, 246. Bhadra, 52. Bhaga, 124, 243.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1914)
- **Original**: 1896 The Ramayana Bhagírath, 53, 54, 55, 82, 220, 372. Bhágírathí, 56. Bharadvája, 4, 7, 9, 10, 158, 159, 193, 196, 197, 199, 200, 201, 501. Bharat, 4, 9, 10, 32, 81, 83, 84, 88, 89, 94, 97,passim. Bharatas, 550. BháruG a, 178. Bhásí, 246. BhásakarGa, 420. Bhava, 78. Bhímá, 198. Bhogavatí, 12 note, 267, 375. Bhrigu, 40, 63, 73, 81, 85, 86, 88, 133, 220. Brahmá, 6, 7, 10, 19, 25, 26, 33, 38, 39, 42, 46, 48, 54, 56, 59, 61, 63, 65, 67, 68, 74, 75, 77, 81,passim. Brahmadatta, 46, 47. Brahmádikas, 133 note. Bhrahmamálas, 548. Budha, 287. Buddhist, 219. Cancer, 109. Ceylon, 375 note. Chaitra, 91. Chaitraratha, 41, 178, 199, 267, 279, 315, 493. Chakraván, 376. Champá, 30. ChaG a, 448. ChaG ála, 69, 70. Chandra, 464. Chatushmom, 24. Chitrá, 111, 250, 283. Chitrakúma, 4, 9, 160, 161, 197, 200, 201, 202, 209, 235, 236, 317, 416, 501. Chitraratha, 132.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1915)
- **Original**: INDEX OF PRINCIPAL NAMES 1897 Cholas, 549. Chúli, 47. Chyavan, 81, 220. Dadhimukh, 426. Dadhivakra, 364 note. Daitya, 125, 152, 211, 246, 289, 306, 371, 418. Daksha, 36, 78, 228, 245, 257, 396. Dánav, 255, 270, 306, 307, 311, 371, 372, 382, 432, 443, 477. Da G ak, 9, 99, 103, 117, 124, 126, 130, 166, 181, 199, 211, 238, 271, 374. Da G aká, 5. Danú, 245, 246, 313. Dapple skin, 64, 65. Dardar, 110, 198. Dardur, 448. Darímukha, 371. Da [árGa, 374. Dasáratha, 3, 9, 12, 14, 16, 18 ff., 25, 26, 29, 30, 32, 34, 41, 61, 62, 77, 79, 80 ff., 91, 92, 95,passim. Dasyus, 444. Devamí ha, 82. Devántak, 479, 480. Devarát, 77, 82, 86. Devasakhá, 378. Devavatí, 515. Dhanvantari, 57 note. Dhanyamáliní, 481. Dharmabhrit, 240. Dharmapál, 14. DharmáraGya, 46. Dharmavardhan, 179. Dhritaráshmrí, 246. [568] Dhrishmaketu, 82. Dhrishmi, 14, 202.
- **Translation**: 

---

### Verse 11 (Ramayana 0.1916)
- **Original**: 1898 The Ramayana Dhruvasandhi, 81, 219. Dhúmra, 371, 448. Dhúmráksha, 433 note, 465, 466. Dhúmrá [va, 60, 481. Dhundhumár, 81, 171, 219. Dikshá, 44. Dilípa, 5 note, 53, 54, 56, 82, 171, 190, 220. Diti, 58, 59, 245, 246, 323. Dragon, 101. Dri hanetra, 68. Drishmi, 202. DroGa, 464. Drumakulya, 444. Dundubhi, 333, 335, 338. Durdhar, 420. Durdharsha, 433 note. Durjaya, 256 note. Durmukha, 432, 433 note. Durvásas, 521. DúshaG, 5, 250, 254, 255, 256, 258, 259, 261, 264, 265, 267-271, 294, 461, 502. Dwida, 364 note. Dwijihva, 474. Dwivid, 371, 428, 430, 449, 451, 475, 483, 484. Dwivida, 28. Dyumatsena, 129. Ekapádakas, 549. Eka[ála, 179. Fame, 26, 283. Fate, 42, 68, 70, 71, 81, 119, 122, 123, 130, 181, 182, 195, 256, 293, 296, 309, 343, 349, 351, 354, 386, 404, 415, 439, 492. Fire, 2, 30, 45, 49, 218, 374. Fortune, 2, 58, 90, 94, 124, 146, 160, 188, 242, 244, 283, 449, 453.
- **Translation**: 

---

### Verse 12 (Ramayana 0.1917)
- **Original**: INDEX OF PRINCIPAL NAMES 1899 Fire-god, 74, 124, 328. Gádhi, 40, 48, 63, 64, 67, 68. Gaja, 364 note, 371, 429, 449, 459. Gálava, 518. Gandhamádan, 28, 159, 381, 429, 446, 476. Gandharva, 199, 256, 258, 259, 278, 285, 351, 396, 425, 437, 441, 454, 466, 468, 491. Gandharvas, 267, 270, 281, 283, 306, 307, 308, 318, 364, 370, 375, 377, 388, 394, 409, 420, 432, 449, 455, 472. Gandharví, 246, 265. Gangá, 7, 9, 37, 38, 45, 48, 49,passim. Garga, 133. Garu , 28, 29, 53, 246, 271, 373, 453, 465, 470, 475. Gautam, 60, 61, 62, 505. Gautama, 236. Gaváksha, 364 note, 429, 449, 468, 475, 476. Gavaya, 364 note, 371, 429, 448, 468. Gaya, 482. Gayá, 216. Gáyatrí, 243. Ghoralohamukhas, 548. Ghritáchí, 46, 198, 367. Girivraja, 46, 176. Glory, 301. Godávarí, 245, 247, 248, 249, 282, 303, 310, 374, 500. Gokarna, 54. Golabh, 351. Gomatí, 151, 179, 448, 502, 503. Gopa, 199. Guha, 4, 9, 152-156, 162, 192, 193, 194, 208, 501. Guhyakas, 378. Háhá, 198. Haihayas, 81, 219.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1918)
- **Original**: 1900 The Ramayana Hanúmán, 5, 9, 10, 28, 324 ff., 328, 332, 337, 340, 350, 355, 359, 360, 363, 364 note, 368, 371, 374, 378 ff., 392 ff., 411 ff., 424 ff., 449, 456. Hara, 448. Harí, 246. Hárítas, 66. Harya[va, 82. Hástinapura, 176. Hastiprishmhak, 179.[569] Havishyand, 68. Hayagriva, 346, 376. Hemá, 198, 382. Hemachandra, 60. Heti, 515. Himálaya, 3, 14, 45, 48, 49, 50, 53, 54, 61, 67, 76, 81, 88. Himaváu, 380. HiraGyaka[ipu, 391 note, 407. HiraGyanábha, 500. Hládini, 55, 178. Honour, 283. Hotri, 24. Hra[varomá, 82. Huhú, 198. Ikshumatí, 80, 176. Ikshváku, 2, 11, 13, 18, 24, 25, 35, 59, 60, 69, 70, 71, 73, 81, 82, 83, 90, 94, 96, 103, 219, 390. Ilval, 241. Indra, 2, 5, 13, 14, 25, 28, 29, 36, 39, 40, 43 ff., 50, 56, passim. Indrajánu, 371 note. Indrajít, 420, 432, 436, 437, 441, 455, 459 ff., 482, 485. Indra[atru, 433 note. Indra[ira, 178. Irávatí, 246.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1919)
- **Original**: INDEX OF PRINCIPAL NAMES 1901 Jábáli, 505. Jahnu, 55. Jáhnaví, 49, 55, 154. Jamadagni, 85, 86, 87, 119. Jámbaván, 371, 374, 388, 391, 393, 402, 425, 428, 429, 439, 446, 448, 456, 464, 483, 503. Jambudvip, 51, 373. Jambumálí, 418, 419, 420, 459, 460. Jambuprastha, 179. Jámbuvatu, 364 note. Janak, 4, 8, 9, 21, 45, 60, 61, 62, 77-85, 88, 090,passim. Janamejaya, 171. Janasthán, 225, 251, 254, 255, 264, 265, 271, 281, 282, 294, 295, 298, 308, 404, 439, 454, 463, 474, 493, 500. Játarúpa, 373. Jamáyu, 5. Jamáyus, 245, 247, 280, 288, 290, 308, 385 ff., 500, 502. Java, 231. Jáváli, 20, 80, 174, 217, 218, 219, 222. Jayá, 36. Jayanta, 14, 175. Jumna, 109, 501, 502. Jupiter, 144. Justice, 3, 35, 42, 149, 243, 346, 454. Jyotishmom, 24. Kabandha, 5, 9, 310-316, 446, 500. Kadrú, 246. Kadrumá, 246. Kaikasí, 516. Kaikeyí, 3, 4, 9, 27, 32, 88, 96-103,passim. Kailása, 38, 85, 92, 96, 110, 111, 267, 286, 357, 364, 368, 369, 373, 378, 421, 431. Kakustha, 35, 37, 82, 109, 110, 123, 137, 142, 147, 149, 151, 153, 192, 208, 211, 220, 311.
- **Translation**: 

---

### Verse 15 (Ramayana 0.1920)
- **Original**: 1902 The Ramayana Kalá, 378. Kálak, 246. Kálaká, 245, 246. Kálakámuka, 256 note. Kálamahí, 372. Kalinda, 178. Kálindí, 81, 160, 220. Kalinga, 179. Kalingas, 549, Kalmáshapáda, 82, 220. Káma 37, 38, 42, 283, 286, 296. Kámboja, 13, 66.[570] Kámbojas, 66. Kámpili, 47 Ka Gdu, 118, 380, 440. Kandarpa, 37, 74, 75, 76, 250, 269. Ka Gva, 440. Kanyákubja, 47. Kapil, 51, 52, 53. Kapivati, 179. Kardam, 245. KarGaprávaraGas, 548. Kártikeya, 243. Kárttavírya, 518. Ká [i, 21, 102. Kásíkosalas, 548. Ka [yap, 15, 16, 20, 30, 57-59, 80, 81, 86, 87, 91, 92, 118, 219, 215, passim. Kátyáyan, 505. Kátyáyana, 80, 174. Kau [alyá, 3, 23, 27, 30, 31, 79, 84, 88, 93, 94, 97, 98, 100, passim. Kau [ámbí, 46. Kau [ikas, 549.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1921)
- **Original**: INDEX OF PRINCIPAL NAMES 1903 Kau [ikí, 48, 372. Káverí, 375. Kaustubha, 58. Kávya, 40. Kekaya, 21, 84, 88, 90, 137, 139, 174, 175. Kerala, 190. Keralas, 549. Kesarí, 371. Ke [ini, 49, 50. Khara, 9, 225, 250 ff., 281, 288, 290, 294, 295, 433, 446, 451, 461, 477, 493. Kinnars, 270, 306, 308, 318, 321, 373, 425. Kimpurushas, 28 note. Kirátas, 66, 549. Kírtirát, 82. Kirtirátha, 82. Kishkindhá, 5, 333, 334, 336, 338, 339, 351, 357, 362, 369, 385, 449, 464, 500. Ko [al, 11, 102, 273, 307, 359, 418. Ko [ala, 151, 173. Krathan, 448. Kratu, 245. Krauncha, 310, 378, 476. Kraunchi, 246. Kri[á[va, 36, 41, 43. KrishGa, 497. KrishGagiri, 448. KrishGveni, 374. Krita, 57, 395. Krodhava[á, 245, 246. Kshatriyas, 246, 346. Kukshi, 81, 219. Kulingá, 176. Kumbha, 484.
- **Translation**: 

---

### Verse 17 (Ramayana 0.1922)
- **Original**: 1904 The Ramayana Kumbhakar Ga, 10, 250, 399, 411, 435 ff., 441, 470 ff. Kúmuda, 364 note, 448. Kunjar, 375, 392. Kuru(s), North, 198, 203, 315. Kurujángal, 176. Ku [a, 10, 46, 48, 63, 526. Ku [adhwaj, 80, 82, 88. Ku [ámba, 46. Ku [anábha, 46, 47, 48, 63. Ku [á[va, 60. Ku [ik, 33, 35, 36, 38, 44, 56, 62, 63, 68, 70 ff., 83. Ku míká, 179. Ku mikoshmiká, 179. Kuvera, 23, 88, 109, 110, 111, 112, 198, 199, 204, 232, 267, 378, 422, 431, 432, 483. Lakshma G, 4, 8, 11, 32, 36, 38, 40, 41, 44, 45, 56, 61, 79, 80, 82-84, 88, 91, 94, 97, 98,passim. Lakshmí, 88, 116, 146, 227, 400, 453, 462, 497. Lamba, 397. Lanká, 5, 10, 265, 267, 284, 286, 293, 295-297, 367, 387, 397, 411, 423 ff., 439, 456 ff. Lankamankamá, 515. Lava, 10, 526. Lohitya, 179. Lokapálas, 485. Lomapád, 15, 16, 18, 19, 21, 30.[571] Mádhaví, 520. Madhu, 26, 51, 57, 87, 95. Madhúka, 245. Madhushyand, 68, 74. Madrakas, 550. Magadh, 46, 102. Mágadnas, 548. Maghá, 83.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1923)
- **Original**: INDEX OF PRINCIPAL NAMES 1905 Mahábír, 82. Mahábala, 433 note. Mahábhárat, 520, 524, 551, 554. Mahádeva, 61, 515. Mahákapála, 256 note, 260. Mahámáli, 256 note. Mahándhrak, 82. Mahápadma, 14, 52. Mahápárá[va, 433, 436, 455, 478, 480, 487. Mahárath, 68. Maháromá, 82. MaháruG, 368. Mahá [aila, 368. Mahendra, 28, 59, 86, 87, 88, 140, 167, 213, 243, 244, 307, 336, 344, 364, 368, 370, 375, 490, 531, 554. Mahe [war, 369, 498. Mahí, 372. Máhishmatí, 518. Mahishikas, 549. Mahodar, 433 note, 450, 455, 474, 478 ff. Mahodaya, 46, 70, 71, 488. Maináka, 10, 394, 500 note. Mainda, 28, 364 note, 371, 428, 430, 439, 449, 451, 458, 482, 483. Makaráksha, 485 note. Malaja, 39. Málavas, 548. Malaya, 198, 324, 328, 375, 379, 430. Málí, 515, 516. Máliní, 175, 539. Malyaván, 454, 455. Mályavat, 515, 516. Mánas, 38. MandakarGi, 240.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1924)
- **Original**: 1906 The Ramayana Mandákiní, 200, 201, 203, 209, 234, 235, 304, 322, 416 note. Mandalí, 556. Mandar, 57, 163, 285, 362, 368, 372, 399, 402, 421, 485, 491, 493, 525. Mandarí, 444. Mándhátá, 81, 219, 347, 518. Mándavi, 84. Má G avya, 226 note. Mandehas, 373. Mandodarí, 402, 492, 500, 516. Mandra, 14. Ma Gibhadra, 441. Manthará, 40, 96, 97, 99, 187. Manu, 11, 12, 13, 81, 103, 151, 179, 219, 245, 246, 347, 490, 505, 537, 555. Marícha, 58. Márícha, 5, 9, 35, 39, 40, 44, 266, 271-280, 298. Maríchi, 81, 91, 219, 245. Maríchipas, 270, 271. MárkaG eya, 80, 174. Mars, 93, 144, 339, 404, 445, 467, 489. Maru, 82, 220. Maruts, 25, 54, 59, 403, 517, 547, 555. Máshas, 270, 271. Mátali, 109, 142, 489, 491, 493. Matanga, 14, 246, 315, 316, 317, 318, 319, 336, 337, 380. Mátangí, 246. Mátari[va, 389. Matsya, 102, 523, 537, 549. Maya, 293, 382, 432, 488. Máyá, 293, 521. Máyáví, 333, 334, 379. Meghamáli, 256 note. Meghanáda, 10.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1925)
- **Original**: INDEX OF PRINCIPAL NAMES 1907 Mekhal, 374. Mená, 49, 394 note. Menaká, 74. Mercury, 144, 339, 467. Meru, 4, 49, 92, 109, 110, 142, 182, 232, 236, 254, 291, 315, 368, 370, 377, 380, 418, 493. Meru [avarGi, 382. Mina, 32. Mi [rake[í, 199. Mithi, 82. Míthilá, 9 note, 21, 45, 60, 61, 78, 81, 83, 84, 85. Mitraghna, 459. [572] Mlechchhas, 66, 537, 550. Modesty, 26. Moon, 30, 42, 58, 109 ff., 124, 218, 227, 243, 276, 367, 413, 414, 488. Mriga, 14. Mrigamandá, 246. Mrigí, 246. Mudgalya, 174. Nábhág, 82, 220. Nágadantá, 198. Nágas, 12, 55, 66, 68, 145, 270, 273, 395, 409, 413, 420, 427, 518. Nahush, 82, 95, 171, 190, 220, 307. Nairrit, 430. Nala, 10, 340, 364 note, 428, 444, 445, 448, 449, 468, 475, 483. Nalá, 246. Naliní, 55, 203, 204, 267, 436. Namuchi, 39, 261, 264, 275, 336. Nandá, 415. Nandan, 26, 175, 200, 267, 279, 315, 316, 426. Nandi, 249, 421.
- **Translation**: 

---

