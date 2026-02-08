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

### Verse 1 (Ramayan 0.1921)
- **Original**: INDEX OF PRINCIPAL NAMES 1903 Kau [ikí, 48, 372. Káverí, 375. Kaustubha, 58. Kávya, 40. Kekaya, 21, 84, 88, 90, 137, 139, 174, 175. Kerala, 190. Keralas, 549. Kesarí, 371. Ke [ini, 49, 50. Khara, 9, 225, 250 ff., 281, 288, 290, 294, 295, 433, 446, 451, 461, 477, 493. Kinnars, 270, 306, 308, 318, 321, 373, 425. Kimpurushas, 28 note. Kirátas, 66, 549. Kírtirát, 82. Kirtirátha, 82. Kishkindhá, 5, 333, 334, 336, 338, 339, 351, 357, 362, 369, 385, 449, 464, 500. Ko [al, 11, 102, 273, 307, 359, 418. Ko [ala, 151, 173. Krathan, 448. Kratu, 245. Krauncha, 310, 378, 476. Kraunchi, 246. Kri[á[va, 36, 41, 43. KrishGa, 497. KrishGagiri, 448. KrishGveni, 374. Krita, 57, 395. Krodhava[á, 245, 246. Kshatriyas, 246, 346. Kukshi, 81, 219. Kulingá, 176. Kumbha, 484.
- **Translation**: 

---

### Verse 2 (Ramayan 0.1922)
- **Original**: 1904 The Ramayana Kumbhakar Ga, 10, 250, 399, 411, 435 ff., 441, 470 ff. Kúmuda, 364 note, 448. Kunjar, 375, 392. Kuru(s), North, 198, 203, 315. Kurujángal, 176. Ku [a, 10, 46, 48, 63, 526. Ku [adhwaj, 80, 82, 88. Ku [ámba, 46. Ku [anábha, 46, 47, 48, 63. Ku [á[va, 60. Ku [ik, 33, 35, 36, 38, 44, 56, 62, 63, 68, 70 ff., 83. Ku míká, 179. Ku mikoshmiká, 179. Kuvera, 23, 88, 109, 110, 111, 112, 198, 199, 204, 232, 267, 378, 422, 431, 432, 483. Lakshma G, 4, 8, 11, 32, 36, 38, 40, 41, 44, 45, 56, 61, 79, 80, 82-84, 88, 91, 94, 97, 98,passim. Lakshmí, 88, 116, 146, 227, 400, 453, 462, 497. Lamba, 397. Lanká, 5, 10, 265, 267, 284, 286, 293, 295-297, 367, 387, 397, 411, 423 ff., 439, 456 ff. Lankamankamá, 515. Lava, 10, 526. Lohitya, 179. Lokapálas, 485. Lomapád, 15, 16, 18, 19, 21, 30.[571] Mádhaví, 520. Madhu, 26, 51, 57, 87, 95. Madhúka, 245. Madhushyand, 68, 74. Madrakas, 550. Magadh, 46, 102. Mágadnas, 548. Maghá, 83.
- **Translation**: 

---

### Verse 3 (Ramayan 0.1923)
- **Original**: INDEX OF PRINCIPAL NAMES 1905 Mahábír, 82. Mahábala, 433 note. Mahábhárat, 520, 524, 551, 554. Mahádeva, 61, 515. Mahákapála, 256 note, 260. Mahámáli, 256 note. Mahándhrak, 82. Mahápadma, 14, 52. Mahápárá[va, 433, 436, 455, 478, 480, 487. Mahárath, 68. Maháromá, 82. MaháruG, 368. Mahá [aila, 368. Mahendra, 28, 59, 86, 87, 88, 140, 167, 213, 243, 244, 307, 336, 344, 364, 368, 370, 375, 490, 531, 554. Mahe [war, 369, 498. Mahí, 372. Máhishmatí, 518. Mahishikas, 549. Mahodar, 433 note, 450, 455, 474, 478 ff. Mahodaya, 46, 70, 71, 488. Maináka, 10, 394, 500 note. Mainda, 28, 364 note, 371, 428, 430, 439, 449, 451, 458, 482, 483. Makaráksha, 485 note. Malaja, 39. Málavas, 548. Malaya, 198, 324, 328, 375, 379, 430. Málí, 515, 516. Máliní, 175, 539. Malyaván, 454, 455. Mályavat, 515, 516. Mánas, 38. MandakarGi, 240.
- **Translation**: 

---

### Verse 4 (Ramayan 0.1924)
- **Original**: 1906 The Ramayana Mandákiní, 200, 201, 203, 209, 234, 235, 304, 322, 416 note. Mandalí, 556. Mandar, 57, 163, 285, 362, 368, 372, 399, 402, 421, 485, 491, 493, 525. Mandarí, 444. Mándhátá, 81, 219, 347, 518. Mándavi, 84. Má G avya, 226 note. Mandehas, 373. Mandodarí, 402, 492, 500, 516. Mandra, 14. Ma Gibhadra, 441. Manthará, 40, 96, 97, 99, 187. Manu, 11, 12, 13, 81, 103, 151, 179, 219, 245, 246, 347, 490, 505, 537, 555. Marícha, 58. Márícha, 5, 9, 35, 39, 40, 44, 266, 271-280, 298. Maríchi, 81, 91, 219, 245. Maríchipas, 270, 271. MárkaG eya, 80, 174. Mars, 93, 144, 339, 404, 445, 467, 489. Maru, 82, 220. Maruts, 25, 54, 59, 403, 517, 547, 555. Máshas, 270, 271. Mátali, 109, 142, 489, 491, 493. Matanga, 14, 246, 315, 316, 317, 318, 319, 336, 337, 380. Mátangí, 246. Mátari[va, 389. Matsya, 102, 523, 537, 549. Maya, 293, 382, 432, 488. Máyá, 293, 521. Máyáví, 333, 334, 379. Meghamáli, 256 note. Meghanáda, 10.
- **Translation**: 

---

### Verse 5 (Ramayan 0.1925)
- **Original**: INDEX OF PRINCIPAL NAMES 1907 Mekhal, 374. Mená, 49, 394 note. Menaká, 74. Mercury, 144, 339, 467. Meru, 4, 49, 92, 109, 110, 142, 182, 232, 236, 254, 291, 315, 368, 370, 377, 380, 418, 493. Meru [avarGi, 382. Mina, 32. Mi [rake[í, 199. Mithi, 82. Míthilá, 9 note, 21, 45, 60, 61, 78, 81, 83, 84, 85. Mitraghna, 459. [572] Mlechchhas, 66, 537, 550. Modesty, 26. Moon, 30, 42, 58, 109 ff., 124, 218, 227, 243, 276, 367, 413, 414, 488. Mriga, 14. Mrigamandá, 246. Mrigí, 246. Mudgalya, 174. Nábhág, 82, 220. Nágadantá, 198. Nágas, 12, 55, 66, 68, 145, 270, 273, 395, 409, 413, 420, 427, 518. Nahush, 82, 95, 171, 190, 220, 307. Nairrit, 430. Nala, 10, 340, 364 note, 428, 444, 445, 448, 449, 468, 475, 483. Nalá, 246. Naliní, 55, 203, 204, 267, 436. Namuchi, 39, 261, 264, 275, 336. Nandá, 415. Nandan, 26, 175, 200, 267, 279, 315, 316, 426. Nandi, 249, 421.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1926)
- **Original**: 1908 The Ramayana Nandigráma, 4, 6, 9, 224, 502, 503. Nandí[vara, 471. Nandivardhan, 82. Nárad, 1, 2, 8, 9, 124, 199, 543. Narak, 479. Narántak, 479. NáráyaG, 25, 26, 95, 393, 474, 497, 516, 517, 522, 535, 559. Narmadá, 374, 448, 518. Nikumbha, 432, 433 note, 437, 459, 484. Níla, 28, 340, 352, 360, 364 note, 371, 374, 428, 429, 430, 446, 448, 449, 456, 458, 459, 469, 472, 475, 482. Nimi, 77, 82. Ni[akar, 389, 390. Nishádas, 4, 152, 192, 196, 271, 501, 537. Ocean, 10, 95, 144, 285, 286, 336, 346, 387. OshmhakarGakas, 548. Pahlavas, 66. Páka, 252, 297, 498. Pampá, 5, 9, 235, 293, 314-321, 327. Panas, 371, 428, 448, 464. Panasa, 455 note. Panchajan, 376. Panchála, 176, 539. Panchápsaras, 240. Panchavama, 9. Panchavamí, 244, 245, 247. PáG yas, 375, 549. Pará[ara, 517. Para[uráma, 119 note, 523, 531. Paravíráksha, 256 note. Páriyátra, 376, 448. Parjanya, 112, 174, 261, 448. Párvati, 249 note, 515, 542. Paulastya, 472.
- **Translation**: 

---

### Verse 7 (Ramayan 0.1927)
- **Original**: INDEX OF PRINCIPAL NAMES 1909 Paulomí, 29, 370. Pávaní, 55. Phálguní, 83. Pináka, 67. Pitris, 550. Prabháva, 363. Prachetas, 1, 245. Praghas, 420, 459, 460. Prágvam, 179. Prahasta, 399, 418, 419, 421, 422, 432 ff., 441, 451, 452, 455, 456, 471, 481. Praheti, 515. Prahláda, 391. Prajangha, 459, 460. Prajápati, 133 note, 554, 560. Pralamba, 175. Pramátha, 256 note. Pramathí, 260, 448. Pramati, 455 note. Prasenajit, 81, 219. Pra[ravaG, 304, 357, 380, 383, 415, 426. Prasthalas, 550. Pra[u[[ruka, 82, 220. Pratindhak, 82. Pravargya, 22. Prayág, 158, 159, 196. [573] Prithu, 81, 219. Prithu[yáma, 256 note. Proshmhapadá, 32. Pulah, 245. Pulastya, 35, 245, 254, 268, 288, 408, 515. Pulindas, 550. Puloma, 370. Punarvasu, 93.
- **Translation**: 

---

### Verse 8 (Ramayan 0.1928)
- **Original**: 1910 The Ramayana PuG aríká, 199. PuG ras, 548, 549. Punjikasthalá, 436, 552. Puranda, 522. Purandara, 384, 522. Purúravas, 286, 544, 545. Purusha, 256 note, 559. Purushádak, 82, 220. Purushottam, 498, 517. Púshá, 124. Pushpak, 10, 80, 286, 499, 519. Pushya, 32, 90, 92, 94, 96, 98, 109, 126. Rabhasa, 433 note. Rághava, 5 note. Raghu, 5, 9, 22, 32 ff., 50, 56, 61,passim. Raghunandana, 522. Ráhu, 93, 223, 261, 272, 303, 351, 480. Rain, Lord of, 92, 222. Rájagriha, 174, 175. Ráma, passim. Rámáyana, 8 note, 10, 11, 541, 542. Rambhá, 75, 232, 448. Rama Gá, 199. Ra[miketu, 433 note, 459. RávaG, 5, 9, 10, 25, 26, 32, 35,passim. ReGuká, 63, 119. Richíka, 48, 73, 86. Right, 42, 68. Riksharajas, 386, 442. Rikshaván, 448. Rishabh, 373, 375, 429, 446, 476, 483. Rishmikas, 549. Rishyamúka, 9, 314, 315, 316, 318 ff., 332, 335, 339, 340, 353, 380, 500.
- **Translation**: 

---

### Verse 9 (Ramayan 0.1929)
- **Original**: INDEX OF PRINCIPAL NAMES 1911 Rishya[ring, 15-24, 29, 30. RohiGí, 4, 112, 223, 227, 246, 251, 282, 287, 367, 404, 413, 445. Rohitas, 376, 558. Rudhirá[ana, 256 note. Rudra, 49, 57, 67, 77, 78, 162, 249, 257, 264, 283, 296, 378, 413, 483. Rudras, 246, 558. Rukmi Gí, 517. Rumá, 346, 349, 350, 363, 366, 367, 371, 385, 403. Ruman, 371. Sachí, 29, 202, 234, 238, 276, 286, 297, 370, 408, 415, 494, 519, 522. Sádhyas, 490, 555, 558, 559. Sagar, 11, 50 ff., 82, 119, 137, 171, 441. Sahadeva, 60. Sahya, 429, 430. Zaivya, 104, 107, 171, 533. Zakas, 66, 550. Zakra, 75, 234, 307, 313, 336, 344, 448, 464. Zálmalí, 176, 539. Zályakartan, 178. Záman, 186, 326, 359. Zambar, 479. Zambara, 99, 100. Sampáti, 5, 9, 246, 364 note, 385, 387 ff., 412, 455 note, 459, 460, 464. Samprakshálas, 235. Sanatkumár, 15, 16. Sandhyá, 515. Sanháras, 36. Sanhráda, 474. Zani[char, 283. Zankan, 82.
- **Translation**: 

---

### Verse 10 (Ramayan 0.1930)
- **Original**: 1912 The Ramayana Zankar, 57, 335. Sánká[yá, 80, 81, 82, 83. Zankha, 555. Zankhan, 220, 432. Sanrochan, 448. Zan[ray, 245. Zántá, 16, 19, 29, 30, 31. Zarabh, 364 note, 439, 476. Zarabhanga, 9, 233, 234, 235, 236, 265, 502. ZaradaG á, 176, 539. Saramá, 452, 453. SáraG, 446, 447, 455. Sarandib, 375 note. Sáranga, 556. Sarasvatí, 178, 372, 516, 522. Zárdúla, 441, 449, 450. Zárdúlí, 246.[574] Sarjú, 11, 20, 22, 36, 37, 38, 50,passim. Sárvabhauma, 429. Sarvartírtha, 179. Za[ivindhus, 81, 219. Zatabali, 371, 377, 379, 380. Zatadrú, 178, 539. Zatahradá, 231. Zatánanda, 62, 63, 77, 79, 80, 81, 84. Zatrughna, 32, 83, 84, 88, 89, 97,passim. Zatrunjay, 504. Satyaván, 129. Satyavatí, 48. Sávitrí, 129, 227. Zavarí, 315, 316, 317. Saumanas, 373. SávarGí, 377. Seven Rishis, 23.
- **Translation**: 

---

### Verse 11 (Ramayan 0.1931)
- **Original**: INDEX OF PRINCIPAL NAMES 1913 Zesha, 245. Siddhárth, 14, 137, 138, 175. Siddhas, 28 note, 540, 559. Zíghraga, 82, 220. Zilá, 178. Zilávahá, 178. Sindhu, 13, 21, 55, 102, 372, 376, 443. Sinhiká, 10, 396. Zi[ir(a), 372, 555. Sítá, 4 ff., 55, 78, 79, 83, 84, 88, 93,passim. Ziva, 4, 36, 42, 54, 55, 57, 67, 78, 82, 85, 86, 109, 110, 205, 523, 524, 543, 554. Skanda, 554. Soma, 52, 58, 198, 267, 378, 554. Somadatta, 60. Somadá, 47. Somagiri, 376, 378. ZoGa, 45, 48, 372. Zringavera, 4, 192, 196, 223, 501, 502. Srinjay, 60. Srutakírti, 84. StháGu, 25, 37, 245. StháGumatí, 179. Sthúláksha, 256 note, 260. Sthúla[iras, 313. Subáhu, 364 note. Suchakshu, 55. Suchandra, 60. Zuchi, 238. Sudámá, 178. Sudáman, 81, 176. Sudar[an, 82, 83, 220, 373, 378, 448. Sudar[andwíp, 374. Sudhanvá, 82.
- **Translation**: 

---

### Verse 12 (Ramayan 0.1932)
- **Original**: 1914 The Ramayana Sudhriti, 82. Zúdras, 6, 13, 246. Sugríva, 5, 6, 9, 28, 29, 314, 316, 318, 324 ff., 337, 339, 344, 346 ff., 371, 375 ff., 412, 414, 422, 424, 430, 439 ff., 446, 450, 519, 545. Zuka, 442, 446, 447, 455 ff. Suke[a, 515, 516. Suketu, 39, 82. Sukí, 246. Zukra, 124, 210, 279, 384, 429. Sumáli, 515, 516. Sumágadhí, 46. Sumantra, 15, 16, 19, 21, 80, 92,passim. Sumati, 49, 50, 59, 60. Sumitrá, 27, 30, 32, 88, 94,passim. Sun, 93, 109, 110, 124, 243. Sunábha, 425. Zunah[epha, 72, 73, 74 Sunda, 35, 39. Sunetra, 364 note. SuparGa, 53, 125, 231, 343, 349, 388. Supár[va, 388. Supátala, 364 note. Suptaghna, 433 note. Surá, 58. Surabhí, 183, 246. Surapati, 522. Suras, 58. Surasá, 246, 395. Suráshmra, 21, 102, 376. Súrasenas, 550. ZúrpaGakhá, 5, 9, 249 ff., 267 ff., 288, 502. Súrya, 555. Súryáksha, 364 note.
- **Translation**: 

---

### Verse 13 (Ramayan 0.1933)
- **Original**: INDEX OF PRINCIPAL NAMES 1915 Súrya[atru, 433 note. Súryaván, 375. Susandhi, 81, 219. SusheG, 28, 351, 364 note, 376, 379, 380. Sutanu, 199. SutíkshGa, 9, 234, 236, 237, 240, 241. [575] Suváhu, 35, 44, 45, 146. Suvarat, 220. Suvela, 450, 456, 457. Suvíra, 21, 102. Suyajùa, 20, 132. Svayambhu, 394. Svayamprabhá, 382. ZvetáraGya, 264. Swarga, 54, 101, 202, 493. SwarGaromá, 82. Zweta, 448. Zyáma, 160. Syandiká, 151. Zyenagámí, 256 note, 260. Zyení, 246. Tá aká, 38, 39, 40, 41. Tá akeya, 266. Taittiríya, 132. Takshak, 432. Takshaka, 267. Tálajanghas, 81, 219. Tamasá, 7, 147, 148, 149. Támrá, 245, 246. TámraparGí, 375. Tapan, 459, 555. Tára, 364 note, 379 ff. Tárá, 9, 336, 349 ff., 355, 359, 362, 363, 366, 367, 369, 371, 385, 403, 449, 546.
- **Translation**: 

---

### Verse 14 (Ramayan 0.1934)
- **Original**: 1916 The Ramayana Tárak, 430. Tárkshya, 214. Ten-necked, 250. Thirty-three Gods, 51. Thousand-eyed, 41, 59, 60, 74, 75, 76, 86, 90, 112, 252, 297, 504. Three-eyed God, 86. Thunderer, 234. Titan, 58, 67, 72, 79, 109, 114, 124. ToraG, 179. Town-Destroyer, 59, 60. Trident, 68. Trident-wielding, 54, 57. Trijam, 133. Trijamá, 410, 463. Trikúma, 456, 457, 500, 515. TriGavindu, 515. Trípathagá, 56. Tripur, 306. Tripura, 85, 86. Tri[anku, 68-72, 81, 144, 219, 429. Tri[irá, 9. Tri[irás, 256 note, 260, 261, 264, 267, 271, 478, 479, 480, 502. Tumburu, 198, 199, 232. Uchchaih[ravas, 58, 522. Udayagiri, 379 note. Udávasu, 82. Ujjiháná, 179. Ukthya, 24. Umá, 49, 54, 205, 249 note, 471, 542, 543. Upasad, 22. Upasunda, 35. Upendra, 74, 559.
- **Translation**: 

---

### Verse 15 (Ramayan 0.1935)
- **Original**: INDEX OF PRINCIPAL NAMES 1917 Urmilá, 47, 83, 84, 88, 228. Urva[í, 286, 544, 545. U [anas, 382. Utkal, 374. Uttániká, 179, 539. Váhli, 13. Váhlíka, 376. Vahni, 555. Vaidyut, 375. Vaijayanta, 99, 179, 522. Vaikhánasas, 270, 271, 374. Vainateya, 388. Vai[ravaG, 265, 285, 378, 414, 515. Vai[yas, 246. VaitaraGí, 293. Vajra, 376. Vajradanshmra, 432, 433 note, 466, 467. Válmíki, 1, 7-11, 161, 519, 542. Vámadeva, 14, 79, 80, 91, 174, 222, 505. Vámana, 14, 523. Vá Ga, 81, 219. Vanáyu, 13. Vangas, 102. [576] Varadas, 550. VaruG, 1 note, 28, 42, 67, 88, 109, 124, 228, 243, 272, 293, 338, 377, 383, 448, 471, 518. Vará[ya, 256 note. Varútha, 179. Vásav, 92. Vásava, 236, 522. Va [ishmha, 14, 15, 19-22, 25, 32,passim. Vásudeva, 51, 52. Vásuki, 57, 267, 375, 432, 518, 522. Vasus, 14, 46, 246, 283, 377, 403, 522, 554.
- **Translation**: 

---

### Verse 16 (Ramayan 0.1936)
- **Original**: 1918 The Ramayana Vasvaukasárá, 203. Vátápi, 241, 280. Váyu, 59, 243, 369, 427, 428, 555. Vedas, 1 note, 3, 12, 22, 70, 89, 109, 125, 147, 184, 229, 559. Veda[rutí, 151. Vedavatí, 470, 517. Vegadar[í, 429, 446, 483. Ve Gá, 448, 537. VibháG ak, 15, 16, 17, 18, 25. VibhíshaG, 6, 10, 250, 273, 415, 422, 423, 433 ff., 449 ff., 472, 483, 487 ff., 516. Vibudh, 82. Vidarbha, 46, 49. Vidarbhas, 549. Videha, 79 ff., 129, 130, 142, 166, 195, 227. Videhan, 9, 79, 95, 104, 119, 125,passim. Videhas, 548. Vidyádharí, 203 note. Vidyujjihva, 450. Vidyunmáli, 364 note. Vidyutke[a, 515. Vihangama, 256 note. Vijay, 14, 36, 175, 505. Vikamá, 409. Vikrit, 245. Vikukshi, 81, 219. Vinata, 179, 379, 380, 388, 448. Vinatá, 53, 125, 246. Vindhya, 14, 51, 242, 364, 370, 374, 380. Vindu, 55. Vipá[á, 176, 539. Vírabáhu, 364 note. Virádha, 5, 9, 229, 232, 404, 446, 502. Viráj, 124.
- **Translation**: 

---

### Verse 17 (Ramayan 0.1937)
- **Original**: INDEX OF PRINCIPAL NAMES 1919 Viramatsya, 178. Virochan, 40, 43. Virtue, 223, 272. Virúpáksha, 52, 420, 433, 459, 460, 487. Vi[ákhás, 144, 430. Vi[álá, 56, 57, 59, 60, 62. VishGu, 1 note, 2, 3, 25, 32, 40,passim. Vi[ravas, 35, 309, 408, 515, 516. Vi[váchi, 198. Vi[vajit, 24. Vi[vakarmá, 28, 42, 198, 376, 387, 444, 445, 448, 499, 500, 515, 556. Vi[vámitra, 9, 32 ff., 39, 41, 44, 45,passim. Vi[varúpa, 353. Vi[vas, 377. Vi[vávasu, 198. Vi[vedevas, 162. Vitardan, 474. Vivasvat, 81, 171, 219, 245, 386, 532. VraGa, 444. Vrihadratha, 82. Vrihaspati, 28, 31, 95, 124, 210, 307, 464, 517. Vritra, 125, 264, 288, 387, 487, 491, 536. Vulture-king, 9. War-god, 124, 476. Wind, 30, 218. Wind-god, 10, 36, 42, 68, 325, 326, 379, 392 ff., 417 ff., 449, 470, 478, 481, 488, 502, 503. Yavadwípa, 372. Yajnakopa, 433 note, 459. Yajush, 326. Yajna[atru, 256 note. Yaksha, 236 note, 306, 318, 363, 375, 394, 420, 422, 425, 431, 454, 458, 468.
- **Translation**: 

---

### Verse 18 (Ramayan 0.1938)
- **Original**: 1920 The Ramayana Yáma, 68, 71, 112, 117, 124, 140, 166, 171, 241, 248, 262, 275, 287, 313, 343 ff., 432, 437, 449, 472, 475, 496, 518, 554. Yamuná, 158, 159, 160, 178, 214, 223, 372. Yámun, 372. Yavanas, 66, 550. Yayáti, 82, 95, 107, 119, 163, 186, 307, 344. Yudhájit, 84, 88, 180, 190. Yúpáksha, 420, 472. Yuvaná[va, 81, 219.
- **Translation**: 

---

### Verse 19 (Ramayan 0.1939)
- **Original**: Footnotes
- **Translation**: 

---

### Verse 20 (Ramayan 0.1940)
- **Original**: ***END OF THE PROJECT GUTENBERG EBOOK THE RAMAYANA***
- **Translation**: 

---

