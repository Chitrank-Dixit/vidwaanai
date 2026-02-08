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

### Verse 1 (Ramayana 0.1926)
- **Original**: 1908 The Ramayana Nandigráma, 4, 6, 9, 224, 502, 503. Nandí[vara, 471. Nandivardhan, 82. Nárad, 1, 2, 8, 9, 124, 199, 543. Narak, 479. Narántak, 479. NáráyaG, 25, 26, 95, 393, 474, 497, 516, 517, 522, 535, 559. Narmadá, 374, 448, 518. Nikumbha, 432, 433 note, 437, 459, 484. Níla, 28, 340, 352, 360, 364 note, 371, 374, 428, 429, 430, 446, 448, 449, 456, 458, 459, 469, 472, 475, 482. Nimi, 77, 82. Ni[akar, 389, 390. Nishádas, 4, 152, 192, 196, 271, 501, 537. Ocean, 10, 95, 144, 285, 286, 336, 346, 387. OshmhakarGakas, 548. Pahlavas, 66. Páka, 252, 297, 498. Pampá, 5, 9, 235, 293, 314-321, 327. Panas, 371, 428, 448, 464. Panasa, 455 note. Panchajan, 376. Panchála, 176, 539. Panchápsaras, 240. Panchavama, 9. Panchavamí, 244, 245, 247. PáG yas, 375, 549. Pará[ara, 517. Para[uráma, 119 note, 523, 531. Paravíráksha, 256 note. Páriyátra, 376, 448. Parjanya, 112, 174, 261, 448. Párvati, 249 note, 515, 542. Paulastya, 472.
- **Translation**: 

---

### Verse 2 (Ramayana 0.1927)
- **Original**: INDEX OF PRINCIPAL NAMES 1909 Paulomí, 29, 370. Pávaní, 55. Phálguní, 83. Pináka, 67. Pitris, 550. Prabháva, 363. Prachetas, 1, 245. Praghas, 420, 459, 460. Prágvam, 179. Prahasta, 399, 418, 419, 421, 422, 432 ff., 441, 451, 452, 455, 456, 471, 481. Praheti, 515. Prahláda, 391. Prajangha, 459, 460. Prajápati, 133 note, 554, 560. Pralamba, 175. Pramátha, 256 note. Pramathí, 260, 448. Pramati, 455 note. Prasenajit, 81, 219. Pra[ravaG, 304, 357, 380, 383, 415, 426. Prasthalas, 550. Pra[u[[ruka, 82, 220. Pratindhak, 82. Pravargya, 22. Prayág, 158, 159, 196. [573] Prithu, 81, 219. Prithu[yáma, 256 note. Proshmhapadá, 32. Pulah, 245. Pulastya, 35, 245, 254, 268, 288, 408, 515. Pulindas, 550. Puloma, 370. Punarvasu, 93.
- **Translation**: 

---

### Verse 3 (Ramayana 0.1928)
- **Original**: 1910 The Ramayana PuG aríká, 199. PuG ras, 548, 549. Punjikasthalá, 436, 552. Puranda, 522. Purandara, 384, 522. Purúravas, 286, 544, 545. Purusha, 256 note, 559. Purushádak, 82, 220. Purushottam, 498, 517. Púshá, 124. Pushpak, 10, 80, 286, 499, 519. Pushya, 32, 90, 92, 94, 96, 98, 109, 126. Rabhasa, 433 note. Rághava, 5 note. Raghu, 5, 9, 22, 32 ff., 50, 56, 61,passim. Raghunandana, 522. Ráhu, 93, 223, 261, 272, 303, 351, 480. Rain, Lord of, 92, 222. Rájagriha, 174, 175. Ráma, passim. Rámáyana, 8 note, 10, 11, 541, 542. Rambhá, 75, 232, 448. Rama Gá, 199. Ra[miketu, 433 note, 459. RávaG, 5, 9, 10, 25, 26, 32, 35,passim. ReGuká, 63, 119. Richíka, 48, 73, 86. Right, 42, 68. Riksharajas, 386, 442. Rikshaván, 448. Rishabh, 373, 375, 429, 446, 476, 483. Rishmikas, 549. Rishyamúka, 9, 314, 315, 316, 318 ff., 332, 335, 339, 340, 353, 380, 500.
- **Translation**: 

---

### Verse 4 (Ramayana 0.1929)
- **Original**: INDEX OF PRINCIPAL NAMES 1911 Rishya[ring, 15-24, 29, 30. RohiGí, 4, 112, 223, 227, 246, 251, 282, 287, 367, 404, 413, 445. Rohitas, 376, 558. Rudhirá[ana, 256 note. Rudra, 49, 57, 67, 77, 78, 162, 249, 257, 264, 283, 296, 378, 413, 483. Rudras, 246, 558. Rukmi Gí, 517. Rumá, 346, 349, 350, 363, 366, 367, 371, 385, 403. Ruman, 371. Sachí, 29, 202, 234, 238, 276, 286, 297, 370, 408, 415, 494, 519, 522. Sádhyas, 490, 555, 558, 559. Sagar, 11, 50 ff., 82, 119, 137, 171, 441. Sahadeva, 60. Sahya, 429, 430. Zaivya, 104, 107, 171, 533. Zakas, 66, 550. Zakra, 75, 234, 307, 313, 336, 344, 448, 464. Zálmalí, 176, 539. Zályakartan, 178. Záman, 186, 326, 359. Zambar, 479. Zambara, 99, 100. Sampáti, 5, 9, 246, 364 note, 385, 387 ff., 412, 455 note, 459, 460, 464. Samprakshálas, 235. Sanatkumár, 15, 16. Sandhyá, 515. Sanháras, 36. Sanhráda, 474. Zani[char, 283. Zankan, 82.
- **Translation**: 

---

### Verse 5 (Ramayana 0.1930)
- **Original**: 1912 The Ramayana Zankar, 57, 335. Sánká[yá, 80, 81, 82, 83. Zankha, 555. Zankhan, 220, 432. Sanrochan, 448. Zan[ray, 245. Zántá, 16, 19, 29, 30, 31. Zarabh, 364 note, 439, 476. Zarabhanga, 9, 233, 234, 235, 236, 265, 502. ZaradaG á, 176, 539. Saramá, 452, 453. SáraG, 446, 447, 455. Sarandib, 375 note. Sáranga, 556. Sarasvatí, 178, 372, 516, 522. Zárdúla, 441, 449, 450. Zárdúlí, 246.[574] Sarjú, 11, 20, 22, 36, 37, 38, 50,passim. Sárvabhauma, 429. Sarvartírtha, 179. Za[ivindhus, 81, 219. Zatabali, 371, 377, 379, 380. Zatadrú, 178, 539. Zatahradá, 231. Zatánanda, 62, 63, 77, 79, 80, 81, 84. Zatrughna, 32, 83, 84, 88, 89, 97,passim. Zatrunjay, 504. Satyaván, 129. Satyavatí, 48. Sávitrí, 129, 227. Zavarí, 315, 316, 317. Saumanas, 373. SávarGí, 377. Seven Rishis, 23.
- **Translation**: 

---

### Verse 6 (Ramayana 0.1931)
- **Original**: INDEX OF PRINCIPAL NAMES 1913 Zesha, 245. Siddhárth, 14, 137, 138, 175. Siddhas, 28 note, 540, 559. Zíghraga, 82, 220. Zilá, 178. Zilávahá, 178. Sindhu, 13, 21, 55, 102, 372, 376, 443. Sinhiká, 10, 396. Zi[ir(a), 372, 555. Sítá, 4 ff., 55, 78, 79, 83, 84, 88, 93,passim. Ziva, 4, 36, 42, 54, 55, 57, 67, 78, 82, 85, 86, 109, 110, 205, 523, 524, 543, 554. Skanda, 554. Soma, 52, 58, 198, 267, 378, 554. Somadatta, 60. Somadá, 47. Somagiri, 376, 378. ZoGa, 45, 48, 372. Zringavera, 4, 192, 196, 223, 501, 502. Srinjay, 60. Srutakírti, 84. StháGu, 25, 37, 245. StháGumatí, 179. Sthúláksha, 256 note, 260. Sthúla[iras, 313. Subáhu, 364 note. Suchakshu, 55. Suchandra, 60. Zuchi, 238. Sudámá, 178. Sudáman, 81, 176. Sudar[an, 82, 83, 220, 373, 378, 448. Sudar[andwíp, 374. Sudhanvá, 82.
- **Translation**: 

---

### Verse 7 (Ramayana 0.1932)
- **Original**: 1914 The Ramayana Sudhriti, 82. Zúdras, 6, 13, 246. Sugríva, 5, 6, 9, 28, 29, 314, 316, 318, 324 ff., 337, 339, 344, 346 ff., 371, 375 ff., 412, 414, 422, 424, 430, 439 ff., 446, 450, 519, 545. Zuka, 442, 446, 447, 455 ff. Suke[a, 515, 516. Suketu, 39, 82. Sukí, 246. Zukra, 124, 210, 279, 384, 429. Sumáli, 515, 516. Sumágadhí, 46. Sumantra, 15, 16, 19, 21, 80, 92,passim. Sumati, 49, 50, 59, 60. Sumitrá, 27, 30, 32, 88, 94,passim. Sun, 93, 109, 110, 124, 243. Sunábha, 425. Zunah[epha, 72, 73, 74 Sunda, 35, 39. Sunetra, 364 note. SuparGa, 53, 125, 231, 343, 349, 388. Supár[va, 388. Supátala, 364 note. Suptaghna, 433 note. Surá, 58. Surabhí, 183, 246. Surapati, 522. Suras, 58. Surasá, 246, 395. Suráshmra, 21, 102, 376. Súrasenas, 550. ZúrpaGakhá, 5, 9, 249 ff., 267 ff., 288, 502. Súrya, 555. Súryáksha, 364 note.
- **Translation**: 

---

### Verse 8 (Ramayana 0.1933)
- **Original**: INDEX OF PRINCIPAL NAMES 1915 Súrya[atru, 433 note. Súryaván, 375. Susandhi, 81, 219. SusheG, 28, 351, 364 note, 376, 379, 380. Sutanu, 199. SutíkshGa, 9, 234, 236, 237, 240, 241. [575] Suváhu, 35, 44, 45, 146. Suvarat, 220. Suvela, 450, 456, 457. Suvíra, 21, 102. Suyajùa, 20, 132. Svayambhu, 394. Svayamprabhá, 382. ZvetáraGya, 264. Swarga, 54, 101, 202, 493. SwarGaromá, 82. Zweta, 448. Zyáma, 160. Syandiká, 151. Zyenagámí, 256 note, 260. Zyení, 246. Tá aká, 38, 39, 40, 41. Tá akeya, 266. Taittiríya, 132. Takshak, 432. Takshaka, 267. Tálajanghas, 81, 219. Tamasá, 7, 147, 148, 149. Támrá, 245, 246. TámraparGí, 375. Tapan, 459, 555. Tára, 364 note, 379 ff. Tárá, 9, 336, 349 ff., 355, 359, 362, 363, 366, 367, 369, 371, 385, 403, 449, 546.
- **Translation**: 

---

### Verse 9 (Ramayana 0.1934)
- **Original**: 1916 The Ramayana Tárak, 430. Tárkshya, 214. Ten-necked, 250. Thirty-three Gods, 51. Thousand-eyed, 41, 59, 60, 74, 75, 76, 86, 90, 112, 252, 297, 504. Three-eyed God, 86. Thunderer, 234. Titan, 58, 67, 72, 79, 109, 114, 124. ToraG, 179. Town-Destroyer, 59, 60. Trident, 68. Trident-wielding, 54, 57. Trijam, 133. Trijamá, 410, 463. Trikúma, 456, 457, 500, 515. TriGavindu, 515. Trípathagá, 56. Tripur, 306. Tripura, 85, 86. Tri[anku, 68-72, 81, 144, 219, 429. Tri[irá, 9. Tri[irás, 256 note, 260, 261, 264, 267, 271, 478, 479, 480, 502. Tumburu, 198, 199, 232. Uchchaih[ravas, 58, 522. Udayagiri, 379 note. Udávasu, 82. Ujjiháná, 179. Ukthya, 24. Umá, 49, 54, 205, 249 note, 471, 542, 543. Upasad, 22. Upasunda, 35. Upendra, 74, 559.
- **Translation**: 

---

### Verse 10 (Ramayana 0.1935)
- **Original**: INDEX OF PRINCIPAL NAMES 1917 Urmilá, 47, 83, 84, 88, 228. Urva[í, 286, 544, 545. U [anas, 382. Utkal, 374. Uttániká, 179, 539. Váhli, 13. Váhlíka, 376. Vahni, 555. Vaidyut, 375. Vaijayanta, 99, 179, 522. Vaikhánasas, 270, 271, 374. Vainateya, 388. Vai[ravaG, 265, 285, 378, 414, 515. Vai[yas, 246. VaitaraGí, 293. Vajra, 376. Vajradanshmra, 432, 433 note, 466, 467. Válmíki, 1, 7-11, 161, 519, 542. Vámadeva, 14, 79, 80, 91, 174, 222, 505. Vámana, 14, 523. Vá Ga, 81, 219. Vanáyu, 13. Vangas, 102. [576] Varadas, 550. VaruG, 1 note, 28, 42, 67, 88, 109, 124, 228, 243, 272, 293, 338, 377, 383, 448, 471, 518. Vará[ya, 256 note. Varútha, 179. Vásav, 92. Vásava, 236, 522. Va [ishmha, 14, 15, 19-22, 25, 32,passim. Vásudeva, 51, 52. Vásuki, 57, 267, 375, 432, 518, 522. Vasus, 14, 46, 246, 283, 377, 403, 522, 554.
- **Translation**: 

---

### Verse 11 (Ramayana 0.1936)
- **Original**: 1918 The Ramayana Vasvaukasárá, 203. Vátápi, 241, 280. Váyu, 59, 243, 369, 427, 428, 555. Vedas, 1 note, 3, 12, 22, 70, 89, 109, 125, 147, 184, 229, 559. Veda[rutí, 151. Vedavatí, 470, 517. Vegadar[í, 429, 446, 483. Ve Gá, 448, 537. VibháG ak, 15, 16, 17, 18, 25. VibhíshaG, 6, 10, 250, 273, 415, 422, 423, 433 ff., 449 ff., 472, 483, 487 ff., 516. Vibudh, 82. Vidarbha, 46, 49. Vidarbhas, 549. Videha, 79 ff., 129, 130, 142, 166, 195, 227. Videhan, 9, 79, 95, 104, 119, 125,passim. Videhas, 548. Vidyádharí, 203 note. Vidyujjihva, 450. Vidyunmáli, 364 note. Vidyutke[a, 515. Vihangama, 256 note. Vijay, 14, 36, 175, 505. Vikamá, 409. Vikrit, 245. Vikukshi, 81, 219. Vinata, 179, 379, 380, 388, 448. Vinatá, 53, 125, 246. Vindhya, 14, 51, 242, 364, 370, 374, 380. Vindu, 55. Vipá[á, 176, 539. Vírabáhu, 364 note. Virádha, 5, 9, 229, 232, 404, 446, 502. Viráj, 124.
- **Translation**: 

---

### Verse 12 (Ramayana 0.1937)
- **Original**: INDEX OF PRINCIPAL NAMES 1919 Viramatsya, 178. Virochan, 40, 43. Virtue, 223, 272. Virúpáksha, 52, 420, 433, 459, 460, 487. Vi[ákhás, 144, 430. Vi[álá, 56, 57, 59, 60, 62. VishGu, 1 note, 2, 3, 25, 32, 40,passim. Vi[ravas, 35, 309, 408, 515, 516. Vi[váchi, 198. Vi[vajit, 24. Vi[vakarmá, 28, 42, 198, 376, 387, 444, 445, 448, 499, 500, 515, 556. Vi[vámitra, 9, 32 ff., 39, 41, 44, 45,passim. Vi[varúpa, 353. Vi[vas, 377. Vi[vávasu, 198. Vi[vedevas, 162. Vitardan, 474. Vivasvat, 81, 171, 219, 245, 386, 532. VraGa, 444. Vrihadratha, 82. Vrihaspati, 28, 31, 95, 124, 210, 307, 464, 517. Vritra, 125, 264, 288, 387, 487, 491, 536. Vulture-king, 9. War-god, 124, 476. Wind, 30, 218. Wind-god, 10, 36, 42, 68, 325, 326, 379, 392 ff., 417 ff., 449, 470, 478, 481, 488, 502, 503. Yavadwípa, 372. Yajnakopa, 433 note, 459. Yajush, 326. Yajna[atru, 256 note. Yaksha, 236 note, 306, 318, 363, 375, 394, 420, 422, 425, 431, 454, 458, 468.
- **Translation**: 

---

### Verse 13 (Ramayana 0.1938)
- **Original**: 1920 The Ramayana Yáma, 68, 71, 112, 117, 124, 140, 166, 171, 241, 248, 262, 275, 287, 313, 343 ff., 432, 437, 449, 472, 475, 496, 518, 554. Yamuná, 158, 159, 160, 178, 214, 223, 372. Yámun, 372. Yavanas, 66, 550. Yayáti, 82, 95, 107, 119, 163, 186, 307, 344. Yudhájit, 84, 88, 180, 190. Yúpáksha, 420, 472. Yuvaná[va, 81, 219.
- **Translation**: 

---

### Verse 14 (Ramayana 0.1939)
- **Original**: Footnotes
- **Translation**: 

---

### Verse 15 (Ramayana 0.1940)
- **Original**: ***END OF THE PROJECT GUTENBERG EBOOK THE RAMAYANA***
- **Translation**: 

---

### Verse 16 (Ramayana 0.1941)
- **Original**: Credits March 18, 2008 Project Gutenberg TEI edition 1 Produced by Juliet Sutherland, John Bruno Hare, David King, and the Online Distributed Proofreading Team at <http://www.pgdp.net/>. Page-images available at <http://www.pgdp.net/projects/projectID3e283e798085a/>
- **Translation**: 

---

### Verse 17 (Ramayana 0.1942)
- **Original**: A Word from Project Gutenberg This file should be named 24869-pdf.pdf or 24869-pdf.zip. This and all associated files of various formats will be found in: http://www.gutenberg.org/dirs/2/4/8/6/24869/ Updated editions will replace the previous one— the old editions will be renamed. Creating the works from public domain print editions means that no one owns a United States copyright in these works, so the Foundation (and you!) can copy and distribute it in the United States without permission and without paying copyright royalties. Special rules, set forth in the General Terms of Use part of this license, apply to copying and distributing Project Gutenberg™ electronic works to protect the Project Gutenberg™ concept and trademark. Project Gutenberg is a registered trademark, and may not be used if you charge for the eBooks, unless you receive specific permission. If you do not charge anything for copies of this eBook, complying with the rules is very easy. You may use this eBook for nearly any purpose such as creation of deriva- tive works, reports, performances and research. They may be modified and printed and given away— you may do practically anythingwith public domain eBooks. Redistribution is subject to the trademark license, especially commercial redistribution.
- **Translation**: 

---

### Verse 18 (Ramayana 0.1943)
- **Original**: The Full Project Gutenberg License Please read this before you distribute or use this work. To protect the Project Gutenberg™ mission of promoting the free distribution of electronic works, by using or distributing this work (or any other work associated in any way with the phrase “Project Gutenberg”), you agree to comply with all the terms of the Full Project Gutenberg™ License (available with this file or online at http://www.gutenberg.org/license). Section 1. General Terms of Use & Redistributing Project Gutenberg™ electronic works 1.A. By reading or using any part of this Project Gutenberg™ elec- tronic work, you indicate that you have read, understand, agree to and accept all the terms of this license and intellectual property (trademark/copyright) agreement. If you do not agree to abide by all the terms of this agreement, you must cease using and return or destroy all copies of Project Gutenberg™ electronic works in your possession. If you paid a fee for obtaining a copy of or access to a Project Gutenberg™ electronic work and you do not agree to be bound by the terms of this agreement, you may obtain a refund from the person or entity to whom you paid the fee as set forth in paragraph 1.E.8.
- **Translation**: 

---

### Verse 19 (Ramayana 0.1944)
- **Original**: The Full Project Gutenberg License 1929 1.B. “Project Gutenberg” is a registered trademark. It may only be used on or associated in any way with an electronic work by people who agree to be bound by the terms of this agreement. There are a few things that you can do with most Project Guten- berg™ electronic works even without complying with the full terms of this agreement. See paragraph 1.C below. There are a lot of things you can do with Project Gutenberg™ electronic works if you follow the terms of this agreement and help preserve free future access to Project Gutenberg™ electronic works. See paragraph 1.E below. 1.C. The Project Gutenberg Literary Archive Foundation (“the Foun- dation” or PGLAF), owns a compilation copyright in the col- lection of Project Gutenberg™ electronic works. Nearly all the individual works in the collection are in the public domain in the United States. If an individual work is in the public domain in the United States and you are located in the United States, we do not claim a right to prevent you from copying, distributing, performing, displaying or creating derivative works based on the work as long as all references to Project Gutenberg are removed. Of course, we hope that you will support the Project Gutenberg™ mission of promoting free access to electronic works by freely sharing Project Gutenberg™ works in compliance with the terms of this agreement for keeping the Project Gutenberg™ name associated with the work. You can easily comply with the terms of this agreement by keeping this work in the same format with its attached full Project Gutenberg™ License when you share it without charge with others.
- **Translation**: 

---

### Verse 20 (Ramayana 0.1945)
- **Original**: 1930 The Ramayana 1.D. The copyright laws of the place where you are located also govern what you can do with this work. Copyright laws in most countries are in a constant state of change. If you are outside the United States, check the laws of your country in addition to the terms of this agreement before downloading, copying, displaying, performing, distributing or creating derivative works based on this work or any other Project Gutenberg™ work. The Foundation makes no representations concerning the copyright status of any work in any country outside the United States. 1.E. Unless you have removed all references to Project Gutenberg: 1.E.1. The following sentence, with active links to, or other immediate access to, the full Project Gutenberg™ License must appear prominently whenever any copy of a Project Gutenberg™ work (any work on which the phrase“Project Gutenberg” appears, or with which the phrase“Project Gutenberg” is associated) is accessed, displayed, performed, viewed, copied or distributed: This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever. You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at http://www.gutenberg.org 1.E.2.
- **Translation**: 

---

